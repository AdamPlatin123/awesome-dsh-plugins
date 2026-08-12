# 🔭 DSH Plugin Radar

> **你的插件还兼容最新 dsh 吗？** 每天自动扫描 org 全部插件仓库与 mainline 的接口漂移，编译验证、补丁检测、seam 追踪，公测前最有价值的兼容性检查站。

[![repos](https://img.shields.io/badge/扫描插件-180+-blue)]() [![compat](https://img.shields.io/badge/兼容验证-编译级-green)]() [![mainline](https://img.shields.io/badge/mainline-每日快照-orange)]() [![cron](https://img.shields.io/badge/自动-每日%2002:00-purple)]()

## 为什么关注这里

dsh 每天都有新快照，mainline 接口持续漂移——你的插件今天兼容，明天可能就编译不过。**DSH Plugin Radar 每天自动跑一遍**：

| 能力 | 说明 |
|---|---|
| 🔍 **四维兼容对比** | 补丁 `apply --check` / seam 符号存在性 / peerDeps 版本 / 快照锚定 |
| 🧪 **编译验证** | 插件源码放进最新 mainline workspace 跑 `tsc`——编译失败 = 100% 不兼容 |
| 📡 **每日自动更新** | 02:00 抓最新快照全量索引，报告/仪表盘随 cron 推送 |
| 🐙 **PR 跟踪** | org 全部 open PR 一览 |
| ⚠️ **漂移 issue 直报** | 发现 API 漂移自动提交到对应插件 repo 的 issue |

## 现在

<!-- AUTO:ecosystem:START -->
> 自动更新：2026-08-12_0305（cron 每 8 小时 · 报告日 2026-08-12 · mainline `0882344`）

**生态仪表盘**

| 指标 | 值 |
|---|---|
| 仓库总数 | 147 |
| ✅ 无需适配 | 67 |
| ⚠️ 需适配 | 10 |
| 关注 / 占位 / 不适用 / 已删除 | 3 / 6 / 2 / 1 |
| 🐙 开放 PR | 3 |

📄 **最新报告**：[mainline-compat.md](reports/2026-08-09/mainline-compat.md) · [当日索引](reports/2026-08-09/index.md)（完整矩阵 + 双方建议）

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
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | 未知（不同谱系） | 需适配 |
| [dsh-subagent-tree](https://github.com/dsh-external/dsh-subagent-tree) | 未知 | 需适配 |
| [dsh-working-activity](https://github.com/dsh-external/dsh-working-activity) | 未知（非 commit 锚定: 20260804T143803Z） | 需适配 |
| [ex-setting](https://github.com/dsh-external/ex-setting) | 未知（不同谱系） | 需适配 |
| [plugin-registry](https://github.com/dsh-external/plugin-registry) | 未知（非 commit 锚定: 20260804T143803Z） | 需适配 |
| [Qwen-MM-Plugins](https://github.com/dsh-external/Qwen-MM-Plugins) | 未知（不同谱系） | 需适配 |
| [sandbox-mxc](https://github.com/dsh-external/sandbox-mxc) | 未知（不同谱系） | 需适配 |
| [turtle-ui](https://github.com/dsh-external/turtle-ui) | 未知（不同谱系） | 需适配 |
| [web-components](https://github.com/dsh-external/web-components) | 未知（不同谱系） | 需适配 |
**正在跟踪的 open PR**

| 仓库 | PR | 标题 | 更新 |
|---|---|---|---|
| [group-chat-diary](https://github.com/dsh-external/group-chat-diary) | [#4](https://github.com/dsh-external/group-chat-diary/pull/4) | Automate Cloudflare Pages deployment | 2026-08-07 |
| [dsh-live-stats](https://github.com/dsh-external/dsh-live-stats) | [#1](https://github.com/dsh-external/dsh-live-stats/pull/1) | fix: make live token and TPS accounting provider-aligned | 2026-08-07 |
<!-- AUTO:ecosystem:END -->

## 开发者怎么用

1. **查自己的插件**：看上面仪表盘"需适配"清单 → 有你的插件？点进 [每日报告](reports/latest/) 看具体原因（补丁 CONFLICT / seam 缺失 / peerDeps 不匹配）
2. **mainline 更新后**：看 [CHANGELOG.md](CHANGELOG.md) 的破坏性变更清单，提前适配
3. **编译验证**：[compile-compat.md](reports/) 里查编译级兼容（失败=100% 不兼容）
4. **收到漂移 issue？** 本雷达自动提交的——对照新 API 签名修即可

## 关于

<details>
<summary>📖 工作原理与限制（点击展开）</summary>

- **每日 02:00 自动全量**：动态发现 org 仓库 → 拉最新 mainline 快照 → 四维对比 + 编译验证 + 构建部署 → 报告推送（`cron-check.sh` / `compare-mainline.sh`）
- **内容 private**：仅供 org 内测成员；org 插件迁移到个人账号后仍在本雷达扫描范围（动态发现自动跟随）
- **诚实边界**：编译失败 ≠ 不可用（56% 自带 lib 可运行）；未知（待调研）仓库标注明确不猜测
- 完整 SOP：`docs/SOP.md`；插件修复/安装测试：`docs/plugin-fix-test.md`

</details>
