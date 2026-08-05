# mainline 兼容性报告（2026-08-05）

- mainline：`bfb9136`（snapshots/20260805T134133Z）
- 上次对比：`02d755595816a6d384033c96fb67a1fda3b28228`
- 兼容性：54/57 无需适配，3 需适配（dsh-working-activity dsh-subagent-tree turtle-ui）；其中关注 0、占位 5、不适用 2

## 兼容性矩阵

| 仓库 | 锚定 | 补丁 | seam | peerDeps | 综合判定 |
|---|---|---|---|---|---|
| issues | 未知 | 不适用 | 不适用 | 不适用 | 不适用 |
| dsh-live-stats | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| dsh-working-activity | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 11 项匹配 | 兼容 |
| sandbox-mxc | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| web-components | 未知（不同谱系） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| dsh-opencode-server | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| toybox | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| ex-setting | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| tg-bot | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 12 项匹配 | 兼容 |
| group-chat-diary | 未知 | 不适用 | 不适用 | 不适用 | 不适用 |
| dsh-skins | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-coding-receipt | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| qqbot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-subagent-tree | 未知 | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 6 项匹配 | 需适配 |
| review-panel | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-github-integration | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| dsh-weixin-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| marisa | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-feishu-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-wecom-bot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| session-chatlog | 未知 | 无补丁 | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| distill | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| telegram | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| dsh-tool-browser | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-my-rsi | 未知（不同谱系） | OK（2 个补丁全部干净应用） | 缺: tuiPrompt | 26 项匹配 | 兼容 |
| dsh-win-port | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-desktop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-pty-windows | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-shell-windows | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| deepseek-harness-desktop | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| session-persistence-rdb | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| deepseek-harness-distro | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-tool-calculator | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dshx-update-check | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-acp | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-sfw | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-issue-filer | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-gh-bridge | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-vision | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-web-ui-approval-notify | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-agent-session-sources | 未知 | 无补丁 | 缺: tuiPrompt | 29 项匹配 | 兼容 |
| dsh-companion | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| hub | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-tool-json | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-skills-manager | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-pi-adapter | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| chat-width | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| dsh-memory-evolve | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-artifact | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| dsh-session-search | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| dsh-cordis-examples | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| dsh-web-terminal | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-ui-progress | 未知 | 无补丁 | 缺: tuiPrompt | 2 项匹配 | 兼容 |
| turtle-ui | 未知（不同谱系） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 21 项匹配 | 需适配 |
| dsh-cc-tui | 未知 | 无补丁 | 缺: tuiPrompt | 3 项匹配 | 兼容 |
| Qwen-MM-Plugins | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |

## mainline 变更分析（02d755595816a6d384033c96fb67a1fda3b28228 → bfb9136）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **workspace catalog 变更**：pnpm-workspace.yaml 增补条目（见 diffstat）。
- **包级变化**：packages/ 下删除 0 个包目录、新增 14 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：

新增文件：
```
packages/bash/bash-env/README.i18n.yaml
packages/bash/bash-env/README.md
packages/bash/bash-env/README.zh.md
packages/bash/bash-env/package.json
packages/bash/bash-env/src/index.ts
packages/bash/bash-env/src/invariant.ts
packages/bash/bash-env/tsconfig.json
packages/bash/bash-sandbox/tests/partial-landlock.spec.ts
packages/bash/pwsh-local/README.i18n.yaml
packages/bash/pwsh-local/README.md
packages/bash/pwsh-local/README.zh.md
packages/bash/pwsh-local/package.json
packages/bash/pwsh-local/src/index.ts
packages/bash/pwsh-local/src/invariant.ts
packages/bash/pwsh-local/src/resolve.ts
```

### seam 符号变化

| 符号 | prev 文件数 | cur 文件数 | 变化 |
|---|---|---|---|
| `ThemeService` | 26 | 26 | 存在 → 存在（稳定） |
| `settingsNamespace` | 16 | 16 | 存在 → 存在（稳定） |
| `sessionProjections` | 21 | 21 | 存在 → 存在（稳定） |
| `tuiPrompt` | 0 | 0 | 缺失 → 缺失 |
| `slots` | 15 | 15 | 存在 → 存在（稳定） |
| `session/event` | 48 | 48 | 存在 → 存在（稳定） |

### diffstat（packages/ patches/ workspace）

