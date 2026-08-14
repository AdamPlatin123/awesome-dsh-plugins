# Agent 运行级测试（2026-08-14 · dsh + Qwen3.6-35B · k8s 5 分片）

- 方法：容器内 dsh（agent）经 de-stream 代理用 Qwen 读插件 README → 自主导入 → 验证；3 次重试，全败判不兼容。
- 总计 763：✅可用 616 / ❌不兼容 124 / ⏭️跳过 0 / 未知 0

## 分类统计（README 功能领域）

| 分类 | 已测 | ✅ | ❌ | ⚠️ |
|---|---|---|---|---|
| 未收录 | 622 | 533 | 68 | 21 |
| 🤖 Agent 能力 | 30 | 17 | 12 | 1 |
| 🗂 文件数据 | 25 | 12 | 13 | 0 |
| 🔌 Web UI 增强 | 24 | 16 | 8 | 0 |
| 🛠 基建部署 | 22 | 14 | 8 | 0 |
| 💻 编码开发 | 16 | 11 | 5 | 0 |
| 🎮 娱乐生活 | 9 | 7 | 2 | 0 |
| 📚 学习研究 | 6 | 3 | 3 | 0 |
| 📡 消息通讯 | 6 | 2 | 4 | 0 |
| ❓ 其他 | 3 | 1 | 1 | 1 |

## ✅ 可用（616）

