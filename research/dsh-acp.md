# dsh-acp 调研摘要

## 一句话定位

`dsh-acp` 是一个独立、客户端中立的 Agent Client Protocol (ACP) 适配器：它发现用户本机已安装的 DeepSeek Harness (DSH) 源码运行时，将其会话/流式事件/取消/转向/权限语义翻译为 ACP，使任意支持 ACP 的客户端（编辑器、自动化宿主）能通过 stdio NDJSON 接入 DSH。

## 技术栈与依赖

- 语言/运行时：TypeScript（ESM），Node.js `^22.19.0 || >=24.0.0`；开发期用 `tsx` 直跑 TS，发布产物是 esbuild 打出的 portable JS bundle（不发布 TS 源）。
- 测试/构建：`vitest@4.1.10`、`esbuild@0.27.0`、`typescript@5.9.3`；脚本全用 `.mjs`（`scripts/build.mjs`、`build-binaries.mjs`、`package-release.mjs`、`verify-release.mjs`、`publish-npm.mjs`、`test-release-safety.mjs`、`test-publish-npm.mjs`）。
- 运行期依赖仅两条：`@agentclientprotocol/sdk@1.3.0`（ACP 协议 SDK）、`zod@4.1.12`（校验）。
- 包元数据：`name: dsh-acp`、`version: 0.1.1`、`license: MIT`、`bin: { "dsh-acp": "dist/index.js" }`、`engines.node: ^22.19.0 || >=24.0.0`。
- 实验性 Bun standalone 编译（Linux/macOS/Windows × x86_64/arm64 共 6 目标），但因 Bun 内嵌 LGPL 的 JavaScriptCore/WebKit 且当前 DSH 驱动不兼容 Bun，仅保留 manifest，不作为默认产物。
- CI：`.github/workflows/ci.yml`（typecheck + vitest + release-safety + build）、`release.yml`（双 npm 身份发布）。
- 仓库元数据（gh api）：创建/最近推送均为 `2026-08-05T02:47:28Z`，默认分支 `main`，主语言 TypeScript，0 star，未归档；`description: "Client-neutral ACP adapter for DeepSeek Harness"`。
- 注意：`package.json` 的 `repository.url`、README 中的安全通告链接、issue 链接全部指向 `github.com/OffloopHQ/dsh-acp`——`dsh-external/dsh-acp` 是该上游仓库在本组织的镜像/再发布位（与第一轮调研的 `dsh-external/*` 命名规律一致，外部发布身份仍是 OffloopHQ）。

## 文件结构概览

```
dsh-acp/
├── src/
│   ├── index.ts                 # 入口 shebang，调用 cli/services.ts 的 main()
│   ├── logger.ts                # 诊断日志（凭据脱敏、字节/深度有界）
│   ├── cli/                     # parse.ts(参数)、run.ts(分发)、services.ts(主循环)、types.ts、version.ts
│   ├── acp/                     # ACP 协议层（无 DSH 导入）
│   │   ├── agent.ts   (54KB)    # 协议核心：会话状态机、取消围栏、权限/转向/elicitation 路由
│   │   ├── app.ts     (12KB)    # 连接生命周期、teardown 重试与所有权
│   │   ├── mapping.ts (21KB)    # Runtime↔ACP 类型/事件/能力映射
│   │   └── types.ts             # DshAcpClient、steering 方法等
│   ├── runtime/                 # 客户端中立的运行时抽象
│   │   ├── types.ts   (11KB)    # DshRuntimeDriver 契约 + 全部 Runtime* 类型
│   │   ├── factory.ts           # 选 driver + 启动前再次校验
│   │   └── drivers/dsh-0.0.1/   # 唯一驱动
│   │       ├── driver.ts (60KB) # 会话 new/load/resume/fork/list/close、prompt 流、teardown
│   │       ├── host.ts   (53KB) # DSH in-process 加载、boot plan、 Cordis 组合、网络面校验
│   │       ├── events.ts        # DSH 事件→RuntimeEvent 映射、有界序列化
│   │       ├── tool-kinds.ts    # 工具分类
│   │       └── index.ts
│   ├── discovery/               # 发现并验证已安装 DSH（绝不下载/修改）
│   │   ├── index.ts   (11KB)    # inspectDsh/doctorDsh/assertDshUnchanged
│   │   ├── layout.ts  (7KB)     # 0.0.1 布局校验、Node/tsx 版本、包名/版本断言
│   │   ├── fingerprint.ts(13KB) # sha256 兼容性指纹（~120 个 DSH 关键文件清单）
│   │   └── types.ts
│   └── testing/                 # fake-runtime.ts、fake-client.ts（测试桩）
├── test/                        # vitest 套件：acp/、cli/、discovery/、runtime/（含 fake-host.ts）
├── docs/                        # architecture / compatibility / cli / distribution / npm-publishing / independent-implementation / bun-standalone-relinking / reviews/
├── scripts/                     # build/package/verify/publish/test-release-safety 全套 .mjs
├── package.json / package-lock.json / tsconfig.json / vitest.config.ts
├── AGENTS.md (6.9KB)            # 贡献者规则（客户端中立、安全边界、teardown 所有权等）
├── README.md / SECURITY.md / LICENSE(MIT) / THIRD_PARTY_NOTICES.md
└── .github/workflows/{ci,release}.yml
```

