# Agent 运行级测试（2026-08-14 · dsh + Qwen3.6-35B · k8s 5 分片）

- 方法：容器内 dsh（agent）经 de-stream 代理用 Qwen 读插件 README → 自主导入 → 验证；3 次重试，全败判不兼容。
- 总计 242：✅可用 152 / ❌不兼容 90 / ⏭️跳过 0 / 未知 0

## ✅ 可用（152）

| 插件 | 结论 | 原因 |
|---|---|---|
| chat-width | ✅ 可用 | (无) |
| cross-harness-cite | ✅ 可用 | (无) |
| deepseek-harness-desktop | ✅ 可用 | (无) |
| deepseek-harness-huggingface | ✅ 可用 | (无) |
| deepseek-manners | ✅ 可用 | (无) |
| dsh-acp | ✅ 可用 | (无) |
| dsh-acp-for-bitfun | ✅ 可用 | (无) |
| dsh-activity-plugin | ✅ 可用 | (无) |
| dsh-ads | ✅ 可用 | (无) |
| dsh-advisor | ✅ 可用 | (无) |
| dsh-agent-budget | ✅ 可用 | (无) |
| dsh-agent-rp | ✅ 可用 | (无) |
| dsh-aigc-canvas | ✅ 可用 | (无) |
| dsh-annotation | ✅ 可用 | (无) |
| dsh-anti-ads | ✅ 可用 | (无) |
| dsh-artifact | ✅ 可用 | (无) |
| dsh-auto-blame | ✅ 可用 | (无) |
| dsh-bash-encoding | ✅ 可用 | (无) |
| DSH-better-sidebar | ✅ 可用 | (无) |
| dsh-better-sidebar-plugin-office | ✅ 可用 | (无) |
| dsh-browser | ✅ 可用 | (无) |
| dsh-browser-bridge | ✅ 可用 | (无) |
| dsh-browser-panel | ✅ 可用 | (无) |
| dsh-change-ledger | ✅ 可用 | (无) |
| dsh-chat-thumb | ✅ 可用 | (无) |
| dsh-chat-width | ✅ 可用 | (无) |
| dsh-client-ui-plan-execute | ✅ 可用 | (无) |
| dsh-code | ✅ 可用 | (无) |
| dsh-code-map | ✅ 可用 | (无) |
| dsh-companion | ✅ 可用 | (无) |
| dsh-context-doctor | ✅ 可用 | (无) |
| dsh-conversation-share | ✅ 可用 | (无) |
| dsh-cot-summary | ✅ 可用 | (无) |
| dsh-crew | ✅ 可用 | (无) |
| dsh-custom-tool | ✅ 可用 | (无) |
| dsh-d399 | ✅ 可用 | (无) |
| dsh-deeplink | ✅ 可用 | (无) |
| dsh-design | ✅ 可用 | (无) |
| dsh-desktop-electron | ✅ 可用 | (无) |
| dsh-drag-and-drop | ✅ 可用 | (无) |
| dsh-dzcf | ✅ 可用 | (无) |
| dsh-emoji | ✅ 可用 | (无) |
| dsh-engram-relay | ✅ 可用 | (无) |
| dsh-evolve | ✅ 可用 | (无) |
| dsh-explain | ✅ 可用 | (无) |
| dsh-feishu-bot | ✅ 可用 | (无) |
| dsh-feishu-notify | ✅ 可用 | (无) |
| dsh-focus-chat | ✅ 可用 | (无) |
| dsh-genui | ✅ 可用 | (无) |
| dsh-gh-bridge | ✅ 可用 | (无) |
| dsh-git-graph | ✅ 可用 | (无) |
| dsh-git-identity | ✅ 可用 | (无) |
| dsh-gomoku | ✅ 可用 | (无) |
| dsh-hub | ✅ 可用 | (无) |
| dsh-humanize | ✅ 可用 | (无) |
| dsh-input-history | ✅ 可用 | (无) |
| dsh-inspect | ✅ 可用 | (无) |
| dsh-interconnect | ✅ 可用 | (无) |
| dsh-interpreters | ✅ 可用 | (无) |
| dsh-involute | ✅ 可用 | (无) |
| dsh-kb-sieve | ✅ 可用 | (无) |
| dsh-kimi-bridge | ✅ 可用 | (无) |
| dsh-lazyfish | ✅ 可用 | (无) |
| dsh-mega | ✅ 可用 | (无) |
| dsh-meme | ✅ 可用 | (无) |
| dsh-memory-evolve | ✅ 可用 | (无) |
| dsh-message-edit | ✅ 可用 | (无) |
| dsh-mineru | ✅ 可用 | (无) |
| dsh-minigames | ✅ 可用 | (无) |
| dsh-mnemon | ✅ 可用 | (无) |
| dsh-mobileweb-adapter | ✅ 可用 | (无) |
| dsh-multimedia-webui-input | ✅ 可用 | (无) |
| dsh-my-rsi | ✅ 可用 | (无) |
| dsh-navbar | ✅ 可用 | (无) |
| dsh-notification | ✅ 可用 | (无) |
| dsh-nowledge-mem | ✅ 可用 | (无) |
| dsh-office | ✅ 可用 | (无) |
| dsh-openpencil | ✅ 可用 | (无) |
| dsh-paste-input | ✅ 可用 | (无) |
| dsh-pet | ✅ 可用 | (无) |
| dsh-pet-web | ✅ 可用 | (无) |
| dsh-pi-adapter | ✅ 可用 | (无) |
| dsh-plannotator | ✅ 可用 | (无) |
| dsh-plugin-background | ✅ 可用 | (无) |
| dsh-plugin-check | ✅ 可用 | (无) |
| dsh-plus | ✅ 可用 | (无) |
| dsh-prompt-studio | ✅ 可用 | (无) |
| dsh-question-collapse | ✅ 可用 | (无) |
| dsh-roleplay-portable-spike | ✅ 可用 | (无) |
| dsh-scholar | ✅ 可用 | (无) |
| dsh-scout | ✅ 可用 | (无) |
| dsh-selection-chat | ✅ 可用 | (无) |
| dsh-self-control-guard | ✅ 可用 | (无) |
| dsh-sentinel | ✅ 可用 | (无) |
| dsh-serenity-plugin | ✅ 可用 | (无) |
| dsh-session-health | ✅ 可用 | (无) |
| dsh-session-notification | ✅ 可用 | (无) |
| dsh-session-search | ✅ 可用 | (无) |
| dsh-sfw | ✅ 可用 | (无) |
| dsh-share | ✅ 可用 | (无) |
| dsh-shell-windows | ✅ 可用 | (无) |
| dsh-side-panel | ✅ 可用 | (无) |
| dsh-skill-stats | ✅ 可用 | (无) |
| dsh-skills-manager | ✅ 可用 | (无) |
| dsh-skins | ✅ 可用 | (无) |
| dsh-sleep | ✅ 可用 | (无) |
| dsh-slice-agent-loop | ✅ 可用 | (无) |
| dsh-split-panes | ✅ 可用 | (无) |
| dsh-spur | ✅ 可用 | (无) |
| dsh-task-board | ✅ 可用 | (无) |
| dsh-task-status | ✅ 可用 | (无) |
| dsh-tavern-plugin | ✅ 可用 | (无) |
| dsh-teamwork | ✅ 可用 | (无) |
| dsh-tianshu-tui | ✅ 可用 | (无) |
| dsh-tool-diff | ✅ 可用 | (无) |
| dsh-tool-encoding | ✅ 可用 | (无) |
| dsh-tool-schema | ✅ 可用 | (无) |
| dsh-tool-search | ✅ 可用 | (无) |
| dsh-tool-stat | ✅ 可用 | (无) |
| dsh-tps | ✅ 可用 | (无) |
| dsh-trace | ✅ 可用 | (无) |
| dsh-travel-plugin | ✅ 可用 | (无) |
| dsh-turn-navigator | ✅ 可用 | (无) |
| dsh-turn-rewind | ✅ 可用 | (无) |
| dsh-ui-progress | ✅ 可用 | (无) |
| dsh-ui-whale | ✅ 可用 | (无) |
| dsh-ultra-ui | ✅ 可用 | (无) |
| dsh-undo | ✅ 可用 | (无) |
| dsh-vision-toolkit | ✅ 可用 | (无) |
| dsh-visualize | ✅ 可用 | (无) |
| dsh-vscode | ✅ 可用 | (无) |
| dsh-web-archive | ✅ 可用 | (无) |
| dsh-web-panel | ✅ 可用 | (无) |
| dsh-web-review | ✅ 可用 | (无) |
| dsh-web-terminal | ✅ 可用 | (无) |
| dsh-web-ui-approval-notify | ✅ 可用 | (无) |
| dsh-web-ui-notify | ✅ 可用 | (无) |
| dsh-wecom-bot | ✅ 可用 | (无) |
| dsh-weixin-bot | ✅ 可用 | (无) |
| dshx-update-check | ✅ 可用 | (无) |
| fabric | ✅ 可用 | (无) |
| group-chat-diary | ✅ 可用 | (无) |
| marisa | ✅ 可用 | (无) |
| oh-dsh-desktop | ✅ 可用 | (无) |
| plugin-template | ✅ 可用 | (无) |
| qqbot | ✅ 可用 | (无) |
| repo-visibility-guard | ✅ 可用 | (无) |
| sandbox-nono | ✅ 可用 | (无) |
| session-teleport | ✅ 可用 | (无) |
| toybox | ✅ 可用 | (无) |
| whale-girl | ✅ 可用 | (无) |
| ya-workspace-sidebar | ✅ 可用 | (无) |

