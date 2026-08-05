# dsh-memory-evolve

## 一句话定位
DeepSeek Harness 的「跨会话长期记忆 + 后台自我进化」纯插件——四层分层记忆（用户档案 / 全局事实 / 项目记忆 / 每日日志）+ 周期性后台审查子代理（增量转录 + 经验沉淀）+ 技能自动创建/优化，零核心改动、零运行时依赖。源码注释自称 **Hermes 机制复刻**（`Hermes-style` / `Hermes-compatible`），最新提交专门清除用户可见的 Hermes 痕迹。

## 技术栈与依赖
- **语言**：JavaScript（Node.js ESM，`"type": "module"`），Web 端客户端用 TypeScript + React（`src/client/*.tsx`）。
- **运行时依赖**：**0**（纯 `node:fs` / `node:crypto` / `node:child_process` / `node:http` / `node:url`，文件级锁用 `Atomics.wait + SharedArrayBuffer` 同步睡眠）。
- **DSH 客户端**：`dshClient.inject = ["@deepseek-ai/dsh-client-runtime"]`，`platform: "web"`；导出 `.`（主插件）与 `./client`（Web UI 包）。
- **构建/测试**：`node --test 'tests/*.test.js'` 原生测试器；`scripts/build.mjs` 打包；`tsdown`/React 类型走 `tsconfig.json`。
- **License**：MIT；`private: true`（不发布 npm）。

## 文件结构概览
```
dsh-memory-evolve/
├── lib/                       # 编译产物（运行时入口）
│   ├── index.js      (532行)  # apply()、resolveConfig、renderSnapshot、resolveRevealTarget、记忆工具
│   ├── store.js      (535行)  # MemoryStore / SuggestionQueue、文件锁、漂移检测、注入扫描
│   ├── review.js     (561行)  # installReview、buildReviewPrompt、suggestToolDefinition、批准/拒绝
│   ├── skills.js     (409行)  # skill_manage 工具、read-before-write、pending-skills 队列
│   ├── digest.js              # buildDigest 会话转录重建（仅对话，过滤工具/思考/系统注入）
│   ├── api.js                 # Web HTTP API（/memory-evolve/api/* 路由）
│   ├── memory-tab.js          # 会话页「记忆」Tab 文件视图
│   └── client.js     (48.7KB) # Web UI 编译产物（设置面板 + 记忆 Tab）
├── src/client/                # Web UI 源码（TypeScript + React）
│   ├── index.ts / MemoryPanel.tsx / MemoryTabView.tsx / styles.css
├── tests/                     # 6 个测试文件，≈70 个 test() 用例
│   ├── plugin.test.js (31.9KB) / skills.test.js / store.test.js
│   ├── digest.test.js / api.test.js / memory-tab.test.js
├── docs/rules.md     (10KB)   # 行为规则说明（四层记忆 + 审查产出规则）
├── package.json / tsconfig.json / README.md (13.3KB) / LICENSE
```

## 核心功能与实现要点

1. **四层记忆轨道**（`lib/store.js` `MemoryStore`、`lib/index.js` `renderSnapshot`）：用户档案 `USER.md`、全局事实 `MEMORY.md` 每会话注入（低频变化、缓存友好）；项目记忆 `projects/<sha1(cwd)>/MEMORY.md` 与每日日志 `daily/YYYY-MM-DD.md` **不注入**，靠固定提示行引导模型按需用 `memory` 工具读取——避免每轮破坏 LLM 前缀缓存（`lib/index.js:217-243` 注入策略 + 注释解释）。

2. **后台审查机制**（`lib/review.js` `installReview` + `lib/digest.js` `buildDigest`）：监听 `agent/settled` 计数每 N 回合触发；从持久化水位线（`review-watermarks.json`，进程重启不丢）起重建**增量**只读转录——仅含用户输入与助手文本，工具调用/思考/系统注入一律剔除（`digest.js:38-100`）；派生受限子代理（工具白名单 `memory` / `memory_suggest` / `skill_manage`，可选 `agent_session_read`）；`origin: 'subagent'` 会话永不触发（防递归）；同时仅一个审查在飞，15 分钟安全超时释放槽位（`review.js:18-25`）。

