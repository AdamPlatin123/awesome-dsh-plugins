# dsh-wecom-bot 调研摘要

## 一句话定位
DeepSeek Harness 官方插件，通过**企业微信「AI 智能机器人」WebSocket 网关**（`wss://openws.work.weixin.qq.com`）把企业微信私聊与群聊接入 DSH agent——**无需公网端点、无需回调配置**，每个聊天一个持久会话。

## 技术栈与依赖
- **运行时**：Node.js（ESM，`"type": "module"`），纯 Node 内置 API（`node:https`、`node:crypto`、`node:events`、`node:fs/promises`、`node:os`、`node:path`）
- **运行时依赖：零**（`package.json:14` BSD-3-Clause；只有 `node:test` + `node:assert` 做测试）
- **版本**：`dsh-wecombot@0.1.0`，`main: lib/index.js`
- **测试**：`tests/*.spec.mjs` 用 `node:test`（wecom-client 13KB / ws-client 7KB / onboard 5KB），全部基于可注入的 fetch/WebSocket 实现，零外部测试框架
- **无构建步骤、无 lint、无 CI 配置**（仓库根只有 `package.json` / `README.md` / `LICENSE` / `.gitignore` / `lib/` / `tests/`）

## 文件结构概览
```
dsh-wecom-bot/
├── lib/
│   ├── index.js          6.4KB   插件入口（cordis 风格 apply/inject + /wecom 命令）
│   ├── wecom-client.js   25.5KB  企业微信 AI Bot 协议客户端（订阅/回调/回复/上传/重连）
│   ├── ws-client.js       8.7KB  自实现 RFC 6455 WebSocket（基于 node:https）
│   ├── agent-bridge.js   18.5KB  消息↔DSH agent 会话桥（每个 chat 一个 session）
│   ├── config.js          4.2KB  配置归一化 + 三档访问控制（open/allowlist/disabled）
│   ├── onboard.js         4.2KB  扫码绑定：拉二维码任务 + 轮询结果
│   └── credentials.js     4.3KB  把绑定结果按行写回 ~/.dsh/config.yaml（无 YAML 解析器）
├── tests/
│   ├── wecom-client.spec.mjs  13.4KB
│   ├── ws-client.spec.mjs      7.2KB
│   └── onboard.spec.mjs        4.8KB
├── package.json   400B
├── README.md      6.4KB
└── LICENSE        1.0KB（BSD-3-Clause）
```

## 核心功能与实现要点

1. **零依赖 WebSocket 客户端**（`lib/ws-client.js`）：用 `node:https` 手写 RFC 6455（client 掩码、ping/pong、close 握手、frame 解析），不用内置 `WebSocket`。原因写在文件头：某些网络中间设备会按 TLS 指纹拦截 undici 的 `WebSocket`，而 `node:https` + libcurl 能过（`lib/ws-client.js:1-15`）。表面 API 与内置 `WebSocket` 兼容（`addEventListener`/`send`/`close`/`readyState`）。

2. **企业微信 AI Bot 协议封装**（`lib/wecom-client.js`）：
   - 连接 → `aibot_subscribe {bot_id, secret, device_id}` 等 errcode=0 ack（`lib/wecom-client.js:295-310`）
   - 入站：`aibot_msg_callback` / 旧版 `aibot_callback` 归一化为 `{kind:'c2c'|'group', chatId, userId, messageId, content, reqId}`
   - 出站：优先 `aibot_respond_msg`（关联入站 `req_id`，**群聊必须用回复模式**）；私聊无回复上下文时降级 `aibot_send_msg`（`lib/wecom-client.js:519-565`）
   - 协议帧格式：`{cmd, headers:{req_id}, body:{...}}`，按 `req_id` 关联请求/响应（`lib/wecom-client.js:18-23`）
   - 30s 应用层 `ping` 心跳；指数退避重连 2/5/10/30/60s（`lib/wecom-client.js:39-41`）
   - 进程级单连接守卫：同一 `botId` 只允许一个活跃 `WeComClient`（`activeClients` Map，`lib/wecom-client.js:60` 与 `start()` 内的替换逻辑），避免热重载产生双连接

3. **每聊天一个持久会话**（`lib/agent-bridge.js`）：
   - 私聊 `wecom-c2c-<userid>`、群聊 `wecom-group-<chatid>`
   - 通过 `ctx.agents.create` 创建，或当 `ctx.sessionPersistence` 里能找到该 id 时用 `ctx.agents.resume` 恢复——和 Web GUI 走同一会话存储，**重启 dsh 后对话仍在**，且出现在 Web 会话列表
   - `/new`（`/reset` 同义）按 chatKey 把代数 +1，会话 id 加 `-g<n>` 后缀，旧对话归档而非删除（`sessionIdFor`，`lib/agent-bridge.js:55-62`、`STATE_FILE=~/.dsh/wecombot-state.json`）
   - 监听 `ctx.on('session/event')`，只在 `turn/start`→`assistant/message`→`turn/end` 这一轮里把 assistant 文本回送；每轮首条用回复模式关联入站 messageId，后续分片主动发送（`lib/agent-bridge.js:407-450`）

