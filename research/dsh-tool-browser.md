# dsh-tool-browser 调研摘要

## 一句话定位
DeepSeek Harness 的官方浏览器控制插件 `@deepseek-ai/dsh-tool-browser`：基于 Playwright，向模型暴露一组浏览器操作工具，每个调用 Agent 独占一个真实浏览器页面，会话进程内本地化、随 Agent 或插件销毁、不跨 DSH 重启。

## 技术栈与依赖
- 语言/打包：TypeScript（ESM，`type: "module"`），入口 `lib/index.js`，类型 `lib/types/index.d.ts`；包私有（`private: true`），版本 `0.0.1`，BSD-3-Clause。
- 运行时依赖：`playwright-core ^1.61.1`（不下载浏览器，需 `channel`/`executablePath` 或 `npx playwright install chromium`）、`schemastery ^3.18.0`（配置 schema）。
- 宿主 peer 依赖（必须在完整 Harness workspace 内运行）：`@deepseek-ai/dsh-agent`、`@deepseek-ai/dsh-invariants`、`@deepseek-ai/dsh-llm`、`@deepseek-ai/dsh-system-prompt`、`@deepseek-ai/dsh-tools`、`cordis ^4.0.0-rc.7`。
- 构建产物约定：仅发布 `lib/index.js`、`lib/invariant.js` 及类型声明，同时附带 `src`；通过 `exports` 暴露 `.` 与 `./invariant` 两个子路径。
- 测试：Vitest（42 个用例 = 30 无 key 单测 + 12 真实浏览器压测），需在完整 SDK workspace 下用 tsconfig paths 解析 `@deepseek-ai/dsh-*`。

## 文件结构概览
```
dsh-tool-browser/
├── README.md / README.zh.md / README.i18n.yaml   顶层双语 README + i18n 元数据
├── LICENSE                                        BSD 3-Clause
├── packages/web/tool-browser/                     插件本体
│   ├── package.json                               包元数据、依赖、exports
│   ├── tsconfig.json                              继承 workspace tsconfig
│   ├── README.md / README.zh.md / README.i18n.yaml  插件级双语文档
│   ├── src/
│   │   ├── index.ts          主插件（496 行）：Config/Session/工具注册/会话回收
│   │   └── invariant.ts      不变量伴随插件：断言"会话不苟活于已销毁 Agent"
│   └── tests/
│       ├── tools.spec.ts                  30 个无 key 单元测试
│       └── stress-browser.spec.ts         12 个真实浏览器压测（仅 Win32 + Playwright 浏览器存在时跑）
└── examples/browser-control/
    ├── browser.cordis.yml                 最小挂载 overlay（headless: true）
    └── README.md / README.zh.md           双语使用说明
```

## 核心功能与实现要点
1. **七件模型可见工具**（`src/index.ts` 中 `ctx.tools.register(defineTool(...))`）：`browser_open`（幂等，必须先调用）、`browser_navigate`、`browser_click`、`browser_type`、`browser_extract`（按 CSS 选择器或整页 body 取可见文本，受 `maxExtractChars` 截断）、`browser_screenshot`（写 PNG 到文件并返回路径与字节数）、`browser_list`/`browser_close`。每个工具都用 `defineTool` 注册 JSON Schema 输出与文本 render。

2. **每 Agent 一页面的 BrowserSession**（`src/index.ts` `class BrowserSession`）：`sessions = new Map<Agent, BrowserSession>()` 按执行 Agent 绑定；`ensurePage()` 懒启动 Chromium（`chromium.launch`，参数化 `channel`/`executablePath`/`headless`/`launchTimeoutMs`），并在浏览器断连时自动重启；`close()` 幂等关闭。

3. **中止即弃页的关键设计**（README 重点 + `browser_navigate.execute`）：工具调用通过 `withAbort(signal, work)` 与 `exec.signal` 竞速；中止时底层 Playwright 操作继续 detached 运行（其 late settlement 被观察以避免 unhandled rejection），而对 `browser_navigate` 额外调用 `session.invalidatePage()` 立即关闭处于半导航状态的页面，下一次操作会开新页，避免 DOM 操作卡在 pending 导航上直到自身超时。