3. **建议确认制 + 技能待确认队列**（`lib/review.js` `suggestToolDefinition` / `lib/skills.js` `approvePendingSkill`）：全局轨（user/memory）只能由审查子代理经 `memory_suggest` 进 `SUGGESTIONS.jsonl` 队列，重复内容去重并累计 `hits` 频次（`review.js:243-280`）；新技能默认进 `pending-skills/` 目录，用户在 Web 设置面板采纳后才 `rename` 进 `~/.agents/skills` 立即生效（`skills.js:185-205`）。

4. **技能自我进化 + read-before-write 保护**（`lib/skills.js` `skillManageTool` / `hasReadSkill`）：`skill_manage` 工具支持 create / patch / read / list；patch（优化已有技能）前必须先在会话日志中找到 `skill_manage action=read <name>` 的 `tool/call` 事件（`skills.js:262-285`），凭空改写他人技能会被拒；写入前还会查 DSH 核心 `ctx.skills` 注册表跳过 `modelInvocable: false` 的禁用技能（`skills.js:306-318`）。

5. **Web UI 三入口**（`lib/api.js` `installApi` + `src/client/`）：设置面板「记忆管理」（待确认建议/技能、运行时配置表单、一键打开文件，徽标 `记忆管理 (N)`）+ 可选「会话页记忆 Tab」（预览/编辑记忆文件）+ `/memory-evolve/api/*` HTTP 路由（badge、suggestions、config、reveal、memory-files、pending-skills）；`httpServer` 不存在时（如 TUI）插件静默降级（`index.js:482-506` `ctx.inject(['httpServer'], ...)`）。

6. **用户命令**（`lib/index.js:508-533`）：`/memory_review [approve|reject N...]`、`/memory_now` 立即触发一次审查；`commands` 服务不存在时静默跳过。

7. **安全设计**（散落各处）：跨进程文件锁（`store.js:91-141` `withLock`，10s 视为 stale、5s 超时）；原子写（`tmp.${pid}` + `rename`）；漂移检测——文件无法解析器往返时拒绝重写并备份 `.bak.<时间戳>`（`store.js:361-380`）；提示注入扫描中英双语模式（`store.js:144-160` `scanThreat`）；字符上限硬拒绝；技能名 kebab-case 同时排除路径穿越；YAML frontmatter 兼容性校验（`description` 必须双引号）。

## 与 DeepSeek Harness 主仓库的集成点
- **纯插件、零核心改动**：仅用公开 seam——`tools`（注册 memory / memory_suggest / skill_manage 工具）、`systemPrompt`（注入记忆快照，DSH 物化为 user-role 尾部消息）、`commands`（`/memory_review`、`/memory_now`）、`subagents`（`spawn` 派生审查子代理 + `toolFilter` 白名单）、`approval`（auto 模式写前批准）、`httpServer`（Web API）、`skills`（查禁用状态）、`agents`（按 sessionId 解析 cwd）；全部注册都是 fiber `ctx.effect`，卸载即恢复（`index.js:423-533` `apply`）。
- **目录约定**：记忆默认 `$DSH_HOME/memories`（即 `~/.dsh/memories`），技能默认 `~/.agents/skills`（DSH 技能库，与外部扫描器共享）。
- **客户端注入**：`dshClient.inject = ["@deepseek-ai/dsh-client-runtime"]`，Web 平台——配合 DSH Web 的 ui-slots/ui-settings 渲染面板。
- **可选协同插件**：
  - `dsh-session-search`（同 org 私有仓）：安装后自动把 `agent_session_read` 加入审查子代理白名单，实现「深读」完整会话；未装也不影响摘要式审查（`README.md` 可选增强章节）。
  - `dsh-skills-manager`：通过共享 `ctx.skills` 运行时注册表识别被禁用技能；不装时降级为「不视为禁用」（`skills.js:306-318`）。
