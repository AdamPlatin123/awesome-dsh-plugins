# dsh-feishu-bot 调研摘要

## 一句话定位
DeepSeek Harness 的飞书/Lark 远程通道插件——通过飞书官方长连接（WebSocket）协议把飞书私聊与群聊 @机器人 变成 agent 的对话界面，零运行时依赖。

## 技术栈与依赖
- 语言：纯 JavaScript（ESM，`"type":"module"`），Node ≥ 22（用了 `Promise.withResolvers`、全局 `WebSocket`、全局 `fetch`）
- 运行时依赖：**无**（README 强调 "零运行时依赖"；`package.json` 无 `dependencies`/`devDependencies`，连测试也只用 `node:test` + `node:assert`）
- 关键内置能力：`node:events`、`node:crypto`（randomUUID）、`node:fs/promises`、`node:os`、`node:path`、全局 `WebSocket`（undici）、全局 `fetch`、`TextEncoder/TextDecoder`
- 协议：飞书开放平台长连接 WS 协议（自写 protobuf 帧编解码 `pb.js`）+ REST `im/v1/messages`、`auth/v3/tenant_access_token/internal`、`bot/v3/info`
- 包元信息：`name: dsh-feishu`, `version: 0.1.0`, `private: true`, `main: lib/index.js`；`package.json` 声明 `BSD-3-Clause`，但仓库根 `LICENSE` 文件其实是 **MIT**——两者不一致（见风险）

## 文件结构概览
```
dsh-feishu-bot/
├── README.md          5.4 KB  使用/配置/已知限制全说明
├── package.json       413 B   零依赖、ESM、private
├── LICENSE            1.0 KB  MIT（与 package.json 的 BSD-3-Clause 不一致）
├── .gitignore         24 B    node_modules/、.DS_Store
├── lib/
│   ├── index.js          6.7 KB  插件入口（apply/inject/export）、/feishu 命令、绑定流程
│   ├── feishu-client.js  24.8 KB 长连接 WS 客户端 + REST 发消息 + 消息归一化
│   ├── agent-bridge.js   18.8 KB 会话桥（每聊天一会话、内联命令、事件订阅）
│   ├── pb.js             7.2 KB  手写 protobuf 帧编解码（飞书 Frame proto2）
│   ├── onboard.js        5.1 KB  扫码绑定（device-code flow）
│   ├── credentials.js    3.6 KB  把绑定结果写回 ~/.dsh/config.yaml
│   └── config.js         3.9 KB  配置归一化 + 访问控制（allows）
└── tests/
    ├── feishu.spec.mjs   14.6 KB 协议/客户端/归一化/onboard 单测
    └── bridge.spec.mjs   5.1 KB  会话桥单测
```
共 7 个源文件 + 2 个测试文件，约 75 KB；仓库 GitHub size=33 KB。

## 核心功能与实现要点

1. **长连接协议实现（`lib/feishu-client.js:1-300` + `lib/pb.js`）**
   先 `POST /callback/ws/endpoint` 用 AppID/AppSecret 换 wss URL 和 `client_config`（重连/抖动/Ping 间隔由服务端下发）；连上 WS 后所有帧都是 `pb.js` 编解码的 protobuf Frame（`method=0` CONTROL / `method=1` DATA）。CONTROL 的 ping 不回、pong 可能携带新 `client_config`；DATA 帧头 `type=event` 的载荷是事件 JSON，多片消息按 `message_id + seq` 重组（`combine()`，TTL 5s）。收到事件帧后必须把同一帧回带 `{"code":0}` 作为 ACK（`ackFrame()`），否则飞书会重推。客户端 `binaryType='arraybuffer'`——注释明确指出 undici 默认 `blob` 会让 protobuf 解码抛错。`USER_AGENT = 'dsh-feishu/0.1 channel'`——缺 `channel` 标记就不会被识别为 Channel 协议客户端，**收不到消息事件**。