| 插件 | 结论 | 原因 |
|---|---|---|
| A_memorix-deepseek-harness | ✅ 可用 | (无) |
| agent-loop-workflow | ✅ 可用 | (无) |
| Angelina-dsh-plugin | ✅ 可用 | (无) |
| anysearch-dsh | ✅ 可用 | (无) |
| aureways | ✅ 可用 | (无) |
| AuroraCoder | ✅ 可用 | (无) |
| awesome-dsh-background-plugin | ✅ 可用 | (无) |
| better-model-provider | ✅ 可用 | (无) |
| Better_Deepseek_Harkness | ✅ 可用 | (无) |
| billion-context-dsh | ✅ 可用 | (无) |
| blender | ✅ 可用 | (无) |
| cascade | ✅ 可用 | (无) |
| ChatCCC | ✅ 可用 | (无) |
| claude-harness-desktop | ✅ 可用 | (无) |
| claude-parchment-theme | ✅ 可用 | (无) |
| codex-plugin-dsh | ✅ 可用 | (无) |
| computer-use-plus | ✅ 可用 | (无) |
| context-vista | ✅ 可用 | (无) |
| ContextGate | ✅ 可用 | (无) |
| DeepJIT | ✅ 可用 | (无) |
| deepseek-harness-acp | ✅ 可用 | (无) |
| deepseek-harness-desktop | ✅ 可用 | (无) |
| DeepSeek-harness-desktop-plugin | ✅ 可用 | (无) |
| DeepSeek-harness-dingtalk | ✅ 可用 | (无) |
| deepseek-harness-dsh-plugin-hub | ✅ 可用 | (无) |
| DeepSeek-Harness-for-VS-Code | ✅ 可用 | (无) |
| deepseek-harness-for-vscode | ✅ 可用 | (无) |
| deepseek-harness-huggingface | ✅ 可用 | (无) |
| DeepSeek-harness-lark | ✅ 可用 | (无) |
| DeepSeek-Harness-Pet | ✅ 可用 | (无) |
| Deepseek-Harness-plug | ✅ 可用 | (无) |
| deepseek-harness-plugin-from-scratch | ✅ 可用 | (无) |
| deepseek-harness-plugin-manager | ✅ 可用 | (无) |
| deepseek-harness-plugin-mcp | ✅ 可用 | (无) |
| deepseek-harness-ppt | ✅ 可用 | (无) |
| deepseek-harness-release | ✅ 可用 | (无) |
| Deepseek-harness-routing-layer- | ✅ 可用 | (无) |
| deepseek-harness-skillx | ✅ 可用 | (无) |
| deepseek-harness-skin | ✅ 可用 | (无) |
| deepseek-harness-tui | ✅ 可用 | (无) |
| deepseek-harness-typescript-sdk | ✅ 可用 | (无) |
| deepseek-harness-vision-plugin | ✅ 可用 | (无) |
| deepseek-harness-vsc-extension | ✅ 可用 | (无) |
| deepseek-harness-vscode | ✅ 可用 | (无) |
| DeepSeek-harness-wecom | ✅ 可用 | (无) |
| deepseek-harness.dsh-agent-vscode | ✅ 可用 | (无) |
| deepseek-manners | ✅ 可用 | (无) |
| deepseek-pet | ✅ 可用 | (无) |
| deepseek_harness_ui_schema_fix | ✅ 可用 | (无) |
| DeepSeekHarness-Desktop | ✅ 可用 | (无) |
| DeepSeekHarness-DesktopUI | ✅ 可用 | (无) |
| DeepSeekHarnessDesktop | ✅ 可用 | (无) |
| DeepSeekHarnessThirdModelThinkMgr | ✅ 可用 | (无) |
| dhs-theme-plugin | ✅ 可用 | (无) |
| Digital-Sweet-Heart | ✅ 可用 | (无) |
| Dive | ✅ 可用 | (无) |
| DIzzy-DSH | ✅ 可用 | (无) |
| ds-api-usage | ✅ 可用 | (无) |
| ds-balance-card | ✅ 可用 | (无) |
| ds-forge | ✅ 可用 | (无) |
| ds-vision-plugin | ✅ 可用 | (无) |
| ds-web-ui | ✅ 可用 | (无) |
| dscode | ✅ 可用 | (无) |
| dsh-acp-for-bitfun | ✅ 可用 | (无) |
| dsh-acp-plugin | ✅ 可用 | (无) |
| dsh-ads | ✅ 可用 | (无) |
| dsh-advisor | ✅ 可用 | (无) |
| dsh-agent-arcade | ✅ 可用 | (无) |
| dsh-agent-budget | ✅ 可用 | (无) |
| dsh-agent-messaging | ✅ 可用 | (无) |
| dsh-agent-sdk | ✅ 可用 | (无) |
| dsh-aigc-canvas | ✅ 可用 | (无) |
| dsh-all-search | ✅ 可用 | (无) |
| dsh-angry | ✅ 可用 | (无) |
| dsh-annotation | ✅ 可用 | (无) |
| dsh-answer-pet | ✅ 可用 | (无) |
| dsh-anti-ads | ✅ 可用 | (无) |
| dsh-archive-manager | ✅ 可用 | (无) |
| dsh-archive-viewer | ✅ 可用 | (无) |
| dsh-archived-sessions | ✅ 可用 | (无) |
| dsh-article-publish | ✅ 可用 | (无) |
| dsh-artifact | ✅ 可用 | (无) |
| dsh-attachment-formats | ✅ 可用 | (无) |
| dsh-atuin | ✅ 可用 | (无) |
| dsh-auto-approve | ✅ 可用 | (无) |
| dsh-auto-blame | ✅ 可用 | (无) |
| dsh-auto-compact | ✅ 可用 | (无) |
| dsh-auto-continue | ✅ 可用 | (无) |
| dsh-auto-memory | ✅ 可用 | (无) |
| dsh-auto-review | ✅ 可用 | (无) |
| dsh-aux-vision | ✅ 可用 | (无) |
| dsh-background-agents | ✅ 可用 | (无) |
| dsh-balance | ✅ 可用 | (无) |
| dsh-balance-display | ✅ 可用 | (无) |
| dsh-balance-meter | ✅ 可用 | (无) |
| dsh-balance-monitor | ✅ 可用 | (无) |
| dsh-balance-stats | ✅ 可用 | (无) |
| dsh-balance-tide | ✅ 可用 | (无) |
| dsh-batch-regression | ✅ 可用 | (无) |
| dsh-benchmark | ✅ 可用 | (无) |
| dsh-better-archive | ✅ 可用 | (无) |
| dsh-better-chat-history | ✅ 可用 | (无) |
| DSH-better-sidebar | ✅ 可用 | (无) |
| dsh-better-sidebar-plugin-office | ✅ 可用 | (无) |
| dsh-bg-image | ✅ 可用 | (无) |
| dsh-bg-wallpaper | ✅ 可用 | (无) |
| dsh-billing-glass | ✅ 可用 | (无) |
| dsh-bisect-debug | ✅ 可用 | (无) |
| dsh-black-whale | ✅ 可用 | (无) |
| dsh-blue-whale-maid | ✅ 可用 | (无) |
| dsh-bottom-bar | ✅ 可用 | (无) |
| dsh-bottom-stats | ✅ 可用 | (无) |
| dsh-browser | ✅ 可用 | (无) |
| dsh-browser-bridge | ✅ 可用 | (无) |
| dsh-browser-control | ✅ 可用 | (无) |
| dsh-cache-stabilizer | ✅ 可用 | (无) |
| dsh-capability-receipt | ✅ 可用 | (无) |
| dsh-change-ledger | ✅ 可用 | (无) |
| dsh-chat-import | ✅ 可用 | (无) |
| dsh-chat-width | ✅ 可用 | (无) |
| dsh-chatnode-wechat | ✅ 可用 | (无) |
| dsh-chrome | ✅ 可用 | (无) |
| DSH-Chrome-devtools | ✅ 可用 | (无) |
| dsh-claude-marketplace | ✅ 可用 | (无) |
| dsh-claude-move | ✅ 可用 | (无) |
| dsh-client-pricing | ✅ 可用 | (无) |
| dsh-client-shortcuts | ✅ 可用 | (无) |
| dsh-client-ui-mobile-adapt | ✅ 可用 | (无) |
| dsh-client-ui-monitor | ✅ 可用 | (无) |
| dsh-client-usage | ✅ 可用 | (无) |
| dsh-cloudflare-browser-run | ✅ 可用 | (无) |
| dsh-code | ✅ 可用 | (无) |
| dsh-codex-agent-bridge | ✅ 可用 | (无) |
| dsh-codex-auth | ✅ 可用 | (无) |
| dsh-codex-canvas | ✅ 可用 | (无) |
| dsh-codex-import | ✅ 可用 | (无) |
| dsh-codex-provider | ✅ 可用 | (无) |
| dsh-codex-subs-plugin | ✅ 可用 | (无) |
| dsh-codex-subscription | ✅ 可用 | (无) |
| dsh-command-opt | ✅ 可用 | (无) |
| dsh-commandcode-provider | ✅ 可用 | (无) |
| dsh-compaction-instant | ✅ 可用 | (无) |
| dsh-companion | ✅ 可用 | (无) |
| dsh-composer-enter | ✅ 可用 | (无) |
| dsh-composer-polish | ✅ 可用 | (无) |
| dsh-console-web-search | ✅ 可用 | (无) |
| dsh-content-rewriter | ✅ 可用 | (无) |
| dsh-context-doctor | ✅ 可用 | (无) |
| dsh-context-lens | ✅ 可用 | (无) |
| dsh-context-provenance | ✅ 可用 | (无) |
| dsh-continual-evolve | ✅ 可用 | (无) |
| dsh-conv-search | ✅ 可用 | (无) |
| dsh-conversation-indicator | ✅ 可用 | (无) |
| dsh-conversation-share | ✅ 可用 | (无) |
| dsh-cost | ✅ 可用 | (无) |
| dsh-cost-ledger | ✅ 可用 | (无) |
| dsh-cot-summary | ✅ 可用 | (无) |
| dsh-credentials-system | ✅ 可用 | (无) |
| dsh-crew | ✅ 可用 | (无) |
| dsh-crosstalk | ✅ 可用 | (无) |
| dsh-cue-plugin | ✅ 可用 | (无) |
| dsh-custom-workspace | ✅ 可用 | (无) |
| dsh-d399 | ✅ 可用 | (无) |
| dsh-data-extractor | ✅ 可用 | (无) |
| dsh-data-ledger | ✅ 可用 | (无) |
| dsh-deeplink | ✅ 可用 | (无) |
| dsh-deepseek-girl-pet | ✅ 可用 | (无) |
| dsh-deepseek-price-timer | ✅ 可用 | (无) |
| dsh-deepseek-usage | ✅ 可用 | (无) |
| dsh-deepseek-usage-dashboard | ✅ 可用 | (无) |
| dsh-delayed-task | ✅ 可用 | (无) |
| dsh-desk | ✅ 可用 | (无) |
| dsh-desktop-codex | ✅ 可用 | (无) |
| dsh-desktop-electron | ✅ 可用 | (无) |
| dsh-dingtalk | ✅ 可用 | (无) |
| dsh-douyin | ✅ 可用 | (无) |
| dsh-drag-and-drop | ✅ 可用 | (无) |
| dsh-dzcf | ✅ 可用 | (无) |
| dsh-effort-config | ✅ 可用 | (无) |
| dsh-emoji | ✅ 可用 | (无) |
| dsh-evolve | ✅ 可用 | (无) |
| dsh-explain | ✅ 可用 | (无) |
| dsh-eyecare | ✅ 可用 | (无) |
| dsh-eyes-upload | ✅ 可用 | (无) |
| dsh-fail-logger | ✅ 可用 | (无) |
| dsh-failure-capsule | ✅ 可用 | (无) |
| dsh-feishu-plugin | ✅ 可用 | (无) |
| dsh-figma-to-lottie | ✅ 可用 | (无) |
| dsh-file-changes | ✅ 可用 | (无) |
| dsh-file-claim | ✅ 可用 | (无) |
| dsh-file-explorer | ✅ 可用 | (无) |
| dsh-file-preview | ✅ 可用 | (无) |
| dsh-files | ✅ 可用 | (无) |
| dsh-filexplore | ✅ 可用 | (无) |
| dsh-find-plugin | ✅ 可用 | (无) |
| dsh-fleet-audit | ✅ 可用 | (无) |
| dsh-focus-chat | ✅ 可用 | (无) |
| DSH-for-VSC | ✅ 可用 | (无) |
| dsh-fs-explorer | ✅ 可用 | (无) |
| dsh-funpack | ✅ 可用 | (无) |
| dsh-gateway-presets | ✅ 可用 | (无) |
| dsh-gateway-provider | ✅ 可用 | (无) |
| dsh-genshin-skin | ✅ 可用 | (无) |
| dsh-genui | ✅ 可用 | (无) |
| dsh-git-graph | ✅ 可用 | (无) |
| dsh-git-identity | ✅ 可用 | (无) |
| dsh-git-status | ✅ 可用 | (无) |
| dsh-github | ✅ 可用 | (无) |
| dsh-go-rotator | ✅ 可用 | (无) |
| dsh-godot-skill | ✅ 可用 | (无) |
| dsh-gomoku | ✅ 可用 | (无) |
| dsh-governance | ✅ 可用 | (无) |
| dsh-harness-mcp-server | ✅ 可用 | (无) |
| dsh-hdc-bridge | ✅ 可用 | (无) |
| dsh-history | ✅ 可用 | (无) |
| dsh-host-web-compat | ✅ 可用 | (无) |
| dsh-hotswap | ✅ 可用 | (无) |
| dsh-huadongbianzuqi | ✅ 可用 | (无) |
| dsh-hub | ✅ 可用 | (无) |
| dsh-hud | ✅ 可用 | (无) |
| dsh-humanize | ✅ 可用 | (无) |
| dsh-humanizer | ✅ 可用 | (无) |
| dsh-im-gateway | ✅ 可用 | (无) |
| dsh-im-hub | ✅ 可用 | (无) |
| dsh-image-subagent | ✅ 可用 | (无) |
| dsh-image-theme | ✅ 可用 | (无) |
| dsh-imggenerate | ✅ 可用 | (无) |
| dsh-input-history | ✅ 可用 | (无) |
| dsh-inspect | ✅ 可用 | (无) |
| dsh-interconnect | ✅ 可用 | (无) |
| dsh-interpreters | ✅ 可用 | (无) |
| dsh-involute | ✅ 可用 | (无) |
| dsh-jingle | ✅ 可用 | (无) |
| dsh-k12-lesson-builder | ✅ 可用 | (无) |
| dsh-kb-sieve | ✅ 可用 | (无) |
| dsh-lan | ✅ 可用 | (无) |
| dsh-lan-access | ✅ 可用 | (无) |
| dsh-landscape | ✅ 可用 | (无) |
| dsh-lark | ✅ 可用 | (无) |
| dsh-lark-bot | ✅ 可用 | (无) |
| dsh-lark-link | ✅ 可用 | (无) |
| dsh-lark-meeting-notifier | ✅ 可用 | (无) |
| dsh-latex-tools | ✅ 可用 | (无) |
| dsh-launcher-lifetime | ✅ 可用 | (无) |
| dsh-lazy-tools | ✅ 可用 | (无) |
| dsh-lineage | ✅ 可用 | (无) |
| dsh-live2d-pets | ✅ 可用 | (无) |
| dsh-llm-codebuddy | ✅ 可用 | (无) |
| dsh-llm-codex-oauth | ✅ 可用 | (无) |
| dsh-llm-fallback | ✅ 可用 | (无) |
| dsh-llm-proxy | ✅ 可用 | (无) |
| dsh-local-filetree | ✅ 可用 | (无) |
| dsh-market | ✅ 可用 | (无) |
| dsh-marketplace-entry | ✅ 可用 | (无) |
| dsh-mattpocock-skills | ✅ 可用 | (无) |
| dsh-mcp-adapter | ✅ 可用 | (无) |
| dsh-mcp-manager | ✅ 可用 | (无) |
| dsh-mcp-settings | ✅ 可用 | (无) |
| dsh-mcpguard | ✅ 可用 | (无) |
| dsh-media-skills | ✅ 可用 | (无) |
| dsh-memento | ✅ 可用 | (无) |
| dsh-memory-evidence | ✅ 可用 | (无) |
| dsh-memory-evolve | ✅ 可用 | (无) |
| dsh-message-edit | ✅ 可用 | (无) |
| dsh-message-navigator | ✅ 可用 | (无) |
| dsh-metaplugin | ✅ 可用 | (无) |
| dsh-mic-input | ✅ 可用 | (无) |
| dsh-miku-skin | ✅ 可用 | (无) |
| dsh-mineru | ✅ 可用 | (无) |
| dsh-minigames | ✅ 可用 | (无) |
| dsh-mnemon | ✅ 可用 | (无) |
| dsh-mobile-control | ✅ 可用 | (无) |
| dsh-mobile-ui | ✅ 可用 | (无) |
| dsh-mod-manager | ✅ 可用 | (无) |
| dsh-model-provider-label | ✅ 可用 | (无) |
| dsh-model-selector | ✅ 可用 | (无) |
| dsh-model-thinking | ✅ 可用 | (无) |
| dsh-multimodal | ✅ 可用 | (无) |
| dsh-nanobananapro | ✅ 可用 | (无) |
| dsh-navbar | ✅ 可用 | (无) |
| dsh-nebulagraph-v5 | ✅ 可用 | (无) |
| dsh-netdoctor | ✅ 可用 | (无) |
| dsh-nocturne-memory | ✅ 可用 | (无) |
| dsh-node-nav | ✅ 可用 | (无) |
| dsh-notification | ✅ 可用 | (无) |
| dsh-notification-center | ✅ 可用 | (无) |
| dsh-notify | ✅ 可用 | (无) |
| dsh-notify-plugin | ✅ 可用 | (无) |
| dsh-notify-windows | ✅ 可用 | (无) |
| dsh-oauth-api | ✅ 可用 | (无) |
| dsh-observer | ✅ 可用 | (无) |
| dsh-obsidian-export | ✅ 可用 | (无) |
| dsh-open-auth-plugin | ✅ 可用 | (无) |
| dsh-open-in-finder | ✅ 可用 | (无) |
| dsh-openai-codex | ✅ 可用 | (无) |
| dsh-openapi | ✅ 可用 | (无) |
| dsh-opencode-go-usage | ✅ 可用 | (无) |
| dsh-openpencil | ✅ 可用 | (无) |
| dsh-ops-kit-legacy | ✅ 可用 | (无) |
| dsh-outline | ✅ 可用 | (无) |
| dsh-password-prompt | ✅ 可用 | (无) |
| dsh-passwords | ✅ 可用 | (无) |
| dsh-paste-input | ✅ 可用 | (无) |
| dsh-patchouli | ✅ 可用 | (无) |
| dsh-pdf | ✅ 可用 | (无) |
| dsh-peer-link | ✅ 可用 | (无) |
| dsh-permission-rules | ✅ 可用 | (无) |
| dsh-personalize | ✅ 可用 | (无) |
| dsh-pet-web | ✅ 可用 | (无) |
| dsh-pet-zhuangfangyi | ✅ 可用 | (无) |
| dsh-pets | ✅ 可用 | (无) |
| dsh-pi-adapter | ✅ 可用 | (无) |
| dsh-pin-recall | ✅ 可用 | (无) |
| dsh-plan-first-dev | ✅ 可用 | (无) |
| dsh-plannotator | ✅ 可用 | (无) |
| dsh-playwright-browser | ✅ 可用 | (无) |
| dsh-playwright-native | ✅ 可用 | (无) |
| DSH-Plugin-Account-HUD | ✅ 可用 | (无) |
| dsh-plugin-acn | ✅ 可用 | (无) |
| dsh-plugin-anti-ads | ✅ 可用 | (无) |
| dsh-plugin-approval-alert | ✅ 可用 | (无) |
| dsh-plugin-background | ✅ 可用 | (无) |
| dsh-plugin-background-image | ✅ 可用 | (无) |
| dsh-plugin-browser | ✅ 可用 | (无) |
| dsh-plugin-browser-notify | ✅ 可用 | (无) |
| dsh-plugin-cas-kb | ✅ 可用 | (无) |
| dsh-plugin-center | ✅ 可用 | (无) |
| dsh-plugin-check | ✅ 可用 | (无) |
| dsh-plugin-codex-import | ✅ 可用 | (无) |
| dsh-plugin-colorscheme | ✅ 可用 | (无) |
| dsh-plugin-confirm-check | ✅ 可用 | (无) |
| dsh-plugin-connection-banner | ✅ 可用 | (无) |
| dsh-plugin-console | ✅ 可用 | (无) |
| dsh-plugin-context-compressor | ✅ 可用 | (无) |
| dsh-plugin-cost | ✅ 可用 | (无) |
| dsh-plugin-cost-tracker | ✅ 可用 | (无) |
| dsh-plugin-d399 | ✅ 可用 | (无) |
| dsh-plugin-dated-folders | ✅ 可用 | (无) |
| dsh-plugin-dedup | ✅ 可用 | (无) |
| dsh-plugin-deepeye | ✅ 可用 | (无) |
| dsh-plugin-deepseek-balance | ✅ 可用 | (无) |
| dsh-plugin-description | ✅ 可用 | (无) |
| dsh-plugin-eval | ✅ 可用 | (无) |
| dsh-plugin-eyecare-theme | ✅ 可用 | (无) |
| dsh-plugin-genshin-startup | ✅ 可用 | (无) |
| dsh-plugin-git-inspect | ✅ 可用 | (无) |
| dsh-plugin-git-workflow | ✅ 可用 | (无) |
| dsh-plugin-github-market | ✅ 可用 | (无) |
| dsh-plugin-gomoku | ✅ 可用 | (无) |
| dsh-plugin-greeter | ✅ 可用 | (无) |
| dsh-plugin-grok2api-media-tool | ✅ 可用 | (无) |
| dsh-plugin-hooks | ✅ 可用 | (无) |
| dsh-plugin-installer | ✅ 可用 | (无) |
| dsh-plugin-jinji | ✅ 可用 | (无) |
| dsh-plugin-llm-codex | ✅ 可用 | (无) |
| dsh-plugin-manager-installer | ✅ 可用 | (无) |
| dsh-plugin-marketplace | ✅ 可用 | (无) |
| dsh-plugin-mermaid | ✅ 可用 | (无) |
| dsh-plugin-mineru | ✅ 可用 | (无) |
| dsh-plugin-model-provider-readout | ✅ 可用 | (无) |
| dsh-plugin-notify | ✅ 可用 | (无) |
| dsh-plugin-open-editor | ✅ 可用 | (无) |
| dsh-plugin-opencode-bridge | ✅ 可用 | (无) |
| dsh-plugin-peak-pricing | ✅ 可用 | (无) |
| dsh-plugin-pet | ✅ 可用 | (无) |
| dsh-plugin-pi-bridge | ✅ 可用 | (无) |
| dsh-plugin-product-subagents | ✅ 可用 | (无) |
| dsh-plugin-provider-quota | ✅ 可用 | (无) |
| dsh-plugin-ptc-context | ✅ 可用 | (无) |
| dsh-plugin-qr-connect | ✅ 可用 | (无) |
| dsh-plugin-rag | ✅ 可用 | (无) |
| dsh-plugin-recall | ✅ 可用 | (无) |
| dsh-plugin-release | ✅ 可用 | (无) |
| dsh-plugin-reload | ✅ 可用 | (无) |
| dsh-plugin-scaffold | ✅ 可用 | (无) |
| dsh-plugin-security-audit | ✅ 可用 | (无) |
| dsh-plugin-session-import | ✅ 可用 | (无) |
| dsh-plugin-session-outline | ✅ 可用 | (无) |
| dsh-plugin-shady-relay | ✅ 可用 | (无) |
| dsh-plugin-skill-tree | ✅ 可用 | (无) |
| dsh-plugin-slashx-gateway | ✅ 可用 | (无) |
| dsh-plugin-spur | ✅ 可用 | (无) |
| dsh-plugin-starter | ✅ 可用 | (无) |
| DSH-plugin-switch | ✅ 可用 | (无) |
| dsh-plugin-sysmon | ✅ 可用 | (无) |
| dsh-plugin-task-notification | ✅ 可用 | (无) |
| dsh-plugin-template | ✅ 可用 | (无) |
| dsh-plugin-terminal | ✅ 可用 | (无) |
| dsh-plugin-tokenmeter | ✅ 可用 | (无) |
| dsh-plugin-ui-turnav | ✅ 可用 | (无) |
| dsh-plugin-usage | ✅ 可用 | (无) |
| dsh-plugin-vision-toolkit | ✅ 可用 | (无) |
| dsh-plugin-voice-input | ✅ 可用 | (无) |
| dsh-plugin-web-notify | ✅ 可用 | (无) |
| dsh-plugin-wechat | ✅ 可用 | (无) |
| dsh-plugin-wepre | ✅ 可用 | (无) |
| dsh-plugin-workshop | ✅ 可用 | (无) |
| dsh-plugin-ya-workspace-sidebar | ✅ 可用 | (无) |
| dsh-plugins-hub | ✅ 可用 | (无) |
| dsh-plugins-market | ✅ 可用 | (无) |
| DSH-Plugins-Marketplace | ✅ 可用 | (无) |
| dsh-plugins-plan-usage | ✅ 可用 | (无) |
| dsh-policy-drift-proof | ✅ 可用 | (无) |
| dsh-portable-tavern | ✅ 可用 | (无) |
| dsh-postmortem | ✅ 可用 | (无) |
| dsh-precise-cache | ✅ 可用 | (无) |
| dsh-product-delivery-workflow | ✅ 可用 | (无) |
| dsh-project-file-explorer | ✅ 可用 | (无) |
| dsh-project-mcp-bridge | ✅ 可用 | (无) |
| dsh-prompt-optimizer | ✅ 可用 | (无) |
| dsh-prompt-polish | ✅ 可用 | (无) |
| dsh-prompt-profile | ✅ 可用 | (无) |
| dsh-prompt-studio | ✅ 可用 | (无) |
| dsh-qq-bridge | ✅ 可用 | (无) |
| dsh-qq-brige | ✅ 可用 | (无) |
| dsh-quota-panel | ✅ 可用 | (无) |
| dsh-quote-annotate | ✅ 可用 | (无) |
| dsh-qwen-mm | ✅ 可用 | (无) |
| dsh-read-history | ✅ 可用 | (无) |
| dsh-reasoning-settings | ✅ 可用 | (无) |
| dsh-reasoning-translator | ✅ 可用 | (无) |
| dsh-recall | ✅ 可用 | (无) |
| dsh-resume-plugin | ✅ 可用 | (无) |
| dsh-reverse-skill | ✅ 可用 | (无) |
| dsh-roleplay-portable-spike | ✅ 可用 | (无) |
| dsh-routines | ✅ 可用 | (无) |
| dsh-safe-web-fetch | ✅ 可用 | (无) |
| dsh-same-mode-sandbox-noop | ✅ 可用 | (无) |
| dsh-scholar | ✅ 可用 | (无) |
| dsh-science | ✅ 可用 | (无) |
| dsh-science-workbench | ✅ 可用 | (无) |
| dsh-scout | ✅ 可用 | (无) |
| dsh-search-endpoint-guard | ✅ 可用 | (无) |
| dsh-search-free | ✅ 可用 | (无) |
| dsh-security-scan | ✅ 可用 | (无) |
| dsh-security-suite | ✅ 可用 | (无) |
| dsh-see-image | ✅ 可用 | (无) |
| dsh-seedance2 | ✅ 可用 | (无) |
| dsh-self-control-guard | ✅ 可用 | (无) |
| dsh-sentinel | ✅ 可用 | (无) |
| dsh-seo-writer | ✅ 可用 | (无) |
| dsh-session-audit | ✅ 可用 | (无) |
| dsh-session-cost | ✅ 可用 | (无) |
| dsh-session-deeplink | ✅ 可用 | (无) |
| dsh-session-export | ✅ 可用 | (无) |
| dsh-session-health | ✅ 可用 | (无) |
| dsh-session-html-export | ✅ 可用 | (无) |
| dsh-session-import | ✅ 可用 | (无) |
| dsh-session-index | ✅ 可用 | (无) |
| dsh-session-management | ✅ 可用 | (无) |
| dsh-session-manager | ✅ 可用 | (无) |
| dsh-session-notification | ✅ 可用 | (无) |
| dsh-session-report | ✅ 可用 | (无) |
| dsh-session-search | ✅ 可用 | (无) |
| dsh-session-timeline | ✅ 可用 | (无) |
| dsh-sfw | ✅ 可用 | (无) |
| dsh-share | ✅ 可用 | (无) |
| dsh-side-panel | ✅ 可用 | (无) |
| dsh-skill-loader | ✅ 可用 | (无) |
| dsh-skill-lord-serf | ✅ 可用 | (无) |
| dsh-skill-manager | ✅ 可用 | (无) |
| dsh-skillport | ✅ 可用 | (无) |
| dsh-skillradar | ✅ 可用 | (无) |
| dsh-skin | ✅ 可用 | (无) |
| dsh-skin-amis | ✅ 可用 | (无) |
| dsh-skin-claude-code | ✅ 可用 | (无) |
| dsh-skin-switcher | ✅ 可用 | (无) |
| dsh-skins | ✅ 可用 | (无) |
| dsh-sleep | ✅ 可用 | (无) |
| dsh-slice-agent-loop | ✅ 可用 | (无) |
| dsh-specflow | ✅ 可用 | (无) |
| dsh-spend | ✅ 可用 | (无) |
| dsh-split-panes | ✅ 可用 | (无) |
| dsh-spur | ✅ 可用 | (无) |
| dsh-status-rotator | ✅ 可用 | (无) |
| dsh-sticky-note | ✅ 可用 | (无) |
| dsh-subagent-model | ✅ 可用 | (无) |
| dsh-subprocess-inherit-environment | ✅ 可用 | (无) |
| dsh-system-control | ✅ 可用 | (无) |
| dsh-task-board | ✅ 可用 | (无) |
| dsh-task-console | ✅ 可用 | (无) |
| dsh-task-models | ✅ 可用 | (无) |
| dsh-task-notify | ✅ 可用 | (无) |
| dsh-task-relay | ✅ 可用 | (无) |
| dsh-task-status | ✅ 可用 | (无) |
| dsh-taskboard-plugin | ✅ 可用 | (无) |
| dsh-tavern | ✅ 可用 | (无) |
| dsh-telegram-channel | ✅ 可用 | (无) |
| dsh-theme | ✅ 可用 | (无) |
| dsh-theme-blackgold | ✅ 可用 | (无) |
| dsh-theme-ti | ✅ 可用 | (无) |
| dsh-think-chinese | ✅ 可用 | (无) |
| dsh-think-flow-flow | ✅ 可用 | (无) |
| dsh-thinking-status-customizer | ✅ 可用 | (无) |
| dsh-tianshu-tui | ✅ 可用 | (无) |
| dsh-token-monitor | ✅ 可用 | (无) |
| dsh-token-stats | ✅ 可用 | (无) |
| dsh-token-usage | ✅ 可用 | (无) |
| dsh-tool-diff | ✅ 可用 | (无) |
| dsh-tool-encoding | ✅ 可用 | (无) |
| dsh-tool-schema | ✅ 可用 | (无) |
| dsh-tool-search | ✅ 可用 | (无) |
| dsh-tool-stat | ✅ 可用 | (无) |
| dsh-tool-todo-tree | ✅ 可用 | (无) |
| dsh-tool-turbo | ✅ 可用 | (无) |
| dsh-tool-underseal | ✅ 可用 | (无) |
| dsh-tool-user-memory | ✅ 可用 | (无) |
| dsh-tool-vision | ✅ 可用 | (无) |
| dsh-trace | ✅ 可用 | (无) |
| dsh-tray | ✅ 可用 | (无) |
| dsh-turn-approval | ✅ 可用 | (无) |
| dsh-turn-done-notify | ✅ 可用 | (无) |
| dsh-turn-index | ✅ 可用 | (无) |
| dsh-turn-navigator | ✅ 可用 | (无) |
| dsh-ui-background | ✅ 可用 | (无) |
| dsh-ui-progress | ✅ 可用 | (无) |
| dsh-ui-quote-selection | ✅ 可用 | (无) |
| dsh-ui-topbar-compact | ✅ 可用 | (无) |
| dsh-ultra-ui | ✅ 可用 | (无) |
| dsh-undo | ✅ 可用 | (无) |
| dsh-undo-plugin | ✅ 可用 | (无) |
| dsh-update-checker | ✅ 可用 | (无) |
| dsh-update-radar | ✅ 可用 | (无) |
| dsh-updater-ui | ✅ 可用 | (无) |
| dsh-usage-cost | ✅ 可用 | (无) |
| dsh-usage-dashboard | ✅ 可用 | (无) |
| dsh-user-experience | ✅ 可用 | (无) |
| DSH-user-plugin-list | ✅ 可用 | (无) |
| dsh-vision-adapter | ✅ 可用 | (无) |
| dsh-vision-android | ✅ 可用 | (无) |
| dsh-vision-helper | ✅ 可用 | (无) |
| dsh-vision-paste | ✅ 可用 | (无) |
| dsh-vision-provider | ✅ 可用 | (无) |
| dsh-vision-proxy | ✅ 可用 | (无) |
| dsh-vision-router | ✅ 可用 | (无) |
| dsh-vision-sidecar | ✅ 可用 | (无) |
| dsh-voice | ✅ 可用 | (无) |
| dsh-vsc-integration | ✅ 可用 | (无) |
| dsh-wallpaper | ✅ 可用 | (无) |
| dsh-waterball-pet | ✅ 可用 | (无) |
| dsh-web-archive | ✅ 可用 | (无) |
| dsh-web-attention-badge | ✅ 可用 | (无) |
| dsh-web-background | ✅ 可用 | (无) |
| dsh-web-plugin-manager | ✅ 可用 | (无) |
| dsh-web-search-brave | ✅ 可用 | (无) |
| dsh-web-search-pro | ✅ 可用 | (无) |
| dsh-web-search-tavily | ✅ 可用 | (无) |
| dsh-web-speech-input | ✅ 可用 | (无) |
| dsh-web-terminal | ✅ 可用 | (无) |
| dsh-web-ui-approval-notify | ✅ 可用 | (无) |
| dsh-web-ui-notify | ✅ 可用 | (无) |
| dsh-webfetch | ✅ 可用 | (无) |
| dsh-webhook-bridge | ✅ 可用 | (无) |
| dsh-webui-auth | ✅ 可用 | (无) |
| dsh-webUI-Glass-Theme | ✅ 可用 | (无) |
| dsh-webui-market-plugin | ✅ 可用 | (无) |
| dsh-wecom | ✅ 可用 | (无) |
| dsh-whale-girl-tauri | ✅ 可用 | (无) |
| dsh-whale-pet | ✅ 可用 | (无) |
| dsh-width-tiers | ✅ 可用 | (无) |
| dsh-wordbox | ✅ 可用 | (无) |
| dsh-worktrees | ✅ 可用 | (无) |
| dsh-yali-image-generator | ✅ 可用 | (无) |
| dsh2wechat | ✅ 可用 | (无) |
| dshbase-catalog | ✅ 可用 | (无) |
| DSHDesktop | ✅ 可用 | (无) |
| embedded-workbench | ✅ 可用 | (无) |
| fabric | ✅ 可用 | (无) |
| feishu-local-agent-bridge-windows | ✅ 可用 | (无) |
| flomo-dsh-plugin | ✅ 可用 | (无) |
| focal-dsh | ✅ 可用 | (无) |
| forkprobe | ✅ 可用 | (无) |
| free-vision-skill | ✅ 可用 | (无) |
| function-testing | ✅ 可用 | (无) |
| galgame-dsh-plugin | ✅ 可用 | (无) |
| group-chat-diary | ✅ 可用 | (无) |
| harness-code | ✅ 可用 | (无) |
| harness-doctor | ✅ 可用 | (无) |
| harnessproof | ✅ 可用 | (无) |
| jina-web-search-dsh-plugin | ✅ 可用 | (无) |
| long-draft-input | ✅ 可用 | (无) |
| mindspace-dsh-local-rag | ✅ 可用 | (无) |
| modlens | ✅ 可用 | (无) |
| modsearch | ✅ 可用 | (无) |
| moon-lovers-skill | ✅ 可用 | (无) |
| noatmark-dsh-plugin | ✅ 可用 | (无) |
| oh-dsh-desktop | ✅ 可用 | (无) |
| omdp | ✅ 可用 | (无) |
| omdsh-runtime | ✅ 可用 | (无) |
| opencode-usage | ✅ 可用 | (无) |
| OpenFlowFrames | ✅ 可用 | (无) |
| paste-to-workspace | ✅ 可用 | (无) |
| pi2dsh | ✅ 可用 | (无) |
| plugin-template | ✅ 可用 | (无) |
| prompt-polish | ✅ 可用 | (无) |
| quantum-practices | ✅ 可用 | (无) |
| repo-visibility-guard | ✅ 可用 | (无) |
| reSanity | ✅ 可用 | (无) |
| sandbase-harness | ✅ 可用 | (无) |
| sandbox-nono | ✅ 可用 | (无) |
| securstack-dsh-plugin | ✅ 可用 | (无) |
| superpowers-dsh | ✅ 可用 | (无) |
| task-passport | ✅ 可用 | (无) |
| timem-dsh-memory | ✅ 可用 | (无) |
| timemspace-dsh-memory | ✅ 可用 | (无) |
| toybox | ✅ 可用 | (无) |
| trio | ✅ 可用 | (无) |
| uiopt | ✅ 可用 | (无) |
| upstream-radar | ✅ 可用 | (无) |
| visionDS | ✅ 可用 | (无) |
| vocaloid-mcp | ✅ 可用 | (无) |
| VoiceLens | ✅ 可用 | (无) |
| weshop-dsh-plugin | ✅ 可用 | (无) |
| whale-girl | ✅ 可用 | (无) |
| wps-dsh-plugin | ✅ 可用 | (无) |
| ya-workspace-sidebar | ✅ 可用 | (无) |

