# dsh-web-ui-approval-notify 调研摘要

## 一句话定位

DeepSeek Harness Web UI 浏览器侧客户端插件：当工具有审批请求、或 DSH 向你提问，而你正在浏览其他标签页时，弹出系统桌面通知（`Notification` API），避免 DSH 在后台空等。

## 技术栈与依赖

- 语言/类型：TypeScript（`type: module`），React + JSX（`.tsx`），CSS Modules
- 形态：DSH 客户端插件，Cordis 风格 dual-face 包（Node 半 + 浏览器半），零运行时 npm 依赖
- 浏览器侧三个 `require`（`react`、`react/jsx-runtime`、`@deepseek-ai/dsh-client-ui-slots`）走 DSH 前端自己的模块表，不经 npm
- 注入的 host 服务：`@deepseek-ai/dsh-client-runtime`（`ClientContext`/`ISessions`/`SessionId`/`PendingInteraction`）、`@deepseek-ai/dsh-client-locale`、`@deepseek-ai/dsh-client-ui-slots`（`deferRegistration`/`PropsRuntime`/`PropsLocale`）
- 构建工具链：`tsc` + `tsdown`，复用 DSH checkout 的 `packages/client/tsdown.client.ts` 中的 `clientBundle` 预设
- 测试：Vitest + jsdom + @testing-library/react；host 包通过 `DSH_CHECKOUT` 路径别名解析到 DSH 源码 src（不读 built lib）
- 包名：`@dsh-external/dsh-web-ui-approval-notify`，版本 `0.1.0`，BSD-3-Clause

## 文件结构概览

```
.
├── package.json           # dshClient.inject=['@deepseek-ai/dsh-client-ui-slots']，platform=web
├── README.md              # 中文文档：能力、安装、使用、卸载
├── LICENSE                # BSD-3-Clause
├── tsconfig.json
├── tsdown.config.mjs      # 调 DSH checkout 的 clientBundle 预设打 client 包
├── vitest.config.ts       # 用 DSH_CHECKOUT 把 @deepseek-ai/* 和 cordis 别名到 src
├── scripts/
│   └── build.mjs          # 定位 DSH checkout、临时 symlink node_modules、跑 tsc+tsdown
├── src/
│   ├── index.ts           # Node 半：no-op Cordis 插件（name/inject=[]/apply 空函数）
│   ├── css-modules.d.ts
│   └── client/
│       ├── index.ts            # 浏览器半 apply：注册词典、订阅当前会话、注册设置行
│       ├── notify.ts           # 纯函数：hiddenNow/notificationUsable/fireNotification
│       ├── NotificationSettingsRow.tsx  # 设置→通用 里的通知权限行（4 态）
│       ├── NotificationSettingsRow.module.css
│       └── locales.ts          # zh（key 集 source of truth）+ en，命名空间 'approval-notify'
├── lib/                   # 预构建产物（仓库自带，安装后直接可用）
│   ├── index.js           # Node 半构建产物
│   ├── client.js          # 浏览器半 bundle（10KB）
│   ├── client.js.map
│   └── types/index.d.ts
└── tests/
    ├── browser-plugin.spec.ts   # apply 整体 wiring（9.1KB，8 个用例）
    └── settings-row.spec.tsx    # NotificationSettingsRow 4 态测试（2.6KB）
```

## 核心功能与实现要点

1. **Dual-face Cordis 包结构**（`src/index.ts:1-15`）：Node 半是无操作 Cordis 插件（`inject: []`，`apply()` 空实现），仅为让插件根在 host Loader 里显示为一个完整条目；所有真实逻辑在浏览器半 `src/client/index.ts`，由 package.json 的 `dshClient` 声明被发现。

2. **观察模型只盯当前会话**（`src/client/index.ts:20-31`，注释 17-23）：审批/提问 wait 在 composer 链上「弹出来」的语义只对当前会话成立，因此订阅 `sessions.list` 的快照 + `sessions.binding(current).session.subscribe(scan)`，与 UI 弹窗语义完全对齐。非当前会话的 wait 只在被打开时（缓冲帧 replay）才出现，那也才是通知有意义的时机。

