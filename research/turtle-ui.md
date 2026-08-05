# dsh-external/turtle-ui

## 一句话定位
`@deepseek-ai/dsh-tui`：DeepSeek Harness 的「外置」交互式终端前端——基于 `@earendil-works/pi-tui` 渲染持久化会话转录、驱动一个配置好的 agent、提供键盘驱动的用户问答/模型选择/会话恢复等对话框；不持有 agent/model/tool/persistence 生命周期，也不恢复被剥离的 TUI 专属 CLI launcher。README 自嘲为「a Friday afternoon 的第一个 dsh UI」，实为从 deepseek-harness 主仓 monorepo 中抽出的 `packages/ui/tui`，独立成 sibling 仓库。

## 技术栈与依赖
- 语言/运行时：TypeScript ESM，Node `^22.19.0 || >=24.0.0`，包管理器 pnpm@11.7.0；私有包 `@deepseek-ai/dsh-tui@0.0.1`，BSD-3-Clause。
- 框架/构建：Cordis `^4.0.0-rc.7`（plugin/Service/Context/Fiber），schemastery `^3.18.0`（配置 schema），tsdown `^0.22.2`（产物打包），Vitest `^4.1.8` + `@xterm/headless@5.5.0`（终端快照测试），vite-tsconfig-paths。
- 核心运行依赖：`@earendil-works/pi-tui@0.80.7`（终端 UI 内核，带 patches/ 下 347 行补丁）、`diff@^9`（编辑差异）、`saxes@6.0.0`（XML 工具输出解析）。
- 主仓对等依赖（peerDependencies，24 个 `@deepseek-ai/dsh-*` 包，3 个可选）：agent / agent-loop / commands / compact / invariants / llm / llm-retry / goal / session / session-persistence / session-projection(-cache) / session-query / session-reference / session-title / skill / subprocess / system-prompt / token-meter / tools / user-interaction。
- tsconfig 显式 `extends ../deepseek-harness/tsconfig.base.json` 并通过 project references 把所有 dsh-* 包指向 `../deepseek-harness/packages/...`——硬编码「sibling 仓」布局。

## 文件结构概览
共 90 个 git 跟踪文件，深度 1 浅克隆仅见 1 commit（`08b3c42 Rename Cordis config`，2026-08-05 19:52 +0800）。

```
turtle-ui/
├── package.json              # @deepseek-ai/dsh-tui, exports map 含 . / invariant / prompt / src/*
├── tsconfig.json             # extends ../deepseek-harness/tsconfig.base.json
├── tsdown.config.ts / vitest.config.ts / tsconfig.vitest.json
├── pnpm-lock.yaml / pnpm-workspace.yaml
├── cordis.yaml               # dsh --config overlay：TUI 绑到 sessionId=main
├── AGENTS.md                 # 单条规约：在 tmux 里展示 TUI，不要污染会话转录
├── README.md                 # 开发与运行说明
├── LICENSE                   # BSD-3-Clause
├── patches/
│   └── @earendil-works__pi-tui@0.80.7.patch   # 给 Editor 加 frame/prompt 选项 + wordWrap 续行宽度
├── src/
│   ├── index.ts              # 主插件（1994 行）：name='ui-tui'，inject 9 服务，createTuiChat
│   ├── prompt.ts             # TuiPromptService：可信 ANSI 片段 + 微任务合并通知
│   ├── runtime.ts            # TuiRuntime / TuiResumeHost 边界接口
│   ├── config.ts             # Schemastery Config / TuiConfigSchema / resolveTuiConfig 默认值
│   ├── invariant.ts          # 占位 invariant companion（无运行时不变量）
│   ├── extension/
│   │   ├── types.ts          # 公开扩展契约：TuiComponent/Theme/Viewport/Overlay*
│   │   └── overlay-manager.ts # 378 行：FIFO 模态队列、信号中止、teardown 收尾
│   ├── components/           # theme / dialogs / transcript / content / text
│   └── chat/                 # 10 个子控制器：tokens/channel/file-autocomplete/helpers
│                             #   /model-command/questions/resume/skill-invocation
│                             #   /timing/autocomplete
└── tests/
    ├── harness.ts            # createTuiTestHarness：内存 Session + 假 Agent + 假 LLM
    ├── headless-terminal.ts / session-query.ts / tui.snapshot.ts 等
    ├── *.spec.ts             # 14 个测试套件（plugin-shape / prompt / extension / retry / status 等）
    └── snapshots/*.expected.txt  # 40+ 渲染期望文本（对话流、问答、模型选择、retry、compaction 等）
```