4. **生命周期与进程内本地化**（`src/index.ts` `apply` 中 `ctx.on('agent/disposed', ...)` 与 `ctx.effect`）：Agent 销毁时 `closeFor(agent)` 关闭其浏览器；插件卸载时清空全部会话并关闭所有浏览器；README 明确"会话进程内本地化、不跨 DSH 重启"。

5. **不变量伴随插件**（`src/invariant.ts` + `index.ts` 中 `ACTIVE_SESSION_MAPS`/`checkSessionOwnership`）：将每个活跃会话表注册到全局 `ACTIVE_SESSION_MAPS`，伴随插件在 install 时与每次 `agent/disposed` 后的微任务里扫描所有会话表，发现任一 Agent 已不在权威 `agents` 注册表中仍持有会话即 `fail("browser session outlives its agent: <id>")`。这是 DSH "invariant companion" 契约的实例。

6. **系统提示注入**（`apply` 中 `ctx.systemPrompt.section({ name: 'tool:browser', order: 117, ... })`）：在 `order: 117` 处追加一段提示，告诉模型浏览器工具的用法及"只读检索优先用 web_search/web_fetch，仅当需要交互/JS 渲染/Cookie/截图时才用浏览器"。

7. **配置 schema 与超时预算**（`Config` via schemastery + 一组 `*_TIMEOUT_MS` 常量）：`channel/executablePath/headless(默认 true)/launchTimeoutMs(30s)/screenshotDir(OS 临时目录)/actionTimeoutMs(15s)/maxExtractChars(100k)`；工具侧 cooperative 超时：open/close 30s、DOM 动作 30s、navigate 60s、list 15s，Playwright 侧导航超时 45s 独立设置。

8. **自带示例 overlay**（`examples/browser-control/browser.cordis.yml`）：通过 `insert` 挂载插件 `id: tool-browser`，`headless: true`，可直接 `dsh --config "$PWD/examples/browser-control/browser.cordis.yml"` 运行。

## 与 DeepSeek Harness 主仓库的集成点
- **分发定位**：本仓是插件的"独立分发版"，只含插件包与示例，**不含**完整 SDK 源；必须放进完整 Harness workspace 才能构建/测试/运行（README 与 package.json peerDependencies 均明示）。
- **Seam 1 — Cordis 插件协议**：`export const name = 'tool-browser'`、`export const inject = ['tools', 'systemPrompt', 'agents']`、`export function apply(ctx: Context, config: Config)`，是标准 DSH/Cordis 插件形态；通过 `ctx.plugin(ToolBrowser, config)` 或 YAML `id: tool-browser, name: '@deepseek-ai/dsh-tool-browser'` 挂载。
- **Seam 2 — 工具注册**：消费 `@deepseek-ai/dsh-tools` 的 `defineTool`、`TOOL_ABORTED`、`ToolExecution`（含 `exec.agent` 与 `exec.signal`），把七个浏览器工具注册进工具注册表。
- **Seam 3 — Agent 所有权**：消费 `@deepseek-ai/dsh-agent` 的 `Agent` 类型，按 `exec.agent` 做 per-agent 会话映射，并订阅 Cordis 事件 `agent/disposed` 做清理。
- **Seam 4 — System Prompt**：消费 `@deepseek-ai/dsh-system-prompt` 的 `ctx.systemPrompt.section(...)` 注入工具使用说明。
- **Seam 5 — 错误类型**：使用 `@deepseek-ai/dsh-llm` 的 `HarnessError` 携带 `TOOL_ABORTED` code 构造规范中止错误。
- **Seam 6 — Invariant 契约**：`src/invariant.ts` 通过 `ctx.invariants.register(PACKAGE_NAME, install)`（来自 `@deepseek-ai/dsh-invariants` 的 `InvariantInstaller`/`InvariantFailure`）注册伴随不变量，与 DSH 主仓的不变量框架对接。
- **测试侧**：`tests/stress-browser.spec.ts` 通过 `@deepseek-ai/dsh-agent`（默认导出 AgentRegistry）、`@deepseek-ai/dsh-session` 的 `Session`/`SessionId`、`@deepseek-ai/dsh-llm` 的 `CallId`、`@deepseek-ai/dsh-system-prompt` 默认导出、`@deepseek-ai/dsh-tools` 默认导出 构造真实 Context，证明这些是 DSH 主仓 workspace 包。

