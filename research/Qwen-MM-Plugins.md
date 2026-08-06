# dsh-external/Qwen-MM-Plugins

## 一句话定位
DeepSeek Harness（DSH）侧的 Cordis 插件发布包 `@deepseek-ai/dsh-qwen-mm`：把上游 QwenLM/Qwen-MM-Plugins 的视觉语言能力以"运行时拉取的 Agent Skill + 严格 MCP 工具 server"方式挂载进 harness；本身不 vendor 也 不修改 上游 Python 实现，附带的 host 补丁为 DSH 主仓库补齐 Qwen-MM 结果链所需的通用图像基础设施。注意它不是 QwenLM 上游那个多模态插件仓库本身，而是 DSH 的适配层。

## 技术栈与依赖
- TypeScript（ESM，`type: "module"`），Cordis 插件框架 `cordis ^4.0.0-rc.7`，配置 schema 用 `schemastery ^3.18.0`。
- DSH workspace peer/dev 依赖：`@deepseek-ai/dsh-mcp-client`、`dsh-skill-local`、`dsh-skill`、`dsh-paths`、`dsh-invariants`、`dsh-system-prompt`、`dsh-tools`、`dsh-llm`；测试侧 `@modelcontextprotocol/sdk ^1.12.0`、`zod ^4.4.3`。
- 运行时外部工具：`git`（sparse-checkout 拉取 skill）、`uvx`（默认启动 MCP server）、上游 Python 包、Blender/FreeCAD 等宿主应用。
- 许可：包内 `BSD-3-Clause`（`packages/qwen/qwen-mm/package.json:31`），但 GitHub 仓库级 `license` 字段为 `null`，根 README 明确要求发布时按组织要求补充仓库级 LICENSE。
- 版本 `0.0.1`、`private: true`，处于早期发布形态。

## 文件结构概览
```text
README.md                                # 根发布说明（安装到 DSH 的步骤、补丁说明）
.gitattributes                           # *.patch 关闭 trailing-space 检查
.gitignore                               # lib/、node_modules、coverage
patches/qwen-mm-plugin.patch             # 113.9 KB / 2106 行 DSH host 通用补丁
packages/qwen/qwen-mm/
  package.json                           # @deepseek-ai/dsh-qwen-mm 包定义
  tsconfig.json                          # 继承 tsconfig.base.json，引用 skill/mcp/paths/invariants
  README.md / README.zh.md               # 双语等权威说明（i18n 哈希配对）
  README.i18n.yaml                       # 双语 README blob 哈希一致性记录
  src/index.ts                           # 插件主体：能力注册表 + 拉取 + 挂载
  src/invariant.ts                       # 包级 invariant companion（无运行时不变量）
  tests/qwen-mm.spec.ts                  # 单测：能力注册表 / Config / ensureSkillSource
  tests/loader-composition.spec.ts       # 真实 Loader 组装 E2E：fixture 上游 + stdio MCP
```

## 核心功能与实现要点
1. **静态能力注册表**（`src/index.ts:55-62` `CAPABILITIES`）：把上游六个目录映射为 `id` + 可选 MCP `serverName` + 可选 `extraEnv`：`core` / `video-memory` / `video-edit` / `blender`（带 `QWEN_MM_AUTOLAUNCH=1`）/ `freecad`（同上）/ `edu-agent`（纯 skill，无 MCP server）。MCP server 名严格形如 `qwen-mm-plugins-<id>`。

2. **git sparse-checkout 拉取 + ref marker 缓存**（`src/index.ts:97-145` `ensureSkillSource`）：对每个能力在 `$DSH_HOME/cache/qwen-mm/<id>` 下做 `git init` + `sparse-checkout set src/capabilities/<id>/skill` + `fetch --depth 1 origin <ref>` + `checkout FETCH_HEAD`，并在根目录写 `.dsh-qwen-ref` marker。ref 未变直接复用；`update: 'never'` 时 ref 不匹配直接抛错（绝不悄悄拉新）。

3. **工具就绪先于 skill 挂载**（`src/index.ts:177-205` `mountCapability`）：先 `ctx.plugin(McpClient, …)` 启动 MCP server，强制 `requireInitialDiscovery: true`——connect 与首次 `tools/list` 必须在 client 时限内成功，因此死 server 会在这一步失败；只有工具确认存活后才 `ctx.plugin(SkillLocal, …)` 以隔离 provider `qwen-mm:<id>`（`includeDefaultRoots: false`、`watch: false`）注册 skill。失败时回滚已收集的 disposer。

