# qqbot 调研摘要

## 一句话定位
`dsh-qqbot` 是 DeepSeek Harness 的纯宿主端插件，通过官方 QQ 机器人 API v2（q.qq.com 开放平台）把 QQ 私聊（C2C）与群聊 @机器人 变成 agent 的对话界面，零运行时依赖。

## 技术栈与依赖
- 语言：纯 ES Module JavaScript（Node.js，需 `>= 21` 以使用全局 `WebSocket`）。
- 框架/契约：DSH 宿主端 cordis 风格插件（导出 `name`/`inject`/`apply(ctx, config)`）。
- 依赖：**零运行时依赖**（`package.json` 仅声明 `private:true`、`type:"module"`、`main`、`exports`、`license`）。全部用 Node 内置：`WebSocket`、`fetch`、`node:events`、`node:crypto`、`node:fs/promises`、`node:os`、`node:path`。
- 测试：`node:test` + `node:assert/strict`（`tests/*.spec.mjs`，零第三方测试框架）。

## 文件结构概览
```
qqbot/
├── README.md              6.5 KB  使用文档（架构图、配置表、斜杠命令、限制）
├── LICENSE                       MIT（与 package.json 声明的 BSD-3-Clause 不一致）
├── package.json                  dsh-qqbot@0.1.0, private, ESM
├── .gitignore                    .DS_Store / node_modules/
├── lib/
│   ├── index.js          7.1 KB  插件入口：apply()、/qq 命令、扫码绑定编排
│   ├── config.js         4.6 KB  配置归一化 + 访问控制 (allows)
│   ├── credentials.js    4.5 KB  把绑定凭据按行写回 ~/.dsh/config.yaml
│   ├── onboard.js        6.7 KB  扫码绑定：AES-256-GCM 解密 client_secret
│   ├── qq-client.js     24.8 KB  QQ Bot API v2 客户端（WS 网关 + REST）
│   └── agent-bridge.js  20.6 KB  QQ 消息 ↔ DSH agent 会话桥
└── tests/
    ├── qq-client.spec.mjs 14.3 KB 协议/握手/REST/关闭码策略/ACL 单测
    └── onboard.spec.mjs    7.9 KB 扫码绑定流单测
```

