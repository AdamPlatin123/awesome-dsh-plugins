# mainline 兼容性报告（2026-08-13）

- mainline：`7b9644f`（snapshots/20260812T172954Z-final-unwatermarked）
- 上次对比：`340d23a3aa833f4d5a66489297a6c6820ff049fc`
- 兼容性：87/282 无需适配，10 需适配（dsh-subagent-tree dsh-working-activity turtle-ui fabric dsh-tps dsh-split-panes dsh-question-collapse dsh-code dsh-ohos-patch dsh-cot-summary）；其中关注 30、占位 15、不适用 2、已删除 0、未知 185

## 兼容性矩阵

| 仓库 | 锚定 | 补丁 | seam | peerDeps | 综合判定 |
|---|---|---|---|---|---|
| chat-width | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-client-locale=>=0.0.1-0↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=>=0.0.1-0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=>=0.0.1-0↔0.0.1-rc.2 | 关注 |
| deepseek-harness-desktop | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| deepseek-harness-distro | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| distill | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-acp | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-agent-session-sources | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 29 项中 25 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent-claude-code=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-artifact | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-cc-tui | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 12 项中 1 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-coding-receipt | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-companion | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-cordis-examples | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-desktop | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-feishu-bot | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-gh-bridge | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-github-integration | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 5 不匹配: @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-issue-filer | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-live-stats | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-memory-evolve | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-my-rsi | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 95 项中 47 不匹配: @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-command-feedback=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-opencode-server | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-pi-adapter | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-prompt-studio | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-pty-windows | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-session-search | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-sfw | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-shell-windows | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-skills-manager | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 关注 |
| dsh-skins | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 5 项中 5 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-subagent-tree | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-workspace=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 需适配 |
| dsh-tool-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 5 项中 5 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-tool-calculator | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 关注 |
| dsh-tool-encoding | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 关注 |
| dsh-tool-json | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 关注 |
| dsh-tool-time | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 关注 |
| dsh-ui-progress | 未知（非 commit 锚定: 20260805T134133Z） | 无补丁 | 缺: ThemeService tuiPrompt | 2 项匹配 | 兼容 |
| dsh-ui-whale | 未知（非 commit 锚定: 20260805T134133Z） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-vision | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-web-terminal | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 关注 |
| dsh-web-ui-approval-notify | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-web-ui | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 65 项中 51 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-workspace=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-workspace=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-sidebar=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1-rc.1↔0.0.1-rc.2 | 关注 |
| dsh-wecom-bot | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-weixin-bot | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-win-port | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-working-activity | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 | 需适配 |
| dshx-update-check | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| ex-setting | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 9 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 | 关注 |
| group-chat-diary | 未知（非 commit 锚定: YYYY-MM-DD） | 不适用 | 不适用 | 不适用 | 不适用 |
| hub | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| issues | 未知 | 不适用 | 不适用 | 不适用 | 不适用 |
| marisa | 未知（非 commit 锚定: snapshot-20260807T130646Z） | 无补丁 | 缺: ThemeService tuiPrompt | 2 项匹配 | 关注 |
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| qqbot | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| Qwen-MM-Plugins | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-mcp-client=^0.0.1↔0.0.1-rc.2 | 关注 |
| Recall | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| review-panel | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-mxc | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 3 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 | 关注 |
| session-chatlog | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| session-persistence-rdb | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项匹配 | 兼容 |
| telegram | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 | 关注 |
| tg-bot | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 12 项中 10 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 | 关注 |
| toybox | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| turtle-ui | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 22 项中 20 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent-loop=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-cmdline=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm-retry=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection-cache=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 需适配 |
| web-components | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 关注 |
| dsh-web-ui-notify | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-web-panel | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-evolve | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-island | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-drag-and-drop | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-message-edit | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-deep-research | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-multimedia-webui-input | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| repo-visibility-guard | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-grok-tui | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 5 项中 4 不匹配: @deepseek-ai/dsh-agent=>=0.0.1-0↔0.0.1-rc.2 @deepseek-ai/dsh-llm=>=0.0.1-0↔0.0.1-rc.2 @deepseek-ai/dsh-session=>=0.0.1-0↔0.0.1-rc.2 @deepseek-ai/dsh-tools=>=0.0.1-0↔0.0.1-rc.2 | 未知（待调研） |
| ds_web_craw | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| fabric | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 1 项匹配 | 需适配 |
| dsh-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 5 项中 4 不匹配: @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-desktop-mac | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-public-repo-monitor | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tui | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-inspect | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-hub | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-alphasolve | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 关注 |
| zotero-wave-rag | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| onboarding | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| ego-browser | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-nowledge-mem | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-sidechain | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-a2a | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 20 项中 18 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-feishu-notify | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-remote | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| mstar-workflow | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-scholar | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-issue-like-skill | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-csv | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-tool-regex | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-session-repair-skill | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| DSH-better-sidebar | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 14 项中 14 不匹配: @deepseek-ai/dsh-agent=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-schema-form=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-session-hub | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-ica | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-advisor | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 18 项中 16 不匹配: @deepseek-ai/dsh-agent=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-api-gateway=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-schema-form=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-typert-registry=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-llm-fallbacks | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 14 项中 12 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-api-gateway=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-api-remotes=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-web-workflow-visualizer | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-checkpoint | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-rewind | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 5 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| official-plugins-port | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| oh-my-dsh | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1465 项匹配 | 未知（待调研） |
| dsh-side-panel | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-profile-bundle-example | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plan-execute | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 12 项中 12 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-plan-mode=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-paste-input | 未知（非 commit 锚定: 20260808T121140Z） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| zotero-harvest | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| zephyr | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 149 项匹配 | 未知（待调研） |
| dsh-bash-encoding | 未知（非 commit 锚定: 20260808T121140Z） | 无补丁 | 缺: ThemeService tuiPrompt | 1 项匹配 | 兼容 |
| dsh-skill-stats | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-web-archive | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| sandbox-micro | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-git-identity | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-android | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-lazyfish | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-auto-approval | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-input-history | 未知（非 commit 锚定: 20260808T121140Z） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-client-ui-plan-execute | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-stickers | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项匹配 | 未知（待调研） |
| deep-standard-skill | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-serenity-plugin | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 5 项中 5 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-toolkit | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 22 项中 22 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-tool-markdown | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-session-health | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-desktop-tools | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-reuse-first | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plus | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-session-cluster | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 5 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| DSH-UI4A | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-visualize | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-tps | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 | 需适配 |
| dsh-plugin-check | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-plugin-dev | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-gomoku | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-101 | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 16 项中 15 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-layout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-turn-rewind | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-genui | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 9 项中 8 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-tool=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-mygo | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 11 项中 5 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| cross-harness-cite | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 15 项中 10 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-split-panes | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 4 项匹配 | 需适配 |
| dsh-activity-plugin | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-diff | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-mobileweb-adapter | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-desktop-electron | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-mineru | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-pet | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-paseo | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-superpowers | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-spec-kit | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-context7 | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-vscode | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tui-front-door | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 5 不匹配: @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-webbridge | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-custom-css | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项匹配 | 未知（待调研） |
| tonghuashun-harness | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-club | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-humanize | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-agent-budget | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 10 项匹配 | 未知（待调研） |
| dsh-track | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 4 项匹配 | 未知（待调研） |
| dsh-spur | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-selection-chat | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-browser-panel | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-engram-relay | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 5 项中 5 不匹配: @deepseek-ai/dsh-client-runtime=>=0.0.1-rc <2↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=>=0.0.1-rc <2↔0.0.1-rc.2 @deepseek-ai/dsh-llm=>=0.0.1-rc <2↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=>=0.0.1-rc <2↔0.0.1-rc.2 @deepseek-ai/dsh-tools=>=0.0.1-rc <2↔0.0.1-rc.2 | 未知（待调研） |
| yet-another-subagent | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 17 项中 16 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-tool=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-voice-chat | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-client-runtime=>=0.0.1-rc <2↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=>=0.0.1-rc <2↔0.0.1-rc.2 | 未知（待调研） |
| dsh-ads | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-skill-session-recovery | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tavern-plugin | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-qq2006 | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-plugin-guide | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-mnemon | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-pet-rs | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-auto-blame | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 13 项中 13 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-question-collapse | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 需适配 |
| dsh-latex | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-tool-stat | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-tool-schema | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-security-audit | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-browser-bridge | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-attachment=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| ya-workspace-sidebar | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-sidebar=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-d399 | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| 7d7d | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cordis-rocks | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-sleep | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-minigames | 未知（非 commit 锚定: 20260810T155924Z） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-nono | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-auto-chess | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dshfind | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cyber-sec | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 15 项匹配 | 未知（待调研） |
| dsh-anti-ads | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-self-control-guard | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| whale-girl | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-codex-bridge | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-kimi-bridge | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| session-teleport | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-code-map | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-loop | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-navbar | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-task-status | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-annotation | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-ui-webview | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-web-review | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cc-connect | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-focus-chat | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-build | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| oh-my-deepseek | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-save-intp | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-find-plugins | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-fkin-vibe | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-harness-ops | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-vision-toolkit | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 13 项中 13 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-tool=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-code | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 1341 项中 854 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm-deepseek=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent-default-model=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent-default-model=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-code-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-mcp-client=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-hook-protocol=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-hook-protocol=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-code-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-spill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs-local=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-spill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-spill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm-retry=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-api-remotes=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-modules=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-tool=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-plan-mode=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-typert-registry=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sdk-protocol=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm-deepseek=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sdk-protocol=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-typert-registry=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-acp=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent-spine-demo=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-app-boot=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-checkpoint-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence-jsonl=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-query-sqlite=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent-loop=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm-retry=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tool-bash=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tool-goal=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tool-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-command-feedback=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-telemetry=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-title-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-title-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-lsp=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-lsp=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-typert-registry=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-typert-registry=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-e2b=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-e2b=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sdk-client=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sdk-protocol=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection-cache=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-directory-picker-browse=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-directory-picker-native=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-workspace=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-workspace=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-bash-local=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 | 需适配 |
| Top | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| __perm_probe__ | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-kimi-browser | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-edu | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-ohos-patch | 未知 | CONFLICT（4 个补丁中 3 个 OK） | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 需适配 |
| oh-dsh-desktop | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plugin-skills | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-deep-whale | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-search | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 5 项匹配 | 未知（待调研） |
| oh-my-dsh-distribution | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-memory | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-chat | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-web | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh_ide | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-trace | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 4 项匹配 | 未知（待调研） |
| deepseek-manners | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| plugin-template | 未知（非 commit 锚定: README） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-design | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-computer-use | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 16 项中 16 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-meme | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-agent-rp | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-music-player | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-multica-runtime | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-agent=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent-default-model=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-cmdline=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-mcp-client=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-mega | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-office | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 22 项中 18 不匹配: @deepseek-ai/dsh-client-runtime=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-schema-form=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-tool=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-schema-form=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-tool=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.1.0↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.1.0↔0.0.1-rc.2 | 未知（待调研） |
| savemoneybenchmark | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-slice-agent-loop | 未知（非 commit 锚定: 20260811T152241Z） | 无补丁 | 缺: ThemeService tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-agent=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 关注 |
| dsh-kb-sieve | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-data-agent | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-security | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-teamwork | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项匹配 | 未知（待调研） |
| ui-status-label | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-connection=>=0.0.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=>=0.0.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=>=0.0.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=>=0.0.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=>=0.0.0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=>=0.0.0↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=>=0.0.0↔0.0.1-rc.2 @deepseek-ai/dsh-settings=>=0.0.0↔0.0.1-rc.2 | 未知（待调研） |
| dsh-easy-ctx-manager | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 10 项匹配 | 未知（待调研） |
| browser4-dsh | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| show-bash-command | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-chat-thumb | 未知（非 commit 锚定: README） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-super-injector | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=>=0.0.1-rc <2↔0.0.1-rc.2 | 未知（待调研） |
| dsh-hmz | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-better-sidebar-plugin-office | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项中 1 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-explain | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 15 项中 14 不匹配: @deepseek-ai/dsh-api-gateway=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-brand=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-commands=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-typert-generator=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-interpreters | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 10 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-stock-market | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-scout | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 4 项中 3 不匹配: @deepseek-ai/dsh-agent=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-diff-viewer | 未知 | OK（1 个补丁全部干净应用） | 缺: ThemeService tuiPrompt | 2 项匹配 | 兼容 |
| dsh-turn-navigator | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 5 项匹配 | 未知（待调研） |
| dsh-mobile | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-share | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-travel-plugin | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-suggested-replies | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 13 项中 13 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-aigc-canvas | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 11 项中 10 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-sonar | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项匹配 | 未知（待调研） |
| dsh-ultra-ui | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 4 项匹配 | 未知（待调研） |
| dsh-deepresearch | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 9 项匹配 | 未知（待调研） |
| dsh-notebooks | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 8 项匹配 | 未知（待调研） |
| context-doctor | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-openpencil | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-theme=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-tool=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-deeplink | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cot-summary | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 17 项匹配 | 需适配 |
| dsh-emoji | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 11 项匹配 | 未知（待调研） |
| dsh_workflow | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-openmaic | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 5 项匹配 | 未知（待调研） |
| dsh-deepcel | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-STAR | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-STAGE | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-conversation-share | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| tonghuashun-webui | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |

## mainline 变更分析（340d23a3aa833f4d5a66489297a6c6820ff049fc → 7b9644f）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **包级变化**：packages/ 下删除 26 个包目录、新增 14 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：packages/bash/bash packages/bash/bash-env packages/bash/pwsh-local packages/bash/pwsh-sandbox packages/bash/tool-bash packages/bash/tool-pwsh packages/client/ui-command packages/client/ui-model packages/client/ui-models packages/client/ui-permission packages/client/ui-plugin-config packages/client/ui-slash packages/client/ui-task packages/interaction/permission packages/pty/pty-local packages/pty/tool-bash-persistent packages/pty/tool-pty packages/self-modification/tool-cordis packages/support/invariants packages/support/llm-replay packages/tasks/tasks packages/tasks/tasks-local packages/tasks/tool-tasks packages/typert/type-meta packages/util/environment packages/util/paths packages/util/retention

新增文件：
```
packages/api/gateway/tsconfig.client.json
packages/api/gateway/tsconfig.host.json
packages/client/connection/tsconfig.client.json
packages/client/connection/tsconfig.host.json
packages/client/runtime/src/client/sessions/remotes.ts
packages/client/ui-attachment/src/DropOverlay.module.css
packages/client/ui-attachment/src/DropOverlay.tsx
packages/client/ui-attachment/tests/drop-overlay.client.spec.tsx
packages/client/ui-commands/README.zh.md
packages/client/ui-commands/tsconfig.json
packages/client/ui-conversation/src/client/conversation-nodes/turn-max-tokens.ts
packages/client/ui-deliverables/tests/prompt.client.spec.ts
packages/client/ui-directory-picker-browse/README.i18n.yaml
packages/client/ui-directory-picker-browse/README.md
packages/client/ui-directory-picker-browse/README.zh.md
```

### seam 符号变化

| 符号 | prev 存在性 | cur 存在性 | 变化 |
|---|---|---|---|
| `ThemeService` | 出现 | 消失 | 出现 → 消失（破坏性） |
| `settingsNamespace` | 出现 | 出现 | 出现 → 出现（稳定） |
| `sessionProjections` | 出现 | 出现 | 出现 → 出现（稳定） |
| `tuiPrompt` | 消失 | 消失 | 消失 → 消失 |
| `slots` | 出现 | 出现 | 出现 → 出现（稳定） |
| `session/event` | 出现 | 出现 | 出现 → 出现（稳定） |

### diffstat（packages/ patches/ workspace）

