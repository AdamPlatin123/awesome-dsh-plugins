# dsh-a2a — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/dsh-a2a) · 深度摘要待调研（当前为引擎自动判定）\n\n
## 克隆证据

- 克隆 HEAD：d139faa
- 锚定：未知（catalog，未知（catalog ref，非 mainline 锚定））
- 补丁：无补丁
- seam：缺: ThemeService tuiPrompt
- peerDeps：20 项中 18 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（catalog ref，非 mainline 锚定） |
| 补丁 apply --check --3way | 无补丁 |
| seam 符号存在性 | 缺: ThemeService tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 20 项中 18 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 |
| **综合判定** | **未知（待调研）** |

## 建议

- 未知（待调研）：当日 mainline（7b9644f，snapshots/20260812T172954Z-final-unwatermarked）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
