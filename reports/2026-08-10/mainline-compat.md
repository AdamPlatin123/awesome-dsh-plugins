# mainline 兼容性报告（2026-08-10）

- mainline：`1c4950a`（snapshots/20260809T140917Z）
- 上次对比：`0882344227593b67a3f6459f791162d1eeeafd25`
- 兼容性：73/168 无需适配，6 需适配（dsh-subagent-tree dsh-working-activity plugin-registry turtle-ui dsh-tps dsh-split-panes）；其中关注 3、占位 9、不适用 2、已删除 1、未知 88

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
| dsh-cc-tui | 未知 | 无补丁 | 缺: tuiPrompt | 9 项匹配 | 关注 |
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
| dsh-a2a | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 18 项匹配 | 未知（待调研） |
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
| dsh-llm-fallbacks | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
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
| dsh-mygo | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 未知（待调研） |
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

## mainline 变更分析（0882344227593b67a3f6459f791162d1eeeafd25 → 1c4950a）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **包级变化**：packages/ 下删除 13 个包目录、新增 14 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：packages/cordis/repository-plugin packages/sdk/scripts packages/sdk/sdk-client packages/sdk/sdk-protocol packages/session-persistence/session-persistence packages/session-persistence/session-persistence-sqlite packages/session-projection/session-projection packages/telemetry/session-telemetry packages/telemetry/session-telemetry-otel packages/ui/app-boot packages/ui/jsonrpc packages/ui/tool-ask-user packages/ui/user-approval packages/ui/user-interaction