2. **断线重连与单连接守卫（`lib/feishu-client.js:300-380`）**
   重连参数全部来自服务端 `client_config`，`ReconnectCount=-1` 表示无限重连；重连前加一个 `Math.random()*ReconnectNonce` 抖动。模块级 `activeClients: Map<appId, FeishuClient>` 做单连接守卫——同一 appId 只允许一个长连接，热重载时新实例会先 `stop()` 旧实例（README 行为细节里提到的 "热加载时新连接会先关闭旧连接"）。

3. **每聊天一会话 + 重启续接（`lib/agent-bridge.js:1-120, 380-460`）**
   会话 id 规则：私聊 `feishu-p2p-<openid>`，群聊 `feishu-group-<chatId>`；`/new` 自增 `generation`，id 加 `-g<n>` 后缀（旧对话归档在 `~/.dsh/sessions`）。generation 与 300s 去重窗口持久化到 `~/.dsh/feishu-state.json`（debounce 500ms 写盘）。首次进入通过 `ctx.agents.create()`，已存在则 `ctx.agents.resume({resumeSessionId})`（先查 `ctx.get('sessionPersistence').list()`）。这些会话同样出现在 Web GUI 会话列表里。

4. **扫码绑定（`lib/onboard.js` + `lib/index.js:startBindFlow/pollBindLoop`）**
   走飞书账号体系的 device-code 流：`POST accounts.feishu.cn/oauth/v1/app/registration` 依次 `init → begin`（archetype=`PersonalAgent`, auth_method=`client_secret`, request_user_info=`open_id`）拿 `device_code + verification_uri_complete`，用户在飞书 App 里扫码确认；后台 `poll`（每 5s，600s 超时）直到返回 `client_id/client_secret`。`tenant_brand=='lark'` 时自动切到 `accounts.larksuite.com`——**自动识别国内 feishu / 国际 lark**。绑定成功后调用 `writeCredentialsToConfig()` 把凭据写进 `~/.dsh/config.yaml` 的 `dsh-feishu` 条目，触发宿主 HMR 重连。

5. **凭据写回：行级 YAML 编辑（`lib/credentials.js`）**
   为了保持零依赖，不引入 YAML 解析器，而是按行扫描 `~/.dsh/config.yaml`，定位 `id: dsh-feishu` 行后插入/更新 `config:` 块的字段。处理三种情形：条目不存在则追加 `- insert:`；存在但无 `config:` 则插入；存在 `config:` 则原地替换或追加字段。

6. **内联斜杠命令（`lib/agent-bridge.js:handleCommand` + `handleModelCommand` + `handleModelsCommand`）**
   `/help` / `/new`（同义 `/reset`）/ `/status` / `/model [provider/]name` / `/models [provider]`。`/model` 切换是**会话级**的（写入 `modelOverrides` map，只影响当前聊天），并主动 `dispose` 当前 agent handle 让下一条消息重建。`/models` 通过 `ctx.get('llm').listModels(provider)` 拉模型列表（前 20 条）。这些命令**不走模型**，直接由插件回复。

7. **访问控制与去重（`lib/config.js:allows` + `lib/feishu-client.js:isDuplicate` + `lib/agent-bridge.js:isDuplicateMessage`）**
   两级策略：`dmPolicy`/`groupPolicy` 各为 `open|allowlist|disabled`；`ownerIds` 作为 "始终放行" 的第二道安全网。群聊消息只有在 mentions 非空时才处理（`isBotMentioned`）。**双重去重**：客户端层 1000 条上限的 LRU；桥层持久化 300s 窗口，跨重连/热加载双连接都不会重复处理。

8. **会话事件→飞书回复（`lib/agent-bridge.js:onSessionEvent`）**
   订阅 `ctx.on('session/event', ...)`，过滤本插件拥有的 sessionId。`turn/start` 记录当前 turn 号；`assistant/message`（turn 匹配且 `repliedThisTurn==false` 时）作为对原消息的 **reply** 发回（首条回复后改为普通发送），实现"流式"送达（每个 assistant step 一条消息）；`turn/end` 检查 `reason.kind`，error/max-tokens 都给用户友好提示。出站消息按 chatId 排队（`sendQueues`）保证顺序。

