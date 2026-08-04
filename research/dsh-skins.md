# dsh-skins 调研摘要

## 一句话定位

`dsh-external/dsh-skins` 是 DeepSeek Harness（DSH）Web GUI 的第三方换肤插件仓库：每个皮肤都是对官方 `ThemeService.register({ id, colorScheme, tokens })` 接口的一次合法调用（覆盖 `--dsw-alias-*` 语义 token，必要时叠加 data-URL 内联的 AI 生图背景），通过 `dshClient` 客户端插件契约挂进 `dsh web`，**零核心改动、配置即安装**。

## 技术栈与依赖

- **语言/类型**：TypeScript（target ES2024，`module: ESM`），React 18 + JSX（SkinRow.tsx），CSS Modules（lightningcss 编译）。
- **包管理/构建**：pnpm workspace（根 `package.json` 是 `private: true` 的壳），tsdown 0.22 双产物（node 半 + 浏览器 closure-factory bundle），vitest 4 测试，tsc 6 类型检查。
- **运行时 peer 依赖**（DSH 客户端运行时注入，不打包）：`@deepseek-ai/dsh-client-runtime` / `-locale` / `-ui-slots` / `-ui-primitives` / `-ui-theme`（均 `^0.0.1`），`cordis ^4.0.0-rc.7`，`react ^18.2.0`。
- **真实依赖**：仅 `clsx ^2.0.0`。
- **构建链严格对齐**：Private DSH snapshot `20260804T143803Z`（commit `f1792735`）的 `packages/client/tsdown.client.ts`——平台模块表（react/cordis/ui-*）写死成 inline 常量，避免对 harness checkout 的构建期依赖。
- **版权/分发**：私有仓库，版权归作者 作者（昵称已脱敏） 个人所有；当前仅供 dsh-external 组织内测成员使用。

## 文件结构概览

```
dsh-skins/
├── README.md / README.en.md / README.i18n.yaml   # 双语 README + i18n sidecar（hash 锚点）
├── catalog.json                                  # schema dsh-skins-index/v0.2，pin 到发布 commit
├── package.json                                  # workspace 壳，pnpm -r 跑子包
├── pnpm-workspace.yaml / pnpm-lock.yaml
├── tsconfig.base.json
├── preview/index.html                            # 本地试穿预览页（mock 聊天布局）
├── docs/
│   ├── install.md (+ .en.md / .i18n.yaml)        # 三种安装路径 + 配置行语义
│   ├── skin-authoring.md (+ .en.md / .i18n.yaml) # SkinDefinition 字段 + GPT Image 提示词 + 水印模板
│   ├── gallery.md (+ .en.md / .i18n.yaml)        # 每皮肤预览图与创作思路
│   └── images/skin-{nord,aurora,paper,dream}.svg # 艺术资产单一来源
├── scripts/
│   ├── embed-image.mjs     # PNG/SVG → data URL，给 AI 生图背景用
│   ├── gen-skin-styles.mjs # 从 docs/images/*.svg 生成 skin-styles.ts
│   ├── preview.mjs         # 启动本地试穿页
│   ├── publish.mjs         # pin HEAD → catalog.json + 双语 README INSTALL/REFS 块
│   ├── verify.mjs          # typecheck+build+test+i18n+产物冒烟（vm 沙箱跑 client.js）
│   └── verify-i18n.mjs     # 双语一致性门禁（hash + 结构签名）
├── .github/workflows/verify.yml                  # CI：clone 兄弟快照 + pnpm verify
└── packages/dsh-web-skins/                       # 唯一交付插件包 @dsh-external/dsh-web-skins
    ├── package.json        # dshClient 契约：{ inject:[runtime,locale], platform:"web" }
    ├── tsdown.config.ts    # vendored 官方预设，inline 平台模块表
    ├── src/
    │   ├── index.ts                            # 宿主半 apply() 空实现
    │   └── client/
    │       ├── index.ts          # 浏览器半：注册皮肤 + 镜像 DOM + 注册设置行
    │       ├── skins.ts          # SkinDefinition 类型 + SKINS 数组（nord/aurora/paper/dream）
    │       ├── skin-styles.ts    # 自动生成：AURORA_CSS/PAPER_CSS/DREAM_CSS + SKIN_PREVIEWS（data URL）
    │       ├── skin-dom.ts       # applySkinDom/retractSkinDom：body[data-ds-skin] + <style id=dsh-web-skins/active>
    │       ├── SkinRow.tsx       # 设置页图库式瓦片（slot 组件）
    │       ├── SkinRow.module.css
    │       ├── settings-store.ts # defineStore：镜像 theme snapshot 的 active.id + revision
    │       ├── settings-contract.ts
    │       └── locales.ts        # settings.skins 命名空间 zh/en 词典
    ├── tests/                # vitest：apply / skins / skin-dom / skin-row / settings-store
    └── lib/                  # 构建产物：index.js / client.js(+.map) / preview-skins.js
```

