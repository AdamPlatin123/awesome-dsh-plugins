# telegram — 与 mainline 兼容性对比（2026-08-09）
> 调研摘要（只读资产，本报告不复制其正文）：[research/telegram.md](../../research/telegram.md)——集成点与调研全文以 research 为准。

## 克隆证据

- 克隆 HEAD：dc5dbf9
- 锚定：未知（unknown，未知）
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：3 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 3 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（0882344，snapshots/20260808T121140Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
