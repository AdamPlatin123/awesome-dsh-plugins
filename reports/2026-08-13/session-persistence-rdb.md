# session-persistence-rdb — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/session-persistence-rdb) · 调研摘要（只读资产，本报告不复制其正文）：[research/session-persistence-rdb.md](../../research/session-persistence-rdb.md)\n\n
## 克隆证据

- 克隆 HEAD：dcb5a8f
- 锚定：未知（unknown，未知）
- 补丁：无补丁
- seam：缺: ThemeService tuiPrompt
- peerDeps：6 项匹配

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: ThemeService tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 6 项匹配 |
| **综合判定** | **兼容** |

## 建议

- 兼容：当日 mainline（7b9644f，snapshots/20260812T172954Z-final-unwatermarked）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
