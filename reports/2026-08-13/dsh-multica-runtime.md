# dsh-multica-runtime — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/dsh-multica-runtime) · 深度摘要待调研（当前为引擎自动判定）\n\n
## 克隆证据

- 克隆 HEAD：d70eeb1
- 锚定：未知（unknown，未知）
- 补丁：无补丁
- seam：缺: ThemeService tuiPrompt
- peerDeps：8 项中 8 不匹配: @deepseek-ai/dsh-agent=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent-default-model=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-cmdline=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-mcp-client=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=0.0.1-rc.1↔0.0.1-rc.2

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: ThemeService tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 8 项中 8 不匹配: @deepseek-ai/dsh-agent=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent-default-model=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-cmdline=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-mcp-client=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=0.0.1-rc.1↔0.0.1-rc.2 |
| **综合判定** | **未知（待调研）** |

## 建议

- 未知（待调研）：当日 mainline（7b9644f，snapshots/20260812T172954Z-final-unwatermarked）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
