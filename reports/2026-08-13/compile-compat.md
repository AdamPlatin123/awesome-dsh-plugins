# 实际兼容性验证：编译验证（2026-08-13）

- 方法：插件源码 symlink 进 mainline workspace（snapshots/HEAD）→ `tsc --noEmit`
- 结论：编译失败 = 100% 不兼容；编译通过 = 类型层兼容

## 汇总

- 候选 TS 167：**通过 20 / 失败 28 / 跳过 119**
- 候选 JS 0：**通过 1 / 失败 0**（node --check 语法级）
- 非插件/无源码（标注排除）：124
- 覆盖：3505 克隆仓全部纳入

## JS 语法失败清单

（无）

## 编译失败清单（实际不兼容）

| 插件 | 首个错误 |
|---|---|
| 7d7d | TS2307: Cannot find module 'react' or its corresponding type declarations. |
| cross-harness-cite | TS6053: File '/home/adam/dsh-external-research/.mainline-build/packages/tools/locale' not  |
| deepseek-manners | TS2688: Cannot find type definition file for 'node'. |
| dsh-a2a | TS6053: File '/home/adam/dsh-external-research/.mainline-build/packages/tasks/tasks' not f |
| dsh-acp | TS2339: Property 'requestCancelled' does not exist on type 'typeof RequestError'. |
| dsh-advisor | TS2307: Cannot find module '@deepseek-ai/dsh-llm' or its corresponding type declarations. |
| dsh-aigc-canvas | TS2307: Cannot find module 'react' or its corresponding type declarations. |
| dsh-auto-chess | TS2307: Cannot find module 'react' or its corresponding type declarations. |
| dsh-bash-encoding | TS2307: Cannot find module '@deepseek-ai/dsh-bash' or its corresponding type declarations. |
| DSH-better-sidebar | TS2307: Cannot find module 'node-pty' or its corresponding type declarations. |
| dsh-browser-panel | TS2307: Cannot find module 'playwright-core' or its corresponding type declarations. |
| dsh-cc-connect | TS2307: Cannot find module 'cordis' or its corresponding type declarations. |
| dsh-change-ledger | TS2307: Cannot find module 'cordis' or its corresponding type declarations. |
| dsh-chat-thumb | TS2307: Cannot find module 'schemastery' or its corresponding type declarations. |
| dsh-checkpoint | TS6053: File '/home/adam/dsh-external-research/.mainline-build/packages/support/invariants |
| dsh-code-map | TS2307: Cannot find module 'schemastery' or its corresponding type declarations. |
| dsh-codex-bridge | TS2307: Cannot find module 'react' or its corresponding type declarations. |
| dsh-companion | TS5101: Option 'baseUrl' is deprecated and will stop functioning in TypeScript 7.0. Specif |
| dsh-crew | TS2307: Cannot find module 'commander' or its corresponding type declarations. |
| dsh-custom-css | TS2307: Cannot find module '@deepseek-ai/dsh-client-ui-primitives' or its corresponding ty |
| dsh-data-agent | TS2307: Cannot find module 'schemastery' or its corresponding type declarations. |
| dsh-deep-research | TS5083: Cannot read file '/home/adam/dsh-external-research/.mainline-build/packages/deepse |
| dsh-desktop-electron | TS2307: Cannot find module 'electron' or its corresponding type declarations. |
| dsh-diff-viewer | TS5101: Option 'baseUrl' is deprecated and will stop functioning in TypeScript 7.0. Specif |
| dsh-easy-ctx-manager | TS2307: Cannot find module '@deepseek-ai/cordis' or its corresponding type declarations. |
| dsh-engram-relay | TS2307: Cannot find module '@deepseek-ai/dsh-llm' or its corresponding type declarations. |
| dsh-evolve | TS2307: Cannot find module 'cordis' or its corresponding type declarations. |
| dsh-explain | TS5058: The specified path does not exist: 'packages/tools/dsh-explain/tsconfig.json'. |

## 编译通过（类型层兼容）

chat-width(lib) context-doctor(lib) distill(lib) dsh-101(lib) dsh-activity-plugin(lib) dsh-ads(lib) dsh-agent-budget(lib) dsh-alphasolve(lib) dsh-anti-ads dsh-artifact(lib) dsh-auto-approval(lib) dsh-auto-blame(lib) dsh-better-sidebar-plugin-office(lib) dsh-cc-tui(lib) dsh-computer-use(lib) dsh-conversation-share(lib) dsh-d399(lib) dsh-design(lib) dsh-drag-and-drop(lib) dsh-emoji(lib)
