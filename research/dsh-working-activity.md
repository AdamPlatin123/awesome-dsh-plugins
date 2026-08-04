# dsh-working-activity 调研摘要

## 一句话定位
DeepSeek Harness 的实时"模型工作状态行"插件：把会话事件流（`turn/start`、`assistant/chunk`、`tool/call`、`tool/result`、`turn/end`）和 `agent/status` 折叠成一个俏皮的实时状态文案，同时输出到 TUI prompt 槽位 `${activity}` 和 Web UI 的状态标签（`WorkingLine`/`TurnStatus`）。

## 技术栈与依赖
- **语言/运行时**：TypeScript（ESM，`type: "module"`），目标为 DSH monorepo（pnpm workspace）的 cordis 宿主插件
- **构建/产物**：`lib/index.js` + `lib/types/*.d.ts`；`exports` 同时暴露 `./src/*` 便于源码级引用
- **运行时依赖**：`schemastery ^3.18.0`（配置 schema）
- **Cordis peerDeps**（DSH 内部包，未发 npm）：
  - `@deepseek-ai/dsh-agent`（`AgentStatus` 类型）
  - `@deepseek-ai/dsh-invariants`（事件不变量校验框架）
  - `@deepseek-ai/dsh-session`（`Session`、`SessionEvent`、`SessionEventMap` 扩展）
  - `@deepseek-ai/dsh-system-prompt`（注入 `⏵` 自述约定）
  - `cordis ^4.0.0-rc.7`（插件宿主）
- **测试**：`vitest`（4 个 spec：integration / narration / phrases / status，README 自述共 34 项）
- **许可证**：插件代码 BSD-3-Clause；仓库说明文档 MIT
- **版本/状态**：`0.0.1`，`private: true`（不发 npm，源码级分发）

## 文件结构概览
```
dsh-working-activity/
├── README.md                       4.5KB   顶层说明（中文，含安装/配置/已知限制）
├── LICENSE                         1.1KB
├── patches/
│   └── webui-working-activity.patch  27.8KB  Web UI 集成补丁（基于官方 0804 快照，改 12 个文件）
└── packages/activity/working-activity/        插件本体
    ├── package.json                1.6KB
    ├── README.md / README.zh.md    6KB    双语说明（含配置表、配置示例）
    ├── README.i18n.yaml            444B
    ├── tsconfig.json
    ├── src/
    │   ├── index.ts        8.6KB   apply()：事件订阅、TUI/Web 两个出口、tick 渲染、⏵ 注入
    │   ├── status.ts       18.6KB  纯状态机 ActivityTracker（5 阶段，时钟注入）
    │   ├── phrases.ts      12.4KB  8 个内置文案池 + 随机选择器
    │   ├── events.ts       1.7KB   `activity/status` 事件类型 + SessionEventMap 扩展
    │   └── invariant.ts    2.9KB   伴生不变量校验插件
    └── tests/
        ├── status.spec.ts       7.9KB
        ├── narration.spec.ts    6.1KB   ⏵ 自述抽取/新鲜度/工具行前缀
        ├── integration.spec.ts  7.3KB
        └── phrases.spec.ts      2.9KB
```

## 核心功能与实现要点

### 1. 文案来源：**全部内置静态池**，无 LLM 生成（`src/phrases.ts`）
- 8 个硬编码池：`THINKING_PHRASES`（思考 ~90 条）、`WAITING_PHRASES`（等首 token ~43 条）、`ACTION_MAP`（17 个工具名正则 → 动作词池）、`FAIL_PHRASES`（失败 ~35 条）、`DONE_PHRASES`（收尾 ~38 条）、`NIGHT_PHRASES`（深夜 00:00–06:00 混入 ~17 条）、`THINKING_TIERS`（30s/60s/300s 三档升级文案）、`FALLBACK_ACTIONS`（未知工具的兜底动词）。
- 选择器 `pickPhrase(entries, previous)` 随机抽取，并尽量避免与上一次重复（最多重试 8 次，`phrases.ts:14-22`）。
- 用户可通过配置 `customActions: {工具名: [词1, 词2, ...]}` 提供自定义池（大小写不敏感精确匹配，优先于内置 `ACTION_MAP`，`phrases.ts:144-153`）。
- 全局开关 `phrases: false`（默认 true）让所有文案退化为朴素功能标签（`思考中`/`等待模型响应`/`搞定 ✓`/工具原名），`status.ts:renderThinking/doneSummary`。

