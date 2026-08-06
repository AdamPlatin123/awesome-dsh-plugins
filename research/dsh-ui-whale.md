# dsh-external/dsh-ui-whale

## 一句话定位
DSH Web UI 的常驻像素鲸鱼伙伴插件——在会话标题栏（`conversation.session.header.actions` 槽位）常驻一只 25×40 像素鲸鱼，随会话快照（running / reasoning partial / 工具调用）实时切换情绪与动画，**零核心改动**的纯客户端 UI 装饰插件。

## 技术栈与依赖
- **语言/运行时**：TypeScript（`typescript ^5.9.3`）、ESM（`"type": "module"`）、React 18（peer `^18.2.0`）、cordis 4（peer `^4.0.0-rc.7`）。
- **构建/测试**：`tsdown ^0.22.2`（产物到 `lib/{index,invariant,client}.js`）、`vitest ^4.1.1` + jsdom + `@testing-library/react ^16.1.0`、`lightningcss`、`vite-tsconfig-paths`。包管理 pnpm（`pnpm-lock.yaml` 在库）。
- **DSH 依赖（均为 link:）**：`@deepseek-ai/dsh-client-locale` / `-runtime` / `-ui-conversation` / `-ui-slots` / `-test-runtime` / `dsh-invariants`，全部 link 到 `../.dsh/source/current/...` 的 DSH 已构建快照——**离开 DSH 主仓快照无法独立 install/build**。
- **engines**：`dsh >=0.0.1`；`private: true`（不可发布 npm）；BSD-3-Clause；版本 0.1.0。

## 文件结构概览
```
dsh-ui-whale/
├── dsh.plugin.json          # 插件清单（id=dsh-ui-whale, contributes.tools/skills 均为 []）
├── package.json             # dshClient.inject 声明 + exports 映射
├── INSTALL.md               # 组织内安装手册（link / git 依赖两条路径 + config.yaml）
├── README.md                # 用户文档 + 内嵌 demo 视频
├── tsdown.config.ts / tsconfig*.json / vitest.config.ts
├── lib/                     # 构建产物（已入库）：index.js / invariant.js / client.js (31.5KB)
├── src/
│   ├── index.ts             # Node half：空 apply（仅占位让插件出现在 cordis.yml）
│   ├── invariant.ts         # 包所有权 invariant companion（无运行时 invariant）
│   └── client/
│       ├── index.ts         # 浏览器 half：注册 locale 命名空间 + WhalePet 到 header 槽
│       ├── WhalePet.tsx     # React 组件：读快照 → 驱动 tick 动画
│       ├── animation.ts     # 纯 tick 状态机（TICK_MS=120ms，5 种 mood）
│       ├── sprite.ts        # 分层 box-shadow 像素画（body+eye+tail+fin+spout）
│       ├── sprite-data.ts   # 13 帧 25×40 像素矩阵（STANDARD/BLINK/FIN_1-2/SPOUT_1-6/TAIL_1-3）
│       ├── locales.ts       # zh（key 来源）+ en 字典
│       └── WhalePet.module.css  # 调色板变量 + 1x1 box-shadow 渲染 + 缩放
├── sprites/                 # 帧矩阵原始存档（whale-raw.txt / whale-frames.json）
├── tests/                   # animation.spec.ts / sprite.spec.ts / browser-plugin.spec.tsx
└── docs/dsh-ui-whale-demo.mp4  # 演示视频（~0.9MB）
```
共 31 个 git 跟踪文件、约 7930 行（绝大部分为 sprite 像素矩阵 + lock 文件）。

