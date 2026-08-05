# distill 调研摘要

## 一句话定位

DeepSeek Harness（dsh）的外部插件 `@dsh-external/distill`（清单 id `distill`，v0.1.0），在每次 agent 回合结束后台反省近期人类用户消息，把可复用的工作流自动蒸馏成 `SKILL.md` 技能包写入本地技能目录，让随后的会话自动发现并复用——主对话不注册任何模型可见工具，唯一的副作用是磁盘上的技能文件。

## 技术栈与依赖

- **语言/构建**：TypeScript（`target: ES2024`，`module: esnext`，`moduleResolution: bundler`，`strict: true`），通过 dsh checkout 的 `tsc` 编译到 `lib/`；ESM（`"type": "module"`）。
- **运行时**：Node.js，使用 `using` 语法糖（`Symbol.asyncDispose`/`deadline`）。
- **插件框架**：cordis `^4.0.0-rc.7`（fiber/context/plugin 系统，`ctx.on`/`ctx.plugin`/`ctx.subagents`）。
- **配置**：schemastery `^3.18.0`（`z.object` 定义可校验的 `Config`）。
- **dsh peer 依赖**（全部 `^0.0.1`）：`@deepseek-ai/dsh-agent`、`dsh-llm`、`dsh-session`、`dsh-skill`、`dsh-subagent`、`dsh-timeout`、`dsh-tools`。
- **许可**：BSD-3-Clause；反省提示词改编自 Nous Research `hermes-agent` 的 `_SKILL_REVIEW_PROMPT`（MIT，Copyright (c) 2025 Nous Research），署名见 `src/index.ts` 文件头。
- **dev**：`typescript ^5.9.0`、vitest（测试）。
- **构建脚本**：`scripts/build.sh`，把 dsh checkout 的 vendored 包（cordis、cosmokit、schemastery、各 `@deepseek-ai/dsh-*`、`@standard-schema/spec`）软链到本仓 `node_modules/` 再 `tsc -p tsconfig.json`。

## 文件结构概览

```
distill/
├── dsh.plugin.json        # 插件清单：id=distill，contributes.tools/skills 均为空
├── package.json           # @dsh-external/distill，peerDeps 锚定 dsh 包
├── tsconfig.json          # 仅 include src，输出 lib + lib/types
├── README.md              # 中文（唯一一次提交把英文/zh 双版本合并成单中文）
├── probe.mjs              # 启动真实 base.cordis.yml（移除内置 distill 块）后的冒烟探针
├── src/
│   └── index.ts           # 全部实现（634 行），单一 entry
├── lib/                   # 编译产物（已提交）
│   ├── index.js
│   └── types/index.d.ts
├── scripts/
│   └── build.sh           # 软链 dsh checkout 依赖 + tsc
└── tests/
    └── distill.spec.ts    # 27 个用例，覆盖调度/路由/所有权/检查点/解析/渲染
```

## 核心功能与实现要点

1. **事件入口与调度**（`src/index.ts:280-302` `apply`）：`inject: ['subagents']`；在 `ctx.on('agent/settled', …)` 中仅响应 `reason.kind === 'completed'`；用 `pending: Map<sessionId, Promise>` 保证每个会话同时只有一次反省在飞，`session/disposed` 时清理；任何异常只 `ctx.logger.warn`，绝不让循环崩溃。

2. **消息窗口与检查点**（`collectWindow` + `checkpointSeq`，`src/index.ts:319-353` 与 `:301-318`）：从会话事件流筛出 `user/message` 且 `source.kind === 'user'` 的事件，提取 text 块拼成窗口；检查点从最近一条 `session/distill-review-request` 日志事件的 `messageSeqs` 末尾推导——没有就从 -1 起（即首条用户消息）。窗口未达 `minUserMessages`（默认 3）直接跳过。

3. **反省子代理派发**（`runReview`，`src/index.ts:355-402`）：通过 `ctx.subagents.start(config.providerName, …)` 派发；子代理携带 `label: 'distill-review'`、`parent: agent`、`toolFilter: { allow: ['skill'] }`（白名单只有技能查看器）、`outputSchema: REVIEW_SCHEMA`、`agentOptions: { provider, model, maxTokens }`；用 `deadline(undefined, config.timeoutMs, 'DISTILL_TIMEOUT')` 作为共享截止时间，超时会取消子代理。子代理 stopReason 非 `completed`、`structured` 缺失都只记录警告并返回 undefined。

4. **路由解析**（`resolveTarget`，`src/index.ts:304-316`）：优先用配置中的显式 `provider`+`model`（两者必须同时给，否则 `validateConfig` 抛错），否则回落到刚结束 agent 自身的 `agent.options.provider/model`；两者都没本轮跳过并告警。

