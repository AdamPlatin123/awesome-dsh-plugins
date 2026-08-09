# SOP：DSH 生态情报自动化（拉取 → 构建 → 部署 → 比对 → 报告 → 推送）

> 适用：dsh-external-research 监控链路 · 远程主机 10.144.144.9 · 更新日期 2026-08-10
> 目标：对快速迭代的 deepseek-harness 与 org 插件生态，自动拉取最新内容、构建验证、部署实例、比对兼容性、产出报告，全链路无人值守。

## 1. 流程总览

```text
[触发器] cron 02:00/10:00/18:00 + post-merge hook（人工推送监控 repo）
    ↓
cron-check.sh（总调度）
    ├─ 1. git pull 自身（同步最新脚本/配置）
    ├─ 2. 动态发现 org 新仓库（gh api）→ .scope-current.txt
    ├─ 3. 检测 mainline 最新快照 + 各仓 HEAD（.cron-state.json）
    ├─ 4. 有变化/--full → compare-mainline.sh 四维比对 → reports/<日期>/
    ├─ 4.5 --full 时 → build-mainline.sh（后台异步）
    │        ├─ 拉取最新快照到 .mainline-build/
    │        ├─ pnpm install（--frozen-lockfile）
    │        ├─ pnpm run build
    │        ├─ 自动部署：软链 ~/.local/bin/dsh → 构建产物（验证 --version）
    │        └─ 报告 reports/<日期>/mainline-build.md（install/build/部署状态）
    ├─ 5. commit + push（报告/CHANGELOG/状态）
    └─ 6. update-readme.sh → README 仪表盘（指标/新增修改/需适配/PR）
```

## 2. 触发器定义

| 触发器 | 时间/条件 | 行为 |
|---|---|---|
| cron 全量班 | 每日 02:00 | `cron-check.sh --full`：全量索引 + 自动构建 |
| cron 增量班 | 每日 10:00 / 18:00 | 仅索引有变化的仓库 |
| post-merge hook | 人工推送监控 repo（作者非 bot） | 自动触发 `--full` 全量 + 构建 |
| 手动 | `bash -lc 'cd /home/adam/dsh-external-research && ./scripts/cron-check.sh [--full]'` | 任意时刻 |

## 3. 各环节标准操作

### 3.1 拉取最新内容
- **mainline**：`git ls-remote ... "refs/heads/snapshots/*"` 取最新快照 → clone/fetch 到 `.mainline/`（比对用）与 `.mainline-build/`（构建用）
- **org 仓库**：逐仓 `ls-remote HEAD` 对比 `.cron-state.json` → 变化仓 fetch 到 `.clones/`

### 3.2 构建最新 mainline（build-mainline.sh）
```bash
./scripts/build-mainline.sh          # 全流程（拉取+install+build+部署+报告）
SKIP_BUILD=1 ./scripts/build-mainline.sh  # 跳过构建（不部署）
```
- install 失败 → 报告 ❌ + 错误摘要；build 失败 → 同上
- **成功 → 自动部署**：`ln -sfn .mainline-build/apps/cli/lib/bin.js ~/.local/bin/dsh`，验证 `dsh --version`
- 报告：`reports/<日期>/mainline-build.md`（快照/耗时/install rc/build rc/部署状态/错误摘要）

### 3.3 比对兼容性（compare-mainline.sh）
四维：补丁 `git apply --check --3way` / seam 符号 `git grep` / peerDeps / 锚定
输出：`reports/<日期>/mainline-compat.md`（矩阵 + 双方建议 + mainline 变更分析）+ 逐仓详情 + index

### 3.4 报告与推送
- 报告、CHANGELOG、README 仪表盘随 cron 提交，`dsh-ecosystem-bot` 身份推送到 org 仓库
- 构建报告由下一轮 cron 随报告提交（异步不阻塞）

## 4. 故障处理

| 故障 | 表现 | 处理 |
|---|---|---|
| TLS/网络失败 | 引擎退出码 3 | 检查 xray 代理（`ps aux \| grep [x]ray`）；git 走 per-URL proxy 已配；下轮 cron 自动重试 |
| 引擎退出码 >1 | 本轮不 commit 不推进状态 | 查看 `logs/cron-<日期>.log` 尾部错误；修复后手动重跑 |
| 构建失败 | mainline-build.md ❌ | 查 `logs/build-install.log` / `build-build.log`；上游问题提 issue |
| 状态文件 mv 失败 | .cron-state.json 滞后 | 确认无 `.tmp` 残留；增量轮网络中断所致，下轮修复 |
| hook 未触发 | 推送后无索引 | 查 `cat /tmp/hook-full.log`；作者是否为 bot（bot 提交不触发，属正常） |
| 并发冲突 | 两轮 cron 重叠 | flock 已防护（/tmp/dsh-hook-full.lock）；确认 crontab 排班 |

## 5. 验证清单（每次变更后）

- [ ] `bash -n scripts/*.sh` 全部通过
- [ ] `./scripts/compare-mainline.sh --scope <小仓> --dry-run` 只读验证
- [ ] 远程同步：`git pull dsh-ext main` 后 HEAD 一致
- [ ] README 仪表盘数字与最新报告一致（无需适配+需适配+已删除+未知=总数）
- [ ] 构建：`reports/<日期>/mainline-build.md` 存在且状态 ✅
- [ ] 部署：`~/.local/bin/dsh --version` 可运行

## 6. 关键路径

| 项 | 位置 |
|---|---|
| 总调度 | `scripts/cron-check.sh` |
| 兼容引擎 | `scripts/compare-mainline.sh` |
| 构建+部署 | `scripts/build-mainline.sh` |
| README 渲染 | `scripts/update-readme.sh` |
| 目录/ref 检查 | `scripts/check-ref-lag.sh` · `scripts/check-placeholders.sh` |
| DSH skill 入口 | `.agents/skills/mainline-compat/SKILL.md` |
| 日志 | `logs/cron-<日期>.log` · `logs/build*.log` |
| 状态文件 | `.cron-state.json` · `.mainline-state.json` · `.last-changes.json`（均 gitignore） |
| 部署实例 | `~/.local/bin/dsh` → `.mainline-build/apps/cli/lib/bin.js` |
