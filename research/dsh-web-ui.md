# dsh-external/dsh-web-ui

## 一句话定位

`dsh-web-ui` 是 DeepSeek Harness Web GUI（`dsh web`）的**皮肤 / UI 插件集合仓库**：收录若干可热插拔的纯呈现层客户端皮肤包，不是 Web 前端本体，而是主仓库 `packages/client/` 的可选卫星包。

## 技术栈与依赖

- **语言/打包**：TypeScript + CSS Modules；`tsdown` 打包（每个皮肤复用主仓库 checkout 内的 `packages/client/tsdown.client.ts` 预设，CSS Modules 自动注入 + 平台模块外部化）。
- **运行时框架**：`cordis`（peer dep `^4.0.0-rc.7`）—— 皮肤的 `apply(ctx)` 即 cordis 插件入口，用 `ctx.effect()` 注册收回副作用。
- **内部依赖**：`@deepseek-ai/dsh-invariants`（workspace dev dep，提供 invariant companion 注册服务）。
- **测试**：`vitest` + `jsdom`，每个皮肤带 `tests/apply.spec.ts`（断言挂载 + 拆卸双向）与 `tests/invariant.spec.ts`。
- **产物**：每个皮肤 `lib/client.js`（约 22 KB，CSS 内联的预构建 bundle）+ sourcemap，拷进 checkout 即可用、无需现场构建。
- **包命名**：`@deepseek-ai/dsh-client-ui-skin-<name>`，`private: true`，`dshClient.platform: "web"`，许可证 BSD-3-Clause。

## 文件结构概览

```
dsh-web-ui/
├── README.md                      仓库总览（中英双语），说明结构与接入步骤
└── skins/
    ├── qq98/                      QQ98/OICQ 怀旧皮肤（首个入库）
    │   ├── src/
    │   │   ├── client/{index.ts, qq98.module.css}   apply() 挂载逻辑 + ~23 KB 样式
    │   │   ├── index.ts           包入口（re-export client）
    │   │   ├── invariant.ts       invariant companion（空 install，仅占位注册）
    │   │   └── css-modules.d.ts
    │   ├── lib/client.js(+.map)   预构建 bundle
    │   ├── tests/{apply,invariant}.spec.ts
    │   ├── package.json / tsdown.config.ts
    │   └── README.md(+.zh.md, .i18n.yaml)
    ├── ths/                       同花顺炒股主题（结构同上，CSS ~26 KB）
    └── xp/                        Windows XP(Luna) 复古主题（结构同上，CSS ~29 KB）
```

三个皮肤目录结构完全一致，便于互为模板复制。

## 核心功能与实现要点

1. **热插拔皮肤契约**：每个皮肤是一个 cordis 客户端插件，`apply(ctx)` 拥有并管理全部 DOM 写入，`ctx.effect()` 注册的 disposer 在 fiber dispose 时**只收回自己写过的东西**（ThemePresenter 收回纪律）。见 `skins/qq98/src/client/index.ts:69-95`（apply 主体 + effect 收回）。

2. **样式作用域 = body 属性**：`apply()` 第一步是 `body.dataset.dshRetro/dshXp/dshThs = ''`，整个 `.module.css` 都挂在该属性选择器下（如 `body[data-dsh-retro]`），从根上避免皮肤互相污染；深色变体走 `body[data-dsh-*][data-ds-dark-theme]`。见 `skins/qq98/src/client/index.ts:71`。

3. **固定窗口铬（chrome）注入**：每个皮肤 `document.createElement` 出固定定位的标题栏 + 状态栏，标题栏带图标 + 装饰性窗口按钮（`– □ ✕`，`aria-hidden`），状态栏带若干信息单元。CSS 走 bundle 的 CSS-modules 自动注入，<link>/<style> 标签由 loader 持有、entry dispose 时一并移除。见 `skins/qq98/src/client/index.ts:73-101`。