3. **dedupe key 稳定跨 replay**（`src/client/index.ts:33-46`）：用 `Set<string>` 记录已通知的 `PendingWait.key`（`a:<rpcId>` / `q:<rpcId>`），断线重连 mux-open replay 时 key 不变，所以同一请求只通知一次。注释指出 key 是「by construction」稳定的。

4. **触发三重门 + 不自动消失**（`src/client/notify.ts:33-50`）：`hiddenNow()`（`document.visibilityState === 'hidden'`）&& `notificationUsable()`（`Notification.permission === 'granted'`）才通知；`new Notification(title, { body, tag: wait.key, requireInteraction: true })` 让通知不自动消失，等用户处理。审批正文优先用 `payload.reason`，否则回退到 `notify.approval.body` 模板；提问正文取 `payload.questions[0].question`，空则用 `notify.question.bodyGeneric`。

5. **点击通知跳回页面**（`src/client/notify.ts:46-49`）：`notification.onclick = () => { window.focus(); notification.close() }`——macOS/Windows 上不 reclaim click 的话只抬起浏览器，不聚焦页面。

6. **设置行四态**（`src/client/NotificationSettingsRow.tsx:30-66`）：`permissionState()` 读 `Notification.permission`，无 API 时返回 `'unsupported'`；按 `granted`/`denied`/`default`/`unsupported` 渲染不同文案；非 granted/unsupported 时显示「开启桌面通知」按钮，按钮点击调 `Notification.requestPermission()`（浏览器要求的 user-gesture 入口）。注册到 `settings.general.item` slot，`order: 30`，通过 `deferRegistration` 等 hole 声明就绪后再注册（`src/client/index.ts:60-71`）。

7. **会话切换时重绑订阅**（`src/client/index.ts:48-59`）：`watchCurrent` 监听 `sessions.list`，当 `current` 变化时取消旧订阅、对新当前会话重新订阅 scan；保证切换会话后通知仍能正确触发。

8. **构建链路零 npm install**（`scripts/build.mjs:23-90`）：`resolveCheckout()` 优先用 `DSH_CHECKOUT` 环境变量，否则沿 `dsh` 启动器符号链接链向上找 `packages/client/tsdown.client.ts`；把 checkout 的 `node_modules` symlink 到本仓，再用 `.pnpm` store 拼 `react`/`@types/react`，把 `@deepseek-ai/dsh-client-*` workspace 包 symlink 进来；先 `tsc -p`（生成 `lib/types/index.js`），再 `tsdown`（生成 `lib/client.js`）；`finally` 里删掉临时 `node_modules` 不污染打包。

## 与 DeepSeek Harness 主仓库的集成点

- **Seam：DSH 客户端插件契约**。通过 package.json 的 `dshClient` 字段声明（`package.json:13-18`）：
  ```json
  "dshClient": { "inject": ["@deepseek-ai/dsh-client-ui-slots"], "platform": "web" }
  ```
  DSH Web 客户端模块系统据此发现浏览器半 `lib/client.js`，注入到 `ui-slots` 注册器。
- **Cordis 服务注入**：浏览器半 `inject = ['slots', 'sessions', 'locale']`（`src/client/index.ts:30`），由 host 提供 `ClientContext`，调用 `ctx.effect`/`ctx.locale.register`/`ctx.sessions`/`ctx.slots.register`。
- **UI Slots 扩展点**：注册到 `settings.general.item`（通用设置列表），向 host 注入新的 `LocaleNamespaceMap['approval-notify']` 命名空间（TypeScript `declare module`，`src/client/index.ts:24-29`）——纯类型补丁，不修改 host 代码。
- **运行时数据模型**：依赖 host 的 `PendingInteraction`（`{ kind: 'approval' | 'question', key, payload }`）和 `ISessions` 接口（`list.subscribe`/`list.getSnapshot().current`/`binding(id).session.subscribe/getSnapshot().pending`）。
- **安装方式**（README）：`pnpm --filter @deepseek-ai/dsh add "github:dsh-external/dsh-web-ui-approval-notify"`，然后在 `~/.dsh/config.yaml` 个人配置覆盖层加 `id: ui-approval-notify` + `name: '@dsh-external/dsh-web-ui-approval-notify'` 两条，不改 DSH 仓库本体；卸载走 `pnpm remove` + 删配置。
- **构建期依赖**：`scripts/build.mjs` 和 `vitest.config.ts` 都要求 `DSH_CHECKOUT` 指向一份 DSH 源码 checkout，依赖 `packages/client/tsdown.client.ts` 预设和 `packages/client/{runtime,locale,ui-slots,test-runtime}/src` 的源码（非 built lib，确保 cordis 单实例）。

