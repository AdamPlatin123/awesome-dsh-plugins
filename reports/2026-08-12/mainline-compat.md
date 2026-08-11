# mainline 兼容性报告（2026-08-12）

- mainline：`340d23a`（snapshots/20260811T152241Z）
- 上次对比：`3c21611f061661686ff987827a112da19461027d`
- 兼容性：89/251 无需适配，5 需适配（dsh-subagent-tree dsh-working-activity dsh-tps dsh-split-panes dsh-ohos-patch）；其中关注 26、占位 15、不适用 2、已删除 0、未知 157

## 兼容性矩阵

| 仓库 | 锚定 | 补丁 | seam | peerDeps | 综合判定 |
|---|---|---|---|---|---|
| chat-width | 未知 | 无补丁 | 缺: tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 | 关注 |
| deepseek-harness-desktop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| deepseek-harness-distro | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| distill | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-acp | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-agent-session-sources | 未知 | 无补丁 | 缺: tuiPrompt | 29 项中 25 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent-claude-code=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-artifact | 未知 | 无补丁 | 缺: tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-cc-tui | 未知 | 无补丁 | 缺: tuiPrompt | 12 项中 1 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-coding-receipt | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-companion | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-cordis-examples | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-desktop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-feishu-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-gh-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-github-integration | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 5 不匹配: @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-issue-filer | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-live-stats | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-memory-evolve | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-my-rsi | 未知（不同谱系） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 89 项中 38 不匹配: @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-command-feedback=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-opencode-server | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-pi-adapter | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-prompt-studio | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-pty-windows | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-session-search | 未知 | 无补丁 | 缺: tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-sfw | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-shell-windows | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-skills-manager | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 关注 |
| dsh-skins | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 5 项中 5 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-subagent-tree | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-workspace=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 需适配 |
| dsh-tool-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 5 项中 5 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-tool-calculator | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-tool-encoding | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-tool-json | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-tool-time | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-ui-progress | 未知（非 commit 锚定: 20260805T134133Z） | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-ui-whale | 未知（非 commit 锚定: 20260805T134133Z） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-vision | 未知 | 无补丁 | 缺: tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-web-terminal | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-web-ui-approval-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-web-ui | 未知 | 无补丁 | 缺: tuiPrompt | 61 项匹配 | 兼容 |
| dsh-wecom-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-weixin-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-win-port | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-working-activity | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 | 需适配 |
| dshx-update-check | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| ex-setting | 未知 | 无补丁 | 缺: tuiPrompt | 9 项中 9 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 | 关注 |
| group-chat-diary | 未知（非 commit 锚定: YYYY-MM-DD） | 不适用 | 不适用 | 不适用 | 不适用 |
| hub | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| issues | 未知 | 不适用 | 不适用 | 不适用 | 不适用 |
| marisa | 未知（非 commit 锚定: snapshot-20260807T130646Z） | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 关注 |
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| qqbot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| Qwen-MM-Plugins | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-mcp-client=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill-local=^0.0.1↔0.0.1-rc.1 | 关注 |
| Recall | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| review-panel | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-mxc | 未知 | 无补丁 | 缺: tuiPrompt | 4 项中 3 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 | 关注 |
| session-chatlog | 未知 | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| session-persistence-rdb | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| telegram | 未知 | 无补丁 | 缺: tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 | 关注 |
| tg-bot | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 12 项中 12 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-interaction=^0.0.1↔0.0.1-rc.1 | 关注 |
| toybox | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| turtle-ui | 未知（不同谱系） | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| web-components | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-web-ui-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-web-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-evolve | 未知 | 无补丁 | 缺: tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-island | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-drag-and-drop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-message-edit | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-deep-research | 未知 | 无补丁 | 缺: tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-multimedia-webui-input | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| repo-visibility-guard | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-grok-tui | 未知 | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 未知（待调研） |
| ds_web_craw | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| fabric | 未知 | 无补丁 | 缺: tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-command=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 5 项中 5 不匹配: @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-desktop-mac | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-public-repo-monitor | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tui | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-inspect | 未知 | 无补丁 | 缺: tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-hub | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-alphasolve | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| zotero-wave-rag | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| onboarding | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| ego-browser | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-nowledge-mem | 未知 | 无补丁 | 缺: tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-sidechain | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-a2a | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 19 项中 18 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-feishu-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-remote | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| mstar-workflow | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill-local=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-scholar | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-issue-like-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-csv | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-tool-regex | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-session-repair-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| DSH-better-sidebar | 未知 | 无补丁 | 缺: tuiPrompt | 14 项匹配 | 未知（待调研） |
| dsh-session-hub | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-ica | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-advisor | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 17 项中 17 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-api-gateway=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-type-meta=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-typert-registry=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-llm-fallbacks | 未知（不同谱系） | OK（4 个补丁全部干净应用） | 缺: tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-web-workflow-visualizer | 未知 | 无补丁 | 缺: tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-checkpoint | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-rewind | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| official-plugins-port | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| oh-my-dsh | 未知 | 无补丁 | 缺: tuiPrompt | 2167 项中 838 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-retention=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-interaction=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash-env=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-code-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-retention=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-web=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm-deepseek=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sdk-protocol=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-interaction=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-hook-protocol=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-hook-protocol=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-mcp-client=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill-local=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-code-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-retention=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-spill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs-local=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-spill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-retention=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-spill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-modules=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-command=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-plan-mode=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-command=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-permission=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-typert-registry=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent-spine-demo=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-app-boot=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-checkpoint-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence-jsonl=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workspace-context=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-acp=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent-spine-demo=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-app-boot=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-checkpoint-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence-jsonl=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-query-sqlite=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workspace-context=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent-loop=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm-retry=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill-local=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks-local=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash-env=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tool-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tool-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tool-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tool-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workspace-context=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sdk-protocol=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-lsp=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-lsp=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-title=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-query=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact-tool-result-prune=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-compact=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-pty=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-pty=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-retention=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-pty=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-command-feedback=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-telemetry=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent-inprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sdk-client=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sdk-protocol=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent-inprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-scope=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection-cache=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-directory-picker-browse=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-directory-picker-native=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-workspace=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-workspace=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash-local=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash-env=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-bash-env=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-side-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-profile-bundle-example | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plan-execute | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 12 项中 12 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-plan-mode=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-paste-input | 未知（非 commit 锚定: 20260808T121140Z） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| zotero-harvest | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| zephyr | 未知 | 无补丁 | 缺: tuiPrompt | 134 项匹配 | 未知（待调研） |
| dsh-bash-encoding | 未知（非 commit 锚定: 20260808T121140Z） | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-skill-stats | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-web-archive | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| sandbox-micro | 未知 | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-git-identity | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-android | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-lazyfish | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-auto-approval | 未知 | 无补丁 | 缺: tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-input-history | 未知（非 commit 锚定: 20260808T121140Z） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-client-ui-plan-execute | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-stickers | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| deep-standard-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-serenity-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 5 项中 5 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-toolkit | 未知 | 无补丁 | 缺: tuiPrompt | 16 项匹配 | 未知（待调研） |
| dsh-tool-markdown | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-session-health | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-desktop-tools | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-reuse-first | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plus | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-session-cluster | 未知 | 无补丁 | 缺: tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| DSH-UI4A | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-visualize | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-tps | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| dsh-plugin-check | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-plugin-dev | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-gomoku | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-101 | 未知 | 无补丁 | 缺: tuiPrompt | 16 项中 16 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-layout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-turn-rewind | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-genui | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 9 项中 9 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-tool=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 关注 |
| dsh-mygo | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 9 项中 6 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 | 关注 |
| cross-harness-cite | 未知 | 无补丁 | 缺: tuiPrompt | 15 项中 11 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-split-panes | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| dsh-task-board | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-activity-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-diff | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-git-graph | 未知 | 无补丁 | 缺: tuiPrompt | 10 项中 10 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workspace=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-mobileweb-adapter | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-desktop-electron | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-mineru | 未知 | 无补丁 | 缺: tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-pet | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-paseo | 未知 | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-remote-web-ui | 未知 | 无补丁 | 缺: tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-sidebar=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-superpowers | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-spec-kit | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-context7 | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-vscode | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tui-front-door | 未知 | 无补丁 | 缺: tuiPrompt | 6 项中 5 不匹配: @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-webbridge | 未知 | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-custom-css | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| tonghuashun-harness | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-club | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-humanize | 未知 | 无补丁 | 缺: tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-agent-budget | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 10 项中 10 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-commands=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-goal=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-track | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 未知（待调研） |
| dsh-spur | 未知 | 无补丁 | 缺: tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-selection-chat | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-browser-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-engram-relay | 未知 | 无补丁 | 缺: tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| yet-another-subagent | 未知 | 无补丁 | 缺: tuiPrompt | 17 项中 17 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-tool=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tasks=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-voice-chat | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-ads | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-skill-session-recovery | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tavern-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-qq2006 | 未知 | 无补丁 | 缺: tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-plugin-guide | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-mnemon | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-pet-rs | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-auto-blame | 未知 | 无补丁 | 缺: tuiPrompt | 13 项中 13 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-question-collapse | 未知（不同谱系） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-latex | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-tool-stat | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-tool-schema | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-security-audit | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-browser-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-attachment=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| ya-workspace-sidebar | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-sidebar=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-d399 | 未知 | 无补丁 | 缺: tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| 7d7d | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cordis-rocks | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-pet-web | 未知 | 无补丁 | 缺: tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-sleep | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-minigames | 未知（非 commit 锚定: 20260810T155924Z） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-nono | 未知 | 无补丁 | 缺: tuiPrompt | 3 项中 2 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-auto-chess | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dshfind | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cyber-sec | 未知 | 无补丁 | 缺: tuiPrompt | 15 项匹配 | 未知（待调研） |
| dsh-anti-ads | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-self-control-guard | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| whale-girl | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-codex-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-kimi-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| session-teleport | 未知 | 无补丁 | 缺: tuiPrompt | 2 项中 2 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-code-map | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-loop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-navbar | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-task-status | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-annotation | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-ui-webview | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-web-review | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-cc-connect | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-focus-chat | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-build | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| oh-my-deepseek | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-save-intp | 未知 | 无补丁 | 缺: tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-find-plugins | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-fkin-vibe | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-harness-ops | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-vision-toolkit | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 13 项中 13 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-tool=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-code | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| Top | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| __perm_probe__ | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-kimi-browser | 未知 | 无补丁 | 缺: tuiPrompt | 3 项中 3 不匹配: @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-edu | 未知 | 无补丁 | 缺: tuiPrompt | 7 项中 7 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-ohos-patch | 未知 | CONFLICT（4 个补丁中 3 个 OK） | 缺: tuiPrompt | 无 dsh-* 依赖 | 需适配 |
| oh-dsh-desktop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plugin-skills | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-deep-whale | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-search | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| oh-my-dsh-distribution | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-memory | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-chat | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-web | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh_ide | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-trace | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 4 项中 4 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-telemetry=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| deepseek-manners | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| plugin-template | 未知（非 commit 锚定: README） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-design | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-computer-use | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 16 项中 16 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-meme | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-roleplay-portable-spike | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-music-player | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-multica-runtime | 未知 | 无补丁 | 缺: tuiPrompt | 8 项匹配 | 未知（待调研） |
| dsh-mega | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-office | 未知 | 无补丁 | 缺: tuiPrompt | 22 项中 20 不匹配: @deepseek-ai/dsh-client-runtime=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-schema-form=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-tool=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-brand=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-schema-form=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-tool=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.1.0↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.1.0↔0.0.1-rc.1 | 未知（待调研） |
| savemoneybenchmark | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-slice-agent-loop | 未知（非 commit 锚定: 20260811T152241Z） | 无补丁 | 缺: tuiPrompt | 8 项匹配 | 兼容 |
| dsh-kb-sieve | 未知 | 无补丁 | 缺: tuiPrompt | 1 项中 1 不匹配: @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-data-agent | 未知 | 无补丁 | 缺: tuiPrompt | 8 项中 8 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-webserver=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 | 未知（待调研） |
| dsh-security | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-teamwork | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 未知（待调研） |

## mainline 变更分析（3c21611f061661686ff987827a112da19461027d → 340d23a）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **workspace catalog 变更**：pnpm-workspace.yaml 增补条目（见 diffstat）。
- **包级变化**：packages/ 下删除 6 个包目录、新增 14 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：packages/scaffold/create-sdk packages/scaffold/helper packages/scaffold/protocol packages/scaffold/scripts packages/scaffold/server packages/scaffold/telemetry packages/self-modification/repository-plugin

新增文件：
```
packages/api/remotes/src/remote-events.ts
packages/api/remotes/src/types.ts
packages/bash/bash-local/tests/settings.spec.ts
packages/bash/pwsh-local/tests/settings.spec.ts
packages/boot/cmdline/README.md
packages/boot/cmdline/README.zh.md
packages/boot/cmdline/package.json
packages/boot/cmdline/src/index.ts
packages/boot/cmdline/src/invariant.ts
packages/boot/cmdline/tests/cmdline.spec.ts
packages/bundle/headless/src/startup.ts
packages/bundle/headless/tests/startup.spec.ts
packages/bundle/web-app/src/startup.ts
packages/bundle/web-app/tests/startup.spec.ts
packages/bundle/web-app/tests/trusted-hosts.spec.ts
```

### seam 符号变化

| 符号 | prev 存在性 | cur 存在性 | 变化 |
|---|---|---|---|
| `ThemeService` | 出现 | 出现 | 出现 → 出现（稳定） |
| `settingsNamespace` | 出现 | 出现 | 出现 → 出现（稳定） |
| `sessionProjections` | 出现 | 出现 | 出现 → 出现（稳定） |
| `tuiPrompt` | 消失 | 消失 | 消失 → 消失 |
| `slots` | 出现 | 出现 | 出现 → 出现（稳定） |
| `session/event` | 出现 | 出现 | 出现 → 出现（稳定） |

### diffstat（packages/ patches/ workspace）

