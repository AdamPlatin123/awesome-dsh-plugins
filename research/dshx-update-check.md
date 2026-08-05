# dshx-update-check 调研摘要

## 一句话定位

`dshx-update-check` 是 dsh-external/marisa#1 提案的「可跑原型」：用 commit SHA 对比检测已安装的外部插件是否有新版，**只检测、不自动更新**，更新命令打印出来由人工执行。

## 技术栈与依赖

- 纯 Node.js ESM（`"type": "module"`），**零运行时依赖**（`package.json` 无 `dependencies`）。
- 仅用 Node 内置：`node:child_process` 的 `execFileSync`、`node:fs`、`node:path`。
- 外部命令依赖：`git`（读本地 SHA / origin remote）、`gh` CLI（取 GitHub 默认分支 HEAD、compare 接口）；`sh -c 'command -v dsh'`（定位 checkout）。
- `package.json` 关键字段：`"name": "@dsh-external/dshx-update-check"`、`"version": "0.1.0"`、`"bin": { "dshx-update-check": "./bin/dshx-update-check.mjs" }`、`"license": "MIT"`。

## 文件结构概览

```
dshx-update-check/
├── README.md                       1.9KB  说明用法/原理/已知边界
├── package.json                    282B   零依赖，仅声明 bin
└── bin/
    └── dshx-update-check.mjs       4.5KB  全部逻辑，单文件
```

## 核心功能与实现要点

1. **定位 dsh 活动 checkout**（`bin/dshx-update-check.mjs:18-29`）：优先读 `DSH_CHECKOUT` 环境变量；否则解析 PATH 上的 `dsh` 启动器符号链接链（`readlinkSync` 逐级解引用），取其 `dirname(dirname(target))`，并校验 `<checkout>/packages` 存在——思路与 marisa 一致。

2. **枚举已安装外部插件**（`bin/dshx-update-check.mjs:67-75`）：扫描 `<checkout>/.external-plugins/` 目录，过滤隐藏项；目录不存在或为空时给提示并优雅退出。

3. **本地指纹来源**（`bin/dshx-update-check.mjs:88-92`）：依赖 `dshx install` 从 git 安装时整仓浅克隆后整体拷贝、保留了 `.git`，因此 `git -C <插件目录> rev-parse HEAD` 即本地 SHA；非 git 安装（本地目录/tgz）诚实报「❓ 无法判断」，不猜。

4. **远端指纹来源**（`bin/dshx-update-check.mjs:39-55`、`81-86`）：先用 `git remote get-url origin` 配合正则 `github\.com[/:]([^/]+)/([^/]+?)(?:\.git)?$` 推出 owner/repo；再 `gh api repos/:o/:r` 取 `default_branch`，`gh api repos/:o/:r/commits/:branch` 取 HEAD sha；非 GitHub 来源或 gh 未登录/无权限都归入「无法判断」。

5. **轻量 changelog**（`bin/dshx-update-check.mjs:57-63`、`102-105`）：落后时调 `gh api repos/:o/:r/compare/<local>...<remote> --jq '.commits[].commit.message'`，按 `\n\n` 拆段、取每段首行，最多列 5 条；取不到就空数组（不阻断）。

6. **刻意分离检测与更新**（`bin/dshx-update-check.mjs:106-111`、README）：发现落后时只打印 `⬆️ 可更新：本地 xxx → 远端 yyy (branch)` 加 commit 摘要，并给出 `更新（人工执行）: dshx install <id> <url>` 提示，**绝不自动执行**；末尾汇总「N 个可更新 / M 个无法判断 / 其余最新」。

7. **输出形态**：纯 stdout 文本，三态符号 `✅/⬆️/❓`，无 exit code 区分（除早期 `process.exit(0)`）。

## 与 DeepSeek Harness 主仓库的集成点

- **定位 seam**：与 marisa 同一约定——通过 `dsh` 启动器符号链接链回溯到活动 checkout 根（`packages/` 为探测锚点）；可被 `DSH_CHECKOUT` 环境变量覆盖。本工具是**消费者**，不修改 checkout。
- **数据来源 seam**：直接读 `<checkout>/.external-plugins/<plugin-id>/.git`，依赖 `dshx install`（来自 marisa/dshx 工具链）从 git 安装时**保留 `.git` 目录**这一实现细节——README 在「已知边界」明确警告：若未来 marisa 改为不保留 `.git`，本工具退化为全部「无法判断」，届时需要提案里的 lockfile 方案。
- **更新动作 seam**：仅打印 `dshx install <id> <url>` 命令（即 marisa 提供的安装器），由人执行；本仓库不含任何写入/安装逻辑。
- **鉴权依赖**：通过已登录的 `gh` CLI 访问 dsh-external 组织的（可能私有的）GitHub 仓库 API；不自带 token 管理。
- **提案追溯**：直接对应 `dsh-external/marisa` issue #1 的「路线 B：commit SHA 对比」，是提案的可执行论证原型而非生产组件。

## 亮点与风险

**亮点**

- 零依赖、单文件、约 130 行，作为提案验证原型极为精简；`README.md` 把「为什么不需要 lockfile」「为什么不自动更新」都讲清楚了，可读性高。
- 失败路径诚实：非 git 安装、非 GitHub origin、gh 未登录/无权限统统归入「❓ 无法判断」而非抛错或误报（`bin/dshx-update-check.mjs:43-47、82-86、94-97`）。
- 与 marisa 共用 checkout 定位算法，集成面一致。

**风险**

- **强耦合 marisa 的实现细节**：依赖 `.external-plugins/<id>/.git` 保留；marisa 一旦改安装方式即整体失效（README 已自认）。
- **无测试、无 CI、无 lockfile 兜底**：原型定位，作者明确说「当原型读不当产品用」。
- **正则解析 origin URL**（`bin/dshx-update-check.mjs:43`）：仅匹配 `github.com[/:]owner/repo`，不支持其它 Git 托管（GitLab/Gitea 等），全归「无法判断」。
- **`execFileSync` 同步阻塞**：逐插件串行调 `gh api`（每插件至少 2 次请求 + 落后时再 1 次 compare），插件多了会慢；无并发、无缓存。
- **无退出码语义**：有可更新也返回 0，无法被脚本/CI 直接判定状态。
- **依赖外部环境**：`dsh` 在 PATH、`gh` 已登录、网络可达 GitHub，三者缺一即大面积退化为「无法判断」。

## 维护状态

- 仓库仅 **1 个 commit**（`54f41e0`，2026-08-04，作者 Jack），处于「提案原型一次性提交」状态。
- 版本号 `0.1.0`，README 自述「当原型读不当产品用」，未见后续迭代痕迹。
- 无 Issues/PR/CI/测试痕迹（仅本仓自身，未查 GitHub Issues 页面——如需可后续 `gh api` 补查）。

## 备注

- 调研方式：`git clone --depth 1` 成功；本地无 `.external-plugins` 故无法实跑，但脚本逻辑、README、package.json 三处自洽，结论可信。
- 与第一轮调研中的 marisa 仓库强相关：本仓是 marisa#1 提案的「路线 B」原型，可与其摘要对照阅读。
- 脱敏：作者署名仅「Jack」（GitHub 仓内可见），未出现邮箱/真实姓名。
