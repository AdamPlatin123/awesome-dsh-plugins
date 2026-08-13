# PLUGINS.md — 插件登记清单（分类版）

> 想更快被收录？在对应类别的表格追加一行并提 PR。未登记的仓库只要打 `dsh-plugin` / `dsh-external` topic，会在每日 02:00 全量扫描时自动收录。
>
> 分类体系参考 [dsh-external/hub](https://github.com/dsh-external/hub)（catalog v0.1）：🔌 单插件 / 🧰 插件集 / 🎓 技能 / 📡 远程渠道 / 🛠 基础设施 / 💬 社区 / 🔬 研究 / ❓ 未分类。
>
> 约定：插件名与 repo 名一致；scope 使用 `@dsh-external/*`（勿占用 `@deepseek-ai/*` 保留命名空间）；repo 打 `dsh-plugin` topic。

## 🔌 单插件

| 插件 | 仓库 | 说明 | 运行级 |
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

## ❓ 未分类

| 插件 | 仓库 | 说明 |
|---|---|---|
| （暂无手工登记；打标自动收录） | | |

<!-- 新增条目示例（复制下面一行修改后插入对应分类表格末尾）：
| my-plugin | [你的账号/my-plugin](https://github.com/你的账号/my-plugin) | 一句话功能描述 | 待测 |
-->
