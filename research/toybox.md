# toybox 调研摘要

## 一句话定位

`dsh-external/toybox` 是 DeepSeek Harness（DSH）生态的"整活插件玩具箱"——收藏有梗、好玩但仍达到官方验收标准的 DSH 插件（技能 + MCP 服务器），与"正经通用插件"仓库 `dsh-hub` 形成互补；作者 作者（昵称已脱敏），私有仓库，供 dsh 内测成员使用。

## 技术栈与依赖（语言、框架、关键依赖）

- **语言**：TypeScript（`.mts` 源码，`.gitattributes` 显式归为 TypeScript；构建产物标为 generated）。MCP 服务器源码全用 TS，技能插件为纯 Markdown（SKILL.md）。
- **运行时**：Node ≥ 22；MCP 产物是**零依赖单文件 ESM**（`.mjs`，只 `import node:` 内置模块），最终用户机器上无需 `node_modules`。
- **构建链**：自研 `scripts/build.mjs`（每插件独立 `tsconfig.json` 调 `tsc`）+ `scripts/verify.mjs`（build + 官方 prepare 冒烟 + MCP 协议冒烟 + skill frontmatter 校验）+ `scripts/publish.mjs`（把全部插件 pin 到 HEAD，重生成 README 安装块/ref 表/catalog.json）。
- **TS 严格度**：`tsconfig.base.json` 对齐官方 0804 快照——`strict` + `noUncheckedIndexedAccess` + `exactOptionalPropertyTypes` + `noEmitOnError`，`target/module` 为 `es2024`/`esnext`，`moduleResolution: bundler`。`.mts` 输入保证 `.mjs` ESM 输出。
- **测试**：vitest ^4.1.10；`tests/lib/mcp-client.ts` 提供共享 stdio MCP 客户端（换行分隔 JSON-RPC）。
- **CI**：`.github/workflows/verify.yml`（pnpm + Node 22，跑 typecheck/build/test/verify 全门）。
- **包管理**：pnpm（lockfile 已提交）；根 `package.json` 仅 3 个 devDep（`@types/node`、`typescript`、`vitest`）。
- **许可**：仓库编排为 MIT；各插件包内 `package.json#license` 默认 BSD-3-Clause（与 DSH 对齐）。

## 文件结构概览

```
toybox/
├── README.md                  # 住户表 + 构建链 + 入住指南 + 规划中住户（8.8KB）
├── catalog.json               # 机器可读插件索引（schema toybox-index/v0.1）
├── package.json               # 根包：build/verify/publish/test 脚本
├── pnpm-lock.yaml
├── tsconfig.base.json         # 共享严格 TS 选项（对齐官方 0804）
├── vitest.config.ts
├── plugins/                   # 8 个插件，每插件独立目录
│   ├── code-archaeologist/    # skill（旗舰）
│   ├── bug-tamer/             # skill
│   ├── code-talent-scout/     # skill
│   ├── almanac-mcp/           # mcp
│   ├── naming-master-mcp/     # mcp
│   ├── decision-dice-mcp/     # mcp
│   ├── chinese-colors-mcp/    # mcp
│   └── time-capsule-mcp/      # mcp
├── scripts/                   # build.mjs / verify.mjs / publish.mjs
├── tests/                     # vitest 协议测试 + tests/lib/mcp-client.ts
├── docs/                      # INSTALL.md / CONTRIBUTING.md
├── .github/workflows/verify.yml
└── LICENSE                    # MIT
```

**MCP 插件目录模板**（如 `plugins/almanac-mcp/`）：
```
plugins/<id>/
├── src/<id>.mts               # TS 源码（零依赖）
├── tests/<id>.spec.ts         # vitest 协议测试
├── tsconfig.json              # extends 根 base
├── README.md
└── .dsh-plugin/               # 官方静态交付格式（提交产物）
    ├── package.json           # name/version/license/scripts.prepare/dsh.mcpServers
    ├── prepare.js             # 官方 0804 prepare 的拷贝（133KB，全插件共用同一份）
    ├── .mcp.json              # { "mcpServers": { "<id>": { "type":"stdio", "command":"node", "args":["server/<id>.mjs"] } } }
    └── server/<id>.mjs        # ← tsc 编译产物，零依赖单文件
```

