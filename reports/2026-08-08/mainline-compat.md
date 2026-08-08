# mainline 兼容性报告（2026-08-08）

- mainline：`0882344`（snapshots/20260808T121140Z）
- 上次对比：`e72bf03c5f10c76f3ba426e42237206423fc186e`
- 兼容性：123/134 无需适配，10 需适配（dsh-my-rsi dsh-subagent-tree dsh-working-activity ex-setting plugin-registry Qwen-MM-Plugins sandbox-mxc turtle-ui web-components fabric）；其中关注 3、占位 8、不适用 2、已删除 1

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
| dsh-cc-tui | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 关注 |
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
| dsh-my-rsi | 未知（不同谱系） | CONFLICT（3 个补丁中 1 个 OK） | 缺: tuiPrompt | 29 项匹配 | 需适配 |
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
| dsh-tool-encoding | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-tool-json | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-tool-time | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-ui-progress | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
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
| ex-setting | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 10 项匹配 | 需适配 |
| group-chat-diary | 未知（非 commit 锚定: YYYY-MM-DD） | 不适用 | 不适用 | 不适用 | 不适用 |
| hub | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| issues | 未知 | 不适用 | 不适用 | 不适用 | 不适用 |
| marisa | 未知（非 commit 锚定: snapshot-20260807T130646Z） | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 关注 |
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（4 个补丁中 0 个 OK） | 缺: tuiPrompt | 12 项匹配 | 需适配 |
| qqbot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| Qwen-MM-Plugins | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| Recall | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| review-panel | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-mxc | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| session-chatlog | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| session-persistence-rdb | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 已删除 |
| telegram | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| tg-bot | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 12 项匹配 | 兼容 |
| toybox | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| turtle-ui | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 21 项匹配 | 需适配 |
| web-components | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| dsh-web-ui-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-evolve | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-island | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-drag-and-drop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-message-edit | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-deep-research | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-multimedia-webui-input | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| repo-visibility-guard | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-grok-tui | 未知 | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| ds_web_craw | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| fabric | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 9 项匹配 | 需适配 |
| dsh-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-desktop-mac | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-public-repo-monitor | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-tui | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-inspect | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-hub | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-alphasolve | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| zotero-wave-rag | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| onboarding | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| ego-browser | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-nowledge-mem | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| dsh-sidechain | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| dsh-a2a | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 18 项匹配 | 兼容 |
| dsh-feishu-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-remote | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| mstar-workflow | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-scholar | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-issue-like-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-tool-csv | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-tool-regex | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-session-repair-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| DSH-better-sidebar | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-session-hub | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-ica | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-advisor | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-llm-fallbacks | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-web-workflow-visualizer | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| dsh-checkpoint | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| dsh-rewind | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| official-plugins-port | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| oh-my-dsh | 未知 | 无补丁 | 缺: tuiPrompt | 1427 项匹配 | 兼容 |
| dsh-side-panel | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-profile-bundle-example | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-plan-execute | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 13 项匹配 | 兼容 |
| dsh-paste-input | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| zotero-harvest | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-Modular-Yet-Graceful-Orchestrator | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| zephyr | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-bash-encoding | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-skill-stats | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-web-archive | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| sandbox-micro | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-git-identity | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-android | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-lazyfish | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-auto-approval | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| dsh-crew | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-input-history | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-client-ui-plan-execute | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| dsh-stickers | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| deep-standard-skill | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-serenity-plugin | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-toolkit | 未知 | 无补丁 | 缺: tuiPrompt | 10 项匹配 | 兼容 |
| dsh-tool-markdown | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-session-health | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |
| dsh-desktop-tools | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-reuse-first | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-plus | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-session-cluster | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |
| DSH-UI4A | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |

## mainline 变更分析（e72bf03c5f10c76f3ba426e42237206423fc186e → 0882344）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **包级变化**：packages/ 下删除 0 个包目录、新增 14 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：packages/examples/cli-demo

新增文件：
```
packages/api/README.md
packages/api/README.zh.md
packages/api/gateway/README.i18n.yaml
packages/api/gateway/README.md
packages/api/gateway/README.zh.md
packages/api/gateway/package.json
packages/api/gateway/src/client/index.ts
packages/api/gateway/src/index.ts
packages/api/gateway/src/invariant.ts
packages/api/gateway/src/types.ts
packages/api/gateway/tests/client.spec.ts
packages/api/gateway/tests/gateway.spec.ts
packages/api/gateway/tsconfig.json
packages/api/gateway/tsdown.config.ts
packages/api/remotes/README.i18n.yaml
```

### seam 符号变化

| 符号 | prev 文件数 | cur 文件数 | 变化 |
|---|---|---|---|
| `ThemeService` | 26 | 26 | 存在 → 存在（稳定） |
| `settingsNamespace` | 16 | 16 | 存在 → 存在（稳定） |
| `sessionProjections` | 21 | 21 | 存在 → 存在（稳定） |
| `tuiPrompt` | 0 | 0 | 缺失 → 缺失 |
| `slots` | 13 | 14 | 存在 → 存在（稳定） |
| `session/event` | 52 | 54 | 存在 → 存在（稳定） |

### diffstat（packages/ patches/ workspace）

