# Awesome DSH Plugins

社区维护的 DeepSeek Harness（DSH）插件目录与兼容性证据索引。

*A community-maintained catalog and compatibility evidence index for DeepSeek Harness plugins.*

[浏览分类目录](PLUGINS.md) · [查看最新快照](#当前生态快照) · [浏览历史报告](reports/) · [查看变更](CHANGELOG.md) · [提交插件](#提交插件)

> [!IMPORTANT]
> **收录不等于兼容，静态检查不等于运行可用，运行可用也不等于安全审计。**
> 本仓库提供可追溯的筛选信号，不代表 DSH 官方背书。安装第三方插件前，请检查插件源码、权限、依赖、许可证及测试日期。

## 从这里开始

| 你的目标 | 建议入口 |
|---|---|
| 按用途找一个插件 | [分类登记清单](PLUGINS.md) |
| 浏览自动发现的全部仓库 | 从[当前生态快照](#当前生态快照)进入当日完整索引 |
| 判断某插件是否需要适配当前 mainline | 从[当前生态快照](#当前生态快照)进入当日静态矩阵 |
| 查看真实加载与工具调用结果 | 从[当前生态快照](#当前生态快照)进入当日运行实测 |
| 了解最近发生了什么 | [CHANGELOG](CHANGELOG.md) |
| 登记或维护一个插件 | [开发者指南](#给插件开发者) |
| 维护本雷达 | [自动化 SOP](docs/SOP.md) |

## 分类目录

<!-- AUTO:catalog:START -->
> 分类参考 [dsh-external/hub](https://github.com/dsh-external/hub)（catalog v0.1）。每类显示前 10 条，其余折叠；「单插件」默认展开。

<details>
<summary>💬 社区（4）</summary>

| 插件 | 说明 |
|---|---|
| [group-chat-diary](https://github.com/dsh-external/group-chat-diary) | DSH 内测群聊日记归档 |
| [issues](https://github.com/dsh-external/issues) | 内测时遇到的问题 |
| [onboarding](https://github.com/dsh-external/onboarding) | Private onboarding hub for DeepSeek Harness beta |
| [review-panel](https://github.com/dsh-external/review-panel) | Internal beta review panel for DeepSeek Harness |
</details>

<details>
<summary>🎓 技能（11）</summary>

| 插件 | 说明 |
|---|---|
| [browser4-dsh](https://github.com/dsh-external/browser4-dsh) | Browser4 — an AI-native browser engine for auton |
| [deep-standard-skill](https://github.com/dsh-external/deep-standard-skill) | 把工程规范从没人读的文档变成会拒绝违规的程序 |
| [dsh-find-plugins](https://github.com/dsh-external/dsh-find-plugins) | null |
| [dsh-humanize](https://github.com/dsh-external/dsh-humanize) | null |
| [dsh-issue-filer](https://github.com/dsh-external/dsh-issue-filer) | DSH 提 issue 技能：向 dsh-external/issues 自动查重、格式化并创建 |
| [dsh-issue-like-skill](https://github.com/dsh-external/dsh-issue-like-skill) | dsh-issue-like skill: react 👍 to DSH issues on d |
| [dsh-plugin-dev](https://github.com/dsh-external/dsh-plugin-dev) | DSH 插件开发踩坑与做法档案（skill + 文档）：cordis 双副本、tsconfig  |
| [dsh-plugin-skills](https://github.com/dsh-external/dsh-plugin-skills) | Agent skills for building and testing DeepSeek H |
| [dsh-reuse-first](https://github.com/dsh-external/dsh-reuse-first) | null |
| [dsh-session-repair-skill](https://github.com/dsh-external/dsh-session-repair-skill) | Detect and repair corrupted dsh session history  |

<details>
<summary>展开全部（剩余 1 条）</summary>

| 插件 | 说明 |
|---|---|
| [dsh-skill-session-recovery](https://github.com/dsh-external/dsh-skill-session-recovery) | DSH 会话丢失事故的定位/无损修复/安全重启 skill：诊断 corrupt session |
</details>
</details>

<details open>
<summary>🔌 单插件（180）</summary>

| 插件 | 说明 |
|---|---|
| [7d7d](https://github.com/dsh-external/7d7d) | 7k7d 游戏门户 —— 7k7k 风格 DSH 小游戏平台：模型生成/上传 HTML5 与 F |
| [chat-width](https://github.com/dsh-external/chat-width) | 自由调节正文和输入框的展示宽度 |
| [context-doctor](https://github.com/dsh-external/context-doctor) | DSH 上下文注入审计插件：统计 AGENTS.md 指令链/技能目录/工具 schema 的  |
| [cross-harness-cite](https://github.com/dsh-external/cross-harness-cite) | 支持跨Harness引用codex/claude code的历史对话 |
| [deepseek-manners](https://github.com/dsh-external/deepseek-manners) | DSH 插件：给每次消息后注入感谢语（deepseek-manners） |
| [distill](https://github.com/dsh-external/distill) | Marisa 插件：自动对话蒸馏（后台 subagent 反省 + 技能 create/upda |
| [dsh-101](https://github.com/dsh-external/dsh-101) | DSH 文档阅读模式 |
| [dsh-a2a](https://github.com/dsh-external/dsh-a2a) | Agent2Agent mesh for the Harness |
| [dsh-acp](https://github.com/dsh-external/dsh-acp) | Client-neutral ACP adapter for DeepSeek Harness |
| [dsh-activity-plugin](https://github.com/dsh-external/dsh-activity-plugin) | null |

<details>
<summary>展开全部（剩余 170 条）</summary>

| 插件 | 说明 |
|---|---|
| [dsh-ads](https://github.com/dsh-external/dsh-ads) | 是兄弟就来蹬我！DSH Web UI 广告：2005 年中文站点风格的侧栏广告 / 对话内信息流 |
| [dsh-advisor](https://github.com/dsh-external/dsh-advisor) | Advisor - Pair a second model that passively rev |
| [dsh-agent-budget](https://github.com/dsh-external/dsh-agent-budget) | Native Harness agent-tree token budget plugin |
| [dsh-agent-rp](https://github.com/dsh-external/dsh-agent-rp) | SillyTavern migration and next-generation Agent  |
| [dsh-aigc-canvas](https://github.com/dsh-external/dsh-aigc-canvas) | null |
| [dsh-alphasolve](https://github.com/dsh-external/dsh-alphasolve) | Session-scoped AlphaSolve workflow for DeepSeek  |
| [dsh-annotation](https://github.com/dsh-external/dsh-annotation) | DSH Web 选中批注插件：选文字→批注→回车随消息发送；气泡隐藏批注块（零闪烁）；回复按 A |
| [dsh-anti-ads](https://github.com/dsh-external/dsh-anti-ads) | null |
| [dsh-artifact](https://github.com/dsh-external/dsh-artifact) | dsh 插件：文件交付协议——send_artifact 工具经 tool/result met |
| [dsh-auto-approval](https://github.com/dsh-external/dsh-auto-approval) | null |
| [dsh-auto-blame](https://github.com/dsh-external/dsh-auto-blame) | null |
| [dsh-auto-chess](https://github.com/dsh-external/dsh-auto-chess) | DSH Web里的自走棋插件：人机对战或双AI对弈 |
| [dsh-bash-encoding](https://github.com/dsh-external/dsh-bash-encoding) | DSH bash 输出编码自动识别插件：替换 ctx.bash，自管 spawn 收集原始字节， |
| [DSH-better-sidebar](https://github.com/dsh-external/DSH-better-sidebar) | 一个侧边栏的完整工作台，支持三方接入/文件渲染编辑/终端/Git/子代理，一个面板全部搞定 |
| [dsh-better-sidebar-plugin-office](https://github.com/dsh-external/dsh-better-sidebar-plugin-office) | null |
| [dsh-browser-bridge](https://github.com/dsh-external/dsh-browser-bridge) | Prompt-scoped bridge between DSH and explicitly  |
| [dsh-browser-panel](https://github.com/dsh-external/dsh-browser-panel) | WebUI 内嵌完整有头浏览器视图插件：模型在 DSH WebUI 内实时操控真实浏览器，用户可 |
| [dsh-cc-connect](https://github.com/dsh-external/dsh-cc-connect) | 通过cc connect远程使用dsh |
| [dsh-cc-tui](https://github.com/dsh-external/dsh-cc-tui) | Claude Code 风格全屏交互终端插件：像素鲸鱼顶栏、流光大字、思考流式展开、双击 Esc |
| [dsh-chat](https://github.com/dsh-external/dsh-chat) | DSH 对话插件：对话视图增强 |
| [dsh-chat-thumb](https://github.com/dsh-external/dsh-chat-thumb) | Chat缩略图 |
| [dsh-checkpoint](https://github.com/dsh-external/dsh-checkpoint) | Mark an exploration start in the session; pairs  |
| [dsh-client-ui-plan-execute](https://github.com/dsh-external/dsh-client-ui-plan-execute) | DSH Web 设置页「规划/执行模型」设置行插件：编辑 dsh-plan-execute 双模 |
| [dsh-club](https://github.com/dsh-external/dsh-club) | DSH 俱乐部 — DeepSeek Harness 内测用户排行榜(每日自动采集) |
| [dsh-code-map](https://github.com/dsh-external/dsh-code-map) | DSH 代码地图插件：symbol 索引 / 文档符号 / 调用层级 / 继承树——给模型补上「 |
| [dsh-codex-bridge](https://github.com/dsh-external/dsh-codex-bridge) | null |
| [dsh-computer-use](https://github.com/dsh-external/dsh-computer-use) | Accessibility-first macOS Computer Use bundle fo |
| [dsh-context7](https://github.com/dsh-external/dsh-context7) | Reserved DSH integration for Context7: current,  |
| [dsh-custom-css](https://github.com/dsh-external/dsh-custom-css) | null |
| [dsh-cyber-sec](https://github.com/dsh-external/dsh-cyber-sec) | dsh 生态授权渗透测试 profile bundle：容器化 bash 执行（可降级本机）+  |
| [dsh-d399](https://github.com/dsh-external/dsh-d399) | 深夜寂寞？来玩 D399 — 当模型生成时弹出小游戏菜单（wordle / 消消乐，可拓展游戏注 |
| [dsh-data-agent](https://github.com/dsh-external/dsh-data-agent) | 让AI帮你连数据库、写SQL的DSH插件 |
| [dsh-deep-research](https://github.com/dsh-external/dsh-deep-research) | Adaptive deep-research orchestrator plugin for D |
| [dsh-deeplink](https://github.com/dsh-external/dsh-deeplink) | DSH WebUI 深链插件：?session=/?workspace= 直接打开指定项目对话 |
| [dsh-deepresearch](https://github.com/dsh-external/dsh-deepresearch) | null |
| [dsh-design](https://github.com/dsh-external/dsh-design) | DSH-native Web/UI design Agent bundle for Create |
| [dsh-diff-viewer](https://github.com/dsh-external/dsh-diff-viewer) | DSH Web GUI PiUI-style diff viewer plugin: repla |
| [dsh-drag-and-drop](https://github.com/dsh-external/dsh-drag-and-drop) | 为 DSH Web UI 增加跨平台文件拖拽与原始路径插入能力，无需复制文件 |
| [dsh-easy-ctx-manager](https://github.com/dsh-external/dsh-easy-ctx-manager) | 一个适用于dsh的上下文管理插件，包含上下文节省，注意力优化，压缩档案馆等功能 |
| [dsh-emoji](https://github.com/dsh-external/dsh-emoji) | null |
| [dsh-engram-relay](https://github.com/dsh-external/dsh-engram-relay) | 外置 engram 转接模型插件：内置 <1B 模型（transformers.js/ONNX） |
| [dsh-evolve](https://github.com/dsh-external/dsh-evolve) | 自进化插件：agent 在 session 内随对话给自己长出/剪掉能力 —— evolve_a |
| [dsh-explain](https://github.com/dsh-external/dsh-explain) | DSH 学习模式插件（WIP）：开关打开后，agent 工作时实时讲解涉及的知识点，用于用户学习 |
| [dsh-feishu-notify](https://github.com/dsh-external/dsh-feishu-notify) | 为dsh新增飞书的通知：会话结束/需要等待输入 |
| [dsh-focus-chat](https://github.com/dsh-external/dsh-focus-chat) | 一个聚焦对话视图插件：提供对话的精简阅读界面——工具调用折叠成摘要行、回合折叠、Think 行 |
| [dsh-genui](https://github.com/dsh-external/dsh-genui) | DSH的生成式UI能力,不断更新中,欢迎issue&pr! |
| [dsh-gh-bridge](https://github.com/dsh-external/dsh-gh-bridge) | DSH plugin: bridge the macOS Keychain GitHub tok |
| [dsh-git-identity](https://github.com/dsh-external/dsh-git-identity) | DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub  |
| [dsh-gomoku](https://github.com/dsh-external/dsh-gomoku) | 在DSH中与AI下五子棋，也可以让AI对局，看哪个AI棋力更强 |
| [dsh-grok-tui](https://github.com/dsh-external/dsh-grok-tui) | Use dsh via grok-build's TUI. |
| [dsh-input-history](https://github.com/dsh-external/dsh-input-history) | null |
| [dsh-inspect](https://github.com/dsh-external/dsh-inspect) | 发现问题(checkup) → 修复交付(fix) → 质量复查(review) 的对抗式闭环插 |
| [dsh-interpreters](https://github.com/dsh-external/dsh-interpreters) | null |
| [dsh-kb-sieve](https://github.com/dsh-external/dsh-kb-sieve) | DSH knowledge-base plugin: build audit-able KB p |
| [dsh-kimi-bridge](https://github.com/dsh-external/dsh-kimi-bridge) | null |
| [dsh-kimi-browser](https://github.com/dsh-external/dsh-kimi-browser) | DSH 插件：经 Kimi WebBridge 让模型驱动你的真实浏览器——13 个 webbr |
| [dsh-latex](https://github.com/dsh-external/dsh-latex) | DSH LaTeX 插件：agent 写 LaTeX 文档 → 一键编译 PDF（复用本机 Wi |
| [dsh-lazyfish](https://github.com/dsh-external/dsh-lazyfish) | DSH 右侧摸鱼面板：多源信息流 + B站播放器 + 任务联动（Lazy Fish = 摸鱼） |
| [dsh-live-stats](https://github.com/dsh-external/dsh-live-stats) | Live input/output token estimates and generation |
| [dsh-llm-fallbacks](https://github.com/dsh-external/dsh-llm-fallbacks) | An dsh plugin for role-based LLM retry&fallback  |
| [dsh-loop](https://github.com/dsh-external/dsh-loop) | DSH 插件：定时循环（/loop 命令 + loop 工具 + 活动状态条） |
| [dsh-meme](https://github.com/dsh-external/dsh-meme) | 让 agent 在回复正文内联表情包：inject_meme 工具 + httpServer 图 |
| [dsh-memory](https://github.com/dsh-external/dsh-memory) | DSH 记忆插件：跨会话长期记忆与自我进化 |
| [dsh-memory-evolve](https://github.com/dsh-external/dsh-memory-evolve) | 为 DeepSeek Harness 带来「跨会话长期记忆 + 后台自我进化」能力的纯插件实现： |
| [dsh-message-edit](https://github.com/dsh-external/dsh-message-edit) | DSH plugin: branch-based message editing, reroll |
| [dsh-mineru](https://github.com/dsh-external/dsh-mineru) | DSH plugin exposing MineRU document parsing tool |
| [dsh-minigames](https://github.com/dsh-external/dsh-minigames) | DSH Web UI 右侧小游戏面板：恐龙跳一跳 / 俄罗斯方块 / 坦克大战(AI)，可扩展游 |
| [dsh-mnemon](https://github.com/dsh-external/dsh-mnemon) | Mnemonic layer for DSH (integration with mnemon- |
| [dsh-mobile](https://github.com/dsh-external/dsh-mobile) | null |
| [dsh-mobileweb-adapter](https://github.com/dsh-external/dsh-mobileweb-adapter) | DSH 手机 Web 适配器 —— 让 DeepSeek Harness Web GUI 在手机 |
| [dsh-multica-runtime](https://github.com/dsh-external/dsh-multica-runtime) | 支持在 Multica 上使用 DSH 作为 runtime |
| [dsh-multimedia-webui-input](https://github.com/dsh-external/dsh-multimedia-webui-input) | Community multimedia file and folder input for D |
| [dsh-music-player](https://github.com/dsh-external/dsh-music-player) | null |
| [dsh-navbar](https://github.com/dsh-external/dsh-navbar) | DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息） |
| [dsh-notebooks](https://github.com/dsh-external/dsh-notebooks) | null |
| [dsh-nowledge-mem](https://github.com/dsh-external/dsh-nowledge-mem) | DSH plugin for Nowledge Mem™ |
| [dsh-office](https://github.com/dsh-external/dsh-office) | null |
| [dsh-opencode-server](https://github.com/dsh-external/dsh-opencode-server) | 把dsh的tui换成opencode！本插件为dsh web实现了opencode api的必要 |
| [dsh-openmaic](https://github.com/dsh-external/dsh-openmaic) | Generate OpenMAIC classrooms (interactive AI les |
| [dsh-openpencil](https://github.com/dsh-external/dsh-openpencil) | OpenPencil design preview and editing plugin for |
| [dsh-paseo](https://github.com/dsh-external/dsh-paseo) | DSH 的paseo插件扩展支持 |
| [dsh-paste-input](https://github.com/dsh-external/dsh-paste-input) | DSH WebUI 文件输入增强：Ctrl+V 粘贴（带首次告知弹窗）+ 拖拽 + 选择文件，发 |
| [dsh-pet](https://github.com/dsh-external/dsh-pet) | 🐋 DSH 桌宠：悬浮桌面的 DeepSeek 小鲸鱼，不打开 DSH 也能实时感知会话状态（需 |
| [dsh-pi-adapter](https://github.com/dsh-external/dsh-pi-adapter) | Run pi coding-agent extensions (ExtensionAPI) in |
| [dsh-plan-execute](https://github.com/dsh-external/dsh-plan-execute) | DSH plan/execute 双模型路由插件：plan 模式用规划模型（推理型），批准后自动 |
| [dsh-plugin-check](https://github.com/dsh-external/dsh-plugin-check) | DSH 插件健康检查工具：扫描插件仓库的清单协议 / patch 格式 / 构建陷阱 / hub |
| [dsh-prompt-studio](https://github.com/dsh-external/dsh-prompt-studio) | DSH plugin: edit user and built-in system-prompt |
| [dsh-pty-windows](https://github.com/dsh-external/dsh-pty-windows) | Marisa 插件：Windows PTY 进程检查器（PowerShell CIM 枚举 +  |
| [dsh-qq2006](https://github.com/dsh-external/dsh-qq2006) | DSH (DeepSeek Harness) QQ2006 skin plugin: theme |
| [dsh-question-collapse](https://github.com/dsh-external/dsh-question-collapse) | DSH WebUI 提问栏折叠插件：保留问题标题与取消按钮，展开后保留未提交草稿 |
| [dsh-rewind](https://github.com/dsh-external/dsh-rewind) | Fold everything since the last checkpoint mark i |
| [dsh-save-intp](https://github.com/dsh-external/dsh-save-intp) | null |
| [dsh-scout](https://github.com/dsh-external/dsh-scout) | null |
| [dsh-security-audit](https://github.com/dsh-external/dsh-security-audit) | DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告 |
| [dsh-selection-chat](https://github.com/dsh-external/dsh-selection-chat) | DSH WebUI plugin: select conversation text → add |
| [dsh-self-control-guard](https://github.com/dsh-external/dsh-self-control-guard) | DSH self-control guard: intercept host-kill atte |
| [dsh-session-cluster](https://github.com/dsh-external/dsh-session-cluster) | Same-machine cross-session messaging for DeepSee |
| [dsh-session-health](https://github.com/dsh-external/dsh-session-health) | DSH 会话健康检查插件：多帧 zstd 会话文件的帧级扫描诊断（torn/损坏/空会话检测）， |
| [dsh-session-hub](https://github.com/dsh-external/dsh-session-hub) | 跨工具会话互通插件：把 opencode / Claude Code / Antigravity |
| [dsh-session-search](https://github.com/dsh-external/dsh-session-search) | 跨工具会话全文搜索插件（dsh/codex/claude/pi/opencode）— Cross |
| [dsh-sfw](https://github.com/dsh-external/dsh-sfw) | 为了防止你的好bro/同事看到内测dsh然后：？这是什么 |
| [dsh-share](https://github.com/dsh-external/dsh-share) | dsh对话分享插件 |
| [dsh-shell-windows](https://github.com/dsh-external/dsh-shell-windows) | Marisa 插件：Windows PowerShell 外壳适配器（ctx.shell，win |
| [dsh-side-panel](https://github.com/dsh-external/dsh-side-panel) | DSH 侧边栏，集成文件浏览器、终端和 Git 审查，方便预览文件 |
| [dsh-sidechain](https://github.com/dsh-external/dsh-sidechain) | DSH 侧会话插件：/side 持续性侧会话（Codex 风格）与 /btw 一次性侧问（Cla |
| [dsh-skill-stats](https://github.com/dsh-external/dsh-skill-stats) | 技能调用统计插件：历史回放 + 实时订阅，统计每个技能的调用次数、会话分布与调用时间线；会话 T |
| [dsh-skills-manager](https://github.com/dsh-external/dsh-skills-manager) | 在webui中方便的列出、禁用启用、编辑skills |
| [dsh-sleep](https://github.com/dsh-external/dsh-sleep) | null |
| [dsh-slice-agent-loop](https://github.com/dsh-external/dsh-slice-agent-loop) | A drop-in DeepSeek Harness agent loop whose cont |
| [dsh-sonar](https://github.com/dsh-external/dsh-sonar) | null |
| [dsh-spec-kit](https://github.com/dsh-external/dsh-spec-kit) | Reserved DSH integration for GitHub Spec Kit: sp |
| [dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | null |
| [dsh-spur](https://github.com/dsh-external/dsh-spur) | null |
| [dsh-stickers](https://github.com/dsh-external/dsh-stickers) | DSH WebUI sticker plugin for bidirectional user  |
| [dsh-stock-market](https://github.com/dsh-external/dsh-stock-market) | 有效解决了写代码的时候账户不能同时亏钱的BUG |
| [dsh-subagent-tree](https://github.com/dsh-external/dsh-subagent-tree) | DSH 工作区侧栏树子代理分支插件（会话行扩展 hole）— 非官方，版权归作者 |
| [dsh-suggested-replies](https://github.com/dsh-external/dsh-suggested-replies) | DSH Web 预测回复插件：AI 回复后在输入框上方生成可点击填入草稿的下一步消息候选 |
| [dsh-super-injector](https://github.com/dsh-external/dsh-super-injector) | null |
| [dsh-superpowers](https://github.com/dsh-external/dsh-superpowers) | Reserved DSH integration for Superpowers: reusab |
| [dsh-task-status](https://github.com/dsh-external/dsh-task-status) | DSH 插件：后台任务状态条（对话页任务进度 + 实时输出 tail） |
| [dsh-tavern-plugin](https://github.com/dsh-external/dsh-tavern-plugin) | 小酒馆 (Tavern) plugin — character cards, chat, mem |
| [dsh-teamwork](https://github.com/dsh-external/dsh-teamwork) | null |
| [dsh-tool-calculator](https://github.com/dsh-external/dsh-tool-calculator) | DSH 计算器工具插件：安全的数学表达式求值器，零依赖递归下降解析器 |
| [dsh-tool-csv](https://github.com/dsh-external/dsh-tool-csv) | DSH CSV 数据工具插件：解析/查询/统计/转换 CSV 文本（RFC 4180），零依赖状 |
| [dsh-tool-diff](https://github.com/dsh-external/dsh-tool-diff) | DSH Diff 工具插件：文本/JSON/CSV/Markdown 结构化比较与 unifie |
| [dsh-tool-encoding](https://github.com/dsh-external/dsh-tool-encoding) | DSH 编码/哈希工具插件：base64/base64url/url/hex 编解码、md5/s |
| [dsh-tool-json](https://github.com/dsh-external/dsh-tool-json) | DSH JSON 查询工具插件：JMESPath 子集查询，零依赖递归下降解析器 |
| [dsh-tool-markdown](https://github.com/dsh-external/dsh-tool-markdown) | DSH Markdown 工具插件：HTML↔Markdown 转换、GFM 表格规范化、目录生 |
| [dsh-tool-regex](https://github.com/dsh-external/dsh-tool-regex) | DSH 正则工具插件：测试匹配/提取捕获组/安全替换/静态解释正则（不执行代码），零依赖，注册  |
| [dsh-tool-schema](https://github.com/dsh-external/dsh-tool-schema) | DSH JSON Schema 验证工具插件：validate/paths/explain/no |
| [dsh-tool-search](https://github.com/dsh-external/dsh-tool-search) | Per-agent on-demand tool discovery and progressi |
| [dsh-tool-stat](https://github.com/dsh-external/dsh-tool-stat) | DSH 统计工具插件：描述统计/百分位数/频数分布/相关性，零依赖纯函数确定性 |
| [dsh-tool-time](https://github.com/dsh-external/dsh-tool-time) | DSH 时间工具插件：严格 ISO 8601 解析、IANA 时区转换、UTC 日历运算、固定时 |
| [dsh-tps](https://github.com/dsh-external/dsh-tps) | 只是一个 tps 插件 |
| [dsh-track](https://github.com/dsh-external/dsh-track) | DSH Track Bridge 插件：嵌入式任务管理引擎——决策点协议、念头捕获墙、Linea |
| [dsh-travel-plugin](https://github.com/dsh-external/dsh-travel-plugin) | 旅行小插件 |
| [dsh-tui-front-door](https://github.com/dsh-external/dsh-tui-front-door) | Standalone dsh TUI front door: ink REPL + keybin |
| [dsh-turn-navigator](https://github.com/dsh-external/dsh-turn-navigator) | Private DSH Web turn navigation plugin |
| [dsh-turn-rewind](https://github.com/dsh-external/dsh-turn-rewind) | Turn Rewind for DSH — rewind conversation and wo |
| [dsh-ui-progress](https://github.com/dsh-external/dsh-ui-progress) | DSH Web UI 任务进度插件：report_progress 工具动画卡片 + 输入框停靠 |
| [dsh-ui-whale](https://github.com/dsh-external/dsh-ui-whale) | 【求⭐】🐋DSH Web UI 全手绘像素鲸鱼伙伴插件：会话标题栏常驻，平时眨眼/偶尔摆尾/动胸 |
| [DSH-UI4A](https://github.com/dsh-external/DSH-UI4A) | UI4A(UI for Agent)的DSH实现 https://macaron.im/blog |
| [dsh-ultra-ui](https://github.com/dsh-external/dsh-ultra-ui) | null |
| [dsh-vision](https://github.com/dsh-external/dsh-vision) | dsh 插件：给纯文本 DeepSeek 加视觉——view_image 工具桥接任意 Open |
| [dsh-vision-toolkit](https://github.com/dsh-external/dsh-vision-toolkit) | DeepSeek Harness-native integration for agent-vi |
| [dsh-visualize](https://github.com/dsh-external/dsh-visualize) | DSH 对话内生成式 UI 插件：模型把交互式 HTML 卡片直接画进会话流——visualiz |
| [dsh-voice-chat](https://github.com/dsh-external/dsh-voice-chat) | 实时语音对话插件：WebUI 内语音输入/输出，边说话边编程（vibe coding），0 打字 |
| [dsh-web](https://github.com/dsh-external/dsh-web) | DSH Web 插件：Web UI 增强 |
| [dsh-web-archive](https://github.com/dsh-external/dsh-web-archive) | 折叠对话当中众多的“无用消息”，例如Think、Bash等 |
| [dsh-web-panel](https://github.com/dsh-external/dsh-web-panel) | DSH Web UI 内嵌交互式终端插件（dsh-external/issues#111）：支持 |
| [dsh-web-review](https://github.com/dsh-external/dsh-web-review) | null |
| [dsh-web-ui-notify](https://github.com/dsh-external/dsh-web-ui-notify) | 为 DSH 增加桌面通知提醒 |
| [dsh-web-workflow-visualizer](https://github.com/dsh-external/dsh-web-workflow-visualizer) | DSH Web GUI 的 Workflow 可视化 + 图工程插件：多 agent 动态工作流 |
| [dsh-webbridge](https://github.com/dsh-external/dsh-webbridge) | DSH 结合 Kimi WebBridge |
| [dsh-working-activity](https://github.com/dsh-external/dsh-working-activity) | DSH 实时模型工作状态行：俏皮思考文案、运行中的工具、回合总结、自我叙述（⏵）— 用于 TUI |
| [dshx-update-check](https://github.com/dsh-external/dshx-update-check) | marisa#1 提案原型：commit SHA 对比检测插件更新（只检测不自动更新） |
| [ego-browser](https://github.com/dsh-external/ego-browser) | DSH（DeepSeek Harness）插件：把 ego-lite 浏览器（给 AI Agen |
| [ex-setting](https://github.com/dsh-external/ex-setting) | DSH的设置扩展 |
| [mstar-workflow](https://github.com/dsh-external/mstar-workflow) | A Skill-driven Harness/Loop Engineering Workflow |
| [session-chatlog](https://github.com/dsh-external/session-chatlog) | Marisa 插件：会话聊天记录读取工具（session_list / session_read |
| [session-persistence-rdb](https://github.com/dsh-external/session-persistence-rdb) | session 关系型数据库持久化 |
| [session-teleport](https://github.com/dsh-external/session-teleport) | PostgreSQL-backed single-writer session handoff  |
| [show-bash-command](https://github.com/dsh-external/show-bash-command) | 显示命令具体内容而不是描述 |
| [turtle-ui](https://github.com/dsh-external/turtle-ui) | fine |
| [ui-status-label](https://github.com/dsh-external/ui-status-label) | 把你鲸鱼娘思考时的 deep diving 自定义成任意你想要的样子 |
| [whale-girl](https://github.com/dsh-external/whale-girl) | DSH Web GUI 桌面宠物插件（QQ 宠物形态）：右下角悬浮、可拖拽/投喂/玩耍的积累型伙 |
| [ya-workspace-sidebar](https://github.com/dsh-external/ya-workspace-sidebar) | null |
| [yet-another-subagent](https://github.com/dsh-external/yet-another-subagent) | null |
| [zotero-harvest](https://github.com/dsh-external/zotero-harvest) | Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAl |
| [zotero-wave-rag](https://github.com/dsh-external/zotero-wave-rag) | 面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件 |
</details>
</details>

<details>
<summary>🧰 插件集（23）</summary>

| 插件 | 说明 |
|---|---|
| [dsh-agent-session-sources](https://github.com/dsh-external/dsh-agent-session-sources) | This repository contains the provider-neutral ag |
| [dsh-cordis-examples](https://github.com/dsh-external/dsh-cordis-examples) | Minimal native DSH/Cordis extension examples |
| [dsh-cordis-rocks](https://github.com/dsh-external/dsh-cordis-rocks) | 16-chapter companion tutorial for reversible Cor |
| [dsh-cot-summary](https://github.com/dsh-external/dsh-cot-summary) | 啊哈哈哈哈，最后一天了，我要总结cot！ |
| [dsh-deep-whale](https://github.com/dsh-external/dsh-deep-whale) | DSH Web 鲸娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA |
| [dsh-deepcel](https://github.com/dsh-external/dsh-deepcel) | Deepcel spreadsheet-workbook skin for DeepSeek H |
| [dsh-edu](https://github.com/dsh-external/dsh-edu) | 教育版 DeepSeek Harness（ohmydsh 式）：7 个教育 bundle 插件  |
| [dsh-github-integration](https://github.com/dsh-external/dsh-github-integration) | DSH GitHub integration plugin |
| [dsh-harness-ops](https://github.com/dsh-external/dsh-harness-ops) | DSH 运维工具箱：升级、重启、故障都不用操心 |
| [dsh-mega](https://github.com/dsh-external/dsh-mega) | dsh 整合包：精选插件一行安装（loop / task-status / plugin-con |

<details>
<summary>展开全部（剩余 13 条）</summary>

| 插件 | 说明 |
|---|---|
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | DSH 本地插件集：tool-failure-guard / commit-gate / com |
| [dsh-plugin-guide](https://github.com/dsh-external/dsh-plugin-guide) | DSH 插件开发指南：从零到精通 |
| [dsh-plus](https://github.com/dsh-external/dsh-plus) | DeepSeek Harness Plus: curated plugin manifest a |
| [dsh-profile-bundle-example](https://github.com/dsh-external/dsh-profile-bundle-example) | Minimal script-free Profile Bundle example for D |
| [dsh-serenity-plugin](https://github.com/dsh-external/dsh-serenity-plugin) | dsh version serenity-plugin |
| [dsh-skins](https://github.com/dsh-external/dsh-skins) | DSH Web 换肤插件仓库：官方 ThemeService 第三方皮肤（token + AI  |
| [dsh-tool-browser](https://github.com/dsh-external/dsh-tool-browser) | Private toybox snapshot of the DeepSeek Harness  |
| [dsh-toolkit](https://github.com/dsh-external/dsh-toolkit) | DSH 零依赖工具包 collection —— time / encoding / json  |
| [dsh-web-ui](https://github.com/dsh-external/dsh-web-ui) | null |
| [official-plugins-port](https://github.com/dsh-external/official-plugins-port) | Official Claude Code / Codex plugins ported to t |
| [oh-my-dsh](https://github.com/dsh-external/oh-my-dsh) | Perpetual-motion swarm: DSH feature-gap plugins  |
| [Qwen-MM-Plugins](https://github.com/dsh-external/Qwen-MM-Plugins) | Qwen-MM-Plugins支持 |
| [toybox](https://github.com/dsh-external/toybox) | DSH 插件玩具箱 🧸 —— 有趣的技能/MCP 插件收藏：代码考古学家在此安家（更多整活插件陆 |
</details>
</details>

<details>
<summary>📡 远程渠道（7）</summary>

| 插件 | 说明 |
|---|---|
| [dsh-feishu-bot](https://github.com/dsh-external/dsh-feishu-bot) | Feishu remote channel for DeepSeek Harness |
| [dsh-ica](https://github.com/dsh-external/dsh-ica) | dsh 但是 icalingua 前端 |
| [dsh-wecom-bot](https://github.com/dsh-external/dsh-wecom-bot) | Wecom remote channel for DeepSeek Harness |
| [dsh-weixin-bot](https://github.com/dsh-external/dsh-weixin-bot) | WeiXin remote channel for DeepSeek Harness |
| [qqbot](https://github.com/dsh-external/qqbot) | QQ remote channel for DeepSeek Harness |
| [telegram](https://github.com/dsh-external/telegram) | Marisa 插件：Telegram Bot API 桥接（长轮询、per-chat 会话、HT |
| [tg-bot](https://github.com/dsh-external/tg-bot) | Telegram remote channel for DeepSeek Harness |
</details>

<details>
<summary>🛠 基础设施（35）</summary>

| 插件 | 说明 |
|---|---|
| [deepseek-harness-desktop](https://github.com/dsh-external/deepseek-harness-desktop) | DSH 桌面应用 |
| [deepseek-harness-distro](https://github.com/dsh-external/deepseek-harness-distro) | 自定义发行版 |
| [ds_web_craw](https://github.com/dsh-external/ds_web_craw) | null |
| [dsh-android](https://github.com/dsh-external/dsh-android) | run dsh on your android device. |
| [dsh-browser](https://github.com/dsh-external/dsh-browser) | Chrome侧边栏拓展，使用 DSH 直接操作浏览器（0视觉能力依赖） |
| [dsh-coding-receipt](https://github.com/dsh-external/dsh-coding-receipt) | Turn a DeepSeek Harness session log into a local |
| [dsh-companion](https://github.com/dsh-external/dsh-companion) | DeepSeek Harness 的常驻桌面助手：全局唤起、定时自动化、快捷回复、插件市场 |
| [dsh-desktop](https://github.com/dsh-external/dsh-desktop) | null |
| [dsh-desktop-electron](https://github.com/dsh-external/dsh-desktop-electron) | Cross-platform Electron desktop shell for the DS |
| [dsh-desktop-mac](https://github.com/dsh-external/dsh-desktop-mac) | null |

<details>
<summary>展开全部（剩余 25 条）</summary>

| 插件 | 说明 |
|---|---|
| [dsh-desktop-tools](https://github.com/dsh-external/dsh-desktop-tools) | DSH 桌面工具集:一键启动、自动升级、开机自启、PWA 可安装补丁(内测私有) |
| [dsh-hub](https://github.com/dsh-external/dsh-hub) | OMDSH community extension hub built on official  |
| [dsh-island](https://github.com/dsh-external/dsh-island) | DSH Dynamic Island — macOS notch panel for DSH；m |
| [dsh-mygo](https://github.com/dsh-external/dsh-mygo) | null |
| [dsh-ohos-patch](https://github.com/dsh-external/dsh-ohos-patch) | 让deepseek harness能在 ohos上跑！ |
| [dsh-pet-rs](https://github.com/dsh-external/dsh-pet-rs) | null |
| [dsh-public-repo-monitor](https://github.com/dsh-external/dsh-public-repo-monitor) | null |
| [dsh-trace](https://github.com/dsh-external/dsh-trace) | DeepSeek Harness telemetry backend that exports  |
| [dsh-tui](https://github.com/dsh-external/dsh-tui) | null |
| [dsh-vscode](https://github.com/dsh-external/dsh-vscode) | Native VS Code chat integration for DeepSeek Har |
| [dsh-win-port](https://github.com/dsh-external/dsh-win-port) | null |
| [fabric](https://github.com/dsh-external/fabric) | 一种类似MC Fabric的hook处理器 |
| [marisa](https://github.com/dsh-external/marisa) | Marisa（魔理沙）— DeepSeek Harness 外部插件管理器：寄生安装、CLI + |
| [oh-dsh-desktop](https://github.com/dsh-external/oh-dsh-desktop) | Extensible macOS workbench for DeepSeek Harness  |
| [oh-my-dsh-distribution](https://github.com/dsh-external/oh-my-dsh-distribution) | Pure-data Oh My DSH distribution Recipes for DSH |
| [plugin-registry](https://github.com/dsh-external/plugin-registry) | DSH 插件生态基建：薄控制台（浏览器面板管理官方 repository 插件，0 patch） |
| [plugin-template](https://github.com/dsh-external/plugin-template) | 基于原turtle ui官方仓库创建的plugin模板仓库 |
| [Recall](https://github.com/dsh-external/Recall) | Switch agents. Keep the memory. Local-first sear |
| [repo-visibility-guard](https://github.com/dsh-external/repo-visibility-guard) | Automatically remediate public repositories in d |
| [sandbox-micro](https://github.com/dsh-external/sandbox-micro) | microsandbox支持 |
| [sandbox-mxc](https://github.com/dsh-external/sandbox-mxc) | 微软跨平台沙盒支持 |
| [sandbox-nono](https://github.com/dsh-external/sandbox-nono) | nono沙盒支持 |
| [tonghuashun-harness](https://github.com/dsh-external/tonghuashun-harness) | null |
| [web-components](https://github.com/dsh-external/web-components) | web-components支持 |
| [zephyr](https://github.com/dsh-external/zephyr) | deepseek harness composer |
</details>
</details>

<details>
<summary>🔬 研究（5）</summary>

| 插件 | 说明 |
|---|---|
| [dsh-plugin-radar](https://github.com/dsh-external/dsh-plugin-radar) | DSH 插件兼容性雷达：每日自动扫描 org 插件与 mainline 接口漂移（补丁/seam |
| [dsh-scholar](https://github.com/dsh-external/dsh-scholar) | null |
| [dsh-security](https://github.com/dsh-external/dsh-security) | DSH 现有的可行的攻击链 demo |
| [dshfind](https://github.com/dsh-external/dshfind) | 从0开始学习dsh，dsh资源和导航站 dsh.com |
| [savemoneybenchmark](https://github.com/dsh-external/savemoneybenchmark) | 降本增效benchmark |
</details>

<details>
<summary>❓ 未分类（10）</summary>

| 插件 | 说明 |
|---|---|
| [dsh_ide](https://github.com/dsh-external/dsh_ide) | DSH IDE 大工程：集成开发环境方向（编辑器/工程视图/调试） |
| [dsh_workflow](https://github.com/dsh-external/dsh_workflow) | Dynamic Workflow for dsh |
| [dsh-build](https://github.com/dsh-external/dsh-build) | dsh-build |
| [dsh-code](https://github.com/dsh-external/dsh-code) | null |
| [dsh-fkin-vibe](https://github.com/dsh-external/dsh-fkin-vibe) | null |
| [dsh-hmz](https://github.com/dsh-external/dsh-hmz) | null |
| [dsh-remote](https://github.com/dsh-external/dsh-remote) | 为DSH引入类似于Codex APP的通过SSH控制远端机器的能力 |
| [dsh-ui-webview](https://github.com/dsh-external/dsh-ui-webview) | null |
| [oh-my-deepseek](https://github.com/dsh-external/oh-my-deepseek) | oh-my-deepseek |
| [Top](https://github.com/dsh-external/Top) | 📊 Daily leaderboard for the dsh-external plugin  |
</details>

<!-- AUTO:catalog:END -->

## 欢迎加入社群

DSH 插件生态交流群（微信群）：插件作者、维护者与使用者都在这里，讨论插件开发、兼容性问题与新插件发布。

<img src="assets/wechat-group-qr.png" width="300" alt="DSH-Plugins 交流群二维码">

> 二维码 7 天内有效（2026-08-20 前）。

## 当前生态快照

<!-- AUTO:ecosystem:START -->
> 更新于 2026-08-13 23:45 · 每 8 小时刷新 · mainline `7b9644f`

| 证据层 | 当前结果 |
|---|---:|
| 自动收录 | 288 个仓库 |
| 静态综合判定 | 41 兼容 · 31 关注 · 9 需适配 |
| 证据不足 | 188 待调研 |
| 其他 | 13 占位 · 2 不适用 · 4 已删除 |
| 运行级实测 | 0 可用 · 5 失败（共测试 5 个） |
| 正在跟踪的 PR | 11 |

[完整索引](reports/2026-08-13/index.md) · [静态矩阵](reports/2026-08-13/mainline-compat.md) · [编译实验](reports/2026-08-13/compile-compat.md) · [运行实测](reports/2026-08-13/runtime-test.md)

**插件目录**（288 个仓库 · 按判定状态分群）

**兼容**（41）

| 仓库 | 状态 |
|---|---|
| [deepseek-harness-desktop](https://github.com/dsh-external/deepseek-harness-desktop) | 兼容 |
| [deepseek-harness-distro](https://github.com/dsh-external/deepseek-harness-distro) | 兼容 |
| [dsh-acp](https://github.com/dsh-external/dsh-acp) | 兼容 |
| [dsh-desktop](https://github.com/dsh-external/dsh-desktop) | 兼容 |
| [dsh-feishu-bot](https://github.com/dsh-external/dsh-feishu-bot) | 兼容 |
| [dsh-gh-bridge](https://github.com/dsh-external/dsh-gh-bridge) | 兼容 |
| [dsh-issue-filer](https://github.com/dsh-external/dsh-issue-filer) | 兼容 |
| [dsh-memory-evolve](https://github.com/dsh-external/dsh-memory-evolve) | 兼容 |
| [dsh-opencode-server](https://github.com/dsh-external/dsh-opencode-server) | 兼容 |
| [dsh-pi-adapter](https://github.com/dsh-external/dsh-pi-adapter) | 兼容 |
| [dsh-prompt-studio](https://github.com/dsh-external/dsh-prompt-studio) | 兼容 |
| [dsh-pty-windows](https://github.com/dsh-external/dsh-pty-windows) | 兼容 |
| [dsh-sfw](https://github.com/dsh-external/dsh-sfw) | 兼容 |
| [dsh-shell-windows](https://github.com/dsh-external/dsh-shell-windows) | 兼容 |
| [dsh-ui-progress](https://github.com/dsh-external/dsh-ui-progress) | 兼容 |
| [dsh-ui-whale](https://github.com/dsh-external/dsh-ui-whale) | 兼容 |
| [dsh-web-ui-approval-notify](https://github.com/dsh-external/dsh-web-ui-approval-notify) | 兼容 |
| [dsh-wecom-bot](https://github.com/dsh-external/dsh-wecom-bot) | 兼容 |
| [dsh-weixin-bot](https://github.com/dsh-external/dsh-weixin-bot) | 兼容 |
| [dsh-win-port](https://github.com/dsh-external/dsh-win-port) | 兼容 |
| [dshx-update-check](https://github.com/dsh-external/dshx-update-check) | 兼容 |
| [hub](https://github.com/dsh-external/hub) | 兼容 |
| [plugin-registry](https://github.com/dsh-external/plugin-registry) | 兼容 |
| [qqbot](https://github.com/dsh-external/qqbot) | 兼容 |
| [Recall](https://github.com/dsh-external/Recall) | 兼容 |
| [review-panel](https://github.com/dsh-external/review-panel) | 兼容 |
| [session-persistence-rdb](https://github.com/dsh-external/session-persistence-rdb) | 兼容 |
| [toybox](https://github.com/dsh-external/toybox) | 兼容 |
| [dsh-multimedia-webui-input](https://github.com/dsh-external/dsh-multimedia-webui-input) | 兼容 |
| [dsh-hub](https://github.com/dsh-external/dsh-hub) | 兼容 |
| [dsh-paste-input](https://github.com/dsh-external/dsh-paste-input) | 兼容 |
| [dsh-bash-encoding](https://github.com/dsh-external/dsh-bash-encoding) | 兼容 |
| [dsh-android](https://github.com/dsh-external/dsh-android) | 兼容 |
| [dsh-input-history](https://github.com/dsh-external/dsh-input-history) | 兼容 |
| [dsh-desktop-electron](https://github.com/dsh-external/dsh-desktop-electron) | 兼容 |
| [dsh-track](https://github.com/dsh-external/dsh-track) | 兼容 |
| [dsh-minigames](https://github.com/dsh-external/dsh-minigames) | 兼容 |
| [dsh-harness-ops](https://github.com/dsh-external/dsh-harness-ops) | 兼容 |
| [plugin-template](https://github.com/dsh-external/plugin-template) | 兼容 |
| [dsh-chat-thumb](https://github.com/dsh-external/dsh-chat-thumb) | 兼容 |
| [dsh-diff-viewer](https://github.com/dsh-external/dsh-diff-viewer) | 兼容 |

**需适配**（9）

| 仓库 | 状态 |
|---|---|
| [dsh-subagent-tree](https://github.com/dsh-external/dsh-subagent-tree) | 需适配 |
| [dsh-working-activity](https://github.com/dsh-external/dsh-working-activity) | 需适配 |
| [turtle-ui](https://github.com/dsh-external/turtle-ui) | 需适配 |
| [fabric](https://github.com/dsh-external/fabric) | 需适配 |
| [dsh-tps](https://github.com/dsh-external/dsh-tps) | 需适配 |
| [dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | 需适配 |
| [dsh-question-collapse](https://github.com/dsh-external/dsh-question-collapse) | 需适配 |
| [dsh-ohos-patch](https://github.com/dsh-external/dsh-ohos-patch) | 需适配 |
| [dsh-cot-summary](https://github.com/dsh-external/dsh-cot-summary) | 需适配 |

**关注**（31）

| 仓库 | 状态 |
|---|---|
| [chat-width](https://github.com/dsh-external/chat-width) | 关注 |
| [distill](https://github.com/dsh-external/distill) | 关注 |
| [dsh-agent-session-sources](https://github.com/dsh-external/dsh-agent-session-sources) | 关注 |
| [dsh-artifact](https://github.com/dsh-external/dsh-artifact) | 关注 |
| [dsh-cc-tui](https://github.com/dsh-external/dsh-cc-tui) | 关注 |
| [dsh-companion](https://github.com/dsh-external/dsh-companion) | 关注 |
| [dsh-github-integration](https://github.com/dsh-external/dsh-github-integration) | 关注 |
| [dsh-live-stats](https://github.com/dsh-external/dsh-live-stats) | 关注 |
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | 关注 |
| [dsh-session-search](https://github.com/dsh-external/dsh-session-search) | 关注 |
| [dsh-skills-manager](https://github.com/dsh-external/dsh-skills-manager) | 关注 |
| [dsh-skins](https://github.com/dsh-external/dsh-skins) | 关注 |
| [dsh-tool-browser](https://github.com/dsh-external/dsh-tool-browser) | 关注 |
| [dsh-tool-calculator](https://github.com/dsh-external/dsh-tool-calculator) | 关注 |
| [dsh-tool-encoding](https://github.com/dsh-external/dsh-tool-encoding) | 关注 |
| [dsh-tool-json](https://github.com/dsh-external/dsh-tool-json) | 关注 |
| [dsh-tool-time](https://github.com/dsh-external/dsh-tool-time) | 关注 |
| [dsh-vision](https://github.com/dsh-external/dsh-vision) | 关注 |
| [dsh-web-terminal](https://github.com/dsh-external/dsh-web-terminal) | 关注 |
| [dsh-web-ui](https://github.com/dsh-external/dsh-web-ui) | 关注 |
| [ex-setting](https://github.com/dsh-external/ex-setting) | 关注 |
| [marisa](https://github.com/dsh-external/marisa) | 关注 |
| [Qwen-MM-Plugins](https://github.com/dsh-external/Qwen-MM-Plugins) | 关注 |
| [sandbox-mxc](https://github.com/dsh-external/sandbox-mxc) | 关注 |
| [session-chatlog](https://github.com/dsh-external/session-chatlog) | 关注 |
| [telegram](https://github.com/dsh-external/telegram) | 关注 |
| [tg-bot](https://github.com/dsh-external/tg-bot) | 关注 |
| [web-components](https://github.com/dsh-external/web-components) | 关注 |
| [dsh-alphasolve](https://github.com/dsh-external/dsh-alphasolve) | 关注 |
| [dsh-slice-agent-loop](https://github.com/dsh-external/dsh-slice-agent-loop) | 关注 |
| [dsh-custom-tool](https://github.com/dsh-external/dsh-custom-tool) | 关注 |

**待调研**（188）

| 仓库 | 状态 |
|---|---|
| [---](https://github.com/dsh-external/---) | 待调研 |
| [dsh-web-ui-notify](https://github.com/dsh-external/dsh-web-ui-notify) | 待调研 |
| [dsh-web-panel](https://github.com/dsh-external/dsh-web-panel) | 待调研 |
| [dsh-evolve](https://github.com/dsh-external/dsh-evolve) | 待调研 |
| [dsh-island](https://github.com/dsh-external/dsh-island) | 待调研 |
| [dsh-drag-and-drop](https://github.com/dsh-external/dsh-drag-and-drop) | 待调研 |
| [dsh-message-edit](https://github.com/dsh-external/dsh-message-edit) | 待调研 |
| [dsh-deep-research](https://github.com/dsh-external/dsh-deep-research) | 待调研 |
| [repo-visibility-guard](https://github.com/dsh-external/repo-visibility-guard) | 待调研 |
| [dsh-grok-tui](https://github.com/dsh-external/dsh-grok-tui) | 待调研 |
| [ds_web_craw](https://github.com/dsh-external/ds_web_craw) | 待调研 |
| [dsh-browser](https://github.com/dsh-external/dsh-browser) | 待调研 |
| [dsh-desktop-mac](https://github.com/dsh-external/dsh-desktop-mac) | 待调研 |
| [dsh-public-repo-monitor](https://github.com/dsh-external/dsh-public-repo-monitor) | 待调研 |
| [dsh-inspect](https://github.com/dsh-external/dsh-inspect) | 待调研 |
| [zotero-wave-rag](https://github.com/dsh-external/zotero-wave-rag) | 待调研 |
| [onboarding](https://github.com/dsh-external/onboarding) | 待调研 |
| [ego-browser](https://github.com/dsh-external/ego-browser) | 待调研 |
| [dsh-nowledge-mem](https://github.com/dsh-external/dsh-nowledge-mem) | 待调研 |
| [dsh-sidechain](https://github.com/dsh-external/dsh-sidechain) | 待调研 |
| [dsh-a2a](https://github.com/dsh-external/dsh-a2a) | 待调研 |
| [dsh-feishu-notify](https://github.com/dsh-external/dsh-feishu-notify) | 待调研 |
| [dsh-remote](https://github.com/dsh-external/dsh-remote) | 待调研 |
| [mstar-workflow](https://github.com/dsh-external/mstar-workflow) | 待调研 |
| [dsh-scholar](https://github.com/dsh-external/dsh-scholar) | 待调研 |
| [dsh-issue-like-skill](https://github.com/dsh-external/dsh-issue-like-skill) | 待调研 |
| [dsh-tool-csv](https://github.com/dsh-external/dsh-tool-csv) | 待调研 |
| [dsh-tool-regex](https://github.com/dsh-external/dsh-tool-regex) | 待调研 |
| [dsh-session-repair-skill](https://github.com/dsh-external/dsh-session-repair-skill) | 待调研 |
| [DSH-better-sidebar](https://github.com/dsh-external/DSH-better-sidebar) | 待调研 |
| [dsh-ica](https://github.com/dsh-external/dsh-ica) | 待调研 |
| [dsh-advisor](https://github.com/dsh-external/dsh-advisor) | 待调研 |
| [dsh-llm-fallbacks](https://github.com/dsh-external/dsh-llm-fallbacks) | 待调研 |
| [dsh-web-workflow-visualizer](https://github.com/dsh-external/dsh-web-workflow-visualizer) | 待调研 |
| [dsh-checkpoint](https://github.com/dsh-external/dsh-checkpoint) | 待调研 |
| [dsh-rewind](https://github.com/dsh-external/dsh-rewind) | 待调研 |
| [official-plugins-port](https://github.com/dsh-external/official-plugins-port) | 待调研 |
| [oh-my-dsh](https://github.com/dsh-external/oh-my-dsh) | 待调研 |
| [dsh-side-panel](https://github.com/dsh-external/dsh-side-panel) | 待调研 |
| [dsh-profile-bundle-example](https://github.com/dsh-external/dsh-profile-bundle-example) | 待调研 |
| [dsh-plan-execute](https://github.com/dsh-external/dsh-plan-execute) | 待调研 |
| [zotero-harvest](https://github.com/dsh-external/zotero-harvest) | 待调研 |
| [zephyr](https://github.com/dsh-external/zephyr) | 待调研 |
| [dsh-skill-stats](https://github.com/dsh-external/dsh-skill-stats) | 待调研 |
| [dsh-web-archive](https://github.com/dsh-external/dsh-web-archive) | 待调研 |
| [sandbox-micro](https://github.com/dsh-external/sandbox-micro) | 待调研 |
| [dsh-git-identity](https://github.com/dsh-external/dsh-git-identity) | 待调研 |
| [dsh-lazyfish](https://github.com/dsh-external/dsh-lazyfish) | 待调研 |
| [dsh-auto-approval](https://github.com/dsh-external/dsh-auto-approval) | 待调研 |
| [dsh-client-ui-plan-execute](https://github.com/dsh-external/dsh-client-ui-plan-execute) | 待调研 |
| [dsh-stickers](https://github.com/dsh-external/dsh-stickers) | 待调研 |
| [deep-standard-skill](https://github.com/dsh-external/deep-standard-skill) | 待调研 |
| [dsh-serenity-plugin](https://github.com/dsh-external/dsh-serenity-plugin) | 待调研 |
| [dsh-toolkit](https://github.com/dsh-external/dsh-toolkit) | 待调研 |
| [dsh-tool-markdown](https://github.com/dsh-external/dsh-tool-markdown) | 待调研 |
| [dsh-session-health](https://github.com/dsh-external/dsh-session-health) | 待调研 |
| [dsh-desktop-tools](https://github.com/dsh-external/dsh-desktop-tools) | 待调研 |
| [dsh-reuse-first](https://github.com/dsh-external/dsh-reuse-first) | 待调研 |
| [dsh-plus](https://github.com/dsh-external/dsh-plus) | 待调研 |
| [dsh-session-cluster](https://github.com/dsh-external/dsh-session-cluster) | 待调研 |
| [DSH-UI4A](https://github.com/dsh-external/DSH-UI4A) | 待调研 |
| [dsh-visualize](https://github.com/dsh-external/dsh-visualize) | 待调研 |
| [dsh-plugin-check](https://github.com/dsh-external/dsh-plugin-check) | 待调研 |
| [dsh-plugin-dev](https://github.com/dsh-external/dsh-plugin-dev) | 待调研 |
| [dsh-gomoku](https://github.com/dsh-external/dsh-gomoku) | 待调研 |
| [dsh-101](https://github.com/dsh-external/dsh-101) | 待调研 |
| [dsh-turn-rewind](https://github.com/dsh-external/dsh-turn-rewind) | 待调研 |
| [dsh-genui](https://github.com/dsh-external/dsh-genui) | 待调研 |
| [dsh-mygo](https://github.com/dsh-external/dsh-mygo) | 待调研 |
| [cross-harness-cite](https://github.com/dsh-external/cross-harness-cite) | 待调研 |
| [dsh-activity-plugin](https://github.com/dsh-external/dsh-activity-plugin) | 待调研 |
| [dsh-tool-diff](https://github.com/dsh-external/dsh-tool-diff) | 待调研 |
| [dsh-mobileweb-adapter](https://github.com/dsh-external/dsh-mobileweb-adapter) | 待调研 |
| [dsh-mineru](https://github.com/dsh-external/dsh-mineru) | 待调研 |
| [dsh-pet](https://github.com/dsh-external/dsh-pet) | 待调研 |
| [dsh-paseo](https://github.com/dsh-external/dsh-paseo) | 待调研 |
| [dsh-vscode](https://github.com/dsh-external/dsh-vscode) | 待调研 |
| [dsh-tui-front-door](https://github.com/dsh-external/dsh-tui-front-door) | 待调研 |
| [dsh-webbridge](https://github.com/dsh-external/dsh-webbridge) | 待调研 |
| [dsh-custom-css](https://github.com/dsh-external/dsh-custom-css) | 待调研 |
| [tonghuashun-harness](https://github.com/dsh-external/tonghuashun-harness) | 待调研 |
| [dsh-club](https://github.com/dsh-external/dsh-club) | 待调研 |
| [dsh-humanize](https://github.com/dsh-external/dsh-humanize) | 待调研 |
| [dsh-agent-budget](https://github.com/dsh-external/dsh-agent-budget) | 待调研 |
| [dsh-spur](https://github.com/dsh-external/dsh-spur) | 待调研 |
| [dsh-selection-chat](https://github.com/dsh-external/dsh-selection-chat) | 待调研 |
| [dsh-browser-panel](https://github.com/dsh-external/dsh-browser-panel) | 待调研 |
| [dsh-engram-relay](https://github.com/dsh-external/dsh-engram-relay) | 待调研 |
| [yet-another-subagent](https://github.com/dsh-external/yet-another-subagent) | 待调研 |
| [dsh-voice-chat](https://github.com/dsh-external/dsh-voice-chat) | 待调研 |
| [dsh-ads](https://github.com/dsh-external/dsh-ads) | 待调研 |
| [dsh-skill-session-recovery](https://github.com/dsh-external/dsh-skill-session-recovery) | 待调研 |
| [dsh-tavern-plugin](https://github.com/dsh-external/dsh-tavern-plugin) | 待调研 |
| [dsh-qq2006](https://github.com/dsh-external/dsh-qq2006) | 待调研 |
| [dsh-plugin-guide](https://github.com/dsh-external/dsh-plugin-guide) | 待调研 |
| [dsh-mnemon](https://github.com/dsh-external/dsh-mnemon) | 待调研 |
| [dsh-pet-rs](https://github.com/dsh-external/dsh-pet-rs) | 待调研 |
| [dsh-auto-blame](https://github.com/dsh-external/dsh-auto-blame) | 待调研 |
| [dsh-latex](https://github.com/dsh-external/dsh-latex) | 待调研 |
| [dsh-tool-stat](https://github.com/dsh-external/dsh-tool-stat) | 待调研 |
| [dsh-tool-schema](https://github.com/dsh-external/dsh-tool-schema) | 待调研 |
| [dsh-security-audit](https://github.com/dsh-external/dsh-security-audit) | 待调研 |
| [dsh-browser-bridge](https://github.com/dsh-external/dsh-browser-bridge) | 待调研 |
| [ya-workspace-sidebar](https://github.com/dsh-external/ya-workspace-sidebar) | 待调研 |
| [dsh-d399](https://github.com/dsh-external/dsh-d399) | 待调研 |
| [7d7d](https://github.com/dsh-external/7d7d) | 待调研 |
| [dsh-cordis-rocks](https://github.com/dsh-external/dsh-cordis-rocks) | 待调研 |
| [dsh-sleep](https://github.com/dsh-external/dsh-sleep) | 待调研 |
| [sandbox-nono](https://github.com/dsh-external/sandbox-nono) | 待调研 |
| [dsh-auto-chess](https://github.com/dsh-external/dsh-auto-chess) | 待调研 |
| [dshfind](https://github.com/dsh-external/dshfind) | 待调研 |
| [dsh-cyber-sec](https://github.com/dsh-external/dsh-cyber-sec) | 待调研 |
| [dsh-anti-ads](https://github.com/dsh-external/dsh-anti-ads) | 待调研 |
| [dsh-self-control-guard](https://github.com/dsh-external/dsh-self-control-guard) | 待调研 |
| [whale-girl](https://github.com/dsh-external/whale-girl) | 待调研 |
| [dsh-codex-bridge](https://github.com/dsh-external/dsh-codex-bridge) | 待调研 |
| [dsh-kimi-bridge](https://github.com/dsh-external/dsh-kimi-bridge) | 待调研 |
| [session-teleport](https://github.com/dsh-external/session-teleport) | 待调研 |
| [dsh-code-map](https://github.com/dsh-external/dsh-code-map) | 待调研 |
| [dsh-loop](https://github.com/dsh-external/dsh-loop) | 待调研 |
| [dsh-navbar](https://github.com/dsh-external/dsh-navbar) | 待调研 |
| [dsh-task-status](https://github.com/dsh-external/dsh-task-status) | 待调研 |
| [dsh-annotation](https://github.com/dsh-external/dsh-annotation) | 待调研 |
| [dsh-web-review](https://github.com/dsh-external/dsh-web-review) | 待调研 |
| [dsh-cc-connect](https://github.com/dsh-external/dsh-cc-connect) | 待调研 |
| [dsh-focus-chat](https://github.com/dsh-external/dsh-focus-chat) | 待调研 |
| [dsh-save-intp](https://github.com/dsh-external/dsh-save-intp) | 待调研 |
| [dsh-find-plugins](https://github.com/dsh-external/dsh-find-plugins) | 待调研 |
| [dsh-vision-toolkit](https://github.com/dsh-external/dsh-vision-toolkit) | 待调研 |
| [Top](https://github.com/dsh-external/Top) | 待调研 |
| [dsh-kimi-browser](https://github.com/dsh-external/dsh-kimi-browser) | 待调研 |
| [dsh-edu](https://github.com/dsh-external/dsh-edu) | 待调研 |
| [oh-dsh-desktop](https://github.com/dsh-external/oh-dsh-desktop) | 待调研 |
| [dsh-plugin-skills](https://github.com/dsh-external/dsh-plugin-skills) | 待调研 |
| [dsh-deep-whale](https://github.com/dsh-external/dsh-deep-whale) | 待调研 |
| [dsh-tool-search](https://github.com/dsh-external/dsh-tool-search) | 待调研 |
| [oh-my-dsh-distribution](https://github.com/dsh-external/oh-my-dsh-distribution) | 待调研 |
| [dsh-trace](https://github.com/dsh-external/dsh-trace) | 待调研 |
| [deepseek-manners](https://github.com/dsh-external/deepseek-manners) | 待调研 |
| [dsh-design](https://github.com/dsh-external/dsh-design) | 待调研 |
| [dsh-computer-use](https://github.com/dsh-external/dsh-computer-use) | 待调研 |
| [dsh-meme](https://github.com/dsh-external/dsh-meme) | 待调研 |
| [dsh-agent-rp](https://github.com/dsh-external/dsh-agent-rp) | 待调研 |
| [dsh-music-player](https://github.com/dsh-external/dsh-music-player) | 待调研 |
| [dsh-multica-runtime](https://github.com/dsh-external/dsh-multica-runtime) | 待调研 |
| [dsh-mega](https://github.com/dsh-external/dsh-mega) | 待调研 |
| [dsh-office](https://github.com/dsh-external/dsh-office) | 待调研 |
| [savemoneybenchmark](https://github.com/dsh-external/savemoneybenchmark) | 待调研 |
| [dsh-kb-sieve](https://github.com/dsh-external/dsh-kb-sieve) | 待调研 |
| [dsh-data-agent](https://github.com/dsh-external/dsh-data-agent) | 待调研 |
| [dsh-security](https://github.com/dsh-external/dsh-security) | 待调研 |
| [dsh-teamwork](https://github.com/dsh-external/dsh-teamwork) | 待调研 |
| [ui-status-label](https://github.com/dsh-external/ui-status-label) | 待调研 |
| [dsh-easy-ctx-manager](https://github.com/dsh-external/dsh-easy-ctx-manager) | 待调研 |
| [browser4-dsh](https://github.com/dsh-external/browser4-dsh) | 待调研 |
| [show-bash-command](https://github.com/dsh-external/show-bash-command) | 待调研 |
| [dsh-super-injector](https://github.com/dsh-external/dsh-super-injector) | 待调研 |
| [dsh-better-sidebar-plugin-office](https://github.com/dsh-external/dsh-better-sidebar-plugin-office) | 待调研 |
| [dsh-explain](https://github.com/dsh-external/dsh-explain) | 待调研 |
| [dsh-interpreters](https://github.com/dsh-external/dsh-interpreters) | 待调研 |
| [dsh-stock-market](https://github.com/dsh-external/dsh-stock-market) | 待调研 |
| [dsh-scout](https://github.com/dsh-external/dsh-scout) | 待调研 |
| [dsh-turn-navigator](https://github.com/dsh-external/dsh-turn-navigator) | 待调研 |
| [dsh-mobile](https://github.com/dsh-external/dsh-mobile) | 待调研 |
| [dsh-share](https://github.com/dsh-external/dsh-share) | 待调研 |
| [dsh-travel-plugin](https://github.com/dsh-external/dsh-travel-plugin) | 待调研 |
| [dsh-suggested-replies](https://github.com/dsh-external/dsh-suggested-replies) | 待调研 |
| [dsh-aigc-canvas](https://github.com/dsh-external/dsh-aigc-canvas) | 待调研 |
| [dsh-sonar](https://github.com/dsh-external/dsh-sonar) | 待调研 |
| [dsh-ultra-ui](https://github.com/dsh-external/dsh-ultra-ui) | 待调研 |
| [dsh-deepresearch](https://github.com/dsh-external/dsh-deepresearch) | 待调研 |
| [dsh-notebooks](https://github.com/dsh-external/dsh-notebooks) | 待调研 |
| [context-doctor](https://github.com/dsh-external/context-doctor) | 待调研 |
| [dsh-openpencil](https://github.com/dsh-external/dsh-openpencil) | 待调研 |
| [dsh-deeplink](https://github.com/dsh-external/dsh-deeplink) | 待调研 |
| [dsh-emoji](https://github.com/dsh-external/dsh-emoji) | 待调研 |
| [dsh_workflow](https://github.com/dsh-external/dsh_workflow) | 待调研 |
| [dsh-openmaic](https://github.com/dsh-external/dsh-openmaic) | 待调研 |
| [dsh-deepcel](https://github.com/dsh-external/dsh-deepcel) | 待调研 |
| [dsh-STAR](https://github.com/dsh-external/dsh-STAR) | 待调研 |
| [dsh-STAGE](https://github.com/dsh-external/dsh-STAGE) | 待调研 |
| [dsh-conversation-share](https://github.com/dsh-external/dsh-conversation-share) | 待调研 |
| [tonghuashun-webui](https://github.com/dsh-external/tonghuashun-webui) | 待调研 |
| [dsh-session-notification](https://github.com/dsh-external/dsh-session-notification) | 待调研 |
| [dsh-openbiliclaw](https://github.com/dsh-external/dsh-openbiliclaw) | 待调研 |
| [dsh-longbridge](https://github.com/dsh-external/dsh-longbridge) | 待调研 |
| [dsh-dzcf](https://github.com/dsh-external/dsh-dzcf) | 待调研 |
| [---](https://github.com/dsh-external/---) | 待调研 |

**占位**（13）

| 仓库 | 状态 |
|---|---|
| [dsh-coding-receipt](https://github.com/dsh-external/dsh-coding-receipt) | 占位 |
| [dsh-cordis-examples](https://github.com/dsh-external/dsh-cordis-examples) | 占位 |
| [dsh-tui](https://github.com/dsh-external/dsh-tui) | 占位 |
| [dsh-session-hub](https://github.com/dsh-external/dsh-session-hub) | 占位 |
| [dsh-superpowers](https://github.com/dsh-external/dsh-superpowers) | 占位 |
| [dsh-spec-kit](https://github.com/dsh-external/dsh-spec-kit) | 占位 |
| [dsh-context7](https://github.com/dsh-external/dsh-context7) | 占位 |
| [dsh-ui-webview](https://github.com/dsh-external/dsh-ui-webview) | 占位 |
| [dsh-build](https://github.com/dsh-external/dsh-build) | 占位 |
| [oh-my-deepseek](https://github.com/dsh-external/oh-my-deepseek) | 占位 |
| [dsh-fkin-vibe](https://github.com/dsh-external/dsh-fkin-vibe) | 占位 |
| [__perm_probe__](https://github.com/dsh-external/__perm_probe__) | 占位 |
| [dsh-hmz](https://github.com/dsh-external/dsh-hmz) | 占位 |

**不适用**（2）

| 仓库 | 状态 |
|---|---|
| [group-chat-diary](https://github.com/dsh-external/group-chat-diary) | 不适用 |
| [issues](https://github.com/dsh-external/issues) | 不适用 |

**已删除**（4）

| 仓库 | 状态 |
|---|---|
| [dsh-memory](https://github.com/dsh-external/dsh-memory) | 已删除 |
| [dsh-chat](https://github.com/dsh-external/dsh-chat) | 已删除 |
| [dsh-web](https://github.com/dsh-external/dsh-web) | 已删除 |
| [dsh_ide](https://github.com/dsh-external/dsh_ide) | 已删除 |

**今日新增 / 修改**（完整变更见 [CHANGELOG](CHANGELOG.md)）

| 仓库 | 类型 |
|---|---|
| （今日无新增） | |

| （今日无修改） | |


**⚠️ 需适配**（完整矩阵见 [mainline-compat.md](reports/2026-08-13/mainline-compat.md)）

| 插件 | 锚定 | 判定 |
|---|---|---|
| [dsh-subagent-tree](https://github.com/dsh-external/dsh-subagent-tree) | 未知 | 需适配 |
| [dsh-working-activity](https://github.com/dsh-external/dsh-working-activity) | 未知（非 commit 锚定: 20260804T143803Z） | 需适配 |
| [turtle-ui](https://github.com/dsh-external/turtle-ui) | 未知（不同谱系） | 需适配 |
| [fabric](https://github.com/dsh-external/fabric) | 未知 | 需适配 |
| [dsh-tps](https://github.com/dsh-external/dsh-tps) | 未知 | 需适配 |
| [dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | 未知 | 需适配 |
| [dsh-question-collapse](https://github.com/dsh-external/dsh-question-collapse) | 未知（不同谱系） | 需适配 |
| [dsh-ohos-patch](https://github.com/dsh-external/dsh-ohos-patch) | 未知 | 需适配 |
| [dsh-cot-summary](https://github.com/dsh-external/dsh-cot-summary) | 未知 | 需适配 |

**🐙 正在跟踪的 open PR**

| 仓库 | PR | 标题 | 更新 |
|---|---|---|---|
| [dsh-deeptag](https://github.com/dsh-external/dsh-deeptag) | [#1](https://github.com/dsh-external/dsh-deeptag/pull/1) | Implement security-first DeepTag MVP | 2026-08-13 |
| [dsh-web-review](https://github.com/dsh-external/dsh-web-review) | [#1](https://github.com/dsh-external/dsh-web-review/pull/1) | dsh-web-review: add managed multi-tab browser preview | 2026-08-13 |
| [dsh-pi-adapter](https://github.com/dsh-external/dsh-pi-adapter) | [#6](https://github.com/dsh-external/dsh-pi-adapter/pull/6) | feat: register commands through cordis DI activation, not first session/created | 2026-08-12 |
| [dsh-pi-adapter](https://github.com/dsh-external/dsh-pi-adapter) | [#5](https://github.com/dsh-external/dsh-pi-adapter/pull/5) | feat: adapt-interactive ctx.ui tier + session-log quarantine audit | 2026-08-12 |
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | [#50](https://github.com/dsh-external/dsh-my-rsi/pull/50) | feat: migrate to 20260811 snapshot and reuse upstream surfaces | 2026-08-11 |
| [dsh-hub-private-archive](https://github.com/dsh-external/dsh-hub-private-archive) | [#15](https://github.com/dsh-external/dsh-hub-private-archive/pull/15) | Align optional host capabilities and legacy cleanup | 2026-08-11 |
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | [#49](https://github.com/dsh-external/dsh-my-rsi/pull/49) | docs: record external method provenance (#45) | 2026-08-11 |
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | [#43](https://github.com/dsh-external/dsh-my-rsi/pull/43) | feat: rsi-core live plugin execution face (#41) + supervised revival layer (#42) | 2026-08-11 |
| [session-teleport](https://github.com/dsh-external/session-teleport) | [#2](https://github.com/dsh-external/session-teleport/pull/2) | Add safe plugin lifecycle and real-device acceptance | 2026-08-10 |
| [group-chat-diary](https://github.com/dsh-external/group-chat-diary) | [#4](https://github.com/dsh-external/group-chat-diary/pull/4) | Automate Cloudflare Pages deployment | 2026-08-07 |
| [dsh-live-stats](https://github.com/dsh-external/dsh-live-stats) | [#1](https://github.com/dsh-external/dsh-live-stats/pull/1) | fix: make live token and TPS accounting provider-aligned | 2026-08-07 |

<!-- AUTO:ecosystem:END -->

快照只回答“当前证据是什么”，不在首页复制几百行仓库和变更记录。逐仓结论、失败原因、当日新增和开放 PR 以对应报告为准。

## 给插件使用者

### 1. 找到候选插件

- 优先从 [PLUGINS.md](PLUGINS.md) 选择已有人工分类和说明的插件。
- 若分类目录没有，再从[当前生态快照](#当前生态快照)进入当日完整索引，搜索仓库名或关键词。
- 仓库无法公开访问、没有 README、没有许可证或长期无维护时，把它视为高风险候选，而不是“已验证插件”。

### 2. 看懂状态

| 状态 | 它说明什么 | 它不说明什么 |
|---|---|---|
| 已收录 | 发现流程找到了仓库及插件入口信号 | 未证明能安装、能运行或安全 |
| 兼容（静态） | 在指定 mainline 快照上未发现当前规则定义的阻断信号 | 未经过真实加载时，不能等同于“可用” |
| 关注 | 存在版本、扩展点或元数据变化，需要人工确认 | 不一定已经损坏 |
| 需适配 | 已发现补丁冲突、接口漂移或其他明确阻断信号 | 不代表插件永远不可用；作者可能已在其他分支修复 |
| 运行可用 | 在报告记录的环境、插件提交和 mainline 快照上完成了加载或任务测试 | 不是完整功能测试、性能测试或安全审计 |
| 未知 / 待调研 | 当前证据不足 | 不应推断为兼容或不兼容 |

每个结论都应同时看四项：**插件 commit、mainline commit、测试日期、测试层级**。缺少其中任一项时，降低对结果的信任等级。

### 3. 安装、验证和回滚

本目录不是包管理器，也没有被本仓库验证过的统一安装命令。请以插件自身 README 的安装方式为准，并建议按以下顺序操作：

1. 阅读插件的安装、配置、权限和卸载说明。
2. 固定插件版本或 commit，不直接依赖会漂移的默认分支。
3. 先在隔离 profile 或测试环境加载，不提供生产密钥和敏感数据。
4. 执行一个最小功能任务，记录 DSH 版本、插件版本和日志。
5. 保留原配置与锁文件；失败时能移除插件并恢复环境。

若插件安装或功能本身出错，请优先在插件仓库反馈；若目录链接、分类或状态证据有误，请在本仓库提交 issue 或 PR。

## 给插件开发者

### 最低收录条件

公开目录建议只列出普通访问者能够打开的仓库。自动发现候选至少应满足：

- 仓库公开可访问，并添加 `dsh-plugin` topic；
- 根目录存在合法的 `package.json` 和非空 `name`；
- 提供 `main`、`exports` 或明确的 `dsh` 集成入口；
- README 说明插件做什么、如何安装、如何卸载以及最小使用示例；
- 所有运行时依赖在 `dependencies` / `peerDependencies` 中显式声明；
- 声明支持的 DSH 版本、快照或已验证 commit；
- 提供许可证，并避免把密钥、个人信息或私有仓库内容提交到公开目录。

包名应使用你有权控制的命名空间。只有获得 `dsh-external` 维护权限的项目才应使用 `@dsh-external/*`；不要占用不属于你的组织或官方保留命名空间。

### 一个合格的插件 README 至少包含

| 章节 | 应回答的问题 |
|---|---|
| Overview | 插件解决什么问题？适合谁？ |
| Compatibility | 支持哪些 DSH 版本或 mainline commit？最后验证日期是什么？ |
| Install / Uninstall | 如何安装、升级、禁用和彻底移除？ |
| Quick start | 最小配置和一个可复现示例是什么？ |
| Configuration | 配置项、默认值、环境变量和敏感项有哪些？ |
| Permissions & data | 会访问哪些文件、网络、凭据或用户数据？ |
| Troubleshooting | 常见错误、日志位置和回滚方式是什么？ |
| Development | 如何构建、测试和贡献？ |
| License & security | 使用什么许可证？安全问题如何私下报告？ |

### 提交插件

1. 给插件仓库添加 `dsh-plugin` topic，等待下一次扫描。
2. 在 [PLUGINS.md](PLUGINS.md) 的合适分类追加插件名、仓库链接和一句话说明。
3. 对照上面的最低条件完成自检。
4. 使用 [PR 模板](.github/PULL_REQUEST_TEMPLATE.md) 提交变更，并附上测试环境与结果。

仅修正链接、分类、描述或状态证据时，也欢迎直接提交小型 PR。请不要在目录 PR 中复制私有 issue、密钥、成员信息或大段第三方内容。

## 本仓库如何判定

| 层级 | 当前检查 | 合理结论 |
|---|---|---|
| L0 发现 | topic、仓库可见性、基本元数据 | 这是一个候选仓库 |
| L1 清单 | `package.json`、名称、入口字段 | 它“看起来可安装”，但还未证明能加载 |
| L2 静态兼容 | 补丁、扩展点（seam）、依赖版本范围 | 发现已知漂移信号，或暂未发现阻断信号 |
| L3 编译实验 | 在指定 workspace 中执行类型或语法检查 | 仅对该构建环境有效；缺依赖和环境问题需与真实 API 漂移分开 |
| L4 运行实测 | 安装、加载、最小任务或工具调用 | 在记录的环境和 commit 上观察到成功或失败 |

> [!NOTE]
> 首页不把以上层级合并成一个模糊的“兼容率”。静态通过、编译通过和运行通过使用不同字段与分母；完整证据保留在日期化报告中。

### 已知边界

- mainline 和插件都在快速变化，旧结论可能很快失效。
- 静态未发现问题不代表真实运行一定成功。
- 编译失败可能来自测试环境、缺失依赖或配置错误，不应自动等同于 API 不兼容。
- 运行成功只覆盖报告中的最小任务，不代表全部功能、平台和配置。
- 自动生成的 LLM 摘要只用于导航，不能替代原始矩阵和日志。

## 仓库结构

| 路径 | 内容 |
|---|---|
| `PLUGINS.md` | 人工分类和登记的精选入口 |
| `reports/<YYYY-MM-DD>/index.md` | 指定日期的完整扫描索引 |
| `reports/<YYYY-MM-DD>/mainline-compat.md` | 指定日期的静态兼容性矩阵 |
| `reports/<YYYY-MM-DD>/compile-compat.md` | 指定日期的编译与语法实验结果 |
| `reports/<YYYY-MM-DD>/runtime-test.md` | 指定日期的运行级测试结果 |
| `CHANGELOG.md` | 日期化生态变更摘要 |
| `docs/SOP.md` | 自动化、构建与报告维护说明 |
| `scripts/` | 发现、检查、测试和渲染脚本 |

<details>
<summary>维护者：README 自动生成约定</summary>

- 人工内容放在自动标记块之外；生成器只替换 `AUTO:ecosystem` 块。
- 首页只输出汇总和报告链接，不输出完整仓库表。
- 新增/修改项最多显示 10 条，其余链接到 `CHANGELOG.md`。
- 仓库链接必须使用扫描结果中的完整 `owner/name`，不得硬编码组织名。
- 自动块使用真实日期路径；另生成普通文件 `reports/LATEST.md` 作为可验证的稳定入口，不依赖目录符号链接。
- 报告缺失、为空或数字校验失败时显示“数据暂不可用”，不得沿用旧值或生成强结论。
- 运行结果与静态结果使用不同字段、不同分母，并展示测试覆盖数。

</details>

## 项目边界与致谢

本仓库维护目录、检测规则和证据报告，不托管第三方插件代码。感谢所有提交插件、复现问题、修正元数据和维护测试链路的贡献者。

当前仓库尚未声明许可证；在复制、修改或再分发目录内容与脚本前，请先向维护者确认授权。维护者应在公开推广前补充明确的 `LICENSE`。
