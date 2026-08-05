# telegram 调研摘要

## 一句话定位

`dsh-external/telegram` 是 DeepSeek Harness 的 **Marisa/dshx 外部插件**形式的 Telegram 桥接：通过 Bot API 长轮询把 Telegram 私聊桥接到 harness agent 会话，每个聊天一个 agent 会话，仅文本接缝。它是对同一组织内 `dsh-external/tg-bot` 的**重新实现**——把 tg-bot 的「源码 + 主仓 patch + Web UI」重型方案，替换成轻量、纯后台、`dshx install telegram <git-url>` 一行装载的标准插件。

## 技术栈与依赖

- 语言：TypeScript（`target: ES2024`，`module: esnext`，`moduleResolution: bundler`，`strict: true`），构建产物在 `lib/`（JS + `lib/types/` 声明）。
- 运行时：Node（`type: module`），宿主为 cordis 4（`cordis ^4.0.0-rc.7`）。
- 运行依赖（`dependencies`）：仅 `schemastery ^3.18.0`（配置 Schema）。
- peerDependencies（必须由宿主组合提供）：
  - `@deepseek-ai/dsh-agent ^0.0.1`（提供 `ctx.agents.create` 工厂）
  - `@deepseek-ai/dsh-llm ^0.0.1`（`createUserMessage`）
  - `@deepseek-ai/dsh-session ^0.0.1`（`Session` / `SessionEvent` / `SessionId`）
  - `cordis ^4.0.0-rc.7`
- devDependencies：`typescript ^5.9.0`。
- 无运行时第三方 HTTP 库——直接用全局 `fetch` 调 Telegram Bot API。
- 许权：`package.json` 声明 `BSD-3-Clause`，但仓库根**未提交 LICENSE 文件**（见风险）。

## 文件结构概览

```
telegram/
├── dsh.plugin.json         # 320B  外部插件清单：id=telegram，contributes.tools/skills 均为 []
├── package.json            # @dsh-external/telegram 0.1.0，private，main=lib/index.js
├── tsconfig.json           # 严格模式，仅编译 src → lib
├── probe.mjs               # 2.8KB 加载探针：用 dsh 启动真实组合，断言插件 fiber 激活
├── README.md               # 4.2KB 中文单一 README（最近一次提交刚把 en/zh 双版合并为中文）
├── src/
│   ├── index.ts            # 2.4KB 插件入口：Schema、apply、inject:['agents']
│   ├── bridge.ts           # 10.4KB 核心：长轮询循环 + 每聊天会话 + slash 命令 + 投递
│   ├── client.ts           # 6.0KB Bot API 客户端：getUpdates/sendMessage/sendChatAction/getMe
│   └── format.ts           # 3.0KB Markdown→HTML 子集 + 4096 字符分片
├── tests/                  # 5 个 vitest 规范（bridge/client/format/plugin-apply/plugin-shape）
├── scripts/build.sh        # 把 dsh checkout 的依赖 symlink 进 node_modules 后跑 tsc
├── lib/                    # 构建产物（已提交）
└── examples/telegram-agent/
    ├── cordis.yml          # 3.2KB 完整可运行组合：telegram + dsh-llm-deepseek + bash + fs + sessions
    ├── package.json
    ├── README.md / README.zh.md
```

## 核心功能与实现要点

1. **外部插件清单声明为「纯后台服务」** —— `dsh.plugin.json` 的 `contributes.tools` 与 `contributes.skills` 都是 `[]`；不向模型暴露任何工具或技能，只把 Telegram 文本桥接到 agent 会话（`dsh.plugin.json`，`src/index.ts`）。

2. **单条长轮询循环服务所有聊天** —— `TelegramBridge.pollLoop()` 串行 `getUpdates(offset)`，按 `update_id+1` 推进 offset；空批次 `sleep(50ms)` 防热循环；错误按 `min(1000*errorCount, 10000)` 指数退避（`src/bridge.ts` 的 `pollLoop`）。

3. **每聊天一个 agent 会话，通过 `ctx.agents.create` 创建** —— `inject: ['agents']`；`ensureChat(chatId)` 用 `SessionId('telegram:<chatId>')` 创建并缓存到内存 `Map`；`/new` `/clear` 旋转会话并 dispose 旧 handle（`src/bridge.ts: ensureChat / handleCommand`）。每条已授权文本消息通过 `agent.followup(createUserMessage({...}))` 注入（`src/bridge.ts: handleUpdate`）。

4. **会话事件回投 Telegram** —— 监听 `ctx.on('session/event', …)`：`turn/start` 触发 `typing` 聊天动作，`assistant/message` 抽取文本块并投递（`src/bridge.ts: handleSessionEvent`）。投递经 `markdownToHtml`（围栏代码→`<pre>`、行内代码→`<code>`、`**粗体**`→`<b>`，其余 HTML 转义）转换后，按 4096 字符分片，优先在换行 / 中文句号 / 句点+空格处断行（`src/format.ts: markdownToHtml / splitMessage`）。HTML 投递失败时该片回退纯文本重发（`src/bridge.ts: safeSend`）。

