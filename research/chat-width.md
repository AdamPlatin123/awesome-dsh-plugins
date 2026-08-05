# dsh-external/chat-width 调研摘要

## 一句话定位
DSH Web 的「消息列宽度调节」客户端插件：让用户拖动输入框左右边缘即可调整 AI 回复正文的消息列宽度（默认固定 748px、宽屏左右留白），并把偏好持久化到 localStorage；零核心改动，纯样式表与 DOM 注入。

## 技术栈与依赖
- 语言/构建：TypeScript 5.9 + tsdown 0.22（产物 `lib/index.js` + `lib/client.js` 随源码提交）；Vitest 4 + Testing Library + jsdom 跑 44 个测试
- 运行时 peerDependencies：`@deepseek-ai/dsh-client-runtime`、`dsh-client-locale`、`dsh-client-ui-slots`、`cordis` 4、React 18
- devDependencies 用 `link:` 指向 DSH 0805 凌晨快照（`staging-20260805T022914Z`），即开发期把 harness 当作对端
- 包通过 `dshClient: { inject: [...], platform: 'web' }` 声明自己是 DSH Web 客户端插件包；`exports` 暴露 `.`（host loader，空 apply）和 `./client`（浏览器半）
- 仅 Web 平台，无 Node 半逻辑

## 文件结构概览
```
chat-width/
├── package.json            # @dsh-external/chat-width 0.1.0，private，dshClient 声明
├── install.sh              # 一键 link 进 harness + 写 ~/.dsh/config.yaml
├── INSTALL.md              # 组织内安装/卸载/开发指引（中）
├── README.md / README.en.md
├── tsconfig.base.json / tsconfig.json
├── tsdown.config.ts        # 双入口打包（host + client）
├── vitest.config.ts
├── lib/                    # 构建产物（已提交）：index.js, client.js(29KB)
└── src/
    ├── index.ts            # host loader：apply() 空实现
    ├── width.ts            # 纯策略：MIN/MAX/STEP、PRESETS、clampWidth、parseWidth
    ├── persistence.ts      # localStorage 读写（key dsh-external.chat-width）
    ├── stylesheet-engine.ts# 核心：改写官方 --dsh-chat-content-width 变量/兜底 0803 硬编码
    └── client/
        ├── index.ts        # 插件主体（cordis apply）：引擎+持久化+手柄+设置行
        ├── drag-handle.ts  # 两侧拖拽手柄（纯 DOM + Pointer Events）
        ├── WidthRow.tsx    # 设置页「消息宽度」行（预设 pill + 当前值只读）
        ├── WidthRow.module.css
        ├── settings-store.ts # defineStore 单写者：px + 单调 revision
        └── locales.ts      # zh/en 文案（namespace settings.chatWidth）
```

## 核心功能与实现要点
1. **样式引擎双代兼容**（`src/stylesheet-engine.ts`）：
   - 0804+ 「variable mode」：定位官方定义 `--dsh-chat-content-width` 的那一条 `CSSStyleRule`，直接 `setProperty` 改写变量值，输入卡（列宽+32px）与「回到底部」对齐随之联动；同时注入一份 `:root` 定义供位于会话根之外的拖拽手柄读取。
   - 0803 「legacy mode」：把硬编码 `736px`（消息列、stats 行、对齐 calc）**幂等**替换为 `var(--dsh-chat-content-width, 736px)`，再通过注入 `:root` 喂值；每条规则只转一次，HMR 重注入后下次调用会重新探测并自愈（`stylesheet-engine.ts:166-220`）。
2. **拖拽手柄几何**（`src/client/drag-handle.ts`）：列居中，故「右边缘 x = (视口+宽)/2」「左边缘 x = (视口−宽)/2」；手柄贴在**输入卡**边缘而非列边缘，0804 卡比列宽 32px、0803 卡固定 800px，所以 `dragCenter()` 把 `(cardWidth - columnWidth)/2` 的内缩折算进虚拟中心，使 `width = 2·(x − center)` 的 2× 公式对两代都精确（`drag-handle.ts:90-130`）。双击重置为官方默认。
3. **测量而非假设**（`src/client/index.ts:120-160`）：通过持久 `var(--dsh-composer-card-max-width)` 探针 div 解析卡片宽度（避免每次测量触发 MutationObserver 自激），并以 `[data-conversation-scroll]` 中心作 hero 阶段兜底；`MutationObserver` + `requestAnimationFrame` 合并布局抖动，窗口缩放/会话切换/侧栏折叠后自动重贴。
4. **声明式可见性**：手柄仅在会话页存在（`body:has([data-conversation-scroll])`），悬停或拖拽中才显现，平时页面无任何常驻竖线；样式由插件自带 `<style data-plugin="@dsh-external/chat-width">` 注入，与 dsh-skins 同款「直接动 document」先例。
5. **设置行集成**（`src/client/WidthRow.tsx` + `index.ts:185-215`）：通过 `deferRegistration` 注册到 `settings.general.item` 槽（order 30），提供紧凑 640 / 宽屏 960 / 超宽 1280 三个预设 pill + 「跟随官方」重置；当前值只读，所有写入走「引擎 + 持久化 + store」三联 `applyWidth`，store 单写者配合单调 revision 防过期回放。
6. **持久化策略**（`src/client/index.ts:60-80`）：拖拽过程 300ms 节流写 localStorage，拖拽结束 / pill 点击立即落盘；范围 320–2560px，越界/非整数读回 null（视为跟随官方）。
7. **纯策略可测**：`width.ts`（钳位/解析/预设）与 `persistence.ts` 完全无 DOM，44 个 vitest 用例覆盖宽度策略、引擎、持久化、拖拽手柄、设置行。