```
 packages/AGENTS.md                                 |   4 +-
 packages/README.i18n.yaml                          |   4 +-
 packages/README.md                                 |  15 +-
 packages/README.zh.md                              |  35 +-
 packages/acp/acp/package.json                      |   2 +-
 packages/acp/acp/src/index.ts                      |   2 +-
 packages/acp/acp/tests/approval.spec.ts            |   4 +-
 packages/acp/acp/tests/dispose.spec.ts             |   2 +-
 packages/acp/acp/tests/edges.spec.ts               |   2 +-
 packages/acp/acp/tests/harness.ts                  |   2 +-
 packages/acp/acp/tsconfig.json                     |   2 +-
 packages/api/README.i18n.yaml                      |   4 +-
 packages/api/README.md                             |   6 +-
 packages/api/README.zh.md                          |   6 +-
 packages/api/gateway/README.i18n.yaml              |   4 +-
 packages/api/gateway/README.md                     |  10 +-
 packages/api/gateway/README.zh.md                  |  10 +-
 packages/api/gateway/package.json                  |   6 +-
 packages/api/gateway/src/client/index.ts           |  97 ++-
 packages/api/gateway/src/index.ts                  |  95 ++-
 packages/api/gateway/src/invariant.ts              |   2 +-
 packages/api/gateway/src/types.ts                  |   4 +-
 .../{client.spec.ts => gateway.client.spec.ts}     | 324 ++++++---
 .../{gateway.spec.ts => gateway.host.spec.ts}      | 148 +++-
 packages/api/gateway/tsconfig.client.json          |  22 +
 packages/api/gateway/tsconfig.host.json            |  30 +
 packages/api/gateway/tsconfig.json                 |  22 +-
 packages/api/remotes/README.i18n.yaml              |   4 +-
 packages/api/remotes/README.md                     |   8 +-
 packages/api/remotes/README.zh.md                  |   9 +-
 packages/api/remotes/package.json                  |  12 +-
 packages/api/remotes/src/agent-lookup.ts           |  10 +-
 packages/api/remotes/src/client/index.ts           |  46 +-
 packages/api/remotes/src/index.ts                  |   4 +-
 packages/api/remotes/src/invariant.ts              |   2 +-
 packages/api/remotes/src/types.ts                  |   4 +-
 packages/api/remotes/tests/agent-lookup.spec.ts    |   4 +-
 packages/api/remotes/tests/built-lib.e2e.ts        |  14 +-
 packages/api/remotes/tsconfig.client.json          |  13 +-
 packages/api/remotes/tsconfig.host.json            |   4 +-
 packages/attachment/README.i18n.yaml               |   2 +-
 packages/attachment/README.zh.md                   |   2 +-
 packages/attachment/attachment-local/package.json  |   6 +-
 packages/attachment/attachment-local/src/index.ts  |   6 +-
 .../attachment/attachment-local/src/invariant.ts   |   2 +-
 .../attachment-local/tests/index.spec.ts           |   1 +
 packages/attachment/attachment-local/tsconfig.json |   4 +-
 packages/attachment/attachment/package.json        |   2 +-
 packages/attachment/attachment/src/invariant.ts    |   2 +-
 packages/attachment/attachment/tsconfig.json       |   2 +-
 packages/bash/bash-env/README.md                   |  51 --
 packages/bash/bash-env/README.zh.md                |  51 --
 packages/bash/bash/README.zh.md                    |  53 --
 packages/bash/pwsh-local/README.i18n.yaml          |   6 -
 packages/bash/pwsh-sandbox/README.i18n.yaml        |   6 -
 packages/bash/tool-bash/README.i18n.yaml           |   6 -
 packages/bash/tool-pwsh/README.i18n.yaml           |   6 -
 packages/boot/app-boot/README.i18n.yaml            |   4 +-
 packages/boot/app-boot/README.md                   |   2 +-
 packages/boot/app-boot/README.zh.md                |  20 +-
 packages/boot/app-boot/package.json                |  10 +-
 packages/boot/app-boot/src/index.ts                |  10 +-
 packages/boot/app-boot/src/profile.ts              |   8 +-
 packages/boot/app-boot/tests/app-boot.spec.ts      |   2 +-
 packages/boot/app-boot/tests/hmr-config.spec.ts    |   2 +-
 packages/boot/app-boot/tests/user-patches.spec.ts  |  70 +-
 packages/boot/app-boot/tsconfig.json               |   6 +-
 packages/boot/cmdline/README.i18n.yaml             |   4 +-
 packages/boot/cmdline/README.md                    |   9 +-
 packages/boot/cmdline/README.zh.md                 |   9 +-
 packages/boot/cmdline/package.json                 |   2 +-
 packages/boot/cmdline/src/index.ts                 |  92 ++-
 packages/boot/cmdline/tests/cmdline.spec.ts        |  80 +-
 packages/boot/cmdline/tsconfig.json                |   2 +-
 packages/bundle/base/README.i18n.yaml              |   4 +-
 packages/bundle/base/README.md                     |   2 +-
 packages/bundle/base/README.zh.md                  |   8 +-
 packages/bundle/base/cordis.patch.yml              |  93 +--
 packages/bundle/base/package.json                  |  40 +-
 packages/bundle/base/tests/base.spec.ts            |  63 +-
 packages/bundle/base/tsconfig.json                 |   2 +-
 packages/bundle/base/windows.cordis.patch.yml      |  31 -
 packages/bundle/headless/README.i18n.yaml          |   2 +-
 packages/bundle/headless/README.zh.md              |   6 +-
 packages/bundle/headless/cordis.patch.yml          |   2 +-
 packages/bundle/headless/package.json              |   4 +-
 packages/bundle/headless/src/startup.ts            |  25 +-
 packages/bundle/headless/tests/headless.spec.ts    |   6 +-
 packages/bundle/headless/tsconfig.json             |   2 +-
 packages/bundle/web-app/README.i18n.yaml           |   4 +-
 packages/bundle/web-app/README.md                  |   2 +-
 packages/bundle/web-app/README.zh.md               |   2 +-
 packages/bundle/web-app/cordis.patch.yml           | 107 ++-
 packages/bundle/web-app/package.json               |  35 +-
 packages/bundle/web-app/src/index.ts               |  26 +-
 packages/bundle/web-app/src/startup.ts             |  38 +-
 packages/bundle/web-app/tests/web-app.spec.ts      |  34 +-
 packages/bundle/web-app/tsconfig.json              |   4 +-
 packages/client/AGENTS.md                          |   4 +-
 packages/client/README.i18n.yaml                   |   4 +-
 packages/client/README.md                          |  19 +-
 packages/client/README.zh.md                       |  37 +-
 packages/client/connection/README.i18n.yaml        |   4 +-
 packages/client/connection/README.md               |   3 +-
 packages/client/connection/README.zh.md            |   7 +-
 packages/client/connection/package.json            |   2 +-
 packages/client/connection/src/client/api.ts       |   4 +-
 .../client/connection/src/client/connection.ts     |   4 +-
 packages/client/connection/src/client/fixture.ts   | 387 +++++++---
 packages/client/connection/src/client/index.ts     |   4 +-
 packages/client/connection/src/http-bridge.ts      |  10 +-
 packages/client/connection/src/index.ts            |  12 +-
 packages/client/connection/src/rpc-host.ts         |   4 +-
 .../client/connection/src/websocket-downlink.ts    |   2 +-
 ...-helpers.spec.ts => api-helpers.client.spec.ts} |   0
 ...rust.spec.ts => api-request-trust.host.spec.ts} |   0
 ...t-apply.spec.ts => client-apply.client.spec.ts} |   0
 ...onnection.spec.ts => connection.client.spec.ts} |   4 +-
 .../tests/{fake-api.ts => fake-api.client.ts}      |  19 +-
 ...nds.spec.ts => fixture-commands.client.spec.ts} |  88 +--
 .../{fixture.spec.ts => fixture.client.spec.ts}    |  49 +-
 ...ttp-bridge.spec.ts => http-bridge.host.spec.ts} |   0
 ...me.spec.ts => loopback-hostname.client.spec.ts} |   0
 .../{node-half.spec.ts => node-half.host.spec.ts}  |  20 +-
 ...ink.spec.ts => websocket-downlink.host.spec.ts} |   0
 packages/client/connection/tsconfig.client.json    |  49 ++
 packages/client/connection/tsconfig.host.json      |  33 +
 packages/client/connection/tsconfig.json           |  41 +-
 packages/client/hmr/package.json                   |   2 +-
 packages/client/hmr/src/client/index.ts            |   2 +-
 packages/client/hmr/src/index.ts                   |  20 +-
 packages/client/hmr/src/invariant.ts               |   2 +-
 ...{node-half.spec.ts => node-half.client.spec.ts} |  20 +-
 packages/client/hmr/tsconfig.json                  |   2 +-
 packages/client/locale/README.i18n.yaml            |   4 +-
 packages/client/locale/README.md                   |   2 +-
 packages/client/locale/README.zh.md                |   2 +-
 packages/client/locale/package.json                |   2 +-
 packages/client/locale/src/client/index.ts         |  10 +-
 .../client/locale/src/client/settings-store.ts     |   2 +-
 .../tests/{apply.spec.ts => apply.client.spec.ts}  |  24 +-
 .../tests/{host.spec.ts => host.client.spec.ts}    |   4 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |  16 +-
 ...e-row.spec.tsx => language-row.client.spec.tsx} |   2 +-
 .../{locale.spec.ts => locale.client.spec.ts}      |  10 +-
 ...store.spec.ts => settings-store.client.spec.ts} |   0
 packages/client/locale/tsconfig.json               |   2 +-
 packages/client/modules/README.i18n.yaml           |   2 +-
 packages/client/modules/README.zh.md               |  12 +-
 packages/client/modules/package.json               |   2 +-
 packages/client/modules/src/client/manifest.ts     |   2 +-
 packages/client/modules/src/client/system.ts       |   2 +-
 packages/client/modules/src/index.ts               |  18 +-
 packages/client/modules/src/invariant.ts           |   2 +-
 .../{loader.spec.ts => loader.client.spec.ts}      |   0
 ...{node-half.spec.ts => node-half.client.spec.ts} |  14 +-
 packages/client/modules/tsconfig.json              |   2 +-
 packages/client/runtime/README.i18n.yaml           |   4 +-
 packages/client/runtime/README.md                  |  18 +-
 packages/client/runtime/README.zh.md               |  32 +-
 packages/client/runtime/package.json               |  20 +-
 packages/client/runtime/src/client/agents/scope.ts |   6 +-
 .../runtime/src/client/contract/conversation.ts    |   2 +-
 .../client/runtime/src/client/contract/session.ts  |   7 +-
 .../runtime/src/client/contract/sessions-port.ts   |   4 +-
 .../client/runtime/src/client/contract/sessions.ts |   2 +-
 .../client/runtime/src/client/contract/store.ts    |   2 +-
 .../runtime/src/client/contract/workspaces.ts      |  16 +-
 .../src/client/conversation/event-registry.ts      |   2 +-
 packages/client/runtime/src/client/index.ts        |  41 +-
 .../src/client/sessions/assistant-timing.ts        |  23 +-
 .../src/client/sessions/context-provenance.ts      |   2 +-
 .../client/sessions/conversation-location-index.ts |   2 +-
 .../runtime/src/client/sessions/conversation.ts    |  24 +-
 .../runtime/src/client/sessions/failure-display.ts |   2 +-
 .../client/runtime/src/client/sessions/lineage.ts  |   4 +-
 .../client/runtime/src/client/sessions/manager.ts  |  48 +-
 .../client/runtime/src/client/sessions/partial.ts  |   2 +-
 .../client/runtime/src/client/sessions/pending.ts  |   4 +-
 .../src/client/sessions/projection-store.ts        |   2 +-
 .../client/runtime/src/client/sessions/provide.ts  |   4 +-
 .../runtime/src/client/sessions/queue-mirror.ts    |   4 +-
 .../client/runtime/src/client/sessions/remotes.ts  |  12 +
 .../client/runtime/src/client/sessions/service.ts  |  36 +-
 .../client/runtime/src/client/sessions/session.ts  |  20 +-
 .../src/client/sessions/subagent-lineage.ts        |   2 +-
 .../runtime/src/client/sessions/tool-call-tree.ts  |   2 +-
 packages/client/runtime/src/client/slots.ts        |  10 +-
 .../runtime/src/client/workspaces/manager.ts       | 113 ++-
 .../runtime/src/client/workspaces/service.ts       |  36 +-
 .../runtime/src/client/workspaces/workspace.ts     |  10 +-
 ...t-apply.spec.ts => client-apply.client.spec.ts} |  23 +-
 ...e.spec.ts => context-provenance.client.spec.ts} | Bin 4572 -> 4540 bytes
 ...ec.ts => conversation-assembler.client.spec.ts} |   4 +-
 ...pec.ts => conversation-registry.client.spec.ts} |   8 +-
 ...rsation.spec.ts => conversation.client.spec.ts} |   4 +-
 .../{event-script.ts => event-script.client.ts}    |   6 +-
 .../tests/{fake-api.ts => fake-api.client.ts}      |  34 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |  12 +-
 .../{lineage.spec.ts => lineage.client.spec.ts}    |   4 +-
 .../{manager.spec.ts => manager.client.spec.ts}    | 176 +++--
 ...{node-half.spec.ts => node-half.client.spec.ts} |   0
 .../{notifier.spec.ts => notifier.client.spec.ts}  |   2 +-
 .../{partial.spec.ts => partial.client.spec.ts}    |   2 +-
 ...ore.spec.ts => projection-store.client.spec.ts} |  20 +-
 ...ue-store.spec.ts => queue-store.client.spec.ts} |  12 +-
 .../tests/{scope.spec.ts => scope.client.spec.ts}  |   2 +-
 .../{session.spec.ts => session.client.spec.ts}    |  18 +-
 ...ice.spec.ts => sessions-service.client.spec.ts} |  16 +-
 ...ervice.spec.ts => slots-service.client.spec.ts} |  10 +-
 .../tests/{store.spec.ts => store.client.spec.ts}  |   2 +-
 ...age.spec.ts => subagent-lineage.client.spec.ts} |   2 +-
 ...{time-zone.spec.ts => time-zone.client.spec.ts} |   0
 ...-tree.spec.ts => tool-call-tree.client.spec.ts} |   0
 ...e-events.spec.ts => wire-events.client.spec.ts} |   5 +-
 ...e.spec.ts => workspaces-service.client.spec.ts} | 193 ++++-
 packages/client/runtime/tsconfig.json              |  11 +-
 packages/client/schema-form/README.i18n.yaml       |   2 +-
 packages/client/schema-form/README.zh.md           |  12 +-
 packages/client/schema-form/package.json           |   2 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 .../tests/{model.spec.ts => model.client.spec.ts}  |   0
 packages/client/schema-form/tsconfig.json          |   2 +-
 packages/client/tsdown.client.ts                   |   2 +-
 packages/client/ui-agent-preset/README.i18n.yaml   |   2 +-
 packages/client/ui-agent-preset/README.zh.md       |   4 +-
 packages/client/ui-agent-preset/package.json       |   2 +-
 .../src/client/AgentPresetSection.tsx              |   2 +-
 .../client/ui-agent-preset/src/client/index.ts     |   4 +-
 .../client/ui-agent-preset/src/client/locales.ts   |   2 +-
 .../ui-agent-preset/src/client/seat-store.ts       |   2 +-
 .../ui-agent-preset/src/client/section-store.ts    |   2 +-
 .../ui-agent-preset/src/client/settings-store.ts   |   2 +-
 .../tests/{apply.spec.ts => apply.client.spec.ts}  |  16 +-
 ...ponents.spec.tsx => components.client.spec.tsx} |   0
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 .../{locales.spec.ts => locales.client.spec.ts}    |   0
 ...-store.spec.ts => section-store.client.spec.ts} |   2 +-
 .../{section.spec.tsx => section.client.spec.tsx}  |   2 +-
 ...store.spec.ts => settings-store.client.spec.ts} |   4 +-
 packages/client/ui-agent-preset/tsconfig.json      |   7 +-
 packages/client/ui-attachment/README.i18n.yaml     |   4 +-
 packages/client/ui-attachment/README.md            |   8 +-
 packages/client/ui-attachment/README.zh.md         |   8 +-
 packages/client/ui-attachment/package.json         |   2 +-
 .../client/ui-attachment/src/AttachmentRail.tsx    |   2 +-
 .../ui-attachment/src/DropOverlay.module.css       |  54 ++
 packages/client/ui-attachment/src/DropOverlay.tsx  |  77 ++
 .../ui-attachment/src/ImageLightbox.module.css     |  14 +-
 .../client/ui-attachment/src/ImageLightbox.tsx     |   7 +-
 .../ui-attachment/src/MessageImage.module.css      |  22 +-
 packages/client/ui-attachment/src/MessageImage.tsx |  47 +-
 packages/client/ui-attachment/src/index.ts         |   8 +-
 ...il.spec.tsx => attachment-rail.client.spec.tsx} |   0
 .../tests/drop-overlay.client.spec.tsx             |  38 +
 ...box.spec.tsx => image-lightbox.client.spec.tsx} |   7 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 ...mage.spec.tsx => message-image.client.spec.tsx} |  68 +-
 packages/client/ui-attachment/tsconfig.json        |   2 +-
 packages/client/ui-command/README.zh.md            |  27 -
 packages/client/ui-command/tsdown.config.ts        |   3 -
 .../{ui-question => ui-commands}/README.i18n.yaml  |   6 +-
 .../client/{ui-command => ui-commands}/README.md   |  10 +-
 packages/client/ui-commands/README.zh.md           |  29 +
 .../{ui-command => ui-commands}/package.json       |  21 +-
 .../src/client/PopupSelectView.module.css          |   0
 .../src/client/PopupSelectView.tsx                 |   2 +-
 .../src/client/contract.ts                         |  10 +-
 .../src/client/directory.ts                        |  11 +-
 .../src/client/index.ts                            |  24 +-
 .../src/client/locales.ts                          |   0
 .../src/client/popup.ts                            |   8 +-
 .../src/client/service.ts                          |  99 ++-
 .../src/css-modules.d.ts                           |   0
 .../{ui-command => ui-commands}/src/index.ts       |   2 +-
 .../{ui-command => ui-commands}/src/invariant.ts   |   8 +-
 .../tests/browser-plugin.client.spec.ts}           |  47 +-
 .../tests/directory.client.spec.ts}                |   2 +-
 .../tests/popup-view.client.spec.tsx}              |   2 +-
 .../tests/popup.client.spec.ts}                    |   0
 .../tests/service.client.spec.ts}                  | 153 +++-
 packages/client/ui-commands/tsconfig.json          |  45 ++
 .../{ui-question => ui-commands}/tsdown.config.ts  |   2 +-
 packages/client/ui-conversation/README.i18n.yaml   |   4 +-
 packages/client/ui-conversation/README.md          |  20 +-
 packages/client/ui-conversation/README.zh.md       |  34 +-
 packages/client/ui-conversation/package.json       |  14 +-
 .../client/ui-conversation/src/client/apply.ts     |  31 +-
 .../src/client/chat/AssistantMarkdown.tsx          |  77 +-
 .../src/client/chat/AssistantNodeView.tsx          |   2 +-
 .../ui-conversation/src/client/chat/ChatView.tsx   |   4 +-
 .../src/client/chat/CommandNodeView.tsx            |   2 +-
 .../src/client/chat/CompactionItem.tsx             |   2 +-
 .../src/client/chat/ContextBody.tsx                |   2 +-
 .../src/client/chat/MessageIconActions.tsx         |  11 +-
 .../src/client/chat/MessageItem.module.css         |   6 +
 .../src/client/chat/MessageItem.tsx                |  20 +
 .../ui-conversation/src/client/chat/StatsLine.tsx  |  30 +-
 .../src/client/chat/TurnTailNodeView.tsx           |  12 +-
 .../src/client/chat/register-node-renderers.ts     |   9 +-
 .../src/client/chat/tool-node-reader.ts            |   2 +-
 .../src/client/chat/use-calendar-day.ts            |   2 +-
 .../ui-conversation/src/client/contract/slots.ts   |  40 +-
 .../src/client/conversation-nodes/assistant.ts     |   1 +
 .../conversation-nodes/chat-snapshot-builder.ts    |   3 +-
 .../src/client/conversation-nodes/command.ts       |  22 +-
 .../src/client/conversation-nodes/common.ts        |   5 +-
 .../src/client/conversation-nodes/compaction.ts    |  12 +-
 .../src/client/conversation-nodes/message.ts       |   2 +-
 .../src/client/conversation-nodes/register.ts      |   2 +
 .../src/client/conversation-nodes/retry.ts         |   2 +-
 .../src/client/conversation-nodes/tool.ts          |   2 +-
 .../client/conversation-nodes/turn-max-tokens.ts   |  82 +++
 .../src/client/conversation-nodes/turn-tail.ts     |   2 +-
 .../ui-conversation/src/client/image-labels.ts     |  70 +-
 .../client/ui-conversation/src/client/index.ts     |   3 +-
 .../ui-conversation/src/client/input/blocks.ts     |   2 +-
 .../ui-conversation/src/client/input/contract.ts   |   8 +-
 .../src/client/input/decorations.ts                |   2 +-
 .../ui-conversation/src/client/input/facade.ts     |  38 +-
 .../client/ui-conversation/src/client/input/hub.ts |  30 +-
 .../ui-conversation/src/client/input/machine.ts    |   4 +-
 .../client/ui-conversation/src/client/locales.ts   |  32 +-
 .../client/ui-conversation/src/client/service.ts   |  16 +-
 .../client/skeleton/ConversationRoot.module.css    |  49 +-
 .../src/client/skeleton/ConversationRoot.tsx       |   6 +-
 .../src/client/skeleton/ConversationSession.tsx    |  49 +-
 .../src/client/skeleton/DetailsPanel.tsx           |   2 +-
 .../src/client/skeleton/EmptyHero.tsx              |   6 +-
 .../src/client/skeleton/HeroShell.module.css       |  34 +-
 .../src/client/skeleton/InputBar.module.css        |  19 -
 .../src/client/skeleton/InputBar.tsx               | 166 +++--
 .../src/client/skeleton/PermissionSelect.tsx       |   2 +-
 .../client/ui-conversation/src/client/stores.ts    |   2 +-
 ...nject.spec.tsx => apply-inject.client.spec.tsx} |   8 +-
 ....spec.tsx => assembly-surfaces.client.spec.tsx} |  18 +-
 ...t-apply.spec.tsx => chat-apply.client.spec.tsx} |   6 +-
 ....spec.tsx => chat-branch-tails.client.spec.tsx} |  32 +-
 ...-fixture.ts => chat-snapshot-fixture.client.ts} |   2 +-
 ...t-stats.spec.tsx => chat-stats.client.spec.tsx} |  83 ++-
 ...hat-store.spec.ts => chat-store.client.spec.ts} |   0
 ...hat-view.spec.tsx => chat-view.client.spec.tsx} |  25 +-
 ...eter.spec.tsx => context-meter.client.spec.tsx} |   0
 ...> conversation-node-definitions.client.spec.ts} | 101 ++-
 ...ils.spec.tsx => coverage-tails.client.spec.tsx} |   0
 ...spec.tsx => enter-behavior-row.client.spec.tsx} |   2 +-
 ....spec.tsx => gate-branch-tails.client.spec.tsx} |  18 +-
 .../tests/{host.spec.ts => host.client.spec.ts}    |   4 +-
 ...abels.spec.tsx => image-labels.client.spec.tsx} |  56 ++
 ...nput-bar.spec.tsx => input-bar.client.spec.tsx} | 167 ++++-
 ...achine.spec.ts => input-machine.client.spec.ts} |   4 +-
 ...atrix.spec.tsx => input-matrix.client.spec.tsx} |   6 +-
 ...os.spec.tsx => input-scenarios.client.spec.tsx} |  48 +-
 ...ue-dock.spec.tsx => queue-dock.client.spec.tsx} |   2 +-
 ...-row.spec.tsx => reasoning-row.client.spec.tsx} |   0
 ...spec.tsx => selection-survival.client.spec.tsx} |   4 +-
 ...pec.ts => service-orchestration.client.spec.ts} |  22 +-
 ...{skeleton.spec.tsx => skeleton.client.spec.tsx} |   4 +-
 ...cy.spec.ts => submission-policy.client.spec.ts} |   0
 ...o-panel.spec.tsx => todo-panel.client.spec.tsx} |   0
 ...metrics.spec.ts => turn-metrics.client.spec.ts} |   2 +-
 ...n.spec.tsx => views-type-chain.client.spec.tsx} |   8 +-
 packages/client/ui-conversation/tsconfig.json      |  12 +-
 packages/client/ui-deliverables/README.i18n.yaml   |   4 +-
 packages/client/ui-deliverables/README.md          |  17 +-
 packages/client/ui-deliverables/README.zh.md       |  21 +-
 packages/client/ui-deliverables/package.json       |   6 +-
 packages/client/ui-deliverables/src/index.ts       |  31 +-
 packages/client/ui-deliverables/src/invariant.ts   |   7 +-
 ...les.spec.tsx => produced-files.client.spec.tsx} |  11 +-
 .../ui-deliverables/tests/prompt.client.spec.ts    |  30 +
 packages/client/ui-deliverables/tsconfig.json      |   5 +-
 .../ui-directory-picker-browse/README.i18n.yaml    |   6 +
 .../client/ui-directory-picker-browse/README.md    |  24 +
 .../client/ui-directory-picker-browse/README.zh.md |  24 +
 .../client/ui-directory-picker-browse/package.json |  80 ++
 .../src/client/DirectoryBrowser.module.css         |   0
 .../src/client/DirectoryBrowser.tsx                |   2 +-
 .../ui-directory-picker-browse}/src/client/flow.ts |   0
 .../src/client/index.ts                            |   4 +-
 .../src/css-modules.d.ts                           |   0
 .../client/ui-directory-picker-browse/src/index.ts |  10 +
 .../ui-directory-picker-browse/src/invariant.ts    |  31 +
 .../tests/client-flow.client.spec.tsx}             |  21 +-
 .../tests/directory-browser.client.spec.tsx}       |   2 +-
 .../tsconfig.json                                  |  10 +-
 .../ui-directory-picker-browse/tsdown.config.ts    |   3 +
 .../ui-directory-picker-native/README.i18n.yaml    |   6 +
 .../client/ui-directory-picker-native/README.md    |  22 +
 .../client/ui-directory-picker-native/README.zh.md |  22 +
 .../client/ui-directory-picker-native/package.json |  71 ++
 .../ui-directory-picker-native}/src/client/flow.ts |   4 +-
 .../src/client/index.ts                            |   2 +-
 .../client/ui-directory-picker-native/src/index.ts |  10 +
 .../ui-directory-picker-native/src/invariant.ts    |  31 +
 .../tests/client-flow.client.spec.tsx}             |  19 +-
 .../ui-directory-picker-native/tsconfig.json       |  24 +
 .../ui-directory-picker-native/tsdown.config.ts    |   3 +
 packages/client/ui-goal/package.json               |   2 +-
 packages/client/ui-goal/src/client/GoalBar.tsx     |   4 +-
 packages/client/ui-goal/src/client/index.ts        |  37 +-
 packages/client/ui-goal/src/client/slots.ts        |  12 +-
 ...gin.spec.tsx => browser-plugin.client.spec.tsx} |  77 +-
 ...spec.tsx => goal-command-input.client.spec.tsx} |   0
 .../{goalbar.spec.tsx => goalbar.client.spec.tsx}  |  16 +-
 packages/client/ui-goal/tsconfig.json              |   2 +-
 .../README.i18n.yaml                               |   6 +-
 packages/client/ui-input-trigger/README.md         |  25 +
 packages/client/ui-input-trigger/README.zh.md      |  25 +
 .../{ui-slash => ui-input-trigger}/package.json    |   6 +-
 .../src/client/MenuView.module.css                 |   0
 .../src/client/MenuView.tsx                        |   6 +-
 .../src/client/contract.ts                         |  14 +-
 .../src/client/controller.ts                       |  36 +-
 .../src/client/index.ts                            |  30 +-
 .../src/client/locales.ts                          |   0
 .../src/client/service.ts                          |  32 +-
 .../src/client/slots.ts                            |   4 +-
 .../src/core/contract.ts                           |   8 +-
 .../src/core/detect.ts                             |   2 +-
 .../src/core/menu.ts                               |   6 +-
 .../src/css-modules.d.ts                           |   0
 .../{ui-slash => ui-input-trigger}/src/index.ts    |   0
 .../src/invariant.ts                               |   8 +-
 .../{ui-slash => ui-input-trigger}/src/types.ts    |  16 +-
 .../tests/apply.client.spec.ts}                    |  32 +-
 .../tests/core-detect.client.spec.ts}              |   0
 .../tests/core-menu.client.spec.ts}                |   0
 .../tests/menu-view.client.spec.tsx}               |   4 +-
 .../tests/service.client.spec.ts}                  | 128 ++--
 .../{ui-slash => ui-input-trigger}/tsconfig.json   |   2 +-
 packages/client/ui-input-trigger/tsdown.config.ts  |   3 +
 .../client/{ui-task => ui-jobs}/README.i18n.yaml   |   6 +-
 packages/client/ui-jobs/README.md                  |  24 +
 packages/client/{ui-task => ui-jobs}/README.zh.md  |  12 +-
 packages/client/{ui-task => ui-jobs}/package.json  |   8 +-
 .../src/client/JobListAction.module.css}           |   2 +-
 .../src/client/JobListAction.tsx}                  |  76 +-
 .../{ui-task => ui-jobs}/src/client/index.ts       |  22 +-
 .../{ui-task => ui-jobs}/src/client/locales.ts     |  20 +-
 .../{ui-slash => ui-jobs}/src/css-modules.d.ts     |   0
 packages/client/{ui-task => ui-jobs}/src/index.ts  |   2 +-
 .../client/{ui-task => ui-jobs}/src/invariant.ts   |  10 +-
 .../tests/browser-plugin.client.spec.ts}           |  32 +-
 .../tests/job-list-action.client.spec.tsx}         | 118 +--
 packages/client/{ui-task => ui-jobs}/tsconfig.json |   2 +-
 .../client/{ui-task => ui-jobs}/tsdown.config.ts   |   2 +-
 packages/client/ui-layout/README.i18n.yaml         |   4 +-
 packages/client/ui-layout/README.md                |   2 +-
 packages/client/ui-layout/README.zh.md             |   2 +-
 packages/client/ui-layout/package.json             |   2 +-
 packages/client/ui-layout/src/client/columns.ts    |   8 +-
 packages/client/ui-layout/src/client/index.ts      |   6 +-
 packages/client/ui-layout/src/client/service.ts    |   6 +-
 .../client/ui-layout/src/client/theme-presenter.ts |   2 +-
 ...pp-frame.spec.tsx => app-frame.client.spec.tsx} |   0
 .../tests/{apply.spec.ts => apply.client.spec.ts}  |  20 +-
 .../{columns.spec.ts => columns.client.spec.ts}    |   2 +-
 ...t-store.spec.ts => layout-store.client.spec.ts} |   0
 .../{service.spec.ts => service.client.spec.ts}    |  12 +-
 ...nter.spec.ts => theme-presenter.client.spec.ts} |   0
 packages/client/ui-layout/tsconfig.json            |   2 +-
 .../client/ui-message-feedback/README.i18n.yaml    |   6 +
 packages/client/ui-message-feedback/README.md      |  25 +
 packages/client/ui-message-feedback/README.zh.md   |  25 +
 packages/client/ui-message-feedback/package.json   |  86 +++
 .../src/client/MessageFeedbackActions.module.css   | 108 +++
 .../src/client/MessageFeedbackActions.tsx          | 153 ++++
 .../ui-message-feedback/src/client/controller.ts   | 377 ++++++++++
 .../client/ui-message-feedback/src/client/index.ts |  84 +++
 .../ui-message-feedback/src/client/locales.ts      |  43 ++
 .../client/ui-message-feedback/src/client/slots.ts |  64 ++
 .../src/css-modules.d.ts                           |   0
 packages/client/ui-message-feedback/src/index.ts   |   9 +
 .../client/ui-message-feedback/src/invariant.ts    |  33 +
 .../tests/browser-plugin.client.spec.tsx           | 214 ++++++
 .../tests/controller.client.spec.ts                | 674 +++++++++++++++++
 .../tests/message-feedback-actions.client.spec.tsx | 249 +++++++
 .../tsconfig.json                                  |  18 +-
 .../client/ui-message-feedback/tsdown.config.ts    |   3 +
 .../README.i18n.yaml                               |   6 +-
 .../{ui-model => ui-model-selection}/README.md     |   8 +-
 .../{ui-model => ui-model-selection}/README.zh.md  |   8 +-
 .../{ui-model => ui-model-selection}/package.json  |  16 +-
 .../src/client/ModelSelect.module.css              |   0
 .../src/client/ModelSelect.tsx                     |   4 +-
 .../src/client/directory.ts                        |   4 +-
 .../src/client/index.ts                            |  33 +-
 .../src/client/locales.ts                          |   0
 .../src/client/service.ts                          |  26 +-
 .../src/client/slots.ts                            |   2 +-
 .../ui-model-selection}/src/css-modules.d.ts       |   0
 .../{ui-model => ui-model-selection}/src/index.ts  |   0
 .../src/invariant.ts                               |   8 +-
 .../tests/browser-plugin.client.spec.ts}           |  26 +-
 .../tests/model-select.client.spec.tsx}            |   2 +-
 .../{ui-model => ui-model-selection}/tsconfig.json |  10 +-
 .../client/ui-model-selection/tsdown.config.ts     |   3 +
 packages/client/ui-model/tsdown.config.ts          |   3 -
 packages/client/ui-models/tests/readiness.spec.ts  |  97 ---
 packages/client/ui-models/tsdown.config.ts         |   3 -
 .../client/ui-permission-presets/README.i18n.yaml  |   6 +
 .../README.md                                      |   4 +-
 .../README.zh.md                                   |   4 +-
 .../package.json                                   |  20 +-
 .../src/client/PermissionRow.module.css            |   0
 .../src/client/PermissionRow.tsx                   |   0
 .../src/client/index.ts                            |  16 +-
 .../src/client/locales.ts                          |   0
 .../src/client/presentation.ts                     |   2 +-
 .../src/client/settings-store.ts                   |   8 +-
 .../src/css-modules.d.ts                           |   0
 .../src/index.ts                                   |   0
 .../src/invariant.ts                               |   8 +-
 .../tests/browser-plugin.client.spec.ts}           |  16 +-
 .../tests/permission-presets-row.client.spec.tsx}  |  16 +-
 .../tests/settings-store.client.spec.ts}           |  24 +-
 .../tsconfig.json                                  |  11 +-
 .../tsdown.config.ts                               |   2 +-
 packages/client/ui-permission/README.i18n.yaml     |   6 -
 packages/client/ui-plan/package.json               |   8 +-
 .../client/ui-plan/src/client/PlanModeControl.tsx  |   4 +-
 packages/client/ui-plan/src/client/index.ts        |  11 +-
 ...lugin.spec.ts => browser-plugin.client.spec.ts} |  43 +-
 ....spec.tsx => plan-mode-control.client.spec.tsx} |   4 +-
 packages/client/ui-plan/tsconfig.json              |   8 +-
 packages/client/ui-plugin-config/README.i18n.yaml  |   6 -
 .../src/client/PluginConfigSection.module.css      |  36 -
 .../src/client/PluginConfigSection.tsx             |  49 --
 .../client/ui-plugin-config/src/client/index.ts    | 110 ---
 packages/client/ui-plugin-config/tsdown.config.ts  |   3 -
 packages/client/ui-primitives/README.i18n.yaml     |   2 +-
 packages/client/ui-primitives/README.zh.md         |   2 +-
 packages/client/ui-primitives/package.json         |   2 +-
 packages/client/ui-primitives/src/DiffBlock.tsx    |   2 +-
 packages/client/ui-primitives/src/HoverCard.tsx    |   2 +-
 packages/client/ui-primitives/src/JsonTree.tsx     |   2 +-
 packages/client/ui-primitives/src/Menu.module.css  |   9 +
 packages/client/ui-primitives/src/Menu.tsx         |  15 +-
 packages/client/ui-primitives/src/Modal.tsx        |   2 +-
 packages/client/ui-primitives/src/ReadBlock.tsx    |   2 +-
 packages/client/ui-primitives/src/SearchBlock.tsx  |   2 +-
 packages/client/ui-primitives/src/Tooltip.tsx      |   2 +-
 packages/client/ui-primitives/src/WebBlock.tsx     |   2 +-
 packages/client/ui-primitives/src/ansi.ts          |   2 +-
 packages/client/ui-primitives/src/icons/index.tsx  |  12 +
 .../client/ui-primitives/src/markdown/render.tsx   |   2 +-
 packages/client/ui-primitives/src/pointer-grace.ts |   2 +-
 .../ui-primitives/src/useAnchoredMaxHeight.ts      |   2 +-
 .../tests/{ansi.spec.ts => ansi.client.spec.ts}    |   4 +-
 .../{atoms.spec.tsx => atoms.client.spec.tsx}      |   2 +-
 ...e-block.spec.tsx => code-block.client.spec.tsx} |   4 +-
 ...f-block.spec.tsx => diff-block.client.spec.tsx} |   4 +-
 ...er-card.spec.tsx => hover-card.client.spec.tsx} |   2 +-
 .../{icons.spec.tsx => icons.client.spec.tsx}      |   6 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 ...son-tree.spec.tsx => json-tree.client.spec.tsx} |   2 +-
 ...pec.tsx => markdown-dom-parity.client.spec.tsx} |   0
 ...ec.tsx => markdown-incremental.client.spec.tsx} |   0
 ....spec.ts => markdown-plain-text.client.spec.ts} |   6 +-
 ...c.tsx => markdown-render-units.client.spec.tsx} |   2 +-
 ...{markdown.spec.tsx => markdown.client.spec.tsx} |   0
 ...spec.tsx => onboarding-surface.client.spec.tsx} |   0
 ...d-block.spec.tsx => read-block.client.spec.tsx} |   2 +-
 ...block.spec.tsx => search-block.client.spec.tsx} |   0
 ...tate-dot.spec.tsx => state-dot.client.spec.tsx} |   2 +-
 ...ock.spec.tsx => terminal-block.client.spec.tsx} |   2 +-
 .../{toast.spec.tsx => toast.client.spec.tsx}      |   0
 .../{tooltip.spec.tsx => tooltip.client.spec.tsx}  |   2 +-
 ...eb-block.spec.tsx => web-block.client.spec.tsx} |   0
 packages/client/ui-primitives/tsconfig.json        |   2 +-
 .../client/ui-settings-general/README.i18n.yaml    |   4 +-
 packages/client/ui-settings-general/README.md      |   2 +-
 packages/client/ui-settings-general/README.zh.md   |   2 +-
 packages/client/ui-settings-general/package.json   |   2 +-
 .../src/client/SettingsDocumentAction.tsx          |   2 +-
 .../src/client/SettingsRoot.module.css             |  18 +-
 .../src/client/WelcomeNotice.tsx                   |   2 +-
 .../ui-settings-general/src/client/chrome.tsx      |   2 +-
 .../client/ui-settings-general/src/client/index.ts |   6 +-
 .../src/client/settings-document-store.ts          |   2 +-
 .../src/client/welcome-store.ts                    |   4 +-
 .../ui-settings-general/src/onboarding-copy.ts     |   6 +-
 .../tests/{apply.spec.ts => apply.client.spec.ts}  |  14 +-
 ...ponents.spec.tsx => components.client.spec.tsx} |   2 +-
 .../tests/{host.spec.ts => host.client.spec.ts}    |   4 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 ...c.ts => settings-document-store.client.spec.ts} |   2 +-
 ...root.spec.tsx => settings-root.client.spec.tsx} |   0
 .../tests/{shell.spec.ts => shell.client.spec.ts}  |  10 +-
 ...ice.spec.tsx => welcome-notice.client.spec.tsx} |   4 +-
 ...-store.spec.ts => welcome-store.client.spec.ts} |   2 +-
 packages/client/ui-settings-general/tsconfig.json  |   5 +-
 .../README.i18n.yaml                               |   6 +-
 .../{ui-models => ui-settings-models}/README.md    |   6 +-
 .../{ui-models => ui-settings-models}/README.zh.md |   8 +-
 .../{ui-models => ui-settings-models}/package.json |   6 +-
 .../src/client/CustomProviderCard.tsx              |   4 +-
 .../src/client/DeepSeekModelsEditor.tsx            |   0
 .../src/client/DeepSeekOnboardingDialog.module.css |   0
 .../src/client/DeepSeekOnboardingDialog.tsx        |  18 +-
 .../src/client/EditorFooter.tsx                    |   2 +-
 .../src/client/ModelListEditor.tsx                 |   4 +-
 .../src/client/ModelsSection.module.css            |   0
 .../src/client/ModelsSection.tsx                   |  62 +-
 .../src/client/ProviderEditor.tsx                  |   6 +-
 .../src/client/apiKey.ts                           |   4 +-
 .../src/client/index.ts                            |   8 +-
 .../src/client/locales.ts                          |   0
 .../src/client/store.ts                            |  61 +-
 .../client/ui-settings-models/src/css-modules.d.ts |   6 +
 .../{ui-models => ui-settings-models}/src/index.ts |   0
 .../src/invariant.ts                               |   8 +-
 .../tests/apply.client.spec.ts}                    |  18 +-
 .../tests/components.client.spec.tsx}              | 203 ++++--
 .../tests/invariant.client.spec.ts}                |   8 +-
 .../tests/onboarding-dialog.client.spec.tsx}       |   2 +-
 .../tests/provider-form.client.spec.tsx}           |   2 +-
 .../tests/readiness.client.spec.ts                 | 130 ++++
 .../tests/store.client.spec.ts}                    |   4 +-
 .../tests/styles.client.spec.ts}                   |   2 +-
 .../tsconfig.json                                  |   5 +-
 .../client/ui-settings-models/tsdown.config.ts     |   3 +
 .../ui-settings-plugin-inventory/README.i18n.yaml  |   6 +
 .../client/ui-settings-plugin-inventory/README.md  |  20 +
 .../ui-settings-plugin-inventory/README.zh.md      |  20 +
 .../ui-settings-plugin-inventory/package.json      |  80 ++
 .../client/PluginInventorySettingsTab.module.css   | 279 +++++++
 .../src/client/PluginInventorySettingsTab.tsx      | 197 +++++
 .../src/client/index.ts                            |  47 ++
 .../src/client/locales.ts                          |  48 ++
 .../src/css-modules.d.ts                           |   6 +
 .../ui-settings-plugin-inventory/src/index.ts      |   4 +
 .../ui-settings-plugin-inventory/src/invariant.ts  |  20 +
 .../tests/browser-plugin.client.spec.tsx           |  93 +++
 .../tests/components.client.spec.tsx               | 127 ++++
 .../tests/invariant.client.spec.ts                 |  15 +
 .../ui-settings-plugin-inventory/tsconfig.json     |  36 +
 .../ui-settings-plugin-inventory/tsdown.config.ts  |   3 +
 .../client/ui-settings-plugins/README.i18n.yaml    |   6 +
 .../README.md                                      |   8 +-
 .../README.zh.md                                   |   8 +-
 .../package.json                                   |   8 +-
 .../src/client/AgentLoopCard.tsx                   |   4 +-
 .../src/client/BashCard.tsx                        |   4 +-
 .../src/client/ConfigurablePluginsTab.tsx          |  25 +
 .../src/client/PluginCard.module.css               |   0
 .../src/client/PluginCard.tsx                      |  10 +-
 .../src/client/PluginsSettingsSection.module.css   |  85 +++
 .../src/client/PluginsSettingsSection.tsx          | 123 ++++
 .../src/client/WebSearchCard.tsx                   |   4 +-
 .../src/client/agent-loop-card-controller.ts}      |   2 +-
 .../src/client/bash-card-controller.ts}            |   4 +-
 .../src/client/card-form.ts}                       |   2 +-
 .../src/client/fields.module.css                   |   0
 .../src/client/fields.tsx                          |   2 +-
 .../client/ui-settings-plugins/src/client/index.ts | 158 ++++
 .../src/client/locales.ts                          |  24 +-
 .../src/client/slot-contract.ts                    |   0
 .../src/client/web-search-card-controller.ts}      |   2 +-
 .../src/css-modules.d.ts                           |   0
 .../src/index.ts                                   |   6 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/apply.client.spec.ts}                    |  55 +-
 .../tests/fields.client.spec.tsx}                  |   0
 .../tests/invariant.client.spec.ts}                |   8 +-
 .../tests/section.client.spec.tsx}                 | 114 ++-
 .../tests/stores.client.spec.ts}                   |   8 +-
 .../tsconfig.json                                  |   7 +-
 .../client/ui-settings-plugins/tsdown.config.ts    |   3 +
 packages/client/ui-settings/README.i18n.yaml       |   4 +-
 packages/client/ui-settings/README.md              |   2 +-
 packages/client/ui-settings/README.zh.md           |   2 +-
 packages/client/ui-settings/package.json           |   5 +-
 .../ui-settings/src/client/contract/slots.ts       |  15 +
 packages/client/ui-settings/src/client/index.ts    |   8 +-
 .../ui-settings/src/client/settings-scope.ts       |  10 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 .../{plugin.spec.ts => plugin.client.spec.ts}      |   4 +-
 ...scope.spec.ts => settings-scope.client.spec.ts} |  10 +-
 packages/client/ui-settings/tsconfig.json          |   7 +-
 packages/client/ui-sidebar/README.i18n.yaml        |   4 +-
 packages/client/ui-sidebar/README.md               |   8 +-
 packages/client/ui-sidebar/README.zh.md            |   8 +-
 packages/client/ui-sidebar/package.json            |   2 +-
 .../ui-sidebar/src/client/SidebarRoot.module.css   |   8 +-
 .../client/ui-sidebar/src/client/contract/slots.ts |   4 +-
 packages/client/ui-sidebar/src/client/index.ts     |   2 +-
 ....snap => sidebar-snapshot.client.spec.tsx.snap} |   0
 .../{apply.spec.tsx => apply.client.spec.tsx}      |  12 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 ...spec.tsx => pointer-scrollbars.client.spec.tsx} |   0
 ...ec.ts => scrollbar-quiet-styles.client.spec.ts} |   0
 ...-root.spec.tsx => sidebar-root.client.spec.tsx} |   4 +-
 ...t.spec.tsx => sidebar-snapshot.client.spec.tsx} |   6 +-
 ...tyles.spec.ts => sidebar-styles.client.spec.ts} |   4 +
 packages/client/ui-sidebar/tsconfig.json           |   2 +-
 packages/client/ui-skill/README.i18n.yaml          |   4 +-
 packages/client/ui-skill/README.md                 |   2 +-
 packages/client/ui-skill/README.zh.md              |  12 +-
 packages/client/ui-skill/package.json              |  12 +-
 packages/client/ui-skill/src/client/SkillRow.tsx   |   2 +-
 packages/client/ui-skill/src/client/index.ts       |  19 +-
 ...lugin.spec.ts => browser-plugin.client.spec.ts} |  32 +-
 ...kill-row.spec.tsx => skill-row.client.spec.tsx} |   0
 packages/client/ui-skill/tsconfig.json             |   8 +-
 packages/client/ui-slash/README.i18n.yaml          |   6 -
 packages/client/ui-slash/README.md                 |  25 -
 packages/client/ui-slash/README.zh.md              |  25 -
 packages/client/ui-slash/tsdown.config.ts          |   3 -
 packages/client/ui-slots/README.i18n.yaml          |   2 +-
 packages/client/ui-slots/README.zh.md              |  12 +-
 packages/client/ui-slots/package.json              |   2 +-
 packages/client/ui-slots/src/index.ts              |   4 +-
 packages/client/ui-slots/src/invariant.ts          |   2 +-
 packages/client/ui-slots/src/renderer.ts           |   4 +-
 .../tests/{core.spec.ts => core.client.spec.ts}    |   4 +-
 ...ic-keys.spec.ts => dynamic-keys.client.spec.ts} |   0
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 ...e-chain.spec.tsx => type-chain.client.spec.tsx} |   2 +-
 packages/client/ui-slots/tsconfig.json             |   2 +-
 packages/client/ui-subagent/README.i18n.yaml       |   4 +-
 packages/client/ui-subagent/README.md              |   4 +-
 packages/client/ui-subagent/README.zh.md           |   4 +-
 packages/client/ui-subagent/package.json           |   8 +-
 packages/client/ui-subagent/src/client/index.ts    |  10 +-
 ...lugin.spec.ts => browser-plugin.client.spec.ts} |  28 +-
 ...ui.spec.tsx => conversation-ui.client.spec.tsx} |   2 +-
 packages/client/ui-subagent/tsconfig.json          |   4 +-
 packages/client/ui-task/README.md                  |  24 -
 packages/client/ui-theme/README.i18n.yaml          |   4 +-
 packages/client/ui-theme/README.md                 |   4 +-
 packages/client/ui-theme/README.zh.md              |   8 +-
 packages/client/ui-theme/package.json              |   4 +-
 packages/client/ui-theme/src/client/index.ts       |   8 +-
 packages/client/ui-theme/src/index.ts              |   4 +-
 .../client/ui-theme/src/styles/design-platform.css |   2 +
 ...row.spec.tsx => appearance-row.client.spec.tsx} |   4 +-
 .../tests/{apply.spec.ts => apply.client.spec.ts}  |  30 +-
 ...oot-theme.spec.ts => boot-theme.client.spec.ts} |   0
 .../tests/{host.spec.ts => host.client.spec.ts}    |  14 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |  12 +-
 ...les.spec.ts => scrollbar-styles.client.spec.ts} |   2 +-
 ...store.spec.ts => settings-store.client.spec.ts} |   0
 .../tests/{theme.spec.ts => theme.client.spec.ts}  |   8 +-
 packages/client/ui-theme/tsconfig.json             |   2 +-
 packages/client/ui-tool/README.i18n.yaml           |   4 +-
 packages/client/ui-tool/README.md                  |   2 +-
 packages/client/ui-tool/README.zh.md               |  28 +-
 packages/client/ui-tool/package.json               |   8 +-
 .../client/ui-tool/src/client/tool/ToolDetails.tsx |   2 +-
 .../ui-tool/src/client/tool/components/ToolRow.tsx |   2 +-
 .../src/client/tool/models/terminal-card-model.ts  |   2 +-
 .../src/client/tool/toolviews/ask-question-row.tsx |   2 +-
 .../src/client/tool/toolviews/search-row.tsx       |   9 +-
 .../ui-tool/src/client/tool/toolviews/todo-row.tsx |   2 +-
 .../ui-tool/src/client/tool/toolviews/web-row.tsx  |   5 +-
 ...w.spec.tsx => ask-question-row.client.spec.tsx} |   6 +-
 ....spec.tsx => assembly-surfaces.client.spec.tsx} |  10 +-
 ...spec.tsx => chat-code-subcalls.client.spec.tsx} |  20 +-
 ...ils.spec.tsx => coverage-tails.client.spec.tsx} |   2 +-
 ...iff-card.spec.tsx => diff-card.client.spec.tsx} |  12 +-
 ...ead-card.spec.tsx => read-card.client.spec.tsx} |  12 +-
 ...h-card.spec.tsx => search-card.client.spec.tsx} |  11 +-
 ...card.spec.tsx => terminal-card.client.spec.tsx} |  12 +-
 ...{todo-row.spec.tsx => todo-row.client.spec.tsx} |   0
 ...ree.spec.tsx => tool-call-tree.client.spec.tsx} |   2 +-
 ...s-render.tsx => tool-details-render.client.tsx} |   2 +-
 ...yles.spec.ts => tool-row-styles.client.spec.ts} |   2 +-
 ...{tool-row.spec.tsx => tool-row.client.spec.tsx} |   0
 ...slot.spec.tsx => toolview-slot.client.spec.tsx} |  16 +-
 ...pec.tsx => toolview-type-chain.client.spec.tsx} |   4 +-
 ...{web-card.spec.tsx => web-card.client.spec.tsx} |  11 +-
 packages/client/ui-tool/tsconfig.json              |   5 +-
 packages/client/ui-trajectory/README.i18n.yaml     |   4 +-
 packages/client/ui-trajectory/README.md            |   2 +-
 packages/client/ui-trajectory/README.zh.md         |   2 +-
 packages/client/ui-trajectory/package.json         |   6 +-
 .../ui-trajectory/src/client/TrajectoryCell.tsx    |   2 +-
 .../ui-trajectory/src/client/TrajectoryTable.tsx   |   2 +-
 .../src/client/TrajectoryToolbar.module.css        |  40 -
 .../ui-trajectory/src/client/TrajectoryToolbar.tsx |  23 -
 .../ui-trajectory/src/client/TrajectoryView.tsx    |  29 +-
 .../client/ui-trajectory/src/client/export-log.ts  |  45 --
 packages/client/ui-trajectory/src/client/index.ts  |   2 -
 packages/client/ui-trajectory/src/client/layout.ts |   2 +-
 .../client/ui-trajectory/src/client/locales.ts     |  12 -
 .../src/client/trajectory-assistant-definition.ts  |   1 +
 .../src/client/trajectory-compaction-definition.ts |  30 +-
 .../ui-trajectory/src/client/trajectory-record.ts  |   2 +-
 .../src/client/trajectory-virtual-rows.ts          |   2 +-
 .../ui-trajectory/src/client/views.module.css      |  12 -
 .../tests/{cell.spec.tsx => cell.client.spec.tsx}  |   2 +-
 ...bundle.spec.ts => client-bundle.client.spec.ts} |  13 +-
 ....ts => conversation-definitions.client.spec.ts} |   8 +-
 .../client/ui-trajectory/tests/export-log.spec.ts  |  51 --
 .../{layout.spec.tsx => layout.client.spec.tsx}    |   0
 ...der.spec.ts => snapshot-builder.client.spec.ts} |   0
 .../{table.spec.tsx => table.client.spec.tsx}      |   8 +-
 .../client/ui-trajectory/tests/toolbar.spec.tsx    |  61 --
 .../{views.spec.tsx => views.client.spec.tsx}      |  62 +-
 ...al-rows.spec.ts => virtual-rows.client.spec.ts} |   2 +-
 packages/client/ui-trajectory/tsconfig.json        |   4 +-
 .../README.i18n.yaml                               |   6 +-
 .../{ui-question => ui-user-questions}/README.md   |   2 +-
 .../README.zh.md                                   |  10 +-
 .../package.json                                   |  18 +-
 .../src/client/PlanReviewPanel.module.css          |   0
 .../src/client/PlanReviewPanel.tsx                 |   0
 .../src/client/QuestionComposer.module.css         |   0
 .../src/client/QuestionComposer.tsx                |   2 +-
 .../src/client/contract/slots.ts                   |  10 +-
 .../src/client/index.ts                            |   4 +-
 .../src/client/locales.ts                          |   0
 .../src/css-modules.d.ts                           |   0
 .../src/index.ts                                   |   0
 .../src/invariant.ts                               |   8 +-
 .../tests/browser-plugin.client.spec.ts}           |  18 +-
 .../tests/node-plugin.client.spec.ts}              |  10 +-
 .../tests/plan-review-panel.client.spec.tsx}       |   4 +-
 .../tests/user-questions-composer.client.spec.tsx} |   4 +-
 .../tsconfig.json                                  |   6 +-
 packages/client/ui-user-questions/tsdown.config.ts |   3 +
 packages/client/ui-workflow-run/README.i18n.yaml   |   4 +-
 packages/client/ui-workflow-run/README.md          |   4 +-
 packages/client/ui-workflow-run/README.zh.md       |   8 +-
 packages/client/ui-workflow-run/package.json       |   2 +-
 .../src/client/WorkflowRunPanel.module.css         |   2 -
 .../src/client/WorkflowRunPanel.tsx                |  81 ++-
 .../client/ui-workflow-run/src/client/index.ts     |   2 +-
 ...w-run.spec.tsx => workflow-run.client.spec.tsx} | 230 +++---
 packages/client/ui-workflow-run/tsconfig.json      |   2 +-
 packages/client/ui-workspace/README.i18n.yaml      |   4 +-
 packages/client/ui-workspace/README.md             |   4 +-
 packages/client/ui-workspace/README.zh.md          |   4 +-
 packages/client/ui-workspace/package.json          |   2 +-
 .../src/client/WorkspaceBrowser.module.css         | 268 ++++++-
 .../ui-workspace/src/client/WorkspaceBrowser.tsx   | 804 +++++++++++++++++----
 .../ui-workspace/src/client/contract/slots.ts      |  11 +-
 packages/client/ui-workspace/src/client/index.ts   |   9 +-
 packages/client/ui-workspace/src/client/locales.ts |  16 +-
 .../ui-workspace/src/client/rows/Rows.module.css   |  87 ++-
 .../client/ui-workspace/src/client/rows/Rows.tsx   | 123 ++--
 packages/client/ui-workspace/src/client/stores.ts  |  65 +-
 packages/client/ui-workspace/src/client/tree.ts    |  64 +-
 .../tests/{apply.spec.ts => apply.client.spec.ts}  |  14 +-
 ...tyles.spec.ts => browser-styles.client.spec.ts} |  49 +-
 ...{invariant.spec.ts => invariant.client.spec.ts} |   4 +-
 ...ly.spec.tsx => rename-assembly.client.spec.tsx} |   6 +-
 .../tests/{rows.spec.tsx => rows.client.spec.tsx}  |  18 +-
 .../tests/{tree.spec.ts => tree.client.spec.ts}    |  70 +-
 ....spec.tsx => workspace-browser.client.spec.tsx} | 413 ++++++++++-
 ...r.spec.tsx => workspace-picker.client.spec.tsx} |   4 +-
 packages/client/ui-workspace/tsconfig.json         |   2 +-
 packages/client/web-react/README.i18n.yaml         |   4 +-
 packages/client/web-react/README.md                |   2 +-
 packages/client/web-react/README.zh.md             |   2 +-
 packages/client/web-react/package.json             |   2 +-
 packages/client/web-react/src/bind.ts              |   2 +-
 packages/client/web-react/src/scoped-slots.tsx     |   4 +-
 packages/client/web-react/src/use-invoke.ts        |   2 +-
 .../tests/{bind.spec.tsx => bind.client.spec.tsx}  |   0
 ....tsx => scoped-slots-real-core.client.spec.tsx} |   2 +-
 ...slots.spec.tsx => scoped-slots.client.spec.tsx} |   4 +-
 ...r.spec.tsx => session-provider.client.spec.tsx} |   2 +-
 ...pec.tsx => stale-authorization.client.spec.tsx} |   0
 ...-invoke.spec.tsx => use-invoke.client.spec.tsx} |   0
 ...ion.spec.tsx => use-projection.client.spec.tsx} |   4 +-
 packages/client/web-react/tsconfig.json            |   2 +-
 packages/client/web/README.i18n.yaml               |   2 +-
 packages/client/web/README.zh.md                   |   4 +-
 packages/client/web/package.json                   |   2 +-
 packages/client/web/src/AppRoot.tsx                |   4 +-
 packages/client/web/src/DocumentTitle.tsx          |   2 +-
 packages/client/web/src/app.tsx                    |   2 +-
 packages/client/web/src/boot.tsx                   |   2 +-
 packages/client/web/src/loader-status.ts           |   2 +-
 ...{app-root.spec.tsx => app-root.client.spec.tsx} |   2 +-
 ...pp-shell.spec.tsx => app-shell.client.spec.tsx} |  10 +-
 .../tests/{app.spec.tsx => app.client.spec.tsx}    |   4 +-
 ...e-styles.spec.ts => base-styles.client.spec.ts} |   2 +-
 ...tle.spec.tsx => document-title.client.spec.tsx} |   0
 packages/client/web/tsconfig.json                  |   2 +-
 packages/code-runtime/README.i18n.yaml             |   4 +-
 packages/code-runtime/README.md                    |   2 +-
 packages/code-runtime/README.zh.md                 |   4 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |   8 +-
 .../README.zh.md                                   |   8 +-
 .../package.json                                   |   6 +-
 .../src/bootstrap.ts                               |   8 +-
 .../src/index.ts                                   |  30 +-
 .../src/invariant.ts                               |   8 +-
 .../src/output-json.ts                             |   4 +-
 .../src/protocol.ts                                |   2 +-
 .../src/worker-json.ts                             |   7 +-
 .../src/worker.ts                                  |   4 +-
 .../tests/bootstrap.spec.ts                        |   0
 .../tests/built-lib.e2e.ts                         |   4 +-
 .../tests/output-json.spec.ts                      |   2 +-
 .../tests/runtime.spec.ts                          |  34 +-
 .../tests/source-worker.compat.spec.ts             |   2 +-
 .../tests/worker-json.spec.ts                      |   0
 .../tsconfig.json                                  |   2 +-
 .../tsdown.config.ts                               |   0
 packages/code-runtime/code-runtime/package.json    |   2 +-
 .../code-runtime/tests/service.spec.ts             |   4 +-
 packages/code-runtime/code-runtime/tsconfig.json   |   2 +-
 packages/compact/README.md                         |  16 -
 packages/compact/README.zh.md                      |  16 -
 packages/{compact => compaction}/README.i18n.yaml  |   6 +-
 packages/compaction/README.md                      |  16 +
 packages/compaction/README.zh.md                   |  16 +
 .../command-compact/README.i18n.yaml               |   6 +-
 .../command-compact/README.md                      |  14 +-
 .../command-compact/README.zh.md                   |  14 +-
 .../command-compact/package.json                   |   8 +-
 .../command-compact/src/index.ts                   |   6 +-
 .../command-compact/src/invariant.ts               |   0
 .../command-compact/tests/command-compact.spec.ts  |  32 +-
 .../command-compact/tests/invariant.spec.ts        |   2 +-
 .../tests/loader-composition.spec.ts               |  32 +-
 .../command-compact/tsconfig.json                  |   4 +-
 .../compaction-basic}/README.i18n.yaml             |   6 +-
 .../compaction-basic}/README.md                    |  40 +-
 .../compaction-basic}/README.zh.md                 |  42 +-
 .../compaction-basic}/package.json                 |  16 +-
 .../compaction-basic}/src/config.ts                |  36 +-
 .../compaction-basic}/src/index.ts                 |  34 +-
 .../compaction-basic}/src/invariant.ts             |   8 +-
 .../compaction-basic}/src/region.ts                |  40 +-
 .../compaction-basic}/src/summarizer.ts            |   8 +-
 .../compaction-basic}/src/types.ts                 |   8 +-
 .../tests/compaction-basic.spec.ts}                | 196 ++---
 .../tests/compaction-loop-repro.spec.ts}           |  46 +-
 .../tests/loader-composition.spec.ts               |  54 +-
 .../tests/manual-compaction.spec.ts}               | 144 ++--
 .../compaction-basic}/tsconfig.json                |   6 +-
 .../README.i18n.yaml                               |   6 +-
 .../compaction-tool-result-pruner}/README.md       |  12 +-
 .../compaction-tool-result-pruner}/README.zh.md    |  12 +-
 .../compaction-tool-result-pruner}/package.json    |  10 +-
 .../compaction-tool-result-pruner}/src/config.ts   |   4 +-
 .../compaction-tool-result-pruner}/src/index.ts    |  18 +-
 .../src/invariant.ts                               |   8 +-
 .../compaction-tool-result-pruner}/src/types.ts    |   0
 .../tests/loader-composition.spec.ts               |  20 +-
 .../tests/tool-result-pruner.spec.ts}              |  30 +-
 .../compaction-tool-result-pruner}/tsconfig.json   |   4 +-
 .../compaction}/README.i18n.yaml                   |   6 +-
 .../compact => compaction/compaction}/README.md    |  34 +-
 .../compact => compaction/compaction}/README.zh.md |  36 +-
 .../compact => compaction/compaction}/package.json |   8 +-
 .../compact => compaction/compaction}/src/brand.ts |   0
 .../compaction}/src/checkpoint.ts                  |  10 +-
 .../compact => compaction/compaction}/src/index.ts |  32 +-
 .../compaction}/src/invariant.ts                   |  74 +-
 .../compaction}/src/tool-pairing.ts                |   4 +-
 .../compact => compaction/compaction}/src/types.ts |  26 +-
 .../compaction/tests/compaction.spec.ts}           |  64 +-
 .../compaction}/tests/invariant.spec.ts            | 190 ++---
 .../compaction}/tests/tool-pairing.spec.ts         |   2 +-
 .../compaction}/tsconfig.json                      |   2 +-
 .../compaction}/tsdown.config.ts                   |   0
 packages/context/README.i18n.yaml                  |   4 +-
 packages/context/README.md                         |   8 +-
 packages/context/README.zh.md                      |   8 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |   4 +-
 .../README.zh.md                                   |   4 +-
 .../package.json                                   |  10 +-
 .../src/config.ts                                  |   4 +-
 .../src/digest.ts                                  |   2 +-
 .../src/files.ts                                   |   6 +-
 .../src/index.ts                                   |  28 +-
 .../src/invariant.ts                               |   6 +-
 .../src/render.ts                                  |  10 +-
 .../src/state.ts                                   |  48 +-
 .../tests/agent-instructions.e2e.ts}               |  12 +-
 .../tests/agent-instructions.spec.ts}              | 146 ++--
 .../tsconfig.json                                  |   4 +-
 .../context/session-reference/README.i18n.yaml     |   4 +-
 packages/context/session-reference/README.md       |   6 +-
 packages/context/session-reference/README.zh.md    |   6 +-
 packages/context/session-reference/package.json    |  12 +-
 packages/context/session-reference/src/index.ts    |  10 +-
 .../context/session-reference/src/projection.ts    |   8 +-
 packages/context/session-reference/src/uri.ts      |   4 +-
 .../tests/session-reference.spec.ts                |  86 +--
 packages/context/session-reference/tsconfig.json   |   6 +-
 packages/context/time-context/package.json         |   2 +-
 packages/context/time-context/src/index.ts         |   4 +-
 packages/context/time-context/src/invariant.ts     |   2 +-
 packages/context/time-context/src/request-zone.ts  |   4 +-
 .../context/time-context/tests/invariant.spec.ts   |   8 +-
 .../time-context/tests/time-context.spec.ts        |   6 +-
 packages/context/time-context/tsconfig.json        |   4 +-
 packages/context/tmux-context/README.i18n.yaml     |   4 +-
 packages/context/tmux-context/README.md            |   4 +-
 packages/context/tmux-context/README.zh.md         |  12 +-
 packages/context/tmux-context/package.json         |   6 +-
 packages/context/tmux-context/src/index.ts         |  12 +-
 .../tmux-context/tests/tmux-context.spec.ts        |  22 +-
 packages/context/tmux-context/tsconfig.json        |   4 +-
 packages/core/README.i18n.yaml                     |   2 +-
 packages/core/README.zh.md                         |   4 +-
 packages/core/agent-default-model/README.i18n.yaml |   4 +-
 packages/core/agent-default-model/README.md        |   2 +-
 packages/core/agent-default-model/README.zh.md     |   2 +-
 packages/core/agent-default-model/package.json     |   2 +-
 packages/core/agent-default-model/src/index.ts     |   6 +-
 .../tests/agent-default-model.spec.ts              |  14 +-
 packages/core/agent-default-model/tsconfig.json    |   2 +-
 packages/core/agent-loop/README.i18n.yaml          |   4 +-
 packages/core/agent-loop/README.md                 |   2 +-
 packages/core/agent-loop/README.zh.md              |  10 +-
 packages/core/agent-loop/package.json              |   2 +-
 packages/core/agent-loop/src/agent.ts              |   6 +-
 packages/core/agent-loop/src/index.ts              |  20 +-
 packages/core/agent-loop/src/invariant.ts          |   4 +-
 packages/core/agent-loop/src/tool-calls.ts         |  12 +-
 .../core/agent-loop/tests/agent-initiator.spec.ts  |  16 +-
 packages/core/agent-loop/tests/agent.spec.ts       |  10 +-
 packages/core/agent-loop/tests/cancel.spec.ts      |  14 +-
 .../agent-loop/tests/config-session-id.spec.ts     |  60 +-
 .../agent-loop/tests/contract-regressions.spec.ts  |  42 +-
 .../core/agent-loop/tests/coverage-edges.spec.ts   |  10 +-
 .../core/agent-loop/tests/interception.spec.ts     |   8 +-
 packages/core/agent-loop/tests/invariant.spec.ts   |   6 +-
 packages/core/agent-loop/tests/loop.spec.ts        |  30 +-
 packages/core/agent-loop/tests/properties.spec.ts  |  12 +-
 .../core/agent-loop/tests/request-cache.e2e.ts     |  10 +-
 .../core/agent-loop/tests/request-error.spec.ts    |  10 +-
 .../tests/request-reconstruction.spec.ts           |  16 +-
 packages/core/agent-loop/tests/resume.spec.ts      |  76 +-
 .../core/agent-loop/tests/scope-lifecycle.spec.ts  |  12 +-
 packages/core/agent-loop/tests/settings.spec.ts    |  12 +-
 packages/core/agent-loop/tests/tool-calls.spec.ts  |  95 ++-
 packages/core/agent-loop/tests/tool-order.spec.ts  |   8 +-
 packages/core/agent-loop/tsconfig.json             |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |   6 +-
 .../README.zh.md                                   |  10 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |   6 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/agent-tool-presentation.spec.ts}         |   8 +-
 .../tsconfig.json                                  |   2 +-
 packages/core/agent/README.i18n.yaml               |   2 +-
 packages/core/agent/README.zh.md                   |   6 +-
 packages/core/agent/package.json                   |   6 +-
 packages/core/agent/src/index.ts                   |  14 +-
 packages/core/agent/tests/agent-initiator.spec.ts  |   2 +-
 packages/core/agent/tests/agent.spec.ts            |   2 +-
 packages/core/agent/tests/invariant.spec.ts        |   4 +-
 .../core/agent/tests/verify-export-jsdoc.spec.ts   |   2 +-
 packages/core/agent/tsconfig.json                  |   4 +-
 packages/core/scope/README.i18n.yaml               |   2 +-
 packages/core/scope/README.zh.md                   |  10 +-
 packages/core/scope/package.json                   |   2 +-
 packages/core/scope/src/index.ts                   |   2 +-
 packages/core/scope/src/invariant.ts               |   2 +-
 packages/core/scope/tests/invariant.spec.ts        |   6 +-
 packages/core/scope/tests/scope.spec.ts            |   2 +-
 packages/core/scope/tsconfig.json                  |   2 +-
 packages/core/session/README.i18n.yaml             |   4 +-
 packages/core/session/README.md                    |   4 +-
 packages/core/session/README.zh.md                 |  18 +-
 packages/core/session/package.json                 |   6 +-
 packages/core/session/src/chunk-rows.ts            |   4 +-
 packages/core/session/src/index.ts                 |  12 +-
 packages/core/session/src/json.ts                  |   2 +-
 packages/core/session/src/known-event-types.ts     |   8 +-
 packages/core/session/src/repair.ts                |   2 +-
 packages/core/session/src/surface.ts               |   2 +-
 packages/core/session/src/types.ts                 |   4 +-
 packages/core/session/tests/chunk-rows.spec.ts     |   2 +-
 packages/core/session/tests/fork.spec.ts           |   4 +-
 .../session/tests/gen-persistence-catalog.spec.ts  |   2 +-
 packages/core/session/tests/invariant.spec.ts      |   6 +-
 packages/core/session/tests/repair.spec.ts         |   4 +-
 packages/core/session/tests/request-header.spec.ts |   2 +-
 packages/core/session/tests/scoped.spec.ts         |   2 +-
 packages/core/session/tests/session.spec.ts        |   6 +-
 packages/core/session/tests/surface.spec.ts        |   2 +-
 packages/core/session/tests/typert.spec.ts         |   2 +-
 packages/core/session/tsconfig.json                |   4 +-
 packages/core/system-prompt/README.i18n.yaml       |   4 +-
 packages/core/system-prompt/README.md              |   8 +-
 packages/core/system-prompt/README.zh.md           |  16 +-
 packages/core/system-prompt/package.json           |   2 +-
 packages/core/system-prompt/src/index.ts           |   6 +-
 packages/core/system-prompt/src/invariant.ts       |   6 +-
 .../core/system-prompt/tests/invariant.spec.ts     |   4 +-
 packages/core/system-prompt/tests/scoped.spec.ts   |   4 +-
 .../core/system-prompt/tests/system-prompt.spec.ts |  12 +-
 packages/core/system-prompt/tsconfig.json          |   2 +-
 packages/core/tools/README.i18n.yaml               |   4 +-
 packages/core/tools/README.md                      |  14 +-
 packages/core/tools/README.zh.md                   |  30 +-
 packages/core/tools/package.json                   |   2 +-
 packages/core/tools/src/code-mode.ts               |   8 +-
 packages/core/tools/src/index.ts                   | 240 ++++--
 packages/core/tools/src/invariant.ts               |   2 +-
 packages/core/tools/src/json-schema.ts             |   4 +-
 packages/core/tools/src/presentation.ts            |   2 +-
 packages/core/tools/src/schema.ts                  |   2 +-
 packages/core/tools/src/ts-types.ts                |   2 +-
 packages/core/tools/tests/code-mode.spec.ts        | 126 +++-
 packages/core/tools/tests/execution-mode.spec.ts   |   8 +-
 packages/core/tools/tests/gen-tool-catalog.spec.ts |   4 +-
 packages/core/tools/tests/invariant.spec.ts        |  12 +-
 packages/core/tools/tests/json-schema.spec.ts      |   2 +-
 packages/core/tools/tests/properties.spec.ts       |   2 +-
 packages/core/tools/tests/schema.spec.ts           |   2 +-
 packages/core/tools/tests/scoped.spec.ts           |  12 +-
 packages/core/tools/tests/tools.spec.ts            |  27 +-
 packages/core/tools/tests/ts-types.spec.ts         |   2 +-
 packages/core/tools/tsconfig.json                  |   2 +-
 .../credentials/credentials-local/README.i18n.yaml |   4 +-
 packages/credentials/credentials-local/README.md   |   2 +-
 .../credentials/credentials-local/README.zh.md     |   8 +-
 .../credentials/credentials-local/package.json     |  10 +-
 .../credentials/credentials-local/src/index.ts     |  30 +-
 .../credentials-local/tests/drain.spec.ts          |   4 +-
 .../credentials-local/tests/local.spec.ts          |  30 +-
 .../credentials-local/tests/review-fixes.spec.ts   |   8 +-
 .../credentials-local/tests/watcher.spec.ts        |   8 +-
 .../credentials/credentials-local/tsconfig.json    |   6 +-
 packages/credentials/credentials/README.i18n.yaml  |   2 +-
 packages/credentials/credentials/README.zh.md      |  12 +-
 packages/credentials/credentials/package.json      |   2 +-
 packages/credentials/credentials/src/index.ts      |  12 +-
 packages/credentials/credentials/src/invariant.ts  |   4 +-
 .../credentials/tests/credentials.spec.ts          |   4 +-
 .../credentials/tests/invariant.spec.ts            |   8 +-
 packages/credentials/credentials/tests/memory.ts   |   4 +-
 packages/credentials/credentials/tsconfig.json     |   2 +-
 packages/e2b/README.i18n.yaml                      |   4 +-
 packages/e2b/README.md                             |   2 +-
 packages/e2b/README.zh.md                          |   2 +-
 packages/e2b/e2b/README.i18n.yaml                  |   2 +-
 packages/e2b/e2b/README.zh.md                      |   2 +-
 packages/e2b/e2b/package.json                      |   2 +-
 packages/e2b/e2b/src/index.ts                      |   8 +-
 packages/e2b/e2b/tests/composition.e2e.ts          |  14 +-
 packages/e2b/e2b/tests/e2b.spec.ts                 |  28 +-
 packages/e2b/e2b/tsconfig.json                     |   2 +-
 packages/e2b/fs-e2b/README.i18n.yaml               |   2 +-
 packages/e2b/fs-e2b/README.zh.md                   |   4 +-
 packages/e2b/fs-e2b/package.json                   |   2 +-
 packages/e2b/fs-e2b/tests/filesystem.spec.ts       |  10 +-
 packages/e2b/fs-e2b/tsconfig.json                  |   2 +-
 packages/e2b/subprocess-e2b/README.i18n.yaml       |   4 +-
 packages/e2b/subprocess-e2b/README.md              |   2 +-
 packages/e2b/subprocess-e2b/README.zh.md           |  10 +-
 packages/e2b/subprocess-e2b/package.json           |   2 +-
 packages/e2b/subprocess-e2b/src/index.ts           |   8 +-
 packages/e2b/subprocess-e2b/src/process.ts         |   6 +-
 packages/e2b/subprocess-e2b/src/terminal.ts        |   4 +-
 .../e2b/subprocess-e2b/tests/subprocess.spec.ts    |  20 +-
 packages/e2b/subprocess-e2b/tests/terminal.spec.ts |  14 +-
 packages/e2b/subprocess-e2b/tsconfig.json          |   2 +-
 packages/examples/README.i18n.yaml                 |   4 +-
 packages/examples/README.md                        |   2 +-
 packages/examples/README.zh.md                     |   6 +-
 packages/examples/acp-demo/README.i18n.yaml        |   4 +-
 packages/examples/acp-demo/README.md               |   3 +-
 packages/examples/acp-demo/README.zh.md            |  13 +-
 packages/examples/acp-demo/package.json            |   6 +-
 packages/examples/acp-demo/src/bin.ts              |   2 +-
 packages/examples/acp-demo/src/index.ts            |  25 +-
 packages/examples/acp-demo/tests/acp-agent.spec.ts |  49 +-
 packages/examples/acp-demo/tests/built-bin.e2e.ts  |   8 +-
 packages/examples/acp-demo/tests/load-path.e2e.ts  |   4 +-
 packages/examples/acp-demo/tsconfig.json           |   4 +-
 .../examples/agent-spine-demo/README.i18n.yaml     |   4 +-
 packages/examples/agent-spine-demo/README.md       |  20 +-
 packages/examples/agent-spine-demo/README.zh.md    |  20 +-
 packages/examples/agent-spine-demo/package.json    |  34 +-
 packages/examples/agent-spine-demo/src/index.ts    |  84 ++-
 .../agent-spine-demo/tests/agent-core.spec.ts      |  74 +-
 .../tests/multi-project-sandbox.e2e.ts             |  12 +-
 packages/examples/agent-spine-demo/tsconfig.json   |  20 +-
 packages/examples/jsonrpc-demo/README.i18n.yaml    |   4 +-
 packages/examples/jsonrpc-demo/README.md           |   6 +-
 packages/examples/jsonrpc-demo/README.zh.md        |   6 +-
 packages/examples/jsonrpc-demo/package.json        |   4 +-
 packages/examples/jsonrpc-demo/src/bin.ts          |   2 +-
 packages/examples/jsonrpc-demo/src/index.ts        |   4 +-
 packages/examples/jsonrpc-demo/src/invariant.ts    |   8 +-
 packages/examples/jsonrpc-demo/src/packaged-bin.ts |   2 +-
 packages/examples/jsonrpc-demo/src/runner.ts       |   4 +-
 packages/examples/jsonrpc-demo/tsconfig.json       |   2 +-
 .../README.i18n.yaml                               |   4 +-
 .../{self-modification => extensions}/README.md    |   0
 .../{self-modification => extensions}/README.zh.md |   4 +-
 packages/extensions/tool-cordis/README.i18n.yaml   |   6 +
 .../tool-cordis/README.md                          |   4 +-
 .../tool-cordis/README.zh.md                       |   2 +-
 .../tool-cordis/package.json                       |   4 +-
 .../tool-cordis/src/api-catalog.ts                 | 646 ++++++++---------
 .../tool-cordis/src/fiber-state.ts                 |   0
 .../tool-cordis/src/guard.ts                       |   4 +-
 .../tool-cordis/src/index.ts                       |  10 +-
 .../tool-cordis/src/inspect.ts                     |   2 +-
 .../tool-cordis/src/invariant.ts                   |   0
 .../tool-cordis/src/mount.ts                       |   0
 .../tool-cordis/src/present.ts                     |   2 +-
 .../tool-cordis/src/sandbox.ts                     |   4 +-
 .../tool-cordis/tests/cordis-lifecycle.spec.ts     |   0
 .../tool-cordis/tests/cross-mount.spec.ts          |   0
 .../tool-cordis/tests/helpers.ts                   |   8 +-
 .../tool-cordis/tests/inspect.spec.ts              |  10 +-
 .../tool-cordis/tests/integration.spec.ts          |   0
 .../tool-cordis/tests/mount.spec.ts                |   0
 .../tool-cordis/tests/present.spec.ts              |   0
 .../tool-cordis/tests/sandbox-context.spec.ts      |   4 +-
 .../tool-cordis/tests/tool-cordis.spec.ts          |   2 +-
 .../tool-cordis/tests/unmount-hmr.spec.ts          |   6 +-
 .../tool-cordis/tsconfig.json                      |   2 +-
 .../feedback/command-feedback/README.i18n.yaml     |   4 +-
 packages/feedback/command-feedback/README.md       |   6 +-
 packages/feedback/command-feedback/README.zh.md    |  16 +-
 packages/feedback/command-feedback/package.json    |   6 +-
 packages/feedback/command-feedback/src/index.ts    |  12 +-
 .../tests/command-feedback.spec.ts                 |  28 +-
 .../tests/loader-composition.spec.ts               |   8 +-
 packages/feedback/command-feedback/tsconfig.json   |   4 +-
 .../feedback/message-feedback/README.i18n.yaml     |   4 +-
 packages/feedback/message-feedback/README.md       |   2 +-
 packages/feedback/message-feedback/README.zh.md    |   4 +-
 packages/feedback/message-feedback/package.json    |  10 +-
 packages/feedback/message-feedback/src/index.ts    |   6 +-
 .../feedback/message-feedback/tests/helpers.ts     |   2 +-
 .../message-feedback/tests/invariant.spec.ts       |   4 +-
 .../tests/loader-composition.spec.ts               |  10 +-
 .../tests/message-feedback.spec.ts                 |   6 +-
 packages/feedback/message-feedback/tsconfig.json   |   4 +-
 packages/fs/README.i18n.yaml                       |   4 +-
 packages/fs/README.md                              |   4 +-
 packages/fs/README.zh.md                           |   8 +-
 packages/fs/fs-local/README.i18n.yaml              |   4 +-
 packages/fs/fs-local/README.md                     |   2 +-
 packages/fs/fs-local/README.zh.md                  |  10 +-
 packages/fs/fs-local/package.json                  |   2 +-
 packages/fs/fs-local/src/fsio.ts                   |   2 +-
 packages/fs/fs-local/src/index.ts                  |   4 +-
 packages/fs/fs-local/src/win32.ts                  |   2 +-
 packages/fs/fs-local/tests/filesystem.spec.ts      |   4 +-
 packages/fs/fs-local/tests/fsio.spec.ts            |   6 +-
 packages/fs/fs-local/tests/win32.spec.ts           |   2 +-
 packages/fs/fs-local/tsconfig.json                 |   2 +-
 packages/fs/fs-observation-policy/README.i18n.yaml |   6 +
 .../{fs-policy => fs-observation-policy}/README.md |   8 +-
 .../README.zh.md                                   |  20 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |  16 +-
 .../src/invariant.ts                               |   8 +-
 .../src/types.ts                                   |   8 +-
 .../tests/policy.spec.ts                           |  12 +-
 .../tsconfig.json                                  |   2 +-
 packages/fs/fs-sandbox/README.i18n.yaml            |   4 +-
 packages/fs/fs-sandbox/README.md                   |   4 +-
 packages/fs/fs-sandbox/README.zh.md                |   4 +-
 packages/fs/fs-sandbox/package.json                |   2 +-
 packages/fs/fs-sandbox/src/containment.ts          |   2 +-
 packages/fs/fs-sandbox/src/index.ts                |   4 +-
 packages/fs/fs-sandbox/tests/fs-sandbox.spec.ts    |   2 +-
 packages/fs/fs-sandbox/tsconfig.json               |   2 +-
 packages/fs/fs/README.i18n.yaml                    |   4 +-
 packages/fs/fs/README.md                           |   6 +-
 packages/fs/fs/README.zh.md                        |   8 +-
 packages/fs/fs/package.json                        |   2 +-
 packages/fs/fs/src/index.ts                        |   2 +-
 packages/fs/fs/src/invariant.ts                    |   4 +-
 packages/fs/fs/tests/invariant.spec.ts             |   6 +-
 packages/fs/fs/tests/service.spec.ts               |   2 +-
 packages/fs/fs/tsconfig.json                       |   2 +-
 packages/fs/tool-fs-search/README.i18n.yaml        |   4 +-
 packages/fs/tool-fs-search/README.md               |   6 +-
 packages/fs/tool-fs-search/README.zh.md            |   8 +-
 packages/fs/tool-fs-search/package.json            |   6 +-
 packages/fs/tool-fs-search/src/glob.ts             |   2 +-
 packages/fs/tool-fs-search/src/grep.ts             |   6 +-
 packages/fs/tool-fs-search/src/index.ts            |  11 +-
 packages/fs/tool-fs-search/src/presentation.ts     |   4 +-
 packages/fs/tool-fs-search/src/search-core.ts      |  12 +-
 .../fs/tool-fs-search/tests/integration.spec.ts    |  10 +-
 packages/fs/tool-fs-search/tests/load-path.spec.ts |   8 +-
 packages/fs/tool-fs-search/tests/tools.spec.ts     |  22 +-
 packages/fs/tool-fs-search/tsconfig.json           |   6 +-
 packages/fs/tool-fs/README.i18n.yaml               |   4 +-
 packages/fs/tool-fs/README.md                      |  14 +-
 packages/fs/tool-fs/README.zh.md                   |  18 +-
 packages/fs/tool-fs/package.json                   |   4 +-
 packages/fs/tool-fs/src/diff.ts                    |   2 +-
 packages/fs/tool-fs/src/edit.ts                    |   4 +-
 packages/fs/tool-fs/src/index.ts                   |   4 +-
 packages/fs/tool-fs/src/read-render.ts             |   2 +-
 packages/fs/tool-fs/src/read-target.ts             |   4 +-
 packages/fs/tool-fs/src/read.ts                    |   2 +-
 packages/fs/tool-fs/src/sandbox.ts                 |   2 +-
 packages/fs/tool-fs/src/session-cwd.ts             |   2 +-
 packages/fs/tool-fs/src/write.ts                   |   2 +-
 packages/fs/tool-fs/tests/fs-tools.e2e.ts          |   2 +-
 packages/fs/tool-fs/tests/harness.ts               |   2 +-
 packages/fs/tool-fs/tests/integration.spec.ts      |  18 +-
 packages/fs/tool-fs/tests/read-image.spec.ts       |  12 +-
 packages/fs/tool-fs/tests/read-render.spec.ts      |   4 +-
 packages/fs/tool-fs/tests/tools.spec.ts            |  20 +-
 packages/fs/tool-fs/tsconfig.json                  |   4 +-
 .../fs/tool-str-replace-editor/README.i18n.yaml    |   2 +-
 packages/fs/tool-str-replace-editor/README.zh.md   |   8 +-
 packages/fs/tool-str-replace-editor/package.json   |   4 +-
 packages/fs/tool-str-replace-editor/src/index.ts   |   2 +-
 .../fs/tool-str-replace-editor/tests/tools.spec.ts |  10 +-
 packages/fs/tool-str-replace-editor/tsconfig.json  |   2 +-
 packages/goal/README.i18n.yaml                     |   4 +-
 packages/goal/README.md                            |   2 +-
 packages/goal/README.zh.md                         |   2 +-
 packages/goal/command-goal/package.json            |   2 +-
 packages/goal/command-goal/src/index.ts            |   4 +-
 .../goal/command-goal/tests/command-goal.spec.ts   |   8 +-
 packages/goal/command-goal/tsconfig.json           |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../{goal-session => goal-round-driver}/README.md  |   6 +-
 .../README.zh.md                                   |  14 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |  24 +-
 .../src/invariant.ts                               |  10 +-
 .../src/prompt.ts                                  |   0
 .../tests/goal-round-driver.spec.ts}               |   8 +-
 .../tests/invariant.spec.ts                        |  24 +-
 .../tsconfig.json                                  |   2 +-
 .../tsdown.config.ts                               |   0
 packages/goal/goal/package.json                    |  10 +-
 packages/goal/goal/src/index.ts                    |   4 +-
 packages/goal/goal/tests/goal.e2e.ts               |   2 +-
 packages/goal/goal/tests/goal.spec.ts              |   2 +-
 packages/goal/goal/tests/invariant.spec.ts         |   6 +-
 packages/goal/goal/tsconfig.json                   |   4 +-
 packages/goal/tool-goal/README.i18n.yaml           |   2 +-
 packages/goal/tool-goal/README.zh.md               |   4 +-
 packages/goal/tool-goal/package.json               |   2 +-
 packages/goal/tool-goal/src/authority.ts           |   2 +-
 packages/goal/tool-goal/tests/tool-goal.spec.ts    |  12 +-
 packages/goal/tool-goal/tsconfig.json              |   2 +-
 packages/guard/README.i18n.yaml                    |   4 +-
 packages/guard/README.md                           |   2 +-
 packages/guard/README.zh.md                        |   4 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |  10 +-
 .../README.zh.md                                   |  10 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |  20 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/repeat-tool-reminder.spec.ts}            |  10 +-
 .../tsconfig.json                                  |   2 +-
 packages/guard/timeout-policy/README.i18n.yaml     |   4 +-
 packages/guard/timeout-policy/README.md            |   4 +-
 packages/guard/timeout-policy/README.zh.md         |  12 +-
 packages/guard/timeout-policy/package.json         |   4 +-
 packages/guard/timeout-policy/src/index.ts         |   2 +-
 packages/guard/timeout-policy/src/invariant.ts     |   6 +-
 .../timeout-policy/tests/timeout-policy.spec.ts    |  16 +-
 packages/guard/timeout-policy/tsconfig.json        |   2 +-
 packages/hooks/README.i18n.yaml                    |   4 +-
 packages/hooks/README.md                           |   2 +-
 packages/hooks/README.zh.md                        |   4 +-
 packages/hooks/hook-protocol/README.i18n.yaml      |   4 +-
 packages/hooks/hook-protocol/README.md             |  12 +-
 packages/hooks/hook-protocol/README.zh.md          |  16 +-
 packages/hooks/hook-protocol/package.json          |   6 +-
 packages/hooks/hook-protocol/src/codec.ts          |   2 +-
 packages/hooks/hook-protocol/src/detached.ts       |   4 +-
 packages/hooks/hook-protocol/src/events.ts         |   4 +-
 packages/hooks/hook-protocol/src/invariant.ts      |   4 +-
 packages/hooks/hook-protocol/src/matcher.ts        |   4 +-
 packages/hooks/hook-protocol/src/merge.ts          |   2 +-
 packages/hooks/hook-protocol/src/runner.ts         |  10 +-
 packages/hooks/hook-protocol/src/types.ts          |   8 +-
 packages/hooks/hook-protocol/tests/events.spec.ts  |   8 +-
 .../hooks/hook-protocol/tests/invariant.spec.ts    |  14 +-
 packages/hooks/hook-protocol/tests/matcher.spec.ts |  34 +-
 packages/hooks/hook-protocol/tests/runner.spec.ts  |  22 +-
 packages/hooks/hook-protocol/tsconfig.json         |   4 +-
 .../README.i18n.yaml                               |   6 +-
 .../{hooks-claude => hooks-claude-code}/README.md  |  10 +-
 .../README.zh.md                                   |  16 +-
 .../package.json                                   |   8 +-
 .../src/config.ts                                  |  12 +-
 .../src/index.ts                                   |  38 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/bridge.spec.ts                           |  46 +-
 .../tests/config.spec.ts                           |  36 +-
 .../tests/coverage-cases.ts                        |  54 +-
 .../tests/coverage-config.spec.ts                  |   0
 .../tests/coverage-context.spec.ts                 |   0
 .../tests/coverage-edge-paths.spec.ts              |   0
 .../tests/coverage-stop.spec.ts                    |   0
 .../tsconfig.json                                  |   4 +-
 packages/hooks/hooks-codex/README.i18n.yaml        |   2 +-
 packages/hooks/hooks-codex/README.zh.md            |   6 +-
 packages/hooks/hooks-codex/package.json            |   4 +-
 packages/hooks/hooks-codex/src/config.ts           |   2 +-
 packages/hooks/hooks-codex/src/index.ts            |   6 +-
 packages/hooks/hooks-codex/tests/bridge.spec.ts    |  12 +-
 packages/hooks/hooks-codex/tests/coverage-cases.ts |  18 +-
 packages/hooks/hooks-codex/tsconfig.json           |   4 +-
 packages/host/README.i18n.yaml                     |   4 +-
 packages/host/README.md                            |   7 +-
 packages/host/README.zh.md                         |   7 +-
 packages/host/apiproxy/README.i18n.yaml            |   4 +-
 packages/host/apiproxy/README.md                   |  12 +-
 packages/host/apiproxy/README.zh.md                |  28 +-
 packages/host/apiproxy/package.json                |   8 +-
 packages/host/apiproxy/src/api-proxy.ts            | 204 +++---
 packages/host/apiproxy/src/api/commands.schema.ts  |  44 --
 packages/host/apiproxy/src/api/commands.ts         |  50 --
 packages/host/apiproxy/src/api/downloads.schema.ts |   2 +-
 packages/host/apiproxy/src/api/events.schema.ts    |  11 +-
 packages/host/apiproxy/src/api/events.ts           |  12 +-
 packages/host/apiproxy/src/api/index.ts            |   5 +-
 .../src/api/{tasks.schema.ts => jobs.schema.ts}    |  14 +-
 .../host/apiproxy/src/api/{tasks.ts => jobs.ts}    |  10 +-
 packages/host/apiproxy/src/api/questions.schema.ts |   4 +-
 packages/host/apiproxy/src/api/questions.ts        |   4 +-
 packages/host/apiproxy/src/api/rpc-map.ts          |   4 +-
 packages/host/apiproxy/src/api/rpc.schema.ts       |   7 +-
 packages/host/apiproxy/src/api/sessions.schema.ts  |  19 +-
 packages/host/apiproxy/src/api/sessions.ts         |  17 +-
 packages/host/apiproxy/src/api/workspace.schema.ts |  11 +
 packages/host/apiproxy/src/api/workspace.ts        |   9 +
 packages/host/apiproxy/src/fetch/client.ts         |  20 +-
 packages/host/apiproxy/src/fetch/handler.ts        |  16 +-
 packages/host/apiproxy/src/index.ts                |   4 +-
 packages/host/apiproxy/src/native-path-opener.ts   |   2 +-
 packages/host/apiproxy/src/session-export.ts       |   8 +-
 .../apiproxy/tests/api-proxy-agent-preset.spec.ts  |   6 +-
 .../host/apiproxy/tests/api-proxy-approval.spec.ts |  10 +-
 .../host/apiproxy/tests/api-proxy-blank.spec.ts    |   8 +-
 .../host/apiproxy/tests/api-proxy-cold.spec.ts     |  36 +-
 .../host/apiproxy/tests/api-proxy-commands.spec.ts | 427 -----------
 .../host/apiproxy/tests/api-proxy-config.spec.ts   |  34 +-
 .../host/apiproxy/tests/api-proxy-fork.spec.ts     |   8 +-
 ...-proxy-tasks.spec.ts => api-proxy-jobs.spec.ts} |  90 +--
 .../host/apiproxy/tests/api-proxy-models.spec.ts   |   8 +-
 .../apiproxy/tests/api-proxy-projections.spec.ts   |  52 +-
 .../host/apiproxy/tests/api-proxy-question.spec.ts |  10 +-
 .../host/apiproxy/tests/api-proxy-rename.spec.ts   |   4 +-
 .../host/apiproxy/tests/api-proxy-search.spec.ts   |   6 +-
 .../apiproxy/tests/api-proxy-subagents.spec.ts     |   4 +-
 .../host/apiproxy/tests/api-proxy-view.spec.ts     |  14 +-
 .../apiproxy/tests/api-proxy-workspace.spec.ts     |  54 +-
 .../host/apiproxy/tests/client-handler.spec.ts     |  18 +-
 packages/host/apiproxy/tests/fetch-carrier.spec.ts |  69 +-
 .../host/apiproxy/tests/native-path-opener.spec.ts |   2 +-
 packages/host/apiproxy/tests/rpc-schemas.spec.ts   |  89 +--
 .../host/apiproxy/tests/session-export.spec.ts     |  28 +-
 packages/host/apiproxy/tsconfig.json               |   6 +-
 .../host/directory-picker-auto/README.i18n.yaml    |   4 +-
 packages/host/directory-picker-auto/README.md      |   2 +-
 packages/host/directory-picker-auto/README.zh.md   |   4 +-
 packages/host/directory-picker-auto/package.json   |  14 +-
 packages/host/directory-picker-auto/src/index.ts   |  83 ++-
 packages/host/directory-picker-auto/src/resolve.ts |   2 +-
 .../tests/loader-composition.spec.ts               |  58 +-
 .../directory-picker-auto/tests/resolve.spec.ts    |   2 +-
 packages/host/directory-picker-auto/tsconfig.json  |   2 +-
 packages/host/directory-picker-browse/package.json |  36 +-
 packages/host/directory-picker-browse/src/index.ts |   4 +-
 .../directory-picker-browse/tests/service.spec.ts  |   2 +-
 .../host/directory-picker-browse/tsconfig.json     |  19 +-
 .../host/directory-picker-browse/tsdown.config.ts  |  16 +-
 packages/host/directory-picker-native/package.json |  27 +-
 .../src/win32-dialog-logic.ts                      |   2 +-
 .../src/win32-dialog-worker.ts                     |   2 +-
 .../directory-picker-native/src/win32-dialog.ts    |   2 +-
 .../tests/built-worker.e2e.ts                      |   2 +-
 .../tests/win32-dialog-bindings.spec.ts            |   2 +-
 .../tests/win32-dialog-logic.spec.ts               |   2 +-
 .../host/directory-picker-native/tsconfig.json     |  13 +-
 .../host/directory-picker-native/tsdown.config.ts  |  48 +-
 packages/host/directory-picker/README.i18n.yaml    |   2 +-
 packages/host/directory-picker/README.zh.md        |   2 +-
 packages/host/directory-picker/package.json        |   2 +-
 packages/host/directory-picker/tests/seam.spec.ts  |   2 +-
 packages/host/directory-picker/tsconfig.json       |   2 +-
 packages/host/frontend-static/README.i18n.yaml     |   4 +-
 packages/host/frontend-static/README.md            |   2 +-
 packages/host/frontend-static/README.zh.md         |   2 +-
 packages/host/frontend-static/package.json         |   4 +-
 packages/host/frontend-static/src/index.ts         |  12 +-
 packages/host/frontend-static/src/invariant.ts     |   8 +-
 .../frontend-static/tests/frontend-static.spec.ts  |   6 +-
 packages/host/frontend-static/tsconfig.json        |   2 +-
 packages/host/plugin-inventory/README.i18n.yaml    |   6 +
 packages/host/plugin-inventory/README.md           |  22 +
 packages/host/plugin-inventory/README.zh.md        |  22 +
 packages/host/plugin-inventory/package.json        |  68 ++
 packages/host/plugin-inventory/src/index.ts        |  72 ++
 packages/host/plugin-inventory/src/invariant.ts    |  20 +
 packages/host/plugin-inventory/src/types.ts        |  28 +
 .../host/plugin-inventory/tests/invariant.spec.ts  |  16 +
 .../host/plugin-inventory/tests/inventory.spec.ts  |  89 +++
 packages/host/plugin-inventory/tsconfig.json       |  27 +
 packages/host/webserver/README.i18n.yaml           |   4 +-
 packages/host/webserver/README.md                  |   2 +-
 packages/host/webserver/README.zh.md               |  10 +-
 packages/host/webserver/package.json               |   2 +-
 packages/host/webserver/src/index.ts               |  12 +-
 packages/host/webserver/src/invariant.ts           |   4 +-
 packages/host/webserver/tests/webserver.spec.ts    |   6 +-
 packages/host/webserver/tsconfig.json              |   2 +-
 packages/{pty => identity}/README.i18n.yaml        |   6 +-
 packages/identity/README.md                        |   9 +
 packages/identity/README.zh.md                     |   9 +
 .../identity/anonymous-user-id/README.i18n.yaml    |   6 +
 .../anonymous-user-id}/README.md                   |   6 +-
 .../anonymous-user-id}/README.zh.md                |   8 +-
 .../anonymous-user-id}/package.json                |  10 +-
 .../anonymous-user-id}/src/index.ts                |  12 +-
 .../anonymous-user-id}/src/invariant.ts            |   8 +-
 .../tests/anonymous-user-id.spec.ts}               |  20 +-
 .../anonymous-user-id}/tests/invariant.spec.ts     |   6 +-
 .../anonymous-user-id}/tsconfig.json               |   4 +-
 packages/interaction/README.i18n.yaml              |   4 +-
 packages/interaction/README.md                     |   6 +-
 packages/interaction/README.zh.md                  |  12 +-
 packages/interaction/commands/package.json         |  21 +-
 packages/interaction/commands/src/index.ts         |  60 +-
 packages/interaction/commands/src/types.ts         |  39 +
 .../interaction/commands/tests/commands.spec.ts    |   6 +-
 .../interaction/commands/tests/invariant.spec.ts   |   6 +-
 packages/interaction/commands/tsconfig.json        |   5 +-
 .../README.i18n.yaml                               |   6 +-
 packages/interaction/permission-presets/README.md  |  28 +
 .../interaction/permission-presets/README.zh.md    |  28 +
 .../package.json                                   |  12 +-
 .../src/client.ts                                  |   2 +-
 .../src/index.ts                                   |  30 +-
 .../src/invariant.ts                               |  12 +-
 .../src/types.ts                                   |   2 +-
 .../tests/invariant.spec.ts                        |  10 +-
 .../tests/permission-presets.spec.ts}              |  88 +--
 .../tests/projection.spec.ts                       |  20 +-
 .../tsconfig.json                                  |   4 +-
 packages/interaction/permission/README.md          |  28 -
 packages/interaction/permission/README.zh.md       |  28 -
 .../interaction/tool-ask-user/README.i18n.yaml     |   4 +-
 packages/interaction/tool-ask-user/README.md       |   6 +-
 packages/interaction/tool-ask-user/README.zh.md    |   6 +-
 packages/interaction/tool-ask-user/package.json    |   8 +-
 packages/interaction/tool-ask-user/src/index.ts    |  10 +-
 .../tool-ask-user/tests/tool-ask-user.spec.ts      |  38 +-
 packages/interaction/tool-ask-user/tsconfig.json   |   4 +-
 .../interaction/user-approval/README.i18n.yaml     |   2 +-
 packages/interaction/user-approval/README.zh.md    |   4 +-
 packages/interaction/user-approval/package.json    |   2 +-
 .../user-approval/tests/approval.spec.ts           |   2 +-
 .../user-approval/tests/invariant.spec.ts          |   8 +-
 packages/interaction/user-approval/tsconfig.json   |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../{user-interaction => user-questions}/README.md |  16 +-
 .../README.zh.md                                   |  18 +-
 .../package.json                                   |   8 +-
 .../src/index.ts                                   |  46 +-
 .../src/invariant.ts                               |   8 +-
 .../src/types.ts                                   |   4 +-
 .../tests/user-questions.spec.ts}                  | 106 +--
 .../tsconfig.json                                  |   2 +-
 packages/{bash => jobs}/README.i18n.yaml           |   6 +-
 packages/jobs/README.md                            |  15 +
 packages/jobs/README.zh.md                         |  15 +
 .../jobs-local}/README.i18n.yaml                   |   6 +-
 packages/jobs/jobs-local/README.md                 |  34 +
 .../tasks-local => jobs/jobs-local}/README.zh.md   |  16 +-
 .../tasks-local => jobs/jobs-local}/package.json   |  17 +-
 .../tasks-local => jobs/jobs-local}/src/index.ts   | 335 +++++----
 packages/jobs/jobs-local/src/invariant.ts          |  33 +
 .../jobs-local/tests/jobs.spec.ts}                 | 679 +++++++++--------
 .../jobs-local/tests/loader-composition.spec.ts    |  66 ++
 .../tasks-local => jobs/jobs-local}/tsconfig.json  |   7 +-
 packages/{bash/bash => jobs/jobs}/README.i18n.yaml |   6 +-
 packages/jobs/jobs/README.md                       |  40 +
 packages/{tasks/tasks => jobs/jobs}/README.zh.md   |  18 +-
 packages/{tasks/tasks => jobs/jobs}/package.json   |   8 +-
 packages/{tasks/tasks => jobs/jobs}/src/brand.ts   |  16 +-
 packages/{tasks/tasks => jobs/jobs}/src/index.ts   | 119 +--
 .../{tasks/tasks => jobs/jobs}/src/invariant.ts    |  30 +-
 packages/{tasks/tasks => jobs/jobs}/src/types.ts   |  92 +--
 .../tasks => jobs/jobs}/tests/invariant.spec.ts    |  52 +-
 packages/jobs/jobs/tests/service.spec.ts           |  96 +++
 packages/{tasks/tasks => jobs/jobs}/tsconfig.json  |   2 +-
 .../bash-env => jobs/tool-jobs}/README.i18n.yaml   |   6 +-
 packages/jobs/tool-jobs/README.md                  |  96 +++
 .../tool-tasks => jobs/tool-jobs}/README.zh.md     |  24 +-
 .../tool-tasks => jobs/tool-jobs}/package.json     |  18 +-
 .../tool-tasks => jobs/tool-jobs}/src/index.ts     | 156 ++--
 .../tool-tasks => jobs/tool-jobs}/src/invariant.ts |   8 +-
 .../tool-jobs/tests/tool-jobs.spec.ts}             | 349 ++++-----
 .../tool-tasks => jobs/tool-jobs}/tsconfig.json    |   6 +-
 packages/llm/README.i18n.yaml                      |   2 +-
 packages/llm/README.zh.md                          |   4 +-
 packages/llm/llm-deepseek/README.i18n.yaml         |   4 +-
 packages/llm/llm-deepseek/README.md                |   6 +-
 packages/llm/llm-deepseek/README.zh.md             |   6 +-
 packages/llm/llm-deepseek/package.json             |  10 +-
 packages/llm/llm-deepseek/src/adapter.ts           |   4 +-
 packages/llm/llm-deepseek/src/index.ts             |  12 +-
 packages/llm/llm-deepseek/src/translate.ts         |   4 +-
 packages/llm/llm-deepseek/tests/adapter.e2e.ts     |  16 +-
 packages/llm/llm-deepseek/tests/adapter.spec.ts    |  62 +-
 .../llm/llm-deepseek/tests/dynamic-config.spec.ts  |  18 +-
 .../llm-deepseek/tests/loader-composition.spec.ts  |  20 +-
 packages/llm/llm-deepseek/tests/mock-server.ts     |   2 +-
 packages/llm/llm-deepseek/tests/serialize.spec.ts  |   2 +-
 packages/llm/llm-deepseek/tests/sse.spec.ts        |   2 +-
 packages/llm/llm-deepseek/tests/translate.spec.ts  |   2 +-
 packages/llm/llm-deepseek/tsconfig.json            |   6 +-
 packages/llm/llm-pi-ai/README.i18n.yaml            |   4 +-
 packages/llm/llm-pi-ai/README.md                   |   9 +-
 packages/llm/llm-pi-ai/README.zh.md                |  22 +-
 packages/llm/llm-pi-ai/package.json                |   6 +-
 packages/llm/llm-pi-ai/src/catalog.ts              |  46 +-
 packages/llm/llm-pi-ai/src/config.ts               |  49 +-
 packages/llm/llm-pi-ai/src/index.ts                |   7 +-
 packages/llm/llm-pi-ai/src/replay.ts               |   2 +-
 packages/llm/llm-pi-ai/tests/adapter.e2e.ts        |   6 +-
 packages/llm/llm-pi-ai/tests/adapter.spec.ts       |  42 +-
 packages/llm/llm-pi-ai/tests/assemble.ts           |   2 +-
 packages/llm/llm-pi-ai/tests/catalog.spec.ts       | 114 ++-
 packages/llm/llm-pi-ai/tests/config.spec.ts        |  56 +-
 packages/llm/llm-pi-ai/tests/convert.spec.ts       |   4 +-
 packages/llm/llm-pi-ai/tests/discovery.spec.ts     |  10 +-
 .../llm/llm-pi-ai/tests/dynamic-config.spec.ts     |  14 +-
 .../llm/llm-pi-ai/tests/loader-composition.spec.ts |  20 +-
 packages/llm/llm-pi-ai/tests/mock-server.ts        |   2 +-
 packages/llm/llm-pi-ai/tests/provider-apis.e2e.ts  |   4 +-
 packages/llm/llm-pi-ai/tests/sdk-options.spec.ts   |   2 +-
 packages/llm/llm-pi-ai/tsconfig.json               |   4 +-
 packages/llm/llm-retry/README.i18n.yaml            |   2 +-
 packages/llm/llm-retry/README.zh.md                |   4 +-
 packages/llm/llm-retry/package.json                |   2 +-
 packages/llm/llm-retry/src/history.ts              |   2 +-
 packages/llm/llm-retry/src/index.ts                |   2 +-
 packages/llm/llm-retry/tests/invariant.spec.ts     |  12 +-
 .../llm/llm-retry/tests/loader-composition.spec.ts |   8 +-
 packages/llm/llm-retry/tests/persistence.spec.ts   |  12 +-
 packages/llm/llm-retry/tests/retry.spec.ts         |  10 +-
 packages/llm/llm-retry/tsconfig.json               |   2 +-
 packages/llm/llm/README.i18n.yaml                  |   4 +-
 packages/llm/llm/README.md                         |   8 +-
 packages/llm/llm/README.zh.md                      |  20 +-
 packages/llm/llm/package.json                      |   2 +-
 packages/llm/llm/src/assembler.ts                  |   2 +-
 packages/llm/llm/src/call-config.ts                |   4 +-
 packages/llm/llm/src/error.ts                      |   2 +-
 packages/llm/llm/src/index.ts                      |  22 +-
 packages/llm/llm/src/invariant.ts                  |   6 +-
 packages/llm/llm/src/message.ts                    |  24 +-
 packages/llm/llm/src/never.ts                      |   2 +-
 packages/llm/llm/src/types.ts                      |   2 +-
 packages/llm/llm/tests/adapter-failure.spec.ts     |   2 +-
 packages/llm/llm/tests/assembler.spec.ts           |   4 +-
 packages/llm/llm/tests/call-config.spec.ts         |   2 +-
 packages/llm/llm/tests/invariant.spec.ts           |  14 +-
 packages/llm/llm/tests/properties.spec.ts          |   2 +-
 packages/llm/llm/tests/retry-policy.spec.ts        |   2 +-
 packages/llm/llm/tests/service.spec.ts             |  98 +--
 packages/llm/llm/tests/topology.spec.ts            |   6 +-
 packages/llm/llm/tsconfig.json                     |   2 +-
 packages/llm/token-meter/README.i18n.yaml          |   4 +-
 packages/llm/token-meter/README.md                 |   8 +-
 packages/llm/token-meter/README.zh.md              |  10 +-
 packages/llm/token-meter/package.json              |   6 +-
 packages/llm/token-meter/src/estimate.ts           |   2 +-
 packages/llm/token-meter/src/index.ts              |   8 +-
 packages/llm/token-meter/src/surface-fold.ts       |   2 +-
 packages/llm/token-meter/src/surface-projection.ts |   8 +-
 packages/llm/token-meter/src/usage-projection.ts   |   2 +-
 .../tests/context-breakdown-projection.spec.ts     |  16 +-
 packages/llm/token-meter/tests/token-meter.spec.ts |  22 +-
 .../tests/token-usage-projection.spec.ts           |  16 +-
 packages/llm/token-meter/tsconfig.json             |   4 +-
 packages/lsp/README.i18n.yaml                      |   4 +-
 packages/lsp/README.md                             |   2 +-
 packages/lsp/README.zh.md                          |   8 +-
 .../lsp/{lsp-local => lsp-stdio}/README.i18n.yaml  |   6 +-
 packages/lsp/{lsp-local => lsp-stdio}/README.md    |   2 +-
 packages/lsp/{lsp-local => lsp-stdio}/README.zh.md |   2 +-
 packages/lsp/{lsp-local => lsp-stdio}/package.json |   6 +-
 packages/lsp/{lsp-local => lsp-stdio}/src/abort.ts |   2 +-
 .../lsp/{lsp-local => lsp-stdio}/src/connection.ts |   4 +-
 .../lsp/{lsp-local => lsp-stdio}/src/framing.ts    |   4 +-
 packages/lsp/{lsp-local => lsp-stdio}/src/host.ts  |   0
 packages/lsp/{lsp-local => lsp-stdio}/src/index.ts |  26 +-
 .../lsp/{lsp-local => lsp-stdio}/src/instance.ts   |   2 +-
 .../lsp/{lsp-local => lsp-stdio}/src/invariant.ts  |   8 +-
 .../lsp/{lsp-local => lsp-stdio}/src/protocol.ts   |   2 +-
 .../lsp/{lsp-local => lsp-stdio}/src/translate.ts  |   4 +-
 .../tests/built-lib.e2e.ts                         |   8 +-
 .../tests/connection.spec.ts                       |   4 +-
 .../tests/fixture-server.ts                        |   6 +-
 .../{lsp-local => lsp-stdio}/tests/framing.spec.ts |   4 +-
 .../{lsp-local => lsp-stdio}/tests/host.spec.ts    |   2 +-
 .../tests/instance.spec.ts                         |  10 +-
 .../tests/lifecycle.spec.ts                        |  24 +-
 .../tests/provider.spec.ts                         |  38 +-
 .../tests/translate.spec.ts                        |   4 +-
 .../tests/typescript-server.e2e.ts                 |   8 +-
 .../lsp/{lsp-local => lsp-stdio}/tsconfig.json     |   2 +-
 packages/lsp/lsp/README.i18n.yaml                  |   4 +-
 packages/lsp/lsp/README.md                         |   2 +-
 packages/lsp/lsp/README.zh.md                      |   6 +-
 packages/lsp/lsp/package.json                      |   2 +-
 packages/lsp/lsp/src/index.ts                      |   4 +-
 packages/lsp/lsp/tests/lsp.spec.ts                 |   4 +-
 packages/lsp/lsp/tsconfig.json                     |   2 +-
 packages/lsp/tool-lsp/README.i18n.yaml             |   4 +-
 packages/lsp/tool-lsp/README.md                    |   2 +-
 packages/lsp/tool-lsp/README.zh.md                 |  10 +-
 packages/lsp/tool-lsp/package.json                 |   6 +-
 packages/lsp/tool-lsp/src/index.ts                 |   6 +-
 packages/lsp/tool-lsp/src/render.ts                |   2 +-
 packages/lsp/tool-lsp/tests/integration.spec.ts    |  14 +-
 packages/lsp/tool-lsp/tests/tool-lsp.spec.ts       |   8 +-
 packages/lsp/tool-lsp/tsconfig.json                |   2 +-
 packages/mcp/mcp-client/package.json               |   2 +-
 packages/mcp/mcp-client/src/connection.ts          |   2 +-
 packages/mcp/mcp-client/src/index.ts               |   2 +-
 packages/mcp/mcp-client/src/tools.ts               |  12 +-
 packages/mcp/mcp-client/tests/apply.spec.ts        |  10 +-
 packages/mcp/mcp-client/tests/mcp-client.e2e.ts    |   4 +-
 packages/mcp/mcp-client/tests/mcp-client.spec.ts   |  12 +-
 packages/mcp/mcp-client/tests/reconnect.spec.ts    |   4 +-
 packages/mcp/mcp-client/tsconfig.json              |   2 +-
 packages/plan/plan-mode/README.i18n.yaml           |   4 +-
 packages/plan/plan-mode/README.md                  |   4 +-
 packages/plan/plan-mode/README.zh.md               |  10 +-
 packages/plan/plan-mode/package.json               |   6 +-
 packages/plan/plan-mode/src/index.ts               |  20 +-
 packages/plan/plan-mode/tests/integration.spec.ts  |  16 +-
 packages/plan/plan-mode/tests/invariant.spec.ts    |  12 +-
 packages/plan/plan-mode/tests/plan-mode.spec.ts    | 102 +--
 packages/plan/plan-mode/tests/projection.spec.ts   |  14 +-
 packages/plan/plan-mode/tsconfig.json              |   4 +-
 packages/preset/README.i18n.yaml                   |   2 +-
 packages/preset/README.zh.md                       |   2 +-
 packages/preset/agent-presets/README.i18n.yaml     |   4 +-
 packages/preset/agent-presets/README.md            |  17 +-
 packages/preset/agent-presets/README.zh.md         |  21 +-
 packages/preset/agent-presets/package.json         |   8 +-
 packages/preset/agent-presets/src/authoring.ts     |   2 +-
 packages/preset/agent-presets/src/discovery.ts     |  17 +-
 packages/preset/agent-presets/src/index.ts         |  47 +-
 packages/preset/agent-presets/src/invariant.ts     |   2 +-
 packages/preset/agent-presets/src/metadata.ts      |   2 +-
 packages/preset/agent-presets/src/mount.ts         |   2 +-
 packages/preset/agent-presets/src/preset.ts        |   5 +
 .../preset/agent-presets/tests/authoring.spec.ts   |   7 +
 .../preset/agent-presets/tests/invariant.spec.ts   |  40 +-
 .../preset/agent-presets/tests/metadata.spec.ts    |   2 +-
 packages/preset/agent-presets/tests/mount.spec.ts  |  40 +-
 .../preset/agent-presets/tests/settings.spec.ts    |  14 +-
 .../preset/agent-presets/tests/user-root.spec.ts   | 131 ++++
 packages/preset/agent-presets/tsconfig.json        |   4 +-
 packages/preset/persona/README.i18n.yaml           |   2 +-
 packages/preset/persona/README.zh.md               |   4 +-
 packages/preset/persona/package.json               |   2 +-
 packages/preset/persona/src/index.ts               |   2 +-
 packages/preset/persona/tsconfig.json              |   2 +-
 packages/pty/README.md                             |  15 -
 packages/pty/README.zh.md                          |  15 -
 packages/pty/pty-local/README.i18n.yaml            |   6 -
 packages/pty/tool-bash-persistent/README.i18n.yaml |   6 -
 packages/pty/tool-pty/README.i18n.yaml             |   6 -
 packages/pty/tool-pty/README.md                    |  71 --
 packages/pty/tool-pty/README.zh.md                 |  71 --
 .../invariants/README.i18n.yaml                    |   6 +
 .../invariants/README.md                           |  14 +-
 .../invariants/README.zh.md                        |  28 +-
 .../invariants/package.json                        |   4 +-
 .../invariants/src/index.ts                        |   8 +-
 .../invariants/src/invariant.ts                    |   0
 .../invariants/tests/service.spec.ts               |  18 +-
 .../invariants/tsconfig.json                       |   0
 packages/sandbox/sandbox-local/README.i18n.yaml    |   4 +-
 packages/sandbox/sandbox-local/README.md           |   4 +-
 packages/sandbox/sandbox-local/README.zh.md        |  12 +-
 packages/sandbox/sandbox-local/package.json        |   2 +-
 packages/sandbox/sandbox-local/src/index.ts        |   2 +-
 .../sandbox/sandbox-local/tests/acl-grants.spec.ts |   2 +-
 packages/sandbox/sandbox-local/tests/bwrap.e2e.ts  |   4 +-
 .../sandbox/sandbox-local/tests/landlock.e2e.ts    |   4 +-
 packages/sandbox/sandbox-local/tests/local.spec.ts |  38 +-
 .../sandbox-local/tests/packed-install.e2e.ts      |   6 +-
 packages/sandbox/sandbox-local/tsconfig.json       |   2 +-
 packages/sandbox/sandbox-policy/package.json       |   2 +-
 packages/sandbox/sandbox-policy/src/invariant.ts   |   2 +-
 .../sandbox/sandbox-policy/tests/invariant.spec.ts |   8 +-
 .../sandbox/sandbox-policy/tests/policy.spec.ts    |   2 +-
 packages/sandbox/sandbox-policy/tsconfig.json      |   2 +-
 .../sandbox/sandbox-windows-acl/README.i18n.yaml   |   4 +-
 packages/sandbox/sandbox-windows-acl/README.md     |   2 +-
 packages/sandbox/sandbox-windows-acl/README.zh.md  |   8 +-
 packages/sandbox/sandbox-windows-acl/package.json  |   2 +-
 packages/sandbox/sandbox-windows-acl/src/index.ts  |   2 +-
 packages/sandbox/sandbox-windows-acl/src/runner.ts |  10 +-
 .../tests/failure-paths.spec.ts                    |   2 +-
 .../sandbox-windows-acl/tests/grant.spec.ts        |   2 +-
 .../tests/token-failure-paths.spec.ts              |   2 +-
 packages/sandbox/sandbox-windows-acl/tsconfig.json |   2 +-
 packages/sandbox/sandbox/README.i18n.yaml          |   4 +-
 packages/sandbox/sandbox/README.md                 |   6 +-
 packages/sandbox/sandbox/README.zh.md              |   6 +-
 packages/sandbox/sandbox/package.json              |   2 +-
 packages/sandbox/sandbox/src/index.ts              |   2 +-
 packages/sandbox/sandbox/tests/escalation.spec.ts  |   2 +-
 packages/sandbox/sandbox/tsconfig.json             |   2 +-
 packages/schedule/README.i18n.yaml                 |   4 +-
 packages/schedule/README.md                        |   2 +-
 packages/schedule/README.zh.md                     |   2 +-
 .../{tool-schedule => schedule}/README.i18n.yaml   |   6 +-
 .../schedule/{tool-schedule => schedule}/README.md |   4 +-
 .../{tool-schedule => schedule}/README.zh.md       |   4 +-
 .../{tool-schedule => schedule}/package.json       |   6 +-
 .../{tool-schedule => schedule}/src/domain.ts      |   2 +-
 .../{tool-schedule => schedule}/src/index.ts       |  32 +-
 .../{tool-schedule => schedule}/src/invariant.ts   |   4 +-
 .../{tool-schedule => schedule}/src/persistence.ts |   0
 .../{tool-schedule => schedule}/src/runtime.ts     |  34 +-
 .../{tool-schedule => schedule}/src/tools.ts       |  12 +-
 .../{tool-schedule => schedule}/src/transaction.ts |   2 +-
 .../{tool-schedule => schedule}/src/types.ts       |   2 +-
 .../tests/domain.spec.ts                           |   2 +-
 .../tests/invariant.spec.ts                        |   8 +-
 .../tests/jsonl-restart.spec.ts                    |   8 +-
 .../tests/plugin.spec.ts                           |   2 +-
 .../tests/recurrence.spec.ts                       |   0
 .../tests/runtime.spec.ts                          | 258 +++----
 .../tests/tools.spec.ts                            |   6 +-
 .../{tool-schedule => schedule}/tsconfig.json      |   2 +-
 .../{tool-schedule => schedule}/tsdown.config.ts   |   0
 packages/sdk/client/package.json                   |   2 +-
 packages/sdk/client/src/dispose.ts                 |   2 +-
 packages/sdk/client/tests/fake-runtime.ts          |   2 +-
 packages/sdk/client/tsconfig.json                  |   2 +-
 packages/sdk/protocol/README.i18n.yaml             |   4 +-
 packages/sdk/protocol/README.md                    |   8 +-
 packages/sdk/protocol/README.zh.md                 |   8 +-
 packages/sdk/protocol/package.json                 |   2 +-
 packages/sdk/protocol/src/index.ts                 |   2 +-
 packages/sdk/protocol/src/transport.ts             |   2 +-
 packages/sdk/protocol/src/types.ts                 |   4 +-
 packages/sdk/protocol/tests/transport.spec.ts      |   2 +-
 packages/sdk/protocol/tsconfig.json                |   2 +-
 packages/sdk/server/README.i18n.yaml               |   4 +-
 packages/sdk/server/README.md                      |   4 +-
 packages/sdk/server/README.zh.md                   |  10 +-
 packages/sdk/server/package.json                   |   4 +-
 packages/sdk/server/src/index.ts                   |  12 +-
 packages/sdk/server/src/invariant.ts               |   8 +-
 packages/sdk/server/src/server.ts                  |  18 +-
 .../sdk/server/tests/built-scope-carrier.e2e.ts    |  16 +-
 packages/sdk/server/tests/plugin-apply.spec.ts     |   8 +-
 packages/sdk/server/tests/plugin-shape.spec.ts     |   4 +-
 packages/sdk/server/tests/server.spec.ts           |  54 +-
 packages/sdk/server/tsconfig.json                  |   2 +-
 .../self-modification/tool-cordis/README.i18n.yaml |   6 -
 packages/session-query/README.i18n.yaml            |   4 +-
 packages/session-query/README.md                   |   1 +
 packages/session-query/README.zh.md                |   1 +
 .../session-log-download}/README.i18n.yaml         |   6 +-
 .../session-query/session-log-download/README.md   |  49 ++
 .../session-log-download/README.zh.md              |  49 ++
 .../session-log-download/package.json              |  63 ++
 .../session-log-download/src/client/Dialog.tsx     |  49 ++
 .../src/client/HeaderAction.module.css             |  36 +
 .../src/client/HeaderAction.tsx                    |  31 +
 .../session-log-download/src/client/controller.ts  | 137 ++++
 .../session-log-download/src/client/index.ts       |  52 ++
 .../session-log-download/src/client/locales.ts     |  27 +
 .../session-log-download/src/css-modules.d.ts      |   6 +
 .../session-log-download/src/index.ts              |  26 +
 .../session-log-download/src/invariant.ts          |  22 +
 .../tests/client-apply.client.spec.tsx             |  86 +++
 .../tests/command.client.spec.ts                   |  33 +
 .../tests/controller.client.spec.ts                | 146 ++++
 .../tests/dialog.client.spec.tsx                   |  76 ++
 .../tests/header-action.client.spec.tsx            |  72 ++
 .../tests/invariant.client.spec.ts                 |  16 +
 .../tests/loader-composition.client.spec.ts        |  68 ++
 .../session-log-download/tsconfig.json             |  21 +
 .../session-log-download/tsdown.config.ts          |   3 +
 .../session-query-sqlite/README.i18n.yaml          |   4 +-
 .../session-query/session-query-sqlite/README.md   |   2 +-
 .../session-query-sqlite/README.zh.md              |  12 +-
 .../session-query-sqlite/package.json              |   2 +-
 .../session-query-sqlite/src/index.ts              |  10 +-
 .../session-query-sqlite/src/query.ts              |   2 +-
 .../session-query-sqlite/src/schema.ts             |   2 +-
 .../session-query-sqlite/tests/load-path.e2e.ts    |  10 +-
 .../session-query-sqlite/tests/sqlite.spec.ts      |  96 +--
 .../session-query-sqlite/tsconfig.json             |   2 +-
 .../session-query/session-query/README.i18n.yaml   |   4 +-
 packages/session-query/session-query/README.md     |   4 +-
 packages/session-query/session-query/README.zh.md  |   6 +-
 packages/session-query/session-query/package.json  |   2 +-
 .../session-query/session-query/src/documents.ts   |   4 +-
 packages/session-query/session-query/src/index.ts  |   8 +-
 .../session-query/session-query/src/tracing.ts     |   2 +-
 .../session-query/tests/search-helpers.spec.ts     |   8 +-
 .../session-query/tests/session-query.spec.ts      |  20 +-
 .../session-query/tests/test-service.ts            |   4 +-
 .../session-query/tests/tracing.spec.ts            |   4 +-
 packages/session-query/session-query/tsconfig.json |   2 +-
 .../session-query/tool-session-query/package.json  |   4 +-
 .../session-query/tool-session-query/src/index.ts  |   4 +-
 .../session-query/tool-session-query/src/input.ts  |   2 +-
 .../tool-session-query/src/operations.ts           |   2 +-
 .../tool-session-query/src/presentation.ts         |   6 +-
 .../tool-session-query/src/service-boundary.ts     |   6 +-
 .../tool-session-query/src/workspace-access.ts     |   2 +-
 .../tests/sqlite-integration.spec.ts               |  20 +-
 .../tests/tool-session-query.spec.ts               |  18 +-
 .../session-query/tool-session-query/tsconfig.json |   2 +-
 packages/session/README.i18n.yaml                  |   4 +-
 packages/session/README.md                         |   9 +-
 packages/session/README.zh.md                      |  15 +-
 .../session/session-checkpoint-policy/package.json |   2 +-
 .../session/session-checkpoint-policy/src/index.ts |   2 +-
 .../tests/crash-recovery.e2e.ts                    |   4 +-
 .../tests/fixtures/crash-child.ts                  |   6 +-
 .../tests/session-checkpoint-policy.spec.ts        |  12 +-
 .../session-checkpoint-policy/tsconfig.json        |   2 +-
 .../session-persistence-jsonl/README.i18n.yaml     |   2 +-
 .../session/session-persistence-jsonl/README.zh.md |  20 +-
 .../session/session-persistence-jsonl/package.json |   2 +-
 .../session/session-persistence-jsonl/src/index.ts |   6 +-
 .../src/zstd-private-decoder.ts                    |   2 +-
 .../session/session-persistence-jsonl/src/zstd.ts  |   2 +-
 .../session-persistence-jsonl/tests/jsonl.spec.ts  |  62 +-
 .../session-persistence-jsonl/tests/zstd.spec.ts   |  20 +-
 .../session-persistence-jsonl/tsconfig.json        |   2 +-
 .../session-persistence-sqlite/README.i18n.yaml    |   2 +-
 .../session-persistence-sqlite/README.zh.md        |  12 +-
 .../session-persistence-sqlite/package.json        |   2 +-
 .../session-persistence-sqlite/src/index.ts        |   4 +-
 .../session-persistence-sqlite/src/schema.ts       |   2 +-
 .../tests/sqlite.spec.ts                           |  46 +-
 .../session-persistence-sqlite/tsconfig.json       |   2 +-
 .../session/session-persistence/README.i18n.yaml   |   4 +-
 packages/session/session-persistence/README.md     |   2 +-
 packages/session/session-persistence/README.zh.md  |  28 +-
 packages/session/session-persistence/package.json  |   2 +-
 .../session/session-persistence/src/coordinator.ts |   2 +-
 .../session-persistence/src/preparations.ts        |   2 +-
 .../session/session-persistence/tests/contract.ts  |   2 +-
 .../tests/coordinator-contract.ts                  |   2 +-
 .../session-persistence/tests/persistence.spec.ts  |   2 +-
 packages/session/session-persistence/tsconfig.json |   2 +-
 .../session-projection-cache/README.i18n.yaml      |   2 +-
 .../session/session-projection-cache/README.zh.md  |  10 +-
 .../session/session-projection-cache/package.json  |   2 +-
 .../session/session-projection-cache/tsconfig.json |   2 +-
 .../session/session-projection/README.i18n.yaml    |   2 +-
 packages/session/session-projection/README.zh.md   |   4 +-
 packages/session/session-projection/package.json   |   2 +-
 packages/session/session-projection/src/index.ts   |   2 +-
 .../session-projection/tests/registry.spec.ts      |   2 +-
 packages/session/session-projection/tsconfig.json  |   2 +-
 .../{user-id => session-stats}/README.i18n.yaml    |   6 +-
 packages/session/session-stats/README.md           |  39 +
 packages/session/session-stats/README.zh.md        |  39 +
 packages/session/session-stats/package.json        |  62 ++
 packages/session/session-stats/src/client.ts       |  10 +
 packages/session/session-stats/src/index.ts        |  29 +
 packages/session/session-stats/src/invariant.ts    |  35 +
 packages/session/session-stats/src/projection.ts   | 183 +++++
 packages/session/session-stats/src/types.ts        |  46 ++
 .../session-stats/tests/loader-composition.spec.ts |  86 +++
 .../session/session-stats/tests/projection.spec.ts | 292 ++++++++
 .../session-stats}/tsconfig.json                   |   4 +-
 .../session-telemetry-otel/README.i18n.yaml        |   4 +-
 packages/session/session-telemetry-otel/README.md  |  20 +-
 .../session/session-telemetry-otel/README.zh.md    |  20 +-
 .../session/session-telemetry-otel/package.json    |   6 +-
 .../session/session-telemetry-otel/src/index.ts    |  68 +-
 .../tests/loader-composition.e2e.ts                |   4 +-
 .../session-telemetry-otel/tests/otel.spec.ts      | 125 ++--
 .../session/session-telemetry-otel/tsconfig.json   |   4 +-
 .../session/session-telemetry/README.i18n.yaml     |   4 +-
 packages/session/session-telemetry/README.md       |  12 +-
 packages/session/session-telemetry/README.zh.md    |  12 +-
 packages/session/session-telemetry/package.json    |   4 +-
 .../session/session-telemetry/src/coordinator.ts   |  24 +-
 packages/session/session-telemetry/src/index.ts    |  48 +-
 .../session/session-telemetry/tests/redact.spec.ts |  32 +-
 .../session-telemetry/tests/telemetry.spec.ts      |  56 +-
 packages/session/session-telemetry/tsconfig.json   |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |   4 +-
 .../README.zh.md                                   |   6 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |   8 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/provider.spec.ts                         |   6 +-
 .../tsconfig.json                                  |   2 +-
 .../README.i18n.yaml                               |   6 +
 .../README.md                                      |   4 +-
 .../README.zh.md                                   |   6 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |   8 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/loader-composition.spec.ts               |  14 +-
 .../tests/provider.e2e.ts                          |  12 +-
 .../tests/provider.spec.ts                         |  10 +-
 .../tsconfig.json                                  |   2 +-
 .../session/session-title-llm/README.i18n.yaml     |   2 +-
 packages/session/session-title-llm/README.zh.md    |   2 +-
 packages/session/session-title-llm/package.json    |   2 +-
 .../session/session-title-llm/tests/llm.spec.ts    |  12 +-
 packages/session/session-title-llm/tsconfig.json   |   2 +-
 packages/session/session-title/README.i18n.yaml    |   4 +-
 packages/session/session-title/README.md           |   4 +-
 packages/session/session-title/README.zh.md        |   6 +-
 packages/session/session-title/package.json        |   2 +-
 packages/session/session-title/src/index.ts        |   6 +-
 packages/session/session-title/src/invariant.ts    |   2 +-
 packages/session/session-title/src/normalize.ts    |   4 +-
 .../session/session-title/tests/invariant.spec.ts  |   4 +-
 .../session-title/tests/persistence.spec.ts        |  12 +-
 .../session/session-title/tests/projection.spec.ts |   2 +-
 .../session/session-title/tests/provider.spec.ts   |  30 +-
 .../session/session-title/tests/rename.spec.ts     |   4 +-
 .../session-title/tests/service-contracts.spec.ts  |  24 +-
 packages/session/session-title/tsconfig.json       |   2 +-
 packages/settings/README.i18n.yaml                 |   4 +-
 packages/settings/README.md                        |   2 +-
 packages/settings/README.zh.md                     |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../{settings-local => settings-file}/README.md    |   2 +-
 .../{settings-local => settings-file}/README.zh.md |   2 +-
 .../{settings-local => settings-file}/package.json |  10 +-
 .../{settings-local => settings-file}/src/index.ts |  28 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/concurrency.spec.ts                      |   8 +-
 .../tests/loader-composition.spec.ts               |  10 +-
 .../tests/local.spec.ts                            |   8 +-
 .../tests/lock-race.spec.ts                        |  10 +-
 .../tests/watcher.spec.ts                          |  10 +-
 .../tsconfig.json                                  |   4 +-
 packages/settings/settings/README.i18n.yaml        |   2 +-
 packages/settings/settings/README.zh.md            |  24 +-
 packages/settings/settings/package.json            |   2 +-
 packages/settings/settings/src/index.ts            |   8 +-
 packages/settings/settings/src/invariant.ts        |   4 +-
 packages/settings/settings/src/redact.ts           |   2 +-
 packages/settings/settings/tests/invariant.spec.ts |   4 +-
 packages/settings/settings/tests/memory.ts         |   6 +-
 packages/settings/settings/tests/settings.spec.ts  |   8 +-
 packages/settings/settings/tsconfig.json           |   2 +-
 packages/{tasks => shell}/README.i18n.yaml         |   6 +-
 packages/{bash => shell}/README.md                 |  16 +-
 packages/{bash => shell}/README.zh.md              |  14 +-
 packages/shell/bash-local/README.i18n.yaml         |   6 +
 packages/{bash => shell}/bash-local/README.md      |   8 +-
 packages/{bash => shell}/bash-local/README.zh.md   |  12 +-
 packages/{bash => shell}/bash-local/package.json   |   8 +-
 packages/{bash => shell}/bash-local/src/index.ts   |  28 +-
 .../{bash => shell}/bash-local/src/invariant.ts    |   0
 .../bash-local/tests/executor.spec.ts              |  26 +-
 .../bash-local/tests/settings.spec.ts              |  30 +-
 packages/{bash => shell}/bash-local/tsconfig.json  |   4 +-
 packages/shell/bash-sandbox/README.i18n.yaml       |   6 +
 packages/{bash => shell}/bash-sandbox/README.md    |  10 +-
 packages/{bash => shell}/bash-sandbox/README.zh.md |  14 +-
 packages/{bash => shell}/bash-sandbox/package.json |   8 +-
 .../{bash => shell}/bash-sandbox/src/helpers.ts    |   6 +-
 packages/{bash => shell}/bash-sandbox/src/index.ts |  22 +-
 .../{bash => shell}/bash-sandbox/src/invariant.ts  |   0
 .../bash-sandbox/tests/bwrap.e2e.ts                |   8 +-
 .../bash-sandbox/tests/landlock.e2e.ts             |   8 +-
 .../bash-sandbox/tests/partial-landlock.spec.ts    |  12 +-
 .../bash-sandbox/tests/sandbox.spec.ts             |  28 +-
 .../bash-sandbox/tests/seatbelt.e2e.ts             |  10 +-
 .../{bash => shell}/bash-sandbox/tsconfig.json     |   6 +-
 packages/shell/pwsh-local/README.i18n.yaml         |   6 +
 packages/{bash => shell}/pwsh-local/README.md      |  10 +-
 packages/{bash => shell}/pwsh-local/README.zh.md   |  24 +-
 packages/{bash => shell}/pwsh-local/package.json   |   8 +-
 packages/{bash => shell}/pwsh-local/src/index.ts   |  28 +-
 .../{bash => shell}/pwsh-local/src/invariant.ts    |   0
 packages/{bash => shell}/pwsh-local/src/resolve.ts |   0
 .../pwsh-local/tests/executor.spec.ts              |  36 +-
 .../pwsh-local/tests/settings.spec.ts              |  26 +-
 packages/{bash => shell}/pwsh-local/tsconfig.json  |   4 +-
 packages/shell/pwsh-sandbox/README.i18n.yaml       |   6 +
 packages/{bash => shell}/pwsh-sandbox/README.md    |   2 +-
 packages/{bash => shell}/pwsh-sandbox/README.zh.md |   2 +-
 packages/{bash => shell}/pwsh-sandbox/package.json |   8 +-
 .../{bash => shell}/pwsh-sandbox/src/helpers.ts    |   4 +-
 packages/{bash => shell}/pwsh-sandbox/src/index.ts |  20 +-
 .../{bash => shell}/pwsh-sandbox/src/invariant.ts  |   0
 .../{bash => shell}/pwsh-sandbox/tests/acl.e2e.ts  |   6 +-
 .../pwsh-sandbox/tests/sandbox.spec.ts             |  18 +-
 .../{bash => shell}/pwsh-sandbox/tsconfig.json     |   6 +-
 packages/shell/shell-env/README.i18n.yaml          |   6 +
 packages/shell/shell-env/README.md                 |  51 ++
 packages/shell/shell-env/README.zh.md              |  51 ++
 .../bash-env => shell/shell-env}/package.json      |  14 +-
 .../bash-env => shell/shell-env}/src/index.ts      |  32 +-
 .../bash-env => shell/shell-env}/src/invariant.ts  |   8 +-
 .../shell-env/tests/shell-env.spec.ts}             |  42 +-
 .../bash-env => shell/shell-env}/tsconfig.json     |   6 +-
 packages/shell/shell/README.i18n.yaml              |   6 +
 packages/{bash/bash => shell/shell}/README.md      |  28 +-
 packages/shell/shell/README.zh.md                  |  53 ++
 packages/{bash/bash => shell/shell}/package.json   |   8 +-
 packages/{bash/bash => shell/shell}/src/index.ts   |  48 +-
 .../{bash/bash => shell/shell}/src/invariant.ts    |   6 +-
 packages/{bash/bash => shell/shell}/src/render.ts  |   4 +-
 packages/{bash/bash => shell/shell}/src/types.ts   |  44 +-
 .../bash => shell/shell}/tests/render.spec.ts      |   0
 .../bash => shell/shell}/tests/service.spec.ts     |  34 +-
 packages/{bash/bash => shell/shell}/tsconfig.json  |   2 +-
 .../shell/tool-bash-persistent/README.i18n.yaml    |   6 +
 .../{pty => shell}/tool-bash-persistent/README.md  |   2 +-
 .../tool-bash-persistent/README.zh.md              |   2 +-
 .../tool-bash-persistent/package.json              |  10 +-
 .../tool-bash-persistent/src/index.ts              |  38 +-
 .../tool-bash-persistent/src/invariant.ts          |   0
 .../tests/loader-composition.spec.ts               |  20 +-
 .../tool-bash-persistent/tests/tools.spec.ts       |  58 +-
 .../tool-bash-persistent/tsconfig.json             |   4 +-
 packages/shell/tool-bash/README.i18n.yaml          |   6 +
 packages/{bash => shell}/tool-bash/README.md       |  30 +-
 packages/{bash => shell}/tool-bash/README.zh.md    |  40 +-
 packages/{bash => shell}/tool-bash/package.json    |  22 +-
 .../{bash => shell}/tool-bash/src/background.ts    |   8 +-
 packages/{bash => shell}/tool-bash/src/index.ts    |  54 +-
 .../{bash => shell}/tool-bash/src/invariant.ts     |   0
 packages/{bash => shell}/tool-bash/src/render.ts   |  18 +-
 .../tool-bash/tests/integration.spec.ts            |  34 +-
 .../{bash => shell}/tool-bash/tests/tools.spec.ts  | 178 ++---
 packages/{bash => shell}/tool-bash/tsconfig.json   |   8 +-
 packages/shell/tool-pwsh/README.i18n.yaml          |   6 +
 packages/{bash => shell}/tool-pwsh/README.md       |  26 +-
 packages/{bash => shell}/tool-pwsh/README.zh.md    |  76 +-
 packages/{bash => shell}/tool-pwsh/package.json    |  20 +-
 .../{bash => shell}/tool-pwsh/src/background.ts    |   8 +-
 packages/{bash => shell}/tool-pwsh/src/index.ts    |  56 +-
 .../{bash => shell}/tool-pwsh/src/invariant.ts     |   0
 packages/{bash => shell}/tool-pwsh/src/render.ts   |  10 +-
 .../tool-pwsh/tests/integration.spec.ts            |  26 +-
 .../{bash => shell}/tool-pwsh/tests/loader.spec.ts |   4 +-
 .../{bash => shell}/tool-pwsh/tests/tools.spec.ts  | 138 ++--
 packages/{bash => shell}/tool-pwsh/tsconfig.json   |  10 +-
 packages/skill/README.i18n.yaml                    |   4 +-
 packages/skill/README.md                           |   2 +-
 packages/skill/README.zh.md                        |   2 +-
 packages/skill/skill-badge/package.json            |   2 +-
 .../skill/skill-badge/tests/skill-badge.spec.ts    |   4 +-
 packages/skill/skill-badge/tsconfig.json           |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../{skill-local => skill-filesystem}/README.md    |   6 +-
 .../{skill-local => skill-filesystem}/README.zh.md |   8 +-
 .../{skill-local => skill-filesystem}/package.json |  10 +-
 .../{skill-local => skill-filesystem}/src/index.ts |  30 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/skill-filesystem-watcher.spec.ts}        |  58 +-
 .../tests/skill-filesystem.spec.ts}                |  88 +--
 .../tsconfig.json                                  |   4 +-
 packages/skill/skill/README.i18n.yaml              |   4 +-
 packages/skill/skill/README.md                     |   4 +-
 packages/skill/skill/README.zh.md                  |  10 +-
 packages/skill/skill/package.json                  |   2 +-
 packages/skill/skill/src/index.ts                  |  10 +-
 packages/skill/skill/tests/skill.spec.ts           |  86 +--
 packages/skill/skill/tsconfig.json                 |   2 +-
 packages/skill/tool-skill/README.i18n.yaml         |   2 +-
 packages/skill/tool-skill/README.zh.md             |  12 +-
 packages/skill/tool-skill/package.json             |   4 +-
 packages/skill/tool-skill/src/index.ts             |   6 +-
 packages/skill/tool-skill/tests/tool-skill.spec.ts |  28 +-
 packages/skill/tool-skill/tsconfig.json            |   2 +-
 packages/spill/spill-local/package.json            |   2 +-
 packages/spill/spill-local/src/index.ts            |   2 +-
 packages/spill/spill-local/src/store.ts            |   6 +-
 packages/spill/spill-local/tsconfig.json           |   2 +-
 packages/spill/spill-policy/README.i18n.yaml       |   4 +-
 packages/spill/spill-policy/README.md              |   4 +-
 packages/spill/spill-policy/README.zh.md           |   4 +-
 packages/spill/spill-policy/package.json           |   8 +-
 packages/spill/spill-policy/src/index.ts           |   8 +-
 .../spill/spill-policy/tests/spill-policy.spec.ts  |  30 +-
 packages/spill/spill-policy/tsconfig.json          |   4 +-
 packages/spill/spill/README.i18n.yaml              |   4 +-
 packages/spill/spill/README.md                     |   4 +-
 packages/spill/spill/README.zh.md                  |  10 +-
 packages/spill/spill/package.json                  |   2 +-
 packages/spill/spill/src/index.ts                  |   2 +-
 packages/spill/spill/tsconfig.json                 |   2 +-
 packages/storage/storage-domain/package.json       |   2 +-
 packages/storage/storage-domain/src/domain.ts      |   2 +-
 packages/storage/storage-domain/src/error.ts       |   2 +-
 packages/storage/storage-domain/src/index.ts       |   2 +-
 packages/storage/storage-domain/src/invariant.ts   |   4 +-
 packages/storage/storage-domain/src/spec.ts        |   4 +-
 .../storage-domain/tests/helpers/memory-backend.ts |   4 +-
 .../storage/storage-domain/tests/invariant.spec.ts |   4 +-
 packages/storage/storage-domain/tsconfig.json      |   2 +-
 packages/storage/storage-json/package.json         |   2 +-
 packages/storage/storage-json/src/unit.ts          |   2 +-
 .../storage-json/tests/json-backend.spec.ts        |   4 +-
 packages/storage/storage-json/tsconfig.json        |   2 +-
 packages/storage/storage-sqlite/README.i18n.yaml   |   2 +-
 packages/storage/storage-sqlite/README.zh.md       |   6 +-
 packages/storage/storage-sqlite/package.json       |   2 +-
 packages/storage/storage-sqlite/src/unit.ts        |   8 +-
 .../storage/storage-sqlite/tests/invariant.spec.ts |   4 +-
 .../storage-sqlite/tests/sqlite-backend.spec.ts    |   2 +-
 packages/storage/storage-sqlite/tsconfig.json      |   2 +-
 packages/storage/storage/package.json              |   2 +-
 packages/storage/storage/src/index.ts              |   8 +-
 packages/storage/storage/tests/registry.spec.ts    |   2 +-
 packages/storage/storage/tsconfig.json             |   2 +-
 packages/subagent/README.i18n.yaml                 |   4 +-
 packages/subagent/README.md                        |   6 +-
 packages/subagent/README.zh.md                     |   8 +-
 packages/subagent/subagent-acp/README.i18n.yaml    |   2 +-
 packages/subagent/subagent-acp/README.zh.md        |   6 +-
 packages/subagent/subagent-acp/package.json        |   2 +-
 packages/subagent/subagent-acp/src/index.ts        |   2 +-
 packages/subagent/subagent-acp/src/run.ts          |   4 +-
 .../subagent-acp/tests/loader-composition.e2e.ts   |   2 +-
 .../subagent/subagent-acp/tests/mock-acp-server.ts |   2 +-
 .../subagent-acp/tests/subagent-acp.e2e.ts         |  14 +-
 .../subagent-acp/tests/subagent-acp.spec.ts        |  54 +-
 packages/subagent/subagent-acp/tsconfig.json       |   4 +-
 .../subagent/subagent-claude-code/README.i18n.yaml |   2 +-
 .../subagent/subagent-claude-code/README.zh.md     |  10 +-
 .../subagent/subagent-claude-code/package.json     |   2 +-
 .../subagent/subagent-claude-code/src/process.ts   |   2 +-
 .../subagent-claude-code/tests/messages-fixture.ts |   2 +-
 .../tests/real-deepseek.e2e.ts                     |   8 +-
 .../tests/real-product.spec.ts                     |   8 +-
 .../tests/subagent-claude-code.spec.ts             |  12 +-
 .../subagent/subagent-claude-code/tsconfig.json    |   2 +-
 packages/subagent/subagent-codex/README.i18n.yaml  |   2 +-
 packages/subagent/subagent-codex/README.zh.md      |  12 +-
 packages/subagent/subagent-codex/package.json      |   2 +-
 .../subagent-codex/tests/real-deepseek.e2e.ts      |   8 +-
 .../subagent-codex/tests/real-product.spec.ts      |  10 +-
 .../subagent-codex/tests/responses-fixture.ts      |   2 +-
 .../subagent-codex/tests/subagent-codex.spec.ts    |  16 +-
 packages/subagent/subagent-codex/tsconfig.json     |   2 +-
 packages/subagent/subagent-dsh-sdk/package.json    |   2 +-
 packages/subagent/subagent-dsh-sdk/src/index.ts    |   6 +-
 .../tests/loader-composition.e2e.ts                |   2 +-
 .../tests/subagent-dsh-sdk.spec.ts                 |  16 +-
 packages/subagent/subagent-dsh-sdk/tsconfig.json   |   4 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |   6 +-
 .../README.zh.md                                   |   6 +-
 .../package.json                                   |  12 +-
 .../src/index.ts                                   |  12 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/multi-subagent.spec.ts                   |  10 +-
 .../tests/subagent-fork-in-process.spec.ts}        |  18 +-
 .../tsconfig.json                                  |   4 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |   2 +-
 .../README.zh.md                                   |   2 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |   4 +-
 .../src/invariant.ts                               |   8 +-
 .../src/structured.ts                              |   8 +-
 .../tests/fixtures/plugins/preset-tool.js          |   0
 .../tests/fixtures/presets/coding/agent.cordis.yml |   0
 .../fixtures/presets/reviewing/agent.cordis.yml    |   0
 .../tests/inheritance.spec.ts                      |   4 +-
 .../tests/preset-inheritance.spec.ts               |   2 +-
 .../tests/structured.spec.ts                       |   8 +-
 .../tests/subagent-in-process-driver.spec.ts}      |  12 +-
 .../tsconfig.json                                  |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |   4 +-
 .../README.zh.md                                   |   4 +-
 .../package.json                                   |  10 +-
 .../src/index.ts                                   |  10 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/harness.ts                               |  10 +-
 .../tests/spawn-in-process.e2e.ts}                 |   0
 .../tests/subagent-spawn-in-process.spec.ts}       |  28 +-
 .../tsconfig.json                                  |   4 +-
 packages/subagent/subagent/README.i18n.yaml        |   4 +-
 packages/subagent/subagent/README.md               |   6 +-
 packages/subagent/subagent/README.zh.md            |  32 +-
 packages/subagent/subagent/package.json            |   8 +-
 .../subagent/src/activation-setup-registry.ts      |   2 +-
 packages/subagent/subagent/src/child-agent.ts      |   4 +-
 packages/subagent/subagent/src/continuation.ts     |   4 +-
 packages/subagent/subagent/src/descriptor.ts       |   4 +-
 packages/subagent/subagent/src/index.ts            |  16 +-
 packages/subagent/subagent/src/invariant.ts        |   2 +-
 packages/subagent/subagent/src/list-children.ts    |   4 +-
 packages/subagent/subagent/src/out-of-process.ts   |   4 +-
 packages/subagent/subagent/src/projection.ts       |   2 +-
 packages/subagent/subagent/src/run-settlement.ts   |  14 +-
 packages/subagent/subagent/src/types.ts            |   2 +-
 .../tests/activation-setup-registry.spec.ts        |   2 +-
 .../tests/continuation-inheritance.spec.ts         |   8 +-
 .../subagent/subagent/tests/continuation.spec.ts   |  24 +-
 packages/subagent/subagent/tests/invariant.spec.ts |   8 +-
 .../subagent/subagent/tests/list-children.spec.ts  |  18 +-
 .../subagent/subagent/tests/out-of-process.spec.ts |   4 +-
 packages/subagent/subagent/tests/service.spec.ts   |  12 +-
 .../subagent/tests/timing-projection.spec.ts       |   4 +-
 packages/subagent/subagent/tsconfig.json           |   4 +-
 .../tool-subagent-control/README.i18n.yaml         |   2 +-
 .../subagent/tool-subagent-control/README.zh.md    |  10 +-
 .../subagent/tool-subagent-control/package.json    |   4 +-
 .../subagent/tool-subagent-control/src/index.ts    |   2 +-
 .../tool-subagent-control/src/list-agents.ts       |   2 +-
 .../tests/list-agents.spec.ts                      |   8 +-
 .../tool-subagent-control/tests/park-parent.ts     |   2 +-
 .../tests/tool-subagent-control.spec.ts            |  12 +-
 .../subagent/tool-subagent-control/tsconfig.json   |   2 +-
 .../subagent/tool-subagent-report/README.i18n.yaml |   2 +-
 .../subagent/tool-subagent-report/README.zh.md     |   4 +-
 .../subagent/tool-subagent-report/package.json     |   4 +-
 .../subagent/tool-subagent-report/src/index.ts     |   2 +-
 .../tests/tool-subagent-report.spec.ts             |  12 +-
 .../subagent/tool-subagent-report/tsconfig.json    |   2 +-
 packages/subagent/tool-subagent/README.i18n.yaml   |   4 +-
 packages/subagent/tool-subagent/README.md          |   8 +-
 packages/subagent/tool-subagent/README.zh.md       |  10 +-
 packages/subagent/tool-subagent/package.json       |  12 +-
 packages/subagent/tool-subagent/src/index.ts       |  24 +-
 .../tool-subagent/tests/scripted-provider.spec.ts  |   6 +-
 .../tool-subagent/tests/scripted-provider.ts       |   2 +-
 .../tool-subagent/tests/tool-subagent.spec.ts      | 170 ++---
 packages/subagent/tool-subagent/tsconfig.json      |   4 +-
 packages/subprocess/README.i18n.yaml               |   4 +-
 packages/subprocess/README.md                      |   2 +-
 packages/subprocess/README.zh.md                   |   6 +-
 .../subprocess/subprocess-local/README.i18n.yaml   |   4 +-
 packages/subprocess/subprocess-local/README.md     |   6 +-
 packages/subprocess/subprocess-local/README.zh.md  |   8 +-
 packages/subprocess/subprocess-local/package.json  |   3 +-
 packages/subprocess/subprocess-local/src/index.ts  |  95 ++-
 .../subprocess-local/src/process-inspector.ts      |   2 +-
 packages/subprocess/subprocess-local/src/spawn.ts  |  21 +-
 .../subprocess/subprocess-local/src/terminal.ts    |  37 +
 .../tests/fixtures/managed-tree.ts                 |  16 +
 .../tests/fixtures/process-exit-host.ts            |  79 ++
 .../subprocess-local/tests/local.spec.ts           | 158 +++-
 .../subprocess-local/tests/process-exit.spec.ts    | 173 +++++
 .../tests/process-inspector.spec.ts                |   2 +-
 .../subprocess-local/tests/spawn.spec.ts           |  46 +-
 .../subprocess-local/tests/terminal.spec.ts        |  80 ++
 packages/subprocess/subprocess-local/tsconfig.json |   2 +-
 packages/subprocess/subprocess/README.i18n.yaml    |   4 +-
 packages/subprocess/subprocess/README.md           |   4 +-
 packages/subprocess/subprocess/README.zh.md        |   6 +-
 packages/subprocess/subprocess/package.json        |   2 +-
 packages/subprocess/subprocess/src/index.ts        |   6 +-
 packages/subprocess/subprocess/src/types.ts        |   4 +-
 .../subprocess/subprocess/tests/service.spec.ts    |  14 +-
 packages/subprocess/subprocess/tsconfig.json       |   2 +-
 packages/support/README.i18n.yaml                  |   6 -
 packages/support/invariants/README.i18n.yaml       |   6 -
 packages/support/llm-replay/README.i18n.yaml       |   6 -
 packages/tasks/README.md                           |  15 -
 packages/tasks/README.zh.md                        |  15 -
 packages/tasks/tasks-local/README.i18n.yaml        |   6 -
 packages/tasks/tasks-local/README.md               |  28 -
 packages/tasks/tasks-local/src/invariant.ts        |  30 -
 packages/tasks/tasks/README.i18n.yaml              |   6 -
 packages/tasks/tasks/README.md                     |  40 -
 packages/tasks/tasks/tests/service.spec.ts         |  96 ---
 packages/tasks/tool-tasks/README.i18n.yaml         |   6 -
 packages/tasks/tool-tasks/README.md                |  96 ---
 packages/{pty/pty => terminal}/README.i18n.yaml    |   6 +-
 packages/terminal/README.md                        |  15 +
 packages/terminal/README.zh.md                     |  15 +
 packages/terminal/terminal-bash/README.i18n.yaml   |   6 +
 .../pty-local => terminal/terminal-bash}/README.md |  10 +-
 .../terminal-bash}/README.zh.md                    |  10 +-
 .../terminal-bash}/package.json                    |  10 +-
 .../terminal-bash}/src/config.ts                   |  10 +-
 .../terminal-bash}/src/index.ts                    |  34 +-
 .../terminal-bash}/src/invariant.ts                |   8 +-
 .../terminal-bash}/src/sanitize.ts                 |   2 +-
 .../terminal-bash}/src/session.ts                  |  60 +-
 .../terminal-bash}/tests/config.spec.ts            |   6 +-
 .../terminal-bash}/tests/index.spec.ts             |  92 +--
 .../terminal-bash}/tests/local.spec.ts             |  70 +-
 .../terminal-bash}/tests/sanitize.spec.ts          |   2 +-
 .../terminal-bash}/tests/session.spec.ts           |  60 +-
 .../terminal-bash}/tsconfig.json                   |   4 +-
 .../terminal}/README.i18n.yaml                     |   6 +-
 packages/{pty/pty => terminal/terminal}/README.md  |  14 +-
 .../{pty/pty => terminal/terminal}/README.zh.md    |  12 +-
 .../{pty/pty => terminal/terminal}/package.json    |   6 +-
 .../{pty/pty => terminal/terminal}/src/index.ts    | 158 ++--
 .../pty => terminal/terminal}/src/invariant.ts     |   8 +-
 .../{pty/pty => terminal/terminal}/src/types.ts    |  74 +-
 .../terminal}/tests/service.spec.ts                | 248 +++----
 .../{pty/pty => terminal/terminal}/tsconfig.json   |   2 +-
 packages/terminal/tool-terminal/README.i18n.yaml   |   6 +
 packages/terminal/tool-terminal/README.md          |  71 ++
 packages/terminal/tool-terminal/README.zh.md       |  71 ++
 .../tool-terminal}/package.json                    |  26 +-
 .../tool-terminal}/src/index.ts                    |  66 +-
 .../tool-terminal}/src/invariant.ts                |  10 +-
 .../tool-terminal}/src/render.ts                   |   6 +-
 .../tests/loader-composition.spec.ts               |  32 +-
 .../tool-terminal}/tests/render.spec.ts            |  22 +-
 .../tool-terminal}/tests/tools.spec.ts             |  80 +-
 .../tool-terminal}/tsconfig.json                   |   8 +-
 .../fs-policy => test-support}/README.i18n.yaml    |   6 +-
 packages/{support => test-support}/README.md       |   6 +-
 packages/{support => test-support}/README.zh.md    |   6 +-
 .../acp-snapshot/README.i18n.yaml                  |   4 +-
 .../acp-snapshot/README.md                         |   0
 .../acp-snapshot/README.zh.md                      |  16 +-
 .../acp-snapshot/package.json                      |   4 +-
 .../acp-snapshot/src/harness.ts                    |   0
 .../acp-snapshot/src/index.ts                      |   0
 .../acp-snapshot/src/invariant.ts                  |   0
 .../acp-snapshot/src/launcher.ts                   |   2 +-
 .../acp-snapshot/src/normalize.ts                  |   2 +-
 .../acp-snapshot/src/suite.ts                      |   4 +-
 .../acp-snapshot/tests/fixtures/fake-acp-agent.ts  |   4 +-
 .../fixtures/record-suite/rec-child/behavior.json  |   0
 .../fixtures/record-suite/rec-child/input.json     |   0
 .../record-suite/rec-child/session.1.jsonl         |   0
 .../fixtures/record-suite/rec-child/session.jsonl  |   0
 .../record-suite/rec-child/stdout.expected.jsonl   |   0
 .../fixtures/record-suite/rec-pin/behavior.json    |   0
 .../tests/fixtures/record-suite/rec-pin/input.json |   0
 .../fixtures/record-suite/rec-pin/session.1.jsonl  |   0
 .../fixtures/record-suite/rec-pin/session.jsonl    |   0
 .../record-suite/rec-pin/stdout.expected.jsonl     |   0
 .../record-suite/rec-pin/system-prompt.expected.md |   0
 .../rec-pin/tool-schemas.expected.json             |   0
 .../fixtures/record-suite/rec-skip/behavior.json   |   0
 .../fixtures/record-suite/rec-skip/input.json      |   0
 .../record-suite/rec-skip/replay.override.json     |   0
 .../fixtures/record-suite/rec-skip/session.jsonl   |   0
 .../record-suite/rec-skip/stdout.expected.jsonl    |   0
 .../fixtures/suite/authored-error/behavior.json    |   0
 .../tests/fixtures/suite/authored-error/input.json |   0
 .../suite/authored-error/replay.override.json      |   0
 .../fixtures/suite/authored-error/session.jsonl    |   0
 .../suite/authored-error/stdout.expected.jsonl     |   0
 .../tests/fixtures/suite/blocked-log/behavior.json |   0
 .../tests/fixtures/suite/blocked-log/input.json    |   0
 .../tests/fixtures/suite/blocked-log/session.jsonl |   0
 .../suite/blocked-log/stdout.expected.jsonl        |   0
 .../tests/fixtures/suite/no-model/behavior.json    |   0
 .../tests/fixtures/suite/no-model/input.json       |   0
 .../tests/fixtures/suite/no-model/session.jsonl    |   0
 .../fixtures/suite/no-model/stdout.expected.jsonl  |   0
 .../tests/fixtures/suite/pin-turn/behavior.json    |   0
 .../tests/fixtures/suite/pin-turn/input.json       |   0
 .../tests/fixtures/suite/pin-turn/session.jsonl    |   0
 .../fixtures/suite/pin-turn/stdout.expected.jsonl  |   0
 .../suite/pin-turn/system-prompt.expected.md       |   0
 .../suite/pin-turn/tool-schemas.expected.json      |   0
 .../tests/fixtures/suite/plain-turn/behavior.json  |   0
 .../tests/fixtures/suite/plain-turn/input.json     |   0
 .../fixtures/suite/plain-turn/session.1.jsonl      |   0
 .../tests/fixtures/suite/plain-turn/session.jsonl  |   0
 .../suite/plain-turn/stdout.expected.jsonl         |   0
 .../suite/plain-turn/system-prompt.1.expected.md   |   0
 .../suite/plain-turn/tool-schemas.1.expected.json  |   0
 .../fixtures/suite/plain-turn/workspace/seed.txt   |   0
 .../tests/fixtures/suite/shared-pin/behavior.json  |   0
 .../tests/fixtures/suite/shared-pin/input.json     |   0
 .../tests/fixtures/suite/shared-pin/session.jsonl  |   0
 .../suite/shared-pin/stdout.expected.jsonl         |   0
 .../acp-snapshot/tests/harness.spec.ts             |   0
 .../acp-snapshot/tests/normalize.spec.ts           |   2 +-
 .../acp-snapshot/tests/suite.spec.ts               |   4 +-
 .../acp-snapshot/tsconfig.json                     |   2 +-
 .../agent-loop-testkit/README.i18n.yaml            |   2 +-
 .../agent-loop-testkit/README.md                   |   0
 .../agent-loop-testkit/README.zh.md                |   0
 .../agent-loop-testkit/package.json                |   4 +-
 .../agent-loop-testkit/src/index.ts                |  12 +-
 .../agent-loop-testkit/src/invariant.ts            |   0
 .../tests/agent-loop-testkit.spec.ts               |   0
 .../agent-loop-testkit/tsconfig.json               |   2 +-
 .../test-support/client-runtime/README.i18n.yaml   |   6 +
 .../client-runtime}/README.md                      |   4 +-
 .../client-runtime}/README.zh.md                   |   4 +-
 .../client-runtime}/package.json                   |   6 +-
 .../client-runtime}/src/fixtures.ts                |   2 +-
 .../client-runtime}/src/index.ts                   |  24 +-
 .../client-runtime}/src/invariant.ts               |   2 +-
 .../client-runtime}/src/locale-env.ts              |   2 +-
 .../client-runtime}/src/remote.ts                  |   2 +-
 .../client-runtime}/src/sessions.ts                |  12 +-
 .../client-runtime}/src/settings-scope.ts          |   0
 .../client-runtime}/src/snapshot.ts                |   4 +-
 .../client-runtime}/src/translate.ts               |   4 +-
 .../client-runtime}/src/workspaces.ts              |  10 +
 .../__snapshots__/runtime.client.spec.tsx.snap}    |   0
 .../client-runtime/tests/invariant.client.spec.ts} |   4 +-
 .../client-runtime/tests/remote.client.spec.ts}    |   2 +-
 .../client-runtime/tests/runtime.client.spec.tsx}  |  11 +-
 packages/test-support/client-runtime/tsconfig.json |  30 +
 .../client-runtime}/tsdown.config.ts               |   2 +-
 .../llm-mock-server/README.i18n.yaml               |   2 +-
 .../llm-mock-server/README.md                      |   0
 .../llm-mock-server/README.zh.md                   |   0
 .../llm-mock-server/package.json                   |   4 +-
 .../llm-mock-server/src/bin.ts                     |   2 +-
 .../llm-mock-server/src/cli.ts                     |   2 +-
 .../llm-mock-server/src/index.ts                   |   0
 .../llm-mock-server/src/invariant.ts               |   0
 .../llm-mock-server/tests/cli.spec.ts              |   2 +-
 .../llm-mock-server/tests/invariant.spec.ts        |   4 +-
 .../llm-mock-server/tests/server.spec.ts           |   2 +-
 .../llm-mock-server/tsconfig.json                  |   2 +-
 .../llm-mock-server/tsdown.config.ts               |   0
 packages/test-support/llm-replay/README.i18n.yaml  |   6 +
 .../{support => test-support}/llm-replay/README.md |   4 +-
 .../llm-replay/README.zh.md                        |  10 +-
 .../llm-replay/package.json                        |   8 +-
 .../llm-replay/src/index.ts                        |  16 +-
 .../llm-replay/src/invariant.ts                    |   0
 .../llm-replay/tests/llm-replay.spec.ts            | 100 +--
 packages/test-support/llm-replay/tsconfig.json     |  30 +
 .../loader-smoke/README.i18n.yaml                  |   2 +-
 .../loader-smoke/README.md                         |   0
 .../loader-smoke/README.zh.md                      |   0
 .../loader-smoke/package.json                      |   4 +-
 .../loader-smoke/src/agent-turn.ts                 |   2 +-
 .../loader-smoke/src/index.ts                      |   0
 .../loader-smoke/src/invariant.ts                  |   0
 .../loader-smoke/tests/agent-turn.spec.ts          |   2 +-
 .../loader-smoke/tests/example-launch.spec.ts      |   2 +-
 .../loader-smoke/tests/fixtures/fail.ts            |   0
 .../loader-smoke/tests/fixtures/hang.ts            |   0
 .../loader-smoke/tests/fixtures/success.ts         |   0
 .../loader-smoke/tests/loader-smoke.spec.ts        |   0
 .../loader-smoke/tsconfig.json                     |   2 +-
 packages/todo/tool-todo/README.i18n.yaml           |   2 +-
 packages/todo/tool-todo/README.zh.md               |   2 +-
 packages/todo/tool-todo/package.json               |   4 +-
 packages/todo/tool-todo/src/index.ts               |   4 +-
 packages/todo/tool-todo/src/invariant.ts           |   2 +-
 packages/todo/tool-todo/tests/integration.spec.ts  |   2 +-
 packages/todo/tool-todo/tests/invariant.spec.ts    |  12 +-
 .../tool-todo/tests/loader-composition.spec.ts     |   4 +-
 packages/todo/tool-todo/tests/projection.spec.ts   |  10 +-
 packages/todo/tool-todo/tests/tool-todo.spec.ts    |   8 +-
 packages/todo/tool-todo/tsconfig.json              |   2 +-
 packages/typert/generator/README.i18n.yaml         |   4 +-
 packages/typert/generator/README.md                |   4 +-
 packages/typert/generator/README.zh.md             |   4 +-
 packages/typert/generator/package.json             |   2 +-
 packages/typert/generator/src/analyzer.ts          | 138 ++--
 packages/typert/generator/src/cordis-catalog.ts    |   6 +-
 packages/typert/generator/src/emitter.ts           |  27 +-
 packages/typert/generator/src/model.ts             |   8 +-
 packages/typert/generator/src/tsdown-plugin.ts     |   2 +-
 packages/typert/generator/src/workspace.ts         |   6 +-
 .../tests/cordis-catalog-contract.spec.ts          |   4 +-
 .../typert/generator/tests/cordis-catalog.spec.ts  |   2 +-
 .../remote-model/packages/domain/src/index.ts      |  12 +-
 .../remote-model/packages/remote/package.json      |   3 +-
 .../remote-model/packages/remote/src/index.ts      |   4 +-
 .../tests/fixtures/remote-model/tsconfig.base.json |   2 +-
 .../{type-meta.d.ts => typert-protocol.d.ts}       |  44 +-
 .../typert/generator/tests/remote-model.spec.ts    | 153 ++--
 .../typert/generator/tests/tools-catalog.spec.ts   |   2 +-
 .../typert/generator/tests/tsdown-plugin.spec.ts   |   2 +-
 packages/typert/generator/tests/type-model.spec.ts |   6 +-
 packages/typert/generator/tsconfig.json            |   2 +-
 packages/typert/loader/README.i18n.yaml            |   2 +-
 packages/typert/loader/README.zh.md                |   4 +-
 packages/typert/loader/package.json                |   2 +-
 packages/typert/loader/src/index.ts                |   4 +-
 packages/typert/loader/tests/loader.spec.ts        |   2 +-
 packages/typert/loader/tsconfig.json               |   2 +-
 .../{type-meta => protocol}/README.i18n.yaml       |   6 +-
 packages/typert/{type-meta => protocol}/README.md  |  20 +-
 packages/typert/protocol/README.zh.md              |  38 +
 .../typert/{type-meta => protocol}/package.json    |   8 +-
 .../typert/{type-meta => protocol}/src/index.ts    | 122 ++--
 .../{type-meta => protocol}/src/invariant.ts       |   8 +-
 .../typert/{type-meta => protocol}/src/types.ts    | 204 +++---
 .../tests/fixtures/source-launch.ts                |   6 +-
 .../tests/protocol.spec.ts}                        |  58 +-
 .../typert/{type-meta => protocol}/tsconfig.json   |   2 +-
 packages/typert/registry/package.json              |   4 +-
 packages/typert/registry/src/client/index.ts       |   2 +-
 packages/typert/registry/src/index.ts              |  10 +-
 packages/typert/registry/src/service.ts            | 139 ++--
 packages/typert/registry/src/types.ts              |   2 +-
 packages/typert/registry/tests/typert.spec.ts      |  35 +-
 packages/typert/registry/tsconfig.json             |   4 +-
 packages/typert/type-meta/README.zh.md             |  38 -
 packages/util/README.i18n.yaml                     |   4 +-
 packages/util/README.md                            |   4 +-
 packages/util/README.zh.md                         |   4 +-
 packages/util/atomic-write/README.i18n.yaml        |   4 +-
 packages/util/atomic-write/README.md               |   2 +-
 packages/util/atomic-write/README.zh.md            |   2 +-
 packages/util/atomic-write/package.json            |   2 +-
 .../util/atomic-write/tests/atomic-write.spec.ts   |   2 +-
 packages/util/atomic-write/tests/invariant.spec.ts |   4 +-
 packages/util/atomic-write/tsconfig.json           |   2 +-
 packages/util/brand/README.i18n.yaml               |   4 +-
 packages/util/brand/README.md                      |   4 +-
 packages/util/brand/README.zh.md                   |   4 +-
 packages/util/brand/package.json                   |   2 +-
 packages/util/brand/src/index.ts                   |   2 +-
 packages/util/brand/tsconfig.json                  |   2 +-
 packages/util/environment/README.i18n.yaml         |   6 -
 packages/util/home-paths/README.i18n.yaml          |   6 +
 packages/util/{paths => home-paths}/README.md      |   2 +-
 packages/util/{paths => home-paths}/README.zh.md   |   2 +-
 packages/util/{paths => home-paths}/package.json   |   6 +-
 packages/util/{paths => home-paths}/src/index.ts   |   4 +-
 .../{retention => home-paths}/src/invariant.ts     |   8 +-
 .../tests/home-paths.spec.ts}                      |   4 +-
 .../util/{environment => home-paths}/tsconfig.json |   2 +-
 packages/util/launch-environment/README.i18n.yaml  |   6 +
 .../{environment => launch-environment}/README.md  |   8 +-
 .../README.zh.md                                   |   8 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |  42 +-
 .../src/invariant.ts                               |   8 +-
 .../tests/launch-environment.spec.ts}              |  20 +-
 .../{paths => launch-environment}/tsconfig.json    |   2 +-
 packages/util/native-command/README.i18n.yaml      |   4 +-
 packages/util/native-command/README.md             |   2 +-
 packages/util/native-command/README.zh.md          |   2 +-
 packages/util/native-command/package.json          |   2 +-
 packages/util/native-command/tsconfig.json         |   2 +-
 packages/util/output-retention/README.i18n.yaml    |   6 +
 .../util/{retention => output-retention}/README.md |   8 +-
 .../{retention => output-retention}/README.zh.md   |   8 +-
 .../{retention => output-retention}/package.json   |   6 +-
 .../{retention => output-retention}/src/index.ts   |   4 +-
 .../{paths => output-retention}/src/invariant.ts   |   8 +-
 .../tests/output-retention.spec.ts}                |   4 +-
 .../{retention => output-retention}/tsconfig.json  |   2 +-
 packages/util/paths/README.i18n.yaml               |   6 -
 packages/util/retention/README.i18n.yaml           |   6 -
 packages/util/timeout/README.i18n.yaml             |   4 +-
 packages/util/timeout/README.md                    |   2 +-
 packages/util/timeout/README.zh.md                 |  10 +-
 packages/util/timeout/package.json                 |   2 +-
 packages/util/timeout/tests/timeout.spec.ts        |   4 +-
 packages/util/timeout/tsconfig.json                |   2 +-
 packages/web/README.i18n.yaml                      |   4 +-
 packages/web/README.md                             |   2 +-
 packages/web/README.zh.md                          |   2 +-
 packages/web/tool-web/README.i18n.yaml             |   4 +-
 packages/web/tool-web/README.md                    |   8 +-
 packages/web/tool-web/README.zh.md                 |  10 +-
 packages/web/tool-web/package.json                 |   6 +-
 packages/web/tool-web/src/fetch.ts                 |   4 +-
 packages/web/tool-web/src/index.ts                 |   2 +-
 packages/web/tool-web/src/search.ts                |   6 +-
 packages/web/tool-web/tests/integration.spec.ts    |  26 +-
 packages/web/tool-web/tests/load-path.spec.ts      |   8 +-
 packages/web/tool-web/tests/spill.spec.ts          |  10 +-
 packages/web/tool-web/tests/tool-web.spec.ts       |  24 +-
 packages/web/tool-web/tsconfig.json                |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../{web-fetch-local => web-fetch-http}/README.md  |   6 +-
 .../README.zh.md                                   |   8 +-
 .../package.json                                   |   6 +-
 .../src/index.ts                                   |  28 +-
 .../src/invariant.ts                               |   8 +-
 .../src/policy.ts                                  |   8 +-
 .../src/provider.ts                                |  14 +-
 .../tests/fetch-http.spec.ts}                      |  44 +-
 .../tsconfig.json                                  |   2 +-
 packages/web/web-search-deepseek/README.i18n.yaml  |   2 +-
 packages/web/web-search-deepseek/README.zh.md      |   6 +-
 packages/web/web-search-deepseek/package.json      |   6 +-
 packages/web/web-search-deepseek/src/index.ts      |   6 +-
 .../web/web-search-deepseek/tests/deepseek.e2e.ts  |   2 +-
 .../web/web-search-deepseek/tests/deepseek.spec.ts |  22 +-
 .../web/web-search-deepseek/tests/settings.spec.ts |   8 +-
 packages/web/web-search-deepseek/tsconfig.json     |   4 +-
 packages/web/web-search-exa/package.json           |   6 +-
 packages/web/web-search-exa/src/index.ts           |   6 +-
 packages/web/web-search-exa/src/provider.ts        |   2 +-
 packages/web/web-search-exa/tests/exa.e2e.ts       |   2 +-
 packages/web/web-search-exa/tests/exa.spec.ts      |  12 +-
 packages/web/web-search-exa/tsconfig.json          |   4 +-
 .../web/web-search-perplexity/README.i18n.yaml     |   2 +-
 packages/web/web-search-perplexity/README.zh.md    |   2 +-
 packages/web/web-search-perplexity/package.json    |   6 +-
 packages/web/web-search-perplexity/src/index.ts    |   4 +-
 packages/web/web-search-perplexity/src/provider.ts |   2 +-
 .../web-search-perplexity/tests/perplexity.e2e.ts  |   2 +-
 .../web-search-perplexity/tests/perplexity.spec.ts |  12 +-
 packages/web/web-search-perplexity/tsconfig.json   |   4 +-
 packages/web/web/README.i18n.yaml                  |   4 +-
 packages/web/web/README.md                         |   6 +-
 packages/web/web/README.zh.md                      |   8 +-
 packages/web/web/package.json                      |   2 +-
 packages/web/web/src/index.ts                      |  14 +-
 packages/web/web/tests/web.spec.ts                 |  22 +-
 packages/web/web/tsconfig.json                     |   2 +-
 packages/workflow/README.i18n.yaml                 |   4 +-
 packages/workflow/README.md                        |   4 +-
 packages/workflow/README.zh.md                     |   4 +-
 packages/workflow/tool-ralph/README.i18n.yaml      |   4 +-
 packages/workflow/tool-ralph/README.md             |   6 +-
 packages/workflow/tool-ralph/README.zh.md          |  12 +-
 packages/workflow/tool-ralph/package.json          |   8 +-
 packages/workflow/tool-ralph/src/index.ts          |   6 +-
 .../workflow/tool-ralph/tests/integration.spec.ts  |  18 +-
 .../workflow/tool-ralph/tests/tool-ralph.spec.ts   |  18 +-
 packages/workflow/tool-ralph/tsconfig.json         |   2 +-
 packages/workflow/tool-workflow/README.i18n.yaml   |   4 +-
 packages/workflow/tool-workflow/README.md          |   2 +-
 packages/workflow/tool-workflow/README.zh.md       |   8 +-
 packages/workflow/tool-workflow/package.json       |   6 +-
 packages/workflow/tool-workflow/src/index.ts       |   6 +-
 packages/workflow/tool-workflow/src/invariant.ts   |   2 +-
 .../workflow/tool-workflow/tests/invariant.spec.ts |  10 +-
 .../tool-workflow/tests/tool-workflow.spec.ts      |  26 +-
 packages/workflow/tool-workflow/tsconfig.json      |   2 +-
 .../README.i18n.yaml                               |   6 +-
 .../README.md                                      |   6 +-
 .../README.zh.md                                   |   6 +-
 .../package.json                                   |   8 +-
 .../src/host.ts                                    |  14 +-
 .../src/index.ts                                   |  12 +-
 .../src/invariant.ts                               |   8 +-
 .../src/meta.ts                                    |   4 +-
 .../src/protocol.ts                                |   2 +-
 .../src/realm.ts                                   |   6 +-
 .../src/runtime.ts                                 |   4 +-
 .../src/session.ts                                 |   2 +-
 .../src/types.ts                                   |   2 +-
 .../src/worker.ts                                  |   2 +-
 .../tests/built-worker.e2e.ts                      |  10 +-
 .../tests/integration.spec.ts                      |  28 +-
 .../tests/meta.spec.ts                             |   4 +-
 .../tests/realm.spec.ts                            |   0
 .../tests/session.spec.ts                          |   4 +-
 .../tests/source-worker.compat.spec.ts             |  10 +-
 .../tests/workflow-worker-thread.e2e.ts}           |  24 +-
 .../tests/workflow-worker-thread.spec.ts}          | 152 ++--
 .../tsconfig.json                                  |   2 +-
 .../tsdown.config.ts                               |   0
 packages/workflow/workflow/README.i18n.yaml        |   4 +-
 packages/workflow/workflow/README.md               |   6 +-
 packages/workflow/workflow/README.zh.md            |  16 +-
 packages/workflow/workflow/package.json            |   4 +-
 packages/workflow/workflow/src/index.ts            |  10 +-
 packages/workflow/workflow/src/invariant.ts        |   2 +-
 packages/workflow/workflow/tests/invariant.spec.ts |   4 +-
 packages/workflow/workflow/tests/workflow.spec.ts  |  26 +-
 packages/workflow/workflow/tsconfig.json           |   2 +-
 packages/workspace/README.i18n.yaml                |   4 +-
 packages/workspace/README.md                       |   2 +-
 packages/workspace/README.zh.md                    |   2 +-
 packages/workspace/workspace/README.i18n.yaml      |   4 +-
 packages/workspace/workspace/README.md             |  15 +-
 packages/workspace/workspace/README.zh.md          |  15 +-
 packages/workspace/workspace/package.json          |   4 +-
 packages/workspace/workspace/src/entity.ts         |   2 +-
 packages/workspace/workspace/src/index.ts          |  41 +-
 packages/workspace/workspace/src/invariant.ts      |   8 +-
 .../workspace/workspace/tests/invariant.spec.ts    |   8 +-
 .../workspace/workspace/tests/workspace.spec.ts    |  61 +-
 packages/workspace/workspace/tsconfig.json         |   2 +-
 2784 files changed, 27992 insertions(+), 16521 deletions(-)
```

