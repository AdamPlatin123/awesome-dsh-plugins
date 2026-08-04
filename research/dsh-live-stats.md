# dsh-live-stats 调研摘要

## 一句话定位
DSH Web 的私有插件（`@dsh-external/live-stats`），在对话流式响应期间实时显示输入/输出 token 估算值与生成吞吐率（TPS，tok/s），用启发式字符密度估算，待 provider 真实 usage 到达后再校正。

## 技术栈与依赖（语言、框架、关键依赖）
- **语言/编译**：TypeScript（ESM），目标 `es2024`（服务端 Node）/`es2022`（浏览器）；构建用 `tsdown`（基于 rolldown）+ `tsc` 类型检查；测试 `vitest` + `@testing-library/react` + `jsdom`。
- **运行时框架**：Cordis（`^4.0.0-rc.7`，DSH 仓库 vendored）——插件即 `apply(ctx, config)` + `inject` 声明式服务注入。
- **配置 schema**：`schemastery`（运行时配置）+ `zod`（projection 快照 schema 校验）。
- **DSH 主仓库 peer 依赖**（均 `^0.0.1`，devDeps 用 `link:../../deepseek-harness/packages/...`）：
  - `@deepseek-ai/dsh-session`（事件类型：`SessionEvent`/`SurfaceEvent`/`EpochHeader`）
  - `@deepseek-ai/dsh-session-projection`（`ProjectionDefinition` 注册接口）
  - `@deepseek-ai/dsh-llm`（`Message`/`ContentBlock`/`StreamChunk`/`TokenUsage`）
  - `@deepseek-ai/dsh-token-meter`（`LiveTokenUsageProjection`/`TokenUsageProjection` 类型契约）
  - `@deepseek-ai/dsh-client-runtime`、`@deepseek-ai/dsh-client-ui-conversation`、`@deepseek-ai/dsh-client-ui-slots`（客户端注入与插槽）
- **UI**：React 18（peer），无独立样式系统，全部内联引用 DSH Web 的 CSS 变量（`--dsh-chat-content-width`、`--dsh-composer-side-clearance`、`--dsw-alias-label-tertiary`）。

## 文件结构概览
```
dsh-live-stats/
├── README.md                2.0KB  使用说明 + Cordis 配置示例
├── package.json             2.3KB  双产物（server ESM + client CJS 包装）
├── cordis.yml               70B    最小插件挂载配置（id+name）
├── tsdown.config.ts         1.0KB  双入口构建（含 window.__ModuleLoader__ 包装）
├── tsconfig.json            518B
├── pnpm-lock.yaml           54.5KB
├── LICENSE                  BSD-3-Clause，Copyright 2026 gordongauerk
├── src/
│   ├── index.ts             1.2KB  服务端入口：声明 inject=['sessionProjections']，
│   │                              注册 projection，导出 Config schema（schemastery）
│   ├── projection.ts        11.3KB 核心：replayable projection 状态机（liveTokenUsage）
│   ├── estimator.ts         4.0KB  纯函数：token 估算算法（chars/block/role overhead）
│   └── client/
│       ├── index.ts         713B   客户端入口：注册 composer.dock 插槽
│       └── TpsLine.tsx      1.2KB  React 视图：TPS 行（含 formatTokensPerSecond）
└── tests/
    ├── projection.spec.ts   5.0KB  projection 行为测试（retry/abort/exact 校正）
    └── tps-line.spec.tsx    1.3KB  TPS 行渲染测试
```

## 核心功能与实现要点

### 1. 注册可回放 projection（服务端入口）
- **文件**：`src/index.ts`（`apply` 函数，第 30-33 行）
- 注入 `sessionProjections` 服务，调用 `ctx.sessionProjections.register(createLiveTokenUsageProjectionDefinition(spec))`。
- projection key = `'liveTokenUsage'`，与 DSH 主仓库 `liveTokenUsage` 客户端 projection 契约（README 要求的 optional 契约）一一对应。projection 是 replayable：同一份事件日志可重放，支持时间旅行调试与崩溃恢复。