## 核心功能与实现要点
1. **插件入口与 Context 服务声明**（`src/index.ts:240-285`）：`name='ui-tui'`，`inject=['agents','sessions','commands','userInteraction','tools','llm','systemPrompt','tokenMeter','tuiPrompt']`。通过 `declare module 'cordis'` 给 Context 加 5 个新成员（`tui` / `tuiResumeHost` / `mainSessionId` / `tuiGoodbyeMessage` / `tuiInitialSkill`），并导出 3 个 `ctx.provide` key（`MAIN_SESSION_ID_KEY` / `TUI_GOODBYE_MESSAGE_KEY` / `INITIAL_SKILL_KEY`）作为 launcher→Loader-mounted plugin 的唯一传参通道（因 `!!js` 仅对 entry context 求值）。
2. **交互扩展服务 `TuiExtensionService`**（`src/index.ts:~290` + `src/extension/types.ts` + `src/extension/overlay-manager.ts`）：抽象 Service，向其它插件暴露 `openOverlay(request)` 入口；`TuiOverlayManager` 维护单条 FIFO 模态队列，按调用方 fiber 拥有 overlay 生命周期，使用 `AbortSignal` 在请求/调用方/TUI 关闭时统一中止，teardown 时 settle 所有 queued/active overlay。`TuiTheme` 提供语义色（text/brand/dim/accent/success/warning/error/bold），`TuiViewport` 暴露 columns/rows 而不交出可变 Terminal 对象。
3. **Prompt 模板服务**（`src/prompt.ts`）：`TuiPromptService` 维护一组 `${name}` 模板片段（小写斜杠命名正则校验），支持可信 ANSI 控制序列；变更合并到 microtask 单次回调；listener 抛错/reject 都被 `errorChain` 容器化，避免饿死后续观察者。配套导出 `parseTuiPromptTemplate` / `renderTuiPromptTemplate`（缺值时吃掉前导空白）。
4. **运行时边界与原子 resume handoff**（`src/runtime.ts`）：`TuiRuntime` 接口给 CLI 注入 `terminal / exit / formatCwd / gitBranch / now / handoffResume / goodbyeMessage`；`TuiResumeHost.handoff(sessionId, cwd)` 在提交 teardown 后接管致命错误上报与进程退出——这是 README 明确点名的「独立运行时不可用」的能力。
5. **配置 schema 与默认值**（`src/config.ts`）：`Config = z.object({...})` 提供给 app bundle 嵌入；`TuiConfigSchema` 提供给 Loader 校验；`resolveTuiConfig()` 为绕过 Loader 的直接调用方补默认值（颜色、对话宽度/高度、`@` 文件搜索阈值等）。默认左 prompt 为 `${cwd}${git/worktree}${model}${token_meter/cache_hit_rate}${context}`。
6. **第三方依赖补丁**（`patches/@earendil-works__pi-tui@0.80.7.patch`，347 行）：给 pi-tui 的 `Editor` 加 `frame: "horizontal" | "none"` 与 `prompt: {first, continuation}` 一对等宽前缀，并改造 `wordWrapLine` 引入 `continuationWidth`，使得 Turtle UI 能在输入区显示 `${symbol} ${indicator}` 形态的多行续行 prefix——属于非琐碎上游增强。
7. **Chat 子控制器**（`src/chat/`）：通过 `ChatChannelDeps`（`src/chat/channel.ts`）共享 `ctx / resolved / palette / overlayManager` 与回调，分模块实现：模型选择（`model-command.ts`）、ask-user 队列（`questions.ts`）、会话 resume（`resume.ts`，含并发扫描上限 `resumeScanConcurrency`）、`@` 工作区文件搜索（`file-autocomplete.ts`）、step 计时与状态 glyph 渐变（`timing.ts`）、`/skill:` 调用渲染（`skill-invocation.ts`）。
8. **测试基础设施**（`tests/harness.ts`）：`createTuiTestHarness` 用 `@xterm/headless` 终端 + 内存 `SessionStore` + 假 `Agent`（记录 sent/steered/injected/cancelled）+ 假 LLM 目录构造生产形态 TUI；40+ 个 `*.expected.txt` 快照覆盖窄宽、错误、模型切换、retry 四态、问答分页、resume loading、压缩前后等渲染状态。

## 与 DeepSeek Harness 主仓库的集成点
- **Sibling 布局强约束**：README 要求把 `turtle-ui` 与 `deepseek-harness` 平级放在 `~/git/` 下；`tsconfig.json` 通过 `extends ../deepseek-harness/tsconfig.base.json` + 21 个 project references 直接指向主仓 `packages/...`，所有 dsh-* peer 依赖都靠这一布局在 typecheck/test 时解析。
- **Link 进 CLI app**：开发流程 `pnpm install && pnpm run build && pnpm --dir ~/.dsh/source/current/apps/cli link ~/git/turtle-ui`——即把本包软链进源码安装的 `dsh` CLI 应用，由 Loader 解析两条裸插件入口（`@deepseek-ai/dsh-tui/prompt` 与 `@deepseek-ai/dsh-tui`）。
- **cordis.yaml overlay**：`dsh --config ~/git/turtle-ui/cordis.yaml` 启动；该 overlay 显式装配 agent-loop / system-prompt / llm-deepseek（`deepseek-v4-pro` + `reasoningEffort: max`）/ fs-sandbox / tools(native)，并 `insert` 一系列主仓插件——`dsh-session-reference` / `dsh-session-projection`(+cache) / `dsh-storage(-json/-domain)` / `dsh-tmux-context` / `dsh-tui/prompt` / `dsh-tui`（`sessionId: main, showReasoning: true, maxToolOutputLines: 6`）/ `dsh-tool-ask-user`。
- **通过 Context key 接收 launcher 输入**：`MAIN_SESSION_ID_KEY` / `TUI_GOODBYE_MESSAGE_KEY` / `INITIAL_SKILL_KEY` 是 launcher argv → Loader-mounted plugin 的唯一通道，主仓 shipped CLI 在挂载前 `ctx.provide` 这些 key 来固定 main session、退出提示语、首次 `/skill:` 调用（`dsh migrate` / `dsh upgrade`）。
- **明确不可用项**：README 与 `runtime.ts` 都标注——独立 overlay 启动不会恢复被剥离的 TUI 专属 launcher，因此 launcher 拥有的 `/resume` 原地交接（`handoffResume`）与退出提示行（`goodbyeMessage`）在 sibling standalone 模式下不可用。