**skill 插件目录模板**（如 `plugins/code-archaeologist/`）：无 `src/`，`.dsh-plugin/` 下是 `package.json`（`dsh.skills: ["skills"]`）+ `prepare.js` + `skills/<id>/SKILL.md`（YAML frontmatter 必含 `name` + `description`）+ 可选 `skills/<id>/resources/`。

## 核心功能与实现要点

### 集合层（构建/发布/校验基础设施）

1. **统一构建链**（`scripts/build.mjs`）：遍历有 `tsconfig.json` 的插件，逐个跑 `tsc -p`，把 `src/*.mts` 编译成 `.dsh-plugin/server/*.mjs` 单文件产物；支持 `--check` 仅类型检查、`<id>` 单插件构建。
2. **一键全量校验**（`scripts/verify.mjs`）：三段门禁——① 全插件 tsc 构建；② 每个 MCP 插件复制到临时目录跑官方 `prepare.js`，断言 `dsh-plugin-assets/.mcp.json` 与 `dsh-plugin.mjs` wrapper 生成，再起子进程做真实 MCP 协议冒烟（initialize → tools/list → 每工具一次 call）；③ skill 插件校验 SKILL.md frontmatter。`MCP_CASES` 字典硬编码了每插件的冒烟调用参数。
3. **发布脚手架**（`scripts/publish.mjs`）：`git rev-parse HEAD` 取 40 位 commit，把全部插件 pin 到该 ref，重写 README 的 `<!-- INSTALL -->` / `<!-- REFS -->` 块、`docs/INSTALL.md` 安装块、`catalog.json`（schema `toybox-index/v0.1`）。体现官方"不可变身份 = 完整 commit ref，不用分支名/短 hash"纪律。
4. **共享 MCP 测试客户端**（`tests/lib/mcp-client.ts`）：`McpClient` 类封装 spawn 子进程 + readline 解析换行分隔 JSON-RPC，提供 `initialize/toolNames/call/callText/close`，8 秒超时；所有 MCP 插件的 vitest 测试复用它。

### 插件层（8 个住户）

5. **code-archaeologist（代码考古学家，skill，旗舰）** —— `plugins/code-archaeologist/.dsh-plugin/skills/code-archaeologist/SKILL.md`（5.8KB）。把"看懂老代码"重构为田野考古：现场勘察 → 地层判定（史前/青铜/铁器/现代/断层，每层需 2 条以上证据）→ 出土文物登记（镇馆之宝/幽灵/定时炸弹/彩蛋）→ 发掘报告（含保护性迁移建议，按风险排序且每条带可验证验收标准）。核心纪律是"只读优先 + 证据链（每条判断附 `文件:行`）+ 幽默但诚实"，配套 `resources/report-template.md` 报告模板。"代码考古学家"即此技能的人格化角色——不是来改代码，而是来发掘、断代、登记、写报告。
6. **bug-tamer（Bug 驯兽师，skill）** —— `SKILL.md`（3.9KB）。把 bug 当野兽，方法论四步：诱捕（最小复现）→ 驯化（区分根因 vs 导火索）→ 放归（修复 + 回归测试）→ 饲养手册（防复发 + 同族排查）。强调"没有稳定复现前一切根因都是推测"，输出标准化驯兽报告。
7. **code-talent-scout（代码星探，skill）** —— `SKILL.md`。把代码评审做成选秀：四维评分（职责/可读性/健壮性/可测性，各 25 分）→ 评级（S 出道位 / A 训练生 / B 候补 / C 回炉重造）→ 名单公布（C 级 Top 1 给重写方案 + 验收标准）。
8. **almanac-mcp（老黄历，mcp，3 工具）** —— `src/almanac.mts`（14.9KB）。工具：`yi_ji`（干支日/五行/宜忌/冲煞/幸运方向 + 星期彩蛋）、`chou_qian`（FNV-1a hash seed 可复现抽签）、`tang_shi`（按日期稳定选唐诗）。基准 1900-01-31 甲子日推算，诚实标注"简化算法，仅供娱乐"。
9. **naming-master-mcp（取名大师，mcp，2 工具）** —— `name_it`（variable/function/class/project/module/pet/command 七主题 × gu_feng/cyber/minimal/geek 四风格，1-5 个名字 + 含义，seed 稳定）、`name_styles`（列出风格说明）。
10. **decision-dice-mcp（决策骰子，mcp，3 工具）** —— `flip`（抛硬币）、`roll`（2-100 面、1-10 次）、`fate`（2-10 选项天意抉择 + 决策技巧提示），均支持 seed 复现。
11. **chinese-colors-mcp（中国传统色，mcp，3 工具）** —— `color_search`（按名称/典故/色系搜索）、`color_of_day`（按日期稳定今日色）、`color_palette`（按色系出 4 色和谐色板）。内置 60 色库（catalog.json 描述）/ 61 色（README 描述，存在不一致）。
12. **time-capsule-mcp（时间胶囊，mcp，3 工具）** —— `seal`/`list`/`open`。把消息封存到 `~/.dsh-capsules/`（可用 `DSH_CAPSULES_DIR` 覆盖）下的 JSON 文件，`open` 在未到期时**服务器拒绝返回内容**（只显示倒计时），到期才泄露；诚实纪律："密封即密封"。

