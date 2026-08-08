# dsh-my-rsi — 与 mainline 兼容性对比（2026-08-08）
> 调研摘要（只读资产，本报告不复制其正文）：[research/dsh-my-rsi.md](../../research/dsh-my-rsi.md)——集成点与调研全文以 research 为准。

## 克隆证据

- 克隆 HEAD：4cfe085
- 锚定：17fdde293847c502f14814f38f6e698b565b69c8（commit，未知（不同谱系））
- 补丁：CONFLICT（3 个补丁中 1 个 OK）
- seam：缺: tuiPrompt
- peerDeps：29 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | CONFLICT（3 个补丁中 1 个 OK） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 29 项匹配 |
| **综合判定** | **需适配** |

## 建议

- 需适配：当日 mainline（0882344，snapshots/20260808T121140Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
