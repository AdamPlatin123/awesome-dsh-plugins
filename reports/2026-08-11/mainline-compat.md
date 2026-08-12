# mainline 兼容性报告（2026-08-11）

- mainline：`3c21611`（snapshots/20260810T155924Z）
- 上次对比：`1c4950ab71fa4d128c749d9b22af17373edddb73`
- 兼容性：81/210 无需适配，5 需适配（dsh-subagent-tree dsh-working-activity dsh-advisor dsh-tps dsh-split-panes）；其中关注 3、占位 11、不适用 2、已删除 1、未知 123

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
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| qqbot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| Qwen-MM-Plugins | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| Recall | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| review-panel | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-mxc | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| session-chatlog | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| session-persistence-rdb | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| telegram | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| tg-bot | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 12 项匹配 | 兼容 |
| toybox | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| turtle-ui | 未知（不同谱系） | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 已删除 |
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
| DSH-better-sidebar | 未知 | 无补丁 | 缺: tuiPrompt | 14 项匹配 | 未知（待调研） |
| dsh-session-hub | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-ica | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-advisor | 未知（catalog ref，非 mainline 锚定） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 14 项匹配 | 需适配 |
| dsh-llm-fallbacks | 未知 | OK（2 个补丁全部干净应用） | 缺: tuiPrompt | 8 项匹配 | 兼容 |
| dsh-web-workflow-visualizer | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-checkpoint | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 未知（待调研） |
| dsh-rewind | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| official-plugins-port | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| oh-my-dsh | 未知 | 无补丁 | 缺: tuiPrompt | 2167 项匹配 | 未知（待调研） |
| dsh-side-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-profile-bundle-example | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-plan-execute | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 12 项匹配 | 未知（待调研） |
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
| dsh-input-history | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-client-ui-plan-execute | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-stickers | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| deep-standard-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-serenity-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 未知（待调研） |
| dsh-toolkit | 未知 | 无补丁 | 缺: tuiPrompt | 16 项匹配 | 未知（待调研） |
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
| dsh-gomoku | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 未知（待调研） |
| dsh-101 | 未知 | 无补丁 | 缺: tuiPrompt | 16 项匹配 | 未知（待调研） |
| dsh-turn-rewind | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-genui | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 9 项匹配 | 兼容 |
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
| dsh-track | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-spur | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-selection-chat | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-browser-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-engram-relay | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| yet-another-subagent | 未知 | 无补丁 | 缺: tuiPrompt | 17 项匹配 | 未知（待调研） |
| dsh-voice-chat | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-ads | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-skill-session-recovery | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tavern-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-qq2006 | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-plugin-guide | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 未知（待调研） |
| dsh-mnemon | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-pet-rs | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-auto-blame | 未知 | 无补丁 | 缺: tuiPrompt | 13 项匹配 | 未知（待调研） |
| dsh-question-collapse | 未知（不同谱系） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-latex | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-tool-stat | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-tool-schema | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-security-audit | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-browser-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| ya-workspace-sidebar | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 未知（待调研） |
| dsh-d399 | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| 7d7d | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cordis-rocks | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-pet-web | 未知 | 无补丁 | 缺: tuiPrompt | 8 项匹配 | 未知（待调研） |
| dsh-sleep | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-minigames | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-nono | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-auto-chess | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 未知（待调研） |
| dshfind | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-cyber-sec | 未知（非 commit 锚定: 20260809T140917Z） | 无补丁 | 缺: tuiPrompt | 15 项匹配 | 兼容 |
| dsh-anti-ads | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-self-control-guard | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| whale-girl | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-codex-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| dsh-kimi-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 未知（待调研） |
| session-teleport | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 未知（待调研） |
| dsh-code-map | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-loop | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-navbar | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-task-status | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 未知（待调研） |
| dsh-annotation | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |
| dsh-ui-webview | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-web-review | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 未知（待调研） |

## mainline 变更分析（1c4950ab71fa4d128c749d9b22af17373edddb73 → 3c21611）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **包级变化**：packages/ 下删除 0 个包目录、新增 14 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：

