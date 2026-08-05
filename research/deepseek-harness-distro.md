# deepseek-harness-distro 调研摘要

## 一句话定位
**DeepSeek Harness 的自定义发行版**：把上游 `deepseek-harness` 的核心抽象抽取成一个**自包含、0 依赖的扩展开发 SDK**（`@deepseek-harness/sdk`），并附带一套"SDK 构建器"（`vendor/sdk-builder/`）从上游构建产物重新生成该 SDK 的类型、运行时 bundle 与测试基建——消费方扩展无需安装任何上游包即可开发与跑闭环测试。仓库自述 `description: "自定义发行版"`（gh 元数据），README.md:3 定位为"基于上游 DeepSeek Harness 的发行版"。

## 技术栈与依赖
- **语言/运行时**：TypeScript（ESM，`target: esnext`、`moduleResolution: bundler`，strict + `noUncheckedIndexedAccess` + `exactOptionalPropertyTypes` + `noImplicitOverride`），Node.js（`@types/node ^26.1.2`）。gh primaryLanguage 标 JavaScript，实质是 TS。
- **包管理器**：`nub ^0.6.0`（非标准，非 npm/pnpm/yarn/bun），由 `mise.toml` 的 `[tools] nub="latest"` 固定；锁文件 `nub.lock`（46KB，已提交）；`.npmrc` 仅一行 `store-dir=./.nub-store`。
- **构建工具链**：`tsdown ^0.22.0`（rolldown-based bundler，做 dts tree-shaking 与 single-file bundle）、`tsx ^4.0.0`（脚本直跑 TS）、`typescript ^6.x`（vendor 内 devDep）、根 `typescript ^7.x`。
- **测试**：`vitest ^4.1.10`，配置见 `vitest.config.ts`（只跑 `tspkg/*/tests/**/*.spec.ts`，vendor/target 排除；`@deepseek-harness/sdk` 与 `/testing` 子路径经 alias 指向 `tspkg/sdk/src/` 源码）。
- **Lint/Format**：`oxlint ^1.77.0`（含 `oxlint-tsgolint`、`typeAware + typeCheck`）+ `oxfmt ^0.62.0`；`.oxlintrc.json` 把全部生成物目录（`src/types/`、`src/testing/`、`src/runtime/`、`src/session-persistence/testing/`）ignore 掉。
- **任务编排**：`just`（justfile，`mise.toml` 固定 `just="latest"`），分根 `justfile` 与 `vendor/sdk-builder/justfile` 两个层级（`mod sdk-builder`）。
- **运行期依赖（关键卖点）**：**SDK 0 依赖**。`tspkg/sdk/package.json` 的 `peerDependencies` 为空；`cordis`（Context/Service）、`schemastery`（z）、`cosmokit`、`@standard-schema/spec`、session 域（dsh-session / dsh-session-persistence / dsh-llm / dsh-scope / dsh-invariants）的运行时值全部由 `gen-sdk-types.ts` 内联成单文件 bundle（`src/runtime/`、`src/testing/`），类型 tree-shake 成自包含 `.d.mts`（`src/types/`），消费方 `import 'cordis'` 解析到 `src/types/ambient.d.mts` 的 `declare module` 块。
- **仓库元数据（gh repo view）**：创建 `2026-08-05T01:36:58Z`，最近推送 `2026-08-05T09:59:51Z`，默认分支 `main`，private，0 star / 0 fork，未归档，**无 LICENSE**（licenseInfo: null），无 CHANGELOG，无 `.github/`（无 CI）。
- **作者**：3 个提交全部来自 GitHub 用户 `morlay`（用户名保留；无邮箱/真实姓名泄露）。
- **包身份**：根 `package.json` `name: deepseek-harness-distro`、`version: 0.0.1`、`private: true`、`workspaces: ["tspkg/*", "tsdevpkg/*"]`；SDK 包 `name: @deepseek-harness/sdk`、`version: 0.0.1`、`sideEffects: false`；builder 包 `name: @dhd/deepseek-harness`（私有，仅承载上游 workspace）。