4. **按能力失败隔离**（`src/index.ts:212-238` `apply`）：在 `ctx.effect` 生成器中逐能力挂载，单个能力任一阶段失败时，默认仅 `logger.warn` 跳过、其余能力保留；`strict: true` 时改为整体加载失败。未知 capability id 一律 warn-skip。

5. **uvx 启动参数与 ref 绑定**（`src/index.ts:171-176` `defaultMcpArgs`）：默认启动参数 `uvx --from qwen-mm-plugins[<cap>] @ git+<source>@<ref> <serverName>`，让 skill 正文与 server 实现精确锁在同一上游 ref；每能力可覆盖 `command`/`args`/`env`/`cwd`。

6. **凭据隔离契约**（README "Dependencies and privacy"、补丁内 mcp-client）：API key（`DASHSCOPE_API_KEY`、`SERPER_API_KEY` 等）不由本插件处理，`dsh-mcp-client` 会从子进程环境清除形似凭据的变量，必须按能力显式注入（如 `env: { DASHSCOPE_API_KEY: !!js process.env.X }`）。

7. **包级 invariant companion 为空操作**（`src/invariant.ts`）：仅 `ctx.invariants.register(PACKAGE_NAME, () => {})` 占位——能力通过既有 tool/skill 注册表贡献，包本身不维护独立的组合快照。

8. **测试覆盖**：`tests/qwen-mm.spec.ts` 用本地 fixture git 仓库验证 sparse-checkout 落盘、ref 复用与 `update: 'never'` 拒绝、缺 skill 目录的错误路径；`tests/loader-composition.spec.ts` 用真实 `@cordisjs/plugin-loader` + fixture 上游 + 内联 stdio MCP server（注册 `ping` 工具）验证端到端组装、按能力失败隔离、`strict` 模式整体失败三条路径。

## 与 DeepSeek Harness 主仓库的集成点
- **作为 workspace 包接入**：插件本体复制到 DSH 主仓库 `packages/qwen/qwen-mm/`；根 README 给出 `cp -a` 命令与 `pnpm install` + `pnpm exec tsc -b packages/qwen/qwen-mm` 构建步骤。
- **host 补丁强依赖**：必须 `git apply patches/qwen-mm-plugin.patch`，基线锁定 DSH `master` `b4b67f0`（0804 snapshot）。补丁不是 Qwen 业务 wrapper，而是 Qwen-MM 结果链需要的通用 DSH 基础设施，覆盖以下核心包：
  - 新增 `packages/mcp/mcp-client/src/image.ts`（186 行）——header-only PNG/GIF/JPEG/WebP 尺寸读取 + 网络边界 `projectImage` 校验（MIME 白名单、base64 合法性、单图与单结果字节/数量上限），非法载荷退化为确定性占位文本。
  - `packages/llm/llm/*` ——新增 `ImageBlock` 类型与图像输入 modality、LLM adapter 的 image 输入能力检查（不支持时在 provider I/O 前抛 `UNSUPPORTED_IMAGE_INPUT`）。
  - `packages/llm/token-meter/*` ——按图像尺寸计价的 token 测量更新。
  - `packages/compact/compact-basic/*`、`packages/core/session/*` ——compaction / replay / derived-cache 对图像块的 shadow 处理。
  - `packages/client/ui-conversation/*` ——Web tool-result 行对 image 块仅渲染尺寸/MIME 摘要，绝不渲染 base64。
  - `packages/mcp/mcp-client/src/index.ts`、`tools.ts`、多份 spec ——接线 required-initial-discovery 与 image 投影。
  - `tsconfig.host.json` 新增 `{ "path": "./packages/qwen/qwen-mm" }` 引用（补丁末尾，`patches/qwen-mm-plugin.patch:2094-2106`）。
  - 大量 `README.md`/`*.zh.md`/`README.i18n.yaml` 同步更新（含 mcp-client、llm、token-meter、compact-basic、llm-pi-ai、core-data-structures 等）。
- **composition opt-in**：插件不进默认 composition，使用方需在 cordis.yml / overlay 显式加 `- id: qwen-mm` 配置块（含 `source`、`ref`、`capabilities`）；由 `apps/cli` Loader 加载时还要在 `apps/cli/package.json` 加 `"@deepseek-ai/dsh-qwen-mm": "workspace:^"` 依赖。
- **来源**：根 README 说明本目录是从 DSH `feat-qwen-mm-plugin` worktree 分离出来的独立发布目录，对应上游 DSH 提交 `39a0f56 feat(qwen-mm): image content blocks and Cordis plugin for Qwen-MM capabilities`。

