# session-chatlog 调研摘要

## 一句话定位
DeepSeek Harness（dsh）的外部 cordis 插件，向模型暴露两个工具 `session_list` 与 `session_read_chat`，使其能够只读地枚举并读取本机共享会话存储（`~/.dsh/sessions`）中任意持久化会话的聊天记录——包括其他 agent / 其他进程的会话。

## 技术栈与依赖
- 语言/打包：TypeScript（`typescript ^5.9.0`），ESM（`"type": "module"`），源码 `src/`，编译产物 `lib/`（JS + `lib/types/*.d.ts`）已入库。
- 运行时框架：cordis（`^4.0.0-rc.7`），通过 `apply(ctx, config)` 注册插件，schemastery（`^3.18.0`）声明 `Config`。
- dsh peerDependencies（宿主须提供）：`@deepseek-ai/dsh-session`、`@deepseek-ai/dsh-session-persistence`、`@deepseek-ai/dsh-system-prompt`、`@deepseek-ai/dsh-tools`（均 `^0.0.1`）。`inject = ['tools', 'systemPrompt', 'sessionPersistence']`（`src/index.ts:36`）。
- Node 内建：`node:fs/promises`、`node:zlib`（zstd 解码）。
- 测试：vitest（`tests/tool-session-chatlog.spec.ts`，含 FakePersistence 后端 + cordis Context 全栈组合）。
- 构建：`scripts/build.sh` 通过 symlink dsh checkout 内的 vendored 包到本地 `node_modules` 再跑 tsc，与 marisa-panel 同款做法。
- 许可证：BSD-3-Clause；包名 `@dsh-external/session-chatlog`，私有（`"private": true`）。

## 文件结构概览
```
session-chatlog/
├── dsh.plugin.json              # 插件清单：id、main、contributes.tools
├── package.json                 # 依赖与导出（main → lib/index.js）
├── tsconfig.json                # tsc 配置
├── README.md                    # 中文文档（安装/工具/配置/局限）
├── probe.mjs                    # 真实 dsh 启动探测（无 API key 验证工具注册）
├── scripts/build.sh             # 链接 dsh checkout 依赖并编译
├── src/
│   ├── index.ts                 # apply()：注册 systemPrompt section + 2 个工具；transcript 投影
│   └── operations.ts            # listSnapshots/inspect/locate + zstd 容错解码 + preview 头读
├── lib/                         # 编译产物（含 types/ 声明）
└── tests/tool-session-chatlog.spec.ts   # vitest 集成测试
```

## 核心功能与实现要点
1. **两个模型可见工具**（`src/index.ts:79-110`）：
   - `session_list`：无参数，调 `ctx.sessionPersistence.listSnapshots()`，返回 `{id, cwd, createdAt, revision, preview}`，按 `createdAt` 升序（`operations.ts:38-50`）。
   - `session_read_chat`：参数 `id`（必填）、`limit`（尾部截取）、`includeReasoning`；调 `readSessionTranscript` 拿事件流，过滤 `user/message`、`steering/message`、`assistant/message` 三类聊天事件，按 `seq` 升序输出（`src/index.ts:178-198`）。
2. **消息文本提取兼容两种形状**（`src/index.ts:147-175`，`operations.ts:81-99`）：user/steering 走 `data.content[]`，assistant 走 `data.message.content[]`；只取 `type === 'text'` 的块拼接，reasoning 块按配置单独返回。
3. **非变更读取保证**：通过 `inspect` / `listSnapshots`（均为只读 API）观察外部会话，不会修复 torn tail 或关闭未完成回合——这是 README 与 `operations.ts` 模块注释反复强调的契约（README "概述" 段，`operations.ts:8-10`）。
4. **容错 zstd fallback 链**（`operations.ts:117-160`）：`inspect` 严格校验失败（如并发写留下的 seq gap）时，自动 `listSnapshots().find(id)` 定位、`ctx.sessionPersistence.locate(header)` 拿到 JSONL 工件路径，再走手写的 `scanZstdFrames`（魔数 `0xFD2FB528`，`operations.ts:138-180`）逐帧 `zstdDecompressSync` 解码、`parseEventLines` 跳过坏行，保证聊天记录仍可读。
5. **廉价 preview 头读**（`operations.ts:58-79`）：`session_list` 的 `preview` 字段（首条 user 消息前 160 字符）只解码 JSONL 工件前 4 个 zstd 帧（`PREVIEW_FRAME_LIMIT = 4`），避免大开销；`locate` 返回非 jsonl 或失败时返回 null。
6. **系统提示注入**（`src/index.ts:67-72`）：`apply` 内 `ctx.systemPrompt.section({ name: 'tool:session-chatlog', order: 114, text: PROMPT_TEXT })`，order=114 与其他 dsh 工具提示排序衔接。
7. **配置项**（`src/index.ts:46-50`）：`maxMessages`（默认 200，1–10000）、`includeReasoning`（默认 false），通过 schemastery 在 Loader 侧落默认值并生成配置文档。
8. **探测脚本**（`probe.mjs`）：用 `@deepseek-ai/dsh-app-boot` 的 `boot()` 真实启动 dsh 组合（base + personal overlay），provide `launcherSessionQueryPath` 后断言两个工具在 registry 上注册；CI/部署自检入口。

