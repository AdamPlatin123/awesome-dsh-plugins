# dsh-external/dsh-cc-tui 调研摘要

## 一句话定位
Claude Code 风格的全屏交互终端（TUI），作为 DeepSeek Harness 的官方 cordis 插件"前门"（与 `dsh-jsonrpc` 同类客户端驱动入口），UI 核心是从 Claude Code 泄漏源码近乎逐字移植的 Ink（React 终端渲染器、yoga 布局、termio 解析、差分渲染），DSH 侧的屏幕与通道则是新写的。

## 技术栈与依赖
- **运行时**：Node `^22.19 || >=24`，纯 ESM（`"type": "module"`），`engines.dsh: >=0.0.1`
- **语言/框架**：TypeScript `^6.0.3`、React `^19.2`、`react-reconciler ^0.33`
- **核心 peer**：`cordis ^4.0.0-rc.7`、`@deepseek-ai/dsh-agent`、`@deepseek-ai/dsh-llm`、`@deepseek-ai/dsh-session`（均 `^0.0.1`）、`schemastery ^3.18`
- **业务依赖**：`chalk 5`、`marked 18`、`highlight.js`、`cli-highlight`、`lodash-es`、`wrap-ansi`、`auto-bind`、`bidi-js`、`get-east-asian-width`、`@alcalzone/ansi-tokenize` 等（ANSI 渲染、Markdown、双向/CJK 宽度处理）
- **构建**：仅 `tsc -p tsconfig.json` → `lib/types/`（无 bundler；README 说明 rolldown 的单文件产物留作后续）
- **License**：BSD 3-Clause（"dsh-external", 2026）；但 README 自述 Ink 派生代码属 Anthropic 专有、仅供个人使用、不得公开发布到 registry

## 文件结构概览
```
dsh-cc-tui/
├── src/
│   ├── ink/                    # 近逐字移植的 Ink 核心（renderer/yoga/termio/hooks/components，38+ 文件）
│   ├── native-ts/yoga-layout/  # 纯 TS 的 yoga 布局移植
│   ├── cc/                     # 移植的 CC 工具：markdown.ts(11.8KB)/terminal.ts/figures.ts/spinnerVerbs.ts/cliHighlight.ts
│   ├── components/             # messages/, design-system/, Spinner/, Whale.tsx, bigfont.ts, activityFrames.ts, StreamingMarkdown, WorkingSpinner, ActivityLine, ToolUseLoader
│   ├── screens/                # Chat.tsx(32.8KB)/StatusLine.tsx/StatusMetrics.ts(10KB)
│   ├── bootstrap/state.ts      # 交互期 stub（CC 遥测未移植）
│   ├── utils/                  # CC 应用代码的最小 shim（debug/log/env/intl/semver/sliceAnsi/...）
│   ├── hooks/useBlink.ts       # 移植
│   ├── theme.ts(8.4KB)         # CC 暗色主题，逐字 RGB 复制
│   ├── ui.ts                   # 主题化公共表面（ThemedBox/ThemedText + Ink hooks）
│   ├── channel.ts(43.7KB)      # DSH 适配器：session/event → transcript 行；followup → 发送
│   ├── commands.ts             # 本地 slash 命令表（/clear /compact /help /model /thinking /tokens /resume /exit）
│   ├── history.ts / sessionHistory.ts
│   ├── types/cc.d.ts
│   └── index.tsx(5.9KB)        # Cordis 插件入口：name/inject/Config/apply
├── scripts/
│   ├── build.sh                # tsc 编译；symlink 接入 DSH checkout 的 cordis/dsh-* 依赖
│   ├── smoke.tsx               # 内存流上的 headless 渲染冒烟
│   └── pty-*-probe.mjs         # 端到端 PTY 探针（narrow/cjk/resume/int/meta/keys/multiline/rewind/e2e）
├── cordis.yml                  # 完整可跑示例：cc-tui + llm-deepseek + bash + fs + agent-spine + working-activity + persistence + token-meter + compact
├── install.sh                  # 一键 `pnpm add -w link:$REPO_DIR`，幂等
├── dsh-cc.cmd                  # Windows 启动器（tsx 直跑 scripts/run.ts）
├── README.md(22.6KB)           # 极详尽：定位、DSH 机制映射表、UI 还原清单、已知限制
├── package.json / package-lock.json
├── tsconfig.json / .npmrc / .npmignore / .gitignore
└── LICENSE (BSD-3)
```