## ❌ 不兼容（90）

| 插件 | 结论 | 原因 |
|---|---|---|
| 7d7d | ❌ 不兼容 | FAIL: 缺少 DSH SDK（`~/.dsh/source/current` 不存在），`link:` 本地依赖无法解析，且 `lib/` 未构建。 |
| context-doctor | ❌ 不兼容 | FAIL: peer dependency @deepseek-ai/cordis 无法在当前环境安装（npm 仓库中不存在该包，非公开 npm 包） |
| distill | ❌ 不兼容 | FAIL: peer dependencies (@deepseek-ai/schemastery 等) 无法安装——npm 缓存目录权限被拒，且沙箱阻止在 /clones/distill 创建 node_modules。 |
| dsh-101 | ❌ 不兼容 | FAIL: peer dependencies (e.g. @deepseek-ai/dsh-paths) not resolvable when loaded standalone |
| dsh-a2a | ❌ 不兼容 | FAIL: workspace:^ dependencies require full DSH monorepo pnpm workspace; no prebuilt lib/ exists in isolation. |
| dsh-agent-teams | ❌ 不兼容 | FAIL: 仓库为只读文件系统，无法安装 peerDependencies（如 @deepseek-ai/schemastery），插件加载失败。 |
| dsh-alphasolve | ❌ 不兼容 | FAIL: 依赖安装失败，npm 不支持 package.json 中的 link: 协议（指向 deepseek-harness 的本地路径），且 pnpm 未安装 |
| dsh-at-file | ❌ 不兼容 | FAIL: 插件的依赖（@deepseek-ai/dsh-typert-protocol 等 peer 包）需要 dsh 单体仓库的 link 路径，环境中不存在，导致模块加载失败 |
| dsh-auto-approval | ❌ 不兼容 | FAIL: 缺少 @deepseek-ai/dsh-settings 依赖，无法加载 |
| dsh-auto-chess | ❌ 不兼容 | FAIL: npm缓存目录权限问题（EACCES），无法安装依赖，因此插件无法加载。 |
| dsh-automation | ❌ 不兼容 | FAIL: 缺少依赖包 @deepseek-ai/schemastery（未列入 package.json） |
| dsh-cc-connect | ❌ 不兼容 | FAIL: peer 依赖 schemastery 和 @deepseek-ai/dsh-tools 是 dsh 内部包，npm 上不存在，无法安装依赖，加载失败 |
| dsh-cc-tui | ❌ 不兼容 | FAIL: 缺少 DSH monorepo 的 workspace:^ 依赖（如 @deepseek-ai/schemastery），无法独立加载 |
| dsh-checkpoint | ❌ 不兼容 | FAIL: 源码未编译（无lib/输出），且依赖使用workspace协议需monorepo环境，peer deps无法解析。 |
| dsh-club | ❌ 不兼容 | FAIL: 项目是 Next.js 应用（dsh-club 排行榜网站），缺少 dsh.plugin.json / .dsh-plugin/ / catalog.json 插件清单，无法作为 DSH 插件加载。 |
| dsh-codex-bridge | ❌ 不兼容 | FAIL: 插件本身构建成功，但缺少 DSH 宿主环境（@deepseek-ai/cordis、@deepseek-ai/dsh-tools 仅为 peerDep，外部无法独立安装），无法脱离 DSH 验证加载。 |
| dsh-computer-use | ❌ 不兼容 | FAIL: 模块为 ESM 且依赖多个未发布的 DSH 内部包（如 @deepseek-ai/cordis），当前环境无法解析。 |
| dsh-custom-css | ❌ 不兼容 | FAIL: 构建产物 lib/ 不存在且无法安装依赖（只读文件系统，无法创建 node_modules） |
| dsh-cyber-sec | ❌ 不兼容 | FAIL: 源码目录只读无法安装依赖（`ROFS`），且无 node_modules/dist 产物，无法加载 |
| dsh-data-agent | ❌ 不兼容 | FAIL: 插件依赖的 8 个 `@deepseek-ai/*` peer deps（dsh-client-locale、dsh-client-runtime、dsh-client-ui-conversation、dsh-client-ui-slots、dsh-host-webs |
| dsh-deep-research | ❌ 不兼容 | FAIL: 缺少 peer 依赖 `@deepseek-ai/dsh-tools` 和 `@deepseek-ai/dsh-workflow`（这些包由 DSH 宿主环境提供，不在 npm 上，独立安装时无法解析） |
| dsh-deepresearch | ❌ 不兼容 | FAIL: peer dependencies are internal @deepseek-ai packages not resolvable on public npm, plus workspace lacks write permissions for .dsh and |
| dsh-diff-viewer | ❌ 不兼容 | FAIL: 源码未编译（lib/ 目录不存在），且 devDependencies 中的 link: 本地路径依赖在当前环境无法解析 |
| dsh-easy-ctx-manager | ❌ 不兼容 | FAIL: 所有依赖通过 link: 指向 ../test-snnh，该目录在当前环境不存在，无法安装依赖。 |
| dsh-edu | ❌ 不兼容 | FAIL: 沙箱权限不足，无法在 `/home/node/.dsh/profiles/edu` 下创建 profile 目录，且源码目录为只读无法安装依赖。 |
| dsh-grok-tui | ❌ 不兼容 | dsh: EMPTY_RESPONSE: model returned a completed response with no content |
| dsh-kimi-browser | ❌ 不兼容 | FAIL: peer dependencies (schemastery, cordis, @deepseek-ai/dsh-*) 未发布到 npm，无法解析 |
| dsh-latex | ❌ 不兼容 | FAIL: link: protocol deps (dsh internal packages) cannot be resolved and lib/ build output does not exist. |
| dsh-live-stats | ❌ 不兼容 | FAIL: 插件依赖使用 link: 协议指向 ~/deepseek-harness 目录（该目录不存在），无法安装构建，导致 dsh 加载失败 |
| dsh-llm-fallbacks | ❌ 不兼容 | FAIL: dist/index.js 缺失，构建未完成（prepare 阶段因缺少 pnpm 而失败，dist 中仅有 .d.ts 无 .js） |
| dsh-longbridge | ❌ 不兼容 | FAIL: 依赖私有 DSH 包（@deepseek-ai/dsh-*、cordis）无法通过 npm 安装，无 DSH 工作空间无法解析 |
| dsh-loop | ❌ 不兼容 | FAIL: 缺少内部依赖 `@deepseek-ai/dsh-tools`，无法解析模块 |
| dsh-mobile | ❌ 不兼容 | FAIL: 依赖使用 link: 协议指向不存在的 ../dsh2026/test-lehhair 路径，npm install 失败导致 lib/ 未构建，dsh 插件无法加载 |
| dsh-multica-runtime | ❌ 不兼容 | FAIL: 编译产物存在但运行时缺少传递依赖 @deepseek-ai/dsh-scope（dsh-session 间接引入），导致模块无法加载。 |
| dsh-music-player | ❌ 不兼容 | FAIL: 文件系统只读，无法创建 node_modules 和 lib/（缺依赖，无法构建） |
| dsh-notebooks | ❌ 不兼容 | FAIL: 缺少 peer 依赖（如 @deepseek-ai/cordis），且 npm install 因 ~/.npm 权限不足、dsh plugin 因 ~/.dsh 权限不足，均无法完成安装，模块无法加载。 |
| dsh-open-in-vscode | ❌ 不兼容 | FAIL: 依赖 `@deepseek-ai/dsh-typert-protocol` 等通过 `link:` 指向 `../dsh` 本地路径的 peer 包缺失，且 `dsh` 源码不存在，导致模块无法加载。 |
| dsh-openbiliclaw | ❌ 不兼容 | FAIL: 缺少 @deepseek-ai/dsh-tools 等 DSH peer 依赖，无法独立加载 |
| dsh-opencode-server | ❌ 不兼容 | FAIL: 缺少 DSH 主仓库（@deepseek-ai/dsh-root），无法生成 tsconfig 和构建，插件不能加载 |
| dsh-openmaic | ❌ 不兼容 | FAIL: 缺少 @deepseek-ai/dsh-tools 等 peer 依赖（需手动 symlink 宿主机依赖） |
| dsh-paseo | ❌ 不兼容 | FAIL: build fails — no dsh snapshot/monorepo found (needs DSH_MONOREPO set or dsh source at ~/.dsh/source/current) |
| dsh-plan-execute | ❌ 不兼容 | FAIL: 缺少运行时依赖 `@deepseek-ai/schemastery`，且 devDependencies 使用 `workspace:^` 协议（需 pnpm monorepo），fs 只读无法安装依赖。 |
| dsh-pty-windows | ❌ 不兼容 | FAIL: 缺少依赖 @deepseek-ai/dsh-pty（该包需从宿主 checkout 的 node_modules 向上解析获取，当前环境中不可用） |
| dsh-qq2006 | ❌ 不兼容 | FAIL: 插件需构建（无lib/产物）且peer依赖仅在DSH monorepo内可用，无法独立加载 |
| dsh-remote-web-ui | ❌ 不兼容 | FAIL: 缺少 sibling DSH 源码仓导致 prepare 构建失败（lib/ 未生成），且 peer 依赖（@deepseek-ai/dsh-*、cordis）无法从 npm 解析 |
| dsh-rewind | ❌ 不兼容 | FAIL: lib/index.js 未编译存在，且依赖 workspace:^ monorepo 协议无法单独安装 |
| dsh-save-intp | ❌ 不兼容 | FAIL: 依赖通过 link: 协议指向不存在的 /clones/test-r05En1cU-0810 目录，且缺少 src/ 源码和 lib/ 构建产物，无法安装也无法加载。 |
| dsh-security-audit | ❌ 不兼容 | FAIL: 缺少 peer 依赖 `@deepseek-ai/dsh-tools`，且 /clones 目录为只读无法安装 npm 包。 |
| dsh-session-cluster | ❌ 不兼容 | FAIL: 插件是TypeScript源码，其peer依赖(cordis等@deepseek-ai/dsh-*)的symlink指向不存在的路径(/home/adam/dsh-external-research/.mainline-build/)，依赖不可用 |
| dsh-sidechain | ❌ 不兼容 | FAIL: 依赖使用 link: 指向本机 .dsh/source/current 路径，当前环境不存在该路径，npm install 失败且 lib/ 未构建 |
| dsh-sonar | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/dsh-paths@^0.0.1-rc.1 在公共 npm registry 不存在（404），且 lib/ 未构建，插件无法加载。 |
| dsh-stickers | ❌ 不兼容 | FAIL: 无法安装加载 — peerDependencies 使用 link: 协议需 pnpm 解析，且 dsh plugin add 在 .dsh 目录写入被拒绝 |
| dsh-stock-market | ❌ 不兼容 | FAIL: Peer dependencies (@deepseek-ai/cordis, @deepseek-ai/dsh-*) are required but unavailable — no DSH workspace linked. |
| dsh-suggested-replies | ❌ 不兼容 | FAIL: 缺少 DSH 平台内部依赖（如 @deepseek-ai/schemastery 等 peer deps），无法在独立 Node 环境中加载 |
| dsh-super-injector | ❌ 不兼容 | FAIL: 源码在只读目录 `/clones` 下，无法创建 node_modules 和 symlink 依赖链，构建脚本也要求外部 DSH_CHECKOUT，无法在此环境加载 |
| dsh-tool-calculator | ❌ 不兼容 | FAIL: 只读文件系统无法安装依赖，且 peer 依赖 @deepseek-ai/dsh-tools 未安装导致模块加载失败（需通过 dsh plugin 安装或在 monorepo workspace 环境中使用） |
| dsh-tool-csv | ❌ 不兼容 | FAIL: 缺少 peer 依赖 @deepseek-ai/dsh-tools，单独 require 无法解析（需通过 dsh plugin 安装到 profile 才能加载） |
| dsh-tool-json | ❌ 不兼容 | FAIL: Peer 依赖 @deepseek-ai/dsh-tools 为私有包，安装失败导致插件无法加载 |
| dsh-tool-markdown | ❌ 不兼容 | FAIL: 缺少 peer 依赖（@deepseek-ai/dsh-tools 等），独立加载失败 |
| dsh-tool-regex | ❌ 不兼容 | FAIL: 缺少 peer 依赖（@deepseek-ai/dsh-tools / dsh-invariants / cordis），这些是内部包在当前 npm 环境中无法安装，导致模块加载时报 Cannot find package。 |
| dsh-tool-time | ❌ 不兼容 | FAIL: peer dependency '@deepseek-ai/dsh-tools' not found and node_modules is read-only (无法安装依赖) |
| dsh-toolkit | ❌ 不兼容 | FAIL: 插件依赖 `@deepseek-ai/dsh-tools` 未安装（无 node_modules），且 npm install 和 dsh profile 创建均受限于只读文件系统/权限，无法完成加载。 |
| dsh-track | ❌ 不兼容 | FAIL: 缺少 DSH 平台依赖（~/.dsh/source/current 不存在、peerDependencies 为内部 @deepseek-ai 包、tsc 不可用导致构建失败） |
| dsh-tui-front-door | ❌ 不兼容 | FAIL: 缺少运行时依赖（react）和 peer 依赖（需 ds-harness 兄弟目录，均未安装） |
| dsh-vision | ❌ 不兼容 | FAIL: 缺少 peer 依赖 @deepseek-ai/dsh-tools、@deepseek-ai/cordis、@deepseek-ai/dsh-system-prompt，无法 resolve ES module 导入。 |
| dsh-voice-chat | ❌ 不兼容 | FAIL: 插件依赖的 @deepseek-ai/dsh-client-runtime 和 @deepseek-ai/dsh-client-ui-slots 是 DSH 内部私有包，未发布到 npm 公共注册表，无法单独安装加载。 |
| dsh-web-ui | ❌ 不兼容 | dsh: EMPTY_RESPONSE: model returned a completed response with no content |
| dsh-webbridge | ❌ 不兼容 | FAIL: peerDependencies @deepseek-ai/dsh-tools 等 dsh 内部包无法找到，npm install 失败 |
| dsh_workflow | ❌ 不兼容 | FAIL: peer dependency `@deepseek-ai/schemastery` 未安装导致模块加载失败 |
| dshfind | ❌ 不兼容 | FAIL: /clones/dshfind 所在目录为只读文件系统，无法安装 node_modules 依赖，插件不能加载。 |
| ego-browser | ❌ 不兼容 | FAIL: 缺少 DSH 内部依赖包 @deepseek-ai/dsh-tools（未发布到公共 npm registry，安装失败） |
| ex-setting | ❌ 不兼容 | FAIL: peer 依赖 @deepseek-ai/dsh-api-remotes@^0.0.1 等私有包在 npm 上不存在，无法安装和加载 |
| mstar-harness | ❌ 不兼容 | **FAIL: 缺少 bun 运行时且 engine 包 tsconfig 仅 emit declaration 不生成 .js，导致 dist/engine.js 等入口文件不存在，无法加载。** |
| mstar-workflow | ❌ 不兼容 | FAIL: 源码为纯 TypeScript (无 dist/) 需 `bun` 编译、peer deps (`@deepseek-ai/cordis` 等) 无法安装、`dsh` CLI 硬编码 `/home/node/.dsh/profiles/web` 无 sudo 无法创建 |
| oh-my-dsh | ❌ 不兼容 | FAIL: npm 缓存目录 `/home/node/.npm` 权限不足（root 所有），无法安装依赖或构建插件 |
| Qwen-MM-Plugins | ❌ 不兼容 | FAIL: 依赖的 @deepseek-ai/dsh-* peer 包为内部包，npm 无法找到对应版本；且 lib/ 未构建（无 pnpm 无法执行 tsc build）。 |
| sandbox-micro | ❌ 不兼容 | FAIL: 无法加载——lib/ 目录不存在（未构建），且 peerDependencies 中的 @deepseek-ai/dsh-invariants 等依赖在 npm 上不存在，需_sibling 源码仓库。 |
| sandbox-mxc | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/dsh-invariants 等 DSH 内部包和 @dsh-external/mxc-sdk（需 GitHub Packages 认证）无法解析，且源码未编译（无 lib/ 目录） |
| session-chatlog | ❌ 不兼容 | FAIL: peer dependencies (schemastery, @deepseek-ai/dsh-session 等) 无法安装且 dsh 版本过低 |
| session-persistence-rdb | ❌ 不兼容 | FAIL: peer dependencies on internal @deepseek-ai packages are not resolvable; TypeScript entry not directly executable without full dsh buil |
| show-bash-command | ❌ 不兼容 | FAIL: 插件依赖使用了 `link:` 本地路径指向 DSH 源码（如 `../../.dsh/source/current/packages/client/runtime`），本机不存在该路径，导致安装失败、无法加载。 |
| telegram | ❌ 不兼容 | FAIL: peerDependencies (@deepseek-ai/dsh-agent, dsh-llm, dsh-session, cordis, schemastery) 为内部包，npm 注册表不可用，模块无法加载 |
| tonghuashun-webui | ❌ 不兼容 | FAIL: 沙箱为只读文件系统，无法写入 node_modules 目录，npm install 失败导致插件无法加载。 |
| turtle-ui | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/dsh-agent 等 peer 包不存在于 npm registry，且缺少 sibling deepseek-harness 源码，无法独立安装和构建。 |
| ui-status-label | ❌ 不兼容 | FAIL: 无法安装 peer 依赖（@deepseek-ai/dsh-settings 等），且文件系统只读导致 npm install 失败 |
| web-components | ❌ 不兼容 | FAIL: peer dependencies (`@deepseek-ai/dsh-client-locale`, `@deepseek-ai/dsh-client-runtime`, `@deepseek-ai/dsh-client-ui-slots`, `@deepseek |
| yet-another-subagent | ❌ 不兼容 | dsh: TRANSPORT: DeepSeek API request to http://127.0.0.1:18093/v1 failed |
| zephyr | ❌ 不兼容 | FAIL: 依赖安装失败 — 仓库使用 workspace: 协议需要 pnpm 管理器，但无法安装 pnpm（npm cache 权限问题）且 no registry 提供这些 rc 包 |
| zotero-harvest | ❌ 不兼容 | FAIL: peerDependency `@deepseek-ai/dsh-tools@^0.0.1` no matching version in npm registry (only `0.0.1-rc.5` / `0.1.0-rc.*` exist); manual `l |
| zotero-wave-rag | ❌ 不兼容 | FAIL: peer依赖 `@deepseek-ai/dsh-tools@^0.0.1` 在 npm 上不存在，无法安装依赖 |
