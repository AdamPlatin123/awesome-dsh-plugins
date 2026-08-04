# issues 调研摘要

## 一句话定位
DeepSeek Harness（DSH）内测期的**官方问题反馈仓库**——本身不含任何代码，仅承载一个 README 与 308 个 issue，作为整个 DSH 产品（harness 核心 + WebUI + TUI + 插件生态）内测期间的用户反馈池与缺陷台账。

## 技术栈与依赖（语言、框架、关键依赖）
- 仓库本身**无代码、无依赖**：仅 `README.md` 一个文件（547 字节，UTF-8 中文），加上 `.git` 历史。
- 仓库形式上不是 npm/Python 项目，而是 **GitHub Issue Tracker 承载仓库**（pure tracker repo）。
- 上游被反馈的产品（DSH）技术线索（从 issue 标题与正文反推）：
  - 运行时：Node.js（出现 `--expose-internals`、`process.execve`、顶层 await、HMR、ReadableStream、`crypto.randomUUID`）
  - 持久化：JSONL trajectory 事件流 + zstd 压缩帧 + SQLite（会话列表）
  - 通信：SSE 流（`api/events.mux`、`api/events.host`）
  - 架构：Cordis 插件底座（"一切皆插件，含 agent-loop"），`ctx.tools / ctx.llm / ctx.skills / ctx.web / ctx.subagents` 扩展点
  - 前端：自研 WebUI（含 Trajectory 检查器、ui-primitives、Modal/HoverCard/Tooltip 等组件）
  - 终端：TUI（带 `/new`、`/resume`、`/model`、`/compact` 等命令）
  - 文件附件约定：`.jsonl` trajectory（可压缩为 `.zip` 上传）

## 文件结构概览
```
issues/
├── .git/                  # depth=1 克隆，仅 3 个对象
└── README.md              # 547 字节，说明 Issue 提交规范
```
- default_branch：`main`
- 实际"内容"全部在 Issue Tracker 中，共 **308 个 issue / 0 个 PR / 0 条 label**。

## 核心功能与实现要点
仓库本身没有功能实现，只有反馈流程。README 规定的 issue 提交契约（`README.md:1-17`）：
1. **反馈引导**：README 第 1-3 行说明用途（"提交 Issue，帮助我们发现并改进问题"）。
2. **必须信息清单**：要求提供问题现象/复现步骤、预期与实际行为、完整 `.jsonl` trajectory、截图或录屏、版本与 OS（`README.md:7-12`）。
3. **大附件处理**：`.jsonl` 无法直传时压缩为 `.zip`（`README.md:14`）。
4. **安全红线**：要求上传前清除 API Key、访问令牌、个人信息（`README.md:16`）——这是 issue tracker 类仓库的关键合规要求。
5. **自动化工单台账**：Issue #147「Issue 跟踪清单（每 20 分钟自动更新）」由机器人维护一份 P1 优先级勾选清单，是事实上的 backlog 单一信息源（见 #147 issue body）。

## 与 DeepSeek Harness 主仓库的集成点
- **无代码层集成**：本仓库不是插件、不是技能、不挂载到 harness。
- **流程层集成（强）**：本仓库就是 DSH 内测的反馈漏斗。所有 issue 的标题前缀（`[bug][web]`、`[feature][core]`、`[proposal][plugin]` 等）直接对应 DSH 主仓库的子系统——`core / web / tui / tool / plugin / protocol / persistence / headless / subagent / session / memory / goal / a11y / models / connection / history / lifecycle`，与 DSH 主仓库的目录/扩展点结构一一映射。
- **追踪机制**：通过 #147 自动清单 + `P1` 标记 + 子系统代号（如 `core`、`web`、`tui`）建立与主仓库修复分支的隐性引用关系（无 GitHub label，仅靠标题约定）。

## 亮点与风险

### 亮点
1. **反馈密度极高**：4 天 308 个 issue（8/01→8/04 单调爬升：10→31→105→162），说明内测社区活跃，且反馈质量普遍较高——大量 issue 含复现步骤、控制台日志、截图与 `.jsonl` 附件。
2. **统一的标题前缀约定**：尽管平台 label 缺失，社区自发形成 `[类别][子系统] 标题` 范式（bug 160 / feature 106 / suggestion 5 / proposal 2 / perf 5），可机器解析、可统计，事实上承担了 label 的角色。
3. **自动化 P1 台账**：#147 每 20 分钟自动重建勾选清单，把跨子系统的最高优先级缺陷收敛到单一视图，是一种低成本高效的 backlog 治理模式。
4. **明确的安全提示**：README 显式要求清除密钥/令牌/个人信息，issue 提交规范到位。

### 风险
1. **平台 label 完全缺失**（308/308 unlabeled）——所有分类依赖标题正则，任何标题书写偏差都会导致漏统。建议主仓库维护者补一套 `bug/feature/web/core/tui/...` label 并回填。证据：`gh api .../issues` 返回所有 issue `labels: []`。
2. **大量"静默失败"类缺陷，涉及安全/审计红线**：
   - #300 `[bug][core]` Agent 可删除自身会话审计日志（无沙箱、无篡改检测、exit 0 无诊断）。
   - #302 `[bug][core]` AGENTS.md 无信任门槛自动升级为 system-reminder（注入封套与真实提醒逐字节相同，无同意环节）。
   - #301 `[bug][core]` /compact 压缩对摘要零保真校验，含用户硬约束的历史被压成 "else."，红线静默消失。
   - #176 `[bug][core]` torn zstd 帧静默恢复，尾部事件丢失且日志被改写为 "interrupted"。
   - #73 `[bug][core]` OutputCollector spill 写入失败（writeSync）未捕获，ENOSPC 时整个进程崩溃。
