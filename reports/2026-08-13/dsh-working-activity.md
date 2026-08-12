# dsh-working-activity — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/dsh-working-activity) · 调研摘要（只读资产，本报告不复制其正文）：[research/dsh-working-activity.md](../../research/dsh-working-activity.md)\n\n
## 克隆证据

- 克隆 HEAD：aa00794
- 锚定：20260804T143803Z（label，未知（非 commit 锚定: 20260804T143803Z））
- 补丁：CONFLICT（1 个补丁中 0 个 OK）
- seam：缺: tuiPrompt
- peerDeps：4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（非 commit 锚定: 20260804T143803Z） |
| 补丁 apply --check --3way | CONFLICT（1 个补丁中 0 个 OK） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 |
| **综合判定** | **需适配** |

## 建议

- 需适配：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