5. **fail-loud / fail-closed 安全姿态** —— `apply()` 在 token 缺失（`config.token` 与 `DSH_TELEGRAM_TOKEN` 均空）时直接 `throw`，绝不惰性启动（`src/index.ts: apply`）；`allowedUserIds` 为空时拒绝所有人，`allowAllUsers: true` 仅开发用（`src/bridge.ts: authorized`）。所有错误经 `ctx.logger` 记录，token 在错误信息中被 `redactToken` 替换为 `***`（`src/client.ts: redactToken / redactedMessage`）。

6. **可测试接缝** —— `TelegramBridgeOptions` 暴露 `client`（替换为 fake）与 `sleep`（替换为瞬时定时器）两个仅运行时使用的字段；`TelegramClient` 同样接受 `fetch`/`baseUrl`/`pollingTimeoutSec` 注入，便于测试（`src/bridge.ts`、`src/client.ts`）。

7. **可运行的示例组合 `examples/telegram-agent`** —— 一份完整的 `cordis.yml`：telegram + `dsh-llm-deepseek`（开启 thinking/max effort）+ `dsh-bash-local` + `dsh-fs-local` + JSONL 会话持久化 + `dsh-compact-basic` 自动压缩；模型可见工具仅 `bash`/`read`/`write`/`edit`/`subagent`/`todo_write`。`README.zh.md` 列出 8 个运行时环境变量（`DSH_TELEGRAM_TOKEN` 等）。

8. **加载探针 `probe.mjs`** —— 不调任何 API key，仅断言「真实 dsh 组合启动后插件 entry 的 fiber 已激活」；为绕过 `apply` 的 token 必填校验，注入一个 `probe-dummy-token`，运行期 Telegram 401 警告被记录但不算加载失败。

## 与 DeepSeek Harness 主仓库的集成点

- **装载方式**：标准 Marisa 外部插件。`dshx install telegram <dir|git-url>` 把本仓库挂到 dsh 的外部插件目录；`dsh.plugin.json` 的 `engines.dsh >=0.0.1`。
- **接缝（seam）**：`inject: ['agents']` —— 依赖宿主组合挂载 `agents` 服务（`@deepseek-ai/dsh-agent`），调用 `ctx.agents.create({ sessionId, meta, agentOptions })` 创建 agent handle；监听 `ctx.on('session/event', …)` 接收 `turn/start` 与 `assistant/message`；调用 `agent.followup(userMessage)` 注入用户输入。
- **协议**：复用 `@deepseek-ai/dsh-llm` 的 `createUserMessage`（content blocks `[{type:'text', text}]`、`source.kind:'user'`）；复用 `@deepseek-ai/dsh-session` 的 `Session` / `SessionEvent` / `SessionId(...)`。
- **LLM / 工具 / 会话持久化全部外置** —— 插件本身不声明任何模型、工具或技能；它们全部来自外围 `cordis.yml`（`examples/telegram-agent/cordis.yml` 是参考实现）。
- **构建期耦合**：`scripts/build.sh` 通过 symlink 进 dsh checkout 的 `node_modules` 来 type-check，硬编码了若干路径：`vendor/cordis`、`vendor/cosmokit`、`vendor/schemastery`、`packages/core/agent`、`packages/util/brand`、`packages/llm/llm`、`packages/core/scope`、`packages/core/session`——任一路径变更都会破坏构建。
- **与 `dsh-external/tg-bot` 的关系**：两者**不冲突，是同一目标的两条路线**（详见下文对比）。`telegram` 是 0.1.0 的 Marisa 插件，`tg-bot` 是 0.0.1 的源码 + 主仓 patch + Web UI 方案；同一天（2026-08-04）创建，tg-bot（16:21 UTC）早于 telegram（21:18 UTC）约 5 小时。

### 与 `dsh-external/tg-bot` 的关键差异

| 维度 | `telegram`（本仓） | `tg-bot`（同组织） |
|---|---|---|
| 分发形态 | `dshx install` 装载的标准外部插件（已构建 `lib/`） | 源码 + `integration/deepseek-harness.patch` 注入 harness checkout |
| 接缝 | `ctx.agents.create` 工厂 + `session/event` 流 | `ApiProxy.sessions` 面向 Web 进程内集成 |
| UI | 无 | `packages/client/ui-tg-bot` Web Settings 区块 + 写入式 token 字段 |
| 渲染 | 文本→HTML 子集，每条 assistant 一条消息 | 流式编辑单条消息 + `ask-user-question` 渲染为 inline keyboard |
| 持久化 | 内存 `Map<chatId, ChatSession>`，重启即丢 | `$DSH_HOME/tg-bot/chats.json` 原子持久化，重启可恢复 |
| 范围 | 仅私聊、仅文本、仅长轮询、无重试账本 | 与 Web UI 同会话、有 `/status`、群聊/话题亦在路线 |
| 体量 | 4 个 src 文件 ≈ 22KB | 多包 workspace（`packages/experimental/tg-bot` + `packages/client/ui-tg-bot`） |

