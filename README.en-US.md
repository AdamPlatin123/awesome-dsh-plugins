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

[![confirmed](https://img.shields.io/badge/confirmed-7738-blue)](#featured) [![scan](https://img.shields.io/badge/scan-every_6h-green)](#ecosystem-snapshot) [![tested](https://img.shields.io/badge/tested-9747-orange)](#how-we-assess-compatibility) [![dshfind](https://dshfind.com/api/badge/AdamPlatin123/awesome-dsh-plugins?lang=en)](https://dshfind.com/plugins/AdamPlatin123/awesome-dsh-plugins?ref=badge) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

[![runtime OK](https://img.shields.io/badge/runtime_OK-6560-brightgreen)](#2-understand-status-unified-4-tier-scale) [![incompatible](https://img.shields.io/badge/incompatible-2159-red)](#2-understand-status-unified-4-tier-scale) [![pending](https://img.shields.io/badge/pending-1028-yellow)](#2-understand-status-unified-4-tier-scale) [![untested](https://img.shields.io/badge/untested-0-lightgrey)](#2-understand-status-unified-4-tier-scale)

[English](README.en-US.md) | [简体中文](README.md)

---

**What is this?** DeepSeek Harness (DSH) is an open-source coding agent where everything is a plugin. This repo is a **radar** that automatically tracks its plugin ecosystem — **7738 plugin repos indexed** (manifest-level classification, v2 engine), **9747 runtime-tested on the k8s track**.

## How it works

> Data as of snapshot `20260828T203001Z` (2026-08-29 04:30:03 UTC+8 · classifier unified-v2-bridge)

<!-- AUTO:pipeline:START -->
```mermaid
flowchart TB
    subgraph Discovery["Discovery (every 6h · probe every 15 min)"]
        A1["GitHub Search<br/>topic ×2 + keyword ×3<br/>candidates 15930 · age 178m"]
        A2["Local DB merge · dedupe by repo id"]
        A3["Private org repos excluded<br/>35s stagger · 403 backoff · dshow blocklist"]
    end
    subgraph Validation["Validation (driver 20s streaming loop)"]
        B1{"package.json<br/>name + main/exports/dsh?"}
    end
    B1 -->|"plugins 7738"| C1["k8s runtime test<br/>1 pod per plugin · concurrency 10<br/>dsh agent + Qwen (de-stream)"]
    B1 -->|"non-plugins (dropped 1064)"| B3["dropped to save space"]
    C1 --> D1{"verdict · total 9747"}
    D1 -->|"6560 / 2159"| E1["aggregate + README stats"]
    D1 -->|"1028 env retries"| C1
    E1 --> E2["cadence deliver<br/>delta this cycle —/100<br/>dual-repo bot PRs (idempotent)"]
    M["radar-probe every 15 min self-heal<br/>7 metric streams × 60s · done 16"]
    M -.-> A1
    M -.-> C1
```
<!-- AUTO:pipeline:END -->

**🔌 Open-Source Plan — this page is produced automatically by the DSH Plugin Radar, which is being open-sourced in stages:**

| Phase | Content | Status |
|---|---|---|
| Phase 1 | Pipeline docs: [overview & roadmap](docs/radar/overview.md) · [architecture](docs/radar/architecture.md) · [data contracts](docs/radar/data-contracts.md) | ✅ Open-sourced |
| Phase 2 | Radar engine source (discovery · aggregation · rendering · distribution) | 🔜 After stabilization |
| Phase 3 | Test engine source: lightweight edition (no k8s · runs locally) · server edition (k8s cluster) | 🔜 After stabilization |

## Quick Start

| Goal | Link |
|---|---|
| Browse featured plugins | [Featured](#featured) — curated · 11 categories |
| Install a bundle instead of picking one by one | [Bundles](#-bundles) — presets · skill collections · distributions · recipes |
| Find a plugin by use case | [Plugin Catalog](#plugin-catalog) — 13 categories · per-plugin details in [PLUGINS-ALL.md](PLUGINS-ALL.md); [PLUGINS.md](PLUGINS.md) is the PR-registered list |
| Browse all auto-discovered repos | [ Ecosystem Snapshot](#ecosystem-snapshot) — dated compatibility matrix |
| See what changed recently | [ CHANGELOG](CHANGELOG.md) |
| Register or submit a plugin | [ For Plugin Developers](#for-plugin-developers) · add the `dsh-plugin` topic → discovered within 8h · [PR template](.github/PULL_REQUEST_TEMPLATE.md) |
| Learn about the radar & open-source plan | [ Radar overview & roadmap](docs/radar/overview.md) · architecture in [docs/radar/](docs/radar/) |
| Plugin user guide | [ For Plugin Users](#for-plugin-users) |
| How we assess compatibility | [ How We Assess Compatibility](#how-we-assess-compatibility) |
| Join the community | [ dshfind.com](#dsh-learning-community-dshfindcom) · [Discussion group](#community-discussion-group) |

> [!IMPORTANT]
> **Inclusion ≠ compatible, static check ≠ runtime-usable, runtime-usable ≠ security-audited.**
> This repo provides traceable filtering signals, not official DSH endorsement. Always review plugin source, permissions, dependencies, and license before installing.

## Featured

<!-- AUTO:featured:START -->

> 人工策展 50 款插件，按 11 类分组、类内按星标排序；星标每 6 小时自动刷新（成员调整请提 PR 修改 data/awesome-50.json）。数据截至 2026-08-28 19:30（UTC+8）。

### 🚀 智力增强 Booster（6）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | 6922 | — | 注入器 × 思维模式路由套装：免重启运行时注入器 + 任务感知推理模式路由预设（P1-P23 实测） |
| [harmony-next.skills](https://github.com/linhay/harmony-next.skills) | 342 | ✅ | 技能驱动的工作流增强 |
| [superpowers-dsh](https://github.com/LayneChai/superpowers-dsh) | 105 | ✅ | TDD/调试/计划等开发技能集 |
| [forkprobe](https://github.com/Jayden-X-L/forkprobe) | 71 | ✅ | 同一任务跑多个技能对比，自动选优 |
| [dsh-tool-turbo](https://github.com/Electricitysheep/dsh-tool-turbo) | 7 | ✅ | 按轮次自动优化 reasoning_effort（推理力度） |
| [dsh-reasoning-settings](https://github.com/JuneLearn/dsh-reasoning-settings) | 6 | ✅ | 推理设置控制：让模型按任务切换思考档位 |

### 🖥 界面与工作台（7）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | 6354 | ✅ | Web UI 增强与皮肤合集：任务看板、Git 图、移动端、皮肤中心 |
| [DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | 3055 | ✅ | 侧边栏变完整工作台：文件编辑/终端/Git/子代理，支持三方注册扩展页 |
| [dsh-genui](https://github.com/omdsh-dev/dsh-genui) | 360 | ✅ | GenUI 内联组件：图表/表单/测验/3D 场景 + action 事件环 |
| [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) | 224 | ✅ | 对话中生成交互式可视化卡片 |
| [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) | 101 | ✅ | 划选文字→批注→随消息发送，回复逐条对照 |
| [Liang-Saint-Slider](https://github.com/BruzWJ/Liang-Saint-Slider) | 95 | ✅ | 模型与思考力度选择滑条 |
| [dsh-navbar](https://github.com/vlln/dsh-navbar) | 59 | ✅ | 对话节点导航条：右缘节点串快速跳转（官方 bundle 插件） |

### ⌨️ 终端与桌面端（5）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | 2651 | ✅ | Claude Code 风全屏 TUI：鲸鱼顶栏/流式思考/双击 Esc 回滚 |
| [deepseek-harness-desktop](https://github.com/hairyf/deepseek-harness-desktop) | 1322 | ✅ | Tauri 桌面版：5MB 安装包零环境配置，Win/macOS/Linux |
| [Bigfish](https://github.com/turtle2209/Bigfish) | 302 | 未测 | 第三方桌面端：内置 Node 运行时，双击即用 |
| [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) | 288 | ✅ | 社区发行版：桌面/Web/TUI 三形态统一体验 |
| [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | 244 | 待定 | 自研 ANSI 渲染的极简终端 UI |

### 👁 视觉与多模态（3）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [modlens](https://github.com/liustack/modlens) | 3736 | ✅ | 生态第一个视觉插件，视觉工作流的基准方案 |
| [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | 1011 | ✅ | 内置免费视觉模型路由，给文本 agent 装眼睛 |
| [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | 837 | 需适配 | 带意图图片问答、长截图 OCR、UI 还原 |

### 🤖 Agent 能力与编排（6）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | 1146 | 待定 | 多代理团队编排 |
| [helloagents](https://github.com/hellowind777/helloagents) | 701 | ✅ | agent 能力合集 |
| [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | 635 | ✅ | CMA 兼容开源 agent 运行时，任意模型可驱动 |
| [rea](https://github.com/morluto/rea) | 380 | ✅ | 用 agent 逆向工程任何东西：从应用行为到原生二进制 |
| [open-record-replay](https://github.com/humblebanana/open-record-replay) | 142 | ✅ | macOS 录制回放：把鼠标/键盘/UI 事件存为结构化轨迹供 agent 学习重放 |
| [axern](https://github.com/cofy-x/axern) | 58 | ✅ | AI agent 开源沙箱：不可信代码执行与持久服务 |

### 💻 编码与生产力（4）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [TokenTracker](https://github.com/xiufengsun/TokenTracker) | 1443 | 未测 | 本地优先的 31 种编码工具 token 用量与成本追踪 |
| [claude-paper](https://github.com/alaliqing/claude-paper) | 329 | ✅ | 跨 agent 论文工具箱：速读摘要/深度研读材料/代码演示 + 本地 Web 阅读器 |
| [mobius](https://github.com/nutshellai-tech/mobius) | 286 | ✅ | 编码增强 |
| [dsh-remote](https://github.com/flymysql/dsh-remote) | 39 | ✅ | 多机远程工作区：SSH 连接管理、远程目录→本地镜像→原生工作区收养、SFTP 双向同步与 rw_* 工具族 |

### 🧠 记忆与上下文（2）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [mnemon](https://github.com/mnemon-dev/mnemon) | 534 | ✅ | 跨 agent、本地优先的持久记忆 |
| [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) | 256 | ✅ | 五轨记忆 + git 分支托管 + 后台自我进化 |

### 📡 消息通讯与 IM（4）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-lark](https://github.com/omdsh-dev/dsh-lark) | 47 | ✅ | 飞书 IM bot 频道（官方渠道插件） |
| [dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) | 44 | ✅ | 分支式消息编辑、reroll、重试、多版本 |
| [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) | 34 | 待定 | 跨 DSH 实例消息/事件交接 |
| [ChatCCC](https://github.com/wzj998/ChatCCC) | 22 | ✅ | 飞书/微信聊天控制 DSH / Claude Code |

### 🗂 文件、数据与浏览（4）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-browser](https://github.com/Lum1104/dsh-browser) | 498 | 需适配 | Chrome 侧栏扩展，让 DSH 直接操作浏览器 |
| [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) | 154 | ✅ | OpenPencil 设计稿预览与编辑 |
| [dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) | 53 | ✅ | 增强型持久网页搜索 |
| [dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) | 43 | 待定 | PDF/图片/Office 转结构化 Markdown |

### 🛒 市场与管理（4）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-market](https://github.com/dsh-market/dsh-market) | 2662 | ✅ | 持续收录 1000+ 插件的市场：中文搜索 + 五维评分 |
| [dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) | 67 | ✅ | Web UI 一键管理插件：启停/装卸/环境管理 |
| [dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) | 27 | ✅ | 插件健康检查：清单协议/patch 格式/构建陷阱 |
| [deepseek-plugin-store](https://github.com/Ericwong5021/deepseek-plugin-store) | 25 | ✅ | 独立社区插件商店：发现/安装/提交经验证的插件 |

### 🎮 娱乐生活（5）

| 插件 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [petdex](https://github.com/crafter-station/petdex) | 3986 | ✅ | 生态最高星桌宠图鉴 |
| [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | 1784 | 待定 | 深海鲸鱼养成 |
| [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) | 582 | ✅ | 把 DSH 变回 2005 门户网站：怀旧广告/小游戏/弹窗 |
| [whale-girl](https://github.com/vlln/whale-girl) | 296 | ✅ | QQ 宠物形态桌宠：可拖拽/投喂/玩耍 |
| [dsh-kun-like-pet](https://github.com/liyupi/dsh-kun-like-pet) | 86 | ✅ | 小坤桌宠：随 Agent 工作状态切换 9 种动作 |

> 实测 = 雷达 k8s 运行级判定（✅ 可用 · 待定 · 需适配 · 未测，四档口径见下文）；rc.8 + v4flash 源码路径重测（2026-08-21，50 仓 + 对方清单高星 22 仓）证据见 [data/rc8-retest-20260821/](data/rc8-retest-20260821/) 与 [PLUGINS-ALL.md](PLUGINS-ALL.md)；安装第三方插件前请审查源码并固定 commit。

<!-- AUTO:featured:END -->

## 📦 Bundles

<!-- AUTO:bundles:START -->

> 人工策展 16 个整合包：内测成员作品置顶，其下按预设套件 / 能力合集 / 发行版 / 配方管理器四形态分组，类内按星标排序；星标每 6 小时自动刷新（成员调整请提 PR 修改 data/bundles.json）。数据截至 2026-08-28 19:30（UTC+8）。

### ⭐ 内测成员作品（1）

| 整合包 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [marisa-distro](https://github.com/LoserFox/marisa-distro) | 8 | 未测 | 魔理沙整合发行版（内测成员作品）：DSH 0.1.0-rc.7 + 桌面壳 + 29 个插件 + MyGO 插件市场，Windows MSI/便携版/profile 三形态安装（v0.1.11，Release 带 SHA256 校验） |

### 🎚 预设与配置套件（4）

| 整合包 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | 6922 | ✅ | 注入器 × 思维模式路由套装：免重启运行时注入器 + P1-P23 任务感知推理模式路由（rc.8 实测 ✅） |
| [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | 3783 | ✅ | 两阶段预设：极简模式对齐启动 → 全量装载（rc.8 实测 ✅） |
| [dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset) | 138 | 未测 | Windows 一键「极简模式 Git Bash」预设：把自带极简模式的 bash 调用映射到 Git Bash |
| [dsh-roleplay-preset](https://github.com/oliblue-evan/dsh-roleplay-preset) | 19 | 未测 | 沉浸式角色扮演预设：零工具纯对话、酒馆式演出格式、文件记忆库 |

### 🧩 能力合集（8）

| 整合包 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [Aegis](https://github.com/GanyuanRan/Aegis) | 1139 | ✅ | 软件工程方法论技能包：baseline-first 规划、系统性重构（rc.8 实测 ✅） |
| [helloagents](https://github.com/hellowind777/helloagents) | 701 | ✅ | agent 能力合集（rc.8 实测 ✅） |
| [DeepSec](https://github.com/Unclecheng-li/DeepSec) | 353 | 未测 | AI 安全攻防一体化合集：Android · Web · Native · 协议 · 恶意代码 · AI 六域 |
| [harmony-next.skills](https://github.com/linhay/harmony-next.skills) | 342 | ✅ | 技能驱动的工作流增强（rc.8 实测 ✅） |
| [superpowers-dsh](https://github.com/LayneChai/superpowers-dsh) | 105 | ✅ | TDD/调试/计划等开发技能集（rc.8 实测 ✅） |
| [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) | 89 | 未测 | 完整逆向工程技能合集（85 个 SKILL.md） |
| [dsh-daily-kit](https://github.com/zhouwei713/dsh-daily-kit) | 2 | 未测 | 日常插件集合：16 插件 monorepo + 4 bundle，含 596 单测 |
| [dsh-plugins](https://github.com/MkaliezZ/dsh-plugins) | 0 | 未测 | DSH 插件家族索引：agentfuse / evidence-task-board / test-normalizer 等 16 插件合集（monorepo） |

### 📀 发行版（2）

| 整合包 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [Bigfish](https://github.com/turtle2209/Bigfish) | 302 | 未测 | 第三方桌面端发行版：内置 Node 运行时，双击即用（雷达判需适配——发行版形态非单插件安装） |
| [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) | 288 | 未测 | 社区发行版：桌面/Web/TUI 三形态统一体验 |

### 📑 配方管理器（1）

| 整合包 | ⭐ | 实测 | 说明 |
|---|---:|---|---|
| [dsh-recipe](https://github.com/863683348/dsh-recipe) | 1 | 未测 | 场景配方管理器（插件界的 dotfiles）：列出/搜索/安装插件组合（形态稀缺，豁免星标门槛） |

> 实测口径同精选榜；整合包安装方式以各仓库 README 为准（预设类多为 `dsh plugin add` 后在设置中启用，发行版类需按其自身安装器操作）。

<!-- AUTO:bundles:END -->

## Plugin Catalog

<!-- AUTO:catalog:START -->

Per-plugin details (verdict · location · stars) in **PLUGINS-ALL.md**.

- **🎓 技能包**（24）— OK 6 · incompatible 1 · pending 3 · untested 11 · watching 3 — [details](PLUGINS-ALL.md#-技能包24)
- **🧠 记忆增强**（26）— OK 14 · incompatible 1 · pending 3 · untested 3 · watching 5 — [details](PLUGINS-ALL.md#-记忆增强26)
- **🎨 主题皮肤**（15）— OK 6 · incompatible 0 · pending 2 · untested 5 · watching 2 — [details](PLUGINS-ALL.md#-主题皮肤15)
- **🛒 市场与管理**（176）— OK 74 · incompatible 15 · pending 12 · untested 7 · watching 68 — [details](PLUGINS-ALL.md#-市场与管理176)
- **🔌 Web UI 增强**（1521）— OK 846 · incompatible 264 · pending 143 · untested 21 · watching 247 — [details](PLUGINS-ALL.md#-web-ui-增强1521)
- **💻 编码开发**（1165）— OK 606 · incompatible 210 · pending 127 · untested 20 · watching 202 — [details](PLUGINS-ALL.md#-编码开发1165)
- **🤖 Agent 能力**（974）— OK 444 · incompatible 166 · pending 106 · untested 12 · watching 246 — [details](PLUGINS-ALL.md#-agent-能力974)
- **📡 消息通讯**（389）— OK 162 · incompatible 84 · pending 36 · untested 3 · watching 104 — [details](PLUGINS-ALL.md#-消息通讯389)
- **🗂 文件数据**（322）— OK 148 · incompatible 58 · pending 37 · untested 9 · watching 70 — [details](PLUGINS-ALL.md#-文件数据322)
- **🎮 娱乐生活**（204）— OK 100 · incompatible 16 · pending 22 · untested 0 · watching 66 — [details](PLUGINS-ALL.md#-娱乐生活204)
- **🛠 基建部署**（760）— OK 309 · incompatible 95 · pending 105 · untested 3 · watching 248 — [details](PLUGINS-ALL.md#-基建部署760)
- **📚 学习研究**（73）— OK 22 · incompatible 5 · pending 3 · untested 2 · watching 41 — [details](PLUGINS-ALL.md#-学习研究73)
- **❓ 其他**（2401）— OK 757 · incompatible 215 · pending 153 · untested 21 · watching 1255 — [details](PLUGINS-ALL.md#-其他2401)

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
> **Test version**: dsh (in-container agent) driven by Qwen3.6-35B (via the de-stream proxy) · k8s, 5 shards · each run is anchored by the snapshot `run_id` (currently `20260828T203001Z`). The DSH npm version is not recorded per snapshot — cross-check via run_id and the `reports/agent-test/` dates.
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
| `docs/radar/` | Radar overview, architecture, and data contracts (incl. open-source roadmap) |
| `docs/CATALOGING.md` | Plugin taxonomy (kept in sync with `scripts/classify.py`) |
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
> 渲染于快照 20260828T203001Z（2026-08-29 04:30 UTC+8）· 数据源 data/snapshots/（渲染即对齐）

| 证据层 | 当前结果 |
|---|---:|
| 自动收录 全量索引 2943 · 收录（克隆验证）2996 · 当前版本（0.1.1-rc.2）已测 345 个仓库 |
| 运行级实测 | 6560 可用 · 2159 不兼容 · 1028 待定（共 9747 个，k8s agent 口径）|

[完整索引](PLUGINS-ALL.md) · [运行实测](reports/2026-08-27/agent-test-v2.md)

<!-- AUTO:ecosystem:END -->

<!-- AUTO:ecosystem:END -->

The snapshot only answers "what does today's evidence say" — the front page never copies hundreds of repo rows and change logs. Per-repo verdicts, failure reasons, daily additions, and open PRs live in the dated reports.

## Boundaries & Credits

This repo maintains the catalog, detection rules, and evidence reports — it does not host third-party plugin code. Thanks to every contributor who submitted plugins, reproduced issues, corrected metadata, and kept the test pipeline alive.

This repository's catalog content and scripts are available under the [MIT License](LICENSE); third-party plugins remain governed by the licenses declared in their own repositories.

Huge thanks to everyone who joined the beta test — the group photo shows only part of the list, and many more friends contributed along the way!

![DSH beta group photo](assets/dsh-miji-heying.png)

Let's keep deep diving!
