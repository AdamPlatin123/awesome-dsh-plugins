# dsh-cot-summary — 与 mainline 兼容性对比（2026-08-13）> [打开仓库](https://github.com/dsh-external/dsh-cot-summary) · 深度摘要待调研（当前为引擎自动判定）\n\n
## 克隆证据

- 克隆 HEAD：651573e
- 锚定：未知（unknown，未知）
- 补丁：OK（1 个补丁全部干净应用）
- seam：缺: tuiPrompt
- peerDeps：17 项中 15 不匹配: @deepseek-ai/dsh-llm=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-llm-retry=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.2↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知 |
| 补丁 apply --check --3way | OK（1 个补丁全部干净应用） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 17 项中 15 不匹配: @deepseek-ai/dsh-llm=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-llm-retry=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.2↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.2↔0.0.1-rc.1 |
| **综合判定** | **关注** |

## 建议

- 关注：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
