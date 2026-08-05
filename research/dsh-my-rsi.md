# dsh-my-rsi 调研摘要

## 一句话定位

DSH 内测成员 hanlinxuy 的"个人 RSI 仓"——承载所有本地插件、树内补丁与可执行场景配方，让上游快照仓（`dsh2026/test-hanlinxuy`）保持纯净，本仓做实际迭代与试错。

## 技术栈与依赖

- 语言：TypeScript（`tsconfig.base.json`：`target: ES2022`、`module/moduleResolution: NodeNext`、`strict + noImplicitAny + declarationMap`）。
- 插件模型：[cordis](https://cordis.js.org/) `^4.0.0-rc.7` + [schemastery](https://github.com/Shigma/schemastery) `^3.18.0`（`apply(ctx, config)` + 同名 `Config` schema 的官方插件范式）。
- 测试工具链：vitest `^4.1.8` + vite `^6.4.3` + `vite-tsconfig-paths`（本仓用 npm 布局；upstream 子模块用 pnpm）。
- 运行时：Node.js 原生模块（`node:crypto`、`node:fs`、`node:os`、`node:path`）；session-analytics 可选后端为 DuckDB（嵌入式 OLAP，懒加载）。
- 上游 harness 依赖（类型/测试时解析，不打进本仓 deps）：`@deepseek-ai/dsh-tools`、`dsh-agent`、`dsh-agent-loop`、`dsh-session`、`dsh-llm`、`dsh-bash`、`dsh-compact`、`dsh-credentials` 等——经 `vitest.config.ts` 别名 + `upstream/tsconfig.base.json` paths 解析到 submodule 源码。
- 构建：无独立构建步骤（`main` 直接指向 `src/index.ts`），由 harness 运行时即时加载；脚本仅 `test` / `typecheck` / `verify-manifests`。
- 许可：MIT，作者 hanlinxuy；`packages/github/` 三件套 vendored 自 `dsh-external/dsh-github-integration`（MIT, mattheliu）。

## 文件结构概览

```
dsh-my-rsi/
├── README.md / THIRD_PARTY_NOTICES.md / LICENSE         # 中文 README + 第三方声明
├── package.json / tsconfig.base.json / vitest.config.ts # 本仓测试工具链（npm 布局）
├── packages/                                            # 8 个插件包
│   ├── guard/{tool-failure-guard, commit-gate}/         # 咨询式失败守卫 + 证据链提交门禁
│   ├── compact/compact-continuity/                      # 压缩边界债务快照 + 恢复重注入
│   ├── memory/memory-recall/                            # 蒸馏记忆管道（主动召回 + 候选 + 失效）
│   ├── analytics/session-analytics/                     # 会话统计（pure-JS / DuckDB 双后端）
│   └── github/{github, github-local-rest, tool-github}/ # GitHub 深度集成三件套（vendored）
├── recipes/                                             # 场景配方（剧本 + 可执行 demo spec）
│   ├── gpu-optimization-change/
│   ├── mobile-harness-optimization/
│   └── run.sh
├── patches/                                             # 树内补丁（应用到 upstream/）
│   ├── dsh-hooks-claude-precompact.patch (~32KB)
│   └── dsh-dev-instance.patch (~261KB)
├── upstream/                                            # git submodule → dsh2026/test-hanlinxuy 快照
├── scripts/                                             # init-dev-home.sh / plugin-mgr.sh / verify-manifests.mjs
└── iterations/                                          # 已迁移到 GitHub Issues（仅留 README 索引）
```

每个插件根目录统一布局：`dsh.plugin.json`（注册表清单）+ `package.json` + `src/{index.ts, invariant.ts}` + `tests/{*.spec.ts, *.composition.spec.ts, fixture/}` + 中英双 README + `README.i18n.yaml`（双语一致性 hash 校验）。

## 核心功能与实现要点

1. **tool-failure-guard（咨询式工具失败守卫）** — `packages/guard/tool-failure-guard/src/index.ts`：监听 `ctx.on('tools/post-execute')`，扫描工具结果的失败信封（`[exit code: N]`、`[sandbox: ...denied]`、`[timed out]`、Python Traceback 等 6 个 `FAILURE_PATTERNS`），通过 `agent.inject()` 注入 `{kind:'plugin'}` 来源的提醒。**不否决、不重写**——只 fold 一条 `additionalContexts` 到下游决策。`level` 配置（`all` / `effect-bearing`，默认后者）按 `toolEffect()` 对工具分级（`read`/`write`/`external`/`unknown`），只读工具失败（如 `ls` 一个不存在的路径）不提醒；bash/git 走动词启发式分类（如 `git push`=external、`git status`=read）。

2. **commit-gate（证据链提交门禁）** — `packages/guard/commit-gate/src/index.ts`：`tools/pre-execute` 在 `git commit` 调用前 deny（或 `askOnMissing` 走 approval seam），除非 session log 中存在与当前 staged-tree digest（`git write-tree` 的 sha）匹配的 `commit-gate/test-pass` 与 `commit-gate/review-pass` 事件。证据由 `tools/post-execute` 异步抓取：测试命令模式（默认覆盖 pnpm/npm/yarn/bun/make/cargo/go/pytest/vitest/jest）+ 独立评审工具模式（默认 `subagent`）+ clean-verdict 正则（`verdict: approve|clean` 等）。设计源自 SuzakuHarness，DSH 化的关键是把证据存进 session log（rebuildable）而非 `.suzakuharness` markdown，绕过门禁走 harness 原生 approval seam 而非自铸 token。严格遵守"model-visible ⟺ logged"不变量——只信循环实际记录的工具结果，不信模型 prose。

3. **compact-continuity（压缩连续性）** — `packages/compact/compact-continuity/src/index.ts`：监听 `ctx.on('session/event')`，在 `compact/start` 用 bash seam 跑 `debtCommand`（默认 `git status --short`）抓"未完成工作快照"，作为 log-only 的 `compact-continuity/debt` 事件入 log，并向模型注入来源化债务摘要；在 `compact/end` 从 `lastDebt()` 重注入恢复指针。让 compaction 对模型的 working state 接近无损。注意 `compact/end` 分支用 `await Promise.resolve()` 让出，避免 `session/event` 同步发布期重入 `session.append`（reentrancy guard 会拒绝）。

4. **memory-recall（蒸馏记忆管道，iteration 005）** — `packages/memory/memory-recall/src/index.ts`：三阶段。Phase A `agent/prompt-submit` 按 prompt 与条目 keywords 重叠度（`minOverlap` 默认 1）+ 每 topic 节流（`recallIntervalMs` 默认 60s）召回，注入 `[memory:topic]` sourced 消息。Phase B 注册模型工具 `memory_propose`，写入**隔离候选**（绝不直接变 active entry），带 source anchor（sessionId + seq）。Phase C 候选可声明 `contradicts` 把目标 entry 标 `stale`，召回跳过 stale。Store 按 git repo top-level（`git rev-parse --show-toplevel`，worktree-safe）sha256 取 key，存 `$DSH_HOME/memory/<repoKey>.json`，原子写（`tmp` + `rename`）；store 是派生媒介，session log 才是事实源。

5. **session-analytics（会话分析，iteration 006）** — `packages/analytics/session-analytics/src/index.ts` + `duckdb.ts`：注册模型工具 `session_stats`，把一个或多个 session 的 events 聚合成 `{totalEvents, turns, toolCalls, toolFailures, failures, denials}`。双后端：默认 pure-JS `aggregateEvents`（零依赖、确定性、可由 log 重建）；`backend:'duckdb'` 懒加载 `./duckdb.ts`，把 events flatten 成行后跑嵌入式 OLAP。失败检测同时识别结构化 `isError` 与文本失败信封；门禁拒绝按 result 文本含 `blocked` 计数；工具名靠 `tool/call` 事件的 callId 相关性回填。

6. **github 三件套（vendored 三方能力）** — `packages/github/{github, github-local-rest, tool-github}/`：vendored 自 `dsh-external/dsh-github-integration`。`github` 提供 `ctx.github` seam（request/spec 分离 + 平台卫生 client），`github-local-rest` 是 Node fetch 实现后端（per-call 凭据解析、rate-limit/etag/pagination 卫生），`tool-github` 暴露 11 个模型工具（`github_issue_{list,view,comments,comment,create,update}` + `github_pr_{list,view,diff,create,comment}`）。组合加载：实现 + 工具两包同时启用。

7. **场景配方（recipes）** — `recipes/gpu-optimization-change/`、`recipes/mobile-harness-optimization/`：每个 recipe = `RECIPE.md`（步骤/门禁/插件编排/验收 + `[INTEGRATION-POINT]` 接入点契约）+ `*.demo.spec.ts`（vitest 规格，**只 mock 模型**——`@test/mock-adapter` 按脚本回放，但 `LocalBashExecutor` + `git` 在临时真仓里跑、插件全为真实实现）。断言落在 `agent.session.events`（注入的 sourced 消息、tool/result、门禁证据事件）与 git 真实状态（HEAD、工作树）。`./recipes/run.sh [场景名]` 跑全部或单个。GPU recipe 验证 batch-size 优化失败 → 无证据提交被拒 → 测试+评审后放行的完整链路。

8. **树内补丁机制 + 双实例 dev home** — `patches/` + `scripts/`：上游 harness 以 `upstream/` submodule 引入（指向 `dsh2026/test-hanlinxuy` 固定 commit），本地改动固化为 patch，submodule bump 后 `git -C upstream apply ../patches/*.patch`（基线漂移时 `--3way`）。两份关键 patch：`dsh-hooks-claude-precompact.patch` 给 hooks-claude 桥加 PreCompact/PostCompact（映射 DSH 的 `compact/start|end`）；`dsh-dev-instance.patch`（261KB）是 dev 实例端到端集成——把 `@deepseek-ai/dsh-plugin`（plugin-local）vendor 进 workspace 作为插件管理器，注册 8 个插件包为 tsconfig paths，加 lefthook postinstall 容错。`scripts/init-dev-home.sh`（327 行）按数据类别管理 dev home 生命周期：凭据/配置永远保留、运行数据可清空、插件跟 repo 走；`scripts/plugin-mgr.sh` 是配置级插件管理器，封装 cordis.yml 配置行的 list/enable/disable/install/status。

## 与 DeepSeek Harness 主仓库的集成点

本仓是**面向 DSH harness 的插件/补丁集**，自身不包含 harness 源码（harness 在 `upstream/` submodule 里，指向私有快照仓 `dsh2026/test-hanlinxuy`）。集成通过 DSH 官方扩展契约：

- **插件注册表清单**：每个插件根的 `dsh.plugin.json`（`id`/`version`/`main`/`engines.dsh`/`contributes.{tools,skills}`）。`scripts/verify-manifests.mjs` 校验 id 形如 `<group>/<name>` 且有 `main`+`version`。
- **cordis 插件契约**：`export const name` / `inject` / `apply(ctx, config)` / `Config`（schemastery schema）。`inject` 声明依赖的 cordis service（`bash`/`tools`/`sessions`/`agents`）。
- **事件 seam**：`ctx.on('tools/pre-execute' | 'tools/post-execute' | 'agent/prompt-submit' | 'session/event')`。
- **工具注册**：`ctx.tools.register({name, parameters, output, execute})`（`memory_propose`、`session_stats`、11 个 `github_*`）。
- **服务获取**：`ctx.get('bash' | 'tools' | 'sessions' | 'agents' | 'github')`。
- **类型合并扩展**：通过 `declare module '@deepseek-ai/dsh-session' { interface SessionEventMap {...} }` 注入自定义 log-only 事件类型（`commit-gate/test-pass`、`commit-gate/review-pass`、`compact-continuity/debt`）；compact-continuity 通过 `import type {} from '@deepseek-ai/dsh-compact'` 触发 `compact/start|end` 事件的 declaration-merge。
- **来源化注入**：`createUserMessage({content, source: {kind:'plugin', plugin: <name>}})`——标签是 load-bearing，否则注入在派生历史里会被当 user prompt。
- **approval seam**：commit-gate 的 `askOnMissing` 走 `{kind:'ask'}` → harness 原生 approval，而非自铸绕过 token。
- **补丁固化为代码**：`dsh-dev-instance.patch` 把 plugin-local 插件管理器 vendor 进 upstream 快照、把 8 个本仓包注册为 tsconfig paths 目标；`dsh-hooks-claude-precompact.patch` 扩展 hooks-claude 桥的事件覆盖。
- **测试隔离**：`vitest.config.ts` 用 `define: { __DSH_ROOT__ }` 把快照根注入组合规格，用 alias 把 bare `@deepseek-ai/dsh-*` 名映射到 `upstream/packages/.../src/index.ts`，让本仓测试在 layout-independent 下跑到真实 harness 源码。

## 亮点与风险

**亮点**

- **"model-visible ⟺ logged"不变量**贯穿 commit-gate / session-analytics：证据只认 session log 里实际记录的工具结果，不认模型 prose，从根上防伪造证据。
- **digest 绑定**（`git write-tree` 暂存树 sha）让证据与暂存内容密码学挂钩，重新 stage 后旧证据自动失效（`packages/guard/commit-gate/src/index.ts:matchingEvidence`）。
- **纯净快照策略**：上游以 submodule 固定 commit 引入，本地改动一律 patch 化，让快照仓可独立 bump、可独立公开。
- **advisory 原则**：tool-failure-guard 只提醒不否决（决策权留给模型）；commit-gate 提供了 `ask` 逃生口而非硬 deny。
- **双后端 analytics**：同一聚合契约下，默认 pure-JS 零依赖，大数据集切 DuckDB OLAP，懒加载保住热路径（`packages/analytics/session-analytics/src/index.ts:apply`）。
- **可执行配方 + 接入点契约**：recipes 把"插件协同是否真的跑通"做成 vitest 断言（只 mock 模型，bash/git/插件全真），又用 `[INTEGRATION-POINT]` 把业务代码落地位置与契约显式留给用户，工程闭环很扎实。
- **dev home 数据分类**：init-dev-home.sh 区分凭据/运行数据/插件本体三类，分别处理，避免一键 reset 丢凭据。

**风险**

- **upstream submodule 指向 dsh2026 私有仓**：README 明确警告"正式公开前需移除 `upstream/` submodule，避免暴露 dsh2026 私有仓地址"（`README.md`"开发与验证"节末）。
- **plugin-local（`@deepseek-ai/dsh-plugin`）依赖外部生态**：dev 实例整套插件管理（安装/启停/热插拔）依赖该 vlln/dsh-external 包，外部变动会波及本仓（`patches/dsh-dev-instance.patch`）。
- **session/event 通知期 append 重入**：compact-continuity 已用 `await Promise.resolve()` 绕过 reentrancy guard，但语义脆弱，依赖 harness 通知时序（`packages/compact/compact-continuity/src/index.ts` 的 `compact/end` 分支）。
- **DuckDB 原生依赖历史包袱**：`.gitignore` 注释指出 duckdb 等原生包曾误入仓，已于 2026-08-05 重写清除；若 backend 选 `duckdb`，CI/部署环境需具备原生构建链。
- **bash/git 动词分类是启发式**：tool-failure-guard 的 `toolEffect()` 对未知动词判 `unknown`（保守地提醒），但任何新工具/别名都可能落到 `unknown`；分类表需手动维护（`packages/guard/tool-failure-guard/src/index.ts:READ_TOOLS/WRITE_TOOLS/BASH_*`）。
- **memory store 是派生媒介**：`$DSH_HOME/memory/<repoKey>.json` 损坏会被静默丢弃重建（log 才是事实源），但用户若误以为是权威存储会困惑（`packages/memory/memory-recall/src/index.ts:loadStore` 的 catch）。
- **recipes 业务代码留空**：`[INTEGRATION-POINT]` 是契约占位，实际 GPU 训练脚本 / 手机侧 harness 代码需用户重新定向，本仓不提供。

## 维护状态

**活跃维护**。最新提交 `4b17c10 docs(patches): regenerate dev-instance patch for plugin-local architecture`，时间 **2026-08-05 22:48 +0800**（与本次调研同日）。迭代追踪已从本地 `iterations/issues/` 迁移到 GitHub Issues（#1–#10，#1–#8 已 closed，含 005 蒸馏记忆管道、006 DuckDB 分析投影、001–004 收尾、场景配方 my-rsi-workflow；#9 dev-home 生命周期管理、#10 本地迭代布局迁移进行中）。所有插件版本号统一 `0.0.1`，`engines.dsh: ">=0.0.1"`，处于内测期。仓内中英双 README 带 `README.i18n.yaml` hash 校验（双语一致性可验证）。

## 备注

- 与同组织下 `dsh-github-integration` 的关系：本仓 `packages/github/` 是其 vendored 副本（同 MIT、同作者 mattheliu），用户可任选独立装 `dsh-github-integration` 还是用本仓的 vendored 版。
- 与上游快照仓 `dsh2026/test-hanlinxuy` 的关系：本仓是"工作仓"，snapshot 仓保持纯净（bill9109 维护，1 commit，2026-08-05 更新），本仓以 submodule 固定其某次快照作为测试基线。
- 本仓私有，供 dsh 内测成员在 dsh-external 组织内协作；正式公开前请勿分发（README 版权节）。
- 调研快照：shallow clone（`--depth 1`），未初始化 `upstream/` submodule——本摘要中所有 harness 集成点描述来自本仓源码与 README，未交叉读 submodule 内 harness 源码（如需可后续 `git submodule update --init`）。
