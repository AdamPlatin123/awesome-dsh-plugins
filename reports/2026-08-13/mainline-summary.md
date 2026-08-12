# 开发者摘要与建议（2026-08-13 · LLM 生成）

1) 今日生态：共扫描 269 仓库、275 项判定，91 项兼容、6 项需适配，关注 25 项、未知 178 项；整体稳定，但待确认比例偏高，需尽快收敛。

2) 需适配插件行动建议：
- dsh-subagent-tree：补丁 CONFLICT，6 个依赖 `^0.0.1` 与 `rc.1` 不匹配；将依赖改为 `^0.0.1-rc.1` 并重打补丁。
- dsh-working-activity：补丁 CONFLICT 且 tuiPrompt 缺失；同前更新依赖，并移除/替换 tuiPrompt 调用。
- turtle-ui：tuiPrompt 缺失，UI 插槽依赖漂移；适配 rc.1 并改用新 prompt 扩展点。
- dsh-tps：TUI prompt 契约变更导致加载失败；对照 mainline 快照重编相关模块。
- dsh-split-panes：runtime/ui-slots 版本不匹配；升级到 rc.1 并同步插槽 API。
- dsh-ohos-patch：补丁基线偏移；rebase 到最新 snapshot，适配 tuiPrompt 变更。

3) mainline 变更影响：核心变更即 `@deepseek-ai/*` 从 `^0.0.1` 切换到 `0.0.1-rc.1`，同时 `tuiPrompt` 被移除/改名，导致大量依赖范围不匹配与 API 缺失。提前适配：统一用 `^0.0.1-rc.1`（或 `>=0.0.1-rc.1 <0.1.0`），并加兼容导出映射替代 tuiPrompt，即可批量通过。

4) 今天最该做的事：优先修复 6 个需适配插件，并推动 25 个关注插件统一升 rc.1，避免阻塞主线路。

---
> 由 DSH Plugin Radar 自动生成（deepseek-v4-flash）；数据源：[2026-08-13 兼容性报告](mainline-compat.md)
