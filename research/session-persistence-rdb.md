# session-persistence-rdb 调研摘要

## 一句话定位

`@morlay/session-persistence-rdb` 是把 DeepSeek Harness 主仓内置的 SQLite 持久会话后端（`ctx.sessionPersistence`）抽出来作为**独立扩展仓库**重新实现，对外接口与主仓同名包完全兼容，但存储层换成参考 [playpen-session](https://github.com/morlay/playpen) 的三表事件存储；仓库描述 "WIP"，2026-08-05 当天新建、单 commit、单作者（GitHub 用户 `Morlay`），目前还没有 release/license/star。

## 技术栈与依赖

- 语言：TypeScript（严格模式，`tsconfig.json` 中 `strict / exactOptionalPropertyTypes / noUncheckedIndexedAccess / noImplicitOverride / noUnusedLocals/Parameters` 全开），ESM，`moduleResolution: bundler`，`allowImportingTsExtensions: true`。
- 运行时：Node.js 原生 `node:sqlite`（`DatabaseSync`），不需要 `better-sqlite3` 等原生依赖；`node:crypto/randomUUID`、`node:fs/promises`、`node:fs/statSync`。
- 包管理：`nub`（`mise.toml` 锁 `nub=latest`、`just=latest`；`.npmrc` 用本地 `./.nub-store`；`package.json` 的 `devEngines.packageManager=nub ^0.6.0`），`package.json` workspaces `packages/*`。
- 构建工具：`tsdown`（仅在 inner `package.json` 的 `files` 里出现 `lib/*`，但仓库内未见独立 build 脚本，应靠 Loader 相对路径直读源码）。
- 校验/格式化：`oxlint` + `oxfmt` + `oxlint-tsgolint`（type-aware），`vitest@^4` 复用上游契约测试。
- 依赖收敛策略：`@deepseek-harness/sdk` 通过 `resolutions` 指向 `file:../deepseek-harness-distro/tspkg/sdk`（`just sync` 克隆上游 harness，严禁修改）；`@morlay/session-persistence-rdb` inner 包以 `peerDependencies` 声明该 SDK。
- 许可：inner `package.json` 声明 `BSD-3-Clause`（但 GitHub 元数据 `license=null`，未在仓库根放 LICENSE 文件）。

## 文件结构概览

```
.
├── AGENTS.md                                仓库守则（中文）：本仓是 harness 的 session-persistence-rdb 扩展，上游源码由 just sync 克隆，不得修改 deepseek-harness/ 下文件
├── package.json                             根 workspace，devDeps（SDK/oxlint/vitest/tsdown），resolutions 把 SDK 钉到 distro 本地路径
├── nub.lock                                 nub 锁文件（~63KB）
├── mise.toml                                工具版本：nub/just
├── justfile                                 dep/test/fmt/lint/clean（用 nubx 调用 vitest/oxfmt/oxlint）
├── tsconfig.json                            独立严格 TS 配置（不继承 harness）
├── vitest.config.ts                         vitest inline `@deepseek-harness/sdk`
├── .oxlintrc.json / .oxfmtrc.json / .npmrc  工具配置
├── scripts/
│   └── repair-source-event-seqs.mts         一次性幂等修复历史库里的坏 provenance 引用（dry-run 默认，--apply 落库）
└── packages/session-persistence-rdb/
    ├── package.json                         `@morlay/session-persistence-rdb@0.0.1`，private，peerDep SDK
    ├── README.md                            ~9.8KB，详尽中文实现说明
    ├── src/
    │   ├── index.ts                         主类 `SessionPersistenceRdb`，实现 `PersistenceBackend<number>`，27KB/676 行
    │   ├── schema.ts                        建表/`openDatabase`/`scanRows`/`buildSeqMap`/`eventDimensions`/`rowToEvent`/`remapSurfaceOp`，19KB/475 行
    │   └── invariant.ts                     空的 invariant companion（注册 `session-persistence-rdb-invariant`，无运行时不变量）
    └── tests/
        ├── rdb.spec.ts                      61KB，专项用例 + 调 `runPersistenceContract`/`runCoordinatorContract` 复用上游契约
        ├── multi-instance.spec.ts           4KB，两实例共享同一 SQLite 的并发写检测
        ├── multi-session.spec.ts            8.6KB，多会话场景
        └── busy-timeout.spec.ts             4KB，busy_timeout 行为
```

## 核心功能与实现要点

1. **三表事件存储（playpen-session 风格）**：`schema.ts:openDatabase` 创建 4 张 STRICT 表——`persistence_state`（singleton + store_id UUID）、`sessions`（会话头 + head 游标 `f_head_event_id/f_head_sequence`）、`events`（全局事件实体，按 UUID 唯一，带 `f_parent_id` 父链 + `f_kind/f_role/f_name/f_action_id` 维度 + `f_original_seq` + `source_event_seqs/surface_op`）、`session_events`（会话↔事件桥接，`UNIQUE(f_session_id, f_sequence)`）；附 5 个索引（parent_id/kind/role/created_at/会话链）。建库以 `BEGIN IMMEDIATE` + `PRAGMA application_id=0x44534850` + `PRAGMA user_version=SCHEMA_VERSION(=1)` 守门；非空且 `user_version=0`、版本不匹配、application id 不符均拒绝且不迁移（`schema.ts:configureDatabase`）。

2. **delta 过滤 + 稠密重编号**：`EPHEMERAL_EVENT_TYPES = ['assistant/chunk']`（`schema.ts`）。`index.ts:appendBatch` 写入时整行丢弃 chunk 事件，存活事件按 head 游标稠密重编号，原始上游 seq 落到 `f_original_seq`；纯 delta 批次为 no-op（不建行、不 bump revision）。读取侧 `buildSeqMap`（first-wins，覆盖 resume/fork 的 seq 重叠场景）把 `sourceEventSeqs` 与位置式 `surfaceOp=replace` 的 `start/end` 从上游 seq 重映射回稠密 seq。

3. **写路径 provenance 剪枝**：`index.ts:surfaceBindings` 在写 `assistant/message` 时，从其 `sourceEventSeqs` 中剔除指向本实例已丢弃 delta 的上游 seq 引用（同批与跨批均生效，剔除后为空则存 NULL）；这是为了避免读取时 `assertProvenance` 报 `sourceEventSeqs must reference earlier events`。配套 `scripts/repair-source-event-seqs.mts` 为已落库的坏引用做一次性幂等修复（每会话一个 `BEGIN IMMEDIATE` 事务，默认 dry-run，`--apply` 落库）。

4. **并发写入者检测（fail-loud）**：`index.ts:assertNoConcurrentWriter`（在 `appendBatch` 中事务内调用）维护本实例"已确认的稠密 head" `headSeqs: Map<SessionId, number>`；磁盘 head 与该值不一致、或本实例从未读过该会话却遇到已有行时直接拒绝（`modified by another writer` / `has a persisted log this instance has not read`）。理由：稠密重编号天然不会触发 `UNIQUE(f_session_id, f_sequence)`，第二个实例若按陈旧游标续写会把两段独立 turn 静默拼成同一个 log（log 级损坏）。不同 session id 的并发写不受限。

5. **崩溃尾部修复**：`schema.ts:scanRows` 找到最后一个 `turn/end`，把它之前无法解析的行视为"committed 损坏"抛错，之后的孔视作"torn tail"截断并返回 `tornFrom`；`index.ts:commitRepair` 在单事务内 `DELETE FROM session_events` 删除 torn tail、回退 head 游标、追加合成 closers、`revision + 1`，COMMIT 后重新确认 head。

6. **保留的上游语义**：懒物化（`sessions` 行存在即视为 materialized，决定 `list` 返回集）、`locate()` 恒返回 `undefined`（无独立 per-session 文件）、`revision/incarnation` 快照、WAL 默认 `journal_mode`（可改 `delete/truncate/persist` 应对网络挂）、`busy_timeout` 默认 5000ms（`DEFAULT_BUSY_TIMEOUT_MS`）、目录/库文件 0o700/0o600 owner-only。

7. **可装配性**：实现 `PersistenceBackend<number>` 并通过 `PersistenceCoordinator` 安装写路径监听；`static inject = ["sessions"]`，`static Config` 用 SDK 的 `z` 校验 `path/journalMode/busyTimeout`；可作 `ctx.plugin(SessionPersistenceRdb, cfg)` 加载，或 cordis.yml 配置。Loader 还支持以 `.` 开头的插件名按配置文件 baseUrl 相对解析源码（无需发布到 npm、无需 node_modules 解析）。

8. **测试复用上游契约套件**：`tests/rdb.spec.ts` import 自 `@deepseek-harness/sdk/session-persistence/testing` 的 `runPersistenceContract` / `runCoordinatorContract`（契约本身不含 delta 事件，原样通过），并补三类专项用例：三表存储 + delta 过滤（`rdb.spec.ts`）、多实例并发（`multi-instance.spec.ts`）、busy_timeout 行为（`busy-timeout.spec.ts`）、多会话（`multi-session.spec.ts`）。

## 与 DeepSeek Harness 主仓库的集成点

- **协议契约**：本包**完全实现** SDK 公开的 `PersistenceBackend<number>` 接口，并继承 `SessionPersistence` 服务基类；通过 `PersistenceCoordinator` 接入会话层的写路径监听。装配后注册 cordis 服务 `ctx.sessionPersistence`（单 provider，与内置 jsonl 后端互斥）。
- **依赖解析**：`@deepseek-harness/sdk` 通过 `package.json` `resolutions` 锁到 `file:../deepseek-harness-distro/tspkg/sdk`；上游主仓源码由 `just sync` 克隆（`AGENTS.md` 明令禁止修改 `deepseek-harness/` 下任何文件）；测试经 `vite-tsconfig-paths` + `vitest` inline 直接从上游源码解析 `@deepseek-ai/*`。
- **替换内置 jsonl**：CLI 场景用 `--config-replace <cfg>` 把整棵配置树替换掉，配置里只声明这一个 persistence 插件（README 与 `index.ts:Config` 注释均强调不要并存两个 persistence 插件）。
- **共享产物**：仓库根目录所有 lint/format/test 配置独立于 harness；`.gitignore` 显式忽略 `deepseek-harness/`、`deepseek-harness-*/`、`vendor/`、`target/`、`.nub-store/`、`mise.*.toml`，把上游克隆隔离在版本控制外。
- **生态对比**：dsh-external org 还有 `session-chatlog`（只读聊天记录展示）、`dsh-session-search`（跨工具会话全文搜索）、`dsh-agent-session-sources`（agent-session dock）、`dsh-coding-receipt`（会话回执）等；本仓是其中**唯一一个重写持久化存储后端**的（其他都是消费已持久化的会话）。它是把主仓内置能力"外置化"的样板，与 `dsh-coding-receipt`/`dsh-session-search` 形成"写后端 ↔ 读消费"的分工。

## 亮点与风险

**亮点**
- README 质量极高：用中文逐项讲清楚三表设计、delta 过滤的"库内 seq 与上游内存 seq 错位"代价、并发写为什么必须 fail-loud（稠密重编号天然绕过 UNIQUE 约束）、`sourceEventSeqs` 剪枝的来龙去脉，每条都直接指向 `src/index.ts`/`src/schema.ts` 的具体行。
- 工程纪律严：所有写操作一律 `BEGIN IMMEDIATE` 单事务原子化（`appendBatch`、`commitRepair`、修复脚本每会话一个事务），`busy_timeout` 必须先于锁获取设置，所有外部数据库靠 `application_id` + `user_version` 双重守门，文件/目录 owner-only。
- 复用上游契约测试套件而非自造一套，对外可互换性有客观保证。
- 修复脚本 `scripts/repair-source-event-seqs.mts` 默认 dry-run、`--apply` 时每会话独立事务、显式回滚路径，幂等且对在跑的进程友好。

**风险**
- **极早期**：仓库今天（2026-08-05）才建，单 commit `feat: init`（`d5d45d6`），无 LICENSE 文件（GitHub 元数据 license=null，inner package.json 写 BSD-3-Clause 不一致），无 CHANGELOG，无 CI（仓库根无 `.github/`），无 release。
- **`SCHEMA_VERSION = 1` + 写路径活跃演进**：delta 过滤 + 稠密重编号 + provenance 剪枝是一套新设计，README 自承"上游未来给 chunk 分配独立通道后两套 seq 才会合一"——目前库内 seq 与上游内存 seq 不一致是已知技术债。
- **单作者**：commit author=committer=`Morlay`，bus factor 低。
- **多实例约束硬**：同一进程重复加载持久化插件、或两个 dsh 进程共享同一 `sessions.sqlite` 时，同 session id 只允许一个写入者，否则直接抛错（`assertNoConcurrentWriter`）。多实例部署必须按 session id 分流或各自独立库文件。
- **修复脚本默认路径写死 `~/.dsh/sessions/sessions.sqlite`**：跑脚本前需确认目标库路径（脚本支持位置参数覆盖）。
- **隐私/安全**：owner-only 权限仅在创建时设置；README 与 `createDatabaseFile` 注释明示"无法防御可替换该目录条目的其它 principal"。
- **`vitest.config.ts` 注释提到 `gen-sdk-types 第 9 步`**：说明 SDK 类型需要一道预处理（手动替换 import 路径），新贡献者拉下来直接 `nubx vitest run` 可能遇到解析问题，需要先走 `just sync` + `just dep`。

## 维护状态

- 创建：2026-08-05T01:34:50Z；最近 push：2026-08-05T10:05:57Z（同日）；可见性 private，未 archived，未 fork。
- 仅 1 commit、0 issue、0 star、0 fork、size 62KB；默认分支 main。
- 描述 "WIP"，无 release/tag。
- 单一作者 `Morlay`（无邮箱/真名泄露，仅 GitHub 用户名）。

## 备注

- 调研方式：`git clone --depth 1` + `gh api repos/dsh-external/session-persistence-rdb` 取元数据 + `gh api 'search/repositories?q=org:dsh-external+session'` 取生态全貌 + 直读 `README.md`/`package.json`/`src/index.ts`/`src/schema.ts`/`src/invariant.ts`/`scripts/repair-source-event-seqs.mts`/`AGENTS.md`/`justfile`/`mise.toml`/`tsconfig.json`/`vitest.config.ts`/`.oxlintrc.json`/`.gitignore`/`.npmrc`/`tests/multi-instance.spec.ts`/`tests/rdb.spec.ts`。
- 命名小坑：仓库 `session-persistence-rdb` ↔ 内部包 `@morlay/session-persistence-rdb`（scoped），与 dsh-external 生态其它包（`session-chatlog`、`dsh-session-search` 等）命名风格不一致，但与上游 harness 内同名 SQLite 包刻意"接口兼容、独立重实现"的定位吻合。
- 与主仓关系不是"集成进 harness 源码树"，而是"以独立扩展包身份被 harness 的 Loader 加载"——是 dsh-external 把 harness 内置能力外置化的样本，可以作为其它"重写某内置服务为外部扩展"项目的模板（如 Loader 相对路径插件名、契约测试复用、SDK `resolutions` 锁本地路径的套路）。
