# dsh-companion — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/dsh-companion) · 调研摘要（只读资产，本报告不复制其正文）：[research/dsh-companion.md](../../research/dsh-companion.md)\n\n
## 克隆证据

- 克隆 HEAD：18e992e
- 锚定：未知（unknown，未知）
- 补丁：无补丁
- seam：缺: ThemeService tuiPrompt
- peerDeps：7 项中 7 不匹配: @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: ThemeService tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 7 项中 7 不匹配: @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 |
| **综合判定** | **关注** |

## 建议

- 关注：当日 mainline（7b9644f，snapshots/20260812T172954Z-final-unwatermarked）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