## ❌ 不兼容（124）

| 插件 | 结论 | 原因 |
|---|---|---|
| 7d7d | ❌ 不兼容 | FAIL: 缺少 DSH SDK（`~/.dsh/source/current` 不存在），`link:` 本地依赖无法解析，且 `lib/` 未构建。 |
| adhd-one | ❌ 不兼容 | FAIL: ADHD One is a Windows-only Electron desktop app, not a dsh plugin — Electron can't load in this Linux headless environment. |
| context-doctor | ❌ 不兼容 | FAIL: peer dependency @deepseek-ai/cordis 无法在当前环境安装（npm 仓库中不存在该包，非公开 npm 包） |
| DCode | ❌ 不兼容 | FAIL: DCode is a standalone Electron app with no dsh plugin configuration (no dsh patch files, no dsh references in package.json), cannot be |
| deepseek-harness-cli | ❌ 不兼容 | FAIL: 插件依赖 workspace:^ 内部的 monorepo 包，缺少 deepseek-harness 根仓库导致无法解析依赖 |
| Deepseek-Harness-Desktop | ❌ 不兼容 | FAIL: npm install 失败（目录权限问题）且 electron 模块未安装，导致插件无法加载 |
| deepseek-harness-desktop-windows | ❌ 不兼容 | FAIL: 项目依赖 Electron（Windows GUI 框架），当前为 Linux 无头环境，无法运行 Electron 应用。 |
| deepseek-harness-flow | ❌ 不兼容 | FAIL: 缺少运行时依赖 @deepseek-ai/dsh-typert-protocol 和 @deepseek-ai/dsh（非独立 npm 包，无法解析） |
| DeepSeek-Harness-linux- | ❌ 不兼容 | FAIL: 缺少运行时依赖 @deepseek-ai/dsh-settings，无法加载 |
| deepseek-harness-shell | ❌ 不兼容 | FAIL: @deepseek-ai/dsh npm包无法安装（缓存目录权限问题 + 安装超时），插件不能加载。 |
| desktop | ❌ 不兼容 | FAIL: build:dsh 需从 GitHub 克隆 DSH 源码但网络不可用，npm 上的 @deepseek-ai/* 包不存在或无法访问。 |
| distill | ❌ 不兼容 | FAIL: peer dependencies (@deepseek-ai/schemastery 等) 无法安装——npm 缓存目录权限被拒，且沙箱阻止在 /clones/distill 创建 node_modules。 |
| dsh-101 | ❌ 不兼容 | FAIL: peer dependencies (e.g. @deepseek-ai/dsh-paths) not resolvable when loaded standalone |
| dsh-a2a | ❌ 不兼容 | FAIL: workspace:^ dependencies require full DSH monorepo pnpm workspace; no prebuilt lib/ exists in isolation. |
| dsh-adaptive-subagent-report | ❌ 不兼容 | FAIL: index.mjs 入口文件不存在，插件源码未实现 |
| dsh-agent-teams | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/schemastery 是内部包，无法从 npm 安装，导致 ES 模块导入失败 |
| dsh-apple-mode | ❌ 不兼容 | FAIL: 该插件是纯配置型 DSH 插件（无 JS 入口），安装依赖 macOS + Xcode，当前运行环境为 Linux，无法加载。 |
| dsh-archived-conversations | ❌ 不兼容 | FAIL: 缺少 peerDependency `@deepseek-ai/dsh-typert-protocol`，且目录为只读无法安装依赖。 |
| dsh-ark-quota | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/schemastery@0.1.0-rc.6 在 npm 上不存在，无法安装依赖导致模块加载失败 |
| dsh-assembler | ❌ 不兼容 | FAIL: 缺少 DSH 内部 peer 依赖 (@deepseek-ai/cordis、@deepseek-ai/dsh-llm 等)，构建和加载均失败。 |
| dsh-at-file | ❌ 不兼容 | FAIL: plugin lib/index.js has non-type runtime imports from @deepseek-ai/dsh-typert-protocol, @deepseek-ai/dsh-settings, @deepseek-ai/dsh-ll |
| dsh-auto-approval | ❌ 不兼容 | FAIL: 缺少 @deepseek-ai/dsh-settings 依赖，无法加载 |
| dsh-auto-chess | ❌ 不兼容 | FAIL: npm缓存目录权限问题（EACCES），无法安装依赖，因此插件无法加载。 |
| dsh-automation | ❌ 不兼容 | FAIL: lib/index.js 依赖私有包 `@deepseek-ai/schemastery`，无法安装和加载 |
| dsh-bash-rtk | ❌ 不兼容 | FAIL: 项目依赖 link: 协议指向不存在的 deepseek-harness，且 lib/ 未构建，npm install 失败 |
| dsh-capability-inspector | ❌ 不兼容 | FAIL: 依赖 `@deepseek-ai/dsh-tools` 和 `@deepseek-ai/cordis` 为本地 link 路径，但对应的 deepseek-harness 源码不存在，导致模块无法加载。 |
| dsh-cc-connect | ❌ 不兼容 | FAIL: peer 依赖 schemastery 和 @deepseek-ai/dsh-tools 是 dsh 内部包，npm 上不存在，无法安装依赖，加载失败 |
| dsh-checkpoint | ❌ 不兼容 | FAIL: 源码未编译（无lib/输出），且依赖使用workspace协议需monorepo环境，peer deps无法解析。 |
| dsh-claude-theme | ❌ 不兼容 | FAIL: 沙箱权限限制导致无法在 ~/.dsh/profiles/web 创建配置文件，且插件依赖 `@deepseek-ai/dsh-settings`（内部包）无法通过独立 node -e require 加载 |
| dsh-codex-bridge | ❌ 不兼容 | FAIL: 缺少 dsh 平台 peer 依赖 @deepseek-ai/dsh-tools（需完整 dsh 环境） |
| dsh-config-watch | ❌ 不兼容 | FAIL: 插件代码引用 `@deepseek-ai/dsh-tools`，但该依赖未声明在 package.json 中，导致安装后也无法解析 |
| dsh-context-viewer | ❌ 不兼容 | FAIL: Electron 未正确安装（跳过二进制下载后依赖缺失，无法加载） |
| dsh-cost-display | ❌ 不兼容 | FAIL: 缺少 peer 依赖（@deepseek-ai/schemastery、@deepseek-ai/cordis、react 未安装，且插件目录为只读无法安装） |
| dsh-cost-tracker | ❌ 不兼容 | FAIL: 缺少 peer 依赖（@deepseek-ai/cordis 等内部包未安装） |
| dsh-custom-css | ❌ 不兼容 | FAIL: 构建产物 lib/ 不存在且无法安装依赖（只读文件系统，无法创建 node_modules） |
| dsh-data-agent | ❌ 不兼容 | FAIL: 插件依赖的 8 个 `@deepseek-ai/*` peer deps（dsh-client-locale、dsh-client-runtime、dsh-client-ui-conversation、dsh-client-ui-slots、dsh-host-webs |
| dsh-deep-research | ❌ 不兼容 | FAIL: 缺少 peer 依赖 `@deepseek-ai/dsh-tools` 和 `@deepseek-ai/dsh-workflow`（这些包由 DSH 宿主环境提供，不在 npm 上，独立安装时无法解析） |
| dsh-deepresearch | ❌ 不兼容 | FAIL: peer dependencies are internal @deepseek-ai packages not resolvable on public npm, plus workspace lacks write permissions for .dsh and |
| dsh-delegate | ❌ 不兼容 | FAIL: peerDependencies (@deepseek-ai/dsh-client-runtime, dsh-subagent, dsh-tools, schemastery) 为私有包，npm registry 404，无法独立加载。 |
| dsh-diff-viewer | ❌ 不兼容 | FAIL: 源码未编译（lib/ 目录不存在），且 devDependencies 中的 link: 本地路径依赖在当前环境无法解析 |
| dsh-feishu-bridge | ❌ 不兼容 | FAIL: tsdown build 失败，缺少 @babel/helper-validator-identifier 依赖，无法产出 dist/index.js |
| dsh-feishu-gateway | ❌ 不兼容 | FAIL: 源码包未预编译（lib/不存在）且工作区为只读导致无法构建，另peer依赖需DSH宿主环境提供 |
| dsh-gateway-config | ❌ 不兼容 | FAIL: 依赖 `@deepseek-ai/dsh-tools` 未安装且环境中不存在该包，无法加载。 |
| dsh-git-branch-switcher | ❌ 不兼容 | FAIL: 缺少私有依赖 @deepseek-ai/dsh-typert-protocol |
| dsh-git-credentials | ❌ 不兼容 | FAIL: 依赖版本(@deepseek-ai/cordis@0.1.0-rc.5)在npm不存在、未设DSH_REPO指向harness仓库，且构建产物lib/缺失导致入口lib/index.js不存在 |
| dsh-her-eyes | ❌ 不兼容 | FAIL: 插件依赖平台内部包 @deepseek-ai/dsh-tools，脱离 dsh 平台环境无法加载 |
| dsh-hotkeys | ❌ 不兼容 | FAIL: link: 依赖指向不存在的内部 DSH 包（cordis、dsh-settings 等），且 pnpm 未安装 |
| dsh-http-probe | ❌ 不兼容 | FAIL: @deepseek-ai/dsh-tools@0.1.0-rc.5 未发布到 npm，peer 依赖无法解析，源码安装被阻塞 |
| dsh-image-to-path | ❌ 不兼容 | FAIL: peer 依赖 @deepseek-ai/dsh-session 等缺失，npm install 因权限/目录问题无法完成，require 时报 Cannot find package |
| dsh-import-agents | ❌ 不兼容 | FAIL: 插件模块自身 `import('./plugin/index.mjs')` 加载成功，但 README 的安装方式需要将插件加入 dsh profile 的 `cordis.patch.yml` 并配合 dsh web 运行环境（peerDependencies 依赖 |
| dsh-kimi-bridge | ❌ 不兼容 | FAIL: 构建成功但独立加载失败——`@deepseek-ai/dsh-tools` 是 peerDependency，`npm install --omit=peer` 未安装该包，node -e require 时报 `ERR_MODULE_NOT_FOUND`；该插件需在 |
| dsh-kimi-browser | ❌ 不兼容 | FAIL: peer dependencies (schemastery, cordis, @deepseek-ai/dsh-*) 未发布到 npm，无法解析 |
| dsh-Kimi-WebBridge | ❌ 不兼容 | FAIL: 缺少运行时依赖 @deepseek-ai/dsh-tools，index.js import 时抛出 "Cannot find package" 错误 |
| dsh-literature | ❌ 不兼容 | FAIL: 缺少运行时依赖 `@deepseek-ai/schemastery`（devDependencies 中的 link 路径不存在） |
| dsh-live-stats | ❌ 不兼容 | FAIL: 依赖使用 link: 协议指向本地 deepseek-harness 路径，但该路径不存在且无预编译产物 lib/ |
| dsh-llm-fallbacks | ❌ 不兼容 | FAIL: dist/index.js 缺失，构建未完成（prepare 阶段因缺少 pnpm 而失败，dist 中仅有 .d.ts 无 .js） |
| dsh-llm-kiro | ❌ 不兼容 | FAIL: npm install 超时且 node_modules 为空，依赖（@deepseek-ai/schemastery 等 peer deps）缺失导致无法加载 |
| dsh-loop | ❌ 不兼容 | FAIL: 缺少内部依赖 `@deepseek-ai/dsh-tools`，无法解析模块 |
| dsh-mobile | ❌ 不兼容 | FAIL: 依赖使用 link: 协议指向不存在的 ../dsh2026/test-lehhair 路径，npm install 失败导致 lib/ 未构建，dsh 插件无法加载 |
| dsh-multica-runtime | ❌ 不兼容 | FAIL: 编译产物存在但运行时缺少传递依赖 @deepseek-ai/dsh-scope（dsh-session 间接引入），导致模块无法加载。 |
| dsh-notebooks | ❌ 不兼容 | FAIL: 缺少 peer 依赖（如 @deepseek-ai/cordis），且 npm install 因 ~/.npm 权限不足、dsh plugin 因 ~/.dsh 权限不足，均无法完成安装，模块无法加载。 |
| dsh-open-in-vscode | ❌ 不兼容 | FAIL: 缺少 dsh 源码依赖（link:../dsh/vendor/cordis 等路径不存在，peerDependencies 无法解析） |
| dsh-openbiliclaw | ❌ 不兼容 | FAIL: 缺少 @deepseek-ai/dsh-tools 等 DSH peer 依赖，无法独立加载 |
| dsh-ops-kit | ❌ 不兼容 | FAIL: peer dependency @deepseek-ai/dsh-tools not installed, require fails with "Cannot find package" |
| dsh-paseo | ❌ 不兼容 | FAIL: build fails — no dsh snapshot/monorepo found (needs DSH_MONOREPO set or dsh source at ~/.dsh/source/current) |
| dsh-plugin-clawrouters | ❌ 不兼容 | FAIL: 缺少 dsh 内部依赖包 (@deepseek-ai/dsh-credentials 等)，仅在 dsh 运行时环境存在，无法单独加载 |
| dsh-plugin-consult | ❌ 不兼容 | FAIL: cordis.yml 硬编码路径 `/mnt/shared-storage-user/chenguanxu/workspace/dsh/plugin-consult/src/index.ts` 不存在且 `@deepseek-ai/cordis` 依赖未安装 |
| dsh-plugin-overview | ❌ 不兼容 | FAIL: 缺少运行时依赖 @deepseek-ai/dsh-typert-protocol（需 DSH runtime node_modules junction 才能解析） |
| dsh-plugin-session-delete | ❌ 不兼容 | FAIL: ESM peer dependency @deepseek-ai/dsh-tools 无法解析（项目无 node_modules，且沙箱阻止 npm install 和 symlink 创建） |
| dsh-plugin-subagent-director | ❌ 不兼容 | FAIL: npm install 失败 — 所有 peerDependencies 的 `file:` 路径指向不存在的 DeepSeekHarness/node_modules/@deepseek-ai/*，导致依赖无法解析 |
| dsh-plugin-text-translation | ❌ 不兼容 | FAIL: peer dependencies (@deepseek-ai/dsh-tools, @deepseek-ai/cordis, @deepseek-ai/schemastery) not installed — plugin requires a DSH profil |
| dsh-plugin-token-billing | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/dsh-settings、dsh-credentials、schemastery 为 DSH 内部私有包，不在公共 npm 上，无法独立安装和加载 |
| dsh-plugin-yet-another-subagent | ❌ 不兼容 | FAIL: 无法安装依赖 — node_modules 目录不可创建（只读文件系统），且 schemastery 等 peer 依赖缺失导致导入失败。 |
| dsh-project-wiki | ❌ 不兼容 | FAIL: 缺少内部依赖包 @deepseek-ai/schemastery，该包非开源，需 DSH 平台环境才能解析 |
| dsh-provider-model-configurator | ❌ 不兼容 | FAIL: 缺少 peer 依赖 `@deepseek-ai/dsh-typert-protocol`（预构建产物 `lib/index.js` 在 import 时直接引用，非可选运行时降级） |
| dsh-qq2006 | ❌ 不兼容 | FAIL: lib/ 未编译且 peerDependencies（@deepseek-ai/dsh-client-ui-theme 等）为内部包，npm 上不存在，无法独立加载 |
| dsh-reloader | ❌ 不兼容 | FAIL: 缺少 peer 依赖 @deepseek-ai/dsh-tools（DSH 平台包，无法在外部环境中解析） |
| dsh-remote-web-ui | ❌ 不兼容 | FAIL: 缺少 sibling DSH 源码仓导致 prepare 构建失败（lib/ 未生成），且 peer 依赖（@deepseek-ai/dsh-*、cordis）无法从 npm 解析 |
| dsh-review-loop | ❌ 不兼容 | FAIL: 缺少 @deepseek-ai/dsh-llm 等 peer 依赖（package.json 中 devDependencies 的 link 路径指向 /home/wxr，当前环境不存在） |
| dsh-rewind | ❌ 不兼容 | FAIL: lib/index.js 未编译存在，且依赖 workspace:^ monorepo 协议无法单独安装 |
| dsh-search-mcp | ❌ 不兼容 | FAIL: npm install 失败（/clones 目录为只读，无法创建 node_modules 安装依赖），导致模块加载时找不到 `@deepseek-ai/schemastery` 等依赖包。 |
| dsh-security-audit | ❌ 不兼容 | FAIL: 缺少 peer 依赖 `@deepseek-ai/dsh-tools`，且 /clones 目录为只读无法安装 npm 包。 |
| dsh-session-memory | ❌ 不兼容 | FAIL: 沙箱限制无法安装依赖（node_modules 不可写），模块加载因缺少 @deepseek-ai/schemastery 等依赖失败 |
| dsh-sidechain | ❌ 不兼容 | FAIL: 依赖使用 link: 指向本机 .dsh/source/current 路径，当前环境不存在该路径，npm install 失败且 lib/ 未构建 |
| dsh-stickers | ❌ 不兼容 | FAIL: 无法安装加载 — peerDependencies 使用 link: 协议需 pnpm 解析，且 dsh plugin add 在 .dsh 目录写入被拒绝 |
| dsh-stock-market | ❌ 不兼容 | FAIL: Peer dependencies (@deepseek-ai/cordis, @deepseek-ai/dsh-*) are required but unavailable — no DSH workspace linked. |
| dsh-suggested-replies | ❌ 不兼容 | FAIL: 缺少 DSH 平台内部依赖（如 @deepseek-ai/schemastery 等 peer deps），无法在独立 Node 环境中加载 |
| dsh-terminal-panel | ❌ 不兼容 | FAIL: 缺少依赖 @deepseek-ai/schemastery，且 npm install 因只读文件系统无法安装 |
| dsh-tool-calculator | ❌ 不兼容 | FAIL: 只读文件系统无法安装依赖，且 peer 依赖 @deepseek-ai/dsh-tools 未安装导致模块加载失败（需通过 dsh plugin 安装或在 monorepo workspace 环境中使用） |
| dsh-tool-csv | ❌ 不兼容 | FAIL: 缺少 peer 依赖 @deepseek-ai/dsh-tools，单独 require 无法解析（需通过 dsh plugin 安装到 profile 才能加载） |
| dsh-tool-json | ❌ 不兼容 | FAIL: Peer 依赖 @deepseek-ai/dsh-tools 为私有包，安装失败导致插件无法加载 |
| dsh-tool-markdown | ❌ 不兼容 | FAIL: 缺少 peer 依赖（@deepseek-ai/dsh-tools 等），独立加载失败 |
| dsh-tool-regex | ❌ 不兼容 | FAIL: 缺少 peer 依赖（@deepseek-ai/dsh-tools / dsh-invariants / cordis），这些是内部包在当前 npm 环境中无法安装，导致模块加载时报 Cannot find package。 |
| dsh-tool-time | ❌ 不兼容 | FAIL: peer dependency '@deepseek-ai/dsh-tools' not found and node_modules is read-only (无法安装依赖) |
| dsh-toolkit | ❌ 不兼容 | FAIL: 插件依赖 `@deepseek-ai/dsh-tools` 未安装（无 node_modules），且 npm install 和 dsh profile 创建均受限于只读文件系统/权限，无法完成加载。 |
| dsh-track | ❌ 不兼容 | FAIL: 缺少 DSH 平台依赖（~/.dsh/source/current 不存在、peerDependencies 为内部 @deepseek-ai 包、tsc 不可用导致构建失败） |
| dsh-vision | ❌ 不兼容 | FAIL: 缺少 peer 依赖 @deepseek-ai/dsh-tools、@deepseek-ai/cordis、@deepseek-ai/dsh-system-prompt，无法 resolve ES module 导入。 |
| dsh-vision-fix | ❌ 不兼容 | FAIL: peer dependencies @deepseek-ai/dsh-tools 和 @deepseek-ai/dsh-system-prompt 是 dsh 内部包，不在 npm 上，导致 import 失败。 |
| dsh-visionary | ❌ 不兼容 | FAIL: npm 安装依赖失败（权限不足，无法创建 node_modules 和写入 .npm-cache），且插件依赖 @deepseek-ai 内部包（cordis/dsh-llm/dsh-session 等），需通过 `dsh plugin add` 在 DSH harn |
| dsh-web-search-firecrawl | ❌ 不兼容 | FAIL: peer dependencies (@deepseek-ai/schemastery etc.) unavailable because npm install failed under sandbox restrictions |
| dsh-webbridge | ❌ 不兼容 | FAIL: peerDependencies @deepseek-ai/dsh-tools 等 dsh 内部包无法找到，npm install 失败 |
| dsh-win-terminal-inspector | ❌ 不兼容 | FAIL: npm install 失败，npm cache 目录权限问题 (ENOENT/EACCES)，无法安装 node-pty 等依赖。 |
| dsh-workspace-digest | ❌ 不兼容 | FAIL: 缺少 peerDependencies（@deepseek-ai/dsh-tools、@deepseek-ai/schemastery），npm install 因权限受限未能完成安装，require 时找不到依赖。 |
| dsh4vscode | ❌ 不兼容 | FAIL: 文件系统只读导致无法安装依赖和编译 TypeScript，out/extension.js 不存在，插件无法加载 |
| dsh_workflow | ❌ 不兼容 | FAIL: peer dependency `@deepseek-ai/schemastery` 未安装导致模块加载失败 |
| ego-browser | ❌ 不兼容 | FAIL: 缺少 DSH 内部依赖包 @deepseek-ai/dsh-tools（未发布到公共 npm registry，安装失败） |
| ex-setting | ❌ 不兼容 | FAIL: peer 依赖 @deepseek-ai/dsh-api-remotes@^0.0.1 等私有包在 npm 上不存在，无法安装和加载 |
| localharness | ❌ 不兼容 | FAIL: 文件系统只读（/clones 挂载为只读），无法运行 npm install 安装依赖，且源码为 TypeScript 未编译（out/main/index.js 不存在），缺少 Electron 运行环境，插件无法加载。 |
| logicprobe | ❌ 不兼容 | FAIL: 依赖包 @deepseek-ai/dsh-timeout 等不在 npm 注册表上（私有包），无法完成加载 |
| mimo-vision | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/schemastery 等 monorepo 内部包未发布到 npm，独立环境无法解析（README 自身说明"插件不能 npm install 独立安装"）。 |
| mindspace-dsh-session-memory | ❌ 不兼容 | FAIL: 无法安装依赖（node_modules 目录不可写，缺少预构建包） |
| mstar-workflow | ❌ 不兼容 | FAIL: 源码为纯 TypeScript (无 dist/) 需 `bun` 编译、peer deps (`@deepseek-ai/cordis` 等) 无法安装、`dsh` CLI 硬编码 `/home/node/.dsh/profiles/web` 无 sudo 无法创建 |
| project-blueprint | ❌ 不兼容 | FAIL: 缺少必需 peer 依赖 `@deepseek-ai/dsh-skill-filesystem`（npm 上不存在，无法加载） |
| Qwen-MM-Plugins | ❌ 不兼容 | FAIL: 依赖的 @deepseek-ai/dsh-* peer 包为内部包，npm 无法找到对应版本；且 lib/ 未构建（无 pnpm 无法执行 tsc build）。 |
| sandbox-micro | ❌ 不兼容 | FAIL: 无法加载——lib/ 目录不存在（未构建），且 peerDependencies 中的 @deepseek-ai/dsh-invariants 等依赖在 npm 上不存在，需_sibling 源码仓库。 |
| sandbox-mxc | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/dsh-invariants 等 DSH 内部包和 @dsh-external/mxc-sdk（需 GitHub Packages 认证）无法解析，且源码未编译（无 lib/ 目录） |
| session-persistence-rdb | ❌ 不兼容 | FAIL: peer dependencies on internal @deepseek-ai packages are not resolvable; TypeScript entry not directly executable without full dsh buil |
| telegram | ❌ 不兼容 | FAIL: peerDependencies (@deepseek-ai/dsh-agent, dsh-llm, dsh-session, cordis, schemastery) 为内部包，npm 注册表不可用，模块无法加载 |
| tonghuashun-webui | ❌ 不兼容 | FAIL: 沙箱为只读文件系统，无法写入 node_modules 目录，npm install 失败导致插件无法加载。 |
| turtle-ui | ❌ 不兼容 | FAIL: 依赖 @deepseek-ai/dsh-agent 等 peer 包不存在于 npm registry，且缺少 sibling deepseek-harness 源码，无法独立安装和构建。 |
| ui-status-label | ❌ 不兼容 | FAIL: 无法安装 peer 依赖（@deepseek-ai/dsh-settings 等），且文件系统只读导致 npm install 失败 |
| web-components | ❌ 不兼容 | FAIL: peer dependencies (`@deepseek-ai/dsh-client-locale`, `@deepseek-ai/dsh-client-runtime`, `@deepseek-ai/dsh-client-ui-slots`, `@deepseek |
| zotero-harvest | ❌ 不兼容 | FAIL: peerDependency `@deepseek-ai/dsh-tools@^0.0.1` no matching version in npm registry (only `0.0.1-rc.5` / `0.1.0-rc.*` exist); manual `l |
| zotero-wave-rag | ❌ 不兼容 | FAIL: peer依赖 `@deepseek-ai/dsh-tools@^0.0.1` 在 npm 上不存在，无法安装依赖 |
