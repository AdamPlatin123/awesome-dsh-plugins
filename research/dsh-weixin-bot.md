# dsh-weixin-bot 调研摘要

## 一句话定位

DeepSeek Harness 的**个人微信**通道插件：通过腾讯 **iLink Bot API**（非企业微信）把微信私聊/群聊变成 agent 对话界面，零运行时依赖、HTTP 长轮询、扫码登录，与同组织的 `tg-bot` / `qqbot` / `dsh-feishu-bot` / `dsh-wecom-bot` 同属 "X remote channel for DeepSeek Harness" 通道家族（其中 `dsh-wecom-bot` 是企业微信变体，本仓是个人微信变体）。

## 技术栈与依赖

- **语言/运行时**：纯 Node.js（ESM，`"type": "module"`），目标 Node ≥ 18（用全局 `fetch` / `AbortSignal.timeout`）。
- **运行时依赖**：**零**（README/package.json 双重声明，仅用 `node:*` 内置模块：`fetch`、`node:fs/promises`、`node:crypto`、`node:events`、`node:os`、`node:path`）。
- **dev/test**：`node:test` + `node:assert/strict`（`tests/weixin-client.spec.mjs`），无构建步骤、无 lint 配置。
- **外部服务**：腾讯 **iLink Bot API**（`https://ilinkai.weixin.qq.com`，端点见 `lib/weixin-client.js:EP_*`）。
- **协议**：HTTP 长轮询收消息（`ilink/bot/getupdates`，35 秒）、`sendmessage` / `sendtyping` / `getconfig` 发消息与 typing ticket、`get_bot_qrcode` + `get_qrcode_status` 扫码登录。
- **License 文件**：MIT；**但 `package.json` 写 `BSD-3-Clause`**（见"亮点与风险"）。

## 文件结构概览

```
dsh-weixin-bot/
├── README.md                  5.9KB  使用与配置文档（中文，最完整的入口）
├── LICENSE                    MIT，版权 2026 dsh-external
├── package.json               name=dsh-weixin, version=0.1.0, type=module, main=lib/index.js
├── .gitignore                 24B（仅忽略 node_modules 等）
├── lib/
│   ├── index.js         7.3KB  插件入口：apply()、/weixin 命令、扫码登录流程
│   ├── weixin-client.js 19.9KB iLink API 客户端 + 长轮询 + 消息归一化 + QR 流程
│   ├── agent-bridge.js  18.2KB 微信消息 ↔ DSH agent 会话桥（核心业务逻辑）
│   ├── config.js         4.2KB 配置归一化 + 访问控制（dmPolicy/groupPolicy/ownerIds）
│   └── credentials.js    4.0KB QR 登录成功后把凭据写回 ~/.dsh/config.yaml（行级编辑）
└── tests/
    └── weixin-client.spec.mjs  8.8KB  iLink 协议烟测（fake fetch，无网络）
```

## 核心功能与实现要点

1. **零依赖长轮询客户端**（`lib/weixin-client.js:WeixinClient`）：基于 `EventEmitter`，`runPollLoop()` 持续 `getupdates`，`get_updates_buf` 游标持久化后断点续传；错误退避 2 秒、连续 3 次后 30 秒；会话过期（errcode `-14` 或 ret `-2`+`unknown error`）暂停 10 分钟并提示重登（`lib/weixin-client.js:301-380`）。MIN_POLL_INTERVAL_MS=1s 防止空响应变成 busy spin。

2. **每聊天一个持久会话**（`lib/agent-bridge.js:AgentBridge`）：私聊 `wx-c2c-<userId>`、群聊 `wx-group-<groupId>`；通过 `ctx.agents.resume({ resumeSessionId })` 重启后接续，否则 `ctx.agents.create({ sessionId, agentOptions, meta:{cwd} })` 新建；`/new` 通过 `generations` Map 自增后缀 `-g<n>` 生成全新会话 id 并归档旧的（`lib/agent-bridge.js:sessionIdFor`、`handleCommand` 的 `/new` 分支）。

3. **流式回复 + 分片发送**：监听 `ctx.on('session/event', …)` 的 `turn/start`、`assistant/message`、`turn/end`；每条 assistant 文本块即时回发到微信，超 4000 字按换行/句号切分（`chunkText`），分片间 300ms 防限流；`turn/end` 的 `error`/`max-tokens` 会以 ⚠️ 提示用户（`lib/agent-bridge.js:onSessionEvent`、`lib/weixin-client.js:chunkText`）。

