# dsh-external 生态超级调研

## 项目定位

本仓库是对 **dsh-external 组织**（DeepSeek Harness 内测期私有组织）下 **15 个仓库**的聚合调研产出。调研以 orchestrate 方式并行推进：15 个 scout 子代理各负责一个仓库的只读深挖，同时引入旧 session（`019fc8ab`）在 deepseek-harness 快照上的磁盘 I/O / 版本差异 / 群聊对齐上下文，最终在 `cross-analysis/` 汇成交叉分析与生态全景报告。

**核心结论一句话**：0804 官方快照之后，dsh-external 组织出现一轮"生态圈地潮"——11 个仓库承载了插件协议（两代格式并存）、IM 远程通道、Web UI 扩展与工具链资产，另有 4 个仓库（sandbox-mxc、dsh-opencode-server、ex-setting、dsh-coding-receipt）仍为空占位；所有已落地仓库几乎全部依赖"复制 + git apply 锚定 0804 快照补丁"的集成模式，这是当前最大的系统性运维债务。

## 快速导航

- **聚合报告**：`cross-analysis/summary.md` —— 生态全景分类、插件格式演进、补丁集成模式、扩展点利用全景、tg-bot/qqbot 远程通道对比、风险热区（主仓库红线 + 插件共性风险 + 安全面）、维护状态矩阵、8 条洞察建议，附证据索引/术语表/不一致清单三个附录。
- **逐仓库摘要**：`research/*.md` —— 15 份统一契约摘要，每份含定位/技术栈/文件结构/核心功能（带文件与行号）/集成点/亮点与风险/维护状态。
- **旧 session 上下文**：`context/session-019fc8ab-summary.md` —— 磁盘 I/O 四类热点、版本差异、TUI 移除、插件格式演进时间线。
- **变更记录**：[CHANGELOG.md](CHANGELOG.md) —— mainline 版本差异与兼容状态更新日志。
- **最新报告**：[reports/latest/](reports/latest/) —— 各日 mainline 兼容性报告（软链指向最新一日，当前为 2026-08-05）。
- **基线说明**：[reports/2026-08-04/](reports/2026-08-04/) —— 0803→0804 版本差异基线，0805 报告的变更分析以此为基础。
- **重点先读**：`research/issues.md`（主仓库红线与内测反馈密度）、`research/plugin-registry.md`（下一代插件协议）、`research/qqbot.md` 与 `research/tg-bot.md`（远程通道对比）。

## 目录结构

```
/mnt/shared/_Projects/dsh-external-research/
├── README.md                  # 本文件：项目说明与关键结论
├── research/                  # 15 个仓库的独立调研摘要（.md，只读，scout 产出）
│   ├── issues.md              #   dsh-external/issues（Issue Tracker 承载仓库，308 issue）
│   ├── toybox.md              #   整活插件玩具箱（.dsh-plugin 静态格式，8 插件）
│   ├── plugin-registry.md     #   dsh.plugin.json 第三方插件系统（协议层）
│   ├── tg-bot.md              #   Telegram 远程通道（长轮询 + ApiProxy）
│   ├── qqbot.md               #   QQ Bot API v2 远程通道（WS 网关，零依赖）
│   ├── web-components.md      #   原生 Custom Elements 渲染臂（补丁集成）
│   ├── dsh-skins.md           #   Web GUI 换肤（ThemeService，零核心改动）
│   ├── dsh-subagent-tree.md   #   侧栏子代理树（对应 issues#44）
│   ├── dsh-live-stats.md      #   实时 token/TPS 统计（projection seam）
│   ├── dsh-working-activity.md#   模型工作状态行（TUI + Web 双出口）
│   ├── group-chat-diary.md    #   内测群每日归档 HTML（工具链/档案）
│   ├── sandbox-mxc.md         #   占位：微软跨平台沙盒支持
│   ├── dsh-opencode-server.md #   占位：用 opencode 替换 TUI
│   ├── ex-setting.md          #   占位：DSH 设置扩展
│   └── dsh-coding-receipt.md  #   占位：session log → coding receipt
├── context/                   # 旧 session 调研上下文归档（只读）
│   └── session-019fc8ab-summary.md   # 磁盘 I/O 四类热点 / 版本差异 / 插件格式演进 / TUI 移除
├── cross-analysis/            # 聚合产出
│   └── summary.md             # 生态全景 + 主题聚类 + 风险热区 + 维护矩阵 + 洞察建议
├── reports/                   # mainline 兼容性报告（按日归档；latest -> 最新一日）
│   ├── 2026-08-04/            # 0803→0804 基线说明（0805 变更分析的基础）
│   ├── 2026-08-05/            # 0805 当日报告（mainline-compat.md + 逐仓库 + 索引）
│   └── latest -> 2026-08-05   # 最新报告软链
└── plan/                      # 调研计划/过程产物（当前为空）
```

## 调研方法