## 亮点与风险
亮点：
- **工具优先挂载顺序 + `requireInitialDiscovery`**（`src/index.ts:184-198`）是核心正确性保证：死 server 不会留下"有 skill 但无工具"的半挂载态。
- **ref 双绑**（`src/index.ts:153-157` + `defaultMcpArgs`）：同一精确 ref 同时锁住 skill 正文与 `uvx --from` 的 Python 发行版，避免指令与实现漂移。
- **凭据不外泄**：依赖 `dsh-mcp-client` 清扫环境，强制按能力显式传 key。
- **真实 Loader E2E 测试**（`tests/loader-composition.spec.ts`）覆盖正常组装、按能力隔离、strict 整体失败三条路径，质量较高。

风险：
- **host 补丁庞大且基线敏感**：`patches/qwen-mm-plugin.patch` 2106 行、触及 llm/mcp-client/token-meter/compact/ui-conversation 等核心包，基线锁死 `b4b67f0`；DSH 主仓库后续演进后 rebase 风险高（根 README 已警告"其他基线需先确认补丁可安全应用"）。
- **运行时强网络/工具依赖**：`ensureSkillSource` 首次拉取需要 `git`+网络，MCP 启动需要 `uvx`+上游 Python 解析；离线启动必须预热缓存与已解析 server（README "Known Limitations"）。
- **skill 正文非 vendored**：上游指令变化只在下一次配置 ref 到达，永不自动（`src/index.ts:111-145`）；这也意味着上游仓库结构若变动（如 `src/capabilities/<id>/skill` 路径漂移）会让本插件在拉取阶段失败。
- **Blender/FreeCAD 仍需宿主应用**：`extraEnv` 仅设 `QWEN_MM_AUTOLAUNCH=1` 告知 server 去启动，应用本身必须已安装授权（`src/index.ts:88-89`、README）。
- **仓库级 license 缺失**：`gh api` 显示 `license: null`，包内声明 BSD-3-Clause，根 README 提醒需补组织级 LICENSE——发布合规需跟进。
- **版本 0.0.1 + private:true + 单 commit**：处于"刚发布"形态，无 lockfile（根 README 明确"不含 pnpm-lock.yaml，由目标 workspace 重新生成"），无 CI 配置，无 LICENSE 文件落盘。
- **遗留开发痕迹**：根 README 的"发布到 GitHub"小节仍含开发机绝对路径 `/home/raum/deepseek-harness/qwen-mm-plugin-release`（README.md 中段），属卫生问题，不影响功能。
- **Loader 注入路径**：`loader-composition.spec.ts:99-110` 通过 `ctx.loader.internal.import` 注入插件模块；生产环境必须走真实 workspace 依赖，否则 Loader 找不到 `@deepseek-ai/dsh-qwen-mm`。
- **缓存目录信任边界**：`.dsh-qwen-ref` marker 是普通文件，单机缓存被篡改至匹配 ref 时不触发重新拉取（`src/index.ts:104-110`）；威胁面有限但依赖 `$DSH_HOME/cache/qwen-mm` 的本地完整性。

## 维护状态
- 仓库元数据（`gh api repos/dsh-external/Qwen-MM-Plugins`）：私有、未 archived/disabled、非 fork，主语言 TypeScript，`size: 49` KB，`stargazers_count: 0`，`default_branch: main`。
- 创建于 2026-08-05 14:55 UTC，最近 push 2026-08-05 16:13 UTC，最近更新 2026-08-05 16:14 UTC——本次 8.6 调研时点的新仓。
- 仅 1 个 commit：`d796a32 feat: publish Qwen-MM plugin`（本地 shallow clone 时间戳 2026-08-06 00:09 +0800）。
- 无 release、无 CI 工作流文件、无 LICENSE 落盘、无 CHANGELOG；处于首次发布后的初始形态。

## 备注
- 调研产物：克隆于 `/tmp/dsh-ext-research2/Qwen-MM-Plugins/`，本摘要在 `/tmp/dsh-ext-research2/Qwen-MM-Plugins.md`。
- 该仓库与上游 `QwenLM/Qwen-MM-Plugins`（Python 多模态插件本体）方向不同——本仓只做 DSH 接入；如 cron-check 同时检测到上游仓库，应作为独立条目处理。
- 入库 `research/` 后，cron-check 的 KNOWN_REPOS 同步会把本仓加入已知集合，避免后续重复报为新增。
- 与 dsh-external 其它 DSH 插件仓同构（workspace 包 + host 补丁 + 双语 README + i18n yaml 哈希配对），可归入"DSH 插件发布仓"族。
- 已按契约脱敏：未出现作者邮箱或真实姓名；保留的开发机路径仅作风险/卫生提示。