## 文件结构概览
```
deepseek-harness-distro/
├── README.md (3.7KB)              # 中文文档：定位/结构/快速开始/编写扩展/依赖说明
├── AGENTS.md (120B)               # 极简：仅指向 mise.toml + justfile
├── package.json                   # 根 workspace，devDeps：oxfmt/oxlint/typescript/vitest
├── tsconfig.json                  # paths: @deepseek-harness/sdk → ./tspkg/sdk/src/index.ts
├── vitest.config.ts               # 只跑 tspkg/*/tests；sdk 入口经 alias 指向源码
├── justfile                       # 根：dep/test/fmt/lint/clean + mod sdk-builder
├── mise.toml                      # tools: nub/just；env: OPENSSL_CONF=/dev/null
├── nub.lock (46KB)                # 包锁（已提交）
├── .npmrc / .oxlintrc.json / .oxfmtrc.json / .prettierignore / .gitignore
├── tspkg/
│   └── sdk/                       # @deepseek-harness/sdk（发行版交付物）
│       ├── package.json           # exports: . / ./testing / ./session / ./session-persistence / ./session-persistence/testing
│       ├── src/
│       │   ├── index.ts           # 主入口：definePlugin + z + 全量类型 + ctx 增强 + session 域运行时值
│       │   ├── session.ts         # 兼容入口（default = SessionStore，对齐上游 @deepseek-ai/dsh-session 形态）
│       │   ├── testing.ts         # @deepseek-harness/sdk/testing：AgentLoop + ScriptedAdapter + mountAgentLoopTestDependencies
│       │   ├── types/             # 生成物：context/tools/prompts/agents/llm/session/scope/session-persistence/invariants/ambient .d.mts + .mjs
│       │   ├── testing/           # 生成物：sdk-testing-entry.mjs/.d.mts（上游 bundle 单文件）
│       │   ├── runtime/           # 生成物：runtime-entry.mjs/.d.mts（cordis+schemastery+session 域 bundle）
│       │   └── session-persistence/   # 旁路域（非核心）
│       │       ├── index.ts       # re-export 自 runtime bundle + types 产物
│       │       ├── src/index.ts   # stub：re-export 旁路类型（承接契约的 ../src/index.ts 引用）
│       │       └── testing/       # 生成物：contract.ts / coordinator-contract.ts / index.ts（上游持久化契约，包名已改写）
│       └── tests/                 # 闭环测试（真实 AgentLoop + mock LLM 驱动）
│           ├── helper.ts          # createLoop/runTurn/toolCallResponse/textResponse
│           ├── plugin-loop.spec.ts
│           ├── plugin-tool.spec.ts
│           ├── plugin-prompt.spec.ts
│           ├── plugin-events.spec.ts
│           ├── plugin-scope.spec.ts
│           ├── plugin-service.spec.ts
│           └── schemastery.spec.ts
└── vendor/
    └── sdk-builder/               # @dhd/deepseek-harness（私有），SDK 构建器
        ├── justfile               # gen: sync→dep→build-libs→gen-sdk-types；分步 sync/dep/build-libs/gen-sdk-types
        ├── package.json           # workspaces=source/vendor/* + source/packages/*/*；patchedDependencies: node-pty
        ├── sdk.config.ts          # SDK 类型结构定义：每个入口从哪个上游包提取哪些符号
        ├── sdk-testing-entry.ts   # testing bundle 入口：聚合 testkit+AgentLoop+LlmService+Session+ScriptedAdapter
        ├── runtime-entry.ts       # runtime bundle 入口：cordis Context/Service + schemastery z + session 域 re-export
        ├── tsdown.runtime.config.ts / tsdown.testing.config.ts
        ├── scripts/
        │   ├── gen-sdk-types.ts   # 417 行生成主脚本（9 步管线）
        │   └── gen-ambient.ts     # ambient 全局声明生成（react 式 tree-shake）
        └── source/                # 上游源码（gitignored，sync 时 clone；不在仓库里）
```

## 核心功能与实现要点
1. **`definePlugin` 类型收敛扩展入口**（`tspkg/sdk/src/index.ts:36-58`）：一个恒等函数（返回值=输入，无运行时行为），核心价值在类型层——`inject: K` 把 `apply(ctx)` 的 `ctx` 收窄为 `PluginContext<K>`，只保留 `inject` 声明的 SDK 服务键（`tools/sessions/systemPrompt/agents/llm`），未声明的服务在类型上不可见，强制扩展显式声明依赖。SDK 服务键类型见 `index.ts:23` 的 `SdkServiceKey`。