### 2. 启发式 token 估算器（纯函数）
- **文件**：`src/estimator.ts`
- 默认密度：`charsPerToken=4`、`blockOverhead=4`（每个 content block 的固定 framing）、`roleOverhead=4`（每条消息的 framing）。三者均可在 Cordis `config` 下覆盖。
- 文本类块（text/reasoning）：`Math.ceil(characters / charsPerToken) + blockOverhead`。
- tool-call 块：`Math.ceil(name/4) + Math.ceil(args/4) + blockOverhead`。
- tool-result 块：递归估内容 + blockOverhead。
- 系统提示：`Math.ceil(system.length/4) + roleOverhead`；工具 schema：`Math.ceil(JSON.stringify(tools).length/4) + blockOverhead`。
- `resolveEstimatorConfig`（estimator.ts:21）严格校验：拒绝未知 key、非正 charsPerToken、非整数 overhead——fail-fast。

### 3. 事件流 → projection 状态机（核心数据流）
- **文件**：`src/projection.ts`（`createLiveTokenUsageProjectionDefinition` 的 `apply` 函数，第 256-354 行）
- 处理 6 类 `SessionEvent`，维护 `State`（settled 累计桶 / surface 消息序列 / 当前 active step / last 上次 sample）：
  1. **`user/message` 等 surface 事件**（`applySurface`，第 109-145 行）：估算该消息 token，append 或 replace（按 `surfaceOp.start/end` seq 范围）进 `state.surface[]`，累加进 `surfaceTokens`。replace 抛错若 seq 范围非法（projection.ts:135-139）。
  2. **`step/start`**（第 269-280 行）：建 `active` 步骤，初始 `uncachedInputTokens = estimateHeaderTokens(header) + surfaceTokens`（= 系统提示 + 工具 schema + 全部对话历史估算）。
  3. **`request/header`**：保存 `EpochHeader`（system+tools），若已有 active 则即时重算 input。
  4. **`assistant/chunk`**（`applyOutputChunk`，第 148-194 行）：
     - text-delta / reasoning-delta / tool-call-delta → 累加字符数到 `active.blocks[index]`（保留 streaming 累积，不每帧重算全文）。
     - `block-end` → 用 `estimateContentTokens([block])` 锁定为 `fixed`。
     - `usage` chunk（provider 真实 usage 到达）→ `exactStep` 把 buckets 整体替换为真实值，置 `exact=true`，并补 first/latestOutputTime。
     - 每次 blocks 变化 → `outputTokens(blocks)` 重算输出 token 总数 → 写入 `active.buckets.outputTokens`；若 >0 则记录 `firstOutputTime`（首次）和 `latestOutputTime`（每次更新）。
  5. **`assistant/message`**（第 311-321 行）：若 data 带 `usage`，再次 `exactStep` 校正。
  6. **`step/end`**（第 322-342 行）：把 `active` 提交到 `last` 样本，并用 `addReplacing` 把该 step 的样本并入 `settled` 累计桶——关键：若同 turn/step 已有 `last`（重试场景），先减去旧样本再加新样本，避免重复计数。`settledEstimates` 同步维护"当前有多少个 step 是估算值"计数。
  7. **`turn/end` 且 reason.kind !== 'completed' 且 last 是估算**（第 343-354 行）：撤销该估算样本（aborted 清理），`settled` 减掉、`settledEstimates--`、清空 `last`。

### 4. TPS 计算（吞吐率核心算法）
- **文件**：`src/projection.ts`，`rateOf`（第 215-221 行）
- 公式：`tokensPerSecond = active.buckets.outputTokens * 1000 / (latestOutputTime - firstOutputTime)`。
- `firstOutputTime` 在首次出现 `outputTokens > 0` 时记录；`latestOutputTime` 随每个输出 chunk 更新（projection.ts:294-300）。
- 即：从"首 token 到达"到"最新 chunk"的墙钟跨度内累计的输出 token 数。Provider usage 校正后 `outputTokens` 会跳到真实值，TPS 也会相应反映真实吞吐（见 spec 用例 2：fake timer 1s→4s 共 3s，30 个 output token → 10 tok/s）。
- 防御：`elapsedMs <= 0 || outputTokens <= 0` 返回 undefined（不显示 TPS）。

