# session-persistence-rdb — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/session-persistence-rdb) · 调研摘要（只读资产，本报告不复制其正文）：[research/session-persistence-rdb.md](../../research/session-persistence-rdb.md)\n\n
## 克隆证据

- 克隆 HEAD：dcb5a8f
- 锚定：未知（unknown，未知）
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：6 项中 6 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1-rc.2↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 6 项中 6 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1-rc.2↔0.0.1-rc.1 |
| **综合判定** | **关注** |

## 建议

- 关注：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
