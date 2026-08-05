# dsh-pi-adapter 调研摘要

## 一句话定位
dsh-pi-adapter 是一个 cordis 插件，把 [pi coding-agent](https://github.com/earendil-works/pi)（earendil-works 出品的 CLI 编码代理，**不是** "Pi AI"）的扩展 API（`ExtensionAPI`）桥接到 DeepSeek Harness（dsh）中，让 `export default (pi) => {...}` 形式的 pi 扩展无需修改即可在 dsh 里加载运行。注意：它**不是** LLM/Provider 适配器——LLM 接缝（model/provider）刻意不桥接，由 dsh 自己拥有。

## 技术栈与依赖
- 语言/运行时：TypeScript（`typescript ^5.9`），ESM（`"type": "module"`），目标 Node 22/24（CI matrix）。
- 宿主框架：cordis `4.0.0-rc.7`（peerDependency，沿用 dsh 宿主实例以保留 service 身份）。
- 核心依赖：`jiti ^2.4.2`（按 pi 自身的方式直接加载 `.ts` 扩展，无构建步骤）、`schemastery ^3.2.0`（Config schema 校验）。
- 构建发布：`tsdown ^0.22.14` 把 jiti/schemastery 内联进自包含 `lib/index.js`（仅 cordis 留外部），`tsc` 产 `lib/types/`；`lib/` 入仓以便插件管理器直接从 git 安装。
- 测试：`vitest ^3.0.0`，三套——hermetic fixtures、bridge（对 contract-fake ctx）、integration（真 dsh 注册表，自动跳过无 sibling checkout 的环境）。
- 包管理：pnpm@11.20.0（pnpm-workspace.yaml）；私有包（`"private": true`），MIT License。
- dsh 集成声明：`dsh.plugin.json` manifest（`engines.dsh >=0.0.1`，`contributes.tools/skills` 均为空——工具/命令由 pi 扩展动态注册）。

## 文件结构概览
```
dsh-pi-adapter/
├── src/
│   ├── index.ts                    # cordis 插件入口（apply + Config schema + inject:['tools']）
│   ├── loader/jiti-loader.ts       # jiti 加载 + pi 运行时 alias 解析（指向 npm root -g 的 pi 安装）
│   └── compat/
│       ├── ExtensionApi.ts         # PiCompat + ExtensionBridge，1202 行，ExtensionAPI 全表面桥接
│       ├── SessionProjection.ts    # dsh session 事件日志 → pi SessionEntry[] 视图
│       └── unsupported.ts          # guardSeam Proxy + UnsupportedSeamError（fail-fast 边界）
├── test/
│   ├── fixtures/                   # 18 个无依赖的 pi 扩展夹具（echo-tool/blocker/mutator/lifecycle/...）
│   ├── fixtures.test.ts            # loader 测试（hermetic + 可选加载真实 ~/.pi 扩展）
│   ├── bridge.test.ts              # 对 contract-fake ctx 的单测（29.7KB，镜像 dsh 校验行为）
│   └── integration.test.ts         # 针对真 dsh 的注册/执行/瀑布否决（13.1KB，自跳过）
├── lib/                            # 入仓的构建产物（lib/index.js 320KB + lib/types/）
├── dsh.plugin.json                 # dsh 插件 manifest
├── package.json / tsconfig*.json / tsdown.config.ts / pnpm-*
├── .github/workflows/ci.yml        # CI + 每周一 cron（监控 pi-coding-agent@latest 漂移）
└── README.md                       # 12.5KB，文档极完整（含翻译分级表）
```

## 核心功能与实现要点
1. **ExtensionBridge + PiCompat 实现 pi `ExtensionAPI` 全表面**（`src/compat/ExtensionApi.ts:111` 起）。每个方法归入四档之一：
   - `[direct]` 形状与 cordis 接缝一一对应（如 `session_start→session/created`、`ctx.isIdle()` 直读 agent.status）。
   - `[adapt]` 用兼容包装器适配 dsh 表面（如 `registerTool` 加 dsh 必需的 `output{schema,render}`，TypeBox→JSON Schema；`tool_call`→`tools/pre-execute` 瀑布）。
   - `[degrade]` 只写无返回的 sink（`ui.notify/setStatus/setWidget`、`registerShortcut`、`setModel` 等）大声日志后继续。
   - `[unsupported]` 无真值的读接缝（`ctx.ui.confirm/select/input`、`isProjectTrusted`、`modelRegistry.*`、`getThinkingLevel`）抛 `UnsupportedSeamError`。
2. **"Answer-truthfully" 不变量**（`src/compat/unsupported.ts:1-58`、README 同名小节）：扩展会**读取并据此分支**的接缝，桥接器要么给真值要么抛错，绝不伪造。原文举的反例很具体——`permission-gate.ts` 会基于 `ctx.ui.select()` 的返回值放行/拦截，返回伪造的 `undefined` 会让"显式 No 才放行"的门**静默 fail-open**；`isProjectTrusted()` 早期硬编码 `true` 属同类。`guardSeam` 用 Proxy 把"读未实现成员"从"扩展内 `Cannot read properties of undefined`"变成带扩展名+接缝名的明确错误。
3. **jiti 加载器 + pi 运行时 alias**（`src/loader/jiti-loader.ts:78-128`）：扩展常 `import '@earendil-works/pi-ai' / 'pi-tui' / 'pi-coding-agent' / 'typebox'`，这些包只存在于全局 pi 安装（`npm root -g/@earendil-works/pi-coding-agent`）。loader 把每个 alias 映射到**具体入口文件**（不是目录——jiti 的目录 alias 会绕过 package-exports）。子路径如 `/compat` 也单独映射。
4. **事件/瀑布桥接**（`src/compat/ExtensionApi.ts:209-360`）：`tool_call`→`tools/pre-execute` 瀑布（`block`→`{kind:'deny'}`，未 block 必须 `next()`）；`tool_result`→`tools/post-execute`；`input`/`before_agent_start`→`agent/prompt-submit`；`agent_settled` 刻意不走 `agent/settled`（每终态 turn 都触发、retry 中会闪烁），改订阅 `agent/status` 到达 `idle`；`session_compact`→`session/event` 流里 `compact/end` 且无 `error`。被禁用的扩展（quarantine）的 `tool_call` 监听**保持订阅且持续 deny**——绝不"消失变放行"。
5. **SessionProjection**（`src/compat/SessionProjection.ts`）：把 dsh 线性 session 日志投影成 pi `SessionEntry[]`。两模型差异处一律"少答不编造"：`parentId` 恒为上一条（dsh fork 会 mint 新 session 而非分支，故 `getBranch()≡getEntries()`）；`toolName` 从更早的 `tool/call` 配对（`tool/result` 只有 `callId`）；`details` 仅对 pi 注册的工具存活（走 `presentationMeta→tool/result.meta`）。
6. **可观测的运行时追踪**（`ExtensionApi.ts:139-180`）：`trackRuntime()` 始终订阅 `session/created|event`、`agent/session-start|status|inbox/*`，所以即便扩展不订阅任何事件也能回答 `ctx.isIdle()`、`hasPendingMessages()`（inbox 深度计数）、`getSystemPrompt()`（从最近 `request/header` 折叠——dsh 的"模型可见即可日志"规则）。
7. **配置 + 处置语义**（`src/index.ts:73-110`）：Config 含 `extensions`/`scanDirs`（**相对路径相对宿主进程 cwd**，与 `cordis.yml` 里插件 specifier 相对配置文件位置的规则相反——README 反复强调）、`toolPrefix:'pi_'`、`includePiHome:true`、`strictUi:false`、`onUnsupported:'disable'|'fail'`。`apply` 返回 async disposer，按注册逆序卸载全部扩展效果；`mount` 中异步 factory 出错会先 unwind 部分注册再抛出（绝不挂半个扩展）。

## 与 DeepSeek Harness 主仓库的集成点
**接缝类型：cordis 插件（运行时桥接），不是补丁、不是 LLM provider。**

直接消费的 dsh 服务/事件（`inject: ['tools']`，其余靠 `ctx.get()` 探测+降级）：
- `ctx.tools.register()` —— `packages/core/tools`，强制带 `output{schema,render}` 与 `presentationMeta`；`tools/pre-execute`、`tools/post-execute` 瀑布（参数 deep-frozen，handler 收可变 clone，故**原地改参数会被丢弃**而非报错）。
- `ctx.commands.register()` / `commands.list()` —— `packages/ui/commands`，单对象定义、必填 `description`、handler 收 `CommandInvocation{rawInput}`。
- `ctx.bash` BashExecutor —— `packages/bash/bash`，`resolve(request)`→`run(spec)`；pi 的 argv 单词逐个 shell-quote（dsh 收 shell 字符串）。
- `agent/*` 生命周期：`agent/session-start`、`agent/settled`、`agent/status`（idle 边）、`agent/inbox/enqueue|dequeue|discard`、`agent/prompt-submit` 瀑布、`agent.followup()`/`agent.steer()`/`agent.cancel({kind:'user'})`。
- `session/created|disposed|event`、`compact/end`、`compact.compactNow()`、`request/header|context`、`assistant/message`。
- `ctx.user-interaction`（`packages/ui/user-interaction`）—— 仅当 UI provider 已挂载时，`ctx.ui.confirm/select/input/editor` 路由过去；否则抛错不伪造。
- cordis 自身：`ctx.on/emit`、`ctx.get`、`ctx.logger`、`crypto.randomUUID`。

**与"主仓库 llm seam"的对比结论**：本仓**不**是 LLM 适配器（任务标题里的"Pi AI 适配器？"是误解——`pi` 指 earendil-works/pi coding-agent CLI 的扩展生态，与 LLM provider 无关）。`registerProvider`/`unregisterProvider`/`setModel`/`setThinkingLevel`/`getThinkingLevel`/`modelRegistry.*` 全部 `[degrade]` 或 `[unsupported]`——dsh 通过 `cordis.yml` 自管 provider/model，桥接器刻意不碰这一层。integration test 引用的 dsh 包路径里也没有任何 llm/provider 包（仅 `core/tools`、`core/session`、`core/system-prompt`、`ui/commands`、`ui/user-interaction`、`vendor/cordis`）。

## 亮点与风险
**亮点**
- 设计纪律强：四档翻译分级 + "answer-truthfully" 不变量 + Proxy 守卫（`src/compat/unsupported.ts:46-58`），把"静默 fail-open"这类安全敏感 bug 显式化，注释里直接给出历史反例（`permission-gate.ts` / 硬编码 `isProjectTrusted=true`）。
- 自包含发布：`lib/` 入仓 + `dsh.plugin.json`，两种 dsh-external 管理器（`dshx install <git-url>` 与 `dsh plugin install <dir>`）都可直接装，无需发布到 npm。
- 文档/代码一致：README 的翻译分级表与源码 `// [direct|adapt|degrade|unsupported]` 标注、`EVENT_MAP`（`ExtensionApi.ts:181-205`）逐一对应。
- CI 周一 cron 监控 `@earendil-works/pi-coding-agent@latest` 漂移（`.github/workflows/ci.yml:8-12`），并 gate `lib/` 新鲜度（`git diff --exit-code lib/`）。
- 18 个夹具覆盖面广（typebox-tool、async-init、seam-at-mount、seam-in-gate、bus-publisher/subscriber、input-transform、session-state...）。

**风险**
- 依赖未公开/私有的 dsh 内部契约（`packages/core/tools`、`packages/ui/commands` 的 register 形状，`vendor/cordis`），dsh 内部 API 变更会直接打破桥接；integration test 因 dsh 仓库不可公开 clone 而**默认自跳过**（`test/integration.test.ts:7-28`、CI 注释），CI 实际只跑 hermetic 套件。
- 依赖全局 pi 安装做 alias（`loader/jiti-loader.ts:106-128` `locatePi()` 调 `npm root -g`）：无 pi 全局安装时 alias 全空，依赖这些包的扩展会加载失败。
- 桥接面有已知缺口（README Status 节）：per-prompt `agent_start` 无精确 dsh 等价、`ctx.ui` 全交互面需 UI provider、provider/model 不桥接、pi 自定义 session 条目持久化、`event.input` 参数重写被丢弃。
- 仅一位作者（GitHub `yzchen`），12 次提交全部集中在 2026-08-05 一天——非常新，无外部使用者反馈。
- `lib/index.js` 320KB 入仓，每次源码改动需同步重 build 否则 CI gate 失败；同时 `extensions/scanDirs` 相对 cwd 解析与 `cordis.yml` 插件 specifier 相对配置文件位置的不对称（README 反复提示）是配置陷阱。

## 维护状态
- 极新：全部 12 次提交均发生于 2026-08-05（最近一次 `2026-08-05T14:58:35Z`，`ci: gate committed lib freshness`），单一作者 `yzchen`，远端 `https://github.com/dsh-external/dsh-pi-adapter.git`。
- CI 绿色矩阵 Node 22/24，覆盖 install/typecheck/build/hermetic test；integration 自跳过。
- 单仓 56 对象（`--depth 1` 共 56 objects / 51 pack），属小型纯桥接仓。
- 当前定位为"核心接缝已验证、端到端跑通 headless-agent 示例（fixture `pi_echo` + 真实 `~/.pi/todo.ts` 均执行过）"的工作中版本（v0.1.0）。

## 备注
- "Pi AI 适配器"的猜测**不成立**：仓库名 `pi` 指代 earendil-works/pi coding-agent CLI，与 Raspberry Pi / Pi AI / Inflection Pi 等均无关。
- 摘要基于 `--depth 1` clone（HEAD=`d387cb5`）+ `gh api` 取全部 12 次提交元数据交叉验证。
- 仓库无 CHANGELOG、无 CONTRIBUTING、无 issues/PR 模板（仅 ci.yml），无 release/tags。
- 主交付物为本摘要文件 `/tmp/dsh-ext-research2/dsh-pi-adapter.md`；clone 产物在 `/tmp/dsh-ext-research2/dsh-pi-adapter/`。