## 核心功能与实现要点

1. **ThemeService 是官方支持的第三方主题表面**：`@deepseek-ai/dsh-client-ui-theme` 暴露 `ctx.theme.register({ id, colorScheme, tokens })`，返回 disposer；`getTheme()` 拿 `ThemeSnapshot { active, revision }`，`setTheme(id)` 写偏好（持久化到 `dsh.theme`），`theme/change` 事件广播快照。`ThemePresenter`（官方）把 token 以 body 内联 CSS 变量铺出去，并管 `body[data-ds-dark-theme]`——本插件**从不碰**这两个，只追加自己的 `data-ds-skin` 属性。
   - 关键文件：`packages/dsh-web-skins/src/client/index.ts:36-47`（注册）、`skin-dom.ts` 注释明确职责边界。

2. **皮肤 = ThemeDefinition + 可选富 CSS**：`SkinDefinition`（`skins.ts:30-49`）字段：`id` / `colorScheme: 'light'|'dark'` / `tokens: Record<string,string>` / `css?` / `preview` / `focal` / `accent` / `labelKey`。SKINS 数组 `Object.freeze` 4 个皮肤：`nord`（dark, token-only）、`aurora`（dark, image）、`paper`（light, image）、`dream`（dark, image）。token 集 80+ 个 `--dsw-alias-*` / `--dsw-specific-*` 别名层覆盖（如 `--dsw-alias-bg-base`、`--dsw-alias-brand-primary`、`--dsw-alias-label-primary`、`--dsw-specific-sidebar-fill`）；`--dsw-static-*` 原始色阶明确禁止覆盖。

3. **AI 生图背景接入流程**（`docs/skin-authoring.md`）：①用 GPT Image/DALL·E 出 1200×800 图（提示词强调 `no text / no logo / empty middle / very dark|light`，主体放四角）；②`node scripts/embed-image.mjs <图> <变量名>` 转 base64 data URL；③贴进 `skin-styles.ts` 配 `body[data-ds-skin="<id>"] { background-image: url("data:..."); }`；④把 `--dsw-alias-bg-base` 等基底 token 设半透明（如 `rgba(13,16,30,0.86)`）让背景透出来，layer-1/2/3 保持接近不透明保证可读性。`scripts/gen-skin-styles.mjs` 从 `docs/images/*.svg` 重新生成 `skin-styles.ts`（艺术资产单一来源）；DSH 鱼 logo 水印走 SVG 模板手工叠加（不让 AI 画 logo）。

4. **零核心改动的三段机制**：①主题注册走官方 `ctx.theme.register`；②DOM 镜像由 `skin-dom.ts` 独立维护——`body[data-ds-skin="<id>"]` 属性 + 一个 id 固定为 `dsh-web-skins/active` 的 `<style data-plugin>` 标签，切换皮肤时整体替换 textContent、卸载时整体 remove，**只回收自己写的东西**；③设置页 UI 复用官方 `settings.general.item` slot（`order: 20`，外观行下方），通过 `deferRegistration` 处理声明时序竞态。三段全是客户端插件契约内的合法扩展点。

5. **客户端插件契约**（`packages/dsh-web-skins/package.json`）：`dshClient: { inject: ['@deepseek-ai/dsh-client-runtime', '@deepseek-ai/dsh-client-locale'], platform: 'web' }`；`exports['./client'] → lib/client.js`。`dsh web` 的 `ClientModuleHostService` 扫配置树所有 `dshClient` 行，用 `createRequire(baseUrl)` 解析 `${name}/package.json`，把 `lib/client.js` 当 closure-factory 喂给 `window.__ModuleLoader__.load({ id, factory })`。tsdown 把 react/cordis/ui-* 标 external，走 loader 冻结模块表；CSS Modules 由 lightningcss 编译成自动注入的 `<style data-plugin>`。`src/index.ts` 宿主半 `apply()` 空实现。

6. **皮肤选择行**（`SkinRow.tsx` + `settings-store.ts`）：图库式瓦片，每皮肤一块——背景图缩略图（图片皮肤复用 `skin.preview` data URL，token-only 给渐变色板）+ accent swatch + 本地化名称。选中态镜像 **resolved** active 主题（系统偏好解析到 light/dark 时无瓦片选中）。点击 → `ctx.theme.setTheme(id)`；store 的 `revision` 守卫丢弃过期重复 sync（`settings-store.ts:24-29`）。