## 核心功能与实现要点
1. **Cordis 插件入口（`src/index.tsx`）**：`name='cc-tui'`、`inject=['agents']`；`Config` 经 `schemastery` 描述（`sessionId`/`provider`/`model`/`cwd`/`effort`/`activity`/`activityFrames`/`fullscreen`，默认 `deepseek-official` + `deepseek-v4-flash`）；`apply` 校验 TTY，经 `resolveAgent` 选取/恢复/创建 agent，挂载 `<Chat>` React 树，`render(tree, { exitOnCtrlC: false })`；退出走 `disposeRootAndExit`（先 `ctx.root.fiber.dispose()`，带 5s 兜底定时器后 `process.exit(0)`，注释明示"镜像已删除的 dsh-tui 前门退出语义"——`src/index.tsx:117,143-170`）。

2. **DSH 适配通道（`src/channel.ts`，43.7KB）**：所有行为挂在 DSH 服务/事件流上，**无平行持久化或绕框架执行**（README 明示）。会话转写来自 `agent.session.events` 重放 + 实时 `session/event`；`Agent.followup`/`Agent.cancel` 实现 turn 语义；`sessionPersistence.list()` 供 `/resume`；`ctx.sessions.fork` 边界 + `ctx.agents.create` 实现双击 Esc rewind；`ctx.bash`（`!`/`!!`/git 分支）、`ctx.fs`（`@` 补全）、`ctx.compact.compactNow`（`/compact`）、`ctx.llm.listModels`（`/model`）；服务统一通过 `ctx.get` 在使用时懒查找，缺服务的叶子"优雅降级"而非加载失败。

3. **Claude Code 泄漏源码移植层（`src/ink/`、`src/cc/`、`src/screens/Chat.tsx`）**：FullscreenLayout、StickyPromptHeader、NewMessagesPill、ScrollBox、MarkdownTable、StreamingMarkdown（稳定前缀切分，按 delta 只重解析最后块，无闪烁）、ToolUseLoader、PromptInputFooterSuggestions、Pane/Select/ListItem、SearchBox（Ctrl+R 历史搜索）、TranscriptSearchBar（`/` incsearch）、PromptInputHelpMenu、TokenWarning、AnimatedTerminalTitle——全部标注为从泄漏移植。`extract-maps.mjs` 工具可从泄漏内联 sourcemap 反推原始 TS。

4. **主题与启动画面**：`src/theme.ts` 是 CC 暗色主题的**逐字 RGB 复制**（`claude`、`subtle`、`inactiveShimmer`、`userMessageBackground` 等），经 `ThemedBox`/`ThemedText` 解析；`src/components/Whale.tsx` 用半块 `▀`/`▄` 渲染 24×18 真彩像素鲸鱼精灵，`bigfont.ts` 渲染 `DEEPSEEK`/`HARNESS` 块字体（品牌蓝→冰蓝水平渐变 + 白色流光高亮），`LogoV2.tsx` 渲染冰蓝 `探索未至之境！` 欢迎语带白色扫光。

5. **状态行 / 上下文条 / TPS 仪表（`src/screens/StatusLine.tsx`、`StatusMetrics.ts`）**：三行布局——上 `model · tps · effort · cache% · tokens in→out`（左）+ `git · cwd · title`（右对齐）；中行是 pi-nano-context 风格分段上下文进度条（DeepSeek 蓝调：deep navy→brand blue，按 system/prompt/assistant/thinking/tools 分段，标签随宽度收缩，free 段右对齐 usage）；下行模式提示。TPS 参考 pi-tps-meter：流式时 1/8 cell 实时 gauge `▕███████▋···▏ 47 tps`，结束后变 min-max 归一 sparkline；颜色 ≥50 绿、≥20 黄、<20 红。

6. **工作活动行（`src/components/ActivityLine.tsx` + `activityFrames.ts`）**：当叶子挂载 `dsh-working-activity` 时，消费其 log-only `activity/status` 事件，pi-working-activity 风格动画指示器（28 预设，`config.activityFrames` 默认 `claude`）、白色 shimmer 扫光、上下文压力 ≥80%/95% 时琥珀/红 `⚠ 上下文N%` 前缀（本地由 `lastUsage + contextWindow` 算）；回合结束转 `搞定 ✓ · N 工具 · 想Xs 干Ys` 摘要卡；首轮事件前或 `activity:false` 时仍走经典 CC verb 转轮。

