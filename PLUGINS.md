# PLUGINS.md — 插件登记清单（分类版）

> 想更快被收录？在对应类别的表格追加一行并提 PR。未登记的仓库只要打 `dsh-plugin` / `dsh-external` topic，会在每日 02:00 全量扫描时自动收录。
>
> 分类体系参考 [dsh-external/hub](https://github.com/dsh-external/hub)（catalog v0.1）：🔌 单插件 / 🧰 插件集 / 🎓 技能 / 📡 远程渠道 / 🛠 基础设施 / 💬 社区 / 🔬 研究 / ❓ 未分类。
>
> 约定：插件名与 repo 名一致；scope 使用 `@dsh-external/*`（勿占用 `@deepseek-ai/*` 保留命名空间）；repo 打 `dsh-plugin` topic。

## 🔌 单插件

| 插件 | 仓库 | 说明 | 运行级 |
| dsh-repo-context | [qing3a/dsh-repo-context](https://github.com/qing3a/dsh-repo-context) | 把 git 状态与仓库规范动态注入 system prompt（section/context/variable，官方 system-prompt 缝隙插件）；dsh-plugin-verify 0.1.2 实测 7/7 waterfall + 工具真实执行（R3 isError:false） | ✅ |
| dsh-event-auditor | [qing3a/dsh-event-auditor](https://github.com/qing3a/dsh-event-auditor) | Harness 事件流审计面板：观察事件类型/分发模式/计数/最近事件，settings 热改 + /audit 会话命令；已用 mock-llm 运行时验证（74 事件/12 waterfall） | ✅ |
| dsh-spend | [nonewind/dsh-spend](https://github.com/nonewind/dsh-spend) | Token 用量统计与预计费用：右下角悬浮窗，按模型/按天/按会话多维聚合，内置供应商知识库自动识别计费计划（web bundle） | ✅ |
| dsh-tray | [qing3a/dsh-tray](https://github.com/qing3a/dsh-tray) | DeepSeek Harness Windows 系统托盘插件（trayicon exe 宿主，无 native 编译）；菜单/通知/headless 降级，双 profile 已验证 | ✅ |
| dsh-lan-access | [Leon0555/dsh-lan-access](https://github.com/Leon0555/dsh-lan-access) | 局域网访问：Web GUI 绑定 0.0.0.0 + crypto.randomUUID polyfill（修复非安全上下文下 RPC 崩溃），npm 可装 | ✅ |
|---|---|---|---|
| dsh-bash-terminal | [MAXeaglet/dsh-bash-terminal](https://github.com/MAXeaglet/dsh-bash-terminal) | Windows 三终端 shell 工具（PowerShell/Git Bash/WSL，默认终端由用户在设置中选择）+ 交互式 PTY 终端 + 官方沙箱对接；4 套件测试 + GitHub Actions CI 全绿 | ✅ |
| chat-width | [dsh-external/chat-width](https://github.com/dsh-external/chat-width) | 终端宽度感知 | ✅ |
| dsh-artifact | [dsh-external/dsh-artifact](https://github.com/dsh-external/dsh-artifact) | 制品管理 | ✅ |
| dsh-split-panes | [dsh-external/dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | 分屏面板 | ✅ |
| dsh-question-collapse | [dsh-external/dsh-question-collapse](https://github.com/dsh-external/dsh-question-collapse) | 问题折叠 | ✅ |
| dsh-sentinel | [fuhefei/dsh-sentinel](https://github.com/fuhefei/dsh-sentinel) | 事件驱动唤醒 agent loop（文件/命令/http/进程/webhook 传感器） | 待测 |
| dsh-plugin-automations | [Sev7een/dsh-plugin-automations](https://github.com/Sev7een/dsh-plugin-automations) | Web 设置页定时任务：支持准点或 DeepSeek 谷时段执行、单次/每日重复，并持久化任务状态 | 待测 |
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
| dsh-sticky-note | [Meredith2328/dsh-sticky-note](https://github.com/Meredith2328/dsh-sticky-note) | 输入框工具栏快速便签：点子/感想/TODO，Markdown 预览、自动保存、一键发送、保留与自动清除 | 待测 |
| dsh-sidebar-mode | [Meredith2328/dsh-sidebar-mode](https://github.com/Meredith2328/dsh-sidebar-mode) | 侧边栏「新会话」按钮内嵌 Agent 预设快速切换：点击弹出预设菜单即点即用，与设置里的「Agent 预设」双向同步 | 待测 |
| dsh-oauth-mcp-client | [springbrand-lab/dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) | 为 DSH 连接支持 OAuth 2.1 的 Streamable HTTP MCP 服务 | 待测 |
| dsh-balance | [TwotwoPiggy/dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) | 在 DSH Web 聊天框底部实时估算对话 Token 消耗并显示您的 DeepSeek 账户余额 | 待测 |
| ds-api-usage | [Sev7een/ds-api-usage](https://github.com/Sev7een/ds-api-usage) | 在设置页展示 DeepSeek API 余额与最近 24 小时用量，包括估算消费、Token、请求次数和按小时时间线 | 待测 |
| dsh-balance | [TwotwoPiggy/dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) | 在 DSH Web 聊天框底部实时估算对话 Token 消耗并显示您的 DeepSeek 账户余额 | ✅ |
| falsify-dsh | [shi275773124/falsify-dsh](https://github.com/shi275773124/falsify-dsh) | 公开 Falsify CLI 适配器：裁决收据（lint / review --json / gate）。不是第二意见工作流；selftest ≠ claim-bearing | 待测 |
| billion-context-dsh | [Tyan66666/billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) | 模型驱动上下文压缩（ACP）：compress/decompress/search_context/acp_status 工具，模型决定何时压缩，移植自 billion-context-pi | 待测 |
| dsh-web-search-firecrawl | [yangzhe1003/dsh-web-search-firecrawl](https://github.com/yangzhe1003/dsh-web-search-firecrawl) | Firecrawl 搜索提供方：内置 web_search 工具接入 Firecrawl 搜索 API（npm @yangzhe1003/dsh-web-search-firecrawl） | ✅ |
| dsh-test-runner | [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) | 结构化测试运行工具 test_run：自动探测 vitest/jest/pytest/node:test，执行并解析失败摘要，避免模型阅读整段原始测试输出 | 待测 |
| dsh-agent-message | [GengDaPeng/dsh-agent-message](https://github.com/GengDaPeng/dsh-agent-message) | 跨会话 Agent 通信：让运行在同一 DeepSeek Harness 进程里的不同 Agent 会话互相收发消息 | 待测 |
| dsh-plugin-audit | [jkrandom-sudo/dsh-plugin-audit](https://github.com/jkrandom-sudo/dsh-plugin-audit) | 插件安全审计器：plugin_audit 静态权限画像（能力/凭证路径/外发主机，文件行号实证，只读契约）+ tools/pre-execute 运行时哨兵（凭证访问/非白名单外发/dotfile 写入 → 审批）；23 单测 + headless/web 真实 profile 双验证 | ✅ |
| dsh-claude-move | [PerryLink/dsh-claude-move](https://github.com/PerryLink/dsh-claude-move) | 从 Claude Code 全保真复制历史会话/记忆/技能/CLAUDE.md 到 DSH：可续聊会话按项目归入工作区，复制式增量同步（与运行中的 Claude Code 实时续写），Web 面板 + /claude-import-all + /resume-claude | 待测 |
| dsh-session-pins | [alooshxl/dsh-session-pins](https://github.com/alooshxl/dsh-session-pins) | 在侧边栏持久置顶并快速打开可用普通会话；rc.6 归档项可识别、可移除但不可重新打开（无凭据运行级实测） | ✅ |
| dsh-cost-ledger | [suimi8/dsh-cost-ledger](https://github.com/suimi8/dsh-cost-ledger) | 跨会话持久成本账本：订阅 llm/stream 自动记录每次模型调用的 token 用量到 SQLite，内置 DeepSeek 官方 CNY 定价（可热改），提供 record_cost/query_cost/set_budget 三个 agent 工具 + /api/cost-ledger/* HTTP API 供 WebUI 仪表盘 | 待测 |
| dsh-mdbox | [Chi-hong22/dsh-mdbox](https://github.com/Chi-hong22/dsh-mdbox) | DSH Web 输入框 Markdown 编辑辅助：Shift+Enter 列表续行与空项退出、有序列表自动重编号、Tab/Shift+Tab 双向缩进；纯客户端零运行时依赖，不碰文件/网络/凭据 | 待测 |
| vpshub | [Sdongmaker/vpshub](https://github.com/Sdongmaker/vpshub) | DSH 的 VPS Hub:本地 SSH 台账(Orca 风格 ssh-config/manual + tombstone),vps_* 工具让 AI 发现/测试/执行/传输,密钥仅路径引用;可选设置页 UI(真实会话闭环实测:发现/连接/增删/别名预填) | ✅ |
| dsh-latexcp | [Chi-hong22/dsh-latexcp](https://github.com/Chi-hong22/dsh-latexcp) | DSH Web 界面 LaTeX 公式复制插件：悬停 KaTeX 公式复制按钮，一键复制 TeX 源码（$…$ / \(…\) 两种格式 | 待测 |
| dsh-plugin-web-access | [junhongchashui/dsh-plugin-web-access](https://github.com/junhongchashui/dsh-plugin-web-access) | 纯本地按需网页访问：web_fetch 命令行抓取 + 无头浏览器（browser_open/snapshot/eval/screenshot）双通道，零 API Key，注册 ctx.web fetch provider | ✅ |
| dsh-web-access | [NexusAgentX/dsh-web-access](https://github.com/NexusAgentX/dsh-web-access) | 多提供方联网：web_search / fetch_content / source_check，注册 ctx.web 的 web-access 搜索/抓取提供方，Web 面板改配置与策展；npm `dsh-web-access` | ✅ |
| dsh-lens | [NexusAgentX/dsh-lens](https://github.com/NexusAgentX/dsh-lens) | 写/改文件时的实时代码反馈：LSP / linter / formatter / ast-grep / symbol_search，Web chip+dock；npm `dsh-lens` | ✅ |
| dsh-mnemon | [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) | Mnemon 深度集成的本地记忆系统：运行时热记忆 / 项目档案 / 长期记忆体三层存储，受监督写回、检索工具与 8 页 Web UI | ✅ |
| dsh-daily-brief | [Equinox7379/dsh-daily-brief](https://github.com/Equinox7379/dsh-daily-brief) | 回合日报：跨 live 会话统计回合/用户消息/助手回复/工具调用（daily_brief 工具，只读零依赖） | ✅ |
| dsh-config-watch | [Equinox7379/dsh-config-watch](https://github.com/Equinox7379/dsh-config-watch) | 配置漂移侦探：启动时快照 profile/插件清单并记录变更历史（config_changes 工具） | ✅ |
| dsh-turn-watchdog | [Equinox7379/dsh-turn-watchdog](https://github.com/Equinox7379/dsh-turn-watchdog) | 回合守夜人：检测疑似卡住的会话并注入警示（turn_watchdog_status 工具） | ✅ |
| dsh-session-repair | [Equinox7379/dsh-session-repair](https://github.com/Equinox7379/dsh-session-repair) | 会话日志修复：给未知事件类型补 ignorable 并按合规帧格式重写，修复 SessionFormatUnsupportedError（修复前自动备份） | 待测 |
| dsh-update-radar | [Equinox7379/dsh-update-radar](https://github.com/Equinox7379/dsh-update-radar) | 已装插件更新雷达：git 对比 link 插件本地与上游 HEAD，报告落后项（只读） | 待测 |
| dsh-skill-search | [Equinox7379/dsh-skill-search](https://github.com/Equinox7379/dsh-skill-search) | 按需技能搜索器：海量技能库零预加载，关键词搜索 SKILL.md（rg 快路径 + Node 兜底），AI 只读命中的那份 | ✅ |
| dsh-visual-plugin | [jyh20030112/dsh-visual-plugin](https://github.com/jyh20030112/dsh-visual-plugin) | DSH 视觉桥接插件：主模型无视觉时把用户图片转发到任意 OpenAI 兼容视觉模型（DeepSeek (Vision) 包装适配器 + Web 右侧面板配置/测试/历史），自动拦截描述并支持按问题定向提示词 | ✅ |
| DSH-Plugins-Marketplace | [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) | DSH 插件市场：聚合 GitHub `dsh-plugin` 话题插件，Web GUI 一键安装/更新/已安装识别（含预装插件自动比对），静态索引 CI 每 2 小时刷新，中英双语 | ✅ |
| dsh-doublecheck | [PerryLink/dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) | 工程纪律插件：交付前三查——需求审讯（grill-requirements 技能）+ 红绿测试证据门 + 对抗评审；原生实现于 DSH 扩展点（技能/工具策略/审批 seam/会话日志） | 待测 |

| dsh-mcp-adapter | [NexusAgentX/dsh-mcp-adapter](https://github.com/NexusAgentX/dsh-mcp-adapter) | 一个 mcp 代理工具：按需 search/describe/call，不把每个 MCP schema 塞进上下文；Web `/mcp` 菜单可添加/连接/授权 | ✅ |
| dsh-ci-doctor | [jkrandom-sudo/dsh-ci-doctor](https://github.com/jkrandom-sudo/dsh-ci-doctor) | CI 失败自动诊断：ci_watch 后台监视新增失败运行（基线对比/退避/可取消）+ ci_diagnose 日志签名提取分类（嫌疑文件/裁剪摘录/markdown 诊断卡）+ 失败签名账本去重复发；85 单测 + web profile 进程内 boot 18 项 + headless 真实模型回路实测 | ✅ |

| dsh-hdc-bridge | [1na-ko/dsh-hdc-bridge](https://github.com/1na-ko/dsh-hdc-bridge) | 鸿蒙设备桥：hdc 设备闭环（截图/装包/日志/崩溃/UI 自动化）+ 官方优先 API 知识层（SDK .d.ts + 离线 Tier-1 随包）+ DevEco CLI 构建/签名/lint；无头 DSH 实例真实 E2E 已验证 | 待测 |
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
| dsh-session-cleaner-cli | [ChenChen913/dsh-session-cleaner-cli](https://github.com/ChenChen913/dsh-session-cleaner-cli) | DSH 会话数据离线清理 CLI：按工作区交互/命令删除会话（回收站+恢复+自动备份）、同步工作区账目与投影缓存、修剪幽灵条目；零依赖 Node≥18，8 项端到端测试全绿 + CI | 待测 |

## ❓ 未分类

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-subagent-tools | [lynx-gt/dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) | 子代理委派按次覆盖 model/provider/persona/toolFilter、@preset: 引用、provider/model 复合 id（bundle，不改官方文件）；rc.6 headless+web 实测通过 | ✅ |
| dsh-subagent-cwd | [lynx-gt/dsh-subagent-cwd](https://github.com/lynx-gt/dsh-subagent-cwd) | dsh-subagent-tools 加按次 cwd（子代理工作目录），附两处进程内 provider 补丁；rc.6 前台/后台 cwd 实测通过 | ✅ |
| （暂无手工登记；打标自动收录） | | |

<!-- 新增条目示例（复制下面一行修改后插入对应分类表格末尾）：
| my-plugin | [你的账号/my-plugin](https://github.com/你的账号/my-plugin) | 一句话功能描述 | 待测 |
| dsh-tianshu-tui | [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | åºäºå®æ¹ DeepSeek Harness è£åªçäº¤äºå¼ç»ç«¯ UIï¼å®æ¶ä¼è¯ãå¾ç/è§è§æ¡¥ï¼å¹¶æ¥å¥æ¹é å·¥ä½æµãTDD è¯æ®é¨ä¸æºè½ç´¢å¼ | å¾æµ |
| dsh-plugin-workshop | [yyyyukari/dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) | Ã¥ÂÂÃ¦ÂÂÃ¥Â·Â¥Ã¥ÂÂÃ¥Â¼ÂÃ¦ÂÂÃ¤Â»Â¶Ã¦ÂµÂÃ¨Â§ÂÃ¥ÂÂ¨Ã¯Â¼ÂÃ¤Â¾Â§Ã¦Â ÂÃ¥Â¸Â¸Ã©Â©Â»Ã¥ÂÂ¥Ã¥ÂÂ£Ã¯Â¼ÂÃ¦ÂÂÃ§Â´Â¢/Ã¦ÂÂÃ§ÂÂ­/Ã¦ÂÂÃ¦ÂÂ°/Ã¨Â¿Â 7-90 Ã¥Â¤Â©Ã©Â£ÂÃ¥ÂÂÃ¦Â¦ÂÃ£ÂÂÃ¤Â¸Â­Ã¦ÂÂÃ¥ÂÂ³Ã©ÂÂ®Ã¨Â¯ÂÃ¦ÂÂ Ã¥Â°ÂÃ£ÂÂÃ¦ÂÂÃ¨Â¿Â°Ã¤Â¸Â README Ã¦ÂÂºÃ§Â¿Â»Ã£ÂÂÃ¦ÂÂÃ¤Â»Â¶Ã§ÂÂ¹Ã¥Â¾ÂÃ©ÂªÂÃ¨Â¯ÂÃ¨Â¿ÂÃ¦Â»Â¤Ã£ÂÂÃ¤Â¸ÂÃ©ÂÂ®Ã¥Â®ÂÃ¨Â£Â/Ã¦ÂÂ´Ã¦ÂÂ°/Ã¥ÂÂ¸Ã¨Â½Â½Ã¯Â¼ÂÃ¥ÂÂÃ§Â½Â®Ã¥Â·Â²Ã¥Â®ÂÃ¨Â£ÂÃ¦ÂÂÃ¤Â»Â¶Ã§Â®Â¡Ã§ÂÂÃ¯Â¼ÂÃ©ÂÂ¶Ã¦ÂÂÃ¥ÂÂ¡Ã¥ÂÂ¨Ã¯Â¼ÂGitHub Ã§ÂÂ´Ã¨Â¿ÂÃ¯Â¼Â | Ã¢ÂÂ |-->
| dsh-file-review | [left0ver/dsh-file-review](https://github.com/left0ver/dsh-file-review) | Ã¦ÂÂÃ¤Â»Â¶Ã¥Â®Â¡Ã¦ÂÂ¥Ã¦ÂÂÃ¤Â»Â¶Ã¯Â¼ÂdiffÃ§ÂÂÃ¥Â½Â¢Ã¥Â¼ÂÃ¦ÂÂ¥Ã§ÂÂÃ¦ÂÂÃ¤Â»Â¶Ã§ÂÂÃ¤Â¿Â®Ã¦ÂÂ¹Ã¥ÂÂÃ¥Â®Â¹Ã¯Â¼ÂÃ¦ÂÂ¹Ã¤Â¾Â¿Ã¥Â¯Â¹agentÃ§ÂÂÃ¤Â¿Â®Ã¦ÂÂ¹Ã¨Â¿ÂÃ¨Â¡ÂÃ¥Â®Â¡Ã¦ÂÂ¥ | Ã¢ÂÂ |-->
| dsh-ui-quote-selection | [nekogpt/dsh-ui-quote-selection](https://github.com/nekogpt/dsh-ui-quote-selection) | å¨ DSH Web ä¸­éä¸­æå­ï¼ä¸é®å¼ç¨å°è¾å¥æ¡ï¼åéé®é¢æ¶èªå¨éä¸å®æ´åæ | å¾æµ || dsh-file-claim | [Nwflower/dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) | Ã¥ÂÂÃ¤Â¸ÂÃ¥Â·Â¥Ã¤Â½ÂÃ¥ÂÂºÃ¥Â¹Â¶Ã¨Â¡ÂÃ¥Â¤ÂÃ¤Â¼ÂÃ¨Â¯ÂÃ§ÂÂÃ¦ÂÂÃ¤Â»Â¶Ã¨Â®Â¤Ã©Â¢ÂÃ¤Â¸ÂÃ¥ÂÂÃ¥ÂÂ¥Ã¤Â¿ÂÃ¦ÂÂ¤Ã¯Â¼Âclaim/releaseÃ£ÂÂÃ¥Â¿ÂÃ¨Â·Â³ stale Ã¦ÂÂ¥Ã§Â®Â¡Ã£ÂÂpending Ã¤Â¸ÂÃ¨Â·Â¯Ã¥ÂÂÃ¥Â¹Â¶Ã¯Â¼Â | Ã¥Â¾ÂÃ¦ÂµÂ |-->| dsh-memento | [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) | ÃÂ¦ÃÂÃÂÃÂ§ÃÂÃÂÃÂ£ÃÂÃÂÃÂ¥ÃÂÃÂÃÂ¥ÃÂ±ÃÂÃÂ£ÃÂÃÂÃÂ¥ÃÂ®ÃÂ¡ÃÂ¦ÃÂÃÂ¹ÃÂ©ÃÂÃÂ¨ÃÂ£ÃÂÃÂÃÂ¥ÃÂÃÂ¯ÃÂ¥ÃÂ®ÃÂ¡ÃÂ¨ÃÂ®ÃÂ¡ÃÂ§ÃÂÃÂÃÂ¨ÃÂ·ÃÂ¨ÃÂ¤ÃÂ¼ÃÂÃÂ¨ÃÂ¯ÃÂÃÂ¨ÃÂ®ÃÂ°ÃÂ¥ÃÂ¿ÃÂÃÂ¦ÃÂÃÂ¥ÃÂ§ÃÂ¼ÃÂÃÂ¯ÃÂ¼ÃÂctx.memory ÃÂ¦ÃÂÃÂÃÂ¥ÃÂÃÂ¡ + ÃÂ¦ÃÂÃÂ¬ÃÂ¥ÃÂÃÂ° SQLiteÃÂ¯ÃÂ¼ÃÂÃÂ©ÃÂÃÂ¶ÃÂ¤ÃÂ¾ÃÂÃÂ¨ÃÂµÃÂÃÂ¯ÃÂ¼ÃÂ+ memory ÃÂ¥ÃÂ·ÃÂ¥ÃÂ¥ÃÂÃÂ· + ÃÂ¥ÃÂÃÂ»ÃÂ§ÃÂ»ÃÂÃÂ¥ÃÂ¿ÃÂ«ÃÂ§ÃÂÃÂ§ÃÂ¦ÃÂ³ÃÂ¨ÃÂ¥ÃÂÃÂ¥ÃÂ¯ÃÂ¼ÃÂÃÂ¥ÃÂÃÂÃÂ¥ÃÂ¿ÃÂÃÂ¥ÃÂ®ÃÂ¡ÃÂ¦ÃÂÃÂ¹ÃÂ£ÃÂÃÂÃÂ¦ÃÂ¨ÃÂ¡ÃÂ¥ÃÂÃÂÃÂ¥ÃÂÃÂ¯ÃÂ¨ÃÂ§ÃÂ ÃÂ¢ÃÂÃÂº ÃÂ¨ÃÂÃÂ½ÃÂ§ÃÂÃÂ | ÃÂ¥ÃÂ¾ÃÂÃÂ¦ÃÂµÃÂ |-->| dsh-mcp-panel | [PerryLink/dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) | Ã¥Â®ÂÃ¦ÂÂ¹ MCP Ã¥Â®Â¢Ã¦ÂÂ·Ã§Â«Â¯Ã¯Â¼Âdsh-mcp-clientÃ¯Â¼ÂÃ¥ÂÂªÃ¨Â¯Â»Ã¨Â¿ÂÃ¨Â¡ÂÃ¦ÂÂ¶Ã§Â®Â¡Ã§ÂÂÃ©ÂÂ¢Ã¦ÂÂ¿Ã¯Â¼Â/mcp Ã¥ÂÂ½Ã¤Â»Â¤ + Ã¨Â®Â¾Ã§Â½Â®Ã©Â¡Âµ MCP Ã©Â¡ÂµÃ§Â­Â¾Ã¥Â±ÂÃ§Â¤ÂºÃ¨Â¿ÂÃ¦ÂÂ¥Ã§ÂÂ¶Ã¦ÂÂ/Ã¥Â·Â²Ã¦Â³Â¨Ã¥ÂÂÃ¥Â·Â¥Ã¥ÂÂ·/Ã©ÂÂÃ¨Â¯Â¯/Ã©ÂÂÃ¨Â¿ÂÃ¨Â®Â¡Ã¦ÂÂ°Ã¯Â¼ÂÃ¨ÂÂ±Ã¦ÂÂÃ¥Â±ÂÃ§Â¤ÂºÃ¤Â¸ÂÃ¥ÂÂÃ¦ÂÂ§Ã¥ÂÂ¯Ã¥ÂÂ patch Ã¥Â»ÂºÃ¨Â®Â® | Ã¥Â¾ÂÃ¦ÂµÂ |-->| dsh-auto-continue | [HsiangNianian/dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | DSH Web Ã¨Â¯Â·Ã¦Â±ÂÃ¤Â¸Â­Ã¦ÂÂ­Ã¨ÂÂªÃ¥ÂÂ¨Ã§Â»Â­Ã¨Â·ÂÃ¦ÂÂÃ¤Â»Â¶Ã¯Â¼ÂÃ¥ÂÂÃ¥ÂÂÃ¥ÂÂ Ã§Â½ÂÃ§Â»Â/Ã¨Â¶ÂÃ¦ÂÂ¶Ã§Â­ÂÃ©ÂÂÃ¤ÂºÂºÃ¤Â¸ÂºÃ¥ÂÂÃ¥ÂÂ Ã¥Â¤Â±Ã¨Â´Â¥Ã¥ÂÂÃ¨ÂÂªÃ¥ÂÂ¨Ã¥ÂÂÃ©ÂÂÃ£ÂÂÃ§Â»Â§Ã§Â»Â­Ã£ÂÂÃ§Â»Â­Ã¨Â·ÂÃ¯Â¼ÂÃ¥ÂÂ«Ã¥Â®Â¿Ã¤Â¸Â»Ã¥Â´Â©Ã¦ÂºÂÃ©ÂÂÃ§ÂÂÃ¥ÂÂÃ¥ÂÂÃ¦ÂÂ«Ã¦ÂÂÃ¦ÂÂ¢Ã¥Â¤ÂÃ¯Â¼ÂÃ¯Â¼ÂÃ¥ÂÂ¨Ã©ÂÂ¨Ã¥ÂÂÃ¦ÂÂ°Ã¥ÂÂ¯Ã¥ÂÂ¨Ã¨Â®Â¾Ã§Â½Â®Ã¢ÂÂÃ¦ÂÂÃ¤Â»Â¶Ã©ÂÂÃ§Â½Â®Ã¤Â¸Â­Ã¨Â°ÂÃ¦ÂÂ´ | Ã¢ÂÂ |-->| [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) | ÃÂ°ÃÂÃÂÃÂ ÃÂ¦ÃÂÃÂ°ÃÂ¥ÃÂ¢ÃÂ |-->| sandbase-harness | [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | DSH bundle for SandBase managed-agents, exposing agent discovery, durable sessions, streamed runs, artifacts, and cancellation over stdio MCP; verified against DSH 47f9438 | ✅ |
| sandbase-skills | [sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills) | Research and growth skill collection with an npm CLI that installs complete bundles into DSH native .dsh/skills discovery root; verified against DSH 47f9438 | 待测 |