2. **SDK 构建器一键管线**（`vendor/sdk-builder/justfile:5` `gen: sync dep build-libs gen-sdk-types`）：`sync` 用 `git clone --depth=1 $DEEPSEEK_HARNESS_REPO source` 同步上游（URL 走环境变量、未硬编码）；`dep` 跑 `nub install`；`build-libs` 在 source/ 内 `tsc -b && tsdown`；`gen-sdk-types` 跑生成脚本。上游源码目录 `source/` 在 `.gitignore` 内（`vendor/sdk-builder/source/`），每次同步全量删除重建（`justfile:11` `rm -rf source`）。

3. **类型 tree-shake 生成（生成主脚本 `gen-sdk-types.ts:1-300`）**：`sdk.config.ts` 声明 9 个入口（context/tools/prompts/agents/llm/session/scope/session-persistence/invariants）各自从哪个上游包提取哪些类型符号；脚本扫描上游 `source/vendor/*` + `source/packages/<group>/<pkg>` 建立包名→目录映射，为每个入口生成纯类型 re-export 文件，再用 tsdown dts 模式（`alwaysBundle: [@deepseek-ai//, @standard-schema//, schemastery]`，`external: ['cordis']`）把符号及其依赖闭包内联成自包含 `.d.mts`，输出到 `tspkg/sdk/src/types/`。

4. **运行时单文件 bundle（`runtime-entry.ts` + `tsdown.runtime.config.ts`）**：把上游 `vendor/cordis/lib`（Context/Service）、`vendor/schemastery/lib`（z）、`packages/core/session/lib`、`packages/session-persistence/session-persistence/lib`、`packages/llm/llm/lib`、`packages/core/scope/lib`、`packages/support/invariants/lib` 聚合为一个 `runtime-entry.mjs`（`codeSplitting: false`，`target: es2024`），cordis 单实例；同名值+类型符号（SessionStore/Session/SessionId/MessageId/CallId/SessionPersistence/PersistenceCoordinator/InvariantService 等）由手写的 `runtime-entry.d.mts` 成对声明（gen-sdk-types.ts:301-417 末段），保证 `import { Session } from '@deepseek-harness/sdk'` 同时拿到值与类型。

5. **插件循环测试基建（`sdk-testing-entry.ts` + `tspkg/sdk/src/testing.ts`）**：从上游聚合 `mountAgentLoopTestDependencies`（testkit）、`AgentLoop`、`LlmService`、`Session`、`SessionStore`，并自实现 `ScriptedAdapter`（继承上游 `LlmAdapter`，按队列依次返回流式响应、记录全部 `GenerateOptions` 请求），打包为单文件 `sdk-testing-entry.mjs`；`testing.ts` 在其上手写类型，与主入口类型互通。消费方写法：`new Context() → mountAgentLoopTestDependencies(ctx) → ctx.plugin(AgentLoop, {agents:[]}) → ctx.llm.registerAdapter(['mock'], new ScriptedAdapter([...])) → ctx.agents.create(...) → followup`（`tspkg/sdk/src/testing.ts:11-25` 注释）。

6. **ambient 全局声明（`scripts/gen-ambient.ts`）**：扫描 SDK 类型产物里 `import {...} from 'cordis'` 的符号，生成临时入口 → tsdown dts tree-shake 出 cordis 闭包（含 cosmokit/@standard-schema），用 TS compiler API 把同名 `interface Context`/`Events` 的声明合并成员（解决 rolldown 把增强分到共享 chunk 的问题），包装为 `declare module 'cordis' { ... }`。这是 0 依赖消费方 `import 'cordis'` 的解析宿主（react 式、tree-shaken）。

