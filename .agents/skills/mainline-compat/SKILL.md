---
name: mainline-compat
description: 运行 dsh-external 生态与当日 mainline 快照的兼容性对比引擎（scripts/compare-mainline.sh）：拉取 dsh2026/test-AdamPlatin123 最新快照分支，对比 15 个生态仓库的锚定/补丁/seam/peerDeps 四个维度，输出 mainline 自身变更分析与双方适配建议，并更新 CHANGELOG、reports/latest 软链与状态文件。当用户要求 mainline 对比、生态兼容性检查、接口差异分析、兼容性报告、或提到"对比当日 mainline""插件与主仓库接口是否兼容""生成兼容性报告"时使用；也用于按日期重新生成对比报告。
---

# mainline-compat — 生态与当日 mainline 的兼容性对比

## 目标

对 `dsh-external` 组织 15 个仓库，自动对比它们与**当日 mainline**（`github.com/dsh2026/test-AdamPlatin123` 最新快照分支）的接口差异，判定每个仓库是否可继续在当日 mainline 上集成，并分别给插件侧与主仓库侧提出适配建议。产出按日期分立的报告，`CHANGELOG.md` 为主更新视图。

## 前置与约束

- 引擎：`scripts/compare-mainline.sh`（bash，零第三方依赖：bash/git/gh/jq）。依赖缺失 → exit 2；网络不可达 → exit 3。
- 内容 **private**：报告不复制 issue 正文、真实密钥值、成员昵称（脱敏规则同 `AGENTS.md`）。
- 只读资产不触碰：`research/`、`context/`、`cross-analysis/`、`plan/`、`README.md`。
- 自动执行（发布 issue / 写修复）默认关闭，必须逐项人工确认。

## 工作流（7 步）

1. **索引**：从 `research/<name>.md` 的「与 DeepSeek Harness 主仓库的集成点」节读取集成点摘要；从 `.clones/<name>/` 提取证据——`patches/` 目录与补丁文件、README 中的 40 位 commit 与 `snapshot-*` 引用、`package.json` 中 `peerDependencies`/`dependencies` 的 `dsh-*` 范围。
2. **拉取 mainline**：`.mainline/` 缓存（blob:none clone，chmod 700）fetch `dsh2026/test-AdamPlatin123` 全部 `snapshots/*` 分支，取**最新快照分支**为当日 mainline（`MAINLINE_COMMIT`）。
3. **对比四维**（每仓库）：
   - ① 锚定：仓库锚定 commit/标签 vs 当日 mainline（对齐 / 落后 / 超前 / 未知——快照与 master 不同谱系时如实标注）；
   - ② 补丁：`patches/*.patch` 在 `.mainline/` 上 `git apply --check --3way`（OK / CONFLICT / 缺文件 / 无补丁——无 `patches/` 目录的仓库按 README 说明标注）；
   - ③ seam 符号：`ThemeService` / `settingsNamespace` / `sessionProjections` / `tuiPrompt` / `slots` / `session/event` 在 `.mainline/packages/` 的存在性（缺失面只在与仓库集成点相关时计入判定）；
   - ④ peerDeps：`dsh-*` 依赖范围 vs mainline workspace 实际版本（`.mainline/packages/*/*/package.json`）。
4. **mainline 变更分析**：`git diff --stat` 上次记录 commit → 当日（首次无状态时用 `--base`，默认 `cab66cd`），输出删除/新增包、seam 符号变化、破坏性变更清单与 ≥3 条关键变更（如 TUI 移除、WebSocket 下行通道新增）。
5. **生成报告**：`reports/<date>/mainline-compat.md`（15 仓库兼容性矩阵 + 插件侧建议 ≥15 条 + 主仓库侧建议 ≥3 条 + mainline 变更分析节）、`reports/<date>/<name>.md` × 15（各仓库详情，头部相对链接 `research/<name>.md`）、`reports/<date>/index.md`（当日索引）。
6. **更新**：`reports/latest` 软链 → 当日日期；`CHANGELOG.md` 顶部插入当日条目（格式见 `AGENTS.md` 第 3 节）；写 `.mainline-state.json`（lastMainlineCommit / lastDate / repos 状态）。
7. **可选自动执行**（默认关闭）：`--publish-issues` 解析 `actions/org-issues.md` 草稿（默认仅打印将发布清单，实际发布逐条确认后 `gh issue create`）；`--apply-fix` 输出待改 diff（如 catalog ref 滞后），实际写须逐项确认。

## 自动化边界（重要）

- `--publish-issues` 与 `--apply-fix` **默认关闭**；未传标志时引擎绝不写远程、不改任何文件（含本地 clone）。
- 传标志但**非交互**（stdin 非 tty）时，逐项确认自动跳过（只打印清单/diff），绝不静默执行。
- `--dry-run` 全程只读：不写报告 / CHANGELOG / 状态 / 软链；缓存（`.mainline/`、`.clones/`）走临时目录，结束即删。
- 实际发布 issue 是**写远程**动作：每次运行前向用户说明将创建哪些 issue，逐条获得确认。

## 运行命令示例

```sh
# 1) 完整对比（当日），生成报告并更新 CHANGELOG / 软链 / 状态
bash /mnt/shared/_Projects/dsh-external-research/scripts/compare-mainline.sh

# 2) 只读预演：验证网络、克隆、判定，不落盘任何产物
bash /mnt/shared/_Projects/dsh-external-research/scripts/compare-mainline.sh --dry-run

# 3) 限定仓库范围（每行一个仓库名，# 注释）
bash /mnt/shared/_Projects/dsh-external-research/scripts/compare-mainline.sh --scope /tmp/scope.txt

# 4) 指定日期目录与首次对比基线
bash /mnt/shared/_Projects/dsh-external-research/scripts/compare-mainline.sh --date 2026-08-05 --base cab66cd

# 5) 查看将发布的 issue 草稿（不写远程）
bash /mnt/shared/_Projects/dsh-external-research/scripts/compare-mainline.sh --publish-issues --dry-run

# 6) 查看待修 diff（如 toybox/skins catalog ref 滞后），不写入
bash /mnt/shared/_Projects/dsh-external-research/scripts/compare-mainline.sh --apply-fix --dry-run
```

退出码：`0` 全部兼容；`1` 存在需适配（含 mainline 破坏性变更）；`2` 脚本错误；`3` 离线。

## 产出核对清单

- `reports/<date>/` 存在且含 `mainline-compat.md` + 15 个 `<repo>.md` + `index.md`；`reports/latest` 软链指向 `<date>`。
- `CHANGELOG.md` 顶部为当日条目，报告链接为相对路径可点击直达。
- `.mainline-state.json` 已写入；下次运行以上次 commit 为对比基线。
- 报告无 issue 正文复制、无真实密钥值、无成员昵称；矩阵/建议/变更分析三节齐备。