```
 packages/AGENTS.md                                 |    2 +-
 packages/README.i18n.yaml                          |    4 +-
 packages/README.md                                 |    1 +
 packages/README.zh.md                              |    1 +
 .../{examples/cli-demo => api}/README.i18n.yaml    |    6 +-
 packages/api/README.md                             |   17 +
 packages/api/README.zh.md                          |   17 +
 packages/api/gateway/README.i18n.yaml              |    6 +
 packages/api/gateway/README.md                     |   39 +
 packages/api/gateway/README.zh.md                  |   39 +
 packages/api/gateway/package.json                  |   66 +
 packages/api/gateway/src/client/index.ts           |  498 ++++++++
 packages/api/gateway/src/index.ts                  |  638 ++++++++++
 packages/api/gateway/src/invariant.ts              |   30 +
 packages/api/gateway/src/types.ts                  |   54 +
 packages/api/gateway/tests/client.spec.ts          |  573 +++++++++
 packages/api/gateway/tests/gateway.spec.ts         | 1317 ++++++++++++++++++++
 packages/api/gateway/tsconfig.json                 |   27 +
 packages/api/gateway/tsdown.config.ts              |    3 +
 packages/api/remotes/README.i18n.yaml              |    6 +
 packages/api/remotes/README.md                     |   33 +
 packages/api/remotes/README.zh.md                  |   33 +
 packages/api/remotes/package.json                  |   64 +
 packages/api/remotes/src/agent-lookup.ts           |  194 +++
 packages/api/remotes/src/client/index.ts           |   27 +
 packages/api/remotes/src/index.ts                  |   18 +
 packages/api/remotes/src/invariant.ts              |   24 +
 packages/api/remotes/tests/agent-lookup.spec.ts    |  154 +++
 packages/api/remotes/tests/built-lib.e2e.ts        |  224 ++++
 packages/api/remotes/tsconfig.client.json          |   22 +
 packages/api/remotes/tsconfig.host.json            |   36 +
 packages/api/remotes/tsconfig.json                 |   11 +
 packages/api/remotes/tsdown.config.ts              |    7 +
 packages/bash/bash-sandbox/package.json            |    2 +-
 packages/bash/bash-sandbox/tests/landlock.e2e.ts   |    8 +-
 .../bash-sandbox/tests/partial-landlock.spec.ts    |    2 +-
 packages/bash/bash-sandbox/tsconfig.json           |    3 +
 packages/bundle/base/cordis.patch.yml              |   24 +-
 packages/bundle/base/package.json                  |    4 +
 .../bundle/base/tests/fixtures/root.cordis.yml     |    1 +
 packages/bundle/headless/README.i18n.yaml          |    4 +-
 packages/bundle/headless/README.md                 |    2 +-
 packages/bundle/headless/README.zh.md              |    2 +-
 packages/bundle/headless/src/index.ts              |   25 +-
 packages/bundle/headless/tests/headless.spec.ts    |   72 +-
 packages/bundle/web-app/cordis.patch.yml           |   12 +-
 packages/bundle/web-app/package.json               |    2 +
 packages/client/AGENTS.md                          |    2 +-
 packages/client/README.i18n.yaml                   |    4 +-
 packages/client/README.md                          |    1 +
 packages/client/README.zh.md                       |    1 +
 packages/client/connection/README.i18n.yaml        |    4 +-
 packages/client/connection/README.md               |    2 +-
 packages/client/connection/README.zh.md            |    2 +-
 .../client/connection/src/api-request-trust.ts     |    9 +-
 packages/client/connection/src/client/fixture.ts   |  301 +++--
 packages/client/connection/src/client/index.ts     |   10 +-
 .../client/connection/src/client/random-uuid.ts    |   14 +
 packages/client/connection/src/client/rpc.ts       |   63 +
 packages/client/connection/src/http-bridge.ts      |   12 +-
 packages/client/connection/src/index.ts            |   95 +-
 packages/client/connection/src/rpc-host.ts         |  224 ++++
 packages/client/connection/src/rpc.ts              |   77 ++
 .../client/connection/tests/client-apply.spec.ts   |  115 ++
 packages/client/connection/tests/fake-api.ts       |    1 +
 .../client/connection/tests/http-bridge.spec.ts    |    2 +-
 packages/client/connection/tests/node-half.spec.ts |  232 +++-
 packages/client/runtime/README.i18n.yaml           |    4 +-
 packages/client/runtime/README.md                  |    8 +-
 packages/client/runtime/README.zh.md               |    8 +-
 packages/client/runtime/package.json               |    7 +-
 packages/client/runtime/src/client/agents/scope.ts |   23 +-
 .../client/runtime/src/client/contract/sessions.ts |    5 +-
 packages/client/runtime/src/client/index.ts        |   35 +-
 .../src/client/session-history/history-fold.ts     |   92 +-
 .../src/client/sessions/context-provenance.ts      |    3 +
 .../runtime/src/client/sessions/conversation.ts    |   41 +-
 .../client/runtime/src/client/sessions/history.ts  |    6 +-
 .../client/runtime/src/client/sessions/service.ts  |    8 +-
 .../client/runtime/src/client/sessions/session.ts  |   87 +-
 .../src/client/sessions/subagent-lineage.ts        |   50 +
 .../runtime/src/client/sessions/tool-call-tree.ts  |  212 ++++
 .../src/client/sessions/transcript-adapter.ts      |   70 +-
 packages/client/runtime/src/client/slots.ts        |   15 +-
 .../client/runtime/src/client/workspaces/path.ts   |   13 +
 packages/client/runtime/tests/client-apply.spec.ts |    6 +
 .../runtime/tests/compact-checkpoint-pin.spec.ts   |    5 +-
 packages/client/runtime/tests/event-script.ts      |   15 +-
 packages/client/runtime/tests/fake-api.ts          |    1 +
 packages/client/runtime/tests/history-fold.spec.ts |   31 +
 packages/client/runtime/tests/session.spec.ts      |   81 +-
 .../client/runtime/tests/subagent-lineage.spec.ts  |   53 +
 .../client/runtime/tests/tool-call-tree.spec.ts    |   89 ++
 .../runtime/tests/transcript-adapter.spec.ts       |   56 +-
 packages/client/runtime/tests/wire-events.spec.ts  |    6 +
 packages/client/runtime/tsconfig.json              |    6 +
 packages/client/schema-form/tsdown.config.ts       |    6 +
 packages/client/test-runtime/src/fixtures.ts       |    1 -
 packages/client/test-runtime/src/sessions.ts       |    8 +-
 packages/client/test-runtime/tsdown.config.ts      |    6 +
 packages/client/tsdown.client.ts                   |  134 +-
 packages/client/ui-conversation/README.i18n.yaml   |    4 +-
 packages/client/ui-conversation/README.md          |   25 +-
 packages/client/ui-conversation/README.zh.md       |   25 +-
 packages/client/ui-conversation/package.json       |    2 +-
 .../client/ui-conversation/src/client/apply.ts     |   53 +-
 .../src/client/chat/AssistantMarkdown.tsx          |   34 +-
 .../src/client/chat/ChatView.module.css            |   11 -
 .../ui-conversation/src/client/chat/ChatView.tsx   |  175 +--
 .../src/client/chat/CompactionCommandCard.tsx      |   28 +
 .../src/client/chat/CompactionItem.tsx             |   37 +-
 .../src/client/chat/ContextBody.tsx                |    2 +-
 .../src/client/chat/ContextInjectionRow.tsx        |    3 +-
 .../src/client/chat/GenericCommandCard.module.css  |   86 ++
 .../src/client/chat/GenericCommandCard.tsx         |   60 +-
 .../src/client/chat/MessageItem.module.css         |   33 +-
 .../src/client/chat/MessageItem.tsx                |   20 +-
 .../src/client/chat/ReasoningRow.module.css        |   81 ++
 .../src/client/chat/ReasoningRow.tsx               |   65 +
 .../src/client/chat/accessibility.module.css       |    8 +
 .../ui-conversation/src/client/chat/chat-flow.ts   |   64 +-
 .../src/client/chat/use-throttled-visual-update.ts |    4 +-
 .../ui-conversation/src/client/contract/slots.ts   |   77 +-
 .../client/ui-conversation/src/client/index.ts     |    7 +-
 .../client/ui-conversation/src/client/locales.ts   |    8 +-
 .../src/client/skeleton/DetailsPanel.module.css    |   33 -
 .../src/client/skeleton/DetailsPanel.tsx           |  141 +--
 packages/client/ui-conversation/src/invariant.ts   |    2 +-
 .../tests/assembly-surfaces.spec.tsx               |  134 +-
 .../ui-conversation/tests/chat-apply.spec.tsx      |   24 +-
 .../tests/chat-branch-tails.spec.tsx               |   10 +-
 ...ts-bash-sample.spec.tsx => chat-stats.spec.tsx} |   59 +-
 .../ui-conversation/tests/chat-view.spec.tsx       |  284 +++--
 .../ui-conversation/tests/coverage-tails.spec.tsx  |   90 +-
 .../tests/gate-branch-tails.spec.tsx               |   60 +-
 .../ui-conversation/tests/input-bar.spec.tsx       |    2 +-
 .../ui-conversation/tests/input-matrix.spec.tsx    |    2 +-
 .../ui-conversation/tests/input-scenarios.spec.tsx |    2 +-
 .../ui-conversation/tests/queue-dock.spec.tsx      |    2 +-
 .../ui-conversation/tests/reasoning-row.spec.tsx   |  117 ++
 .../client/ui-conversation/tests/skeleton.spec.tsx |   12 +-
 .../ui-conversation/tests/todo-panel.spec.tsx      |  157 +--
 .../ui-conversation/tests/turn-metrics.spec.ts     |    2 +-
 .../tests/views-type-chain.spec.tsx                |   39 +-
 .../src/client/turn-deliverables.ts                |    2 +-
 .../ui-deliverables/tests/produced-files.spec.tsx  |    3 +-
 packages/client/ui-goal/README.i18n.yaml           |    4 +-
 packages/client/ui-goal/README.md                  |    4 +-
 packages/client/ui-goal/README.zh.md               |    4 +-
 packages/client/ui-goal/package.json               |    5 +-
 packages/client/ui-goal/src/client/index.ts        |   51 +-
 .../client/ui-goal/tests/browser-plugin.spec.tsx   |  109 +-
 packages/client/ui-goal/tsconfig.json              |    4 +-
 packages/client/ui-layout/README.i18n.yaml         |    4 +-
 packages/client/ui-layout/README.md                |    2 +-
 packages/client/ui-layout/README.zh.md             |    2 +-
 .../client/ui-layout/src/client/theme-presenter.ts |   26 +-
 packages/client/ui-layout/tests/apply.spec.ts      |   10 +-
 .../client/ui-layout/tests/theme-presenter.spec.ts |   36 +-
 packages/client/ui-models/README.i18n.yaml         |    4 +-
 packages/client/ui-models/README.md                |    6 +-
 packages/client/ui-models/README.zh.md             |    6 +-
 .../ui-models/src/client/CustomProviderCard.tsx    |    2 +-
 .../client/ui-models/src/client/ModelsSection.tsx  |   14 +-
 .../client/ui-models/src/client/ProviderEditor.tsx |   17 +-
 packages/client/ui-models/src/client/store.ts      |   17 -
 .../client/ui-models/tests/components.spec.tsx     |   31 +-
 .../ui-models/tests/onboarding-dialog.spec.tsx     |    6 +-
 packages/client/ui-models/tests/readiness.spec.ts  |    8 -
 packages/client/ui-models/tests/store.spec.ts      |   27 +-
 packages/client/ui-primitives/README.i18n.yaml     |    4 +-
 packages/client/ui-primitives/README.md            |    4 +-
 packages/client/ui-primitives/README.zh.md         |    4 +-
 .../src}/DisclosureRow.module.css                  |    2 +-
 .../chat => ui-primitives/src}/DisclosureRow.tsx   |   10 +-
 packages/client/ui-primitives/src/index.ts         |    2 +
 packages/client/ui-primitives/tsdown.config.ts     |    6 +-
 .../ui-settings-general/src/client/chrome.tsx      |    2 +-
 packages/client/ui-skill/README.i18n.yaml          |    4 +-
 packages/client/ui-skill/README.md                 |   19 +-
 packages/client/ui-skill/README.zh.md              |   19 +-
 packages/client/ui-skill/package.json              |    6 +-
 packages/client/ui-skill/src/client/SkillRow.tsx   |   12 +-
 packages/client/ui-skill/src/client/index.ts       |   46 +-
 packages/client/ui-skill/src/client/locales.ts     |    2 +
 .../client/ui-skill/tests/browser-plugin.spec.ts   |   58 +-
 packages/client/ui-skill/tests/skill-row.spec.tsx  |    3 +-
 packages/client/ui-skill/tsconfig.json             |    2 +-
 packages/client/ui-slots/tsdown.config.ts          |    6 +
 .../src/client/SubagentCatalogAction.tsx           |   51 +-
 .../ui-subagent/tests/conversation-ui.spec.tsx     |   11 +-
 packages/client/ui-theme/tsdown.config.ts          |   12 +-
 packages/client/ui-tool/README.i18n.yaml           |    6 +
 packages/client/ui-tool/README.md                  |   49 +
 packages/client/ui-tool/README.zh.md               |   49 +
 packages/client/ui-tool/package.json               |   73 ++
 packages/client/ui-tool/src/client/apply.ts        |   43 +
 .../client/ui-tool/src/client/contract/slots.ts    |   39 +
 packages/client/ui-tool/src/client/index.ts        |    3 +
 packages/client/ui-tool/src/client/locale.ts       |    2 +
 .../src/client/tool/ToolCallTree.module.css        |   12 +
 .../ui-tool/src/client/tool/ToolCallTree.tsx       |  104 ++
 .../ui-tool/src/client/tool/ToolDetails.module.css |   46 +
 .../client/ui-tool/src/client/tool/ToolDetails.tsx |   66 +
 .../src/client/tool/components}/ToolRow.module.css |   18 -
 .../src/client/tool/components}/ToolRow.tsx        |  109 +-
 .../src/client/tool/models}/diff-card-model.ts     |    0
 .../src/client/tool/models}/read-card-model.ts     |    2 +-
 .../src/client/tool/models}/search-card-model.ts   |    2 +-
 .../src/client/tool/models}/terminal-card-model.ts |    9 +-
 .../src/client/tool/models}/tool-call-model.ts     |   29 +-
 .../src/client/tool/models}/web-card-model.ts      |    0
 .../src/client/tool/toolviews}/GenericToolCard.tsx |   28 +-
 .../client/tool}/toolviews/ask-question-row.tsx    |   18 +-
 .../client/tool}/toolviews/bash-sample.module.css  |    0
 .../src/client/tool}/toolviews/bash-sample.tsx     |   16 +-
 .../client/tool}/toolviews/file-mutation-row.tsx   |   20 +-
 .../src/client/tool}/toolviews/plan-summary.ts     |    0
 .../src/client/tool}/toolviews/read-row.tsx        |   20 +-
 .../src/client/tool}/toolviews/search-row.tsx      |   22 +-
 .../src/client/tool}/toolviews/todo-row.tsx        |   20 +-
 .../src/client/tool}/toolviews/web-row.tsx         |   20 +-
 packages/client/ui-tool/src/css-modules.d.ts       |    4 +
 packages/client/ui-tool/src/index.ts               |    4 +
 packages/client/ui-tool/src/invariant.ts           |   30 +
 .../tests/ask-question-row.spec.tsx                |   12 +-
 .../ui-tool/tests/assembly-surfaces.spec.tsx       |  150 +++
 .../tests/chat-code-subcalls.spec.tsx              |   74 +-
 .../client/ui-tool/tests/coverage-tails.spec.tsx   |  116 ++
 .../tests/diff-card.spec.tsx                       |   21 +-
 .../tests/read-card.spec.tsx                       |   23 +-
 .../tests/search-card.spec.tsx                     |   25 +-
 .../tests/terminal-card.spec.tsx                   |   36 +-
 packages/client/ui-tool/tests/todo-row.spec.tsx    |  158 +++
 .../client/ui-tool/tests/tool-call-tree.spec.tsx   |   72 ++
 .../client/ui-tool/tests/tool-details-render.tsx   |   22 +
 .../tests/tool-row-styles.spec.ts                  |    4 +-
 .../tests/tool-row.spec.tsx}                       |  129 +-
 .../tests/toolview-slot.spec.tsx}                  |   41 +-
 .../ui-tool/tests/toolview-type-chain.spec.tsx     |   34 +
 .../tests/web-card.spec.tsx                        |   32 +-
 packages/client/ui-tool/tsconfig.json              |   33 +
 packages/client/ui-tool/tsdown.config.ts           |    3 +
 .../ui-trajectory/src/client/TrajectoryView.tsx    |    4 +-
 packages/client/ui-trajectory/src/client/layout.ts |   47 +-
 .../client/ui-trajectory/tests/layout.spec.tsx     |   64 +-
 packages/client/ui-trajectory/tests/views.spec.tsx |    5 +-
 packages/client/ui-workspace/README.i18n.yaml      |    4 +-
 packages/client/ui-workspace/README.md             |    2 +-
 packages/client/ui-workspace/README.zh.md          |    2 +-
 packages/client/ui-workspace/src/client/locales.ts |    4 +
 .../client/ui-workspace/src/client/rows/Rows.tsx   |   95 +-
 packages/client/ui-workspace/src/client/tree.ts    |   25 +-
 packages/client/ui-workspace/tests/rows.spec.tsx   |  102 +-
 packages/client/ui-workspace/tests/tree.spec.ts    |   28 +-
 packages/client/web-react/tsdown.config.ts         |    4 +-
 packages/client/web/tsdown.config.ts               |    6 +-
 packages/compact/command-compact/README.i18n.yaml  |    4 +-
 packages/compact/command-compact/README.md         |    2 +-
 packages/compact/command-compact/README.zh.md      |    2 +-
 packages/compact/command-compact/src/index.ts      |    1 +
 .../command-compact/tests/command-compact.spec.ts  |   31 +-
 .../tests/loader-composition.spec.ts               |   35 +-
 packages/compact/compact-basic/README.i18n.yaml    |    4 +-
 packages/compact/compact-basic/README.md           |    2 +-
 packages/compact/compact-basic/README.zh.md        |    2 +-
 packages/compact/compact-basic/src/region.ts       |    8 +-
 packages/compact/compact-basic/src/summarizer.ts   |   20 +-
 .../compact-basic/tests/compact-basic.spec.ts      |   16 +-
 packages/compact/compact/src/types.ts              |   17 +-
 .../context/workspace-context/README.i18n.yaml     |    4 +-
 packages/context/workspace-context/README.md       |    6 +-
 packages/context/workspace-context/README.zh.md    |    6 +-
 packages/context/workspace-context/src/index.ts    |   68 +-
 .../tests/workspace-context.spec.ts                |  106 +-
 packages/cordis/tool-cordis/README.i18n.yaml       |    4 +-
 packages/cordis/tool-cordis/README.md              |    2 +-
 packages/cordis/tool-cordis/README.zh.md           |    2 +-
 packages/cordis/tool-cordis/src/api-catalog.ts     |   68 +-
 packages/cordis/tool-cordis/src/guard.ts           |    1 -
 packages/core/agent/package.json                   |    8 +
 packages/core/agent/src/index.ts                   |   25 +
 packages/core/agent/tests/agent.spec.ts            |   26 +
 packages/core/agent/tsconfig.json                  |    3 +
 packages/core/session/package.json                 |    3 +
 packages/core/session/src/index.ts                 |   16 +
 packages/core/session/tests/request-header.spec.ts |    2 +-
 packages/core/session/tests/typert.spec.ts         |   26 +
 packages/core/session/tsconfig.json                |    3 +
 packages/core/tools/tests/json-schema.spec.ts      |    2 +-
 .../credentials/credentials-local/README.i18n.yaml |    4 +-
 packages/credentials/credentials-local/README.md   |   41 +-
 .../credentials/credentials-local/README.zh.md     |   41 +-
 .../credentials/credentials-local/package.json     |    6 +-
 .../credentials/credentials-local/src/index.ts     |  358 +++---
 .../credentials-local/tests/drain.spec.ts          |    2 +-
 .../credentials-local/tests/local.spec.ts          |  298 ++++-
 .../credentials-local/tests/review-fixes.spec.ts   |  106 +-
 .../credentials-local/tests/watcher.spec.ts        |   60 +-
 .../credentials/credentials-local/tsconfig.json    |    3 +
 packages/credentials/credentials/README.i18n.yaml  |    4 +-
 packages/credentials/credentials/README.md         |    2 +-
 packages/credentials/credentials/README.zh.md      |    2 +-
 packages/credentials/credentials/src/index.ts      |    2 +-
 packages/examples/README.i18n.yaml                 |    4 +-
 packages/examples/README.md                        |    3 +-
 packages/examples/README.zh.md                     |    3 +-
 packages/examples/acp-demo/tests/load-path.e2e.ts  |    2 -
 packages/examples/agent-spine-demo/package.json    |    2 +-
 .../agent-spine-demo/tests/agent-core.spec.ts      |    1 +
 .../tests/multi-project-sandbox.e2e.ts             |    2 +-
 packages/examples/agent-spine-demo/tsconfig.json   |    3 +
 packages/examples/cli-demo/README.md               |   78 --
 packages/examples/cli-demo/README.zh.md            |   78 --
 packages/examples/cli-demo/package.json            |   68 -
 packages/examples/cli-demo/src/bin.ts              |   34 -
 packages/examples/cli-demo/src/cli.ts              |  406 ------
 packages/examples/cli-demo/src/index.ts            |   96 --
 packages/examples/cli-demo/tests/built-bin.e2e.ts  |  221 ----
 packages/examples/cli-demo/tests/cli-demo.spec.ts  |  202 ---
 packages/examples/cli-demo/tests/cli.spec.ts       |  614 ---------
 packages/examples/cli-demo/tsconfig.json           |   47 -
 packages/examples/cli-demo/tsdown.config.ts        |   13 -
 packages/goal/goal/package.json                    |   18 +-
 packages/goal/goal/src/domain.ts                   |   29 +-
 packages/goal/goal/src/index.ts                    |   31 +-
 packages/goal/goal/src/types.ts                    |   32 +
 packages/goal/goal/tests/goal.e2e.ts               |    7 +-
 packages/goal/goal/tests/goal.spec.ts              |   16 +
 packages/goal/goal/tsconfig.json                   |    3 +
 packages/hooks/hooks-claude/tests/bridge.spec.ts   |    4 +-
 packages/host/apiproxy/README.i18n.yaml            |    4 +-
 packages/host/apiproxy/README.md                   |    4 +-
 packages/host/apiproxy/README.zh.md                |    4 +-
 packages/host/apiproxy/package.json                |    3 +
 packages/host/apiproxy/src/api-proxy.ts            |  196 +--
 packages/host/apiproxy/src/api/index.ts            |    5 +
 packages/host/apiproxy/src/api/skills.schema.ts    |    1 +
 packages/host/apiproxy/src/api/skills.ts           |   14 +-
 .../host/apiproxy/tests/api-proxy-cold.spec.ts     |   96 ++
 .../host/apiproxy/tests/api-proxy-commands.spec.ts |    5 +-
 .../host/apiproxy/tests/api-proxy-question.spec.ts |   14 +-
 packages/host/apiproxy/tests/fetch-carrier.spec.ts |    4 +-
 packages/host/apiproxy/tests/rpc-schemas.spec.ts   |    9 +-
 packages/host/apiproxy/tsconfig.json               |    3 +
 .../host/directory-picker-native/tsdown.config.ts  |   29 +-
 packages/host/frontend-static/README.i18n.yaml     |    4 +-
 packages/host/frontend-static/README.md            |    2 +-
 packages/host/frontend-static/README.zh.md         |    2 +-
 packages/host/frontend-static/src/index.ts         |    1 +
 .../frontend-static/tests/frontend-static.spec.ts  |    8 +-
 packages/llm/llm-deepseek/README.i18n.yaml         |    4 +-
 packages/llm/llm-deepseek/README.md                |    4 +-
 packages/llm/llm-deepseek/README.zh.md             |    4 +-
 packages/llm/llm-deepseek/package.json             |    2 +
 packages/llm/llm-deepseek/src/adapter.ts           |    9 +-
 packages/llm/llm-deepseek/src/index.ts             |   61 +-
 packages/llm/llm-deepseek/tests/adapter.e2e.ts     |    6 +-
 packages/llm/llm-deepseek/tests/adapter.spec.ts    |   96 +-
 .../llm/llm-deepseek/tests/dynamic-config.spec.ts  |   35 +-
 .../llm-deepseek/tests/loader-composition.spec.ts  |   27 +-
 packages/llm/llm-deepseek/tsconfig.json            |    3 +
 packages/llm/llm-pi-ai/README.i18n.yaml            |    4 +-
 packages/llm/llm-pi-ai/README.md                   |   51 +-
 packages/llm/llm-pi-ai/README.zh.md                |   51 +-
 packages/llm/llm-pi-ai/package.json                |    2 +
 packages/llm/llm-pi-ai/src/catalog.ts              |  282 ++++-
 packages/llm/llm-pi-ai/src/config.ts               |   96 +-
 packages/llm/llm-pi-ai/src/index.ts                |   30 +-
 packages/llm/llm-pi-ai/src/provider.ts             |    9 +-
 packages/llm/llm-pi-ai/tests/adapter.spec.ts       |  220 +++-
 packages/llm/llm-pi-ai/tests/catalog.spec.ts       |  289 ++++-
 packages/llm/llm-pi-ai/tests/config.spec.ts        |   38 +-
 .../llm/llm-pi-ai/tests/dynamic-config.spec.ts     |   30 +-
 .../llm/llm-pi-ai/tests/loader-composition.spec.ts |    6 +-
 packages/llm/llm-pi-ai/tests/sdk-options.spec.ts   |    1 -
 packages/llm/llm-pi-ai/tsconfig.json               |    3 +
 packages/llm/llm-retry/README.i18n.yaml            |    4 +-
 packages/llm/llm-retry/README.md                   |    2 +-
 packages/llm/llm-retry/README.zh.md                |    2 +-
 .../llm/llm-retry/tests/transport-recovery.spec.ts |    4 +-
 packages/llm/llm/README.i18n.yaml                  |    4 +-
 packages/llm/llm/README.md                         |    2 +-
 packages/llm/llm/README.zh.md                      |    2 +-
 packages/llm/llm/src/attribution.ts                |    3 +-
 packages/llm/llm/src/call-config.ts                |    2 +
 packages/plan/plan-mode/README.i18n.yaml           |    4 +-
 packages/plan/plan-mode/README.md                  |    1 +
 packages/plan/plan-mode/README.zh.md               |    1 +
 packages/plan/plan-mode/tests/plan-mode.spec.ts    |   42 +-
 packages/sandbox/sandbox-local/README.i18n.yaml    |    4 +-
 packages/sandbox/sandbox-local/README.md           |    2 +-
 packages/sandbox/sandbox-local/README.zh.md        |    2 +-
 packages/sandbox/sandbox-local/package.json        |    2 +-
 packages/sandbox/sandbox-local/src/index.ts        |    2 +-
 packages/sandbox/sandbox-local/src/profiles.ts     |    2 +-
 .../sandbox/sandbox-local/tests/landlock.e2e.ts    |    4 +-
 packages/sandbox/sandbox-local/tests/local.spec.ts |    2 +-
 .../sandbox-local/tests/packed-install.e2e.ts      |   44 +-
 packages/sandbox/sandbox-local/tsconfig.json       |    3 +
 packages/sdk/create-sdk/tests/create.spec.ts       |    2 +-
 .../sdk/helper/src/features/builtin/provider.ts    |    9 +-
 packages/sdk/helper/tests/documents.spec.ts        |   12 +-
 packages/sdk/helper/tests/project.spec.ts          |    3 +-
 packages/sdk/scripts/tests/scripts.spec.ts         |    2 +-
 packages/sdk/telemetry/README.i18n.yaml            |    4 +-
 packages/sdk/telemetry/README.md                   |    2 +-
 packages/sdk/telemetry/README.zh.md                |    2 +-
 packages/sdk/telemetry/src/reporter.ts             |    9 +-
 .../sdk/telemetry/tests/consent-resolver.spec.ts   |    3 +-
 .../session-checkpoint-policy/README.i18n.yaml     |    4 +-
 .../session-checkpoint-policy/README.md            |    4 +-
 .../session-checkpoint-policy/README.zh.md         |    4 +-
 .../session-persistence-jsonl/README.i18n.yaml     |    4 +-
 .../session-persistence-jsonl/README.md            |    3 +-
 .../session-persistence-jsonl/README.zh.md         |    3 +-
 .../session-persistence-jsonl/src/index.ts         |   10 +-
 .../session-persistence-jsonl/tests/jsonl.spec.ts  |    1 +
 .../session-persistence-sqlite/README.i18n.yaml    |    4 +-
 .../session-persistence-sqlite/README.md           |    3 +-
 .../session-persistence-sqlite/README.zh.md        |    3 +-
 .../session-persistence-sqlite/src/index.ts        |   10 +-
 .../tests/sqlite.spec.ts                           |    1 +
 .../session-persistence/README.i18n.yaml           |    4 +-
 .../session-persistence/README.md                  |    4 +-
 .../session-persistence/README.zh.md               |    4 +-
 .../session-persistence/package.json               |    2 +
 .../session-persistence/src/coordinator.ts         |   95 +-
 .../session-persistence/src/index.ts               |    2 +
 .../session-persistence/src/write-behind.ts        |  159 +++
 .../session-persistence/tests/persistence.spec.ts  |  120 +-
 .../session-persistence/tests/write-behind.spec.ts |  275 ++++
 packages/settings/settings-local/src/index.ts      |    9 +-
 packages/skill/README.i18n.yaml                    |    4 +-
 packages/skill/README.md                           |    1 +
 packages/skill/README.zh.md                        |    1 +
 packages/skill/skill-badge/README.i18n.yaml        |    6 +
 packages/skill/skill-badge/README.md               |   22 +
 packages/skill/skill-badge/README.zh.md            |   22 +
 packages/skill/skill-badge/assets/dsh-badge.md     |   31 +
 packages/skill/skill-badge/assets/dsh-badge.png    |  Bin 0 -> 12339 bytes
 packages/skill/skill-badge/package.json            |   37 +
 packages/skill/skill-badge/src/index.ts            |   60 +
 packages/skill/skill-badge/src/invariant.ts        |   30 +
 .../skill/skill-badge/tests/skill-badge.spec.ts    |   40 +
 packages/skill/skill-badge/tsconfig.json           |   14 +
 packages/skill/skill-local/src/index.ts            |    4 +-
 packages/skill/skill/README.i18n.yaml              |    4 +-
 packages/skill/skill/README.md                     |    4 +
 packages/skill/skill/README.zh.md                  |    4 +
 packages/skill/skill/package.json                  |    2 +
 packages/skill/skill/src/index.ts                  |   95 ++
 packages/skill/skill/tests/skill.spec.ts           |   63 +
 packages/skill/skill/tsconfig.json                 |    3 +
 packages/skill/tool-skill/README.i18n.yaml         |    4 +-
 packages/skill/tool-skill/README.md                |   17 +-
 packages/skill/tool-skill/README.zh.md             |   17 +-
 packages/skill/tool-skill/src/index.ts             |  132 +-
 packages/skill/tool-skill/tests/tool-skill.spec.ts |  132 ++
 .../subagent-codex/tests/responses-fixture.ts      |    2 +-
 packages/support/acp-snapshot/README.i18n.yaml     |    4 +-
 packages/support/acp-snapshot/README.md            |    6 +-
 packages/support/acp-snapshot/README.zh.md         |    6 +-
 packages/support/acp-snapshot/package.json         |    2 +
 packages/support/acp-snapshot/src/index.ts         |    1 +
 packages/support/acp-snapshot/src/suite.ts         |  205 ++-
 .../fixtures/record-suite/rec-child/behavior.json  |    6 +-
 .../record-suite/rec-child/session.1.jsonl         |    1 +
 .../fixtures/record-suite/rec-child/session.jsonl  |    1 +
 packages/support/acp-snapshot/tests/suite.spec.ts  |  246 +++-
 packages/support/acp-snapshot/tsconfig.json        |    3 +
 packages/support/llm-replay/README.i18n.yaml       |    4 +-
 packages/support/llm-replay/README.md              |   10 +-
 packages/support/llm-replay/README.zh.md           |   10 +-
 packages/support/llm-replay/package.json           |    2 +
 packages/support/llm-replay/src/index.ts           |   52 +-
 .../support/llm-replay/tests/llm-replay.spec.ts    |  153 +++
 packages/support/llm-replay/tsconfig.json          |    3 +
 packages/support/loader-smoke/README.i18n.yaml     |    4 +-
 packages/support/loader-smoke/README.md            |    6 +-
 packages/support/loader-smoke/README.zh.md         |    6 +-
 packages/support/loader-smoke/package.json         |    8 +-
 packages/support/loader-smoke/src/agent-turn.ts    |  100 ++
 packages/support/loader-smoke/src/index.ts         |    6 +
 .../support/loader-smoke/tests/agent-turn.spec.ts  |  160 +++
 .../loader-smoke/tests/example-launch.spec.ts      |    6 +-
 packages/support/loader-smoke/tsconfig.json        |    9 +
 packages/typert/generator/README.i18n.yaml         |    4 +-
 packages/typert/generator/README.md                |    4 +-
 packages/typert/generator/README.zh.md             |    4 +-
 packages/typert/generator/package.json             |    1 +
 packages/typert/generator/src/analyzer.ts          | 1049 +++++++++++++++-
 packages/typert/generator/src/cordis-catalog.ts    |    2 +-
 packages/typert/generator/src/emitter.ts           |  546 +++++++-
 packages/typert/generator/src/model.ts             |   58 +
 packages/typert/generator/src/renderer.ts          |  101 +-
 packages/typert/generator/src/tsdown-plugin.ts     |  121 +-
 packages/typert/generator/src/workspace.ts         |   51 +-
 .../tests/__snapshots__/type-model.spec.ts.snap    |    5 +
 .../tests/fixtures/remote-model/package.json       |    5 +
 .../remote-model/packages/domain/package.json      |    9 +
 .../remote-model/packages/domain/src/index.ts      |   19 +
 .../remote-model/packages/domain/src/types.ts      |    2 +
 .../remote-model/packages/domain/tsconfig.json     |   11 +
 .../remote-model/packages/remote/package.json      |   24 +
 .../remote-model/packages/remote/src/index.ts      |   33 +
 .../remote-model/packages/remote/src/types.ts      |   20 +
 .../remote-model/packages/remote/tsconfig.json     |   14 +
 .../tests/fixtures/remote-model/tsconfig.base.json |   20 +
 .../tests/fixtures/remote-model/tsconfig.host.json |    8 +
 .../tests/fixtures/remote-model/type-meta.d.ts     |   64 +
 .../typert/generator/tests/remote-model.spec.ts    |  705 +++++++++++
 .../typert/generator/tests/schema-emitter.spec.ts  |  232 +++-
 .../typert/generator/tests/tools-catalog.spec.ts   |    2 +-
 .../typert/generator/tests/tsdown-plugin.spec.ts   |  121 +-
 packages/typert/generator/tests/type-model.spec.ts |  180 +++
 packages/typert/loader/src/index.ts                |   95 +-
 packages/typert/loader/tests/loader.spec.ts        |  231 +++-
 packages/typert/registry/README.i18n.yaml          |    4 +-
 packages/typert/registry/README.md                 |    2 +
 packages/typert/registry/README.zh.md              |    2 +
 packages/typert/registry/package.json              |   15 +
 packages/typert/registry/src/client/index.ts       |   15 +
 packages/typert/registry/src/index.ts              |  220 +---
 packages/typert/registry/src/service.ts            |  718 +++++++++++
 packages/typert/registry/src/types.ts              |    3 +
 packages/typert/registry/tests/typert.spec.ts      |  428 ++++++-
 packages/typert/registry/tsconfig.json             |    3 +
 packages/typert/registry/tsdown.config.ts          |   26 +-
 packages/typert/type-meta/README.i18n.yaml         |    6 +
 packages/typert/type-meta/README.md                |   36 +
 packages/typert/type-meta/README.zh.md             |   36 +
 packages/typert/type-meta/package.json             |   40 +
 packages/typert/type-meta/src/index.ts             |  275 ++++
 .../cli-demo => typert/type-meta}/src/invariant.ts |   12 +-
 packages/typert/type-meta/src/types.ts             |  428 +++++++
 .../type-meta/tests/fixtures/source-launch.ts      |   32 +
 packages/typert/type-meta/tests/type-meta.spec.ts  |  230 ++++
 packages/typert/type-meta/tsconfig.json            |   21 +
 packages/ui/app-boot/README.i18n.yaml              |    4 +-
 packages/ui/app-boot/README.md                     |    7 +-
 packages/ui/app-boot/README.zh.md                  |    7 +-
 packages/ui/app-boot/package.json                  |    2 +
 packages/ui/app-boot/src/index.ts                  |  113 +-
 packages/ui/app-boot/src/profile.ts                |    2 +-
 packages/ui/app-boot/tests/app-boot.spec.ts        |  186 ++-
 packages/ui/app-boot/tests/config-dump.spec.ts     |   12 +-
 packages/ui/app-boot/tsconfig.json                 |    3 +
 packages/ui/commands/README.i18n.yaml              |    4 +-
 packages/ui/commands/README.md                     |    4 +-
 packages/ui/commands/README.zh.md                  |    4 +-
 packages/ui/commands/src/index.ts                  |   32 +-
 packages/ui/commands/src/invariant.ts              |   10 +
 packages/ui/commands/tests/commands.spec.ts        |   22 +
 packages/ui/commands/tests/invariant.spec.ts       |   89 ++
 packages/ui/tool-ask-user/README.i18n.yaml         |    4 +-
 packages/ui/tool-ask-user/README.md                |    1 +
 packages/ui/tool-ask-user/README.zh.md             |    1 +
 .../ui/tool-ask-user/tests/tool-ask-user.spec.ts   |   49 +-
 packages/ui/user-interaction/README.i18n.yaml      |    4 +-
 packages/ui/user-interaction/README.md             |    8 +-
 packages/ui/user-interaction/README.zh.md          |    8 +-
 packages/ui/user-interaction/src/index.ts          |   26 +-
 .../tests/user-interaction.spec.ts                 |   77 ++
 packages/util/environment/README.i18n.yaml         |    6 +
 packages/util/environment/README.md                |   36 +
 packages/util/environment/README.zh.md             |   36 +
 packages/util/environment/package.json             |   35 +
 packages/util/environment/src/index.ts             |  124 ++
 packages/util/environment/src/invariant.ts         |   30 +
 .../util/environment/tests/environment.spec.ts     |   69 +
 packages/util/environment/tsconfig.json            |   15 +
 packages/web/tool-web/README.i18n.yaml             |    4 +-
 packages/web/tool-web/README.md                    |    2 +-
 packages/web/tool-web/README.zh.md                 |    2 +-
 packages/web/web-search-deepseek/README.i18n.yaml  |    4 +-
 packages/web/web-search-deepseek/README.md         |    4 +-
 packages/web/web-search-deepseek/README.zh.md      |    4 +-
 packages/web/web-search-deepseek/package.json      |    2 +
 packages/web/web-search-deepseek/src/index.ts      |   18 +-
 .../web/web-search-deepseek/tests/deepseek.spec.ts |    2 +-
 packages/web/web-search-deepseek/tsconfig.json     |    3 +
 packages/web/web-search-exa/package.json           |    2 +
 packages/web/web-search-exa/src/index.ts           |    5 +-
 packages/web/web-search-exa/tsconfig.json          |    3 +
 packages/web/web-search-perplexity/package.json    |    2 +
 packages/web/web-search-perplexity/src/index.ts    |    5 +-
 packages/web/web-search-perplexity/tsconfig.json   |    3 +
 pnpm-workspace.yaml                                |   11 +-
 589 files changed, 21215 insertions(+), 5842 deletions(-)
```

