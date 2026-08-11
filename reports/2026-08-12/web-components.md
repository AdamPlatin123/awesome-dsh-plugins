# web-components — 与 mainline 兼容性对比（2026-08-12）> [打开仓库](https://github.com/dsh-external/web-components) · 调研摘要（只读资产，本报告不复制其正文）：[research/web-components.md](../../research/web-components.md)\n\n
## 克隆证据

- 克隆 HEAD：6d6f77a
- 锚定：b4b67f0（commit，未知（不同谱系））
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：4 项中 4 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 4 项中 4 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 |
| **综合判定** | **关注** |

## 建议

- 关注：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