## 与 DeepSeek Harness 主仓库的集成点
- **客户端插件包契约**：`package.json` 的 `dshClient: { inject: ['@deepseek-ai/dsh-client-runtime', '@deepseek-ai/dsh-client-locale'], platform: 'web' }` 是 DSH Web 客户端插件的注册声明；harness 配置树通过 `~/.dsh/config.yaml` 里一行 `name: '@dsh-external/chat-width'` 解析并加载。
- **运行时 API 依赖**：消费 `ClientContext`（cordis 上下文）、`ctx.effect`、`ctx.locale.register`、`ctx.slots.register`、`deferRegistration`、`defineStore`、`PropsRuntime/PropsStore/PropsLocale` 等官方 client-runtime / ui-slots / locale 表面。
- **DOM 槽位约定**：依赖会话根 `[data-conversation-scroll]`、输入卡容器 `[data-composer-seat]`、CSS 变量 `--dsh-chat-content-width`、`--dsh-composer-card-max-width`，以及 `--dsw-alias-*` 设计令牌——这些是 harness 0804+ 的稳定表面。
- **dev 期联编**：`devDependencies` 用 `link:../.dsh/source/staging-20260805T022914Z/...` 把 harness 当对端做类型检查与测试。
- **安装方式**：`pnpm add -w link:<path>` 进 harness workspace + 写 `~/.dsh/config.yaml` 一行；或 git 依赖固定 commit；重启 `dsh web` 生效。
- **节点半留空**：`src/index.ts` 的 `apply()` 为空——所有逻辑在浏览器半，因为宽度调节只动 Web 客户端样式表，无服务/Node 行为。

## 亮点与风险
- **亮点**
  - 双代兼容 + 幂等转换：单一代码路径同时支持 0804 变量代与 0803 硬编码代，且 0803 转换可重复执行不破坏已转规则（`stylesheet-engine.ts:113-138`）。
  - 拖拽几何用「虚拟中心折算内缩」一招吃掉输入卡比列宽的差，2× 公式对两代都精确，避免在拖拽中重测列宽（`drag-handle.ts:90-130`）。
  - HMR/异步 bundle 自愈：失败的定义探测不缓存，下次 `setWidth` 重探；被 HMR 摘掉的规则捕获异常后落回注入定义（`stylesheet-engine.ts:200-230`）。
  - 探针 div 一次创建、seat 重挂时才再连，规避「测量 → MutationObserver → 再测」自激循环（`client/index.ts:130-150`）。
  - 纯策略模块（width/persistence）零 DOM，44 个测试覆盖核心几何与边界。
- **风险**
  - 强耦合官方 DOM 选择器与 CSS 变量名（`--dsh-chat-content-width`、`--dsh-composer-card-max-width`、`[data-composer-seat]`、`[data-conversation-scroll]`、CSS Modules 哈希类里的 `736px` 字面量）：harness 任一改名/重构都会让对应代失效；0803 legacy 路径靠扫描 `736px` 字面量，若官方改为别的像素值或 calc，legacy 转换会静默失效（`stylesheet-engine.ts:113-138`）。
  - `walkRules` 只下钻一层 `@media`，更深的 `@layer`/嵌套 `@media` 不扫（已注释承认「shipped sheets 不用更深」，但 harness 演进后需复查）（`stylesheet-engine.ts:70-90`）。
  - `lib/` 构建产物随源码提交（29KB `client.js`），若贡献者只改源码忘跑 `pnpm build`，安装者会拿到过期 client——INSTALL.md 已写「构建产物已入库，无需构建」即默认信任此约定。
  - devDependencies 用绝对 `link:` 路径指向特定 staging 快照（`staging-20260805T022914Z`），换机器/换快照需手改 package.json，复现性脆弱（`package.json` devDependencies）。
  - 跨源样式表的 `cssRules` 不可读时静默跳过（`stylesheet-engine.ts:75-79`），若官方表被打到独立 origin/被 CORS 隔离，会退化到 legacy 兜底而不报错。
  - 窄屏下「列撑满，拖拽只改变量值，视觉无变化」是已知限制（README 已注明），用户可能误判为坏。

## 维护状态
- 仓库非空，单文件历史可见（`--depth 1` 仅见 HEAD `12db242` 「feat: one-command install script + README install section」，提交时间 **2026-08-05 14:28 +0800**，即调研当日）。
- 0.1.0 首发，私有仓库（README/INSTALL.md 均标「仅限 dsh-external 组织成员」），处于首轮交付期；44 个 vitest 测试 + typecheck + tsdown 构建脚本齐备。
- devDependencies 锁定到当日凌晨 staging 快照，与 harness 0804+ 表面同步，可视为活跃维护。

## 备注
- 与本批其它「客户端插件包」结构同型（`dshClient` 声明 + `exports['./client']` + cordis `apply` + ui-slots 注册），可作为该范式的参考样板。
- 安装可走两条路径：`install.sh`（link + 写 config.yaml，幂等）或 `pnpm add '@dsh-external/chat-width@github:dsh-external/chat-width#<commit>'` 固定 commit；二者都需重启 `dsh web`。
- 脱敏：本摘要不含作者邮箱/真名；所有引用均为文件路径与公开 API。
