# mainline 兼容性报告（2026-08-07）

- mainline：`9d84ab4`（snapshots/20260806T160212Z）
- 上次对比：`bfb913696efaa241b92fe8731b2d2336bdb7f697`
- 兼容性：68/79 无需适配，10 需适配（dsh-my-rsi dsh-subagent-tree dsh-working-activity ex-setting plugin-registry Qwen-MM-Plugins sandbox-mxc turtle-ui web-components fabric）；其中关注 3、占位 4、不适用 2、已删除 1

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
| dsh-cc-tui | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 关注 |
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
| dsh-sfw | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-shell-windows | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-skills-manager | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 关注 |
| dsh-skins | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-subagent-tree | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 6 项匹配 | 需适配 |
| dsh-tool-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-tool-calculator | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-tool-encoding | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-tool-json | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-tool-time | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-ui-progress | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-ui-whale | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
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
| marisa | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 关注 |
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 11 项匹配 | 需适配 |
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
| dsh-grok-tui | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| ds_web_craw | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| fabric | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 9 项匹配 | 需适配 |
| dsh-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-desktop-mac | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-public-repo-monitor | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-tui | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-inspect | 未知 | 无补丁 | 缺: tuiPrompt | 1 项匹配 | 兼容 |

## mainline 变更分析（bfb913696efaa241b92fe8731b2d2336bdb7f697 → 9d84ab4）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **包级变化**：packages/ 下删除 0 个包目录、新增 14 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：

新增文件：
```
packages/bash/bash/src/render.ts
packages/bash/bash/tests/render.spec.ts
packages/bundle/README.i18n.yaml
packages/bundle/README.md
packages/bundle/README.zh.md
packages/bundle/base/README.i18n.yaml
packages/bundle/base/README.md
packages/bundle/base/README.zh.md
packages/bundle/base/cordis.patch.yml
packages/bundle/base/package.json
packages/bundle/base/src/index.ts
packages/bundle/base/src/invariant.ts
packages/bundle/base/tests/base.spec.ts
packages/bundle/base/tsconfig.json
packages/bundle/headless/README.i18n.yaml
```

### seam 符号变化

| 符号 | prev 文件数 | cur 文件数 | 变化 |
|---|---|---|---|
| `ThemeService` | 26 | 26 | 存在 → 存在（稳定） |
| `settingsNamespace` | 16 | 16 | 存在 → 存在（稳定） |
| `sessionProjections` | 21 | 21 | 存在 → 存在（稳定） |
| `tuiPrompt` | 0 | 0 | 缺失 → 缺失 |
| `slots` | 15 | 13 | 存在 → 存在（稳定） |
| `session/event` | 48 | 52 | 存在 → 存在（稳定） |

### diffstat（packages/ patches/ workspace）