```
 packages/README.i18n.yaml                          |   4 +-
 packages/README.md                                 |  84 +-
 packages/README.zh.md                              |   6 +-
 packages/acp/acp/package.json                      |  25 +-
 packages/acp/acp/src/index.ts                      |   8 +-
 packages/acp/acp/src/invariant.ts                  |   2 +-
 packages/acp/acp/tests/harness.ts                  |   2 +-
 packages/api/gateway/README.i18n.yaml              |   4 +-
 packages/api/gateway/README.md                     |   3 +
 packages/api/gateway/README.zh.md                  |   3 +
 packages/api/gateway/package.json                  |  21 +-
 packages/api/gateway/src/client/index.ts           |  79 +-
 packages/api/gateway/src/index.ts                  |   2 +-
 packages/api/gateway/src/invariant.ts              |   5 +-
 packages/api/gateway/src/types.ts                  |   2 +-
 packages/api/gateway/tests/client.spec.ts          | 162 +++-
 packages/api/gateway/tests/gateway.spec.ts         |   2 +-
 packages/api/remotes/README.i18n.yaml              |   4 +-
 packages/api/remotes/README.md                     |  14 +-
 packages/api/remotes/README.zh.md                  |  14 +-
 packages/api/remotes/package.json                  |  44 +-
 packages/api/remotes/src/agent-lookup.ts           |   2 +-
 packages/api/remotes/src/client/index.ts           |  21 +-
 packages/api/remotes/src/index.ts                  |  25 +
 packages/api/remotes/src/invariant.ts              |   2 +-
 packages/api/remotes/src/remote-events.ts          |  23 +
 packages/api/remotes/src/types.ts                  |  19 +
 packages/api/remotes/tests/agent-lookup.spec.ts    |   2 +-
 packages/api/remotes/tests/built-lib.e2e.ts        |   4 +-
 packages/api/remotes/tsconfig.client.json          |  22 +-
 packages/api/remotes/tsconfig.host.json            |  19 +-
 .../attachment/attachment-local/README.i18n.yaml   |   4 +-
 packages/attachment/attachment-local/README.md     |   2 +-
 packages/attachment/attachment-local/README.zh.md  |   2 +-
 packages/attachment/attachment-local/package.json  |  23 +-
 packages/attachment/attachment-local/src/index.ts  |   8 +-
 .../attachment/attachment-local/src/invariant.ts   |   4 +-
 packages/attachment/attachment-local/src/store.ts  |  14 +-
 .../attachment-local/tests/index.spec.ts           |   2 +-
 .../attachment-local/tests/store.spec.ts           |  27 +-
 packages/attachment/attachment/README.i18n.yaml    |   4 +-
 packages/attachment/attachment/README.md           |   2 +-
 packages/attachment/attachment/README.zh.md        |   2 +-
 packages/attachment/attachment/package.json        |  19 +-
 packages/attachment/attachment/src/index.ts        |   8 +-
 packages/attachment/attachment/src/invariant.ts    |   4 +-
 packages/bash/bash-env/README.i18n.yaml            |   4 +-
 packages/bash/bash-env/README.md                   |   2 +-
 packages/bash/bash-env/README.zh.md                |   2 +-
 packages/bash/bash-env/package.json                |  27 +-
 packages/bash/bash-env/src/index.ts                |   6 +-
 packages/bash/bash-env/src/invariant.ts            |   2 +-
 packages/bash/bash-env/tests/bash-env.spec.ts      |   2 +-
 packages/bash/bash-local/README.i18n.yaml          |   4 +-
 packages/bash/bash-local/README.md                 |   3 +-
 packages/bash/bash-local/README.zh.md              |   3 +-
 packages/bash/bash-local/package.json              |  27 +-
 packages/bash/bash-local/src/index.ts              |  55 +-
 packages/bash/bash-local/src/invariant.ts          |   2 +-
 packages/bash/bash-local/tests/executor.spec.ts    |   4 +-
 packages/bash/bash-local/tests/settings.spec.ts    | 115 +++
 packages/bash/bash-local/tsconfig.json             |   3 +
 packages/bash/bash-sandbox/package.json            |  25 +-
 packages/bash/bash-sandbox/src/index.ts            |   2 +-
 packages/bash/bash-sandbox/src/invariant.ts        |   2 +-
 packages/bash/bash-sandbox/tests/bwrap.e2e.ts      |   2 +-
 packages/bash/bash-sandbox/tests/landlock.e2e.ts   |   2 +-
 .../bash-sandbox/tests/partial-landlock.spec.ts    |   2 +-
 packages/bash/bash-sandbox/tests/sandbox.spec.ts   |   2 +-
 packages/bash/bash-sandbox/tests/seatbelt.e2e.ts   |   2 +-
 packages/bash/bash/README.i18n.yaml                |   4 +-
 packages/bash/bash/README.md                       |   4 +-
 packages/bash/bash/README.zh.md                    |   4 +-
 packages/bash/bash/package.json                    |  23 +-
 packages/bash/bash/src/index.ts                    |  16 +-
 packages/bash/bash/src/invariant.ts                |   2 +-
 packages/bash/bash/tests/service.spec.ts           |   2 +-
 packages/bash/bash/tsconfig.json                   |   3 +
 packages/bash/pwsh-local/README.i18n.yaml          |   4 +-
 packages/bash/pwsh-local/README.md                 |   3 +-
 packages/bash/pwsh-local/README.zh.md              |   3 +-
 packages/bash/pwsh-local/package.json              |  27 +-
 packages/bash/pwsh-local/src/index.ts              |  78 +-
 packages/bash/pwsh-local/src/invariant.ts          |   2 +-
 packages/bash/pwsh-local/tests/executor.spec.ts    |   6 +-
 packages/bash/pwsh-local/tests/settings.spec.ts    | 108 +++
 packages/bash/pwsh-local/tsconfig.json             |   3 +
 packages/bash/pwsh-sandbox/README.i18n.yaml        |   4 +-
 packages/bash/pwsh-sandbox/README.md               |   4 +-
 packages/bash/pwsh-sandbox/README.zh.md            |   4 +-
 packages/bash/pwsh-sandbox/package.json            |  25 +-
 packages/bash/pwsh-sandbox/src/index.ts            |   2 +-
 packages/bash/pwsh-sandbox/src/invariant.ts        |   2 +-
 packages/bash/pwsh-sandbox/tests/acl.e2e.ts        |  46 +-
 packages/bash/pwsh-sandbox/tests/sandbox.spec.ts   |   2 +-
 packages/bash/tool-bash/README.i18n.yaml           |   4 +-
 packages/bash/tool-bash/README.md                  |   2 +-
 packages/bash/tool-bash/README.zh.md               |   2 +-
 packages/bash/tool-bash/package.json               |  39 +-
 packages/bash/tool-bash/src/index.ts               |   4 +-
 packages/bash/tool-bash/src/invariant.ts           |   2 +-
 packages/bash/tool-bash/src/render.ts              |   2 +-
 packages/bash/tool-bash/tests/integration.spec.ts  |  61 +-
 packages/bash/tool-bash/tests/tools.spec.ts        |   8 +-
 packages/bash/tool-pwsh/README.i18n.yaml           |   4 +-
 packages/bash/tool-pwsh/README.md                  |   2 +-
 packages/bash/tool-pwsh/README.zh.md               |   2 +-
 packages/bash/tool-pwsh/package.json               |  39 +-
 packages/bash/tool-pwsh/src/index.ts               |  12 +-
 packages/bash/tool-pwsh/src/invariant.ts           |   2 +-
 packages/bash/tool-pwsh/tests/integration.spec.ts  |   2 +-
 packages/bash/tool-pwsh/tests/tools.spec.ts        |  11 +-
 packages/boot/README.i18n.yaml                     |   4 +-
 packages/boot/README.md                            |   5 +-
 packages/boot/README.zh.md                         |   5 +-
 packages/boot/app-boot/README.i18n.yaml            |   4 +-
 packages/boot/app-boot/README.md                   |   8 +-
 packages/boot/app-boot/README.zh.md                |   8 +-
 packages/boot/app-boot/package.json                |  43 +-
 packages/boot/app-boot/src/index.ts                |  72 +-
 packages/boot/app-boot/src/invariant.ts            |   2 +-
 packages/boot/app-boot/src/profile.ts              |   6 +-
 packages/boot/app-boot/tests/app-boot.spec.ts      | 104 ++-
 packages/boot/app-boot/tests/config-dump.spec.ts   |   2 +-
 packages/boot/app-boot/tests/config-reload.spec.ts |   6 +-
 packages/boot/app-boot/tests/hmr-config.spec.ts    |   8 +-
 .../boot/app-boot/tests/repository-cache.spec.ts   | 218 -----
 packages/boot/app-boot/tests/user-patches.spec.ts  | 125 ++-
 packages/boot/app-boot/tsdown.config.ts            |   2 +-
 .../cmdline}/README.i18n.yaml                      |   6 +-
 packages/boot/cmdline/README.md                    |  72 ++
 packages/boot/cmdline/README.zh.md                 |  72 ++
 packages/boot/cmdline/package.json                 |  46 +
 packages/boot/cmdline/src/index.ts                 | 150 ++++
 packages/boot/cmdline/src/invariant.ts             |  30 +
 packages/boot/cmdline/tests/cmdline.spec.ts        | 198 ++++
 .../create-sdk => boot/cmdline}/tsconfig.json      |  11 +-
 packages/bundle/base/README.i18n.yaml              |   4 +-
 packages/bundle/base/README.md                     |   3 +-
 packages/bundle/base/README.zh.md                  |   3 +-
 packages/bundle/base/cordis.patch.yml              |  28 +-
 packages/bundle/base/package.json                  |  24 +-
 packages/bundle/base/src/invariant.ts              |   2 +-
 packages/bundle/base/tests/base.spec.ts            |  13 +-
 packages/bundle/headless/README.i18n.yaml          |   4 +-
 packages/bundle/headless/README.md                 |   6 +-
 packages/bundle/headless/README.zh.md              |   6 +-
 packages/bundle/headless/cordis.patch.yml          |  17 +-
 packages/bundle/headless/package.json              |  37 +-
 packages/bundle/headless/src/index.ts              |  43 +-
 packages/bundle/headless/src/invariant.ts          |   2 +-
 packages/bundle/headless/src/startup.ts            |  62 ++
 packages/bundle/headless/tests/headless.spec.ts    |  46 +-
 packages/bundle/headless/tests/startup.spec.ts     | 106 +++
 packages/bundle/headless/tsconfig.json             |   3 +
 packages/bundle/web-app/README.i18n.yaml           |   4 +-
 packages/bundle/web-app/README.md                  |  10 +-
 packages/bundle/web-app/README.zh.md               |  10 +-
 packages/bundle/web-app/cordis.patch.yml           |  86 +-
 packages/bundle/web-app/package.json               |  40 +-
 packages/bundle/web-app/src/index.ts               | 120 ++-
 packages/bundle/web-app/src/invariant.ts           |   2 +-
 packages/bundle/web-app/src/startup.ts             |  84 ++
 packages/bundle/web-app/tests/startup.spec.ts      | 131 +++
 .../bundle/web-app/tests/trusted-hosts.spec.ts     |  34 +
 packages/bundle/web-app/tests/web-app.spec.ts      |  70 +-
 packages/bundle/web-app/tsconfig.json              |   9 +
 packages/client/AGENTS.md                          |   4 +-
 packages/client/README.i18n.yaml                   |   4 +-
 packages/client/README.md                          |   4 +
 packages/client/README.zh.md                       |   4 +
 packages/client/connection/README.i18n.yaml        |   4 +-
 packages/client/connection/README.md               |   2 +-
 packages/client/connection/README.zh.md            |   2 +-
 packages/client/connection/package.json            |  21 +-
 packages/client/connection/src/client/api.ts       |   1 +
 .../client/connection/src/client/connection.ts     |  18 +-
 packages/client/connection/src/client/fixture.ts   |  12 +-
 packages/client/connection/src/client/index.ts     |  60 +-
 packages/client/connection/src/index.ts            |   4 +-
 packages/client/connection/src/invariant.ts        |   2 +-
 packages/client/connection/src/rpc-host.ts         |   4 +-
 .../client/connection/tests/client-apply.spec.ts   |  87 +-
 .../client/connection/tests/connection.spec.ts     |  65 +-
 packages/client/connection/tests/fake-api.ts       |  11 +-
 packages/client/connection/tests/node-half.spec.ts |   2 +-
 .../connection/tests/websocket-downlink.spec.ts    |   6 +-
 packages/client/hmr/README.i18n.yaml               |   4 +-
 packages/client/hmr/README.md                      |   2 +-
 packages/client/hmr/README.zh.md                   |   2 +-
 packages/client/hmr/package.json                   |  27 +-
 packages/client/hmr/src/client/index.ts            |   4 +-
 packages/client/hmr/src/index.ts                   |   8 +-
 packages/client/hmr/src/invariant.ts               |   2 +-
 packages/client/hmr/tests/node-half.spec.ts        |   2 +-
 packages/client/locale/package.json                |  35 +-
 packages/client/locale/src/client/LanguageRow.tsx  |   2 +-
 packages/client/locale/src/client/index.ts         |  17 +-
 .../client/locale/src/client/settings-contract.ts  |  26 -
 packages/client/locale/src/index.ts                |   2 +-
 packages/client/locale/src/invariant.ts            |   4 +-
 packages/client/locale/src/locale-settings.ts      |   2 +-
 packages/client/locale/tests/apply.spec.ts         |  13 +-
 packages/client/locale/tests/host.spec.ts          |   2 +-
 packages/client/locale/tests/invariant.spec.ts     |   8 +-
 packages/client/locale/tests/language-row.spec.tsx |   2 +-
 packages/client/locale/tests/locale.spec.ts        |   2 +-
 packages/client/locale/tsconfig.json               |   3 +
 packages/client/modules/README.i18n.yaml           |   2 +-
 packages/client/modules/README.md                  |   2 +-
 packages/client/modules/package.json               |  19 +-
 packages/client/modules/src/client/index.ts        |   2 +-
 packages/client/modules/src/client/manifest.ts     |  22 +-
 packages/client/modules/src/client/system.ts       |  20 +-
 packages/client/modules/src/index.ts               |   8 +-
 packages/client/modules/src/invariant.ts           |   2 +-
 packages/client/modules/tests/loader.spec.ts       |  18 +-
 packages/client/modules/tests/node-half.spec.ts    |   2 +-
 packages/client/runtime/README.i18n.yaml           |   4 +-
 packages/client/runtime/README.md                  |  18 +-
 packages/client/runtime/README.zh.md               |  18 +-
 packages/client/runtime/package.json               |  31 +-
 packages/client/runtime/src/client/agents/scope.ts |   4 +-
 .../runtime/src/client/contract/conversation.ts    |  21 +-
 .../runtime/src/client/contract/session-history.ts |  43 -
 .../client/runtime/src/client/contract/sessions.ts |   2 +-
 .../runtime/src/client/contract/settings-scope.ts  |  81 ++
 .../client/runtime/src/client/contract/store.ts    |   4 +-
 .../src/client/conversation/definition-registry.ts |   2 +-
 .../src/client/conversation/event-registry.ts      |  13 +-
 .../src/client/conversation/view-registry.ts       |   2 +-
 packages/client/runtime/src/client/index.ts        | 112 +--
 .../src/client/session-history/history-fold.ts     | 428 ---------
 .../runtime/src/client/session-history/service.ts  |  66 --
 .../runtime/src/client/session-history/source.ts   | 432 ---------
 .../src/client/sessions/conversation-assembler.ts  |  57 +-
 .../runtime/src/client/sessions/conversation.ts    |  14 +-
 .../client/runtime/src/client/sessions/history.ts  | 121 ---
 .../client/runtime/src/client/sessions/manager.ts  |  40 +-
 .../src/client/sessions/request-inspection.ts      | 328 +------
 .../client/runtime/src/client/sessions/service.ts  |  16 +-
 .../client/runtime/src/client/sessions/session.ts  |  26 +-
 packages/client/runtime/src/client/slots.ts        |   4 +-
 packages/client/runtime/src/client/time-zone.ts    |  14 +
 .../runtime/src/client/workspaces/service.ts       |   2 +-
 packages/client/runtime/src/invariant.ts           |   2 +-
 packages/client/runtime/tests/client-apply.spec.ts |  11 +-
 .../runtime/tests/conversation-assembler.spec.ts   | 114 ++-
 .../runtime/tests/conversation-registry.spec.ts    |  37 +-
 packages/client/runtime/tests/fake-api.ts          |  11 +-
 packages/client/runtime/tests/history-fold.spec.ts | 232 -----
 packages/client/runtime/tests/invariant.spec.ts    |   2 +-
 packages/client/runtime/tests/manager.spec.ts      |  58 ++
 .../runtime/tests/request-inspection.spec.ts       | 319 -------
 packages/client/runtime/tests/scope.spec.ts        |   4 +-
 .../runtime/tests/session-history-source.spec.ts   | 180 ----
 packages/client/runtime/tests/session.spec.ts      |  38 +-
 .../client/runtime/tests/sessions-service.spec.ts  |  19 +-
 .../client/runtime/tests/slots-service.spec.ts     |   2 +-
 packages/client/runtime/tests/time-zone.spec.ts    |  24 +
 packages/client/runtime/tests/wire-events.spec.ts  | 116 ++-
 .../runtime/tests/workspaces-service.spec.ts       |   2 +-
 packages/client/runtime/tsconfig.json              |   6 +-
 packages/client/schema-form/package.json           |  19 +-
 packages/client/schema-form/src/invariant.ts       |   2 +-
 packages/client/schema-form/src/model.ts           |   2 +-
 .../client/schema-form/tests/invariant.spec.ts     |   2 +-
 packages/client/schema-form/tests/model.spec.ts    |   2 +-
 packages/client/test-runtime/package.json          |  25 +-
 packages/client/test-runtime/src/fixtures.ts       |   5 +-
 packages/client/test-runtime/src/index.ts          |   5 +-
 packages/client/test-runtime/src/invariant.ts      |   2 +-
 packages/client/test-runtime/src/remote.ts         |  66 ++
 packages/client/test-runtime/src/sessions.ts       |   4 +-
 packages/client/test-runtime/src/settings-scope.ts |   8 +-
 .../client/test-runtime/tests/invariant.spec.ts    |   2 +-
 packages/client/test-runtime/tests/remote.spec.ts  |  43 +
 .../client/test-runtime/tests/runtime.spec.tsx     |  30 +
 packages/client/tsdown.client.ts                   |  11 +-
 packages/client/ui-agent-preset/README.i18n.yaml   |   4 +-
 packages/client/ui-agent-preset/README.md          |   6 +-
 packages/client/ui-agent-preset/README.zh.md       |   6 +-
 packages/client/ui-agent-preset/package.json       |  38 +-
 .../src/client/AgentPresetLabel.module.css         |   2 +-
 .../src/client/AgentPresetLabel.tsx                |   4 +-
 .../src/client/AgentPresetSeat.module.css          |  57 +-
 .../ui-agent-preset/src/client/AgentPresetSeat.tsx |  79 +-
 .../src/client/AgentPresetSection.module.css       |  33 +-
 .../src/client/AgentPresetSection.tsx              | 276 +++---
 .../client/ui-agent-preset/src/client/index.ts     |  30 +-
 .../client/ui-agent-preset/src/client/locales.ts   |  12 +-
 .../ui-agent-preset/src/client/seat-store.ts       |  20 +-
 .../ui-agent-preset/src/client/section-store.ts    |   7 +-
 packages/client/ui-agent-preset/src/invariant.ts   |   2 +-
 .../client/ui-agent-preset/tests/apply.spec.ts     |  54 +-
 .../ui-agent-preset/tests/components.spec.tsx      |  95 +-
 .../client/ui-agent-preset/tests/invariant.spec.ts |   2 +-
 .../client/ui-agent-preset/tests/section.spec.tsx  |  83 +-
 .../ui-agent-preset/tests/settings-store.spec.ts   |   2 +-
 packages/client/ui-agent-preset/tsconfig.json      |   3 +
 .../ui-attachment}/README.i18n.yaml                |   6 +-
 packages/client/ui-attachment/README.md            |  27 +
 packages/client/ui-attachment/README.zh.md         |  27 +
 packages/client/ui-attachment/package.json         |  51 ++
 .../ui-attachment/src/AttachmentRail.module.css    | 118 +++
 .../client/ui-attachment/src/AttachmentRail.tsx    | 200 +++++
 .../src}/ImageLightbox.module.css                  |   0
 .../client/ui-attachment/src/ImageLightbox.tsx     |  61 ++
 .../src}/MessageImage.module.css                   |   2 +-
 packages/client/ui-attachment/src/MessageImage.tsx |  95 ++
 packages/client/ui-attachment/src/css-modules.d.ts |   6 +
 packages/client/ui-attachment/src/index.ts         |  14 +
 .../ui-attachment}/src/invariant.ts                |  15 +-
 .../ui-attachment/tests/attachment-rail.spec.tsx   | 173 ++++
 .../ui-attachment/tests/image-lightbox.spec.tsx    |  50 ++
 .../client/ui-attachment/tests/invariant.spec.ts   |  12 +
 .../ui-attachment/tests/message-image.spec.tsx     | 103 +++
 packages/client/ui-attachment/tsconfig.json        |  21 +
 packages/client/ui-attachment/tsdown.config.ts     |  35 +
 packages/client/ui-command/README.i18n.yaml        |   4 +-
 packages/client/ui-command/README.md               |   2 +-
 packages/client/ui-command/README.zh.md            |   2 +-
 packages/client/ui-command/package.json            |  36 +-
 packages/client/ui-command/src/client/index.ts     |   4 +-
 packages/client/ui-command/src/client/service.ts   |  13 +-
 packages/client/ui-command/src/invariant.ts        |   2 +-
 .../client/ui-command/tests/browser-plugin.spec.ts |   7 +-
 packages/client/ui-command/tests/service.spec.ts   |  14 +-
 packages/client/ui-command/tsconfig.json           |   3 +
 packages/client/ui-conversation/README.i18n.yaml   |   4 +-
 packages/client/ui-conversation/README.md          |   6 +-
 packages/client/ui-conversation/README.zh.md       |   4 +-
 packages/client/ui-conversation/package.json       |  65 +-
 .../client/ui-conversation/src/client/apply.ts     |  11 +-
 .../src/client/chat/AssistantMarkdown.tsx          |   5 +-
 .../src/client/chat/MessageImage.tsx               |  72 --
 .../src/client/chat/MessageItem.tsx                |   5 +-
 .../src/client/chat/register-node-renderers.ts     |   2 +-
 .../ui-conversation/src/client/contract/slots.ts   |  16 +-
 .../src/client/conversation-nodes/assistant.ts     |   6 +-
 .../conversation-nodes/chat-snapshot-builder.ts    |   2 +-
 .../src/client/conversation-nodes/command.ts       |   6 +-
 .../src/client/conversation-nodes/compaction.ts    |   6 +-
 .../src/client/conversation-nodes/fallback.ts      |   5 +-
 .../src/client/conversation-nodes/inbox.ts         |   3 +-
 .../src/client/conversation-nodes/message.ts       |   7 +-
 .../src/client/conversation-nodes/register.ts      |   2 +-
 .../src/client/conversation-nodes/retry.ts         |   7 +-
 .../src/client/conversation-nodes/tool.ts          |   6 +-
 .../src/client/conversation-nodes/turn-error.ts    |   6 +-
 .../src/client/conversation-nodes/turn-tail.ts     |   6 +-
 .../ui-conversation/src/client/image-labels.ts     |  48 +
 .../client/ui-conversation/src/client/index.ts     |   2 +-
 .../client/ui-conversation/src/client/locales.ts   |  14 +-
 .../ui-conversation/src/client/queue/QueueDock.tsx |   2 +-
 .../client/ui-conversation/src/client/service.ts   |   6 +-
 .../client/skeleton/ConversationRoot.module.css    |   7 +-
 .../src/client/skeleton/ConversationRoot.tsx       |   9 +-
 .../src/client/skeleton/HeroShell.module.css       |   2 +-
 .../src/client/skeleton/ImageLightbox.tsx          |  40 -
 .../src/client/skeleton/InputBar.module.css        | 111 +--
 .../src/client/skeleton/InputBar.tsx               | 158 ++--
 .../client/skeleton/PermissionSelect.module.css    |   3 +
 .../src/client/skeleton/TodoPanel.tsx              |   2 +-
 packages/client/ui-conversation/src/index.ts       |   2 +-
 packages/client/ui-conversation/src/invariant.ts   |   2 +-
 .../ui-conversation/src/submission-settings.ts     |   2 +-
 .../ui-conversation/tests/apply-inject.spec.tsx    |  69 +-
 .../tests/assembly-surfaces.spec.tsx               |  30 +-
 .../ui-conversation/tests/chat-apply.spec.tsx      |   5 +-
 .../ui-conversation/tests/chat-stats.spec.tsx      |   3 +-
 .../ui-conversation/tests/chat-view.spec.tsx       |   9 +-
 .../ui-conversation/tests/coverage-tails.spec.tsx  |   2 +-
 .../tests/enter-behavior-row.spec.tsx              |   2 +-
 .../tests/gate-branch-tails.spec.tsx               |  10 +-
 packages/client/ui-conversation/tests/host.spec.ts |   2 +-
 .../ui-conversation/tests/image-labels.spec.tsx    |  82 ++
 .../ui-conversation/tests/input-bar.spec.tsx       | 103 ++-
 .../ui-conversation/tests/input-matrix.spec.tsx    |   8 +-
 .../ui-conversation/tests/input-scenarios.spec.tsx |  10 +-
 .../ui-conversation/tests/message-image.spec.tsx   |  81 --
 .../ui-conversation/tests/queue-dock.spec.tsx      |   6 +-
 .../tests/service-orchestration.spec.ts            |   2 +-
 .../client/ui-conversation/tests/skeleton.spec.tsx |  22 +-
 .../tests/views-type-chain.spec.tsx                |   2 +-
 packages/client/ui-conversation/tsconfig.json      |   6 +
 packages/client/ui-deliverables/README.i18n.yaml   |   4 +-
 packages/client/ui-deliverables/README.md          |   3 +-
 packages/client/ui-deliverables/README.zh.md       |   3 +-
 packages/client/ui-deliverables/package.json       |  28 +-
 .../src/client/ProducedFiles.module.css            |  75 +-
 .../ui-deliverables/src/client/ProducedFiles.tsx   | 149 ++-
 .../client/ui-deliverables/src/client/index.ts     |   8 +-
 .../client/ui-deliverables/src/client/locales.ts   |   8 +-
 .../src/client/turn-deliverables.ts                |   1 -
 packages/client/ui-deliverables/src/invariant.ts   |   2 +-
 .../ui-deliverables/tests/produced-files.spec.tsx  | 169 +++-
 packages/client/ui-goal/README.i18n.yaml           |   4 +-
 packages/client/ui-goal/README.md                  |   4 +-
 packages/client/ui-goal/README.zh.md               |   2 +
 packages/client/ui-goal/package.json               |  33 +-
 .../src/client/GoalCommandInputView.module.css     |  25 +
 .../ui-goal/src/client/GoalCommandInputView.tsx    |  30 +
 .../ui-goal/src/client/goal-command-input.ts       |  71 ++
 packages/client/ui-goal/src/client/index.ts        |  13 +-
 packages/client/ui-goal/src/client/locales.ts      |   2 +
 packages/client/ui-goal/src/invariant.ts           |   2 +-
 .../client/ui-goal/tests/browser-plugin.spec.tsx   |  20 +-
 .../ui-goal/tests/goal-command-input.spec.tsx      | 134 +++
 packages/client/ui-goal/tsconfig.json              |   3 +
 packages/client/ui-layout/README.i18n.yaml         |   2 +-
 packages/client/ui-layout/README.md                |   2 +-
 packages/client/ui-layout/package.json             |  23 +-
 packages/client/ui-layout/src/client/index.ts      |   6 +-
 packages/client/ui-layout/src/invariant.ts         |   2 +-
 packages/client/ui-layout/tests/apply.spec.ts      |  10 +-
 packages/client/ui-model/README.i18n.yaml          |   4 +-
 packages/client/ui-model/README.md                 |   4 +-
 packages/client/ui-model/README.zh.md              |   2 +
 packages/client/ui-model/package.json              |  39 +-
 .../client/ui-model/src/client/ModelSelect.tsx     |  65 +-
 packages/client/ui-model/src/client/index.ts       |   4 +-
 packages/client/ui-model/src/client/service.ts     |  19 +-
 packages/client/ui-model/src/invariant.ts          |   2 +-
 .../client/ui-model/tests/browser-plugin.spec.ts   |   8 +-
 .../client/ui-model/tests/model-select.spec.tsx    |  32 +
 packages/client/ui-model/tsconfig.json             |   3 +
 packages/client/ui-models/README.i18n.yaml         |   4 +-
 packages/client/ui-models/README.md                |   6 +-
 packages/client/ui-models/README.zh.md             |   6 +-
 packages/client/ui-models/package.json             |  34 +-
 .../ui-models/src/client/CustomProviderCard.tsx    |   2 +-
 .../client/ui-models/src/client/ModelsSection.tsx  |  28 +-
 .../client/ui-models/src/client/ProviderEditor.tsx |  85 +-
 packages/client/ui-models/src/client/index.ts      |  11 +-
 packages/client/ui-models/src/client/locales.ts    |   2 +
 packages/client/ui-models/src/invariant.ts         |   2 +-
 packages/client/ui-models/tests/apply.spec.ts      |  17 +-
 .../client/ui-models/tests/components.spec.tsx     |   2 +-
 packages/client/ui-models/tests/invariant.spec.ts  |   2 +-
 .../client/ui-models/tests/provider-form.spec.tsx  | 153 +++-
 packages/client/ui-models/tests/styles.spec.ts     |  23 +
 packages/client/ui-models/tsconfig.json            |   3 +
 packages/client/ui-permission/README.i18n.yaml     |   2 +-
 packages/client/ui-permission/README.md            |   2 +-
 packages/client/ui-permission/package.json         |  44 +-
 packages/client/ui-permission/src/client/index.ts  |  17 +-
 packages/client/ui-permission/src/invariant.ts     |   2 +-
 .../ui-permission/tests/browser-plugin.spec.ts     |  10 +-
 packages/client/ui-permission/tsconfig.json        |   6 +
 packages/client/ui-plan/package.json               |  31 +-
 packages/client/ui-plan/src/invariant.ts           |   2 +-
 .../client/ui-plan/tests/browser-plugin.spec.ts    |   2 +-
 packages/client/ui-plugin-config/README.i18n.yaml  |   6 +
 packages/client/ui-plugin-config/README.md         |  40 +
 packages/client/ui-plugin-config/README.zh.md      |  40 +
 packages/client/ui-plugin-config/package.json      |  86 ++
 .../ui-plugin-config/src/client/AgentLoopCard.tsx  |  47 +
 .../ui-plugin-config/src/client/BashCard.tsx       |  61 ++
 .../src/client/PluginCard.module.css               | 157 ++++
 .../ui-plugin-config/src/client/PluginCard.tsx     |  98 ++
 .../src/client/PluginConfigSection.module.css      |  36 +
 .../src/client/PluginConfigSection.tsx             |  49 +
 .../ui-plugin-config/src/client/WebSearchCard.tsx  |  78 ++
 .../src/client/agent-loop-store.ts                 |  57 ++
 .../ui-plugin-config/src/client/bash-store.ts      |  63 ++
 .../ui-plugin-config/src/client/card-store.ts      | 351 ++++++++
 .../ui-plugin-config/src/client/fields.module.css  | 113 +++
 .../client/ui-plugin-config/src/client/fields.tsx  | 123 +++
 .../client/ui-plugin-config/src/client/index.ts    | 110 +++
 .../client/ui-plugin-config/src/client/locales.ts  |  91 ++
 .../ui-plugin-config/src/client/slot-contract.ts   |  24 +
 .../src/client/web-search-store.ts                 | 192 ++++
 .../client/ui-plugin-config/src/css-modules.d.ts   |   4 +
 packages/client/ui-plugin-config/src/index.ts      |  11 +
 packages/client/ui-plugin-config/src/invariant.ts  |  31 +
 .../client/ui-plugin-config/tests/apply.spec.ts    | 134 +++
 .../client/ui-plugin-config/tests/fields.spec.tsx  | 156 ++++
 .../ui-plugin-config/tests/invariant.spec.ts       |  25 +
 .../client/ui-plugin-config/tests/section.spec.tsx | 325 +++++++
 .../client/ui-plugin-config/tests/stores.spec.ts   | 540 +++++++++++
 packages/client/ui-plugin-config/tsconfig.json     |  45 +
 packages/client/ui-plugin-config/tsdown.config.ts  |   3 +
 packages/client/ui-primitives/README.i18n.yaml     |   4 +-
 packages/client/ui-primitives/README.md            |   6 +-
 packages/client/ui-primitives/README.zh.md         |   6 +-
 packages/client/ui-primitives/package.json         |  17 +-
 packages/client/ui-primitives/src/Toast.module.css |  70 ++
 packages/client/ui-primitives/src/Toast.tsx        |  59 ++
 packages/client/ui-primitives/src/Tooltip.tsx      |  78 +-
 packages/client/ui-primitives/src/icons/index.tsx  |  29 +
 packages/client/ui-primitives/src/index.ts         |   1 +
 packages/client/ui-primitives/src/invariant.ts     |   4 +-
 packages/client/ui-primitives/tests/icons.spec.tsx |   4 +-
 .../client/ui-primitives/tests/invariant.spec.ts   |   2 +-
 packages/client/ui-primitives/tests/toast.spec.tsx |  57 ++
 .../client/ui-primitives/tests/tooltip.spec.tsx    | 126 ++-
 packages/client/ui-question/package.json           |  19 +-
 packages/client/ui-question/src/invariant.ts       |   2 +-
 .../ui-question/tests/browser-plugin.spec.ts       |   2 +-
 .../client/ui-question/tests/node-plugin.spec.ts   |   2 +-
 .../client/ui-settings-general/README.i18n.yaml    |   4 +-
 packages/client/ui-settings-general/README.md      |   6 +-
 packages/client/ui-settings-general/README.zh.md   |   6 +-
 packages/client/ui-settings-general/package.json   |  42 +-
 .../src/client/SettingsRoot.module.css             |   4 +-
 .../src/client/SettingsRoot.tsx                    |  10 +-
 .../client/ui-settings-general/src/client/index.ts | 107 ++-
 .../src/client/shell-contract.ts                   |  59 ++
 packages/client/ui-settings-general/src/index.ts   |   4 +-
 .../client/ui-settings-general/src/invariant.ts    |   2 +-
 .../client/ui-settings-general/tests/apply.spec.ts |  13 +-
 .../client/ui-settings-general/tests/host.spec.ts  |   2 +-
 .../ui-settings-general/tests/invariant.spec.ts    |   2 +-
 .../tests/settings-root.spec.tsx                   |  26 +-
 .../tests/shell.spec.ts}                           |  32 +-
 packages/client/ui-settings-general/tsconfig.json  |   6 +
 packages/client/ui-settings/README.i18n.yaml       |   4 +-
 packages/client/ui-settings/README.md              |   9 +-
 packages/client/ui-settings/README.zh.md           |   9 +-
 packages/client/ui-settings/package.json           |  51 +-
 .../ui-settings/src/client/contract/slots.ts       |  81 +-
 packages/client/ui-settings/src/client/index.ts    | 116 +--
 .../src/client/settings-scope.ts                   | 193 ++--
 packages/client/ui-settings/src/index.ts           |   2 +-
 packages/client/ui-settings/src/invariant.ts       |   2 +-
 .../client/ui-settings/tests/invariant.spec.ts     |   2 +-
 packages/client/ui-settings/tests/plugin.spec.ts   |  29 +
 .../tests/settings-scope.spec.ts                   | 102 ++-
 packages/client/ui-settings/tsconfig.json          |  13 +-
 packages/client/ui-sidebar/README.i18n.yaml        |   2 +-
 packages/client/ui-sidebar/README.md               |   2 +-
 packages/client/ui-sidebar/package.json            |  25 +-
 .../ui-sidebar/src/client/SidebarRoot.module.css   |   8 +-
 packages/client/ui-sidebar/src/invariant.ts        |   2 +-
 packages/client/ui-sidebar/tests/apply.spec.tsx    |   2 +-
 packages/client/ui-sidebar/tests/invariant.spec.ts |   2 +-
 packages/client/ui-skill/README.i18n.yaml          |   4 +-
 packages/client/ui-skill/README.md                 |   4 +-
 packages/client/ui-skill/README.zh.md              |   2 +-
 packages/client/ui-skill/package.json              |  36 +-
 packages/client/ui-skill/src/client/index.ts       |   6 +-
 packages/client/ui-skill/src/invariant.ts          |   2 +-
 .../client/ui-skill/tests/browser-plugin.spec.ts   |  12 +-
 packages/client/ui-skill/tsconfig.json             |   3 +
 packages/client/ui-slash/README.i18n.yaml          |   2 +-
 packages/client/ui-slash/README.md                 |   2 +-
 packages/client/ui-slash/package.json              |  25 +-
 packages/client/ui-slash/src/client/index.ts       |   2 +-
 packages/client/ui-slash/src/client/service.ts     |   4 +-
 packages/client/ui-slash/src/invariant.ts          |   2 +-
 packages/client/ui-slash/src/types.ts              |   2 +-
 packages/client/ui-slash/tests/apply.spec.ts       |   2 +-
 packages/client/ui-slash/tests/service.spec.ts     |   2 +-
 packages/client/ui-slots/package.json              |  17 +-
 packages/client/ui-slots/src/invariant.ts          |   2 +-
 packages/client/ui-slots/src/renderer.ts           |   8 +-
 packages/client/ui-slots/tests/core.spec.ts        |   4 +-
 .../{surface.spec.ts => dynamic-keys.spec.ts}      |  22 +-
 packages/client/ui-slots/tests/invariant.spec.ts   |   2 +-
 packages/client/ui-slots/tests/type-chain.spec.tsx |   2 +-
 packages/client/ui-subagent/package.json           |  33 +-
 .../src/client/SubagentCatalogAction.module.css    |   1 -
 .../src/client/SubagentCatalogAction.tsx           |   8 +-
 packages/client/ui-subagent/src/invariant.ts       |   2 +-
 .../ui-subagent/tests/browser-plugin.spec.ts       |   9 +-
 .../ui-subagent/tests/conversation-ui.spec.tsx     |  18 +-
 .../helper => client/ui-task}/README.i18n.yaml     |   6 +-
 packages/client/ui-task/README.md                  |  24 +
 packages/client/ui-task/README.zh.md               |  24 +
 packages/client/ui-task/package.json               |  77 ++
 .../ui-task/src/client/TaskListAction.module.css   | 125 +++
 .../client/ui-task/src/client/TaskListAction.tsx   | 192 ++++
 packages/client/ui-task/src/client/index.ts        |  40 +
 packages/client/ui-task/src/client/locales.ts      |  45 +
 packages/client/ui-task/src/css-modules.d.ts       |   6 +
 packages/client/ui-task/src/index.ts               |   9 +
 .../helper => client/ui-task}/src/invariant.ts     |  16 +-
 .../client/ui-task/tests/browser-plugin.spec.ts    |  95 ++
 .../client/ui-task/tests/task-list-action.spec.tsx | 239 +++++
 .../ui-task}/tsconfig.json                         |  14 +-
 packages/client/ui-task/tsdown.config.ts           |   3 +
 packages/client/ui-theme/README.i18n.yaml          |   4 +-
 packages/client/ui-theme/README.md                 |   4 +-
 packages/client/ui-theme/README.zh.md              |   2 +
 packages/client/ui-theme/package.json              |  41 +-
 packages/client/ui-theme/src/boot-theme.ts         |  40 +
 .../client/ui-theme/src/client/AppearanceRow.tsx   |   2 +-
 packages/client/ui-theme/src/client/index.ts       |  21 +-
 .../ui-theme/src/client/settings-contract.ts       |   9 -
 packages/client/ui-theme/src/index.ts              |  36 +-
 packages/client/ui-theme/src/invariant.ts          |   2 +-
 packages/client/ui-theme/src/theme-settings.ts     |   2 +-
 .../client/ui-theme/tests/appearance-row.spec.tsx  |   2 +-
 packages/client/ui-theme/tests/apply.spec.ts       |  14 +-
 packages/client/ui-theme/tests/boot-theme.spec.ts  |  71 ++
 packages/client/ui-theme/tests/host.spec.ts        |  37 +-
 packages/client/ui-theme/tests/invariant.spec.ts   |  10 +-
 packages/client/ui-theme/tests/theme.spec.ts       |   2 +-
 packages/client/ui-theme/tsconfig.json             |   6 +
 packages/client/ui-tool/package.json               |  27 +-
 .../src/client/tool/toolviews/ask-question-row.tsx |   2 +-
 .../src/client/tool/toolviews/bash-sample.tsx      |   2 +-
 .../client/tool/toolviews/file-mutation-row.tsx    |   2 +-
 .../ui-tool/src/client/tool/toolviews/read-row.tsx |   2 +-
 .../src/client/tool/toolviews/search-row.tsx       |   2 +-
 .../ui-tool/src/client/tool/toolviews/todo-row.tsx |   2 +-
 .../ui-tool/src/client/tool/toolviews/web-row.tsx  |   2 +-
 packages/client/ui-tool/src/invariant.ts           |   2 +-
 .../ui-tool/tests/assembly-surfaces.spec.tsx       |   5 +-
 .../ui-tool/tests/chat-code-subcalls.spec.tsx      |  14 +-
 .../client/ui-tool/tests/coverage-tails.spec.tsx   |   2 +-
 packages/client/ui-tool/tests/diff-card.spec.tsx   |  13 +-
 packages/client/ui-tool/tests/read-card.spec.tsx   |  15 +-
 packages/client/ui-tool/tests/search-card.spec.tsx |   9 +-
 .../client/ui-tool/tests/terminal-card.spec.tsx    |  15 +-
 .../client/ui-tool/tests/toolview-slot.spec.tsx    |   8 +-
 packages/client/ui-tool/tests/web-card.spec.tsx    |  11 +-
 packages/client/ui-trajectory/README.i18n.yaml     |   4 +-
 packages/client/ui-trajectory/README.md            |   2 +-
 packages/client/ui-trajectory/README.zh.md         |   2 +-
 packages/client/ui-trajectory/package.json         |  31 +-
 .../ui-trajectory/src/client/TrajectoryTable.tsx   | 593 ++++++------
 .../src/client/TrajectoryTimeline.tsx              |   2 +-
 .../src/client/TrajectoryToolbar.module.css        |  40 +
 .../ui-trajectory/src/client/TrajectoryToolbar.tsx |  54 +-
 .../ui-trajectory/src/client/TrajectoryView.tsx    | 260 +++---
 .../ui-trajectory/src/client/context-branches.ts   | 122 ---
 .../client/ui-trajectory/src/client/export-log.ts  |  45 +
 packages/client/ui-trajectory/src/client/index.ts  |  45 +-
 packages/client/ui-trajectory/src/client/layout.ts | 212 +++--
 .../client/ui-trajectory/src/client/locales.ts     |  76 ++
 .../src/client/trajectory-assistant-definition.ts  | 405 +++++++++
 .../src/client/trajectory-compaction-definition.ts | 141 +++
 .../src/client/trajectory-contract.ts              |  75 ++
 .../src/client/trajectory-definition-common.ts     |  28 +
 .../src/client/trajectory-message-definitions.ts   | 122 +++
 .../ui-trajectory/src/client/trajectory-preview.ts |  20 +
 .../ui-trajectory/src/client/trajectory-record.ts  |   9 +-
 .../client/trajectory-request-header-definition.ts |  80 ++
 .../src/client/trajectory-search-index.ts          | 133 +++
 .../src/client/trajectory-snapshot-builder.ts      | 284 ++++++
 .../src/client/trajectory-tool-definition.ts       | 273 ++++++
 .../ui-trajectory/src/client/views.module.css      |  12 +
 packages/client/ui-trajectory/src/invariant.ts     |   2 +-
 .../ui-trajectory/tests/client-bundle.spec.ts      |  43 +-
 .../ui-trajectory/tests/context-branches.spec.ts   | 102 ---
 .../tests/conversation-definitions.spec.ts         | 287 ++++++
 .../client/ui-trajectory/tests/export-log.spec.ts  |  51 ++
 .../client/ui-trajectory/tests/layout.spec.tsx     | 151 +++-
 .../ui-trajectory/tests/snapshot-builder.spec.ts   | 237 +++++
 packages/client/ui-trajectory/tests/table.spec.tsx |  37 +
 .../client/ui-trajectory/tests/toolbar.spec.tsx    |  61 ++
 packages/client/ui-trajectory/tests/views.spec.tsx | 384 ++++----
 packages/client/ui-trajectory/tsconfig.json        |  12 +
 packages/client/ui-workflow-run/README.i18n.yaml   |   6 +
 packages/client/ui-workflow-run/README.md          |  35 +
 packages/client/ui-workflow-run/README.zh.md       |  35 +
 packages/client/ui-workflow-run/package.json       |  82 ++
 .../src/client/WorkflowRunPanel.module.css         | 256 ++++++
 .../src/client/WorkflowRunPanel.tsx                | 245 +++++
 .../client/ui-workflow-run/src/client/index.ts     |  32 +
 .../client/ui-workflow-run/src/client/locales.ts   |  51 ++
 .../src/client/workflow-definition.ts              | 193 ++++
 .../client/ui-workflow-run/src/css-modules.d.ts    |   6 +
 packages/client/ui-workflow-run/src/index.ts       |   4 +
 packages/client/ui-workflow-run/src/invariant.ts   |  24 +
 .../ui-workflow-run/tests/workflow-run.spec.tsx    | 523 +++++++++++
 packages/client/ui-workflow-run/tsconfig.json      |  42 +
 packages/client/ui-workflow-run/tsdown.config.ts   |   3 +
 packages/client/ui-workspace/package.json          |  25 +-
 .../src/client/WorkspaceBrowser.module.css         |   5 +-
 packages/client/ui-workspace/src/invariant.ts      |   2 +-
 packages/client/ui-workspace/tests/apply.spec.ts   |   2 +-
 .../client/ui-workspace/tests/invariant.spec.ts    |   2 +-
 packages/client/ui-workspace/tests/tree.spec.ts    |   2 +-
 .../ui-workspace/tests/workspace-browser.spec.tsx  |   2 +-
 .../ui-workspace/tests/workspace-picker.spec.tsx   |   2 +-
 packages/client/web-react/package.json             |  17 +-
 packages/client/web-react/src/index.ts             |   2 +-
 packages/client/web-react/src/invariant.ts         |   2 +-
 packages/client/web-react/src/session-provider.tsx |   4 +-
 .../tests/scoped-slots-real-core.spec.tsx          |   2 +-
 packages/client/web/README.i18n.yaml               |   2 +-
 packages/client/web/README.md                      |   2 +-
 packages/client/web/package.json                   |  22 +-
 packages/client/web/src/app-shell.ts               |   4 +-
 packages/client/web/src/app.tsx                    |   2 +-
 packages/client/web/src/boot.tsx                   |   4 +-
 packages/client/web/src/invariant.ts               |   2 +-
 packages/client/web/src/loader-status.ts           |   2 +-
 packages/client/web/src/platform.ts                |   3 +-
 packages/client/web/src/seed.ts                    |   8 +-
 packages/client/web/tests/app-shell.spec.tsx       |   2 +-
 packages/client/web/tests/app.spec.tsx             |   2 +-
 packages/client/web/tsconfig.json                  |   3 +
 .../code-runtime-worker/README.i18n.yaml           |   2 +-
 .../code-runtime/code-runtime-worker/README.md     |   4 +-
 .../code-runtime/code-runtime-worker/package.json  |  25 +-
 .../code-runtime-worker/src/bootstrap.ts           |   4 +-
 .../code-runtime/code-runtime-worker/src/index.ts  |   4 +-
 .../code-runtime-worker/src/invariant.ts           |   2 +-
 .../code-runtime-worker/tests/built-lib.e2e.ts     |   2 +-
 .../code-runtime-worker/tests/runtime.spec.ts      |   2 +-
 .../code-runtime/code-runtime/README.i18n.yaml     |   2 +-
 packages/code-runtime/code-runtime/README.md       |   2 +-
 packages/code-runtime/code-runtime/package.json    |  17 +-
 packages/code-runtime/code-runtime/src/index.ts    |   4 +-
 .../code-runtime/code-runtime/src/invariant.ts     |   2 +-
 .../code-runtime/tests/service.spec.ts             |   2 +-
 packages/compact/command-compact/package.json      |  25 +-
 packages/compact/command-compact/src/index.ts      |   2 +-
 packages/compact/command-compact/src/invariant.ts  |   2 +-
 .../command-compact/tests/command-compact.spec.ts  |   4 +-
 .../tests/loader-composition.spec.ts               |   6 +-
 packages/compact/compact-basic/README.i18n.yaml    |   4 +-
 packages/compact/compact-basic/README.md           |   2 +-
 packages/compact/compact-basic/README.zh.md        |   2 +-
 packages/compact/compact-basic/package.json        |  37 +-
 packages/compact/compact-basic/src/index.ts        |   4 +-
 packages/compact/compact-basic/src/invariant.ts    |   2 +-
 packages/compact/compact-basic/src/summarizer.ts   |   2 +-
 .../compact-basic/tests/compact-basic.spec.ts      |   2 +-
 .../compact-basic/tests/compact-loop-repro.spec.ts |   2 +-
 .../compact-basic/tests/loader-composition.spec.ts |   6 +-
 .../compact-basic/tests/manual-compact.spec.ts     |   2 +-
 .../compact-tool-result-prune/README.i18n.yaml     |   4 +-
 .../compact/compact-tool-result-prune/README.md    |   2 +-
 .../compact/compact-tool-result-prune/README.zh.md |   2 +-
 .../compact/compact-tool-result-prune/package.json |  31 +-
 .../compact/compact-tool-result-prune/src/index.ts |   6 +-
 .../compact-tool-result-prune/src/invariant.ts     |   2 +-
 .../tests/loader-composition.spec.ts               |   6 +-
 .../tests/tool-result-prune.spec.ts                |   2 +-
 packages/compact/compact/package.json              |  25 +-
 packages/compact/compact/src/index.ts              |   4 +-
 packages/compact/compact/src/invariant.ts          |   2 +-
 packages/compact/compact/tests/compact.spec.ts     |   2 +-
 packages/compact/compact/tests/invariant.spec.ts   |   2 +-
 packages/context/session-reference/package.json    |  31 +-
 packages/context/session-reference/src/index.ts    |   6 +-
 .../context/session-reference/src/invariant.ts     |   2 +-
 .../tests/session-reference.spec.ts                |   2 +-
 packages/context/time-context/README.i18n.yaml     |   4 +-
 packages/context/time-context/README.md            |  39 +-
 packages/context/time-context/README.zh.md         |  39 +-
 packages/context/time-context/package.json         |  23 +-
 packages/context/time-context/src/index.ts         |  78 +-
 packages/context/time-context/src/invariant.ts     | 121 ++-
 packages/context/time-context/src/request-zone.ts  |  79 ++
 packages/context/time-context/src/timestamp.ts     |  37 +
 .../context/time-context/tests/invariant.spec.ts   | 180 +++-
 .../time-context/tests/request-zone.spec.ts        |  57 ++
 .../time-context/tests/time-context.spec.ts        |  53 +-
 packages/context/time-context/tsdown.config.ts     |  25 +
 packages/context/tmux-context/package.json         |  25 +-
 packages/context/tmux-context/src/index.ts         |   4 +-
 packages/context/tmux-context/src/invariant.ts     |   2 +-
 .../tmux-context/tests/tmux-context.spec.ts        |   2 +-
 packages/context/workspace-context/package.json    |  33 +-
 packages/context/workspace-context/src/config.ts   |   2 +-
 packages/context/workspace-context/src/index.ts    |   2 +-
 .../context/workspace-context/src/invariant.ts     |   2 +-
 .../tests/workspace-context.e2e.ts                 |   2 +-
 .../tests/workspace-context.spec.ts                |   8 +-
 packages/core/agent-default-model/README.i18n.yaml |   4 +-
 packages/core/agent-default-model/README.md        |   2 +-
 packages/core/agent-default-model/README.zh.md     |   2 +-
 packages/core/agent-default-model/package.json     |  25 +-
 packages/core/agent-default-model/src/index.ts     |   6 +-
 packages/core/agent-default-model/src/invariant.ts |   2 +-
 .../tests/agent-default-model.spec.ts              |   2 +-
 packages/core/agent-loop/README.i18n.yaml          |   4 +-
 packages/core/agent-loop/README.md                 |   4 +-
 packages/core/agent-loop/README.zh.md              |   2 +-
 packages/core/agent-loop/package.json              |  35 +-
 packages/core/agent-loop/src/agent.ts              |   2 +-
 packages/core/agent-loop/src/index.ts              |  47 +-
 packages/core/agent-loop/src/invariant.ts          |   2 +-
 packages/core/agent-loop/src/runtime-context.ts    |   2 +-
 packages/core/agent-loop/src/tool-calls.ts         |   2 +-
 .../core/agent-loop/tests/agent-initiator.spec.ts  |   2 +-
 packages/core/agent-loop/tests/agent.spec.ts       |   2 +-
 packages/core/agent-loop/tests/cancel.spec.ts      |   2 +-
 .../agent-loop/tests/config-session-id.spec.ts     |  51 +-
 .../agent-loop/tests/contract-regressions.spec.ts  |   2 +-
 .../core/agent-loop/tests/coverage-edges.spec.ts   |   2 +-
 .../core/agent-loop/tests/interception.spec.ts     |   4 +-
 packages/core/agent-loop/tests/invariant.spec.ts   |   2 +-
 packages/core/agent-loop/tests/loop.spec.ts        |   2 +-
 packages/core/agent-loop/tests/properties.spec.ts  |   2 +-
 .../core/agent-loop/tests/request-cache.e2e.ts     |   2 +-
 .../core/agent-loop/tests/request-error.spec.ts    |   2 +-
 .../tests/request-reconstruction.spec.ts           |   2 +-
 packages/core/agent-loop/tests/resume.spec.ts      |   2 +-
 .../core/agent-loop/tests/runtime-context.spec.ts  |   2 +-
 .../core/agent-loop/tests/scope-lifecycle.spec.ts  |   4 +-
 packages/core/agent-loop/tests/settings.spec.ts    | 106 +++
 packages/core/agent-loop/tests/tool-calls.spec.ts  |   2 +-
 packages/core/agent-loop/tests/tool-order.spec.ts  |   2 +-
 packages/core/agent-loop/tsconfig.json             |   3 +
 packages/core/agent-tool-mode/package.json         |  21 +-
 packages/core/agent-tool-mode/src/index.ts         |  14 +-
 packages/core/agent-tool-mode/src/invariant.ts     |   2 +-
 .../agent-tool-mode/tests/agent-tool-mode.spec.ts  |   2 +-
 packages/core/agent/README.i18n.yaml               |   4 +-
 packages/core/agent/README.md                      |   4 +-
 packages/core/agent/README.zh.md                   |   4 +-
 packages/core/agent/package.json                   |  27 +-
 packages/core/agent/src/consumed-work.ts           | 108 +++
 packages/core/agent/src/dispatch.ts                |   2 +-
 packages/core/agent/src/index.ts                   |   9 +-
 packages/core/agent/src/invariant.ts               |   2 +-
 packages/core/agent/src/model-selection.ts         |   2 +-
 packages/core/agent/src/runtime-types.ts           |   4 +-
 packages/core/agent/tests/agent-initiator.spec.ts  |   2 +-
 packages/core/agent/tests/agent.spec.ts            |   2 +-
 packages/core/agent/tests/consumed-work.spec.ts    | 160 ++++
 packages/core/agent/tests/invariant.spec.ts        |   2 +-
 packages/core/agent/tests/model-selection.spec.ts  |   2 +-
 .../core/agent/tests/verify-export-jsdoc.spec.ts   |  18 +-
 packages/core/scope/README.i18n.yaml               |   2 +-
 packages/core/scope/README.md                      |   6 +-
 packages/core/scope/package.json                   |  17 +-
 packages/core/scope/src/index.ts                   |   8 +-
 packages/core/scope/src/invariant.ts               |   2 +-
 packages/core/scope/src/store.ts                   |   2 +-
 packages/core/scope/tests/invariant.spec.ts        |   4 +-
 packages/core/scope/tests/scope.spec.ts            |   4 +-
 packages/core/scope/tests/store.spec.ts            |   2 +-
 packages/core/session/README.i18n.yaml             |   4 +-
 packages/core/session/README.md                    |   5 +-
 packages/core/session/README.zh.md                 |   5 +-
 packages/core/session/package.json                 |  25 +-
 packages/core/session/src/index.ts                 |  30 +-
 packages/core/session/src/invariant.ts             |   2 +-
 packages/core/session/src/known-event-types.ts     |  64 ++
 packages/core/session/src/types.ts                 |  35 +-
 packages/core/session/tests/fork.spec.ts           |   2 +-
 packages/core/session/tests/invariant.spec.ts      |   2 +-
 packages/core/session/tests/scoped.spec.ts         |   2 +-
 packages/core/session/tests/session.spec.ts        |  27 +-
 packages/core/session/tests/typert.spec.ts         |   2 +-
 packages/core/system-prompt/README.i18n.yaml       |   4 +-
 packages/core/system-prompt/README.md              |  12 +-
 packages/core/system-prompt/README.zh.md           |  12 +-
 packages/core/system-prompt/package.json           |  23 +-
 packages/core/system-prompt/src/index.ts           |  47 +-
 packages/core/system-prompt/src/invariant.ts       |   2 +-
 .../core/system-prompt/tests/invariant.spec.ts     |   2 +-
 packages/core/system-prompt/tests/scoped.spec.ts   |   2 +-
 .../core/system-prompt/tests/system-prompt.spec.ts |  30 +-
 .../core/system-prompt/tests/tool-order.spec.ts    |   2 +-
 packages/core/tools/README.i18n.yaml               |   4 +-
 packages/core/tools/README.md                      |   4 +-
 packages/core/tools/README.zh.md                   |   2 +-
 packages/core/tools/package.json                   |  33 +-
 packages/core/tools/src/code-mode.ts               |   4 +-
 packages/core/tools/src/index.ts                   |  30 +-
 packages/core/tools/src/invariant.ts               |   2 +-
 packages/core/tools/src/presentation.ts            |   2 +-
 packages/core/tools/src/schema.ts                  |   2 +-
 packages/core/tools/src/ts-types.ts                |   2 +-
 packages/core/tools/tests/code-mode.spec.ts        |   4 +-
 packages/core/tools/tests/execution-mode.spec.ts   |   2 +-
 .../tools/tests/execution-signal-types.spec.ts     |   2 +-
 packages/core/tools/tests/gen-tool-catalog.spec.ts |   2 +-
 packages/core/tools/tests/invariant.spec.ts        |   2 +-
 packages/core/tools/tests/scoped.spec.ts           |   4 +-
 packages/core/tools/tests/tools.spec.ts            |   2 +-
 .../credentials/credentials-local/package.json     |  27 +-
 .../credentials/credentials-local/src/index.ts     |   4 +-
 .../credentials/credentials-local/src/invariant.ts |   2 +-
 .../credentials-local/tests/drain.spec.ts          |   2 +-
 .../credentials-local/tests/local.spec.ts          |   2 +-
 .../credentials-local/tests/review-fixes.spec.ts   |   2 +-
 .../credentials-local/tests/watcher.spec.ts        |   2 +-
 packages/credentials/credentials/README.i18n.yaml  |   4 +-
 packages/credentials/credentials/README.md         |   4 +-
 packages/credentials/credentials/README.zh.md      |   4 +-
 packages/credentials/credentials/package.json      |  24 +-
 packages/credentials/credentials/src/index.ts      |  25 +-
 packages/credentials/credentials/src/invariant.ts  |   2 +-
 packages/credentials/credentials/src/types.ts      |  31 +
 .../credentials/tests/credentials.spec.ts          |   2 +-
 .../credentials/tests/invariant.spec.ts            |   2 +-
 packages/credentials/credentials/tests/memory.ts   |   2 +-
 packages/e2b/e2b/package.json                      |  19 +-
 packages/e2b/e2b/src/index.ts                      |   6 +-
 packages/e2b/e2b/src/invariant.ts                  |   2 +-
 packages/e2b/e2b/tests/composition.e2e.ts          |   2 +-
 packages/e2b/e2b/tests/e2b.spec.ts                 |   2 +-
 packages/e2b/fs-e2b/README.i18n.yaml               |   4 +-
 packages/e2b/fs-e2b/README.md                      |   1 +
 packages/e2b/fs-e2b/README.zh.md                   |   1 +
 packages/e2b/fs-e2b/package.json                   |  21 +-
 packages/e2b/fs-e2b/src/index.ts                   |  77 +-
 packages/e2b/fs-e2b/src/invariant.ts               |   2 +-
 packages/e2b/fs-e2b/tests/filesystem.spec.ts       |  40 +-
 packages/e2b/subprocess-e2b/package.json           |  25 +-
 packages/e2b/subprocess-e2b/src/index.ts           |   4 +-
 packages/e2b/subprocess-e2b/src/invariant.ts       |   2 +-
 .../e2b/subprocess-e2b/tests/subprocess.spec.ts    |   2 +-
 packages/e2b/subprocess-e2b/tests/terminal.spec.ts |   2 +-
 packages/examples/README.i18n.yaml                 |   4 +-
 packages/examples/README.md                        |   2 +-
 packages/examples/README.zh.md                     |   2 +-
 packages/examples/acp-demo/package.json            |  47 +-
 packages/examples/acp-demo/src/index.ts            |   6 +-
 packages/examples/acp-demo/src/invariant.ts        |   2 +-
 packages/examples/acp-demo/tests/acp-agent.spec.ts |   4 +-
 .../examples/agent-spine-demo/README.i18n.yaml     |   4 +-
 packages/examples/agent-spine-demo/README.md       |   2 +-
 packages/examples/agent-spine-demo/README.zh.md    |   2 +-
 packages/examples/agent-spine-demo/package.json    |  65 +-
 packages/examples/agent-spine-demo/src/index.ts    |   6 +-
 .../examples/agent-spine-demo/src/invariant.ts     |   2 +-
 .../agent-spine-demo/tests/agent-core.spec.ts      |   4 +-
 .../tests/gen-config-catalog.spec.ts               |  70 +-
 .../tests/multi-project-sandbox.e2e.ts             |   2 +-
 packages/examples/jsonrpc-demo/README.i18n.yaml    |   4 +-
 packages/examples/jsonrpc-demo/README.md           |   2 +-
 packages/examples/jsonrpc-demo/README.zh.md        |   2 +-
 packages/examples/jsonrpc-demo/package.json        |  22 +-
 packages/examples/jsonrpc-demo/src/bin.ts          |  49 +-
 packages/examples/jsonrpc-demo/src/index.ts        |   7 +-
 packages/examples/jsonrpc-demo/src/invariant.ts    |   2 +-
 packages/examples/jsonrpc-demo/src/packaged-bin.ts |  12 +
 packages/examples/jsonrpc-demo/src/runner.ts       |  55 ++
 packages/examples/jsonrpc-demo/tsdown.config.ts    |  32 +-
 packages/experimental/AGENTS.md                    |  11 -
 packages/experimental/README.md                    |   7 -
 packages/experimental/README.zh.md                 |   7 -
 packages/feedback/README.i18n.yaml                 |   4 +-
 packages/feedback/README.md                        |   7 +-
 packages/feedback/README.zh.md                     |   7 +-
 .../feedback/command-feedback/README.i18n.yaml     |   4 +-
 packages/feedback/command-feedback/README.md       |  16 +-
 packages/feedback/command-feedback/README.zh.md    |  16 +-
 packages/feedback/command-feedback/package.json    |  29 +-
 packages/feedback/command-feedback/src/index.ts    |  52 +-
 .../feedback/command-feedback/src/invariant.ts     |   2 +-
 .../tests/command-feedback.spec.ts                 |  63 +-
 .../tests/loader-composition.spec.ts               |   8 +-
 packages/feedback/command-feedback/tsconfig.json   |   3 +
 .../feedback/message-feedback/README.i18n.yaml     |   6 +
 packages/feedback/message-feedback/README.md       |  84 ++
 packages/feedback/message-feedback/README.zh.md    |  84 ++
 packages/feedback/message-feedback/package.json    |  82 ++
 packages/feedback/message-feedback/src/index.ts    | 383 ++++++++
 .../feedback/message-feedback/src/invariant.ts     |  27 +
 packages/feedback/message-feedback/src/spec.ts     |  90 ++
 packages/feedback/message-feedback/src/types.ts    | 147 +++
 .../feedback/message-feedback/tests/helpers.ts     | 215 +++++
 .../message-feedback/tests/invariant.spec.ts       |  23 +
 .../tests/loader-composition.spec.ts               | 115 +++
 .../tests/message-feedback.spec.ts                 | 655 ++++++++++++++
 packages/feedback/message-feedback/tsconfig.json   |  45 +
 packages/fs/fs-local/README.i18n.yaml              |   4 +-
 packages/fs/fs-local/README.md                     |   5 +-
 packages/fs/fs-local/README.zh.md                  |   3 +-
 packages/fs/fs-local/package.json                  |  21 +-
 packages/fs/fs-local/src/fsio.ts                   |  46 +
 packages/fs/fs-local/src/index.ts                  |   9 +-
 packages/fs/fs-local/src/invariant.ts              |   2 +-
 packages/fs/fs-local/tests/filesystem.spec.ts      |  39 +-
 packages/fs/fs-policy/README.i18n.yaml             |   4 +-
 packages/fs/fs-policy/README.md                    |   2 +-
 packages/fs/fs-policy/README.zh.md                 |   2 +-
 packages/fs/fs-policy/package.json                 |  21 +-
 packages/fs/fs-policy/src/index.ts                 |   2 +-
 packages/fs/fs-policy/src/invariant.ts             |   2 +-
 packages/fs/fs-policy/tests/policy.spec.ts         |   4 +-
 packages/fs/fs-sandbox/package.json                |  25 +-
 packages/fs/fs-sandbox/src/index.ts                |   2 +-
 packages/fs/fs-sandbox/src/invariant.ts            |   2 +-
 packages/fs/fs-sandbox/tests/fs-sandbox.spec.ts    |   2 +-
 packages/fs/fs/README.i18n.yaml                    |   4 +-
 packages/fs/fs/README.md                           |  11 +-
 packages/fs/fs/README.zh.md                        |  11 +-
 packages/fs/fs/package.json                        |  23 +-
 packages/fs/fs/src/index.ts                        |  16 +-
 packages/fs/fs/src/invariant.ts                    |   2 +-
 packages/fs/fs/src/types.ts                        |   3 +-
 packages/fs/fs/tests/invariant.spec.ts             |   2 +-
 packages/fs/fs/tests/service.spec.ts               |  19 +-
 packages/fs/tool-fs-search/package.json            |  35 +-
 .../src/{surface.ts => direct-call.ts}             |   8 +-
 packages/fs/tool-fs-search/src/glob.ts             |   6 +-
 packages/fs/tool-fs-search/src/grep.ts             |   6 +-
 packages/fs/tool-fs-search/src/index.ts            |   4 +-
 packages/fs/tool-fs-search/src/invariant.ts        |   2 +-
 packages/fs/tool-fs-search/src/search-core.ts      |   4 +-
 .../fs/tool-fs-search/tests/integration.spec.ts    |   2 +-
 packages/fs/tool-fs-search/tests/load-path.spec.ts |   4 +-
 packages/fs/tool-fs-search/tests/rg-path.spec.ts   |   2 +-
 packages/fs/tool-fs-search/tests/tools.spec.ts     |   6 +-
 packages/fs/tool-fs/README.i18n.yaml               |   4 +-
 packages/fs/tool-fs/README.md                      |  38 +-
 packages/fs/tool-fs/README.zh.md                   |  38 +-
 packages/fs/tool-fs/package.json                   |  37 +-
 packages/fs/tool-fs/src/edit.ts                    |   8 +-
 packages/fs/tool-fs/src/index.ts                   |  21 +-
 packages/fs/tool-fs/src/invariant.ts               |   2 +-
 packages/fs/tool-fs/src/read-image.ts              | 231 +++++
 packages/fs/tool-fs/src/read-target.ts             |  32 +
 packages/fs/tool-fs/src/read.ts                    |  14 +-
 packages/fs/tool-fs/src/sandbox.ts                 |   8 +-
 packages/fs/tool-fs/src/write.ts                   |   8 +-
 packages/fs/tool-fs/tests/fs-tools.e2e.ts          |   2 +-
 packages/fs/tool-fs/tests/harness.ts               |   2 +-
 packages/fs/tool-fs/tests/integration.spec.ts      |   2 +-
 packages/fs/tool-fs/tests/read-image.spec.ts       | 499 +++++++++++
 packages/fs/tool-fs/tests/tools.spec.ts            |  15 +-
 packages/fs/tool-fs/tsconfig.json                  |   3 +
 packages/fs/tool-str-replace-editor/package.json   |  27 +-
 packages/fs/tool-str-replace-editor/src/index.ts   |   4 +-
 .../fs/tool-str-replace-editor/src/invariant.ts    |   2 +-
 .../fs/tool-str-replace-editor/tests/tools.spec.ts |   2 +-
 packages/goal/command-goal/README.i18n.yaml        |   2 +-
 packages/goal/command-goal/README.md               |   2 +-
 packages/goal/command-goal/package.json            |  23 +-
 packages/goal/command-goal/src/index.ts            |   2 +-
 packages/goal/command-goal/src/invariant.ts        |   2 +-
 .../goal/command-goal/tests/command-goal.spec.ts   |   4 +-
 packages/goal/goal-session/package.json            |  25 +-
 packages/goal/goal-session/src/index.ts            |   4 +-
 packages/goal/goal-session/src/invariant.ts        |   2 +-
 .../goal/goal-session/tests/goal-session.spec.ts   |   2 +-
 packages/goal/goal-session/tests/invariant.spec.ts |   2 +-
 packages/goal/goal/package.json                    |  33 +-
 packages/goal/goal/src/domain.ts                   |   2 +-
 packages/goal/goal/src/index.ts                    |   6 +-
 packages/goal/goal/src/invariant.ts                |   2 +-
 packages/goal/goal/tests/goal.spec.ts              |   2 +-
 packages/goal/goal/tests/invariant.spec.ts         |   2 +-
 packages/goal/goal/tests/projection.spec.ts        |   2 +-
 packages/goal/tool-goal/README.i18n.yaml           |   4 +-
 packages/goal/tool-goal/README.md                  |   2 +-
 packages/goal/tool-goal/README.zh.md               |   2 +-
 packages/goal/tool-goal/package.json               |  33 +-
 packages/goal/tool-goal/src/authority.ts           |   2 +-
 packages/goal/tool-goal/src/index.ts               |   4 +-
 packages/goal/tool-goal/src/invariant.ts           |   2 +-
 packages/goal/tool-goal/tests/tool-goal.spec.ts    |   4 +-
 packages/guard/repeat-tool-guard/package.json      |  23 +-
 packages/guard/repeat-tool-guard/src/index.ts      |   4 +-
 packages/guard/repeat-tool-guard/src/invariant.ts  |   2 +-
 .../tests/repeat-tool-guard.spec.ts                |   2 +-
 packages/guard/timeout-policy/package.json         |  23 +-
 packages/guard/timeout-policy/src/index.ts         |   2 +-
 packages/guard/timeout-policy/src/invariant.ts     |   2 +-
 .../timeout-policy/tests/timeout-policy.spec.ts    |   4 +-
 packages/hooks/hook-protocol/README.i18n.yaml      |   2 +-
 packages/hooks/hook-protocol/README.md             |   2 +-
 packages/hooks/hook-protocol/package.json          |  21 +-
 packages/hooks/hook-protocol/src/invariant.ts      |   2 +-
 packages/hooks/hook-protocol/src/runner.ts         |   2 +-
 .../hooks/hook-protocol/tests/invariant.spec.ts    |   2 +-
 packages/hooks/hooks-claude/package.json           |  33 +-
 packages/hooks/hooks-claude/src/index.ts           |   4 +-
 packages/hooks/hooks-claude/src/invariant.ts       |   2 +-
 packages/hooks/hooks-claude/tests/bridge.spec.ts   |   4 +-
 .../hooks/hooks-claude/tests/coverage-cases.ts     |   2 +-
 packages/hooks/hooks-codex/package.json            |  31 +-
 packages/hooks/hooks-codex/src/index.ts            |   4 +-
 packages/hooks/hooks-codex/src/invariant.ts        |   2 +-
 packages/hooks/hooks-codex/tests/bridge.spec.ts    |   4 +-
 packages/hooks/hooks-codex/tests/coverage-cases.ts |   2 +-
 packages/host/apiproxy/README.i18n.yaml            |   4 +-
 packages/host/apiproxy/README.md                   |  17 +-
 packages/host/apiproxy/README.zh.md                |  17 +-
 packages/host/apiproxy/package.json                |  23 +-
 packages/host/apiproxy/src/api-proxy.ts            | 385 ++++++--
 packages/host/apiproxy/src/api/downloads.schema.ts |  26 +
 packages/host/apiproxy/src/api/downloads.ts        |  25 +
 packages/host/apiproxy/src/api/events.schema.ts    |  12 +-
 packages/host/apiproxy/src/api/events.ts           |  61 +-
 packages/host/apiproxy/src/api/host.schema.ts      |   1 +
 packages/host/apiproxy/src/api/host.ts             |   2 +
 packages/host/apiproxy/src/api/index.ts            |  12 +-
 packages/host/apiproxy/src/api/llm.ts              |   3 +-
 packages/host/apiproxy/src/api/rpc.schema.ts       |   1 +
 packages/host/apiproxy/src/api/rpc.ts              |   3 +-
 packages/host/apiproxy/src/api/sessions.schema.ts  |   6 +-
 packages/host/apiproxy/src/api/sessions.ts         |  20 +-
 packages/host/apiproxy/src/api/subagents.schema.ts |   1 +
 packages/host/apiproxy/src/api/subagents.ts        |   7 +-
 packages/host/apiproxy/src/api/tasks.schema.ts     |  33 +
 packages/host/apiproxy/src/api/tasks.ts            |  36 +
 packages/host/apiproxy/src/fetch/client.ts         |   2 +-
 packages/host/apiproxy/src/fetch/handler.ts        |  12 +
 packages/host/apiproxy/src/index.ts                |  25 +-
 packages/host/apiproxy/src/invariant.ts            |   2 +-
 packages/host/apiproxy/src/session-export.ts       | 457 ++++++++++
 .../apiproxy/tests/api-proxy-agent-preset.spec.ts  |  45 +-
 .../host/apiproxy/tests/api-proxy-approval.spec.ts |   2 +-
 .../host/apiproxy/tests/api-proxy-blank.spec.ts    |   2 +-
 .../host/apiproxy/tests/api-proxy-cold.spec.ts     |  76 +-
 .../host/apiproxy/tests/api-proxy-commands.spec.ts |  30 +-
 .../host/apiproxy/tests/api-proxy-config.spec.ts   |  93 +-
 .../host/apiproxy/tests/api-proxy-fork.spec.ts     |   2 +-
 .../host/apiproxy/tests/api-proxy-models.spec.ts   |   2 +-
 .../apiproxy/tests/api-proxy-projections.spec.ts   |   2 +-
 .../host/apiproxy/tests/api-proxy-question.spec.ts |   2 +-
 .../host/apiproxy/tests/api-proxy-rename.spec.ts   |   2 +-
 .../host/apiproxy/tests/api-proxy-search.spec.ts   |   2 +-
 .../apiproxy/tests/api-proxy-subagents.spec.ts     |  44 +-
 .../host/apiproxy/tests/api-proxy-tasks.spec.ts    | 263 ++++++
 .../host/apiproxy/tests/api-proxy-view.spec.ts     |   2 +-
 .../apiproxy/tests/api-proxy-workspace.spec.ts     |  15 +-
 .../host/apiproxy/tests/client-handler.spec.ts     |   5 +-
 packages/host/apiproxy/tests/fetch-carrier.spec.ts |  13 +-
 packages/host/apiproxy/tests/rpc-schemas.spec.ts   |  61 +-
 .../host/apiproxy/tests/session-export.spec.ts     | 684 ++++++++++++++
 packages/host/apiproxy/tsconfig.json               |   3 +
 packages/host/directory-picker-auto/package.json   |  29 +-
 packages/host/directory-picker-auto/src/index.ts   |   4 +-
 .../host/directory-picker-auto/src/invariant.ts    |   2 +-
 .../tests/loader-composition.spec.ts               |   6 +-
 packages/host/directory-picker-browse/package.json |  29 +-
 packages/host/directory-picker-browse/src/index.ts |   4 +-
 .../host/directory-picker-browse/src/invariant.ts  |   2 +-
 .../tests/client-flow.spec.tsx                     |   2 +-
 .../directory-picker-browse/tests/service.spec.ts  |   2 +-
 packages/host/directory-picker-native/package.json |  23 +-
 .../host/directory-picker-native/src/invariant.ts  |   2 +-
 .../tests/client-flow.spec.tsx                     |   2 +-
 .../directory-picker-native/tests/service.spec.ts  |   2 +-
 packages/host/directory-picker/package.json        |  17 +-
 packages/host/directory-picker/src/index.ts        |   4 +-
 packages/host/directory-picker/src/invariant.ts    |   2 +-
 packages/host/directory-picker/tests/seam.spec.ts  |   2 +-
 packages/host/frontend-static/package.json         |  23 +-
 packages/host/frontend-static/src/index.ts         |   4 +-
 packages/host/frontend-static/src/invariant.ts     |   2 +-
 .../frontend-static/tests/frontend-static.spec.ts  |   6 +-
 packages/host/webserver/package.json               |  19 +-
 packages/host/webserver/src/index.ts               |   6 +-
 packages/host/webserver/src/invariant.ts           |   2 +-
 packages/host/webserver/tests/webserver.spec.ts    |   6 +-
 packages/interaction/README.i18n.yaml              |   4 +-
 packages/interaction/README.md                     |   2 +-
 packages/interaction/README.zh.md                  |   2 +-
 packages/interaction/commands/README.i18n.yaml     |   4 +-
 packages/interaction/commands/README.md            |   2 +-
 packages/interaction/commands/README.zh.md         |   2 +-
 packages/interaction/commands/package.json         |  27 +-
 packages/interaction/commands/src/index.ts         |  16 +-
 packages/interaction/commands/src/invariant.ts     |   2 +-
 packages/interaction/commands/src/types.ts         |  17 +-
 .../interaction/commands/tests/commands.spec.ts    |   2 +-
 .../interaction/commands/tests/invariant.spec.ts   |   2 +-
 packages/interaction/permission/package.json       |  35 +-
 packages/interaction/permission/src/index.ts       |   6 +-
 packages/interaction/permission/src/invariant.ts   |   2 +-
 .../interaction/permission/tests/invariant.spec.ts |   2 +-
 .../permission/tests/permission.spec.ts            |   2 +-
 .../permission/tests/projection.spec.ts            |   2 +-
 packages/interaction/tool-ask-user/package.json    |  23 +-
 packages/interaction/tool-ask-user/src/index.ts    |   2 +-
 .../interaction/tool-ask-user/src/invariant.ts     |   2 +-
 .../tool-ask-user/tests/tool-ask-user.spec.ts      |   2 +-
 packages/interaction/user-approval/package.json    |  31 +-
 packages/interaction/user-approval/src/index.ts    |   6 +-
 .../interaction/user-approval/src/invariant.ts     |   2 +-
 .../user-approval/tests/approval.spec.ts           |   2 +-
 .../user-approval/tests/invariant.spec.ts          |   2 +-
 packages/interaction/user-interaction/package.json |  21 +-
 packages/interaction/user-interaction/src/index.ts |   6 +-
 .../interaction/user-interaction/src/invariant.ts  |   2 +-
 .../tests/user-interaction.spec.ts                 |   2 +-
 packages/llm/llm-deepseek/README.i18n.yaml         |   4 +-
 packages/llm/llm-deepseek/README.md                |   2 +
 packages/llm/llm-deepseek/README.zh.md             |   2 +
 packages/llm/llm-deepseek/package.json             |  31 +-
 packages/llm/llm-deepseek/src/adapter.ts           |   9 +-
 packages/llm/llm-deepseek/src/index.ts             |   9 +-
 packages/llm/llm-deepseek/src/invariant.ts         |   2 +-
 packages/llm/llm-deepseek/tests/adapter.e2e.ts     |  12 +-
 packages/llm/llm-deepseek/tests/adapter.spec.ts    |  30 +-
 packages/llm/llm-deepseek/tests/assemble.ts        |   2 +-
 .../llm/llm-deepseek/tests/dynamic-config.spec.ts  |   7 +-
 .../llm-deepseek/tests/loader-composition.spec.ts  |   9 +-
 packages/llm/llm-deepseek/tsconfig.json            |   3 +
 packages/llm/llm-pi-ai/README.i18n.yaml            |   2 +-
 packages/llm/llm-pi-ai/README.md                   |   2 +-
 packages/llm/llm-pi-ai/package.json                |  31 +-
 packages/llm/llm-pi-ai/src/config.ts               |   2 +-
 packages/llm/llm-pi-ai/src/index.ts                |   2 +-
 packages/llm/llm-pi-ai/src/invariant.ts            |   2 +-
 packages/llm/llm-pi-ai/tests/adapter.e2e.ts        |   2 +-
 packages/llm/llm-pi-ai/tests/adapter.spec.ts       |   2 +-
 packages/llm/llm-pi-ai/tests/assemble.ts           |   2 +-
 packages/llm/llm-pi-ai/tests/catalog.spec.ts       |   2 +-
 packages/llm/llm-pi-ai/tests/discovery.spec.ts     |   2 +-
 .../llm/llm-pi-ai/tests/dynamic-config.spec.ts     |   2 +-
 .../llm/llm-pi-ai/tests/loader-composition.spec.ts |   6 +-
 packages/llm/llm-pi-ai/tests/provider-apis.e2e.ts  |   2 +-
 packages/llm/llm-retry/package.json                |  33 +-
 packages/llm/llm-retry/src/index.ts                |   4 +-
 packages/llm/llm-retry/src/invariant.ts            |   2 +-
 packages/llm/llm-retry/tests/invariant.spec.ts     |   2 +-
 .../llm/llm-retry/tests/loader-composition.spec.ts |   6 +-
 packages/llm/llm-retry/tests/persistence.spec.ts   |   2 +-
 packages/llm/llm-retry/tests/retry.spec.ts         |   4 +-
 .../llm/llm-retry/tests/transport-recovery.spec.ts |   2 +-
 packages/llm/llm/README.i18n.yaml                  |   2 +-
 packages/llm/llm/README.md                         |   4 +-
 packages/llm/llm/package.json                      |  25 +-
 packages/llm/llm/src/attribution.ts                |   5 +-
 packages/llm/llm/src/index.ts                      |  18 +-
 packages/llm/llm/src/invariant.ts                  |   2 +-
 packages/llm/llm/src/retry-policy.ts               |   2 +-
 packages/llm/llm/src/types.ts                      |  19 +-
 packages/llm/llm/tests/attribution.spec.ts         |   4 +-
 packages/llm/llm/tests/invariant.spec.ts           |   2 +-
 packages/llm/llm/tests/service.spec.ts             |   2 +-
 packages/llm/llm/tests/topology.spec.ts            |   2 +-
 packages/llm/token-meter/package.json              |  27 +-
 packages/llm/token-meter/src/index.ts              |   6 +-
 packages/llm/token-meter/src/invariant.ts          |   2 +-
 .../tests/context-breakdown-projection.spec.ts     |   4 +-
 packages/llm/token-meter/tests/token-meter.spec.ts |   2 +-
 .../tests/token-usage-projection.spec.ts           |   2 +-
 packages/lsp/lsp-local/package.json                |  31 +-
 packages/lsp/lsp-local/src/index.ts                |   4 +-
 packages/lsp/lsp-local/src/invariant.ts            |   2 +-
 packages/lsp/lsp-local/tests/built-lib.e2e.ts      |   2 +-
 packages/lsp/lsp-local/tests/host.spec.ts          |   2 +-
 packages/lsp/lsp-local/tests/instance.spec.ts      |   2 +-
 packages/lsp/lsp-local/tests/lifecycle.spec.ts     |   2 +-
 packages/lsp/lsp-local/tests/provider.spec.ts      |   2 +-
 .../lsp/lsp-local/tests/typescript-server.e2e.ts   |   2 +-
 packages/lsp/lsp/README.i18n.yaml                  |   2 +-
 packages/lsp/lsp/README.md                         |   2 +-
 packages/lsp/lsp/package.json                      |  21 +-
 packages/lsp/lsp/src/index.ts                      |   4 +-
 packages/lsp/lsp/src/invariant.ts                  |   2 +-
 packages/lsp/lsp/tests/lsp.spec.ts                 |   2 +-
 packages/lsp/tool-lsp/package.json                 |  29 +-
 packages/lsp/tool-lsp/src/index.ts                 |   4 +-
 packages/lsp/tool-lsp/src/invariant.ts             |   2 +-
 packages/lsp/tool-lsp/tests/integration.spec.ts    |   2 +-
 packages/lsp/tool-lsp/tests/load-path.spec.ts      |   2 +-
 packages/lsp/tool-lsp/tests/tool-lsp.spec.ts       |   2 +-
 packages/mcp/mcp-client/README.i18n.yaml           |   4 +-
 packages/mcp/mcp-client/README.md                  |  16 +-
 packages/mcp/mcp-client/README.zh.md               |  14 +-
 packages/mcp/mcp-client/package.json               |  27 +-
 packages/mcp/mcp-client/src/connection.ts          | 351 ++++++++
 packages/mcp/mcp-client/src/index.ts               | 104 +--
 packages/mcp/mcp-client/src/invariant.ts           |   2 +-
 packages/mcp/mcp-client/src/tools.ts               |   2 +-
 packages/mcp/mcp-client/tests/apply.spec.ts        |  81 +-
 packages/mcp/mcp-client/tests/fixture-server.ts    |  11 +
 packages/mcp/mcp-client/tests/load-path.spec.ts    |   2 +-
 packages/mcp/mcp-client/tests/mcp-client.e2e.ts    |  85 +-
 packages/mcp/mcp-client/tests/mcp-client.spec.ts   |   2 +-
 packages/mcp/mcp-client/tests/reconnect.spec.ts    | 521 +++++++++++
 packages/mcp/mcp-client/tsconfig.json              |   3 +
 packages/plan/plan-mode/README.i18n.yaml           |   2 +-
 packages/plan/plan-mode/README.md                  |   2 +-
 packages/plan/plan-mode/package.json               |  33 +-
 packages/plan/plan-mode/src/index.ts               |   4 +-
 packages/plan/plan-mode/src/invariant.ts           |   2 +-
 packages/plan/plan-mode/tests/integration.spec.ts  |   2 +-
 packages/plan/plan-mode/tests/invariant.spec.ts    |   2 +-
 packages/plan/plan-mode/tests/plan-mode.spec.ts    |   4 +-
 packages/plan/plan-mode/tests/projection.spec.ts   |   2 +-
 packages/preset/agent-presets/README.i18n.yaml     |   4 +-
 packages/preset/agent-presets/README.md            |   7 +-
 packages/preset/agent-presets/README.zh.md         |   7 +-
 packages/preset/agent-presets/package.json         |  44 +-
 packages/preset/agent-presets/src/authoring.ts     |   2 +-
 packages/preset/agent-presets/src/discovery.ts     |   4 +-
 packages/preset/agent-presets/src/index.ts         |  50 +-
 packages/preset/agent-presets/src/invariant.ts     |  38 +-
 packages/preset/agent-presets/src/mount.ts         |  10 +-
 packages/preset/agent-presets/src/preset.ts        |  88 ++
 packages/preset/agent-presets/src/types.ts         |  97 +-
 .../preset/agent-presets/tests/authoring.spec.ts   |   6 +-
 .../preset/agent-presets/tests/invariant.spec.ts   |  38 +-
 .../preset/agent-presets/tests/metadata.spec.ts    |   2 +-
 packages/preset/agent-presets/tests/mount.spec.ts  |  52 +-
 .../preset/agent-presets/tests/settings.spec.ts    |   6 +-
 packages/preset/agent-presets/tsconfig.json        |   6 +
 packages/preset/persona/README.i18n.yaml           |   4 +-
 packages/preset/persona/README.md                  |   9 +-
 packages/preset/persona/README.zh.md               |   9 +-
 packages/preset/persona/package.json               |  21 +-
 packages/preset/persona/src/index.ts               |  10 +-
 packages/preset/persona/src/invariant.ts           |   5 +-
 packages/preset/persona/tests/persona.spec.ts      |  19 +-
 packages/pty/pty-local/package.json                |  31 +-
 packages/pty/pty-local/src/config.ts               |   2 +-
 packages/pty/pty-local/src/index.ts                |   2 +-
 packages/pty/pty-local/src/invariant.ts            |   2 +-
 packages/pty/pty-local/tests/index.spec.ts         |   4 +-
 packages/pty/pty-local/tests/local.spec.ts         |   2 +-
 packages/pty/pty/package.json                      |  21 +-
 packages/pty/pty/src/index.ts                      |   4 +-
 packages/pty/pty/src/invariant.ts                  |   2 +-
 packages/pty/pty/tests/service.spec.ts             |   2 +-
 packages/pty/tool-bash-persistent/package.json     |  31 +-
 packages/pty/tool-bash-persistent/src/index.ts     |   4 +-
 packages/pty/tool-bash-persistent/src/invariant.ts |   4 +-
 .../tests/loader-composition.spec.ts               |   6 +-
 .../pty/tool-bash-persistent/tests/tools.spec.ts   |   2 +-
 packages/pty/tool-pty/README.i18n.yaml             |   4 +-
 packages/pty/tool-pty/README.md                    |   2 +-
 packages/pty/tool-pty/README.zh.md                 |   2 +-
 packages/pty/tool-pty/package.json                 |  37 +-
 packages/pty/tool-pty/src/index.ts                 |   4 +-
 packages/pty/tool-pty/src/invariant.ts             |   2 +-
 .../pty/tool-pty/tests/loader-composition.spec.ts  |   6 +-
 packages/pty/tool-pty/tests/tools.spec.ts          |   4 +-
 packages/sandbox/sandbox-local/README.i18n.yaml    |   4 +-
 packages/sandbox/sandbox-local/README.md           |   6 +-
 packages/sandbox/sandbox-local/README.zh.md        |   6 +-
 packages/sandbox/sandbox-local/package.json        |  25 +-
 packages/sandbox/sandbox-local/src/index.ts        | 197 ++--
 packages/sandbox/sandbox-local/src/invariant.ts    |   2 +-
 .../sandbox/sandbox-local/tests/acl-grants.spec.ts | 375 ++++----
 packages/sandbox/sandbox-local/tests/bwrap.e2e.ts  |   2 +-
 .../sandbox/sandbox-local/tests/landlock.e2e.ts    |   2 +-
 packages/sandbox/sandbox-local/tests/local.spec.ts |   4 +-
 .../sandbox-local/tests/packed-install.e2e.ts      |  26 +-
 .../sandbox/sandbox-local/tests/seatbelt.e2e.ts    |   2 +-
 packages/sandbox/sandbox-policy/README.i18n.yaml   |   2 +-
 packages/sandbox/sandbox-policy/README.md          |   2 +-
 packages/sandbox/sandbox-policy/package.json       |  27 +-
 packages/sandbox/sandbox-policy/src/index.ts       |   6 +-
 packages/sandbox/sandbox-policy/src/invariant.ts   |   2 +-
 .../sandbox/sandbox-policy/tests/invariant.spec.ts |   2 +-
 .../sandbox/sandbox-policy/tests/policy.spec.ts    |   2 +-
 .../sandbox/sandbox-windows-acl/README.i18n.yaml   |   4 +-
 packages/sandbox/sandbox-windows-acl/README.md     |  54 +-
 packages/sandbox/sandbox-windows-acl/README.zh.md  |  52 +-
 packages/sandbox/sandbox-windows-acl/package.json  |  20 +-
 packages/sandbox/sandbox-windows-acl/src/acl.ts    |  20 +-
 packages/sandbox/sandbox-windows-acl/src/grant.ts  |  17 +-
 packages/sandbox/sandbox-windows-acl/src/index.ts  | 226 +++--
 .../sandbox/sandbox-windows-acl/src/invariant.ts   |   2 +-
 .../sandbox-windows-acl/src/path-boundary.ts       |  40 +
 packages/sandbox/sandbox-windows-acl/src/runner.ts | 142 +--
 packages/sandbox/sandbox-windows-acl/src/token.ts  |  26 +-
 .../sandbox/sandbox-windows-acl/src/win32-abi.ts   |   2 +-
 .../sandbox-windows-acl/src/workspace-sid.ts       |  22 +-
 .../sandbox/sandbox-windows-acl/tests/acl.spec.ts  |  65 +-
 .../tests/failure-paths.spec.ts                    |   2 +-
 .../sandbox-windows-acl/tests/grant.spec.ts        |   2 +-
 .../tests/index-failure-paths.spec.ts              |  95 +-
 .../tests/path-boundary.spec.ts                    |  65 ++
 .../sandbox-windows-acl/tests/probe.spec.ts        |  33 +-
 .../tests/provider-chain.spec.ts                   |   8 +-
 .../sandbox-windows-acl/tests/runner.spec.ts       | 207 ++++-
 .../tests/token-failure-paths.spec.ts              |  10 +-
 .../tests/workspace-sid.spec.ts                    |  19 +-
 packages/sandbox/sandbox/package.json              |  21 +-
 packages/sandbox/sandbox/src/index.ts              |  14 +-
 packages/sandbox/sandbox/src/invariant.ts          |   2 +-
 packages/scaffold/README.md                        |  17 -
 packages/scaffold/README.zh.md                     |  17 -
 packages/scaffold/create-sdk/README.md             |  25 -
 packages/scaffold/create-sdk/README.zh.md          |  25 -
 packages/scaffold/create-sdk/package.json          |  42 -
 packages/scaffold/create-sdk/src/args.ts           |  96 --
 packages/scaffold/create-sdk/src/bin.ts            |  10 -
 packages/scaffold/create-sdk/src/command.ts        | 144 ---
 .../scaffold/create-sdk/src/create-questions.ts    | 204 -----
 packages/scaffold/create-sdk/src/create-wizard.ts  | 233 -----
 packages/scaffold/create-sdk/src/headless.ts       |  96 --
 packages/scaffold/create-sdk/src/index.ts          |   7 -
 .../scaffold/create-sdk/src/project-scaffolder.ts  |  39 -
 .../src/templates/assets/created.txt.tpl           |   1 -
 .../src/templates/assets/install-question.txt.tpl  |   1 -
 .../src/templates/assets/next-steps.txt.tpl        |   5 -
 .../src/templates/assets/setup-failure.txt.tpl     |   2 -
 .../create-sdk/src/templates/assets/usage.txt.tpl  |  14 -
 .../create-sdk/src/templates/create-templates.ts   |  59 --
 .../create-sdk/tests/built-artifacts.e2e.ts        |  28 -
 .../scaffold/create-sdk/tests/create.snapshot.ts   | 391 --------
 packages/scaffold/create-sdk/tests/create.spec.ts  | 674 --------------
 .../create-sdk/tests/link-workspace.e2e.ts         | 126 ---
 packages/scaffold/create-sdk/tsdown.config.ts      |  14 -
 packages/scaffold/helper/README.md                 |  29 -
 packages/scaffold/helper/README.zh.md              |  29 -
 packages/scaffold/helper/package.json              |  52 --
 .../helper/src/documents/cordis-yaml-file.ts       | 190 ----
 packages/scaffold/helper/src/documents/env-file.ts | 111 ---
 .../helper/src/documents/package-json-file.ts      | 169 ----
 .../helper/src/documents/pnpm-workspace-file.ts    |  96 --
 .../scaffold/helper/src/documents/project-file.ts  |  64 --
 .../scaffold/helper/src/documents/tsconfig-file.ts |  89 --
 .../scaffold/helper/src/features/builtin/app.ts    | 100 ---
 .../helper/src/features/builtin/helpers.ts         | 122 ---
 .../scaffold/helper/src/features/builtin/index.ts  | 368 --------
 .../helper/src/features/builtin/provider.ts        | 108 ---
 .../scaffold/helper/src/features/builtin/spine.ts  |  59 --
 .../scaffold/helper/src/features/define-feature.ts | 286 ------
 .../helper/src/features/feature-configurator.ts    | 111 ---
 packages/scaffold/helper/src/features/feature.ts   | 345 -------
 packages/scaffold/helper/src/features/registry.ts  |  87 --
 packages/scaffold/helper/src/features/resources.ts |  97 --
 packages/scaffold/helper/src/ids.ts                |  31 -
 packages/scaffold/helper/src/index.ts              |  50 --
 .../helper/src/package-managers/link-workspace.ts  | 137 ---
 .../helper/src/package-managers/package-manager.ts | 332 -------
 .../helper/src/plugins/local-plugin-blueprint.ts   | 123 ---
 packages/scaffold/helper/src/project/change-set.ts |  26 -
 .../helper/src/project/npm-dependency-policy.ts    |  62 --
 .../helper/src/project/project-edit-session.ts     | 616 -------------
 .../scaffold/helper/src/project/sdk-project.ts     | 307 -------
 packages/scaffold/helper/src/project/types.ts      |  48 -
 .../src/questions/clack-nested-multiselect.ts      | 304 -------
 .../helper/src/questions/clack-prompt-port.ts      | 127 ---
 .../helper/src/questions/headless-prompt-port.ts   |  97 --
 .../scaffold/helper/src/questions/prompt-port.ts   | 124 ---
 packages/scaffold/helper/src/questions/question.ts | 206 -----
 .../helper/src/templates/assets/README.md.tpl      |  27 -
 .../helper/src/templates/assets/gitignore.tpl      |   5 -
 .../helper/src/templates/assets/index.ts.tpl       |  20 -
 .../assets/local-plugin-tsdown.config.ts.tpl       |  13 -
 .../src/templates/assets/local-plugin.ts.tpl       |   9 -
 .../helper/src/templates/assets/local-tool.ts.tpl  |  17 -
 .../helper/src/templates/assets/package.json.tpl   |  14 -
 .../helper/src/templates/assets/persona.txt.tpl    |   3 -
 .../src/templates/assets/tsconfig.base.json.tpl    |  14 -
 .../src/templates/assets/tsdown.config.ts.tpl      |  13 -
 .../helper/src/templates/assets/yarnrc.yml.tpl     |   1 -
 .../helper/src/templates/project-template.ts       | 110 ---
 .../helper/src/templates/template-assets.ts        |  19 -
 .../scaffold/helper/src/templates/text-template.ts |  44 -
 packages/scaffold/helper/tests/documents.spec.ts   | 409 ---------
 .../helper/tests/headless-prompt-port.spec.ts      |  95 --
 packages/scaffold/helper/tests/project.spec.ts     | 997 ---------------------
 packages/scaffold/helper/tests/questions.spec.ts   | 484 ----------
 packages/scaffold/helper/tsdown.config.ts          |  14 -
 packages/scaffold/protocol/README.i18n.yaml        |   6 -
 packages/scaffold/scripts/README.i18n.yaml         |   6 -
 packages/scaffold/scripts/README.md                |  37 -
 packages/scaffold/scripts/README.zh.md             |  37 -
 packages/scaffold/scripts/package.json             |  64 --
 packages/scaffold/scripts/src/args.ts              |  74 --
 packages/scaffold/scripts/src/bin.ts               |  10 -
 packages/scaffold/scripts/src/build.ts             |  94 --
 packages/scaffold/scripts/src/command.ts           |  76 --
 packages/scaffold/scripts/src/config.ts            |  37 -
 .../scaffold/scripts/src/config/config-workflow.ts | 241 -----
 packages/scaffold/scripts/src/create-plugin.ts     |  91 --
 packages/scaffold/scripts/src/dev/tsdown-config.ts |   7 -
 packages/scaffold/scripts/src/index.ts             |  11 -
 packages/scaffold/scripts/src/invariant.ts         |  30 -
 .../scripts/src/local-plugin-loader-hooks.ts       |  27 -
 packages/scaffold/scripts/src/runtime.ts           | 137 ---
 packages/scaffold/scripts/src/telemetry.ts         |  63 --
 .../assets/config-install-failure.txt.tpl          |   2 -
 .../scripts/src/templates/assets/usage.txt.tpl     |   8 -
 .../scripts/src/templates/dsh-sdk-templates.ts     |  21 -
 .../tests/__snapshots__/config.snapshot.ts.snap    | 288 ------
 packages/scaffold/scripts/tests/config.snapshot.ts | 128 ---
 packages/scaffold/scripts/tests/scripts.spec.ts    | 650 --------------
 packages/scaffold/scripts/tsconfig.json            |  15 -
 packages/scaffold/scripts/tsdown.config.ts         |  26 -
 packages/scaffold/server/README.i18n.yaml          |   6 -
 packages/scaffold/telemetry/README.i18n.yaml       |   6 -
 packages/scaffold/telemetry/README.md              |  30 -
 packages/scaffold/telemetry/README.zh.md           |  30 -
 packages/scaffold/telemetry/package.json           |  42 -
 packages/scaffold/telemetry/src/anonymous-id.ts    |  93 --
 .../scaffold/telemetry/src/consent-resolver.ts     | 125 ---
 packages/scaffold/telemetry/src/index.ts           |  50 --
 packages/scaffold/telemetry/src/invariant.ts       |  30 -
 packages/scaffold/telemetry/src/payload.ts         |  82 --
 packages/scaffold/telemetry/src/reporter.ts        | 148 ---
 packages/scaffold/telemetry/src/secret-redactor.ts | 208 -----
 .../scaffold/telemetry/tests/anonymous-id.spec.ts  |  90 --
 .../telemetry/tests/consent-resolver.spec.ts       | 132 ---
 packages/scaffold/telemetry/tests/payload.spec.ts  |  69 --
 packages/scaffold/telemetry/tests/reporter.spec.ts | 134 ---
 .../telemetry/tests/secret-redactor.spec.ts        | 174 ----
 packages/scaffold/telemetry/tsconfig.json          |  15 -
 packages/schedule/AGENTS.md                        |  10 +
 packages/{scaffold => schedule}/README.i18n.yaml   |   6 +-
 packages/schedule/README.md                        |  13 +
 packages/schedule/README.zh.md                     |  13 +
 packages/schedule/tool-schedule/README.i18n.yaml   |   6 +
 packages/schedule/tool-schedule/README.md          | 117 +++
 packages/schedule/tool-schedule/README.zh.md       | 117 +++
 packages/schedule/tool-schedule/package.json       |  59 ++
 packages/schedule/tool-schedule/src/domain.ts      | 807 +++++++++++++++++
 packages/schedule/tool-schedule/src/index.ts       |  77 ++
 packages/schedule/tool-schedule/src/invariant.ts   |  53 ++
 packages/schedule/tool-schedule/src/persistence.ts |  31 +
 packages/schedule/tool-schedule/src/runtime.ts     | 324 +++++++
 packages/schedule/tool-schedule/src/tools.ts       | 467 ++++++++++
 packages/schedule/tool-schedule/src/transaction.ts |  23 +
 packages/schedule/tool-schedule/src/types.ts       | 221 +++++
 .../schedule/tool-schedule/tests/domain.spec.ts    | 478 ++++++++++
 .../schedule/tool-schedule/tests/invariant.spec.ts | 124 +++
 .../tool-schedule/tests/jsonl-restart.spec.ts      | 138 +++
 .../schedule/tool-schedule/tests/plugin.spec.ts    | 105 +++
 .../tool-schedule/tests/recurrence.spec.ts         |  54 ++
 .../schedule/tool-schedule/tests/runtime.spec.ts   | 798 +++++++++++++++++
 .../schedule/tool-schedule/tests/tools.spec.ts     | 573 ++++++++++++
 .../tool-schedule}/tsconfig.json                   |  28 +-
 packages/schedule/tool-schedule/tsdown.config.ts   |  25 +
 packages/sdk/README.i18n.yaml                      |   6 +
 packages/sdk/README.md                             |  11 +
 packages/sdk/README.zh.md                          |  11 +
 packages/{scaffold => sdk}/client/README.i18n.yaml |   2 +-
 packages/{scaffold => sdk}/client/README.md        |   0
 packages/{scaffold => sdk}/client/README.zh.md     |   0
 packages/{scaffold => sdk}/client/package.json     |  23 +-
 packages/{scaffold => sdk}/client/src/api.ts       |   2 +-
 packages/{scaffold => sdk}/client/src/client.ts    |   0
 packages/{scaffold => sdk}/client/src/dispose.ts   |   2 +-
 packages/{scaffold => sdk}/client/src/index.ts     |   0
 packages/{scaffold => sdk}/client/src/invariant.ts |   2 +-
 packages/{scaffold => sdk}/client/src/types.ts     |   0
 .../{scaffold => sdk}/client/tests/dispose.spec.ts |   2 +-
 .../{scaffold => sdk}/client/tests/fake-runtime.ts |   8 +-
 .../client/tests/sdk-client.spec.ts                |   0
 packages/{scaffold => sdk}/client/tsconfig.json    |   0
 packages/sdk/protocol/README.i18n.yaml             |   6 +
 packages/{scaffold => sdk}/protocol/README.md      |   2 +-
 packages/{scaffold => sdk}/protocol/README.zh.md   |   2 +-
 packages/{scaffold => sdk}/protocol/package.json   |  23 +-
 packages/{scaffold => sdk}/protocol/src/index.ts   |   0
 .../{scaffold => sdk}/protocol/src/invariant.ts    |   2 +-
 .../{scaffold => sdk}/protocol/src/transport.ts    |   2 +-
 packages/{scaffold => sdk}/protocol/src/types.ts   |   2 +-
 .../protocol/tests/transport.spec.ts               |   4 +-
 packages/{scaffold => sdk}/protocol/tsconfig.json  |   0
 packages/sdk/server/README.i18n.yaml               |   6 +
 packages/{scaffold => sdk}/server/README.md        |   2 +-
 packages/{scaffold => sdk}/server/README.zh.md     |   2 +-
 packages/{scaffold => sdk}/server/package.json     |  35 +-
 packages/{scaffold => sdk}/server/src/index.ts     |   6 +-
 packages/{scaffold => sdk}/server/src/invariant.ts |   2 +-
 packages/{scaffold => sdk}/server/src/server.ts    |  10 +-
 .../server/tests/built-scope-carrier.e2e.ts        |   5 +-
 .../server/tests/plugin-apply.spec.ts              |   6 +-
 .../server/tests/plugin-shape.spec.ts              |   2 +-
 .../{scaffold => sdk}/server/tests/server.spec.ts  |   5 +-
 packages/{scaffold => sdk}/server/tsconfig.json    |   0
 packages/self-modification/README.i18n.yaml        |   4 +-
 packages/self-modification/README.md               |   3 +-
 packages/self-modification/README.zh.md            |   3 +-
 .../repository-plugin/README.i18n.yaml             |   6 -
 .../self-modification/repository-plugin/README.md  | 128 ---
 .../repository-plugin/README.zh.md                 | 128 ---
 .../repository-plugin/package.json                 |  73 --
 .../self-modification/repository-plugin/src/bin.ts |  12 -
 .../repository-plugin/src/format.ts                | 249 -----
 .../repository-plugin/src/index.ts                 | 147 ---
 .../repository-plugin/src/invariant.ts             |  30 -
 .../self-modification/repository-plugin/src/mcp.ts | 156 ----
 .../repository-plugin/src/source.ts                | 130 ---
 .../repository-plugin/tests/mcp-format.spec.ts     | 121 ---
 .../tests/repository-plugin.spec.ts                | 674 --------------
 .../repository-plugin/tsdown.config.ts             |  17 -
 .../self-modification/tool-cordis/README.i18n.yaml |   4 +-
 packages/self-modification/tool-cordis/README.md   |   3 +-
 .../self-modification/tool-cordis/README.zh.md     |   3 +-
 .../self-modification/tool-cordis/package.json     |  27 +-
 .../tool-cordis/src/api-catalog.ts                 | 151 +++-
 .../tool-cordis/src/fiber-state.ts                 |   2 +-
 .../self-modification/tool-cordis/src/guard.ts     |   8 +-
 .../self-modification/tool-cordis/src/index.ts     |   6 +-
 .../self-modification/tool-cordis/src/inspect.ts   |   4 +-
 .../self-modification/tool-cordis/src/invariant.ts |   2 +-
 .../self-modification/tool-cordis/src/mount.ts     |   2 +-
 .../tool-cordis/tests/cordis-lifecycle.spec.ts     |   2 +-
 .../self-modification/tool-cordis/tests/helpers.ts |   4 +-
 .../tool-cordis/tests/inspect.spec.ts              |   4 +-
 .../tool-cordis/tests/integration.spec.ts          |   2 +-
 .../tool-cordis/tests/tool-cordis.spec.ts          |   4 +-
 .../tool-cordis/tests/unmount-hmr.spec.ts          |   2 +-
 .../session-query-sqlite/package.json              |  27 +-
 .../session-query-sqlite/src/index.ts              |   6 +-
 .../session-query-sqlite/src/invariant.ts          |   2 +-
 .../session-query-sqlite/tests/load-path.e2e.ts    |   4 +-
 .../session-query-sqlite/tests/sqlite.spec.ts      |   4 +-
 packages/session-query/session-query/package.json  |  27 +-
 packages/session-query/session-query/src/corpus.ts |   2 +-
 packages/session-query/session-query/src/index.ts  |   4 +-
 .../session-query/session-query/src/invariant.ts   |   2 +-
 .../session-query/tests/search-helpers.spec.ts     |   2 +-
 .../session-query/tests/session-query.spec.ts      |  11 +-
 .../session-query/tests/tracing.spec.ts            |   4 +-
 .../session-query/tool-session-query/package.json  |  31 +-
 .../session-query/tool-session-query/src/index.ts  |   4 +-
 .../tool-session-query/src/invariant.ts            |   2 +-
 .../tool-session-query/src/operations.ts           |   2 +-
 .../tool-session-query/src/service-boundary.ts     |   2 +-
 .../tool-session-query/src/workspace-access.ts     |   2 +-
 .../tests/sqlite-integration.spec.ts               |   2 +-
 .../tests/tool-session-query.spec.ts               |   2 +-
 .../session/session-checkpoint-policy/package.json |  29 +-
 .../session/session-checkpoint-policy/src/index.ts |   2 +-
 .../session-checkpoint-policy/src/invariant.ts     |   2 +-
 .../tests/crash-recovery.e2e.ts                    |   2 +-
 .../tests/fixtures/crash-child.ts                  |   2 +-
 .../tests/session-checkpoint-policy.spec.ts        |   6 +-
 .../session-persistence-jsonl/README.i18n.yaml     |   4 +-
 .../session/session-persistence-jsonl/README.md    |   4 +-
 .../session/session-persistence-jsonl/README.zh.md |   2 +-
 .../session/session-persistence-jsonl/package.json |  23 +-
 .../session-persistence-jsonl/src/format.ts        |  20 +-
 .../session/session-persistence-jsonl/src/index.ts | 128 ++-
 .../session-persistence-jsonl/src/invariant.ts     |   2 +-
 .../session/session-persistence-jsonl/src/win32.ts |   2 +-
 .../session-persistence-jsonl/tests/jsonl.spec.ts  | 114 ++-
 .../session-persistence-jsonl/tests/zstd.spec.ts   |  35 +-
 .../session-persistence-sqlite/README.i18n.yaml    |   2 +-
 .../session/session-persistence-sqlite/README.md   |   2 +-
 .../session-persistence-sqlite/package.json        |  23 +-
 .../session-persistence-sqlite/src/index.ts        |  35 +-
 .../session-persistence-sqlite/src/invariant.ts    |   2 +-
 .../session-persistence-sqlite/src/schema.ts       |   7 +-
 .../tests/sqlite.spec.ts                           |  17 +-
 .../session/session-persistence/README.i18n.yaml   |   4 +-
 packages/session/session-persistence/README.md     |   8 +-
 packages/session/session-persistence/README.zh.md  |   6 +-
 packages/session/session-persistence/package.json  |  23 +-
 .../session/session-persistence/src/coordinator.ts | 108 ++-
 packages/session/session-persistence/src/index.ts  |  44 +-
 .../session/session-persistence/src/invariant.ts   |   2 +-
 .../tests/coordinator-contract.ts                  |  60 +-
 .../session-persistence/tests/persistence.spec.ts  |  27 +-
 .../session/session-projection-cache/package.json  |  27 +-
 .../session/session-projection-cache/src/index.ts  |   6 +-
 .../session-projection-cache/src/invariant.ts      |   2 +-
 .../session-projection-cache/tests/cache.spec.ts   |   2 +-
 .../session/session-projection/README.i18n.yaml    |   4 +-
 packages/session/session-projection/README.md      |   1 +
 packages/session/session-projection/README.zh.md   |   1 +
 packages/session/session-projection/package.json   |  19 +-
 packages/session/session-projection/src/index.ts   |   4 +-
 .../session/session-projection/src/invariant.ts    |   2 +-
 .../session-projection/tests/registry.spec.ts      |   2 +-
 .../session-telemetry-otel/README.i18n.yaml        |   4 +-
 packages/session/session-telemetry-otel/README.md  |   2 +
 .../session/session-telemetry-otel/README.zh.md    |   2 +
 .../session/session-telemetry-otel/package.json    |  31 +-
 .../session/session-telemetry-otel/src/index.ts    |  18 +-
 .../session-telemetry-otel/src/invariant.ts        |   2 +-
 .../session-telemetry-otel/tests/otel.spec.ts      |  29 +-
 .../session/session-telemetry/README.i18n.yaml     |   4 +-
 packages/session/session-telemetry/README.md       |   6 +
 packages/session/session-telemetry/README.zh.md    |   8 +
 packages/session/session-telemetry/package.json    |  21 +-
 .../session/session-telemetry/src/coordinator.ts   |   2 +-
 packages/session/session-telemetry/src/index.ts    |  22 +-
 .../session/session-telemetry/src/invariant.ts     |   2 +-
 .../session/session-telemetry/tests/redact.spec.ts |   2 +-
 .../session-telemetry/tests/telemetry.spec.ts      |   2 +-
 .../session-title-all-messages-llm/package.json    |  27 +-
 .../session-title-all-messages-llm/src/index.ts    |   4 +-
 .../src/invariant.ts                               |   2 +-
 .../tests/provider.spec.ts                         |   2 +-
 .../session-title-first-message-llm/package.json   |  31 +-
 .../session-title-first-message-llm/src/index.ts   |   4 +-
 .../src/invariant.ts                               |   2 +-
 .../tests/loader-composition.spec.ts               |   6 +-
 .../tests/provider.e2e.ts                          |   2 +-
 .../tests/provider.spec.ts                         |   2 +-
 packages/session/session-title-llm/package.json    |  27 +-
 packages/session/session-title-llm/src/index.ts    |   4 +-
 .../session/session-title-llm/src/invariant.ts     |   2 +-
 .../session/session-title-llm/tests/llm.spec.ts    |   2 +-
 packages/session/session-title/package.json        |  27 +-
 packages/session/session-title/src/index.ts        |   6 +-
 packages/session/session-title/src/invariant.ts    |   2 +-
 .../session/session-title/tests/invariant.spec.ts  |   2 +-
 .../session-title/tests/persistence.spec.ts        |   2 +-
 .../session/session-title/tests/projection.spec.ts |   2 +-
 .../session/session-title/tests/provider.spec.ts   |   2 +-
 .../session/session-title/tests/rename.spec.ts     |   2 +-
 .../session-title/tests/service-contracts.spec.ts  |   2 +-
 .../session-title/tests/session-title.spec.ts      |   2 +-
 packages/session/user-id/README.i18n.yaml          |   4 +-
 packages/session/user-id/README.md                 |  13 +-
 packages/session/user-id/README.zh.md              |  13 +-
 packages/session/user-id/package.json              |  21 +-
 packages/session/user-id/src/index.ts              |   5 +-
 packages/session/user-id/src/invariant.ts          |   2 +-
 packages/session/user-id/tests/invariant.spec.ts   |   2 +-
 packages/settings/settings-local/package.json      |  25 +-
 packages/settings/settings-local/src/index.ts      |   4 +-
 packages/settings/settings-local/src/invariant.ts  |   2 +-
 .../settings-local/tests/concurrency.spec.ts       |   4 +-
 .../tests/loader-composition.spec.ts               |   8 +-
 .../settings/settings-local/tests/local.spec.ts    |   4 +-
 .../settings-local/tests/lock-race.spec.ts         |   4 +-
 .../settings/settings-local/tests/watcher.spec.ts  |   4 +-
 packages/settings/settings/README.i18n.yaml        |   4 +-
 packages/settings/settings/README.md               |   2 +
 packages/settings/settings/README.zh.md            |   2 +
 packages/settings/settings/package.json            |  28 +-
 packages/settings/settings/src/index.ts            |  47 +-
 packages/settings/settings/src/invariant.ts        |   2 +-
 packages/settings/settings/src/redact.ts           |   2 +-
 packages/settings/settings/src/types.ts            |  50 ++
 packages/settings/settings/tests/invariant.spec.ts |   4 +-
 packages/settings/settings/tests/redact.spec.ts    |   4 +-
 packages/settings/settings/tests/settings.spec.ts  |   4 +-
 packages/skill/skill-badge/assets/dsh-badge.md     |   4 +-
 packages/skill/skill-badge/package.json            |  19 +-
 packages/skill/skill-badge/src/index.ts            |   2 +-
 packages/skill/skill-badge/src/invariant.ts        |   2 +-
 .../skill/skill-badge/tests/skill-badge.spec.ts    |   2 +-
 packages/skill/skill-local/README.i18n.yaml        |   4 +-
 packages/skill/skill-local/README.md               |   2 +-
 packages/skill/skill-local/README.zh.md            |   2 +-
 packages/skill/skill-local/package.json            |  25 +-
 packages/skill/skill-local/src/index.ts            |  11 +-
 packages/skill/skill-local/src/invariant.ts        |   2 +-
 .../skill-local/tests/skill-local-watcher.spec.ts  |   2 +-
 .../skill/skill-local/tests/skill-local.spec.ts    |   8 +-
 packages/skill/skill/README.i18n.yaml              |   2 +-
 packages/skill/skill/README.md                     |   2 +-
 packages/skill/skill/package.json                  |  23 +-
 packages/skill/skill/src/index.ts                  |   8 +-
 packages/skill/skill/src/invariant.ts              |   2 +-
 packages/skill/skill/tests/skill.spec.ts           |   2 +-
 packages/skill/tool-skill/README.i18n.yaml         |   2 +-
 packages/skill/tool-skill/README.md                |   2 +-
 packages/skill/tool-skill/package.json             |  27 +-
 packages/skill/tool-skill/src/index.ts             |   4 +-
 packages/skill/tool-skill/src/invariant.ts         |   2 +-
 packages/skill/tool-skill/tests/tool-skill.spec.ts |   2 +-
 packages/spill/spill-local/package.json            |  21 +-
 packages/spill/spill-local/src/index.ts            |   4 +-
 packages/spill/spill-local/src/invariant.ts        |   2 +-
 .../spill/spill-local/tests/spill-local.spec.ts    |   2 +-
 packages/spill/spill-policy/README.i18n.yaml       |   2 +-
 packages/spill/spill-policy/README.md              |   4 +-
 packages/spill/spill-policy/package.json           |  31 +-
 packages/spill/spill-policy/src/index.ts           |   4 +-
 packages/spill/spill-policy/src/invariant.ts       |   2 +-
 .../spill/spill-policy/tests/spill-policy.spec.ts  |   4 +-
 packages/spill/spill/package.json                  |  23 +-
 packages/spill/spill/src/index.ts                  |   4 +-
 packages/spill/spill/src/invariant.ts              |   2 +-
 packages/spill/spill/tests/service.spec.ts         |   2 +-
 packages/storage/storage-domain/package.json       |  21 +-
 packages/storage/storage-domain/src/domain.ts      |   2 +-
 packages/storage/storage-domain/src/events.ts      |   2 +-
 packages/storage/storage-domain/src/index.ts       |   6 +-
 packages/storage/storage-domain/src/invariant.ts   |   2 +-
 .../storage/storage-domain/tests/domain.spec.ts    |   2 +-
 .../storage/storage-domain/tests/invariant.spec.ts |   2 +-
 packages/storage/storage-json/package.json         |  21 +-
 packages/storage/storage-json/src/index.ts         |   4 +-
 packages/storage/storage-json/src/invariant.ts     |   2 +-
 .../storage-json/tests/json-backend.spec.ts        |   2 +-
 packages/storage/storage-sqlite/package.json       |  21 +-
 packages/storage/storage-sqlite/src/index.ts       |   4 +-
 packages/storage/storage-sqlite/src/invariant.ts   |   2 +-
 .../storage/storage-sqlite/tests/invariant.spec.ts |   2 +-
 .../storage-sqlite/tests/sqlite-backend.spec.ts    |   2 +-
 packages/storage/storage/package.json              |  17 +-
 packages/storage/storage/src/index.ts              |   4 +-
 packages/storage/storage/src/invariant.ts          |   2 +-
 packages/storage/storage/tests/registry.spec.ts    |   2 +-
 packages/subagent/subagent-acp/package.json        |  33 +-
 packages/subagent/subagent-acp/src/index.ts        |   4 +-
 packages/subagent/subagent-acp/src/invariant.ts    |   2 +-
 packages/subagent/subagent-acp/src/run.ts          |  19 +-
 .../subagent-acp/tests/subagent-acp.e2e.ts         |   2 +-
 .../subagent-acp/tests/subagent-acp.spec.ts        |   4 +-
 .../subagent/subagent-claude-code/README.i18n.yaml |   4 +-
 packages/subagent/subagent-claude-code/README.md   |  12 +-
 .../subagent/subagent-claude-code/README.zh.md     |  12 +-
 .../subagent/subagent-claude-code/package.json     |  29 +-
 .../subagent/subagent-claude-code/src/index.ts     |  12 +-
 .../subagent/subagent-claude-code/src/invariant.ts |   2 +-
 .../subagent/subagent-claude-code/src/process.ts   |  18 +-
 packages/subagent/subagent-claude-code/src/run.ts  |   3 +
 .../tests/real-deepseek.e2e.ts                     |   5 +-
 .../tests/real-product.spec.ts                     |  38 +-
 .../tests/subagent-claude-code.spec.ts             |  39 +-
 packages/subagent/subagent-codex/README.i18n.yaml  |   4 +-
 packages/subagent/subagent-codex/README.md         |   3 +-
 packages/subagent/subagent-codex/README.zh.md      |   3 +-
 packages/subagent/subagent-codex/package.json      |  33 +-
 packages/subagent/subagent-codex/src/index.ts      |   4 +-
 packages/subagent/subagent-codex/src/invariant.ts  |   2 +-
 .../subagent-codex/tests/real-deepseek.e2e.ts      |   2 +-
 .../subagent-codex/tests/real-product.spec.ts      |   6 +-
 .../subagent-codex/tests/subagent-codex.spec.ts    |   4 +-
 packages/subagent/subagent-codex/tsconfig.json     |   2 +-
 .../subagent/subagent-dsh-sdk/README.i18n.yaml     |   4 +-
 packages/subagent/subagent-dsh-sdk/README.md       |   4 +-
 packages/subagent/subagent-dsh-sdk/README.zh.md    |   4 +-
 packages/subagent/subagent-dsh-sdk/package.json    |  33 +-
 packages/subagent/subagent-dsh-sdk/src/index.ts    |   4 +-
 .../subagent/subagent-dsh-sdk/src/invariant.ts     |   2 +-
 packages/subagent/subagent-dsh-sdk/src/run.ts      |  22 +-
 .../tests/subagent-dsh-sdk.spec.ts                 |  18 +-
 packages/subagent/subagent-dsh-sdk/tsconfig.json   |   4 +-
 packages/subagent/subagent-fork/README.i18n.yaml   |   4 +-
 packages/subagent/subagent-fork/README.md          |   3 +-
 packages/subagent/subagent-fork/README.zh.md       |   3 +-
 packages/subagent/subagent-fork/package.json       |  29 +-
 packages/subagent/subagent-fork/src/index.ts       |  10 +-
 packages/subagent/subagent-fork/src/invariant.ts   |   2 +-
 .../subagent-fork/tests/multi-subagent.spec.ts     |   2 +-
 .../subagent-fork/tests/subagent-fork.spec.ts      |   4 +-
 .../subagent/subagent-inprocess/README.i18n.yaml   |   4 +-
 packages/subagent/subagent-inprocess/README.md     |   4 +-
 packages/subagent/subagent-inprocess/README.zh.md  |   4 +-
 packages/subagent/subagent-inprocess/package.json  |  43 +-
 packages/subagent/subagent-inprocess/src/index.ts  |  40 +-
 .../subagent/subagent-inprocess/src/invariant.ts   |   2 +-
 .../subagent/subagent-inprocess/src/structured.ts  |   2 +-
 .../subagent-inprocess/tests/inheritance.spec.ts   |  69 +-
 .../tests/preset-inheritance.spec.ts               |   6 +-
 .../subagent-inprocess/tests/structured.spec.ts    |   6 +-
 .../tests/subagent-inprocess.spec.ts               |  53 +-
 packages/subagent/subagent-inprocess/tsconfig.json |   6 -
 packages/subagent/subagent-spawn/package.json      |  25 +-
 packages/subagent/subagent-spawn/src/index.ts      |   4 +-
 packages/subagent/subagent-spawn/src/invariant.ts  |   2 +-
 packages/subagent/subagent-spawn/tests/harness.ts  |   2 +-
 .../subagent/subagent-spawn/tests/spawn.e2e.ts     |   2 +-
 .../subagent-spawn/tests/subagent-spawn.spec.ts    |   4 +-
 packages/subagent/subagent/README.i18n.yaml        |   4 +-
 packages/subagent/subagent/README.md               |  52 +-
 packages/subagent/subagent/README.zh.md            |  50 +-
 packages/subagent/subagent/package.json            |  54 +-
 .../subagent/src/activation-setup-registry.ts      |   2 +-
 packages/subagent/subagent/src/assistant-output.ts |  74 ++
 packages/subagent/subagent/src/child-agent.ts      | 102 ++-
 packages/subagent/subagent/src/continuation.ts     | 262 +++++-
 packages/subagent/subagent/src/index.ts            |  12 +-
 packages/subagent/subagent/src/invariant.ts        |   2 +-
 packages/subagent/subagent/src/lifecycle.ts        |  90 +-
 packages/subagent/subagent/src/list-children.ts    |   2 +-
 packages/subagent/subagent/src/types.ts            |  23 +-
 .../tests/activation-setup-registry.spec.ts        |   2 +-
 .../subagent/tests/assistant-output.spec.ts        |  92 ++
 .../tests/continuation-inheritance.spec.ts         | 231 +++++
 .../subagent/subagent/tests/continuation.spec.ts   | 610 ++++++++++++-
 packages/subagent/subagent/tests/invariant.spec.ts |   2 +-
 .../subagent/subagent/tests/list-children.spec.ts  |   2 +-
 packages/subagent/subagent/tests/service.spec.ts   |  14 +-
 .../subagent/tests/timing-projection.spec.ts       |   2 +-
 packages/subagent/subagent/tsconfig.json           |   9 +
 .../tool-subagent-control/README.i18n.yaml         |   4 +-
 packages/subagent/tool-subagent-control/README.md  |   6 +-
 .../subagent/tool-subagent-control/README.zh.md    |   6 +-
 .../subagent/tool-subagent-control/package.json    |  25 +-
 .../subagent/tool-subagent-control/src/index.ts    |   4 +-
 .../tool-subagent-control/src/invariant.ts         |   2 +-
 .../tool-subagent-control/src/list-agents.ts       |  22 +-
 .../tests/list-agents.spec.ts                      |  26 +-
 .../tool-subagent-control/tests/park-parent.ts     |  22 +
 .../tests/tool-subagent-control.spec.ts            |   8 +-
 .../subagent/tool-subagent-report/README.i18n.yaml |   4 +-
 packages/subagent/tool-subagent-report/README.md   |  20 +-
 .../subagent/tool-subagent-report/README.zh.md     |  20 +-
 .../subagent/tool-subagent-report/package.json     |  27 +-
 .../subagent/tool-subagent-report/src/index.ts     | 149 +--
 .../subagent/tool-subagent-report/src/invariant.ts |   2 +-
 .../tests/tool-subagent-report.spec.ts             | 135 ++-
 .../subagent/tool-subagent-report/tsconfig.json    |   3 +
 packages/subagent/tool-subagent/README.i18n.yaml   |   4 +-
 packages/subagent/tool-subagent/README.md          |  20 +-
 packages/subagent/tool-subagent/README.zh.md       |  20 +-
 packages/subagent/tool-subagent/package.json       |  32 +-
 packages/subagent/tool-subagent/src/index.ts       | 132 ++-
 packages/subagent/tool-subagent/src/invariant.ts   |   2 +-
 .../tool-subagent/tests/scripted-provider.spec.ts  |   2 +-
 .../tool-subagent/tests/scripted-provider.ts       |   9 +-
 .../tool-subagent/tests/tool-subagent.spec.ts      | 196 +++-
 packages/subagent/tool-subagent/tsconfig.json      |   3 +
 .../subprocess/subprocess-local/README.i18n.yaml   |   4 +-
 packages/subprocess/subprocess-local/README.md     |   2 +-
 packages/subprocess/subprocess-local/README.zh.md  |   2 +-
 packages/subprocess/subprocess-local/package.json  |  21 +-
 packages/subprocess/subprocess-local/src/index.ts  |   2 +-
 .../subprocess/subprocess-local/src/invariant.ts   |   2 +-
 .../subprocess-local/tests/local.spec.ts           |   2 +-
 .../subprocess-local/tests/spawn.spec.ts           |   2 +-
 packages/subprocess/subprocess/package.json        |  17 +-
 packages/subprocess/subprocess/src/index.ts        |   4 +-
 packages/subprocess/subprocess/src/invariant.ts    |   2 +-
 .../subprocess/subprocess/tests/service.spec.ts    |   2 +-
 packages/support/acp-snapshot/README.i18n.yaml     |   4 +-
 packages/support/acp-snapshot/README.md            |   2 +
 packages/support/acp-snapshot/README.zh.md         |   2 +
 packages/support/acp-snapshot/package.json         |  19 +-
 packages/support/acp-snapshot/src/invariant.ts     |   2 +-
 packages/support/acp-snapshot/src/launcher.ts      |   2 +-
 packages/support/acp-snapshot/src/suite.ts         |  87 +-
 .../tests/fixtures/suite/plain-turn/behavior.json  |   2 +-
 .../suite/plain-turn/system-prompt.1.expected.md   |   3 +
 packages/support/acp-snapshot/tests/suite.spec.ts  |  33 +
 .../support/agent-loop-testkit/README.i18n.yaml    |   4 +-
 packages/support/agent-loop-testkit/README.md      |   2 +-
 packages/support/agent-loop-testkit/README.zh.md   |   2 +-
 packages/support/agent-loop-testkit/package.json   |  27 +-
 packages/support/agent-loop-testkit/src/index.ts   |   2 +-
 .../support/agent-loop-testkit/src/invariant.ts    |   2 +-
 .../tests/agent-loop-testkit.spec.ts               |   2 +-
 packages/support/invariants/README.i18n.yaml       |   4 +-
 packages/support/invariants/README.md              |   4 +-
 packages/support/invariants/README.zh.md           |   2 +-
 packages/support/invariants/package.json           |  17 +-
 packages/support/invariants/src/index.ts           |  10 +-
 packages/support/invariants/src/invariant.ts       |   2 +-
 packages/support/invariants/tests/service.spec.ts  |   6 +-
 packages/support/llm-mock-server/README.i18n.yaml  |   4 +-
 packages/support/llm-mock-server/README.md         |   2 +-
 packages/support/llm-mock-server/README.zh.md      |   2 +-
 packages/support/llm-mock-server/package.json      |  17 +-
 packages/support/llm-mock-server/src/invariant.ts  |   2 +-
 .../llm-mock-server/tests/invariant.spec.ts        |   2 +-
 packages/support/llm-replay/README.i18n.yaml       |   4 +-
 packages/support/llm-replay/README.md              |   2 +-
 packages/support/llm-replay/README.zh.md           |   2 +-
 packages/support/llm-replay/package.json           |  23 +-
 packages/support/llm-replay/src/index.ts           |  26 +-
 packages/support/llm-replay/src/invariant.ts       |   2 +-
 .../support/llm-replay/tests/llm-replay.spec.ts    |  32 +-
 packages/support/loader-smoke/package.json         |  23 +-
 packages/support/loader-smoke/src/agent-turn.ts    |   2 +-
 packages/support/loader-smoke/src/invariant.ts     |   2 +-
 .../support/loader-smoke/tests/agent-turn.spec.ts  |   2 +-
 packages/tasks/tasks-local/README.i18n.yaml        |   4 +-
 packages/tasks/tasks-local/README.md               |   6 +-
 packages/tasks/tasks-local/README.zh.md            |   6 +-
 packages/tasks/tasks-local/package.json            |  25 +-
 packages/tasks/tasks-local/src/index.ts            | 141 ++-
 packages/tasks/tasks-local/src/invariant.ts        |   2 +-
 packages/tasks/tasks-local/tests/tasks.spec.ts     | 259 +++++-
 packages/tasks/tasks/README.i18n.yaml              |   4 +-
 packages/tasks/tasks/README.md                     |  11 +-
 packages/tasks/tasks/README.zh.md                  |  11 +-
 packages/tasks/tasks/package.json                  |  28 +-
 packages/tasks/tasks/src/brand.ts                  |  28 +
 packages/tasks/tasks/src/index.ts                  |  57 +-
 packages/tasks/tasks/src/invariant.ts              |   2 +-
 packages/tasks/tasks/src/types.ts                  |  39 +-
 packages/tasks/tasks/tests/invariant.spec.ts       |   2 +-
 packages/tasks/tasks/tests/service.spec.ts         |  18 +-
 packages/tasks/tool-tasks/README.i18n.yaml         |   4 +-
 packages/tasks/tool-tasks/README.md                |  24 +-
 packages/tasks/tool-tasks/README.zh.md             |  24 +-
 packages/tasks/tool-tasks/package.json             |  31 +-
 packages/tasks/tool-tasks/src/index.ts             |  75 +-
 packages/tasks/tool-tasks/src/invariant.ts         |   2 +-
 packages/tasks/tool-tasks/tests/tool-tasks.spec.ts | 219 ++++-
 packages/todo/tool-todo/package.json               |  31 +-
 packages/todo/tool-todo/src/index.ts               |   4 +-
 packages/todo/tool-todo/src/invariant.ts           |   2 +-
 packages/todo/tool-todo/tests/integration.spec.ts  |   2 +-
 packages/todo/tool-todo/tests/invariant.spec.ts    |   2 +-
 .../tool-todo/tests/loader-composition.spec.ts     |   6 +-
 packages/todo/tool-todo/tests/projection.spec.ts   |   2 +-
 packages/todo/tool-todo/tests/tool-todo.spec.ts    |   4 +-
 packages/typert/generator/README.i18n.yaml         |   2 +-
 packages/typert/generator/README.md                |   2 +-
 packages/typert/generator/package.json             |  17 +-
 packages/typert/generator/src/analyzer.ts          |   4 +-
 packages/typert/generator/src/cordis-catalog.ts    |  18 +-
 packages/typert/generator/src/index.ts             |   2 +-
 packages/typert/generator/src/invariant.ts         |   2 +-
 packages/typert/generator/src/renderer.ts          |   2 +-
 .../tests/__snapshots__/type-model.spec.ts.snap    |  88 +-
 .../tests/cordis-catalog-contract.spec.ts          |   6 +-
 .../tests/fixtures/type-model/cordis.d.ts          |   2 +-
 .../type-model/packages/client/src/index.ts        |   4 +-
 .../fixtures/type-model/packages/host/src/index.ts |   6 +-
 .../type-model/packages/write/src/index.ts         |   4 +-
 .../tests/fixtures/type-model/tsconfig.base.json   |   2 +-
 .../typert/generator/tests/tools-catalog.spec.ts   |   2 +-
 packages/typert/generator/tests/type-model.spec.ts |  10 +-
 packages/typert/loader/package.json                |  25 +-
 packages/typert/loader/src/index.ts                |   6 +-
 packages/typert/loader/src/invariant.ts            |   2 +-
 packages/typert/loader/tests/loader.spec.ts        |   4 +-
 packages/typert/registry/package.json              |  17 +-
 packages/typert/registry/src/client/index.ts       |   2 +-
 packages/typert/registry/src/invariant.ts          |   2 +-
 packages/typert/registry/src/service.ts            |   2 +-
 packages/typert/registry/tests/typert.spec.ts      |   2 +-
 packages/typert/type-meta/README.i18n.yaml         |   4 +-
 packages/typert/type-meta/README.md                |   4 +-
 packages/typert/type-meta/README.zh.md             |   2 +
 packages/typert/type-meta/package.json             |  17 +-
 packages/typert/type-meta/src/index.ts             |   5 +-
 packages/typert/type-meta/src/invariant.ts         |   2 +-
 packages/typert/type-meta/src/types.ts             |  43 +-
 .../type-meta/tests/fixtures/source-launch.ts      |   2 +-
 packages/typert/type-meta/tests/type-meta.spec.ts  |  40 +-
 packages/util/atomic-write/package.json            |  17 +-
 packages/util/atomic-write/src/invariant.ts        |   2 +-
 .../util/atomic-write/tests/atomic-write.spec.ts   |   2 +-
 packages/util/atomic-write/tests/invariant.spec.ts |   2 +-
 packages/util/brand/package.json                   |  17 +-
 packages/util/brand/src/invariant.ts               |   2 +-
 packages/util/environment/README.i18n.yaml         |   4 +-
 packages/util/environment/README.md                |   2 +-
 packages/util/environment/README.zh.md             |   2 +-
 packages/util/environment/package.json             |  17 +-
 packages/util/environment/src/index.ts             |   4 +-
 packages/util/environment/src/invariant.ts         |   2 +-
 .../util/environment/tests/environment.spec.ts     |   2 +-
 packages/util/native-command/package.json          |  17 +-
 packages/util/native-command/src/invariant.ts      |   2 +-
 packages/util/paths/package.json                   |  17 +-
 packages/util/paths/src/invariant.ts               |   2 +-
 packages/util/retention/README.i18n.yaml           |   2 +-
 packages/util/retention/README.md                  |   2 +-
 packages/util/retention/package.json               |  17 +-
 packages/util/retention/src/invariant.ts           |   2 +-
 packages/util/timeout/README.i18n.yaml             |   2 +-
 packages/util/timeout/README.md                    |   2 +-
 packages/util/timeout/package.json                 |  17 +-
 packages/util/timeout/src/invariant.ts             |   2 +-
 packages/web/tool-web/README.i18n.yaml             |   2 +-
 packages/web/tool-web/README.md                    |   2 +-
 packages/web/tool-web/package.json                 |  27 +-
 packages/web/tool-web/src/fetch.ts                 |   2 +-
 packages/web/tool-web/src/index.ts                 |   4 +-
 packages/web/tool-web/src/invariant.ts             |   2 +-
 packages/web/tool-web/src/search.ts                |   2 +-
 packages/web/tool-web/tests/integration.spec.ts    |   2 +-
 packages/web/tool-web/tests/load-path.spec.ts      |   4 +-
 packages/web/tool-web/tests/spill.spec.ts          |   2 +-
 packages/web/tool-web/tests/tool-web.spec.ts       |   2 +-
 packages/web/web-fetch-local/package.json          |  23 +-
 packages/web/web-fetch-local/src/index.ts          |   4 +-
 packages/web/web-fetch-local/src/invariant.ts      |   2 +-
 .../web/web-fetch-local/tests/fetch-local.spec.ts  |   2 +-
 packages/web/web-search-deepseek/README.i18n.yaml  |   4 +-
 packages/web/web-search-deepseek/README.md         |   4 +-
 packages/web/web-search-deepseek/README.zh.md      |   2 +
 packages/web/web-search-deepseek/package.json      |  31 +-
 packages/web/web-search-deepseek/src/index.ts      |  57 +-
 packages/web/web-search-deepseek/src/invariant.ts  |   2 +-
 packages/web/web-search-deepseek/src/provider.ts   |  57 +-
 packages/web/web-search-deepseek/src/types.ts      |   4 +-
 .../web/web-search-deepseek/tests/deepseek.e2e.ts  |   8 +-
 .../web/web-search-deepseek/tests/deepseek.spec.ts |  90 +-
 .../web/web-search-deepseek/tests/redirect.spec.ts |   8 +-
 .../web/web-search-deepseek/tests/settings.spec.ts | 124 +++
 packages/web/web-search-deepseek/tsconfig.json     |   3 +
 packages/web/web-search-exa/package.json           |  23 +-
 packages/web/web-search-exa/src/index.ts           |   4 +-
 packages/web/web-search-exa/src/invariant.ts       |   2 +-
 packages/web/web-search-exa/tests/exa.spec.ts      |   2 +-
 packages/web/web-search-perplexity/package.json    |  23 +-
 packages/web/web-search-perplexity/src/index.ts    |   4 +-
 .../web/web-search-perplexity/src/invariant.ts     |   2 +-
 packages/web/web-search-perplexity/src/provider.ts |   2 +-
 packages/web/web-search-perplexity/src/types.ts    |   4 +-
 .../web-search-perplexity/tests/perplexity.spec.ts |   2 +-
 packages/web/web/README.i18n.yaml                  |   2 +-
 packages/web/web/README.md                         |   2 +-
 packages/web/web/package.json                      |  21 +-
 packages/web/web/src/index.ts                      |   6 +-
 packages/web/web/src/invariant.ts                  |   2 +-
 packages/web/web/src/types.ts                      |   2 +-
 packages/web/web/tests/web.spec.ts                 |   2 +-
 packages/workflow/tool-ralph/README.i18n.yaml      |   2 +-
 packages/workflow/tool-ralph/README.md             |   2 +-
 packages/workflow/tool-ralph/package.json          |  33 +-
 packages/workflow/tool-ralph/src/index.ts          |   4 +-
 packages/workflow/tool-ralph/src/invariant.ts      |   2 +-
 .../workflow/tool-ralph/tests/integration.spec.ts  |   2 +-
 .../workflow/tool-ralph/tests/tool-ralph.spec.ts   |   4 +-
 packages/workflow/tool-workflow/README.i18n.yaml   |   4 +-
 packages/workflow/tool-workflow/README.md          |   7 +-
 packages/workflow/tool-workflow/README.zh.md       |   5 +
 packages/workflow/tool-workflow/package.json       |  35 +-
 packages/workflow/tool-workflow/src/index.ts       | 124 ++-
 packages/workflow/tool-workflow/src/invariant.ts   | 177 +++-
 packages/workflow/tool-workflow/src/types.ts       |  64 ++
 .../workflow/tool-workflow/tests/invariant.spec.ts | 199 ++++
 .../tool-workflow/tests/tool-workflow.spec.ts      | 205 ++++-
 packages/workflow/tool-workflow/tsconfig.json      |   3 +
 .../workflow/workflow-workerthread/package.json    |  33 +-
 .../workflow/workflow-workerthread/src/host.ts     |   2 +-
 .../workflow/workflow-workerthread/src/index.ts    |   4 +-
 .../workflow-workerthread/src/invariant.ts         |   2 +-
 .../tests/built-worker.e2e.ts                      |   2 +-
 .../tests/integration.spec.ts                      |   2 +-
 .../tests/source-worker.compat.spec.ts             |   2 +-
 .../tests/workflow-workerthread.e2e.ts             |   2 +-
 .../tests/workflow-workerthread.spec.ts            |   6 +-
 packages/workflow/workflow/README.i18n.yaml        |   4 +-
 packages/workflow/workflow/README.md               |   4 +-
 packages/workflow/workflow/README.zh.md            |   2 +
 packages/workflow/workflow/package.json            |  30 +-
 packages/workflow/workflow/src/index.ts            |  10 +-
 packages/workflow/workflow/src/invariant.ts        |   2 +-
 packages/workflow/workflow/src/runtime-types.ts    |  49 +
 packages/workflow/workflow/src/types.ts            |  54 +-
 packages/workflow/workflow/tests/invariant.spec.ts |   2 +-
 packages/workflow/workflow/tests/workflow.spec.ts  |   4 +-
 packages/workflow/workflow/tsconfig.json           |   3 +
 packages/workspace/workspace/package.json          |  27 +-
 packages/workspace/workspace/src/index.ts          |   4 +-
 packages/workspace/workspace/src/invariant.ts      |   2 +-
 .../workspace/workspace/tests/invariant.spec.ts    |   2 +-
 .../workspace/workspace/tests/workspace.spec.ts    |   2 +-
 pnpm-workspace.yaml                                |  10 +-
 2113 files changed, 41776 insertions(+), 26459 deletions(-)
```

