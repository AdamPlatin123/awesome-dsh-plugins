# dsh-bash-encoding — 与 mainline 兼容性对比（2026-08-10）> [打开仓库](https://github.com/dsh-external/dsh-bash-encoding) · 深度摘要待调研（当前为引擎自动判定）\n\n
## 克隆证据

- 克隆 HEAD：31ce515
- 锚定：7f25d3e98c（commit，未知（不同谱系））
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：1 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 1 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（1c4950a，snapshots/20260809T140917Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