## 亮点与风险

**亮点**

- 零运行时依赖、仓库自带 `lib/` 构建产物，装完即用，不需 build；浏览器侧 require 完全走 DSH 前端模块表，包体积极小（client.js 10KB）。
- 观察模型设计精确：注释（`src/client/index.ts:17-23`）显式论证「只盯当前会话」与 composer 弹窗语义的一致性，并解释 dedupe key 在 mux replay 下稳定的「by construction」原因。
- 通知侧三个纯函数 `hiddenNow`/`notificationUsable`/`fireNotification`（`src/client/notify.ts:23-50`）做了副作用隔离，测试可用 stub Notification + fake visibilityState 驱动。
- 测试覆盖完整（`tests/browser-plugin.spec.ts:1-225`，8 用例）：inject 声明、settings row 延迟注册、审批/提问两种 wait 触发、replay dedupe、可见时不通知、未授权时不通知、点击 focus+close、会话切换重绑。
- 构建链路巧用 symlink，开发者克隆后无需 `pnpm install`，版本与运行中的 harness 始终对齐（`scripts/build.mjs:50-90`）。

**风险**

- 强耦合 DSH 内部 API：`PendingInteraction` 形状、`ISessions` 接口、`deferRegistration`、`LocaleService`、`SlotsService` 都是 host 内部包（`@deepseek-ai/dsh-client-*`，未发布到 npm），host 重构这些 seam 时本插件会直接坏。`src/client/index.ts:20-22` 注释依赖 `PendingInteraction` 是 `{ approval, question }` 精确二分。
- `dshClient.inject: ['@deepseek-ai/dsh-client-ui-slots']` 的发现机制、`dshClient.platform: 'web'` 字段、`deferRegistration` API 都是 host 私契约，无版本化保证。
- 仓库明确声明属于 dsh-external 内测社区组织，README 头部警告「官方不保证公开发布后该组织仍然存在，请自行保留副本」。
- 通知触发完全依赖 `document.visibilityState`：浏览器节流/系统休眠时 hidden 状态可能滞后；多窗口场景下「当前会话」语义不覆盖跨窗口。
- macOS 需用户额外在系统设置里允许浏览器通知，否则插件静默——README 已说明，但仍是一个落地摩擦点。
- `notify.ts:43` 使用 `wait.payload.questions[0]` 而未防御空数组/undefined（除 `first?.question` 的可选链外），如果 host 给出 `questions: []` 会落到 `bodyGeneric` 兜底——目前 OK，但属隐式契约。

## 维护状态

- 全新仓库：唯一一次提交 `4b17c10` 「Update README.md」于 2026-08-05 14:05:32 +0800（与本调研同日），作者 GitHub 用户名 `bill9109`（昵称 `hanlinxuy` 在另一条 reflog 出现）。
- `git rev-list --count HEAD` = 1，深度克隆可见仅为单次快照。
- 版本号 `0.1.0`（`package.json`），处于早期阶段。
- 测试和构建脚本完备，注释密度高且解释设计意图，质量显著高于「扔出来」的占位仓库——明显是有意发布的可用插件。

## 备注

- 安装需先有 DSH 源码环境（`scripts/install.sh` 装出来的 checkout，默认 `~/.dsh/source/current`）；本插件不动 DSH 仓库文件，只在 `~/.dsh/config.yaml` 个人覆盖层加条目。
- 「工具审批和 DSH 提问」对应 host 的两种 `PendingInteraction`：审批显示越权原因（`payload.reason`），提问显示问题原文（`payload.questions[0].question`）。
- 通知权限需用户手动在「设置 → 通用 → 桌面通知」点按钮授权（浏览器要求 user-gesture），未授权时插件静默；四种状态（已开启 / 未授权 / 已被浏览器阻止 / 浏览器不支持）在设置行明确展示。
- 与同批次其他 DSH 客户端 UI 插件一样走 ui-slots + locale 双 seam 模式，是研究 DSH 插件契约的范本案例。
