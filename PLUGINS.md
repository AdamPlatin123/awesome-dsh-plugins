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
| chat-width | [dsh-external/chat-width](https://github.com/dsh-external/chat-width) | 终端宽度感知 | ✅ |
| dsh-artifact | [dsh-external/dsh-artifact](https://github.com/dsh-external/dsh-artifact) | 制品管理 | ✅ |
| dsh-split-panes | [dsh-external/dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | 分屏面板 | ✅ |
| dsh-question-collapse | [dsh-external/dsh-question-collapse](https://github.com/dsh-external/dsh-question-collapse) | 问题折叠 | ✅ |
| dsh-sentinel | [fuhefei/dsh-sentinel](https://github.com/fuhefei/dsh-sentinel) | 事件驱动唤醒 agent loop（文件/命令/http/进程/webhook 传感器） | 待测 |
| dsh-tianshu-tui | [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | DSH 的 TUI（终端界面） | 待测 |
| dsh-genui | [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) | GenUI 内联交互组件：dsh-ui fence 渲染图表/表单/测验/3D 场景，带 action 事件环 | 待测 |
| dsh-annotation | [omdsh-dev/dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) | DSH Web 选中批注插件：选文字→批注→回车随消息发送，回复按 Annotation N 逐条对照（可悬浮芯片） | 待测 |
| dsh-security-scan | [ben7am1n/dsh-security-scan](https://github.com/ben7am1n/dsh-security-scan) | Secret & dangerous-pattern scanner — API keys/tokens/private keys redacted; ignore lists; zero deps | 待测 |
| dsh-turn-index | [Simon314620/dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) | 对话轮次索引侧边栏：每轮提问一目了然，点击跳转 + 滚动联动高亮，双语纯客户端 | 待测 |
| dsh-chat-import | [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) | 从 Claude Code JSONL 全保真导入历史会话为可续聊的 DSH 会话（含工具调用/思考块） | 待测 |
| dsh-oauth-mcp-client | [springbrand-lab/dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) | 为 DSH 连接支持 OAuth 2.1 的 Streamable HTTP MCP 服务 | 待测 |
| dsh-balance | [TwotwoPiggy/dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) | 在 DSH Web 聊天框底部实时估算对话 Token 消耗并显示您的 DeepSeek 账户余额 | 待测 |
| falsify-dsh | [shi275773124/falsify-dsh](https://github.com/shi275773124/falsify-dsh) | 公开 Falsify CLI 适配器：裁决收据（lint / review --json / gate）。不是第二意见工作流；selftest ≠ claim-bearing | 待测 |
| billion-context-dsh | [Tyan66666/billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) | 模型驱动上下文压缩（ACP）：compress/decompress/search_context/acp_status 工具，模型决定何时压缩，移植自 billion-context-pi | 待测 |
| dsh-web-search-firecrawl | [yangzhe1003/dsh-web-search-firecrawl](https://github.com/yangzhe1003/dsh-web-search-firecrawl) | Firecrawl 搜索提供方：内置 web_search 工具接入 Firecrawl 搜索 API（npm @yangzhe1003/dsh-web-search-firecrawl） | ✅ |
| dsh-test-runner | [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) | 结构化测试运行工具 test_run：自动探测 vitest/jest/pytest/node:test，执行并解析失败摘要，避免模型阅读整段原始测试输出 | 待测 |
| dsh-plugin-cost | [yweilai77-dev/dsh-plugin-cost](https://github.com/yweilai77-dev/dsh-plugin-cost) | DSH Web 会话费用估算：tokenUsage 四桶 × 可配置价格表，一键刷新官方价格（估算非账单） | 待测 |

## 🧰 插件集

| 插件 | 仓库 | 说明 |
|---|---|---|
| （暂无手工登记；打标自动收录） | | |

## 🎓 技能

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-review-skills | [ben7am1n/dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) | Engineering-discipline skill pack — code-review, simplify, plan-then-execute, test-first, resolve-conflict; bundled ctx.skills provider |

## 📡 远程渠道

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-telegram | [ben7am1n/dsh-telegram](https://github.com/ben7am1n/dsh-telegram) | Telegram runtime adapter — chat with dsh agents from Telegram; per-chat sessions, followup bridging, committed-text streaming, allowlist auth, zero runtime deps |
| dsh-webhook-bridge | [ben7am1n/dsh-webhook-bridge](https://github.com/ben7am1n/dsh-webhook-bridge) | Generic webhook receiver — POST /hook/:channel wakes per-channel dsh agents; Bearer auth, reply_url callbacks, 200/401/400/413 |

## 🛠 基础设施

| 插件 | 仓库 | 说明 |
|---|---|---|
| dsh-work | [vibeinging/dsh-work](https://github.com/vibeinging/dsh-work) | 以 dsh 为骨、codex 为皮的桌面 app | 待测 |
| deepseek-harness-desktop | [chyra-moon/deepseek-harness-desktop](https://github.com/chyra-moon/deepseek-harness-desktop) | Windows 原生桌面外壳:1:1 官方 Web UI、内置服务器托管、托盘驻留与掉线自动恢复 | 待测 |
| dsh-remote-sandbox | [weijiafu14/dsh-remote-sandbox](https://github.com/weijiafu14/dsh-remote-sandbox) | 生产级远程执行世界：E2B 沙箱内纯 JS sidecar，fs/subprocess 单次往返、进程输出有界、心跳保活、崩溃透明恢复（resume/recreate）、tar 工作区同步；修复官方 e2b POC 两处 host 假设。43 项测试（含 6 项真机 E2E）全绿 | 已测 |

## ❓ 未分类

| 插件 | 仓库 | 说明 |
|---|---|---|
| （暂无手工登记；打标自动收录） | | |

<!-- 新增条目示例（复制下面一行修改后插入对应分类表格末尾）：
| my-plugin | [你的账号/my-plugin](https://github.com/你的账号/my-plugin) | 一句话功能描述 | 待测 |
-->