## 与 DeepSeek Harness 主仓库的集成点
- **seam = cordis 服务注入**：通过 `inject = ['tools', 'systemPrompt', 'sessionPersistence']`（`src/index.ts:36`）依赖三个宿主服务，宿主需在 `cordis.yml` 已挂载 `sessionPersistence`（README "宿主前提"明确：内置 `@deepseek-ai/dsh-session-persistence-jsonl` 或 `-sqlite` 任一即可）。
- **协议契约**：
  - 调用 `ctx.sessionPersistence.listSnapshots()` → `SessionPersistenceSnapshot[] { header, revision }`
  - 调用 `ctx.sessionPersistence.inspect(SessionId)` → `{ meta: SessionHeader, events: SessionEvent[] }`
  - 调用 `ctx.sessionPersistence.locate(header)` → `SessionLocation | undefined`（仅 `kind === 'jsonl'` 时使用路径）
  - 调用 `ctx.tools.register(defineTool({...}))`、`ctx.systemPrompt.section({...})`
  - 事件类型契约：`SessionEvent`（`@deepseek-ai/dsh-session`）、`type` ∈ {`user/message`, `steering/message`, `assistant/message`}，seq 升序。
- **分发方式**：dshx 外部插件（`dshx install session-chatlog`），清单 `dsh.plugin.json`（`id: session-chatlog`, `engines.dsh >= 0.0.1`, `contributes.tools`），与 marisa-panel 等同为 dsh-external 仓库族的外部 cordis 插件；无对主仓库的源码补丁。
- **类型来源**：peer dep 指向 `@deepseek-ai/dsh-*`（dsh 主仓库 packages/* 发布的子包）；`scripts/build.sh` 通过 symlink dsh checkout 的 vendored 包让 tsc 在线类型检查与运行时 dsh 一致。

## 亮点与风险
- **亮点**
  - 双层容错（严格 `inspect` → 容错 zstd 直读）应对多 agent 并发写造成的损坏，对"跨 agent 共享存储"场景特别实用（`operations.ts:117-135`）。
  - preview 头读限制前 4 帧（`operations.ts:23-25, 58-79`），避免长会话列项放大开销，思路借鉴 Codex `read_head_summary`。
  - 非变更语义边界清晰：明确以 `inspect`/`listSnapshots` 为读取入口，绝不触发 `append`/修复（`operations.ts:8-10`，README "概述"）。
  - 测试覆盖完整：含 FakePersistence 的 locate 缺失、inspect 抛错、limit/includeReasoning、未知 id 拒绝等路径（`tests/tool-session-chatlog.spec.ts`）。
- **风险**
  - **隐私/越权面**：工具按设计可读取本机所有持久化会话（含其他 agent / 其他 owner），当前 `session_list` 无 workspace/owner 过滤（README "Known Limitations" 自陈；`src/index.ts:79-91` 无过滤参数）。
  - **手写 zstd 帧解析**：`scanZstdFrames`（`operations.ts:138-180`）自行解析 descriptor、block header、checksum，正确性高度依赖测试；reserved 位、dictionary、single-segment 等分支任一处偏差可能漏帧。属于"自造轮子"在 `node:zlib` 之上的局部解构。
  - **preview 依赖 locate 后端**：`session_list` 的 `preview` 只在 `locate()` 返回 `kind === 'jsonl'` 的后端上有效；FakePersistence 测试中 preview 恒为 null（`tests/...:108` 注释佐证），SQLite 后端是否会缺失 preview 值得关注。
  - **作用范围窄**：`session_read_chat` 仅返回聊天消息，不含 tool call/result、todo、turn/start 等事件（README "Known Limitations"），无法满足需要完整事件审计的用例。
  - **`lib/` 入库**：仓库提交了编译产物（`lib/index.js`、`lib/operations.js`），与 `package.json.files: ["lib"]` 配合用于无构建安装，但意味着源码与产物需同步维护。

## 维护状态
- **最新提交**：`7a29e31 docs: single Chinese README (README.md), remove the English/zh pair`，时间 **2026-08-05**（与调研日同期）。
- **作者署名**：`DSH Agent`（自动化/agent 提交），浅克隆仅可见 1 条提交。
- 版本 `0.1.0`，与 `dsh.plugin.json`、`package.json` 一致。
- 判定：**活跃维护**——最新提交即日，文档刚刚整合为单一中文 README，依赖对齐 cordis 4.x / dsh 0.0.1 现行线。

## 备注
- 仓库非空、非占位；属于 dsh-external 外部插件族（与 marisa-panel、gh-bridge、telegram-bot 等并列），服务于"模型可观察任意持久化会话"这一 dsh 核心能力补全场景。
- 安装路径与卸载：`dshx install session-chatlog <目录|git-url>` / `dshx remove session-chatlog`（README "安装"）。
- 隐私注意点：在共享开发机或多 agent 主机上，该工具会让任何装载它的 agent 读到其他 agent 的对话；如需隔离应在 `session_list` 增加过滤参数（README 已自陈此项 deferred work）。
- 摘要中未出现作者真实姓名/邮箱；GitHub 用户名/agent 昵称（`DSH Agent`）按要求保留。
