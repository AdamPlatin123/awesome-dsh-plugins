# 安全与隐私问题清单：主仓库红线 + 插件侧风险

> 日期：2026-08-05
> 依据：`research/issues.md`（issue 编号与摘要）、`research/plugin-registry.md`、`research/qqbot.md`、`research/tg-bot.md`、`research/toybox.md`、`research/group-chat-diary.md`、`context/session-019fc8ab-summary.md`
> 脱敏声明：本文不复制任何 issue 正文、真实密钥值、成员昵称；所有论断仅引用编号、标题与摘要结论。
> 严重级定义：Critical = 信任边界可被击穿 / 不可逆数据或审计破坏；High = 数据丢失、静默失败或敏感凭据暴露；Medium = 隐私面扩大或可用性风险；Low = 合规/一致性问题。

---

## 0. 总览

| # | 问题 | 侧 | 严重级 | 建议去向 |
|---|---|---|---|---|
| 1 | AGENTS.md 无信任门槛自动升级为 system-reminder（#302） | 主仓库 core | Critical | org issue（P0） |
| 2 | Agent 可删除自身会话审计日志（#300） | 主仓库 core | Critical | org issue（P0） |
| 3 | /compact 压缩零保真校验，硬约束静默消失（#301） | 主仓库 core | High | org issue（P1） |
| 4 | torn zstd 帧静默恢复，尾部事件丢失（#176） | 主仓库 core | High | org issue（P1） |
| 5 | ENOSPC 时 spill 写入异常未捕获致进程崩溃（#73） | 主仓库 core | High | org issue（P1） |
| 6 | 跨进程并发写同一会话 JSONL seq 冲突（#118/#20） | 主仓库 core/persistence | High | org issue（P1） |
| 7 | SSE 流 ReadableStream queue 无限堆积内存泄漏（#7） | 主仓库 web | Medium-High | org issue（P1） |
| 8 | plugin-registry 同进程任意代码：无沙箱/无签名/无发布者身份 | 插件侧（生态信任） | Critical | org issue（P1） |
| 9 | qqbot 凭据明文落盘 config.yaml，无 chmod 600 | 插件侧 qqbot | High | org issue（P1） |
| 10 | tg-bot token 明文存 settings 文件与进程环境 | 插件侧 tg-bot | High | org issue（P2） |
| 11 | toybox time-capsule 胶囊明文 JSON 落地 | 插件侧 toybox | Medium | org issue（P2）/ toybox 自修 |
| 12 | group-chat-diary 内嵌 109 名成员 PII | 插件侧 group-chat-diary | High（合规） | 本 repo（隐私整改）+ org issue（P2） |

---

## 1. 主仓库红线（依据 issues 台账 #147 与 research/issues.md）

### 1.1 #302 AGENTS.md 注入：无信任门槛自动升级为 system-reminder —— Critical

- **问题**：仓库级 `AGENTS.md` 内容无需任何信任声明/同意环节即被升级为 system-reminder 注入；注入封套与真实系统提醒逐字节相同，模型无法区分"用户仓库里的指令"与"系统真实约束"。
- **影响**：克隆/打开一个含恶意 AGENTS.md 的仓库即可在无感知下改写模型行为，是完整的信任边界击穿向量（供应链级）。
- **修复建议**：① AGENTS.md 需显式 opt-in（如头部声明"本文件可作为指令"）才允许升级为 system-reminder，否则仅作为可读上下文；② 注入封套引入可区分标记（不同前缀/签名）；③ 升级动作触发用户可见提示（TUI/Web 横幅）。
- **建议去向**：**org issue（P0）**——这是主仓库信任边界缺陷，需上游修复，本 repo 只能做证据汇总。

### 1.2 #300 审计日志可自删：无篡改检测、exit 0 无诊断 —— Critical

- **问题**：workspace 模式下 agent 可删除自身会话审计日志：无沙箱防护、无篡改检测，删除后进程 exit 0 无任何诊断。
- **影响**：审计日志是事后追责的唯一依据，可被 agent（或被注入的指令）静默抹除，审计完整性归零。
- **修复建议**：① 审计日志 append-only 存储（独立于 workspace 的目录 + 只追加文件句柄）；② 删除/截断操作本身写审计事件并告警；③ 日志链加 HMAC 或摘要链做篡改检测；④ 会话结束时校验日志完整性，不一致则非零退出并提示。
- **建议去向**：**org issue（P0）**。

### 1.3 #301 /compact 压缩零保真：硬约束被压成一句并落地 —— High