## 与 DeepSeek Harness 主仓库的集成点
- **形态**：纯宿主插件（README "DeepSeek Harness 插件"），遵循 cordis 风格契约——`export const name`、`export const inject = ['agents','commands']`、`export function apply(ctx, config)`。**不打补丁、不改主仓库代码**。
- **注入的服务**：
  - `ctx.agents`：`create({sessionId, agentOptions:{provider,model}, meta:{cwd}})` / `resume({resumeSessionId, agentOptions})` / `get(sessionId)` —— 与 Web GUI 同一套会话 API
  - `ctx.commands.register(...)`：注册 `/feishu status`、`/feishu bind` 宿主命令
  - `ctx.on('session/event', ...)` / `ctx.on('dispose', ...)`：cordis 生命周期
  - `ctx.get('llm')`：`listProviders()` / `listModels(provider)` —— 内联命令的模型列表来源
  - `ctx.get('sessionPersistence')`：`list()` —— 重启后续接会话
  - `ctx.logger`、`ctx.effect()`：日志与副作用注册
- **配置**：从 `~/.dsh/config.yaml` 的插件 `config:` 字段读取（`normalizeConfig`），支持 `DSH_FEISHU_*` / 旧 `FEISHU_*` 环境变量回退；绑定成功后由本插件**反向写回** config.yaml，借助宿主 HMR 触发热重载。
- **安装位置**：`~/.dsh/plugins/dsh-feishu/`，并通过 `~/node_modules/@dsh-local/dsh-feishu` 软链让宿主 resolve。
- **协议层与主仓库无关**：飞书长连接 + REST + 账号体系 device-code 流全是本插件自实现，不依赖主仓库的任何飞书相关代码（主仓库也不提供）。

## 亮点与风险

**亮点**
- **零依赖** + Node 内置 WebSocket/fetch + 自写 protobuf（`lib/pb.js:1-215`，仅 215 行实现 varint/length-delimited 编解码，能跳过未知字段，`tests/feishu.spec.mjs:30-44` 有 round-trip 测试）——体积小、攻击面小。
- **扫码即用**：用户完全不用碰飞书开发者后台，`/feishu bind` → 飞书 App 扫码 → 凭据自动写入并热重载（`lib/onboard.js` + `lib/index.js:startBindFlow`），体验明显优于同类需要手动建应用的方案。
- **国内/国际自动识别**：`tenant_brand` 检测后切换 `accounts.feishu.cn` ↔ `accounts.larksuite.com`（`lib/onboard.js:pollRegistration`）。
- **健壮的长连接**：服务端下发重连参数、抖动、ping；多片重组；ACK；持久化去重；单连接守卫——工程化程度高。
- **协议踩坑写在注释里**：例如 `USER_AGENT` 必须带 `channel` 否则收不到事件（`lib/feishu-client.js:38-43`）、undici WebSocket 必须设 `binaryType='arraybuffer'`（`lib/feishu-client.js:openSocket`）——对二次维护非常友好。
- **测试覆盖**：`tests/feishu.spec.mjs`（375 行）测 pb 编解码、客户端帧处理、归一化、onboarding；`tests/bridge.spec.mjs` 测桥逻辑。`node:test` 原生，零测试依赖。