- **catalog 注册**：hub `catalog.json` / `plugins.json` 列为 marisa + cordis 管理的 plugin 类目，tags `["memory", "skill"]`。

## 亮点与风险（附文件:行号）

**亮点**
- **缓存友好的分层注入**（`lib/index.js:217-243`）：明确区分「低频全局轨（注入）」与「高频项目/每日轨（按需读取）」，并诚实标注已知局限——任何全局轨写入仍会破坏前缀缓存（DSH 核心机制固有），README「已知局限：缓存命中」章节展开说明。
- **三层写入松紧策略 + 严格创建门槛**（`docs/rules.md` §3、`lib/review.js` `buildReviewPrompt`）：daily/project 宽松自动沉淀，全局轨严格走确认队列；技能创建需同时满足「多次踩坑 + 难度大 + 可复用」，禁止一次性任务命名。
- **read-before-write 防凭空改写**（`lib/skills.js:262-285`）：patch 必须在会话日志留下 read 证据；`skill_manage` 工具同时面向审查子代理与普通会话。
- **完善的测试覆盖**：≈70 个 `node --test` 用例覆盖配置校验、四轨读写、增量审查、水位线持久化、跨进程锁、漂移检测、注入扫描、技能 read-before-write、Web API 路由（`tests/*.test.js`）。

**风险**
- **代码极新**：catalog `pushedAt: 2026-08-05T14:36:19Z`（与调研同日），浅克隆仅见 1 条提交 `8319edc chore: remove all user-visible Hermes traces`——历史深度未知，刚上线、生产稳定性待观察。
- **审查子代理提示注入面**（`lib/review.js` `buildReviewPrompt`）：转录来自用户会话，恶意内容可被审查子代理「建议」进队列；缓解依赖用户确认制 + 写入扫描，但 `autoApproveGlobal` / `skillReviewEnabled` 一旦开启即绕过确认（默认关，README 显式警告提示注入风险）。
- **硬编码开发者路径**（`tsconfig.json:13-37`）：`paths` 指向 `/Users/edgar/...` 的 DSH 源码 pnpm 目录——仅影响类型检查（`noEmit`），但说明是在 macOS 单人环境开发，他人贡献门槛偏高（脱敏：此处仅路径，不含账号/邮箱）。
- **跨进程锁阻塞主路径**（`lib/store.js:91-141` `withLock`）：同步阻塞 + `Atomics.wait` 睡眠，5 秒超时；多 DSH 进程并发或外部编辑器持锁时会拒绝写入并抛错——非致命但需要运维知晓。
- **审查依赖 `subagents` + 外部模型**：`reviewProvider/reviewModel` 默认空（用主模型）；无 `subagents` 服务的客户端表面（部分 TUI）会静默跳过审查，仅记忆工具可用。

## 维护状态
- **活跃**：pushedAt 2026-08-05（调研当日），hub catalog 今日 14:50 重新生成时已纳入并标记 `empty: false`（早先 `catalog.source.json` 标 `empty: true`，现已过时）。
- **管理者**：marisa + cordis（来自 `plugins.json`）。
- **成熟度信号**：完整 README（13KB）+ 独立 `docs/rules.md`（10KB 行为说明）+ ≈70 个测试用例 + 详细 JSDoc——文档与测试密度高于 org 内一般插件，但提交历史浅、上线极新。

## 备注
- 仓库为私有（org `dsh-external` 的 `public_repos: 0`），未认证 API/Web 抓取均 404；本次通过 `hub op:start git clone`（凭证由环境注入）拉取成功，浅克隆仅见 1 条提交。
- 源码 docstring 仍多处提及 Hermes（如 `store.js:1-20`、`review.js:1-22`、`skills.js:13-26`），README 与工具描述已被清洗为「DSH 长期记忆」措辞——可推断是对上游 Hermes 记忆系统的复刻/移植，Hermes 本体不在本 org。
- 与同仓 `distill`（自动对话蒸馏）功能有部分重叠，但定位不同：distill 偏「对话→技能」的实时蒸馏，本仓偏「跨会话持久记忆 + 周期审查」。