7. **CC 风格交互完整移植**：消息选择模式（Shift+↑）、`!`/`!!` 本地命令（`<bash-stdout>` 信封）、slash 命令建议覆盖层（Tab 补全 / Enter 执行，最新 commit `4de7dd1` 加了唯一匹配直跑规则）、`@` 文件补全（3 层深扫，跳 `node_modules`/`.git`/`dist`/`build`，上限 100）、双击 Esc rewind、Ctrl+R 历史（`~/.dsh-cc/history.jsonl`，dedup 上限 200）、readline 编辑键（`Ctrl+←/→` 词跳、`Ctrl+A/E/U/K/W`）、`Ctrl+C/Esc` 中断（`Agent.cancel({kind:'user'})`）、`Ctrl+L` 重绘、长会话 300 行折叠（Ctrl+E 展开）。

8. **可靠性探针矩阵（`scripts/pty-*-probe.mjs`）**：narrow（80 列布局）、cjk（中文 + 混合宽度输入）、resume（两阶段 boot→消息→退出→选老会话→reboot→验证回放）、int（中断行）、meta（Ctrl+O 元数据）、keys（编辑键）、multiline（多行 + 选择）、rewind（双击 Esc：picker→确认→fork→回后 rewind 一回合）、e2e。构建/冒烟：`sh scripts/build.sh`（tsc → `lib/types/`）、`node --import tsx/esm scripts/smoke.tsx`（内存流 headless 渲染检查）。

## 与 DeepSeek Harness 主仓库的集成点
- **peerDependencies**：`@deepseek-ai/dsh-agent`、`@deepseek-ai/dsh-llm`、`@deepseek-ai/dsh-session`（均 `^0.0.1`）、`cordis ^4.0.0-rc.7`；`engines.dsh: >=0.0.1`
- **服务调用**：统一通过 cordis `ctx.get` 懒查找——`ctx.agents.{create,resume,get,cancel,followup}`、`ctx.sessions.fork`、`ctx.bash`、`ctx.fs`、`ctx.compact.compactNow`、`ctx.llm.listModels`、`ctx.commands`（README 标注为"未来 `ctx.commands` 集成的接缝"，`src/commands.ts` 当前为本地命令表）
- **依赖链接入**：`scripts/build.sh:21-32` 必须能定位 DSH checkout（`$DSH_HOME/source/current` 或 `~/.dsh/source/current` 或 PATH 上 `dsh` 二进制），再 symlink `cordis`/`cosmokit`/`schemastery`/`@deepseek-ai/dsh-*` 进 `node_modules`；`install.sh` 用 `pnpm add -w link:$REPO_DIR` 把本包装进 harness 工作区依赖链（幂等）
- **配套官方插件（`cordis.yml` 示例叶子）**：`dsh-llm-deepseek`、`dsh-subprocess-local`、`dsh-bash-local`、`dsh-fs-local`、`dsh-agent-spine-demo`、`dsh-working-activity`（`publishIntervalMs: 500` 平滑计时）、`dsh-session-persistence-jsonl`（默认 `~/.dsh-cc/sessions/`）、`dsh-session-checkpoint-policy`、`dsh-token-meter`、`dsh-compact-basic`（`thresholdRatio` 默认 0.2 配合 DeepSeek 1M 上下文）
- **架构定位**：客户端驱动前门（与 `dsh-jsonrpc` 同类），不修改 DSH 核心；周围 `cordis.yml` 提供 agent spine、LLM adapter、tool plugins
- **与 TUI 移除/opencode-server 背景的关联**：本仓库正是 DSH 主仓库删除内置 `dsh-tui` 后的**外置承接**——`src/index.tsx:117` 注释"Mirrors the deleted dsh-tui front-door exit semantics"明确指向已删除的内置 TUI；用 Claude Code 风格 UI（移植的 Ink 核心 + CC 暗色主题 + CC 组件）填补该空缺，作为官方外置 cordis 插件分发

## 亮点与风险
**亮点**
- UI 还原度极高：CC 暗色主题逐字 RGB、Ink 核心近逐字移植、像素鲸鱼启动画面、`DEEPSEEK`/`HARNESS` 块字体品牌渐变，DSH 侧无对应物时自己写
- 架构干净：所有行为挂 DSH 服务、无平行持久化/执行；服务懒查找、缺服务优雅降级；tsc-only 构建无 bundler
- 工程严谨：`scripts/pty-*-probe.mjs` 九类 PTY 端到端探针；smoke headless 渲染检查；`install.sh` 幂等；README 22.6KB 含完整 DSH 机制映射表与已知 v0 限制清单
- 中文/品牌细节到位：`探索未至之境！` 欢迎语、`搞定 ✓ · N 工具 · 想Xs 干Ys` 摘要、`⚠ 上下文N%` 压力提示

