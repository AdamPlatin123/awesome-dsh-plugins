# plugin-registry — 与 mainline 兼容性对比（2026-08-11）> [打开仓库](https://github.com/dsh-external/plugin-registry) · 调研摘要（只读资产，本报告不复制其正文）：[research/plugin-registry.md](../../research/plugin-registry.md)\n\n
## 克隆证据

- 克隆 HEAD：c02714d
- 锚定：20260804T143803Z（label，未知（非 commit 锚定: 20260804T143803Z））
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：2 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（非 commit 锚定: 20260804T143803Z） |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 2 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（3c21611，snapshots/20260810T155924Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
