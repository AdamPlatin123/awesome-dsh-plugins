# ex-setting — 与 mainline 兼容性对比（2026-08-09）
> 调研摘要（只读资产，本报告不复制其正文）：[research/ex-setting.md](../../research/ex-setting.md)——集成点与调研全文以 research 为准。

## 克隆证据

- 克隆 HEAD：3562158
- 锚定：e6b10664af9c4ca82ef0120e53a493c5e0ce7e7d（commit，未知（不同谱系））
- 补丁：OK（1 个补丁全部干净应用）
- seam：缺: tuiPrompt
- peerDeps：10 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | OK（1 个补丁全部干净应用） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 10 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（0882344，snapshots/20260808T121140Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