5. **所有权标记与写策略**（`applyProposal` + `isOwnedSkill` + `renderSkillFile`，`src/index.ts:404-470`、`:545-572`）：
   - 写入文件统一带 frontmatter 行 `distilled-by: dsh-distill` 作为所有权标记。
   - `create`：目标 `SKILL.md` 已存在则跳过（不覆盖任何已有技能）。
   - `update`：目标必须存在**且**包含所有权标记；否则告警跳过——用户手写、内置、运行时注册的技能永不被改写。
   - 仅整文件重写，不支持补丁、不支持 `references/`/`templates/`/`scripts/` 旁路文件。

6. **反省提示词**（`buildReviewPrompt`，`src/index.ts:472-540`）：把 Hermes 的策展课程改写为本界面契约——要求"主动"提案（默认应行动而非 skip），列出触发信号（用户对风格/工作流的纠正、新出现的技术/修复/调试路径、当前技能缺失步骤等），明确规定不捕获的内容（环境性失败、"某工具坏了"的负面断言、未解决的失败序列、一次性任务），并注入可更新技能清单与消息窗口 JSON。

7. **结构化输出契约**（`REVIEW_SCHEMA`，`src/index.ts:170-191`）：`{action: 'create'|'update'|'skip', skill?: {name, description, whenToUse?, content}}`；`parseReflection` 校验 action、`isSkillName`（kebab-case）、description/content 非空；`renderSkillFile` 用 YAML frontmatter 渲染并转义引号/反斜杠。

8. **派发前的可观测事件**（`DistillReviewRequestEventData` 与 `declare module`，`src/index.ts:131-160`）：派发前 `session.append('session/distill-review-request', {messageSeqs, route, prompt, toolFilter, maxTokens})`，记录精确路由、提示词、工具白名单和 token 上限——使"模型可见输入"可从会话日志完整重建。这是仅日志事件，对话循环不可见。

## 与 DeepSeek Harness 主仓库的集成点

- **清单契约**：`dsh.plugin.json` 声明 `engines.dsh: ">=0.0.1"`、`main: ./lib/index.js`、`contributes.tools/skills` 均为空数组——插件不向模型暴露任何工具或技能，只挂接 `agent/settled`。
- **cordis 插件系统**：`apply(ctx, config)`、`ctx.on('agent/settled' | 'session/disposed')`、`ctx.subagents.start`、`ctx.logger`、`inject: ['subagents']`——典型的 dsh cordis 插件形态。
- **宿主前提**（README 明示）：组合（`cordis.yml`）必须挂载 `subagent-spawn`（注册反省子代理使用的 `spawn` 子代理提供方）与 `tool-skill`（提供反省子代理可调用的 `skill` 查看器），两者在 `base.cordis.yml` 默认存在。
- **同名替换关系**：宿主 `base.cordis.yml` 默认挂载了内置 `@deepseek-ai/dsh-distill`（id 同为 `distill`）；外挂本插件时需要先把内置块移除（`probe.mjs` 就是把 `base.cordis.yml` 中 `- id: distill` 整块剔除后再 boot，验证外挂形态能正常激活）。
- **peer 依赖**：`@deepseek-ai/dsh-agent`（`Agent`、`SettleReason`、`agentEvents`）、`dsh-llm`（`ContentBlock`、`createUserMessage`）、`dsh-session`（`Session`、`SessionEvent`、`SessionEventMap` 扩展）、`dsh-skill`（`isSkillName`）、`dsh-subagent`（`SubagentResult`、`ctx.subagents.start`）、`dsh-timeout`（`deadline`、`MAX_TIMER_DELAY_MS`）、`dsh-tools`（`assertObjectJsonSchema`、`ObjectJsonSchema`）。
- **会话事件扩展**：通过 `declare module '@deepseek-ai/dsh-session' { interface SessionEventMap { 'session/distill-review-request': … } }` 注入自定义仅日志事件类型。
- **技能目录落地**：`project` 目标写入 `<git-root>/.agents/skills/<name>/SKILL.md`（`findProjectRootSync` 向上找 `.git`，缺失回落到 cwd）；`user` 目标写入 `<agentsHome>/.agents/skills/`，`agentsHome` 优先级：config → `DSH_AGENTS_HOME` → `homedir()`。这些目录由 `dsh-skill-local` 自动发现。
- **构建集成**：`scripts/build.sh` 通过 PATH 上的 `dsh` 解析 checkout 路径，把 vendored 的 cordis/cosmokit/schemastery 与各 `@deepseek-ai/dsh-*` workspace 包软链到本仓 `node_modules/`，确保 `tsc` 用与运行时一致的类型检查。