```
 packages/acp/README.i18n.yaml                      |   4 +-
 packages/acp/README.md                             |   2 +-
 packages/acp/README.zh.md                          |   2 +-
 packages/acp/acp/README.i18n.yaml                  |   4 +-
 packages/acp/acp/README.md                         |   2 +-
 packages/acp/acp/README.zh.md                      |   8 +-
 packages/acp/acp/package.json                      |   4 +-
 packages/bash/README.i18n.yaml                     |   4 +-
 packages/bash/README.md                            |  15 +-
 packages/bash/README.zh.md                         |  17 +-
 packages/bash/bash-env/README.i18n.yaml            |   6 +
 packages/bash/bash-env/README.md                   |  51 ++
 packages/bash/bash-env/README.zh.md                |  51 ++
 packages/bash/bash-env/package.json                |  48 ++
 packages/bash/bash-env/src/index.ts                | 217 +++++++
 packages/bash/bash-env/src/invariant.ts            |  30 +
 .../{tool-bash => bash-env}/tests/bash-env.spec.ts |  50 +-
 packages/bash/bash-env/tsconfig.json               |  36 ++
 packages/bash/bash-local/README.i18n.yaml          |   4 +-
 packages/bash/bash-local/README.md                 |  12 +-
 packages/bash/bash-local/README.zh.md              |  14 +-
 packages/bash/bash-local/package.json              |   4 +-
 packages/bash/bash-local/src/index.ts              |  59 +-
 packages/bash/bash-sandbox/README.i18n.yaml        |   4 +-
 packages/bash/bash-sandbox/README.md               |  12 +-
 packages/bash/bash-sandbox/README.zh.md            |  12 +-
 packages/bash/bash-sandbox/package.json            |   4 +-
 packages/bash/bash-sandbox/src/helpers.ts          |  91 ++-
 packages/bash/bash-sandbox/src/index.ts            | 109 ++--
 .../bash-sandbox/tests/partial-landlock.spec.ts    | 270 +++++++++
 packages/bash/bash-sandbox/tests/sandbox.spec.ts   | 369 +++++++++++-
 packages/bash/bash-sandbox/tests/seatbelt.e2e.ts   |  28 +-
 packages/bash/bash/README.i18n.yaml                |   4 +-
 packages/bash/bash/README.md                       |   2 +-
 packages/bash/bash/README.zh.md                    |   6 +-
 packages/bash/bash/package.json                    |   4 +-
 packages/bash/pwsh-local/README.i18n.yaml          |   6 +
 packages/bash/pwsh-local/README.md                 |  56 ++
 packages/bash/pwsh-local/README.zh.md              |  56 ++
 packages/bash/pwsh-local/package.json              |  45 ++
 packages/bash/pwsh-local/src/index.ts              | 288 ++++++++++
 packages/bash/pwsh-local/src/invariant.ts          |  30 +
 packages/bash/pwsh-local/src/resolve.ts            |  60 ++
 packages/bash/pwsh-local/tests/executor.spec.ts    | 454 +++++++++++++++
 packages/bash/pwsh-local/tsconfig.json             |  36 ++
 packages/bash/tool-bash/README.i18n.yaml           |   4 +-
 packages/bash/tool-bash/README.md                  |  27 +-
 packages/bash/tool-bash/README.zh.md               |  29 +-
 packages/bash/tool-bash/package.json               |  10 +-
 packages/bash/tool-bash/src/background.ts          |   8 +-
 packages/bash/tool-bash/src/index.ts               | 202 +------
 packages/bash/tool-bash/tests/integration.spec.ts  |   4 +-
 packages/bash/tool-bash/tests/tools.spec.ts        |  25 +-
 packages/bash/tool-bash/tsconfig.json              |   9 +-
 packages/bash/tool-pwsh/README.i18n.yaml           |   6 +
 packages/bash/tool-pwsh/README.md                  | 125 ++++
 packages/bash/tool-pwsh/README.zh.md               | 125 ++++
 packages/bash/tool-pwsh/package.json               |  57 ++
 packages/bash/tool-pwsh/src/background.ts          |  31 +
 packages/bash/tool-pwsh/src/index.ts               | 306 ++++++++++
 packages/bash/tool-pwsh/src/invariant.ts           |  30 +
 packages/bash/tool-pwsh/src/render.ts              |  81 +++
 packages/bash/tool-pwsh/tests/integration.spec.ts  | 154 +++++
 packages/bash/tool-pwsh/tests/loader.spec.ts       |  63 ++
 packages/bash/tool-pwsh/tests/tools.spec.ts        | 637 +++++++++++++++++++++
 packages/bash/tool-pwsh/tsconfig.json              |  45 ++
 packages/client/AGENTS.md                          |  10 +-
 packages/client/README.i18n.yaml                   |   4 +-
 packages/client/README.md                          |  61 +-
 packages/client/README.zh.md                       |  61 +-
 packages/client/connection/README.i18n.yaml        |   4 +-
 packages/client/connection/README.md               |  11 +-
 packages/client/connection/README.zh.md            |  11 +-
 packages/client/connection/package.json            |   4 +-
 packages/client/connection/src/client/fixture.ts   |   4 +
 packages/client/connection/src/index.ts            |   1 +
 packages/client/connection/tests/fake-api.ts       |   3 +-
 packages/client/connection/tests/node-half.spec.ts |   4 +-
 packages/client/hmr/README.i18n.yaml               |   4 +-
 packages/client/hmr/README.md                      |   4 +-
 packages/client/hmr/README.zh.md                   |   4 +-
 packages/client/hmr/package.json                   |   4 +-
 packages/client/locale/README.i18n.yaml            |   4 +-
 packages/client/locale/README.md                   |   2 +-
 packages/client/locale/README.zh.md                |   4 +-
 packages/client/locale/package.json                |   4 +-
 packages/client/modules/package.json               |   4 +-
 packages/client/runtime/README.i18n.yaml           |   4 +-
 packages/client/runtime/README.md                  |  10 +-
 packages/client/runtime/README.zh.md               |  10 +-
 packages/client/runtime/package.json               |   4 +-
 .../runtime/src/client/contract/session-history.ts |  16 +-
 packages/client/runtime/src/client/index.ts        |   4 +-
 .../src/client/session-history/history-fold.ts     |  65 ++-
 .../runtime/src/client/session-history/source.ts   |  75 ++-
 .../client/runtime/src/client/sessions/history.ts  |  59 ++
 .../client/runtime/src/client/sessions/lineage.ts  |  21 +-
 .../client/runtime/src/client/sessions/manager.ts  | 163 ++++--
 .../client/runtime/src/client/sessions/pending.ts  |   3 +
 .../src/client/sessions/request-inspection.ts      |   6 +-
 .../client/runtime/src/client/sessions/service.ts  |  10 +-
 .../src/client/sessions/transcript-adapter.ts      |   1 -
 .../runtime/src/client/workspaces/service.ts       |  12 +-
 packages/client/runtime/tests/fake-api.ts          |   3 +-
 packages/client/runtime/tests/history-fold.spec.ts |  64 +++
 packages/client/runtime/tests/manager.spec.ts      | 109 +++-
 .../runtime/tests/request-inspection.spec.ts       |  50 ++
 .../runtime/tests/session-history-source.spec.ts   |  29 +-
 .../runtime/tests/workspaces-service.spec.ts       |  27 +-
 packages/client/schema-form/README.i18n.yaml       |   4 +-
 packages/client/schema-form/README.md              |   6 +-
 packages/client/schema-form/README.zh.md           |   8 +-
 packages/client/schema-form/package.json           |   4 +-
 packages/client/test-runtime/README.i18n.yaml      |   4 +-
 packages/client/test-runtime/README.md             |   2 +-
 packages/client/test-runtime/README.zh.md          |   2 +-
 packages/client/test-runtime/package.json          |   4 +-
 packages/client/test-runtime/src/sessions.ts       |   1 -
 packages/client/tsdown.client.ts                   |   2 +-
 packages/client/ui-command/README.i18n.yaml        |   4 +-
 packages/client/ui-command/README.md               |   1 -
 packages/client/ui-command/README.zh.md            |   3 +-
 packages/client/ui-command/package.json            |   4 +-
 packages/client/ui-conversation/README.i18n.yaml   |   4 +-
 packages/client/ui-conversation/README.md          |  16 +-
 packages/client/ui-conversation/README.zh.md       |  10 +-
 packages/client/ui-conversation/package.json       |   4 +-
 .../src/client/contract/diff-card-model.ts         |   7 +-
 .../client/skeleton/ConversationRoot.module.css    |  13 +-
 .../tests/chat-code-subcalls.spec.tsx              |   2 +-
 .../tests/chat-stats-bash-sample.spec.tsx          |   2 +-
 .../ui-conversation/tests/coverage-tails.spec.tsx  |   2 +-
 .../ui-conversation/tests/diff-card.spec.tsx       |   4 +-
 .../ui-conversation/tests/read-card.spec.tsx       |   4 +-
 .../client/ui-conversation/tests/skeleton.spec.tsx |   4 +-
 .../ui-conversation/tests/terminal-card.spec.tsx   |   4 +-
 packages/client/ui-goal/README.i18n.yaml           |   4 +-
 packages/client/ui-goal/README.md                  |   2 +-
 packages/client/ui-goal/README.zh.md               |  12 +-
 packages/client/ui-goal/package.json               |   4 +-
 packages/client/ui-layout/README.i18n.yaml         |   4 +-
 packages/client/ui-layout/README.md                |   4 +-
 packages/client/ui-layout/README.zh.md             |  10 +-
 packages/client/ui-layout/package.json             |   4 +-
 packages/client/ui-model/README.i18n.yaml          |   4 +-
 packages/client/ui-model/README.md                 |   6 +-
 packages/client/ui-model/README.zh.md              |  12 +-
 packages/client/ui-model/package.json              |   4 +-
 .../ui-model/src/client/ModelSelect.module.css     |   7 +-
 .../client/ui-model/src/client/ModelSelect.tsx     |  14 +-
 packages/client/ui-model/src/client/index.ts       |   4 +-
 packages/client/ui-model/src/client/locales.ts     |  16 +-
 .../client/ui-model/tests/model-select.spec.tsx    |  23 +
 packages/client/ui-models/README.i18n.yaml         |   4 +-
 packages/client/ui-models/README.md                |   7 +-
 packages/client/ui-models/README.zh.md             |   9 +-
 packages/client/ui-models/package.json             |   4 +-
 .../ui-models/src/client/DeepSeekModelsEditor.tsx  | 364 ++++++++++++
 .../ui-models/src/client/ModelsSection.module.css  | 387 +++++++++++--
 .../client/ui-models/src/client/ProviderEditor.tsx |  55 +-
 packages/client/ui-models/src/client/locales.ts    |  42 ++
 .../client/ui-models/tests/components.spec.tsx     | 441 +++++++++++++-
 packages/client/ui-models/tests/store.spec.ts      |   5 +-
 packages/client/ui-models/tests/styles.spec.ts     |  31 +-
 packages/client/ui-permission/README.i18n.yaml     |   2 +-
 packages/client/ui-permission/README.zh.md         |   8 +-
 packages/client/ui-permission/package.json         |   4 +-
 .../ui-permission/tests/browser-plugin.spec.ts     |   2 +-
 .../ui-permission/tests/permission-row.spec.tsx    |  10 +-
 .../ui-permission/tests/settings-store.spec.ts     |  14 +-
 packages/client/ui-plan/README.i18n.yaml           |   2 +-
 packages/client/ui-plan/README.zh.md               |  10 +-
 packages/client/ui-plan/package.json               |   4 +-
 packages/client/ui-primitives/README.i18n.yaml     |   4 +-
 packages/client/ui-primitives/README.md            |   8 +-
 packages/client/ui-primitives/README.zh.md         |   8 +-
 packages/client/ui-primitives/package.json         |   9 +-
 packages/client/ui-primitives/src/StateDot.tsx     |   2 +-
 packages/client/ui-primitives/src/head-tail-cap.ts |   3 +-
 .../ui-primitives/src/markdown/MarkdownText.tsx    |   7 +-
 .../src/markdown/remarkMathCompatibility.ts        | 353 ++++++++++++
 .../client/ui-primitives/tests/markdown.spec.tsx   | 157 +++++
 packages/client/ui-question/README.i18n.yaml       |   2 +-
 packages/client/ui-question/README.zh.md           |   4 +-
 packages/client/ui-question/package.json           |   4 +-
 .../client/ui-settings-general/README.i18n.yaml    |   4 +-
 packages/client/ui-settings-general/README.md      |   4 +-
 packages/client/ui-settings-general/README.zh.md   |   4 +-
 packages/client/ui-settings-general/package.json   |   4 +-
 .../src/client/SettingsDocumentAction.module.css   |  16 +
 .../src/client/SettingsDocumentAction.tsx          |  50 ++
 .../client/ui-settings-general/src/client/index.ts |  39 +-
 .../ui-settings-general/src/client/locales.ts      |   4 +
 .../src/client/settings-document-store.ts          |  96 ++++
 .../client/ui-settings-general/src/invariant.ts    |   5 +-
 .../client/ui-settings-general/tests/apply.spec.ts |  48 +-
 .../ui-settings-general/tests/components.spec.tsx  |  97 +++-
 .../tests/settings-document-store.spec.ts          | 132 +++++
 .../tests/welcome-notice.spec.tsx                  |   1 +
 .../tests/welcome-store.spec.ts                    |  15 +-
 packages/client/ui-settings/README.i18n.yaml       |   4 +-
 packages/client/ui-settings/README.md              |   2 +-
 packages/client/ui-settings/README.zh.md           |   4 +-
 packages/client/ui-settings/package.json           |   4 +-
 .../ui-settings/src/client/SettingsRoot.module.css |  12 +-
 .../client/ui-settings/src/client/SettingsRoot.tsx |   1 +
 .../ui-settings/src/client/contract/slots.ts       |  17 +-
 packages/client/ui-settings/src/client/index.ts    |   1 +
 packages/client/ui-settings/tests/apply.spec.ts    |   7 +-
 .../ui-settings/tests/settings-root.spec.tsx       |   8 +
 packages/client/ui-sidebar/README.i18n.yaml        |   4 +-
 packages/client/ui-sidebar/README.md               |   6 +-
 packages/client/ui-sidebar/README.zh.md            |   6 +-
 packages/client/ui-sidebar/package.json            |   4 +-
 packages/client/ui-skill/README.i18n.yaml          |   2 +-
 packages/client/ui-skill/README.zh.md              |   8 +-
 packages/client/ui-skill/package.json              |   4 +-
 packages/client/ui-slash/README.i18n.yaml          |   4 +-
 packages/client/ui-slash/README.md                 |   2 +-
 packages/client/ui-slash/README.zh.md              |   4 +-
 packages/client/ui-slash/package.json              |   4 +-
 packages/client/ui-slots/README.i18n.yaml          |   2 +-
 packages/client/ui-slots/README.zh.md              |   2 +-
 packages/client/ui-slots/package.json              |   4 +-
 packages/client/ui-subagent/README.i18n.yaml       |   2 +-
 packages/client/ui-subagent/README.zh.md           |   8 +-
 packages/client/ui-subagent/package.json           |   4 +-
 .../ui-subagent/tests/conversation-ui.spec.tsx     |   2 -
 packages/client/ui-theme/README.i18n.yaml          |   2 +-
 packages/client/ui-theme/README.zh.md              |   2 +-
 packages/client/ui-theme/package.json              |   7 +-
 packages/client/ui-theme/tsdown.config.ts          |  10 +-
 packages/client/ui-trajectory/README.i18n.yaml     |   4 +-
 packages/client/ui-trajectory/README.md            |   4 +-
 packages/client/ui-trajectory/README.zh.md         |   4 +-
 packages/client/ui-trajectory/package.json         |  12 +-
 .../src/client/TrajectoryTable.module.css          |  81 ++-
 .../ui-trajectory/src/client/TrajectoryTable.tsx   | 531 ++++++++++++++---
 .../src/client/TrajectoryTimeline.module.css       |  40 ++
 .../src/client/TrajectoryTimeline.tsx              |  70 ++-
 .../ui-trajectory/src/client/TrajectoryView.tsx    | 285 +++++----
 .../ui-trajectory/src/client/context-branches.ts   |   7 +
 packages/client/ui-trajectory/src/client/index.ts  |   3 +-
 packages/client/ui-trajectory/src/client/layout.ts |  68 ++-
 .../client/ui-trajectory/src/client/timeline.ts    |   9 +-
 .../ui-trajectory/src/client/trajectory-record.ts  |  33 +-
 .../src/client/trajectory-virtual-rows.ts          |  83 +++
 packages/client/ui-trajectory/tests/cell.spec.tsx  |  32 +-
 .../ui-trajectory/tests/client-bundle.spec.ts      |   1 +
 .../ui-trajectory/tests/context-branches.spec.ts   |  12 +
 .../client/ui-trajectory/tests/layout.spec.tsx     |  70 ++-
 packages/client/ui-trajectory/tests/table.spec.tsx | 363 +++++++++++-
 packages/client/ui-trajectory/tests/views.spec.tsx | 174 +++++-
 .../ui-trajectory/tests/virtual-rows.spec.ts       |  95 +++
 packages/client/ui-workspace/README.i18n.yaml      |   4 +-
 packages/client/ui-workspace/README.md             |   8 +-
 packages/client/ui-workspace/README.zh.md          |   8 +-
 packages/client/ui-workspace/package.json          |   4 +-
 .../ui-workspace/src/client/WorkspaceBrowser.tsx   |   1 +
 packages/client/ui-workspace/src/client/locales.ts |   4 +
 .../client/ui-workspace/src/client/rows/Rows.tsx   |  39 +-
 packages/client/ui-workspace/src/client/tree.ts    |  14 +-
 packages/client/ui-workspace/tests/rows.spec.tsx   |  46 +-
 packages/client/ui-workspace/tests/tree.spec.ts    |  12 +-
 .../ui-workspace/tests/workspace-browser.spec.tsx  |   2 +-
 packages/client/web-react/README.i18n.yaml         |   4 +-
 packages/client/web-react/README.md                |   2 +-
 packages/client/web-react/README.zh.md             |   4 +-
 packages/client/web-react/package.json             |   4 +-
 packages/client/web/README.i18n.yaml               |   4 +-
 packages/client/web/README.md                      |   4 +-
 packages/client/web/README.zh.md                   |   4 +-
 packages/client/web/package.json                   |   4 +-
 packages/client/web/tests/base-styles.spec.ts      |  14 +-
 packages/code-runtime/README.i18n.yaml             |   4 +-
 packages/code-runtime/README.md                    |   6 +-
 packages/code-runtime/README.zh.md                 |  12 +-
 .../code-runtime-worker/README.i18n.yaml           |   4 +-
 .../code-runtime/code-runtime-worker/README.md     |   4 +-
 .../code-runtime/code-runtime-worker/README.zh.md  |   6 +-
 .../code-runtime/code-runtime-worker/package.json  |   4 +-
 .../code-runtime/code-runtime/README.i18n.yaml     |   2 +-
 packages/code-runtime/code-runtime/README.zh.md    |   2 +-
 packages/code-runtime/code-runtime/package.json    |   4 +-
 packages/compact/README.i18n.yaml                  |   4 +-
 packages/compact/README.md                         |  10 +-
 packages/compact/README.zh.md                      |  14 +-
 packages/compact/command-compact/README.i18n.yaml  |   4 +-
 packages/compact/command-compact/README.md         |   4 +-
 packages/compact/command-compact/README.zh.md      |   4 +-
 packages/compact/command-compact/package.json      |   4 +-
 .../command-compact/tests/command-compact.spec.ts  |   2 +-
 .../tests/loader-composition.spec.ts               |   2 +-
 packages/compact/compact-basic/README.i18n.yaml    |   4 +-
 packages/compact/compact-basic/README.md           |   1 -
 packages/compact/compact-basic/README.zh.md        |   5 +-
 packages/compact/compact-basic/package.json        |   4 +-
 .../compact-basic/tests/compact-basic.spec.ts      |  28 +-
 .../compact-basic/tests/compact-loop-repro.spec.ts |   2 +-
 .../compact-basic/tests/manual-compact.spec.ts     |  12 +-
 .../compact-tool-result-prune/README.i18n.yaml     |   2 +-
 .../compact/compact-tool-result-prune/README.zh.md |   2 +-
 .../compact/compact-tool-result-prune/package.json |   4 +-
 .../tests/tool-result-prune.spec.ts                |   8 +-
 packages/compact/compact/README.i18n.yaml          |   2 +-
 packages/compact/compact/README.zh.md              |   4 +-
 packages/compact/compact/package.json              |   4 +-
 packages/compact/compact/tests/compact.spec.ts     |   6 +-
 packages/compact/compact/tests/invariant.spec.ts   |  10 +-
 .../compact/compact/tests/tool-pairing.spec.ts     |  16 +-
 packages/context/README.i18n.yaml                  |   4 +-
 packages/context/README.md                         |  10 +-
 packages/context/README.zh.md                      |  14 +-
 .../context/session-reference/README.i18n.yaml     |   4 +-
 packages/context/session-reference/README.md       |   4 +-
 packages/context/session-reference/README.zh.md    |   4 +-
 packages/context/session-reference/package.json    |   4 +-
 .../tests/session-reference.spec.ts                |   2 +-
 packages/context/time-context/README.i18n.yaml     |   2 +-
 packages/context/time-context/README.zh.md         |   4 +-
 packages/context/time-context/package.json         |   4 +-
 .../context/time-context/tests/invariant.spec.ts   |   4 +-
 .../time-context/tests/time-context.spec.ts        |  28 +-
 packages/context/tmux-context/README.i18n.yaml     |   4 +-
 packages/context/tmux-context/README.md            |   2 +-
 packages/context/tmux-context/README.zh.md         |   6 +-
 packages/context/tmux-context/package.json         |   4 +-
 .../tmux-context/tests/tmux-context.spec.ts        |  30 +-
 packages/context/workspace-context/package.json    |   4 +-
 .../tests/workspace-context.spec.ts                |   2 +-
 packages/cordis/README.i18n.yaml                   |   4 +-
 packages/cordis/README.md                          |   4 +-
 packages/cordis/README.zh.md                       |  10 +-
 packages/cordis/repository-plugin/README.i18n.yaml |   4 +-
 packages/cordis/repository-plugin/README.md        |   4 +-
 packages/cordis/repository-plugin/README.zh.md     |  34 +-
 packages/cordis/repository-plugin/package.json     |   4 +-
 packages/cordis/tool-cordis/README.i18n.yaml       |   2 +-
 packages/cordis/tool-cordis/README.zh.md           |   6 +-
 packages/cordis/tool-cordis/package.json           |   4 +-
 packages/cordis/tool-cordis/src/api-catalog.ts     |  14 +-
 packages/core/README.i18n.yaml                     |   4 +-
 packages/core/README.md                            |  18 +-
 packages/core/README.zh.md                         |  24 +-
 packages/core/agent-loop/README.i18n.yaml          |   2 +-
 packages/core/agent-loop/README.zh.md              |  18 +-
 packages/core/agent-loop/package.json              |   4 +-
 packages/core/agent-loop/src/index.ts              |  44 +-
 packages/core/agent-loop/src/invariant.ts          |   2 +-
 .../agent-loop/tests/contract-regressions.spec.ts  |   4 +-
 .../tests/request-reconstruction.spec.ts           |   2 +-
 packages/core/agent-loop/tests/resume.spec.ts      |   2 +-
 packages/core/agent/README.i18n.yaml               |   2 +-
 packages/core/agent/README.zh.md                   |  14 +-
 packages/core/agent/package.json                   |   4 +-
 packages/core/agent/tests/agent.spec.ts            |   4 +-
 packages/core/scope/README.i18n.yaml               |   2 +-
 packages/core/scope/README.zh.md                   |   4 +-
 packages/core/scope/package.json                   |   4 +-
 packages/core/session/README.i18n.yaml             |   4 +-
 packages/core/session/README.md                    |  15 +-
 packages/core/session/README.zh.md                 |  25 +-
 packages/core/session/package.json                 |   4 +-
 packages/core/session/src/index.ts                 |  77 ++-
 packages/core/session/src/surface.ts               |  48 +-
 packages/core/session/tests/derived-cache.spec.ts  |  14 +-
 packages/core/session/tests/fork.spec.ts           |   4 +-
 packages/core/session/tests/properties.spec.ts     |   8 +-
 packages/core/session/tests/request-header.spec.ts |  20 +-
 packages/core/session/tests/session.spec.ts        | 170 +++---
 packages/core/session/tests/surface.spec.ts        |  94 ++-
 packages/core/system-prompt/README.i18n.yaml       |   2 +-
 packages/core/system-prompt/README.zh.md           |   4 +-
 packages/core/system-prompt/package.json           |   4 +-
 packages/core/tools/README.i18n.yaml               |   2 +-
 packages/core/tools/README.zh.md                   |  10 +-
 packages/core/tools/package.json                   |   4 +-
 packages/core/tools/tests/code-mode.spec.ts        |   4 +-
 packages/core/tools/tests/gen-tool-catalog.spec.ts |   2 +-
 packages/credentials/README.i18n.yaml              |   4 +-
 packages/credentials/README.md                     |  16 +-
 packages/credentials/README.zh.md                  |  16 +-
 .../credentials/credentials-local/README.i18n.yaml |   2 +-
 .../credentials/credentials-local/README.zh.md     |  28 +-
 .../credentials/credentials-local/package.json     |   4 +-
 packages/credentials/credentials/package.json      |   4 +-
 packages/examples/README.i18n.yaml                 |   4 +-
 packages/examples/README.md                        |  16 +-
 packages/examples/README.zh.md                     |  16 +-
 packages/examples/acp-demo/README.i18n.yaml        |   2 +-
 packages/examples/acp-demo/README.zh.md            |   2 +-
 packages/examples/acp-demo/package.json            |   4 +-
 .../examples/agent-spine-demo/README.i18n.yaml     |   4 +-
 packages/examples/agent-spine-demo/README.md       |   4 +-
 packages/examples/agent-spine-demo/README.zh.md    |   4 +-
 packages/examples/agent-spine-demo/package.json    |   6 +-
 packages/examples/agent-spine-demo/src/index.ts    |   4 +-
 packages/examples/agent-spine-demo/tsconfig.json   |   3 +
 packages/examples/cli-demo/README.i18n.yaml        |   2 +-
 packages/examples/cli-demo/README.zh.md            |   2 +-
 packages/examples/cli-demo/package.json            |   4 +-
 packages/examples/jsonrpc-demo/README.i18n.yaml    |   4 +-
 packages/examples/jsonrpc-demo/README.md           |   2 +-
 packages/examples/jsonrpc-demo/README.zh.md        |   4 +-
 packages/examples/jsonrpc-demo/package.json        |   4 +-
 packages/experimental/README.i18n.yaml             |   2 +-
 packages/experimental/README.zh.md                 |   2 +-
 packages/fs/README.i18n.yaml                       |   4 +-
 packages/fs/README.md                              |  22 +-
 packages/fs/README.zh.md                           |  26 +-
 packages/fs/fs-local/README.i18n.yaml              |   2 +-
 packages/fs/fs-local/README.zh.md                  |   4 +-
 packages/fs/fs-local/package.json                  |   4 +-
 packages/fs/fs-policy/README.i18n.yaml             |   2 +-
 packages/fs/fs-policy/README.zh.md                 |   6 +-
 packages/fs/fs-policy/package.json                 |   4 +-
 packages/fs/fs-sandbox/README.i18n.yaml            |   4 +-
 packages/fs/fs-sandbox/README.md                   |   2 +-
 packages/fs/fs-sandbox/README.zh.md                |   6 +-
 packages/fs/fs-sandbox/package.json                |   4 +-
 packages/fs/fs/README.i18n.yaml                    |   4 +-
 packages/fs/fs/README.md                           |  17 +-
 packages/fs/fs/README.zh.md                        |  19 +-
 packages/fs/fs/package.json                        |   4 +-
 packages/fs/tool-fs-search/README.i18n.yaml        |   2 +-
 packages/fs/tool-fs-search/README.zh.md            |  24 +-
 packages/fs/tool-fs-search/package.json            |   4 +-
 packages/fs/tool-fs/README.i18n.yaml               |   4 +-
 packages/fs/tool-fs/README.md                      |   2 +-
 packages/fs/tool-fs/README.zh.md                   |  14 +-
 packages/fs/tool-fs/package.json                   |   4 +-
 packages/fs/tool-str-replace-editor/package.json   |   4 +-
 .../fs/tool-str-replace-editor/tests/tools.spec.ts |   2 +-
 packages/goal/README.i18n.yaml                     |   4 +-
 packages/goal/README.md                            |   8 +-
 packages/goal/README.zh.md                         |   8 +-
 packages/goal/command-goal/README.i18n.yaml        |   4 +-
 packages/goal/command-goal/README.md               |   6 +-
 packages/goal/command-goal/README.zh.md            |   6 +-
 packages/goal/command-goal/package.json            |   4 +-
 packages/goal/goal-session/README.i18n.yaml        |   2 +-
 packages/goal/goal-session/README.zh.md            |   6 +-
 packages/goal/goal-session/package.json            |   4 +-
 packages/goal/goal/README.i18n.yaml                |   2 +-
 packages/goal/goal/README.zh.md                    |   4 +-
 packages/goal/goal/package.json                    |   4 +-
 packages/goal/goal/tests/goal.spec.ts              |  24 +-
 packages/goal/tool-goal/README.i18n.yaml           |   2 +-
 packages/goal/tool-goal/README.zh.md               |   8 +-
 packages/goal/tool-goal/package.json               |   4 +-
 packages/goal/tool-goal/tests/tool-goal.spec.ts    |   4 +-
 packages/guard/README.i18n.yaml                    |   4 +-
 packages/guard/README.md                           |   6 +-
 packages/guard/README.zh.md                        |  10 +-
 packages/guard/repeat-tool-guard/README.i18n.yaml  |   4 +-
 packages/guard/repeat-tool-guard/README.md         |   4 -
 packages/guard/repeat-tool-guard/README.zh.md      |  10 +-
 packages/guard/repeat-tool-guard/package.json      |   4 +-
 packages/hooks/README.i18n.yaml                    |   4 +-
 packages/hooks/README.md                           |   8 +-
 packages/hooks/README.zh.md                        |  12 +-
 packages/hooks/hook-protocol/package.json          |   4 +-
 packages/hooks/hook-protocol/tests/events.spec.ts  |  16 +-
 .../hooks/hook-protocol/tests/invariant.spec.ts    |   2 +-
 packages/hooks/hooks-claude/README.i18n.yaml       |   2 +-
 packages/hooks/hooks-claude/README.zh.md           |   4 +-
 packages/hooks/hooks-claude/package.json           |   4 +-
 packages/hooks/hooks-codex/README.i18n.yaml        |   2 +-
 packages/hooks/hooks-codex/README.zh.md            |   4 +-
 packages/hooks/hooks-codex/package.json            |   4 +-
 packages/host/README.i18n.yaml                     |   4 +-
 packages/host/README.md                            |  14 +-
 packages/host/README.zh.md                         |  20 +-
 packages/host/apiproxy/README.i18n.yaml            |   4 +-
 packages/host/apiproxy/README.md                   |  14 +-
 packages/host/apiproxy/README.zh.md                |  32 +-
 packages/host/apiproxy/package.json                |   4 +-
 packages/host/apiproxy/src/api-proxy.ts            | 149 +++--
 packages/host/apiproxy/src/api/llm.ts              |   4 +-
 packages/host/apiproxy/src/api/rpc-map.ts          |   1 +
 packages/host/apiproxy/src/api/sessions.schema.ts  |   1 -
 packages/host/apiproxy/src/api/sessions.ts         |   2 -
 packages/host/apiproxy/src/api/settings.schema.ts  |   9 +
 packages/host/apiproxy/src/api/settings.ts         |  22 +-
 packages/host/apiproxy/src/fetch/client.ts         |   6 +-
 packages/host/apiproxy/src/fetch/handler.ts        |   9 +-
 packages/host/apiproxy/src/native-path-opener.ts   |  46 +-
 .../host/apiproxy/tests/api-proxy-config.spec.ts   |  90 ++-
 .../host/apiproxy/tests/api-proxy-models.spec.ts   |  13 +-
 .../host/apiproxy/tests/client-handler.spec.ts     |  17 +-
 packages/host/apiproxy/tests/fetch-carrier.spec.ts |   5 +-
 .../host/apiproxy/tests/native-path-opener.spec.ts |  28 +-
 packages/host/apiproxy/tests/rpc-schemas.spec.ts   |   1 -
 .../host/directory-picker-auto/README.i18n.yaml    |   4 +-
 packages/host/directory-picker-auto/README.md      |   2 +-
 packages/host/directory-picker-auto/README.zh.md   |   6 +-
 packages/host/directory-picker-auto/package.json   |   4 +-
 .../host/directory-picker-browse/README.i18n.yaml  |   4 +-
 packages/host/directory-picker-browse/README.md    |   2 +-
 packages/host/directory-picker-browse/README.zh.md |  14 +-
 packages/host/directory-picker-browse/package.json |   4 +-
 .../host/directory-picker-native/README.i18n.yaml  |   4 +-
 packages/host/directory-picker-native/README.md    |   3 +-
 packages/host/directory-picker-native/README.zh.md |   3 +-
 packages/host/directory-picker-native/package.json |  15 +-
 packages/host/directory-picker-native/src/index.ts |   7 +-
 .../directory-picker-native/src/native-picker.ts   |  24 +-
 .../src/win32-dialog-bindings.ts                   | 195 +++++++
 .../src/win32-dialog-host.ts                       |  33 ++
 .../src/win32-dialog-logic.ts                      | 132 +++++
 .../src/win32-dialog-worker.ts                     |  52 ++
 .../directory-picker-native/src/win32-dialog.ts    | 159 +++++
 .../tests/built-worker.e2e.ts                      |  34 ++
 .../tests/native-picker.spec.ts                    |  86 ++-
 .../tests/win32-dialog-bindings.spec.ts            | 354 ++++++++++++
 .../tests/win32-dialog-logic.spec.ts               |  98 ++++
 .../tests/win32-dialog.spec.ts                     | 163 ++++++
 .../host/directory-picker-native/tsdown.config.ts  |  19 +-
 packages/host/directory-picker/README.i18n.yaml    |   2 +-
 packages/host/directory-picker/README.zh.md        |  10 +-
 packages/host/directory-picker/package.json        |   4 +-
 packages/host/webserver/package.json               |   4 +-
 packages/llm/README.i18n.yaml                      |   4 +-
 packages/llm/README.md                             |  12 +-
 packages/llm/README.zh.md                          |  16 +-
 packages/llm/llm-deepseek/README.i18n.yaml         |   4 +-
 packages/llm/llm-deepseek/README.md                |   8 +-
 packages/llm/llm-deepseek/README.zh.md             |  10 +-
 packages/llm/llm-deepseek/package.json             |   4 +-
 packages/llm/llm-deepseek/src/adapter.ts           |   4 +-
 packages/llm/llm-deepseek/src/index.ts             |  10 +-
 packages/llm/llm-deepseek/tests/adapter.spec.ts    |  20 +
 packages/llm/llm-pi-ai/README.i18n.yaml            |   4 +-
 packages/llm/llm-pi-ai/README.md                   |   4 -
 packages/llm/llm-pi-ai/README.zh.md                |   6 +-
 packages/llm/llm-pi-ai/package.json                |   4 +-
 packages/llm/llm-retry/README.i18n.yaml            |   4 +-
 packages/llm/llm-retry/README.md                   |   2 +-
 packages/llm/llm-retry/README.zh.md                |   2 +-
 packages/llm/llm-retry/package.json                |   4 +-
 packages/llm/llm/README.i18n.yaml                  |   2 +-
 packages/llm/llm/README.zh.md                      |   4 +-
 packages/llm/llm/package.json                      |   4 +-
 packages/llm/token-meter/README.i18n.yaml          |   4 +-
 packages/llm/token-meter/README.md                 |   5 +-
 packages/llm/token-meter/README.zh.md              |   7 +-
 packages/llm/token-meter/package.json              |   4 +-
 packages/llm/token-meter/src/index.ts              |   4 +-
 packages/llm/token-meter/src/projection.ts         |   3 +-
 packages/llm/token-meter/tests/token-meter.spec.ts |  48 +-
 packages/lsp/README.i18n.yaml                      |   4 +-
 packages/lsp/README.md                             |  10 +-
 packages/lsp/README.zh.md                          |  12 +-
 packages/lsp/lsp-local/README.i18n.yaml            |   4 +-
 packages/lsp/lsp-local/README.md                   |   2 +-
 packages/lsp/lsp-local/README.zh.md                |   4 +-
 packages/lsp/lsp-local/package.json                |   4 +-
 packages/lsp/lsp/README.i18n.yaml                  |   2 +-
 packages/lsp/lsp/README.zh.md                      |   4 +-
 packages/lsp/lsp/package.json                      |   4 +-
 packages/lsp/tool-lsp/README.i18n.yaml             |   2 +-
 packages/lsp/tool-lsp/README.zh.md                 |   2 +-
 packages/lsp/tool-lsp/package.json                 |   4 +-
 packages/mcp/README.i18n.yaml                      |   6 +-
 packages/mcp/README.md                             |   2 +-
 packages/mcp/README.zh.md                          |   8 +-
 packages/mcp/mcp-client/package.json               |   4 +-
 packages/plan/README.i18n.yaml                     |   4 +-
 packages/plan/README.md                            |   6 +-
 packages/plan/README.zh.md                         |   6 +-
 packages/plan/plan-mode/README.i18n.yaml           |   4 +-
 packages/plan/plan-mode/README.md                  |   5 +-
 packages/plan/plan-mode/README.zh.md               |  41 +-
 packages/plan/plan-mode/package.json               |   4 +-
 packages/plan/plan-mode/tests/invariant.spec.ts    |   6 +-
 packages/plan/plan-mode/tests/plan-mode.spec.ts    |   6 +-
 packages/pty/README.i18n.yaml                      |   4 +-
 packages/pty/README.md                             |  12 +-
 packages/pty/README.zh.md                          |  12 +-
 packages/pty/pty-local/package.json                |   7 +-
 .../{src => scripts}/ensure-spawn-helper.mjs       |   0
 packages/pty/pty-local/tests/index.spec.ts         |   6 +-
 packages/pty/pty-local/tests/local.spec.ts         |   4 +-
 packages/pty/pty/README.i18n.yaml                  |   2 +-
 packages/pty/pty/README.zh.md                      |   2 +-
 packages/pty/pty/package.json                      |   4 +-
 packages/pty/pty/tests/service.spec.ts             |   2 +-
 packages/pty/tool-bash-persistent/package.json     |   4 +-
 .../tests/loader-composition.spec.ts               |   4 +-
 .../pty/tool-bash-persistent/tests/tools.spec.ts   |   2 +-
 packages/pty/tool-pty/package.json                 |   4 +-
 .../pty/tool-pty/tests/loader-composition.spec.ts  |   4 +-
 packages/pty/tool-pty/tests/tools.spec.ts          |   2 +-
 packages/sandbox/README.i18n.yaml                  |   4 +-
 packages/sandbox/README.md                         |  12 +-
 packages/sandbox/README.zh.md                      |  12 +-
 packages/sandbox/sandbox-local/README.i18n.yaml    |   4 +-
 packages/sandbox/sandbox-local/README.md           |  10 +-
 packages/sandbox/sandbox-local/README.zh.md        |  10 +-
 packages/sandbox/sandbox-local/package.json        |   4 +-
 packages/sandbox/sandbox-local/src/index.ts        |  67 ++-
 packages/sandbox/sandbox-local/tests/local.spec.ts |  43 +-
 packages/sandbox/sandbox-policy/package.json       |   4 +-
 .../sandbox/sandbox-policy/tests/policy.spec.ts    |   8 +-
 packages/sandbox/sandbox/README.i18n.yaml          |   4 +-
 packages/sandbox/sandbox/README.md                 |   3 +-
 packages/sandbox/sandbox/README.zh.md              |   9 +-
 packages/sandbox/sandbox/package.json              |   4 +-
 packages/sandbox/sandbox/src/index.ts              |  23 +-
 packages/sdk/README.i18n.yaml                      |   4 +-
 packages/sdk/README.md                             |  19 +-
 packages/sdk/README.zh.md                          |  21 +-
 packages/sdk/create-sdk/package.json               |   4 +-
 packages/sdk/helper/package.json                   |   4 +-
 packages/sdk/helper/src/features/builtin/index.ts  |   1 +
 .../sdk/helper/src/project/project-edit-session.ts |   4 +-
 packages/sdk/scripts/package.json                  |   6 +-
 packages/sdk/scripts/src/config/config-workflow.ts |   2 +-
 packages/sdk/sdk-client/README.i18n.yaml           |   4 +-
 packages/sdk/sdk-client/README.md                  |   6 +-
 packages/sdk/sdk-client/README.zh.md               |   8 +-
 packages/sdk/sdk-client/package.json               |   4 +-
 packages/sdk/sdk-protocol/README.i18n.yaml         |   2 +-
 packages/sdk/sdk-protocol/README.zh.md             |   2 +-
 packages/sdk/sdk-protocol/package.json             |   4 +-
 packages/sdk/telemetry/README.i18n.yaml            |   2 +-
 packages/sdk/telemetry/README.zh.md                |   2 +-
 packages/sdk/telemetry/package.json                |   4 +-
 packages/session-persistence/README.i18n.yaml      |   4 +-
 packages/session-persistence/README.md             |  12 +-
 packages/session-persistence/README.zh.md          |  12 +-
 .../session-checkpoint-policy/package.json         |   4 +-
 .../session-persistence-jsonl/README.i18n.yaml     |   4 +-
 .../session-persistence-jsonl/README.md            |   2 +-
 .../session-persistence-jsonl/README.zh.md         |   8 +-
 .../session-persistence-jsonl/package.json         |   4 +-
 .../session-persistence-sqlite/package.json        |   4 +-
 .../session-persistence/README.i18n.yaml           |   4 +-
 .../session-persistence/README.md                  |   6 -
 .../session-persistence/README.zh.md               |  42 +-
 .../session-persistence/package.json               |   4 +-
 .../session-persistence/tests/contract.ts          |   2 +-
 .../tests/coordinator-contract.ts                  |   2 +-
 packages/session-projection/README.i18n.yaml       |   4 +-
 packages/session-projection/README.md              |  10 +-
 packages/session-projection/README.zh.md           |  10 +-
 .../session-projection-cache/README.i18n.yaml      |   2 +-
 .../session-projection-cache/README.zh.md          |  16 +-
 .../session-projection-cache/package.json          |   4 +-
 .../session-projection/README.i18n.yaml            |   4 +-
 .../session-projection/README.md                   |   2 +-
 .../session-projection/README.zh.md                |  10 +-
 .../session-projection/package.json                |   4 +-
 .../session-projection/src/index.ts                |   4 +-
 packages/session-query/README.i18n.yaml            |   4 +-
 packages/session-query/README.md                   |  10 +-
 packages/session-query/README.zh.md                |  12 +-
 .../session-query-sqlite/README.i18n.yaml          |   2 +-
 .../session-query-sqlite/README.zh.md              |   2 +-
 .../session-query-sqlite/package.json              |   4 +-
 .../session-query/session-query/README.i18n.yaml   |   2 +-
 packages/session-query/session-query/README.zh.md  |   2 +-
 packages/session-query/session-query/package.json  |   4 +-
 packages/session-query/session-query/src/index.ts  |   2 +-
 .../tool-session-query/README.i18n.yaml            |   2 +-
 .../session-query/tool-session-query/README.zh.md  |   2 +-
 .../session-query/tool-session-query/package.json  |   4 +-
 packages/session-title/README.i18n.yaml            |   4 +-
 packages/session-title/README.md                   |  12 +-
 packages/session-title/README.zh.md                |  16 +-
 .../session-title-all-messages-llm/package.json    |   2 +-
 .../tests/provider.spec.ts                         |   2 +-
 .../session-title-first-message-llm/package.json   |   2 +-
 .../tests/provider.spec.ts                         |   2 +-
 .../session-title-llm/README.i18n.yaml             |   2 +-
 .../session-title/session-title-llm/README.zh.md   |   2 +-
 .../session-title/session-title-llm/package.json   |   4 +-
 .../session-title/session-title/README.i18n.yaml   |   2 +-
 packages/session-title/session-title/README.zh.md  |   2 +-
 packages/session-title/session-title/package.json  |   4 +-
 .../session-title/tests/rename.spec.ts             |   2 +-
 .../session-title/tests/service-contracts.spec.ts  |   4 +-
 .../session-title/tests/session-title.spec.ts      |   2 +-
 packages/settings/README.i18n.yaml                 |   4 +-
 packages/settings/README.md                        |   8 +-
 packages/settings/README.zh.md                     |  12 +-
 packages/settings/settings-local/README.i18n.yaml  |   4 +-
 packages/settings/settings-local/README.md         |   3 +-
 packages/settings/settings-local/README.zh.md      |   9 +-
 packages/settings/settings-local/package.json      |   4 +-
 packages/settings/settings-local/src/index.ts      |  84 ++-
 .../settings/settings-local/tests/local.spec.ts    |  28 +-
 .../settings-local/tests/lock-race.spec.ts         |  60 ++
 packages/settings/settings/README.i18n.yaml        |   4 +-
 packages/settings/settings/README.md               |   4 +-
 packages/settings/settings/README.zh.md            |  12 +-
 packages/settings/settings/package.json            |   4 +-
 packages/settings/settings/src/index.ts            |  21 +
 packages/settings/settings/tests/settings.spec.ts  |   8 +
 packages/skill/README.i18n.yaml                    |   4 +-
 packages/skill/README.md                           |  12 +-
 packages/skill/README.zh.md                        |  12 +-
 packages/skill/skill-local/README.i18n.yaml        |   2 +-
 packages/skill/skill-local/README.zh.md            |  12 +-
 packages/skill/skill-local/package.json            |   4 +-
 packages/skill/skill/README.i18n.yaml              |   2 +-
 packages/skill/skill/README.zh.md                  |   2 +-
 packages/skill/skill/package.json                  |   4 +-
 packages/skill/tool-skill/README.i18n.yaml         |   2 +-
 packages/skill/tool-skill/README.zh.md             |   6 +-
 packages/skill/tool-skill/package.json             |   4 +-
 packages/skill/tool-skill/tests/tool-skill.spec.ts |  18 +-
 packages/spill/README.i18n.yaml                    |   4 +-
 packages/spill/README.md                           |  14 +-
 packages/spill/README.zh.md                        |  14 +-
 packages/spill/spill-local/README.i18n.yaml        |   2 +-
 packages/spill/spill-local/README.zh.md            |   2 +-
 packages/spill/spill-local/package.json            |   4 +-
 packages/spill/spill-policy/README.i18n.yaml       |   2 +-
 packages/spill/spill-policy/README.zh.md           |   4 +-
 packages/spill/spill-policy/package.json           |   4 +-
 packages/spill/spill/README.i18n.yaml              |   2 +-
 packages/spill/spill/README.zh.md                  |   4 +-
 packages/spill/spill/package.json                  |   4 +-
 packages/storage/README.i18n.yaml                  |   4 +-
 packages/storage/README.md                         |  12 +-
 packages/storage/README.zh.md                      |  14 +-
 packages/storage/storage-domain/README.i18n.yaml   |   2 +-
 packages/storage/storage-domain/README.zh.md       |   4 +-
 packages/storage/storage-domain/package.json       |   4 +-
 packages/storage/storage-json/README.i18n.yaml     |   2 +-
 packages/storage/storage-json/README.zh.md         |   2 +-
 packages/storage/storage-json/package.json         |   4 +-
 packages/storage/storage-sqlite/README.i18n.yaml   |   2 +-
 packages/storage/storage-sqlite/README.zh.md       |   4 +-
 packages/storage/storage-sqlite/package.json       |   4 +-
 packages/storage/storage/README.i18n.yaml          |   4 +-
 packages/storage/storage/README.md                 |  15 +-
 packages/storage/storage/README.zh.md              |  15 +-
 packages/storage/storage/package.json              |   4 +-
 packages/subagent/README.i18n.yaml                 |   4 +-
 packages/subagent/README.md                        |  24 +-
 packages/subagent/README.zh.md                     |  26 +-
 packages/subagent/subagent-acp/README.i18n.yaml    |   4 +-
 packages/subagent/subagent-acp/README.md           |   3 -
 packages/subagent/subagent-acp/README.zh.md        |   9 +-
 packages/subagent/subagent-acp/package.json        |   4 +-
 .../subagent/subagent-dsh-sdk/README.i18n.yaml     |   4 +-
 packages/subagent/subagent-dsh-sdk/README.md       |   2 -
 packages/subagent/subagent-dsh-sdk/README.zh.md    |   6 +-
 packages/subagent/subagent-dsh-sdk/package.json    |   4 +-
 packages/subagent/subagent-fork/README.i18n.yaml   |   2 +-
 packages/subagent/subagent-fork/README.zh.md       |   4 +-
 packages/subagent/subagent-fork/package.json       |   4 +-
 .../subagent/subagent-inprocess/README.i18n.yaml   |   2 +-
 packages/subagent/subagent-inprocess/README.zh.md  |  18 +-
 packages/subagent/subagent-inprocess/package.json  |   4 +-
 packages/subagent/subagent-spawn/README.i18n.yaml  |   2 +-
 packages/subagent/subagent-spawn/README.zh.md      |   6 +-
 packages/subagent/subagent-spawn/package.json      |   4 +-
 packages/subagent/subagent-spawn/tests/harness.ts  |   2 +
 packages/subagent/subagent/README.i18n.yaml        |   4 +-
 packages/subagent/subagent/README.md               |  16 +-
 packages/subagent/subagent/README.zh.md            |  38 +-
 packages/subagent/subagent/package.json            |   4 +-
 packages/subagent/subagent/src/descriptor-seed.ts  |   2 +-
 .../tool-subagent-control/README.i18n.yaml         |   2 +-
 .../subagent/tool-subagent-control/README.zh.md    |  10 +-
 .../subagent/tool-subagent-control/package.json    |   4 +-
 .../subagent/tool-subagent-report/README.i18n.yaml |   2 +-
 .../subagent/tool-subagent-report/README.zh.md     |  10 +-
 .../subagent/tool-subagent-report/package.json     |   4 +-
 packages/subagent/tool-subagent/README.i18n.yaml   |   2 +-
 packages/subagent/tool-subagent/README.zh.md       |  16 +-
 packages/subagent/tool-subagent/package.json       |   4 +-
 packages/subprocess/README.i18n.yaml               |   4 +-
 packages/subprocess/README.md                      |  10 +-
 packages/subprocess/README.zh.md                   |  10 +-
 .../subprocess/subprocess-local/README.i18n.yaml   |   4 +-
 packages/subprocess/subprocess-local/README.md     |   4 +-
 packages/subprocess/subprocess-local/README.zh.md  |   6 +-
 packages/subprocess/subprocess-local/package.json  |   4 +-
 packages/subprocess/subprocess/README.i18n.yaml    |   2 +-
 packages/subprocess/subprocess/README.zh.md        |   2 +-
 packages/subprocess/subprocess/package.json        |   4 +-
 packages/subprocess/subprocess/src/index.ts        |   7 +-
 .../subprocess/subprocess/tests/service.spec.ts    |   5 +-
 packages/support/README.i18n.yaml                  |   4 +-
 packages/support/README.md                         |  22 +-
 packages/support/README.zh.md                      |  22 +-
 packages/support/acp-snapshot/README.i18n.yaml     |   4 +-
 packages/support/acp-snapshot/README.md            |   4 +-
 packages/support/acp-snapshot/README.zh.md         |   4 +-
 packages/support/acp-snapshot/package.json         |   4 +-
 packages/support/acp-snapshot/src/suite.ts         |  28 +-
 packages/support/acp-snapshot/tests/suite.spec.ts  |   8 +
 packages/support/agent-loop-testkit/package.json   |   4 +-
 packages/support/invariants/README.i18n.yaml       |   2 +-
 packages/support/invariants/README.zh.md           |   2 +-
 packages/support/invariants/package.json           |   4 +-
 packages/support/llm-mock-server/README.i18n.yaml  |   2 +-
 packages/support/llm-mock-server/README.zh.md      |  34 +-
 packages/support/llm-mock-server/package.json      |   4 +-
 packages/support/llm-replay/README.i18n.yaml       |   4 +-
 packages/support/llm-replay/README.md              |   2 +-
 packages/support/llm-replay/README.zh.md           |  16 +-
 packages/support/llm-replay/package.json           |   4 +-
 packages/support/loader-smoke/package.json         |   4 +-
 packages/tasks/README.i18n.yaml                    |   4 +-
 packages/tasks/README.md                           |  14 +-
 packages/tasks/README.zh.md                        |  12 +-
 packages/tasks/tasks-local/package.json            |   4 +-
 packages/tasks/tasks-local/tests/tasks.spec.ts     |   2 +-
 packages/tasks/tasks/README.i18n.yaml              |   2 +-
 packages/tasks/tasks/README.zh.md                  |   2 +-
 packages/tasks/tasks/package.json                  |   4 +-
 packages/tasks/tool-tasks/package.json             |   4 +-
 packages/telemetry/README.i18n.yaml                |   4 +-
 packages/telemetry/README.md                       |  10 +-
 packages/telemetry/README.zh.md                    |  12 +-
 .../session-telemetry-otel/README.i18n.yaml        |   4 +-
 .../telemetry/session-telemetry-otel/README.md     |   2 +-
 .../telemetry/session-telemetry-otel/README.zh.md  |   2 +-
 .../telemetry/session-telemetry-otel/package.json  |   4 +-
 .../telemetry/session-telemetry/README.i18n.yaml   |   2 +-
 packages/telemetry/session-telemetry/README.zh.md  |   2 +-
 packages/telemetry/session-telemetry/package.json  |   4 +-
 packages/timeout/README.i18n.yaml                  |   4 +-
 packages/timeout/README.md                         |  10 +-
 packages/timeout/README.zh.md                      |  10 +-
 packages/timeout/timeout-policy/README.i18n.yaml   |   2 +-
 packages/timeout/timeout-policy/README.zh.md       |   4 +-
 packages/timeout/timeout-policy/package.json       |   4 +-
 packages/todo/README.i18n.yaml                     |   4 +-
 packages/todo/README.md                            |   6 +-
 packages/todo/README.zh.md                         |   6 +-
 packages/todo/tool-todo/package.json               |   4 +-
 packages/todo/tool-todo/tests/tool-todo.spec.ts    |   2 +-
 packages/typert/README.i18n.yaml                   |   4 +-
 packages/typert/README.md                          |   8 +-
 packages/typert/README.zh.md                       |   8 +-
 packages/typert/generator/README.i18n.yaml         |   2 +-
 packages/typert/generator/README.zh.md             |   4 +-
 packages/typert/generator/package.json             |   4 +-
 packages/typert/loader/README.i18n.yaml            |   2 +-
 packages/typert/loader/README.zh.md                |   4 +-
 packages/typert/loader/package.json                |   4 +-
 packages/typert/registry/README.i18n.yaml          |   2 +-
 packages/typert/registry/README.zh.md              |   4 +-
 packages/typert/registry/package.json              |   4 +-
 packages/ui/README.i18n.yaml                       |   4 +-
 packages/ui/README.md                              |  20 +-
 packages/ui/README.zh.md                           |  22 +-
 packages/ui/app-boot/README.i18n.yaml              |   4 +-
 packages/ui/app-boot/README.md                     |   8 +-
 packages/ui/app-boot/README.zh.md                  |   8 +-
 packages/ui/app-boot/package.json                  |   4 +-
 packages/ui/app-boot/src/index.ts                  |  17 +-
 packages/ui/app-boot/tests/app-boot.spec.ts        |   9 +-
 packages/ui/app-boot/tests/config-reload.spec.ts   |   5 +-
 packages/ui/app-boot/tests/personal-config.spec.ts |  10 +-
 packages/ui/commands/README.i18n.yaml              |   4 +-
 packages/ui/commands/README.md                     |   2 +-
 packages/ui/commands/README.zh.md                  |   4 +-
 packages/ui/commands/package.json                  |   4 +-
 packages/ui/jsonrpc/README.i18n.yaml               |   2 +-
 packages/ui/jsonrpc/README.zh.md                   |   4 +-
 packages/ui/jsonrpc/package.json                   |   4 +-
 packages/ui/permission/README.i18n.yaml            |   2 +-
 packages/ui/permission/README.zh.md                |  16 +-
 packages/ui/permission/package.json                |   4 +-
 packages/ui/permission/tests/permission.spec.ts    |   2 +-
 packages/ui/tool-ask-user/README.i18n.yaml         |   2 +-
 packages/ui/tool-ask-user/README.zh.md             |   6 +-
 packages/ui/tool-ask-user/package.json             |   4 +-
 packages/ui/user-approval/README.i18n.yaml         |   2 +-
 packages/ui/user-approval/README.zh.md             |   4 +-
 packages/ui/user-approval/package.json             |   4 +-
 packages/ui/user-approval/tests/approval.spec.ts   |   2 +-
 packages/ui/user-approval/tests/invariant.spec.ts  |   2 +-
 packages/ui/user-interaction/README.i18n.yaml      |   4 +-
 packages/ui/user-interaction/README.md             |   2 +-
 packages/ui/user-interaction/README.zh.md          |   4 +-
 packages/ui/user-interaction/package.json          |   4 +-
 packages/util/README.i18n.yaml                     |   4 +-
 packages/util/README.md                            |  22 +-
 packages/util/README.zh.md                         |  22 +-
 packages/util/atomic-write/README.i18n.yaml        |   2 +-
 packages/util/atomic-write/README.zh.md            |   6 +-
 packages/util/atomic-write/package.json            |   4 +-
 packages/util/brand/README.i18n.yaml               |   2 +-
 packages/util/brand/README.zh.md                   |   2 +-
 packages/util/brand/package.json                   |   4 +-
 packages/util/native-command/README.i18n.yaml      |   4 +-
 packages/util/native-command/README.md             |   2 +-
 packages/util/native-command/README.zh.md          |  14 +-
 packages/util/native-command/package.json          |   4 +-
 packages/util/paths/README.i18n.yaml               |   2 +-
 packages/util/paths/README.zh.md                   |   2 +-
 packages/util/paths/package.json                   |   4 +-
 packages/util/retention/README.i18n.yaml           |   4 +-
 packages/util/retention/README.md                  |   4 +-
 packages/util/retention/README.zh.md               |   8 +-
 packages/util/retention/package.json               |   4 +-
 packages/util/timeout/README.i18n.yaml             |   4 +-
 packages/util/timeout/README.md                    |   2 +-
 packages/util/timeout/README.zh.md                 |   4 +-
 packages/util/timeout/package.json                 |   4 +-
 packages/web/README.i18n.yaml                      |   4 +-
 packages/web/README.md                             |  20 +-
 packages/web/README.zh.md                          |  20 +-
 packages/web/tool-web/README.i18n.yaml             |   2 +-
 packages/web/tool-web/README.zh.md                 |  10 +-
 packages/web/tool-web/package.json                 |   4 +-
 packages/web/web-fetch-local/README.i18n.yaml      |   2 +-
 packages/web/web-fetch-local/README.zh.md          |   4 +-
 packages/web/web-fetch-local/package.json          |   4 +-
 packages/web/web-search-deepseek/README.i18n.yaml  |   2 +-
 packages/web/web-search-deepseek/README.zh.md      |   4 +-
 packages/web/web-search-deepseek/package.json      |   4 +-
 packages/web/web-search-exa/README.i18n.yaml       |   2 +-
 packages/web/web-search-exa/README.zh.md           |   4 +-
 packages/web/web-search-exa/package.json           |   4 +-
 .../web/web-search-perplexity/README.i18n.yaml     |   2 +-
 packages/web/web-search-perplexity/README.zh.md    |   6 +-
 packages/web/web-search-perplexity/package.json    |   4 +-
 packages/web/web/README.i18n.yaml                  |   2 +-
 packages/web/web/README.zh.md                      |   4 +-
 packages/web/web/package.json                      |   4 +-
 packages/workflow/README.i18n.yaml                 |   4 +-
 packages/workflow/README.md                        |  14 +-
 packages/workflow/README.zh.md                     |  18 +-
 packages/workflow/tool-ralph/README.i18n.yaml      |   2 +-
 packages/workflow/tool-ralph/README.zh.md          |   2 +-
 packages/workflow/tool-ralph/package.json          |   4 +-
 packages/workflow/tool-workflow/README.i18n.yaml   |   2 +-
 packages/workflow/tool-workflow/README.zh.md       |   6 +-
 packages/workflow/tool-workflow/package.json       |   4 +-
 .../workflow-workerthread/README.i18n.yaml         |   2 +-
 .../workflow/workflow-workerthread/README.zh.md    |   4 +-
 .../workflow/workflow-workerthread/package.json    |   4 +-
 packages/workflow/workflow/README.i18n.yaml        |   2 +-
 packages/workflow/workflow/README.zh.md            |   8 +-
 packages/workflow/workflow/package.json            |   4 +-
 packages/workspace/README.i18n.yaml                |   4 +-
 packages/workspace/README.md                       |   8 +-
 packages/workspace/README.zh.md                    |   8 +-
 packages/workspace/workspace/README.i18n.yaml      |   2 +-
 packages/workspace/workspace/README.zh.md          |   4 +-
 packages/workspace/workspace/package.json          |   4 +-
 pnpm-workspace.yaml                                |   9 +
 951 files changed, 13133 insertions(+), 3919 deletions(-)
```