7. **session-persistence 域旁路（`tspkg/sdk/src/session-persistence/`）**：SQLite/JSONL 持久化后端基类被定位为"非核心能力"，不进主入口；走 `@deepseek-harness/sdk/session-persistence`（值从 runtime bundle re-export，纯类型从 types 产物 re-export）+ `/session-persistence/testing`。后者把上游 `dsh-session-persistence` 的 `contract.ts`/`coordinator-contract.ts` 复制过来并把所有 `@deepseek-ai/*`、`cordis` 包名 import **字符串替换为 SDK 相对路径**（gen-sdk-types.ts 第 9 步），让消费方无需安装上游包即可运行上游的持久化契约套件（含崩溃尾修复、fork-seed、四类收养/碰撞、reload/flush/disposal 静默等场景，coordinator-contract.ts 共 1120 行）。

8. **闭环测试覆盖（`tspkg/sdk/tests/*.spec.ts`）**：7 个 spec 验证 SDK 在真实 AgentLoop（mock LLM）下的端到端契约——工具插件被循环调用并回传结果（plugin-tool）、注册的 PromptSection 进入 system prompt（plugin-prompt）、`tools/result` 事件触发监听器（plugin-events）、per-agent setup 注册的工具只对该 agent 可见（plugin-scope）、Service 子类作为插件在 `agent/settled` 事件中被调用（plugin-service）、`z` 走 Standard Schema `~standard.validate`（schemastery）、完整循环（plugin-loop）。helper.ts 提供 `createLoop`/`runTurn` 复用基建。

## 与 DeepSeek Harness 主仓库的集成点
**强集成、单向消费上游，永不修改上游**：

- **上游同步 seam（git clone）**：`vendor/sdk-builder/justfile:10-12` `sync` 目标执行 `git clone --depth=1 {{ env("DEEPSEEK_HARNESS_REPO") }} source`。上游仓库 URL 由构建期环境变量 `DEEPSEEK_HARNESS_REPO` 提供，**仓库内不硬编码上游 URL**；`source/` 在 `.gitignore` 里，每次 gen 全量重建（`rm -rf source`），保证上游与本仓库改动隔离（README.md 结构注释、justfile:11）。

- **类型提取契约 seam（`sdk.config.ts`）**：声明 SDK 每个入口从哪个上游包提取哪些类型符号——`context` 从 `cordis`、`tools` 从 `@deepseek-ai/dsh-tools`、`prompts` 从 `@deepseek-ai/dsh-system-prompt`、`agents` 从 `@deepseek-ai/dsh-agent`、`llm` 从 `@deepseek-ai/dsh-llm`、`session` 从 `@deepseek-ai/dsh-session`、`scope` 从 `@deepseek-ai/dsh-scope`、`session-persistence` 从 `@deepseek-ai/dsh-session-persistence`、`invariants` 从 `@deepseek-ai/dsh-invariants`。这是与上游 API 表面的**机器可读契约清单**，上游增删符号需要在此同步。

- **运行时 bundle seam（`runtime-entry.ts`）**：硬编码引用上游构建产物路径——`./source/vendor/cordis/lib/index.js`、`./source/vendor/schemastery/lib/index.mjs`、`./source/packages/core/session/lib/index.js`、`./source/packages/session-persistence/session-persistence/lib/index.js`、`./source/packages/llm/llm/lib/index.js`、`./source/packages/core/scope/lib/index.js`、`./source/packages/support/invariants/lib/index.js`。上游内部包布局（`packages/<group>/<pkg>/lib`）一旦迁移/改名，bundle 立刻失败。

- **上游构建产物补齐（`ensureLibReactions`，gen-sdk-types.ts:81-118）**：脚本注释明确——上游 `tsc -b` 产出 `lib/types/*.js`，但包入口 main/exports 指向的 `lib/index.js`（tsdown 打包产物）"上游构建被 rolldown tsconfig bug / client lightningcss 卡住，从未产出"。因此 distro 按 `package.json` 的 exports 声明**生成缺失的 ESM 入口**（re-export `lib/types/*.js`）及其 `.d.ts`/`.d.mts` 配对，使 mock bundle 的包名解析（运行时 JS）可用；CJS 入口不生成（SDK 只走 ESM）。这是对上游构建不完整的绕过。