### 5. 视图合成（`view`，projection.ts:223-238）
- 对外可见的 `LiveTokenUsageProjection` = `settled` 累计桶 + 当前 active（替换同 step 旧样本）；`estimated` 布尔由"是否存在非 exact 的 step 样本"决定；`tokensPerSecond` 优先取 active 实时速率，否则取 `last.tokensPerSecond`（最近一次完成步骤的最终速率）。

### 6. 客户端渲染：TPS 行
- **文件**：`src/client/TpsLine.tsx` + `src/client/index.ts`
- `apply`（client/index.ts:18-23）注册插槽：`ctx.slots.register({ name: 'conversation.composer.dock', id: 'live-tps', order: 1 }, TpsLine)`——挂到 DSH Web composer（输入框区）下方紧贴内置统计行。
- `TpsLine`（memo 化）：通过 `useProjection('liveTokenUsage')?.tokensPerSecond` 订阅 projection；无值返回 null；有值渲染 `<div>TPS {format} tok/s</div>`，引用 DSH CSS 变量做居中/截断。
- `formatTokensPerSecond`：<100 tok/s 保留一位小数（`Math.round(v*10)/10`），≥100 取整。

### 7. 双产物构建（tsdown.config.ts）
- 服务端 `lib/index.js`：ESM，Node es2024，不打 dts。
- 客户端 `lib/client.js`：CJS，浏览器 es2022，**关键**：用 `window.__ModuleLoader__.load({ id, factory: require => {...} })` 包装，intro 注入 `var module = { exports: {} };`——适配 DSH Web 的客户端模块加载器沙箱。`neverBundle` 列出 cordis/react/DSH client runtime，由宿主在运行时注入。

## 与 DeepSeek Harness 主仓库的集成点
插件通过两条标准 seam 接入 DSH：

1. **服务端 projection seam**（`@deepseek-ai/dsh-session-projection`）：
   - `ctx.sessionProjections.register(definition)` 注册一个 `ProjectionDefinition<'liveTokenUsage', State>`。
   - projection key `'liveTokenUsage'` 必须与 DSH 客户端 `@deepseek-ai/dsh-token-meter/client` 暴露的 `LiveTokenUsageProjection` 契约匹配（README "Requirements" 显式声明）。
   - projection 接收 `SessionEvent` 流（`step/start`、`request/header`、`assistant/chunk`、`assistant/message`、`step/end`、`turn/end` 以及 `user/message` 等 surface 事件），全部由 DSH session 层产出。

2. **客户端 slot seam**（`@deepseek-ai/dsh-client-ui-slots` + `conversation`）：
   - `ctx.slots.register({ name: 'conversation.composer.dock', ... }, TpsLine)` 占据 composer 下方 dock。
   - 客户端用 `useProjection('liveTokenUsage')`（来自 `@deepseek-ai/dsh-client-runtime/client`）订阅服务端 projection 的快照。

3. **加载方式**：`./bin/dsh web --config cordis.yml`（Cordis 插件加载），`package.json` 的 `dshClient.inject` 字段声明客户端需要 DSH 注入 `dsh-client-runtime` 与 `dsh-client-ui-conversation` 模块。
4. **开发联调**：devDeps 全部 `link:../../deepseek-harness/packages/...`——要求插件 checkout 与 harness checkout 在兄弟目录布局（`~/Projects/dsh-live-stats` 与 `~/deepseek-harness`）。

## 亮点与风险