4. **标题 + favicon 内联注入（零静态资源）**：标题栏图标和 favicon 都是**内联 SVG 字符串**（企鹅 / 四色旗 / K 线 / 同字），favicon 走 `data:image/svg+xml;utf8,...` data URI，皮肤包不携带任何静态资源文件。见 `skins/qq98/src/client/index.ts:39-52`（PENGUIN_SVG）。

5. **会话标题安全拆卸**：disposer 只在 `document.title === SKIN_TITLE` 时才恢复原标题——若 shell 已投影了会话标题（如 "我的会话 — …"），皮肤拆卸不会覆盖它。这是三皮肤共有的细节契约。见 `skins/qq98/src/client/index.ts:91-93`。

6. **XP 皮肤的动态挂载（最复杂的一个）**：xp 皮肤额外在侧边栏 footer 注入绿色「开始」按钮，用 `MutationObserver` 观察 body 子树变化（因 footer 可能晚于皮肤挂载、且设置弹窗会 portal 进 sidebar 列改变 `:last-child`），按钮 click 转发给真实设置触发器 `button[aria-haspopup="dialog"]`。锚点用**显式 class**（`xpTaskbar`）而非 `:last-child`，避免白色 footer 按钮色泄漏到弹窗控件。见 `skins/xp/src/client/index.ts:62`（`SIDEBAR_FOOT_SELECTOR`）与 `:89-121`（mountStart）。

7. **同花顺皮肤的行情装饰**：标题栏带 live-quote chip（上证指数），状态栏带 上证/深证/创业板 三档行情单元，按 A 股惯例 `红涨绿跌`（`data-trend="up|down"`）。但数值是**静态文案**，不接真实行情。见 `skins/ths/src/client/index.ts:14-27`（STOCK_CELLS）。

8. **invariant companion 空实现**：每个皮肤的 `invariant.ts` 调 `ctx.invariants.register(PACKAGE_NAME, () => {})` 注册一个**无运行时校验**的 invariant——因为皮肤不拥有任何 cordis 事件或跨插件可变状态，其全部契约是 DOM 写入，由 `apply.spec.ts` 对组装后的 shell 断言。见 `skins/qq98/src/invariant.ts:30-37`。

## 与 DeepSeek Harness 主仓库的集成点

- **不是主仓库一部分，而是其客户端插件供应商**：主仓库的 Web 前端在 `packages/client/`；本仓库的皮肤作为 **workspace 包**被拷进 `packages/client/`，由主仓库的 `packages/client/tsdown.client.ts` 预设构建。
- **接入清单（四步，见各皮肤 README "Wiring it into a checkout"）**：
  1. 把 `skins/<name>/` 拷进 checkout 的 `packages/client/`（作为 workspace 包）；
  2. 在 `apps/cli/config/web.cordis.yml` 加一行 `dshClient`：`- id: ui-skin-<name>` / `name: '@deepseek-ai/dsh-client-ui-skin-<name>'`；
  3. 在 `apps/cli/package.json` 的 dependencies 与 `tsconfig.client.json` 的 references 各加一项；
  4. `pnpm install` → `pnpm --filter @deepseek-ai/dsh-client-ui-skin-<name> run bundle` → 重启 `dsh web` 刷新。
- **强耦合点**：面板级皮肤（侧栏渐变、会话/详情面板表面）依赖 `ui-layout` AppFrame 列上的 `data-pane` 属性（如 `[data-pane='sidebar']`）；没有这些属性的 ui-layout 版本下皮肤仍能应用，只是失去面板级表面。见各皮肤 README "Requirements"。
- **运行时边界（皮肤契约明文）**：纯呈现层——不注入 cordis 服务、不发事件、不触及任何模型请求、对 KV cache 零影响。所有皮肤 README 都有 "Model Experience: None / KV Cache effect: None" 一节。
- **同一时刻只接线一个皮肤**：两个皮肤会重复注入标题栏/状态栏；换皮肤 = 改 `web.cordis.yml` 那一行。

## 亮点与风险

