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

## 当前生态快照

<!-- AUTO:ecosystem:START -->
> 更新于 2026-08-13 22:59 · 每 8 小时刷新 · mainline `7b9644f`

| 证据层 | 当前结果 |
|---|---:|
| 自动收录 | 286 个仓库 |
| 静态综合判定 | 87 兼容 · 31 关注 · 9 需适配 |
| 证据不足 | 140 待调研 |
| 其他 | 13 占位 · 2 不适用 · 4 已删除 |
| 运行级实测 | 0 可用 · 5 失败（共测试 5 个） |
| 正在跟踪的 PR | 11 |

[完整索引](reports/2026-08-13/index.md) · [静态矩阵](reports/2026-08-13/mainline-compat.md) · [编译实验](reports/2026-08-13/compile-compat.md) · [运行实测](reports/2026-08-13/runtime-test.md)

**今日新增 / 修改**（完整变更见 [CHANGELOG](CHANGELOG.md)）

| 仓库 | 类型 |
|---|---|
| [dsh-web-ui-notify](https://github.com/dsh-external/dsh-web-ui-notify) | 🆕 新增 |
| [dsh-web-panel](https://github.com/dsh-external/dsh-web-panel) | 🆕 新增 |
| [dsh-evolve](https://github.com/dsh-external/dsh-evolve) | 🆕 新增 |
| [dsh-island](https://github.com/dsh-external/dsh-island) | 🆕 新增 |
| [dsh-drag-and-drop](https://github.com/dsh-external/dsh-drag-and-drop) | 🆕 新增 |
| [dsh-message-edit](https://github.com/dsh-external/dsh-message-edit) | 🆕 新增 |
| [dsh-deep-research](https://github.com/dsh-external/dsh-deep-research) | 🆕 新增 |
| [dsh-multimedia-webui-input](https://github.com/dsh-external/dsh-multimedia-webui-input) | 🆕 新增 |
| [repo-visibility-guard](https://github.com/dsh-external/repo-visibility-guard) | 🆕 新增 |
| [dsh-grok-tui](https://github.com/dsh-external/dsh-grok-tui) | 🆕 新增 |
| [ds_web_craw](https://github.com/dsh-external/ds_web_craw) | 🆕 新增 |
| [fabric](https://github.com/dsh-external/fabric) | 🆕 新增 |
| [dsh-browser](https://github.com/dsh-external/dsh-browser) | 🆕 新增 |
| [dsh-desktop-mac](https://github.com/dsh-external/dsh-desktop-mac) | 🆕 新增 |
| [dsh-public-repo-monitor](https://github.com/dsh-external/dsh-public-repo-monitor) | 🆕 新增 |
| [dsh-tui](https://github.com/dsh-external/dsh-tui) | 🆕 新增 |
| [dsh-inspect](https://github.com/dsh-external/dsh-inspect) | 🆕 新增 |
| [dsh-hub](https://github.com/dsh-external/dsh-hub) | 🆕 新增 |
| [dsh-alphasolve](https://github.com/dsh-external/dsh-alphasolve) | 🆕 新增 |
| [zotero-wave-rag](https://github.com/dsh-external/zotero-wave-rag) | 🆕 新增 |
| [onboarding](https://github.com/dsh-external/onboarding) | 🆕 新增 |
| [ego-browser](https://github.com/dsh-external/ego-browser) | 🆕 新增 |
| [dsh-nowledge-mem](https://github.com/dsh-external/dsh-nowledge-mem) | 🆕 新增 |
| [dsh-sidechain](https://github.com/dsh-external/dsh-sidechain) | 🆕 新增 |
| [dsh-a2a](https://github.com/dsh-external/dsh-a2a) | 🆕 新增 |
| [dsh-feishu-notify](https://github.com/dsh-external/dsh-feishu-notify) | 🆕 新增 |
| [dsh-remote](https://github.com/dsh-external/dsh-remote) | 🆕 新增 |
| [mstar-workflow](https://github.com/dsh-external/mstar-workflow) | 🆕 新增 |
| [dsh-scholar](https://github.com/dsh-external/dsh-scholar) | 🆕 新增 |
| [dsh-issue-like-skill](https://github.com/dsh-external/dsh-issue-like-skill) | 🆕 新增 |
| [dsh-tool-csv](https://github.com/dsh-external/dsh-tool-csv) | 🆕 新增 |
| [dsh-tool-regex](https://github.com/dsh-external/dsh-tool-regex) | 🆕 新增 |
| [dsh-session-repair-skill](https://github.com/dsh-external/dsh-session-repair-skill) | 🆕 新增 |
| [DSH-better-sidebar](https://github.com/dsh-external/DSH-better-sidebar) | 🆕 新增 |
| [dsh-session-hub](https://github.com/dsh-external/dsh-session-hub) | 🆕 新增 |
| [dsh-ica](https://github.com/dsh-external/dsh-ica) | 🆕 新增 |
| [dsh-advisor](https://github.com/dsh-external/dsh-advisor) | 🆕 新增 |
| [dsh-llm-fallbacks](https://github.com/dsh-external/dsh-llm-fallbacks) | 🆕 新增 |
| [dsh-web-workflow-visualizer](https://github.com/dsh-external/dsh-web-workflow-visualizer) | 🆕 新增 |
| [dsh-checkpoint](https://github.com/dsh-external/dsh-checkpoint) | 🆕 新增 |
| [dsh-rewind](https://github.com/dsh-external/dsh-rewind) | 🆕 新增 |
| [official-plugins-port](https://github.com/dsh-external/official-plugins-port) | 🆕 新增 |
| [oh-my-dsh](https://github.com/dsh-external/oh-my-dsh) | 🆕 新增 |
| [dsh-side-panel](https://github.com/dsh-external/dsh-side-panel) | 🆕 新增 |
| [dsh-profile-bundle-example](https://github.com/dsh-external/dsh-profile-bundle-example) | 🆕 新增 |
| [dsh-plan-execute](https://github.com/dsh-external/dsh-plan-execute) | 🆕 新增 |
| [dsh-paste-input](https://github.com/dsh-external/dsh-paste-input) | 🆕 新增 |
| [zotero-harvest](https://github.com/dsh-external/zotero-harvest) | 🆕 新增 |
| [zephyr](https://github.com/dsh-external/zephyr) | 🆕 新增 |
| [dsh-bash-encoding](https://github.com/dsh-external/dsh-bash-encoding) | 🆕 新增 |
| [dsh-skill-stats](https://github.com/dsh-external/dsh-skill-stats) | 🆕 新增 |
| [dsh-web-archive](https://github.com/dsh-external/dsh-web-archive) | 🆕 新增 |
| [sandbox-micro](https://github.com/dsh-external/sandbox-micro) | 🆕 新增 |
| [dsh-git-identity](https://github.com/dsh-external/dsh-git-identity) | 🆕 新增 |
| [dsh-android](https://github.com/dsh-external/dsh-android) | 🆕 新增 |
| [dsh-lazyfish](https://github.com/dsh-external/dsh-lazyfish) | 🆕 新增 |
| [dsh-auto-approval](https://github.com/dsh-external/dsh-auto-approval) | 🆕 新增 |
| [dsh-input-history](https://github.com/dsh-external/dsh-input-history) | 🆕 新增 |
| [dsh-client-ui-plan-execute](https://github.com/dsh-external/dsh-client-ui-plan-execute) | 🆕 新增 |
| [dsh-stickers](https://github.com/dsh-external/dsh-stickers) | 🆕 新增 |
| [deep-standard-skill](https://github.com/dsh-external/deep-standard-skill) | 🆕 新增 |
| [dsh-serenity-plugin](https://github.com/dsh-external/dsh-serenity-plugin) | 🆕 新增 |
| [dsh-toolkit](https://github.com/dsh-external/dsh-toolkit) | 🆕 新增 |
| [dsh-tool-markdown](https://github.com/dsh-external/dsh-tool-markdown) | 🆕 新增 |
| [dsh-session-health](https://github.com/dsh-external/dsh-session-health) | 🆕 新增 |
| [dsh-desktop-tools](https://github.com/dsh-external/dsh-desktop-tools) | 🆕 新增 |
| [dsh-reuse-first](https://github.com/dsh-external/dsh-reuse-first) | 🆕 新增 |
| [dsh-plus](https://github.com/dsh-external/dsh-plus) | 🆕 新增 |
| [dsh-session-cluster](https://github.com/dsh-external/dsh-session-cluster) | 🆕 新增 |
| [DSH-UI4A](https://github.com/dsh-external/DSH-UI4A) | 🆕 新增 |
| [dsh-visualize](https://github.com/dsh-external/dsh-visualize) | 🆕 新增 |
| [dsh-tps](https://github.com/dsh-external/dsh-tps) | 🆕 新增 |
| [dsh-plugin-check](https://github.com/dsh-external/dsh-plugin-check) | 🆕 新增 |
| [dsh-plugin-dev](https://github.com/dsh-external/dsh-plugin-dev) | 🆕 新增 |
| [dsh-gomoku](https://github.com/dsh-external/dsh-gomoku) | 🆕 新增 |
| [dsh-101](https://github.com/dsh-external/dsh-101) | 🆕 新增 |
| [dsh-turn-rewind](https://github.com/dsh-external/dsh-turn-rewind) | 🆕 新增 |
| [dsh-genui](https://github.com/dsh-external/dsh-genui) | 🆕 新增 |
| [dsh-mygo](https://github.com/dsh-external/dsh-mygo) | 🆕 新增 |
| [cross-harness-cite](https://github.com/dsh-external/cross-harness-cite) | 🆕 新增 |
| [dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | 🆕 新增 |
| [dsh-activity-plugin](https://github.com/dsh-external/dsh-activity-plugin) | 🆕 新增 |
| [dsh-tool-diff](https://github.com/dsh-external/dsh-tool-diff) | 🆕 新增 |
| [dsh-mobileweb-adapter](https://github.com/dsh-external/dsh-mobileweb-adapter) | 🆕 新增 |
| [dsh-desktop-electron](https://github.com/dsh-external/dsh-desktop-electron) | 🆕 新增 |
| [dsh-mineru](https://github.com/dsh-external/dsh-mineru) | 🆕 新增 |
| [dsh-pet](https://github.com/dsh-external/dsh-pet) | 🆕 新增 |
| [dsh-paseo](https://github.com/dsh-external/dsh-paseo) | 🆕 新增 |
| [dsh-superpowers](https://github.com/dsh-external/dsh-superpowers) | 🆕 新增 |
| [dsh-spec-kit](https://github.com/dsh-external/dsh-spec-kit) | 🆕 新增 |
| [dsh-context7](https://github.com/dsh-external/dsh-context7) | 🆕 新增 |
| [dsh-vscode](https://github.com/dsh-external/dsh-vscode) | 🆕 新增 |
| [dsh-tui-front-door](https://github.com/dsh-external/dsh-tui-front-door) | 🆕 新增 |
| [dsh-webbridge](https://github.com/dsh-external/dsh-webbridge) | 🆕 新增 |
| [dsh-custom-css](https://github.com/dsh-external/dsh-custom-css) | 🆕 新增 |
| [tonghuashun-harness](https://github.com/dsh-external/tonghuashun-harness) | 🆕 新增 |
| [dsh-club](https://github.com/dsh-external/dsh-club) | 🆕 新增 |
| [dsh-humanize](https://github.com/dsh-external/dsh-humanize) | 🆕 新增 |
| [dsh-agent-budget](https://github.com/dsh-external/dsh-agent-budget) | 🆕 新增 |
| [dsh-track](https://github.com/dsh-external/dsh-track) | 🆕 新增 |
| [dsh-spur](https://github.com/dsh-external/dsh-spur) | 🆕 新增 |
| [dsh-selection-chat](https://github.com/dsh-external/dsh-selection-chat) | 🆕 新增 |
| [dsh-browser-panel](https://github.com/dsh-external/dsh-browser-panel) | 🆕 新增 |
| [dsh-engram-relay](https://github.com/dsh-external/dsh-engram-relay) | 🆕 新增 |
| [yet-another-subagent](https://github.com/dsh-external/yet-another-subagent) | 🆕 新增 |
| [dsh-voice-chat](https://github.com/dsh-external/dsh-voice-chat) | 🆕 新增 |
| [dsh-ads](https://github.com/dsh-external/dsh-ads) | 🆕 新增 |
| [dsh-skill-session-recovery](https://github.com/dsh-external/dsh-skill-session-recovery) | 🆕 新增 |
| [dsh-tavern-plugin](https://github.com/dsh-external/dsh-tavern-plugin) | 🆕 新增 |
| [dsh-qq2006](https://github.com/dsh-external/dsh-qq2006) | 🆕 新增 |
| [dsh-plugin-guide](https://github.com/dsh-external/dsh-plugin-guide) | 🆕 新增 |
| [dsh-mnemon](https://github.com/dsh-external/dsh-mnemon) | 🆕 新增 |
| [dsh-pet-rs](https://github.com/dsh-external/dsh-pet-rs) | 🆕 新增 |
| [dsh-auto-blame](https://github.com/dsh-external/dsh-auto-blame) | 🆕 新增 |
| [dsh-question-collapse](https://github.com/dsh-external/dsh-question-collapse) | 🆕 新增 |
| [dsh-latex](https://github.com/dsh-external/dsh-latex) | 🆕 新增 |
| [dsh-tool-stat](https://github.com/dsh-external/dsh-tool-stat) | 🆕 新增 |
| [dsh-tool-schema](https://github.com/dsh-external/dsh-tool-schema) | 🆕 新增 |
| [dsh-security-audit](https://github.com/dsh-external/dsh-security-audit) | 🆕 新增 |
| [dsh-browser-bridge](https://github.com/dsh-external/dsh-browser-bridge) | 🆕 新增 |
| [ya-workspace-sidebar](https://github.com/dsh-external/ya-workspace-sidebar) | 🆕 新增 |
| [dsh-d399](https://github.com/dsh-external/dsh-d399) | 🆕 新增 |
| [7d7d](https://github.com/dsh-external/7d7d) | 🆕 新增 |
| [dsh-cordis-rocks](https://github.com/dsh-external/dsh-cordis-rocks) | 🆕 新增 |
| [dsh-sleep](https://github.com/dsh-external/dsh-sleep) | 🆕 新增 |
| [dsh-minigames](https://github.com/dsh-external/dsh-minigames) | 🆕 新增 |
| [sandbox-nono](https://github.com/dsh-external/sandbox-nono) | 🆕 新增 |
| [dsh-auto-chess](https://github.com/dsh-external/dsh-auto-chess) | 🆕 新增 |
| [dshfind](https://github.com/dsh-external/dshfind) | 🆕 新增 |
| [dsh-cyber-sec](https://github.com/dsh-external/dsh-cyber-sec) | 🆕 新增 |
| [dsh-anti-ads](https://github.com/dsh-external/dsh-anti-ads) | 🆕 新增 |
| [dsh-self-control-guard](https://github.com/dsh-external/dsh-self-control-guard) | 🆕 新增 |
| [whale-girl](https://github.com/dsh-external/whale-girl) | 🆕 新增 |
| [dsh-codex-bridge](https://github.com/dsh-external/dsh-codex-bridge) | 🆕 新增 |
| [dsh-kimi-bridge](https://github.com/dsh-external/dsh-kimi-bridge) | 🆕 新增 |
| [session-teleport](https://github.com/dsh-external/session-teleport) | 🆕 新增 |
| [dsh-code-map](https://github.com/dsh-external/dsh-code-map) | 🆕 新增 |
| [dsh-loop](https://github.com/dsh-external/dsh-loop) | 🆕 新增 |
| [dsh-navbar](https://github.com/dsh-external/dsh-navbar) | 🆕 新增 |
| [dsh-task-status](https://github.com/dsh-external/dsh-task-status) | 🆕 新增 |
| [dsh-annotation](https://github.com/dsh-external/dsh-annotation) | 🆕 新增 |
| [dsh-ui-webview](https://github.com/dsh-external/dsh-ui-webview) | 🆕 新增 |
| [dsh-web-review](https://github.com/dsh-external/dsh-web-review) | 🆕 新增 |
| [dsh-cc-connect](https://github.com/dsh-external/dsh-cc-connect) | 🆕 新增 |
| [dsh-focus-chat](https://github.com/dsh-external/dsh-focus-chat) | 🆕 新增 |
| [dsh-build](https://github.com/dsh-external/dsh-build) | 🆕 新增 |
| [oh-my-deepseek](https://github.com/dsh-external/oh-my-deepseek) | 🆕 新增 |
| [dsh-save-intp](https://github.com/dsh-external/dsh-save-intp) | 🆕 新增 |
| [dsh-find-plugins](https://github.com/dsh-external/dsh-find-plugins) | 🆕 新增 |
| [dsh-fkin-vibe](https://github.com/dsh-external/dsh-fkin-vibe) | 🆕 新增 |
| [dsh-harness-ops](https://github.com/dsh-external/dsh-harness-ops) | 🆕 新增 |
| [dsh-vision-toolkit](https://github.com/dsh-external/dsh-vision-toolkit) | 🆕 新增 |
| [Top](https://github.com/dsh-external/Top) | 🆕 新增 |
| [__perm_probe__](https://github.com/dsh-external/__perm_probe__) | 🆕 新增 |
| [dsh-kimi-browser](https://github.com/dsh-external/dsh-kimi-browser) | 🆕 新增 |
| [dsh-edu](https://github.com/dsh-external/dsh-edu) | 🆕 新增 |
| [dsh-ohos-patch](https://github.com/dsh-external/dsh-ohos-patch) | 🆕 新增 |
| [oh-dsh-desktop](https://github.com/dsh-external/oh-dsh-desktop) | 🆕 新增 |
| [dsh-plugin-skills](https://github.com/dsh-external/dsh-plugin-skills) | 🆕 新增 |
| [dsh-deep-whale](https://github.com/dsh-external/dsh-deep-whale) | 🆕 新增 |
| [dsh-tool-search](https://github.com/dsh-external/dsh-tool-search) | 🆕 新增 |
| [oh-my-dsh-distribution](https://github.com/dsh-external/oh-my-dsh-distribution) | 🆕 新增 |
| [dsh-memory](https://github.com/dsh-external/dsh-memory) | 🆕 新增 |
| [dsh-chat](https://github.com/dsh-external/dsh-chat) | 🆕 新增 |
| [dsh-web](https://github.com/dsh-external/dsh-web) | 🆕 新增 |
| [dsh_ide](https://github.com/dsh-external/dsh_ide) | 🆕 新增 |
| [dsh-trace](https://github.com/dsh-external/dsh-trace) | 🆕 新增 |
| [deepseek-manners](https://github.com/dsh-external/deepseek-manners) | 🆕 新增 |
| [plugin-template](https://github.com/dsh-external/plugin-template) | 🆕 新增 |
| [dsh-design](https://github.com/dsh-external/dsh-design) | 🆕 新增 |
| [dsh-computer-use](https://github.com/dsh-external/dsh-computer-use) | 🆕 新增 |
| [dsh-meme](https://github.com/dsh-external/dsh-meme) | 🆕 新增 |
| [dsh-agent-rp](https://github.com/dsh-external/dsh-agent-rp) | 🆕 新增 |
| [dsh-music-player](https://github.com/dsh-external/dsh-music-player) | 🆕 新增 |
| [dsh-multica-runtime](https://github.com/dsh-external/dsh-multica-runtime) | 🆕 新增 |
| [dsh-mega](https://github.com/dsh-external/dsh-mega) | 🆕 新增 |
| [dsh-office](https://github.com/dsh-external/dsh-office) | 🆕 新增 |
| [savemoneybenchmark](https://github.com/dsh-external/savemoneybenchmark) | 🆕 新增 |
| [dsh-slice-agent-loop](https://github.com/dsh-external/dsh-slice-agent-loop) | 🆕 新增 |
| [dsh-kb-sieve](https://github.com/dsh-external/dsh-kb-sieve) | 🆕 新增 |
| [dsh-data-agent](https://github.com/dsh-external/dsh-data-agent) | 🆕 新增 |
| [dsh-security](https://github.com/dsh-external/dsh-security) | 🆕 新增 |
| [dsh-teamwork](https://github.com/dsh-external/dsh-teamwork) | 🆕 新增 |
| [ui-status-label](https://github.com/dsh-external/ui-status-label) | 🆕 新增 |
| [dsh-easy-ctx-manager](https://github.com/dsh-external/dsh-easy-ctx-manager) | 🆕 新增 |
| [browser4-dsh](https://github.com/dsh-external/browser4-dsh) | 🆕 新增 |
| [show-bash-command](https://github.com/dsh-external/show-bash-command) | 🆕 新增 |
| [dsh-chat-thumb](https://github.com/dsh-external/dsh-chat-thumb) | 🆕 新增 |
| [dsh-super-injector](https://github.com/dsh-external/dsh-super-injector) | 🆕 新增 |
| [dsh-hmz](https://github.com/dsh-external/dsh-hmz) | 🆕 新增 |
| [dsh-better-sidebar-plugin-office](https://github.com/dsh-external/dsh-better-sidebar-plugin-office) | 🆕 新增 |
| [dsh-explain](https://github.com/dsh-external/dsh-explain) | 🆕 新增 |
| [dsh-interpreters](https://github.com/dsh-external/dsh-interpreters) | 🆕 新增 |
| [dsh-stock-market](https://github.com/dsh-external/dsh-stock-market) | 🆕 新增 |
| [dsh-scout](https://github.com/dsh-external/dsh-scout) | 🆕 新增 |
| [dsh-diff-viewer](https://github.com/dsh-external/dsh-diff-viewer) | 🆕 新增 |
| [dsh-turn-navigator](https://github.com/dsh-external/dsh-turn-navigator) | 🆕 新增 |
| [dsh-mobile](https://github.com/dsh-external/dsh-mobile) | 🆕 新增 |
| [dsh-share](https://github.com/dsh-external/dsh-share) | 🆕 新增 |
| [dsh-travel-plugin](https://github.com/dsh-external/dsh-travel-plugin) | 🆕 新增 |
| [dsh-suggested-replies](https://github.com/dsh-external/dsh-suggested-replies) | 🆕 新增 |
| [dsh-aigc-canvas](https://github.com/dsh-external/dsh-aigc-canvas) | 🆕 新增 |
| [dsh-sonar](https://github.com/dsh-external/dsh-sonar) | 🆕 新增 |
| [dsh-ultra-ui](https://github.com/dsh-external/dsh-ultra-ui) | 🆕 新增 |
| [dsh-deepresearch](https://github.com/dsh-external/dsh-deepresearch) | 🆕 新增 |
| [dsh-notebooks](https://github.com/dsh-external/dsh-notebooks) | 🆕 新增 |
| [context-doctor](https://github.com/dsh-external/context-doctor) | 🆕 新增 |
| [dsh-openpencil](https://github.com/dsh-external/dsh-openpencil) | 🆕 新增 |
| [dsh-deeplink](https://github.com/dsh-external/dsh-deeplink) | 🆕 新增 |
| [dsh-cot-summary](https://github.com/dsh-external/dsh-cot-summary) | 🆕 新增 |
| [dsh-emoji](https://github.com/dsh-external/dsh-emoji) | 🆕 新增 |
| [dsh_workflow](https://github.com/dsh-external/dsh_workflow) | 🆕 新增 |
| [dsh-openmaic](https://github.com/dsh-external/dsh-openmaic) | 🆕 新增 |
| [dsh-deepcel](https://github.com/dsh-external/dsh-deepcel) | 🆕 新增 |
| [dsh-STAR](https://github.com/dsh-external/dsh-STAR) | 🆕 新增 |
| [dsh-STAGE](https://github.com/dsh-external/dsh-STAGE) | 🆕 新增 |
| [dsh-conversation-share](https://github.com/dsh-external/dsh-conversation-share) | 🆕 新增 |
| [tonghuashun-webui](https://github.com/dsh-external/tonghuashun-webui) | 🆕 新增 |
| [dsh-session-notification](https://github.com/dsh-external/dsh-session-notification) | 🆕 新增 |
| [dsh-custom-tool](https://github.com/dsh-external/dsh-custom-tool) | 🆕 新增 |
| [dsh-openbiliclaw](https://github.com/dsh-external/dsh-openbiliclaw) | 🆕 新增 |
| [dsh-longbridge](https://github.com/dsh-external/dsh-longbridge) | 🆕 新增 |
| [dsh-dzcf](https://github.com/dsh-external/dsh-dzcf) | 🆕 新增 |
| [chat-width](https://github.com/dsh-external/chat-width) | ✏️ 修改 |
| [deepseek-harness-desktop](https://github.com/dsh-external/deepseek-harness-desktop) | ✏️ 修改 |
| [deepseek-harness-distro](https://github.com/dsh-external/deepseek-harness-distro) | ✏️ 修改 |
| [distill](https://github.com/dsh-external/distill) | ✏️ 修改 |
| [dsh-acp](https://github.com/dsh-external/dsh-acp) | ✏️ 修改 |
| [dsh-agent-session-sources](https://github.com/dsh-external/dsh-agent-session-sources) | ✏️ 修改 |
| [dsh-artifact](https://github.com/dsh-external/dsh-artifact) | ✏️ 修改 |
| [dsh-cc-tui](https://github.com/dsh-external/dsh-cc-tui) | ✏️ 修改 |
| [dsh-coding-receipt](https://github.com/dsh-external/dsh-coding-receipt) | ✏️ 修改 |
| [dsh-companion](https://github.com/dsh-external/dsh-companion) | ✏️ 修改 |
| [dsh-cordis-examples](https://github.com/dsh-external/dsh-cordis-examples) | ✏️ 修改 |
| [dsh-desktop](https://github.com/dsh-external/dsh-desktop) | ✏️ 修改 |
| [dsh-feishu-bot](https://github.com/dsh-external/dsh-feishu-bot) | ✏️ 修改 |
| [dsh-gh-bridge](https://github.com/dsh-external/dsh-gh-bridge) | ✏️ 修改 |
| [dsh-github-integration](https://github.com/dsh-external/dsh-github-integration) | ✏️ 修改 |
| [dsh-issue-filer](https://github.com/dsh-external/dsh-issue-filer) | ✏️ 修改 |
| [dsh-live-stats](https://github.com/dsh-external/dsh-live-stats) | ✏️ 修改 |
| [dsh-memory-evolve](https://github.com/dsh-external/dsh-memory-evolve) | ✏️ 修改 |
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | ✏️ 修改 |
| [dsh-opencode-server](https://github.com/dsh-external/dsh-opencode-server) | ✏️ 修改 |
| [dsh-pi-adapter](https://github.com/dsh-external/dsh-pi-adapter) | ✏️ 修改 |
| [dsh-prompt-studio](https://github.com/dsh-external/dsh-prompt-studio) | ✏️ 修改 |
| [dsh-pty-windows](https://github.com/dsh-external/dsh-pty-windows) | ✏️ 修改 |
| [dsh-session-search](https://github.com/dsh-external/dsh-session-search) | ✏️ 修改 |
| [dsh-sfw](https://github.com/dsh-external/dsh-sfw) | ✏️ 修改 |
| [dsh-shell-windows](https://github.com/dsh-external/dsh-shell-windows) | ✏️ 修改 |
| [dsh-skills-manager](https://github.com/dsh-external/dsh-skills-manager) | ✏️ 修改 |
| [dsh-skins](https://github.com/dsh-external/dsh-skins) | ✏️ 修改 |
| [dsh-subagent-tree](https://github.com/dsh-external/dsh-subagent-tree) | ✏️ 修改 |
| [dsh-tool-browser](https://github.com/dsh-external/dsh-tool-browser) | ✏️ 修改 |
| [dsh-tool-calculator](https://github.com/dsh-external/dsh-tool-calculator) | ✏️ 修改 |
| [dsh-tool-encoding](https://github.com/dsh-external/dsh-tool-encoding) | ✏️ 修改 |
| [dsh-tool-json](https://github.com/dsh-external/dsh-tool-json) | ✏️ 修改 |
| [dsh-tool-time](https://github.com/dsh-external/dsh-tool-time) | ✏️ 修改 |
| [dsh-ui-progress](https://github.com/dsh-external/dsh-ui-progress) | ✏️ 修改 |
| [dsh-ui-whale](https://github.com/dsh-external/dsh-ui-whale) | ✏️ 修改 |
| [dsh-vision](https://github.com/dsh-external/dsh-vision) | ✏️ 修改 |
| [dsh-web-terminal](https://github.com/dsh-external/dsh-web-terminal) | ✏️ 修改 |
| [dsh-web-ui-approval-notify](https://github.com/dsh-external/dsh-web-ui-approval-notify) | ✏️ 修改 |
| [dsh-web-ui](https://github.com/dsh-external/dsh-web-ui) | ✏️ 修改 |
| [dsh-wecom-bot](https://github.com/dsh-external/dsh-wecom-bot) | ✏️ 修改 |
| [dsh-weixin-bot](https://github.com/dsh-external/dsh-weixin-bot) | ✏️ 修改 |
| [dsh-win-port](https://github.com/dsh-external/dsh-win-port) | ✏️ 修改 |
| [dsh-working-activity](https://github.com/dsh-external/dsh-working-activity) | ✏️ 修改 |
| [dshx-update-check](https://github.com/dsh-external/dshx-update-check) | ✏️ 修改 |
| [ex-setting](https://github.com/dsh-external/ex-setting) | ✏️ 修改 |
| [group-chat-diary](https://github.com/dsh-external/group-chat-diary) | ✏️ 修改 |
| [hub](https://github.com/dsh-external/hub) | ✏️ 修改 |
| [issues](https://github.com/dsh-external/issues) | ✏️ 修改 |
| [marisa](https://github.com/dsh-external/marisa) | ✏️ 修改 |
| [plugin-registry](https://github.com/dsh-external/plugin-registry) | ✏️ 修改 |
| [qqbot](https://github.com/dsh-external/qqbot) | ✏️ 修改 |
| [Qwen-MM-Plugins](https://github.com/dsh-external/Qwen-MM-Plugins) | ✏️ 修改 |
| [Recall](https://github.com/dsh-external/Recall) | ✏️ 修改 |
| [review-panel](https://github.com/dsh-external/review-panel) | ✏️ 修改 |
| [sandbox-mxc](https://github.com/dsh-external/sandbox-mxc) | ✏️ 修改 |
| [session-chatlog](https://github.com/dsh-external/session-chatlog) | ✏️ 修改 |
| [session-persistence-rdb](https://github.com/dsh-external/session-persistence-rdb) | ✏️ 修改 |
| [telegram](https://github.com/dsh-external/telegram) | ✏️ 修改 |
| [tg-bot](https://github.com/dsh-external/tg-bot) | ✏️ 修改 |
| [toybox](https://github.com/dsh-external/toybox) | ✏️ 修改 |
| [turtle-ui](https://github.com/dsh-external/turtle-ui) | ✏️ 修改 |
| [web-components](https://github.com/dsh-external/web-components) | ✏️ 修改 |
| [dsh-web-ui-notify](https://github.com/dsh-external/dsh-web-ui-notify) | ✏️ 修改 |
| [dsh-web-panel](https://github.com/dsh-external/dsh-web-panel) | ✏️ 修改 |
| [dsh-evolve](https://github.com/dsh-external/dsh-evolve) | ✏️ 修改 |
| [dsh-island](https://github.com/dsh-external/dsh-island) | ✏️ 修改 |
| [dsh-drag-and-drop](https://github.com/dsh-external/dsh-drag-and-drop) | ✏️ 修改 |
| [dsh-message-edit](https://github.com/dsh-external/dsh-message-edit) | ✏️ 修改 |
| [dsh-deep-research](https://github.com/dsh-external/dsh-deep-research) | ✏️ 修改 |
| [dsh-multimedia-webui-input](https://github.com/dsh-external/dsh-multimedia-webui-input) | ✏️ 修改 |
| [repo-visibility-guard](https://github.com/dsh-external/repo-visibility-guard) | ✏️ 修改 |
| [dsh-grok-tui](https://github.com/dsh-external/dsh-grok-tui) | ✏️ 修改 |
| [ds_web_craw](https://github.com/dsh-external/ds_web_craw) | ✏️ 修改 |
| [fabric](https://github.com/dsh-external/fabric) | ✏️ 修改 |
| [dsh-browser](https://github.com/dsh-external/dsh-browser) | ✏️ 修改 |
| [dsh-desktop-mac](https://github.com/dsh-external/dsh-desktop-mac) | ✏️ 修改 |
| [dsh-public-repo-monitor](https://github.com/dsh-external/dsh-public-repo-monitor) | ✏️ 修改 |
| [dsh-tui](https://github.com/dsh-external/dsh-tui) | ✏️ 修改 |
| [dsh-inspect](https://github.com/dsh-external/dsh-inspect) | ✏️ 修改 |
| [dsh-hub](https://github.com/dsh-external/dsh-hub) | ✏️ 修改 |
| [dsh-alphasolve](https://github.com/dsh-external/dsh-alphasolve) | ✏️ 修改 |
| [zotero-wave-rag](https://github.com/dsh-external/zotero-wave-rag) | ✏️ 修改 |
| [onboarding](https://github.com/dsh-external/onboarding) | ✏️ 修改 |
| [ego-browser](https://github.com/dsh-external/ego-browser) | ✏️ 修改 |
| [dsh-nowledge-mem](https://github.com/dsh-external/dsh-nowledge-mem) | ✏️ 修改 |
| [dsh-sidechain](https://github.com/dsh-external/dsh-sidechain) | ✏️ 修改 |
| [dsh-a2a](https://github.com/dsh-external/dsh-a2a) | ✏️ 修改 |
| [dsh-feishu-notify](https://github.com/dsh-external/dsh-feishu-notify) | ✏️ 修改 |
| [dsh-remote](https://github.com/dsh-external/dsh-remote) | ✏️ 修改 |
| [mstar-workflow](https://github.com/dsh-external/mstar-workflow) | ✏️ 修改 |
| [dsh-scholar](https://github.com/dsh-external/dsh-scholar) | ✏️ 修改 |
| [dsh-issue-like-skill](https://github.com/dsh-external/dsh-issue-like-skill) | ✏️ 修改 |
| [dsh-tool-csv](https://github.com/dsh-external/dsh-tool-csv) | ✏️ 修改 |
| [dsh-tool-regex](https://github.com/dsh-external/dsh-tool-regex) | ✏️ 修改 |
| [dsh-session-repair-skill](https://github.com/dsh-external/dsh-session-repair-skill) | ✏️ 修改 |
| [DSH-better-sidebar](https://github.com/dsh-external/DSH-better-sidebar) | ✏️ 修改 |
| [dsh-session-hub](https://github.com/dsh-external/dsh-session-hub) | ✏️ 修改 |
| [dsh-ica](https://github.com/dsh-external/dsh-ica) | ✏️ 修改 |
| [dsh-advisor](https://github.com/dsh-external/dsh-advisor) | ✏️ 修改 |
| [dsh-llm-fallbacks](https://github.com/dsh-external/dsh-llm-fallbacks) | ✏️ 修改 |
| [dsh-web-workflow-visualizer](https://github.com/dsh-external/dsh-web-workflow-visualizer) | ✏️ 修改 |
| [dsh-checkpoint](https://github.com/dsh-external/dsh-checkpoint) | ✏️ 修改 |
| [dsh-rewind](https://github.com/dsh-external/dsh-rewind) | ✏️ 修改 |
| [official-plugins-port](https://github.com/dsh-external/official-plugins-port) | ✏️ 修改 |
| [oh-my-dsh](https://github.com/dsh-external/oh-my-dsh) | ✏️ 修改 |
| [dsh-side-panel](https://github.com/dsh-external/dsh-side-panel) | ✏️ 修改 |
| [dsh-profile-bundle-example](https://github.com/dsh-external/dsh-profile-bundle-example) | ✏️ 修改 |
| [dsh-plan-execute](https://github.com/dsh-external/dsh-plan-execute) | ✏️ 修改 |
| [dsh-paste-input](https://github.com/dsh-external/dsh-paste-input) | ✏️ 修改 |
| [zotero-harvest](https://github.com/dsh-external/zotero-harvest) | ✏️ 修改 |
| [zephyr](https://github.com/dsh-external/zephyr) | ✏️ 修改 |
| [dsh-bash-encoding](https://github.com/dsh-external/dsh-bash-encoding) | ✏️ 修改 |
| [dsh-skill-stats](https://github.com/dsh-external/dsh-skill-stats) | ✏️ 修改 |
| [dsh-web-archive](https://github.com/dsh-external/dsh-web-archive) | ✏️ 修改 |
| [sandbox-micro](https://github.com/dsh-external/sandbox-micro) | ✏️ 修改 |
| [dsh-git-identity](https://github.com/dsh-external/dsh-git-identity) | ✏️ 修改 |
| [dsh-android](https://github.com/dsh-external/dsh-android) | ✏️ 修改 |
| [dsh-lazyfish](https://github.com/dsh-external/dsh-lazyfish) | ✏️ 修改 |
| [dsh-auto-approval](https://github.com/dsh-external/dsh-auto-approval) | ✏️ 修改 |
| [dsh-input-history](https://github.com/dsh-external/dsh-input-history) | ✏️ 修改 |
| [dsh-client-ui-plan-execute](https://github.com/dsh-external/dsh-client-ui-plan-execute) | ✏️ 修改 |
| [dsh-stickers](https://github.com/dsh-external/dsh-stickers) | ✏️ 修改 |
| [deep-standard-skill](https://github.com/dsh-external/deep-standard-skill) | ✏️ 修改 |
| [dsh-serenity-plugin](https://github.com/dsh-external/dsh-serenity-plugin) | ✏️ 修改 |
| [dsh-toolkit](https://github.com/dsh-external/dsh-toolkit) | ✏️ 修改 |
| [dsh-tool-markdown](https://github.com/dsh-external/dsh-tool-markdown) | ✏️ 修改 |
| [dsh-session-health](https://github.com/dsh-external/dsh-session-health) | ✏️ 修改 |
| [dsh-desktop-tools](https://github.com/dsh-external/dsh-desktop-tools) | ✏️ 修改 |
| [dsh-reuse-first](https://github.com/dsh-external/dsh-reuse-first) | ✏️ 修改 |
| [dsh-plus](https://github.com/dsh-external/dsh-plus) | ✏️ 修改 |
| [dsh-session-cluster](https://github.com/dsh-external/dsh-session-cluster) | ✏️ 修改 |
| [DSH-UI4A](https://github.com/dsh-external/DSH-UI4A) | ✏️ 修改 |
| [dsh-visualize](https://github.com/dsh-external/dsh-visualize) | ✏️ 修改 |
| [dsh-tps](https://github.com/dsh-external/dsh-tps) | ✏️ 修改 |
| [dsh-plugin-check](https://github.com/dsh-external/dsh-plugin-check) | ✏️ 修改 |
| [dsh-plugin-dev](https://github.com/dsh-external/dsh-plugin-dev) | ✏️ 修改 |
| [dsh-gomoku](https://github.com/dsh-external/dsh-gomoku) | ✏️ 修改 |
| [dsh-101](https://github.com/dsh-external/dsh-101) | ✏️ 修改 |
| [dsh-turn-rewind](https://github.com/dsh-external/dsh-turn-rewind) | ✏️ 修改 |
| [dsh-genui](https://github.com/dsh-external/dsh-genui) | ✏️ 修改 |
| [dsh-mygo](https://github.com/dsh-external/dsh-mygo) | ✏️ 修改 |
| [cross-harness-cite](https://github.com/dsh-external/cross-harness-cite) | ✏️ 修改 |
| [dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | ✏️ 修改 |
| [dsh-activity-plugin](https://github.com/dsh-external/dsh-activity-plugin) | ✏️ 修改 |
| [dsh-tool-diff](https://github.com/dsh-external/dsh-tool-diff) | ✏️ 修改 |
| [dsh-mobileweb-adapter](https://github.com/dsh-external/dsh-mobileweb-adapter) | ✏️ 修改 |
| [dsh-desktop-electron](https://github.com/dsh-external/dsh-desktop-electron) | ✏️ 修改 |
| [dsh-mineru](https://github.com/dsh-external/dsh-mineru) | ✏️ 修改 |
| [dsh-pet](https://github.com/dsh-external/dsh-pet) | ✏️ 修改 |
| [dsh-paseo](https://github.com/dsh-external/dsh-paseo) | ✏️ 修改 |
| [dsh-superpowers](https://github.com/dsh-external/dsh-superpowers) | ✏️ 修改 |
| [dsh-spec-kit](https://github.com/dsh-external/dsh-spec-kit) | ✏️ 修改 |
| [dsh-context7](https://github.com/dsh-external/dsh-context7) | ✏️ 修改 |
| [dsh-vscode](https://github.com/dsh-external/dsh-vscode) | ✏️ 修改 |
| [dsh-tui-front-door](https://github.com/dsh-external/dsh-tui-front-door) | ✏️ 修改 |
| [dsh-webbridge](https://github.com/dsh-external/dsh-webbridge) | ✏️ 修改 |
| [dsh-custom-css](https://github.com/dsh-external/dsh-custom-css) | ✏️ 修改 |
| [tonghuashun-harness](https://github.com/dsh-external/tonghuashun-harness) | ✏️ 修改 |
| [dsh-club](https://github.com/dsh-external/dsh-club) | ✏️ 修改 |
| [dsh-humanize](https://github.com/dsh-external/dsh-humanize) | ✏️ 修改 |
| [dsh-agent-budget](https://github.com/dsh-external/dsh-agent-budget) | ✏️ 修改 |
| [dsh-track](https://github.com/dsh-external/dsh-track) | ✏️ 修改 |
| [dsh-spur](https://github.com/dsh-external/dsh-spur) | ✏️ 修改 |
| [dsh-selection-chat](https://github.com/dsh-external/dsh-selection-chat) | ✏️ 修改 |
| [dsh-browser-panel](https://github.com/dsh-external/dsh-browser-panel) | ✏️ 修改 |
| [dsh-engram-relay](https://github.com/dsh-external/dsh-engram-relay) | ✏️ 修改 |
| [yet-another-subagent](https://github.com/dsh-external/yet-another-subagent) | ✏️ 修改 |
| [dsh-voice-chat](https://github.com/dsh-external/dsh-voice-chat) | ✏️ 修改 |
| [dsh-ads](https://github.com/dsh-external/dsh-ads) | ✏️ 修改 |
| [dsh-skill-session-recovery](https://github.com/dsh-external/dsh-skill-session-recovery) | ✏️ 修改 |
| [dsh-tavern-plugin](https://github.com/dsh-external/dsh-tavern-plugin) | ✏️ 修改 |
| [dsh-qq2006](https://github.com/dsh-external/dsh-qq2006) | ✏️ 修改 |
| [dsh-plugin-guide](https://github.com/dsh-external/dsh-plugin-guide) | ✏️ 修改 |
| [dsh-mnemon](https://github.com/dsh-external/dsh-mnemon) | ✏️ 修改 |
| [dsh-pet-rs](https://github.com/dsh-external/dsh-pet-rs) | ✏️ 修改 |
| [dsh-auto-blame](https://github.com/dsh-external/dsh-auto-blame) | ✏️ 修改 |
| [dsh-question-collapse](https://github.com/dsh-external/dsh-question-collapse) | ✏️ 修改 |
| [dsh-latex](https://github.com/dsh-external/dsh-latex) | ✏️ 修改 |
| [dsh-tool-stat](https://github.com/dsh-external/dsh-tool-stat) | ✏️ 修改 |
| [dsh-tool-schema](https://github.com/dsh-external/dsh-tool-schema) | ✏️ 修改 |
| [dsh-security-audit](https://github.com/dsh-external/dsh-security-audit) | ✏️ 修改 |
| [dsh-browser-bridge](https://github.com/dsh-external/dsh-browser-bridge) | ✏️ 修改 |
| [ya-workspace-sidebar](https://github.com/dsh-external/ya-workspace-sidebar) | ✏️ 修改 |
| [dsh-d399](https://github.com/dsh-external/dsh-d399) | ✏️ 修改 |
| [7d7d](https://github.com/dsh-external/7d7d) | ✏️ 修改 |
| [dsh-cordis-rocks](https://github.com/dsh-external/dsh-cordis-rocks) | ✏️ 修改 |
| [dsh-sleep](https://github.com/dsh-external/dsh-sleep) | ✏️ 修改 |
| [dsh-minigames](https://github.com/dsh-external/dsh-minigames) | ✏️ 修改 |
| [sandbox-nono](https://github.com/dsh-external/sandbox-nono) | ✏️ 修改 |
| [dsh-auto-chess](https://github.com/dsh-external/dsh-auto-chess) | ✏️ 修改 |
| [dshfind](https://github.com/dsh-external/dshfind) | ✏️ 修改 |
| [dsh-cyber-sec](https://github.com/dsh-external/dsh-cyber-sec) | ✏️ 修改 |
| [dsh-anti-ads](https://github.com/dsh-external/dsh-anti-ads) | ✏️ 修改 |
| [dsh-self-control-guard](https://github.com/dsh-external/dsh-self-control-guard) | ✏️ 修改 |
| [whale-girl](https://github.com/dsh-external/whale-girl) | ✏️ 修改 |
| [dsh-codex-bridge](https://github.com/dsh-external/dsh-codex-bridge) | ✏️ 修改 |
| [dsh-kimi-bridge](https://github.com/dsh-external/dsh-kimi-bridge) | ✏️ 修改 |
| [session-teleport](https://github.com/dsh-external/session-teleport) | ✏️ 修改 |
| [dsh-code-map](https://github.com/dsh-external/dsh-code-map) | ✏️ 修改 |
| [dsh-loop](https://github.com/dsh-external/dsh-loop) | ✏️ 修改 |
| [dsh-navbar](https://github.com/dsh-external/dsh-navbar) | ✏️ 修改 |
| [dsh-task-status](https://github.com/dsh-external/dsh-task-status) | ✏️ 修改 |
| [dsh-annotation](https://github.com/dsh-external/dsh-annotation) | ✏️ 修改 |
| [dsh-ui-webview](https://github.com/dsh-external/dsh-ui-webview) | ✏️ 修改 |
| [dsh-web-review](https://github.com/dsh-external/dsh-web-review) | ✏️ 修改 |
| [dsh-cc-connect](https://github.com/dsh-external/dsh-cc-connect) | ✏️ 修改 |
| [dsh-focus-chat](https://github.com/dsh-external/dsh-focus-chat) | ✏️ 修改 |
| [dsh-build](https://github.com/dsh-external/dsh-build) | ✏️ 修改 |
| [oh-my-deepseek](https://github.com/dsh-external/oh-my-deepseek) | ✏️ 修改 |
| [dsh-save-intp](https://github.com/dsh-external/dsh-save-intp) | ✏️ 修改 |
| [dsh-find-plugins](https://github.com/dsh-external/dsh-find-plugins) | ✏️ 修改 |
| [dsh-fkin-vibe](https://github.com/dsh-external/dsh-fkin-vibe) | ✏️ 修改 |
| [dsh-harness-ops](https://github.com/dsh-external/dsh-harness-ops) | ✏️ 修改 |
| [dsh-vision-toolkit](https://github.com/dsh-external/dsh-vision-toolkit) | ✏️ 修改 |
| [Top](https://github.com/dsh-external/Top) | ✏️ 修改 |
| [__perm_probe__](https://github.com/dsh-external/__perm_probe__) | ✏️ 修改 |
| [dsh-kimi-browser](https://github.com/dsh-external/dsh-kimi-browser) | ✏️ 修改 |
| [dsh-edu](https://github.com/dsh-external/dsh-edu) | ✏️ 修改 |
| [dsh-ohos-patch](https://github.com/dsh-external/dsh-ohos-patch) | ✏️ 修改 |
| [oh-dsh-desktop](https://github.com/dsh-external/oh-dsh-desktop) | ✏️ 修改 |
| [dsh-plugin-skills](https://github.com/dsh-external/dsh-plugin-skills) | ✏️ 修改 |
| [dsh-deep-whale](https://github.com/dsh-external/dsh-deep-whale) | ✏️ 修改 |
| [dsh-tool-search](https://github.com/dsh-external/dsh-tool-search) | ✏️ 修改 |
| [oh-my-dsh-distribution](https://github.com/dsh-external/oh-my-dsh-distribution) | ✏️ 修改 |
| [dsh-memory](https://github.com/dsh-external/dsh-memory) | ✏️ 修改 |
| [dsh-chat](https://github.com/dsh-external/dsh-chat) | ✏️ 修改 |
| [dsh-web](https://github.com/dsh-external/dsh-web) | ✏️ 修改 |
| [dsh_ide](https://github.com/dsh-external/dsh_ide) | ✏️ 修改 |
| [dsh-trace](https://github.com/dsh-external/dsh-trace) | ✏️ 修改 |
| [deepseek-manners](https://github.com/dsh-external/deepseek-manners) | ✏️ 修改 |
| [plugin-template](https://github.com/dsh-external/plugin-template) | ✏️ 修改 |
| [dsh-design](https://github.com/dsh-external/dsh-design) | ✏️ 修改 |
| [dsh-computer-use](https://github.com/dsh-external/dsh-computer-use) | ✏️ 修改 |
| [dsh-meme](https://github.com/dsh-external/dsh-meme) | ✏️ 修改 |
| [dsh-agent-rp](https://github.com/dsh-external/dsh-agent-rp) | ✏️ 修改 |
| [dsh-music-player](https://github.com/dsh-external/dsh-music-player) | ✏️ 修改 |
| [dsh-multica-runtime](https://github.com/dsh-external/dsh-multica-runtime) | ✏️ 修改 |
| [dsh-mega](https://github.com/dsh-external/dsh-mega) | ✏️ 修改 |
| [dsh-office](https://github.com/dsh-external/dsh-office) | ✏️ 修改 |
| [savemoneybenchmark](https://github.com/dsh-external/savemoneybenchmark) | ✏️ 修改 |
| [dsh-slice-agent-loop](https://github.com/dsh-external/dsh-slice-agent-loop) | ✏️ 修改 |
| [dsh-kb-sieve](https://github.com/dsh-external/dsh-kb-sieve) | ✏️ 修改 |
| [dsh-data-agent](https://github.com/dsh-external/dsh-data-agent) | ✏️ 修改 |
| [dsh-security](https://github.com/dsh-external/dsh-security) | ✏️ 修改 |
| [dsh-teamwork](https://github.com/dsh-external/dsh-teamwork) | ✏️ 修改 |
| [ui-status-label](https://github.com/dsh-external/ui-status-label) | ✏️ 修改 |
| [dsh-easy-ctx-manager](https://github.com/dsh-external/dsh-easy-ctx-manager) | ✏️ 修改 |
| [browser4-dsh](https://github.com/dsh-external/browser4-dsh) | ✏️ 修改 |
| [show-bash-command](https://github.com/dsh-external/show-bash-command) | ✏️ 修改 |
| [dsh-chat-thumb](https://github.com/dsh-external/dsh-chat-thumb) | ✏️ 修改 |
| [dsh-super-injector](https://github.com/dsh-external/dsh-super-injector) | ✏️ 修改 |
| [dsh-hmz](https://github.com/dsh-external/dsh-hmz) | ✏️ 修改 |
| [dsh-better-sidebar-plugin-office](https://github.com/dsh-external/dsh-better-sidebar-plugin-office) | ✏️ 修改 |
| [dsh-explain](https://github.com/dsh-external/dsh-explain) | ✏️ 修改 |
| [dsh-interpreters](https://github.com/dsh-external/dsh-interpreters) | ✏️ 修改 |
| [dsh-stock-market](https://github.com/dsh-external/dsh-stock-market) | ✏️ 修改 |
| [dsh-scout](https://github.com/dsh-external/dsh-scout) | ✏️ 修改 |
| [dsh-diff-viewer](https://github.com/dsh-external/dsh-diff-viewer) | ✏️ 修改 |
| [dsh-turn-navigator](https://github.com/dsh-external/dsh-turn-navigator) | ✏️ 修改 |
| [dsh-mobile](https://github.com/dsh-external/dsh-mobile) | ✏️ 修改 |
| [dsh-share](https://github.com/dsh-external/dsh-share) | ✏️ 修改 |
| [dsh-travel-plugin](https://github.com/dsh-external/dsh-travel-plugin) | ✏️ 修改 |
| [dsh-suggested-replies](https://github.com/dsh-external/dsh-suggested-replies) | ✏️ 修改 |
| [dsh-aigc-canvas](https://github.com/dsh-external/dsh-aigc-canvas) | ✏️ 修改 |
| [dsh-sonar](https://github.com/dsh-external/dsh-sonar) | ✏️ 修改 |
| [dsh-ultra-ui](https://github.com/dsh-external/dsh-ultra-ui) | ✏️ 修改 |
| [dsh-deepresearch](https://github.com/dsh-external/dsh-deepresearch) | ✏️ 修改 |
| [dsh-notebooks](https://github.com/dsh-external/dsh-notebooks) | ✏️ 修改 |
| [context-doctor](https://github.com/dsh-external/context-doctor) | ✏️ 修改 |
| [dsh-openpencil](https://github.com/dsh-external/dsh-openpencil) | ✏️ 修改 |
| [dsh-deeplink](https://github.com/dsh-external/dsh-deeplink) | ✏️ 修改 |
| [dsh-cot-summary](https://github.com/dsh-external/dsh-cot-summary) | ✏️ 修改 |
| [dsh-emoji](https://github.com/dsh-external/dsh-emoji) | ✏️ 修改 |
| [dsh_workflow](https://github.com/dsh-external/dsh_workflow) | ✏️ 修改 |
| [dsh-openmaic](https://github.com/dsh-external/dsh-openmaic) | ✏️ 修改 |
| [dsh-deepcel](https://github.com/dsh-external/dsh-deepcel) | ✏️ 修改 |
| [dsh-STAR](https://github.com/dsh-external/dsh-STAR) | ✏️ 修改 |
| [dsh-STAGE](https://github.com/dsh-external/dsh-STAGE) | ✏️ 修改 |
| [dsh-conversation-share](https://github.com/dsh-external/dsh-conversation-share) | ✏️ 修改 |
| [tonghuashun-webui](https://github.com/dsh-external/tonghuashun-webui) | ✏️ 修改 |
| [dsh-session-notification](https://github.com/dsh-external/dsh-session-notification) | ✏️ 修改 |
| [dsh-custom-tool](https://github.com/dsh-external/dsh-custom-tool) | ✏️ 修改 |
| [dsh-openbiliclaw](https://github.com/dsh-external/dsh-openbiliclaw) | ✏️ 修改 |
| [dsh-longbridge](https://github.com/dsh-external/dsh-longbridge) | ✏️ 修改 |
| [dsh-dzcf](https://github.com/dsh-external/dsh-dzcf) | ✏️ 修改 |**⚠️ 需适配**（完整矩阵见 [mainline-compat.md](reports/2026-08-13/mainline-compat.md)）

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
| [dsh-cot-summary](https://github.com/dsh-external/dsh-cot-summary) | 未知 | 需适配 |**🐙 正在跟踪的 open PR**

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
