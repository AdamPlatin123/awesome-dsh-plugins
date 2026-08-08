# Issue 聚类路线图（dsh-external/issues，308 条）

> ⚠️ 快照：2026-08-04 抓取（308 条），已过期，仅作历史参考

> 生成日期：2026-08-05
> 数据源：`/tmp/dsh-ext-research/issues_all.json`（GitHub Issues API 全量缓存）
> **抓取时间戳**：`2026-08-04T18:49:33Z`（UTC，即北京时间 2026-08-05 02:49；文件 mtime）
> **总数：308 条**（open 286 / closed 22，编号 1–308，创建时间跨度 2026-08-01T17:03:12Z → 2026-08-04T18:31:42Z）
> 脱敏声明：本文件仅含编号 + 标题 + 子系统，不摘录任何 issue 正文。

---

## 1. 聚类方法

- 平台 label 全缺失（308/308 unlabeled），分类依赖**标题前缀正则**：`^\[类别\](\[子系统\])* 标题`。
- 首括号标准化为类别（bug / feature / suggestion / proposal / perf / enhance / goal / fix / junk / research / showcase / agent-loop），其余括号为子系统标签；**一条 issue 可带多个子系统标签**（如 `[bug][core][persistence]`），子系统计数为展开计数。
- 仅含子系统标签（无类别）的标题单独归类为"子系统-only"桶；无任何括号前缀的标题进"未分类桶"。
- 合计校验：280（类别明确）+ 17（子系统-only）+ 11（未分类）= 308。

---

## 2. 类别统计（按标题首括号，标准化后）

| 类别 | 数量 | 占比 | 说明 |
|---|---|---|---|
| bug | 155 | 50.3% | 缺陷（含 `Bug` 大小写变体） |
| feature | 105 | 34.1% | 功能请求（含 `features`/`Feature` 变体） |
| perf | 5 | 1.6% | 性能（含 `performance` 变体） |
| enhance | 3 | 1.0% | 增强类 |
| goal | 2 | 0.6% | 目标管理类 |
| proposal | 2 | 0.6% | 协议/架构提案 |
| junk | 2 | 0.6% | 自标无效记录 |
| suggestion | 2 | 0.6% | 建议（含 `suggsetion` 拼写错误变体） |
| fix | 1 | 0.3% | 修复类 |
| research | 1 | 0.3% | 调研类 |
| showcase | 1 | 0.3% | 展示类 |
| agent-loop | 1 | 0.3% | Agent 循环类 |
| **小计** | **280** | 90.9% | |
| 子系统-only（无类别前缀） | 17 | 5.5% | 全部以 `[web]`/`[Web]` 开头，见 §5 |
| 未分类（无前缀） | 11 | 3.6% | 完整清单见 §6 |

> 注：若把顺序倒置的 `[web][bug]` 类标题（5 条）计入 bug，则 bug 口径为 160——与 `research/issues.md` 的 160 一致；feature 口径同理可到 107。本表采用"首括号=类别"严格口径。

---

## 3. 类别 × 子系统矩阵（标题派生，多标签展开计数）

| 类别 \ 子系统 | web | core | tui | cli | a11y | goal | models | tool | session | connection | i18n | history | headless | web+tui | agent | persistence | 未标注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| bug | 94 | 25 | 12 | 8 | 14 | 7 | 6 | 3 | 5 | 4 | 6 | 3 | 0 | 2 | 2 | 1 | 4 |
| feature | 41 | 17 | 18 | 7 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 3 | 2 | 2 | 0 | 3 |
| perf | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| enhance | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| goal | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| proposal | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| fix | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| junk | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| suggestion | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| agent-loop | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| showcase | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

**读数**：bug 高度集中在 web（94/155）；core 的 bug（25）占比高于 core 的 feature（17），说明核心层以修缺陷为主；a11y（14）全部来自 bug，无障碍是无独立 feature 需求的质量债。

---

## 4. 优先级 × 子系统矩阵（以 #147 P1 台账为背景）

**背景**：#147「Issue 跟踪清单（每 20 分钟自动更新）」是事实上的 backlog 单一信息源，机器人每 20 分钟重建勾选清单，按 `[编号] · 子系统 · 优先级 · 标题` 组织。抓取时台账含 **285 条**（bug 148 / fix 1 / feature 105 / enhance 3 / proposal 2 / suggestion 6 / goal 2 / other 18；另有 closed 段 22 条）。本矩阵直接采用台账的优先级与子系统标注（台账口径，与标题派生口径不同属正常）。