## 亮点与风险
- **亮点：中止安全模型严谨**。`withAbort`（`src/index.ts`）既保证 abort 立即拒绝、又观察 detached 操作的 late settlement 防 unhandled rejection；`browser_navigate` 在 abort 后 `invalidatePage()` 丢弃半导航页面（README "Key design"），避免后续 DOM 操作被 pending 导航阻塞——这是工程上少见的细节处理。
- **亮点：每 Agent 隔离 + 不变量兜底**。`ACTIVE_SESSION_MAPS` + `checkSessionOwnership`（`src/index.ts`/`src/invariant.ts`）跨微任务断言"无会话苟活于已销毁 Agent"，把生命周期错误升级为可观测的不变量失败。
- **亮点：测试覆盖真实浏览器**。`tests/stress-browser.spec.ts`（420 行）覆盖真实 DOM 交互、并发 Agent 隔离、中止悬挂导航、外部杀进程恢复、泄漏检测、50 步马拉松；无浏览器时自动 skip，避免 CI 假红。
- **风险：浏览器需外部供给**。`playwright-core` 不下载浏览器，部署必须配置 `channel`/`executablePath` 或预跑 `npx playwright install chromium`（README "Browser prerequisites"），否则 `chromium.launch` 失败。
- **风险：压测平台耦合**。`tests/stress-browser.spec.ts` 中 `realBrowsersAvailable = process.platform === 'win32' && existsSync(...LOCALAPPDATA/ms-playwright)`，非 Windows 或无 Playwright 浏览器的环境会跳过 12 个核心压测，回归覆盖可能在非 Win CI 上 silently 缩水。
- **风险：分发版无独立可运行性**。peer 依赖均为 workspace 包且未发布（`^0.0.1`），脱离主仓库 workspace 既不能 `pnpm install` 也不能跑测试；本仓单独克隆（如本次调研）只能读源码，不能验证构建。
- **风险：CSS 选择器直传**。`browser_click`/`browser_type`/`browser_extract` 直接接受任意 CSS 选择器，模型若传畸形选择器会抛 Playwright 解析错误，工具层无选择器预处理或沙箱化。

## 维护状态
- 版本 `0.0.1`、`private: true`，处于早期内部分发阶段，尚未作为独立公开 npm 包发布。
- 文档完备：顶层 + 插件 + 示例三层均有中英双语 README 与 `README.i18n.yaml` 元数据，说明有意识在维护多语言文档流。
- 测试体系成熟（42 用例，含真实浏览器压测与泄漏/崩溃探测），显示活跃工程投入。
- LICENSE 为 BSD 3-Clause，与 DSH 主仓一致；无独立 CHANGELOG / 发布记录可见。
- 最近提交时间未能从 shallow clone 直接判断（仅 1 commit depth），但内容与 DSH 主仓库 `packages/web/tool-browser/` 路径同源，应为主仓 plugin 的镜像/拆分分发。

## 备注
- 克隆方式：`git clone --depth 1 https://github.com/dsh-external/dsh-tool-browser.git`，仅含最新一次提交，无历史可考；如需 commit 历史或 blame 信息建议 `gh api repos/dsh-external/dsh-tool-browser/commits`。
- 调研中未发现作者邮箱/真实姓名信息；脱敏无问题。
- 关键文件:行号索引：
  - 主插件定义与工具注册：`packages/web/tool-browser/src/index.ts:1-496`
  - `BrowserSession` 类（懒启动/弃页/关闭）：`packages/web/tool-browser/src/index.ts:74-148`
  - `withAbort` 中止竞速：`packages/web/tool-browser/src/index.ts:163-184`
  - `apply` 生命周期/事件/系统提示：`packages/web/tool-browser/src/index.ts:259-300`（及后续各工具 execute）
  - 不变量伴随：`packages/web/tool-browser/src/invariant.ts:1-49`
  - 配置 schema：`packages/web/tool-browser/src/index.ts:51-65`
  - 压测平台门控：`packages/web/tool-browser/tests/stress-browser.spec.ts:30-32`
