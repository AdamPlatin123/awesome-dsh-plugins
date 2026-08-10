# mainline 兼容性报告（2026-08-10）

- mainline：`1c4950a`（snapshots/20260809T140917Z）
- 上次对比：`1c4950ab71fa4d128c749d9b22af17373edddb73`
- 兼容性：74/176 无需适配，6 需适配（dsh-subagent-tree dsh-working-activity plugin-registry turtle-ui dsh-tps dsh-split-panes）；其中关注 3、占位 9、不适用 2、已删除 1、未知 95

## 兼容性矩阵

| 仓库 | 锚定 | 补丁 | seam | peerDeps | 综合判定 |
|---|---|---|---|---|---|
| chat-width | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| deepseek-harness-desktop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| deepseek-harness-distro | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| distill | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| dsh-acp | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-agent-session-sources | 未知 | 无补丁 | 缺: tuiPrompt | 29 项匹配 | 兼容 |
| dsh-artifact | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-cc-tui | 未知 | 无补丁 | 缺: tuiPrompt | 12 项匹配 | 关注 |
| dsh-coding-receipt | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-companion | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| dsh-cordis-examples | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-desktop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-feishu-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-gh-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-github-integration | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| dsh-issue-filer | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-live-stats | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| dsh-memory-evolve | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-my-rsi | 未知（不同谱系） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 89 项匹配 | 兼容 |
| dsh-opencode-server | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-pi-adapter | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-prompt-studio | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-pty-windows | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-session-search | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| dsh-sfw | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-shell-windows | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-skills-manager | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 关注 |
| dsh-skins | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-subagent-tree | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 6 项匹配 | 需适配 |
| dsh-tool-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-tool-calculator | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-tool-encoding | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-tool-json | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-tool-time | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-ui-progress | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-ui-whale | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-vision | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-web-terminal | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-web-ui-approval-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-web-ui | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-wecom-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-weixin-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-win-port | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-working-activity | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| dshx-update-check | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| ex-setting | 未知 | 无补丁 | 缺: tuiPrompt | 9 项匹配 | 兼容 |
| group-chat-diary | 未知（非 commit 锚定: YYYY-MM-DD） | 不适用 | 不适用 | 不适用 | 不适用 |
| hub | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| issues | 未知 | 不适用 | 不适用 | 不适用 | 不适用 |
| marisa | 未知（非 commit 锚定: snapshot-20260807T130646Z） | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 关注 |
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（4 个补丁中 0 个 OK） | 缺: tuiPrompt | 12 项匹配 | 需适配 |
| qqbot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| Qwen-MM-Plugins | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| Recall | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| review-panel | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-mxc | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| session-chatlog | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| session-persistence-rdb | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 已删除 |
| telegram | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| tg-bot | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 12 项匹配 | 兼容 |
| toybox | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| turtle-ui | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 21 项匹配 | 需适配 |
| web-components | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| dsh-web-ui-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-web-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-evolve | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-island | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-drag-and-drop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-message-edit | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-deep-research | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-multimedia-webui-input | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| repo-visibility-guard | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-grok-tui | 未知 | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 未知（待调研） |
| ds_web_craw | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| fabric | 未知 | 无补丁 | 缺: tuiPrompt | 8 项匹配 | 未知（待调研） |
| dsh-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 未知（待调研） |
| dsh-desktop-mac | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-public-repo-monitor | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tui | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-inspect | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-hub | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-alphasolve | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| zotero-wave-rag | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| onboarding | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| ego-browser | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-nowledge-mem | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-sidechain | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-a2a | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 19 项匹配 | 未知（待调研） |
| dsh-feishu-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-remote | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| mstar-workflow | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 未知（待调研） |
| dsh-scholar | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-issue-like-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-csv | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-tool-regex | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-session-repair-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| DSH-better-sidebar | 未知 | 无补丁 | 缺: tuiPrompt | 11 项匹配 | 未知（待调研） |
| dsh-session-hub | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-ica | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-advisor | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-llm-fallbacks | 未知 | OK（2 个补丁全部干净应用） | 缺: tuiPrompt | 8 项匹配 | 兼容 |
| dsh-web-workflow-visualizer | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-checkpoint | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 未知（待调研） |
| dsh-rewind | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| official-plugins-port | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| oh-my-dsh | 未知 | 无补丁 | 缺: tuiPrompt | 2167 项匹配 | 未知（待调研） |
| dsh-side-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-profile-bundle-example | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plan-execute | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 13 项匹配 | 未知（待调研） |
| dsh-paste-input | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| zotero-harvest | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| zephyr | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-bash-encoding | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-skill-stats | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-web-archive | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| sandbox-micro | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 未知（待调研） |
| dsh-git-identity | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-android | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-lazyfish | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-auto-approval | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-crew | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-input-history | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-client-ui-plan-execute | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 未知（待调研） |
| dsh-stickers | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| deep-standard-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-serenity-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 未知（待调研） |
| dsh-toolkit | 未知 | 无补丁 | 缺: tuiPrompt | 11 项匹配 | 未知（待调研） |
| dsh-tool-markdown | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-session-health | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-desktop-tools | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-reuse-first | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plus | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-session-cluster | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| DSH-UI4A | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-visualize | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-tps | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| dsh-plugin-check | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-plugin-dev | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-gomoku | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-101 | 未知 | 无补丁 | 缺: tuiPrompt | 16 项匹配 | 未知（待调研） |
| dsh-turn-rewind | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-genui | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 8 项匹配 | 兼容 |
| dsh-mygo | 未知 | 无补丁 | 缺: tuiPrompt | 8 项匹配 | 未知（待调研） |
| cross-harness-cite | 未知 | 无补丁 | 缺: tuiPrompt | 15 项匹配 | 未知（待调研） |
| dsh-split-panes | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| dsh-task-board | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-activity-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-diff | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-git-graph | 未知 | 无补丁 | 缺: tuiPrompt | 10 项匹配 | 未知（待调研） |
| dsh-mobileweb-adapter | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-desktop-electron | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-mineru | 未知 | 无补丁 | 缺: tuiPrompt | 8 项匹配 | 未知（待调研） |
| dsh-pet | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-paseo | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 未知（待调研） |
| dsh-remote-web-ui | 未知 | 无补丁 | 缺: tuiPrompt | 8 项匹配 | 未知（待调研） |
| dsh-superpowers | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-spec-kit | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-context7 | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-vscode | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tui-front-door | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-webbridge | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 未知（待调研） |
| dsh-custom-css | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| tonghuashun-harness | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-club | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-humanize | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-agent-budget | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-involute | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-spur | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-selection-chat | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-browser-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-engram-relay | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| yet-another-subagent | 未知 | 无补丁 | 缺: tuiPrompt | 17 项匹配 | 未知（待调研） |
| dsh-voice-chat | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-ads | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-skill-session-recovery | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tavern-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |

