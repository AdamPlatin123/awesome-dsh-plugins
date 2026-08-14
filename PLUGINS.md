# PLUGINS.md — 插件登记清单（分类版）

> 想更快被收录？在对应类别的表格追加一行并提 PR。未登记的仓库只要打 `dsh-plugin` / `dsh-external` topic，会在每日 02:00 全量扫描时自动收录。
>
> 分类体系参考 [dsh-external/hub](https://github.com/dsh-external/hub)（catalog v0.1）：🔌 单插件 / 🧰 插件集 / 🎓 技能 / 📡 远程渠道 / 🛠 基础设施 / 💬 社区 / 🔬 研究 / ❓ 未分类。
>
> 约定：插件名与 repo 名一致；scope 使用 `@dsh-external/*`（勿占用 `@deepseek-ai/*` 保留命名空间）；repo 打 `dsh-plugin` topic。

## 🔌 单插件

| 插件 | 仓库 | 说明 | 运行级 |
| dsh-event-auditor | [qing3a/dsh-event-auditor](https://github.com/qing3a/dsh-event-auditor) | Harness 事件流审计面板：观察事件类型/分发模式/计数/最近事件，settings 热改 + /audit 会话命令；已用 mock-llm 运行时验证（74 事件/12 waterfall） | ✅ |
| dsh-tray | [qing3a/dsh-tray](https://github.com/qing3a/dsh-tray) | DeepSeek Harness Windows 系统托盘插件（trayicon exe 宿主，无 native 编译）；菜单/通知/headless 降级，双 profile 已验证 | ✅ |
|---|---|---|---|
| dsh-bash-terminal | [MAXeaglet/dsh-bash-terminal](https://github.com/MAXeaglet/dsh-bash-terminal) | Windows 三终端 shell 工具（PowerShell/Git Bash/WSL，默认终端由用户在设置中选择）+ 交互式 PTY 终端 + 官方沙箱对接；4 套件测试 + GitHub Actions CI 全绿 | ✅ |
| chat-width | [dsh-external/chat-width](https://github.com/dsh-external/chat-width) | 终端宽度感知 | ✅ |
| dsh-artifact | [dsh-external/dsh-artifact](https://github.com/dsh-external/dsh-artifact) | 制品管理 | ✅ |
| dsh-split-panes | [dsh-external/dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | 分屏面板 | ✅ |
| dsh-question-collapse | [dsh-external/dsh-question-collapse](https://github.com/dsh-external/dsh-question-collapse) | 问题折叠 | ✅ |
| dsh-sentinel | [fuhefei/dsh-sentinel](https://github.com/fuhefei/dsh-sentinel) | 事件驱动唤醒 agent loop（文件/命令/http/进程/webhook 传感器） | 待测 |
| dsh-tianshu-tui | [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | DSH 的 TUI（终端界面） | 待测 |
| dsh-genui | [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) | GenUI 内联交互组件：dsh-ui fence 渲染图表/表单/测验/3D 场景，带 action 事件环 | 待测 |
| dsh-annotation | [omdsh-dev/dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) | DSH Web 选中批注插件：选文字→批注→回车随消息发送，回复按 Annotation N 逐条对照（可悬浮芯片） | 待测 |
| dsh-security-scan | [ben7am1n/dsh-security-scan](https://github.com/ben7am1n/dsh-security-scan) | Secret & dangerous-pattern scanner — API keys/tokens/private keys redacted; ignore lists; zero deps | 待测 |
| dsh-email | [STARDUSTLC666/dsh-email](https://github.com/STARDUSTLC666/dsh-email) | 邮件工具插件：IMAP/SMTP 收/发/搜/列文件夹/附件下载（email_list/read/search/send/folders/attachment），内置 QQ/163/126/新浪/阿里/Gmail/Outlook/iCloud 预设，支持多账号与连接复用，发信默认走审批门；纯 Node 全平台 | 待测 |
| dsh-calendar | [STARDUSTLC666/dsh-calendar](https://github.com/STARDUSTLC666/dsh-calendar) | CalDAV 日历插件：查/建/改/删/搜日程（calendar_list/create/update/delete/search），Google/iCloud/Nextcloud/自定义端点，应用专用密码 | 待测 |
| dsh-dingtalk | [STARDUSTLC666/dsh-dingtalk](https://github.com/STARDUSTLC666/dsh-dingtalk) | 钉钉群机器人通知（dingtalk_notify/dingtalk_text），自定义机器人 webhook+加签，零运行时依赖 | 待测 |
| dsh-slack | [STARDUSTLC666/dsh-slack](https://github.com/STARDUSTLC666/dsh-slack) | Slack 通知插件（slack_notify/slack_channels），Bot Token + 官方 Web API | 待测 |
| dsh-security-scan | [ben7am1n/dsh-security-scan](https://github.com/ben7am1n/dsh-security-scan) | Secret & dangerous-pattern scanner — API keys/tokens/private keys redacted; ignore lists; zero deps | ✅ |
| dsh-turn-index | [Simon314620/dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) | 对话轮次索引侧边栏：每轮提问一目了然，点击跳转 + 滚动联动高亮，双语纯客户端 | 待测 |
| dsh-chat-import | [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) | 从 Claude Code JSONL 全保真导入历史会话为可续聊的 DSH 会话（含工具调用/思考块） | 待测 |
| dsh-sticky-note | [Meredith2328/dsh-sticky-note](https://github.com/Meredith2328/dsh-sticky-note) | 输入框工具栏快速便签：点子/感想/TODO，Markdown 预览、自动保存、一键发送、保留与自动清除 | 待测 |
| dsh-oauth-mcp-client | [springbrand-lab/dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) | 为 DSH 连接支持 OAuth 2.1 的 Streamable HTTP MCP 服务 | 待测 |
| dsh-balance | [TwotwoPiggy/dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) | 在 DSH Web 聊天框底部实时估算对话 Token 消耗并显示您的 DeepSeek 账户余额 | 待测 |
| ds-api-usage | [Sev7een/ds-api-usage](https://github.com/Sev7een/ds-api-usage) | 在设置页展示 DeepSeek API 余额与最近 24 小时用量，包括估算消费、Token、请求次数和按小时时间线 | 待测 |
| dsh-balance | [TwotwoPiggy/dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) | 在 DSH Web 聊天框底部实时估算对话 Token 消耗并显示您的 DeepSeek 账户余额 | ✅ |
| falsify-dsh | [shi275773124/falsify-dsh](https://github.com/shi275773124/falsify-dsh) | 公开 Falsify CLI 适配器：裁决收据（lint / review --json / gate）。不是第二意见工作流；selftest ≠ claim-bearing | 待测 |
| billion-context-dsh | [Tyan66666/billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) | 模型驱动上下文压缩（ACP）：compress/decompress/search_context/acp_status 工具，模型决定何时压缩，移植自 billion-context-pi | 待测 |
| dsh-web-search-firecrawl | [yangzhe1003/dsh-web-search-firecrawl](https://github.com/yangzhe1003/dsh-web-search-firecrawl) | Firecrawl 搜索提供方：内置 web_search 工具接入 Firecrawl 搜索 API（npm @yangzhe1003/dsh-web-search-firecrawl） | ✅ |
| dsh-test-runner | [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) | 结构化测试运行工具 test_run：自动探测 vitest/jest/pytest/node:test，执行并解析失败摘要，避免模型阅读整段原始测试输出 | 待测 |
| dsh-agent-message | [GengDaPeng/dsh-agent-message](https://github.com/GengDaPeng/dsh-agent-message) | 跨会话 Agent 通信：让运行在同一 DeepSeek Harness 进程里的不同 Agent 会话互相收发消息 | 待测 |
| dsh-claude-move | [PerryLink/dsh-claude-move](https://github.com/PerryLink/dsh-claude-move) | 从 Claude Code 全保真复制历史会话/记忆/技能/CLAUDE.md 到 DSH：可续聊会话按项目归入工作区，复制式增量同步（与运行中的 Claude Code 实时续写），Web 面板 + /claude-import-all + /resume-claude | 待测 |
| dsh-session-pins | [alooshxl/dsh-session-pins](https://github.com/alooshxl/dsh-session-pins) | 在侧边栏持久置顶并快速打开可用普通会话；rc.6 归档项可识别、可移除但不可重新打开（无凭据运行级实测） | ✅ |
| dsh-cost-ledger | [suimi8/dsh-cost-ledger](https://github.com/suimi8/dsh-cost-ledger) | 跨会话持久成本账本：订阅 llm/stream 自动记录每次模型调用的 token 用量到 SQLite，内置 DeepSeek 官方 CNY 定价（可热改），提供 record_cost/query_cost/set_budget 三个 agent 工具 + /api/cost-ledger/* HTTP API 供 WebUI 仪表盘 | 待测 |
| dsh-mdbox | [Chi-hong22/dsh-mdbox](https://github.com/Chi-hong22/dsh-mdbox) | DSH Web 输入框 Markdown 编辑辅助：Shift+Enter 列表续行与空项退出、有序列表自动重编号、Tab/Shift+Tab 双向缩进；纯客户端零运行时依赖，不碰文件/网络/凭据 | 待测 |
| vpshub | [Sdongmaker/vpshub](https://github.com/Sdongmaker/vpshub) | DSH 的 VPS Hub:本地 SSH 台账(Orca 风格 ssh-config/manual + tombstone),vps_* 工具让 AI 发现/测试/执行/传输,密钥仅路径引用;可选设置页 UI(真实会话闭环实测:发现/连接/增删/别名预填) | ✅ |

## 🧰 插件集

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-subagent-tools | [lynx-gt/dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) | 子代理委派按次覆盖 model/provider/persona/toolFilter、@preset: 引用、provider/model 复合 id（bundle，不改官方文件）；rc.6 headless+web 实测通过 | ✅ |
| dsh-subagent-cwd | [lynx-gt/dsh-subagent-cwd](https://github.com/lynx-gt/dsh-subagent-cwd) | dsh-subagent-tools 加按次 cwd（子代理工作目录），附两处进程内 provider 补丁；rc.6 前台/后台 cwd 实测通过 | ✅ |
| （暂无手工登记；打标自动收录） | | |

## 🎓 技能

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-review-skills | [ben7am1n/dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) | Engineering-discipline skill pack — code-review, simplify, plan-then-execute, test-first, resolve-conflict; bundled ctx.skills provider |
| project-blueprint | [shuguang1994/project-blueprint](https://github.com/shuguang1994/project-blueprint) | 为新项目一键建立 AI 编程规范体系：AGENTS.md/文档骨架/CI/CD/Git 规范/测试制度；自主发现引擎（7 语言 15 框架 70+ 组件）+ WebSearch 回退；DSH 插件复用官方 skill-filesystem 提供方，零构建 |

## 📡 远程渠道

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-telegram | [ben7am1n/dsh-telegram](https://github.com/ben7am1n/dsh-telegram) | Telegram runtime adapter — chat with dsh agents from Telegram; per-chat sessions, followup bridging, committed-text streaming, allowlist auth, zero runtime deps |
| dsh-webhook-bridge | [ben7am1n/dsh-webhook-bridge](https://github.com/ben7am1n/dsh-webhook-bridge) | Generic webhook receiver — POST /hook/:channel wakes per-channel dsh agents; Bearer auth, reply_url callbacks, 200/401/400/413 |
| dsh-lark-bot | [PlutoKeating/dsh-lark-bot](https://github.com/PlutoKeating/dsh-lark-bot) | Feishu / Lark bridge for DeepSeek Harness — streaming cards, git-worktree project isolation, official dsh SDK/ACP backends, approval & Q&A cards, SECURITY.md |

## 🛠 基础设施

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-work | [vibeinging/dsh-work](https://github.com/vibeinging/dsh-work) | 以 dsh 为骨、codex 为皮的桌面 app | 待测 |
| deepseek-harness-desktop | [chyra-moon/deepseek-harness-desktop](https://github.com/chyra-moon/deepseek-harness-desktop) | Windows 原生桌面外壳:1:1 官方 Web UI、内置服务器托管、托盘驻留与掉线自动恢复 | 待测 |
| dsh-remote-sandbox | [weijiafu14/dsh-remote-sandbox](https://github.com/weijiafu14/dsh-remote-sandbox) | 生产级远程执行世界：E2B 沙箱内纯 JS sidecar，fs/subprocess 单次往返、进程输出有界、心跳保活、崩溃透明恢复（resume/recreate）、tar 工作区同步；修复官方 e2b POC 两处 host 假设。43 项测试（含 6 项真机 E2E）全绿 | 已测 |
| deepseek-harness-desktop | [cnskycn/deepseek-harness-desktop](https://github.com/cnskycn/deepseek-harness-desktop) | DeepSeek Harness (dsh) 官方 Web UI 的 Windows 桌面封装：一键安装包、内置完整 dsh 依赖、Node.js 自动检测与引导安装、原生窗口托管 | 待测 |

## ❓ 未分类

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-subagent-tools | [lynx-gt/dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) | 子代理委派按次覆盖 model/provider/persona/toolFilter、@preset: 引用、provider/model 复合 id（bundle，不改官方文件）；rc.6 headless+web 实测通过 | ✅ |
| dsh-subagent-cwd | [lynx-gt/dsh-subagent-cwd](https://github.com/lynx-gt/dsh-subagent-cwd) | dsh-subagent-tools 加按次 cwd（子代理工作目录），附两处进程内 provider 补丁；rc.6 前台/后台 cwd 实测通过 | ✅ |
| （暂无手工登记；打标自动收录） | | |

<!-- 新增条目示例（复制下面一行修改后插入对应分类表格末尾）：
| my-plugin | [你的账号/my-plugin](https://github.com/你的账号/my-plugin) | 一句话功能描述 | 待测 |
-->

