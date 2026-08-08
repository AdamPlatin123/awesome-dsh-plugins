# 拟投递 dsh-external/issues 的 issue 草稿

> 日期：2026-08-05
> 用途：以下草稿面向 **dsh-external/issues** 仓库（主仓库内测反馈池）投递，每条自包含——评审者无需阅读本调研仓库即可理解背景、证据与影响。
> 脱敏声明：所有草稿不复制任何既有 issue 正文、不出现真实密钥值、不出现成员昵称；涉及具体仓库时仅给出仓库名与 commit 引用（ref 为公开可查的 git 对象，非敏感信息）。
> 快照说明：草稿引用的 HEAD/commit 均为 2026-08-05 时点状态，投递前请复核当前值。
> 优先级与标签建议：采用本组织既有的标题前缀约定（`[类别][子系统]`）与 P0/P1/P2 标注（对齐 #147 台账口径）。

---

## 草稿 1（P1）

**标题**：`[feature][plugin] 本地插件注册表加载第三方代码无沙箱/无签名/无发布者身份，enable 即同进程任意代码执行`

**标签建议**：`[feature][plugin]`、P1

**正文**：

**背景**：DSH 生态已出现本地第三方插件系统（`dsh.plugin.json` 清单协议），插件以本地目录或 tarball 安装，`enable` 后入口 `main` 被动态 import 进宿主进程执行。该通道面向内测成员分发，当前**没有任何代码信任模型**。

**现状证据**（源码事实，公开可查）：
- 插件 `enable` 即 `import(entryUrl)` 在宿主进程执行 `apply(ctx)`，可拿到完整 Cordis context：注册工具、事件、命令、系统提示、TUI 覆盖层；
- 无签名校验：安装目录被篡改（如多用户共享 home、恶意 catalog）后 enable 即执行恶意代码；
- catalog 的 `source` 字段是任意本地路径，无白名单；`installPlugin` 全目录复制（含 `node_modules` 与构建产物）；
- 仓库自报限制："无签名、无发布者身份、无审核"；`contributes.skills` 声明当前不校验（仅 tools 挂载时对账）。

**影响**：这是分发通道层面的供应链风险——一旦有人投递/投毒一个恶意插件，成员 enable 即中招，且事后无发布者身份可追溯。与主仓库既有的单仓库信任问题（如 AGENTS.md 注入、审计日志可删）叠加后，攻击面从"打开恶意仓库"扩大到"安装任意插件"。

**建议修复**：
1. 插件清单增加签名与发布者身份字段（如 Ed25519 签名 + 公钥指纹），安装/启用时校验；
2. catalog `source` 增加白名单/URL 校验，禁止任意本地路径；
3. 提供可选沙箱（worker_thread / vm 隔离或子进程桥接），至少限制 fs 与网络；
4. `contributes.skills` 补齐与 tools 同等的对账校验；
5. 文档明确信任模型：插件代码与宿主进程同权，安装前须人工审核来源。

**验收标准**：安装来源受限 + 签名校验失败即拒绝 + 文档写明信任边界。

---

## 草稿 2（P1）

**标题**：`[bug][plugin] IM 通道插件凭据明文落盘且无文件权限收紧（config.yaml / settings 文件）`

**标签建议**：`[bug][plugin]`、P1

**正文**：

**背景**：两个 IM 远程通道插件（Telegram 与 QQ 通道）都依赖长期机器人凭据（bot token / client secret）。当前凭据以明文落盘，且写入时未收紧文件权限。

**现状证据**：
- QQ 通道：扫码绑定后把凭据明文写入 `~/.dsh/config.yaml`，写文件未显式 `chmod 600`，无 OS keychain 支持；
- Telegram 通道：token 明文存于宿主 settings 文件，且可通过环境变量注入（进程环境也属敏感暴露面）；README 已自承"把本地 settings 文件与进程环境视为敏感存储"，但存储本身无加密、无权限校验；
- 两个通道的配置都是 HMR 监听文件，可被本机任何能读该文件的进程/用户读取。

**影响**：本机多用户、或被植入的任意进程，均可直接读取机器人凭据；凭据一旦泄露可冒充机器人收发消息（含授权用户上下文）。

**建议修复**：
1. 凭据写入时显式 `chmod 600`，读取时校验权限并告警；
2. 引入 OS keychain（macOS Keychain / Linux Secret Service）或加密存储抽象，两通道统一复用；
3. 文档将凭据文件与环境变量列入敏感存储清单；
4. 日志路径禁止打印凭据（含错误信息里的截断值）。

**验收标准**：凭据文件权限 600；支持 keychain 存储；日志无凭据泄露。

---

## 草稿 3（P1）

**标题**：`[bug][plugin] Telegram 通道 mux 事件流断开后不重连，用户 prompt 静默无回复`

**标签建议**：`[bug][plugin]`、P1

**正文**：

**背景**：Telegram 通道插件通过宿主 RPC 的 mux 事件流订阅会话事件（流式回复与交互问题都走这条流），同时独立跑 Bot API 长轮询接收用户消息。

**现状证据**：mux 流失败时仅记日志后返回，长轮询继续运行——此时用户发消息仍会进入 agent（prompt 被接受），但回复永远无法回传（流断了），且**无自动重连、无用户告警**。用户视角是"bot 卡死/丢失消息"。