4. **扫码登录 `/weixin bind`**（`lib/index.js:startBindFlow` + `pollQrLoop`）：`get_bot_qrcode` 取二维码 → 微信扫描 → 1 秒间隔轮询 `get_qrcode_status`，状态机覆盖 `wait/scaned/scaned_but_redirect/expired/confirmed`；过期自动刷新（最多 3 次，480 秒截止）；确认后调用 `writeCredentialsToConfig` 写入 `~/.dsh/config.yaml`，触发宿主 HMR 热重载插件。

5. **微信内斜杠命令**（`lib/agent-bridge.js:handleCommand`）：`/help /new /status /model /models`，其中 `/model <厂商>/<名>` 通过 `ctx.get('llm').listProviders()/listModels()` 校验后做会话级覆盖（`modelOverrides` Map，仅内存、重启失效）。

6. **访问控制 + 多通道策略**（`lib/config.js:allows`）：`dmPolicy`（私聊 open/allowlist/disabled）、`groupPolicy`（默认 **disabled**，因为 iLink 机器人身份通常收不到普通微信群消息）、`ownerIds` 永远放行作为第二道安全网；白名单支持 `*` 通配。

7. **消息去重与上下文延续**：300 秒/1000 条上限的 messageId 去重窗口持久化到 `~/.dsh/weixin-state.json`（`lib/agent-bridge.js:isDuplicateMessage`）；入站消息的 `context_token` 按 userId 缓存并在 `sendmessage` 时回显，iLink 要求回显才能保持回复连续性。

8. **媒体/引用/语音处理**：图片/视频/文件只生成 `[图片: 名]` 等一行摘要喂给模型（不下载、不解密 AES-128-ECB，README列为后续方向）；引用消息以 `[引用: …]` 段落注入；语音用 iLink 自带 STT 的 `voice_item.text` 以 `[语音转写: …]` 注入（`lib/weixin-client.js:extractText`/`attachmentSummary`）。

## 与 DeepSeek Harness 主仓库的集成点

这是**纯宿主侧插件**，通过 cordis 风格插件协议（`ctx` / `inject` / `apply` / `ctx.effect` / `ctx.on('dispose')`）接入 DSH 主进程，不修改主仓库代码：

- **声明依赖服务**：`lib/index.js` 头部 `export const inject = ['agents', 'commands']`。
- **agent 生命周期 API**：`ctx.agents.create({ sessionId, agentOptions:{provider,model}, meta:{cwd} })` 与 `ctx.agents.resume({ resumeSessionId, agentOptions })`、`handle.dispose()`（`agent-bridge.js:ensureAgent/resetSession`）——注释明确"mirror of dsh-llm createUserMessage"，跟随主仓 dsh-llm 的消息形状。
- **事件订阅**：`ctx.on('session/event', (session, event) => …)` 接收 `turn/start` / `assistant/message` / `turn/end`。
- **服务注册**：`ctx.commands.register({ name:'weixin', input:{hint}, handler })` 注册 `/weixin` 斜杠命令；`ctx.get('llm')` 取 provider/model 列表；`ctx.get('sessionPersistence').list()` 判断会话是否已存在。
- **配置/部署 seam**：插件目录 `~/.dsh/plugins/dsh-weixin/`，通过软链 `~/.dsh-local/dsh-weixin` 装入；配置块在 `~/.dsh/config.yaml` 用 `- insert:` 形式声明，`config:` 下的 `accountId/token/baseUrl/provider/model/cwd/dmPolicy/groupPolicy/…` 由 `lib/config.js:normalizeConfig` 归一化，支持 `DSH_WEIXIN_*` 环境变量回退。
- **凭据热重载**：`lib/credentials.js` 行级编辑 `~/.dsh/config.yaml` 的 dsh-weixin 配置块（刻意不引入 YAML parser 以保持零依赖），依赖主仓 `dsh web` 对个人 overlay 的 HMR 监听自动重启插件。
- **无直接 patch/monkey-patch**：完全是黑盒消费 DSH 公开 API，与主仓解耦干净；同组织 `tg-bot`/`qqbot`/`dsh-feishu-bot`/`dsh-wecom-bot` 共享同一套 "remote channel" 模式（仅协议客户端与平台特性不同）。

## 亮点与风险

**亮点**

- **零运行时依赖、零构建**：纯 Node 内置 API，部署只需 `git clone` + 软链，符合 DSH 插件轻量化范式。
- **工程细节扎实**：长轮询游标 / context_token / 去重窗口 / 会话 generation 全部跨重启持久化；扫码登录状态机覆盖 redirect 与过期刷新；typing ticket 600s TTL 缓存；poll loop 有最小间隔兜底防 spin。
- **安全分层**：`dmPolicy` + `allowlist` + `ownerIds` 双层兜底；群聊默认关闭（避免误触发）；凭据可走环境变量。
- **测试覆盖协议层**：`tests/weixin-client.spec.mjs` 用 fake fetch 烟测 extractText/chunkText/getUpdates/sendMessage/QR 流程，无网络依赖。