## 亮点与风险

**亮点**

- **零主对话表面改动**：插件不注册任何模型可见工具/提示，唯一副作用是磁盘上的技能文件；反省派发是记录在日志中的辅助委派（`src/index.ts:280-302`）。
- **严格的所有权护栏**：`update` 必须命中"存在 + 含 `distilled-by: dsh-distill` 标记"双条件，所有非蒸馏所有的技能（用户手写、内置、运行时注册、旧版本未带标记的蒸馏产物）一律不动，从根上避免覆盖用户资产（`src/index.ts:413-430`、`:451-462`）。
- **抗自我设限的提示词**：明确禁止把环境性失败、"某工具坏了"、未解决失败序列写成持久技能——避免后续会话把这些当作自我设限反复引用（`src/index.ts:506-520`）。
- **完整可观测性**：每次派发前写一条 `session/distill-review-request` 日志事件，携带路由/提示词/工具白名单/token 上限，使模型可见输入可从会话日志完整重建（`src/index.ts:248-256`）。
- **测试覆盖充分**：`tests/distill.spec.ts` 共 27 个用例，覆盖调度触发、阈值跳过、路由回落、所有权判定、update/create 各种拒绝路径、检查点续跑、`DSH_AGENTS_HOME`/`HOME` 解析、`parseReflection`/`renderSkillFile` 边界。
- **失败永远不崩**：派发失败、子代理异常、无结构化输出、无效提案都只 `logger.warn` 后吞掉（`src/index.ts:289-294`、`:392-401`、`:419-423`）。

**风险**

- **极新仓库、单次提交**：`git log` 只有一条提交（2026-08-05 "docs: single Chinese README"），整个历史就是今天新建的，处于早期阶段，行为可能后续调整。
- **检查点依赖日志留存**：从 `session/distill-review-request` 事件推导检查点；若会话日志被截断/清理，下次反省会从第一条用户消息重新开始（README 已知限制列出）。
- **项目目标依赖 git 根**：`findProjectRootSync` 找不到 `.git` 祖先时回落到 session cwd，可能写到非预期位置（`src/index.ts:595-604`）。
- **依赖部署的工具**：反省子代理的 `skill` 工具与目录来自同部署中的 `tool-skill`；缺它的部署反省仍会跑，但子代理无法在提案前查看现有技能内容（README 已知限制列出）。
- **整文件更新**：`update` 重写整个 `SKILL.md`，不支持局部补丁，也不支持 `references/`/`templates/`/`scripts/` 旁路文件——提示词要求把支持文件意图并入正文或跳过（README 已知限制列出）。
- **所有权标记按来源选择**：本次变更之前蒸馏出的技能没有标记，会被当作用户所有（永不更新）——历史蒸馏产物需要手动重新创建或加标记才能被继续演化（README 已知限制列出，`src/index.ts:451-462`）。
- **构建假设 PATH 上有 `dsh`**：`scripts/build.sh` 与 `probe.mjs` 都从 PATH 上的 `dsh` 解析 checkout 路径，CI/容器环境若无此软链会失败。

## 维护状态

- **提交历史**：`main` 分支仅 1 次提交（2026-08-05 07:18 +0800），作者署名 "DSH Agent"（自动化账号）。
- **代码体量**：`src/index.ts` 634 行（单一 entry）、`tests/distill.spec.ts` 791 行 27 用例、`README.md` 约 100 行中文文档；`lib/` 编译产物已随仓提交。
- **成熟度判断**：实现完整、契约清晰、测试覆盖良好，但仓库刚发布（今天），属早期阶段；无明显未完成 TODO/占位，已知限制全部在 README 显式列出。

## 备注

- 调研证据：`git clone --depth 1` 成功；`git log --oneline` 仅 1 行；`README.md`、`package.json`、`dsh.plugin.json`、`probe.mjs`、`src/index.ts`、`tests/distill.spec.ts`、`scripts/build.sh` 全部读取核对。
- 脱敏：作者署名为 "DSH Agent"（bot），无真实姓名/邮箱；GitHub 仓库名 `dsh-external/distill`。
- 与本轮调研中其他仓库的关系：本插件与 `dsh-skill-local`（技能发现）、`subagent-spawn`（默认子代理提供方）、`tool-skill`（技能查看器）共同构成"对话→反省→技能→下次发现"闭环；属于 dsh 外部插件矩阵的自适应学习一环。
- 仓库并非空占位：包含完整可运行实现与测试。