3. **并发/持久化数据完整性缺陷**：
   - #118 / #20 `[bug][core][persistence]` WebUI 与 TUI 两个进程并发写同一会话，JSONL seq 冲突后无法加载（corrupt session log: seq gap）。
   - #88 `[bug]` 被中断回合的流晚写导致 compact 卡死，会话在 1M 上下文处死锁。
4. **流式/UI 资源泄漏**：
   - #7 `[bug]` Web 内存持续增长至 1.4GB+，SSE ReadableStream queue 无限堆积（客户端停读 + enqueue 无背压）。
   - #106 `[bug][core][sandbox]` 临时插件卸载后 httpServer 资源未清理（route/tapIndex 残留）。
5. **子代理（subagent）可见性与生命周期是高频痛点**：#11、#44、#85、#96、#99、#307 集中反映 subagent 调度串行化（#99：9 个并行调用实际逐个串行）、子会话归类错乱（#11/#96 进入"未分组"）、父子 turn 感知断裂（#85：后台子代理完成时父代理无感知，导致主 agent 提前结束 turn）。
6. **关闭节奏异常**：22 个 closed issue 中有相当一批在 `2026-08-04T14:48:02Z~14:48:54Z` 这一分钟内被批量关闭（间隔 1-2 秒），疑为脚本/机器人批量处理，需确认是否真的验证修复而非"清账"。
7. **README 未给出 label 规范链接**：虽要求 trajectory 文件，但未给出敏感信息脱敏示例、未给出最小可复现模板（MRE），后续 issue 体积可能继续膨胀。

## 维护状态
- **default_branch**：`main`
- **创建时间**：2026-08-01 16:24:31 UTC
- **最近 push**（代码层）：2026-08-01 16:45:15 UTC（仓库本身创建当天一次性提交 README 后再无代码 push）
- **最近 updated_at**（含 issue 活动）：2026-08-04 18:32:45 UTC
- **提交活跃度**：仓库 git 历史几乎为空（depth=1 仅 3 个对象，单次提交），所有"活跃度"集中在 issue tracker；issue 创建速率 4 天内 10→31→105→162 加速增长，呈典型内测放量曲线。
- **issue 闭环**：308 中 286 open / 22 closed（close rate ≈ 7.1%），大量 P1 仍 open（见 #147 清单）。
- **PR 数量**：0（纯反馈仓库，不接收代码贡献）。
- **README 质量**：简短但目标清晰（547 字节，14 行有效内容），覆盖提交规范、附件格式、安全提示；缺少 label 体系说明与最小复现模板。
- **star/fork**：8 stars / 0 forks（私有仓库，内测白名单可见）。
- **license**：无。
- **topics**：无。

## 备注
- **Top 反馈者**（issue 数）：`yang478` 64、`hewzhew` 27、`cyq1017` 23、`inschrift-spruch-raum` 16、`vlln` 15、`FlytoMAYDAY80` 14——头部 6 人贡献约 51% 的 issue，反馈来源相对集中，建议主仓库维护者优先与这批用户建立直接沟通通道。
- **评论总量**：102 条，平均 0.33 条/issue；最热 #171「插件系统暴露标准入口」（7 评论）说明**插件分发/贡献协议**是社区最关注的架构级议题（涉及 cordis 底座、`ctx.tools/llm/skills/web/subagents` 扩展点统一入口）。
- **主题聚类（按 issue 标题前缀，已去重归类）**：
  - **WebUI（158，~51%）**：断线/重连、SSE 背压、Modal/HoverCard/Tooltip 无障碍、i18n、会话 lineage、fork 按钮、Trajectory 启动卡顿。
  - **Core（44）**：会话日志并发写、zstd 帧损坏、压缩保真、AGENTS.md 信任门槛、审计日志完整性、权限规则（#181）。
  - **TUI（30）**：信号处理（#303 缺 SIGTERM/SIGINT）、`/resume` 在 Windows 崩溃（#113）、ask_user_question 内容裁剪（#75）、运行时输入卡顿（#156）。
  - **A11y（14）**：WAI-ARIA Dialog、SVG accessible name、aria-live、键盘聚焦、屏幕阅读器——WebUI 无障碍是一条独立主线。
  - **Goal（9）**：stale goal ref、blocked 状态无 resume 入口、agent 无法自关闭 goal。
  - **Models/Connection/Session/History/Persistence/Subagent/Headless/Plugin/Protocol**：合计约 25，分布在跨进程并发、模型路由、长会话恢复等横切问题。
- **使用本仓库时的建议**：聚合报告若需要"DSH 内测期最受关注的 10 个缺陷/特性"，可直接以 #147 自动清单为主键，按 `P1 + core/web/tui` 分组取头部 issue；该清单每 20 分钟自动刷新，是当前最权威的优先级源。
