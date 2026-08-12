# dsh-my-rsi — 与 mainline 兼容性对比（2026-08-11）> [打开仓库](https://github.com/dsh-external/dsh-my-rsi) · 调研摘要（只读资产，本报告不复制其正文）：[research/dsh-my-rsi.md](../../research/dsh-my-rsi.md)\n\n
## 克隆证据

- 克隆 HEAD：70ba8b7
- 锚定：c97643832821746b816d80d498e8a66fbb9db895（commit，未知（不同谱系））
- 补丁：OK（1 个补丁全部干净应用）
- seam：缺: tuiPrompt
- peerDeps：89 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | OK（1 个补丁全部干净应用） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 89 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（3c21611，snapshots/20260810T155924Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