## 破坏性变更清单

- 本日快照未发现 seam 符号级破坏。
- 删除的包目录：packages/examples/cli-demo。

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
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 7 项匹配），建议确认所依赖的宿主面当日是否仍满足。
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
- 需适配：锚定 17fdde293847c502f14814f38f6e698b565b69c8（未知（不同谱系））、补丁状态「CONFLICT（3 个补丁中 1 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
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
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dshx-update-check
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ex-setting
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### group-chat-diary
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### hub
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### issues
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### marisa
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 2 项匹配），建议确认所依赖的宿主面当日是否仍满足。
### plugin-registry
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（4 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### qqbot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### Qwen-MM-Plugins
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### Recall
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### review-panel
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-mxc
- 需适配：锚定 93fe8cc2（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
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
- 需适配：锚定 a6fedc9e3b36d066e34860d040db6df47d88c432（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### web-components
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-web-ui-notify
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-evolve
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-island
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-drag-and-drop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-message-edit
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-deep-research
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-multimedia-webui-input
- 兼容：锚定 279244acb0（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### repo-visibility-guard
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-grok-tui
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ds_web_craw
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### fabric
- 需适配：锚定 4d3e1305d7f96c9b8e5842c71eab65b0ee7d36f5（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（0882344）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-browser
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-desktop-mac
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-public-repo-monitor
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tui
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-inspect
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-hub
- 兼容：锚定 e8a0f1a758（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-alphasolve
- 兼容：锚定 279244acb0（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### zotero-wave-rag
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### onboarding
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ego-browser
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-nowledge-mem
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-sidechain
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-a2a
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-feishu-notify
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-remote
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### mstar-workflow
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-scholar
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-issue-like-skill
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-csv
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-regex
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-session-repair-skill
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### DSH-better-sidebar
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-session-hub
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-ica
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-advisor
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-llm-fallbacks
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-web-workflow-visualizer
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-checkpoint
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-rewind
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### official-plugins-port
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### oh-my-dsh
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-side-panel
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-profile-bundle-example
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-plan-execute
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-paste-input
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### zotero-harvest
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-Modular-Yet-Graceful-Orchestrator
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### zephyr
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-bash-encoding
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-skill-stats
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-web-archive
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-micro
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-git-identity
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-android
- 兼容：锚定 e56256082c（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-lazyfish
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-auto-approval
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-crew
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-input-history
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-client-ui-plan-execute
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-stickers
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### deep-standard-skill
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-serenity-plugin
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-toolkit
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-markdown
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-session-health
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-desktop-tools
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-reuse-first
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-plus
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-session-cluster
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### DSH-UI4A
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
