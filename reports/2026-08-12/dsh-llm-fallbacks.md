# dsh-llm-fallbacks — 与 mainline 兼容性对比（2026-08-12）> [打开仓库](https://github.com/dsh-external/dsh-llm-fallbacks) · 深度摘要待调研（当前为引擎自动判定）\n\n
## 克隆证据

- 克隆 HEAD：5dbee64
- 锚定：331b0716ba61da51881da244a5f78c5c0984f026（commit，未知（不同谱系））
- 补丁：OK（4 个补丁全部干净应用）
- seam：缺: tuiPrompt
- peerDeps：8 项中 8 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1

## 四维对比

| 维度 | 结果 |
|---|---|
| 锚定 vs 当日 mainline | 未知（不同谱系） |
| 补丁 apply --check --3way | OK（4 个补丁全部干净应用） |
| seam 符号存在性 | 缺: tuiPrompt |
| peerDeps 范围 vs mainline 实际 | 8 项中 8 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 |
| **综合判定** | **关注** |

## 建议

- 关注：当日 mainline（340d23a，snapshots/20260811T152241Z）对比结论见上表；详细建议汇总于 [mainline-compat.md](mainline-compat.md)。
