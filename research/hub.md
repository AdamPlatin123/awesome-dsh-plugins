# hub 调研摘要

## 一句话定位

`dsh-external/hub` 是 dsh-external 组织（DeepSeek Harness 内测生态）的**组织级索引/目录仓库**：一个零依赖的 Node.js 生成器每隔 2 小时从 GitHub API 抓取所有组织仓库的实时元数据，与人工维护的分类源合并，自动产出机器可读的 `catalog.json`、`plugins.json`（Marisa/dshx 消费）和人类可读的 `README.md`——它本身不是插件，而是整个生态的「事实源目录」。

## 技术栈与依赖

- **运行时**：Node.js（ESM，`import` 语法，`node:` 内置模块），无任何 npm 依赖（`package.json` 不存在；纯 `node:fs/promises` + `node:path` + `node:url` + 全局 `fetch`）
- **GitHub API**：REST v3（`api.github.com`，`Accept: application/vnd.github+json`，`X-GitHub-Api-Version: 2022-11-28`），通过 `GH_TOKEN` 环境变量认证（需可读组织私有仓库）
- **shell**：`bash`（`set -euo pipefail`），依赖 `git` / `gh` / `date`
- **数据格式**：JSON（自定义 schema：`dsh-external-hub/v0.1` 目录、`dsh-external-hub-source/v0.1` 源、各集合仓库自带 `catalog.json` 的多种 schema 透传不重写）
- **无构建系统、无测试、无 CI**（CI 已移除，见「风险」）

## 文件结构概览

```
hub/
├── README.md             # 18.9KB — 人类可读索引（自动生成，state 即文档）
├── LOOP.md               # 5.3KB  — 循环工程运行手册（同步 Loop / Triage / 安全门禁）
├── catalog.source.json   # 9.7KB  — 唯一人工输入：分类/标签/备注/managers 覆盖
├── catalog.json          # 42.2KB — 自动生成：统一机器可读索引（含聚合集合条目）
├── plugins.json          # 12.5KB — 自动生成：Marisa/dshx A 方案消费的插件清单
└── scripts/
    ├── generate.mjs      # 17.1KB — 生成器主体（~400 行，纯 Node ESM）
    └── sync.sh           # 588B   — 一键同步：生成 → diff → 提交 → 推送
```

## 核心功能与实现要点

1. **目录生成器**（`scripts/generate.mjs:1-300`）：单文件 ESM 脚本，分六阶段——抓组织仓库+根目录扫描 → 聚合各仓库 catalog.json → 汇总统计 → 产 `catalog.json` → 产 `plugins.json` → 产 `README.md`。生成器**只读 GitHub API + 写三个产物文件**，绝不改写 `catalog.source.json`。

2. **空仓库 / 清单检测**（`generate.mjs` `mapPool` 回调内）：对每个仓库调 `/repos/{org}/{repo}/contents/` 扫根目录，识别 `dsh.plugin.json` / `package.json` / `SKILL.md` / `catalog.json`，并判定空仓库。**实时检测优先**，人工 `empty` 标记仅在仓库无真实清单时生效（注释明确提及曾因陈旧标记踩坑：`dsh-opencode-server`）。

3. **管理器兼容性推导**（`generate.mjs` `deriveManagers`）：人工 `managers` 字段优先；缺省时按根目录清单推导——`dsh.plugin.json` → `marisa+registry`；纯 `package.json` → `marisa+cordis`；`SKILL.md` → `skill`。仅对 `plugin` / `channel` 类有意义。

4. **集合聚合**（`generate.mjs` 第 2 阶段）：抓取 `toybox` / `dsh-skins` / `dsh-github-integration` 等仓库自带的 `catalog.json`，**透传不重写**（各仓库 schema 不统一，如 `toybox-index/v0.1`），并入 README「插件集内条目」段与 `catalog.json` 的 `collections` 字段；集合内条目不断言管理器兼容性（其 `source` 形如 `github:#path` 不在 marisa 安装器支持的三类来源内）。

5. **并发与重试**（`generate.mjs` `api` + `mapPool`）：`mapPool` 限 12 并发避免打爆 HTTP 代理（注释提及曾出现 `ECONNRESET` TLS 风暴）；`api()` 对 5xx/429/瞬时网络错误（`fetch failed|ECONNRESET|ETIMEDOUT|...`）退避重试至多 3 次（300ms×attempt），4xx 直接抛出 fail-loud。

6. **噪音抑制提交**（`generate.mjs` `writeIfChanged` + `normalizeForCompare`）：写文件前先归一化比对——把生成时间戳（README 头部行、catalog.json 的 `generated` 字段）替换为 `<TS>` 占位，避免每次运行都产生纯时间戳 diff；`sync.sh` 再用 `git diff --quiet` 判断无变化则跳过提交。

7. **自动化同步 Loop**（`scripts/sync.sh` + `LOOP.md`）：本地 Agent Loop 每 2 小时调 `sync.sh`——`GH_TOKEN=$(gh auth token) node scripts/generate.mjs` → 有变化则 `git add` + `git commit -m "chore: 同步 hub 索引（UTC 时间戳）"` + `git push`。生成物即状态，git log 即运行历史（无后台常驻进程，kill switch = 停跑 sync.sh）。

8. **分类 Triage 半自动**（`catalog.source.json` + `LOOP.md` L2 Loop）：未分类仓库会被生成器强制暴露为告警并进 README「未分类」段，触发人工/Agent 在 `catalog.source.json` 的 `repos[]` 补 `name` + `category`（可选 `note`/`tags`/`managers`/`empty`）；分类是语义事实，生成器永不写源文件。当前 6 大类：单插件（28）/ 插件集（7）/ 远程渠道（5）/ 基础设施（12）/ 研究（1）/ 社区（3），共 56 仓库（5 空）。