## 核心功能与实现要点
1. **插件装载与生命周期**（`lib/index.js`）：标准 DSH 插件契约 —— `export const name='dsh-qqbot'`、`inject:['agents','commands']`、`apply(ctx, config)`。`apply` 里 `new QQClient(...)` + `new AgentBridge(ctx, ...)`，订阅 `client.on('message'/'status')`，注册 `/qq` 命令，`ctx.on('dispose')` 时调用 `bridge.dispose()` / `client.dispose()`。
2. **QQ Bot API v2 客户端**（`lib/qq-client.js`）：基于 `api.sgroup.qq.com` REST 与 WebSocket 网关。`POST bots.qq.com/app/getAppAccessToken` 换 token → `GET /gateway` 拿 WS 地址 → `op 10 Hello` 回 `op 2 Identify`（或 `op 6 Resume`）→ `op 1` 心跳 → `op 0 Dispatch` 派发 `C2C_MESSAGE_CREATE` / `GROUP_AT_MESSAGE_CREATE` / `GUILD_*` / `DIRECT_MESSAGE_CREATE`。Intents = `(1<<25)|(1<<30)|(1<<12)|(1<<26)`。
3. **断线重连与关闭码策略**（`lib/qq-client.js` `runListener`，行 ~395–470）：退避序列 `[2,5,10,30,60]` 秒；`FATAL_CLOSE_CODES`（4001/4002/4010–4014/4914/4915）永不重连；`SESSION_INVALID_CODES`（4006/4007/4900–4913）清 session 重 Identify；`4004` 丢 token 重新换；`4008` 限流等 60s；连续 3 次 <5s 的"快速断开"判 fatal（防止权限错配死循环）。
4. **每聊天一个持久化 agent 会话**（`lib/agent-bridge.js`）：会话 id 规则 `qq-<kind>-<chatId>`（`/new` 后追加 `-g<n>` 代数，旧会话归档不丢）。`ensureAgent` 先查 `ctx.agents.get(sessionId)`，再走 singleflight 的 `creations` Map；优先 `ctx.get('sessionPersistence').list()` 找到历史 id 后 `ctx.agents.resume(...)`，否则 `ctx.agents.create({ sessionId, agentOptions:{provider,model}, meta:{cwd} })`。因此 QQ 会话也会出现在 Web GUI 会话列表，重启 dsh 后对话续上。
5. **回复流式回送 + 分片 + Markdown 回退**（`agent-bridge.js` `onSessionEvent` + `qq-client.js sendText/sendChunk/postMessage`）：监听 `session/event`，在 `assistant/message` 事件把文本经 `client.sendText` 发出，`reply_to` 只挂在第一片；`chunkText` 在 4000 字上限内优先按 `\n`/`。` 断行。Markdown（`msg_type=2`）被 QQ API 400 拒绝时（匹配 `markdown|130001|invalid.*content`）自动降级为纯文本重发一次（`sendChunk` 行 ~590–605）。C2C 私聊额外用 `MSG_TYPE_INPUT_NOTIFY=6` 发"输入中"（`sendTyping`，50s 去抖）。
6. **跨实例去重**（`agent-bridge.js` `isDuplicateMessage` + `loadState/saveState`）：`~/.dsh/qqbot-state.json` 持久化 300s 窗口内的 messageId 集合（上限 1000）与 `/new` 代数；即便热重载期间新旧 fiber 短暂双连，或 WS Resume 重放，也不会重复处理同一条消息。`QQClient.start()` 还有进程级 `activeClients: Map<appId, QQClient>` 单连接守卫，新实例同步关掉旧实例再开 socket。
7. **访问控制**（`lib/config.js` `allows`）：分私聊/群聊两套策略 `open|allowlist|disabled`，`ownerIds` 作为"第二道安全网"始终放行；凭据可来自 YAML 或环境变量 `DSH_QQ_APP_ID`/`DSH_QQ_CLIENT_SECRET`（兼容旧 `QQ_*`）。
8. **免开放平台扫码绑定**（`lib/onboard.js` + `index.js startBindFlow/pollBindLoop`）：`/qq bind` → 本地 `randomBytes(32)` 生成 AES-256-GCM 密钥 → `POST q.qq.com/lite/create_bind_task` 拿 `task_id` → 拼 `q.qq.com/qqbot/openclaw/connect.html?task_id=...` 链接（手机 QQ 打开或扫码）→ 轮询 `poll_bind_result` → 拿到 `bot_appid` 和 AES-GCM 加密的 `bot_encrypt_secret`，本地 `decryptSecret` 解出 `client_secret` → `credentials.js writeCredentialsToConfig` 按行写进 `~/.dsh/config.yaml` 的 `dsh-qqbot` 条目，触发 dsh 个人配置 HMR 自动重连。

## 与 DeepSeek Harness 主仓库的集成点
- **插件 seam**：标准 cordis 风格宿主端插件（`name` / `inject:['agents','commands']` / `apply(ctx, config)`）。安装方式：克隆到 `~/.dsh/plugins/dsh-qqbot/`，再软链 `~/node_modules/@dsh-local/dsh-qqbot` → 插件目录，最后在 `~/.dsh/config.yaml` 加一个 `- insert: [{id: dsh-qqbot, name: '@dsh-local/dsh-qqbot', config: {...}}]` 条目即可被宿主装载并热重载。
- **消费的 DSH 宿主 API**：`ctx.agents.{get,create,resume}`、`ctx.get('sessionPersistence')`、`ctx.commands.register`、`ctx.on('session/event', ...)`、`ctx.on('dispose')`、`ctx.effect`、`ctx.logger`、`ctx.setTimeout/clearTimeout`、`ctx.get('llm').{listProviders,listModels}`（用于 `/models` 校验）。
- **会话命名空间**：`qq-c2c-<openid>` / `qq-group-<group_openid>` / `qq-guild-<channel_id>` / `qq-dm-<guild_id>`，与 Web GUI 共享会话持久化层。
- **凭据回写**：直接编辑 `~/.dsh/config.yaml`（个人 overlay，被 `dsh web` 的 HMR 监听）—— 不依赖 YAML parser，按行 regex 改写。
- **状态文件**：`~/.dsh/qqbot-state.json`（去重窗口 + `/new` 代数）、`~/.dsh/qq-workspace/`（agent 工作目录）。
- 与同 org 的 `tg-bot` 是平行的"IM 远程通道"兄弟插件：架构对称（每聊天一会话、流式回送、热重载友好），区别仅在协议层（QQ 用 WS 网关 + 应用级 token，Telegram 用 Bot API HTTP 长轮询）。

