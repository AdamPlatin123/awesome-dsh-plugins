# distill — 与 mainline 兼容性对比（2026-08-05）
> 调研摘要（只读资产，本报告不复制其正文）：[research/distill.md](../../research/distill.md)——集成点与调研全文以 research 为准。

## 克隆证据

- 克隆 HEAD：75a7615
- 锚定：未知（unknown，未知）
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：7 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 7 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（bfb9136，snapshots/20260805T134133Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
