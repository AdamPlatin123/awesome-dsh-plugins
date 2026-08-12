# tg-bot — 与 mainline 兼容性对比（2026-08-12）> [打开仓库](https://github.com/dsh-external/tg-bot) · 调研摘要（只读资产，本报告不复制其正文）：[research/tg-bot.md](../../research/tg-bot.md)\n\n
## 克隆证据

- 克隆 HEAD：f87e8f2
- 锚定：fa3d357fc66102d82f0ddbf67fd3d5d70944d8f7（commit，未知（不同谱系））
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：12 项中 12 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-interaction=^0.0.1↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 12 项中 12 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-interaction=^0.0.1↔0.0.1-rc.1 |
| **综合判定** | **关注** |

## 建议

- 关注：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