## 亮点与风险
**亮点**
- **真正的零运行时依赖**：`package.json` 没有任何 `dependencies`，QQ WS 协议、token 刷新、AES-GCM 解密、YAML 行级改写全用 Node 内置 API 实现，体积小、审计容易。
- **扫码绑定免开放平台操作**：`/qq bind` 一条命令拿到二维码，AES-256-GCM 解密密钥只在本机生成、从不外传，凭据全程加密传输（`lib/onboard.js`）。
- **生产级的连接韧性**：关闭码分类（致命/会话失效/token 失效/限流）+ 退避 + 快速断开熔断 + 进程级单连接守卫 + 跨实例持久化去重，把 HMR 双连、重放、错配都考虑到了（`lib/qq-client.js` 行 ~50、~330、~395）。
- **测试覆盖核心路径**：`tests/qq-client.spec.mjs`（14 KB）用 FakeWebSocket + Fake fetch 跑握手、心跳、关闭码、Markdown 回退、分片；`tests/onboard.spec.mjs`（8 KB）覆盖绑定流，无网络依赖。

**风险**
- **凭据明文落盘**：`lib/credentials.js` 把 `clientSecret` 以 JSON 字符串明文写进 `~/.dsh/config.yaml`（无 OS keychain、无文件权限收紧）。`writeFile` 也没显式 `chmod 600`。位置：`lib/credentials.js` 行 ~110 `writeCredentialsToConfig`。
- **License 不一致**：`package.json` 声明 `"license": "BSD-3-Clause"`，但仓库根的 `LICENSE` 文件实际是 MIT 文本（"MIT License Copyright (c) 2026 dsh-external"）。下游合规会困惑。
- **Identify 硬编码 `$os:'darwin'`**：`lib/qq-client.js` `sendIdentify()` 上报的 `properties.$os` 永远是 `'darwin'`，不论实际 OS，可能影响 QQ 后端的风控/统计准确性（行 ~355）。
- **绑定流绕过可注入 fetch**：`lib/index.js startBindFlow` 调 `createBindTask()` / `pollBindResult(globalThis.fetch, ...)` 直接用 `globalThis.fetch`，没像库内其他模块那样接受可注入 `fetchImpl`；测试只能通过 stub `globalThis.fetch` 介入（行 ~125、~145）。
- **模型列表静默截断**：`agent-bridge.js handleModelsCommand` 把 `/models` 输出硬截到前 20 条（`models.slice(0, 20)`），仅一行 "…共 N 个" 提示，无翻页/筛选（行 ~430 附近）。
- **频道（guild）能力残缺**：README 自承频道媒体上传 v1 不支持；`postMessage` 里 guild 分支用 `/channels/{id}/messages` 且不携带 `msg_seq`，与 C2C/group 路径形态不同，未来扩展时易踩坑（`lib/qq-client.js` 行 ~625）。

## 维护状态
- **default_branch**：`main`。
- **最近 push**：2026-08-05 02:32 (+0800)，对应 2026-08-04 18:32 UTC，与仓库元数据一致。
- **提交活跃度**：极早期 —— 全仓只有 **1 个 commit**（`e08f9f4 dsh-qqbot: chat with your DSH agent in QQ (QQ Bot API v2)`，作者 `dsh-external`）。属于"首版一次性投递"，尚无迭代历史可观察维护节奏。
- **README 质量**：优秀。包含架构时序图、前置条件、安装步骤、完整配置项表格、斜杠命令清单、行为细节（去重/重连/权限）、已知限制与后续方向；中文撰写，工程文档级别的完整度。
- **CI/工程化**：未见 `.github/`、lint、`prettier`、`package.json` scripts 等；测试只能用 `node --test tests/` 手跑。

## 备注
- 仓库描述里写的 "0KB / JavaScript" 与实际不符：clone 后约 34 KiB 源码 + 6.5 KB README，是有完整功能与测试的首版插件。
- 与同 org 的 `tg-bot` 是"IM 远程通道"系列的两个对等实现：QQ 版面向国内用户、协议是 WS 网关 + 应用 token；Telegram 版面向海外、协议是 HTTP 长轮询。两者共用同一套 DSH 会话/持久化 seam，可叠加部署（每份插件独立 `id`）。
- 一次只连一个机器人实例；多机器人需要多份插件配置（README 明示）。
- 不支持内联键盘（`INTERACTION_CREATE` 暂不处理），因此跨端审批按钮、更新确认等交互暂不可用 —— 这是聚合报告里值得标注的"通道能力短板"。
