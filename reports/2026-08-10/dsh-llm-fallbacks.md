# dsh-llm-fallbacks — 与 mainline 兼容性对比（2026-08-10）> [打开仓库](https://github.com/dsh-external/dsh-llm-fallbacks) · 深度摘要待调研（当前为引擎自动判定）\n\n
## 克隆证据

- 克隆 HEAD：7a019bf
- 锚定：未知（unknown，未知）
- 补丁：OK（2 个补丁全部干净应用）
- seam：缺: tuiPrompt
- peerDeps：8 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | OK（2 个补丁全部干净应用） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 8 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（1c4950a，snapshots/20260809T140917Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