## 与 DeepSeek Harness 主仓库的集成点

集成方式为**官方 repository-plugin 静态格式**（非开发层 `dsh.plugin.json`），通过 DSH 的 `@deepseek-ai/dsh-repository-plugin` 加载：

- 在用户 `~/.dsh/config.yaml` 中以 `repository-plugins` 条目挂载，每插件一行 source：
  `github:dsh-external/toybox#<40位commit>&path:/plugins/<id>/.dsh-plugin`
- **不可变身份**：`#<ref>` 必须是完整 40 位 commit（不用分支名/短 hash）；更新插件 = 换 ref。同一 source 字符串永久复用缓存，改代码后官方运行时不会自动发现。
- 协议 seam：MCP 插件走 `.dsh-plugin/.mcp.json`（`mcpServers.<id>.type=stdio`，`command=node`，`args=["server/<id>.mjs"]`）——DSH 拉取后由 `prepare.js` 生成 `dsh-plugin-assets/.mcp.json` + `dsh-plugin.mjs` wrapper，运行时通过 stdio + 换行分隔 JSON-RPC（MCP `initialize`/`tools/list`/`tools/call`）连通模型；skill 插件走 `.dsh-plugin/skills/<id>/SKILL.md`，模型经 `ctx.skills.get()` 读取。
- 缓存路径：`$DSSH_HOME/cache/repository-plugins`；加载失败时官方保留最后一棵好树并广播 `hmr/config-update-failed`，不破坏现有插件。
- **能力边界**：官方 `.dsh-plugin` 静态格式只支持 skills + MCP，**不支持**任意 JS 工具/命令/hooks——CONTRIBUTING.md 明确指出那些能力要走开发层（DSH workspace 包或 plugin-registry 的 `dsh.plugin.json`）。
- 严格对齐官方 **0804 快照**（tsconfig 选项、prepare.js 拷贝、SKILL.md frontmatter 规范引用 `dsh2026/test-作者（昵称已脱敏）` 的 skills 文档）。

## 亮点与风险

**亮点**

- **工程纪律扎实**：整活归整活，但每插件都要过官方 prepare + 真实 MCP 协议冒烟 + skill frontmatter 校验，CI 全门禁；MCP 服务器零依赖单文件，最终用户机器零安装成本。
- **"诚实标注"是明文纪律**：判断类技能强制证据链（`文件:行`），娱乐类插件（老黄历）诚实声明"简化算法、仅供娱乐"，与段子明确分开——这是 toybox 自定的玩具箱纪律。
- **发布脚手架优雅**：`publish.mjs` 一键 pin ref + 重生成 README 块/catalog，杜绝手抄 ref；"不可变 commit ref"纪律贯彻到位。
- **技能方法论设计精巧**：考古/驯兽/选秀三个 skill 都把模糊任务（"看懂老代码""修 bug""评代码质量"）重构成有步骤、有产出模板、有验收标准的工作流，附可复制的报告模板。