## 亮点与风险
- **紧密耦合主仓 internals**：单插件 `inject` 9 个服务 + Context 上声明 5 个新成员 + 3 个 `ctx.provide` key（`src/index.ts:240-285`），任意主仓服务签名变动都会同时砸掉 typecheck 与运行时；升级主仓时此仓几乎必然要同步改。
- **pi-tui 补丁是脆弱面**（`patches/@earendil-works__pi-tui@0.80.7.patch`）：补丁给 Editor/wordWrapLine 增加了 frame/prompt/continuationWidth，涉及渲染主循环多分支；pi-tui 任意 0.80.x 之后版本升级都需要重做补丁，且补丁本身的回归覆盖只能靠 Turtle UI 的 40+ 快照保证。
- **1994 行单文件**（`src/index.ts`）：渲染、键位、转录、控制器装配全在一个文件里，可读性偏低；维护风险集中在该文件。
- **开发流程硬编码路径**（`README.md`）：`pnpm --dir ~/.dsh/source/current/apps/cli link ~/git/turtle-ui` 与 `~/git/` 布局假设较强，非默认安装路径或 Windows 环境需手工调整。
- **快照测试基线庞大**（`tests/snapshots/*.expected.txt`）：40+ 个文本 fixture 与具体渲染输出强绑定，任何细小视觉/ANSI 变化都会触发全量重写快照，CI 噪声偏高但同时也是回归保护。
- **亮点**：扩展契约设计干净——`TuiOverlayManager` 把 pi-tui 的可变 Terminal/焦点/句柄全部私有化，只对外暴露 immutable `TuiViewport` / `TuiTheme` 与 effect-owned overlay 句柄；prompt 服务用 microtask 合并 + listener 抛错容器化的并发模型很扎实；测试 harness 用 fake agent + xterm headless 真驱动终端，渲染契约有真实保障。

## 维护状态
- 当前活跃：最新 commit 落在今天（2026-08-05），消息为「Rename Cordis config」；版本号 `0.0.1`、`private: true`，处于「抽离后早期」阶段。
- 浅克隆仅显示 1 commit（属于 `--depth 1` 限制，非实际历史深度）；README 描述与 `former packages/ui/tui` 字样表明这是 monorepo 拆分后的新 sibling 仓。
- 90 个跟踪文件、40+ 快照、14 个 spec、378 行 overlay-manager 与 1994 行主插件，工程化与测试覆盖成熟度远高于「0.0.1」标签暗示的水平——是从主仓直接迁出的成熟代码。

## 备注
- 脱敏：本摘要不含作者真实姓名/邮箱；commit 哈希 `08b3c42` 为公开 git 历史。
- 关键文件位置（绝对路径）：
  - 主插件：`/tmp/dsh-ext-research2/turtle-ui/src/index.ts`
  - Prompt 服务：`/tmp/dsh-ext-research2/turtle-ui/src/prompt.ts`
  - 运行时边界：`/tmp/dsh-ext-research2/turtle-ui/src/runtime.ts`
  - 配置 schema：`/tmp/dsh-ext-research2/turtle-ui/src/config.ts`
  - 扩展契约：`/tmp/dsh-ext-research2/turtle-ui/src/extension/types.ts`、`/tmp/dsh-ext-research2/turtle-ui/src/extension/overlay-manager.ts`
  - pi-tui 补丁：`/tmp/dsh-ext-research2/turtle-ui/patches/@earendil-works__pi-tui@0.80.7.patch`
  - 启动 overlay：`/tmp/dsh-ext-research2/turtle-ui/cordis.yaml`
  - 测试 harness：`/tmp/dsh-ext-research2/turtle-ui/tests/harness.ts`
- 与第一批调研的其他 dsh-external 仓相比，turtle-ui 是少数对主仓 internals 有「深度耦合 + sibling 路径假设」的仓库，任何主仓重构（尤其 Cordis 升级、Context 服务命名、pi-tui 版本）都需要此仓同步联动。