- **并行 scout**：一次性派发 15 个只读 scout 子代理，每个负责一个仓库，覆盖 `git clone --depth 1`、`gh api` 元数据、源码/测试/README 静态分析。
- **统一摘要契约**：每个 scout 按固定模板输出——一句话定位 / 技术栈 / 文件结构 / 核心功能（附关键文件与行号）/ 集成点 / 亮点与风险 / 维护状态 / 备注，保证 15 份摘要可横向比对。
- **只读纪律**：调研期间不修改被调研仓库的任何文件；本仓库仅新增 `cross-analysis/summary.md` 与 `README.md` 两个文件。
- **上下文衔接**：将旧 session（019fc8ab）对 deepseek-harness 快照的调研结论（磁盘 I/O 四类热点、TUI 移除、issue 仓库迁移 dsh2026→dsh-external、`.dsh-plugin` 格式现状）作为解读插件仓库的背景基线。
- **证据规范**：聚合报告的每个论断都标注来源摘要文件，可直接抽查；摘要间的文档不一致（如 toybox 色数、group-chat-diary 的 issue 仓库指向、catalog ref 滞后）在聚合报告中并列呈现并给出处理建议。
- **时效声明**：基准日 2026-08-05；多数仓库以浅克隆调研，只能观察最近一次提交，"活跃度"结论以可见证据为准。

## 研究约束

- 被调研仓库全部为私有（dsh-external 组织，内测白名单可见），本仓库内容不得外传。
- 依赖未发布 `@deepseek-ai/dsh-*` workspace 包的仓库无法在隔离环境构建验证，相关分析基于源码与测试静态审查。
- 4 个占位仓库（sandbox-mxc、dsh-opencode-server、ex-setting、dsh-coding-receipt）的功能预期均为命名/描述推断，首次 commit 出现前不应作为事实引用。

## 关键结论

1. **插件格式两代并存**：主仓库快照只支持 `.dsh-plugin/package.json` 静态格式（toybox 采用）；plugin-registry 的 `dsh.plugin.json`（id/engines.dsh/contributes 声明即契约 + 安装/启停/校验生命周期）是社区先行实现的下一代协议。issues#171「插件系统暴露标准入口」是 308 个 issue 中评论最多的一条。
2. **补丁集成模式是最大债务**：web-components、plugin-registry、working-activity、tg-bot 四份补丁全部锚定 0804 快照（skins 以 inline 预设 + link 兄弟快照规避），主仓库基线一漂即批量失效；已落地仓库大多为 08-04~08-05 单次提交首发，无迭代历史。
3. **远程通道能力分叉**：tg-bot（长轮询 + ApiProxy 复用 + ask-user-question 内联键盘）交互完备但需 host patch；qqbot（WS 网关 + 零依赖 + 免补丁 HMR 热重载 + 扫码绑定）接入优雅但无内联键盘；两者共享同一套 DSH 会话/持久化 seam，可叠加部署。
4. **安全风险集中在三处**：主仓库侧 #302（AGENTS.md 注入）/ #300（审计日志可删）/ #301（压缩丢硬约束）为信任边界级红线；插件侧 qqbot 凭据明文落盘无 chmod、toybox time-capsule 明文存储；group-chat-diary 内嵌 109 名成员 PII 且数据仍指向已迁移的 dsh2026/issues。
5. **四个占位仓库不计入能力**：sandbox-mxc、dsh-opencode-server（与 TUI 移除直接相关，值得跟踪首 commit）、ex-setting、dsh-coding-receipt 均 0 commit、创建与 push 间隔 1-2 秒，属"先建仓占名"。

## 产出文件清单

| 路径（绝对） | 说明 |
|---|---|
| `/mnt/shared/_Projects/dsh-external-research/cross-analysis/summary.md` | 聚合报告（生态全景/主题聚类/风险热区/矩阵/洞察 + 附录） |
| `/mnt/shared/_Projects/dsh-external-research/README.md` | 本文件 |
| `/mnt/shared/_Projects/dsh-external-research/research/*.md` | 15 份 scout 摘要（只读，调研输入） |
| `/mnt/shared/_Projects/dsh-external-research/context/session-019fc8ab-summary.md` | 旧 session 上下文归档（只读） |
| `/mnt/shared/_Projects/dsh-external-research/plan/` | 调研计划/过程产物（当前为空） |
| `/mnt/shared/_Projects/dsh-external-research/reports/2026-08-04/README.md` | 0803→0804 基线说明（0805 报告的变更分析基础） |
| `/mnt/shared/_Projects/dsh-external-research/reports/2026-08-05/` | 0805 当日 mainline 兼容性报告（mainline-compat.md + 逐仓库 + 索引） |

## 免责声明

本仓库内容来自**私有仓库调研**，所有被调研仓库均属 `dsh-external` 组织私有资产，仅供内部使用；请勿公开分发、外传或用于任何未经许可的用途。
