# turtle-ui — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/turtle-ui) · 调研摘要（只读资产，本报告不复制其正文）：[research/turtle-ui.md](../../research/turtle-ui.md)\n\n
## 克隆证据

- 克隆 HEAD：e5bbbb4
- 锚定：a6fedc9e3b36d066e34860d040db6df47d88c432（commit，未知（不同谱系））
- 补丁：CONFLICT（1 个补丁中 0 个 OK）
- seam：缺: tuiPrompt
- peerDeps：22 项中 22 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent-loop=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-cmdline=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm-retry=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection-cache=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-interaction=^0.0.1↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | CONFLICT（1 个补丁中 0 个 OK） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 22 项中 22 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent-loop=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-cmdline=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm-retry=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection-cache=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-interaction=^0.0.1↔0.0.1-rc.1 |
| **综合判定** | **需适配** |

## 建议

- 需适配：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