```
 packages/README.i18n.yaml                          |    4 +-
 packages/README.md                                 |    7 +-
 packages/README.zh.md                              |    7 +-
 packages/acp/acp/README.i18n.yaml                  |    4 +-
 packages/acp/acp/README.md                         |    4 +-
 packages/acp/acp/README.zh.md                      |    4 +-
 packages/acp/acp/src/codec.ts                      |    8 +-
 packages/acp/acp/src/index.ts                      |   74 +-
 packages/acp/acp/tests/approval.spec.ts            |    2 +-
 packages/acp/acp/tests/codec.spec.ts               |   47 +-
 packages/acp/acp/tests/dispose.spec.ts             |   10 +-
 packages/acp/acp/tests/turns.spec.ts               |  136 +-
 packages/bash/bash-local/README.i18n.yaml          |    4 +-
 packages/bash/bash-local/README.md                 |    2 +-
 packages/bash/bash-local/README.zh.md              |    2 +-
 packages/bash/bash-local/src/index.ts              |    7 +-
 packages/bash/bash-local/tests/executor.spec.ts    |    3 +
 packages/bash/bash/README.i18n.yaml                |    4 +-
 packages/bash/bash/README.md                       |    2 +
 packages/bash/bash/README.zh.md                    |    2 +
 packages/bash/bash/src/index.ts                    |    2 +
 packages/bash/bash/src/render.ts                   |   42 +
 packages/bash/bash/tests/render.spec.ts            |   36 +
 packages/bash/pwsh-local/README.i18n.yaml          |    4 +-
 packages/bash/pwsh-local/README.md                 |    2 +-
 packages/bash/pwsh-local/README.zh.md              |    2 +-
 packages/bash/pwsh-local/src/index.ts              |    7 +-
 packages/bash/pwsh-local/tests/executor.spec.ts    |    5 +-
 packages/bash/tool-bash/src/render.ts              |   37 +-
 packages/bash/tool-bash/tests/integration.spec.ts  |   25 +-
 packages/bash/tool-pwsh/README.i18n.yaml           |    4 +-
 packages/bash/tool-pwsh/README.md                  |    3 +-
 packages/bash/tool-pwsh/README.zh.md               |    3 +-
 packages/bash/tool-pwsh/src/index.ts               |   20 +-
 packages/bash/tool-pwsh/tests/tools.spec.ts        |   89 +-
 packages/bundle/README.i18n.yaml                   |    6 +
 packages/bundle/README.md                          |   13 +
 packages/bundle/README.zh.md                       |   13 +
 packages/bundle/base/README.i18n.yaml              |    6 +
 packages/bundle/base/README.md                     |   19 +
 packages/bundle/base/README.zh.md                  |   19 +
 packages/bundle/base/cordis.patch.yml              |  404 +++++
 packages/bundle/base/package.json                  |  111 ++
 packages/bundle/base/src/index.ts                  |    9 +
 packages/bundle/base/src/invariant.ts              |   28 +
 packages/bundle/base/tests/base.spec.ts            |   25 +
 packages/bundle/base/tsconfig.json                 |   18 +
 packages/bundle/headless/README.i18n.yaml          |    6 +
 packages/bundle/headless/README.md                 |   18 +
 packages/bundle/headless/README.zh.md              |   18 +
 packages/bundle/headless/cordis.patch.yml          |   21 +
 packages/bundle/headless/package.json              |   54 +
 packages/bundle/headless/src/index.ts              |  173 +++
 packages/bundle/headless/src/invariant.ts          |   30 +
 packages/bundle/headless/tests/headless.spec.ts    |  218 +++
 packages/bundle/headless/tsconfig.json             |   36 +
 packages/bundle/web-app/README.i18n.yaml           |    6 +
 packages/bundle/web-app/README.md                  |   26 +
 packages/bundle/web-app/README.zh.md               |   26 +
 packages/bundle/web-app/cordis.patch.yml           |  194 +++
 packages/bundle/web-app/package.json               |   86 ++
 packages/bundle/web-app/src/index.ts               |  157 ++
 packages/bundle/web-app/src/invariant.ts           |   30 +
 packages/bundle/web-app/tests/web-app.spec.ts      |  197 +++
 packages/bundle/web-app/tsconfig.json              |   33 +
 packages/client/AGENTS.md                          |    4 +-
 packages/client/connection/src/client/api.ts       |    5 +-
 packages/client/connection/src/client/fixture.ts   |  197 ++-
 packages/client/connection/src/client/index.ts     |    4 +-
 packages/client/connection/src/index.ts            |   14 +-
 packages/client/connection/tests/fake-api.ts       |    1 +
 packages/client/connection/tests/fixture.spec.ts   |   45 +-
 packages/client/connection/tests/node-half.spec.ts |    7 +-
 packages/client/locale/src/client/index.ts         |   21 +-
 packages/client/runtime/README.i18n.yaml           |    4 +-
 packages/client/runtime/README.md                  |   14 +-
 packages/client/runtime/README.zh.md               |   16 +-
 .../client/runtime/src/client/contract/session.ts  |    4 +-
 packages/client/runtime/src/client/index.ts        |    3 +
 .../src/client/session-history/history-fold.ts     |   74 +-
 .../src/client/sessions/assistant-timing.ts        |   84 ++
 .../src/client/sessions/context-provenance.ts      |  116 ++
 .../runtime/src/client/sessions/conversation.ts    |   16 +-
 .../runtime/src/client/sessions/failure-display.ts |    9 +-
 .../client/runtime/src/client/sessions/lineage.ts  |    5 +
 .../client/runtime/src/client/sessions/manager.ts  |   67 +-
 .../src/client/sessions/request-inspection.ts      |   17 +-
 .../client/runtime/src/client/sessions/service.ts  |    3 +
 .../client/runtime/src/client/sessions/session.ts  |   34 +-
 .../src/client/sessions/steering-history.ts        |   65 +
 .../src/client/sessions/transcript-adapter.ts      |   49 +-
 packages/client/runtime/src/client/slots.ts        |   94 +-
 .../runtime/tests/context-provenance.spec.ts       |  Bin 0 -> 4572 bytes
 packages/client/runtime/tests/event-script.ts      |    9 +-
 packages/client/runtime/tests/fake-api.ts          |    1 +
 packages/client/runtime/tests/history-fold.spec.ts |   45 +-
 packages/client/runtime/tests/lineage.spec.ts      |    7 +
 packages/client/runtime/tests/manager.spec.ts      |  125 ++
 packages/client/runtime/tests/queue-store.spec.ts  |   38 +-
 .../runtime/tests/request-inspection.spec.ts       |   15 +-
 packages/client/runtime/tests/session.spec.ts      |   87 +-
 .../client/runtime/tests/slots-service.spec.ts     |  263 +++-
 .../runtime/tests/transcript-adapter.spec.ts       |  127 +-
 packages/client/ui-command/README.i18n.yaml        |    4 +-
 packages/client/ui-command/README.md               |    2 +
 packages/client/ui-command/README.zh.md            |    2 +
 packages/client/ui-command/src/client/index.ts     |   10 +-
 packages/client/ui-command/src/client/service.ts   |   79 +-
 .../client/ui-command/tests/browser-plugin.spec.ts |   31 +-
 packages/client/ui-command/tests/service.spec.ts   |   26 +-
 packages/client/ui-conversation/README.i18n.yaml   |    4 +-
 packages/client/ui-conversation/README.md          |   18 +-
 packages/client/ui-conversation/README.zh.md       |   24 +-
 .../client/ui-conversation/src/client/apply.ts     |   75 +-
 .../src/client/chat/AssistantMarkdown.tsx          |    8 +-
 .../ui-conversation/src/client/chat/ChatView.tsx   |    7 +
 .../src/client/chat/ContextBody.module.css         |  161 ++
 .../src/client/chat/ContextBody.tsx                |  591 ++++++++
 .../src/client/chat/ContextInjectionRow.module.css |   37 +-
 .../src/client/chat/ContextInjectionRow.tsx        |   90 +-
 .../src/client/chat/MessageIconActions.tsx         |   31 +-
 .../src/client/chat/MessageItem.module.css         |    9 +
 .../src/client/chat/MessageItem.tsx                |   22 +-
 .../ui-conversation/src/client/chat/StatsLine.tsx  |  127 +-
 .../ui-conversation/src/client/chat/chat-flow.ts   |    3 +-
 .../src/client/chat/message-chrome.ts              |   21 +
 .../src/client/chat/turn-metrics.ts                |   97 ++
 .../ui-conversation/src/client/contract/slots.ts   |   59 +-
 .../src/client/contract/terminal-card-model.ts     |    2 +-
 .../src/client/contract/tool-call-model.ts         |    4 +
 .../client/ui-conversation/src/client/index.ts     |    3 +-
 .../client/ui-conversation/src/client/locales.ts   |   54 +
 .../ui-conversation/src/client/queue/QueueDock.tsx |    8 +-
 .../src/client/skeleton/ContextMeter.module.css    |  147 ++
 .../src/client/skeleton/ContextMeter.tsx           |  153 ++
 .../client/skeleton/ConversationRoot.module.css    |    4 +-
 .../src/client/skeleton/ConversationRoot.tsx       |   34 +-
 .../src/client/skeleton/ConversationSession.tsx    |  159 +-
 .../src/client/skeleton/EmptyHero.tsx              |    9 +-
 .../src/client/skeleton/HeroShell.module.css       |   31 +-
 .../src/client/skeleton/InputBar.tsx               |    2 +
 .../src/client/skeleton/TodoPanel.tsx              |   11 +-
 .../src/client/toolviews/ask-question-row.tsx      |   12 +-
 .../src/client/toolviews/bash-sample.tsx           |   11 +-
 .../src/client/toolviews/file-mutation-row.tsx     |   14 +-
 .../src/client/toolviews/read-row.tsx              |   11 +-
 .../src/client/toolviews/search-row.tsx            |   16 +-
 .../src/client/toolviews/todo-row.tsx              |   10 +-
 .../src/client/toolviews/web-row.tsx               |   14 +-
 .../ui-conversation/tests/apply-inject.spec.tsx    |   14 +-
 .../tests/ask-question-row.spec.tsx                |   10 +-
 .../tests/assembly-surfaces.spec.tsx               |   56 +-
 .../ui-conversation/tests/chat-apply.spec.tsx      |   13 +-
 .../tests/chat-branch-tails.spec.tsx               |  471 +++++-
 .../tests/chat-stats-bash-sample.spec.tsx          |  152 +-
 .../ui-conversation/tests/chat-tool-row.spec.tsx   |    7 +
 .../tests/chat-toolview-slot.spec.tsx              |   32 +-
 .../ui-conversation/tests/chat-view.spec.tsx       |   66 +-
 .../ui-conversation/tests/context-meter.spec.tsx   |  158 ++
 .../ui-conversation/tests/diff-card.spec.tsx       |   11 +-
 .../tests/gate-branch-tails.spec.tsx               |   18 +-
 .../ui-conversation/tests/queue-dock.spec.tsx      |    6 +-
 .../ui-conversation/tests/read-card.spec.tsx       |    7 +-
 .../ui-conversation/tests/search-card.spec.tsx     |    7 +-
 .../tests/selection-survival.spec.tsx              |    9 +-
 .../client/ui-conversation/tests/skeleton.spec.tsx |   47 +-
 .../ui-conversation/tests/todo-panel.spec.tsx      |   18 +-
 .../ui-conversation/tests/turn-metrics.spec.ts     |  154 ++
 .../client/ui-conversation/tests/web-card.spec.tsx |    7 +-
 packages/client/ui-goal/README.i18n.yaml           |    4 +-
 packages/client/ui-goal/README.md                  |    4 +-
 packages/client/ui-goal/README.zh.md               |    4 +-
 packages/client/ui-goal/src/client/index.ts        |   85 +-
 .../client/ui-goal/tests/browser-plugin.spec.tsx   |   36 +-
 packages/client/ui-model/src/client/index.ts       |    8 +-
 .../client/ui-model/tests/browser-plugin.spec.ts   |    2 +-
 packages/client/ui-models/README.i18n.yaml         |    4 +-
 packages/client/ui-models/README.md                |   12 +-
 packages/client/ui-models/README.zh.md             |   12 +-
 .../ui-models/src/client/CustomProviderCard.tsx    |  240 +++
 .../src/client/DeepSeekOnboardingDialog.tsx        |   47 +-
 .../client/ui-models/src/client/EditorFooter.tsx   |   65 +
 .../ui-models/src/client/ModelListEditor.tsx       |  459 ++++++
 .../ui-models/src/client/ModelsSection.module.css  |   62 +-
 .../client/ui-models/src/client/ModelsSection.tsx  |   87 +-
 .../client/ui-models/src/client/ProviderEditor.tsx |   92 +-
 packages/client/ui-models/src/client/index.ts      |   41 +-
 packages/client/ui-models/src/client/locales.ts    |   46 +
 packages/client/ui-models/src/client/store.ts      |   24 +-
 packages/client/ui-models/tests/apply.spec.ts      |    2 +-
 .../client/ui-models/tests/provider-form.spec.tsx  |  865 +++++++++++
 packages/client/ui-models/tests/styles.spec.ts     |   43 +-
 packages/client/ui-permission/src/client/index.ts  |   19 +-
 packages/client/ui-plan/src/client/index.ts        |   12 +-
 .../client/ui-plan/tests/browser-plugin.spec.ts    |   16 +-
 packages/client/ui-primitives/README.i18n.yaml     |    4 +-
 packages/client/ui-primitives/README.md            |    5 +-
 packages/client/ui-primitives/README.zh.md         |    5 +-
 packages/client/ui-primitives/package.json         |    9 +-
 .../ui-primitives/src/OnboardingSurface.module.css |   29 +
 .../client/ui-primitives/src/OnboardingSurface.tsx |   34 +
 packages/client/ui-primitives/src/index.ts         |    1 +
 .../ui-primitives/src/markdown/MarkdownText.tsx    |  273 ++--
 .../src/markdown/cjkFriendlyStrong.ts              |   83 ++
 .../ui-primitives/src/markdown/incremental.ts      |  130 ++
 .../client/ui-primitives/src/markdown/katex.tsx    |   90 ++
 ...rkMathCompatibility.ts => mathCompatibility.ts} |   18 +-
 .../client/ui-primitives/src/markdown/parse.ts     |   44 +
 .../ui-primitives/src/markdown/plain-text.ts       |   15 +-
 .../client/ui-primitives/src/markdown/render.tsx   |  544 +++++++
 .../markdown-dom/blockquote-nested.settled.txt     |   12 +
 .../markdown-dom/blockquote-nested.streaming.txt   |   12 +
 .../cjk-strong-and-inline-code-url.settled.txt     |   20 +
 .../cjk-strong-and-inline-code-url.streaming.txt   |   20 +
 .../fixtures/markdown-dom/code-fences.settled.txt  |   78 +
 .../markdown-dom/code-fences.streaming.txt         |   53 +
 .../markdown-dom/definition-only.settled.txt       |    1 +
 .../markdown-dom/definition-only.streaming.txt     |    1 +
 .../markdown-dom/entities-and-escapes.settled.txt  |    3 +
 .../entities-and-escapes.streaming.txt             |    3 +
 .../fence-trailing-blank-lines.settled.txt         |   37 +
 .../fence-trailing-blank-lines.streaming.txt       |   23 +
 .../fixtures/markdown-dom/footnotes.settled.txt    |   29 +
 .../fixtures/markdown-dom/footnotes.streaming.txt  |   29 +
 .../gfm-strikethrough-and-literals.settled.txt     |   12 +
 .../gfm-strikethrough-and-literals.streaming.txt   |   12 +
 .../markdown-dom/hard-breaks-and-hr.settled.txt    |   12 +
 .../markdown-dom/hard-breaks-and-hr.streaming.txt  |   12 +
 .../heading-tight-against-list.settled.txt         |   15 +
 .../heading-tight-against-list.streaming.txt       |   15 +
 .../headings-and-paragraphs.settled.txt            |   33 +
 .../headings-and-paragraphs.streaming.txt          |   33 +
 .../tests/fixtures/markdown-dom/images.settled.txt |   14 +
 .../fixtures/markdown-dom/images.streaming.txt     |   14 +
 .../inline-code-with-newline.settled.txt           |    6 +
 .../inline-code-with-newline.streaming.txt         |    6 +
 .../markdown-dom/links-and-autolinks.settled.txt   |   25 +
 .../markdown-dom/links-and-autolinks.streaming.txt |   25 +
 .../lists-tight-loose-nested.settled.txt           |   44 +
 .../lists-tight-loose-nested.streaming.txt         |   44 +
 .../markdown-dom/math-edge-cases.settled.txt       |  125 ++
 .../markdown-dom/math-edge-cases.streaming.txt     |   29 +
 .../math-inline-and-display.settled.txt            |  320 ++++
 .../math-inline-and-display.streaming.txt          |    9 +
 .../markdown-dom/raw-html-dropped.settled.txt      |    7 +
 .../markdown-dom/raw-html-dropped.streaming.txt    |    7 +
 .../reference-links-and-images.settled.txt         |   16 +
 .../reference-links-and-images.streaming.txt       |   16 +
 .../streaming-typical-partial.settled.txt          |    8 +
 .../streaming-typical-partial.streaming.txt        |    8 +
 .../markdown-dom/table-header-only.settled.txt     |   11 +
 .../markdown-dom/table-header-only.streaming.txt   |   11 +
 .../markdown-dom/table-with-alignment.settled.txt  |   35 +
 .../table-with-alignment.streaming.txt             |   35 +
 .../fixtures/markdown-dom/task-lists.settled.txt   |   19 +
 .../fixtures/markdown-dom/task-lists.streaming.txt |   19 +
 .../tests/markdown-dom-parity.spec.tsx             |  265 ++++
 .../tests/markdown-incremental.spec.tsx            |  427 ++++++
 .../tests/markdown-render-units.spec.tsx           |  225 +++
 .../client/ui-primitives/tests/markdown.spec.tsx   |  106 +-
 .../tests/onboarding-surface.spec.tsx              |   47 +
 packages/client/ui-question/src/client/index.ts    |   20 +-
 .../ui-question/tests/browser-plugin.spec.ts       |   23 +-
 .../src/client/WelcomeNotice.tsx                   |   47 +-
 .../client/ui-settings-general/src/client/index.ts |   76 +-
 packages/client/ui-settings/README.i18n.yaml       |    4 +-
 packages/client/ui-settings/README.md              |    2 +-
 packages/client/ui-settings/README.zh.md           |    2 +-
 .../ui-settings/src/client/SettingsRoot.module.css |   30 -
 .../client/ui-settings/src/client/SettingsRoot.tsx |   34 +-
 .../ui-settings/src/client/contract/slots.ts       |    8 +-
 packages/client/ui-settings/src/client/index.ts    |   34 +-
 packages/client/ui-settings/tests/apply.spec.ts    |    2 +-
 .../ui-settings/tests/settings-root.spec.tsx       |   11 +-
 packages/client/ui-slash/src/client/index.ts       |   10 +-
 packages/client/ui-slash/tests/apply.spec.ts       |   18 +-
 packages/client/ui-slots/README.i18n.yaml          |    4 +-
 packages/client/ui-slots/README.md                 |    2 +-
 packages/client/ui-slots/README.zh.md              |    2 +-
 packages/client/ui-slots/src/deferred.ts           |  128 --
 packages/client/ui-slots/src/index.ts              |   63 +-
 packages/client/ui-slots/tests/core.spec.ts        |   54 +
 packages/client/ui-slots/tests/deferred.spec.ts    |  126 --
 packages/client/ui-subagent/src/client/index.ts    |   10 +-
 .../ui-subagent/tests/browser-plugin.spec.ts       |    3 +-
 packages/client/ui-theme/src/client/index.ts       |   22 +-
 packages/client/ui-trajectory/src/client/index.ts  |   14 +-
 packages/client/ui-trajectory/src/client/layout.ts |   18 +-
 .../ui-trajectory/tests/client-bundle.spec.ts      |    8 +-
 .../ui-trajectory/tests/context-branches.spec.ts   |    2 +
 packages/client/ui-trajectory/tests/views.spec.tsx |   78 +-
 .../ui-trajectory/tests/virtual-rows.spec.ts       |    2 +-
 packages/client/ui-workspace/README.i18n.yaml      |    4 +-
 packages/client/ui-workspace/README.md             |    2 +-
 packages/client/ui-workspace/README.zh.md          |    2 +-
 packages/client/ui-workspace/src/client/index.ts   |   58 +-
 packages/client/ui-workspace/src/client/locales.ts |    2 +
 .../client/ui-workspace/src/client/rows/Rows.tsx   |   12 +-
 packages/client/ui-workspace/src/client/tree.ts    |    6 +
 packages/client/ui-workspace/tests/rows.spec.tsx   |   66 +-
 packages/client/ui-workspace/tests/tree.spec.ts    |   19 +
 packages/compact/command-compact/src/index.ts      |    2 +
 .../command-compact/tests/command-compact.spec.ts  |    1 +
 packages/compact/compact-basic/README.i18n.yaml    |    4 +-
 packages/compact/compact-basic/README.md           |    2 +-
 packages/compact/compact-basic/README.zh.md        |    2 +-
 packages/compact/compact-basic/src/index.ts        |  121 +-
 .../compact-basic/tests/compact-basic.spec.ts      |   61 +-
 .../compact-basic/tests/compact-loop-repro.spec.ts |   37 +-
 .../compact-basic/tests/loader-composition.spec.ts |    2 +-
 .../compact-basic/tests/manual-compact.spec.ts     |   81 +-
 .../compact/compact-tool-result-prune/package.json |    4 +
 .../compact/compact-tool-result-prune/src/index.ts |   21 +-
 .../tests/loader-composition.spec.ts               |   10 +-
 .../tests/tool-result-prune.spec.ts                |   28 +-
 .../compact-tool-result-prune/tsconfig.json        |    2 +
 packages/compact/compact/README.i18n.yaml          |    4 +-
 packages/compact/compact/README.md                 |    2 +-
 packages/compact/compact/README.zh.md              |    2 +-
 packages/compact/compact/src/index.ts              |   32 +-
 packages/compact/compact/src/types.ts              |   24 +-
 packages/compact/compact/tests/compact.spec.ts     |    2 +-
 packages/compact/compact/tests/invariant.spec.ts   |    6 +-
 .../compact/compact/tests/tool-pairing.spec.ts     |    3 +-
 .../context/session-reference/README.i18n.yaml     |    4 +-
 packages/context/session-reference/README.md       |    4 +-
 packages/context/session-reference/README.zh.md    |    4 +-
 packages/context/session-reference/src/index.ts    |    1 +
 .../context/session-reference/src/projection.ts    |    6 -
 packages/context/session-reference/src/types.ts    |    2 +
 .../tests/session-reference.spec.ts                |   39 +-
 packages/context/time-context/README.i18n.yaml     |    4 +-
 packages/context/time-context/README.md            |    8 +-
 packages/context/time-context/README.zh.md         |    8 +-
 packages/context/time-context/src/index.ts         |   38 +-
 packages/context/time-context/src/invariant.ts     |   40 +-
 .../context/time-context/tests/invariant.spec.ts   |   31 +-
 .../context/time-context/tests/time-context.e2e.ts |   16 +-
 .../time-context/tests/time-context.spec.ts        |   71 +-
 packages/context/tmux-context/README.i18n.yaml     |    4 +-
 packages/context/tmux-context/README.md            |    4 +-
 packages/context/tmux-context/README.zh.md         |    4 +-
 packages/context/tmux-context/src/index.ts         |   44 +-
 .../tmux-context/tests/tmux-context.spec.ts        |   48 +-
 .../context/workspace-context/README.i18n.yaml     |    4 +-
 packages/context/workspace-context/README.md       |    6 +-
 packages/context/workspace-context/README.zh.md    |    6 +-
 packages/context/workspace-context/src/index.ts    |  314 ++--
 packages/context/workspace-context/src/state.ts    |  393 ++---
 .../tests/workspace-context.e2e.ts                 |    2 +-
 .../tests/workspace-context.spec.ts                | 1570 +++++++++++++-------
 packages/cordis/repository-plugin/README.i18n.yaml |    4 +-
 packages/cordis/repository-plugin/README.md        |    4 +-
 packages/cordis/repository-plugin/README.zh.md     |    4 +-
 packages/cordis/tool-cordis/src/api-catalog.ts     |  264 ++--
 .../cordis/tool-cordis/tests/integration.spec.ts   |    2 +-
 packages/core/agent-loop/README.i18n.yaml          |    4 +-
 packages/core/agent-loop/README.md                 |   18 +-
 packages/core/agent-loop/README.zh.md              |   18 +-
 packages/core/agent-loop/src/agent.ts              | 1111 ++++----------
 packages/core/agent-loop/src/index.ts              |  108 +-
 packages/core/agent-loop/src/invariant.ts          |   22 +-
 packages/core/agent-loop/src/runtime-context.ts    |   76 +
 packages/core/agent-loop/src/tool-calls.ts         |    2 +-
 .../core/agent-loop/tests/agent-initiator.spec.ts  |   25 +-
 packages/core/agent-loop/tests/agent.spec.ts       |  157 +-
 packages/core/agent-loop/tests/cancel.spec.ts      |  343 ++---
 .../agent-loop/tests/config-session-id.spec.ts     |   43 +-
 .../agent-loop/tests/contract-regressions.spec.ts  |  577 +++----
 .../core/agent-loop/tests/coverage-edges.spec.ts   |  118 +-
 .../core/agent-loop/tests/interception.spec.ts     |  399 ++---
 packages/core/agent-loop/tests/invariant.spec.ts   |   26 +-
 packages/core/agent-loop/tests/loop.spec.ts        |  371 ++---
 packages/core/agent-loop/tests/properties.spec.ts  |    6 +-
 .../core/agent-loop/tests/request-cache.e2e.ts     |    2 +-
 .../core/agent-loop/tests/request-error.spec.ts    |   33 +-
 .../tests/request-reconstruction.spec.ts           |   72 +-
 packages/core/agent-loop/tests/resume.spec.ts      |  215 ++-
 .../core/agent-loop/tests/runtime-context.spec.ts  |   45 +
 .../core/agent-loop/tests/scope-lifecycle.spec.ts  |   40 +-
 packages/core/agent-loop/tests/tool-calls.spec.ts  |   39 +-
 packages/core/agent-loop/tests/tool-order.spec.ts  |   16 +-
 .../core/agent-loop/tests/turn-admission.spec.ts   |  286 ----
 packages/core/agent/README.i18n.yaml               |    4 +-
 packages/core/agent/README.md                      |   33 +-
 packages/core/agent/README.zh.md                   |   33 +-
 packages/core/agent/package.json                   |    7 -
 packages/core/agent/src/brand.ts                   |   23 -
 packages/core/agent/src/dispatch.ts                |   94 +-
 packages/core/agent/src/inbox.ts                   |  222 +++
 packages/core/agent/src/index.ts                   |   10 +-
 packages/core/agent/src/invariant.ts               |   23 +-
 packages/core/agent/src/llm-target.ts              |    2 +-
 packages/core/agent/src/types.ts                   |  439 ++----
 packages/core/agent/tests/agent.spec.ts            |  169 ++-
 packages/core/agent/tests/invariant.spec.ts        |   65 +-
 packages/core/agent/tests/llm-target.spec.ts       |    8 +-
 packages/core/agent/tsconfig.json                  |    3 -
 packages/core/agent/tsdown.config.ts               |    2 +-
 packages/core/scope/src/scoped-events.generated.ts |   30 +-
 packages/core/scope/tests/invariant.spec.ts        |   50 +-
 packages/core/session/README.i18n.yaml             |    4 +-
 packages/core/session/README.md                    |   23 +-
 packages/core/session/README.zh.md                 |   23 +-
 packages/core/session/src/index.ts                 |  228 +--
 packages/core/session/src/invariant.ts             |    5 +-
 packages/core/session/src/preparation.ts           |   49 +
 packages/core/session/src/surface.ts               |   80 +-
 packages/core/session/src/types.ts                 |  109 +-
 packages/core/session/tests/derived-cache.spec.ts  |   12 +-
 packages/core/session/tests/fork.spec.ts           |   28 +-
 packages/core/session/tests/invariant.spec.ts      |   98 +-
 packages/core/session/tests/properties.spec.ts     |    2 +-
 packages/core/session/tests/repair.spec.ts         |    2 +-
 packages/core/session/tests/request-header.spec.ts |    6 +-
 packages/core/session/tests/scoped.spec.ts         |    4 +-
 packages/core/session/tests/session.spec.ts        |  208 ++-
 packages/core/session/tests/surface.spec.ts        |   34 +-
 packages/core/system-prompt/README.i18n.yaml       |    4 +-
 packages/core/system-prompt/README.md              |   22 +-
 packages/core/system-prompt/README.zh.md           |   26 +-
 packages/core/system-prompt/src/index.ts           |   62 +-
 packages/core/tools/tests/invariant.spec.ts        |    4 +-
 .../credentials/credentials-local/README.i18n.yaml |    4 +-
 packages/credentials/credentials-local/README.md   |    2 +-
 .../credentials/credentials-local/README.zh.md     |    2 +-
 packages/examples/acp-demo/tests/acp-agent.spec.ts |   11 +-
 .../agent-spine-demo/tests/agent-core.spec.ts      |   55 +-
 packages/examples/cli-demo/README.i18n.yaml        |    4 +-
 packages/examples/cli-demo/README.md               |   16 +-
 packages/examples/cli-demo/README.zh.md            |   16 +-
 packages/examples/cli-demo/src/cli.ts              |  114 +-
 packages/examples/cli-demo/tests/built-bin.e2e.ts  |   20 +-
 packages/examples/cli-demo/tests/cli-demo.spec.ts  |   11 +-
 packages/examples/cli-demo/tests/cli.spec.ts       |  190 ++-
 packages/fs/tool-fs-search/README.i18n.yaml        |    4 +-
 packages/fs/tool-fs-search/README.md               |    2 +-
 packages/fs/tool-fs-search/README.zh.md            |    2 +-
 packages/fs/tool-fs-search/package.json            |    2 +
 packages/fs/tool-fs-search/src/index.ts            |    6 +-
 packages/fs/tool-fs-search/tests/tools.spec.ts     |   12 +
 packages/fs/tool-fs-search/tsconfig.json           |    3 +
 packages/fs/tool-fs/tests/harness.ts               |    2 +-
 .../fs/tool-str-replace-editor/tests/tools.spec.ts |   12 +-
 packages/goal/command-goal/README.i18n.yaml        |    4 +-
 packages/goal/command-goal/README.md               |    8 +-
 packages/goal/command-goal/README.zh.md            |    8 +-
 .../goal/command-goal/tests/command-goal.spec.ts   |   25 +-
 packages/goal/goal-session/README.i18n.yaml        |    4 +-
 packages/goal/goal-session/README.md               |   23 +-
 packages/goal/goal-session/README.zh.md            |   23 +-
 packages/goal/goal-session/src/index.ts            |  264 ++--
 packages/goal/goal-session/src/outcome.ts          |   51 -
 .../goal/goal-session/tests/goal-session.spec.ts   |  397 ++---
 packages/goal/goal-session/tests/invariant.spec.ts |   35 +-
 packages/goal/goal/README.i18n.yaml                |    4 +-
 packages/goal/goal/README.md                       |   14 +-
 packages/goal/goal/README.zh.md                    |   14 +-
 packages/goal/goal/src/domain.ts                   |   32 +-
 packages/goal/goal/src/fold.ts                     |   65 +-
 packages/goal/goal/src/index.ts                    |  112 +-
 packages/goal/goal/src/render.ts                   |   21 -
 packages/goal/goal/src/types.ts                    |    2 +-
 packages/goal/goal/tests/goal.e2e.ts               |   25 +-
 packages/goal/goal/tests/goal.spec.ts              |  238 +--
 packages/goal/goal/tests/invariant.spec.ts         |   54 +-
 packages/goal/goal/tests/projection.spec.ts        |   78 +-
 packages/goal/tool-goal/README.i18n.yaml           |    4 +-
 packages/goal/tool-goal/README.md                  |    8 +-
 packages/goal/tool-goal/README.zh.md               |    8 +-
 packages/goal/tool-goal/src/authority.ts           |    3 +-
 packages/goal/tool-goal/src/index.ts               |    9 +-
 packages/goal/tool-goal/tests/tool-goal.spec.ts    |   45 +-
 packages/guard/repeat-tool-guard/README.i18n.yaml  |    4 +-
 packages/guard/repeat-tool-guard/README.md         |    2 +-
 packages/guard/repeat-tool-guard/README.zh.md      |    2 +-
 packages/guard/repeat-tool-guard/src/index.ts      |   11 +-
 .../tests/repeat-tool-guard.spec.ts                |   17 +-
 packages/hooks/hook-protocol/README.i18n.yaml      |    4 +-
 packages/hooks/hook-protocol/README.md             |    2 +-
 packages/hooks/hook-protocol/README.zh.md          |    2 +-
 packages/hooks/hook-protocol/src/types.ts          |    2 +-
 .../hooks/hook-protocol/tests/invariant.spec.ts    |    6 +-
 packages/hooks/hooks-claude/README.i18n.yaml       |    4 +-
 packages/hooks/hooks-claude/README.md              |    4 +-
 packages/hooks/hooks-claude/README.zh.md           |    4 +-
 packages/hooks/hooks-claude/src/index.ts           |   30 +-
 packages/hooks/hooks-claude/tests/bridge.spec.ts   |   24 +-
 .../hooks/hooks-claude/tests/coverage-cases.ts     |   28 +-
 packages/hooks/hooks-codex/README.i18n.yaml        |    4 +-
 packages/hooks/hooks-codex/README.md               |    4 +-
 packages/hooks/hooks-codex/README.zh.md            |    4 +-
 packages/hooks/hooks-codex/src/index.ts            |   36 +-
 packages/hooks/hooks-codex/tests/bridge.spec.ts    |    7 +-
 packages/hooks/hooks-codex/tests/coverage-cases.ts |   36 +-
 packages/host/README.i18n.yaml                     |    4 +-
 packages/host/README.md                            |    3 +-
 packages/host/README.zh.md                         |    3 +-
 packages/host/apiproxy/README.i18n.yaml            |    4 +-
 packages/host/apiproxy/README.md                   |   22 +-
 packages/host/apiproxy/README.zh.md                |   22 +-
 packages/host/apiproxy/src/api-proxy.ts            |  223 +--
 packages/host/apiproxy/src/api/events.schema.ts    |    6 +-
 packages/host/apiproxy/src/api/events.ts           |   10 +-
 packages/host/apiproxy/src/api/index.ts            |    3 +-
 packages/host/apiproxy/src/api/llm.schema.ts       |   29 +-
 packages/host/apiproxy/src/api/llm.ts              |   39 +
 packages/host/apiproxy/src/api/rpc-map.ts          |    1 +
 packages/host/apiproxy/src/api/rpc.schema.ts       |    1 +
 packages/host/apiproxy/src/api/rpc.ts              |   15 +-
 packages/host/apiproxy/src/api/sessions.schema.ts  |    8 +-
 packages/host/apiproxy/src/api/sessions.ts         |    4 +-
 packages/host/apiproxy/src/fetch/client.ts         |    5 +-
 packages/host/apiproxy/src/fetch/handler.ts        |    3 +-
 .../host/apiproxy/tests/api-proxy-approval.spec.ts |    8 +-
 .../host/apiproxy/tests/api-proxy-blank.spec.ts    |    2 +-
 .../host/apiproxy/tests/api-proxy-cold.spec.ts     |   75 +-
 .../host/apiproxy/tests/api-proxy-commands.spec.ts |  321 +---
 .../host/apiproxy/tests/api-proxy-config.spec.ts   |  110 ++
 .../host/apiproxy/tests/api-proxy-fork.spec.ts     |   11 +-
 .../host/apiproxy/tests/api-proxy-models.spec.ts   |    4 +-
 .../apiproxy/tests/api-proxy-projections.spec.ts   |   52 +-
 .../host/apiproxy/tests/api-proxy-rename.spec.ts   |    2 +-
 .../host/apiproxy/tests/api-proxy-search.spec.ts   |    4 +-
 .../host/apiproxy/tests/api-proxy-view.spec.ts     |   10 +-
 .../apiproxy/tests/api-proxy-workspace.spec.ts     |    9 +-
 .../host/apiproxy/tests/client-handler.spec.ts     |   19 +-
 packages/host/apiproxy/tests/fetch-carrier.spec.ts |    3 +
 packages/host/apiproxy/tests/rpc-schemas.spec.ts   |   88 +-
 .../tests/loader-composition.spec.ts               |   10 +-
 .../host/directory-picker-browse/README.i18n.yaml  |    4 +-
 packages/host/directory-picker-browse/README.md    |    2 +-
 packages/host/directory-picker-browse/README.zh.md |    2 +-
 .../directory-picker-browse/src/client/index.ts    |   29 +-
 .../tests/client-flow.spec.tsx                     |   25 +-
 .../host/directory-picker-native/README.i18n.yaml  |    4 +-
 packages/host/directory-picker-native/README.md    |    2 +-
 packages/host/directory-picker-native/README.zh.md |    2 +-
 .../directory-picker-native/src/client/index.ts    |   29 +-
 .../src/win32-dialog-logic.ts                      |    2 +-
 .../src/win32-dialog-worker.ts                     |    2 +-
 .../directory-picker-native/src/win32-dialog.ts    |    2 +-
 .../tests/client-flow.spec.tsx                     |   28 +-
 .../tests/win32-dialog-bindings.spec.ts            |    2 +-
 .../tests/win32-dialog-logic.spec.ts               |    2 +-
 packages/host/frontend-static/README.i18n.yaml     |    6 +
 packages/host/frontend-static/README.md            |   19 +
 packages/host/frontend-static/README.zh.md         |   19 +
 packages/host/frontend-static/package.json         |   41 +
 packages/host/frontend-static/src/index.ts         |  109 ++
 packages/host/frontend-static/src/invariant.ts     |   34 +
 .../frontend-static/tests/frontend-static.spec.ts  |  127 ++
 packages/host/frontend-static/tsconfig.json        |   27 +
 packages/host/webserver/README.i18n.yaml           |    4 +-
 packages/host/webserver/README.md                  |    7 +-
 packages/host/webserver/README.zh.md               |    7 +-
 packages/host/webserver/src/index.ts               |   73 +-
 packages/host/webserver/src/static.ts              |   60 -
 packages/host/webserver/tests/webserver.spec.ts    |   47 +-
 packages/llm/llm-deepseek/tests/adapter.spec.ts    |  188 +--
 .../llm/llm-deepseek/tests/dynamic-config.spec.ts  |    3 +-
 packages/llm/llm-pi-ai/README.i18n.yaml            |    4 +-
 packages/llm/llm-pi-ai/README.md                   |   74 +-
 packages/llm/llm-pi-ai/README.zh.md                |   74 +-
 packages/llm/llm-pi-ai/src/adapter.ts              |  202 ++-
 packages/llm/llm-pi-ai/src/catalog.ts              |  223 +++
 packages/llm/llm-pi-ai/src/config.ts               |  165 +-
 packages/llm/llm-pi-ai/src/discovery.ts            |  262 ++++
 packages/llm/llm-pi-ai/src/index.ts                |  180 ++-
 packages/llm/llm-pi-ai/src/provider.ts             |  191 +++
 packages/llm/llm-pi-ai/tests/adapter.spec.ts       |   70 +-
 packages/llm/llm-pi-ai/tests/catalog.spec.ts       |  576 +++++++
 packages/llm/llm-pi-ai/tests/discovery.spec.ts     |  313 ++++
 .../llm/llm-pi-ai/tests/dynamic-config.spec.ts     |   15 +-
 packages/llm/llm-pi-ai/tests/sdk-options.spec.ts   |   83 +-
 packages/llm/llm-retry/src/history.ts              |   19 +-
 packages/llm/llm-retry/src/index.ts                |   42 +-
 packages/llm/llm-retry/src/invariant.ts            |   85 +-
 packages/llm/llm-retry/tests/invariant.spec.ts     |  118 +-
 packages/llm/llm-retry/tests/persistence.spec.ts   |   13 +-
 packages/llm/llm-retry/tests/retry.spec.ts         |   62 +-
 .../llm/llm-retry/tests/transport-recovery.spec.ts |   41 +-
 packages/llm/llm/README.i18n.yaml                  |    4 +-
 packages/llm/llm/README.md                         |   15 +-
 packages/llm/llm/README.zh.md                      |   15 +-
 packages/llm/llm/src/adapter-failure.ts            |  110 +-
 packages/llm/llm/src/assembler.ts                  |   10 +-
 packages/llm/llm/src/error.ts                      |   13 +-
 packages/llm/llm/src/index.ts                      |  230 ++-
 packages/llm/llm/src/invariant.ts                  |    4 +-
 packages/llm/llm/src/message.ts                    |   84 +-
 packages/llm/llm/src/types.ts                      |   48 +-
 packages/llm/llm/tests/adapter-failure.spec.ts     |   68 +
 packages/llm/llm/tests/service.spec.ts             |  662 +++------
 packages/llm/llm/tests/topology.spec.ts            |   87 ++
 packages/llm/token-meter/README.i18n.yaml          |    4 +-
 packages/llm/token-meter/README.md                 |   12 +-
 packages/llm/token-meter/README.zh.md              |   12 +-
 packages/llm/token-meter/package.json              |    2 +
 .../llm/token-meter/src/breakdown-projection.ts    |   70 +
 packages/llm/token-meter/src/estimate.ts           |   87 ++
 packages/llm/token-meter/src/index.ts              |  124 +-
 packages/llm/token-meter/src/invariant.ts          |   11 +-
 packages/llm/token-meter/src/projection.ts         |   42 +-
 packages/llm/token-meter/src/surface-fold.ts       |   65 +
 packages/llm/token-meter/src/surface-projection.ts |   94 ++
 packages/llm/token-meter/src/types.ts              |    2 +-
 packages/llm/token-meter/src/usage-projection.ts   |   95 +-
 .../tests/context-breakdown-projection.spec.ts     |  309 ++++
 packages/llm/token-meter/tests/token-meter.spec.ts |    2 +-
 .../tests/token-usage-projection.spec.ts           |  135 +-
 packages/llm/token-meter/tsconfig.json             |    3 +
 packages/plan/plan-mode/README.i18n.yaml           |    4 +-
 packages/plan/plan-mode/README.md                  |    2 +-
 packages/plan/plan-mode/README.zh.md               |    2 +-
 packages/plan/plan-mode/src/index.ts               |   69 +-
 packages/plan/plan-mode/tests/integration.spec.ts  |   35 +-
 packages/plan/plan-mode/tests/invariant.spec.ts    |   11 +-
 packages/plan/plan-mode/tests/plan-mode.spec.ts    |  146 +-
 packages/plan/plan-mode/tests/projection.spec.ts   |    2 +-
 packages/pty/pty-local/tests/index.spec.ts         |   37 +-
 packages/pty/pty-local/tests/local.spec.ts         |   12 +-
 packages/pty/pty/tests/service.spec.ts             |   12 +-
 .../tests/loader-composition.spec.ts               |   12 +-
 .../pty/tool-bash-persistent/tests/tools.spec.ts   |   22 +-
 .../pty/tool-pty/tests/loader-composition.spec.ts  |   12 +-
 packages/pty/tool-pty/tests/tools.spec.ts          |   12 +-
 packages/sdk/sdk-client/README.i18n.yaml           |    4 +-
 packages/sdk/sdk-client/README.md                  |   12 +-
 packages/sdk/sdk-client/README.zh.md               |   12 +-
 packages/sdk/sdk-client/src/api.ts                 |   79 +-
 packages/sdk/sdk-client/src/client.ts              |   11 +-
 packages/sdk/sdk-client/src/index.ts               |    4 +-
 packages/sdk/sdk-client/src/types.ts               |   19 +-
 packages/sdk/sdk-client/tests/fake-runtime.ts      |   25 +-
 packages/sdk/sdk-client/tests/sdk-client.spec.ts   |  113 +-
 packages/sdk/sdk-protocol/README.i18n.yaml         |    4 +-
 packages/sdk/sdk-protocol/README.md                |    6 +-
 packages/sdk/sdk-protocol/README.zh.md             |    6 +-
 packages/sdk/sdk-protocol/src/index.ts             |    2 +-
 packages/sdk/sdk-protocol/src/types.ts             |   22 +-
 packages/sdk/sdk-protocol/tests/transport.spec.ts  |    4 +-
 .../session-checkpoint-policy/README.i18n.yaml     |    4 +-
 .../session-checkpoint-policy/README.md            |    4 +-
 .../session-checkpoint-policy/README.zh.md         |    4 +-
 .../session-checkpoint-policy/src/index.ts         |    5 +-
 .../tests/crash-recovery.e2e.ts                    |    5 +-
 .../tests/session-checkpoint-policy.spec.ts        |   10 +-
 .../session-persistence-jsonl/README.i18n.yaml     |    4 +-
 .../session-persistence-jsonl/README.md            |    5 +-
 .../session-persistence-jsonl/README.zh.md         |    5 +-
 .../session-persistence-jsonl/src/format.ts        |  217 +--
 .../session-persistence-jsonl/src/index.ts         |  216 ++-
 .../src/zstd-private-decoder.ts                    |  178 +++
 .../src/zstd-public-decoder.ts                     |   40 +
 .../session-persistence-jsonl/src/zstd.ts          |   29 +-
 .../session-persistence-jsonl/tests/jsonl.spec.ts  |  185 ++-
 .../tests/zstd.compat.spec.ts                      |   17 +-
 .../session-persistence-jsonl/tests/zstd.spec.ts   |  163 +-
 .../session-persistence-sqlite/README.i18n.yaml    |    4 +-
 .../session-persistence-sqlite/README.md           |    5 +-
 .../session-persistence-sqlite/README.zh.md        |    5 +-
 .../session-persistence-sqlite/src/index.ts        |   71 +-
 .../tests/sqlite.spec.ts                           |   99 +-
 .../session-persistence/README.i18n.yaml           |    4 +-
 .../session-persistence/README.md                  |   18 +-
 .../session-persistence/README.zh.md               |   20 +-
 .../session-persistence/src/coordinator.ts         |  647 ++++++--
 .../session-persistence/src/index.ts               |  104 +-
 .../session-persistence/src/preparations.ts        |  348 +++++
 .../session-persistence/tests/contract.ts          |   20 +-
 .../tests/coordinator-contract.ts                  |  419 +++++-
 .../session-persistence/tests/persistence.spec.ts  |  877 ++++++++++-
 .../session-persistence/tests/preparations.spec.ts |  360 +++++
 .../session-projection-cache/tests/cache.spec.ts   |    2 +-
 .../session-projection/tests/registry.spec.ts      |   10 +-
 .../session-query-sqlite/tests/sqlite.spec.ts      |    2 +-
 .../session-query/session-query/README.i18n.yaml   |    4 +-
 packages/session-query/session-query/README.md     |    2 +-
 packages/session-query/session-query/README.zh.md  |    2 +-
 packages/session-query/session-query/src/config.ts |    1 +
 packages/session-query/session-query/src/corpus.ts |    9 +-
 .../session-query/session-query/src/extraction.ts  |    6 +-
 .../session-query/tests/search-helpers.spec.ts     |   36 +-
 .../session-query/tests/session-query.spec.ts      |    8 +-
 .../session-query/tests/tracing.spec.ts            |    8 +-
 .../tool-session-query/src/service-boundary.ts     |    4 +
 .../tests/sqlite-integration.spec.ts               |    2 +-
 .../tests/tool-session-query.spec.ts               |    2 +-
 .../tests/provider.spec.ts                         |    4 +-
 .../tests/loader-composition.spec.ts               |    1 -
 .../tests/provider.e2e.ts                          |    1 -
 .../tests/provider.spec.ts                         |    2 +-
 .../session-title-llm/tests/llm.spec.ts            |    1 -
 .../session-title/tests/persistence.spec.ts        |    1 -
 .../session-title/tests/projection.spec.ts         |    2 +-
 .../session-title/tests/provider.spec.ts           |   10 -
 .../session-title/tests/rename.spec.ts             |   10 +-
 .../session-title/tests/service-contracts.spec.ts  |    4 -
 .../session-title/tests/session-title.spec.ts      |    3 -
 .../settings/settings-local/tests/local.spec.ts    |    5 +-
 packages/settings/settings/src/index.ts            |   55 +-
 packages/settings/settings/tests/settings.spec.ts  |   38 +
 packages/skill/tool-skill/README.i18n.yaml         |    4 +-
 packages/skill/tool-skill/README.md                |    8 +-
 packages/skill/tool-skill/README.zh.md             |    8 +-
 packages/skill/tool-skill/src/index.ts             |  184 ++-
 packages/skill/tool-skill/tests/tool-skill.spec.ts |  289 +++-
 packages/subagent/README.i18n.yaml                 |    4 +-
 packages/subagent/README.md                        |    2 +
 packages/subagent/README.zh.md                     |    2 +
 packages/subagent/subagent-acp/README.i18n.yaml    |    4 +-
 packages/subagent/subagent-acp/README.md           |    8 +-
 packages/subagent/subagent-acp/README.zh.md        |    8 +-
 packages/subagent/subagent-acp/package.json        |    2 +
 packages/subagent/subagent-acp/src/index.ts        |   12 +-
 packages/subagent/subagent-acp/src/run.ts          |   25 +-
 .../subagent-acp/tests/subagent-acp.spec.ts        |   41 +-
 packages/subagent/subagent-acp/tsconfig.json       |    3 +
 .../subagent/subagent-claude-code/README.i18n.yaml |    6 +
 packages/subagent/subagent-claude-code/README.md   |   96 ++
 .../subagent/subagent-claude-code/README.zh.md     |   96 ++
 .../subagent/subagent-claude-code/package.json     |   53 +
 .../subagent/subagent-claude-code/src/index.ts     |  107 ++
 .../subagent/subagent-claude-code/src/invariant.ts |   31 +
 .../subagent/subagent-claude-code/src/process.ts   |  156 ++
 packages/subagent/subagent-claude-code/src/run.ts  |  287 ++++
 .../tests/loader-composition.e2e.ts                |   72 +
 .../subagent-claude-code/tests/messages-fixture.ts |  150 ++
 .../tests/real-deepseek.e2e.ts                     |  160 ++
 .../tests/real-product.spec.ts                     |  272 ++++
 .../tests/subagent-claude-code.spec.ts             |  881 +++++++++++
 .../subagent/subagent-claude-code/tsconfig.json    |   37 +
 packages/subagent/subagent-codex/README.i18n.yaml  |    6 +
 packages/subagent/subagent-codex/README.md         |   90 ++
 packages/subagent/subagent-codex/README.zh.md      |   90 ++
 packages/subagent/subagent-codex/package.json      |   55 +
 packages/subagent/subagent-codex/src/index.ts      |  101 ++
 packages/subagent/subagent-codex/src/invariant.ts  |   30 +
 packages/subagent/subagent-codex/src/run.ts        |  200 +++
 packages/subagent/subagent-codex/src/wire.ts       |  374 +++++
 .../tests/deepseek-responses-bridge.ts             |  190 +++
 .../subagent-codex/tests/loader-composition.e2e.ts |   53 +
 .../subagent-codex/tests/real-deepseek.e2e.ts      |  141 ++
 .../subagent-codex/tests/real-product.spec.ts      |  225 +++
 .../subagent-codex/tests/responses-fixture.ts      |  288 ++++
 .../subagent-codex/tests/subagent-codex.spec.ts    | 1120 ++++++++++++++
 packages/subagent/subagent-codex/tsconfig.json     |   45 +
 .../subagent/subagent-dsh-sdk/README.i18n.yaml     |    4 +-
 packages/subagent/subagent-dsh-sdk/README.md       |    4 +-
 packages/subagent/subagent-dsh-sdk/README.zh.md    |    4 +-
 packages/subagent/subagent-dsh-sdk/src/run.ts      |    9 +-
 .../tests/subagent-dsh-sdk.spec.ts                 |   28 +-
 .../subagent/subagent-inprocess/README.i18n.yaml   |    4 +-
 packages/subagent/subagent-inprocess/README.md     |   20 +-
 packages/subagent/subagent-inprocess/README.zh.md  |   23 +-
 packages/subagent/subagent-inprocess/src/index.ts  |   12 +-
 .../tests/subagent-inprocess.spec.ts               |   16 +-
 packages/subagent/subagent-spawn/tests/harness.ts  |    2 +-
 .../subagent-spawn/tests/subagent-spawn.spec.ts    |   12 -
 packages/subagent/subagent/README.i18n.yaml        |    4 +-
 packages/subagent/subagent/README.md               |    2 +-
 packages/subagent/subagent/README.zh.md            |    2 +-
 packages/subagent/subagent/src/continuation.ts     |   57 +-
 packages/subagent/subagent/src/lifecycle.ts        |    1 -
 packages/subagent/subagent/src/list-children.ts    |   28 +-
 packages/subagent/subagent/src/out-of-process.ts   |   17 +-
 .../subagent/subagent/tests/continuation.spec.ts   |  104 +-
 .../subagent/subagent/tests/list-children.spec.ts  |   53 +-
 .../subagent/tool-subagent-control/src/index.ts    |    2 +-
 .../tests/tool-subagent-control.spec.ts            |    2 +-
 .../tests/tool-subagent-report.spec.ts             |   33 +-
 packages/subagent/tool-subagent/src/index.ts       |    4 +-
 packages/subprocess/subprocess-local/package.json  |    2 +
 packages/subprocess/subprocess-local/src/spawn.ts  |   71 +-
 .../subprocess-local/tests/spawn.spec.ts           |   93 +-
 packages/subprocess/subprocess-local/tsconfig.json |    3 +
 packages/subprocess/subprocess/README.i18n.yaml    |    4 +-
 packages/subprocess/subprocess/README.md           |    4 +-
 packages/subprocess/subprocess/README.zh.md        |    4 +-
 packages/subprocess/subprocess/src/types.ts        |   20 +-
 packages/support/acp-snapshot/src/harness.ts       |   86 +-
 .../support/acp-snapshot/tests/harness.spec.ts     |   97 +-
 packages/support/llm-replay/src/index.ts           |   19 +-
 .../support/llm-replay/tests/llm-replay.spec.ts    |   30 +-
 packages/tasks/tasks-local/tests/tasks.spec.ts     |   12 +-
 packages/tasks/tool-tasks/README.i18n.yaml         |    4 +-
 packages/tasks/tool-tasks/README.md                |    2 +-
 packages/tasks/tool-tasks/README.zh.md             |    2 +-
 packages/tasks/tool-tasks/src/index.ts             |   26 +-
 packages/tasks/tool-tasks/tests/tool-tasks.spec.ts |   16 +-
 .../session-telemetry-otel/tests/otel.spec.ts      |   12 +-
 .../telemetry/session-telemetry/src/coordinator.ts |    2 +-
 .../session-telemetry/tests/telemetry.spec.ts      |   14 +-
 packages/todo/tool-todo/tests/integration.spec.ts  |    2 +-
 packages/todo/tool-todo/tests/invariant.spec.ts    |    2 +-
 packages/todo/tool-todo/tests/projection.spec.ts   |    4 +-
 packages/typert/generator/src/analyzer.ts          |    4 +-
 .../tests/.generated-model-O7FJNT/host.mjs         |  310 ++++
 .../tests/.generated-model-qwn8sk/host.mjs         |  310 ++++
 packages/ui/app-boot/README.i18n.yaml              |    4 +-
 packages/ui/app-boot/README.md                     |   21 +-
 packages/ui/app-boot/README.zh.md                  |   21 +-
 packages/ui/app-boot/src/index.ts                  |  196 +--
 packages/ui/app-boot/src/profile.ts                |  388 +++++
 packages/ui/app-boot/tests/config-reload.spec.ts   |   28 +-
 packages/ui/app-boot/tests/profile.spec.ts         |  245 +++
 ...ersonal-config.spec.ts => user-patches.spec.ts} |  129 +-
 packages/ui/commands/tests/commands.spec.ts        |    2 +-
 packages/ui/jsonrpc/README.i18n.yaml               |    4 +-
 packages/ui/jsonrpc/README.md                      |    9 +-
 packages/ui/jsonrpc/README.zh.md                   |    9 +-
 packages/ui/jsonrpc/src/index.ts                   |   14 +-
 packages/ui/jsonrpc/src/server.ts                  |   44 +-
 packages/ui/jsonrpc/tests/plugin-apply.spec.ts     |   20 +-
 packages/ui/jsonrpc/tests/server.spec.ts           |  145 +-
 packages/ui/permission/src/index.ts                |   13 +-
 packages/ui/permission/tests/permission.spec.ts    |    2 +-
 packages/ui/permission/tests/projection.spec.ts    |   26 +-
 packages/ui/user-approval/src/index.ts             |   28 +-
 packages/ui/user-approval/tests/approval.spec.ts   |   45 +-
 packages/ui/user-approval/tests/invariant.spec.ts  |    6 +-
 822 files changed, 36025 insertions(+), 12241 deletions(-)
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
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 4 项匹配），建议确认所依赖的宿主面当日是否仍满足。
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
- 需适配：锚定 4832fffbc8963b8a7b1f8332e691083195bf94bc（未知（不同谱系））、补丁状态「CONFLICT（3 个补丁中 1 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
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
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-shell-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-skills-manager
- 关注：seam 或 peerDeps 存在不匹配（seam: 缺: tuiPrompt；peer: 无 dsh-* 依赖），建议确认所依赖的宿主面当日是否仍满足。
### dsh-skins
- 兼容：锚定 f1792735（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-subagent-tree
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
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
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-ui-whale
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
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
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dshx-update-check
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ex-setting
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### qqbot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### Qwen-MM-Plugins
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### Recall
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### review-panel
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### sandbox-mxc
- 需适配：锚定 93fe8cc2（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
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
- 需适配：锚定 a6fedc9e3b36d066e34860d040db6df47d88c432（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### web-components
- 需适配：锚定 b4b67f0（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
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
- 兼容：锚定 ce1fc03f95（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### repo-visibility-guard
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-grok-tui
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### ds_web_craw
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### fabric
- 需适配：锚定 4d3e1305d7f96c9b8e5842c71eab65b0ee7d36f5（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（9d84ab4）为新基线重新锚定/rebuild 补丁。
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

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
