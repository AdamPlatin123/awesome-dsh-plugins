# PLUGINS.md — 插件登记清单（分类版）

> 想更快被收录？在对应类别的表格追加一行并提 PR。未登记的仓库只要打 `dsh-plugin` / `dsh-external` topic，会在每日 02:00 全量扫描时自动收录。
>
> 分类体系参考 dsh-external/hub（catalog v0.1）：🔌 单插件 / 🧰 插件集 / 🎓 技能 / 📡 远程渠道 / 🛠 基础设施 / 💬 社区 / 🔬 研究 / ❓ 未分类。
>
> 约定：插件名与 repo 名一致；scope 使用 `@dsh-external/*`（勿占用 `@deepseek-ai/*` 保留命名空间）；repo 打 `dsh-plugin` topic。

## 🔌 单插件

| 插件 | 仓库 | 说明 | 运行级 |
|---|---|---|---|
| dsh-office | [Fayelin12/dsh-office](https://github.com/Fayelin12/dsh-office) | 办公室工作区/会话仪表盘：悬浮 6 列精灵面板，可视化工作区、会话、token 用量与子代理（web bundle） | ✅ |
| deepseek-heartflow | [yun520-1/deepseek-heartflow](https://github.com/yun520-1/deepseek-heartflow) | 心虫（AGI 第1层辨别门禁）：47 维纯规则文本判别 heartflow_check 工具 + tools/post-execute 自动输出监督（block 拦截 / rewrite 提醒），引擎缺失 fail-closed；dsh.bundle manifest 可安装 | ✅ |
| dsh-repo-context | [qing3a/dsh-repo-context](https://github.com/qing3a/dsh-repo-context) | 把 git 状态与仓库规范动态注入 system prompt（section/context/variable，官方 system-prompt 缝隙插件）；dsh-plugin-verify 0.1.2 实测 7/7 waterfall + 工具真实执行（R3 isError:false） | ✅ |
| dsh-event-auditor | [qing3a/dsh-event-auditor](https://github.com/qing3a/dsh-event-auditor) | Harness 事件流审计面板：观察事件类型/分发模式/计数/最近事件，settings 热改 + /audit 会话命令；已用 mock-llm 运行时验证（74 事件/12 waterfall） | ✅ |
| dsh-spend | [nonewind/dsh-spend](https://github.com/nonewind/dsh-spend) | Token 用量统计与预计费用：右下角悬浮窗，按模型/按天/按会话多维聚合，内置供应商知识库自动识别计费计划（web bundle） | ✅ |
| dsh-tray | [qing3a/dsh-tray](https://github.com/qing3a/dsh-tray) | DeepSeek Harness Windows 系统托盘插件（trayicon exe 宿主，无 native 编译）；菜单/通知/headless 降级，双 profile 已验证 | ✅ |
| dsh-lan-access | [Leon0555/dsh-lan-access](https://github.com/Leon0555/dsh-lan-access) | 局域网访问：Web GUI 绑定 0.0.0.0 + crypto.randomUUID polyfill（修复非安全上下文下 RPC 崩溃），npm 可装 | ✅ |
| dsh-bash-terminal | [MAXeaglet/dsh-bash-terminal](https://github.com/MAXeaglet/dsh-bash-terminal) | Windows 三终端 shell 工具（PowerShell/Git Bash/WSL，默认终端由用户在设置中选择）+ 交互式 PTY 终端 + 官方沙箱对接；4 套件测试 + GitHub Actions CI 全绿 | ✅ |
| dsh-artifact | [dsh-external/dsh-artifact](https://github.com/dsh-external/dsh-artifact) | 制品管理 | ✅ |
| dsh-split-panes | [dsh-external/dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | 分屏面板 | ✅ |
| dsh-sentinel | [fuhefei/dsh-sentinel](https://github.com/fuhefei/dsh-sentinel) | 事件驱动唤醒 agent loop（文件/命令/http/进程/webhook 传感器） | ✅ |
| dsh-plugin-automations | [Sev7een/dsh-plugin-automations](https://github.com/Sev7een/dsh-plugin-automations) | Web 设置页定时任务：支持准点或 DeepSeek 谷时段执行、单次/每日重复，并持久化任务状态 | 待测 |
| dsh-tianshu-tui | [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | DSH 的 TUI（终端界面） | ✅ |
| dsh-genui | [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) | GenUI 内联交互组件：dsh-ui fence 渲染图表/表单/测验/3D 场景，带 action 事件环 | ✅ |
| dsh-annotation | [omdsh-dev/dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) | DSH Web 选中批注插件：选文字→批注→回车随消息发送，回复按 Annotation N 逐条对照（可悬浮芯片） | ✅ |
| dsh-ui-quote-selection | [nekogpt/dsh-ui-quote-selection](https://github.com/nekogpt/dsh-ui-quote-selection) | 在 DSH Web 中选中文字，一键引用到输入框；发送问题时自动附上完整原文 | ✅ |
| dsh-security-scan | [ben7am1n/dsh-security-scan](https://github.com/ben7am1n/dsh-security-scan) | Secret & dangerous-pattern scanner — API keys/tokens/private keys redacted; ignore lists; zero deps | ✅ |
| dsh-email | [STARDUSTLC666/dsh-email](https://github.com/STARDUSTLC666/dsh-email) | 邮件工具插件：IMAP/SMTP 收/发/搜/列文件夹/附件下载（email_list/read/search/send/folders/attachment），内置 QQ/163/126/新浪/阿里/Gmail/Outlook/iCloud 预设，支持多账号与连接复用，发信默认走审批门；纯 Node 全平台 | 待测 |
| dsh-calendar | [STARDUSTLC666/dsh-calendar](https://github.com/STARDUSTLC666/dsh-calendar) | CalDAV 日历插件：查/建/改/删/搜日程（calendar_list/create/update/delete/search），Google/iCloud/Nextcloud/自定义端点，应用专用密码 | 待测 |
| dsh-dingtalk | [STARDUSTLC666/dsh-dingtalk](https://github.com/STARDUSTLC666/dsh-dingtalk) | 钉钉群机器人通知（dingtalk_notify/dingtalk_text），自定义机器人 webhook+加签，零运行时依赖 | ✅ |
| dsh-slack | [STARDUSTLC666/dsh-slack](https://github.com/STARDUSTLC666/dsh-slack) | Slack 通知插件（slack_notify/slack_channels），Bot Token + 官方 Web API | 待测 |
| dsh-ffmpeg | [STARDUSTLC666/dsh-ffmpeg](https://github.com/STARDUSTLC666/dsh-ffmpeg) | 视频处理插件：ffmpeg_probe/cut/concat/encode/subtitle/extract/gif 七工具（探测/剪辑/拼接/转码/字幕烧录/抽帧/GIF），走官方 subprocess 服务、argv 数组无 shell 注入、零运行时依赖 | 待测 |
| dsh-docker | [STARDUSTLC666/dsh-docker](https://github.com/STARDUSTLC666/dsh-docker) | 容器管理插件：docker_ps/logs/inspect/exec/manage 五工具，官方 subprocess 服务、argv 无 shell 注入、exec 审批门、零运行时依赖 | 待测 |
| dsh-turn-index | [Simon314620/dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) | 对话轮次索引侧边栏：每轮提问一目了然，点击跳转 + 滚动联动高亮，双语纯客户端 | ✅ |
| dsh-outline | [urzeye/dsh-outline](https://github.com/urzeye/dsh-outline) | DSH Web 会话页实时大纲面板：「用户问题 + Markdown 标题（1~6 级）」大纲树，流式生成实时更新，点击节点定位高亮，支持展开层级调节、搜索与会话级收藏 | ✅ |
| dsh-sticky-note | [Meredith2328/dsh-sticky-note](https://github.com/Meredith2328/dsh-sticky-note) | 输入框工具栏快速便签：点子/感想/TODO，Markdown 预览、自动保存、一键发送、保留与自动清除 | ✅ |
| dsh-sidebar-mode | [Meredith2328/dsh-sidebar-mode](https://github.com/Meredith2328/dsh-sidebar-mode) | 侧边栏「新会话」按钮内嵌 Agent 预设快速切换：点击弹出预设菜单即点即用，与设置里的「Agent 预设」双向同步 | 待测 |
| dsh-oauth-mcp-client | [springbrand-lab/dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) | 为 DSH 连接支持 OAuth 2.1 的 Streamable HTTP MCP 服务 | 待测 |
| dsh-balance | [TwotwoPiggy/dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) | 在 DSH Web 聊天框底部实时估算对话 Token 消耗并显示您的 DeepSeek 账户余额 | ✅ |
| ds-api-usage | [Sev7een/ds-api-usage](https://github.com/Sev7een/ds-api-usage) | 在设置页展示 DeepSeek API 余额与最近 24 小时用量，包括估算消费、Token、请求次数和按小时时间线 | ✅ |
| falsify-dsh | [shi275773124/falsify-dsh](https://github.com/shi275773124/falsify-dsh) | 公开 Falsify CLI 适配器：裁决收据（lint / review --json / gate）。不是第二意见工作流；selftest ≠ claim-bearing | ✅ || billion-context-dsh | [Tyan66666/billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) | 模型驱动上下文压缩（ACP）：compress/decompress/search_context/acp_status 工具，模型决定何时压缩，移植自 billion-context-pi | ✅ |
| dsh-web-search-firecrawl | [yangzhe1003/dsh-web-search-firecrawl](https://github.com/yangzhe1003/dsh-web-search-firecrawl) | Firecrawl 搜索提供方：内置 web_search 工具接入 Firecrawl 搜索 API（npm @yangzhe1003/dsh-web-search-firecrawl） | ❌ |
| dsh-test-runner | [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) | 结构化测试运行工具 test_run：自动探测 vitest/jest/pytest/node:test，执行并解析失败摘要，避免模型阅读整段原始测试输出 | 待测 |
| dsh-agent-message | [GengDaPeng/dsh-agent-message](https://github.com/GengDaPeng/dsh-agent-message) | 跨会话 Agent 通信：让运行在同一 DeepSeek Harness 进程里的不同 Agent 会话互相收发消息 | 待测 |
| dsh-plugin-audit | [jkrandom-sudo/dsh-plugin-audit](https://github.com/jkrandom-sudo/dsh-plugin-audit) | 插件安全审计器：plugin_audit 静态权限画像（能力/凭证路径/外发主机，文件行号实证，只读契约）+ tools/pre-execute 运行时哨兵（凭证访问/非白名单外发/dotfile 写入 → 审批）；23 单测 + headless/web 真实 profile 双验证 | ✅ |
| dsh-claude-move | [PerryLink/dsh-claude-move](https://github.com/PerryLink/dsh-claude-move) | 从 Claude Code 全保真复制历史会话/记忆/技能/CLAUDE.md 到 DSH：可续聊会话按项目归入工作区，复制式增量同步（与运行中的 Claude Code 实时续写），Web 面板 + /claude-import-all + /resume-claude | ✅ |
| dsh-chat-import | [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) | 13 源全保真导入（Claude Code/Codex/ChatGPT/Cursor/Gemini/Reasonix/opencode/ZCode/Grok Build/OpenClaw/Pi/Hermes/Kimi）→ 可续聊 DSH 会话，反向 export_claude/sync_to_claude 写回 Claude Code；增量续写/幂等/上下文预算/Web 面板，npm dsh-chat-import | ✅ |
| dsh-session-pins | [alooshxl/dsh-session-pins](https://github.com/alooshxl/dsh-session-pins) | 在侧边栏持久置顶并快速打开可用普通会话；rc.6 归档项可识别、可移除但不可重新打开（无凭据运行级实测） | ✅ |
| dsh-cost-ledger | [suimi8/dsh-cost-ledger](https://github.com/suimi8/dsh-cost-ledger) | 跨会话持久成本账本：订阅 llm/stream 自动记录每次模型调用的 token 用量到 SQLite，内置 DeepSeek 官方 CNY 定价（可热改），提供 record_cost/query_cost/set_budget 三个 agent 工具 + /api/cost-ledger/* HTTP API 供 WebUI 仪表盘 | ✅ |
| dsh-mdbox | [Chi-hong22/dsh-mdbox](https://github.com/Chi-hong22/dsh-mdbox) | DSH Web 输入框 Markdown 编辑辅助：Shift+Enter 列表续行与空项退出、有序列表自动重编号、Tab/Shift+Tab 双向缩进；纯客户端零运行时依赖，不碰文件/网络/凭据 | 待测 |
| vpshub | [Sdongmaker/vpshub](https://github.com/Sdongmaker/vpshub) | DSH 的 VPS Hub:本地 SSH 台账(Orca 风格 ssh-config/manual + tombstone),8 个 vps_* 工具让 AI 发现/测试/执行/传输,密钥仅路径引用;ProxyJump/ProxyCommand、Windows 密钥认证、i18n 设置页 UI;npm 包 dsh-vps-hub(v0.1.8) | ✅ |
| dsh-latexcp | [Chi-hong22/dsh-latexcp](https://github.com/Chi-hong22/dsh-latexcp) | DSH Web 界面 LaTeX 公式复制插件：悬停 KaTeX 公式复制按钮，一键复制 TeX 源码（$…$ / \(…\) 两种格式 | 待测 |
| dsh-plugin-web-access | [junhongchashui/dsh-plugin-web-access](https://github.com/junhongchashui/dsh-plugin-web-access) | 纯本地按需网页访问：web_fetch 命令行抓取 + 无头浏览器（browser_open/snapshot/eval/screenshot）双通道，零 API Key，注册 ctx.web fetch provider | ✅ |
| dsh-web-access | [NexusAgentX/dsh-web-access](https://github.com/NexusAgentX/dsh-web-access) | 多提供方联网：web_search / fetch_content / source_check，注册 ctx.web 的 web-access 搜索/抓取提供方，Web 面板改配置与策展；npm `dsh-web-access` | ✅ |
| dsh-llm-fallback | [Visol-456/dsh-llm-fallback](https://github.com/Visol-456/dsh-llm-fallback) | LLM 回退链插件：请求本身永远是链头（聊天栏所选模型永不被改写），失败自动按备用顺序切换重试；Web UI 配置面板（provider/model 下拉选择、错误码、阈值、冷却，保存热生效）；dsh.bundle 一键激活；69 单测全绿 + Windows 实测 | ✅ |
| dsh-lens | [NexusAgentX/dsh-lens](https://github.com/NexusAgentX/dsh-lens) | 写/改文件时的实时代码反馈：LSP / linter / formatter / ast-grep / symbol_search，Web chip+dock；npm `dsh-lens` | ✅ |
| dsh-mnemon | [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) | Mnemon 深度集成的本地记忆系统：运行时热记忆 / 项目档案 / 长期记忆体三层存储，受监督写回、检索工具与 8 页 Web UI | ✅ |
| dsh-daily-brief | [Equinox7379/dsh-daily-brief](https://github.com/Equinox7379/dsh-daily-brief) | 回合日报：跨 live 会话统计回合/用户消息/助手回复/工具调用（daily_brief 工具，只读零依赖） | ✅ |
| dsh-config-watch | [Equinox7379/dsh-config-watch](https://github.com/Equinox7379/dsh-config-watch) | 配置漂移侦探：启动时快照 profile/插件清单并记录变更历史（config_changes 工具） | ❌ |
| dsh-turn-watchdog | [Equinox7379/dsh-turn-watchdog](https://github.com/Equinox7379/dsh-turn-watchdog) | 回合守夜人：检测疑似卡住的会话并注入警示（turn_watchdog_status 工具） | ✅ |
| dsh-session-repair | [Equinox7379/dsh-session-repair](https://github.com/Equinox7379/dsh-session-repair) | 会话日志修复：给未知事件类型补 ignorable 并按合规帧格式重写，修复 SessionFormatUnsupportedError（修复前自动备份） | 待测 |
| dsh-update-radar | [Equinox7379/dsh-update-radar](https://github.com/Equinox7379/dsh-update-radar) | 已装插件更新雷达：git 对比 link 插件本地与上游 HEAD，报告落后项（只读） | ✅ |
| dsh-skill-search | [Equinox7379/dsh-skill-search](https://github.com/Equinox7379/dsh-skill-search) | 按需技能搜索器：海量技能库零预加载，关键词搜索 SKILL.md（rg 快路径 + Node 兜底），AI 只读命中的那份 | ✅ |
| dsh-visual-plugin | [jyh20030112/dsh-visual-plugin](https://github.com/jyh20030112/dsh-visual-plugin) | DSH 视觉桥接插件：主模型无视觉时把用户图片转发到任意 OpenAI 兼容视觉模型（DeepSeek (Vision) 包装适配器 + Web 右侧面板配置/测试/历史），自动拦截描述并支持按问题定向提示词 | ✅ |
| dsh-vision-proxy | [Flyvhidbwo/dsh-vision-proxy](https://github.com/Flyvhidbwo/dsh-vision-proxy) | DeepSeek 大脑 + 自动识图：GUI 附加的每张图片自动经 OpenAI 兼容 VLM 转译成文字后交给纯文本 DeepSeek——有 key 自动走快速通道（默认 qwen3.7-flash，支持百炼/智谱/OpenRouter 等任意兼容端点），无 key 自动探测本地 Ollama（零配置） | ✅ |
| DSH-Plugins-Marketplace | [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) | DSH 插件市场：聚合 GitHub `dsh-plugin` 话题插件，Web GUI 一键安装/更新/已安装识别（含预装插件自动比对），静态索引 CI 每 2 小时刷新，中英双语 | ✅ |
| dsh-doublecheck | [PerryLink/dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) | 工程纪律插件：交付前三查——需求审讯（grill-requirements 技能）+ 红绿测试证据门 + 对抗评审 + 交付报告与逐维度核对（verify 工作流）；/doublecheck 会话命令、en/zh 双语、npm 已发布 0.6.0 | 待测 |
| dsh-git-plugin | [IT-coder-Yy/dsh-git-plugin](https://github.com/IT-coder-Yy/dsh-git-plugin) | 面向 DSH Web 的可视化 Git 工作台：查看仓库状态、Diff、分支、提交历史与贮藏，点击执行常用 Git 操作，并安全运行 AI 生成的分步骤 Git 提议；npm `dsh-easygit-plugin` 0.2.1，DSH 0.1.0-rc.6 实测 | 待测 |

| dsh-mcp-adapter | [NexusAgentX/dsh-mcp-adapter](https://github.com/NexusAgentX/dsh-mcp-adapter) | 一个 mcp 代理工具：按需 search/describe/call，不把每个 MCP schema 塞进上下文；Web `/mcp` 菜单可添加/连接/授权 | ✅ |
| logicprobe | [AmethystLuna/logicprobe](https://github.com/AmethystLuna/logicprobe) | 设计文档与重构计划声明核查：claim 枚举 + 代码库事实核对 + 逻辑原语验证（7 结构 + 7 对抗探针），dsh 原生 bundle 注入核查纪律门 | ✅ |
| embedded-workbench | [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) | 嵌入式 C/C++ 固件工程插件：8 skills（FreeRTOS/Keil/ARMCLANG/HardFault/状态机/LVGL/架构），dsh 原生 bundle 注入会话启动纪律门（1% Rule / Red Flags / Plan Verification Gate） | ✅ |
| dsh-ci-doctor | [jkrandom-sudo/dsh-ci-doctor](https://github.com/jkrandom-sudo/dsh-ci-doctor) | CI 失败自动诊断：ci_watch 后台监视新增失败运行（基线对比/退避/可取消）+ ci_diagnose 日志签名提取分类（嫌疑文件/裁剪摘录/markdown 诊断卡）+ 失败签名账本去重复发；102 单测 + web profile 进程内 boot 19 项 + headless 真实模型回路实测（v0.1.2 审查修复版） | ✅ |

| dsh-hdc-bridge | [1na-ko/dsh-hdc-bridge](https://github.com/1na-ko/dsh-hdc-bridge) | 鸿蒙设备桥：hdc 设备闭环（截图/装包/日志/崩溃/UI 自动化）+ 官方优先 API 知识层（SDK .d.ts + 离线 Tier-1 随包）+ DevEco CLI 构建/签名/lint；无头 DSH 实例真实 E2E 已验证 | ✅ |
| deepseek-skin-studio | [JueMing2049/deepseek-skin-studio](https://github.com/JueMing2049/deepseek-skin-studio) | DSH 换肤工作室：一张图一套皮肤，三通道注入（书签/CDP/原生插件）+ 可视化工坊 + 13 套内置主题 + DSH-SKIN-SPEC 导出 | 待测 |
| dsh-agent-preset-recommender | [LeemanCheung/dsh-agent-preset-recommender](https://github.com/LeemanCheung/dsh-agent-preset-recommender) | 有界、隐私安全的本地扫描器：汇总 Codex、Claude Code、WorkBuddy、CodeBuddy 元数据，原子保存密钥化聚合证据，并确定性推荐 DSH 内置 preset 与可选能力；不保留正文、不联网、不修改 preset | 待测 |
| dsh-side-chat | [heartmove/dsh-side-chat](https://github.com/heartmove/dsh-side-chat) | DSH Web 侧边聊天：选中对话片段在右侧面板的侧边聊天提问（按会话隔离，继承主会话模型/思考难度/权限），AI 回复可原文或摘要带回主会话，问题弹框选项可一键带入 | 待测 |
| dsh-subagent-max | [aaravarr/dsh-subagent-max](https://github.com/aaravarr/dsh-subagent-max) | 子代理委派按次指定模型/提供商（host 侧 `subagent_with_model` 工具）+ 多面板实时流式子代理查看器（client 侧浮动面板 token 级流式输出、卡片网格、拖拽弹出、中英 i18n）；rc.6 headless 实测通过 | ✅ |
| dsh-permission-rules | [PerryLink/dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules) | Claude Code 风格声明式权限规则：按序 allow/deny/ask YAML 规则，在 tools/pre-execute 瀑布上匹配工具名/参数/工作区路径/agent 身份，带会话日志审计、干跑模式与热重载；npm 已发布 | 待测 |
| dsh-approve-for-me | [timeance/dsh-approve-for-me](https://github.com/timeance/dsh-approve-for-me) | DeepSeek Harness 沙箱扩权审批：Shell/PowerShell 字面命令前缀规则、固定高风险检查、可选无工具 LLM reviewer；成功仅授予一次 `allowed-once`，高危或不确定请求回原生人工审批，支持 Web/headless Profile | 待测 |
| dsh-plugin-marketplace | [Scorp1o117/dsh-plugin-marketplace](https://github.com/Scorp1o117/dsh-plugin-marketplace) | Web UI 内置插件市场：设置页直接浏览 github.com/topics/dsh-plugin，搜索/按 Star 排序/README 摘要；settings 通道一键安装并自动挂载 cordis.patch.yml；AI 解释；npm 已发布 | 待测 |
| dsh-soul-md | [Scorp1o117/dsh-soul-md](https://github.com/Scorp1o117/dsh-soul-md) | soul.md 风格人设 + 长期记忆：设置页输入人设卡名称和内容即可，文件由插件自动管理；按工作区指定人设、聊天框可给会话单独切人设；AI 可自行演化人设与记忆（soul_read/soul_update/memory_*）；npm 已发布 | 待测 |
| dsh-tdai-memory | [Scorp1o117/dsh-tdai-memory](https://github.com/Scorp1o117/dsh-tdai-memory) | TencentDB Agent Memory 的 DSH 移植：L0 对话捕获 → L1 结构化记忆提取 → L2 场景/L3 画像，自动召回注入 + 记忆/对话搜索工具；复用现有 ~/.memory-tencentdb 数据；附 Web UI 设置栏 | 待测 |
| dsh-tool-vision | [Scorp1o117/dsh-tool-vision](https://github.com/Scorp1o117/dsh-tool-vision) | 外置视觉模型插件：inspect_image 把本地图片或 http(s) 图片 URL 发给任意 OpenAI 兼容端点，视觉模型看图的文字回答直接带回对话；附 Web UI 设置栏 | ✅ |
| dsh-compressor | [lifeodyssey/dsh-compressor](https://github.com/lifeodyssey/dsh-compressor) | [Headroom](https://github.com/headroomlabs-ai/headroom) 的精简移植，在不影响模型上下文缓存以及 Agent 性能的情况下，压缩工具的输出，至多减少 20% 的上下文。 | 待测 |
## 🧰 插件集

| 插件 | 仓库 | 说明 | 运行级 |
|---|---|---|---|
| dsh-subagent-tools | [lynx-gt/dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) | 子代理委派按次覆盖 model/provider/persona/toolFilter、@preset: 引用、provider/model 复合 id（bundle，不改官方文件）；rc.6 headless+web 实测通过 | ✅ |
| dsh-subagent-cwd | [lynx-gt/dsh-subagent-cwd](https://github.com/lynx-gt/dsh-subagent-cwd) | dsh-subagent-tools 加按次 cwd（子代理工作目录），附两处进程内 provider 补丁；rc.6 前台/后台 cwd 实测通过 | ✅ |
| dsh-update-notifier | [arvin-yd/dsh-update-notifier](https://github.com/arvin-yd/dsh-update-notifier) | DSH 本体更新提醒：npm latest 高于本地版本时侧边栏左下角红点+Modal（复制更新命令/忽略此版本/稍后再说），官方 ui-primitives 渲染，无更新零 UI；零构建、25 单测、rc.5/rc.6 加载与端点 E2E 实测 | 待测 |

## 🎓 技能

| 插件 | 仓库 | 说明 | 运行级 |
|---|---|---|---|
| dsh-review-skills | [ben7am1n/dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) | Engineering-discipline skill pack — code-review, simplify, plan-then-execute, test-first, resolve-conflict; bundled ctx.skills provider | 待测 |
| project-blueprint | [shuguang1994/project-blueprint](https://github.com/shuguang1994/project-blueprint) | ❌ | ❌ |
| dsh-plugin-guide | [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) | DSH 插件开发知识库：官方约束、任务工作流、API 参考与社区踩坑，作为按需加载的智能体技能（bundle 可安装，注册 ctx.skills 技能） | 待测 |
| dsh-chinese-traditional-wisdom-skill | [dhicoc/dsh-chinese-traditional-wisdom-skill](https://github.com/dhicoc/dsh-chinese-traditional-wisdom-skill) | 中华传统智慧（玄枢）AI Agent 技能包：八字/紫微/六爻/梅花/奇门/风水/五运六气/体质全融合，本地确定性引擎 + 可视化 Dashboard；dsh.bundle manifest 可安装 | ✅ |

## 📡 远程渠道

| 插件 | 仓库 | 说明 | 运行级 |
|---|---|---|---|
| dsh-telegram | [ben7am1n/dsh-telegram](https://github.com/ben7am1n/dsh-telegram) | Telegram runtime adapter — chat with dsh agents from Telegram; per-chat sessions, followup bridging, committed-text streaming, allowlist auth, zero runtime deps | 待测 |
| dsh-webhook-bridge | [ben7am1n/dsh-webhook-bridge](https://github.com/ben7am1n/dsh-webhook-bridge) | ✅ | ✅ |
| dsh-lark-bot | [PlutoKeating/dsh-lark-bot](https://github.com/PlutoKeating/dsh-lark-bot) | dsh-lark-bot：把 DeepSeek Harness (dsh) 桥接进飞书/Lark 的 bot — 标准 dsh profile bundle（`dsh plugin add` 一行安装），桥接引擎在 dsh 进程内运行；流式卡片、git worktree 项目隔离、scope 并行任务、多角色 Agent、会话归档、lark_notify 跨会话通知、安全网守护（dsh 下线后经飞书 /safemode 仅核心自愈）（0.8.0） | ✅ |
| dsh-lark-link | [amlyczz/dsh-lark-link](https://github.com/amlyczz/dsh-lark-link) | High-reliability Feishu/Lark bridge — QR one-click auth, CardKit streaming, zero-loss persistent outbox (at-least-once), per-conversation DSH sessions, self-healing connection, media in/out, reusable DSH Web GUI | ✅ |
| dsh-wechat-bridge | [gtaifu/dsh-wechat-bridge](https://github.com/gtaifu/dsh-wechat-bridge) | WeChat bridge via official Tencent iLink bot API — QR-code login, one friend = one persistent agent session, zero runtime deps, no OpenClaw | ❌ |
| dsh-onebot | [mario841859784/dsh-onebot](https://github.com/mario841859784/dsh-onebot) | QQ 渠道插件（OneBot 11 / NapCat）：反向/正向 WS、dm/群聊访问策略与 @ 门控、入站图片/语音/视频/文件解析 + whisper 转写、t2i 文字图卡片、斜杠命令、loop 合并转发+撤回（99 测试全绿，真实 QQ 链路实测） | 待测 |
| dsh-session-hub | [Asaiuta/dsh-session-hub](https://github.com/Asaiuta/dsh-session-hub) | 多服务器 DSH 会话聚合与原生操控：网关+官方 UI 桥，一屏合并多个远程 dsh web 的会话，支持历史/prompt/取消/重命名/fork/模型选择/审批问答，并导入本机其他工具的历史会话 | 待测 |

## 🛠 基础设施

| 插件 | 仓库 | 说明 | 运行级 |
|---|---|---|---|
| dsh-work | [vibeinging/dsh-work](https://github.com/vibeinging/dsh-work) | 以 dsh 为骨、codex 为皮的桌面 app | 待测 |
| deepseek-harness-desktop | [chyra-moon/deepseek-harness-desktop](https://github.com/chyra-moon/deepseek-harness-desktop) | Windows 原生桌面外壳:1:1 官方 Web UI、内置服务器托管、托盘驻留与掉线自动恢复 | ✅ |
| dsh-remote-sandbox | [weijiafu14/dsh-remote-sandbox](https://github.com/weijiafu14/dsh-remote-sandbox) | 生产级远程执行世界：E2B 沙箱内纯 JS sidecar，fs/subprocess 单次往返、进程输出有界、心跳保活、崩溃透明恢复（resume/recreate）、tar 工作区同步；修复官方 e2b POC 两处 host 假设。43 项测试（含 6 项真机 E2E）全绿 | 已测 |
| dsh-session-cleaner-cli | [ChenChen913/dsh-session-cleaner-cli](https://github.com/ChenChen913/dsh-session-cleaner-cli) | DSH 会话数据离线清理 CLI：按工作区交互/命令删除会话（回收站+恢复+自动备份）、同步工作区账目与投影缓存、修剪幽灵条目；零依赖 Node≥18，8 项端到端测试全绿 + CI | 待测 |
| dsh-suite | [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) | DSH 插件活目录 + 脚手架 + 内置插件商店：785+ 插件每小时刷新、每日兼容 CI 实测、中英双语可搜索目录站；含 create-dsh-plugin 脚手架与 plugin-manager / plugin-notify / plugin-session-export / plugin-team-board 五个 npm 包 | 已测 |

## ❓ 未分类

| 插件 | 仓库 | 说明 | 运行级 |
|---|---|---|---|
<!-- 新增条目示例（复制下面一行修改后插入对应分类表格末尾）：
| my-plugin | [你的账号/my-plugin](https://github.com/你的账号/my-plugin) | 一句话功能描述 | 待测 |
-->
| dsh-plugin-workshop | [yyyyukari/dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) | 创意工坊式插件浏览器：侧栏常驻入口，搜索/最热/最新/近 7-90 天飙升榜、中文关键词映射、描述与 README 机翻、插件特征验证过滤、一键安装/更新/卸载，内置已安装插件管理（零服务器，GitHub 直连） | ✅ |
| dsh-file-review | [left0ver/dsh-file-review](https://github.com/left0ver/dsh-file-review) | 文件审查插件：diff 的形式查看文件的修改内容，方便对 agent 的修改进行审查 | ✅ |
| dsh-file-claim | [Nwflower/dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) | 同一工作区并行多会话的文件认领与写入保护（claim/release、心跳 stale 接管、pending 三路合并） | ✅ |
| dsh-memento | [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) | 有界、分层、审批门、可审计的跨会话记忆接缝：ctx.memory 服务 + 本地 SQLite（零依赖）+ memory 工具 + 冻结快照注入；写必审批、模型可见 ⟺ 落盘 | ✅ |
| dsh-mcp-panel | [PerryLink/dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) | 官方 MCP 客户端（dsh-mcp-client）只读运行时管理面板：/mcp 命令 + 设置页 MCP 页签展示连接状态/已注册工具/错误/重连计数，脱敏展示与受控启停 patch 建议 | 待测 |
| dsh-auto-continue | [HsiangNianian/dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | DSH Web 请求中断自动续跑插件：回合因网络/超时等非人为原因失败后自动发送「继续」续跑（含宿主崩溃遗留回合扫描恢复），全部参数可在设置→插件配置中调整 | ✅ |
| sandbase-harness | [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | DSH bundle for SandBase managed-agents, exposing agent discovery, durable sessions, streamed runs, artifacts, and cancellation over stdio MCP; verified against DSH 47f9438 | ✅ |
| sandbase-skills | [sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills) | Research and growth skill collection with an npm CLI that installs complete bundles into DSH native .dsh/skills discovery root; verified against DSH 47f9438 | 待测 |
| dsh-vision-router | [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | 为纯文本 Agent 提供视觉能力：内置免 Key 视觉链 + 像素级视觉工具（看图问答、定位、裁剪、像素对比、取色、OCR、矢量化、抠图、截图）；粘贴图片即可用，无 Python，一条命令安装；dsh-plugin-verify 实测 7/7 waterfall + tools/result（isError:false，捕获 16 事件） | ✅ |
| dsh-pixel-ui | [zhang66633/dsh-pixel-ui](https://github.com/zhang66633/dsh-pixel-ui) | 像素风皮肤（Agent Xi 风格）：四主题一键切换 + fusion-pixel/Press Start 2P 像素字体 + CRT 质感，随时切回现代默认 UI | 待测 |
| dsh-plugin-installer | [zhang66633/dsh-plugin-installer](https://github.com/zhang66633/dsh-plugin-installer) | 插件商店 + 安装助手：Web GUI「插件商店」页签 + 内置安装技能（npm 直装 / GitHub clone 注册，18 个已知坑配方） | 待测 |
| dsh-malong-bridge | [wulun811/LiuHe](https://github.com/wulun811/LiuHe) | 六合工具集 DSH bundle：44 个 MCP 代码操作工具 + 动态 workspace 注入；npm 安装 @jieai/dsh-malong-bridge | 待测 |
| dsh-oai-oauth | [werifu/dsh-oai-oauth](https://github.com/werifu/dsh-oai-oauth) | OpenAI ChatGPT OAuth LLM 适配器：让 dsh 直接使用 ChatGPT 订阅（非 API Key）接入模型 | 待测 |
| dsh-whale-animation | [LeemanCheung/dsh-whale-animation](https://github.com/LeemanCheung/dsh-whale-animation) | DSH Web 回合状态旁的 60 帧随主题适配的单色鲸鱼深潜动画：传播式水面、无缝闭环、资源内嵌、`prefers-reduced-motion` 静态 PNG 回退，停止时完整清理 | 待测 |
| dsh-token-usage | [LeemanCheung/dsh-token-usage](https://github.com/LeemanCheung/dsh-token-usage) | 本地优先的四 bucket Token 可观测性：持久会话/provider/model/日期仪表盘、趋势、预算与异常信号、公开费率估算、安全聚合导出，以及显式触发的用量/会话轨迹分析 | 待测 |
| dsh-task-dag | [LeemanCheung/dsh-task-dag](https://github.com/LeemanCheung/dsh-task-dag) | 由投影驱动的会话子代理与持久工作流实时 DAG：状态与节点导航、深层链路确定性布局、适应/平移画布，以及当前会话内节点拖动重排；无并行数据库或 Host 轮询 | 待测 |
| dsh-qq2007-skin | [LeemanCheung/dsh-qq2007-skin](https://github.com/LeemanCheung/dsh-qq2007-skin) | DSH Web GUI 的 QQ 2007 风格皮肤：72 个原生主题 token、作用域三栏窗框、原创离线素材与像素伙伴、可选合成发送提示音、响应式/无障碍回退和可恢复设置开关 | 待测 |
| dsh-sql | [STARDUSTLC666/dsh-sql](https://github.com/STARDUSTLC666/dsh-sql) | 工程师级数据库插件：sql_list/query/exec/schema 四工具，SQLite/MySQL/PostgreSQL 三引擎、多连接、只读白名单、写操作审批门、行数钳制 | 待测 |
| dsh-feishucard | [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) | DSH ↔ 飞书桥（自研非 fork）：官方 SDK 长连接（无需公网）+ 流式回复卡片（过程话语内联/工具折叠面板/状态符号/限流退避熔断兜底），每聊天独立会话 + live 复用保上下文，配置独立 ~/.dsh-feishucard；npm dsh-feishucard v0.1.0，冒烟 18 项 + 实机链路实测通过 | ✅ |
| dsh-trajectory-reader | [flyingtimes/dsh-trajectory-reader](https://github.com/flyingtimes/dsh-trajectory-reader) | 轨迹解读标签页：按用户轮次解读助手行为（需求/思路/执行/结果），规则引擎 + 可选 LLM 叙述，文件/命令/错误一目了然，用户消息原样保留；dsh.bundle.patch 一键安装 | ✅ |
| dsh-remotion | [STARDUSTLC666/dsh-remotion](https://github.com/STARDUSTLC666/dsh-remotion) | 视频创作技能插件：注册 Remotion 官方移植技能（React 编程式视频，动画/音频/字幕/3D/图表/字体 + 38 个规则文件），安装即用 | 待测 |
| dsh-hyperframes | [STARDUSTLC666/dsh-hyperframes](https://github.com/STARDUSTLC666/dsh-hyperframes) | 视频创作技能插件：注册 HyperFrames by HeyGen 官方移植技能五件套（HTML 写视频 / hyperframes CLI / 注册表 / 网址转视频 / GSAP 参考），安装即用 | 待测 |
| dsh-voice | [STARDUSTLC666/dsh-voice](https://github.com/STARDUSTLC666/dsh-voice) | 语音双件套：voice_tts（edge-tts 协议免费微软神经语音，Sec-MS-GEC 本地 DRM 生成）/ voice_stt（OpenAI 兼容 ASR）/ voice_list，WS 压缩 + 可选代理隧道 | 待测 |
| dsh-codex-port | [STARDUSTLC666/dsh-codex-port](https://github.com/STARDUSTLC666/dsh-codex-port) | Codex 技能移植插件：扫描 ~/.codex 把官方 Codex 插件（本机实测 186 个插件/583 技能，一次移植 577 成功）批量转为 DSH 技能（codex_list/port/status），frontmatter 自动转换、幂等跳过 | 待测 |
| ncm-player | [WolfGenerals/ncm-player](https://github.com/WolfGenerals/ncm-player) | 网易云音乐浮窗播放器：歌单/歌词/歌词翻译/播放队列/账号登录，适配皮肤主题 | 待测 |
| dsh-theme-plugin | [BeiZi6/dsh-theme-plugin](https://github.com/BeiZi6/dsh-theme-plugin) | DSH Web GUI 主题工作室：5 套内置预设（codex-warm / nord / solarized / graphite / stock）+ 完全可自定义的浅/深配色（强调色、背景、前景、UI 与代码字体、半透明侧栏、对比度），经官方 theme overrideTokens 即时热切换、localStorage 持久化，纯官方接缝无补丁文件 | 待测 |
| dsh-opencodego-usage | [BeiZi6/dsh-opencodego-usage](https://github.com/BeiZi6/dsh-opencodego-usage) | OpenCodeGo 剩余额度监视器：输入框右下角呼吸灯（按剩余额度绿/黄/红）+ 液态玻璃面板（滚动/周/月三窗口用量与重置时间），每 30 秒自动刷新，Key 自动读取 DSH 凭据（opencode-go 提供商）也可手动覆盖 | 待测 |
| dsh-usage-dashboard | [Cassius0924/dsh-usage-dashboard](https://github.com/Cassius0924/dsh-usage-dashboard) | DeepSeek 额度与用量仪表盘：悬浮额度窗 + 「额度」tab，余额可用天数、今日/本月消耗环比、模型/会话成本排行、缓存节省、2026-08-17 峰谷定价前后账单对比，估算算法与单价公开在 src/pricing.ts | 待测 |
| dsh-checkpoint-rewind | [PerryLink/dsh-checkpoint-rewind](https://github.com/PerryLink/dsh-checkpoint-rewind) | Claude Code /rewind 等价能力：每次变更型工具执行前捕获 git 优先工作区快照（stash create / commit-tree 未引用对象，copy 兜底），轮次边界 fork 会话，一条 /rewind 命令恢复文件并回退会话（三段式事务 + 保护检查点 + preview 只读预览 + 增量字节配额）；npm 可装，160 单测 + Win/Linux CI 全绿 | 待测 |
| dsh-composer-history | [PerryLink/dsh-composer-history](https://github.com/PerryLink/dsh-composer-history) | 终端风格作曲器输入历史：边缘优先方向键召回并精确还原草稿与光标、浏览器本地持久化历史、Ctrl+R 反向搜索、滑动上下文感知（压缩摘要加入召回与搜索）；dsh.bundle manifest 可安装；rc.6 headless --patch 加载实测通过 | 待测 |
| dsh-output-styles | [PerryLink/dsh-output-styles](https://github.com/PerryLink/dsh-output-styles) | Claude Code outputStyles 兼容的运行时输出风格切换：/style 命令、按会话持久化（output_style 域）、systemPrompt 注入、六个内置风格、自定义 Markdown/JSON 风格库与热重载、Web 选择器；npm dsh-output-styles 0.3.2；rc.6 真实 bundle 安装 + profile 加载实测通过（详见 PR 自检） | 待测 |
| dsh-auto-review | [PerryLink/dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) | 审批链上的第二模型 AI 自动审查：只读审查子代理返回带理由的 allow/deny 结构化裁决，fail-closed 兜底，全量会话日志审计；Web 审查面板；npm 可装 | 待测 |
| dsh-image-gen | [LeemanCheung/dsh-image-gen](https://github.com/LeemanCheung/dsh-image-gen) | GPT Image 2 `image_gen`：默认复用 Codex 订阅 OAuth，也可显式使用 API Key；显影卡片、最多 3 张 API 实时局部图、持久附件回放/灯箱/下载、纯文本模型输出和受限的凭据安全请求 | 待测 |
| dsh-lsp-actions | [PerryLink/dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions) | LSP 动作面：诊断/格式化/补全/代码动作/符号/签名提示/inlay 提示/重命名 8 工具，官方 seam 优先 + 内置 stdio 客户端兜底；写入走 write-intent 与沙箱策略，其余只读；241 测试 + 真实 tsls e2e + CI 矩阵全绿，npm dsh-lsp-actions | 待测 |
| dsh-agfs | [openAGFS/dsh-agfs](https://github.com/openAGFS/dsh-agfs) | 文件浏览器 Web 插件（npm `@open-agfs/dsh-agfs`，`dsh plugin add` 一行安装）：宿主 webserver 同进程托管 React 前端 + REST API + `/dsh-agfs` 命令 + `browse_files`/`read_file` 模型工具；一键AI分析（右键建工作区并唤醒新会话，与手动创建一致的 agent preset 工具集）、本地打开（系统文件管理器）、三种显示尺寸、Win10 文件管理器主题（Segoe MDL2 Assets 官方图标）；109 单测 + 真实 Loader/HTTP 组合测试全绿，rc.6 web profile 实测通过（一键分析真实运行 55 次工具调用 0 错误） | ✅ |
| dsh-open-eyes | [Hyp6666/dsh-open-eyes](https://github.com/Hyp6666/dsh-open-eyes) | 让用户选择的多模态模型成为 DeepSeek 的眼睛：显式纯文本路由下桥接 WebUI 粘贴/拖入图片，并提供 vision_analyze；原生支持 OpenAI Responses、Chat Completions 与 Anthropic Messages，Credential Reference + workspace 边界；125 单测、Node 22/24 CI 与真实 tarball 临时 profile 安装/卸载通过 | 待测 |
| dsh-plugin | [plur-ai/dsh-plugin](https://github.com/plur-ai/dsh-plugin) | PLUR 持久记忆：engram 在每次 assembly 渲染进 system prompt（section 的 text 为函数），而非藏在工具调用后——记忆块被替换而非追加，上下文长度不随会话增长（实测 60 轮恒定）；全本地 BM25 + BGE 混合检索（RRF 融合，零 API 调用）、可编辑的纯 YAML 存储、按工作区划分 scope、/plur 与 /plur-memory 命令 | ✅ |