## mainline 变更分析（1c4950ab71fa4d128c749d9b22af17373edddb73 → 1c4950a）

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
| `ThemeService` | 出现 | 出现 | 出现 → 出现（稳定） |
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
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### deepseek-harness-desktop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### deepseek-harness-distro
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### distill
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-acp
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-agent-session-sources
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-artifact
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-cc-tui
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 12 项匹配），建议确认所依赖的宿主面当日是否仍满足。
### dsh-coding-receipt
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
- 输入来自 DSH session log，建议在 mainline 会话持久化格式稳定后实现。
### dsh-companion
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-cordis-examples
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-desktop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-feishu-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-gh-bridge
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-github-integration
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-issue-filer
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-live-stats
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-memory-evolve
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-my-rsi
- 兼容：锚定 c97643832821746b816d80d498e8a66fbb9db895（未知（不同谱系））、补丁「OK（1 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 c97643832821746b816d80d498e8a66fbb9db895 显式记录到 README/补丁头，快照一漂即可自动预警。
### dsh-opencode-server
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-pi-adapter
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-prompt-studio
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-pty-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-session-search
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-sfw
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-shell-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-skills-manager
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 无 dsh-* 依赖），建议确认所依赖的宿主面当日是否仍满足。
### dsh-skins
- 兼容：锚定 8abbd65a（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-subagent-tree
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（1c4950a）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-tool-browser
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-calculator
- 兼容：锚定 25b2ad4f67（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-encoding
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-json
- 兼容：锚定 25b2ad4f67（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-time
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-ui-progress
- 兼容：锚定 ce1fc03f95（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-ui-whale
- 兼容：锚定 ce1fc03f95（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-vision
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
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
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（1c4950a）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dshx-update-check
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ex-setting
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### group-chat-diary
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### hub
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### issues
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### marisa
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 2 项匹配），建议确认所依赖的宿主面当日是否仍满足。
### plugin-registry
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（4 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（1c4950a）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### qqbot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### Qwen-MM-Plugins
- 兼容：锚定 b4b67f0（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### Recall
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### review-panel
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-mxc
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### session-chatlog
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### session-persistence-rdb
- 兼容：锚定 未知（未知）、补丁「不适用（空仓库）」，当日 mainline 可干净集成。
- 建议把补丁基线从 未知 显式记录到 README/补丁头，快照一漂即可自动预警。
### telegram
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### tg-bot
- 兼容：锚定 fa3d357fc66102d82f0ddbf67fd3d5d70944d8f7（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### toybox
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### turtle-ui
- 需适配：锚定 a6fedc9e3b36d066e34860d040db6df47d88c432（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（1c4950a）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### web-components
- 兼容：锚定 b4b67f0（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
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
- 兼容：锚定 279244acb0（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
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
- 兼容：锚定 7f25d3e98c（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-alphasolve
- 兼容：锚定 279244acb0（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
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
- 兼容：锚定 未知（未知）、补丁「OK（2 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 未知 显式记录到 README/补丁头，快照一漂即可自动预警。
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
- 兼容：锚定 7f25d3e98c（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### zotero-harvest
- 未建模/状态未知：尚无 research/zotero-harvest.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### zephyr
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-bash-encoding
- 兼容：锚定 7f25d3e98c（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
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
### dsh-crew
- 未建模/状态未知：尚无 research/dsh-crew.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-input-history
- 兼容：锚定 7f25d3e98c（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
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
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（1c4950a）为新基线重新锚定/rebuild 补丁。
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
- 兼容：锚定 7f25d3e98c（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-mygo
- 未建模/状态未知：尚无 research/dsh-mygo.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### cross-harness-cite
- 未建模/状态未知：尚无 research/cross-harness-cite.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-split-panes
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（1c4950a）为新基线重新锚定/rebuild 补丁。
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
### dsh-involute
- 未建模/状态未知：尚无 research/dsh-involute.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
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

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
