# dsh-external 生态情报 · 自动监控

> 面向 DSH 插件开发者的组织级情报门户：每 8 小时自动索引 dsh-external 全部仓库，对比当日 mainline 接口差异，产出兼容性矩阵、新增/修改跟踪与双方开发者建议。

<!-- AUTO:ecosystem:START -->
> 自动更新：2026-08-09_0239（cron 每 8 小时 · 报告日 2026-08-08 · mainline `0882344`）

**生态仪表盘**

| 指标 | 值 |
|---|---|
| 仓库总数 | 134 |
| ✅ 无需适配 | 123 |
| ⚠️ 需适配 | 10 |
| 关注 / 占位 / 不适用 / 已删除 | 3 / 8 / 2 / 1 |
| 🐙 开放 PR | 2 |

📄 **最新报告**：[mainline-compat.md](reports/2026-08-08/mainline-compat.md) · [当日索引](reports/2026-08-08/index.md)（完整矩阵 + 双方建议）

**今日新增 / 修改仓库**

| 仓库 | 类型 |
|---|---|
| dsh-web-ui-notify | 🆕 新增 |
| dsh-evolve | 🆕 新增 |
| dsh-island | 🆕 新增 |
| dsh-drag-and-drop | 🆕 新增 |
| dsh-message-edit | 🆕 新增 |
| dsh-deep-research | 🆕 新增 |
| dsh-multimedia-webui-input | 🆕 新增 |
| repo-visibility-guard | 🆕 新增 |
| dsh-grok-tui | 🆕 新增 |
| ds_web_craw | 🆕 新增 |
| fabric | 🆕 新增 |
| dsh-browser | 🆕 新增 |
| dsh-desktop-mac | 🆕 新增 |
| dsh-public-repo-monitor | 🆕 新增 |
| dsh-tui | 🆕 新增 |
| dsh-inspect | 🆕 新增 |
| dsh-cc-tui | ✏️ 修改 |
| dsh-memory-evolve | ✏️ 修改 |
| dsh-session-search | ✏️ 修改 |
| dsh-sfw | ✏️ 修改 |
| dsh-skins | ✏️ 修改 |
| dsh-ui-progress | ✏️ 修改 |
| dsh-ui-whale | ✏️ 修改 |
| dsh-win-port | ✏️ 修改 |
| hub | ✏️ 修改 |
| dsh-hub | ✏️ 修改 |
| dsh-a2a | ✏️ 修改 |
| dsh-feishu-notify | ✏️ 修改 |
| dsh-web-workflow-visualizer | ✏️ 修改 |
| dsh-checkpoint | ✏️ 修改 |
| dsh-rewind | ✏️ 修改 |
| official-plugins-port | ✏️ 修改 |
| oh-my-dsh | ✏️ 修改 |
| dsh-profile-bundle-example | ✏️ 修改 |
| dsh-plan-execute | ✏️ 修改 |
| dsh-paste-input | ✏️ 修改 |
| zotero-harvest | ✏️ 修改 |
| dsh-bash-encoding | ✏️ 修改 |
| dsh-skill-stats | ✏️ 修改 |
| dsh-web-archive | ✏️ 修改 |
**需适配（补丁基线 / seam 变化）**

| 仓库 | 锚定 | 判定 |
|---|---|---|
| dsh-my-rsi | 未知（不同谱系） | 需适配 |
| dsh-subagent-tree | 未知 | 需适配 |
| dsh-working-activity | 未知（非 commit 锚定: 20260804T143803Z） | 需适配 |
| ex-setting | 未知（不同谱系） | 需适配 |
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | 需适配 |
| Qwen-MM-Plugins | 未知（不同谱系） | 需适配 |
| sandbox-mxc | 未知（不同谱系） | 需适配 |
| turtle-ui | 未知（不同谱系） | 需适配 |
| web-components | 未知（不同谱系） | 需适配 |
| fabric | 未知（不同谱系） | 需适配 |
**正在跟踪的 open PR**