### 亮点
1. **关注点分离干净**：`estimator.ts`（纯函数，零副作用，可单独测试）— `projection.ts`（不可变状态机 reducer，每次 apply 返回新 state，天然 replayable）— 客户端 React 视图（仅消费 projection 快照），三层耦合极低。
2. **双精度策略**：流式期间用字符密度近似实时刷新，provider usage 到达后整体替换 buckets（`exactStep`），`estimated` 标志透明告知用户当前数字来源——既保证响应感又最终对齐真实计费。
3. **重试与中断感知**：`addReplacing`（projection.ts:33-41）以 `(turn, step)` 为复合键，重试同一步骤时先减旧样本再加新样本；abort 场景下未确认的估算样本在 `turn/end` 被回滚——不会污染累计。
4. **可配置 + 严格校验**：三个密度参数可调，`resolveEstimatorConfig` fail-fast 拒绝未知 key 与非法值，避免静默误配。

### 风险
1. **CJK/非拉丁文本严重低估**（`src/estimator.ts:13-15, 53-58`）：默认 4 chars/token 适合英文，中文实际约 1.5-2 chars/token，会显著少估输入/输出 token，使 `estimated` 数字系统性偏低。无语言检测或自适应密度，需部署方手动调高 `charsPerToken` 之外的方案。
2. **TPS 抖动无平滑**（`src/projection.ts:215-221`）：`rateOf` 直接用累计 token / (latest - first)，首 token 后窗口极短时 TPS 易飙高；仅以 `elapsedMs > 0` 防御除零，没有 EMA/滑动窗口/最小窗口，用户会看到数字跳变。
3. **surface replace 抛异常会中断整个 projection**（`src/projection.ts:135-139`）：`applySurface` 在 seq 范围非法时直接 `throw new Error`，而不是降级跳过——若上游 event 序列出现意外，整个 session 的 liveTokenUsage projection 会崩。
4. **客户端强耦合 DSH Web 全局加载器**（`tsdown.config.ts:24-26`）：客户端 bundle 硬编码 `window.__ModuleLoader__.load(...)` banner/footer，依赖 DSH Web 运行时定义该全局；若加载器 API 变更，构建产物直接失效，无版本协商。
5. **peer 依赖版本脆弱**（`package.json` peerDependencies）：所有 `@deepseek-ai/dsh-*` 均 `^0.0.1`（pre-1.0），任何 breaking change 都可能在 patch 版本内发生；`liveTokenUsage` 契约本身在 README 里也被标注为"optional"，存在被主仓库移除/重命名的风险。无 CI 配置文件可见（仓库内无 `.github/`），回归保护依赖本地 `pnpm test`。

## 维护状态
- **default_branch**：`main`（仅此一个远程分支，`origin/main`）。
- **最近提交**：`7a41575 feat: add live token and TPS plugin`，作者 Proton，日期 **2026-08-04**（depth-1 clone 仅可见此 1 个 commit，昨天刚创建）。
- **提交活跃度**：极低（可见范围内单次初始提交），属新立项仓库。
- **README 质量**：**高**——清晰给出功能定位、示例输出、Cordis 配置示例（含三个可调参数）、Requirements、构建/测试/加载/热更新完整命令、License。是 dsh-external 私有插件中 README 最完整的范本之一。
- **测试覆盖**：2 个 spec 文件覆盖核心场景（估算参数解析、流式+usage 校正、retry/abort、TPS 格式化与渲染时机），质量良好但未覆盖 CJK/边界密度。

## 备注
- 版权署名 `gordongauerk`（LICENSE），提交作者 `Proton`——典型的 DSH 生态笔名式归属。
- 仓库体积 1964KB 主要来自 `pnpm-lock.yaml`（54.5KB）+ `src/lib` 源码，整体精简。
- 客户端 contribution 通过 `order: 1` 插槽排序紧贴内置统计行，README 描述的"第二行 TPS"效果即由此实现。
- 启发式参数 `blockOverhead=4`/`roleOverhead=4` 反映的是常见 chat 模型的 framing 开销经验值，但对带大量工具调用的场景可能仍偏低（实际 tool-call framing 常远大于 4 token）。