**风险**

- **License 不一致**：`package.json` 声明 `"license": "BSD-3-Clause"`，而 `LICENSE` 文件是 MIT（`LICENSE:1-2` vs `package.json:license`）——分发或法务合规时需要校正其一。
- **iLink 是非官方接口**：`ilinkai.weixin.qq.com` 不在腾讯公开文档中，登录的是"iLink 机器人身份"（`xxx@im.bot`），存在违反微信服务条款、随时被封号或 API 变动的风险（README 已知限制小节亦承认）。
- **会话过期处理粗暴**：errcode `-14` 直接 `sleep(600_000)` 暂停 10 分钟且只提示重登（`lib/weixin-client.js:SESSION_EXPIRED_ERRCODE` 分支），无主动通知或自动重新走 QR 流程。
- **群聊基本不可用**：iLink 机器人身份默认收不到普通微信群消息，`groupPolicy=disabled` 是默认值（`lib/config.js:groupPolicy`），实际只剩私聊场景。
- **媒体不解密**：图片/视频/文件只做摘要，AES-128-ECB 解密是 TODO（`README.md` 已知限制），多模态用例受限。
- **凭据文件行级编辑脆弱**：`lib/credentials.js:writeCredentialsToConfig` 用正则缩进匹配 YAML 行，用户手动改了格式或字段顺序可能匹配失败（虽有 fallback 追加整块）。
- **单实例限制**：一次只连一个机器人，多账号需多份插件配置（README 已知限制）。
- **commit 历史仅 1 条**（见维护状态），无 CHANGELOG / CI / lint / 类型检查。

## 维护状态

- **仓库元数据**（`gh api repos/dsh-external/dsh-weixin-bot`）：created/pushed `2026-08-04`，0 star / 0 fork / 0 open issue，未 archive、未 disable，default branch `main`。
- **commit 历史**：仅 **1 个 commit**（`e8c2177` "dsh-weixin-bot: chat with your DSH agent in WeChat (iLink Bot API)"，2026-08-05）——首批整体导入，尚无迭代。
- **属于 dsh-external 通道家族**：与 `tg-bot`（TS）/ `qqbot`（JS）/ `dsh-feishu-bot`（JS）/ `dsh-wecom-bot`（JS，企业微信）同期 2026-08-04 创建，描述同为 "X remote channel for DeepSeek Harness"，定位高度一致。
- **无 CI/lint/RELEASE**：`.github/` 不存在，无 workflows，无 CHANGELOG，无 `.editorconfig`/`.prettierrc`；测试需手动 `node --test tests/`。
- **活跃度判断**：刚落地、首批导入阶段；后续是否维护取决于家族整体节奏（同期所有兄弟仓都是单 commit）。

## 备注

- **对比定位**（与同组织兄弟仓）：本仓是**个人微信**通道（iLink Bot API，长轮询，扫码登录 `xxx@im.bot`）；`dsh-wecom-bot` 是**企业微信**通道（API 不同）；`tg-bot` 用 Telegram Bot API（TypeScript）；`qqbot` 是 QQ 通道；`dsh-feishu-bot` 是飞书通道。所有兄弟仓共享同一 "remote channel" 套路：`WeixinClient/TelegramClient` 协议客户端 + `AgentBridge` 把入站消息映射到 `ctx.agents.create/resume` + `session/event` 监听 + `/X bind`/`/X status` 斜杠命令 + 持久化游标/去重/会话。本仓与 `dsh-wecom-bot` 互补（个人 vs 企业微信），不重叠。
- **安装摘要**：`git clone` 到 `~/.dsh/plugins/dsh-weixin/` → 软链到 `@dsh-local/dsh-weixin` → `~/.dsh/config.yaml` 加 `- insert:` 块或 `/weixin bind` 扫码自动写入凭据 → HMR 自动连接。
- **默认 agent 路由**：`provider=deepseek-official` / `model=deepseek-v4-flash`（`lib/config.js`）。
- **关键持久化文件**：`~/.dsh/weixin-state.json`（generations + 去重窗口 + iLink syncBuf/contextTokens）、`~/.dsh/weixin-workspace/`（会话 cwd）、`~/.dsh/config.yaml`（凭据，HMR 监听）。
- **本次调研证据**：本地克隆 `/tmp/dsh-ext-research2/dsh-weixin-bot/` 完整（5 个 lib 文件 + tests + README/LICENSE/package.json，单 commit `e8c2177`）；`gh api` 确认仓库元数据与兄弟仓家族关系。
