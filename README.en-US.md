# Awesome DSH Plugins

<p align="center">
  <img src="assets/banner-entertainment.jpg" width="440" alt="Awesome DSH Plugins banner"><br>
  <img src="assets/stickers/21-tests-passed.png" width="126" alt="Tests passed">
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/147500" title="GitHub Trending Daily #22 · 2026-08-14 · all languages"><img src="https://trendshift.io/api/badge/trendshift/repositories/147500/daily" alt="Trendshift"></a>
</p>

**A daily-updated radar that auto-discovers and compatibility-tests every plugin for DeepSeek Harness.**
Know which plugins work before you install them.

[![confirmed](https://img.shields.io/badge/confirmed-5075-blue)](#featured) [![scan](https://img.shields.io/badge/scan-every_6h-green)](#ecosystem-snapshot) [![tested](https://img.shields.io/badge/tested-1673-orange)](#how-we-assess-compatibility) [![dshfind](https://dshfind.com/api/badge/AdamPlatin123/awesome-dsh-plugins?lang=en)](https://dshfind.com/plugins/AdamPlatin123/awesome-dsh-plugins?ref=badge) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

[![runtime OK](https://img.shields.io/badge/runtime_OK-979-brightgreen)](#2-understand-status-unified-4-tier-scale) [![incompatible](https://img.shields.io/badge/incompatible-600-red)](#2-understand-status-unified-4-tier-scale) [![pending](https://img.shields.io/badge/pending-94-yellow)](#2-understand-status-unified-4-tier-scale) [![untested](https://img.shields.io/badge/untested-0-lightgrey)](#2-understand-status-unified-4-tier-scale)

[English](README.en-US.md) | [简体中文](README.md)

---

**What is this?** DeepSeek Harness (DSH) is an open-source coding agent where everything is a plugin. This repo is a **radar** that automatically tracks its plugin ecosystem — **5075 plugin repos indexed** (manifest-level classification, v2 engine), **1673 runtime-tested on the k8s track**.

## How it works

> Data as of snapshot `20260818T190001Z` (2026-08-19 03:00:01 UTC+8 · classifier unified-v2-bridge)

<!-- AUTO:pipeline:START -->
```mermaid
flowchart TB
    subgraph Discovery["Discovery (every 6h · probe every 15 min)"]
        A1["GitHub Search<br/>topic ×2 + keyword ×3<br/>candidates 9247 · age 58m"]
        A2["Local DB merge · dedupe by repo id"]
        A3["Private org repos excluded<br/>35s stagger · 403 backoff · dshow blocklist"]
    end
    subgraph Validation["Validation (driver 20s streaming loop)"]
        B1{"package.json<br/>name + main/exports/dsh?"}
    end
    B1 -->|"plugins 5075"| C1["k8s runtime test<br/>1 pod per plugin · concurrency 10<br/>dsh agent + Qwen (de-stream)"]
    B1 -->|"non-plugins (dropped 1064)"| B3["dropped to save space"]
    C1 --> D1{"verdict · total 1673"}
    D1 -->|"979 / 600"| E1["aggregate + README stats"]
    D1 -->|"94 env retries"| C1
    E1 --> E2["cadence deliver<br/>delta this cycle —/100<br/>dual-repo bot PRs (idempotent)"]
    M["radar-probe every 15 min self-heal<br/>7 metric streams × 60s · done 0"]
    M -.-> A1
    M -.-> C1
```
<!-- AUTO:pipeline:END -->

## Quick Start

| Goal | Link |
|---|---|
| Browse featured plugins | [Featured](#featured) — rc.8 verified · sorted by stars |
| Find a plugin by use case | [Plugin Catalog](#plugin-catalog) — 13 categories · per-plugin details in [PLUGINS-ALL.md](PLUGINS-ALL.md); [PLUGINS.md](PLUGINS.md) is the PR-registered list |
| Browse all auto-discovered repos | [ Ecosystem Snapshot](#ecosystem-snapshot) — dated compatibility matrix |
| See what changed recently | [ CHANGELOG](CHANGELOG.md) |
| Register or submit a plugin | [ For Plugin Developers](#for-plugin-developers) · add the `dsh-plugin` topic → discovered within 8h · [PR template](.github/PULL_REQUEST_TEMPLATE.md) |
| Maintain this radar | [ Automation SOP](docs/SOP.md) |
| Plugin user guide | [ For Plugin Users](#for-plugin-users) |
| How we assess compatibility | [ How We Assess Compatibility](#how-we-assess-compatibility) |
| Join the community | [ dshfind.com](#dsh-learning-community-dshfindcom) · [Discussion group](#community-discussion-group) |

> [!IMPORTANT]
> **Inclusion ≠ compatible, static check ≠ runtime-usable, runtime-usable ≠ security-audited.**
> This repo provides traceable filtering signals, not official DSH endorsement. Always review plugin source, permissions, dependencies, and license before installing.

## Featured

<!-- AUTO:featured:START -->

> 人工策展 43 款 rc.8 实测可用插件（v4flash 全量重测通过者，2026-08-21），类序与类内均按星标降序；星标每 6 小时自动刷新（成员调整请提 PR 修改 data/awesome-50.json）。数据截至 2026-08-22 03:00（UTC+8）。

### ⌨️ 终端与桌面端（3）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | 17506 | ✅ | 为 DSH 插件生态打造的现代化桌面端（雷达判需适配，星数两日翻倍） |
| [deepseek-harness-desktop](https://github.com/hairyf/deepseek-harness-desktop) | 842 | ✅ | Tauri 桌面版：5MB 安装包零环境配置，Win/macOS/Linux |
| [Bigfish](https://github.com/turtle2209/Bigfish) | 290 | ✅ | 第三方桌面端发行版：内置 Node 运行时双击即用（雷达判需适配——发行版形态非单插件安装） |

### 🧠 记忆与上下文（2）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [EverOS](https://github.com/EverMind-AI/EverOS) | 12313 | ✅ | 全 agent 便携记忆层：本地优先、Markdown-native |
| [mnemon](https://github.com/mnemon-dev/mnemon) | 502 | ✅ | 跨 agent、本地优先的持久记忆 |

### 🚀 智力增强 Booster（8）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | 6552 | ✅ | 注入器 × 思维模式路由套装：免重启运行时注入器 + 任务感知推理模式路由预设（P1-P23 实测） |
| [ouroboros](https://github.com/Q00/ouroboros) | 5602 | ✅ | Agent OS：agent 自我变强、人只守底线——自进化运行时 |
| [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | 3696 | ✅ | 两阶段 DSH 预设：极简模式对齐启动 → 全量装载（智力增强向） |
| [Aegis](https://github.com/GanyuanRan/Aegis) | 1092 | ✅ | 软件工程方法论技能包：baseline-first 规划、系统性重构（对方清单 1089★） |
| [superdesign-skill](https://github.com/superdesigndev/superdesign-skill) | 436 | ✅ | UI 与营销图形设计技能（Superdesign 画布，读仓取上下文） |
| [harmony-next.skills](https://github.com/linhay/harmony-next.skills) | 334 | ✅ | 技能驱动的工作流增强 |
| [superpowers-dsh](https://github.com/LayneChai/superpowers-dsh) | 75 | ✅ | TDD/调试/计划等开发技能集 |
| [forkprobe](https://github.com/Jayden-X-L/forkprobe) | 69 | ✅ | 同一任务跑多个技能对比，自动选优 |

### 🗂 文件、数据与浏览（5）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [openpencil](https://github.com/ZSeven-W/openpencil) | 5530 | ✅ | OpenPencil 设计工具本体（DSH 适配器另列下行） |
| [treg](https://github.com/superdesigndev/treg) | 550 | ✅ | 工具目录：检索约 2600 个外部端点（SEO/SERP/外链/社媒/人脉） |
| [better-deepseek](https://github.com/EdgeTypE/better-deepseek) | 399 | ✅ | Better DeepSeek Chrome 扩展桥接插件 |
| [dsh-browser](https://github.com/Lum1104/dsh-browser) | 372 | ✅ | Chrome 侧栏扩展让 DSH 直接操控浏览器；双件套（桥插件+扩展），rc.8 实测桥插件可装可用 |
| [modsearch](https://github.com/liustack/modsearch) | 210 | ✅ | 纯文本 agent 的网页搜索桥：web/X 结构化 JSON 证据（modlens 同作者） |

### 🖥 界面与工作台（5）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | 5413 | ✅ | Web UI 增强与皮肤合集：任务看板、Git 图、移动端、皮肤中心 |
| [dsh-genui](https://github.com/omdsh-dev/dsh-genui) | 286 | ✅ | GenUI 内联组件：图表/表单/测验/3D 场景 + action 事件环 |
| [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) | 198 | ✅ | 对话中生成交互式可视化卡片 |
| [Liang-Saint-Slider](https://github.com/BruzWJ/Liang-Saint-Slider) | 92 | ✅ | 模型与思考力度选择滑条 |
| [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) | 87 | ✅ | 划选文字→批注→随消息发送，回复逐条对照 |

### 🎮 娱乐生活（3）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [petdex](https://github.com/crafter-station/petdex) | 3947 | ✅ | 生态最高星桌宠图鉴 |
| [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | 1560 | ✅ | 深海鲸鱼养成 |
| [dsh-kun-like-pet](https://github.com/liyupi/dsh-kun-like-pet) | 80 | ✅ | 小坤桌宠：随 Agent 工作状态切换 9 种动作 |

### 👁 视觉与多模态（3）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [modlens](https://github.com/liustack/modlens) | 3496 | ✅ | 生态第一个视觉插件，视觉工作流的基准方案 |
| [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | 930 | ✅ | 内置免费视觉模型路由，给文本 agent 装眼睛 |
| [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | 806 | ✅ | 带意图图片问答、长截图 OCR、UI 还原 |

### 💻 编码与生产力（6）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [TokenTracker](https://github.com/xiufengsun/TokenTracker) | 1398 | ✅ | 本地优先的 31 种编码工具 token 用量与成本追踪 |
| [api-relay-audit](https://github.com/toby-bridges/api-relay-audit) | 798 | ✅ | 从 DSH 发起 AI API 中继/LLM 代理本地安全审计，产出 Markdown 报告 |
| [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) | 448 | ✅ | Codex 风格 @file 引用：搜索并挂载工作区文件 |
| [mobius](https://github.com/nutshellai-tech/mobius) | 284 | ✅ | 编码增强 |
| [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) | 144 | ✅ | 按会话/按日 API 成本、预算与用量、官方余额、历史看板 |
| [TokenLedger](https://github.com/zh667/TokenLedger) | 127 | ✅ | 侧栏用量面板：把 token 归因到实际服务请求的中继站 |

### 🤖 Agent 能力与编排（4）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [helloagents](https://github.com/hellowind777/helloagents) | 693 | ✅ | agent 能力合集 |
| [rea](https://github.com/morluto/rea) | 365 | ✅ | 用 agent 逆向工程任何东西：从应用行为到原生二进制 |
| [dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) | 223 | ✅ | 把 ChatGPT(Codex)/Claude/Grok 订阅作为 DSH 的 LLM 供应商，设置页管理 |
| [open-record-replay](https://github.com/humblebanana/open-record-replay) | 139 | ✅ | macOS 录制回放：把鼠标/键盘/UI 事件存为结构化轨迹供 agent 学习重放 |

### 🛒 市场与管理（3）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [dsh-market](https://github.com/dsh-market/dsh-market) | 1640 | ✅ | 持续收录 1000+ 插件的市场：中文搜索 + 五维评分 |
| [dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) | 62 | ✅ | Web UI 一键管理插件：启停/装卸/环境管理 |
| [dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) | 27 | ✅ | 插件健康检查：清单协议/patch 格式/构建陷阱 |

### 📡 消息通讯与 IM（1）

| 插件 | ⭐ | rc.8 实测 | 说明 |
|---|---:|---|---|
| [dsh-lark](https://github.com/omdsh-dev/dsh-lark) | 40 | ✅ | 飞书 IM bot 频道（官方渠道插件） |

> 实测 = rc.8 + v4flash 标准安装与单任务验证（2026-08-21 对 50 仓全量重测，仅收录通过者；逐仓日志见 data/rc8-retest-20260821/）；雷达 k8s 历史判定见 [PLUGINS-ALL.md](PLUGINS-ALL.md)；安装第三方插件前请审查源码并固定 commit。

<!-- AUTO:featured:END -->

## Plugin Catalog

<!-- AUTO:catalog:START -->

Per-plugin details (verdict · location · stars) in **PLUGINS-ALL.md**.

- **🎓 技能包**（20）— OK 7 · incompatible 1 · pending 1 · untested 11 · watching 0 — [details](PLUGINS-ALL.md#-技能包20)
- **🧠 记忆增强**（15）— OK 7 · incompatible 4 · pending 2 · untested 2 · watching 0 — [details](PLUGINS-ALL.md#-记忆增强15)
- **🎨 主题皮肤**（11）— OK 2 · incompatible 1 · pending 2 · untested 6 · watching 0 — [details](PLUGINS-ALL.md#-主题皮肤11)
- **🛒 市场与管理**（40）— OK 20 · incompatible 11 · pending 3 · untested 2 · watching 4 — [details](PLUGINS-ALL.md#-市场与管理40)
- **🔌 Web UI 增强**（380）— OK 225 · incompatible 71 · pending 41 · untested 24 · watching 19 — [details](PLUGINS-ALL.md#-web-ui-增强380)
- **💻 编码开发**（344）— OK 175 · incompatible 68 · pending 29 · untested 38 · watching 34 — [details](PLUGINS-ALL.md#-编码开发344)
- **🤖 Agent 能力**（287）— OK 132 · incompatible 69 · pending 29 · untested 27 · watching 30 — [details](PLUGINS-ALL.md#-agent-能力287)
- **📡 消息通讯**（109）— OK 58 · incompatible 24 · pending 13 · untested 8 · watching 6 — [details](PLUGINS-ALL.md#-消息通讯109)
- **🗂 文件数据**（93）— OK 47 · incompatible 19 · pending 14 · untested 8 · watching 5 — [details](PLUGINS-ALL.md#-文件数据93)
- **🎮 娱乐生活**（52）— OK 30 · incompatible 9 · pending 6 · untested 1 · watching 6 — [details](PLUGINS-ALL.md#-娱乐生活52)
- **🛠 基建部署**（217）— OK 87 · incompatible 75 · pending 23 · untested 8 · watching 24 — [details](PLUGINS-ALL.md#-基建部署217)
- **📚 学习研究**（16）— OK 5 · incompatible 5 · pending 1 · untested 1 · watching 4 — [details](PLUGINS-ALL.md#-学习研究16)
- **❓ 其他**（595）— OK 273 · incompatible 118 · pending 41 · untested 56 · watching 107 — [details](PLUGINS-ALL.md#-其他595)

<!-- AUTO:catalog:END -->

##  DSH Learning Community dshfind.com

[dshfind.com](https://dshfind.com) — Learn DSH principles, discover plugins & share best practices.

<a href="https://dshfind.com"><img src="assets/dshfind-en.png" width="600" alt="dshfind.com — DSH learning & sharing community"></a>

[ dshfind.com](https://dshfind.com) · [GitHub](https://github.com/hikariming/dshfind)

## Community Discussion Group

The DSH plugin community discussion group on WeChat: plugin authors, maintainers, and users discuss plugin development, compatibility issues, and new releases.

<img src="assets/community-discussion.jpg" width="350" alt="DSH plugin community discussion group">

> The QR code is valid for 7 days (before 2026-08-26).

## For Plugin Users

### 1. Find candidate plugins

- Browse the [Plugin Catalog](#plugin-catalog) first, with per-plugin details in [PLUGINS-ALL.md](PLUGINS-ALL.md) — the auto-discovered, runtime-tested full listing (verdict · location · stars per entry).
- [PLUGINS.md](PLUGINS.md) is the PR-registered community list (manual descriptions + reported runtime results); it complements the auto-discovered catalog.
- If both miss it, search the repo name or keywords in the dated [Ecosystem Snapshot](#ecosystem-snapshot) index.
- Treat repos that are inaccessible, lack a README or license, or sit unmaintained as high-risk candidates — not "verified plugins".

### 2. Understand status (unified 4-tier scale)

All entries use a **single runtime scale** (k8s container tests — see the test version note below). The four tiers are mutually exclusive:

| Status | What it says | What it does not say |
|---|---|---|
|  Runtime OK | Actually loaded and completed the verification task under the recorded test version | Not a full functional, performance, or security test |
|  Runtime incompatible | Hard failure — missing deps, read-only sandbox, missing internal packages (3 retries all failed) | Not permanently unusable; the author may have fixed it in a newer version |
|  Pending | Test-environment failure; the verdict is incomplete | **Not partially compatible** — awaiting a retest |
| · Untested | Never dispatched to a runtime test | Do not infer either compatibility or incompatibility |

> [!NOTE]
> **Test version**: dsh (in-container agent) driven by Qwen3.6-35B (via the de-stream proxy) · k8s, 5 shards · each run is anchored by the snapshot `run_id` (currently `20260818T190001Z`). The DSH npm version is not recorded per snapshot — cross-check via run_id and the `reports/agent-test/` dates.
> **Scale note**: "tested N" in badges and stats is the single-run scale; the catalog and full listing use the cross-run cumulative scale — the numbers legitimately differ.

Every conclusion carries four facts: **plugin commit, mainline commit, test date, test level**. If any one is missing, lower your trust in the result.

### 3. Install, verify, and roll back

This catalog is not a package manager and ships no install command verified by this repo. Follow the plugin's own README, ideally in this order:

1. Read the plugin's install, configuration, permission, and uninstall instructions.
2. Pin a plugin version or commit; do not ride a drifting default branch.
3. Load it first in an isolated profile or test environment — no production keys or sensitive data.
4. Run one minimal functional task; record the DSH version, plugin version, and logs.
5. Keep the previous config and lockfile so a failure can be rolled back cleanly.

If the plugin itself misbehaves, report it in the plugin repo first; if a catalog link, category, or status evidence is wrong, open an issue or PR here.

## For Plugin Developers

### Minimum inclusion criteria

The public catalog should list only repos an ordinary visitor can open. An auto-discovered candidate should at least:

- Be publicly accessible and tagged with the `dsh-plugin` topic;
- Have a valid root `package.json` with a non-empty `name`;
- Provide `main`, `exports`, or an explicit `dsh` integration entry;
- Ship a README covering what it does, how to install, how to uninstall, and a minimal usage example;
- Declare every runtime dependency in `dependencies` / `peerDependencies`;
- State the supported DSH version, snapshot, or verified commit;
- Include a license, and never commit secrets, personal data, or private repo content to the public catalog.

Package names should use a namespace you control. Only projects granted `dsh-external` maintainer access should use `@dsh-external/*`; do not squat namespaces owned by others or reserved by the official project.

### A qualified plugin README must include

| Section | Questions it should answer |
|---|---|
| Overview | What problem does the plugin solve, and for whom? |
| Compatibility | Which DSH versions or mainline commits are supported? When was it last verified? |
| Install / Uninstall | How to install, upgrade, disable, and fully remove? |
| Quick start | What is the minimal config and one reproducible example? |
| Configuration | Which settings, defaults, env vars, and sensitive entries exist? |
| Permissions & data | Which files, network endpoints, credentials, or user data does it touch? |
| Troubleshooting | Common errors, log locations, and rollback? |
| Development | How to build, test, and contribute? |
| License & security | Which license? How are security issues reported privately? |

### Submit a plugin

1. Add the `dsh-plugin` topic to your repo and wait for the next scan.
2. Append the plugin name, repo link, and a one-line description under the right category in [PLUGINS.md](PLUGINS.md).
3. Self-check against the minimum criteria above.
4. Open a PR using the [PR template](.github/PULL_REQUEST_TEMPLATE.md), including your test environment and results.

Small PRs that just fix a link, category, description, or status evidence are always welcome. Do not copy private issues, secrets, member lists, or long third-party excerpts into catalog PRs.

## How We Assess Compatibility

| Level | Current check | Fair conclusion |
|---|---|---|
| L0 Discovery | Topic, repo visibility, basic metadata | This is a candidate repo |
| L1 Manifest | `package.json`, name, entry fields | It "looks installable", but loading is unproven |
| L2 Static compat | Patches, extension points (seams), dependency ranges | Known drift signals found, or no blocking signal so far |
| L3 Compile experiment | Type or syntax check in a pinned workspace | Valid only for that build setup; missing deps and environment issues must be separated from real API drift |
| L4 Runtime test | Install, load, minimal task or tool call | Success or failure observed on the recorded environment and commits |

> [!NOTE]
> The front page never merges these levels into one fuzzy "compatibility rate". Static pass, compile pass, and runtime pass use different fields and denominators; full evidence lives in the dated reports.

### Known limitations

- Both mainline and plugins move fast; older conclusions expire quickly.
- A clean static check does not guarantee a successful real run.
- A compile failure may come from the test environment, missing dependencies, or misconfiguration — do not equate it with API incompatibility.
- A runtime success covers only the minimal task in the report — not every feature, platform, or configuration.
- Auto-generated LLM summaries are navigation aids only; they never replace the raw matrices and logs.

## Repository Structure

| Path | Contents |
|---|---|
| `PLUGINS.md` | Manually curated and categorized entry list |
| `reports/<YYYY-MM-DD>/index.md` | Full scan index for that date |
| `reports/<YYYY-MM-DD>/mainline-compat.md` | Static compatibility matrix for that date |
| `reports/<YYYY-MM-DD>/compile-compat.md` | Compile and syntax experiment results for that date |
| `reports/<YYYY-MM-DD>/runtime-test.md` | Runtime-level test results for that date |
| `CHANGELOG.md` | Dated ecosystem change log |
| `docs/SOP.md` | Automation, build, and report maintenance notes |
| `scripts/` | Discovery, checking, testing, and rendering scripts |

<details>
<summary>Maintainers: README auto-generation conventions</summary>

- Manual content lives outside the auto markers; generators only replace `AUTO:ecosystem` blocks.
- The front page shows only summaries and report links, never full repo tables.
- At most 10 new/changed entries are listed; the rest link to `CHANGELOG.md`.
- Repo links must use the full `owner/name` from scan results — never hardcode an org name.
- Auto blocks use real date paths; a plain `reports/LATEST.md` is also generated as a verifiable stable entry that does not depend on directory symlinks.
- When a report is missing, empty, or fails numeric validation, show "data unavailable" — never reuse stale values or draw strong conclusions.
- Runtime and static results use different fields and denominators, and show test coverage counts.

</details>

## Ecosystem Snapshot

<!-- AUTO:ecosystem:START -->
> 渲染于快照 20260818T190001Z（2026-08-19 03:00 UTC+8）· 数据源 data/snapshots/（渲染即对齐）

| 证据层 | 当前结果 |
|---|---:|
| 自动收录 | 5075 个仓库 |
| 运行级实测 | 979 可用 · 600 不兼容 · 94 待定（共 1673 个，k8s agent 口径）|

[完整索引](PLUGINS-ALL.md) · [运行实测](reports/2026-08-19/agent-test-v2.md)

<!-- AUTO:ecosystem:END -->

<!-- AUTO:ecosystem:END -->

The snapshot only answers "what does today's evidence say" — the front page never copies hundreds of repo rows and change logs. Per-repo verdicts, failure reasons, daily additions, and open PRs live in the dated reports.

## Boundaries & Credits

This repo maintains the catalog, detection rules, and evidence reports — it does not host third-party plugin code. Thanks to every contributor who submitted plugins, reproduced issues, corrected metadata, and kept the test pipeline alive.

This repository's catalog content and scripts are available under the [MIT License](LICENSE); third-party plugins remain governed by the licenses declared in their own repositories.

Huge thanks to everyone who joined the beta test — the group photo shows only part of the list, and many more friends contributed along the way!

![DSH beta group photo](assets/dsh-miji-heying.png)

Let's keep deep diving!
