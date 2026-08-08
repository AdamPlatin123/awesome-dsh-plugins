# mainline 兼容性报告（2026-08-08）

- mainline：`e72bf03`（snapshots/20260807T130646Z）
- 上次对比：`9d84ab42354a70058a66a826c4473e55925052b6`
- 兼容性：106/116 无需适配，9 需适配（dsh-my-rsi dsh-subagent-tree dsh-working-activity ex-setting plugin-registry Qwen-MM-Plugins sandbox-mxc turtle-ui web-components）；其中关注 3、占位 8、不适用 2、已删除 1

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
| dsh-my-rsi | 未知（不同谱系） | CONFLICT（3 个补丁中 1 个 OK） | 缺: tuiPrompt | 26 项匹配 | 需适配 |
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
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（3 个补丁中 0 个 OK） | 缺: tuiPrompt | 12 项匹配 | 需适配 |
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
| fabric | 未知（不同谱系） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 9 项匹配 | 兼容 |
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
| oh-my-dsh | 未知 | 无补丁 | 缺: tuiPrompt | 1306 项匹配 | 兼容 |
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

## mainline 变更分析（9d84ab42354a70058a66a826c4473e55925052b6 → e72bf03）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **包级变化**：packages/ 下删除 0 个包目录、新增 14 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：

新增文件：
```
packages/client/ui-conversation/src/client/input/blocks.ts
packages/client/ui-conversation/src/client/toolviews/plan-summary.ts
packages/client/ui-conversation/tests/tool-row-styles.spec.ts
packages/client/ui-deliverables/README.i18n.yaml
packages/client/ui-deliverables/README.md
packages/client/ui-deliverables/README.zh.md
packages/client/ui-deliverables/package.json
packages/client/ui-deliverables/src/client/ProducedFiles.module.css
packages/client/ui-deliverables/src/client/ProducedFiles.tsx
packages/client/ui-deliverables/src/client/index.ts
packages/client/ui-deliverables/src/client/locales.ts
packages/client/ui-deliverables/src/client/turn-deliverables.ts
packages/client/ui-deliverables/src/css-modules.d.ts
packages/client/ui-deliverables/src/index.ts
packages/client/ui-deliverables/src/invariant.ts
```

### seam 符号变化

| 符号 | prev 文件数 | cur 文件数 | 变化 |
|---|---|---|---|
| `ThemeService` | 26 | 26 | 存在 → 存在（稳定） |
| `settingsNamespace` | 16 | 16 | 存在 → 存在（稳定） |
| `sessionProjections` | 21 | 21 | 存在 → 存在（稳定） |
| `tuiPrompt` | 0 | 0 | 缺失 → 缺失 |
| `slots` | 13 | 13 | 存在 → 存在（稳定） |
| `session/event` | 52 | 52 | 存在 → 存在（稳定） |

### diffstat（packages/ patches/ workspace）

