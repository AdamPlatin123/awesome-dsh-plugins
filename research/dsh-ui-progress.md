# dsh-external/dsh-ui-progress

## 一句话定位
DeepSeek Harness Web GUI 的纯客户端 UI 进度插件——零核心改动地为 Web 端补充两处进度呈现：输入框停靠区的常驻会话进度条 + `report_progress` 工具调用动画卡片。

## 技术栈与依赖
- 语言/构建：TypeScript（ESM）、`tsdown` 打包（基于 rolldown）、`lightningcss` 处理 CSS Modules，输出三份产物（`lib/index.js` Node half、`lib/invariant.js` invariant companion、`lib/client.js` 浏览器 bundle，后者以 `window.__ModuleLoader__.load({ id, factory })` 形式自注册）。
- UI 框架：React 18（peerDependency `^18.2.0`），`clsx` 合并类名。
- 插件宿主：`cordis ^4.0.0-rc.7`（peer）、`@deepseek-ai/dsh-client-ui-primitives`、`@deepseek-ai/dsh-tool-todo`（peer，仅消费其 `todos` session projection 类型）。
- 注入的 client 服务（`dshClient.inject`）：`dsh-client-locale` / `dsh-client-runtime` / `dsh-client-ui-conversation`。
- 运行时 platform module（loader 冻结模块表外部依赖）：`react`、`react/jsx-runtime`、`react-dom*`、`cordis`、`@deepseek-ai/dsh-client-{ui-slots,web-react,ui-primitives,schema-form}` 以及 `dsh-client-runtime/client`。
- devDependencies 全部以 `link:../.dsh/source/current/...` 形式从已构建的 DSH 快照解析（与本批其它 dsh-external 仓库一致）。
- 许可：BSD-3-Clause；私有包 `@dsh-external/dsh-ui-progress` v0.1.0。

## 文件结构概览
```
dsh-ui-progress/
├── README.md                  # 功能与限制说明
├── INSTALL.md                 # 组织内安装路径（link / git 依赖）
├── dsh.plugin.json            # 插件清单：contributes.tools=["report_progress"]
├── package.json               # dshClient.inject 声明 + exports 映射
├── tsconfig.json / tsconfig.base.json
├── tsdown.config.ts           # 三产物打包配置 + CSS Modules 内联 + bundle 纯净门
├── pnpm-lock.yaml
└── src/
    ├── index.ts               # Node half：空 apply（仅占位注册到 Loader）
    ├── invariant.ts           # invariant companion：只占包名，无运行时校验
    ├── css-modules.d.ts
    └── client/
        ├── index.ts           # 浏览器 half：注册词典 + 两个 slot
        ├── locales.ts         # progress 词典（zh/en，zh 为键集真相源）
        ├── SessionProgressBar.tsx + .module.css
        └── ProgressCard.tsx   + .module.css
```

## 核心功能与实现要点

1. **常驻会话进度条**（`conversation.input.dock` slot，`order: 20`）：`SessionProgressBar` (`src/client/SessionProgressBar.tsx:139`) 直接读取框架 `useSession` 快照与 `useProjection('todos')`，渲染真实执行状态——运行中/空闲、当前在飞工具名（`snapshot.runningCalls[0]?.name`）、是否在出推理（`partial.blocks` 含 `reasoning`）、轮次数（`turnTimings.size`）、已结算工具结果数（`snapshot.nodes` 中 `kind==='tool-result'` 计数）。运行中左侧 `IconLoadingOutline16` 加载圈旋转、shimmer 扫光、品牌色 `box-shadow` 光环脉冲；空闲时静态填充。

2. **进度百分比的"真相优先"策略**（`progressPercent`，`src/client/SessionProgressBar.tsx:97`）：若存在非空 `todos` 投影，按 `(done + in_progress)/total` 计算真实任务完成度（进行中的也计入，所以 2 完成且 1 进行中 / 共 5 = 60%）；否则按"每个已结算工具结果推进一格、上限 10"作为有界启发式（每个结果 `*10`，clamp 到 100）。这是最新提交 `feat: count in-progress todos toward the progress fill` 的改动。

3. **`report_progress` 工具卡片**（`conversation.chat.toolview` slot，按 `key: 'report_progress'` 注册，`src/client/index.ts:54`）：`ProgressCard` (`src/client/ProgressCard.tsx:62`) 解析工具 args（`task/percent/stage/note`），`toPercent` 把模型给的任意数值钳到 0..100（非数读 0），`parseArgs` 容错处理流式中途截断或畸形 JSON。运行中（`!('kind' in block)` 表示是 `RunningToolCall`）显示旋转加载圈 + shimmer；100% 完成时切到 `IconCheckOutline16` + 成功色脉冲光晕；可选 stage/note 行。

4. **`report_progress` 工具本体不在本仓库**：本插件只做呈现。`dsh.plugin.json` 里 `contributes.tools=["report_progress"]` 仅是清单标注；README 与 `src/index.ts` 注释明确："工具本体是独立的宿主插件（如挂载的 demo 或常驻工具插件）"。

5. **空 Node half + invariant companion**：`src/index.ts:8` 的 `apply()` 为空函数（仅让插件出现在 `cordis.yml`/Loader）；`src/invariant.ts:23` 的 invariant installer 也是 `() => {}`——只调 `ctx.invariants.register(PACKAGE_NAME, install)` 占住包名所有权，无运行时校验（因为 toolview slot 注册本身就是被 slot registry 拥有并观测的 effect）。

