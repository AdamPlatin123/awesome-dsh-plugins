# dsh-issue-filer 调研摘要

## 一句话定位
向 DSH 内测反馈仓库 `dsh-external/issues` 自动提交 issue 的 DeepSeek Harness skill：负责自动查重、按仓库规范格式化、调用 `gh` 创建 issue，并在本地维护一份台账。

## 技术栈与依赖
- 形态：DSH agent skill（目录即 skill，由 `SKILL.md` 的 YAML frontmatter 描述触发条件）；不是独立应用、无构建系统。
- 运行时：Node.js（仅 `scripts/record.mjs` 一个 `.mjs` 脚本），ESM。
- 依赖：**零运行时依赖**——脚本只用 `node:fs`、`node:path`（`scripts/record.mjs:1-2`），无 `package.json`、无 `node_modules`。
- 外部工具：依赖 `gh` CLI（已认证）；`gh` 不可用时可降级为 GitHub REST API（`curl + GH_TOKEN`），或配合姊妹仓 `dsh-gh-bridge`。
- 凭据：`gh auth status` / `GH_TOKEN` 环境变量 / macOS Keychain。
- 许可：BSD 3-Clause，Copyright (c) 2026, dsh-external contributors。

## 文件结构概览
```
dsh-issue-filer/
├── SKILL.md                      # 技能主文件（含 frontmatter：name=file-dsh-issue）
├── README.md                     # 中英双语说明、目录、用法、脱敏
├── LICENSE                       # BSD 3-Clause
├── .gitignore                    # 忽略 node_modules/lib/coverage/issue-tracker/
├── references/
│   └── issue-format.md           # dsh-external/issues 标题/正文/标签规范参考
└── scripts/
    └── record.mjs                # 本地台账脚本（JSONL + 自动生成 markdown）
```
仅 6 个跟踪文件，单提交 `194556e`（2026-08-05 11:29 +0800，commit 与 author 时间一致）。

## 核心功能与实现要点
1. **工作流编排（SKILL.md:7-9, 25-75）**：定义"认证检查 → 收集信息 → 去重 → 格式化 → 附件处理 → 创建 → 本地记录 → 汇报"的八步流程，全部由 DSH agent 按 SKILL.md 指引执行；skill 本身不含可执行编排逻辑。
2. **强制去重（SKILL.md:25-35）**：标题为"去重（必须执行，不可跳过）"，要求同时拉取 open + closed issue（`gh issue list -R dsh-external/issues --state all --limit 500`），并核对本地台账 `ledger.md`；发现相似则改为评论已有 issue 或在正文中引用 `#<n>`。
3. **本地台账脚本（scripts/record.mjs）**：纯 Node stdlib 实现的命令行工具，把每条已提交 issue 追加到 `issues.jsonl`，并基于模板（`regenerateLedger`，scripts/record.mjs:42-65）重新生成 markdown 表格 `ledger.md`。支持 `--list`（console.table 打印）、按 `--number` 新增或合并更新（`findIndex` + spread，scripts/record.mjs:119-135）。
4. **tracker 目录解析（scripts/record.mjs:37）**：`DSH_ISSUE_TRACKER_DIR` 环境变量优先，否则回退 `<cwd>/issue-tracker/`。
5. **格式参考（references/issue-format.md）**：实地调研 `dsh-external/issues`（295 open + 22 closed，截至 2026-08-05），总结标题前缀 `[类型][组件]`（如 `[bug][web][a11y]`、`[perf][web]`），并给出 bug/enhancement 两类正文模板与可用标签清单（`bug`/`enhancement`/`question`/`duplicate` 等）。
6. **trajectory 附件处理（SKILL.md:38-43）**：定位 DSH 会话日志 `~/.dsh/sessions/<目录>/session-<id>/session.jsonl.zstd`，`unzstd` 解压为 `.jsonl`，强制脱敏（API Key / 访问令牌 / 个人信息），过大则 `zip` 压缩；明确说明 `gh issue create` 不支持直接上传附件，需用户在网页手动补充。
7. **脱敏契约（README.md "安全 / 脱敏"段、SKILL.md:38-43）**：token / 密钥 / 个人信息绝不进入 issue 正文或附件，且本仓库内容自承诺不含任何凭据或用户身份信息。

## 与 DeepSeek Harness 主仓库的集成点
- **集成对象**：DSH agent harness 的 skill 加载机制。安装方式是把本目录放入 `<workspace>/skills/file-dsh-issue/`，DSH 通过 `SKILL.md` 的 frontmatter（`name: file-dsh-issue`、`description:` 列出"提 issue / 提交 bug / 反馈问题"等触发词）发现并在匹配时调用。
- **数据消费**：读取 DSH 自身的会话轨迹文件 `~/.dsh/sessions/<dir>/session-<id>/session.jsonl.zstd`（references/issue-format.md "附件"段、SKILL.md:38），即与 DSH 的 session 存储路径耦合。
- **外部提交目标**：通过 `gh` CLI 向 `dsh-external/issues` 仓库提 issue / 评论 / 查询（SKILL.md:14-15, 26, 57-59）。
- **无代码级 seam**：本仓库与 DSH 主仓没有共享包/导入/类型契约，集成完全靠"目录约定 + frontmatter 描述 + 文件路径"这种 skill 协议；主仓若改 skills 发现规则或 session 路径，本 skill 需手工同步。

## 亮点与风险
- **亮点**：极简、零依赖；台账用 append-only JSONL 作单一事实源、markdown 表格由其派生（scripts/record.mjs:42-65, 122-138），易于版本管理与 diff。
- **亮点**：去重被写成强制步骤（SKILL.md:25 "去重（必须执行，不可跳过）"），且要求同时检查 open/closed 与本地台账，比单纯 grep 远端更稳。
- **风险**：去重逻辑完全由 agent 做语义/关键词比对（SKILL.md:28-32），没有自动化相似度检索，量大时漏判/误判依赖 agent 自觉。
- **风险**：台账是纯本地、无远端同步（scripts/record.mjs 只读写本地文件），多机/多 agent 会割裂；状态漂移需手工 `gh issue view` + `--status` 修补（SKILL.md "管理已有 issue" 段）。
- **风险**：附件不能经 `gh` 直传（SKILL.md:43），需用户网页手工补传，是流程断点；脱敏也完全依赖 agent 自检。
- **风险**：标题/正文规范是"观察现有 issue 总结"（references/issue-format.md），仓库本身无 issue template 强约束，规范会随仓库演化漂移。
- **风险**：仅 1 次提交、2026-08-05 当天新建、无 tests/CI；任何回归只能靠人工演练发现。

## 维护状态
- 单提交仓库（commit `194556e`），作者/提交时间均为 2026-08-05 11:29:15 +0800——**今天新建**，处于初始发布阶段。
- 无 CHANGELOG、无 issues/PR、无 release、无 CI 配置、无测试。
- LICENSE 标 2026 年，BSD 3-Clause，由 "dsh-external contributors" 持有。

## 备注
- 与同仓 `dsh-gh-bridge` 是姊妹项目：当沙箱内 `gh` 不可用时由 bridge 提供等价能力（README.md "安装"段、SKILL.md:14-15）。
- `dsh-external/issues` 是 DSH 内测反馈收集仓，本 skill 是其上游"提交端"，而非常规意义上的产品代码。
- `.gitignore` 包含 `issue-tracker/`，确认台账数据刻意不入库。
