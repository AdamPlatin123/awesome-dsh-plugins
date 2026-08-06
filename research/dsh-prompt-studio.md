# dsh-external/dsh-prompt-studio

## 一句话定位

DeepSeek Harness 的注册表分发插件，在对话页注册 **Prompt Studio** 标签页（`conversation.view` order=20，位于 Chat=0 / Trajectory=10 之后），把运行时原生 system 段、用户补充段、原生覆盖与「请求级一次性合成消息」统一到同一个可视化编辑器里实时编排。

## 技术栈与依赖

- **语言/模块**：TypeScript ESM（`target: es2024`），客户端 React + CSS Modules，宿主端基于 Cordis 插件框架，配置 schema 用 schemastery。
- **构建**：`scripts/build.mjs` → `tsc -b` 类型检查 + `tsdown` 双端打包（服务端自包含 ESM、客户端用 DSH 仓库的 `clientBundle` preset），产物 `index.mjs` / `client.js` / `client.js.map` 直接拷回插件根并提交。
- **测试**：`vitest run`（`scripts/test.mjs`），`pnpm run check = build && test`。
- **依赖解析方式特殊**：`package.json` 不声明任何 dependencies，构建/测试时由 `scripts/dsh-env.mjs` 把 `react` / `cordis` / `schemastery` / `@types` / `vitest` / `@testing-library` 软链到一个**已安装依赖并完成构建的 DSH 源码树**（`DSH_ROOT`，默认 `../dsh`），并软链 `.dsh → $DSH_ROOT`。脱离 DSH 源码树无法独立 typecheck/build/test。
- **宿主包**（均来自 DSH）：`@deepseek-ai/dsh-agent`、`dsh-llm`、`dsh-settings`、`dsh-system-prompt`、`dsh-client-runtime`、`dsh-client-connection`、`dsh-client-ui-slots`、`dsh-client-web-react`、`dsh-client-ui-conversation`。`engines.dsh >= 0.0.1`。
- **许可**：BSD-3-Clause（Copyright 2026 Moeblack）。

## 文件结构概览

| 路径 | 作用 |
|---|---|
| `dsh.plugin.json` | 插件清单：id `moeblack/prompt-studio`、main `./index.mjs`、client `./client.js`，client 注入 `dsh-client-runtime` + `dsh-client-ui-conversation`。 |
| `src/index.ts` (585 行) | 宿主半：可逆效果管线、运行时原生目录发现、原生覆盖、请求级合成注入、`/prompt-studio/state` 路由、模板变量。 |
| `src/shared.ts` (8.7KB) | `PromptComponent` 统一模型、校验、id 分配器、`buildDraftSystemComponents`、`renderSystemPreview`、`renderSupplementBoundary`。 |
| `src/config.ts` | 仅含 `components` 字段的 schemastery settings schema（live scope）。 |
| `src/client/index.ts` | 浏览器入口：注册 `conversation.view` 标签页 `prompt-studio`（order 20），监听 `settings/changed` / `connection/reset` 刷新。 |
| `src/client/store.ts` (7.9KB) | `PromptStudioStore`：`settings.describe` + `GET /prompt-studio/state` 拉取；`settings.mutate` 带 `expectedRevision` 乐观锁保存。 |
| `src/client/PromptStudioView.tsx` (515 行) | 统一列表编辑器 + 完整请求预览；中文 UI。 |
| `src/client/PromptStudioView.module.css` (9.5KB) | 编辑器样式。 |
| `scripts/{build,test}.mjs` + `scripts/dsh-env.mjs` | 双端构建/测试入口 + DSH 环境软链管理。 |
| `tsdown.config.ts` / `tsconfig.json` | 构建配置；`tsconfig` extends `.dsh/tsconfig.base.client.json`，project references 指向 `.dsh/vendor/{cordis,schemastery}` 与多个 `.dsh/packages/...`。 |
| `tests/` | `host.spec.ts`、`shared.spec.ts`、`store.spec.ts`、`apply.spec.ts`、`view.spec.tsx`、`registry-artifacts.spec.ts`、`styles.spec.ts`。 |
| `index.mjs` / `client.js` / `client.js.map` | 提交进仓库的构建产物（50.9KB / 45.4KB / 53.1KB）。 |

## 核心功能与实现要点

1. **统一二分组件模型**：每个 `PromptComponent` 用 `kind`（`native` 运行时只读 / `supplement` 用户可持久化）× `role`（system/user/assistant）× `position`（after_system/anchored/tail，仅非 system）× `order` 多维独立描述；`origin` 字段一旦指向某原生 id，该 supplement 即覆盖原生，**不设单独的 override kind**（`src/shared.ts:36-67`，`isNativeOverride` `src/shared.ts:88-91`）。

