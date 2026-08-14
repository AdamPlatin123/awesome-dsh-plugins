# PLUGINS.md × agent 判定 差异校验表

> 交集 37/73；一致 31，**差异 6**。
> 差异≠必错：PLUGINS.md ✅ 多为人工实测（更可信），agent ❌ 可能是容器环境限制（只读/依赖装不上）。本表供策展人仲裁。

| 插件 | PLUGINS.md | agent | agent 原因 | 仲裁建议 |
|---|---|---|---|---|
| dsh-bash-terminal | ✅ | ⚠️ | dsh: TRANSPORT: DeepSeek API request to http://127.0.0.1:18093/v1 fail | 复核 |
| dsh-event-auditor | ✅ | ⚠️ | dsh: TRANSPORT: DeepSeek API request to http://127.0.0.1:18093/v1 fail | 复核 |
| dsh-session-pins | ✅ | ⚠️ | dsh: TRANSPORT: DeepSeek API request to http://127.0.0.1:18093/v1 fail | 复核 |
| dsh-subagent-cwd | ✅ | ⚠️ | dsh: STREAM_CLOSED: SSE stream ended without [DONE] | 复核 |
| dsh-subagent-tools | ✅ | ⚠️ | </tool_call> | 复核 |
| vpshub | ✅ | ⚠️ | dsh: TRANSPORT: DeepSeek API request to http://127.0.0.1:18093/v1 fail | 复核 |