**风险**
- **法律/许可冲突（高）**：`README.md:7-9` 自述 "Personal-use port. The Ink-derived code is proprietary to Anthropic and has no open-source license; do not publish this package in a public registry."——Ink 核心、CC 暗色主题、CC 组件均为 Anthropic 专有；但仓库带 BSD-3 LICENSE 且发到公开 GitHub org，与"个人用、禁公开"声明矛盾。`package.json` 虽 `private:true`，公开仓库本身即分发
- **包名不一致**：`package.json:2` name 为 `@dsh-external/dsh-cc-tui`，但 `README.md:1`、`cordis.yml:4` 自称 `@deepseek-ai/dsh-cc-tui`；`install.sh` 用 `@dsh-external/dsh-cc-tui`——三处口径不统一
- **路径泄露**：`dsh-cc.cmd:8` 硬编码 `WORKSPACE=D:\code\projects\test-ccch1mneyyy`、`dsh-cc.cmd:18` `D:\node\node.exe`——泄漏原开发机绝对路径（虽然看起来是匿名化测试名）
- **构建依赖外部 DSH checkout**：`scripts/build.sh:21-32` 找不到 `$DSH_HOME/source/current`/`~/.dsh/source/current`/PATH `dsh` 即直接失败；node_modules 经 symlink 接入 checkout，平台敏感（README 警告 WSL 跑 `pnpm install` 会把 Windows-only symlink 替换掉）
- **退出非优雅**：`src/index.tsx:143-170` `disposeRootAndExit` 5s 兜底后直接 `process.exit(0)`；README "Known Limitations (v0)" 自述"TUI exit calls `process.exit(0)` directly; graceful agent flush is deferred"
- **peer dep 绑定松散**：`^0.0.1` 的 DSH 0.0.1 是 rc 期，agent/llm/session API 易变；`/model` 切换需重启（"agent 的 model 创建时固定"）
- **个人用意图 vs 公开分发**：README 反复强调"个人用、勿公开发布"，但仓库处于公开 org、带 BSD LICENSE、有 cordis.yml 完整示例和 `install.sh`——意图与现状割裂

## 维护状态
- 浅 clone（`--depth 1`）仅可见 1 commit：`4de7dd1 feat: slash menu Enter runs the selected command (unique-match rule for ConPTY line input), single Esc closes the menu; /resume picker scrolls (8-row window + more markers)`，HEAD 在 `main`/`origin/main`
- `package.json` version `0.1.0`；README 自述 v0；功能完成度高（UI 还原、9 类 PTY 探针、完整文档），处于活跃开发期
- LICENSE `Copyright (c) 2026, dsh-external`，与调研日期同期

## 备注
- 默认 model `deepseek-v4-flash`、provider `deepseek-official`（`src/index.tsx:62-63`、`cordis.yml:5`）
- 本地状态遵循 CC 自身约定（DSH 无对应物）：输入历史 `~/.dsh-cc/history.jsonl`、会话日志 `~/.dsh-cc/sessions/`、`/resume` 启动交接文件 `~/.dsh-cc/resume.txt`
- 环境变量：`DEEPSEEK_API_KEY`（必需）、`DEEPSEEK_BASE_URL`、`DSH_CC_RESUME_SESSION`（`dsh-cc --resume` 注入）、`DSH_CC_SESSION_ROOT`、`CC_TUI_PERSONA`、`CC_TUI_COMPACT_RATIO`/`CC_TUI_COMPACT_RETAIN`、`CC_TUI_DEBUG`、`CC_TUI_DISABLE_MOUSE`
- `dsh-cc.cmd` 引用 `packages\ui\cc-tui\scripts\run.ts`——暗示本仓库最初是 DSH 主仓库 `packages/ui/cc-tui/` 工作区包，后外置迁出（与"dsh-tui 删除"背景一致）
- 与 `dsh-working-activity`、`pi-tps-meter`、`pi-nano-context`、`pi-working-activity` 等周边 UI 扩展有明确视觉/数据对接（README 状态行章节）