## 核心功能与实现要点
1. **三段式插件结构**（与 DSH 客户端插件契约一致）：Node half（`src/index.ts`）apply 为空，仅为出现在 host `cordis.yml`；invariant companion（`src/invariant.ts`）注册包所有权但无运行时 invariant；浏览器 half（`src/client/index.ts`）通过 `dshClient.inject` 声明（`@deepseek-ai/dsh-client-locale` / `-runtime` / `-ui-conversation`）被发现。
2. **槽位注册**（`src/client/index.ts:30-44`）：`inject = ['slots','conversation','locale']`，先 `ctx.locale.register('whale', {zh,en})`，再 `ctx.inject(['slots','conversation','sessions'], ...)` 内 `scope.slots.register({ name: 'conversation.session.header.actions', id: 'whale', order: 30, locale: 'whale' }, WhalePet)`——`conversation` 是 ordering edge，保证 header.actions 槽已声明后再注册。
3. **分层像素画**（`src/client/sprite.ts`）：13 帧 25×40 网格、5 色调色板（`#203864`/`#0066FF`/`#B4C7E7`/`#F2F2F2` + 透明）。每个动画区域（tail/fin/spout）由"该动作任一帧相对 STANDARD 变化的单元格集合"自动推导（`motionRegion`），BODY = STANDARD 减去眼瞳与所有运动区——避免静体覆盖动体。`framePixelsFor(state)` 拼出 body+eyes+tail+fin+spout 的完整像素集。
4. **渲染**（`WhalePet.tsx` + `WhalePet.module.css`）：所有像素压成单条 `box-shadow` 列表写入一个 1×1 div 的 `--whale-shadows`，`transform: scale(2)` 保持像素锐利。动画 = 固定 DOM 树上的样式切换，**无逐帧 React 重排**；`prefers-reduced-motion: reduce` 时静默降级为静姿。
5. **纯 tick 状态机**（`src/client/animation.ts`）：`TICK_MS=120ms`；`moodOf(running, thinking, toolRunning)` 推导 5 种 mood（idle/thinking/working/running/spouting）。摆尾 `0-1-2-3-2-1-0`、胸鳍 `0-1-2-1-0`、喷水**单向** `0-1-2-3-4-5-6`。每个 mood 有独立的 WAG_HOLD / FIN_HOLD / BLINK_GAP / SPOUT_GAP 节奏；纯函数 `advance(state, mood)` 让动画规则不带定时器即可单测。
6. **情绪来源**（`WhalePet.tsx:18-21, 33-35`）：`useSession(s => s.running)`、`useSession(s => s.partial?.blocks.some(b => b.kind === 'reasoning'))`、`useSession(s => s.runningCalls.length > 0)`；`running true→false` 下降沿把 `spoutLeftRef` 置为 `SPOUT_DURATION=18` tick，触发喷水庆祝。
7. **可访问性 + i18n**：`role="img"` + `aria-label="${t('title')} · ${t(moodKey(mood))}"`；通过 `declare module '@deepseek-ai/dsh-client-ui-slots' { interface LocaleNamespaceMap { whale: WhaleKey } }` 把 `whale` 命名空间并入框架 locale 类型系统（`src/client/index.ts:14-19`），zh 是 key 集 source of truth，en 用 `satisfies Record<WhaleKey, string>` 编译期校验完整。
8. **测试**（`tests/`）：`browser-plugin.spec.tsx` 用真实 cordis Context + 自造 `slots/sessions/conversation/locale` 桩验证注册 id/order/locale、disposal（HMR 安全）、node half 空转、组件 mood 渲染；`sprite.spec.ts` 钉帧一致性（组合姿势逐像素还原原图）；`animation.spec.ts` 钉动画序列。所有 `@deepseek-ai/*` 桩在测试内自给，**无需解析 DSH 快照源码**。

## 与 DeepSeek Harness 主仓库的集成点
- **依赖链**：所有 `@deepseek-ai/dsh-client-*` 与 `cordis` 走 `link:../.dsh/source/current/...`——DSH 必须先有构建好的快照（`~/.dsh/source/current`），否则 `pnpm install` 无法解析。
- **插件发现**：`package.json` 的 `dshClient: { inject: [...], platform: 'web' }` 字段是 DSH 客户端插件加载器的入口；`exports` 暴露 `./client`（浏览器 half）、`./invariant`、`.`（Node half）。
- **槽位契约**：注册到主仓 `@deepseek-ai/dsh-client-ui-conversation` 声明的 `conversation.session.header.actions` 槽（`order: 30`）——服务等待保证此 apply 在声明槽位的 apply 之后。
- **locale 系统**：并入 `@deepseek-ai/dsh-client-ui-slots` 的 `LocaleNamespaceMap`（命名空间名 `whale`）。
- **invariant 系统**：`src/invariant.ts` 向主仓 `@deepseek-ai/dsh-invariants` 的 invariant 服务注册包所有权。
- **安装**（`INSTALL.md`）：`pnpm add -w link:/path/to/dsh-ui-whale`（或 git 依赖 `github:dsh-external/dsh-ui-whale#<commit>`）→ `~/.dsh/config.yaml` 加 `- insert: [{ id: dsh-ui-whale, name: '@dsh-external/dsh-ui-whale' }]` → 重启 `dsh web`。