6. **本地化**（`src/client/locales.ts`）：`progress` 命名空间词典，zh 为键集真相源，en 经 `satisfies ProgressKey` 类型校验确保键集对齐。通过 `declare module '@deepseek-ai/dsh-client-ui-slots' { interface LocaleNamespaceMap }` 合并类型，slot 注册时带 `locale: NS` 让运行时自动把 `t` 注入 props。

7. **bundle 纯净门**（`tsdown.config.ts:118` `dsh-client-bundle-purity` 插件）：任何 `@deepseek-ai/*` 值导入若不在 platform module 表里就在构建期 throw——强制跨插件协作走 cordis 服务（仅类型导入会被擦除、不触发此门）。CSS Modules 经 `dsh-css-inline` 虚拟模块插件用 lightningcss 编译成运行时自注入的 `<style data-plugin data-plugin-css>` 标签，类名映射成 `[hash]_[local]`。

8. **inject 排序边**：`apply` 的 `inject = ['slots', 'conversation', 'locale']`（`src/client/index.ts:42`），但内部又用了一次 `ctx.inject(['slots', 'conversation', 'sessions'], ...)` 包住 dock 注册——README/注释解释 `conversation` 是排序边而非调用依赖，等 ui-conversation 声明 `conversation.input.dock` slot 之后再 register 才不抛未声明 slot 错误。

## 与 DeepSeek Harness 主仓库的集成点
- **peerDependency** 依赖主仓库的 client 子包：`@deepseek-ai/dsh-client-ui-primitives`、`@deepseek-ai/dsh-tool-todo`、`cordis`、`react`。devDependencies 全部 `link:` 到 `~/.dsh/source/current` 的 DSH 已构建快照（`dsh-client-locale/runtime/ui-conversation/ui-primitives/ui-slots`、`dsh-invariants`、`dsh-tool-todo`、cordis vendor）。
- **两个 ui-conversation slot**：`conversation.input.dock`（输入框停靠区，GoalBar 家族）+ `conversation.chat.toolview`（按 `report_progress` 工具名注册的 keyed toolview 洞）。
- **client-runtime**：`useSession` 快照（`ConversationSnapshot`）、`useProjection('todos')`（消费 `@deepseek-ai/dsh-tool-todo` 的 session projection map）、`ToolRowProps` 类型。
- **client-locale**：注册 `progress` 命名空间词典。
- **dsh-invariants**：标准 invariant companion 模式（占包名所有权）。
- **loader module table**：浏览器 bundle 通过 `window.__ModuleLoader__.load({ id, factory })` 自注册；platform modules 必须从 loader 冻结模块表解析（external），不能内联。
- **配置激活**：`~/.dsh/config.yaml` 插入 `id: dsh-ui-progress / name: '@dsh-external/dsh-ui-progress'` 一行，重启 `dsh web` 即生效。

## 亮点与风险
- **亮点**：纯客户端、零核心改动、零运行时 invariant、零配置键——以最小表面积拿到两处 UI 呈现；`todos` 投影真相优先的进度策略比单纯"工具结果数分段"更可信（`src/client/SessionProgressBar.tsx:97`）；bundle 纯净门在构建期硬性切断跨插件值导入，强制走 cordis 服务（`tsdown.config.ts:118`）。
- **风险/限制**：
  - 进度条填充按"窗口分段（每结算一个工具结果进一格、上限 10）"是有界启发式，不是未知总量的真实百分比；会话整体进度的长视图需专门投影（README "Known Limitations"）。
  - 工具卡片严格按 `report_progress` 工具名注册；改名或加命名空间的进度工具需第二条注册（README "Known Limitations"；`src/client/index.ts:48`）。
  - CSS 动效常量（时长/缓动）为本地字面量（`SessionProgressBar.module.css`、`ProgressCard.module.css`），当前样式体系尚无 motion token 族——日后统一可能要返工。
  - `report_progress` 工具本体依赖外部宿主插件提供，本包不可独立工作；清单里 `contributes.tools=["report_progress"]` 容易让人误以为工具定义在此，实际只是标注。
  - shallow clone 仅看到 1 条提交（`ec0dd9c feat: count in-progress todos toward the progress fill`），无法判断完整演进历史。
  - `SessionProgressBar` 对 `session === undefined/null` 做了防御性早返回（`src/client/SessionProgressBar.tsx:145`，带 `oxlint-disable-next-line typescript/no-unnecessary-condition`），暗示宿主类型契约与运行时偶尔不一致。

## 维护状态
- v0.1.0（早期），最近一次提交 `ec0dd9c feat: count in-progress todos toward the progress fill`（date 不可得，shallow clone）。
- 文档完备：README（功能/限制）+ INSTALL.md（两条组织内安装路径）+ 源码注释密度高，呈现纪律与其它 dsh-external 仓库一致。

## 备注
- 安装路径一：`git clone` + `pnpm add -w link:/path/to/dsh-ui-progress`（或 pnpm store 版本不匹配时手动 symlink 到 `node_modules/@dsh-external/`）。
- 安装路径二：`pnpm add '@dsh-external/dsh-ui-progress@github:dsh-external/dsh-ui-progress#<commit>'`（固定 commit，无隐式 latest）。
- 验证方式：会话运行时输入框上方常驻进度条左侧加载圈旋转；模型调 `report_progress` 时对话流出现进度卡片，100% 时脉冲成功色光晕。
- 仓库非空，27 个对象，克隆大小约 33 KB；构建产物 `lib/` 已入库（INSTALL.md 明确"构建产物已入库，无需构建"），但仓库内仍同时保留 `src/` 与 `lib/`。
