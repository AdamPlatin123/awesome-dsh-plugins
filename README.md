# 🔭 DSH Plugin Radar

> **你的插件还兼容最新 dsh 吗？** 每天自动扫描 org 全部插件仓库与 mainline 的接口漂移——编译验证、补丁检测、seam 追踪、LLM 每日摘要。公测前最有价值的兼容性检查站。

[![repos](https://img.shields.io/badge/扫描插件-269+-blue)]() [![compat](https://img.shields.io/badge/兼容验证-编译级-green)]() [![mainline](https://img.shields.io/badge/mainline-每日快照-orange)]() [![cron](https://img.shields.io/badge/自动-每日%2002:00-purple)]()

## 🚀 直接跳转

| 想看 | 跳转 |
|---|---|
| 今天生态状态（LLM 摘要） | [开发者摘要](reports/latest/mainline-summary.md) |
| 完整兼容矩阵（147+ 仓逐仓判定） | [mainline-compat.md](reports/latest/mainline-compat.md) |
| mainline 破坏性变更清单 | [CHANGELOG.md](CHANGELOG.md) |
| 编译级兼容验证（9/98 通过详表） | [compile-compat.md](reports/) |
| 完整 SOP（监控/构建/插件验证） | [docs/SOP.md](docs/SOP.md) |

## 现在

<!-- AUTO:ecosystem:START -->
> 自动更新：2026-08-13_0208（cron 每 8 小时 · 报告日 2026-08-13 · mainline `340d23a`）

**生态仪表盘**

| 指标 | 值 |
|---|---|
| 仓库总数 | 275 |
| ✅ 无需适配 | 91 |
| ⚠️ 需适配 | 6 |
| 关注 / 占位 / 不适用 / 已删除 | 25 / 15 / 2 / 0 |
| 🐙 开放 PR | 11 |

📄 **最新报告**：[兼容矩阵](reports/2026-08-13/mainline-compat.md) · [开发者摘要](reports/2026-08-13/mainline-summary.md) · [当日索引](reports/2026-08-13/index.md)

**今日新增 / 修改仓库**

| 仓库 | 类型 |
|---|---|
| [dsh-web-ui-notify](https://github.com/dsh-external/dsh-web-ui-notify) | 🆕 新增 |
| [dsh-evolve](https://github.com/dsh-external/dsh-evolve) | 🆕 新增 |
| [dsh-island](https://github.com/dsh-external/dsh-island) | 🆕 新增 |
| [dsh-drag-and-drop](https://github.com/dsh-external/dsh-drag-and-drop) | 🆕 新增 |
| [dsh-message-edit](https://github.com/dsh-external/dsh-message-edit) | 🆕 新增 |
| [dsh-deep-research](https://github.com/dsh-external/dsh-deep-research) | 🆕 新增 |
| [dsh-multimedia-webui-input](https://github.com/dsh-external/dsh-multimedia-webui-input) | 🆕 新增 |
| [repo-visibility-guard](https://github.com/dsh-external/repo-visibility-guard) | 🆕 新增 |
| [dsh-grok-tui](https://github.com/dsh-external/dsh-grok-tui) | 🆕 新增 |
| [ds_web_craw](https://github.com/dsh-external/ds_web_craw) | 🆕 新增 |
| [fabric](https://github.com/dsh-external/fabric) | 🆕 新增 |
| [dsh-browser](https://github.com/dsh-external/dsh-browser) | 🆕 新增 |
| [dsh-desktop-mac](https://github.com/dsh-external/dsh-desktop-mac) | 🆕 新增 |
| [dsh-public-repo-monitor](https://github.com/dsh-external/dsh-public-repo-monitor) | 🆕 新增 |
| [dsh-tui](https://github.com/dsh-external/dsh-tui) | 🆕 新增 |
| [dsh-inspect](https://github.com/dsh-external/dsh-inspect) | 🆕 新增 |
| [dsh-cc-tui](https://github.com/dsh-external/dsh-cc-tui) | ✏️ 修改 |
| [dsh-memory-evolve](https://github.com/dsh-external/dsh-memory-evolve) | ✏️ 修改 |
| [dsh-session-search](https://github.com/dsh-external/dsh-session-search) | ✏️ 修改 |
| [dsh-sfw](https://github.com/dsh-external/dsh-sfw) | ✏️ 修改 |
| [dsh-skins](https://github.com/dsh-external/dsh-skins) | ✏️ 修改 |
| [dsh-ui-progress](https://github.com/dsh-external/dsh-ui-progress) | ✏️ 修改 |
| [dsh-ui-whale](https://github.com/dsh-external/dsh-ui-whale) | ✏️ 修改 |
| [dsh-win-port](https://github.com/dsh-external/dsh-win-port) | ✏️ 修改 |
| [hub](https://github.com/dsh-external/hub) | ✏️ 修改 |
| [dsh-hub](https://github.com/dsh-external/dsh-hub) | ✏️ 修改 |
| [dsh-a2a](https://github.com/dsh-external/dsh-a2a) | ✏️ 修改 |
| [dsh-feishu-notify](https://github.com/dsh-external/dsh-feishu-notify) | ✏️ 修改 |
| [dsh-web-workflow-visualizer](https://github.com/dsh-external/dsh-web-workflow-visualizer) | ✏️ 修改 |
| [dsh-checkpoint](https://github.com/dsh-external/dsh-checkpoint) | ✏️ 修改 |
| [dsh-rewind](https://github.com/dsh-external/dsh-rewind) | ✏️ 修改 |
| [official-plugins-port](https://github.com/dsh-external/official-plugins-port) | ✏️ 修改 |
| [oh-my-dsh](https://github.com/dsh-external/oh-my-dsh) | ✏️ 修改 |
| [dsh-profile-bundle-example](https://github.com/dsh-external/dsh-profile-bundle-example) | ✏️ 修改 |
| [dsh-plan-execute](https://github.com/dsh-external/dsh-plan-execute) | ✏️ 修改 |
| [dsh-paste-input](https://github.com/dsh-external/dsh-paste-input) | ✏️ 修改 |
| [zotero-harvest](https://github.com/dsh-external/zotero-harvest) | ✏️ 修改 |
| [dsh-bash-encoding](https://github.com/dsh-external/dsh-bash-encoding) | ✏️ 修改 |
| [dsh-skill-stats](https://github.com/dsh-external/dsh-skill-stats) | ✏️ 修改 |
| [dsh-web-archive](https://github.com/dsh-external/dsh-web-archive) | ✏️ 修改 |
**需适配（补丁基线 / seam 变化）**

| 仓库 | 锚定 | 判定 |
|---|---|---|
| [dsh-subagent-tree](https://github.com/dsh-external/dsh-subagent-tree) | 未知 | 需适配 |
| [dsh-working-activity](https://github.com/dsh-external/dsh-working-activity) | 未知（非 commit 锚定: 20260804T143803Z） | 需适配 |
| [turtle-ui](https://github.com/dsh-external/turtle-ui) | 未知（不同谱系） | 需适配 |
| [dsh-tps](https://github.com/dsh-external/dsh-tps) | 未知 | 需适配 |
| [dsh-split-panes](https://github.com/dsh-external/dsh-split-panes) | 未知 | 需适配 |
| [dsh-ohos-patch](https://github.com/dsh-external/dsh-ohos-patch) | 未知 | 需适配 |
**正在跟踪的 open PR**

| 仓库 | PR | 标题 | 更新 |
|---|---|---|---|
| [dsh-pi-adapter](https://github.com/dsh-external/dsh-pi-adapter) | [#6](https://github.com/dsh-external/dsh-pi-adapter/pull/6) | feat: register commands through cordis DI activation, not first session/created | 2026-08-12 |
| [dsh-auto-approval](https://github.com/dsh-external/dsh-auto-approval) | [#2](https://github.com/dsh-external/dsh-auto-approval/pull/2) | feat: L0 self-kill guard + block-device redirect deny | 2026-08-12 |
| [DSH-better-sidebar](https://github.com/dsh-external/DSH-better-sidebar) | [#8](https://github.com/dsh-external/DSH-better-sidebar/pull/8) | refactor: 移除内置 Office 预览，迁移至独立插件 dsh-better-sidebar-plugin-office | 2026-08-12 |
| [dsh-pi-adapter](https://github.com/dsh-external/dsh-pi-adapter) | [#5](https://github.com/dsh-external/dsh-pi-adapter/pull/5) | feat: adapt-interactive ctx.ui tier + session-log quarantine audit | 2026-08-12 |
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | [#50](https://github.com/dsh-external/dsh-my-rsi/pull/50) | feat: migrate to 20260811 snapshot and reuse upstream surfaces | 2026-08-11 |
| [dsh-hub](https://github.com/dsh-external/dsh-hub) | [#15](https://github.com/dsh-external/dsh-hub/pull/15) | Align optional host capabilities and legacy cleanup | 2026-08-11 |
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | [#49](https://github.com/dsh-external/dsh-my-rsi/pull/49) | docs: record external method provenance (#45) | 2026-08-11 |
| [dsh-my-rsi](https://github.com/dsh-external/dsh-my-rsi) | [#43](https://github.com/dsh-external/dsh-my-rsi/pull/43) | feat: rsi-core live plugin execution face (#41) + supervised revival layer (#42) | 2026-08-11 |
| [session-teleport](https://github.com/dsh-external/session-teleport) | [#2](https://github.com/dsh-external/session-teleport/pull/2) | Add safe plugin lifecycle and real-device acceptance | 2026-08-10 |
| [group-chat-diary](https://github.com/dsh-external/group-chat-diary) | [#4](https://github.com/dsh-external/group-chat-diary/pull/4) | Automate Cloudflare Pages deployment | 2026-08-07 |
| [dsh-live-stats](https://github.com/dsh-external/dsh-live-stats) | [#1](https://github.com/dsh-external/dsh-live-stats/pull/1) | fix: make live token and TPS accounting provider-aligned | 2026-08-07 |
<!-- AUTO:ecosystem:END -->

## 🔍 四个检测维度（详述）

| 维度 | 测什么 | 怎么测 | 不兼容长啥样 |
|---|---|---|---|
| **补丁** | 插件对 mainline 的 git 补丁能否应用 | `git apply --check --3way` 在最新快照上试打 | `CONFLICT（4 个补丁中 0 个 OK）` |
| **seam** | 插件依赖的官方扩展点是否还在 | `git grep` 符号（ThemeService/tuiPrompt/slots…）跨两快照比对 | `缺: tuiPrompt`（TUI 移除后） |
| **peerDeps** | `@deepseek-ai/*` 版本范围与 mainline 实际 | package.json 声明 vs 快照版本 | `^0.0.1` 声明 vs `0.0.1-rc.1` 实际 |
| **编译** | 插件源码在最新 mainline 上能否 tsc 通过 | symlink 进 workspace → `tsc --noEmit` | `TS2339: Property 'requestCancelled' does not exist` |

## 📖 真实实例

**实例 1：漂移直报**（dsh-acp 案例）
```
编译验证发现 dsh-acp 调用了已不存在的 RequestError.requestCancelled
→ 自动提交 issue：[dsh-acp#1](https://github.com/dsh-external/dsh-acp/issues/1)
→ 标题：[compat] 与最新 mainline 很可能不兼容（API 漂移）：TS2339...
→ 插件作者拿到精确到行的修复线索
```

**实例 2：LLM 每日摘要**（08-13 实际产出）
```
> 核心变更即 @deepseek-ai/* 从 ^0.0.1 切换到 0.0.1-rc.1，
> 同时 tuiPrompt 被移除/改名，导致大量依赖范围不匹配与 API 缺失。
> 提前适配：统一用 ^0.0.1-rc.1，并加兼容导出映射替代 tuiPrompt。
```
→ 一次跨插件系统性变更（rc.1 切换）被自动识别——脚本模板做不到，LLM 可以。

**实例 3：插件自查三步**
```
1. 仪表盘"需适配"表看到 dsh-my-rsi
2. 点开每日报告 → "补丁 CONFLICT（3 个补丁中 1 个 OK）+ 缺 tuiPrompt"
3. 对照修复：rebase 补丁到新快照 + 替换 tuiPrompt 调用
```

## 关于

<details>
<summary>📖 工作原理与限制（点击展开）</summary>

- **每日 02:00 自动全量**：动态发现 org 仓库 → 拉最新 mainline 快照 → 四维对比 + 编译验证 + 构建部署 + LLM 摘要 → 报告推送（`cron-check.sh` / `compare-mainline.sh` / `report-llm.sh`）
- **内容 private**：仅供 org 内测成员；插件迁移到个人账号后仍在扫描范围（动态发现自动跟随）
- **诚实边界**：编译失败 ≠ 不可用（56% 自带 lib 可运行）；未知（待调研）仓库标注明确不猜测
- 完整 SOP：`docs/SOP.md`；插件修复/安装测试：`docs/plugin-fix-test.md`

</details>