2. **可逆组合效果管线**：`ComponentPipeline.replace()` 每次设置变更先调用上一轮的 `recover()`，再通过 `ctx.effect()` 把整组组件作为一个 Cordis 生成器效果施加；marker、override 映射、supplement 映射各自 yield 原子逆，组合逆由 `ctx.effect()` 按结构合成（`src/index.ts:140-175`，`RuntimeBindings.activate` `src/index.ts:109-138`）。

3. **原生覆盖走 `system-prompt/assemble` waterfall**：覆盖组件注册为带 marker 名的有序 section；waterfall 中 `applyOverrides` 在 marker 与 origin 同时存在时移除原生段，启用的覆盖段按自身 `role`/`order` 像普通 supplement 一样进消息序列；`enabled=false` 时只摘除原生段（相当于关停）（`src/index.ts:177-205`，监听器 `src/index.ts:465-478` 以 `prepend: true` 注册保证捕获组装前后状态）。

4. **运行时原生目录动态发现**：不维护静态原生清单。监听 `system-prompt/change` 触发一次真实 `ctx.systemPrompt.assemble()`（带去抖循环 `requestRefresh`），waterfall 前后分别捕获原生 name/text 与组装后 system 槽序列，存入 `RuntimeCatalogStore`（按 JSON 串比较去重、revision 单调递增）；浏览器经同源 `GET /prompt-studio/state`（`no-store`）读取单值快照（`src/index.ts:238-265`，路由注册 `src/index.ts:437-463`）。

5. **请求级一次性合成消息**：`SupplementPlans` 在 assemble 时冻结本轮启用的非 system supplement 及其模板渲染结果，按 session 暂存；`llm/stream` 拦截器 `rewriteRequest` 只对「带 sessionId、无 purpose、frozen」的真实循环请求生效，`take()` 出计划后 `insertSupplements` 在 `after_system` / `anchored`（最后一条真实用户消息后，找不到锚点则跳过）/ `tail` 三处插入合成消息，相邻同 role 合并，最后用 `ctx.llm.stream(rewritten)` 重发——**只进本次模型请求，不写入会话记录**（`src/index.ts:283-413`）。

6. **模板变量实时求值**：支持 `{{user_input}}`（最后一条真实用户输入）、`{{model}}`（当前 Agent 模型）、`{{cwd}}`（会话工作目录），组装时从 `AssembleContext.agent` / `agent.session` / `agent.options` 现场读取，非保存时快照；`user_input` 另通过 `ctx.systemPrompt.variable` 暴露给原生组装（`src/index.ts:206-221`，`src/index.ts:460-463`）。

7. **浏览器端统一编辑器**：原生与已配置组件合并排序展示；脏标 `dirty` 时本地用 `buildDraftSystemComponents` 重算预览，未编辑则直接用宿主 assembled 快照；保存走 `settings.mutate` 带 `expectedRevision` 乐观锁，成功后重拉 catalog（`src/client/store.ts:88-110`，`src/client/PromptStudioView.tsx:155-265`）。v0.2.2 新增 assistant supplement 的 `blockType: 'reasoning'` 选项。

## 与 DeepSeek Harness 主仓库的集成点

- **安装链路**：`dsh plugin install /path/to/dsh-prompt-studio` → `dsh plugin enable moeblack/prompt-studio` → 重启 `dsh web`（命令行与运行中 Web 进程不共享内存）。启用索引由 DSH plugin registry 管理，默认禁用。
- **宿主端 inject**：`['settings', 'systemPrompt', 'llm']`，另按需 inject `httpServer`。注册 live settings namespace `'prompt-studio'`（仅持久化 `components`），调用 `ctx.settings.register` / `ctx.systemPrompt.{section, variable, assemble}` / `ctx.llm.stream`。
- **宿主端事件**：`system-prompt/assemble`（`prepend: true`，用于捕获前后快照与覆盖）、`system-prompt/change`（触发重算）、`llm/stream`（请求改写）。
- **HTTP**：`ctx.httpServer.register` 注册 exact 路由 `GET /prompt-studio/state`。
- **客户端 inject**：`['slots', 'conversation', 'connection']`；`ctx.slots.register` 注册 `conversation.view` 标签页；复用 `dsh-client-runtime` 的 `createSnapshotStore` / `bindSnapshotSelector`，`dsh-client-connection` 的 `settings.describe` / `settings.mutate` RPC。
- **构建耦合**：`tsdown.config.ts` 引用 `./.dsh/packages/client/tsdown.client.ts` 的 `clientBundle`；`tsconfig.json` extends `.dsh/tsconfig.base.client.json` 并 project-reference 一堆 `.dsh/packages/*` —— 强耦合已构建的 DSH 源码树。
- **运行时前提**（README 明示）：浏览器端读写 `prompt-studio` 配置段需宿主在 `PRODUCT_SETTINGS_NAMESPACES` 公开 `'prompt-studio'`，当前 DSH 官方 plugin-registry 集成环境已包含。