**影响**：长轮询与 mux 流生命周期解耦导致静默单边失效；Telegram 端无任何提示，属于可用性缺陷（非数据损坏，但会造成消息永久丢失的观感）。

**建议修复**：
1. mux 流断开后自动重连（指数退避，对齐长轮询的退避策略）；
2. 断流期间收到的 prompt 拒绝或排队，并回执"通道暂不可用"；
3. 断流超过阈值时向管理员 chat 发送告警；
4. 增加 mux 流健康心跳/探活。

**验收标准**：mux 断流后自动恢复，恢复期间用户消息不静默丢失。

---

## 草稿 4（P2）

**标题**：`[bug][plugin] toybox 插件索引（README 安装块/catalog.json）发布 ref 落后于仓库 HEAD`

**标签建议**：`[bug][plugin]`、P2

**正文**：

**背景**：toybox 仓库以 `github:<org>/toybox#<40位commit>&path:` 的不可变 ref 挂载方式分发插件，README 的 `INSTALL`/`REFS` 块与 `catalog.json` 由发布脚本统一 pin 到发布时 HEAD。

**现状证据**：索引 pin 的 ref 为 `c02a31be…`，而截至 2026-08-05，仓库 HEAD 为 `7acd885…`（一次 docs 提交之后未重跑发布脚本）。按"更新插件 = 换 ref"纪律，索引与 HEAD 不同步时，下游按索引安装将拿不到最新提交。

**影响**：索引失真，用户安装到旧版本且无感知；长期会破坏"不可变 ref 即真相"的信任假设。

**建议修复**：
1. 每次合并到 main 后自动重跑发布脚本（CI 钩子），或至少将发布脚本纳入提交前门禁；
2. 增加索引与 HEAD 一致性检查（diff ref，不一致则 CI 失败）。

**验收标准**：索引 ref 与 HEAD 一致，或 CI 在失配时显式失败。

---

## 草稿 5（P2）

**标题**：`[bug][plugin] dsh-skins 皮肤索引（catalog.json / README REFS）pin 落后于仓库 HEAD`

**标签建议**：`[bug][plugin]`、P2

**正文**：

**背景**：dsh-skins 以 `dsh-skins-index/v0.2` catalog 分发皮肤，`publish.mjs` 把 catalog 与双语 README 的 `INSTALL`/`REFS` 块 pin 到发布时 commit，遵循"不可变身份 = 完整 commit ref"纪律。

**现状证据**：`catalog.json` pin 在 `083d4c7a…`（updated 时间戳 2026-08-04），而截至 2026-08-05，仓库 HEAD 为 `07238b2…`（一次测试补齐提交之后未重跑发布）。下游按 catalog 安装会拿到缺少最新测试与修复的旧皮肤。

**影响**：与草稿 4 同类的索引失真问题；皮肤是用户可见产物，旧版本差异直接体现在界面上。

**建议修复**：发布脚本纳入 CI/提交门禁；增加 catalog ref 与 HEAD 一致性检查。

**验收标准**：catalog pin 与 HEAD 一致或 CI 显式失败。

---

## 草稿 6（P2）

**标题**：`[bug][plugin] 内测群每日档案 README 与实际数据指向不同的 Issue 仓库（dsh-external/issues vs dsh2026/issues）`

**标签建议**：`[bug][plugin]`、P2

**正文**：

**背景**：内测群每日档案仓库的 README 声明 issue 数据源为 `dsh-external/issues`，但内嵌快照数据的 `issues.source.repository` 与 issue 链接实际指向 `dsh2026/issues`（旧仓库名）。

**现状证据**：README 文本与内嵌 `__DSH_SNAPSHOT__` 数据的仓库字段不一致；该 issue 仓库已迁移（组织改名 dsh2026 → dsh-external），旧 URL 虽可重定向，但新读者按 README 找不到正确仓库时会产生混淆。

**影响**：文档与数据不一致，读者可能向错误仓库提交/查找 issue；也反映生成链路（本机脚本）仍引用旧仓库名，存在未完全迁移的残余。

**建议修复**：
1. README 与生成脚本统一使用 `dsh-external/issues`；
2. 生成链路增加仓库名一致性校验（README 声明的数据源与内嵌数据比对）；
3. 存量归档可在显著位置注明"历史数据生成于迁移前"。

**验收标准**：README 与最新归档的数据源字段一致。

---

## 草稿 7（P2）

**标题**：`[bug][plugin] QQ 通道 WebSocket Identify 上报的 $os 硬编码为 darwin，与实际平台不符`

**标签建议**：`[bug][plugin]`、P2

**正文**：

**背景**：QQ 通道插件通过 WebSocket 网关连接 QQ 开放平台，握手 Identify 帧携带客户端属性（`$os` 等）。

**现状证据**：Identify 中 `$os` 字段硬编码为 `'darwin'`，与实际运行平台（Linux/Windows/macOS）无关。

**影响**：平台属性失真，可能影响 QQ 后端的风控判定与平台统计准确性；用户侧无直接可见影响，但属于可低成本修复的数据正确性问题。

**建议修复**：用 `os.platform()` / `os.version()` 等运行时信息生成 `$os`（可保留 `$os` 与附加字段），并对 Identify 帧做单元测试覆盖。

**验收标准**：Identify 帧 `$os` 反映实际平台；测试覆盖。
