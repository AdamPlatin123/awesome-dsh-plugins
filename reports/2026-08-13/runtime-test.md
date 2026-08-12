# 运行级真实测试（2026-08-13 · Qwen3.6-35B 驱动 · mainline 7b9644f2b664）

- 方法：插件安装进 final 版 workspace → Qwen 拉起 dsh → headless 任务触发插件
- SOP：插件与主仓库均未更新 → 跳过该版本；每 repo 支持性持续记录于 `.support-status.json`

## 本轮结果

| 插件 | 判定 |
|---|---|
| chat-width | ⚠️ 加载失败 |
| distill | ⚠️ 加载失败 |
| dsh-agent-session-sources | ⚠️ 加载失败 |
| dsh-artifact | ⚠️ 加载失败 |
| dsh-cc-tui | ⚠️ 加载失败 |

## 支持性总览（持续跟踪，共 5 个已测）

| 插件 | 支持性 | 最后测试 |
|---|---|---|
| chat-width | ⚠️ 加载失败 | 2026-08-13 |
| distill | ⚠️ 加载失败 | 2026-08-13 |
| dsh-agent-session-sources | ⚠️ 加载失败 | 2026-08-13 |
| dsh-artifact | ⚠️ 加载失败 | 2026-08-13 |
| dsh-cc-tui | ⚠️ 加载失败 | 2026-08-13 |

## 汇总

- 可用 0 / 加载失败 5 / 运行报错 0 / 跳过 0