| 优先级 \ 子系统 | web | core | tui | cli | tool | agent | goal | web+tui | headless | skill | protocol | persistence | other | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P1** | 84 | 17 | 10 | 5 | 4 | 3 | 5 | 2 | 0 | 0 | 0 | 0 | 5 | **135** |
| **P2** | 1 | 6 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **15** |
| **P3** | 56 | 21 | 17 | 7 | 4 | 4 | 2 | 2 | 3 | 2 | 1 | 1 | 15 | **135** |
| 合计 | 141 | 44 | 32 | 15 | 8 | 7 | 7 | 4 | 3 | 2 | 1 | 1 | 20 | **285** |

**读数**：
- **P1 集中在 web（84/135，62%）**：断线重连、SSE 背压、fork/archive 交互是内测期体验主战场；
- **core 的 P1（17）按比例最重**（17/44 ≈ 39%）且全部是数据/信任级缺陷（并发写、zstd、ENOSPC、审计日志、AGENTS.md——详见 `analysis/security-issues.md`），是"数量少但风险最高"的象限；
- P2 仅 15 条（core 6 / tui 5 / cli 3 / web 1），说明台账把绝大多数问题直接定为 P1 或 P3，P2 是窄带；
- **23 条未入台账**（编号 19, 26, 77, 78, 80, 117, 147, 157, 169, 262, 263, 264, 265, 267, 269, 270, 271, 272, 273, 274, 275, 277, 280）：含台账本体 #147 与 260-280 段的最新 issue，多为台账同步之后新建，无优先级标注。

---

## 5. 子系统-only 桶（17 条，无类别前缀、以 [web]/[Web] 开头）

| 编号 | 子系统标签 | 标题（截断至 60 字） |
|---|---|---|
| 1 | web | 屏幕熄屏(ERR_NETWORK_IO_SUSPENDED)断线后提问丢失，聊天区永久卡 "Deep diving..." |
| 2 | web+bug | agent 回复过程中 fork 按钮点击无反应，回复结束后正常 |
| 3 | web | 新对话的存储问题与显示问题 |
| 11 | web | 工作区中 subagent 会话缺少归属标记，堆叠在"未分组"分类 |
| 13 | web+bug | Windows 下工作目录选择器无法正常显示 |
| 16 | web | MacOS 下 Web 端输入框出现滚动条后输入逻辑和渲染错位 |
| 38 | web | 通过 HTTP IP 地址访问时，Add workspace 报 crypto.randomUUID is… |
| 76 | web+bug | SQLite 持久化时 session 列表按创建时间排列，未按最新修改时间排序 |
| 79 | web+suggestion | 交互设计建议汇总：会话消息操作与 Agent 运行观察、干预、工作区浏览 |
| 81 | web+gui | Subagent 相关信息展示不明确，loading 效果需要优化 |
| 83 | web+suggestion | 前端的部分建议 |
| 84 | web+feature | Web 版本较长用户Query，没有自动折叠机制 |
| 86 | web+bug | MacOS 下直接按下 Command+Enter 会使得消息直接发送而不会进入 queue |
| 96 | web+bug | 子Agent的会话，会进入未分组会话中作为独立会话存在 |
| 103 | web+suggestion | dsh web 启动体验：多实例共存时的会话安全（关联 #20）、启动后自动打开浏览器 |
| 114 | web+suggestion | 全局"新会话"应优先沿用当前会话的工作区，而非最近更新的工作区 |
| 214 | web+feature+suggestion | 侧边栏"新建会话"入口需 hover 才显示：新建会话比新建项目更常用 |

> 注：此桶 17 条全部为 web 相关；其中 5 条是顺序倒置的 `[web][bug]`/`[Web][Bug]`（#2/#13/#76/#86/#96），归类时应并入 bug×web。

---

## 6. 未分类桶（11 条，标题无任何括号前缀）

| 编号 | 标题 |
|---|---|
| 12 | 当前思考过程与Tool call 过程会比较占篇幅，会削弱整体有效信息的可见性 |
| 14 | Windows 下无sandbox后端，正常启动会报SandboxUnavailableError |
| 30 | 新增功能:@deepseek-ai/dsh-advisor — hook 触发的进程监督插件 |
| 108 | Web UI 在 Windows 上选择工作区目录的三个问题 |
| 147 | 📋 Issue 跟踪清单(每 20 分钟自动更新) |
| 160 | 📋 历史 PR 与 Issue 完整记录 |
| 202 | Feature Request: Add a Codex-like Steer Mode for Real-Time Task Correction |
| 281 | HMR 插件热重载在 Node 24 下不生效（tsx registerHooks 绕过 cascaded loadCache） |
| 283 | 新增 working-activity 插件：WebUI/TUI 实时显示模型工作状态 |
| 286 | 后端断开连接后Tool工具状态不刷新 |
| 288 | MacOS WebUI 侧边栏与subagent显示问题 |