- **问题**：/compact 对摘要内容零保真校验，含用户硬约束的历史被压缩成一句（"else."）后直接落地，红线静默消失。
- **影响**：用户明示的安全/行为约束可能在压缩后永久丢失且无提示，后续回合不再遵守。
- **修复建议**：① 压缩前抽取硬约束/规则清单，摘要后单独保留并校验（不得被压缩掉）；② 压缩结果与原文做约束级 diff 并向用户展示丢了什么；③ 压缩落地前需确认（而非静默写盘）。
- **建议去向**：**org issue（P1）**。

### 1.4 #176 torn zstd 帧静默恢复：崩溃后尾部事件丢失 —— High

- **问题**：崩溃导致的 torn（截断）zstd 帧被静默恢复，尾部事件丢失且无任何诊断，日志被改写为 "interrupted"。
- **影响**：会话记录静默不完整，事后无法重建崩溃前的真实事件序列（审计/调试双重损失）。
- **修复建议**：① zstd 帧尾部完整性校验，恢复时显式告警（日志 + 用户可见）；② trajectory 分段 checkpoint，降低单帧损坏损失面；③ "interrupted" 改写需带原帧 hash 证据。
- **建议去向**：**org issue（P1）**。

### 1.5 #73 ENOSPC 未捕获：spill 写入失败致进程崩溃 —— High

- **问题**：OutputCollector spill 写入（writeSync）失败未捕获，磁盘写满（ENOSPC）时整个进程崩溃。
- **影响**：磁盘打满时不是优雅降级而是进程级可用性事故，且崩溃本身可能叠加 #176 的日志损坏。
- **修复建议**：① 捕获写失败 → 告警 + 优雅降级（如暂停接受新任务、提示清理磁盘）；② spill 路径提供背压与配额；③ 崩溃前落盘"磁盘不足"可诊断状态。
- **建议去向**：**org issue（P1）**。

### 1.6 #118 / #20 并发写会话：JSONL seq 冲突无法加载 —— High

- **问题**：WebUI 与 TUI 两个进程并发写同一会话时 JSONL seq 冲突，恢复失败（"corrupt session log: seq gap"）。
- **影响**：多进程共享 $DSH_HOME 是官方支持的部署形态（Web + CLI/TUI 并存），会话日志损坏直接丢对话历史。
- **修复建议**：① 会话级跨进程写锁（文件锁而非进程内锁）；② seq 由存储层统一分配（而非各进程本地自增）；③ 冲突时 fail loud 并保留可恢复副本。
- **建议去向**：**org issue（P1）**。

### 1.7 #7 SSE 内存泄漏：ReadableStream queue 无限堆积 —— Medium-High

- **问题**：Web 端内存持续增长至 1.4GB+：SSE 流客户端停读时 enqueue 无背压，ReadableStream queue 无限堆积。
- **影响**：长开页面（内测高频使用场景）内存无限增长，最终卡死/崩溃；与 #4（冷会话恢复全量解压 6 万 zstd 帧）叠加放大。
- **修复建议**：① enqueue 侧背压（队列上限 + 客户端停读时暂停）；② 客户端断线重连时丢弃过期事件；③ 增加队列长度监控与告警。
- **建议去向**：**org issue（P1）**。

---

## 2. 插件侧风险（依据各仓库调研摘要）

### 2.1 plugin-registry：同进程任意代码，无沙箱/无签名/无发布者身份 —— Critical

- **问题**：`enable` 即 `import(entryUrl)` 在宿主进程内执行插件 `apply(ctx)`，拿到完整 Cordis context（可注册工具/事件/服务/命令/系统提示/TUI 覆盖层）；README 自报"无签名、无发布者身份、无审核"；catalog `source` 是任意本地路径，无白名单；`installPlugin` 全目录复制（含 node_modules 与敏感文件）。
- **影响**：这是生态层的"仓库供应链"问题——恶意/被篡改插件一经 enable 等于宿主任意代码执行；多用户共享 $DSH_HOME 或目录被篡改时无任何检测。主仓库 #302/#300 是单仓库信任问题，此处是**分发通道本身无信任模型**。
- **修复建议**：① 插件签名 + 发布者身份绑定（至少 Ed25519 签名清单）；② 安装来源白名单（catalog 路径/URL 校验）；③ 可选沙箱（worker_thread / vm 隔离或子进程桥接，至少限制 fs/网络）；④ 安装时扫描并告警 node_modules 复制；⑤ contributes.skills 补齐校验（当前只校验 tools）。
- **建议去向**：**org issue（P1）**——建议与本 repo 的 plugin-formats 分析（`analysis/plugin-formats.md`）联动，作为 #171 统一入口的必答问题。

### 2.2 qqbot：凭据明文落盘 config.yaml，无 chmod 600 —— High

