# plugin-registry — 与 mainline 兼容性对比（2026-08-05）
> 调研摘要（只读资产，本报告不复制其正文）：[research/plugin-registry.md](../../research/plugin-registry.md)——集成点与调研全文以 research 为准。

## 克隆证据

- 克隆 HEAD：a9c27f0
- 锚定：20260804T143803Z（label，未知（非 commit 锚定: 20260804T143803Z））
- 补丁：OK（1 个补丁全部干净应用）
- seam：缺: tuiPrompt
- peerDeps：11 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（非 commit 锚定: 20260804T143803Z） |
| 补丁 apply --check --3way | OK（1 个补丁全部干净应用） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 11 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（02d7555，snapshots/20260804T143803Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