4. **聊天内斜杠命令**（不走模型，`handleCommand`）：`/help` `/new`(`/reset`) `/status` `/model [厂商/]模型名` `/models [厂商]`；模型切换是**会话级**，存内存（重启回退默认），切换后销毁旧 handle 用新路由重建（`lib/agent-bridge.js:301-374`）。`/model` 会通过 `ctx.get('llm').listProviders()` 校验厂商存在。

5. **入站富文本归一化**（`lib/wecom-client.js`）：
   - 群聊自动剥离开头 `@机器人` 前缀（`normalizeMessage` 里 `content.replace(/^@\S+\s*/, '')`）
   - 引用消息以 `[引用消息]` 段落拼到提示词前面（`extractQuote`）
   - 图片/文件/语音做文字摘要（`[图片]`、`[文件: 名]`、语音转写），混合消息拆解（`extractAttachmentSummary`）
   - 客户端把长消息拆成多条回调时，纯文本按 600ms（接近 3900 字阈值时 2000ms）防抖窗口合并（`queueTextMessage`，`lib/wecom-client.js:344-368`）
   - 300 秒/1000 条双窗口去重，且去重表落盘——重连重推与热重载双连接都不会重复处理

6. **扫码绑定流程**（`lib/onboard.js` + `lib/index.js` 的 `/wecom bind`）：
   - 调 `https://work.weixin.qq.com/ai/qc/generate?source=dsh-wecombot` 拿 `scode`
   - 拼出 `https://work.weixin.qq.com/ai/qc/gen?source=dsh-wecombot&scode=...` 给用户用手机企业微信打开
   - 后台每 3s 轮询 `query_result`，5 分钟超时；成功拿到 `bot_id` + `secret`
   - 写入 `~/.dsh/config.yaml` 的 `dsh-wecombot` 条目，触发 dsh web 的 HMR 自动重连（无需重启进程）
   - **依赖的是企业微信管理后台网页版机器人创建流程的非公开接口**，README 与源码均明确警告"可能随官方页面改版而变化"

7. **三档访问控制 + 双重安全网**（`lib/config.js`）：
   - 私聊 `dmPolicy`、群聊 `groupPolicy` 各自 `open` / `allowlist` / `disabled`
   - `allowFrom` / `groupAllowFrom` 白名单；`ownerIds` 是"始终放行"的第二道安全网
   - 缺凭据**不致命**：插件照常加载，client 拒连并打 warn，`/wecom status` 报告缺口

8. **凭据写回用按行编辑而非 YAML 解析**（`lib/credentials.js`）：保持零依赖前提下，按 `id: dsh-wecombot` 行定位，按 6 空格/8 空格缩进规约插入或替换 `botId`/`secret`；找不到条目就追加完整 `- insert:` 块。

## 与 DeepSeek Harness 主仓库的集成点
**形态**：标准 DSH / cordis 风格的"永久插件"（permanent plugin），通过 `~/.dsh/plugins/dsh-wecombot/` + `node_modules/@dsh-local/dsh-wecombot` 软链安装，在 `~/.dsh/config.yaml` 写 `insert` 条目。

**Seam / 协议**（与 tg-bot / qqbot / feishu-bot 等同类通道插件一致）：
- `export const name = 'dsh-wecombot'`；`export const inject = ['agents', 'commands']`
- `export function apply(ctx, config)`：`ctx.logger`、`ctx.effect()`、`ctx.on('dispose')`、`ctx.commands.register({name, input, handler})`
- **agent 生命周期**：`ctx.agents.get(id)` / `ctx.agents.create({sessionId, agentOptions:{provider,model}, meta:{cwd}})` / `ctx.agents.resume({resumeSessionId, agentOptions})` / `handle.dispose()`
- **会话持久化**：`ctx.get('sessionPersistence').list()` 查已有会话
- **会话事件流**：`ctx.on('session/event', (session, event) => …)`，过滤 `turn/start` / `assistant/message` / `turn/end`，按 `event.data.turn` 关联
- **LLM 元数据**：`ctx.get('llm').listProviders()` / `.listModels(provider)` 给 `/model`、`/models` 提供校验与列表
- **配置热重载**：依赖 dsh web 对 `~/.dsh/config.yaml` 的 HMR 监听，绑定写回即触发插件重启
- **消息构造**：自行 `deepFreeze(structuredClone(...))` 复刻 `dsh-llm` 的 `createUserMessage` 形状（`{id, role:'user', content:[{type:'text',text}], source:{kind:'user'}}`）