## 与 DeepSeek Harness 主仓库的集成点

- **不是补丁式集成**：hub 是**独立工具/元仓库**，不打补丁、不修改 DSH 主仓库源码，而是作为**目录层 seam** 把整个 dsh-external 组织的仓库聚合给消费方。
- **下游消费者**：`plugins.json`（A 方案格式）由 [marisa](https://github.com/dsh-external/marisa) 外部插件管理器（dshx）和 [plugin-registry](https://github.com/dsh-external/plugin-registry) 本地插件系统消费——`dshx install <id> <git-url>` 或设置页「插件」面板据此浏览/安装；离线时 `plugins.json` 兜底目录。
- **上游输入**：`catalog.source.json` 由维护者手工维护，是分类/标签/managers 覆盖的唯一事实源；生成器只读它+GitHub API。
- **协议契约**：自定义 schema `dsh-external-hub/v0.1`（catalog）与 `dsh-external-hub-source/v0.1`（source）；下游若改 schema 需同步本仓库。
- **认证 seam**：`GH_TOKEN` 需 PAT/gh token 且能读组织私有仓库（组织内多数仓库私有），是访问控制的关键点。

## 亮点与风险

**亮点**

- **零依赖纯 Node ESM**（`scripts/generate.mjs:1`）：仅用 `node:fs/promises`、`node:path`、`node:url` 和全局 `fetch`，无 `package.json`、无 `node_modules`，部署仅需 Node 18+。
- **生成物即状态、git log 即历史**的循环工程范本：`LOOP.md` 完整记录同步 Loop（L1 自动+提交）/ Triage（L2 辅助）/ 集合聚合（L1 自动）/ 安全门禁（绝不碰源文件）/ kill switch，是「文档即运行依据」的实践。
- **噪音抑制与 fail-loud 并存**：`writeIfChanged` + `normalizeForCompare`（`generate.mjs`）消除时间戳 diff 噪音；`api()` 对非 2xx 抛错中止，绝不产出陈旧索引。
- **关注点分离干净**：人工语义（`catalog.source.json`）↔ 自动元数据（GitHub API）↔ 三个产物（catalog/plugins/README），三者职责清晰、生成器单向流动。

**风险**

- **Token 安全 seam**（`scripts/sync.sh:7`、`generate.mjs` `headers`）：`GH_TOKEN=$(gh auth token)` 需私有仓库读权限的 PAT/gh token，泄露即等于暴露整个组织私有仓库元数据；CI 已移除，注释提到曾因 `secrets` 不可用于 `if` 条件导致 workflow 校验失败（`LOOP.md` 「Automation status」「Safety & Gates」段），恢复 CI 需 env 中转写法 + `DSH_HUB_PAT` secret。
- **schema 单点自定义**（`catalog.source.json:1` `dsh-external-hub-source/v0.1`、`catalog.json` `dsh-external-hub/v0.1`）：下游（marisa/plugin-registry）若改插件清单格式，需双向同步；目前无版本协商机制。
- **集合 schema 透传不重写**（`generate.mjs` 第 2 阶段注释）：各仓库 catalog schema 不统一（`toybox-index/v0.1` 等），聚合只透传，集合内条目 `source` 形如 `github:#path` 不在 marisa 安装器支持的目录/tgz/git-url 三类来源内——安装路径靠各仓库 catalog.json 自述，存在可发现性 gap。
- **组织私有可见性耦合**：56 仓库中多数私有，索引对组织可见性/token scope 强耦合；token 失效或组织调整会直接破坏索引完整性（生成器 fail-loud 至少不会静默错误）。
- **并发/代理脆弱性**（`generate.mjs` `mapPool` 限 12 并发）：注释明确提及曾出现代理 TLS 连接风暴（`ECONNRESET`），虽已重试兜底，但运行环境网络稳定性是隐性依赖。

## 维护状态

**极其活跃**。README 头部生成时间戳为 `2026-08-05T14:50:53.416Z`（调研当日）；多数仓库「最近更新」列集中在 2026-08-04 ~ 2026-08-05；自动化 Loop 每 2 小时刷新（本地 Agent Loop 驱动）。`LOOP.md` 的「Evolution」段记录组织仓库数在会话期内已新增 4 个，频次与告警策略随规模演进。维护模式：**生成器自动 + 人工维护 `catalog.source.json` 分类**，半自动 Triage 是下一步候选。

## 备注

- 本仓库是 dsh-external 组织的**目录元仓库**，调研其他 dsh-external 仓库时，本 hub 的 `catalog.json` / `catalog.source.json` 是「先看哪里」的入口（含分类、标签、备注、管理器兼容性、空仓库标记）。
- 与本批次调研任务的关系：本 hub 即第一轮/本轮超级调研的组织背景——`catalog.source.json` 中已为 56 仓库给出了人工分类与一句话备注，可作为各 scout 调研的对照基线（注意其备注是仓库自述/维护者标注，非深度调研）。
- 关键产物 `catalog.json` 顶层结构：`schema` / `hub` / `generated` / `stats{repos,empty,collectionPlugins,categories}` / `categories{id→{title,emoji,order}}` / `repos[...]`（每个含 name/url/cloneUrl/description/topics/language/pushedAt/empty/manifest/skill/category/tags/note/managers） / `collections{repoName→{schema,updated,plugins[]}}`。
- 关键产物 `plugins.json` 结构：`{plugins:[{id,source(description,managers}]}`，`id` 形如 `repoName` 或 `collectionRepo/pluginId`（如 `toybox/code-archaeologist`）。
- 安全：本调研为只读 `git clone --depth 1`，未触发任何写操作；摘要已脱敏（无作者邮箱/真实姓名，仅保留 GitHub 用户名/组织名）。