## 破坏性变更清单

- 本日快照未发现 seam 符号级破坏。

## 插件侧建议（按仓库）

### issues
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### dsh-live-stats
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-working-activity
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（bfb9136）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### plugin-registry
- 兼容：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁「OK（1 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 20260804T143803Z 显式记录到 README/补丁头，快照一漂即可自动预警。
### sandbox-mxc
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### web-components
- 兼容：锚定 b4b67f0（未知（不同谱系））、补丁「OK（1 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 b4b67f0 显式记录到 README/补丁头，快照一漂即可自动预警。
### dsh-opencode-server
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### toybox
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### ex-setting
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### tg-bot
- 兼容：锚定 fa3d357fc66102d82f0ddbf67fd3d5d70944d8f7（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### group-chat-diary
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### dsh-skins
- 兼容：锚定 f1792735（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-coding-receipt
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
- 输入来自 DSH session log，建议在 mainline 会话持久化格式稳定后实现。
### qqbot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-subagent-tree
- 需适配：锚定 未知（未知）、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（bfb9136）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### review-panel
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-github-integration
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-weixin-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### marisa
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-feishu-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-wecom-bot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### session-chatlog
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### distill
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### telegram
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-browser
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-my-rsi
- 兼容：锚定 b067916ae930cd9a519996ea9ee673afd1ec7335（未知（不同谱系））、补丁「OK（2 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 b067916ae930cd9a519996ea9ee673afd1ec7335 显式记录到 README/补丁头，快照一漂即可自动预警。
### dsh-win-port
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-desktop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-pty-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-shell-windows
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### deepseek-harness-desktop
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### session-persistence-rdb
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### deepseek-harness-distro
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-calculator
- 兼容：锚定 25b2ad4f67（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dshx-update-check
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-acp
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-sfw
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-issue-filer
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-gh-bridge
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-vision
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-web-ui-approval-notify
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-agent-session-sources
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-companion
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### hub
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-tool-json
- 兼容：锚定 25b2ad4f67（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-skills-manager
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-pi-adapter
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### chat-width
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-memory-evolve
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-artifact
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-session-search
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-cordis-examples
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### dsh-web-terminal
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-ui-progress
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### turtle-ui
- 需适配：锚定 a6fedc9e3b36d066e34860d040db6df47d88c432（未知（不同谱系））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（bfb9136）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### dsh-cc-tui
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### Qwen-MM-Plugins
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
