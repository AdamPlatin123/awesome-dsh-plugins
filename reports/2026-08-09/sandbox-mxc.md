# sandbox-mxc — 与 mainline 兼容性对比（2026-08-09）
> 调研摘要（只读资产，本报告不复制其正文）：[research/sandbox-mxc.md](../../research/sandbox-mxc.md)——集成点与调研全文以 research 为准。

## 克隆证据

- 克隆 HEAD：1798691
- 锚定：93fe8cc2（commit，未知（不同谱系））
- 补丁：CONFLICT（1 个补丁中 0 个 OK）
- seam：缺: tuiPrompt
- peerDeps：4 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | CONFLICT（1 个补丁中 0 个 OK） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 4 项匹配 |
| **综合判定** | **需适配** |

## 建议

- 需适配：当日 mainline（0882344，snapshots/20260808T121140Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