### 2. 状态机：纯函数 + 时钟注入（`src/status.ts`）
- `ActivityTracker` 类管理 5 个 phase：`idle / waiting / thinking / tool / done`。
- 时钟通过构造器注入 `now: () => number = Date.now`，使其在测试中完全确定性（`tests/narration.spec.ts:fixedClock`）。
- 输入是 `onSessionEvent(event)` + `onAgentStatus('idle'|'running')`；输出是 `render(nowMs?): ActivityState`，可被任意 UI 渲染。
- 维护的内部状态：当前 phase、phase 起始时间、turn 起始时间、`thinkingMs/toolMs/toolCount` 分桶、`activeTools Map`、`doneQueue`（最近 6 个）、`turnTokens`、`recentStream` 缓冲（300 字符滚动窗）、`narratedText`。
- done 摘要：`搞定 ✓ · N 工具 · 想Xs 干Ys · 🔥 token`；前缀在 `turn/end` 时只抽一次随机词避免闪烁（`status.ts:turn/end` 处理逻辑 + `narration.spec.ts` 的"done-line stability"测试专门验证）。

### 3. 订阅模型工作状态：通过 cordis 事件（`src/index.ts:apply`）
- **会话事件**：`ctx.on('session/event', (session, event) => { tracker.onSessionEvent(event); publish(...) })`——一次性接住所有 `turn/*`、`assistant/*`、`tool/*`。
- **agent 状态**：`ctx.on('agent/status', (agent, status) => { tracker.onAgentStatus(status); publish(...) })`——收到 `running` 推进到 `waiting`，收到 `idle` 清理停留的 done 卡片。
- **会话销毁**：`ctx.on('session/disposed', ...)` 清理对应的 `ActivityTracker`，避免内存泄漏（`index.ts`）。
- 每个 `Session` 一个独立的 `ActivityTracker`，存于 `trackers: Map<Session, ActivityTracker>`，单 agent 视图。

### 4. 两个出口（消费机制）
- **TUI 槽位**：`ctx.get('tuiPrompt', false)?.register('activity', undefined)`，拿到 `{ set(value), dispose() }` 句柄；每次 publish 时 `promptHandle.set(line)`（idle 时 `undefined` 清空槽）。用户需把 `${activity}` 加进 `theme.leftPrompt` 模板。TUI 未组合时不报错，效果为零。
- **Web / 任意 UI**：默认开启 `publish: true` 时，通过 `session.append('activity/status', payload)` 写入会话事件流。节流策略：line 变化或 phase 变化 → 立即发；live phase（非 idle/done）每 `publishIntervalMs`（默认 2000ms）至少发一次以刷新耗时；idle/done 仅在 line 变化时发。
- **持续 tick**：`setInterval(resolved.tickMs)`（默认 500ms）周期重渲染当前活跃会话，使已耗时和文案轮换自然推进；`ctx.effect(() => () => clearInterval)` 保证 fiber 卸载时清理。
- **log-only 语义**：`activity/status` 通过 `declare module '@deepseek-ai/dsh-session'` 扩展 `SessionEventMap`（`events.ts`），明确标注"never a surface event"——不进入派生模型历史，模型看不见，回放时被忽略，类似 `todo/write`/`plan/mode`。