## 亮点与风险
**亮点**
- 真正"零核心改动"：纯客户端装饰插件，不影响模型请求/提示词/工具 schema（README 显式 Model Experience 声明）。
- 美术与工程闭环：帧矩阵 → 自动推导分层 → 单 box-shadow 列表渲染 → 纯 tick 状态机驱动，每一步都有测试钉住，无 magic number 散落。
- 动画规则全在纯函数里（`advance/frameOf/moodOf`），不带定时器，单测 deterministic。
- 无障碍 + reduced-motion + i18n 都做到位。

**风险**
- **包名不一致**（`src/invariant.ts:8`）：`PACKAGE_NAME = '@deepseek-ai/dsh-client-ui-whale'`，但实际包名是 `@dsh-external/dsh-ui-whale`（`package.json`）。invariant 包所有权注册到了一个不存在的 `@deepseek-ai/dsh-client-ui-whale` 名下——如果 DSH invariant 注册表按包名做唯一性/冲突检查，此处可能注册失败或与未来同名的内部包冲突。
- **Node half 与包名错配**：`src/index.ts` 注释里也把自身称作 `client-ui-whale`，README/INSTALL 文档与 invariant 注释存在两套命名心智模型，长期维护需统一。
- **构建产物入库**：`lib/client.js` 31.5KB 已 commit（git 元数据 31 文件含 lib/），与 DSH 主仓"源码构建"惯例可能冲突，review 时需确认是否应 `.gitignore`。
- **强耦合 DSH 快照**：所有 devDeps 是 `link:../.dsh/source/current`，**仓库不可独立 clone 即装**——CI/外部贡献者必须先有 DSH 主仓快照，否则 `pnpm install` 失败。
- **`private: true`**：无法 npm 发布，只能 link/git 依赖分发，组织外无法消费。
- **测试覆盖盲区**：组件测试只覆盖 idle / working 两个 mood，spouting 庆祝分支（`spoutLeftRef` 下降沿）和 thinking/running mood 未在 `browser-plugin.spec.tsx` 中显式断言（推断——`tests/browser-plugin.spec.tsx` 仅有 2 个组件 case）。
- **文件地址**：`src/client/animation.ts:43-46`（WAG_SEQUENCE）、`src/client/animation.ts:55`（SPOUT_SEQUENCE 单向）、`src/client/sprite.ts:62-71`（motionRegion 自动分层）、`src/client/WhalePet.tsx:39-49`（spout 下降沿）、`src/invariant.ts:8`（包名错配）、`src/client/index.ts:30-44`（槽位注册）。

## 维护状态
- **创建时间**：2026-08-06（与本次 dsh-external 新仓检测同日出现）。
- **提交历史**（shallow clone 仅可见 1 条）：`62a10af docs: add whale demo video and embed it in README`，最后提交人时间戳 `2026-08-06T01:01:56+08:00`。
- **规模**：31 文件 / ~7930 行（含 sprite 数据与 lock）。
- **作者**：单作者（脱敏，不写邮箱/真名）。
- 推断：当日新建、首版即交付完整文档+测试+构建产物，处于"刚发布待组织内试用"阶段，无活跃迭代信号。

## 备注
- 仓库非空、可读、结构完整；README/INSTALL/测试/spirit 数据/演示视频齐全。
- 13 帧命名（STANDARD + BLINK + FIN_1/2 + SPOUT_1..6 + TAIL_1..3）与 README 宣称的"13 帧手绘像素画"一致。
- 此插件对 cron-check 的"新仓库检测"是真正的 dsh-external 新增成员，入库 `research/` 后 KNOWN_REPOS 自动同步即可。