| 仓库 | PR | 标题 | 更新 |
|---|---|---|---|
| [group-chat-diary](https://github.com/dsh-external/group-chat-diary) | [#4](https://github.com/dsh-external/group-chat-diary/pull/4) | Automate Cloudflare Pages deployment | 2026-08-07 |
| [dsh-live-stats](https://github.com/dsh-external/dsh-live-stats) | [#1](https://github.com/dsh-external/dsh-live-stats/pull/1) | fix: make live token and TPS accounting provider-aligned | 2026-08-07 |
<!-- AUTO:ecosystem:END -->

## 项目说明

<details>
<summary>📖 项目定位与核心结论（点击展开）</summary>

本仓库是对 **dsh-external 组织**（DeepSeek Harness 内测期私有组织）下全部仓库（截至 2026-08-08 共 134 个，动态发现）的聚合调研与持续监控产出。调研以 orchestrate 方式并行推进（15 + 41 + 7 轮 scout 子代理），结合旧 session（`019fc8ab`）在 deepseek-harness 快照上的磁盘 I/O / 版本差异 / 群聊对齐上下文。

**核心结论**：0804 官方快照之后，dsh-external 组织出现"生态圈地潮"——插件管理器（marisa/dshx）、目录元仓库（hub）、IM 远程通道（tg/qq/飞书/企微/微信/Telegram 六通道）、桌面分发（dsh-desktop / deepseek-harness-desktop 双轨）、Windows 移植（dsh-win-port）、工具插件与 Web UI 扩展持续涌入；插件格式从 `.dsh-plugin` 演进到 `dsh.plugin.json`（marisa v0.4），"复制 + git apply 锚定快照补丁"仍是主要集成债务。

</details>

<details>
<summary>🧭 快速导航（点击展开）</summary>

- **聚合报告**：`cross-analysis/summary.md`（生态全景/风险热区/洞察）
- **群聊启示**：`analysis/group-chat-plugin-dev-insights.md`（对插件开发者的参考意义）
- **插件格式**：`analysis/plugin-formats.md`（两代协议对照）
- **安全清单**：`analysis/security-issues.md`（红线与整改）
- **逐仓库摘要**：`research/*.md`（63 份，另 71 仓未深调，兼容性以每日报告为准）
- **变更记录**：[CHANGELOG.md](CHANGELOG.md)
- **最新报告**：[reports/ 目录](https://github.com/dsh-external/dsh-external-research/tree/main/reports)（按日归档；自动节顶部有当日直达链接；`reports/latest` 为软链，网页显示目标名、本地克隆可 cd）
- **Issue 路线图**：`actions/issue-roadmap.md`、`actions/org-issues.md`（issue 草稿）
- **旧 session 上下文**：`context/session-019fc8ab-summary.md`

</details>

<details>
<summary>🤖 自动运行机制（点击展开）</summary>

- 部署于远程主机 **10.144.144.9**，cron 每日三班：**02:00（--full 全量）** / 10:00 / 18:00（增量）。02:00 全量班抓取凌晨 2 点前发布的 mainline 新快照并索引全部仓库；10:00/18:00 只索引有变化的仓库。
  1. 动态发现 org 新仓库（gh api，与 `research/*.md` 摘要清单求差集）
  2. 检测 mainline + 全部仓库 HEAD 变化（`.cron-state.json`）
  3. 有变化 → `scripts/compare-mainline.sh` 索引（补丁 apply / seam / peerDeps / 锚定四维对比）
  4. 更新 `reports/<日期>/`、`CHANGELOG.md`、`reports/latest` 软链、本 README 仪表盘
  5. 以 `dsh-ecosystem-bot` 提交并推送回 org 仓库
- 数据源：`.last-changes.json` 记录每轮新增/修改仓库，驱动仪表盘
- 已删除/迁移仓库自动标记跳过（session-persistence-rdb 实例）；离线显式报错不误报
- 手动触发：`bash -lc 'cd /home/adam/dsh-external-research && ./scripts/cron-check.sh'`

</details>

<details>
<summary>📄 研究方法与约束（点击展开）</summary>

- **并行 scout**：每仓库一个只读子代理，统一摘要契约（定位/技术栈/结构/核心功能/集成点/亮点风险/维护状态）
- **只读纪律**：不修改被调研仓库；**内容 private**，仅供 org 内部
- **脱敏**：新文档不复制 issue 正文、真实密钥值、成员邮箱
- **时效**：摘要基准日 2026-08-05（静态资产基准日，最新数据见 reports/ 每日报告）

</details>

<details>
<summary>⚠️ 免责声明（点击展开）</summary>

本仓库内容来自**私有仓库调研**，所有被调研仓库均属 `dsh-external` 组织私有资产，仅供内部使用；请勿公开分发、外传或用于任何未经许可的用途。

</details>