7. **质量门禁**（`pnpm verify` = `scripts/verify.mjs`）：①workspace 级 typecheck + build + test + i18n；②产物存在性 + `dshClient` 契约声明检查；③**冒烟**：把 `lib/client.js` 在 `node:vm` 沙箱里以假 loader（注入 externals require）跑一遍，对 stub ctx 调 `apply()`，验证 bundle 在浏览器形态下能启动；④`skins.spec.ts` 查 id 唯一/不撞内置主题/token 非空/CSS 作用域在 `body[data-ds-skin]` 下/`focal`/`preview` 合法/Safe CSS（只允许 background-* 属性，禁 `!important` 与布局属性）；⑤i18n 双语一致性门禁（结构签名：标题层级/代码块逐字/表格行列数/列表形状/链接目标必须两侧一致）。

8. **发布机制**（`scripts/publish.mjs`）：`git rev-parse HEAD` 当不可变身份 ref，重写 `catalog.json`（schema `dsh-skins-index/v0.2`，含 `id/type/ref/source/description/descriptionEn`）+ 双语 README 的 `<!-- INSTALL -->` / `<!-- REFS -->` 块。pin 到 commit 的纪律（"no implicit latest"）——更新皮肤 = 新 commit + 重跑 publish。

## 与 DeepSeek Harness 主仓库的集成点

- **插件 seam**：客户端插件（`dshClient` 契约），与官方内置客户端插件（ui-theme/ui-sidebar/...）**完全同构**——`web.cordis.yml` 加一行 + 包可解析。挂载点：`dsh web` 的 `ClientModuleHostService` 浏览器名册（`window.__DSH_BOOT__`）。
- **协议层**：
  - `@deepseek-ai/dsh-client-ui-theme` 的 `ThemeService.register({ id, colorScheme, tokens })` —— 主题注册表面；
  - `--dsw-static-*` / `--dsw-alias-*` / `--dsw-specific-*` 三层 CSS 自定义属性 token 体系（权威源：`packages/client/ui-theme/src/styles/design-platform.css`）—— 皮肤主要覆盖 alias 层；
  - `@deepseek-ai/dsh-client-ui-slots` 的 `settings.general.item` slot + `deferRegistration` —— 设置页 UI 入口；
  - `window.__ModuleLoader__.load({ id, factory })` closure-factory 浏览器 bundle 协议；
  - `ctx.on('theme/change', ...)` 事件 + `defineStore` snapshot-store 引擎（`@deepseek-ai/dsh-client-runtime/client`，官方"临时豁免"路径）。
- **配置挂载**：`$DSH_HOME/config.yaml` 追加 `- insert: [{ id: dsh-web-skins, name: '@dsh-external/dsh-web-skins' }]`，重启 `dsh web` 生效（bundle 内容变更走 HMR watch → `rebuilt()` 换 rev，无需重启）。
- **类型依赖**：`@deepseek-ai/dsh-client-*` 通过 `link:` 指向**兄弟目录**的 DSH 快照 checkout（`fulltest-wt/`，对应私有镜像 `dsh2026/test-作者（昵称已脱敏）`），CI 也 clone 一份；缺快照 `pnpm install` 直接失败。
- **不修改核心**：纯客户端扩展，不动 harness 任何源码；与 dsh-hub（正经插件）/ toybox（整活插件）的 `.dsh-plugin` 市场格式**不同**（该格式不支持 web 代码）。

## 亮点与风险

### 亮点
- **零核心改动的范式样本**：三段全是官方公开扩展点（ThemeService.register + settings slot + `--dsw-*` token alias），卸载无残留；`skin-dom.ts` 注释明确"只回收自己写的东西"，与官方 ThemePresenter 职责边界清晰。
- **AI 生图背景自包含**：data URL 内联进 bundle，无外部托管、无仓库二进制；token 层保证可读性（半透明基底 + 不透明内容层），CSS 仅限 `background-*` 类属性（Safe CSS 门禁）。
- **工程质量高**：vendored 官方 tsdown 预设（明确对齐 snapshot commit），vm 沙箱产物冒烟，vitest 5 个测试文件覆盖 apply/skins/skin-dom/SkinRow/store，i18n 双语结构签名门禁，单一发布脚本（pin commit + 重写 catalog + 双语块）。
- **可复用的皮肤纪律**：token-only 优先（nord 是参考实现）；写 CSS 必须作用域在 `body[data-ds-skin="<id>"]` 下；新皮肤四步入住流程文档化（写定义 → 生图 → verify → README 登记）。