新增文件：
```
packages/boot/README.md
packages/boot/README.zh.md
packages/boot/app-boot/README.i18n.yaml
packages/client/runtime/src/client/contract/conversation.ts
packages/client/runtime/src/client/conversation/definition-registry.ts
packages/client/runtime/src/client/conversation/event-registry.ts
packages/client/runtime/src/client/conversation/view-registry.ts
packages/client/runtime/src/client/sessions/conversation-assembler.ts
packages/client/runtime/src/client/sessions/conversation-location-index.ts
packages/client/runtime/src/client/sessions/queue-mirror.ts
packages/client/runtime/tests/conversation-assembler.spec.ts
packages/client/runtime/tests/conversation-registry.spec.ts
packages/client/ui-conversation/src/client/chat/AssistantNodeView.tsx
packages/client/ui-conversation/src/client/chat/ChatNodeSeat.tsx
packages/client/ui-conversation/src/client/chat/CommandNodeView.tsx
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
 packages/AGENTS.md                                 |    2 +-
 packages/README.i18n.yaml                          |    4 +-
 packages/README.md                                 |   30 +-
 packages/README.zh.md                              |   86 +-
 packages/acp/README.i18n.yaml                      |    4 +-
 packages/acp/README.md                             |    4 +-
 packages/acp/README.zh.md                          |    4 +-
 packages/acp/acp/README.i18n.yaml                  |    2 +-
 packages/acp/acp/README.zh.md                      |    6 +-
 packages/acp/acp/src/index.ts                      |    4 +-
 packages/acp/acp/tsconfig.json                     |    2 +-
 packages/api/README.i18n.yaml                      |    2 +-
 packages/api/README.zh.md                          |    4 +-
 packages/api/gateway/README.i18n.yaml              |    2 +-
 packages/api/gateway/README.zh.md                  |    4 +-
 packages/api/remotes/README.i18n.yaml              |    2 +-
 packages/api/remotes/README.zh.md                  |    2 +-
 packages/api/remotes/tsconfig.host.json            |    2 +-
 packages/bash/README.i18n.yaml                     |    4 +-
 packages/bash/README.md                            |    4 +-
 packages/bash/README.zh.md                         |    4 +-
 packages/bash/bash-env/README.i18n.yaml            |    2 +-
 packages/bash/bash-env/README.zh.md                |    2 +-
 packages/bash/bash-env/tests/bash-env.spec.ts      |    1 +
 packages/bash/bash-env/tsconfig.json               |    2 +-
 packages/bash/bash-local/README.i18n.yaml          |    4 +-
 packages/bash/bash-local/README.md                 |    2 +-
 packages/bash/bash-local/README.zh.md              |    2 +-
 packages/bash/bash-local/src/index.ts              |    4 +-
 packages/bash/bash-sandbox/README.i18n.yaml        |    4 +-
 packages/bash/bash-sandbox/README.md               |    8 +-
 packages/bash/bash-sandbox/README.zh.md            |   10 +-
 packages/bash/bash-sandbox/src/helpers.ts          |    2 +-
 packages/bash/bash-sandbox/src/index.ts            |    2 +-
 .../bash-sandbox/tests/partial-landlock.spec.ts    |    2 +-
 packages/bash/bash-sandbox/tests/sandbox.spec.ts   |    4 +-
 packages/bash/bash/README.i18n.yaml                |    4 +-
 packages/bash/bash/README.md                       |   16 +-
 packages/bash/bash/README.zh.md                    |   16 +-
 packages/bash/bash/src/index.ts                    |    2 +-
 packages/bash/bash/src/invariant.ts                |    2 +-
 packages/bash/pwsh-local/README.i18n.yaml          |    4 +-
 packages/bash/pwsh-local/README.md                 |    2 +-
 packages/bash/pwsh-local/README.zh.md              |    6 +-
 packages/bash/pwsh-local/src/index.ts              |    4 +-
 packages/bash/pwsh-local/tests/executor.spec.ts    |    2 +
 packages/bash/tool-bash/README.i18n.yaml           |    4 +-
 packages/bash/tool-bash/README.md                  |    6 +-
 packages/bash/tool-bash/README.zh.md               |   12 +-
 packages/bash/tool-bash/src/index.ts               |    4 +-
 packages/bash/tool-bash/tests/integration.spec.ts  |    2 +-
 packages/bash/tool-bash/tsconfig.json              |    2 +-
 packages/bash/tool-pwsh/README.i18n.yaml           |    2 +-
 packages/bash/tool-pwsh/README.zh.md               |    6 +-
 packages/bash/tool-pwsh/src/background.ts          |    2 +-
 packages/bash/tool-pwsh/src/index.ts               |    4 +-
 packages/{ui => boot}/README.i18n.yaml             |    6 +-
 packages/boot/README.md                            |   11 +
 packages/boot/README.zh.md                         |   11 +
 packages/boot/app-boot/README.i18n.yaml            |    6 +
 packages/{ui => boot}/app-boot/README.md           |    4 +-
 packages/{ui => boot}/app-boot/README.zh.md        |   30 +-
 packages/{ui => boot}/app-boot/package.json        |    0
 packages/{ui => boot}/app-boot/src/index.ts        |   20 +-
 packages/{ui => boot}/app-boot/src/invariant.ts    |    0
 packages/{ui => boot}/app-boot/src/profile.ts      |   45 +-
 .../{ui => boot}/app-boot/tests/app-boot.spec.ts   |    0
 .../app-boot/tests/config-dump.spec.ts             |   12 +-
 .../app-boot/tests/config-reload.spec.ts           |    4 +-
 .../{ui => boot}/app-boot/tests/hmr-config.spec.ts |    2 +-
 .../{ui => boot}/app-boot/tests/profile.spec.ts    |   29 +-
 .../app-boot/tests/repository-cache.spec.ts        |   71 +-
 .../app-boot/tests/user-patches.spec.ts            |    2 +-
 packages/{ui => boot}/app-boot/tsconfig.json       |    0
 packages/{ui => boot}/app-boot/tsdown.config.ts    |    0
 packages/bundle/README.i18n.yaml                   |    4 +-
 packages/bundle/README.md                          |    4 +-
 packages/bundle/README.zh.md                       |    4 +-
 packages/bundle/base/README.i18n.yaml              |    4 +-
 packages/bundle/base/README.md                     |    2 +-
 packages/bundle/base/README.zh.md                  |    2 +-
 packages/bundle/base/cordis.patch.yml              |    8 +
 packages/bundle/base/package.json                  |    1 +
 packages/bundle/headless/README.i18n.yaml          |    4 +-
 packages/bundle/headless/README.md                 |   10 +-
 packages/bundle/headless/README.zh.md              |   10 +-
 packages/bundle/headless/cordis.patch.yml          |   31 +-
 packages/bundle/headless/package.json              |   11 +-
 packages/bundle/headless/src/index.ts              |  215 +--
 packages/bundle/headless/tests/headless.spec.ts    |  352 ++--
 packages/bundle/headless/tsconfig.json             |    6 +-
 packages/bundle/web-app/README.i18n.yaml           |    4 +-
 packages/bundle/web-app/README.md                  |    2 +-
 packages/bundle/web-app/README.zh.md               |    6 +-
 packages/bundle/web-app/cordis.patch.yml           |    6 +-
 packages/bundle/web-app/src/index.ts               |    2 +-
 packages/bundle/web-app/tests/web-app.spec.ts      |    4 +-
 packages/client/AGENTS.md                          |    8 +-
 packages/client/README.i18n.yaml                   |    4 +-
 packages/client/README.md                          |    2 +
 packages/client/README.zh.md                       |   12 +-
 packages/client/connection/README.i18n.yaml        |    4 +-
 packages/client/connection/README.md               |    2 +-
 packages/client/connection/README.zh.md            |    4 +-
 packages/client/connection/src/client/api.ts       |    4 +-
 packages/client/connection/src/client/fixture.ts   |   74 +-
 packages/client/connection/src/client/index.ts     |    2 +-
 packages/client/connection/src/rpc-host.ts         |    2 +-
 packages/client/connection/tests/fake-api.ts       |   15 +-
 packages/client/connection/tests/fixture.spec.ts   |    2 +-
 packages/client/connection/tsconfig.json           |    6 +-
 packages/client/hmr/README.i18n.yaml               |    2 +-
 packages/client/hmr/README.zh.md                   |    2 +-
 packages/client/locale/src/client/index.ts         |    2 +-
 packages/client/locale/tests/locale.spec.ts        |    2 +-
 packages/client/modules/README.i18n.yaml           |    4 +-
 packages/client/modules/README.md                  |    2 +-
 packages/client/modules/README.zh.md               |    4 +-
 packages/client/modules/src/client/manifest.ts     |   16 +-
 packages/client/modules/src/client/system.ts       |    8 +-
 packages/client/modules/tests/loader.spec.ts       |    2 +-
 packages/client/runtime/README.i18n.yaml           |    4 +-
 packages/client/runtime/README.md                  |   18 +-
 packages/client/runtime/README.zh.md               |   16 +-
 packages/client/runtime/package.json               |    4 +-
 .../runtime/src/client/contract/conversation.ts    |  265 +++
 .../client/runtime/src/client/contract/sessions.ts |    2 +-
 .../src/client/conversation/definition-registry.ts |   60 +
 .../src/client/conversation/event-registry.ts      |   56 +
 .../src/client/conversation/view-registry.ts       |   26 +
 packages/client/runtime/src/client/index.ts        |   39 +-
 .../src/client/sessions/assistant-timing.ts        |    7 +-
 .../src/client/sessions/context-provenance.ts      |    2 +-
 .../src/client/sessions/conversation-assembler.ts  |  799 +++++++++
 .../client/sessions/conversation-location-index.ts |  516 ++++++
 .../runtime/src/client/sessions/conversation.ts    |  115 +-
 .../runtime/src/client/sessions/failure-display.ts |    2 +-
 .../client/runtime/src/client/sessions/manager.ts  |   15 +-
 .../client/runtime/src/client/sessions/partial.ts  |    9 +-
 .../src/client/sessions/projection-store.ts        |    2 +-
 .../runtime/src/client/sessions/queue-mirror.ts    |   74 +
 .../src/client/sessions/request-inspection.ts      |  108 +-
 .../client/runtime/src/client/sessions/service.ts  |   42 +-
 .../client/runtime/src/client/sessions/session.ts  |  472 +-----
 .../src/client/sessions/steering-history.ts        |    7 +-
 .../runtime/src/client/sessions/tool-call-tree.ts  |   24 +-
 .../src/client/sessions/transcript-adapter.ts      |  409 -----
 packages/client/runtime/src/client/slots.ts        |    4 +-
 .../runtime/src/client/workspaces/workspace.ts     |    2 +-
 packages/client/runtime/tests/client-apply.spec.ts |   29 +-
 .../runtime/tests/compact-checkpoint-pin.spec.ts   |   52 -
 .../runtime/tests/conversation-assembler.spec.ts   |  959 +++++++++++
 .../runtime/tests/conversation-registry.spec.ts    |  126 ++
 packages/client/runtime/tests/event-script.ts      |    6 +-
 packages/client/runtime/tests/fake-api.ts          |   10 +-
 packages/client/runtime/tests/history-fold.spec.ts |    2 +-
 packages/client/runtime/tests/manager.spec.ts      |    2 +-
 .../client/runtime/tests/projection-store.spec.ts  |    2 +-
 packages/client/runtime/tests/queue-store.spec.ts  |    1 -
 packages/client/runtime/tests/session.spec.ts      |  850 +++-------
 .../client/runtime/tests/slots-service.spec.ts     |    8 +-
 .../runtime/tests/transcript-adapter.spec.ts       |  567 -------
 packages/client/runtime/tsconfig.json              |   12 +-
 packages/client/schema-form/README.i18n.yaml       |    4 +-
 packages/client/schema-form/README.md              |    2 +-
 packages/client/schema-form/README.zh.md           |    6 +-
 packages/client/test-runtime/README.i18n.yaml      |    2 +-
 packages/client/test-runtime/README.zh.md          |   10 +-
 packages/client/test-runtime/src/fixtures.ts       |    2 +
 packages/client/test-runtime/src/index.ts          |   16 +-
 packages/client/test-runtime/src/sessions.ts       |    2 +-
 .../client/test-runtime/tests/runtime.spec.tsx     |    3 +-
 packages/client/ui-command/README.i18n.yaml        |    2 +-
 packages/client/ui-command/README.zh.md            |    4 +-
 packages/client/ui-conversation/README.i18n.yaml   |    4 +-
 packages/client/ui-conversation/README.md          |   12 +-
 packages/client/ui-conversation/README.zh.md       |   16 +-
 packages/client/ui-conversation/package.json       |   10 +
 .../client/ui-conversation/src/client/apply.ts     |   39 +-
 .../src/client/chat/AssistantMarkdown.tsx          |   65 +-
 .../src/client/chat/AssistantNodeView.tsx          |   32 +
 .../src/client/chat/ChatNodeSeat.tsx               |   60 +
 .../src/client/chat/ChatView.module.css            |   14 +-
 .../ui-conversation/src/client/chat/ChatView.tsx   |  303 +---
 .../src/client/chat/CommandNodeView.tsx            |   40 +
 .../src/client/chat/CompactionItem.tsx             |    2 +-
 .../src/client/chat/ContextBody.module.css         |    2 +-
 .../src/client/chat/ContextBody.tsx                |    8 +-
 .../src/client/chat/ContextInjectionRow.tsx        |    2 +-
 .../src/client/chat/MessageItem.tsx                |  126 +-
 .../ui-conversation/src/client/chat/StatsLine.tsx  |    4 +-
 .../src/client/chat/TurnTailNodeView.module.css    |    9 +
 .../src/client/chat/TurnTailNodeView.tsx           |   45 +
 .../ui-conversation/src/client/chat/chat-flow.ts   |  214 ---
 .../src/client/chat/register-node-renderers.ts     |   46 +
 .../src/client/chat/tool-node-reader.ts            |   46 +
 .../src/client/chat/turn-assistant.ts              |   10 +
 .../src/client/chat/turn-metrics.ts                |    6 +-
 .../src/client/contract/chat-nodes.ts              |   82 +
 .../ui-conversation/src/client/contract/slots.ts   |  124 +-
 .../src/client/conversation-nodes/assistant.ts     |  316 ++++
 .../conversation-nodes/chat-snapshot-builder.ts    |  459 +++++
 .../src/client/conversation-nodes/command.ts       |  229 +++
 .../src/client/conversation-nodes/common.ts        |   65 +
 .../src/client/conversation-nodes/compaction.ts    |   65 +
 .../src/client/conversation-nodes/fallback.ts      |   40 +
 .../src/client/conversation-nodes/inbox.ts         |   70 +
 .../src/client/conversation-nodes/message.ts       |   83 +
 .../src/client/conversation-nodes/register.ts      |   30 +
 .../src/client/conversation-nodes/retry.ts         |   96 ++
 .../src/client/conversation-nodes/tool.ts          |  277 +++
 .../src/client/conversation-nodes/turn-error.ts    |  113 ++
 .../src/client/conversation-nodes/turn-tail.ts     |  196 +++
 .../client/ui-conversation/src/client/index.ts     |   17 +-
 .../ui-conversation/src/client/input/facade.ts     |    2 +-
 .../client/ui-conversation/src/client/locales.ts   |    2 +
 .../ui-conversation/src/client/queue/QueueDock.tsx |    2 +-
 .../src/client/skeleton/ApprovalPanel.tsx          |    9 +-
 .../src/client/skeleton/ConversationSession.tsx    |    2 +-
 .../src/client/skeleton/DetailsPanel.tsx           |   27 +-
 .../src/client/skeleton/InputBar.module.css        |    2 +-
 .../src/client/skeleton/InputBar.tsx               |   51 +-
 packages/client/ui-conversation/src/invariant.ts   |    2 +-
 .../ui-conversation/tests/chat-apply.spec.tsx      |   12 +-
 .../tests/chat-branch-tails.spec.tsx               |  167 +-
 .../ui-conversation/tests/chat-snapshot-fixture.ts |  298 ++++
 .../ui-conversation/tests/chat-stats.spec.tsx      |   30 +-
 .../ui-conversation/tests/chat-view.spec.tsx       |  540 +++---
 .../tests/conversation-node-definitions.spec.ts    |  862 ++++++++++
 .../tests/gate-branch-tails.spec.tsx               |   20 +-
 .../ui-conversation/tests/input-bar.spec.tsx       |   57 +-
 .../ui-conversation/tests/input-matrix.spec.tsx    |    5 +-
 .../ui-conversation/tests/input-scenarios.spec.tsx |    7 +-
 .../ui-conversation/tests/queue-dock.spec.tsx      |    4 +-
 .../tests/selection-survival.spec.tsx              |    2 +-
 .../client/ui-conversation/tests/skeleton.spec.tsx |    5 +-
 .../tests/views-type-chain.spec.tsx                |    2 +-
 packages/client/ui-conversation/tsconfig.json      |   16 +-
 packages/client/ui-deliverables/README.i18n.yaml   |    4 +-
 packages/client/ui-deliverables/README.md          |    6 +-
 packages/client/ui-deliverables/README.zh.md       |   10 +-
 .../ui-deliverables/src/client/ProducedFiles.tsx   |    7 +-
 .../client/ui-deliverables/src/client/index.ts     |   32 +-
 .../src/client/turn-deliverables.ts                |  186 +-
 .../ui-deliverables/tests/produced-files.spec.tsx  |  368 +++-
 packages/client/ui-layout/README.i18n.yaml         |    2 +-
 packages/client/ui-layout/README.zh.md             |    4 +-
 packages/client/ui-layout/src/client/index.ts      |    2 +-
 packages/client/ui-layout/src/client/service.ts    |    2 +-
 packages/client/ui-layout/tests/service.spec.ts    |    2 +-
 packages/client/ui-model/README.i18n.yaml          |    4 +-
 packages/client/ui-model/README.md                 |    8 +-
 packages/client/ui-model/README.zh.md              |   10 +-
 .../client/ui-model/src/client/ModelSelect.tsx     |   18 +-
 packages/client/ui-model/src/client/directory.ts   |   28 +-
 packages/client/ui-model/src/client/index.ts       |   22 +-
 packages/client/ui-model/src/client/slots.ts       |    8 +-
 .../client/ui-model/tests/browser-plugin.spec.ts   |    6 +-
 .../client/ui-model/tests/model-select.spec.tsx    |   10 +-
 packages/client/ui-models/README.i18n.yaml         |    2 +-
 packages/client/ui-models/README.zh.md             |    4 +-
 packages/client/ui-models/src/client/apiKey.ts     |    2 +-
 packages/client/ui-models/tests/styles.spec.ts     |    2 +-
 packages/client/ui-permission/tsconfig.json        |    2 +-
 packages/client/ui-primitives/README.i18n.yaml     |    4 +-
 packages/client/ui-primitives/README.md            |    2 +-
 packages/client/ui-primitives/README.zh.md         |   12 +-
 packages/client/ui-primitives/src/clipboard.ts     |    2 +-
 packages/client/ui-primitives/src/index.ts         |    2 +-
 .../src/markdown/MarkdownText.module.css           |   22 +
 .../ui-primitives/src/markdown/MarkdownText.tsx    |   26 +-
 .../ui-primitives/src/markdown/incremental.ts      |    2 +-
 .../client/ui-primitives/src/markdown/render.tsx   |   51 +-
 .../client/ui-primitives/tests/diff-block.spec.tsx |    2 +-
 .../tests/markdown-dom-parity.spec.tsx             |    2 +-
 .../tests/markdown-render-units.spec.tsx           |    3 +-
 .../client/ui-primitives/tests/markdown.spec.tsx   |   43 +
 .../ui-primitives/tests/terminal-block.spec.tsx    |    2 +-
 packages/client/ui-question/tsconfig.json          |    2 +-
 .../client/ui-settings-general/README.i18n.yaml    |    2 +-
 packages/client/ui-settings-general/README.zh.md   |    4 +-
 packages/client/ui-settings/README.i18n.yaml       |    2 +-
 packages/client/ui-settings/README.zh.md           |    2 +-
 packages/client/ui-settings/tests/apply.spec.ts    |   12 +-
 packages/client/ui-sidebar/README.i18n.yaml        |    2 +-
 packages/client/ui-sidebar/README.zh.md            |    4 +-
 .../client/ui-sidebar/src/client/contract/slots.ts |    2 +-
 packages/client/ui-skill/README.i18n.yaml          |    2 +-
 packages/client/ui-skill/README.zh.md              |    4 +-
 packages/client/ui-slash/README.i18n.yaml          |    2 +-
 packages/client/ui-slash/README.zh.md              |    4 +-
 packages/client/ui-slash/src/client/controller.ts  |    2 +-
 packages/client/ui-slots/README.i18n.yaml          |    4 +-
 packages/client/ui-slots/README.md                 |    6 +-
 packages/client/ui-slots/README.zh.md              |    6 +-
 packages/client/ui-slots/src/index.ts              |  204 ++-
 packages/client/ui-slots/src/renderer.ts           |   14 +-
 packages/client/ui-slots/tests/surface.spec.ts     |   11 +
 packages/client/ui-slots/tests/type-chain.spec.tsx |   60 +-
 packages/client/ui-subagent/README.i18n.yaml       |    4 +-
 packages/client/ui-subagent/README.md              |    4 +-
 packages/client/ui-subagent/README.zh.md           |    4 +-
 packages/client/ui-subagent/src/client/index.ts    |    6 +-
 .../ui-subagent/tests/browser-plugin.spec.ts       |    9 +-
 packages/client/ui-theme/README.i18n.yaml          |    2 +-
 packages/client/ui-theme/README.zh.md              |    6 +-
 .../ui-theme/src/client/settings-contract.ts       |    2 +-
 packages/client/ui-tool/README.i18n.yaml           |    4 +-
 packages/client/ui-tool/README.md                  |    4 +-
 packages/client/ui-tool/README.zh.md               |    8 +-
 packages/client/ui-tool/src/client/apply.ts        |    5 +-
 .../client/ui-tool/src/client/contract/slots.ts    |    4 +-
 .../ui-tool/src/client/tool/ToolCallTree.tsx       |    3 +-
 .../client/ui-tool/src/client/tool/ToolDetails.tsx |    2 +-
 .../ui-tool/src/client/tool/toolviews/todo-row.tsx |    2 +-
 .../ui-tool/src/client/tool/toolviews/web-row.tsx  |    2 +-
 .../ui-tool/tests/assembly-surfaces.spec.tsx       |    5 +-
 .../ui-tool/tests/chat-code-subcalls.spec.tsx      |   15 +-
 packages/client/ui-tool/tests/diff-card.spec.tsx   |    9 +-
 packages/client/ui-tool/tests/read-card.spec.tsx   |    7 +-
 packages/client/ui-tool/tests/search-card.spec.tsx |    7 +-
 .../client/ui-tool/tests/terminal-card.spec.tsx    |    7 +-
 .../client/ui-tool/tests/tool-call-tree.spec.tsx   |   17 +-
 .../client/ui-tool/tests/tool-details-render.tsx   |   45 +-
 .../client/ui-tool/tests/toolview-slot.spec.tsx    |    5 +-
 packages/client/ui-tool/tests/web-card.spec.tsx    |    7 +-
 packages/client/ui-trajectory/README.i18n.yaml     |    2 +-
 packages/client/ui-trajectory/README.zh.md         |    2 +-
 .../ui-trajectory/src/client/context-branches.ts   |    4 +-
 .../ui-trajectory/src/client/trajectory-record.ts  |    4 +-
 .../src/client/trajectory-virtual-rows.ts          |    2 +-
 packages/client/ui-workspace/README.i18n.yaml      |    2 +-
 packages/client/ui-workspace/README.zh.md          |   12 +-
 packages/client/web-react/src/scoped-slots.tsx     |  335 +++-
 .../client/web-react/tests/scoped-slots.spec.tsx   |   77 +-
 packages/client/web/README.i18n.yaml               |    4 +-
 packages/client/web/README.md                      |    4 +-
 packages/client/web/README.zh.md                   |    6 +-
 packages/client/web/src/boot.tsx                   |    8 +-
 packages/code-runtime/README.i18n.yaml             |    4 +-
 packages/code-runtime/README.md                    |    8 +-
 packages/code-runtime/README.zh.md                 |    8 +-
 .../code-runtime-worker/README.i18n.yaml           |    2 +-
 .../code-runtime/code-runtime-worker/README.zh.md  |    2 +-
 .../code-runtime/code-runtime-worker/src/index.ts  |    6 +-
 .../code-runtime/code-runtime/README.i18n.yaml     |    4 +-
 packages/code-runtime/code-runtime/README.md       |    8 +-
 packages/code-runtime/code-runtime/README.zh.md    |   14 +-
 packages/code-runtime/code-runtime/src/index.ts    |    6 +-
 packages/code-runtime/code-runtime/src/types.ts    |    2 +-
 .../code-runtime/tests/reserved.spec.ts            |    2 +-
 .../code-runtime/tests/service.spec.ts             |    2 +-
 packages/compact/README.i18n.yaml                  |    4 +-
 packages/compact/README.md                         |    4 +-
 packages/compact/README.zh.md                      |    6 +-
 packages/compact/command-compact/README.i18n.yaml  |    4 +-
 packages/compact/command-compact/README.md         |    2 +-
 packages/compact/command-compact/README.zh.md      |    4 +-
 packages/compact/command-compact/src/index.ts      |    2 +-
 .../command-compact/tests/command-compact.spec.ts  |   24 +-
 .../tests/loader-composition.spec.ts               |   30 +-
 packages/compact/command-compact/tsconfig.json     |    2 +-
 packages/compact/compact-basic/README.i18n.yaml    |    4 +-
 packages/compact/compact-basic/README.md           |   12 +-
 packages/compact/compact-basic/README.zh.md        |   12 +-
 packages/compact/compact-basic/package.json        |    2 +
 packages/compact/compact-basic/src/index.ts        |   13 +-
 packages/compact/compact-basic/src/region.ts       |   42 +-
 packages/compact/compact-basic/src/summarizer.ts   |    4 +-
 .../compact-basic/tests/compact-basic.spec.ts      |   10 +-
 .../compact-basic/tests/manual-compact.spec.ts     |   55 +-
 packages/compact/compact-basic/tsconfig.json       |    3 +
 .../compact/compact-tool-result-prune/src/index.ts |    2 +-
 .../compact/compact-tool-result-prune/src/types.ts |    2 +-
 .../tests/tool-result-prune.spec.ts                |    2 +-
 packages/compact/compact/README.i18n.yaml          |    4 +-
 packages/compact/compact/README.md                 |   30 +-
 packages/compact/compact/README.zh.md              |   34 +-
 packages/compact/compact/package.json              |    8 +
 packages/compact/compact/src/brand.ts              |   13 +
 packages/compact/compact/src/checkpoint.ts         |   44 +-
 packages/compact/compact/src/index.ts              |   20 +-
 packages/compact/compact/src/invariant.ts          |   93 +-
 packages/compact/compact/src/types.ts              |   20 +-
 packages/compact/compact/tests/compact.spec.ts     |   17 +-
 packages/compact/compact/tests/invariant.spec.ts   |  194 ++-
 packages/compact/compact/tsconfig.json             |    6 +
 packages/compact/compact/tsdown.config.ts          |   13 +
 packages/context/README.i18n.yaml                  |    4 +-
 packages/context/README.md                         |    2 +
 packages/context/README.zh.md                      |    4 +-
 .../context/session-reference/README.i18n.yaml     |    2 +-
 packages/context/session-reference/README.zh.md    |    4 +-
 packages/context/session-reference/src/types.ts    |    2 +-
 .../tests/session-reference.spec.ts                |   15 +-
 packages/context/time-context/README.i18n.yaml     |    2 +-
 packages/context/time-context/README.zh.md         |    6 +-
 packages/context/tmux-context/README.i18n.yaml     |    4 +-
 packages/context/tmux-context/README.md            |    2 +-
 packages/context/tmux-context/README.zh.md         |    4 +-
 packages/context/tmux-context/src/index.ts         |    4 +-
 .../context/workspace-context/README.i18n.yaml     |    2 +-
 packages/context/workspace-context/README.zh.md    |    6 +-
 packages/context/workspace-context/src/state.ts    |    2 +-
 .../tests/workspace-context.spec.ts                |   14 +-
 packages/cordis/README.md                          |   10 -
 packages/cordis/README.zh.md                       |   10 -
 packages/cordis/repository-plugin/README.md        |  102 --
 packages/cordis/repository-plugin/README.zh.md     |  102 --
 packages/core/README.i18n.yaml                     |    4 +-
 packages/core/README.md                            |    7 +-
 packages/core/README.zh.md                         |    7 +-
 .../agent-default-model}/README.i18n.yaml          |    6 +-
 packages/core/agent-default-model/README.md        |   25 +
 packages/core/agent-default-model/README.zh.md     |   25 +
 packages/core/agent-default-model/package.json     |   44 +
 packages/core/agent-default-model/src/index.ts     |  107 ++
 packages/core/agent-default-model/src/invariant.ts |   30 +
 .../tests/agent-default-model.spec.ts              |   98 ++
 packages/core/agent-default-model/tsconfig.json    |   30 +
 packages/core/agent-default-model/tsdown.config.ts |   25 +
 packages/core/agent-loop/README.i18n.yaml          |    4 +-
 packages/core/agent-loop/README.md                 |   14 +-
 packages/core/agent-loop/README.zh.md              |   24 +-
 packages/core/agent-loop/src/agent.ts              |   45 +-
 packages/core/agent-loop/src/index.ts              |    2 +-
 packages/core/agent-loop/src/tool-calls.ts         |    4 +-
 packages/core/agent-loop/tests/agent.spec.ts       |    2 +-
 packages/core/agent-loop/tests/cancel.spec.ts      |  156 +-
 .../agent-loop/tests/contract-regressions.spec.ts  |    2 +-
 .../core/agent-loop/tests/interception.spec.ts     |    2 +-
 packages/core/agent-loop/tests/loop.spec.ts        |   75 +-
 packages/core/agent-loop/tests/mock-adapter.ts     |   18 +-
 .../core/agent-loop/tests/request-error.spec.ts    |    2 +-
 packages/core/agent-loop/tsconfig.json             |    2 +-
 packages/core/agent/README.i18n.yaml               |    4 +-
 packages/core/agent/README.md                      |   12 +-
 packages/core/agent/README.zh.md                   |   16 +-
 packages/core/agent/src/dispatch.ts                |    2 +-
 packages/core/agent/src/inbox.ts                   |    6 +-
 packages/core/agent/src/index.ts                   |    7 +-
 .../src/{llm-target.ts => model-selection.ts}      |   44 +-
 packages/core/agent/src/runtime-types.ts           |  292 ++++
 packages/core/agent/src/types.ts                   |  287 +---
 ...{llm-target.spec.ts => model-selection.spec.ts} |   14 +-
 packages/core/scope/README.i18n.yaml               |    4 +-
 packages/core/scope/README.md                      |    2 +-
 packages/core/scope/README.zh.md                   |    6 +-
 packages/core/session/README.i18n.yaml             |    4 +-
 packages/core/session/README.md                    |   18 +-
 packages/core/session/README.zh.md                 |   22 +-
 packages/core/session/src/index.ts                 |   10 +-
 packages/core/session/src/invariant.ts             |    2 +-
 packages/core/session/src/repair.ts                |    4 +-
 packages/core/session/src/surface.ts               |    4 +-
 packages/core/session/src/types.ts                 |   15 +-
 packages/core/session/tests/fork.spec.ts           |    2 +-
 .../session/tests/gen-persistence-catalog.spec.ts  |    8 +-
 packages/core/session/tests/session.spec.ts        |    2 +-
 packages/core/session/tests/surface.spec.ts        |    8 +-
 packages/core/system-prompt/README.i18n.yaml       |    4 +-
 packages/core/system-prompt/README.md              |    4 +-
 packages/core/system-prompt/README.zh.md           |    8 +-
 packages/core/tools/README.i18n.yaml               |    4 +-
 packages/core/tools/README.md                      |   12 +-
 packages/core/tools/README.zh.md                   |   22 +-
 packages/core/tools/package.json                   |    4 +
 packages/core/tools/src/code-mode.ts               |   41 +-
 packages/core/tools/src/index.ts                   |   18 +-
 packages/core/tools/src/invariant.ts               |   28 +
 packages/core/tools/src/presentation.ts            |    6 +-
 packages/core/tools/src/py-types.ts                |    2 +-
 packages/core/tools/src/types.ts                   |   58 +
 packages/core/tools/tests/code-mode.spec.ts        |    7 +-
 packages/core/tools/tests/gen-tool-catalog.spec.ts |    3 +-
 packages/core/tools/tests/invariant.spec.ts        |  105 +-
 packages/core/tools/tests/tools.spec.ts            |    4 +-
 packages/core/tools/tsconfig.json                  |    2 +-
 packages/credentials/README.i18n.yaml              |    4 +-
 packages/credentials/README.md                     |    2 +
 packages/credentials/README.zh.md                  |    2 +
 .../credentials/credentials-local/README.i18n.yaml |    4 +-
 packages/credentials/credentials-local/README.md   |    2 +-
 .../credentials/credentials-local/README.zh.md     |    4 +-
 .../credentials/credentials-local/src/invariant.ts |    2 +-
 packages/credentials/credentials/README.i18n.yaml  |    4 +-
 packages/credentials/credentials/README.md         |    2 +-
 packages/credentials/credentials/README.zh.md      |   22 +-
 packages/credentials/credentials/src/index.ts      |    2 +-
 packages/{sdk => e2b}/README.i18n.yaml             |    6 +-
 packages/e2b/README.md                             |   15 +
 packages/e2b/README.zh.md                          |   15 +
 packages/{timeout => e2b/e2b}/README.i18n.yaml     |    6 +-
 packages/e2b/e2b/README.md                         |   44 +
 packages/e2b/e2b/README.zh.md                      |   44 +
 packages/e2b/e2b/package.json                      |   41 +
 packages/e2b/e2b/src/index.ts                      |  182 ++
 packages/e2b/e2b/src/invariant.ts                  |   30 +
 packages/e2b/e2b/tests/composition.e2e.ts          |  184 ++
 packages/e2b/e2b/tests/e2b.spec.ts                 |  247 +++
 packages/e2b/e2b/tsconfig.json                     |   25 +
 .../{telemetry => e2b/fs-e2b}/README.i18n.yaml     |    6 +-
 packages/e2b/fs-e2b/README.md                      |   31 +
 packages/e2b/fs-e2b/README.zh.md                   |   31 +
 packages/e2b/fs-e2b/package.json                   |   39 +
 packages/e2b/fs-e2b/src/index.ts                   |  527 ++++++
 packages/e2b/fs-e2b/src/invariant.ts               |   30 +
 packages/e2b/fs-e2b/tests/filesystem.spec.ts       |  768 +++++++++
 packages/e2b/fs-e2b/tsconfig.json                  |   25 +
 .../subprocess-e2b}/README.i18n.yaml               |    6 +-
 packages/e2b/subprocess-e2b/README.md              |   43 +
 packages/e2b/subprocess-e2b/README.zh.md           |   43 +
 packages/e2b/subprocess-e2b/package.json           |   44 +
 packages/e2b/subprocess-e2b/src/environment.ts     |  104 ++
 packages/e2b/subprocess-e2b/src/index.ts           |  208 +++
 packages/e2b/subprocess-e2b/src/invariant.ts       |   30 +
 packages/e2b/subprocess-e2b/src/output.ts          |  131 ++
 packages/e2b/subprocess-e2b/src/process.ts         |  698 ++++++++
 packages/e2b/subprocess-e2b/src/remote.ts          |   97 ++
 packages/e2b/subprocess-e2b/src/terminal.ts        |  567 +++++++
 .../e2b/subprocess-e2b/tests/subprocess.spec.ts    | 1792 ++++++++++++++++++++
 packages/e2b/subprocess-e2b/tests/terminal.spec.ts |  926 ++++++++++
 packages/e2b/subprocess-e2b/tsconfig.json          |   30 +
 packages/examples/README.i18n.yaml                 |    2 +-
 packages/examples/README.zh.md                     |    8 +-
 packages/examples/acp-demo/tests/built-bin.e2e.ts  |    6 +-
 packages/examples/acp-demo/tsconfig.json           |    6 +-
 .../examples/agent-spine-demo/README.i18n.yaml     |    4 +-
 packages/examples/agent-spine-demo/README.md       |    4 +-
 packages/examples/agent-spine-demo/README.zh.md    |    6 +-
 .../agent-spine-demo/tests/agent-core.spec.ts      |    1 +
 packages/examples/agent-spine-demo/tsconfig.json   |    2 +-
 packages/examples/jsonrpc-demo/README.i18n.yaml    |    4 +-
 packages/examples/jsonrpc-demo/README.md           |    4 +-
 packages/examples/jsonrpc-demo/README.zh.md        |    4 +-
 packages/examples/jsonrpc-demo/tsconfig.json       |    2 +-
 packages/feedback/README.i18n.yaml                 |    4 +-
 packages/feedback/README.md                        |    2 +-
 packages/feedback/README.zh.md                     |    4 +-
 .../feedback/command-feedback/README.i18n.yaml     |    4 +-
 packages/feedback/command-feedback/README.md       |    6 +-
 packages/feedback/command-feedback/README.zh.md    |    8 +-
 packages/feedback/command-feedback/src/index.ts    |    2 +-
 packages/feedback/command-feedback/tsconfig.json   |    2 +-
 packages/fs/README.i18n.yaml                       |    4 +-
 packages/fs/README.md                              |   24 +-
 packages/fs/README.zh.md                           |   28 +-
 packages/fs/fs-local/README.i18n.yaml              |    4 +-
 packages/fs/fs-local/README.md                     |   13 +-
 packages/fs/fs-local/README.zh.md                  |   23 +-
 packages/fs/fs-local/src/fsio.ts                   |   92 +-
 packages/fs/fs-local/src/index.ts                  |   27 +-
 packages/fs/fs-local/tests/filesystem.spec.ts      |   64 +-
 packages/fs/fs-local/tests/fsio.spec.ts            |   73 +-
 packages/fs/fs-policy/README.i18n.yaml             |    4 +-
 packages/fs/fs-policy/README.md                    |   14 +-
 packages/fs/fs-policy/README.zh.md                 |   14 +-
 packages/fs/fs-policy/src/index.ts                 |   56 +-
 packages/fs/fs-policy/tests/policy.spec.ts         |   53 +-
 packages/fs/fs-sandbox/src/index.ts                |    6 +-
 packages/fs/fs/README.i18n.yaml                    |    4 +-
 packages/fs/fs/README.md                           |   36 +-
 packages/fs/fs/README.zh.md                        |   52 +-
 packages/fs/fs/src/index.ts                        |   56 +-
 packages/fs/fs/src/invariant.ts                    |   15 +-
 packages/fs/fs/src/types.ts                        |   11 +-
 packages/fs/fs/tests/invariant.spec.ts             |   21 +-
 packages/fs/fs/tests/service.spec.ts               |   10 +-
 packages/fs/tool-fs-search/README.i18n.yaml        |    2 +-
 packages/fs/tool-fs-search/README.zh.md            |    4 +-
 packages/fs/tool-fs-search/tests/tools.spec.ts     |    2 +
 packages/fs/tool-fs/README.i18n.yaml               |    4 +-
 packages/fs/tool-fs/README.md                      |    8 +-
 packages/fs/tool-fs/README.zh.md                   |   12 +-
 packages/fs/tool-fs/src/edit.ts                    |    4 +-
 packages/fs/tool-fs/src/read.ts                    |   11 +-
 packages/fs/tool-fs/src/session-cwd.ts             |    2 +-
 packages/fs/tool-fs/src/write.ts                   |    4 +-
 packages/fs/tool-fs/tests/integration.spec.ts      |   46 +-
 packages/fs/tool-fs/tests/tools.spec.ts            |    5 +
 packages/fs/tool-fs/tsconfig.json                  |    2 +-
 .../fs/tool-str-replace-editor/README.i18n.yaml    |    4 +-
 packages/fs/tool-str-replace-editor/README.md      |    2 +-
 packages/fs/tool-str-replace-editor/README.zh.md   |   10 +-
 packages/fs/tool-str-replace-editor/src/index.ts   |    9 +-
 .../fs/tool-str-replace-editor/tests/tools.spec.ts |   29 +
 packages/goal/README.i18n.yaml                     |    4 +-
 packages/goal/README.md                            |    4 +-
 packages/goal/README.zh.md                         |    4 +-
 packages/goal/command-goal/README.i18n.yaml        |    4 +-
 packages/goal/command-goal/README.md               |    2 +-
 packages/goal/command-goal/README.zh.md            |    6 +-
 packages/goal/command-goal/tsconfig.json           |    2 +-
 packages/goal/goal-session/README.i18n.yaml        |    4 +-
 packages/goal/goal-session/README.md               |    2 +-
 packages/goal/goal-session/README.zh.md            |    6 +-
 packages/goal/goal-session/src/index.ts            |    2 +-
 packages/goal/goal/README.i18n.yaml                |    4 +-
 packages/goal/goal/README.md                       |    4 +-
 packages/goal/goal/README.zh.md                    |    8 +-
 packages/goal/goal/src/domain.ts                   |    2 +-
 packages/goal/goal/tsconfig.json                   |    2 +-
 packages/goal/tool-goal/README.i18n.yaml           |    4 +-
 packages/goal/tool-goal/README.md                  |    2 +-
 packages/goal/tool-goal/README.zh.md               |    2 +-
 packages/guard/README.i18n.yaml                    |    4 +-
 packages/guard/README.md                           |    5 +-
 packages/guard/README.zh.md                        |    5 +-
 .../tests/repeat-tool-guard.spec.ts                |    2 +-
 .../timeout-policy/README.i18n.yaml                |    2 +-
 .../{timeout => guard}/timeout-policy/README.md    |    0
 .../{timeout => guard}/timeout-policy/README.zh.md |    0
 .../{timeout => guard}/timeout-policy/package.json |    0
 .../{timeout => guard}/timeout-policy/src/index.ts |   12 +-
 .../timeout-policy/src/invariant.ts                |    0
 .../timeout-policy/tests/timeout-policy.spec.ts    |    0
 .../timeout-policy/tsconfig.json                   |    0
 packages/hooks/README.i18n.yaml                    |    4 +-
 packages/hooks/README.md                           |    2 +-
 packages/hooks/README.zh.md                        |    4 +-
 packages/hooks/hook-protocol/README.i18n.yaml      |    4 +-
 packages/hooks/hook-protocol/README.md             |    6 +-
 packages/hooks/hook-protocol/README.zh.md          |   12 +-
 packages/hooks/hook-protocol/src/detached.ts       |    2 +-
 packages/hooks/hook-protocol/src/events.ts         |    2 +-
 packages/hooks/hook-protocol/src/index.ts          |    2 +-
 packages/hooks/hook-protocol/src/invariant.ts      |    4 +-
 packages/hooks/hook-protocol/src/merge.ts          |    2 +-
 packages/hooks/hook-protocol/src/runner.ts         |    2 +-
 packages/hooks/hook-protocol/src/types.ts          |   14 +-
 .../hooks/hook-protocol/tests/invariant.spec.ts    |    2 +-
 packages/hooks/hook-protocol/tests/runner.spec.ts  |    2 +-
 packages/hooks/hooks-claude/README.i18n.yaml       |    4 +-
 packages/hooks/hooks-claude/README.md              |   10 +-
 packages/hooks/hooks-claude/README.zh.md           |   10 +-
 packages/hooks/hooks-claude/src/index.ts           |   14 +-
 packages/hooks/hooks-claude/src/invariant.ts       |    2 +-
 .../hooks/hooks-claude/tests/coverage-cases.ts     |    2 +-
 packages/hooks/hooks-claude/tsconfig.json          |    2 +-
 packages/hooks/hooks-codex/README.i18n.yaml        |    4 +-
 packages/hooks/hooks-codex/README.md               |    8 +-
 packages/hooks/hooks-codex/README.zh.md            |    8 +-
 packages/hooks/hooks-codex/src/index.ts            |   12 +-
 packages/hooks/hooks-codex/src/invariant.ts        |    2 +-
 packages/hooks/hooks-codex/tests/coverage-cases.ts |    2 +-
 packages/hooks/hooks-codex/tsconfig.json           |    2 +-
 packages/host/README.i18n.yaml                     |    4 +-
 packages/host/README.md                            |    2 +
 packages/host/README.zh.md                         |    6 +-
 packages/host/apiproxy/README.i18n.yaml            |    4 +-
 packages/host/apiproxy/README.md                   |   22 +-
 packages/host/apiproxy/README.zh.md                |   34 +-
 packages/host/apiproxy/package.json                |    1 +
 packages/host/apiproxy/src/api-proxy.ts            |  156 +-
 packages/host/apiproxy/src/api/events.ts           |    2 +-
 packages/host/apiproxy/src/api/index.ts            |    5 +-
 packages/host/apiproxy/src/api/llm.ts              |    4 +-
 packages/host/apiproxy/src/api/rpc-map.ts          |    1 +
 packages/host/apiproxy/src/api/sessions.schema.ts  |   12 +-
 packages/host/apiproxy/src/api/sessions.ts         |   14 +-
 packages/host/apiproxy/src/api/subagents.schema.ts |   12 +
 packages/host/apiproxy/src/api/subagents.ts        |   18 +
 packages/host/apiproxy/src/fetch/client.ts         |    4 +
 packages/host/apiproxy/src/fetch/handler.ts        |    2 +
 packages/host/apiproxy/src/index.ts                |   97 +-
 packages/host/apiproxy/src/native-path-opener.ts   |    6 +-
 .../host/apiproxy/tests/api-proxy-approval.spec.ts |    4 +-
 .../host/apiproxy/tests/api-proxy-blank.spec.ts    |    2 +-
 .../host/apiproxy/tests/api-proxy-cold.spec.ts     |   28 +-
 .../host/apiproxy/tests/api-proxy-commands.spec.ts |    2 +-
 .../host/apiproxy/tests/api-proxy-config.spec.ts   |   19 +-
 .../apiproxy/tests/api-proxy-default-route.spec.ts |  108 --
 .../host/apiproxy/tests/api-proxy-fork.spec.ts     |    4 +-
 .../host/apiproxy/tests/api-proxy-models.spec.ts   |   26 +-
 .../apiproxy/tests/api-proxy-projections.spec.ts   |    2 +-
 .../host/apiproxy/tests/api-proxy-question.spec.ts |    2 +-
 .../host/apiproxy/tests/api-proxy-rename.spec.ts   |    2 +-
 .../host/apiproxy/tests/api-proxy-search.spec.ts   |    4 +-
 .../apiproxy/tests/api-proxy-subagents.spec.ts     |   59 +-
 .../host/apiproxy/tests/api-proxy-view.spec.ts     |   16 +-
 .../apiproxy/tests/api-proxy-workspace.spec.ts     |    2 +-
 .../host/apiproxy/tests/client-handler.spec.ts     |   29 +-
 packages/host/apiproxy/tests/fetch-carrier.spec.ts |    8 +
 packages/host/apiproxy/tests/rpc-schemas.spec.ts   |    2 +-
 packages/host/apiproxy/tsconfig.json               |   17 +-
 .../host/directory-picker-native/README.i18n.yaml  |    2 +-
 packages/host/directory-picker-native/README.zh.md |    4 +-
 .../directory-picker-native/src/native-picker.ts   |    2 +-
 .../src/win32-dialog-logic.ts                      |    2 +-
 .../directory-picker-native/src/win32-dialog.ts    |    2 +-
 packages/host/directory-picker/README.i18n.yaml    |    2 +-
 packages/host/directory-picker/README.zh.md        |    4 +-
 packages/host/directory-picker/src/index.ts        |    2 +-
 packages/host/directory-picker/src/invariant.ts    |    5 +-
 packages/host/frontend-static/README.i18n.yaml     |    2 +-
 packages/host/frontend-static/README.zh.md         |    2 +-
 packages/host/webserver/README.i18n.yaml           |    4 +-
 packages/host/webserver/README.md                  |    2 -
 packages/host/webserver/README.zh.md               |    4 +-
 packages/host/webserver/src/index.ts               |    2 +-
 packages/interaction/README.i18n.yaml              |    6 +
 packages/{ui => interaction}/README.md             |    8 +-
 packages/{ui => interaction}/README.zh.md          |   10 +-
 .../{ui => interaction}/commands/README.i18n.yaml  |    4 +-
 packages/{ui => interaction}/commands/README.md    |    0
 packages/{ui => interaction}/commands/README.zh.md |    6 +-
 packages/{ui => interaction}/commands/package.json |    4 +
 packages/{ui => interaction}/commands/src/brand.ts |    0
 packages/{ui => interaction}/commands/src/index.ts |   50 +-
 .../{ui => interaction}/commands/src/invariant.ts  |    4 +-
 packages/interaction/commands/src/types.ts         |   48 +
 .../commands/tests/commands.spec.ts                |    0
 .../commands/tests/invariant.spec.ts               |    0
 .../{ui => interaction}/commands/tsconfig.json     |    0
 .../permission/README.i18n.yaml                    |    2 +-
 packages/{ui => interaction}/permission/README.md  |    0
 .../{ui => interaction}/permission/README.zh.md    |    0
 .../{ui => interaction}/permission/package.json    |    0
 .../{ui => interaction}/permission/src/client.ts   |    0
 .../{ui => interaction}/permission/src/index.ts    |    6 +-
 .../permission/src/invariant.ts                    |    2 +-
 .../{ui => interaction}/permission/src/types.ts    |    0
 .../permission/tests/invariant.spec.ts             |    2 +-
 .../permission/tests/permission.spec.ts            |    4 +-
 .../permission/tests/projection.spec.ts            |    2 +-
 .../{ui => interaction}/permission/tsconfig.json   |    2 +-
 .../interaction/tool-ask-user/README.i18n.yaml     |    6 +
 .../{ui => interaction}/tool-ask-user/README.md    |    2 +-
 .../{ui => interaction}/tool-ask-user/README.zh.md |    4 +-
 .../{ui => interaction}/tool-ask-user/package.json |    0
 .../{ui => interaction}/tool-ask-user/src/index.ts |    4 +-
 .../tool-ask-user/src/invariant.ts                 |    0
 .../tool-ask-user/tests/tool-ask-user.spec.ts      |    0
 .../tool-ask-user/tsconfig.json                    |    0
 .../interaction/user-approval/README.i18n.yaml     |    6 +
 .../{ui => interaction}/user-approval/README.md    |    2 +-
 .../{ui => interaction}/user-approval/README.zh.md |    2 +-
 .../{ui => interaction}/user-approval/package.json |    0
 .../{ui => interaction}/user-approval/src/index.ts |    6 +-
 .../user-approval/src/invariant.ts                 |    2 +-
 .../{ui => interaction}/user-approval/src/types.ts |    0
 .../user-approval/tests/approval.spec.ts           |    6 +-
 .../user-approval/tests/invariant.spec.ts          |    0
 .../user-approval/tsconfig.json                    |    0
 .../user-approval/tsdown.config.ts                 |    0
 .../interaction/user-interaction/README.i18n.yaml  |    6 +
 .../{ui => interaction}/user-interaction/README.md |    4 +-
 .../user-interaction/README.zh.md                  |    6 +-
 .../user-interaction/package.json                  |    0
 .../user-interaction/src/index.ts                  |    4 +-
 .../user-interaction/src/invariant.ts              |    0
 .../user-interaction/src/types.ts                  |    0
 .../tests/user-interaction.spec.ts                 |    4 +-
 .../user-interaction/tsconfig.json                 |    0
 packages/llm/README.i18n.yaml                      |    4 +-
 packages/llm/README.md                             |    4 +-
 packages/llm/README.zh.md                          |    4 +-
 packages/llm/llm-deepseek/README.i18n.yaml         |    4 +-
 packages/llm/llm-deepseek/README.md                |    2 +-
 packages/llm/llm-deepseek/README.zh.md             |    6 +-
 packages/llm/llm-deepseek/src/adapter.ts           |   15 +-
 packages/llm/llm-deepseek/src/sse.ts               |   19 +-
 packages/llm/llm-deepseek/tests/adapter.spec.ts    |   34 +
 packages/llm/llm-deepseek/tests/sse.spec.ts        |   10 +
 packages/llm/llm-pi-ai/README.i18n.yaml            |    4 +-
 packages/llm/llm-pi-ai/README.md                   |    6 +-
 packages/llm/llm-pi-ai/README.zh.md                |    8 +-
 packages/llm/llm-pi-ai/src/adapter.ts              |    2 +-
 packages/llm/llm-pi-ai/tests/convert.spec.ts       |    2 +-
 packages/llm/llm-retry/README.i18n.yaml            |    4 +-
 packages/llm/llm-retry/README.md                   |    4 +-
 packages/llm/llm-retry/README.zh.md                |    4 +-
 packages/llm/llm-retry/package.json                |    2 +
 packages/llm/llm-retry/src/brand.ts                |   13 +
 packages/llm/llm-retry/src/history.ts              |    2 +-
 packages/llm/llm-retry/src/index.ts                |   47 +-
 packages/llm/llm-retry/src/invariant.ts            |   37 +-
 packages/llm/llm-retry/src/types.ts                |   23 +
 packages/llm/llm-retry/tests/invariant.spec.ts     |   73 +-
 packages/llm/llm-retry/tests/persistence.spec.ts   |    2 +
 packages/llm/llm-retry/tests/retry.spec.ts         |    2 +
 packages/llm/llm-retry/tsconfig.json               |    3 +
 packages/llm/llm/README.i18n.yaml                  |    4 +-
 packages/llm/llm/README.md                         |   10 +-
 packages/llm/llm/README.zh.md                      |   14 +-
 packages/llm/llm/src/call-config.ts                |    2 +-
 packages/llm/llm/src/error.ts                      |    2 +-
 packages/llm/llm/src/message.ts                    |    8 +-
 packages/llm/llm/src/retry-policy.ts               |    2 +-
 packages/llm/llm/tests/attribution.spec.ts         |    2 +-
 packages/llm/llm/tests/message.spec.ts             |    2 +-
 packages/llm/llm/tests/service.spec.ts             |    2 +-
 packages/llm/token-meter/README.i18n.yaml          |    4 +-
 packages/llm/token-meter/README.md                 |    6 +-
 packages/llm/token-meter/README.zh.md              |   12 +-
 packages/llm/token-meter/src/index.ts              |    8 +-
 .../tests/context-breakdown-projection.spec.ts     |    2 +
 packages/llm/token-meter/tests/token-meter.spec.ts |    6 +-
 .../tests/token-usage-projection.spec.ts           |    2 +
 packages/llm/token-meter/tsconfig.json             |    2 +-
 packages/lsp/README.i18n.yaml                      |    4 +-
 packages/lsp/README.md                             |   14 +-
 packages/lsp/README.zh.md                          |   14 +-
 packages/lsp/lsp-local/README.i18n.yaml            |    4 +-
 packages/lsp/lsp-local/README.md                   |   18 +-
 packages/lsp/lsp-local/README.zh.md                |   18 +-
 packages/lsp/lsp-local/package.json                |    3 +
 packages/lsp/lsp-local/src/connection.ts           |   13 +-
 packages/lsp/lsp-local/src/host.ts                 |  194 +--
 packages/lsp/lsp-local/src/index.ts                |  197 ++-
 packages/lsp/lsp-local/src/instance.ts             |   24 +-
 packages/lsp/lsp-local/src/translate.ts            |    6 +-
 packages/lsp/lsp-local/tests/built-lib.e2e.ts      |    5 +-
 packages/lsp/lsp-local/tests/host.spec.ts          |   98 +-
 packages/lsp/lsp-local/tests/instance.spec.ts      |   38 +-
 packages/lsp/lsp-local/tests/lifecycle.spec.ts     |  151 +-
 packages/lsp/lsp-local/tests/provider.spec.ts      |   94 +-
 .../lsp/lsp-local/tests/typescript-server.e2e.ts   |    2 +
 packages/lsp/lsp-local/tsconfig.json               |    3 +
 packages/lsp/lsp/README.i18n.yaml                  |    4 +-
 packages/lsp/lsp/README.md                         |   10 +-
 packages/lsp/lsp/README.zh.md                      |   22 +-
 packages/lsp/lsp/src/index.ts                      |    2 +-
 packages/lsp/lsp/src/types.ts                      |   10 +-
 packages/lsp/lsp/tests/lsp.spec.ts                 |    8 +-
 packages/lsp/tool-lsp/README.i18n.yaml             |    4 +-
 packages/lsp/tool-lsp/README.md                    |    2 +-
 packages/lsp/tool-lsp/README.zh.md                 |   16 +-
 packages/lsp/tool-lsp/package.json                 |    2 +
 packages/lsp/tool-lsp/src/index.ts                 |    6 +-
 packages/lsp/tool-lsp/src/render.ts                |   61 +-
 packages/lsp/tool-lsp/tests/integration.spec.ts    |    2 +
 packages/lsp/tool-lsp/tests/render.spec.ts         |   53 +-
 packages/lsp/tool-lsp/tests/tool-lsp.spec.ts       |   11 +-
 packages/mcp/mcp-client/README.i18n.yaml           |    4 +-
 packages/mcp/mcp-client/README.md                  |    7 +-
 packages/mcp/mcp-client/README.zh.md               |   13 +-
 packages/mcp/mcp-client/src/index.ts               |   45 +-
 packages/mcp/mcp-client/src/tools.ts               |    8 +-
 packages/mcp/mcp-client/tests/apply.spec.ts        |   95 +-
 packages/mcp/mcp-client/tests/mcp-client.e2e.ts    |   35 +-
 packages/mcp/mcp-client/tests/mcp-client.spec.ts   |    6 +
 packages/plan/README.i18n.yaml                     |    4 +-
 packages/plan/README.md                            |    2 +
 packages/plan/README.zh.md                         |    2 +
 packages/plan/plan-mode/README.i18n.yaml           |    4 +-
 packages/plan/plan-mode/README.md                  |    2 +-
 packages/plan/plan-mode/README.zh.md               |    4 +-
 packages/plan/plan-mode/src/index.ts               |    2 +-
 packages/plan/plan-mode/tests/plan-mode.spec.ts    |    2 +-
 packages/plan/plan-mode/tsconfig.json              |    6 +-
 packages/pty/README.i18n.yaml                      |    4 +-
 packages/pty/README.md                             |   13 +-
 packages/pty/README.zh.md                          |   13 +-
 packages/pty/pty-local/README.i18n.yaml            |    4 +-
 packages/pty/pty-local/README.md                   |   12 +-
 packages/pty/pty-local/README.zh.md                |   12 +-
 packages/pty/pty-local/package.json                |    8 +-
 packages/pty/pty-local/src/index.ts                |   81 +-
 packages/pty/pty-local/src/sanitize.ts             |   37 +-
 packages/pty/pty-local/src/session.ts              |  443 +++--
 packages/pty/pty-local/tests/index.spec.ts         |  243 ++-
 packages/pty/pty-local/tests/local.spec.ts         |   61 +-
 packages/pty/pty-local/tests/sanitize.spec.ts      |    6 +-
 packages/pty/pty-local/tests/session.spec.ts       | 1057 ++++++++++--
 packages/pty/pty/README.i18n.yaml                  |    2 +-
 packages/pty/pty/README.zh.md                      |    4 +-
 packages/pty/pty/src/types.ts                      |    6 +-
 packages/pty/tool-bash-persistent/README.i18n.yaml |    2 +-
 packages/pty/tool-bash-persistent/README.zh.md     |    4 +-
 packages/pty/tool-bash-persistent/package.json     |    1 +
 .../tests/loader-composition.spec.ts               |    3 +
 packages/pty/tool-pty/package.json                 |    1 +
 .../pty/tool-pty/tests/loader-composition.spec.ts  |    3 +
 packages/sandbox/README.i18n.yaml                  |    4 +-
 packages/sandbox/README.md                         |    2 +
 packages/sandbox/README.zh.md                      |    2 +
 packages/sandbox/sandbox-local/README.i18n.yaml    |    2 +-
 packages/sandbox/sandbox-local/README.zh.md        |    4 +-
 packages/sandbox/sandbox-local/src/index.ts        |   15 +-
 packages/sandbox/sandbox-local/tests/local.spec.ts |    6 +-
 packages/sandbox/sandbox-policy/README.i18n.yaml   |    2 +-
 packages/sandbox/sandbox-policy/README.zh.md       |    4 +-
 .../sandbox/sandbox-policy/src/session-mode.ts     |    2 +-
 packages/sandbox/sandbox/README.i18n.yaml          |    4 +-
 packages/sandbox/sandbox/README.md                 |    6 +-
 packages/sandbox/sandbox/README.zh.md              |    6 +-
 packages/sandbox/sandbox/src/index.ts              |    2 +-
 packages/{cordis => scaffold}/README.i18n.yaml     |    6 +-
 packages/{sdk => scaffold}/README.md               |    9 +-
 packages/scaffold/README.zh.md                     |   17 +
 packages/scaffold/client/README.i18n.yaml          |    6 +
 .../{sdk/sdk-client => scaffold/client}/README.md  |    2 +-
 .../sdk-client => scaffold/client}/README.zh.md    |    2 +-
 .../sdk-client => scaffold/client}/package.json    |    0
 .../{sdk/sdk-client => scaffold/client}/src/api.ts |    4 +-
 .../sdk-client => scaffold/client}/src/client.ts   |    0
 .../sdk-client => scaffold/client}/src/dispose.ts  |    0
 .../sdk-client => scaffold/client}/src/index.ts    |    0
 .../client}/src/invariant.ts                       |    0
 .../sdk-client => scaffold/client}/src/types.ts    |    0
 .../client}/tests/dispose.spec.ts                  |    0
 .../client}/tests/fake-runtime.ts                  |    2 +-
 .../client}/tests/sdk-client.spec.ts               |    2 +-
 .../sdk-client => scaffold/client}/tsconfig.json   |    2 +-
 .../{sdk => scaffold}/create-sdk/README.i18n.yaml  |    2 +-
 packages/{sdk => scaffold}/create-sdk/README.md    |    0
 packages/{sdk => scaffold}/create-sdk/README.zh.md |    0
 packages/{sdk => scaffold}/create-sdk/package.json |    0
 packages/{sdk => scaffold}/create-sdk/src/args.ts  |    2 +-
 packages/{sdk => scaffold}/create-sdk/src/bin.ts   |    0
 .../{sdk => scaffold}/create-sdk/src/command.ts    |    4 +-
 .../create-sdk/src/create-questions.ts             |    4 +-
 .../create-sdk/src/create-wizard.ts                |    4 +-
 .../{sdk => scaffold}/create-sdk/src/headless.ts   |    6 +-
 packages/{sdk => scaffold}/create-sdk/src/index.ts |    0
 .../{sdk => scaffold}/create-sdk/src/invariant.ts  |    0
 .../create-sdk/src/project-scaffolder.ts           |    6 +-
 .../src/templates/assets/created.txt.tpl           |    0
 .../src/templates/assets/install-question.txt.tpl  |    0
 .../src/templates/assets/next-steps.txt.tpl        |    0
 .../src/templates/assets/setup-failure.txt.tpl     |    0
 .../create-sdk/src/templates/assets/usage.txt.tpl  |    0
 .../create-sdk/src/templates/create-templates.ts   |    0
 .../create-sdk/tests/built-artifacts.e2e.ts        |    4 +-
 .../create-sdk/tests/create.snapshot.ts            |    0
 .../create-sdk/tests/create.spec.ts                |    2 +-
 .../create-sdk/tests/link-workspace.e2e.ts         |    4 +-
 .../{sdk => scaffold}/create-sdk/tsconfig.json     |    0
 .../{sdk => scaffold}/create-sdk/tsdown.config.ts  |    0
 packages/{sdk => scaffold}/helper/README.i18n.yaml |    2 +-
 packages/{sdk => scaffold}/helper/README.md        |    0
 packages/{sdk => scaffold}/helper/README.zh.md     |    0
 packages/{sdk => scaffold}/helper/package.json     |    0
 .../helper/src/documents/cordis-yaml-file.ts       |    4 +-
 .../helper/src/documents/env-file.ts               |    4 +-
 .../helper/src/documents/package-json-file.ts      |    2 +-
 .../helper/src/documents/pnpm-workspace-file.ts    |    2 +-
 .../helper/src/documents/project-file.ts           |    0
 .../helper/src/documents/tsconfig-file.ts          |    6 +-
 .../helper/src/features/builtin/app.ts             |    0
 .../helper/src/features/builtin/helpers.ts         |    2 +-
 .../helper/src/features/builtin/index.ts           |    0
 .../helper/src/features/builtin/provider.ts        |    0
 .../helper/src/features/builtin/spine.ts           |    2 +-
 .../helper/src/features/define-feature.ts          |    0
 .../helper/src/features/feature-configurator.ts    |    2 +-
 .../helper/src/features/feature.ts                 |    0
 .../helper/src/features/registry.ts                |    2 +-
 .../helper/src/features/resources.ts               |    0
 packages/{sdk => scaffold}/helper/src/ids.ts       |    2 +-
 packages/{sdk => scaffold}/helper/src/index.ts     |    4 +
 packages/{sdk => scaffold}/helper/src/invariant.ts |    0
 .../helper/src/package-managers/link-workspace.ts  |    4 +-
 .../helper/src/package-managers/package-manager.ts |    0
 .../helper/src/plugins/local-plugin-blueprint.ts   |    4 +-
 .../helper/src/project/change-set.ts               |    0
 .../helper/src/project/npm-dependency-policy.ts    |    0
 .../helper/src/project/project-edit-session.ts     |    6 +-
 .../helper/src/project/sdk-project.ts              |    6 +-
 .../{sdk => scaffold}/helper/src/project/types.ts  |    0
 .../src/questions/clack-nested-multiselect.ts      |    2 +-
 .../helper/src/questions/clack-prompt-port.ts      |    2 +-
 .../helper/src/questions/headless-prompt-port.ts   |    2 +-
 .../helper/src/questions/prompt-port.ts            |    0
 .../helper/src/questions/question.ts               |    2 +-
 .../helper/src/templates/assets/README.md.tpl      |    0
 .../helper/src/templates/assets/gitignore.tpl      |    0
 .../helper/src/templates/assets/index.ts.tpl       |    0
 .../assets/local-plugin-tsdown.config.ts.tpl       |    0
 .../src/templates/assets/local-plugin.ts.tpl       |    0
 .../helper/src/templates/assets/local-tool.ts.tpl  |    0
 .../helper/src/templates/assets/package.json.tpl   |    0
 .../helper/src/templates/assets/persona.txt.tpl    |    0
 .../src/templates/assets/tsconfig.base.json.tpl    |    0
 .../src/templates/assets/tsdown.config.ts.tpl      |    0
 .../helper/src/templates/assets/yarnrc.yml.tpl     |    0
 .../helper/src/templates/project-template.ts       |    0
 .../helper/src/templates/template-assets.ts        |    0
 .../helper/src/templates/text-template.ts          |    0
 .../helper/tests/documents.spec.ts                 |    4 +-
 .../helper/tests/headless-prompt-port.spec.ts      |    2 +-
 .../{sdk => scaffold}/helper/tests/project.spec.ts |    4 +-
 .../helper/tests/questions.spec.ts                 |    4 +-
 packages/{sdk => scaffold}/helper/tsconfig.json    |    4 +-
 packages/{sdk => scaffold}/helper/tsdown.config.ts |    0
 packages/scaffold/protocol/README.i18n.yaml        |    6 +
 .../sdk-protocol => scaffold/protocol}/README.md   |    6 +-
 .../protocol}/README.zh.md                         |    8 +-
 .../protocol}/package.json                         |    0
 .../protocol}/src/index.ts                         |    0
 .../protocol}/src/invariant.ts                     |    0
 .../protocol}/src/transport.ts                     |    2 +-
 .../protocol}/src/types.ts                         |    0
 .../protocol}/tests/transport.spec.ts              |    4 +-
 .../protocol}/tsconfig.json                        |    0
 .../{sdk => scaffold}/scripts/README.i18n.yaml     |    2 +-
 packages/{sdk => scaffold}/scripts/README.md       |    0
 packages/{sdk => scaffold}/scripts/README.zh.md    |    0
 packages/{sdk => scaffold}/scripts/package.json    |    0
 packages/{sdk => scaffold}/scripts/src/args.ts     |    6 +-
 packages/{sdk => scaffold}/scripts/src/bin.ts      |    0
 packages/{sdk => scaffold}/scripts/src/build.ts    |    0
 packages/{sdk => scaffold}/scripts/src/command.ts  |    0
 packages/{sdk => scaffold}/scripts/src/config.ts   |    4 +-
 .../scripts/src/config/config-workflow.ts          |    0
 .../{sdk => scaffold}/scripts/src/create-plugin.ts |    2 +-
 .../scripts/src/dev/tsdown-config.ts               |    0
 packages/scaffold/scripts/src/index.ts             |   11 +
 .../{sdk => scaffold}/scripts/src/invariant.ts     |    0
 .../scripts/src/local-plugin-loader-hooks.ts       |    0
 packages/{sdk => scaffold}/scripts/src/runtime.ts  |    4 +-
 .../{sdk => scaffold}/scripts/src/telemetry.ts     |    6 +-
 .../assets/config-install-failure.txt.tpl          |    0
 .../scripts/src/templates/assets/usage.txt.tpl     |    0
 .../scripts/src/templates/dsh-sdk-templates.ts     |    0
 .../tests/__snapshots__/config.snapshot.ts.snap    |    0
 .../scripts/tests/config.snapshot.ts               |    4 +-
 .../scripts/tests/scripts.spec.ts                  |    4 +-
 packages/{sdk => scaffold}/scripts/tsconfig.json   |    2 +-
 .../{sdk => scaffold}/scripts/tsdown.config.ts     |    0
 packages/scaffold/server/README.i18n.yaml          |    6 +
 packages/{ui/jsonrpc => scaffold/server}/README.md |    4 +-
 .../{ui/jsonrpc => scaffold/server}/README.zh.md   |    4 +-
 .../{ui/jsonrpc => scaffold/server}/package.json   |    0
 .../{ui/jsonrpc => scaffold/server}/src/index.ts   |   12 +-
 .../jsonrpc => scaffold/server}/src/invariant.ts   |    0
 .../{ui/jsonrpc => scaffold/server}/src/server.ts  |    4 +-
 .../server}/tests/built-scope-carrier.e2e.ts       |    4 +-
 .../server}/tests/plugin-apply.spec.ts             |    8 +-
 .../server}/tests/plugin-shape.spec.ts             |    0
 .../server}/tests/server.spec.ts                   |    2 +-
 .../{ui/jsonrpc => scaffold/server}/tsconfig.json  |    2 +-
 .../{sdk => scaffold}/telemetry/README.i18n.yaml   |    2 +-
 packages/{sdk => scaffold}/telemetry/README.md     |    0
 packages/{sdk => scaffold}/telemetry/README.zh.md  |    0
 packages/{sdk => scaffold}/telemetry/package.json  |    0
 .../telemetry/src/anonymous-id.ts                  |    8 +-
 .../telemetry/src/consent-resolver.ts              |    0
 packages/{sdk => scaffold}/telemetry/src/index.ts  |    5 +
 .../{sdk => scaffold}/telemetry/src/invariant.ts   |    0
 .../{sdk => scaffold}/telemetry/src/payload.ts     |    0
 .../{sdk => scaffold}/telemetry/src/reporter.ts    |    6 +-
 .../telemetry/src/secret-redactor.ts               |    0
 .../telemetry/tests/anonymous-id.spec.ts           |    0
 .../telemetry/tests/consent-resolver.spec.ts       |    2 +-
 .../telemetry/tests/payload.spec.ts                |    2 +-
 .../telemetry/tests/reporter.spec.ts               |    4 +-
 .../telemetry/tests/secret-redactor.spec.ts        |    4 +-
 packages/{sdk => scaffold}/telemetry/tsconfig.json |    0
 packages/sdk/README.zh.md                          |   16 -
 packages/sdk/scripts/src/index.ts                  |    7 -
 packages/sdk/sdk-client/README.i18n.yaml           |    6 -
 packages/sdk/sdk-protocol/README.i18n.yaml         |    6 -
 packages/self-modification/README.i18n.yaml        |    6 +
 packages/self-modification/README.md               |   10 +
 packages/self-modification/README.zh.md            |   10 +
 .../repository-plugin/README.i18n.yaml             |    6 +
 .../self-modification/repository-plugin/README.md  |  128 ++
 .../repository-plugin/README.zh.md                 |  128 ++
 .../repository-plugin/package.json                 |   22 +-
 .../repository-plugin/src/bin.ts                   |    0
 .../repository-plugin/src/format.ts                |   78 +-
 .../repository-plugin/src/index.ts                 |    4 +-
 .../repository-plugin/src/invariant.ts             |    0
 .../repository-plugin/src/mcp.ts                   |    6 +-
 .../repository-plugin/src/source.ts                |   40 +-
 .../repository-plugin/tests/mcp-format.spec.ts     |    4 +
 .../tests/repository-plugin.spec.ts                |  249 ++-
 .../repository-plugin/tsconfig.json                |    0
 .../repository-plugin/tsdown.config.ts             |    0
 .../self-modification/tool-cordis/README.i18n.yaml |    6 +
 .../tool-cordis/README.md                          |    2 +-
 .../tool-cordis/README.zh.md                       |    2 +-
 .../tool-cordis/package.json                       |    0
 .../tool-cordis/src/api-catalog.ts                 |  138 +-
 .../tool-cordis/src/fiber-state.ts                 |    0
 .../tool-cordis/src/guard.ts                       |    6 +-
 .../tool-cordis/src/index.ts                       |    6 +-
 .../tool-cordis/src/inspect.ts                     |    6 +-
 .../tool-cordis/src/invariant.ts                   |    0
 .../tool-cordis/src/mount.ts                       |    0
 .../tool-cordis/src/present.ts                     |    2 +-
 .../tool-cordis/src/sandbox.ts                     |    2 +-
 .../tool-cordis/tests/cordis-lifecycle.spec.ts     |    2 +-
 .../tool-cordis/tests/cross-mount.spec.ts          |    0
 .../tool-cordis/tests/helpers.ts                   |    2 +-
 .../tool-cordis/tests/inspect.spec.ts              |    4 +-
 .../tool-cordis/tests/integration.spec.ts          |    0
 .../tool-cordis/tests/mount.spec.ts                |    2 +-
 .../tool-cordis/tests/present.spec.ts              |    0
 .../tool-cordis/tests/sandbox-context.spec.ts      |    2 +-
 .../tool-cordis/tests/tool-cordis.spec.ts          |    4 +-
 .../tool-cordis/tests/unmount-hmr.spec.ts          |    0
 .../tool-cordis/tsconfig.json                      |    0
 packages/session-persistence/README.md             |   14 -
 packages/session-persistence/README.zh.md          |   14 -
 .../session-persistence-sqlite/README.i18n.yaml    |    6 -
 .../session-persistence/README.i18n.yaml           |    6 -
 packages/session-projection/README.md              |   10 -
 packages/session-projection/README.zh.md           |   10 -
 .../session-projection/README.i18n.yaml            |    6 -
 packages/session-query/README.i18n.yaml            |    4 +-
 packages/session-query/README.md                   |    2 +
 packages/session-query/README.zh.md                |    2 +
 .../session-query-sqlite/README.i18n.yaml          |    4 +-
 .../session-query/session-query-sqlite/README.md   |    2 +-
 .../session-query-sqlite/README.zh.md              |    6 +-
 .../session-query-sqlite/tsconfig.json             |    2 +-
 .../session-query/session-query/README.i18n.yaml   |    4 +-
 packages/session-query/session-query/README.md     |    6 +-
 packages/session-query/session-query/README.zh.md  |   10 +-
 packages/session-query/session-query/src/index.ts  |    6 +-
 .../session-query/session-query/src/tracing.ts     |    2 +-
 packages/session-query/session-query/src/types.ts  |    8 +-
 .../session-query/tests/tracing.spec.ts            |    4 +-
 packages/session-query/session-query/tsconfig.json |    4 +-
 .../session-query/tool-session-query/src/index.ts  |    2 +-
 .../tool-session-query/src/presentation.ts         |    2 +-
 .../tests/tool-session-query.spec.ts               |    1 +
 packages/session-title/README.md                   |   14 -
 packages/session-title/README.zh.md                |   14 -
 .../{session-title => session}/README.i18n.yaml    |    6 +-
 packages/session/README.md                         |   51 +
 packages/session/README.zh.md                      |   51 +
 .../session-checkpoint-policy/README.i18n.yaml     |    2 +-
 .../session-checkpoint-policy/README.md            |    0
 .../session-checkpoint-policy/README.zh.md         |    0
 .../session-checkpoint-policy/package.json         |    0
 .../session-checkpoint-policy/src/index.ts         |    2 +-
 .../session-checkpoint-policy/src/invariant.ts     |    0
 .../tests/crash-recovery.e2e.ts                    |    2 +-
 .../tests/fixtures/crash-child.ts                  |    2 +-
 .../tests/session-checkpoint-policy.spec.ts        |    0
 .../session-checkpoint-policy/tsconfig.json        |    2 +-
 .../session-persistence-jsonl/README.i18n.yaml     |    4 +-
 .../session-persistence-jsonl/README.md            |    0
 .../session-persistence-jsonl/README.zh.md         |    4 +-
 .../session-persistence-jsonl/package.json         |    0
 .../session-persistence-jsonl/src/format.ts        |    0
 .../session-persistence-jsonl/src/index.ts         |    6 +-
 .../session-persistence-jsonl/src/invariant.ts     |    0
 .../session-persistence-jsonl/src/win32.ts         |    0
 .../src/zstd-private-decoder.ts                    |    0
 .../src/zstd-public-decoder.ts                     |    0
 .../session-persistence-jsonl/src/zstd.ts          |    2 +-
 .../session-persistence-jsonl/tests/jsonl.spec.ts  |    4 +-
 .../session-persistence-jsonl/tests/win32.spec.ts  |    0
 .../tests/zstd.compat.spec.ts                      |    0
 .../session-persistence-jsonl/tests/zstd.spec.ts   |    4 +-
 .../session-persistence-jsonl}/tsconfig.json       |    2 +-
 .../session-persistence-sqlite}/README.i18n.yaml   |    6 +-
 .../session-persistence-sqlite/README.md           |    2 +-
 .../session-persistence-sqlite/README.zh.md        |   10 +-
 .../session-persistence-sqlite/package.json        |    0
 .../session-persistence-sqlite/src/index.ts        |    2 +-
 .../session-persistence-sqlite/src/invariant.ts    |    0
 .../session-persistence-sqlite/src/schema.ts       |    2 +-
 .../tests/sqlite.spec.ts                           |    4 +-
 .../session-persistence-sqlite}/tsconfig.json      |    2 +-
 .../session-persistence}/README.i18n.yaml          |    6 +-
 .../session-persistence/README.md                  |    6 +-
 .../session-persistence/README.zh.md               |   20 +-
 .../session-persistence/package.json               |    0
 .../session-persistence/src/coordinator.ts         |    6 +-
 .../session-persistence/src/index.ts               |    4 +-
 .../session-persistence/src/invariant.ts           |    0
 .../session-persistence/src/preparations.ts        |    2 +-
 .../session-persistence/src/revision.ts            |    0
 .../session-persistence/src/write-behind.ts        |    0
 .../session-persistence/tests/contract.ts          |    2 +-
 .../tests/coordinator-contract.ts                  |    2 +-
 .../session-persistence/tests/persistence.spec.ts  |    6 +-
 .../session-persistence/tests/preparations.spec.ts |    0
 .../session-persistence/tests/write-behind.spec.ts |    0
 .../session-persistence/tsconfig.json              |    0
 .../session-projection-cache/README.i18n.yaml      |    4 +-
 .../session-projection-cache/README.md             |    0
 .../session-projection-cache/README.zh.md          |    2 +-
 .../session-projection-cache/package.json          |    0
 .../session-projection-cache/src/index.ts          |    4 +-
 .../session-projection-cache/src/invariant.ts      |    0
 .../session-projection-cache/src/spec.ts           |    0
 .../session-projection-cache/tests/cache.spec.ts   |    4 +-
 .../session-projection-cache/tsconfig.json         |    2 +-
 .../session/session-projection/README.i18n.yaml    |    6 +
 .../session-projection/README.md                   |    6 +-
 .../session-projection/README.zh.md                |   10 +-
 .../session-projection/package.json                |    0
 .../session-projection/src/index.ts                |    8 +-
 .../session-projection/src/invariant.ts            |    0
 .../session-projection/src/types.ts                |    2 +-
 .../session-projection/tests/registry.spec.ts      |    2 +-
 .../session-projection/tsconfig.json               |    0
 .../session-telemetry-otel/README.i18n.yaml        |    6 +
 .../session-telemetry-otel/README.md               |    0
 .../session-telemetry-otel/README.zh.md            |    4 +-
 .../session-telemetry-otel/package.json            |    0
 .../session-telemetry-otel/src/index.ts            |   10 +-
 .../session-telemetry-otel/src/invariant.ts        |    2 +-
 .../session-telemetry-otel/src/user-id.ts          |    8 +-
 .../tests/loader-composition.e2e.ts                |    0
 .../session-telemetry-otel/tests/otel.spec.ts      |    4 +-
 .../session-telemetry-otel/tests/user-id.spec.ts   |    4 +-
 .../session-telemetry-otel/tsconfig.json           |    0
 .../session-telemetry}/README.i18n.yaml            |    6 +-
 .../session-telemetry/README.md                    |    6 +-
 .../session-telemetry/README.zh.md                 |    8 +-
 .../session-telemetry/package.json                 |    0
 .../session-telemetry/src/coordinator.ts           |   10 +-
 .../session-telemetry/src/index.ts                 |   18 +-
 .../session-telemetry/src/invariant.ts             |    2 +-
 .../session-telemetry/tests/redact.spec.ts         |    2 +-
 .../session-telemetry/tests/telemetry.spec.ts      |    4 +-
 .../session-telemetry/tsconfig.json                |    0
 .../README.i18n.yaml                               |    2 +-
 .../session-title-all-messages-llm/README.md       |    0
 .../session-title-all-messages-llm/README.zh.md    |    0
 .../session-title-all-messages-llm/package.json    |    0
 .../session-title-all-messages-llm/src/index.ts    |    0
 .../src/invariant.ts                               |    0
 .../tests/provider.spec.ts                         |    0
 .../session-title-all-messages-llm/tsconfig.json   |    0
 .../README.i18n.yaml                               |    2 +-
 .../session-title-first-message-llm/README.md      |    0
 .../session-title-first-message-llm/README.zh.md   |    0
 .../session-title-first-message-llm/package.json   |    0
 .../session-title-first-message-llm/src/index.ts   |    0
 .../src/invariant.ts                               |    0
 .../tests/loader-composition.spec.ts               |    0
 .../tests/provider.e2e.ts                          |    0
 .../tests/provider.spec.ts                         |    0
 .../session-title-first-message-llm/tsconfig.json  |    0
 .../session/session-title-llm/README.i18n.yaml     |    6 +
 .../session-title-llm/README.md                    |    2 +-
 .../session-title-llm/README.zh.md                 |    6 +-
 .../session-title-llm/package.json                 |    0
 .../session-title-llm/src/index.ts                 |    8 +-
 .../session-title-llm/src/invariant.ts             |    2 +-
 .../session-title-llm/tests/llm.spec.ts            |    4 +-
 .../session-title-llm/tsconfig.json                |    0
 .../session-title}/README.i18n.yaml                |    6 +-
 .../session-title/README.md                        |    4 +-
 .../session-title/README.zh.md                     |    8 +-
 .../session-title/package.json                     |    0
 .../session-title/src/client.ts                    |    0
 .../session-title/src/index.ts                     |   14 +-
 .../session-title/src/invariant.ts                 |    7 +-
 .../session-title/src/normalize.ts                 |    2 +-
 .../session-title/src/types.ts                     |    0
 .../session-title/tests/invariant.spec.ts          |    4 +-
 .../session-title/tests/persistence.spec.ts        |    2 +-
 .../session-title/tests/projection.spec.ts         |    4 +-
 .../session-title/tests/provider.spec.ts           |    2 +-
 .../session-title/tests/rename.spec.ts             |    0
 .../session-title/tests/service-contracts.spec.ts  |   14 +-
 .../session-title/tests/session-title.spec.ts      |    0
 .../session-title/tsconfig.json                    |    2 +-
 packages/settings/README.i18n.yaml                 |    4 +-
 packages/settings/README.md                        |    2 +
 packages/settings/README.zh.md                     |    4 +-
 packages/settings/settings-local/README.i18n.yaml  |    2 +-
 packages/settings/settings-local/README.zh.md      |   20 +-
 .../settings-local/tests/lock-race.spec.ts         |    2 +-
 packages/settings/settings/README.i18n.yaml        |    4 +-
 packages/settings/settings/README.md               |    4 +-
 packages/settings/settings/README.zh.md            |   18 +-
 packages/settings/settings/src/index.ts            |    8 +-
 packages/settings/settings/tests/memory.ts         |    4 +-
 packages/settings/settings/tests/settings.spec.ts  |    2 +-
 packages/skill/README.i18n.yaml                    |    4 +-
 packages/skill/README.md                           |    2 +
 packages/skill/README.zh.md                        |    4 +-
 packages/skill/skill-badge/README.i18n.yaml        |    2 +-
 packages/skill/skill-badge/README.zh.md            |    2 +-
 packages/skill/skill-local/src/index.ts            |    2 +-
 .../skill/skill-local/tests/skill-local.spec.ts    |   16 +-
 packages/skill/skill/README.i18n.yaml              |    2 +-
 packages/skill/skill/README.zh.md                  |    6 +-
 packages/skill/skill/src/index.ts                  |    3 +-
 packages/skill/tool-skill/README.i18n.yaml         |    4 +-
 packages/skill/tool-skill/README.md                |    2 +-
 packages/skill/tool-skill/README.zh.md             |    2 +-
 packages/skill/tool-skill/src/index.ts             |    2 +-
 packages/spill/README.i18n.yaml                    |    4 +-
 packages/spill/README.md                           |    2 +
 packages/spill/README.zh.md                        |    2 +
 packages/spill/spill-policy/src/index.ts           |    2 +-
 packages/spill/spill/README.i18n.yaml              |    4 +-
 packages/spill/spill/README.md                     |   12 +-
 packages/spill/spill/README.zh.md                  |   12 +-
 packages/spill/spill/src/index.ts                  |    6 +-
 packages/spill/spill/src/types.ts                  |    4 +-
 packages/spill/spill/tests/service.spec.ts         |    2 +-
 packages/storage/README.i18n.yaml                  |    4 +-
 packages/storage/README.md                         |    2 +
 packages/storage/README.zh.md                      |    2 +
 packages/storage/storage-domain/README.i18n.yaml   |    4 +-
 packages/storage/storage-domain/README.md          |    2 +-
 packages/storage/storage-domain/README.zh.md       |    2 +-
 packages/storage/storage-domain/src/domain.ts      |    2 +-
 .../storage-domain/tests/helpers/memory-backend.ts |    2 +-
 packages/storage/storage-sqlite/README.i18n.yaml   |    2 +-
 packages/storage/storage-sqlite/README.zh.md       |    2 +-
 packages/storage/storage/README.i18n.yaml          |    2 +-
 packages/storage/storage/README.zh.md              |    2 +-
 packages/subagent/README.i18n.yaml                 |    4 +-
 packages/subagent/README.md                        |    2 +
 packages/subagent/README.zh.md                     |    4 +-
 .../subagent-acp/tests/subagent-acp.e2e.ts         |    2 +-
 .../subagent/subagent-claude-code/README.i18n.yaml |    2 +-
 .../subagent/subagent-claude-code/README.zh.md     |    4 +-
 .../subagent/subagent-claude-code/src/process.ts   |    2 +-
 packages/subagent/subagent-claude-code/src/run.ts  |    4 +-
 packages/subagent/subagent-codex/README.i18n.yaml  |    2 +-
 packages/subagent/subagent-codex/README.zh.md      |    6 +-
 packages/subagent/subagent-codex/src/run.ts        |    4 +-
 packages/subagent/subagent-codex/tsconfig.json     |    2 +-
 .../subagent/subagent-dsh-sdk/README.i18n.yaml     |    4 +-
 packages/subagent/subagent-dsh-sdk/README.md       |    2 +-
 packages/subagent/subagent-dsh-sdk/README.zh.md    |    4 +-
 .../tests/subagent-dsh-sdk.spec.ts                 |    2 +-
 packages/subagent/subagent-dsh-sdk/tsconfig.json   |    4 +-
 packages/subagent/subagent-fork/README.i18n.yaml   |    2 +-
 packages/subagent/subagent-fork/README.zh.md       |    2 +-
 .../subagent/subagent-inprocess/README.i18n.yaml   |    2 +-
 packages/subagent/subagent-inprocess/README.zh.md  |    8 +-
 packages/subagent/subagent-inprocess/tsconfig.json |    2 +-
 packages/subagent/subagent/README.i18n.yaml        |    4 +-
 packages/subagent/subagent/README.md               |   19 +-
 packages/subagent/subagent/README.zh.md            |   23 +-
 packages/subagent/subagent/src/continuation.ts     |   76 +-
 packages/subagent/subagent/src/descriptor.ts       |    2 +-
 packages/subagent/subagent/src/index.ts            |   60 +-
 packages/subagent/subagent/src/invariant.ts        |    2 +-
 packages/subagent/subagent/src/lifecycle.ts        |    2 +-
 packages/subagent/subagent/src/list-children.ts    |  162 +-
 packages/subagent/subagent/src/types.ts            |    9 +-
 .../subagent/subagent/tests/continuation.spec.ts   |  220 +++
 packages/subagent/subagent/tests/invariant.spec.ts |    2 +-
 .../subagent/subagent/tests/list-children.spec.ts  |  240 +++
 packages/subagent/subagent/tests/service.spec.ts   |   10 +
 packages/subagent/subagent/tsconfig.json           |    6 +-
 .../tool-subagent-control/README.i18n.yaml         |    4 +-
 packages/subagent/tool-subagent-control/README.md  |   30 +-
 .../subagent/tool-subagent-control/README.zh.md    |   30 +-
 .../subagent/tool-subagent-control/package.json    |    2 +-
 .../subagent/tool-subagent-control/src/index.ts    |   56 +-
 .../tool-subagent-control/src/list-agents.ts       |  161 +-
 .../tests/list-agents.spec.ts                      |  167 +-
 .../tests/tool-subagent-control.spec.ts            |  204 ++-
 .../subagent/tool-subagent-report/README.i18n.yaml |    4 +-
 packages/subagent/tool-subagent-report/README.md   |    2 +-
 .../subagent/tool-subagent-report/README.zh.md     |    2 +-
 .../tests/tool-subagent-report.spec.ts             |    2 +-
 packages/subagent/tool-subagent/README.i18n.yaml   |    2 +-
 packages/subagent/tool-subagent/README.zh.md       |    2 +-
 packages/subprocess/README.i18n.yaml               |    4 +-
 packages/subprocess/README.md                      |   12 +-
 packages/subprocess/README.zh.md                   |   12 +-
 .../subprocess/subprocess-local/README.i18n.yaml   |    4 +-
 packages/subprocess/subprocess-local/README.md     |    8 +-
 packages/subprocess/subprocess-local/README.zh.md  |    8 +-
 packages/subprocess/subprocess-local/package.json  |    7 +
 .../scripts/ensure-spawn-helper.mjs                |    0
 packages/subprocess/subprocess-local/src/index.ts  |  115 +-
 .../subprocess-local}/src/process-inspector.ts     |   55 +-
 packages/subprocess/subprocess-local/src/spawn.ts  |   26 +-
 .../subprocess/subprocess-local/src/terminal.ts    |  212 +++
 .../subprocess-local/tests/local.spec.ts           |  256 ++-
 .../tests/process-inspector.spec.ts                |   37 +-
 .../subprocess-local/tests/spawn.spec.ts           |   38 +-
 .../subprocess-local/tests/terminal.spec.ts        |  332 ++++
 packages/subprocess/subprocess/README.i18n.yaml    |    4 +-
 packages/subprocess/subprocess/README.md           |   14 +-
 packages/subprocess/subprocess/README.zh.md        |   16 +-
 packages/subprocess/subprocess/src/index.ts        |   49 +-
 packages/subprocess/subprocess/src/invariant.ts    |    2 +-
 packages/subprocess/subprocess/src/types.ts        |   72 +-
 .../subprocess/subprocess/tests/service.spec.ts    |   25 +-
 packages/support/README.i18n.yaml                  |    4 +-
 packages/support/README.md                         |    2 +
 packages/support/README.zh.md                      |    6 +-
 packages/support/acp-snapshot/README.i18n.yaml     |    2 +-
 packages/support/acp-snapshot/README.zh.md         |   14 +-
 .../acp-snapshot/tests/fixtures/fake-acp-agent.ts  |    2 +-
 packages/support/invariants/README.i18n.yaml       |    4 +-
 packages/support/invariants/README.md              |    2 +-
 packages/support/invariants/README.zh.md           |    8 +-
 packages/support/invariants/src/index.ts           |    2 +-
 packages/support/llm-replay/README.i18n.yaml       |    2 +-
 packages/support/llm-replay/README.zh.md           |    4 +-
 .../support/llm-replay/tests/llm-replay.spec.ts    |   20 +-
 packages/support/loader-smoke/README.i18n.yaml     |    2 +-
 packages/support/loader-smoke/README.zh.md         |    2 +-
 packages/tasks/README.i18n.yaml                    |    4 +-
 packages/tasks/README.md                           |    2 +
 packages/tasks/README.zh.md                        |    4 +-
 packages/tasks/tasks-local/README.i18n.yaml        |    4 +-
 packages/tasks/tasks-local/README.md               |    2 +-
 packages/tasks/tasks-local/README.zh.md            |    2 +-
 packages/tasks/tasks-local/src/index.ts            |    4 +-
 packages/tasks/tasks-local/src/invariant.ts        |    2 +-
 packages/tasks/tasks/README.i18n.yaml              |    4 +-
 packages/tasks/tasks/README.md                     |    4 +-
 packages/tasks/tasks/README.zh.md                  |   10 +-
 packages/tasks/tasks/src/index.ts                  |    2 +-
 packages/tasks/tasks/tests/service.spec.ts         |    2 +-
 packages/tasks/tool-tasks/README.i18n.yaml         |    2 +-
 packages/tasks/tool-tasks/README.zh.md             |    2 +-
 packages/telemetry/README.md                       |   10 -
 packages/telemetry/README.zh.md                    |   10 -
 .../session-telemetry-otel/README.i18n.yaml        |    6 -
 .../telemetry/session-telemetry/README.i18n.yaml   |    6 -
 packages/timeout/README.md                         |   11 -
 packages/timeout/README.zh.md                      |   11 -
 packages/todo/README.i18n.yaml                     |    4 +-
 packages/todo/README.md                            |    4 +-
 packages/todo/README.zh.md                         |    6 +-
 packages/todo/tool-todo/README.i18n.yaml           |    4 +-
 packages/todo/tool-todo/README.md                  |    2 +-
 packages/todo/tool-todo/README.zh.md               |    2 +-
 packages/todo/tool-todo/tests/integration.spec.ts  |    2 +-
 packages/todo/tool-todo/tests/projection.spec.ts   |    2 +-
 packages/todo/tool-todo/tsconfig.json              |    2 +-
 packages/typert/README.i18n.yaml                   |    2 +-
 packages/typert/README.zh.md                       |    2 +-
 packages/typert/generator/README.i18n.yaml         |    2 +-
 packages/typert/generator/README.zh.md             |    4 +-
 packages/typert/generator/src/analyzer.ts          |    2 +-
 packages/typert/generator/src/cordis-catalog.ts    |  119 +-
 .../tests/cordis-catalog-contract.spec.ts          |   16 +-
 .../typert/generator/tests/cordis-catalog.spec.ts  |   26 +-
 packages/typert/generator/tests/type-model.spec.ts |   26 +-
 packages/typert/registry/README.i18n.yaml          |    2 +-
 packages/typert/registry/README.zh.md              |    6 +-
 packages/typert/type-meta/README.i18n.yaml         |    2 +-
 packages/typert/type-meta/README.zh.md             |    4 +-
 packages/ui/app-boot/README.i18n.yaml              |    6 -
 packages/ui/jsonrpc/README.i18n.yaml               |    6 -
 packages/ui/tool-ask-user/README.i18n.yaml         |    6 -
 packages/ui/user-approval/README.i18n.yaml         |    6 -
 packages/ui/user-interaction/README.i18n.yaml      |    6 -
 packages/util/README.i18n.yaml                     |    2 +-
 packages/util/README.zh.md                         |    2 +-
 packages/util/atomic-write/README.i18n.yaml        |    2 +-
 packages/util/atomic-write/README.zh.md            |    2 +-
 packages/util/environment/README.i18n.yaml         |    4 +-
 packages/util/environment/README.md                |    2 +-
 packages/util/environment/README.zh.md             |    8 +-
 packages/util/environment/package.json             |    2 +-
 packages/util/environment/src/index.ts             |    4 +-
 packages/util/retention/README.i18n.yaml           |    2 +-
 packages/util/retention/README.zh.md               |    2 +-
 packages/util/timeout/README.i18n.yaml             |    4 +-
 packages/util/timeout/README.md                    |    4 +-
 packages/util/timeout/README.zh.md                 |    4 +-
 packages/util/timeout/src/index.ts                 |   17 +-
 packages/util/timeout/tests/timeout.spec.ts        |   22 +
 packages/web/README.i18n.yaml                      |    4 +-
 packages/web/README.md                             |    2 +
 packages/web/README.zh.md                          |    2 +
 packages/web/tool-web/README.i18n.yaml             |    4 +-
 packages/web/tool-web/README.md                    |    6 +-
 packages/web/tool-web/README.zh.md                 |    8 +-
 packages/web/tool-web/src/fetch.ts                 |    2 +-
 packages/web/tool-web/tsconfig.json                |    2 +-
 packages/web/web-fetch-local/README.i18n.yaml      |    4 +-
 packages/web/web-fetch-local/README.md             |    4 +-
 packages/web/web-fetch-local/README.zh.md          |    4 +-
 packages/web/web-search-deepseek/README.i18n.yaml  |    2 +-
 packages/web/web-search-deepseek/README.zh.md      |    2 +-
 packages/web/web-search-deepseek/src/provider.ts   |    4 +-
 packages/web/web-search-exa/README.i18n.yaml       |    4 +-
 packages/web/web-search-exa/README.md              |    2 +-
 packages/web/web-search-exa/README.zh.md           |    2 +-
 packages/web/web-search-exa/src/provider.ts        |    2 +-
 .../web/web-search-perplexity/README.i18n.yaml     |    4 +-
 packages/web/web-search-perplexity/README.md       |    4 +-
 packages/web/web-search-perplexity/README.zh.md    |    4 +-
 packages/web/web/README.i18n.yaml                  |    4 +-
 packages/web/web/README.md                         |   16 +-
 packages/web/web/README.zh.md                      |   18 +-
 packages/web/web/src/index.ts                      |    2 +-
 packages/workflow/README.i18n.yaml                 |    4 +-
 packages/workflow/README.md                        |    2 +
 packages/workflow/README.zh.md                     |    2 +
 packages/workflow/tool-ralph/README.i18n.yaml      |    2 +-
 packages/workflow/tool-ralph/README.zh.md          |    4 +-
 packages/workflow/tool-ralph/src/index.ts          |    2 +-
 packages/workflow/tool-workflow/README.i18n.yaml   |    2 +-
 packages/workflow/tool-workflow/README.zh.md       |    4 +-
 .../workflow-workerthread/README.i18n.yaml         |    2 +-
 .../workflow/workflow-workerthread/README.zh.md    |    2 +-
 .../workflow/workflow-workerthread/src/runtime.ts  |    4 +-
 packages/workflow/workflow/README.i18n.yaml        |    2 +-
 packages/workflow/workflow/README.zh.md            |    6 +-
 packages/workflow/workflow/src/index.ts            |    4 +-
 packages/workspace/README.i18n.yaml                |    4 +-
 packages/workspace/README.md                       |    2 +
 packages/workspace/README.zh.md                    |    2 +
 packages/workspace/workspace/README.i18n.yaml      |    4 +-
 packages/workspace/workspace/README.md             |    1 +
 packages/workspace/workspace/README.zh.md          |    1 +
 packages/workspace/workspace/src/index.ts          |    4 +-
 packages/workspace/workspace/src/types.ts          |   13 +-
 packages/workspace/workspace/tsconfig.json         |    2 +-
 1507 files changed, 27752 insertions(+), 8730 deletions(-)
```

## 破坏性变更清单

- 本日快照未发现 seam 符号级破坏。
- 删除的包目录：packages/cordis/repository-plugin packages/sdk/scripts packages/sdk/sdk-client packages/sdk/sdk-protocol packages/session-persistence/session-persistence packages/session-persistence/session-persistence-sqlite packages/session-projection/session-projection packages/telemetry/session-telemetry packages/telemetry/session-telemetry-otel packages/ui/app-boot packages/ui/jsonrpc packages/ui/tool-ask-user packages/ui/user-approval packages/ui/user-interaction。

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
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 9 项匹配），建议确认所依赖的宿主面当日是否仍满足。
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

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