**风险**
- **License 不一致**：`package.json` 写 `"license": "BSD-3-Clause"`，但根目录 `LICENSE` 文件是 MIT 全文（`/tmp/dsh-ext-research2/dsh-feishu-bot/LICENSE`）。下游合规需要先 reconcile。
- **手写 YAML 编辑较脆**（`lib/credentials.js:writeCredentialsToConfig`）：按行匹配 `id: dsh-feishu` 和缩进，依赖固定的 6/8 空格缩进形态；若用户手工把 config.yaml 排版得不同（tab、不同缩进层级、注释穿插），可能写错位置。无 YAML parser 是为了零依赖的取舍。
- **手写 protobuf 解码器**（`lib/pb.js`）：只实现了飞书 Frame 的最小子集，飞书未来加新字段虽能跳过（有测试），但若改 wire 类型或帧结构仍可能炸。
- **功能边界窄**（README "已知限制"）：图片/语音/视频/文件**只转占位描述**，无 OCR/STT/视觉；出站**仅文本**，无飞书卡片/审批按钮；群聊只响应 @；一次只能连一个应用实例（多应用需多份插件配置）。
- **token 缓存与 singleflight**（`lib/feishu-client.js:ensureToken`）依赖 `expire - 60s` 提前刷新，逻辑正确但未看到对 `expire` 异常值（0/负数）的防御——属次要。
- **凭据明文落盘**：`appId/appSecret` 以 JSON 字符串形式写入 `~/.dsh/config.yaml`，文件权限沿用用户 umask，无额外加密（与本家族其它 bot 一致，但值得记录）。

## 维护状态
- GitHub 元数据（`gh api repos/dsh-external/dsh-feishu-bot`）：创建于 **2026-08-04 20:14 UTC**，最近 push `2026-08-04 20:16`，最近更新 `2026-08-04 20:17`——**今天刚诞生的仓库**。
- 提交历史：**仅 2 个 commit**——`7694e4b Initial commit`（20:14:27）和 `e56e812 dsh-feishu-bot: chat with your DSH agent in Feishu/Lark (long-connection protocol)`（20:15:38）。
- 0 stars / 0 forks / 0 open issues；`archived=false`、`disabled=false`；默认分支 `main`；语言 JavaScript；size 33 KB。
- 无 CI 配置、无 CHANGELOG、无 contributor 其它仓库线索——属于首日首发状态，尚无社区使用反馈。

## 备注
- **与同家族通道的对比**（dsh-external org 下的同类 bot 仓库：`tg-bot`/`telegram`、`qqbot`、`dsh-wecom-bot`、`dsh-weixin-bot`、`dsh-feishu-bot`）：
  - **共同骨架**（qqbot / dsh-wecom-bot / dsh-weixin-bot / dsh-feishu-bot 一致）：`lib/<channel>-client.js`（传输）+ `lib/agent-bridge.js`（会话桥）+ `lib/config.js`（归一化+访问控制）+ `lib/credentials.js`（写回 config.yaml）+ `lib/onboard.js`（扫码绑定）+ `lib/index.js`（cordis `apply`）。feishu 与 qqbot、wecom-bot 一样有 `onboard.js`；weixin-bot 没有 `onboard.js`（其客户端形态略简）。
  - **feishu 独有 `lib/pb.js`**：因为飞书长连接走二进制 protobuf 帧，是本家族里唯一需要自写二进制编解码的通道；wecom-bot 虽也有 WebSocket（多了 `ws-client.js`），但不需要 protobuf。
  - **telegram 仓库结构不同**：`bridge.js`/`client.js`/`format.js`/`types/`，未采用 agent-bridge.js 命名，可能是较早或不同作者的实现。
  - 集成契约（`ctx.agents.create/resume`、`ctx.on('session/event')`、`ctx.commands.register`、`ctx.get('llm')`、`ctx.get('sessionPersistence')`、写回 `~/.dsh/config.yaml` + HMR）在 feishu 与 qqbot/wecom-bot/weixin-bot 之间是**完全一致的家族协议**——本插件是该家族的飞书实现，没有引入新的宿主侧 seam。
- `package.json` 与 `LICENSE` 的 license 字段不一致需要在引用时留意（建议以仓库 LICENSE 文件 MIT 为准，但 `package.json` 字段需修正）。
- 单测可直接 `node --test tests/` 运行（无第三方 test runner）。