### 风险
- **catalog.json 发布 ref 落后于 HEAD**：`catalog.json` pin 到 `083d4c7a730f1e0d67a12e3a32e639af7a5d0f97`（updated `2026-08-04T17:26:22Z`），但仓库 HEAD 已是 `07238b2`（`2026-08-05T02:29:32+08:00`，"test: 补齐测试缺口"）；最新提交后没重跑 `pnpm publish`，README REFS 块与 catalog 不一致——下游按 catalog ref 安装会拿不到最新测试与修复。`catalog.json:4-5`、`README.md` REFS 块。
- **强依赖私有兄弟快照**：5 个 `@deepseek-ai/dsh-client-*` 走 `link:../../../fulltest-wt/...`，`pnpm install` 缺快照即失败（`docs/install.md` "前置"节）；CI 也依赖能 clone `dsh2026/test-作者（昵称已脱敏）`（私有）——离开 dsh-external 组织完全无法构建。
- **设置页 slot 形状耦合**：`SkinRow` 复用官方 `settings.general.item` slot 结构，官方重构该 slot 时需跟随适配（`docs/install.md` "已知限制"已自承）。
- **bundle 体积偏大**：`skin-styles.ts` 39.5KB（base64 SVG 内联），`lib/client.js` 67.6KB + `client.js.map` 77.9KB——4 个皮肤就这个量级，皮肤数增长会线性放大。
- **AI 生图工作流未自动化**：`embed-image.mjs` 只做单图转 data URL，提示词工程 + 水印 SVG 叠加 + 贴回 `skin-styles.ts` 全靠手工；`gen-skin-styles.mjs` 只处理 `docs/images/*.svg`，PNG 走另一条路（直接贴 data URL），两条艺术资产路径容易混淆。
- **SkinRow 首渲竞态靠 revision 守卫兜底**：`client/index.ts:53-60` 的 `bound?.sync(...)` 在 `bound` 未赋值时静默丢弃事件，靠注册完成后从 getter 重 sync 补救——若 `theme/change` 在 `injected` 调用与首渲之间密集触发，依赖 `revision` 单调递增做去重，假设 theme service revision 严格单调。
- **私有仓库 + 个人版权**：README 明确"正式公开前请勿公开分发"，当前仅供内测；下游集成需先获得 dsh-external 组织读权限。

## 维护状态

- **default_branch**：`main`（depth 1 clone 仅可见 HEAD `07238b2`）。
- **最近 push**：`2026-08-05 02:29:32 +0800`（= `2026-08-04 18:29:32 UTC`，与任务描述吻合），最新提交是测试补齐（SkinRow 瓦片组件行为测试 + 艺术资产单一来源校验 + verify 增加预览页/token 表存在检查）。
- **提交活跃度**：单次 shallow clone 只看到 1 个 commit，但 README 提到对齐的官方 snapshot 已迭代到 `20260804T143803Z`（0804），并明确列出"0804 sourcemap 对齐 / 0803 → 0804 delta"，说明仓库紧跟官方 snapshot 高频迭代。
- **README 质量**：优秀——双语（zh 是默认 + en 镜像 + i18n sidecar hash），含住户表、原理段、构建链、入住指南、纪律段、规划中皮肤、i18n 门禁说明、文档索引；代码注释同样双语且说清"为什么"（职责边界、官方豁免、对齐 delta）。
- **CI**：`.github/workflows/verify.yml` 在 push main / PR 时跑完整 `pnpm verify`（含 vm 冒烟），但需 CI 能 clone 私有快照镜像。
- **测试覆盖**：5 个 vitest spec（apply 组合 / skins 定义 / skin-dom 行为 / SkinRow 瓦片 / settings-store），加 verify.mjs 的产物冒烟。

## 备注

- **与 Codex-Dream-Skin 的关系**：README 与 gallery.md 明确参考 [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)（MIT）的"一图一情绪"与图库试穿思路，但本仓库是 DSH Web GUI 的独立实现，不是 port。
- **规划中皮肤**：赛博竹林 `neon-bamboo`（dark）、墨韵 `ink-wash`（light）、港城夜色 `harbor-night`（dark）——候选状态，未开工。
- **三种安装路径**（`docs/install.md`）：①克隆 + `pnpm add link:<clone>/packages/dsh-web-skins`（推荐）；②`github:` 依赖（待定型，根包是 workspace 壳需先改造）；③直接配置行（包必须先可解析）。
- **不可变身份纪律**：每个 commit 是一个不可变发布身份，更新皮肤 = 新 commit + 重跑 `pnpm publish` 换 ref——这与 dsh-hub / toybox 的 `github:...#&path:` 路径形安装不同（本包不能走市场格式，因为 `.dsh-plugin` 不支持 web 代码）。
- **token 体系权威源**：DSH 主仓库 `packages/client/ui-theme/src/styles/design-platform.css` 是 token 体系的权威定义；本仓库的 `preview/index.html` 直接引用该文件（经兄弟快照）渲染试穿页。