**风险**

- **README/catalog 与 HEAD 的 ref 不一致**：`README.md` 安装块（`<!-- INSTALL -->`）与 `catalog.json` 的发布 ref 仍为 `c02a31be5f5c068075ee09efd67e343da43ba029`，但仓库 HEAD 已是 `7acd885`（2026-08-05 "docs: note language-stats refresh trigger"）。即最近一次 docs 提交后未重跑 `pnpm publish`。虽属文档性 commit、插件产物未变，但按"更新插件=换 ref"纪律，publish 应在每次提交后执行以保持索引与 HEAD 同步（`README.md` INSTALL/REFS 块、`catalog.json:updated`）。
- **中国传统色色数标注不一致**：README 住户表写"61 色库"，`catalog.json` 描述写"60 色库"（`README.md` 第 18 行附近 vs `catalog.json` chinese-colors-mcp 条目）。
- **time-capsule 明文存储隐私风险**：胶囊内容以明文 JSON 落地 `~/.dsh-capsules/*.json`，`message` 字段未加密（`plugins/time-capsule-mcp/src/time-capsule.mts:38, 60-66`）。服务器层只防"未到期经 API 读取"，不防"用户直接 cat 文件"——若用户写入敏感内容，本地任何能读该目录的进程都能看。
- **time-capsule 文件名 id 碰撞窗口**：id 由 `日期 + Date.now()%100000` 组成（`src/time-capsule.mts:55`），同一天内毫秒级并发封存存在理论碰撞；损坏的 JSON 文件被静默 `catch {}` 跳过（`src/time-capsule.mts:44-49`），无告警。
- **私有仓库访问门槛**：安装需 dsh-external 组织读权限，公开分发需作者许可——对未受邀用户是硬阻塞（非代码缺陷，但影响可达性）。

## 维护状态

- **default_branch**：`main`（HEAD = `origin/main` = `7acd885`）。
- **最近 push**：2026-08-05（与调研日同天，极度活跃）。
- **提交活跃度**：depth-1 clone 只暴露 1 个 commit，无法看完整历史；但从 README 住户表"全部 ✅ 0804 对齐，端到端验证通过"、规划中住户清单、CI 配置完整度看，仓库处于积极迭代期。所有 8 个插件状态标注为"已对齐官方 0804 快照 + 端到端验证通过"。
- **README 质量**：优秀（8.8KB）——含住户表、构建链、入住指南、规划住户、许可；`docs/INSTALL.md`（3.3KB）+ `docs/CONTRIBUTING.md`（3.5KB）配套完整。CI（`verify.yml`）覆盖 typecheck/build/test/verify 全门。

## 备注

- **私有问题**：仓库当前为 dsh-external org 私有仓库，仅供内测；README 明确"正式公开前请勿公开分发"。
- **5 个候选住户**：代码瑜伽（code-yoga）、代码翻译官（code-translator）、代码导游（code-tour-guide）、代码塔罗（code-tarot-mcp）、乱码急救员（mojibake-medic，已下架待重启）——均未开工。
- **语言统计技巧**：`.gitattributes` 把构建产物 `.mjs` 标为 generated、`.mts` 显式归 TypeScript，让 GitHub linguist 把仓库正确显示为 TypeScript 主导（README 末尾专门解释了 push 触发/异步刷新的时机）。
- **与 dsh-hub 的分工**：`dsh-hub`（`ohmyd-dev/dsh-hub`）收"正经通用插件"（git 提交信息、代码规范等），toybox 只收"有梗的"，避免重复造轮子。
- **MCP 协议版本**：客户端握手用 `2025-06-18`，服务器回显请求方的 protocolVersion（向后兼容）。