**亮点**
- 收回纪律干净到可作为范本：apply 写什么、dispose 收什么，一一对应；还处理了"会话标题投影后皮肤拆卸"这一边界（`skins/qq98/src/client/index.ts:91-93`）。
- 零静态资源：图标/favicon 全内联 SVG，皮肤包就是 `src + lib/client.js`，移植无目录依赖。
- 作用域隔离彻底：靠 body 属性 + CSS Modules 双重作用域，三皮肤互不干扰。
- 测试覆盖契约而非实现：`apply.spec.ts` 同时断言挂载态与拆卸态，且专门测了会话标题不被覆盖（`skins/qq98/tests/apply.spec.ts:46-56`）。
- 文档完备：每个皮肤带中英 README + `README.i18n.yaml`，接线步骤可复制。

**风险**
- **依赖主仓库内部 DOM 结构**：面板级样式钩在 `ui-layout` 的 `data-pane` 属性上，xp 皮肤更用 `[data-pane='sidebar'] > div > :last-child` 这类脆弱选择器 + `MutationObserver` 轮询挂「开始」按钮——shell DOM 重构会断皮肤（`skins/xp/src/client/index.ts:62`、`:89-121`）。这是与主仓库耦合最紧、最易碎的点。
- **boot/loading 页面无法皮肤化**：shell 启动页在插件 bundle 存在前就渲染，皮肤只在 settled UI 后生效（各皮肤 README "Known Limitations"）。
- **主题切换语义受限**：皮肤把自身调色板钉在 `data-ds-dark-theme` 的两种状态下，在外观设置里切换只会在皮肤的亮/暗变体间翻，回不到原生外观（需卸皮肤）。
- **ths 行情为静态装饰**：状态栏指数是写死文案，不追踪真实行情，可能误导（`skins/ths/src/client/index.ts:14-22`）。
- **单皮肤接线约束**：人为约束，无代码护栏；误接两个会双注入 chrome。
- **License 不一致**：`package.json` 声明 BSD-3-Clause，但 GitHub 仓库元数据 `license` 字段为 null（私有仓库，影响小）。
- **xp 四色旗为扁平近似**：内联 2×2 flag，非真实飘扬 Windows 旗（xp README "Known Limitations"，潜在商标/外观近似风险，私有仓库内部使用影响有限）。

## 维护状态

- **全新仓库**：GitHub 创建于 `2026-08-05T15:08:57Z`，最近 push `2026-08-06T02:14:13Z`（截至调研日 2026-08-06）。
- **提交节奏**：共 6 个 commit，全部集中在 2026-08-05 ~ 08-06 约 11 小时窗口内（qq98 beauty pass → ths 加入与调色 → xp 加入 → xp taskbar 锚点修复），典型的一天内集中铺陈的首批投放。
- **`--depth 1` 浅克隆只见 HEAD 一个 commit**（`aec9c69`，2026-08-06 10:14:11 +0800，"skins/xp: fix taskbar anchoring..."）；完整历史由 `gh api .../commits` 取得。
- **0 open issues，未归档**，无 tag / 无 release。语言统计为 CSS。
- **私有仓库**（`private: true`），仅 `dsh-external` 组织成员可见，size 82 KB。
- 远程已校验为 `https://github.com/dsh-external/dsh-web-ui.git`（中途一次日志曾显示为他仓 remote，系已退出 daemon 的残留输出混入，本次以干净重跑为准）。

## 备注

- **与"Web UI"名称的关系**：仓库名易误导为"Web 前端本体"，实际是 Web GUI 的**皮肤集合**——主仓库的 `packages/client/` 才是前端壳层；本仓库是其可选的呈现层插件供应商，依赖主仓库而非被依赖。调研/索引时勿与主仓库 web 模块混淆。
- **空仓库检查**：非空，已有 3 个完整可用皮肤（含预构建 bundle）。
- **脱敏**：本摘要不含作者邮箱/真名；唯一提交者署名为 git history 中的账号名（zhu1090093659），属仓库公开元数据。
- **入库建议**：可作为 `research/dsh-web-ui.md` 索引；归类应为"UI 插件 / 皮肤集合（客户端呈现层）"，与 web 前端、desktop 端分开标注，避免与主仓库 `packages/client/` 混淆。
