# 0803→0804 基线说明

> 基线日（自动化前人工整理）

> 本目录是 mainline 兼容性分析的**基线快照**，记录 2026-08-04（0803→0804）官方快照相对上一版本的差异，供后续各日报告（如 `../2026-08-05/`）对照引用。

## 基线数据（0803 → 0804）

来源：`../../context/session-019fc8ab-summary.md`（旧 session 019fc8ab 在 deepseek-harness 快照仓库上的版本差异分析）。

- **差异规模**：770 files changed / 12,564 insertions / 30,749 deletions（旧快照 `25b2ad4f67` → 新快照 `6feab99fdf`）。
- **TUI 移除**：`packages/ui/tui` 产品包整体删除；CLI 中 TUI 配置/入口/向导删除、`--interface=tui` 选项移除；SDK 只保留 `acp` 与 `embed`。依据 Agent Note `2026-08-04-remove-tui-package.md`：Web 是保留的交互式产品。
- **WebSocket 下行**：Web 连接层新增 `packages/client/connection/src/client/websocket-downlink.ts`；上行 HTTP 不变，两条下行流分别承载 mux 与 host 数据。
- **九项发布说明均有源码证据**：内置 ripgrep、回合运行时长、`web_search` 完整结果滚动、长输入光标、信号退出与遥测收尾、Thinking 尾部跟随滚动、长对话切换滚动位置保持、侧边栏滚动条统一。

## 与 2026-08-05 报告的关系

- `../2026-08-05/index.md` 与 `../2026-08-05/mainline-compat.md` 中的**变更分析以此基线为基础**：0805 对比的 mainline 快照 `02d7555`（`snapshots/20260804T143803Z`）正是本基线对应的官方 0804 快照；0805 报告描述的 TUI 移除、WebSocket 下行等变化即建立在本基线（0803→0804 差异）之上。
- 生态各仓库（web-components / plugin-registry / working-activity / tg-bot 等）补丁、预设与 link 所锚定的"0804 快照"（`20260804T143803Z`）即本基线。

[返回项目根](../../README.md)