新增文件：
```
packages/attachment/README.i18n.yaml
packages/attachment/README.md
packages/attachment/README.zh.md
packages/attachment/attachment-local/README.i18n.yaml
packages/attachment/attachment-local/README.md
packages/attachment/attachment-local/README.zh.md
packages/attachment/attachment-local/package.json
packages/attachment/attachment-local/src/image.ts
packages/attachment/attachment-local/src/index.ts
packages/attachment/attachment-local/src/invariant.ts
packages/attachment/attachment-local/src/store.ts
packages/attachment/attachment-local/tests/image.spec.ts
packages/attachment/attachment-local/tests/index.spec.ts
packages/attachment/attachment-local/tests/store.spec.ts
packages/attachment/attachment-local/tsconfig.json
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
 packages/AGENTS.md                                 |  12 +-
 packages/README.i18n.yaml                          |   4 +-
 packages/README.md                                 |   6 +-
 packages/README.zh.md                              |   6 +-
 packages/acp/acp/src/index.ts                      |  11 +
 packages/acp/acp/tests/turns.spec.ts               |  29 +
 packages/api/gateway/package.json                  |  16 +-
 packages/api/remotes/package.json                  |  14 +-
 packages/api/remotes/src/agent-lookup.ts           |  23 +-
 packages/attachment/README.i18n.yaml               |   6 +
 packages/attachment/README.md                      |  12 +
 packages/attachment/README.zh.md                   |  12 +
 .../attachment/attachment-local/README.i18n.yaml   |   6 +
 packages/attachment/attachment-local/README.md     |  21 +
 packages/attachment/attachment-local/README.zh.md  |  21 +
 packages/attachment/attachment-local/package.json  |  33 +
 packages/attachment/attachment-local/src/image.ts  |  66 ++
 packages/attachment/attachment-local/src/index.ts  |  76 ++
 .../attachment/attachment-local/src/invariant.ts   |  20 +
 packages/attachment/attachment-local/src/store.ts  | 221 +++++
 .../attachment-local/tests/image.spec.ts           |  51 ++
 .../attachment-local/tests/index.spec.ts           |  60 ++
 .../attachment-local/tests/store.spec.ts           | 208 +++++
 packages/attachment/attachment-local/tsconfig.json |  12 +
 packages/attachment/attachment/README.i18n.yaml    |   6 +
 packages/attachment/attachment/README.md           |  21 +
 packages/attachment/attachment/README.zh.md        |  21 +
 packages/attachment/attachment/package.json        |  27 +
 packages/attachment/attachment/src/brand.ts        |  15 +
 packages/attachment/attachment/src/error.ts        |  26 +
 packages/attachment/attachment/src/index.ts        |  60 ++
 packages/attachment/attachment/src/invariant.ts    |  20 +
 packages/attachment/attachment/src/types.ts        |  48 ++
 packages/attachment/attachment/tsconfig.json       |  11 +
 packages/bash/bash-sandbox/src/index.ts            |   4 +-
 packages/bash/bash/README.i18n.yaml                |   4 +-
 packages/bash/bash/README.md                       |   2 +-
 packages/bash/bash/README.zh.md                    |   2 +-
 packages/bash/pwsh-local/README.i18n.yaml          |   4 +-
 packages/bash/pwsh-local/README.md                 |   2 +-
 packages/bash/pwsh-local/README.zh.md              |   2 +-
 packages/bash/pwsh-local/src/index.ts              |  48 +-
 packages/bash/pwsh-local/tests/executor.spec.ts    |  30 +-
 packages/bash/pwsh-sandbox/README.i18n.yaml        |   6 +
 packages/bash/pwsh-sandbox/README.md               |  34 +
 packages/bash/pwsh-sandbox/README.zh.md            |  34 +
 packages/bash/pwsh-sandbox/package.json            |  45 +
 packages/bash/pwsh-sandbox/src/helpers.ts          | 120 +++
 packages/bash/pwsh-sandbox/src/index.ts            | 189 ++++
 packages/bash/pwsh-sandbox/src/invariant.ts        |  30 +
 packages/bash/pwsh-sandbox/tests/acl.e2e.ts        | 111 +++
 packages/bash/pwsh-sandbox/tests/sandbox.spec.ts   | 326 +++++++
 packages/bash/pwsh-sandbox/tsconfig.json           |  39 +
 packages/bash/tool-bash/src/index.ts               |   6 +-
 packages/bash/tool-bash/tests/tools.spec.ts        |   2 +-
 packages/bash/tool-pwsh/README.i18n.yaml           |   4 +-
 packages/bash/tool-pwsh/README.md                  |  16 +-
 packages/bash/tool-pwsh/README.zh.md               |  16 +-
 packages/bash/tool-pwsh/package.json               |   6 +
 packages/bash/tool-pwsh/src/index.ts               | 162 +++-
 packages/bash/tool-pwsh/src/render.ts              |  52 +-
 packages/bash/tool-pwsh/tests/tools.spec.ts        | 351 +++++++-
 packages/bash/tool-pwsh/tsconfig.json              |  12 +
 packages/boot/app-boot/README.i18n.yaml            |   4 +-
 packages/boot/app-boot/README.md                   |  10 +-
 packages/boot/app-boot/README.zh.md                |  10 +-
 packages/boot/app-boot/package.json                |   2 +
 packages/boot/app-boot/src/index.ts                |  15 +-
 packages/boot/app-boot/src/profile.ts              |  11 +-
 packages/boot/app-boot/tests/config-reload.spec.ts |  51 +-
 packages/boot/app-boot/tests/hmr-config.spec.ts    |  72 +-
 .../boot/app-boot/tests/repository-cache.spec.ts   |  52 +-
 packages/boot/app-boot/tsconfig.json               |   3 +
 packages/bundle/base/README.i18n.yaml              |   4 +-
 packages/bundle/base/README.md                     |   3 +
 packages/bundle/base/README.zh.md                  |   3 +
 packages/bundle/base/cordis.patch.yml              |   8 +-
 packages/bundle/base/package.json                  |   6 +
 packages/bundle/base/tests/base.spec.ts            |  44 +-
 packages/bundle/base/windows.cordis.patch.yml      |  31 +
 packages/bundle/web-app/cordis.patch.yml           | 157 +++-
 packages/bundle/web-app/package.json               |   3 +
 packages/bundle/web-app/src/index.ts               |   2 +-
 packages/client/AGENTS.md                          |  26 +-
 packages/client/README.i18n.yaml                   |   4 +-
 packages/client/README.md                          |   1 +
 packages/client/README.zh.md                       |   1 +
 packages/client/connection/README.i18n.yaml        |   4 +-
 packages/client/connection/README.md               |   2 +-
 packages/client/connection/README.zh.md            |   2 +-
 packages/client/connection/package.json            |  11 +-
 packages/client/connection/src/client/api.ts       |  15 +-
 .../client/connection/src/client/connection.ts     |  18 +-
 packages/client/connection/src/client/fixture.ts   | 229 ++++-
 packages/client/connection/src/client/index.ts     |   4 +-
 packages/client/connection/src/http-bridge.ts      |  28 +-
 packages/client/connection/src/index.ts            |  46 +-
 .../client/connection/tests/connection.spec.ts     |  29 +
 packages/client/connection/tests/fake-api.ts       |  19 +
 packages/client/connection/tests/fixture.spec.ts   |  23 +-
 .../client/connection/tests/http-bridge.spec.ts    |  30 +-
 packages/client/connection/tests/node-half.spec.ts |  28 +-
 packages/client/connection/tsconfig.json           |   3 +
 packages/client/hmr/README.i18n.yaml               |   2 +-
 packages/client/hmr/README.md                      |   2 +-
 packages/client/hmr/package.json                   |  10 +-
 packages/client/hmr/src/client/index.ts            |  15 +-
 packages/client/locale/README.i18n.yaml            |   4 +-
 packages/client/locale/README.md                   |   2 +-
 packages/client/locale/README.zh.md                |   2 +-
 packages/client/locale/package.json                |  22 +-
 packages/client/locale/src/client/index.ts         |  93 +-
 packages/client/locale/src/index.ts                |  25 +-
 packages/client/locale/src/locale-settings.ts      |  26 +
 packages/client/locale/tests/apply.spec.ts         |  55 +-
 packages/client/locale/tests/host.spec.ts          |  30 +
 packages/client/locale/tests/invariant.spec.ts     |   8 +-
 packages/client/locale/tests/locale.spec.ts        |  74 +-
 packages/client/locale/tsconfig.json               |   3 +
 packages/client/modules/README.i18n.yaml           |   4 +-
 packages/client/modules/README.md                  |   4 +-
 packages/client/modules/README.zh.md               |   4 +-
 packages/client/modules/package.json               |  12 +-
 packages/client/modules/src/client/index.ts        |   4 +-
 packages/client/modules/src/client/manifest.ts     |  14 +-
 packages/client/modules/src/client/system.ts       |   2 +-
 packages/client/modules/src/index.ts               |  36 +-
 packages/client/modules/tests/node-half.spec.ts    |  23 +-
 packages/client/runtime/README.i18n.yaml           |   4 +-
 packages/client/runtime/README.md                  |   6 +-
 packages/client/runtime/README.zh.md               |   6 +-
 packages/client/runtime/package.json               |  21 +-
 .../client/runtime/src/client/contract/session.ts  |  16 +-
 .../client/runtime/src/client/contract/sessions.ts |   9 +
 .../client/runtime/src/client/contract/store.ts    |   6 +-
 .../runtime/src/client/contract/workspaces.ts      |   6 +-
 packages/client/runtime/src/client/index.ts        |  20 +-
 .../runtime/src/client/sessions/conversation.ts    |   3 +
 .../client/runtime/src/client/sessions/lineage.ts  |   2 +
 .../client/runtime/src/client/sessions/manager.ts  |  45 +-
 .../src/client/sessions/projection-store.ts        |  11 +-
 .../client/runtime/src/client/sessions/service.ts  |  18 +-
 .../client/runtime/src/client/sessions/session.ts  |  75 +-
 .../client/runtime/src/client/settings-scope.ts    | 261 ++++++
 .../runtime/src/client/workspaces/manager.ts       |   2 +-
 .../runtime/src/client/workspaces/service.ts       |   6 +-
 .../runtime/src/client/workspaces/workspace.ts     |   3 +-
 packages/client/runtime/tests/client-apply.spec.ts |   2 +-
 packages/client/runtime/tests/conversation.spec.ts |  12 +-
 packages/client/runtime/tests/event-script.ts      |   2 +-
 packages/client/runtime/tests/fake-api.ts          |  19 +
 packages/client/runtime/tests/node-half.spec.ts    |   2 +-
 .../client/runtime/tests/projection-store.spec.ts  |   3 +-
 packages/client/runtime/tests/session.spec.ts      |  17 +-
 .../client/runtime/tests/sessions-service.spec.ts  |  34 +
 .../client/runtime/tests/settings-scope.spec.ts    | 352 ++++++++
 .../client/runtime/tests/slots-service.spec.ts     |   2 +-
 packages/client/runtime/tests/wire-events.spec.ts  |  16 +-
 .../runtime/tests/workspaces-service.spec.ts       |   6 +-
 packages/client/runtime/tsconfig.json              |   6 +
 packages/client/test-runtime/README.i18n.yaml      |   4 +-
 packages/client/test-runtime/README.md             |   4 +-
 packages/client/test-runtime/README.zh.md          |   4 +-
 packages/client/test-runtime/src/index.ts          |   4 +-
 packages/client/test-runtime/src/sessions.ts       |  18 +
 packages/client/test-runtime/src/settings-scope.ts |  48 ++
 packages/client/test-runtime/src/workspaces.ts     |  11 +-
 .../client/test-runtime/tests/runtime.spec.tsx     |  14 +-
 packages/client/tsdown.client.ts                   |   8 +-
 packages/client/ui-agent-preset/README.i18n.yaml   |   6 +
 packages/client/ui-agent-preset/README.md          |  69 ++
 packages/client/ui-agent-preset/README.zh.md       |  69 ++
 packages/client/ui-agent-preset/package.json       |  76 ++
 .../src/client/AgentPresetLabel.module.css         |  23 +
 .../src/client/AgentPresetLabel.tsx                |  64 ++
 .../src/client/AgentPresetRow.module.css           |  60 ++
 .../ui-agent-preset/src/client/AgentPresetRow.tsx  |  89 ++
 .../src/client/AgentPresetSeat.module.css          |  64 ++
 .../ui-agent-preset/src/client/AgentPresetSeat.tsx | 105 +++
 .../src/client/AgentPresetSection.module.css       | 388 +++++++++
 .../src/client/AgentPresetSection.tsx              | 381 +++++++++
 .../ui-agent-preset/src/client/PresetMenu.tsx      |  84 ++
 .../client/ui-agent-preset/src/client/index.ts     | 210 +++++
 .../client/ui-agent-preset/src/client/locales.ts   | 192 +++++
 .../ui-agent-preset/src/client/seat-store.ts       | 163 ++++
 .../ui-agent-preset/src/client/section-store.ts    | 347 ++++++++
 .../ui-agent-preset/src/client/settings-store.ts   | 255 ++++++
 .../client/ui-agent-preset/src/css-modules.d.ts    |   4 +
 packages/client/ui-agent-preset/src/index.ts       |   9 +
 packages/client/ui-agent-preset/src/invariant.ts   |  30 +
 .../client/ui-agent-preset/tests/apply.spec.ts     | 546 ++++++++++++
 .../ui-agent-preset/tests/components.spec.tsx      | 312 +++++++
 .../client/ui-agent-preset/tests/invariant.spec.ts |  25 +
 .../client/ui-agent-preset/tests/locales.spec.ts   |  33 +
 .../ui-agent-preset/tests/section-store.spec.ts    | 580 +++++++++++++
 .../client/ui-agent-preset/tests/section.spec.tsx  | 440 ++++++++++
 .../ui-agent-preset/tests/settings-store.spec.ts   | 458 ++++++++++
 packages/client/ui-agent-preset/tsconfig.json      |  45 +
 packages/client/ui-agent-preset/tsdown.config.ts   |   3 +
 packages/client/ui-command/README.i18n.yaml        |   4 +-
 packages/client/ui-command/README.md               |   8 +-
 packages/client/ui-command/README.zh.md            |   8 +-
 packages/client/ui-command/package.json            |  18 +-
 .../ui-command/src/client/PopupSelectView.tsx      |   4 +-
 packages/client/ui-command/src/client/directory.ts |   2 +-
 packages/client/ui-command/src/client/popup.ts     |   2 +-
 packages/client/ui-command/src/client/service.ts   |   5 +
 packages/client/ui-command/src/index.ts            |   2 +-
 .../client/ui-command/tests/popup-view.spec.tsx    |   2 +-
 packages/client/ui-command/tests/popup.spec.ts     |   2 +-
 packages/client/ui-command/tests/service.spec.ts   |  24 +
 packages/client/ui-conversation/README.i18n.yaml   |   4 +-
 packages/client/ui-conversation/README.md          |   6 +-
 packages/client/ui-conversation/README.zh.md       |   6 +-
 packages/client/ui-conversation/package.json       |  29 +-
 .../client/ui-conversation/src/client/apply.ts     |  83 +-
 .../src/client/chat/AssistantMarkdown.tsx          |   7 +-
 .../src/client/chat/AssistantNodeView.tsx          |   3 +-
 .../src/client/chat/ChatNodeSeat.tsx               |   5 +-
 .../ui-conversation/src/client/chat/ChatView.tsx   |   7 +-
 .../src/client/chat/MessageImage.module.css        |  53 ++
 .../src/client/chat/MessageImage.tsx               |  72 ++
 .../src/client/chat/MessageItem.module.css         |  17 +-
 .../src/client/chat/MessageItem.tsx                |  56 +-
 .../src/client/contract/composer-submission.ts     |   9 +-
 .../ui-conversation/src/client/contract/slots.ts   |  79 +-
 .../client/ui-conversation/src/client/index.ts     |   3 +-
 .../ui-conversation/src/client/input/contract.ts   |  34 +-
 .../src/client/input/decorations.ts                |  12 +-
 .../ui-conversation/src/client/input/facade.ts     |  89 +-
 .../client/ui-conversation/src/client/input/hub.ts |  92 +-
 .../ui-conversation/src/client/input/machine.ts    |  15 +-
 .../src/client/input/submission-policy.ts          |  68 +-
 .../client/ui-conversation/src/client/locales.ts   |  32 +-
 .../ui-conversation/src/client/queue/store.ts      |   2 +-
 .../client/ui-conversation/src/client/service.ts   | 214 ++++-
 .../src/client/skeleton/ApprovalPanel.tsx          |   3 +-
 .../src/client/skeleton/ContextMeter.tsx           |   4 +-
 .../src/client/skeleton/ConversationRoot.tsx       |   2 +-
 .../src/client/skeleton/ConversationSession.tsx    |   8 +-
 .../src/client/skeleton/DetailsPanel.module.css    |   2 +-
 .../src/client/skeleton/DetailsPanel.tsx           |   5 +-
 .../src/client/skeleton/ImageLightbox.module.css   |  34 +
 .../src/client/skeleton/ImageLightbox.tsx          |  40 +
 .../src/client/skeleton/InputBar.module.css        |  78 +-
 .../src/client/skeleton/InputBar.tsx               | 161 +++-
 .../client/ui-conversation/src/client/stores.ts    |   9 +-
 packages/client/ui-conversation/src/index.ts       |  25 +-
 .../ui-conversation/src/submission-settings.ts     |  29 +
 .../ui-conversation/tests/apply-inject.spec.tsx    |   1 +
 .../tests/assembly-surfaces.spec.tsx               |   4 +
 .../ui-conversation/tests/chat-apply.spec.tsx      |   7 +-
 .../tests/chat-branch-tails.spec.tsx               |   4 +-
 .../ui-conversation/tests/chat-store.spec.ts       |  13 -
 .../ui-conversation/tests/chat-view.spec.tsx       |  13 +-
 .../ui-conversation/tests/coverage-tails.spec.tsx  |   9 +-
 .../tests/gate-branch-tails.spec.tsx               |  16 +-
 packages/client/ui-conversation/tests/host.spec.ts |  30 +
 .../ui-conversation/tests/input-bar.spec.tsx       | 275 +++++-
 .../ui-conversation/tests/input-machine.spec.ts    |   6 +-
 .../ui-conversation/tests/input-matrix.spec.tsx    |  11 +-
 .../ui-conversation/tests/input-scenarios.spec.tsx |  11 +-
 .../ui-conversation/tests/message-image.spec.tsx   |  81 ++
 .../ui-conversation/tests/queue-dock.spec.tsx      |   9 +-
 .../tests/service-orchestration.spec.ts            | 143 +++-
 .../client/ui-conversation/tests/skeleton.spec.tsx |   9 +-
 .../tests/submission-policy.spec.ts                |  67 +-
 .../ui-conversation/tests/todo-panel.spec.tsx      |   4 +-
 packages/client/ui-conversation/tsconfig.json      |  12 +
 packages/client/ui-deliverables/package.json       |  16 +-
 packages/client/ui-deliverables/src/index.ts       |   2 +-
 .../ui-deliverables/tests/produced-files.spec.tsx  |   1 +
 packages/client/ui-goal/package.json               |  18 +-
 packages/client/ui-goal/src/client/index.ts        |   2 +-
 packages/client/ui-goal/src/index.ts               |   2 +-
 packages/client/ui-layout/package.json             |  14 +-
 packages/client/ui-layout/src/client/AppFrame.tsx  |   4 +-
 packages/client/ui-layout/tests/app-frame.spec.tsx |   2 +-
 packages/client/ui-layout/tests/apply.spec.ts      |   5 +-
 packages/client/ui-model/package.json              |  16 +-
 packages/client/ui-model/src/client/service.ts     |   2 +-
 packages/client/ui-model/src/index.ts              |   2 +-
 packages/client/ui-models/README.i18n.yaml         |   4 +-
 packages/client/ui-models/README.md                |   6 +-
 packages/client/ui-models/README.zh.md             |   8 +-
 packages/client/ui-models/package.json             |  16 +-
 .../ui-models/src/client/CustomProviderCard.tsx    |   2 +-
 .../ui-models/src/client/ModelsSection.module.css  |  16 +-
 .../client/ui-models/tests/components.spec.tsx     |   4 +-
 .../client/ui-models/tests/provider-form.spec.tsx  |  12 +-
 packages/client/ui-permission/package.json         |  18 +-
 packages/client/ui-permission/src/index.ts         |   2 +-
 packages/client/ui-plan/package.json               |  16 +-
 packages/client/ui-plan/src/index.ts               |   2 +-
 packages/client/ui-primitives/README.i18n.yaml     |   4 +-
 packages/client/ui-primitives/README.md            |   4 +-
 packages/client/ui-primitives/README.zh.md         |   4 +-
 .../client/ui-primitives/src/TerminalBlock.tsx     |   4 +-
 .../client/ui-primitives/src/Tooltip.module.css    |   4 +-
 packages/client/ui-primitives/src/icons/index.tsx  |  11 +
 .../client/ui-primitives/src/markdown/highlight.ts |  49 +-
 packages/client/ui-primitives/tests/ansi.spec.ts   |   8 +-
 .../client/ui-primitives/tests/code-block.spec.tsx |   2 +-
 .../client/ui-primitives/tests/hover-card.spec.tsx |   4 +-
 packages/client/ui-primitives/tests/icons.spec.tsx |   4 +-
 .../tests/markdown-incremental.spec.tsx            |   2 +-
 .../client/ui-primitives/tests/markdown.spec.tsx   |   2 +-
 packages/client/ui-primitives/tsdown.config.ts     |   2 +-
 packages/client/ui-question/README.i18n.yaml       |   4 +-
 packages/client/ui-question/README.md              |   2 +-
 packages/client/ui-question/README.zh.md           |   2 +-
 packages/client/ui-question/package.json           |  15 +-
 .../ui-question/src/client/contract/slots.ts       |   4 +-
 packages/client/ui-question/src/index.ts           |  25 +-
 .../client/ui-question/tests/node-plugin.spec.ts   |  15 +-
 packages/client/ui-question/tsconfig.json          |   3 -
 packages/client/ui-settings-general/package.json   |  18 +-
 .../ui-settings-general/tests/components.spec.tsx  |   2 +-
 packages/client/ui-settings/package.json           |  14 +-
 .../ui-settings/src/client/SettingsRoot.module.css |   9 +-
 .../client/ui-settings/src/client/SettingsRoot.tsx |   7 +-
 .../ui-settings/src/client/contract/slots.ts       |  12 +-
 packages/client/ui-settings/src/client/index.ts    |   2 +-
 .../ui-settings/tests/settings-root.spec.tsx       |   1 +
 packages/client/ui-sidebar/package.json            |  16 +-
 .../ui-sidebar/src/client/SidebarRoot.module.css   |   2 +-
 packages/client/ui-skill/README.i18n.yaml          |   4 +-
 packages/client/ui-skill/README.md                 |   4 +-
 packages/client/ui-skill/README.zh.md              |   4 +-
 packages/client/ui-skill/package.json              |  18 +-
 packages/client/ui-skill/src/client/index.ts       |  25 +-
 packages/client/ui-skill/src/index.ts              |   2 +-
 .../client/ui-skill/tests/browser-plugin.spec.ts   |  21 +-
 packages/client/ui-slash/README.i18n.yaml          |   4 +-
 packages/client/ui-slash/README.md                 |   2 +-
 packages/client/ui-slash/README.zh.md              |   2 +-
 packages/client/ui-slash/package.json              |  14 +-
 packages/client/ui-slash/src/client/controller.ts  |   5 +-
 packages/client/ui-slash/src/client/slots.ts       |   2 +-
 packages/client/ui-slash/src/core/contract.ts      |   8 +-
 packages/client/ui-slash/src/core/detect.ts        |   2 +-
 packages/client/ui-slash/src/core/menu.ts          |   2 +-
 packages/client/ui-slash/src/index.ts              |   2 +-
 packages/client/ui-slash/src/types.ts              |  12 +-
 packages/client/ui-slash/tests/core-detect.spec.ts |   4 +-
 packages/client/ui-slash/tests/core-menu.spec.ts   |   3 +-
 packages/client/ui-slash/tests/menu-view.spec.tsx  |   2 +-
 packages/client/ui-slash/tests/service.spec.ts     |   2 +-
 packages/client/ui-slots/src/index.ts              |   2 +-
 packages/client/ui-slots/src/renderer.ts           |   5 +-
 packages/client/ui-slots/tests/type-chain.spec.tsx |   2 +-
 packages/client/ui-subagent/package.json           |  20 +-
 packages/client/ui-subagent/src/client/index.ts    |  12 +-
 packages/client/ui-subagent/src/index.ts           |   2 +-
 .../ui-subagent/tests/browser-plugin.spec.ts       |  14 +-
 packages/client/ui-theme/README.i18n.yaml          |   4 +-
 packages/client/ui-theme/README.md                 |   4 +-
 packages/client/ui-theme/README.zh.md              |   4 +-
 packages/client/ui-theme/package.json              |  22 +-
 .../client/ui-theme/src/client/AppearanceRow.tsx   |   2 +-
 packages/client/ui-theme/src/client/index.ts       |  85 +-
 .../client/ui-theme/src/client/settings-store.ts   |   2 +-
 packages/client/ui-theme/src/index.ts              |  25 +-
 packages/client/ui-theme/src/invariant.ts          |   8 +-
 packages/client/ui-theme/src/theme-settings.ts     |  38 +
 packages/client/ui-theme/tests/apply.spec.ts       |  93 +-
 packages/client/ui-theme/tests/host.spec.ts        |  30 +
 packages/client/ui-theme/tests/invariant.spec.ts   |  19 +-
 packages/client/ui-theme/tests/theme.spec.ts       |  68 +-
 packages/client/ui-theme/tsconfig.json             |   3 +
 packages/client/ui-tool/README.i18n.yaml           |   4 +-
 packages/client/ui-tool/README.md                  |   6 +-
 packages/client/ui-tool/README.zh.md               |   6 +-
 packages/client/ui-tool/package.json               |  16 +-
 .../src/client/tool/models/search-card-model.ts    |  11 +-
 .../src/client/tool/toolviews/ask-question-row.tsx |   4 +-
 .../src/client/tool/toolviews/search-row.tsx       |   4 +-
 .../ui-tool/src/client/tool/toolviews/todo-row.tsx |   2 +-
 .../ui-tool/tests/assembly-surfaces.spec.tsx       |   1 +
 .../ui-tool/tests/chat-code-subcalls.spec.tsx      |   1 +
 packages/client/ui-tool/tests/diff-card.spec.tsx   |   8 +-
 packages/client/ui-tool/tests/read-card.spec.tsx   |   8 +-
 packages/client/ui-tool/tests/search-card.spec.tsx |   8 +-
 .../client/ui-tool/tests/terminal-card.spec.tsx    |   4 +-
 packages/client/ui-tool/tests/tool-row.spec.tsx    |   4 +-
 .../client/ui-tool/tests/toolview-slot.spec.tsx    |   2 +
 packages/client/ui-tool/tests/web-card.spec.tsx    |   8 +-
 packages/client/ui-trajectory/README.i18n.yaml     |   4 +-
 packages/client/ui-trajectory/README.md            |   2 +-
 packages/client/ui-trajectory/README.zh.md         |   2 +-
 packages/client/ui-trajectory/package.json         |  14 +-
 .../ui-trajectory/src/client/TrajectoryView.tsx    |   1 +
 packages/client/ui-trajectory/src/client/layout.ts |  10 +-
 packages/client/ui-trajectory/tests/views.spec.tsx |   9 +-
 packages/client/ui-workspace/package.json          |  18 +-
 .../ui-workspace/src/client/WorkspaceBrowser.tsx   |   4 +-
 packages/client/ui-workspace/src/client/index.ts   |   2 +-
 .../client/ui-workspace/src/client/rows/Rows.tsx   |   6 +-
 packages/client/ui-workspace/src/index.ts          |   2 +-
 .../ui-workspace/tests/rename-assembly.spec.tsx    |   5 +-
 packages/client/web-react/README.i18n.yaml         |   4 +-
 packages/client/web-react/README.md                |   2 +-
 packages/client/web-react/README.zh.md             |   2 +-
 packages/client/web-react/src/scoped-slots.tsx     |   4 +-
 packages/client/web-react/src/session-provider.tsx |   2 +-
 .../client/web-react/tests/scoped-slots.spec.tsx   |   4 +-
 .../web-react/tests/session-provider.spec.tsx      |   4 +-
 .../client/web-react/tests/use-projection.spec.tsx |   3 +-
 packages/client/web/src/AppRoot.tsx                |   2 +-
 packages/client/web/src/boot.tsx                   |  10 +-
 packages/client/web/src/index.ts                   |   2 +-
 packages/client/web/src/loader-status.ts           |   4 +-
 packages/client/web/src/seed.ts                    |   2 +-
 .../code-runtime-worker/src/bootstrap.ts           |   2 +-
 packages/code-runtime/code-runtime/src/index.ts    |  14 +-
 packages/compact/compact-basic/README.i18n.yaml    |   4 +-
 packages/compact/compact-basic/README.md           |   2 +-
 packages/compact/compact-basic/README.zh.md        |   2 +-
 packages/compact/compact-basic/src/summarizer.ts   |  11 +-
 .../compact-basic/tests/compact-basic.spec.ts      |  52 +-
 packages/context/README.i18n.yaml                  |   4 +-
 packages/context/README.md                         |   2 -
 packages/context/README.zh.md                      |   4 +-
 packages/context/time-context/src/invariant.ts     |   4 +-
 .../context/time-context/tests/invariant.spec.ts   |  10 +-
 .../context/workspace-context/README.i18n.yaml     |   4 +-
 packages/context/workspace-context/README.md       |   2 +-
 packages/context/workspace-context/README.zh.md    |   2 +-
 packages/context/workspace-context/src/files.ts    |  25 +-
 packages/context/workspace-context/src/render.ts   | 102 ++-
 packages/context/workspace-context/src/state.ts    |   4 +
 .../tests/workspace-context.spec.ts                | 180 +++-
 packages/core/README.i18n.yaml                     |   2 +-
 packages/core/README.md                            |   4 +-
 packages/core/agent-default-model/README.i18n.yaml |   2 +-
 packages/core/agent-default-model/README.md        |   6 +-
 packages/core/agent-default-model/package.json     |   2 +-
 packages/core/agent-default-model/src/index.ts     |   2 +-
 packages/core/agent-tool-mode/README.i18n.yaml     |   6 +
 packages/core/agent-tool-mode/README.md            |  31 +
 packages/core/agent-tool-mode/README.zh.md         |  31 +
 packages/core/agent-tool-mode/package.json         |  45 +
 packages/core/agent-tool-mode/src/index.ts         |  70 ++
 packages/core/agent-tool-mode/src/invariant.ts     |  32 +
 .../agent-tool-mode/tests/agent-tool-mode.spec.ts  | 129 +++
 packages/core/agent-tool-mode/tsconfig.json        |  27 +
 packages/core/agent/src/index.ts                   |   1 +
 packages/core/agent/src/model-selection.ts         |   4 +-
 packages/core/scope/README.i18n.yaml               |   4 +-
 packages/core/scope/README.md                      |  11 +-
 packages/core/scope/README.zh.md                   |   9 +-
 packages/core/scope/src/index.ts                   |  95 ++-
 packages/core/scope/src/store.ts                   |  34 +-
 packages/core/scope/tests/scope.spec.ts            |  69 +-
 packages/core/session/src/chunk-rows.ts            |   3 +-
 packages/core/session/src/index.ts                 |   8 +-
 packages/core/session/src/types.ts                 |  11 +-
 packages/core/session/tests/session.spec.ts        |   1 +
 packages/core/system-prompt/src/index.ts           |  27 +-
 packages/core/tools/README.i18n.yaml               |   4 +-
 packages/core/tools/README.md                      |  15 +-
 packages/core/tools/README.zh.md                   |  15 +-
 packages/core/tools/src/code-mode.ts               |  50 +-
 packages/core/tools/src/index.ts                   | 298 +++++--
 packages/core/tools/src/json-schema.ts             |   4 +-
 packages/core/tools/src/py-types.ts                |  18 +-
 packages/core/tools/tests/code-mode.spec.ts        | 134 ++-
 packages/core/tools/tests/scoped.spec.ts           |  75 +-
 .../credentials/credentials-local/README.i18n.yaml |   4 +-
 packages/credentials/credentials-local/README.md   |   2 +-
 .../credentials/credentials-local/README.zh.md     |   2 +-
 .../credentials/credentials-local/src/index.ts     |  20 +-
 .../credentials-local/tests/local.spec.ts          |  15 +-
 .../credentials-local/tests/review-fixes.spec.ts   |   2 +-
 .../credentials-local/tests/watcher.spec.ts        |  35 +
 packages/e2b/subprocess-e2b/README.i18n.yaml       |   4 +-
 packages/e2b/subprocess-e2b/README.md              |   2 +-
 packages/e2b/subprocess-e2b/README.zh.md           |   2 +-
 packages/e2b/subprocess-e2b/tests/terminal.spec.ts |  16 +
 packages/examples/README.i18n.yaml                 |   4 +-
 packages/examples/README.md                        |   6 +-
 packages/examples/README.zh.md                     |   4 +-
 packages/examples/acp-demo/README.i18n.yaml        |   4 +-
 packages/examples/acp-demo/README.md               |   2 +-
 packages/examples/acp-demo/README.zh.md            |   2 +-
 packages/examples/acp-demo/src/index.ts            |   4 +-
 .../examples/agent-spine-demo/README.i18n.yaml     |   4 +-
 packages/examples/agent-spine-demo/README.md       |  12 +-
 packages/examples/agent-spine-demo/README.zh.md    |  12 +-
 packages/examples/agent-spine-demo/src/index.ts    |   2 +-
 .../agent-spine-demo/tests/agent-core.spec.ts      |  22 +-
 packages/experimental/AGENTS.md                    |   4 +-
 .../feedback/command-feedback/README.i18n.yaml     |   4 +-
 packages/feedback/command-feedback/README.md       |   6 +-
 packages/feedback/command-feedback/README.zh.md    |   4 +-
 packages/feedback/command-feedback/package.json    |   2 +
 packages/feedback/command-feedback/src/index.ts    |   9 +-
 .../tests/command-feedback.spec.ts                 |  20 +-
 .../tests/loader-composition.spec.ts               |  11 +-
 packages/feedback/command-feedback/tsconfig.json   |   3 +
 packages/fs/README.i18n.yaml                       |   4 +-
 packages/fs/README.md                              |   8 +-
 packages/fs/README.zh.md                           |   8 +-
 packages/fs/fs-local/README.i18n.yaml              |   4 +-
 packages/fs/fs-local/README.md                     |   4 +-
 packages/fs/fs-local/README.zh.md                  |   4 +-
 packages/fs/fs-local/src/fsio.ts                   |  77 +-
 packages/fs/fs-local/src/index.ts                  |  35 +-
 packages/fs/fs-local/tests/filesystem.spec.ts      |  75 ++
 packages/fs/fs-local/tests/fsio.spec.ts            | 258 +++++-
 packages/fs/fs-policy/src/types.ts                 |  12 +-
 packages/fs/fs-sandbox/README.i18n.yaml            |   4 +-
 packages/fs/fs-sandbox/README.md                   |   2 +
 packages/fs/fs-sandbox/README.zh.md                |   2 +
 packages/fs/fs-sandbox/src/index.ts                |   8 +-
 packages/fs/fs/README.i18n.yaml                    |   4 +-
 packages/fs/fs/README.md                           |   2 +-
 packages/fs/fs/README.zh.md                        |   2 +-
 packages/fs/fs/src/types.ts                        |   9 +-
 packages/fs/tool-fs-search/README.i18n.yaml        |   4 +-
 packages/fs/tool-fs-search/README.md               |   2 +-
 packages/fs/tool-fs-search/README.zh.md            |   2 +-
 packages/fs/tool-fs-search/src/grep.ts             |   2 +-
 packages/fs/tool-fs/README.i18n.yaml               |   4 +-
 packages/fs/tool-fs/README.md                      |   2 +-
 packages/fs/tool-fs/README.zh.md                   |   2 +-
 packages/fs/tool-fs/src/edit.ts                    |   2 +-
 packages/fs/tool-fs/src/write.ts                   |   2 +-
 packages/goal/goal/src/domain.ts                   |   6 +-
 packages/goal/goal/src/fold.ts                     |  10 +-
 packages/goal/goal/tests/goal.spec.ts              |  10 +-
 packages/guard/timeout-policy/README.i18n.yaml     |   4 +-
 packages/guard/timeout-policy/README.md            |   2 +-
 packages/guard/timeout-policy/README.zh.md         |   2 +-
 packages/hooks/hook-protocol/README.i18n.yaml      |   4 +-
 packages/hooks/hook-protocol/README.md             |   2 +-
 packages/hooks/hook-protocol/README.zh.md          |   2 +-
 packages/hooks/hooks-claude/src/index.ts           |   6 +-
 packages/hooks/hooks-codex/README.i18n.yaml        |   4 +-
 packages/hooks/hooks-codex/README.md               |   2 +-
 packages/hooks/hooks-codex/README.zh.md            |   2 +-
 packages/hooks/hooks-codex/src/index.ts            |   2 +-
 packages/host/apiproxy/README.i18n.yaml            |   4 +-
 packages/host/apiproxy/README.md                   |  24 +-
 packages/host/apiproxy/README.zh.md                |  24 +-
 packages/host/apiproxy/package.json                |  11 +-
 packages/host/apiproxy/src/api-proxy.ts            | 950 +++++++++++++++++----
 .../host/apiproxy/src/api/agent-presets.schema.ts  |  88 ++
 packages/host/apiproxy/src/api/agent-presets.ts    | 116 +++
 packages/host/apiproxy/src/api/approvals.schema.ts |   2 +-
 packages/host/apiproxy/src/api/commands.schema.ts  |   2 +-
 packages/host/apiproxy/src/api/events.schema.ts    |   4 +-
 packages/host/apiproxy/src/api/events.ts           |  13 +
 packages/host/apiproxy/src/api/host.schema.ts      |   2 -
 packages/host/apiproxy/src/api/index.ts            |   6 +-
 packages/host/apiproxy/src/api/rpc-map.ts          |   8 +
 packages/host/apiproxy/src/api/rpc.schema.ts       |  10 +-
 packages/host/apiproxy/src/api/rpc.ts              |   6 +
 packages/host/apiproxy/src/api/sessions.schema.ts  |  47 +-
 packages/host/apiproxy/src/api/sessions.ts         |  32 +-
 packages/host/apiproxy/src/api/workspace.schema.ts |  10 +-
 packages/host/apiproxy/src/api/workspace.ts        |  19 +-
 packages/host/apiproxy/src/fetch/client.ts         |  36 +
 packages/host/apiproxy/src/fetch/handler.ts        |  12 +
 packages/host/apiproxy/src/index.ts                |  32 +-
 packages/host/apiproxy/src/native-path-opener.ts   |  19 +
 .../apiproxy/tests/api-proxy-agent-preset.spec.ts  | 727 ++++++++++++++++
 .../host/apiproxy/tests/api-proxy-approval.spec.ts |   4 +-
 .../host/apiproxy/tests/api-proxy-blank.spec.ts    |   2 +-
 .../host/apiproxy/tests/api-proxy-cold.spec.ts     |  34 +-
 .../host/apiproxy/tests/api-proxy-commands.spec.ts |   2 +-
 .../host/apiproxy/tests/api-proxy-config.spec.ts   |  74 +-
 .../host/apiproxy/tests/api-proxy-fork.spec.ts     |   1 -
 .../host/apiproxy/tests/api-proxy-models.spec.ts   | 162 +++-
 .../apiproxy/tests/api-proxy-projections.spec.ts   |   2 +-
 .../host/apiproxy/tests/api-proxy-question.spec.ts |   2 +-
 .../host/apiproxy/tests/api-proxy-rename.spec.ts   |   2 +-
 .../host/apiproxy/tests/api-proxy-search.spec.ts   |   2 +-
 .../apiproxy/tests/api-proxy-subagents.spec.ts     |   2 +-
 .../host/apiproxy/tests/api-proxy-view.spec.ts     |  10 +-
 .../apiproxy/tests/api-proxy-workspace.spec.ts     |  85 +-
 .../host/apiproxy/tests/client-handler.spec.ts     |  30 +-
 packages/host/apiproxy/tests/fetch-carrier.spec.ts |  55 ++
 .../host/apiproxy/tests/native-path-opener.spec.ts |  34 +-
 packages/host/apiproxy/tests/rpc-schemas.spec.ts   |  36 +-
 packages/host/apiproxy/tsconfig.json               |   6 +
 .../host/directory-picker-auto/README.i18n.yaml    |   4 +-
 packages/host/directory-picker-auto/README.md      |   2 +-
 packages/host/directory-picker-auto/README.zh.md   |   2 +-
 .../tests/loader-composition.spec.ts               |  48 ++
 packages/host/directory-picker-browse/package.json |  16 +-
 .../src/client/DirectoryBrowser.tsx                |   3 +-
 packages/host/directory-picker-native/package.json |  14 +-
 .../directory-picker-native/src/native-picker.ts   |   4 +-
 packages/host/directory-picker/README.i18n.yaml    |   4 +-
 packages/host/directory-picker/README.md           |   4 +-
 packages/host/directory-picker/README.zh.md        |   4 +-
 packages/host/webserver/README.i18n.yaml           |   4 +-
 packages/host/webserver/README.md                  |   4 +-
 packages/host/webserver/README.zh.md               |   4 +-
 packages/host/webserver/src/index.ts               |  15 +-
 packages/interaction/permission/src/invariant.ts   |   2 +-
 packages/interaction/user-approval/src/index.ts    |   3 +-
 .../interaction/user-interaction/README.i18n.yaml  |   4 +-
 packages/interaction/user-interaction/README.md    |   2 +-
 packages/interaction/user-interaction/README.zh.md |   2 +-
 packages/interaction/user-interaction/src/types.ts |   8 +-
 packages/llm/llm-deepseek/src/adapter.ts           |   7 +-
 packages/llm/llm-deepseek/src/serialize.ts         |  13 +-
 packages/llm/llm-deepseek/tests/adapter.spec.ts    |  12 +-
 .../llm/llm-deepseek/tests/dynamic-config.spec.ts  |   4 +-
 .../llm-deepseek/tests/loader-composition.spec.ts  |   2 +-
 packages/llm/llm-deepseek/tests/serialize.spec.ts  |  16 +-
 packages/llm/llm-pi-ai/README.i18n.yaml            |   4 +-
 packages/llm/llm-pi-ai/README.md                   |   2 +-
 packages/llm/llm-pi-ai/README.zh.md                |   2 +-
 packages/llm/llm-pi-ai/package.json                |   2 +
 packages/llm/llm-pi-ai/src/adapter.ts              |  19 +-
 packages/llm/llm-pi-ai/src/catalog.ts              |  15 +-
 packages/llm/llm-pi-ai/src/config.ts               |   8 +-
 packages/llm/llm-pi-ai/src/context.ts              | 170 +++-
 packages/llm/llm-pi-ai/src/index.ts                |   6 +-
 packages/llm/llm-pi-ai/src/replay.ts               |   2 +
 packages/llm/llm-pi-ai/tests/adapter.spec.ts       | 120 ++-
 packages/llm/llm-pi-ai/tests/catalog.spec.ts       |   2 +-
 packages/llm/llm-pi-ai/tests/context.spec.ts       | 186 ++++
 packages/llm/llm-pi-ai/tests/convert.spec.ts       | 112 ++-
 packages/llm/llm-pi-ai/tests/discovery.spec.ts     |  26 +-
 packages/llm/llm-pi-ai/tests/provider-apis.e2e.ts  |  82 +-
 packages/llm/llm-pi-ai/tsconfig.json               |   3 +
 packages/llm/llm/README.i18n.yaml                  |   4 +-
 packages/llm/llm/README.md                         |   2 +-
 packages/llm/llm/README.zh.md                      |   2 +-
 packages/llm/llm/package.json                      |   2 +
 packages/llm/llm/src/content.ts                    |  16 +
 packages/llm/llm/src/index.ts                      |  17 +-
 packages/llm/llm/src/message.ts                    |  14 +-
 packages/llm/llm/src/types.ts                      |  33 +-
 packages/llm/llm/tests/service.spec.ts             |  21 +
 packages/llm/llm/tsconfig.json                     |   3 +
 packages/llm/token-meter/README.i18n.yaml          |   4 +-
 packages/llm/token-meter/README.md                 |   4 +-
 packages/llm/token-meter/README.zh.md              |   4 +-
 packages/llm/token-meter/src/index.ts              |   4 +-
 packages/llm/token-meter/tests/token-meter.spec.ts |   2 +-
 packages/lsp/lsp-local/tests/provider.spec.ts      |   8 +-
 packages/lsp/lsp/src/types.ts                      |   2 +-
 packages/lsp/tool-lsp/tests/render.spec.ts         |   4 +-
 packages/mcp/mcp-client/src/tools.ts               |   5 +-
 packages/mcp/mcp-client/src/transport.ts           |   5 +-
 packages/mcp/mcp-client/tests/apply.spec.ts        |   1 -
 packages/mcp/mcp-client/tests/mcp-client.spec.ts   |   7 +-
 packages/plan/plan-mode/README.i18n.yaml           |   4 +-
 packages/plan/plan-mode/README.md                  |  12 +-
 packages/plan/plan-mode/README.zh.md               |  12 +-
 packages/plan/plan-mode/src/index.ts               |  79 +-
 packages/plan/plan-mode/src/types.ts               |   4 +-
 packages/plan/plan-mode/tests/projection.spec.ts   |   2 +-
 packages/preset/README.i18n.yaml                   |   6 +
 packages/preset/README.md                          |  16 +
 packages/preset/README.zh.md                       |  16 +
 packages/preset/agent-presets/README.i18n.yaml     |   6 +
 packages/preset/agent-presets/README.md            | 140 +++
 packages/preset/agent-presets/README.zh.md         | 140 +++
 packages/preset/agent-presets/package.json         |  59 ++
 packages/preset/agent-presets/src/authoring.ts     | 196 +++++
 packages/preset/agent-presets/src/discovery.ts     | 171 ++++
 packages/preset/agent-presets/src/index.ts         | 507 +++++++++++
 packages/preset/agent-presets/src/invariant.ts     |  48 ++
 packages/preset/agent-presets/src/metadata.ts      | 105 +++
 packages/preset/agent-presets/src/mount.ts         | 381 +++++++++
 packages/preset/agent-presets/src/session.ts       |  54 ++
 packages/preset/agent-presets/src/types.ts         |  88 ++
 .../preset/agent-presets/tests/authoring.spec.ts   | 296 +++++++
 .../preset/agent-presets/tests/discovery.spec.ts   | 221 +++++
 .../tests/fixtures/plugins/contribute.js           |  20 +
 .../tests/fixtures/plugins/global-service.js       |   5 +
 .../tests/fixtures/plugins/late-service.js         |   6 +
 .../tests/fixtures/plugins/needs-missing.js        |   5 +
 .../tests/fixtures/plugins/self-dispose.js         |   9 +
 .../tests/fixtures/system/minimal/agent.cordis.yml |   4 +
 .../fixtures/system/standard/agent.cordis.yml      |  12 +
 .../tests/fixtures/user/broken/agent.cordis.yml    |   6 +
 .../tests/fixtures/user/isolated/agent.cordis.yml  |   9 +
 .../tests/fixtures/user/late/agent.cordis.yml      |   6 +
 .../tests/fixtures/user/leaky/agent.cordis.yml     |  13 +
 .../tests/fixtures/user/not-a-preset/notes.txt     |   1 +
 .../tests/fixtures/user/pending/agent.cordis.yml   |   2 +
 .../tests/fixtures/user/standard/agent.cordis.yml  |   5 +
 .../fixtures/user/two-broken/agent.cordis.yml      |   7 +
 .../preset/agent-presets/tests/invariant.spec.ts   |  87 ++
 .../preset/agent-presets/tests/metadata.spec.ts    | 114 +++
 packages/preset/agent-presets/tests/mount.spec.ts  | 692 +++++++++++++++
 .../preset/agent-presets/tests/session.spec.ts     |  62 ++
 .../preset/agent-presets/tests/settings.spec.ts    | 163 ++++
 packages/preset/agent-presets/tsconfig.json        |  40 +
 packages/preset/persona/README.i18n.yaml           |   6 +
 packages/preset/persona/README.md                  |  39 +
 packages/preset/persona/README.zh.md               |  39 +
 packages/preset/persona/package.json               |  41 +
 packages/preset/persona/src/index.ts               |  60 ++
 packages/preset/persona/src/invariant.ts           |  30 +
 packages/preset/persona/tests/persona.spec.ts      |  88 ++
 packages/preset/persona/tsconfig.json              |  25 +
 packages/pty/pty-local/tests/index.spec.ts         |   4 +-
 packages/pty/pty-local/tests/local.spec.ts         |   2 +-
 .../pty/tool-bash-persistent/tests/tools.spec.ts   |  37 +-
 packages/sandbox/sandbox-local/README.i18n.yaml    |   4 +-
 packages/sandbox/sandbox-local/README.md           |   2 +-
 packages/sandbox/sandbox-local/README.zh.md        |   2 +-
 packages/sandbox/sandbox-local/package.json        |   5 +-
 packages/sandbox/sandbox-local/src/index.ts        | 296 ++++++-
 .../sandbox/sandbox-local/tests/acl-grants.spec.ts | 404 +++++++++
 packages/sandbox/sandbox-local/tests/local.spec.ts |  71 +-
 .../sandbox-local/tests/packed-install.e2e.ts      |   5 +
 packages/sandbox/sandbox-local/tsconfig.json       |   6 +
 packages/sandbox/sandbox-policy/src/index.ts       |   1 +
 packages/sandbox/sandbox-policy/src/invariant.ts   |   2 +-
 .../sandbox/sandbox-policy/tests/policy.spec.ts    |   4 +
 .../sandbox/sandbox-windows-acl/README.i18n.yaml   |   6 +
 packages/sandbox/sandbox-windows-acl/README.md     |  91 ++
 packages/sandbox/sandbox-windows-acl/README.zh.md  |  93 ++
 packages/sandbox/sandbox-windows-acl/package.json  |  45 +
 packages/sandbox/sandbox-windows-acl/src/acl.ts    | 271 ++++++
 packages/sandbox/sandbox-windows-acl/src/errors.ts |  21 +
 packages/sandbox/sandbox-windows-acl/src/ffi.ts    | 512 +++++++++++
 packages/sandbox/sandbox-windows-acl/src/grant.ts  | 107 +++
 packages/sandbox/sandbox-windows-acl/src/index.ts  | 392 +++++++++
 .../sandbox/sandbox-windows-acl/src/invariant.ts   |  31 +
 packages/sandbox/sandbox-windows-acl/src/runner.ts | 196 +++++
 packages/sandbox/sandbox-windows-acl/src/spawn.ts  | 357 ++++++++
 packages/sandbox/sandbox-windows-acl/src/token.ts  | 220 +++++
 .../sandbox/sandbox-windows-acl/src/win32-abi.ts   | 258 ++++++
 .../sandbox-windows-acl/src/workspace-sid.ts       |  38 +
 .../tests/acl-failure-paths.spec.ts                | 456 ++++++++++
 .../sandbox/sandbox-windows-acl/tests/acl.spec.ts  | 281 ++++++
 .../tests/failure-paths.spec.ts                    | 454 ++++++++++
 .../sandbox/sandbox-windows-acl/tests/ffi.spec.ts  | 202 +++++
 .../tests/grant-failure-paths.spec.ts              | 100 +++
 .../sandbox-windows-acl/tests/grant.spec.ts        |  77 ++
 .../tests/index-failure-paths.spec.ts              | 389 +++++++++
 .../sandbox-windows-acl/tests/probe.spec.ts        |  97 +++
 .../tests/provider-chain.spec.ts                   |  58 ++
 .../sandbox-windows-acl/tests/quote.spec.ts        |  88 ++
 .../sandbox-windows-acl/tests/runner.spec.ts       | 294 +++++++
 .../tests/token-failure-paths.spec.ts              | 436 ++++++++++
 .../tests/workspace-sid.spec.ts                    |  30 +
 packages/sandbox/sandbox-windows-acl/tsconfig.json |  22 +
 .../sandbox/sandbox-windows-acl/tsdown.config.ts   |  16 +
 .../sandbox-windows-acl/verify/abi-probe.cpp       | 195 +++++
 packages/sandbox/sandbox/README.i18n.yaml          |   4 +-
 packages/sandbox/sandbox/README.md                 |   2 +-
 packages/sandbox/sandbox/README.zh.md              |   2 +-
 packages/sandbox/sandbox/package.json              |   2 +
 packages/sandbox/sandbox/src/index.ts              |  14 +-
 packages/sandbox/sandbox/tsconfig.json             |   3 +
 packages/scaffold/README.i18n.yaml                 |   4 +-
 packages/scaffold/README.md                        |   2 +-
 packages/scaffold/README.zh.md                     |   2 +-
 packages/scaffold/client/src/api.ts                |   2 +-
 packages/scaffold/client/tests/sdk-client.spec.ts  |   9 +-
 .../scaffold/helper/src/documents/tsconfig-file.ts |   2 +-
 .../scaffold/helper/src/features/builtin/app.ts    |   6 +-
 .../scaffold/helper/src/features/define-feature.ts |   2 +-
 packages/scaffold/helper/src/features/feature.ts   |   6 +-
 packages/scaffold/helper/src/project/types.ts      |   2 +-
 packages/scaffold/helper/tests/project.spec.ts     |   2 +-
 packages/scaffold/server/tests/server.spec.ts      |   4 +-
 packages/scaffold/telemetry/README.i18n.yaml       |   4 +-
 packages/scaffold/telemetry/README.md              |   2 +-
 packages/scaffold/telemetry/README.zh.md           |   2 +-
 packages/self-modification/README.i18n.yaml        |   4 +-
 packages/self-modification/README.md               |   2 +-
 packages/self-modification/README.zh.md            |   2 +-
 .../repository-plugin/src/index.ts                 |   2 +-
 .../tool-cordis/src/api-catalog.ts                 | 182 +++-
 .../self-modification/tool-cordis/src/sandbox.ts   |   6 +-
 .../session-query-sqlite/README.i18n.yaml          |   4 +-
 .../session-query/session-query-sqlite/README.md   |   2 +-
 .../session-query-sqlite/README.zh.md              |   2 +-
 .../session-query-sqlite/src/index.ts              |  52 +-
 .../session-query-sqlite/src/schema.ts             |   4 +-
 .../session-query-sqlite/tests/sqlite.spec.ts      |   9 +-
 packages/session-query/session-query/src/index.ts  |   4 +-
 .../tests/sqlite-integration.spec.ts               |   2 +-
 .../session-persistence-jsonl/README.i18n.yaml     |   4 +-
 .../session/session-persistence-jsonl/README.md    |   2 +-
 .../session/session-persistence-jsonl/README.zh.md |   2 +-
 .../session-persistence-jsonl/src/format.ts        |   9 +-
 .../session/session-persistence-jsonl/src/win32.ts |   7 +-
 .../session-persistence-jsonl/tests/jsonl.spec.ts  |  35 +-
 .../session-persistence-jsonl/tests/win32.spec.ts  |  32 +
 .../session-persistence-sqlite/README.i18n.yaml    |   4 +-
 .../session/session-persistence-sqlite/README.md   |   5 +-
 .../session-persistence-sqlite/README.zh.md        |   5 +-
 .../session-persistence-sqlite/src/index.ts        |   8 +-
 .../session-persistence-sqlite/src/schema.ts       |   5 +-
 .../tests/sqlite.spec.ts                           |  22 +-
 .../session/session-persistence/README.i18n.yaml   |   4 +-
 packages/session/session-persistence/README.md     |   8 +-
 packages/session/session-persistence/README.zh.md  |   8 +-
 .../session/session-projection-cache/src/spec.ts   |   3 +-
 packages/session/session-projection/src/index.ts   |  46 +-
 .../session-projection/tests/registry.spec.ts      |  35 +-
 .../session/session-telemetry-otel/package.json    |   6 +-
 .../session/session-telemetry-otel/src/index.ts    |  24 +-
 .../session-telemetry-otel/tests/otel.spec.ts      |   2 +-
 .../session/session-telemetry-otel/tsconfig.json   |   5 +-
 .../session/session-telemetry/README.i18n.yaml     |   4 +-
 packages/session/session-telemetry/README.md       |   4 +-
 packages/session/session-telemetry/README.zh.md    |   4 +-
 packages/session/session-telemetry/src/index.ts    |  13 +-
 packages/session/user-id/README.i18n.yaml          |   6 +
 packages/session/user-id/README.md                 |  29 +
 packages/session/user-id/README.zh.md              |  29 +
 packages/session/user-id/package.json              |  39 +
 .../src/user-id.ts => user-id/src/index.ts}        |  26 +-
 packages/session/user-id/src/invariant.ts          |  31 +
 packages/session/user-id/tests/invariant.spec.ts   |  12 +
 .../tests/user-id.spec.ts                          |  10 +-
 packages/session/user-id/tsconfig.json             |  21 +
 packages/settings/settings-local/README.i18n.yaml  |   4 +-
 packages/settings/settings-local/README.md         |   1 +
 packages/settings/settings-local/README.zh.md      |   1 +
 packages/settings/settings-local/src/index.ts      |   4 +-
 .../settings-local/tests/concurrency.spec.ts       |   2 +-
 .../settings/settings-local/tests/local.spec.ts    |  31 +-
 packages/settings/settings/README.i18n.yaml        |   4 +-
 packages/settings/settings/README.md               |   2 +-
 packages/settings/settings/README.zh.md            |   2 +-
 packages/settings/settings/src/index.ts            |  24 +-
 packages/settings/settings/tests/settings.spec.ts  |  10 +-
 packages/skill/skill-local/README.i18n.yaml        |   4 +-
 packages/skill/skill-local/README.md               |   6 +-
 packages/skill/skill-local/README.zh.md            |   6 +-
 packages/skill/skill-local/src/index.ts            |  36 +-
 .../skill-local/tests/skill-local-watcher.spec.ts  |  80 +-
 packages/skill/skill/README.i18n.yaml              |   4 +-
 packages/skill/skill/README.md                     |  16 +-
 packages/skill/skill/README.zh.md                  |  16 +-
 packages/skill/skill/package.json                  |   2 +
 packages/skill/skill/src/index.ts                  | 245 ++++--
 packages/skill/skill/tests/skill.spec.ts           | 193 +++++
 packages/skill/skill/tsconfig.json                 |   3 +
 packages/skill/tool-skill/README.i18n.yaml         |   4 +-
 packages/skill/tool-skill/README.md                |   2 +-
 packages/skill/tool-skill/README.zh.md             |   2 +-
 packages/skill/tool-skill/src/index.ts             |  20 +-
 packages/skill/tool-skill/tests/tool-skill.spec.ts |  47 +-
 packages/storage/storage-domain/src/spec.ts        |   2 +-
 .../storage-json/tests/json-backend.spec.ts        |  14 +-
 packages/storage/storage-sqlite/README.i18n.yaml   |   4 +-
 packages/storage/storage-sqlite/README.md          |   4 +-
 packages/storage/storage-sqlite/README.zh.md       |   4 +-
 .../storage-sqlite/tests/sqlite-backend.spec.ts    |   7 +
 packages/storage/storage/src/backend.ts            |  12 +-
 packages/subagent/subagent-acp/README.i18n.yaml    |   4 +-
 packages/subagent/subagent-acp/README.md           |   4 +-
 packages/subagent/subagent-acp/README.zh.md        |   4 +-
 packages/subagent/subagent-acp/src/index.ts        |   2 +-
 packages/subagent/subagent-acp/src/run.ts          |   6 +-
 .../subagent-acp/tests/subagent-acp.spec.ts        |  38 +-
 .../subagent/subagent-claude-code/README.i18n.yaml |   4 +-
 packages/subagent/subagent-claude-code/README.md   |   2 +-
 .../subagent/subagent-claude-code/README.zh.md     |   2 +-
 .../tests/real-product.spec.ts                     |   4 +-
 packages/subagent/subagent-codex/README.i18n.yaml  |   4 +-
 packages/subagent/subagent-codex/README.md         |   8 +-
 packages/subagent/subagent-codex/README.zh.md      |   8 +-
 packages/subagent/subagent-codex/package.json      |   2 +-
 packages/subagent/subagent-codex/src/wire.ts       |   2 +-
 .../subagent-codex/tests/real-deepseek.e2e.ts      |   4 +-
 .../subagent-codex/tests/real-product.spec.ts      |  41 +-
 .../subagent-codex/tests/responses-fixture.ts      |  44 +-
 .../subagent-codex/tests/subagent-codex.spec.ts    |  12 +-
 .../subagent-fork/tests/subagent-fork.spec.ts      |   2 -
 packages/subagent/subagent-inprocess/package.json  |   3 +
 packages/subagent/subagent-inprocess/src/index.ts  |   2 +-
 .../tests/fixtures/plugins/preset-tool.js          |  20 +
 .../tests/fixtures/presets/coding/agent.cordis.yml |   5 +
 .../fixtures/presets/reviewing/agent.cordis.yml    |   6 +
 .../tests/preset-inheritance.spec.ts               | 135 +++
 .../tests/subagent-inprocess.spec.ts               |   2 +-
 .../subagent-spawn/tests/subagent-spawn.spec.ts    |   2 +-
 packages/subagent/subagent/README.i18n.yaml        |   4 +-
 packages/subagent/subagent/README.md               |   4 +
 packages/subagent/subagent/README.zh.md            |   4 +
 packages/subagent/subagent/package.json            |   5 +
 packages/subagent/subagent/src/child-agent.ts      |  47 +-
 packages/subagent/subagent/src/continuation.ts     |   2 +-
 packages/subagent/subagent/src/list-children.ts    |   9 +-
 packages/subagent/subagent/src/types.ts            |   7 +-
 .../subagent/subagent/tests/list-children.spec.ts  |   4 +-
 packages/subagent/subagent/tsconfig.json           |   3 +
 .../tests/tool-subagent-report.spec.ts             |   8 +-
 .../tool-subagent/tests/tool-subagent.spec.ts      |   2 +-
 .../subprocess/subprocess-local/README.i18n.yaml   |   4 +-
 packages/subprocess/subprocess-local/README.md     |   4 +-
 packages/subprocess/subprocess-local/README.zh.md  |   4 +-
 packages/subprocess/subprocess/src/index.ts        |   4 +-
 packages/support/acp-snapshot/README.i18n.yaml     |   4 +-
 packages/support/acp-snapshot/README.md            |   2 +-
 packages/support/acp-snapshot/README.zh.md         |   2 +-
 packages/support/acp-snapshot/src/harness.ts       |   4 +-
 packages/support/acp-snapshot/src/suite.ts         |   2 +-
 packages/support/invariants/README.i18n.yaml       |   4 +-
 packages/support/invariants/README.md              |   4 +-
 packages/support/invariants/README.zh.md           |   4 +-
 packages/support/llm-replay/README.i18n.yaml       |   4 +-
 packages/support/llm-replay/README.md              |   2 +-
 packages/support/llm-replay/README.zh.md           |   2 +-
 packages/support/llm-replay/src/index.ts           |  31 +-
 .../support/llm-replay/tests/llm-replay.spec.ts    |  20 +-
 packages/tasks/tasks-local/README.i18n.yaml        |   4 +-
 packages/tasks/tasks-local/README.md               |   2 +
 packages/tasks/tasks-local/README.zh.md            |   2 +
 packages/tasks/tasks-local/package.json            |   2 +
 packages/tasks/tasks-local/src/index.ts            |  93 +-
 packages/tasks/tasks-local/tests/tasks.spec.ts     |  99 ++-
 packages/tasks/tasks-local/tsconfig.json           |   3 +
 packages/tasks/tasks/README.i18n.yaml              |   4 +-
 packages/tasks/tasks/README.md                     |   4 +-
 packages/tasks/tasks/README.zh.md                  |   4 +-
 packages/tasks/tasks/src/index.ts                  |  28 +-
 packages/tasks/tool-tasks/README.i18n.yaml         |   4 +-
 packages/tasks/tool-tasks/README.md                |   2 +
 packages/tasks/tool-tasks/README.zh.md             |   2 +
 packages/tasks/tool-tasks/src/index.ts             |   4 +
 packages/tasks/tool-tasks/tests/tool-tasks.spec.ts |  51 +-
 packages/todo/tool-todo/src/index.ts               |   1 -
 packages/todo/tool-todo/src/invariant.ts           |   2 +-
 packages/todo/tool-todo/tests/projection.spec.ts   |   2 +-
 packages/typert/generator/README.i18n.yaml         |   4 +-
 packages/typert/generator/README.md                |   2 +-
 packages/typert/generator/README.zh.md             |   2 +-
 packages/typert/generator/src/analyzer.ts          |  13 +-
 .../typert/generator/tests/remote-model.spec.ts    |  19 +-
 packages/typert/generator/tests/type-model.spec.ts |  15 +-
 packages/typert/loader/src/index.ts                |   6 +-
 packages/typert/loader/tests/loader.spec.ts        |   8 +-
 packages/typert/registry/package.json              |  10 +-
 .../util/atomic-write/tests/atomic-write.spec.ts   |  20 +-
 packages/util/paths/README.i18n.yaml               |   4 +-
 packages/util/paths/README.md                      |   6 +-
 packages/util/paths/README.zh.md                   |   6 +-
 packages/util/paths/src/index.ts                   |  40 +-
 packages/util/paths/tests/paths.spec.ts            |  22 +-
 packages/util/retention/README.i18n.yaml           |   4 +-
 packages/util/retention/README.md                  |   2 +-
 packages/util/retention/README.zh.md               |   2 +-
 packages/util/retention/src/index.ts               |  11 +-
 packages/util/timeout/README.i18n.yaml             |   4 +-
 packages/util/timeout/README.md                    |   2 +-
 packages/util/timeout/README.zh.md                 |   2 +-
 packages/web/tool-web/src/index.ts                 |   2 +-
 packages/web/web-fetch-local/src/index.ts          |   2 +-
 packages/web/web-fetch-local/src/provider.ts       |   2 +-
 packages/web/web-search-deepseek/README.i18n.yaml  |   4 +-
 packages/web/web-search-deepseek/README.md         |   2 +-
 packages/web/web-search-deepseek/README.zh.md      |   2 +-
 packages/web/web/README.i18n.yaml                  |   4 +-
 packages/web/web/README.md                         |   2 +-
 packages/web/web/README.zh.md                      |   2 +-
 packages/web/web/src/index.ts                      |   2 +-
 packages/web/web/src/types.ts                      |   9 +-
 packages/workflow/tool-workflow/README.i18n.yaml   |   4 +-
 packages/workflow/tool-workflow/README.md          |   4 +-
 packages/workflow/tool-workflow/README.zh.md       |   4 +-
 packages/workflow/tool-workflow/src/index.ts       |   2 +-
 .../workflow/workflow-workerthread/src/meta.ts     |   4 +-
 .../workflow/workflow-workerthread/src/realm.ts    |  14 +-
 .../workflow/workflow-workerthread/src/runtime.ts  |   2 +-
 .../tests/workflow-workerthread.spec.ts            |  60 +-
 packages/workflow/workflow/src/index.ts            |   2 +-
 packages/workflow/workflow/src/types.ts            |   8 +-
 packages/workspace/workspace/src/index.ts          |   5 +
 976 files changed, 31193 insertions(+), 3063 deletions(-)
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
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（3c21611）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（3c21611）为新基线重新锚定/rebuild 补丁。
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
- 兼容：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁「无补丁」，当日 mainline 可干净集成。
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
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### telegram
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### tg-bot
- 兼容：锚定 fa3d357fc66102d82f0ddbf67fd3d5d70944d8f7（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### toybox
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### turtle-ui
- 兼容：锚定 a6fedc9e3b36d066e34860d040db6df47d88c432（未知（不同谱系））、补丁「不适用（空仓库）」，当日 mainline 可干净集成。
- 建议把补丁基线从 a6fedc9e3b36d066e34860d040db6df47d88c432 显式记录到 README/补丁头，快照一漂即可自动预警。
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
- 需适配：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（3c21611）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
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
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（3c21611）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（3c21611）为新基线重新锚定/rebuild 补丁。
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
- 兼容：锚定 8ec407cd64（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-nono
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-auto-chess
- 未建模/状态未知：尚无 research/dsh-auto-chess.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dshfind
- 未建模/状态未知：尚无 research/dshfind.md 调研摘要（或 git/gh 无法确认仓库状态），不做兼容性结论；建议先完成调研建模或人工核查后再纳入兼容跟踪。
### dsh-cyber-sec
- 兼容：锚定 20260809T140917Z（未知（非 commit 锚定: 20260809T140917Z））、补丁「无补丁」，当日 mainline 可干净集成。
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

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
