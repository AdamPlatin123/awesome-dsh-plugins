# marisa — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/marisa) · 调研摘要（只读资产，本报告不复制其正文）：[research/marisa.md](../../research/marisa.md)\n\n
## 克隆证据

- 克隆 HEAD：9a11d78
- 锚定：snapshot-20260807T130646Z（label，未知（非 commit 锚定: snapshot-20260807T130646Z））
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：2 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（非 commit 锚定: snapshot-20260807T130646Z） |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 2 项匹配 |
| **综合判定** | **关注** |

## 建议

- 关注：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