**与 tg-bot / qqbot 的定位差异**：
- 协议层不同——tg-bot 走 Telegram Bot HTTP 长轮询/webhook，qqbot 走 QQ 频道/OpenSham 等；本插件走企业微信**专有的 AI 机器人 WebSocket 网关**，**不暴露任何公网端口**（README 头条卖点）
- 业务约束不同——企业微信群聊**只能用回复模式**（`aibot_respond_msg`），不能主动发言；私聊可降级主动发送
- 通用骨架（每聊天一会话、`/new` 归档、`/model` 会话级覆盖、`session/event` 驱动出站、文本命令直通）与同类通道插件完全对齐，可视为同一"聊天通道插件"模板的企业微信实例

## 亮点与风险
**亮点**
- **零运行时依赖**：连 WebSocket 都自实现，部署只需 Node 内置能力（`lib/ws-client.js` 整套 RFC 6455）
- **进程级单连接守卫**（`lib/wecom-client.js:60`、`start()` 内 incumbent 替换）+ 跨实例持久化去重（`lib/agent-bridge.js:130-160`），双保险防热重载/重连导致的消息重复处理
- **回复关联做得扎实**：`replyReqIds`（msgid→req_id）+ `chatReqIds`（chatid→最新 req_id）双映射，群聊无 replyTo 也能回（`resolveReplyReqId`，`lib/wecom-client.js:583-591`）
- **入站长消息合并 + 出站长消息分片**（4000 字上限，优先换行/句号切分，`chunkText`，`lib/wecom-client.js:648-662`）
- **可注入式设计**：`WebSocketImpl`、`fetchImpl`、`backoff`、`stateFile` 都可从测试替换，可测性好

**风险**
- **扫码绑定走非公开接口**：`work.weixin.qq.com/ai/qc/{generate,query_result}` 是管理后台网页的内部接口，源码与 README 均明示"可能随官方页面改版失效"（`lib/onboard.js:10-15`、`README.md` 方式一注解）；好在有手动配置兜底
- **按行编辑 YAML 写凭据**：`credentials.js` 假设 `id: dsh-wecombot` 行下 6 空格缩进 `name`、8 空格缩进 `config.botId/secret`；用户手改 config.yaml 导致缩进异常时可能插错位置（`lib/credentials.js:55-110`）
- **企业微信自建应用回调模式（HTTP 回调 + 主动消息）未实现**：当前只支持 AI Bot WebSocket 模式，已有公网端点的用户无法走经典回调路径（README"已知限制"）
- **出站暂不支持发图/文件**：`aibot_upload_media_init/chunk/finish` 三步上传协议已在客户端封装（`uploadMedia`/`sendMedia`），但 agent-bridge 还没调用——入站附件也只做文字摘要
- **企业微信 AI 机器人本身是新协议**：官方文档有限，帧格式与 errcode 含义多靠逆向，未来变更风险高于成熟 IM 协议
- **模型切换仅存内存**：`modelOverrides` 是 `Map`，重启 dsh 后回退到 config 默认路由（README 已注明）

## 维护状态
- **全新仓库**：git 历史仅 1 个 commit（`82842e6`，2026-08-05 04:34:51 +0800，提交者 `edgarHeiMac`），即调研当天首度提交
- 版本号 `0.1.0`，处于早期阶段
- 测试覆盖较扎实（三个 spec 文件覆盖 client/ws/onboard+credentials 主要路径），但无 CI/lint/自动发布配置
- 无 Issues / PR / Release 数据可参考（克隆为 `--depth 1`，且为新仓）

## 备注
- **包名拼写不一致**：仓库名 `dsh-wecom-bot`，但 `package.json.name`、插件 `name`、README 标题、配置条目 id、安装目录都写作 `dsh-wecombot`（无连字符）；阅读与安装时需注意
- 文档质量高：README 中文，覆盖工作流图、前置条件、两种绑定方式、完整配置项表、斜杠命令清单、行为细节与已知限制，可作为同类通道插件的文档样板
- 与同组织 `dsh-tg-bot` / `dsh-feishu-bot` / `dsh-weixin-bot`（个人微信）等并列，构成 DSH 的"IM 通道插件矩阵"；本仓是企业微信侧的唯一通道
- 安全模型清晰：三档策略 + `ownerIds` 双重保险；但默认 `dmPolicy=open`/`groupPolicy=open`，部署时若不显式收紧，企业内任何成员/群都能直接对话 agent，需在 README 或部署文档中强调