## 亮点与风险

**亮点**

- 可逆组合效果设计干净，设置变更走「disposer + 重施整组」原子语义；覆盖与 supplement 共用同一模型，没有特殊分支。
- 运行时动态发现原生目录（监听 `system-prompt/change` 真实重算），避免维护易腐化的静态原生清单。
- 请求级合成消息通过 `llm/stream` 既有接缝生成一次性副本，不污染会话记录，覆盖语义清晰。

**风险**

- **测试套件与 v0.2.2 源码严重不同步（重要）**：`tests/host.spec.ts:5-6,19,33`、`tests/shared.spec.ts:3-14`、`tests/store.spec.ts:10-11,33-43` 导入并使用**已不存在**的符号 —— `BUILTIN_SECTIONS` / `buildPreviewSections` / `nextSectionName` / `renderPreview` / `resolveBuiltinSections` / `validateBuiltinOverrides` / `validateStudioSections` / 类型 `BuiltinSectionOverride` / `StudioSection`，并使用旧的 `{ sections, overrides }` schema；当前 `src/shared.ts` 只导出 `PromptComponent` / `components` API。三处 spec 在「TS 编译 / 运行时导入 / 断言期望」三个层面都会失败，`pnpm run check` 的 test 步骤必然不通过。仅 `tests/apply.spec.ts` 与 `tests/view.spec.tsx` 与新 API 一致。
- **版本号不一致**：`package.json:4` 与 `dsh.plugin.json:3` 均为 `"version": "0.1.0"`，但唯一 commit 标题为 `v0.2.2: ...`，manifest 与发版标签错位。
- **构建产物入库**：`index.mjs`（50.9KB）、`client.js`（45.4KB）、`client.js.map`（53.1KB）直接提交，与 `src/` 并存，易出现产物与源码漂移（当前 `client.js.map` 的 `sourcesContent` 已是 v0.2.2 源码，但需手动保持同步）。
- **模板变量缺失即抛错**：`renderComponentTemplate`（`src/index.ts:214-216`）遇到未定义变量名直接 `throw`；首轮尚未有 `user_input` 时若 supplement 引用了它，可能阻塞整轮 assemble，依赖宿主侧容错。
- **命名/归属不一致**：插件 id 与 README 标题仍为 `moeblack/prompt-studio`，git remote 已是 `dsh-external/dsh-prompt-studio`，LICENSE 署名 Moeblack —— 迁入 dsh-external org 后未统一品牌。
- **强宿主耦合**：无独立 `node_modules`，构建/类型检查/测试全部依赖一份本地完整构建的 DSH 源码树（`DSH_ROOT`），独立 CI 不可行。

## 维护状态

- 仓库刚从个人账号 `moeblack/prompt-studio` 迁入 `dsh-external` org 并更名为 `dsh-prompt-studio`（LICENSE 署名、插件 id 仍保留 moeblack）。
- shallow clone 仅可见 **1 个 commit**：`9885643` `v0.2.2: assistant 补充可选 reasoning 块（blockType）；UI 删说明文字、预览 supplement 用 CSS 视觉区分…`，时间 **2026-08-06 09:29:10 +0800**（调研当天）。结合 commit 标题里的 v0.2.2，迁入时显然做过 squash，外部有过更早迭代历史。
- 29 个 git 跟踪文件；`package.json` `private: true`，不发布 npm。
- 处于活跃但早期阶段，且测试/版本治理尚未跟上 v0.2.2 的源码迭代。

## 备注

- 浏览器端为简体中文 UI（「新增补充」/「保存更改」/「系统后」/「最后用户输入后」/「请求尾部」/「原生」/「补充」）。
- 与主仓库是纯插件关系，无对本仓的代码反写；功能定位类似 Claude Code 风格的 prompt 编辑器，但深度接入 DSH 的 `system-prompt` 组装管线与 `llm/stream` 改写缝。
- 调研未发现 CI 配置（无 `.github/`），测试治理目前只能靠本地 `pnpm run check`，而该命令当前因测试套件陈旧会失败。
