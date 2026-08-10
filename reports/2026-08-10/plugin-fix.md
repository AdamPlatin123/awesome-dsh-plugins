# 插件修复自动化报告（2026-08-10）

- 模式：DRY-RUN（未写入）

## 1. baseUrl 弃用（TS5101）——自动修复 12

- dsh-companion(baseUrl=.)
- dsh-genui(baseUrl=.)
- dsh-memory-evolve(baseUrl=.)
- dsh-skill-stats(baseUrl=.)
- dsh-split-panes(baseUrl=.)
- dsh-task-board(baseUrl=.)
- ex-setting(baseUrl=.)
- fabric(baseUrl=.)
- Qwen-MM-Plugins(baseUrl=.)
- sandbox-micro(baseUrl=.)
- sandbox-mxc(baseUrl=.)
- web-components(baseUrl=.)

## 2. 缺类型包（TS2688）——建议 6

- pnpm add -D dsh-involute → @types/node
- pnpm add -D dsh-llm-fallbacks → @types/bun-types
- pnpm add -D dsh-vscode → @types/vscode
- pnpm add -D dsh-web-ui-approval-notify → @types/react
- pnpm add -D dsh-web-ui-notify → @types/react
- pnpm add -D zotero-harvest → @types/node

## 3. 第三方依赖缺失（TS2307）——建议 5

- pnpm add dsh-cc-tui → cli-highlight
- pnpm add dsh-crew → commander
- pnpm add dsh-gh-bridge → yaml
- pnpm add dsh-serenity-plugin → zod
- pnpm add dsh-side-panel → dompurify

## 4. 需人工修复（API 漂移类）1

- dsh-acp → TS2339: Property 'requestCancelled' does not exist on type 'typeof RequestError'