- **测试契约改写 seam（gen-sdk-types.ts 第 9 步）**：把上游 `dsh-session-persistence` 的契约测试源码里所有 `from '@deepseek-ai/dsh-session'`、`'@deepseek-ai/dsh-llm'`、`'@deepseek-ai/dsh-scope'`、`'cordis'`、`'@deepseek-ai/dsh-session-persistence'`、`'../src/index.ts'` 字符串替换为 SDK 内相对路径（`../../index.ts`、`../index.ts`），让契约套件在 0 依赖消费方跑起来。

- **消费方引入契约（README.md "依赖"段）**：消费方经 `file:` 依赖引入 SDK（`"@deepseek-harness/sdk": "file:../deepseek-harness-distro/tspkg/sdk"`）；契约测试中的 `@deepseek-ai/*`、`cordis` 包名由消费方 tsconfig paths + vitest alias 映射到 SDK。

- **不集成（明确剥离）**：`source/`（上游全树）在 `.gitignore`，本仓库不携带上游源码；SDK 也不发布 TS 源给上游——发行版与上游是单向消费关系。`AGENTS.md` 仅 120B，没有任何"修改上游"的协作规约（与同 org 的 `deepseek-harness-desktop` 的 AGENTS.md 明确"严禁修改 deepseek-harness 下文件"不同——本仓靠 source/ gitignore 物理隔离）。

**结论**：发行版与主仓库的耦合面是 (a) `git clone $DEEPSEEK_HARNESS_REPO` 单向同步、(b) `sdk.config.ts` 的符号契约清单、(c) `runtime-entry.ts` 的硬编码上游 `lib` 路径、(d) 上游构建产物（含 distro 补齐的缺失入口）。没有任何反向贡献或 patch 机制（仅 `node-pty@1.1.0` patch 在 vendor package.json 里，属上游自身 workspace 的 patchedDependencies，非本 distro 引入）。

## 亮点与风险
- **亮点**
  - **真正 0 依赖的 SDK**：类型 tree-shaken 自上游 dts，运行时单文件 bundle 内联 cordis/schemastery/cosmokit/@standard-schema 与 session 域全量值，消费方 `file:` 引入即可，无需 npm install 任何上游包（README.md "依赖"段、`tspkg/sdk/package.json` 空 peerDependencies）。
  - **`inject` 类型收敛**：`definePlugin` 用 `PluginContext<K>` 在类型层强制扩展声明依赖服务，未声明的 SDK 服务在 `ctx` 上不可见——把 cordis 的"服务可用性"运行时约束前移到编译期（`tspkg/sdk/src/index.ts:25-58`）。
  - **闭环测试基建随 SDK 分发**：把上游 testkit + AgentLoop + 自实现 ScriptedAdapter mock 打包，扩展开发者可直接 `@deepseek-harness/sdk/testing` 跑真实循环验证插件，7 个 spec 覆盖工具/提示词/事件/作用域/服务/schemastery 六条主路径（`tspkg/sdk/tests/`）。
  - **上游持久化契约套件再分发**：session-persistence 的 contract/coordinator-contract（1120 行，覆盖崩溃尾修复、fork-seed 边界、delegation depth、四类收养/碰撞、reload/flush 静默）随 SDK 出货，消费方自带 vitest 即可跑——等价于把上游私有测试表面提升为公共契约。
  - **干净的发行版/上游隔离**：`source/` 全量 git clone + gitignore，本仓库永不携带上游源码、不修改上游；gen 是幂等全量重建。

