# dsh-tool-browser — 与 mainline 兼容性对比（2026-08-12）> [打开仓库](https://github.com/dsh-external/dsh-tool-browser) · 调研摘要（只读资产，本报告不复制其正文）：[research/dsh-tool-browser.md](../../research/dsh-tool-browser.md)\n\n
## 克隆证据

- 克隆 HEAD：eb86454
- 锚定：未知（catalog，未知（catalog ref，非 mainline 锚定））
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：5 项中 5 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（catalog ref，非 mainline 锚定） |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 5 项中 5 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 |
| **综合判定** | **关注** |

## 建议

- 关注：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