## 破坏性变更清单

- `ThemeService`（packages/client/ui-theme）：随 mainline 消失，依赖该面的插件需改适配。
- 删除的包目录：packages/bash/bash packages/bash/bash-env packages/bash/pwsh-local packages/bash/pwsh-sandbox packages/bash/tool-bash packages/bash/tool-pwsh packages/client/ui-command packages/client/ui-model packages/client/ui-models packages/client/ui-permission packages/client/ui-plugin-config packages/client/ui-slash packages/client/ui-task packages/interaction/permission packages/pty/pty-local packages/pty/tool-bash-persistent packages/pty/tool-pty packages/self-modification/tool-cordis packages/support/invariants packages/support/llm-replay packages/tasks/tasks packages/tasks/tasks-local packages/tasks/tool-tasks packages/typert/type-meta packages/util/environment packages/util/paths packages/util/retention。

## 插件侧建议（按仓库）

### chat-width
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 3 项中 3 不匹配: @deepseek-ai/dsh-client-locale=>=0.0.1-0↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=>=0.0.1-0↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=>=0.0.1-0↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### deepseek-harness-desktop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### deepseek-harness-distro
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### distill
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 7 项中 7 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-acp
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-agent-session-sources
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 29 项中 25 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subagent-claude-code=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-artifact
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-cc-tui
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 12 项中 1 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-coding-receipt
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
- 输入来自 DSH session log，建议在 mainline 会话持久化格式稳定后实现。
### dsh-companion
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 7 项中 7 不匹配: @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-cordis-examples
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-desktop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-feishu-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-gh-bridge
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-github-integration
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 7 项中 5 不匹配: @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-issue-filer
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-live-stats
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 7 项中 7 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-memory-evolve
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-my-rsi
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 95 项中 47 不匹配: @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-command-feedback=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-opencode-server
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-pi-adapter
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-prompt-studio
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-pty-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-session-search
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 3 项中 3 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-sfw
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-shell-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-skills-manager
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 无 dsh-* 依赖），建议确认所依赖的宿主面当日是否仍满足。
### dsh-skins
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 5 项中 5 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-subagent-tree
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-tool-browser
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 5 项中 5 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-tool-calculator
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-tool-encoding
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-tool-json
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-tool-time
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 2 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-ui-progress
- 兼容：锚定 20260805T134133Z（未知（非 commit 锚定: 20260805T134133Z））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-ui-whale
- 兼容：锚定 20260805T134133Z（未知（非 commit 锚定: 20260805T134133Z））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-vision
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-web-terminal
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 无 dsh-* 依赖），建议确认所依赖的宿主面当日是否仍满足。
### dsh-web-ui-approval-notify
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-web-ui
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 65 项中 51 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-workspace=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-workspace=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-sidebar=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-webserver=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-projection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-token-meter=^0.0.1-rc.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-wecom-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-weixin-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-win-port
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-working-activity
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dshx-update-check
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ex-setting
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 9 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### group-chat-diary
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### hub
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### issues
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### marisa
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 2 项匹配），建议确认所依赖的宿主面当日是否仍满足。
### plugin-registry
- 兼容：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁「无补丁」，当日 mainline 可干净集成。
### qqbot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### Qwen-MM-Plugins
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 4 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-mcp-client=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### Recall
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### review-panel
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-mxc
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 4 项中 3 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### session-chatlog
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 4 项中 4 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### session-persistence-rdb
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### telegram
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 3 项中 3 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### tg-bot
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 12 项中 10 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### toybox
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### turtle-ui
- 需适配：锚定 a6fedc9e3b36d066e34860d040db6df47d88c432（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### web-components
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 4 项中 4 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-web-ui-notify
- 未建模/状态未知：尚无 research/dsh-web-ui-notify.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-web-panel
- 未建模/状态未知：尚无 research/dsh-web-panel.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-evolve
- 未建模/状态未知：尚无 research/dsh-evolve.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-island
- 未建模/状态未知：尚无 research/dsh-island.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-drag-and-drop
- 未建模/状态未知：尚无 research/dsh-drag-and-drop.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-message-edit
- 未建模/状态未知：尚无 research/dsh-message-edit.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-deep-research
- 未建模/状态未知：尚无 research/dsh-deep-research.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-multimedia-webui-input
- 兼容：锚定 8ec407cd64（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### repo-visibility-guard
- 未建模/状态未知：尚无 research/repo-visibility-guard.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-grok-tui
- 未建模/状态未知：尚无 research/dsh-grok-tui.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### ds_web_craw
- 未建模/状态未知：尚无 research/ds_web_craw.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### fabric
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-browser
- 未建模/状态未知：尚无 research/dsh-browser.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-desktop-mac
- 未建模/状态未知：尚无 research/dsh-desktop-mac.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-public-repo-monitor
- 未建模/状态未知：尚无 research/dsh-public-repo-monitor.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tui
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-inspect
- 未建模/状态未知：尚无 research/dsh-inspect.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-hub
- 兼容：锚定 8ec407cd64（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-alphasolve
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### zotero-wave-rag
- 未建模/状态未知：尚无 research/zotero-wave-rag.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### onboarding
- 未建模/状态未知：尚无 research/onboarding.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### ego-browser
- 未建模/状态未知：尚无 research/ego-browser.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-nowledge-mem
- 未建模/状态未知：尚无 research/dsh-nowledge-mem.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-sidechain
- 未建模/状态未知：尚无 research/dsh-sidechain.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-a2a
- 未建模/状态未知：尚无 research/dsh-a2a.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-feishu-notify
- 未建模/状态未知：尚无 research/dsh-feishu-notify.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-remote
- 未建模/状态未知：尚无 research/dsh-remote.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### mstar-workflow
- 未建模/状态未知：尚无 research/mstar-workflow.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-scholar
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-issue-like-skill
- 未建模/状态未知：尚无 research/dsh-issue-like-skill.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tool-csv
- 未建模/状态未知：尚无 research/dsh-tool-csv.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tool-regex
- 未建模/状态未知：尚无 research/dsh-tool-regex.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-session-repair-skill
- 未建模/状态未知：尚无 research/dsh-session-repair-skill.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### DSH-better-sidebar
- 未建模/状态未知：尚无 research/DSH-better-sidebar.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-session-hub
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-ica
- 未建模/状态未知：尚无 research/dsh-ica.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-advisor
- 未建模/状态未知：尚无 research/dsh-advisor.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-llm-fallbacks
- 未建模/状态未知：尚无 research/dsh-llm-fallbacks.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-web-workflow-visualizer
- 未建模/状态未知：尚无 research/dsh-web-workflow-visualizer.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-checkpoint
- 未建模/状态未知：尚无 research/dsh-checkpoint.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-rewind
- 未建模/状态未知：尚无 research/dsh-rewind.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### official-plugins-port
- 未建模/状态未知：尚无 research/official-plugins-port.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### oh-my-dsh
- 未建模/状态未知：尚无 research/oh-my-dsh.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-side-panel
- 未建模/状态未知：尚无 research/dsh-side-panel.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-profile-bundle-example
- 未建模/状态未知：尚无 research/dsh-profile-bundle-example.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-plan-execute
- 未建模/状态未知：尚无 research/dsh-plan-execute.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-paste-input
- 兼容：锚定 20260808T121140Z（未知（非 commit 锚定: 20260808T121140Z））、补丁「无补丁」，当日 mainline 可干净集成。
### zotero-harvest
- 未建模/状态未知：尚无 research/zotero-harvest.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### zephyr
- 未建模/状态未知：尚无 research/zephyr.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-bash-encoding
- 兼容：锚定 20260808T121140Z（未知（非 commit 锚定: 20260808T121140Z））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-skill-stats
- 未建模/状态未知：尚无 research/dsh-skill-stats.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-web-archive
- 未建模/状态未知：尚无 research/dsh-web-archive.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### sandbox-micro
- 未建模/状态未知：尚无 research/sandbox-micro.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-git-identity
- 未建模/状态未知：尚无 research/dsh-git-identity.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-android
- 兼容：锚定 e56256082c（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-lazyfish
- 未建模/状态未知：尚无 research/dsh-lazyfish.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-auto-approval
- 未建模/状态未知：尚无 research/dsh-auto-approval.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-input-history
- 兼容：锚定 20260808T121140Z（未知（非 commit 锚定: 20260808T121140Z））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-client-ui-plan-execute
- 未建模/状态未知：尚无 research/dsh-client-ui-plan-execute.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-stickers
- 未建模/状态未知：尚无 research/dsh-stickers.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### deep-standard-skill
- 未建模/状态未知：尚无 research/deep-standard-skill.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-serenity-plugin
- 未建模/状态未知：尚无 research/dsh-serenity-plugin.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-toolkit
- 未建模/状态未知：尚无 research/dsh-toolkit.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tool-markdown
- 未建模/状态未知：尚无 research/dsh-tool-markdown.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-session-health
- 未建模/状态未知：尚无 research/dsh-session-health.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-desktop-tools
- 未建模/状态未知：尚无 research/dsh-desktop-tools.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-reuse-first
- 未建模/状态未知：尚无 research/dsh-reuse-first.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-plus
- 未建模/状态未知：尚无 research/dsh-plus.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-session-cluster
- 未建模/状态未知：尚无 research/dsh-session-cluster.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### DSH-UI4A
- 未建模/状态未知：尚无 research/DSH-UI4A.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-visualize
- 未建模/状态未知：尚无 research/dsh-visualize.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tps
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-plugin-check
- 未建模/状态未知：尚无 research/dsh-plugin-check.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-plugin-dev
- 未建模/状态未知：尚无 research/dsh-plugin-dev.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-gomoku
- 未建模/状态未知：尚无 research/dsh-gomoku.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-101
- 未建模/状态未知：尚无 research/dsh-101.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-turn-rewind
- 未建模/状态未知：尚无 research/dsh-turn-rewind.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-genui
- 未建模/状态未知：尚无 research/dsh-genui.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-mygo
- 未建模/状态未知：尚无 research/dsh-mygo.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### cross-harness-cite
- 未建模/状态未知：尚无 research/cross-harness-cite.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-split-panes
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-activity-plugin
- 未建模/状态未知：尚无 research/dsh-activity-plugin.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tool-diff
- 未建模/状态未知：尚无 research/dsh-tool-diff.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-mobileweb-adapter
- 未建模/状态未知：尚无 research/dsh-mobileweb-adapter.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-desktop-electron
- 兼容：锚定 da262ec14c（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-mineru
- 未建模/状态未知：尚无 research/dsh-mineru.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-pet
- 未建模/状态未知：尚无 research/dsh-pet.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-paseo
- 未建模/状态未知：尚无 research/dsh-paseo.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-superpowers
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-spec-kit
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-context7
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-vscode
- 未建模/状态未知：尚无 research/dsh-vscode.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tui-front-door
- 未建模/状态未知：尚无 research/dsh-tui-front-door.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-webbridge
- 未建模/状态未知：尚无 research/dsh-webbridge.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-custom-css
- 未建模/状态未知：尚无 research/dsh-custom-css.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### tonghuashun-harness
- 未建模/状态未知：尚无 research/tonghuashun-harness.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-club
- 未建模/状态未知：尚无 research/dsh-club.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-humanize
- 未建模/状态未知：尚无 research/dsh-humanize.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-agent-budget
- 未建模/状态未知：尚无 research/dsh-agent-budget.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-track
- 未建模/状态未知：尚无 research/dsh-track.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-spur
- 未建模/状态未知：尚无 research/dsh-spur.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-selection-chat
- 未建模/状态未知：尚无 research/dsh-selection-chat.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-browser-panel
- 未建模/状态未知：尚无 research/dsh-browser-panel.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-engram-relay
- 未建模/状态未知：尚无 research/dsh-engram-relay.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### yet-another-subagent
- 未建模/状态未知：尚无 research/yet-another-subagent.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-voice-chat
- 未建模/状态未知：尚无 research/dsh-voice-chat.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-ads
- 未建模/状态未知：尚无 research/dsh-ads.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-skill-session-recovery
- 未建模/状态未知：尚无 research/dsh-skill-session-recovery.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tavern-plugin
- 未建模/状态未知：尚无 research/dsh-tavern-plugin.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-qq2006
- 未建模/状态未知：尚无 research/dsh-qq2006.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-plugin-guide
- 未建模/状态未知：尚无 research/dsh-plugin-guide.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-mnemon
- 未建模/状态未知：尚无 research/dsh-mnemon.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-pet-rs
- 未建模/状态未知：尚无 research/dsh-pet-rs.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-auto-blame
- 未建模/状态未知：尚无 research/dsh-auto-blame.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-question-collapse
- 需适配：锚定 348409b1（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-latex
- 未建模/状态未知：尚无 research/dsh-latex.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tool-stat
- 未建模/状态未知：尚无 research/dsh-tool-stat.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tool-schema
- 未建模/状态未知：尚无 research/dsh-tool-schema.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-security-audit
- 未建模/状态未知：尚无 research/dsh-security-audit.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-browser-bridge
- 未建模/状态未知：尚无 research/dsh-browser-bridge.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### ya-workspace-sidebar
- 未建模/状态未知：尚无 research/ya-workspace-sidebar.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-d399
- 未建模/状态未知：尚无 research/dsh-d399.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### 7d7d
- 未建模/状态未知：尚无 research/7d7d.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-cordis-rocks
- 未建模/状态未知：尚无 research/dsh-cordis-rocks.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-sleep
- 未建模/状态未知：尚无 research/dsh-sleep.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-minigames
- 兼容：锚定 20260810T155924Z（未知（非 commit 锚定: 20260810T155924Z））、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-nono
- 未建模/状态未知：尚无 research/sandbox-nono.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-auto-chess
- 未建模/状态未知：尚无 research/dsh-auto-chess.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dshfind
- 未建模/状态未知：尚无 research/dshfind.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-cyber-sec
- 未建模/状态未知：尚无 research/dsh-cyber-sec.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-anti-ads
- 未建模/状态未知：尚无 research/dsh-anti-ads.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-self-control-guard
- 未建模/状态未知：尚无 research/dsh-self-control-guard.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### whale-girl
- 未建模/状态未知：尚无 research/whale-girl.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-codex-bridge
- 未建模/状态未知：尚无 research/dsh-codex-bridge.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-kimi-bridge
- 未建模/状态未知：尚无 research/dsh-kimi-bridge.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### session-teleport
- 未建模/状态未知：尚无 research/session-teleport.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-code-map
- 未建模/状态未知：尚无 research/dsh-code-map.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-loop
- 未建模/状态未知：尚无 research/dsh-loop.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-navbar
- 未建模/状态未知：尚无 research/dsh-navbar.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-task-status
- 未建模/状态未知：尚无 research/dsh-task-status.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-annotation
- 未建模/状态未知：尚无 research/dsh-annotation.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-ui-webview
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-web-review
- 未建模/状态未知：尚无 research/dsh-web-review.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-cc-connect
- 未建模/状态未知：尚无 research/dsh-cc-connect.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-focus-chat
- 未建模/状态未知：尚无 research/dsh-focus-chat.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-build
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### oh-my-deepseek
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-save-intp
- 未建模/状态未知：尚无 research/dsh-save-intp.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-find-plugins
- 未建模/状态未知：尚无 research/dsh-find-plugins.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-fkin-vibe
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-harness-ops
- 兼容：锚定 8ec407cd64（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-vision-toolkit
- 未建模/状态未知：尚无 research/dsh-vision-toolkit.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-code
- 需适配：锚定 1ec12f796a822c78fba9ad7f6448c3987e325c23（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### Top
- 未建模/状态未知：尚无 research/Top.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### __perm_probe__
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-kimi-browser
- 未建模/状态未知：尚无 research/dsh-kimi-browser.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-edu
- 未建模/状态未知：尚无 research/dsh-edu.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-ohos-patch
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（4 个补丁中 3 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### oh-dsh-desktop
- 未建模/状态未知：尚无 research/oh-dsh-desktop.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-plugin-skills
- 未建模/状态未知：尚无 research/dsh-plugin-skills.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-deep-whale
- 未建模/状态未知：尚无 research/dsh-deep-whale.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tool-search
- 未建模/状态未知：尚无 research/dsh-tool-search.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### oh-my-dsh-distribution
- 未建模/状态未知：尚无 research/oh-my-dsh-distribution.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-memory
- 未建模/状态未知：尚无 research/dsh-memory.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-chat
- 未建模/状态未知：尚无 research/dsh-chat.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-web
- 未建模/状态未知：尚无 research/dsh-web.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh_ide
- 未建模/状态未知：尚无 research/dsh_ide.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-trace
- 未建模/状态未知：尚无 research/dsh-trace.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### deepseek-manners
- 未建模/状态未知：尚无 research/deepseek-manners.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### plugin-template
- 兼容：锚定 README（未知（非 commit 锚定: README））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-design
- 未建模/状态未知：尚无 research/dsh-design.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-computer-use
- 未建模/状态未知：尚无 research/dsh-computer-use.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-meme
- 未建模/状态未知：尚无 research/dsh-meme.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-agent-rp
- 未建模/状态未知：尚无 research/dsh-agent-rp.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-music-player
- 未建模/状态未知：尚无 research/dsh-music-player.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-multica-runtime
- 未建模/状态未知：尚无 research/dsh-multica-runtime.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-mega
- 未建模/状态未知：尚无 research/dsh-mega.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-office
- 未建模/状态未知：尚无 research/dsh-office.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### savemoneybenchmark
- 未建模/状态未知：尚无 research/savemoneybenchmark.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-slice-agent-loop
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 8 项中 8 不匹配: @deepseek-ai/dsh-agent=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-invariants=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-scope=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-session-persistence=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-kb-sieve
- 未建模/状态未知：尚无 research/dsh-kb-sieve.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-data-agent
- 未建模/状态未知：尚无 research/dsh-data-agent.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-security
- 未建模/状态未知：尚无 research/dsh-security.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-teamwork
- 未建模/状态未知：尚无 research/dsh-teamwork.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### ui-status-label
- 未建模/状态未知：尚无 research/ui-status-label.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-easy-ctx-manager
- 未建模/状态未知：尚无 research/dsh-easy-ctx-manager.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### browser4-dsh
- 未建模/状态未知：尚无 research/browser4-dsh.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### show-bash-command
- 未建模/状态未知：尚无 research/show-bash-command.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-chat-thumb
- 兼容：锚定 README（未知（非 commit 锚定: README））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-super-injector
- 未建模/状态未知：尚无 research/dsh-super-injector.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-hmz
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-better-sidebar-plugin-office
- 未建模/状态未知：尚无 research/dsh-better-sidebar-plugin-office.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-explain
- 未建模/状态未知：尚无 research/dsh-explain.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-interpreters
- 未建模/状态未知：尚无 research/dsh-interpreters.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-stock-market
- 未建模/状态未知：尚无 research/dsh-stock-market.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-scout
- 未建模/状态未知：尚无 research/dsh-scout.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-diff-viewer
- 兼容：锚定 未知（未知）、补丁「OK（1 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 未知 显式记录到 README/补丁头，快照一漂即可自动预警。
### dsh-turn-navigator
- 未建模/状态未知：尚无 research/dsh-turn-navigator.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-mobile
- 未建模/状态未知：尚无 research/dsh-mobile.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-share
- 未建模/状态未知：尚无 research/dsh-share.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-travel-plugin
- 未建模/状态未知：尚无 research/dsh-travel-plugin.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-suggested-replies
- 未建模/状态未知：尚无 research/dsh-suggested-replies.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-aigc-canvas
- 未建模/状态未知：尚无 research/dsh-aigc-canvas.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-sonar
- 未建模/状态未知：尚无 research/dsh-sonar.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-ultra-ui
- 未建模/状态未知：尚无 research/dsh-ultra-ui.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-deepresearch
- 未建模/状态未知：尚无 research/dsh-deepresearch.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-notebooks
- 未建模/状态未知：尚无 research/dsh-notebooks.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### context-doctor
- 未建模/状态未知：尚无 research/context-doctor.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-openpencil
- 未建模/状态未知：尚无 research/dsh-openpencil.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-deeplink
- 未建模/状态未知：尚无 research/dsh-deeplink.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-cot-summary
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（7b9644f）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-emoji
- 未建模/状态未知：尚无 research/dsh-emoji.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh_workflow
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-openmaic
- 未建模/状态未知：尚无 research/dsh-openmaic.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-deepcel
- 未建模/状态未知：尚无 research/dsh-deepcel.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-STAR
- 未建模/状态未知：尚无 research/dsh-STAR.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-STAGE
- 未建模/状态未知：尚无 research/dsh-STAGE.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-conversation-share
- 未建模/状态未知：尚无 research/dsh-conversation-share.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### tonghuashun-webui
- 未建模/状态未知：尚无 research/tonghuashun-webui.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