- **风险**
  - **极新仓库，无 LICENSE/CI/CHANGELOG**：2026-08-05 创建并当天 3 个提交（init / feat: added session / fix(sdk): replace upstream package imports），0 star/0 fork，私有，licenseInfo: null——处于早期实验阶段，不能直接外部消费（无许可证 = 默认保留全部权利）。
  - **与上游内部布局强绑定**：`runtime-entry.ts` 硬编码 7 条上游 `lib` 路径，`sdk.config.ts` 声明 9 个上游包名 + 上百个符号。上游一旦重组 `packages/<group>/<pkg>` 或重命名内部包，生成立刻断裂；`gen-sdk-types.ts:147-150` 会 fail-closed 抛 `sdk.config.ts: 上游包 X 未在 source 中找到`，是好的失败模式但仍需手工跟进。
  - **bundle 后处理依赖字符串匹配**：gen-sdk-types.ts:251-273 与 305-326 靠精确匹配 `'const { version } = createRequire(import.meta.url)("../package.json");'` 来去掉 LLM attribution 的版本读取（避免生成幽灵 package.json），匹配失败即 `process.exit(1)`。上游若改写 attribution 代码（换路径、换字段、换写法），生成管线会硬失败。
  - **上游构建不完整的绕过**：`ensureLibReactions`（gen-sdk-types.ts:81-118）注释明示上游 tsdown 打包产物"被 rolldown tsconfig bug / client lightningcss 卡住，从未产出"，distro 靠自动补 re-export 入口绕过。一旦上游修好构建、入口形态变化，本绕过可能与上游真实入口冲突。
  - **cordis 单实例锁死**：SDK 把 cordis 内联进 runtime bundle 并 ambient 声明，消费方自带的 cordis（若有）不会与 SDK 合并——API 漂移时 SDK 的 cordis 版本可能与消费方/上游不同步；`runtime-entry.d.mts` 是大段手写值声明（gen-sdk-types.ts:301-417），新增上游符号需手工同步声明。
  - **非标准工具链**：`nub ^0.6.0`（非主流包管理器）、`typescript ^7.x`（根）/`^6.x`（vendor）跨大版本混用、`OPENSSL_CONF=/dev/null` 全局 env 绕过、`mise.toml` 固定 just/nub——新人上手与 CI 复现成本高（且当前无 CI）。
  - **`definePlugin` 仅类型层**：纯恒等函数无运行时校验，`inject` 收敛只在 tsc 下生效；JS 用户或跳过类型检查的调用方拿不到任何约束。

## 维护状态
- **初始活跃，单人开发**：仓库 2026-08-05 创建（`createdAt 2026-08-05T01:36:58Z`），当天 3 个提交全部来自 `morlay`——`bc70b87 feat: init`（05:13）、`d25cb98 feat: added session`（09:47）、`e144876 fix(sdk): replace upstream package imports in persistence test contracts with SDK paths`（09:59，HEAD）。
- **最近推送** `pushedAt 2026-08-05T09:59:51Z`，HEAD `e144876`。
- **私有仓**：`isPrivate: true`，0 star / 0 fork，未归档，`description: "自定义发行版"`，`primaryLanguage: JavaScript`。
- **License/CI/CHANGELOG 全无**：licenseInfo: null，无 LICENSE 文件，无 `.github/`，无 CHANGELOG。`nub.lock` 与全部生成物（`tspkg/sdk/src/types/`、`src/testing/`、`src/runtime/`、`src/session-persistence/testing/`）随仓库提交。

## 备注
- **调研产物**：本地浅克隆 `/tmp/dsh-ext-research2/deepseek-harness-distro/`（由 Main 用已认证凭据 `git clone --depth 1` 落地；本 ScoutDistro 工具面无 bash/gh，匿名访问该私有仓智能 HTTP 端点返回 401——证明仓库存在但需鉴权）。摘要写入 `/tmp/dsh-ext-research2/deepseek-harness-distro.md`（UTF-8，中文）。
- **生态角色**：与同 org 的 `deepseek-harness-desktop`（桌面打包，靠 gitignore + AGENTS 规约隔离上游）、`dsh-companion`（Cetus 桌面发行版，靠 cordis 插件协议消费上游）不同，本仓是**面向扩展开发者的 SDK 发行版**——把上游内部抽象重打包成 0 依赖、可 `file:` 引入的开发包，是 dsh-external 生态里"扩展开发者入口"的角色。
- **上游身份**：发行版消费的上游是 `deepseek-harness` 主仓库（README.md:3 链接 `github.com/deepseek-harness`），URL 通过构建期环境变量 `DEEPSEEK_HARNESS_REPO` 注入，仓库内不硬编码。
- **脱敏**：摘要中未出现作者邮箱/真实姓名；GitHub 用户名 `morlay`、组织 `dsh-external` 为可公开标识符。git logs/HEAD 中的本地 clone 记录含本机主机名，已不在摘要中使用。
