# dsh-git-graph — 与 mainline 兼容性对比（2026-08-12）> [打开仓库](https://github.com/dsh-external/dsh-git-graph) · 深度摘要待调研（当前为引擎自动判定）\n\n
## 克隆证据

- 克隆 HEAD：45799b6
- 锚定：未知（unknown，未知）
- 补丁：无补丁
- seam：缺: tuiPrompt
- peerDeps：10 项中 10 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workspace=^0.0.1↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 10 项中 10 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workspace=^0.0.1↔0.0.1-rc.1 |
| **综合判定** | **未知（待调研）** |

## 建议

- 未知（待调研）：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