```
 packages/README.i18n.yaml                          |    4 +-
 packages/README.md                                 |    7 +-
 packages/README.zh.md                              |    7 +-
 packages/bundle/base/cordis.patch.yml              |   11 +
 packages/bundle/base/package.json                  |    2 +
 packages/bundle/web-app/README.i18n.yaml           |    4 +-
 packages/bundle/web-app/README.md                  |    2 +-
 packages/bundle/web-app/README.zh.md               |    2 +-
 packages/bundle/web-app/cordis.patch.yml           |    8 +-
 packages/bundle/web-app/package.json               |    2 +-
 packages/client/connection/src/client/fixture.ts   |   34 +-
 packages/client/connection/tests/fake-api.ts       |    1 +
 packages/client/connection/tests/fixture.spec.ts   |    4 +
 .../runtime/src/client/sessions/conversation.ts    |    5 +-
 .../src/client/sessions/transcript-adapter.ts      |    4 +-
 packages/client/runtime/tests/event-script.ts      |    2 +
 packages/client/runtime/tests/fake-api.ts          |    1 +
 .../runtime/tests/transcript-adapter.spec.ts       |    8 +
 packages/client/ui-conversation/README.i18n.yaml   |    4 +-
 packages/client/ui-conversation/README.md          |   14 +-
 packages/client/ui-conversation/README.zh.md       |   14 +-
 .../client/ui-conversation/src/client/apply.ts     |   17 +-
 .../src/client/chat/AssistantMarkdown.tsx          |   25 +-
 .../ui-conversation/src/client/chat/ChatView.tsx   |   63 +-
 .../src/client/chat/MessageIconActions.tsx         |    8 +-
 .../src/client/chat/MessageItem.tsx                |   17 +-
 .../src/client/chat/ToolRow.module.css             |   24 +-
 .../ui-conversation/src/client/chat/ToolRow.tsx    |   26 +-
 .../ui-conversation/src/client/chat/chat-flow.ts   |   40 +-
 .../ui-conversation/src/client/contract/slots.ts   |   47 +-
 .../client/ui-conversation/src/client/index.ts     |    2 +-
 .../ui-conversation/src/client/input/blocks.ts     |   77 ++
 .../client/ui-conversation/src/client/service.ts   |   16 +-
 .../client/skeleton/ConversationRoot.module.css    |    8 +
 .../src/client/skeleton/ConversationRoot.tsx       |   16 +-
 .../src/client/skeleton/HeroShell.module.css       |   22 +-
 .../src/client/skeleton/InputBar.tsx               |   12 +-
 .../src/client/toolviews/bash-sample.tsx           |    6 +-
 .../src/client/toolviews/plan-summary.ts           |   60 +
 .../src/client/toolviews/todo-row.tsx              |   42 +-
 .../tests/chat-branch-tails.spec.tsx               |   64 +-
 .../ui-conversation/tests/chat-tool-row.spec.tsx   |   14 +
 .../ui-conversation/tests/chat-view.spec.tsx       |  109 +-
 .../ui-conversation/tests/context-meter.spec.tsx   |    2 +-
 .../tests/service-orchestration.spec.ts            |    3 +
 .../client/ui-conversation/tests/skeleton.spec.tsx |   49 +-
 .../ui-conversation/tests/todo-panel.spec.tsx      |   87 +-
 .../ui-conversation/tests/tool-row-styles.spec.ts  |   45 +
 packages/client/ui-deliverables/README.i18n.yaml   |    6 +
 packages/client/ui-deliverables/README.md          |   21 +
 packages/client/ui-deliverables/README.zh.md       |   21 +
 packages/client/ui-deliverables/package.json       |   65 ++
 .../src/client/ProducedFiles.module.css            |   44 +
 .../ui-deliverables/src/client/ProducedFiles.tsx   |   54 +
 .../client/ui-deliverables/src/client/index.ts     |   42 +
 .../client/ui-deliverables/src/client/locales.ts   |   21 +
 .../src/client/turn-deliverables.ts                |   90 ++
 .../client/ui-deliverables/src/css-modules.d.ts    |    6 +
 packages/client/ui-deliverables/src/index.ts       |    9 +
 packages/client/ui-deliverables/src/invariant.ts   |   32 +
 .../ui-deliverables/tests/produced-files.spec.tsx  |  178 +++
 packages/client/ui-deliverables/tsconfig.json      |   30 +
 packages/client/ui-deliverables/tsdown.config.ts   |    3 +
 packages/client/ui-model/README.i18n.yaml          |    4 +-
 packages/client/ui-model/README.md                 |    2 +
 packages/client/ui-model/README.zh.md              |    2 +
 packages/client/ui-model/src/client/directory.ts   |   23 +-
 packages/client/ui-model/src/client/index.ts       |    6 +-
 packages/client/ui-model/src/client/locales.ts     |    2 +
 packages/client/ui-model/src/client/service.ts     |   28 +-
 .../client/ui-model/tests/browser-plugin.spec.ts   |   73 +-
 .../client/ui-model/tests/model-select.spec.tsx    |    1 +
 packages/client/ui-models/README.i18n.yaml         |    4 +-
 packages/client/ui-models/README.md                |    8 +-
 packages/client/ui-models/README.zh.md             |    8 +-
 .../ui-models/src/client/CustomProviderCard.tsx    |  120 +-
 .../ui-models/src/client/ModelListEditor.tsx       |   13 +-
 .../ui-models/src/client/ModelsSection.module.css  |   45 +
 .../client/ui-models/src/client/ModelsSection.tsx  |  227 +++-
 .../client/ui-models/src/client/ProviderEditor.tsx |  110 +-
 packages/client/ui-models/src/client/apiKey.ts     |   58 +
 packages/client/ui-models/src/client/locales.ts    |   50 +-
 packages/client/ui-models/src/client/store.ts      |   12 -
 packages/client/ui-models/tests/apply.spec.ts      |    6 +-
 .../client/ui-models/tests/components.spec.tsx     |  294 ++++-
 .../client/ui-models/tests/provider-form.spec.tsx  |  379 ++++++-
 packages/client/ui-primitives/src/icons/index.tsx  |   21 +
 packages/client/ui-primitives/tests/icons.spec.tsx |    4 +-
 .../client/ui-settings-general/README.i18n.yaml    |    4 +-
 packages/client/ui-settings-general/README.md      |    2 +-
 packages/client/ui-settings-general/README.zh.md   |    2 +-
 .../ui-settings-general/src/client/chrome.tsx      |    4 +-
 packages/client/ui-skill/README.i18n.yaml          |    4 +-
 packages/client/ui-skill/README.md                 |    5 +
 packages/client/ui-skill/README.zh.md              |    5 +
 packages/client/ui-skill/package.json              |   20 +-
 .../client/ui-skill/src/client/SkillRow.module.css |  212 ++++
 packages/client/ui-skill/src/client/SkillRow.tsx   |  171 +++
 packages/client/ui-skill/src/client/index.ts       |   26 +-
 packages/client/ui-skill/src/client/locales.ts     |   23 +
 packages/client/ui-skill/src/invariant.ts          |    7 +-
 .../client/ui-skill/tests/browser-plugin.spec.ts   |   67 +-
 packages/client/ui-skill/tests/skill-row.spec.tsx  |  152 +++
 packages/client/ui-skill/tsconfig.json             |    9 +
 packages/client/ui-theme/README.i18n.yaml          |    4 +-
 packages/client/ui-theme/README.md                 |    2 +-
 packages/client/ui-theme/README.zh.md              |    2 +-
 .../client/ui-theme/src/styles/design-platform.css |    4 +
 packages/client/ui-workspace/tests/rows.spec.tsx   |    2 +-
 packages/code-runtime/README.i18n.yaml             |    4 +-
 packages/code-runtime/README.md                    |    2 +-
 packages/code-runtime/README.zh.md                 |    2 +-
 .../code-runtime/code-runtime-worker/src/index.ts  |   45 +-
 .../code-runtime-worker/tests/runtime.spec.ts      |   22 +-
 .../code-runtime-worker/tests/worker-json.spec.ts  |    2 +-
 .../code-runtime/code-runtime/README.i18n.yaml     |    4 +-
 packages/code-runtime/code-runtime/README.md       |    4 +-
 packages/code-runtime/code-runtime/README.zh.md    |    4 +-
 packages/code-runtime/code-runtime/src/index.ts    |   74 +-
 packages/code-runtime/code-runtime/src/types.ts    |   20 +-
 .../code-runtime/tests/reserved.spec.ts            |   57 +
 .../context/workspace-context/README.i18n.yaml     |    4 +-
 packages/context/workspace-context/README.md       |   12 +-
 packages/context/workspace-context/README.zh.md    |   12 +-
 packages/context/workspace-context/src/config.ts   |   23 +
 packages/context/workspace-context/src/files.ts    |   37 +-
 packages/context/workspace-context/src/index.ts    |   94 +-
 packages/context/workspace-context/src/render.ts   |   18 +-
 packages/context/workspace-context/src/state.ts    |   23 +-
 .../tests/workspace-context.spec.ts                |  392 ++++++-
 packages/cordis/tool-cordis/src/api-catalog.ts     |    8 +-
 packages/core/session/src/types.ts                 |    2 +-
 packages/core/tools/README.i18n.yaml               |    4 +-
 packages/core/tools/README.md                      |   10 +-
 packages/core/tools/README.zh.md                   |   10 +-
 packages/core/tools/src/code-mode.ts               |  154 ++-
 packages/core/tools/src/index.ts                   |   68 +-
 packages/core/tools/src/py-types.ts                |  818 ++++++++++++++
 packages/core/tools/src/ts-types.ts                |    5 +-
 packages/core/tools/tests/code-mode.spec.ts        |   86 +-
 packages/core/tools/tests/json-schema.spec.ts      |    2 +-
 packages/core/tools/tests/py-types.spec.ts         | 1163 ++++++++++++++++++++
 .../tests/gen-config-catalog.spec.ts               |   23 +
 packages/feedback/README.i18n.yaml                 |    6 +
 packages/feedback/README.md                        |   11 +
 packages/feedback/README.zh.md                     |   11 +
 .../feedback/command-feedback/README.i18n.yaml     |    6 +
 packages/feedback/command-feedback/README.md       |   59 +
 packages/feedback/command-feedback/README.zh.md    |   59 +
 packages/feedback/command-feedback/package.json    |   43 +
 packages/feedback/command-feedback/src/index.ts    |   63 ++
 .../feedback/command-feedback/src/invariant.ts     |   30 +
 .../tests/command-feedback.spec.ts                 |  186 ++++
 .../tests/loader-composition.spec.ts               |  110 ++
 packages/feedback/command-feedback/tsconfig.json   |   27 +
 packages/fs/fs-policy/README.i18n.yaml             |    4 +-
 packages/fs/fs-policy/README.md                    |    2 +-
 packages/fs/fs-policy/README.zh.md                 |    2 +-
 packages/fs/tool-fs/README.i18n.yaml               |    4 +-
 packages/fs/tool-fs/README.md                      |    2 +-
 packages/fs/tool-fs/README.zh.md                   |    2 +-
 packages/fs/tool-fs/src/edit.ts                    |   14 +-
 packages/fs/tool-fs/src/error.ts                   |   34 +
 packages/fs/tool-fs/src/write.ts                   |    6 +-
 packages/fs/tool-fs/tests/error.spec.ts            |   35 +
 packages/fs/tool-fs/tests/integration.spec.ts      |   80 ++
 packages/fs/tool-fs/tests/tools.spec.ts            |    3 +-
 packages/host/apiproxy/README.i18n.yaml            |    4 +-
 packages/host/apiproxy/README.md                   |   18 +-
 packages/host/apiproxy/README.zh.md                |   18 +-
 packages/host/apiproxy/src/api-proxy.ts            |  296 +++--
 packages/host/apiproxy/src/api/index.ts            |    1 +
 packages/host/apiproxy/src/api/llm.schema.ts       |    1 +
 packages/host/apiproxy/src/api/llm.ts              |    6 +
 packages/host/apiproxy/src/api/sessions.schema.ts  |    1 +
 packages/host/apiproxy/src/api/sessions.ts         |    9 +
 packages/host/apiproxy/src/api/subagents.ts        |    3 +-
 packages/host/apiproxy/src/index.ts                |   88 +-
 packages/host/apiproxy/src/native-path-opener.ts   |  118 +-
 .../host/apiproxy/tests/api-proxy-approval.spec.ts |    4 +-
 .../host/apiproxy/tests/api-proxy-blank.spec.ts    |    2 +-
 .../host/apiproxy/tests/api-proxy-cold.spec.ts     |   62 +-
 .../host/apiproxy/tests/api-proxy-commands.spec.ts |    2 +-
 .../host/apiproxy/tests/api-proxy-config.spec.ts   |   23 +-
 .../apiproxy/tests/api-proxy-default-route.spec.ts |  108 ++
 .../host/apiproxy/tests/api-proxy-fork.spec.ts     |    3 +-
 .../host/apiproxy/tests/api-proxy-models.spec.ts   |  132 ++-
 .../apiproxy/tests/api-proxy-projections.spec.ts   |    2 +-
 .../host/apiproxy/tests/api-proxy-question.spec.ts |    2 +-
 .../host/apiproxy/tests/api-proxy-rename.spec.ts   |    2 +-
 .../host/apiproxy/tests/api-proxy-search.spec.ts   |    2 +-
 .../apiproxy/tests/api-proxy-subagents.spec.ts     |  136 ++-
 .../host/apiproxy/tests/api-proxy-view.spec.ts     |   10 +-
 .../apiproxy/tests/api-proxy-workspace.spec.ts     |    3 +-
 .../host/apiproxy/tests/client-handler.spec.ts     |    1 +
 packages/host/apiproxy/tests/fetch-carrier.spec.ts |    1 +
 .../host/apiproxy/tests/native-path-opener.spec.ts |  191 +++-
 packages/host/apiproxy/tests/rpc-schemas.spec.ts   |    7 +-
 packages/llm/llm-deepseek/README.i18n.yaml         |    4 +-
 packages/llm/llm-deepseek/README.md                |    2 +-
 packages/llm/llm-deepseek/README.zh.md             |    2 +-
 packages/llm/llm-deepseek/src/index.ts             |   33 +-
 packages/llm/llm-deepseek/tests/adapter.spec.ts    |   42 +
 .../llm/llm-deepseek/tests/dynamic-config.spec.ts  |   21 +-
 packages/llm/llm-pi-ai/README.i18n.yaml            |    4 +-
 packages/llm/llm-pi-ai/README.md                   |    8 +-
 packages/llm/llm-pi-ai/README.zh.md                |    8 +-
 packages/llm/llm-pi-ai/src/adapter.ts              |   25 +-
 packages/llm/llm-pi-ai/src/config.ts               |   23 +-
 packages/llm/llm-pi-ai/src/discovery.ts            |   26 +-
 packages/llm/llm-pi-ai/src/index.ts                |   18 +-
 packages/llm/llm-pi-ai/tests/adapter.spec.ts       |   15 +-
 packages/llm/llm-pi-ai/tests/catalog.spec.ts       |   11 +-
 packages/llm/llm-pi-ai/tests/config.spec.ts        |   24 +
 packages/llm/llm-pi-ai/tests/discovery.spec.ts     |   47 +-
 .../llm/llm-pi-ai/tests/dynamic-config.spec.ts     |    1 +
 packages/llm/llm/README.i18n.yaml                  |    4 +-
 packages/llm/llm/README.md                         |    7 +-
 packages/llm/llm/README.zh.md                      |    7 +-
 packages/llm/llm/src/api-key.ts                    |   41 +
 packages/llm/llm/src/error.ts                      |    9 +
 packages/llm/llm/src/index.ts                      |   39 +-
 packages/llm/llm/src/types.ts                      |    9 +
 packages/llm/llm/tests/api-key.spec.ts             |   70 ++
 packages/llm/token-meter/src/surface-fold.ts       |    2 +-
 packages/plan/plan-mode/README.i18n.yaml           |    4 +-
 packages/plan/plan-mode/README.md                  |    2 +-
 packages/plan/plan-mode/README.zh.md               |    2 +-
 packages/plan/plan-mode/src/index.ts               |    1 +
 packages/plan/plan-mode/tests/projection.spec.ts   |   11 +-
 packages/sdk/helper/package.json                   |    1 +
 packages/sdk/helper/src/features/builtin/index.ts  |    8 +-
 packages/sdk/helper/tsconfig.json                  |    3 +
 .../session-query/tests/session-query.spec.ts      |   20 +-
 packages/subagent/subagent/README.i18n.yaml        |    4 +-
 packages/subagent/subagent/README.md               |    6 +-
 packages/subagent/subagent/README.zh.md            |    6 +-
 packages/subagent/subagent/package.json            |   10 +-
 packages/subagent/subagent/src/client.ts           |    2 +-
 packages/subagent/subagent/src/index.ts            |   47 +-
 packages/subagent/subagent/src/list-children.ts    |  410 ++++---
 packages/subagent/subagent/src/projection-types.ts |   39 +
 packages/subagent/subagent/src/projection.ts       |   78 +-
 .../subagent/subagent/tests/list-children.spec.ts  |  695 ++++++++----
 .../subagent/tests/optional-session-query.spec.ts  |   13 -
 .../subagent/tests/timing-projection.spec.ts       |   12 +-
 packages/subagent/subagent/tsconfig.json           |    4 +-
 .../tool-subagent-control/README.i18n.yaml         |    4 +-
 packages/subagent/tool-subagent-control/README.md  |    2 +-
 .../subagent/tool-subagent-control/README.zh.md    |    2 +-
 .../subagent/tool-subagent-control/package.json    |    8 +-
 .../tool-subagent-control/src/list-agents.ts       |   13 +-
 .../tests/list-agents.spec.ts                      |    9 +-
 .../tests/tool-subagent-control.spec.ts            |    2 +
 .../subagent/tool-subagent-control/tsconfig.json   |    3 -
 packages/telemetry/README.i18n.yaml                |    4 +-
 packages/telemetry/README.md                       |    8 +-
 packages/telemetry/README.zh.md                    |    8 +-
 .../session-telemetry-otel/README.i18n.yaml        |    4 +-
 .../telemetry/session-telemetry-otel/README.md     |   20 +-
 .../telemetry/session-telemetry-otel/README.zh.md  |   20 +-
 .../telemetry/session-telemetry-otel/package.json  |    2 +
 .../telemetry/session-telemetry-otel/src/index.ts  |  142 ++-
 .../session-telemetry-otel/src/invariant.ts        |    7 +-
 .../tests/loader-composition.e2e.ts                |   93 +-
 .../session-telemetry-otel/tests/otel.spec.ts      |  182 ++-
 .../telemetry/session-telemetry-otel/tsconfig.json |    3 +
 .../telemetry/session-telemetry/README.i18n.yaml   |    4 +-
 packages/telemetry/session-telemetry/README.md     |   11 +-
 packages/telemetry/session-telemetry/README.zh.md  |   11 +-
 .../telemetry/session-telemetry/src/coordinator.ts |  226 ++--
 packages/telemetry/session-telemetry/src/index.ts  |   23 +-
 .../session-telemetry/tests/telemetry.spec.ts      |  117 +-
 packages/todo/tool-todo/README.i18n.yaml           |    4 +-
 packages/todo/tool-todo/README.md                  |   10 +-
 packages/todo/tool-todo/README.zh.md               |   10 +-
 packages/todo/tool-todo/package.json               |    3 +
 packages/todo/tool-todo/src/index.ts               |  108 +-
 packages/todo/tool-todo/src/invariant.ts           |   13 +-
 packages/todo/tool-todo/tests/integration.spec.ts  |    2 +-
 packages/todo/tool-todo/tests/invariant.spec.ts    |   20 +-
 .../tool-todo/tests/loader-composition.spec.ts     |  139 +++
 packages/todo/tool-todo/tests/projection.spec.ts   |    6 +-
 packages/todo/tool-todo/tests/tool-todo.spec.ts    |   87 +-
 packages/ui/commands/README.i18n.yaml              |    4 +-
 packages/ui/commands/README.md                     |    4 +-
 packages/ui/commands/README.zh.md                  |    4 +-
 packages/ui/commands/src/index.ts                  |   17 +-
 packages/ui/commands/tests/commands.spec.ts        |   19 +
 289 files changed, 10811 insertions(+), 1600 deletions(-)
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
- 需适配：锚定 4832fffbc8963b8a7b1f8332e691083195bf94bc（未知（不同谱系））、补丁状态「CONFLICT（3 个补丁中 1 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dshx-update-check
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ex-setting
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（3 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### qqbot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### Qwen-MM-Plugins
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### Recall
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### review-panel
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-mxc
- 需适配：锚定 93fe8cc2（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 a6fedc9e3b36d066e34860d040db6df47d88c432（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### web-components
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（e72bf03）为新基线重新锚定/rebuild 补丁。
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
- 兼容：锚定 4d3e1305d7f96c9b8e5842c71eab65b0ee7d36f5（未知（不同谱系））、补丁「OK（1 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 4d3e1305d7f96c9b8e5842c71eab65b0ee7d36f5 显式记录到 README/补丁头，快照一漂即可自动预警。
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

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
