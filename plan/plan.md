# dsh-external 生态情报 repo：auto mainline 对比引擎（计划 v6）

> 计划状态：DRAFT v6（v5 + 用户 B 调整：CHANGELOG 主视图、日期文件夹分立、软链接、点击直达）
> 计划日期：2026-08-05
> 目标仓库：`/mnt/shared/_Projects/dsh-external-research/`（private；若推远程仅 private 仓库）
> mainline 定义：`github.com/dsh2026/test-AdamPlatin123` 最新快照分支（当前 HEAD=02d7555）

## 1. 用户意图与约束

> "auto 索引-调研和对比当日 mainline 的 repo，调研其与当日 mainline 接口差异，提示或建议双方开发者的 repo 开发是否可行"
> 约束：内容 **private**；以 **DSH 作为基座**（贡献物 = DSH skill）
> B 调整：①对比范围可配置 ②mainline 自身变更分析 ③skill 自动执行能力（批准后）④**显示以主 CHANGELOG 为主更新，各 repo 按日期文件夹分立，相关文件软链接，点击直接进入**

## 2. 现状盘点（保留）

```
README.md / research/*.md（15 摘要）/ context/session-019fc8ab-summary.md / cross-analysis/summary.md
```

## 3. 仓库结构与更新视图（v6 核心变更）

```
dsh-external-research/
├── README.md                    # 项目说明 + 快速导航（链接到 CHANGELOG 与最新报告）
├── CHANGELOG.md                 # ★主更新视图：按日期倒序的每日条目（mainline 变更 + 生态兼容状态 + 报告链接）
├── reports/                     # 按日期文件夹分立的报告
│   ├── latest -> 2026-08-05     # ★软链接：始终指向最新日期文件夹
│   ├── 2026-08-05/              # 当日文件夹（引擎自动生成）
│   │   ├── mainline-compat.md   #   当日主报告：兼容性矩阵 + 双方建议 + mainline 变更分析
│   │   ├── <repo>.md × 15       #   各 repo 当日对比详情（自动生成）
│   │   └── index.md             #   当日索引（链接全部 repo 详情 + 相关资产）
│   └── 2026-08-04/              # 基线文件夹（首次运行生成 0804 基线对比）
├── research/                    # 15 份静态摘要（原始资产，不变）
├── context/  cross-analysis/  analysis/  actions/
├── .agents/skills/mainline-compat/   # DSH skill（工作流 + 支撑脚本）
└── AGENTS.md / .gitignore
```

**软链接与点击直达**：
- `reports/latest -> <最新日期>`：符号链接，随时指向最新报告（README/CHANGELOG 顶部"最新报告"即指此）
- CHANGELOG 每条目的链接直接进入 `reports/<date>/mainline-compat.md` 与当日 index.md；index.md 列出 15 个 repo 详情链接
- 日期文件夹内 `<repo>.md` 头部软链引用 `research/<repo>.md`（一行说明 + 相对路径链接），避免静态摘要重复维护；软链用符号链接形式（`ln -s ../../research/<repo>.md`）或在文档内以链接呈现（markdown 相对链接在 GitHub 上可直接点击进入，本地 git 查看同样有效）——采用 **markdown 相对链接**为主（跨平台可靠），CHANGELOG/README/index 全部点击直达

**CHANGELOG 条目格式**（DSH CHANGELOG 风格，引擎每次运行自动追加）：
```markdown
## 2026-08-05
- mainline：`02d7555`（snapshots/20260804T143803Z）—— 较上次 [变更摘要 3-5 条]
- 兼容状态：14/15 兼容，1 需适配（<repo>）
- 报告：[mainline-compat.md](reports/2026-08-05/mainline-compat.md) · [当日索引](reports/2026-08-05/index.md)
```

## 4. 构建内容

### 4.1 基座（DSH 集成）
- 根 `AGENTS.md`（DSH 规范：用途、private 约束、skill 用法、CHANGELOG 更新约定）
- `.agents/skills/mainline-compat/SKILL.md`（frontmatter + 工作流定义 + 自动化边界）

### 4.2 核心引擎（`scripts/compare-mainline.sh`）
流程（含 v5 全部能力）：
1. 索引仓库（`--scope` 可配置，默认 dsh-external 15 仓）
2. 拉当日 mainline（`.mainline/`，chmod 700），与状态文件 `.mainline-state.json` 对比
3. 锚定匹配 / 补丁 apply --check / seam 存在性 / peerDeps
4. **mainline 自身变更分析**（快照间 diff：包增删、seam 符号、版本；首次运行以 0803 cab66cd → 0804 02d7555 为基线演示）
5. 生成 `reports/<当日>/mainline-compat.md` + `<repo>.md × 15` + `index.md`
6. 更新 `reports/latest` 软链、追加 CHANGELOG 条目、写状态文件
7. 自动执行（默认关闭）：`--publish-issues`（发布 actions/org-issues.md 草稿，逐条批准）、`--apply-fix`（低风险修复，默认 dry-run 出 diff，写远程须逐项批准）

### 4.3 辅助脚本
- `scripts/check-placeholders.sh`（opencode-server/coding-receipt 三态）
- `scripts/check-ref-lag.sh`（toybox/skins ref 滞后）

### 4.4 情报与行动
- `analysis/plugin-formats.md`、`analysis/security-issues.md`
- `actions/org-issues.md`（≥5 条草稿）、`actions/issue-roadmap.md`（308 issue 聚类，未分类桶 + 时间戳，脱敏）

### 4.5 收尾
- `.gitignore`（.mainline/ .clones/ node_modules/）；脱敏规则进 README+AGENTS.md
- 本地 commit（不 push；最终提交前 STOP：是否 commit / 推 private 远程 / 发布 issue 草稿 / 执行自动修复）

## 5. 验收标准

1. 实跑引擎产出 `reports/<当日>/`（mainline-compat.md + 15 个 repo 详情 + index.md）；`reports/latest` 软链正确；CHANGELOG 追加当日条目且链接可点击直达
2. 首份报告含 mainline 变更分析节（0803→0804 基线：TUI 移除/WebSocket 下行等 ≥3 项）；兼容性矩阵 15 仓库；双方建议（插件侧 ≥15 条、主仓库侧 ≥3 条）
3. `--scope`/`--dry-run`/`--publish-issues`/`--apply-fix` 语义正确；自动执行默认关闭；SKILL.md 写明边界
4. 文档齐备（analysis 2 份、actions 2 份、AGENTS.md、SKILL.md）
5. 脚本 bash -n、依赖预检、退出码、离线报错；`git status` 干净；无未经批准远程写；脱敏抽查通过

## 6. 与 v5 的差异

| 变化 | 来源 |
|---|---|
| CHANGELOG.md 成为主更新视图（自动追加条目） | B④ |
| reports/ 按日期文件夹分立（当日 mainline-compat + 15 repo 详情 + index） | B④ |
| reports/latest 软链 + markdown 相对链接点击直达 | B④ |
| 引擎新增 CHANGELOG/软链/index 更新步骤 | B④ |