### 5. ⏵ 模型自我叙述机制（`narrate`，默认开启）
- **注入**：`narrate: true` 时，在 cordis 上下文里 `ctx.inject(['systemPrompt'], ...)` 调用 `ctx.systemPrompt.section({ name: 'working-activity:narrate', order: 60, text: NARRATE_INSTRUCTION })`，把一段中文约定写入系统提示词（`index.ts` 顶部 `NARRATE_INSTRUCTION` 常量）：要求模型在每个子任务开始时，在回复正文**首行单独**写 `⏵ 你在做的具体事情（≤20 字）`，换行后继续正常回复，整轮只写一行。
- **抽取**：状态机维护 `recentStream`（最近 300 字符滚动缓冲，`STREAM_BUFFER_CHARS=300`，`status.ts` 常量），用正则 `/⏵\s*([^\n⏵]{1,40})/g` 取最后一次匹配作为 `narratedText`（`extractNarration()`，`status.ts`，附 `narration.spec.ts` 4 项专门测试）。
- **渲染**：thinking / waiting / tool 阶段的 `line` 在有新鲜 narration 时前缀 `⏵ ${narration}`（如 `⏵ 跑一下测试 · 跑个命令 npm test · 2s`），并赋给 `state.phrase` 字段。
- **新鲜度窗口**：`NARRATE_GRACE_MS = 5000`——流停顿超过 5 秒就回落到内置文案池（避免陈旧自述卡住）。
- **正文过滤**：注：README 提到"聊天正文自动过滤该行（日志保留）"，但**过滤逻辑不在此插件**，而在 Web UI 补丁的 ui-conversation 渲染侧（见 `patches/webui-working-activity.patch`）；本插件只负责抽取并展示，不动模型正文。

### 6. 不变量伴生插件（`src/invariant.ts`）
- 独立的 cordis 伴生（`name: 'working-activity-invariant'`，`inject: ['invariants']`），通过 `ctx.invariants.register(PACKAGE_NAME, install)` 注册 `activity/status` 载荷的结构校验：phase 必须在 5 个枚举内、`line` 非空、数值字段非负有限、可选字段为字符串——既校验已落盘事件，也通过 `internal/dispatch` 拦截新追加事件。
- Web 客户端侧（patch 中新增 `packages/client/runtime/src/client/sessions/activity.ts`）有镜像的 `parseActivityStatusData()` 结构校验，host 类型不进入 client 程序（避免 cordis Context merge 冲突），双端独立窄化。

## 与 DeepSeek Harness 主仓库的集成点
- **挂载方式**：作为 cordis 插件，在 `cordis.yml` 中 `plugins: - id: working-activity` 启用；包路径需复制到 DSH monorepo 的 `packages/activity/working-activity/`，并在 `tsconfig.host.json` 的 `references` 加该包引用，`tsconfig.base.json` 的 `paths` 含 `./packages/activity/*/src`。
- **协议/seam**：
  1. **会话事件流**：消费 `turn/start | assistant/chunk | assistant/message | tool/call | tool/result | turn/end`；产出 `activity/status` 事件（`SessionEventMap` 模块扩展）。
  2. **TUI prompt 服务**：`ctx.get('tuiPrompt')`（来自 `@deepseek-ai/dsh-tui`）的 `register(name, initial)` 槽位 API。
  3. **系统提示词服务**：`ctx.systemPrompt.section({name, order, text})`（来自 `@deepseek-ai/dsh-system-prompt`）注入 `⏵` 自述约定。
  4. **agent 状态**：`ctx.on('agent/status', ...)` 监听 `@deepseek-ai/dsh-agent` 的运行/空闲。
  5. **不变量框架**：`ctx.invariants.register(...)`（来自 `@deepseek-ai/dsh-invariants`）。
  6. **Web UI**：通过 `patches/webui-working-activity.patch` 给 `packages/client/runtime` 和 ui-conversation 打补丁，新增 `ActivityStatusView` wire 类型 + 解析器，并把状态渲染进 `WorkingLine` 和 `TurnStatus` 组件（共改 12 个文件，基于官方 0804 快照 `20260804T143803Z`）。