> 内容倾向：多为 Windows 相关（#14/#108）、机器人维护（#147/#160）、插件相关（#30/#281/#283）；建议维护者回填前缀（如 #14 → `[bug][core]`、#281 → `[bug][core]`），保证台账正则不漏统。

---

## 7. Top 20 候选清单（P1 + core 优先排序）

排序规则：#147 台账内 P1 全部 135 条，按子系统权重（core > persistence/protocol > web+tui > web > tui > tool > agent > cli > goal > headless > skill > other）再按编号升序取前 20——core 段即主仓库数据/信任红线全集，Web 段仅取到首位 #1。编号列后为标题派生子系统。

| # | 编号 | 子系统 | 标题 |
|---|---|---|---|
| 1 | 20 | core | 会话日志被两个并发进程交错写入，seq 冲突导致恢复失败（corrupt session log: seq gap） |
| 2 | 46 | core | dsh 启动崩溃: HMR 服务需要 --expose-internals 但 launcher 脚本未包含该标志 |
| 3 | 73 | core | OutputCollector spill 写入失败(writeSync)未捕获，ENOSPC 时整个进程崩溃 |
| 4 | 74 | core | installFailLoud 对顶层 await 拒绝无效：启动错误输出完整 Node 堆栈（含内部路径） |
| 5 | 93 | core | 长 session resume 后 TUI 输入明显卡顿，660MB 内存/44% CPU 持续高占用 |
| 6 | 106 | core+sandbox | 临时插件卸载后 httpServer 资源未清理（route/tapIndex 残留） |
| 7 | 118 | core+persistence | WebUI 与 TUI 两个进程并发写入同一会话，JSONL 日志 seq 冲突后无法加载 |
| 8 | 176 | core | torn zstd 帧静默恢复:崩溃后尾部事件丢失无任何诊断,日志被改写为"interrupted" |
| 9 | 177 | core | /model 会话级选择不生效于子代理与新会话,默认路由静默回落 deepseek-v4-pro |
| 10 | 192 | core | max-tokens 截断时保留 tool-call 并回喂失败结果(修复静默丢写)(设计建议) |
| 11 | 205 | core | LLM API 重试率过高，用户无感知且浪费 Token |
| 12 | 206 | core | Turn 未正常结束：turn/start 与 turn/end 数量不匹配 |
| 13 | 231 | core | bwrap 沙箱边界可被 /proc/1/root 写入绕过:read-only/workspace-write 下 bash 可无审批写宿主任意文件 |
| 14 | 232 | core | DSH_HOME 位于工作区内时 agent 可免审批覆写 config.yaml 且 !!js 表达式在 harness 进程内 eval(任意代码执行) |
| 15 | 300 | core | Agent 可删除自身会话审计日志:workspace 模式下无沙箱防护、无篡改检测、exit 0 无诊断 |
| 16 | 301 | core | 压缩对摘要内容零保真校验:/compact 将含用户硬约束历史压成 else. 并落地,红线静默消失 |
| 17 | 302 | core | AGENTS.md 无信任门槛自动升级为 system-reminder:注入封套与真实提醒逐字节相同,无同意环节 |
| 18 | 21 | web+tui | 点击"停止生成"后排队消息丢失，不回到输入框 |
| 19 | 22 | web+tui | 子代理 API 失败在侧边栏与 /resume 堆积"会话中断"死会话 |
| 20 | 1 | web | 屏幕熄屏(ERR_NETWORK_IO_SUSPENDED)断线后提问丢失，聊天区永久卡 "Deep diving..." |

> 说明：web P1 段共 84 条，本清单只收录首位 #1；其余高热度 web P1（如 #7 SSE 内存泄漏、#4 冷会话恢复卡顿）在后续 21+ 位，建议按 §4 矩阵的 web 列继续取。安全/审计红线（#300/#301/#302/#231/#232/#176/#73/#20/#118）已在清单 1-17 位全覆盖。

---

## 8. 附录：方法学限制

1. **标题解析误差**：分类完全依赖标题正则，大小写变体（`Bug`/`Web`）、拼写错误（`suggsetion`）、顺序倒置（`[web][bug]`）均做了标准化归并；仍可能有非常规写法未被覆盖（如 #214 三标签）。
2. **台账口径差异**：§4 采用 #147 台账的子系统与优先级（285 条），§3 采用标题派生口径（308 条），两表不可直接相加；23 条未入台账的最新 issue 无优先级信息。
3. **时效**：台账每 20 分钟自动刷新，本表为抓取时刻快照；引用时以 #147 最新内容为准。