**结论**：`telegram` 是 `tg-bot` 的**精简替代路线**——把 tg-bot 的「源码 patch + Web UI + 流式 + 持久化」四件套砍到「纯后台、纯文本、内存会话」的最小可用形态，换取标准插件装载与零主机改动。

## 亮点与风险

亮点：
- 接缝非常窄：仅 `inject:['agents']` + 一个事件订阅 + 一个 `followup` 调用，干净且可测；`client`/`sleep`/`fetch` 三个可替换 seam 让单测无需网络（`src/bridge.ts`、`src/client.ts`）。
- 安全姿态正确：缺 token 即 `throw`、白名单空即拒绝所有人、token 在所有日志中被脱敏（`src/index.ts: apply`、`src/client.ts: redactToken`）。
- 投递降级链完整：HTML 失败 → 纯文本重发 → 失败记日志（`src/bridge.ts: safeSend`）。

风险：
- **无 LICENSE 文件**：`package.json` 声明 `BSD-3-Clause`，但仓库根未提交 LICENSE 文本；gh API 也返回 `licenseInfo: null`。分发与再分发存在许可证据缺失。
- **会话映射易失**：`chats = new Map<string, ChatSession>()` 仅在内存（`src/bridge.ts` 类字段），进程重启即丢失 chat↔session 绑定，agent 会话需要从 session 持久化层另行恢复——比 tg-bot 的 `chats.json` 弱。
- **无投递重试 / 账本**：投递失败仅记日志后丢弃；与 README 中「Hermes 风格的发送重试与投递账本留待后续」自述一致（`README.md`，`src/bridge.ts: safeSend`）。
- **peer deps 锁在 `^0.0.1`**：harness 处于 pre-release，`Session`/`SessionEvent`/`AgentHandle`/`createUserMessage` 任一签名 churn 都会同时打断构建（`scripts/build.sh` 的硬编码 symlink 路径）与运行（`src/bridge.ts` 顶层 import）。
- **能力边界明确但窄**：仅文本消息（照片/文档/语音/贴纸被静默忽略）、仅私聊（群 @ 提及、topics 未处理）、仅长轮询（主机须可出站访问 `api.telegram.org`，无 webhook 模式）、每条 assistant 输出固定一条消息（工具中间进度不流式）——README 已自陈（`README.md` 已知限制段）。
- **构建依赖 dsh 在 PATH 上**：`probe.mjs` 与 `scripts/build.sh` 都从 PATH 上的 `dsh` 反查 checkout 路径；非 dsh 环境下两者都会失败（`probe.mjs: resolveCheckout`、`scripts/build.sh`）。

## 维护状态

- 仓库 `createdAt` = 2026-08-04T21:18:38Z，`pushedAt` = 2026-08-04T23:18:57Z，单 commit（`git rev-list --count HEAD` = 1），最新提交 `dc5dbf9 docs: single Chinese README (README.md), remove the English/zh pair`。
- 未归档（`isArchived: false`），0 star，主分支 `main`。
- 仅 1 次提交表明**新仓刚发布**，尚未进入迭代周期；与同日创建的 `tg-bot`（commit `f87e8f2 Publish Telegram channel source integration`）属同期产物。

## 备注

- 文件路径（绝对）：
  - 摘要：`/tmp/dsh-ext-research2/telegram.md`
  - 克隆：`/tmp/dsh-ext-research2/telegram/`
  - 对比对象：`/tmp/dsh-ext-research2/tg-bot/`
- 本插件不与 dsh 主仓库做源码 patch 集成；通过标准 Marisa 外部插件契约（`dsh.plugin.json` + `inject:['agents']`）解耦，主仓库仅需提供 `@deepseek-ai/dsh-agent` + `dsh-llm` + `dsh-session` 即可。
- 与同一组织的 `dsh-external/dsh-feishu-bot` / `dsh-external/dsh-weixin-bot` / `dsh-external/dsh-wecom-bot`（其他 IM 桥接）模式同构：均为后台服务型外部插件、仅文本、`inject` 宿主服务。`telegram` 与 `tg-bot` 的双轨值得在 catalog 里注明，避免用户同时装载造成重复桥接。
- 脱敏：本摘要不含作者邮箱/真实姓名；GitHub 用户名（组织 `dsh-external`）按约定保留。
