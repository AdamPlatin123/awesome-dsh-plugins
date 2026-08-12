# 实际兼容性验证：编译验证（2026-08-10 全量）

- 方法：插件源码 symlink 进 mainline workspace（snapshots/20260809T140917Z-a6bb5a95ba）→ tsc --noEmit
- 覆盖：183 克隆仓（TS 插件 98 / 非插件排除 85）

## 汇总

9, 失败 89

## 失败清单（首个错误）

| 插件 | 首个错误 |
|---|---|
| chat-width | TS2307: Cannot find module '@deepseek-ai/dsh-client-ui-slots' or its correspondi
| cross-harness-cite | TS6053: File '/home/adam/dsh-external-research/.mainline-build/packages/tools/lo
| distill | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-101 | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-a2a | TS6053: File '/home/adam/dsh-external-research/.mainline-build/packages/ui/comma
| dsh-acp | TS2339: Property 'requestCancelled' does not exist on type 'typeof RequestError'
| dsh-activity-plugin | TS2307: Cannot find module 'react' or its corresponding type declarations.
| dsh-ads | TS2591: Cannot find name 'node:child_process'. Do you need to install type defin
| dsh-alphasolve | TS2307: Cannot find module '@deepseek-ai/dsh-atomic-write' or its corresponding 
| dsh-artifact | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-auto-approval | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-auto-blame | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| dsh-bash-encoding | TS2307: Cannot find module '@deepseek-ai/dsh-bash' or its corresponding type dec
| DSH-better-sidebar | TS2307: Cannot find module 'react' or its corresponding type declarations.
| dsh-cc-tui | TS2307: Cannot find module 'cli-highlight' or its corresponding type declaration
| dsh-change-ledger | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-client-ui-plan-execute | TS6053: File '/home/adam/dsh-external-research/.mainline-build/packages/tools/ru
| dsh-companion | TS5101: Option 'baseUrl' is deprecated and will stop functioning in TypeScript 7
| dsh-crew | TS2307: Cannot find module 'commander' or its corresponding type declarations.
| dsh-custom-css | TS2307: Cannot find module '@deepseek-ai/dsh-client-ui-primitives' or its corres
| dsh-desktop-electron | TS2307: Cannot find module 'electron' or its corresponding type declarations.
| dsh-drag-and-drop | TS2307: Cannot find module '@deepseek-ai/dsh-client-runtime/client' or its corre
| dsh-engram-relay | TS2307: Cannot find module '@deepseek-ai/dsh-llm' or its corresponding type decl
| dsh-evolve | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-feishu-notify | TS2307: Cannot find module 'schemastery' or its corresponding type declarations.
| dsh-genui | TS5101: Option 'baseUrl' is deprecated and will stop functioning in TypeScript 7
| dsh-gh-bridge | TS2307: Cannot find module 'yaml' or its corresponding type declarations.
| dsh-git-graph | TS6053: File '/home/adam/dsh-external-research/.mainline-build/packages/tools/te
| dsh-input-history | TS2307: Cannot find module '@deepseek-ai/dsh-client-runtime/client' or its corre
| dsh-involute | TS2688: Cannot find type definition file for 'node'.
| dsh-live-stats | TS2307: Cannot find module 'react' or its corresponding type declarations.
| dsh-llm-fallbacks | TS2688: Cannot find type definition file for 'bun-types'.
| dsh-memory-evolve | TS2307: Cannot find module 'react' or its corresponding type declarations.
| dsh-message-edit | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| dsh-mineru | TS2307: Cannot find module 'react' or its corresponding type declarations.
| dsh-nowledge-mem | TS2307: Cannot find module '@deepseek-ai/dsh-agent' or its corresponding type de
| dsh-pi-adapter | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-plugin-check | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-prompt-studio | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| dsh-qq2006 | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-remote-web-ui | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| dsh-serenity-plugin | TS2307: Cannot find module 'zod' or its corresponding type declarations.
| dsh-session-cluster | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-session-health | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-session-search | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-sfw | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-sidechain | TS2307: Cannot find module '@deepseek-ai/dsh-commands' or its corresponding type
| dsh-side-panel | TS2307: Cannot find module 'dompurify' or its corresponding type declarations.
| dsh-skill-stats | TS5101: Option 'baseUrl' is deprecated and will stop functioning in TypeScript 7
| dsh-split-panes | TS5101: Option 'baseUrl' is deprecated and will stop functioning in TypeScript 7
| dsh-spur | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| dsh-stickers | TS2307: Cannot find module '@deepseek-ai/dsh-client-ui-conversation/client' or i
| dsh-task-board | TS5101: Option 'baseUrl' is deprecated and will stop functioning in TypeScript 7
| dsh-tavern-plugin | TS2591: Cannot find name 'node:fs/promises'. Do you need to install type definit
| dsh-tool-calculator | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-tool-csv | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-tool-diff | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-tool-encoding | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-tool-json | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-toolkit | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-tool-markdown | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-tool-regex | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-tool-time | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-tps | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| dsh-tui-front-door | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| dsh-turn-rewind | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-ui-progress | TS2307: Cannot find module '@deepseek-ai/dsh-client-ui-primitives' or its corres
| dsh-ui-whale | TS2307: Cannot find module 'react' or its corresponding type declarations.
| dsh-vision | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-visualize | TS2304: Cannot find name 'TextEncoder'.
| dsh-vscode | TS2688: Cannot find type definition file for 'vscode'.
| dsh-web-archive | TS5097: An import path can only end with a '.ts' extension when 'allowImportingT
| dsh-webbridge | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| dsh-web-panel | TS2307: Cannot find module 'react' or its corresponding type declarations.
| dsh-web-terminal | TS2307: Cannot find module 'react' or its corresponding type declarations.
| dsh-web-ui-approval-notify | TS2688: Cannot find type definition file for 'react'.
| dsh-web-ui-notify | TS2688: Cannot find type definition file for 'react'.
| ego-browser | TS2307: Cannot find module '@deepseek-ai/dsh-tools' or its corresponding type de
| ex-setting | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| fabric | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| Qwen-MM-Plugins | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| sandbox-micro | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| sandbox-mxc | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| session-chatlog | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| telegram | TS2307: Cannot find module 'cordis' or its corresponding type declarations.
| turtle-ui | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| web-components | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| yet-another-subagent | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packa
| zotero-harvest | TS2688: Cannot find type definition file for 'node'.
