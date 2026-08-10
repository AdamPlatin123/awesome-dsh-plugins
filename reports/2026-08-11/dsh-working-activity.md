# dsh-working-activity — 与 mainline 兼容性对比（2026-08-11）> [打开仓库](https://github.com/dsh-external/dsh-working-activity) · 调研摘要（只读资产，本报告不复制其正文）：[research/dsh-working-activity.md](../../research/dsh-working-activity.md)\n\n
## 克隆证据

- 克隆 HEAD：aa00794
- 锚定：20260804T143803Z（label，未知（非 commit 锚定: 20260804T143803Z））
- 补丁：CONFLICT（1 个补丁中 0 个 OK）
- seam：缺: tuiPrompt
- peerDeps：4 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（非 commit 锚定: 20260804T143803Z） |
| 补丁 apply --check --3way | CONFLICT（1 个补丁中 0 个 OK） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 4 项匹配 |
| **综合判定** | **需适配** |

## 建议

- 需适配：当日 mainline（3c21611，snapshots/20260810T155924Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