## 破坏性变更清单

- 本日快照未发现 seam 符号级破坏。
- 删除的包目录：packages/scaffold/create-sdk packages/scaffold/helper packages/scaffold/protocol packages/scaffold/scripts packages/scaffold/server packages/scaffold/telemetry packages/self-modification/repository-plugin。

## 插件侧建议（按仓库）

### chat-width
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 3 项中 3 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### deepseek-harness-desktop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### deepseek-harness-distro
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### distill
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 7 项中 7 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-acp
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-agent-session-sources
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 29 项中 25 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subagent-claude-code=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-artifact
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-cc-tui
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 12 项中 1 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-coding-receipt
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
- 输入来自 DSH session log，建议在 mainline 会话持久化格式稳定后实现。
### dsh-companion
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 7 项中 7 不匹配: @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-cordis-examples
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-desktop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-feishu-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-gh-bridge
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-github-integration
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 7 项中 5 不匹配: @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-issue-filer
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-live-stats
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 7 项中 7 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-conversation=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-projection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-token-meter=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-memory-evolve
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-my-rsi
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 89 项中 38 不匹配: @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-workflow=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-credentials=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-timeout=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-command-feedback=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-fs=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-reference=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox-policy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-approval=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-opencode-server
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-pi-adapter
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-prompt-studio
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-pty-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-session-search
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 3 项中 3 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-sfw
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-shell-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-skills-manager
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 无 dsh-* 依赖），建议确认所依赖的宿主面当日是否仍满足。
### dsh-skins
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 5 项中 5 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-theme=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-subagent-tree
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（340d23a）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-tool-browser
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 5 项中 5 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-tool-calculator
- 兼容：锚定 25b2ad4f67（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-encoding
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-json
- 兼容：锚定 25b2ad4f67（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-time
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-ui-progress
- 兼容：锚定 20260805T134133Z（未知（非 commit 锚定: 20260805T134133Z））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-ui-whale
- 兼容：锚定 20260805T134133Z（未知（非 commit 锚定: 20260805T134133Z））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-vision
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 2 项中 2 不匹配: @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-web-terminal
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-web-ui-approval-notify
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-web-ui
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-wecom-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-weixin-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-win-port
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-working-activity
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（340d23a）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dshx-update-check
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ex-setting
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 9 项中 9 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-schema-form=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### group-chat-diary
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### hub
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### issues
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### marisa
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 2 项匹配），建议确认所依赖的宿主面当日是否仍满足。
### plugin-registry
- 兼容：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁「无补丁」，当日 mainline 可干净集成。
### qqbot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### Qwen-MM-Plugins
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 4 项中 4 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-mcp-client=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-skill-local=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### Recall
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### review-panel
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-mxc
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 4 项中 3 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-sandbox=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-subprocess=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### session-chatlog
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 4 项中 4 不匹配: @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session-persistence=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### session-persistence-rdb
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### telegram
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 3 项中 3 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### tg-bot
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 12 项中 12 不匹配: @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-web-react=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-host-apiproxy=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-user-interaction=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### toybox
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### turtle-ui
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### web-components
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 4 项中 4 不匹配: @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
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
- 未建模/状态未知：尚无 research/fabric.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
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
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 6 项中 6 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-atomic-write=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
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
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 8 项中 8 不匹配: @deepseek-ai/dsh-agent=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-connection=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-locale=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-settings=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-settings=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
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
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（340d23a）为新基线重新锚定/rebuild 补丁。
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
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 9 项中 9 不匹配: @deepseek-ai/dsh-client-runtime=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-primitives=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slash=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-slots=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-client-ui-tool=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-llm=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-system-prompt=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-tools=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### dsh-mygo
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 9 项中 6 不匹配: @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-session=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-invariants=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-paths=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage=^0.0.1↔0.0.1-rc.1 @deepseek-ai/dsh-storage-domain=^0.0.1↔0.0.1-rc.1），建议确认所依赖的宿主面当日是否仍满足。
### cross-harness-cite
- 未建模/状态未知：尚无 research/cross-harness-cite.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-split-panes
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（340d23a）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-task-board
- 未建模/状态未知：尚无 research/dsh-task-board.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-activity-plugin
- 未建模/状态未知：尚无 research/dsh-activity-plugin.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-tool-diff
- 未建模/状态未知：尚无 research/dsh-tool-diff.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-git-graph
- 未建模/状态未知：尚无 research/dsh-git-graph.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-mobileweb-adapter
- 未建模/状态未知：尚无 research/dsh-mobileweb-adapter.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-desktop-electron
- 未建模/状态未知：尚无 research/dsh-desktop-electron.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-mineru
- 未建模/状态未知：尚无 research/dsh-mineru.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-pet
- 未建模/状态未知：尚无 research/dsh-pet.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-paseo
- 未建模/状态未知：尚无 research/dsh-paseo.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-remote-web-ui
- 未建模/状态未知：尚无 research/dsh-remote-web-ui.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
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
- 兼容：锚定 348409b1（未知（不同谱系））、补丁「OK（1 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 348409b1 显式记录到 README/补丁头，快照一漂即可自动预警。
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
### dsh-pet-web
- 未建模/状态未知：尚无 research/dsh-pet-web.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
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
- 兼容：锚定 8ec407cd64（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
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
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### Top
- 未建模/状态未知：尚无 research/Top.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### __perm_probe__
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-kimi-browser
- 未建模/状态未知：尚无 research/dsh-kimi-browser.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-edu
- 未建模/状态未知：尚无 research/dsh-edu.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-ohos-patch
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（4 个补丁中 3 个 OK）」；建议以当日 snapshot HEAD（340d23a）为新基线重新锚定/rebuild 补丁。
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
### dsh-roleplay-portable-spike
- 未建模/状态未知：尚无 research/dsh-roleplay-portable-spike.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
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
- 兼容：锚定 20260811T152241Z（未知（非 commit 锚定: 20260811T152241Z））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-kb-sieve
- 未建模/状态未知：尚无 research/dsh-kb-sieve.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-data-agent
- 未建模/状态未知：尚无 research/dsh-data-agent.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-security
- 未建模/状态未知：尚无 research/dsh-security.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-teamwork
- 未建模/状态未知：尚无 research/dsh-teamwork.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
