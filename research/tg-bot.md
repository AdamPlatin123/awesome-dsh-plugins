# tg-bot 调研摘要

## 一句话定位

`dsh-external/tg-bot` 是 DeepSeek Harness 的一个 **opt-in Telegram 远程通道插件**：把授权的 Telegram 聊天嫁接到 `dsh web` 进程上，让手机端的 Telegram 与浏览器里的 Web GUI 共享同一批 agent 会话——发送 prompt 走宿主的 `ApiProxy` 接口，流式回复和 `ask-user-question` 交互问题回传为 Telegram 消息与 inline keyboard。源码形态分发（不是独立可运行的 bot），需要 cp 进 DSH 检出版本并 `git apply` 一份 host patch 才能激活。

## 技术栈与依赖（语言、框架、关键依赖）

- **语言/运行时**：TypeScript（ESM），Node `^22.19 || >=24`，pnpm `11.7.0`。
- **插件框架**：[Cordis](https://cordis.js.org/) `^4.0.0-rc.7`（`name` / `inject` / `Config` / `apply` 函数插件约定，`ctx.effect` / `ctx.plugin` / 服务注入 `apiProxy`、`settings`、`invariants`）。
- **配置 schema**：`schemastery ^3.18.0`（`z.object(...)`、`z.string().role('secret')` 等）。
- **DSH 内部 peer 包**（workspace，运行期由宿主提供）：
  - `@deepseek-ai/dsh-host-apiproxy`（RPC 网关：`sessions.create/prompt`、`events.mux`、`respond`）
  - `@deepseek-ai/dsh-session`（`SessionId` branded type）
  - `@deepseek-ai/dsh-llm`（`ContentBlock`，text-delta chunk 类型）
  - `@deepseek-ai/dsh-user-interaction`（`AskUserQuestionItem`）
  - `@deepseek-ai/dsh-paths`（`resolveDshHome()`）
  - `@deepseek-ai/dsh-invariants`（`InvariantInstaller`，包所有权登记）
  - `@deepseek-ai/dsh-settings`（`settingsNamespace('tg-bot')`）
- **客户端 UI 包**（`packages/client/ui-tg-bot`）：React 18，`@deepseek-ai/dsh-client-*`（runtime / connection / locale / ui-settings / ui-slots / web-react），`tsdown` 打包。
- **Bot API 客户端**：直接基于 `fetch` 长轮询，**无 telegram SDK 依赖**。
- **测试**：Vitest，6 个 spec（channel / render / state / client / plugin / ui store）。
- **License**：BSD-3-Clause。

## 文件结构概览

```
tg-bot/
├── README.md                          # 5.4KB，安装/运行/安全说明
├── LICENSE                            # BSD-3-Clause
├── .gitignore
├── integration/
│   └── deepseek-harness.patch         # 2.0KB，对 DSH host 的最小侵入式改动
├── apps/cli/config/
│   └── web-tg.cordis.yml              # opt-in Cordis overlay（挂载两个插件）
├── packages/
│   ├── experimental/tg-bot/           # 服务端通道插件
│   │   ├── package.json               # @deepseek-ai/dsh-tg-bot @0.0.1
│   │   ├── tsconfig.json
│   │   ├── src/
│   │   │   ├── index.ts        (11KB) # 插件 apply：settings 注册 + 轮询/mux 启停
│   │   │   ├── channel.ts      (27KB) # 通道控制器（核心）
│   │   │   ├── client.ts       (6.8KB)# fetch 版 Bot API 客户端
│   │   │   ├── render.ts       (4.2KB)# HTML 转义 + 4096 字符分块
│   │   │   ├── state.ts        (2.9KB)# chat↔session 持久化（原子写）
│   │   │   ├── types.ts        (2.5KB)# Bot API wire 类型词汇表
│   │   │   └── invariant.ts    (1.2KB)# 包所有权 invariant（空实现）
│   │   └── tests/                     # 6 个 vitest spec
│   └── client/ui-tg-bot/              # Web 设置面板
│       ├── package.json               # @deepseek-ai/dsh-client-ui-tg-bot
│       └── src/
│           ├── index.ts        (198B) # host loader entry（apply 空实现）
│           ├── invariant.ts           # 包所有权 invariant
│           ├── css-modules.d.ts
│           └── client/
│               ├── index.ts    (3.5KB) # 浏览器入口（注册 settings section）
│               ├── TgBotSection.tsx    # React 设置面板组件
│               ├── TgBotSection.module.css
│               ├── store.ts    (6.7KB) # settings 快照 store（describe/update）
│               └── locales.ts          # en/zh 双语文案
```

> 注：`packages/*` 路径故意镜像它在 DSH 检出内的目标位置——它本身**不是独立 pnpm workspace**，没有 lockfile（patch 故意省略 `pnpm-lock.yaml`），必须在 DSH 仓库内 install/build/test。

## 核心功能与实现要点

### 1. 消息协议：Telegram update → DSH session（双向桥接）

**入站（Telegram → DSH）**：`index.ts` 的 `apply` 起两个并发循环（`/tmp/dsh-ext-research/tg-bot/packages/experimental/tg-bot/src/index.ts`，约 162-220 行）：
- **pollLoop**：`TelegramClient.getUpdates(offset, pollTimeoutSec, abort.signal)` 长轮询（默认 25s，上限 50s），每次拿到 update 调 `channel.handleUpdate(update)`；失败按 `TelegramApiError.retryAfterSec` 或 3 秒退避；401 直接停止。
- **muxConsumer**：通过 `ctx.apiProxy.events.mux(request, abort.signal)` 订阅一条 RPC 流（generator），收到 `session/event` 帧转 `channel.handleSessionEvent(sessionId, event)`，收到 `question/requested` 帧转 `channel.handleQuestion(chatId, rpcId, questions)`。注释明确："the generator body runs synchronously on its first next(), so by the time this function returns the queue is registered and no owned prompt can be missed."

**出站（DSH → Telegram）**：`channel.ts` 的 `handleSessionEvent` 处理 `step/start` / `assistant/chunk`（text-delta 累积）/`assistant/message`（用组装后的完整文本覆盖 chunk 文本，因为 assembly 是权威视图）/`turn/end`（错误转 `⚠️ 执行出错` 并 finalize 流）。

每条用户文本消息最终通过 `ApiProxy.sessions.prompt({ sessionId, mode: 'queue', content: [{ type: 'text', text }] })` 进入 agent，与 Web UI 走**同一个 face**（`channel.ts` `sendPrompt`/`ChannelSessions`，约 395-420 行）。

### 2. 身份与会话映射（chat → session）

- **鉴权**：`allowedChatIds` 白名单，**fail closed**（空列表不接受任何人）。未授权 chat 收到一条带观察到的数字 chat id 的提示（"❌ 未授权...Chat ID: xxx"），且 10 分钟内不重复打扰（`UNAUTHORIZED_NOTICE_INTERVAL_MS`，`channel.ts:50`）。
- **持久化映射**：每个授权 chat 拥有**一个** DSH session，映射存于 `$DSH_HOME/tg-bot/chats.json`（`state.ts`）。文档格式带 `version: 1`，**未知版本拒绝而不静默迁移**；写入用 temp + rename 原子替换；`loadChatState` 对非数字 chat id / 形状错误抛错（fail loud 而非给用户开新会话）。
- **会话 id 规则**：新建时 `brandSessionId(\`tg-${chatId}-${randomUUID()}\`)`，前缀 `tg-` 让其在 Web UI 列表中可识别。
- **`/new`** 强制生成一个 fresh sessionId（`channel.ts` `ensureSession(chatId, preferred)`，约 425-445 行），覆盖旧映射。
- **chatForSession**（`channel.ts:107-112`）用于把 mux 流里的 sessionId 反查 chat id——目前是 O(n) 线性扫描 `this.chats` Map，授权 chat 数量大时低效（见风险）。

### 3. 命令集（本地处理 vs 透传）

`handleCommand`（`channel.ts`，约 348-395 行）：
- `/start` → 欢迎语（"已连接到 DeepSeek Harness..."）
- `/help` → 命令列表
- `/new` → 新建会话（持久化新映射）
- `/status` → 当前会话 id + busy/idle 状态（查 `stream.finalFlushed`）
- **其他 `/xxx`（如 `/model fast`）** → 透传给宿主命令注册表（即走 `sendPrompt`，让 DSH host 自己解释）。注释："Unknown commands fall through to the host registry (which reports unknown-command for names it does not know)."

### 4. 流式回复渲染（render + 节流 + 分块）

- **节流**：每个 turn 编辑同一条消息，间隔 ≥ 800ms（`STREAM_EDIT_INTERVAL_MS`，`channel.ts:48`）；首段文本先 `sendMessage`，后续 `editMessageText`。
- **HTML 渲染**（`render.ts`）：fenced code block ``` ``` ``` → `<pre>`，其它文本走 `escapeHtml`（`&` < `>`），永远 `parse_mode: HTML`。code fence 的语言标签被丢弃。
- **4096 字符上限**（`TELEGRAM_MESSAGE_LIMIT`）：
  - 流式中：超长先截断到 4096 展示。
  - turn 结束 `finalizeStream`：用 `chunkText` 在段落/行/词边界切分，第一条 chunk 编辑进当前消息，其余 chunk 各发一条新消息——保证最终聊天记录是完整文本的精确 chunk 序列。
- **dedup**：`assistant/message` 用组装后的完整文本替换 `stepStart` 之后的 chunk 累积，避免 chunk + message 双视图重复。
- **错误隔离**："message is not modified"（400）当作 no-op；"message to edit not found" 重置 messageId 等待下一段重发。

### 5. 交互问题（ask-user-question → inline keyboard）

`handleQuestion`（`channel.ts`，约 158-180 行）和 `handleCallback`（约 184-235 行）：
- 每个 `AskUserQuestionItem` 的每个选项渲染为一个 inline button，`callback_data` 格式 `tgq:<itemIndex>:<optionIndex>`。
- **单选** item：首次点击即提交答案。
- **多选** item：点击切换 toggle，需另点底部"✅ 完成选择"（`tgq:done`）才提交；每选一次更新消息显示"已选: A、B"。
- **自由文本** item（`options === undefined || length === 0`）：等待用户发下一条普通消息作为答案（一条消息回答所有自由文本 item）；其他选项 item 仍要等按钮。
- "取消"（`tgq:cancel`）→ `respond({ ok: false, error: { code: 'cancelled', message: 'cancelled by the user on Telegram' } })`。
- 答案通过 `ApiProxy.respond({ type: 'client-response', rpcId, result: { ok: true, value: { sessionId, answer } } })` 提交——与 Web 客户端走同一 face。
- 已答后把消息编辑为"✅ 已回答"/"✅ 已取消"。
- **dispose 时**所有 pending question 自动以 `code: 'cancelled', message: 'tg-bot channel disposed'` 结算（避免 agent 永久阻塞）。

### 6. 配置（双 layer：env base + 用户 settings）

- **Loader schema**（`index.ts` `Config`）：每个 key 可选，仅作为 composition **base layer**，被用户 settings layer 覆盖。
- **`tg-bot` settings namespace**（`TGBotSettings` schema）注册到 `ctx.settings.register(...)`：`enabled` / `botToken`(secret) / `allowedChatIds` / `apiBaseURL`(默认 `https://api.telegram.org`) / `pollTimeoutSec`(1..50, 默认 25) / `cwd`。
- **env-driven 启动**（`apps/cli/config/web-tg.cordis.yml`）：`TG_BOT_TOKEN` / `TG_ALLOWED_CHAT_IDS=123,456` / `TG_API_BASE_URL` 通过 Cordis overlay 注入 base layer，token 缺省时通道保持禁用直到设置面板开启。
- **设置面板**（`packages/client/ui-tg-bot/src/client/TgBotSection.tsx`）：开关、`type=password` 的 token（**write-only**：wire 从不回传，只暴露 `tokenSet` boolean）、逗号分隔 chat id 输入（带 `parseChatIds` 校验）、API base URL。保存走 `settings.update({ ns, patch, expectedRevision })`，revision 冲突返回 `settings-conflict` 提示重开面板。
- **生命周期**：`scope.watch(next => queueReconfigure(next))`——settings 写入立即触发"停掉旧 runtime → 起新 runtime"，串行化以避免突发写入竞态（`index.ts:225-230`）。

### 7. 与 DSH host 的集成（挂载方式）

源码形态，三步 cp + 一份 patch（README "Install from source"）：
1. 把 `packages/experimental/tg-bot` 和 `packages/client/ui-tg-bot` 拷进 DSH 检出对应位置。
2. 把 `apps/cli/config/web-tg.cordis.yml` 放到位。
3. `git apply --unidiff-zero integration/deepseek-harness.patch`，patch 内容（`/tmp/dsh-ext-research/tg-bot/integration/deepseek-harness.patch`）：
   - `apps/cli/package.json` 增加 `@deepseek-ai/dsh-client-ui-tg-bot` 与 `@deepseek-ai/dsh-tg-bot` 依赖。
   - **`packages/host/apiproxy/src/api-proxy.ts`**：把 `'tg-bot'` 加入 `PRODUCT_SETTINGS_NAMESPACES` 集合——这是让 host 把 tg-bot namespace 当作"产品设置"暴露给浏览器写入的关键 seam（注释：`tg-bot is the experimental Telegram channel's settings namespace (its Web settings panel writes through this same face)`）。
   - `pnpm-workspace.yaml`：把 `@deepseek-ai/dsh-pty-local` 的 `allowBuilds` 从 `file:packages/...` 收紧为包名（"pnpm 11 否则当作非法 version union 拒绝"）。
   - `tsconfig.base.json` / `tsconfig.client.json` / `tsconfig.host.json`：加路径映射与 project references。
4. `pnpm install && pnpm exec vitest run ... && pnpm run build`。
5. 运行：`node --import tsx/esm apps/cli/src/bin.ts web --config apps/cli/config/web-tg.cordis.yml`。

兼容性锁定 DSH commit `fa3d357fc66102d82f0ddbf67fd3d5d70944d8f7`（pre-release，不承诺 ABI 稳定）。

### 8. Web 设置面板（packages/client/ui-tg-bot）

- React 函数组件 `TgBotSection`，通过 `dshClient.inject`（package.json 的 `dshClient.inject` 字段）注入 store/useSnapshot/t。
- 双语 locales（`locales.ts` en + zh，键完全一致）。
- `TgBotStore`（`store.ts`）：基于 `createSnapshotStore`，load 走 `settings.describe({})` 并投影出 `tg-bot` namespace view（含 `tokenSet` 由 `namespace.secrets` 推断）；save 走 `settings.update({ ns, patch, expectedRevision })`，token/URL 留空表示"不改"（merge patch 语义）。
- 设置面板提示用户用 `@userinfobot` 查 chat id；明确"群 chat id 与 user id 不同且常为负数"。

## 与 DeepSeek Harness 主仓库的集成点

- **plugin seam：Cordis 服务注入**。`inject: ['apiProxy', 'settings']`（`index.ts:46`）和 `inject: ['invariants']`（`invariant.ts`）。
- **RPC face**：通过 `@deepseek-ai/dsh-host-apiproxy` 暴露的三个面与 host 通信——
  - `apiProxy.sessions.create` / `apiProxy.sessions.prompt`（入站用户文本）
  - `apiProxy.events.mux`（出站 session 事件流 + question/requested 帧）
  - `apiProxy.respond`（提交 question 答案 / 取消）
- **settings seam**：`@deepseek-ai/dsh-settings` 的 `settingsNamespace('tg-bot')` 注册 schema；host patch 把 `'tg-bot'` 加进 `PRODUCT_SETTINGS_NAMESPACES` 让浏览器可写。
- **路径**：`@deepseek-ai/dsh-paths` 的 `resolveDshHome()` 定位 `$DSH_HOME/tg-bot/chats.json`。
- **挂载方式**：源码 cp + `git apply` 一份 host patch（非 plugin marketplace 安装；DSH 当前 external repo 格式只支持静态 skill 和 MCP 配置，不支持任意 Cordis 服务端/Web UI 代码，因此以源码分发）。
- **Cordis overlay**：`web-tg.cordis.yml` 在 `dsh web` 启动时被 launcher 叠加到 `base.cordis.yml` + `web.cordis.yml` 之上，mount `tg-bot` 与 `ui-tg-bot` 两个插件到 Web 进程。
- **不变性**：`tg-bot` 与 Web GUI **共享同一组 session**（同 sessionId、同历史）——README 反复强调"the same agent sessions the Web GUI serves"。

## 亮点与风险

### 亮点

1. **零新增攻击面 + 复用既有 RPC face**：不暴露 webhook，纯 outbound getUpdates 长轮询；prompt/respond/events 全走 host 已有的 `ApiProxy` 面，与 Web 客户端等权——没有为 Telegram 单开一条特权通道。
2. **流式渲染工程严谨**：800ms 节流避免 Telegram 限频；4096 上限边界感知切分（段落→行→词→硬切）；`assistant/message` 覆盖 chunk 累积做权威去重；turn 结束的 overflow 用多条消息保证最终转录是完整文本的精确 chunk 序列。
3. **状态持久化的"fail loud"哲学**：状态文件版本化（v1），未知版本/形状/非数字 chat id 一律抛错而不是静默给用户开新会话——避免悄悄丢历史。
4. **鉴权 fail closed + 限频提示**：空 allowlist 不接受任何人；未授权 chat 仍回显观察到的 chat id 方便运维添加，但 10 分钟才提醒一次。
5. **token write-only**：`z.string().role('secret')` + UI 用 `type=password` + wire 只回 `tokenSet: boolean`；patch 注释强调"the token is a settings secret — it never rides the wire back to the browser"。
6. **错误分类清晰**：`TelegramApiError`（带 `code`/`retryAfterSec`）vs `TelegramTransportError`；401/409 视为永久配置冲突保持禁用，瞬时网络问题仍启动并退避重试。
7. **生命周期细节**：dispose 时把所有 pending question 自动以 `cancelled` 结算（防止 agent 永久阻塞）；reconfigure 串行化避免突发 settings 写入竞态；per-chat outgoing chain 串行化避免流式编辑交错。
8. **测试覆盖完整**：6 个 spec 覆盖 auth 路由、prompt 流、流式（含去重/溢出/错误）、question（单选/多选/自由文本/取消/dispose）、状态往返、Bot API client、插件生命周期（含 mock Telegram 服务器）。

### 风险

1. **媒体消息被静默忽略**——`types.ts:23-30` 的 `TelegramMessage` 仅声明 `text?: string`，`channel.ts` 的 `handleMessage` 也只读 `message.text`。用户发照片/语音/文档/贴纸/sticker 完全无反应、无提示。README 未提及此限制，授权用户容易误以为 bot 卡死。位置：`/tmp/dsh-ext-research/tg-bot/packages/experimental/tg-bot/src/types.ts:23`、`/tmp/dsh-ext-research/tg-bot/packages/experimental/tg-bot/src/channel.ts:303-309`（`handleMessage` 取 `text ?? ''`）。
2. **`chatForSession` 是 O(n) 线性扫描**——`channel.ts:107-112` 用 `for (const [chatId, owned] of this.chats)` 反查 sessionId。每个 mux 帧（每条 assistant/chunk）都要扫一遍；授权 chat 数量大 + 长回答高频 chunk 时性能下降。无反向 Map (`SessionId → chatId`) 缓存。
3. **mux 流断开后降级不彻底**——`index.ts:208-217` 中 mux 流失败只 log error 后返回，pollLoop 继续，但"questions and streaming are unavailable"。此时用户发的 prompt 仍会进入 agent，但回复**永远不会显示**给用户，也没有自动重连或向用户告警。位置：`/tmp/dsh-ext-research/tg-bot/packages/experimental/tg-bot/src/index.ts:208`。
4. **host patch 锁定到特定 commit**——`fa3d357fc66102d82f0ddbf67fd3d5d70944d8f7`，DSH 是 pre-release，`PRODUCT_SETTINGS_NAMESPACES`、包路径、tsconfig 路径任一漂移即破坏。patch 不会自动 rebase。位置：`/tmp/dsh-ext-research/tg-bot/integration/deepseek-harness.patch`、README "Compatibility"。
5. **无 lockfile + 私有仓库 + 单次提交 + 0.0.0/0.0.1 版本号**——`git log` 只有 1 个提交（`f87e8f2 2026-08-05 作者（昵称已脱敏）: Publish Telegram channel source integration`），无法判断迭代节奏；patch 故意省略 `pnpm-lock.yaml`，每次安装解析的传递依赖可能漂移。位置：README "Install from source"、`packages/*/package.json`。
6. **token 仍以明文落盘到 settings 文件 + 进程环境**——README "Security" 明确警告："Treat the local settings file and process environment as sensitive storage; do not commit a token or include it in logs." 但宿主 settings 文件无额外加密。位置：README "Run"/"Security"。
7. **slash 命令与自由文本歧义**——`handleMessage`（`channel.ts:303-336`）：若 chat 有 pending 自由文本 question，**任何**非 `/` 消息都会被当成答案，包括用户本想取消或想发新 prompt 的情况。无"取消回答"的逃生口（只能等"取消"按钮，但若问题只有自由文本项，按钮区只有"取消"——实际可用，但用户预期不明确）。
8. **`allowed_chat_ids` 校验在 env overlay 处宽松**——`web-tg.cordis.yml:24` 用 `.filter((id) => Number.isInteger(id) && id > 0)`，**拒绝负数 chat id**（群组 id 常为负）。但 settings 面板和 `parseChatIds`（`store.ts:65-71`）允许负数（locales 例子就是 `-1001234567890`）。env 配置群组场景会静默丢授权。位置：`/tmp/dsh-ext-research/tg-bot/apps/cli/config/web-tg.cordis.yml:24` vs `/tmp/dsh-ext-research/tg-bot/packages/client/ui-tg-bot/src/client/store.ts:65`。

## 维护状态

- **default branch**：`main`。
- **总提交数**：1（`f87e8f2`，2026-08-05 00:21:31 +0800，作者 `作者（昵称与邮箱已脱敏）`，消息 "Publish Telegram channel source integration"）。
- **最近 push**：2026-08-05（与提交同期，单次推送）。
- **提交活跃度**：无法判断迭代节奏——仓库为新增首发，尚无后续 commit 历史。
- **文件数**：35（`git ls-files | wc -l`）。
- **README 质量**：优秀。覆盖定位、兼容性、目录结构、安装步骤、运行（GUI/env 两种）、行为（轮询/鉴权/会话映射/媒体处理边界）、安全声明、License。明确说明"以源码分发、克隆不等于激活"，对 host patch 的 ABI 不稳定性有诚实警告。
- **私有仓库**：是（dsh-external org）。
- **测试**：6 个 vitest spec 文件齐全（channel 478 行 / plugin 165 行 / render / state / client / ui store），plugin.spec.ts 起本地 mock Telegram HTTP server 做端到端 lifecycle 验证。

## 备注

- **目录镜像约定**：`packages/experimental/tg-bot` 与 `packages/client/ui-tg-bot` 的路径就是它们在 DSH 检出内的目标位置——这是一种"源码 overlay"分发模式，与 DSH 当前 external repo 只支持静态 skill + MCP 配置的限制相对应。README 解释："the current DeepSeek Harness external repository format supports static skills and MCP configuration, not arbitrary Cordis server or Web UI code. Installing this repository therefore changes a DeepSeek Harness source checkout; cloning it alone does not activate the plugin."
- **invariant.ts 是空实现**：两个包都注册了 invariant companion 但 `install: InvariantInstaller = () => {}`——注释解释：channel "owns no event stream of its own (it consumes the session/mux streams as a listener, never a producer)"，所以没有运行期不变量可校验。这是 DSH 包所有权登记的占位约定。
- **国际化**：channel 内的中文硬编码（`/new`、`/status`、`已取消`、`⚠️ 执行出错` 等）与 UI locales 的双语支持**不一致**——服务端消息永远是中文，英文用户在 bot 端会看到中文提示。位置：`/tmp/dsh-ext-research/tg-bot/packages/experimental/tg-bot/src/channel.ts`（welcomeText/helpText/noticeUnauthorized 等）。
- **`pollTimeoutSec` 上限 50**：Bot API long-poll 最多 50 秒（Telegram 实际限制 50-60），schema `z.number().min(1).max(50)` 合理。
- **替代用法**：`apiBaseURL` 可指向代理或本地 mock，`plugin.spec.ts` 用 `node:http` 起本地 mock server 做端到端测试——这套测试基础设施对该插件的可维护性贡献显著。
- **无 webhook 模式**：纯长轮询，需要 outbound HTTPS 但不暴露入站端口，部署门槛低（无需公网/反向代理）。