## 亮点与风险
### 亮点
1. **隐私友好**：README 与代码一致声明——不采集、不上传、无网络请求、无遥测；`activity/status` 是 log-only 事件，模型看不见，不进 surfaceOp，回放忽略。
2. **状态机纯函数化**：`ActivityTracker` 无 I/O、无定时器、无 cordis 依赖，时钟可注入；测试完全确定性（`fixedClock`），便于回归。
3. **publish 节流设计扎实**：live phase 节流刷新耗时、idle/done 仅 line 变化才发，避免无效写入；snapshot 在事件回调时取，避免同步连发（如 tool/call+result）丢失中间 phase。
4. **双端独立窄化**：host 插件与 client runtime 各自维护 `ActivityStatusView` 类型校验，规避 cordis Context 类型合并冲突，符合 DSH 跨线事件契约惯例。

### 风险与小提示
1. **文案重复避免有边界**（`phrases.ts:14-22`）：`pickPhrase` 重试上限 8 次；当池只有 2 条时理论上仍可能命中重复（虽概率极低），未硬保证不重复。
2. **`customActions` 大小写折叠**（`phrases.ts:146-148`）：通过 `toolName.trim().toLowerCase()` 匹配，配置里同时给 `Bash` 和 `bash` 会被静默合并为同一个池——文档未提示。
3. **节流状态在 apply 闭包内是单例**（`index.ts:apply`）：`lastPublishedLine / lastPublishedPhase / lastPublishAt` 是闭包级、跨会话共享，多会话切换活跃源时非活跃会话的下次发布会基于上一次活跃会话的"上次发布"判断——多会话场景可能少发若干快照（功能不破坏，仅略影响非活跃会话的节流精度）。
4. **测试无法独立运行**（`package.json` devDeps 全是 `workspace:^`）：单测需在 DSH monorepo 内执行 `pnpm test`；外部贡献者裸 clone 后 `vitest` 跑不起来。
5. **文案池偏中文 + 部分 ASCII 拟声**（`phrases.ts`）：`lol/hm/oh/ok/um/heh/uh/nah/mm/wow/nice/rgrg/okk/hhh/emm/emmm` 等混在 THINKING 池，国际化场景若做翻译需自行重写池（无 i18n 文件机制，仅硬编码数组）。
6. **patch 时效性强**：`patches/webui-working-activity.patch` 基于 `20260804T143803Z` 官方快照生成；DSH 主仓库 UI 持续演进后可能需手工 rebase（README 已声明此约束）。

## 维护状态
- **default_branch**：`main`
- **最近 push**：2026-08-04（commit `7acd885` "docs: note language-stats refresh trigger"，距今 1 天，今天 2026-08-05）
- **提交活跃度**：depth=1 浅克隆只暴露 2 个 commit（`7acd885` docs + `5f67fb2` docs: publish under dsh-external org），看起来刚发布到 dsh-external org 不久；非长期迭代项目，目前为初版（`version: 0.0.1`）。
- **README 质量**：优秀。顶层中文 README 含特性/目录/安装（4 步）/配置表（7 项 key 含类型默认值含义）/隐私与安全/已知限制/开发命令；插件包内还有双语 README（`README.md` + `README.zh.md`）+ `README.i18n.yaml`，覆盖度高于平均水平。

## 备注
- 作者署名 chimney（GitHub `ccch1mneyyy`），DSH 社区贡献，非官方出品。
- 风格灵感明示对齐 `pi-working-activity`（`phrases.ts` 头注 "matching the pi-working-activity tone"）——文案风格可视为同一系列。
- 安全姿态正面：所有用户可控面（`customActions`、文案池）只存在本地配置，正则匹配工具名，无 `eval`/`new Function`/模板字符串注入路径。
- 集成路径建议先开 `phrases: true + narrate: true`（默认）体验完整效果，再视情况关 `narrate`（避免提示词 token 占用）或关 `phrases`（朴素模式适合正式场合）。