- **问题**：扫码绑定后 `client_secret` 明文写入 `~/.dsh/config.yaml`，无 OS keychain、无文件权限收紧（写文件未显式 chmod 600）。
- **影响**：本机任何能读该文件的进程/用户即可拿到 QQ 机器人凭据；config.yaml 还是 HMR 监听文件，被篡改面更大。
- **修复建议**：① 写入时显式 chmod 600；② 支持 OS keychain（macOS Keychain / Linux Secret Service）或加密存储；③ 配置读取时校验文件权限并告警；④ 文档明示"config.yaml 属敏感存储"。
- **建议去向**：**org issue（P1）**（草案见 `actions/org-issues.md`）。

### 2.3 tg-bot：token 明文存 settings 文件与进程环境 —— High

- **问题**：README 安全节自承"token 以明文落盘到本地 settings 文件 + 进程环境"，宿主 settings 文件无额外加密；传输侧做了 write-only（wire 不回传），但静态存储无保护。
- **影响**：与 qqbot 同类的凭据静态暴露；tg-bot 还多一条环境变量暴露面（`TG_BOT_TOKEN`）。
- **修复建议**：与 qqbot 统一走 keychain/加密抽象；settings 文件权限收紧；文档明确环境变量属敏感存储。
- **建议去向**：**org issue（P2）**——两 IM 通道可合并为一个"凭据存储"整改 issue。

### 2.4 toybox time-capsule：胶囊明文 JSON 落地 —— Medium

- **问题**：`seal` 内容以明文 JSON 存 `~/.dsh-capsules/*.json`（`message` 字段未加密）；服务器层只防"未到期经 API 读取"，不防"直接 cat 文件"。
- **影响**：用户写入敏感内容时，任何能读该目录的进程都能看；且损坏 JSON 被静默 `catch {}` 跳过（无告警）、同天毫秒级并发存在 id 碰撞窗口。
- **修复建议**：① 可选加密（AES-GCM，密钥存用户配置并 chmod 600）或至少诚实标注"明文"；② 损坏文件读到时告警而非静默跳过；③ id 加随机分量消除碰撞。
- **建议去向**：**org issue（P2）**或 toybox 自修（玩具箱内整改即可，不必上升为平台 issue）。

### 2.5 group-chat-diary：内嵌 109 名成员 PII —— High（合规）

- **问题**：单文件 HTML 内嵌快照含 109 名成员的真实微信昵称、角色定性、代表性发言原文（部分含主观评判）；private 仓库无法阻止已授权者下载外传（README 自承）。
- **影响**：这是合规级隐私暴露面；一旦外传无法撤回。另：README 写 issue 仓库为 `dsh-external/issues`，而内嵌数据实际指向已迁移的 `dsh2026/issues`，文档与数据不一致。
- **修复建议**：① 昵称化名/哈希化、代表性发言去标识化再发布；② 增加"下载即同意不外传"的可见门槛；③ 修正 README 与数据的 issue 仓库指向；④ 评估只发布聚合统计（保留现有 quality 方法学）是否足够。
- **建议去向**：**本 repo（隐私整改建议）+ org issue（P2）**——整改动作在仓库侧，但需要生态级共识（谁有权看到什么）。

---

## 3. 汇总：去向分配

| 去向 | 条目 | 理由 |
|---|---|---|
| org issue（P0） | #302（AGENTS.md）、#300（审计日志） | 信任边界击穿，需上游最高优先级修复 |
| org issue（P1） | #301、#176、#73、#118/#20、#7、plugin-registry 无沙箱、qqbot 凭据 | 数据/凭据/生态信任，应进 #147 台账前列 |
| org issue（P2） | tg-bot token、toybox time-capsule、group-chat-diary 指向/隐私、qqbot darwin、catalog ref 滞后类 | 整改类，可低优先级排队 |
| 本 repo（仅记录，不投 issue） | 主仓库红线证据汇总、插件格式安全差异、PII 整改指引 | 本 repo 是调研与证据层，红线证据已存在于官方台账 #147，不必重复投 |
| 放弃 | 无 | 12 条全部有真实修复价值，无纯噪音项 |

> 注：主仓库红线（#302/#300/#301/#176/#73/#118/#20/#7）**已存在于官方 issues 台账**（均 open、多为 P1），本 repo 不做重复投递；本 repo 的增量价值是插件侧 5 条（plugin-registry/qqbot/tg-bot/toybox/group-chat-diary）——其中 plugin-registry 无沙箱与 qqbot 凭据 chmod 两条已起草为 org issue（见 `actions/org-issues.md`）。
