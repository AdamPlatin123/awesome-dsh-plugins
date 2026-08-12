# mainline 兼容性报告（2026-08-13）

- mainline：`7b9644f`（snapshots/20260812T172954Z-final-unwatermarked）
- 上次对比：`7b9644f2b664e46c9518506035aa6c8d5af4d8e8`
- 兼容性：87/284 无需适配，9 需适配（dsh-subagent-tree dsh-working-activity turtle-ui fabric dsh-tps dsh-split-panes dsh-question-collapse dsh-ohos-patch dsh-cot-summary）；其中关注 31、占位 13、不适用 2、已删除 0、未知 188

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
| dsh-scholar | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 26 项中 10 不匹配: @deepseek-ai/dsh-commands=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-conversation=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 | 未知（待调研） |
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
| dsh-track | 未知（非 commit 锚定: 20260812T172954Z-final-unwatermarked） | 无补丁 | 缺: ThemeService tuiPrompt | 4 项匹配 | 兼容 |
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
| dsh-openpencil | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 8 项匹配 | 未知（待调研） |
| dsh-deeplink | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cot-summary | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: ThemeService tuiPrompt | 17 项匹配 | 需适配 |
| dsh-emoji | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 11 项匹配 | 未知（待调研） |
| dsh_workflow | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 11 项匹配 | 未知（待调研） |
| dsh-openmaic | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 5 项匹配 | 未知（待调研） |
| dsh-deepcel | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-STAR | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-STAGE | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-conversation-share | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| tonghuashun-webui | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-session-notification | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-custom-tool | 未知（不同谱系） | 无补丁 | 缺: ThemeService tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2 | 关注 |
| dsh-openbiliclaw | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |
| dsh-longbridge | 未知 | 无补丁 | 缺: ThemeService tuiPrompt | 11 项中 11 不匹配: @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.2 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.2 | 未知（待调研） |

## mainline 变更分析（7b9644f2b664e46c9518506035aa6c8d5af4d8e8 → 7b9644f）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **包级变化**：packages/ 下删除 0 个包目录、新增 0 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：

新增文件：
```

```

### seam 符号变化

| 符号 | prev 存在性 | cur 存在性 | 变化 |
|---|---|---|---|
| `ThemeService` | 消失 | 消失 | 消失 → 消失 |
| `settingsNamespace` | 出现 | 出现 | 出现 → 出现（稳定） |
| `sessionProjections` | 出现 | 出现 | 出现 → 出现（稳定） |
| `tuiPrompt` | 消失 | 消失 | 消失 → 消失 |
| `slots` | 出现 | 出现 | 出现 → 出现（稳定） |
| `session/event` | 出现 | 出现 | 出现 → 出现（稳定） |

### diffstat（packages/ patches/ workspace）

```

```

## 破坏性变更清单

- 本日快照未发现 seam 符号级破坏。

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
- 未建模/状态未知：尚无 research/dsh-scholar.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
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
- 兼容：锚定 20260812T172954Z-final-unwatermarked（未知（非 commit 锚定: 20260812T172954Z-final-unwatermarked））、补丁「无补丁」，当日 mainline 可干净集成。
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
- 未建模/状态未知：尚无 research/dsh_workflow.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
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
### dsh-session-notification
- 未建模/状态未知：尚无 research/dsh-session-notification.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-custom-tool
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: ThemeService tuiPrompt；peer: 7 项中 7 不匹配: @deepseek-ai/dsh-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-tools=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-system-prompt=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-runtime=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-settings=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-ui-slots=^0.0.1-rc.1↔0.0.1-rc.2 @deepseek-ai/dsh-client-locale=^0.0.1-rc.1↔0.0.1-rc.2），建议确认所依赖的宿主面当日是否仍满足。
### dsh-openbiliclaw
- 未建模/状态未知：尚无 research/dsh-openbiliclaw.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-longbridge
- 未建模/状态未知：尚无 research/dsh-longbridge.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