## 核心功能与实现要点

1. **只读发现 DSH 源码安装**：`src/discovery/index.ts` 的 `inspectDsh()` 按优先级枚举候选——`--dsh-path`/`DSH_PATH` 环境变量 → `$DSH_HOME/source/current` → `~/.dsh/source/current` → `~/.local/bin/dsh` → `PATH` 中各组件下的 `dsh`。每个候选经 `resolveCandidate()`（`src/discovery/index.ts:170` 起校验 basename 必须为 `dsh`、解析符号链接、比对 `<root>/bin/dsh` 物理路径、防 basename 碰撞与路径逃逸）后，交给 `validateDsh001Layout()`。永不安装/更新/修改 DSH。

2. **sha256 兼容性指纹围栏**：`src/discovery/fingerprint.ts` 的 `DSH_001_FINGERPRINT_FILES` 列出约 120 个 DSH 关键文件（loader/include vendor、core/agent、agent-loop、session、tools、user-approval、permission、sandbox-policy、sandbox、sandbox-local、subprocess-local、bash/*、fs/*、session-persistence、session-query、llm 等直接导入与具体 bash/fs/subprocess 实施层，外加 Linux 下 Landlock 启动器包与二进制），`computeRuntimeFingerprint()` 把这些文件内容连同 Node/tsx 版本一起哈希。三次校验：发现时、`createRuntimeDriver()` 前（`src/runtime/factory.ts` 调 `assertDshUnchanged`）、driver 真正 boot 前（`host.ts`）。`--expected-runtime-fingerprint` 是附加围栏而非绕过。`installation.validatedFiles` 是机器可读的兼容缝权威清单。

3. **分层架构与“仅驱动一层导入 DSH”**：ACP 层（`src/acp/*`）只依赖 `@agentclientprotocol/sdk` 与 `src/runtime/types.ts` 的 `DshRuntimeDriver` 契约，零 DSH 导入。`src/runtime/factory.ts` 按 `driverId` 选 `Dsh001RuntimeDriver`，它是唯一允许 import DSH 内部的层（`src/runtime/drivers/dsh-0.0.1/host.ts:580` 起把 DSH 自带的 tsx loader 装进当前 Node 进程，再 `import()` DSH 的 `app-boot`、`llm`、`session-query` 等）。`Dsh001RuntimeDriver` 通过 `DSH_001_CAPABILITIES`（`driver.ts:43`）声明能力，ACP 层拒绝任何未声明操作。

4. **ACP 能力面（当前实现）**：见 `docs/compatibility.md` 与 `driver.ts:43` 的 `DSH_001_CAPABILITIES`。支持 text + resource-link prompt、agent 消息/思考/工具生命周期/plan/session_info/usage 更新、会话 new/load(回放)/resume(不回放)/fork(完整轮次种子)/workspace 作用域 list(每页≤50、版本化游标)/close、精确 in-flight 取消、steering（DSH agent 空闲时）、单次 approve/reject/cancel 权限（仅当 DSH 主动 `approval/request`）、stdio 与 Streamable HTTP MCP（stderr 强制 `pipe` 且 4KiB/64 行/64KiB 有界脱敏排放）。**不**宣传：delete、image、embedded context、elicitation、SSE MCP、auth/provider 管理。

5. **adapter 拥有的私有 boot 组合**：`host.ts:735` 的 `createDsh001BootPlan()` 把 DSH `app-boot.boot()` 的 patches 拼成最终组合——先装 `dsh-acp` TUI overlay 与 personal overlay（仅选 provider/model/prompt 表面），随后追加 adapter 权威 patches：`sandbox-policy={mode:"workspace-write",workspaceRoot:cwd}`、`approval={policy:"ask"}`、`permission` presets 只允许 `read-only`/`workspace-write`+`ask`、`hmr=disabled`、`session-query-sqlite={path:":memory:"}`，并把 `repository-plugins/web/web-search-deepseek/tool-web/telemetry-otel` 五个网络面 patch 全部 `disabled:true`（`DSH_001_DISABLED_NETWORK_PATCH_IDS`，`host.ts:222`）。boot 后用 `assertDsh001NetworkSurfaceDisabled()`（`host.ts:790` 起）实际查询 settled 全局 `web` 服务与 `tools.schemas()` 目录，验证确实没有 `web_search`/`web_fetch` 等残留，而不是只信 patch 意图。每次 boot 都从 DSH base config 的私有副本起步，不动用户源码配置；`process.env.DSH_PERMISSION_MODE="workspace-write"`（`host.ts:581`）。

6. **会话策略即采纳权威**：在 load/resume/fork 之前、以及 new/resume/fork 实际返回 handle 之后，driver 反复校验持久化会话的 `permission/preset`、`sandbox/mode`、`approval/policy` 事件——只接受“缺失”或精确等于 `read-only`/`workspace-write`+`ask` 的事实；`danger-full-access`、`never`、未知值、合并扩展字段、初始 pin 顺序错误一律 fail-closed（详见 `docs/compatibility.md` 与 `host.ts` 的 `requireSessionHeader/Event`）。同时把所有不可信 DSH 历史做有界校验：≤20000 events、单事件 ≤1MiB、快照 ≤16MiB、title ≤4KiB、list ≤20000 行/≤16MiB、header schema 版本必须为 `0`、seq 必须连续（`host.ts:440` 起 `requireSessionEvent`）。

7. **取消/teardown 所有权不变量**：`agent.ts` 实现一 session 一活跃 prompt、每轮唯一 generation 单次 settle；取消/abort/close/connection-close 汇聚到同一条 cleanup 路径；同一轮的重复 cancel 复用同一个 runtime cleanup promise，ACP 仅在取消 + generator runner 排空到 idle（或有界隔离兜底退役该 session）后才返回 cancelled 响应；teardown 按 stage 保留所有权，pending descendant drain 期间对应的 DSH registry root 保持存活、超时后复用同一 drain（`driver.ts` 的 `continueDescendantDrain` 与 `boundedTeardown`，超时 `DSH_TEARDOWN_TIMEOUT_MS=15000`）。stdout 在 `serve` 模式只放 ACP JSON-RPC 帧。

8. **发布/分发**：`scripts/build.mjs` 产出 `dist/`；`scripts/package-release.mjs`+`verify-release.mjs` 产出 `release/` 与 `SHA256SUMS`；canonical 名 `dsh-acp` 与 scoped mirror `@offloophq/dsh-acp` 必须同版本同 payload 双发，靠 registry integrity 对账，不一致即 fail-closed；构建/验证全 offline，仅最小 publish job 拿 `id-token: write`。GitHub Release 资产公开可匿名下载并校验 checksum，供下游分销商自行打包。

## 与 DeepSeek Harness 主仓库的集成点

- **唯一耦合层 = in-process TypeScript import + Cordis 组合**，无子进程、无 HTTP：`src/runtime/drivers/dsh-0.0.1/host.ts:580` 在 boot 前用 `import(pathToFileURL(installation.tsxLoaderPath).href)` 把 DSH 自带的 tsx loader 装进当前 Node 进程，随后直接 `import()` DSH 的 `app-boot`、`llm`、`session-query` 等**内部**包——这些不是公开 API，而是 DSH 源码树内部模块。被导入的内部模块清单固定在 `src/discovery/fingerprint.ts:DSH_001_FINGERPRINT_FILES`（约 120 项，覆盖 vendor loader/include、core/agent、agent-loop、session、tools、user-approval、permission、sandbox-policy、sandbox、sandbox-local、subprocess-local、bash/*、fs/*、session-persistence、session-query、llm 等），这就是文档所称的“reviewed compatibility seam”。
- **被绑定的具体 DSH 版本/布局**：`@deepseek-ai/dsh-root@0.0.1` + `@deepseek-ai/dsh@0.0.1`，源码 root 必须是 `private:true` 的工作区包，CLI 包 `bin.dsh === "lib/bin.js"`，`tsx` 必须 `4.x`，Node `^22.19 || >=24`，Linux 还要校验架构相关的 `node-addon-landlock-run-linux-<arch>` 包与 `landlock-run` 二进制（`src/discovery/layout.ts`）。任何不符合即 `DSH_UNSUPPORTED_VERSION` / `DSH_LAYOUT_*` fail-closed。
- **boot patch 协议**：通过 DSH 的 `appBoot.boot(name, configPath, patches)` 注入 patches，覆盖 `sandbox-policy / approval / permission / agent-loop / hmr / session-query-sqlite / repository-plugins / web / web-search-deepseek / tool-web / telemetry-otel` 等 DSH 0.0.1 既有的 patch id——这些 id 名是 DSH 暴露给 overlay 系统的稳定字符串契约；`assertDsh001NetworkSurfaceDisabled()` 还会读 DSH settled 后的 `context.get("web")` 与 `tools.schemas()` 目录来反向校验。
- **不集成 / 主动禁用的 DSH 能力**：DSH 的凭证内置 web_search/web_fetch、仓库插件加载器（`repository-plugins`）、OTel 遥测、HMR 全部被关掉；delete/图片/embedded-context/elicitation/SSE-MCP/auth/provider 不宣传。`docs/compatibility.md` 与 `AGENTS.md` 明确：`workspace-write` 只是文件写边界，**不是**进程级出网隔离，DSH bash/execute 仍可走宿主网络且未必触发 ACP `approval/request`——这是与主仓库的安全契约边界。
- **上游发布身份**：`dsh-external/dsh-acp` 是镜像位；真正维护身份是 `OffloopHQ/dsh-acp`（README/SECURITY/package.json 全部指回 OffloopHQ）。本仓库与第一轮的 `dsh-external/*` 一致，作为本组织的公共再发布/巡检副本。

## 亮点与风险

- **亮点**
  - 极度严格的多层 fail-closed：发现→factory→driver→boot→settled 五道闸，每次都重算物理路径与指纹（`src/discovery/index.ts:assertDshUnchanged`、`src/runtime/factory.ts`、`host.ts`）。
  - 明确区分“意图”与“结果”：`assertDsh001NetworkSurfaceDisabled()`（`host.ts:790`）不只信 patch 配置，而是在 boot 后查询真实 settled 目录。
  - 安全模型诚实：`offloop.dsh-acp.security` 元数据（`src/acp/mapping.ts:mapAgentCapabilities`）显式声明 `builtInNetworkTools:false / processNetworkIsolation:false / permissionGate:"dsh-emitted-only" / protectedAdmissionFromInitialize:false`，要求客户端 fail-closed。
  - 会话策略即采纳权威——持久化/fork-seed/新建 handle 三处都重校 sandbox+approval，防止历史或合并扩展悄悄放宽权限。
  - 完备的发布管线与对账（`scripts/verify-release.mjs` 21.8KB、`publish-npm.mjs`、双 npm 身份 integrity 对账）。
  - 测试覆盖厚：`test/runtime/driver.test.ts` 65KB、`test/acp/lifecycle.test.ts` 35KB、`cancellation-permission.test.ts` 14KB，并配 `fake-host.ts`/`fake-runtime.ts` 桩。

- **风险**
  - **强耦合 DSH 0.0.1 内部模块**：直接 import ~120 个 DSH 内部文件路径与 Cordis `app-boot` patch id——DSH 任何内部重构（重命名、patch id 改名、新增必需 patch、settled 服务名变更）都会让指纹或 boot 校验失败。`AGENTS.md` 已要求“driver 开始导入新 DSH 缝时必须同步更新 validatedFiles 与聚焦测试”，但本质上是把 DSH 内部当稳定契约，脆弱。
  - **单一驱动、单一版本**：只支持 `dsh-source-0.0.1`；DSH 一旦升 minor/patch 而内部布局变动，本适配器需要发新版本。
  - **Node 进程内 hosting**：driver 必须与 DSH 共用同一 Node（`--node` 仅当物理路径等于 `process.execPath` 才接受，`docs/cli.md`），无法跨 Node 版本/跨 runtime（Bun 当前不兼容，`docs/distribution.md`）。
  - **0.0.1 是早期版本**：仓库 2026-08-05 才创建、0 star、版本 0.1.1，尚无第三方使用反馈；release trust boundary 仍依赖仓库管理员 actor id（`22412638`）作为事故兜底，Trusted Publisher Environment/tag ruleset 尚未冻结（见 `AGENTS.md` 末段）。
  - **bash 出网未隔离**：已明确声明不是进程级 egress 沙箱，受保护的客户端必须自行在外层做网络/provider 拦截并通过其 conformance——这把安全责任明确转嫁给宿主，但意味着误用（只看 `initialize` 成功就放行）会有风险。
  - **指纹≠供应链溯源**：`docs/compatibility.md` 与 `AGENTS.md` 反复强调指纹只覆盖 `validatedFiles`，不覆盖 Cordis 动态插件与传递依赖，不能当 SBOM/provenance 用。

## 维护状态

- 全新仓库：GitHub `repos/dsh-external/dsh-acp` 的 `created_at` 与 `pushed_at` 都是 `2026-08-05T02:47:28Z`（与本轮调研同日），0 star、未归档、默认分支 `main`、主语言 TypeScript。
- `package.json` version `0.1.1`，CI（typecheck/vitest/release-safety/build）与 release workflow 已就绪；docs/ 下含 `reviews/2026-08-02-initial-implementation.md`（9KB 初版评审记录），说明本项目在镜像到本组织前已在 OffloopHQ 有过一轮实现评审。
- 上游维护身份（issue/security advisory/repository url）统一指向 `github.com/OffloopHQ/dsh-acp`；本 `dsh-external/dsh-acp` 是本组织的镜像/再发布位。

## 备注

- 与主仓库（DSH）的关系是“外部适配器”：本仓不包含也不重分发 DSH 源码，DSH 是用户自行安装的前置依赖；适配器通过 in-process tsx loader 加载已安装的 DSH 内部模块，并通过 Cordis `app-boot` patch 协议覆盖 sandbox/approval/permission/网络面。
- 安全报告通道：`https://github.com/OffloopHQ/dsh-acp/security/advisories/new`（私有漏洞报告），禁止在公开 issue 中放凭据/prompt/客户数据。
- 与第一轮调研的同类 `dsh-external/*` 仓一致：本组织仓库为镜像/巡检副本，真正的发布身份（npm `dsh-acp` / `@offloophq/dsh-acp`、GitHub OffloopHQ）不在 `dsh-external` 名下。
- 调研产物：仓库已 `git clone --depth 1` 到 `/tmp/dsh-ext-research2/dsh-acp/`，本摘要写入 `/tmp/dsh-ext-research2/dsh-acp.md`（UTF-8，中文）。
