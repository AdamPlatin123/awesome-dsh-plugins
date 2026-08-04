# dsh-subagent-tree 调研摘要

## 一句话定位

非官方的 DeepSeek Harness 工作区侧栏树子代理分支插件：把父会话下的子代理目录渲染为会话行内（展开箭头 + 运行计数）与会话行下（嵌套分支树）两个扩展 hole 的 UI 组件，让子代理执行过程从"不可见"变成"侧栏可点击回看"。

## 技术栈与依赖（语言、框架、关键依赖）

- **语言/类型**：TypeScript（严格类型，`type: module`，ESM）。React 18 JSX/TSX 组件。
- **框架/宿主**：基于 cordis 4.0.0-rc.7（DSH 的插件框架）+ DSH 自研的 client runtime / locale / ui-slots / ui-workspace / ui-primitives / invariants 等内部包（全部 `@deepseek-ai/dsh-*` workspace 依赖，未发布 npm）。
- **运行平台**：纯 Web/browser 客户端（`dshClient.platform: "web"`），无 Node 端、无后端。
- **构建**：tsdown（client bundle 入口模板 `tsdown.client.ts`）+ tsconfig 项目引用。测试用 vitest + jsdom + @testing-library/react。
- **运行时依赖**：仅 `clsx ^2.0.0` 与 `react ^18.2.0`；其余为 workspace peer/dev 依赖。
- **许可证**：插件本体 BSD-3-Clause；仓库根 README 说明文档 MIT；版权 2026 vlln。

## 文件结构概览（顶层目录/关键文件树）

```
dsh-subagent-tree/                         仓库根（MIT 说明文档层）
├── LICENSE                                MIT, vlln 2026（仓库说明文档层）
├── README.md                              仓库级说明（特性/安装/隐私/已知限制）
└── packages/
    └── client/
        └── ui-subagent-tree/              ★ 插件本体（BSD-3-Clause）
            ├── package.json               dshClient 声明 + exports 映射
            ├── tsconfig.json              项目引用配置
            ├── tsdown.config.ts           client bundle 入口
            ├── README.md / README.zh.md   插件包说明（英/中）
            ├── README.i18n.yaml           插件包 i18n 元数据
            ├── src/
            │   ├── index.ts               node-half apply()（空占位）
            │   ├── invariant.ts           invariant companion（空 installer）
            │   ├── css-modules.d.ts
            │   └── client/
            │       ├── index.ts           ★ browser-half apply：注册两个组件到 slot
            │       ├── contract.ts        SubagentTreeInjected 接口（openSubagent / setSubagentCatalogOpen）
            │       ├── store.ts           展开状态 store（defineStore toggle）
            │       ├── tree.ts            ★ 纯函数 subagentNodes：目录→行树投影
            │       ├── locales.ts         zh(源)/en 字典，命名空间 'subagent-tree'
            │       ├── SubagentRowActions.tsx + .module.css   行内组件（箭头+计数）
            │       ├── SubagentBranch.tsx  + .module.css      行下分支组件
            │       └── SubagentNodeItem.tsx + .module.css     单行子代理项
            └── tests/
                ├── tree.spec.ts           纯函数推导（22 项之一组）
                ├── branch.spec.tsx        分支渲染/HMR 释放/嵌套展开
                ├── node-item.spec.tsx     单行点击/键盘导航/禁用态
                ├── row-actions.spec.tsx   行内组件条件渲染
                ├── apply.spec.ts          slot 注册 + store 共享 + inject 委托
                └── invariant.spec.ts      invariant companion + node-half no-op
```

## 核心功能与实现要点

1. **会话行扩展 hole 机制（双 hole 注册）**——插件的核心挂载点。`src/client/index.ts` 的 `apply()` 通过 `deferRegistration` 向宿主 `ui-workspace` 声明的两个 keyed slot 注册组件：`sidebar.workspaces.sessionRow`（行内：`SubagentRowActions`）与 `sidebar.workspaces.sessionRow.branch`（行下：`SubagentBranch`）。"defer" 是因为 ui-workspace 与本插件激活顺序不定，需等 hole 声明落到 slot ledger 后再注册（apply.spec.ts 专门验证此竞态）。两个组件共享同一个展开 store 句柄（`store.ts` 的 `createSubagentTreeStore`），由 apply 内一次性创建并注入，避免模块级句柄在 HMR 重载时钉死身份。

2. **行内组件（展开箭头 + 运行计数）**——`SubagentRowActions.tsx`：当会话有子代理子项时渲染一个展开箭头按钮（`IconTriangleRightFill14`）和"N 个运行中"计数；点击 toggle 触发 `actions.toggle(sessionId)` + `setSubagentCatalogOpen(sessionId, openNow)`。无子代理则渲染 `null`（不占位）。这是会话行右侧的轻量指示器。

3. **行下分支组件（嵌套子代理树）**——`SubagentBranch.tsx`：展开后渲染嵌套行，用 `useEffect` 在展开/卸载时 `setSubagentCatalogOpen(parentId, true/false)` 标记父为活跃目录消费者（并触发目录刷新），清理函数保证行消失时释放订阅（防泄漏，测试覆盖）。递归 `renderNodes` 按 depth 缩进渲染子代行。

4. **纯函数推导树 `subagentNodes`（`tree.ts`）**——核心数据流。输入：父 sessionId、运行时 `subagentsByParent` 目录快照、`byId` 摘要、展开数组；输出 `{nodes, running}`。逻辑：优先消费目录的 `child` 条目（跳过 `diagnostic`）；目录未水合时用 summary 投影出"加载中"占位行（标签用 `displayTitle`）；展开的子节点递归进入其自己的目录聚合 `runningSubagents`。标签降级链：`entry.label ?? summary.displayTitle ?? entry.id`（tree.spec.ts 第 4 个用例显式验证三级降级）。

5. **单行子代理项 `SubagentNodeItem.tsx`**——纯展示组件，完整无障碍支持：`role="treeitem"`、`aria-expanded`、`aria-disabled`、`aria-label` 展开/折叠。点击或 Enter/Space 通过 `openSubagent({parentSessionId, childSessionId, mode})` 打开子代理执行记录（持久化直接父地址）。ArrowRight/ArrowLeft 控制子分支展开/折叠。加载/出错态渲染禁用占位。相对时间分桶（刚刚/分钟/小时/天/月）镜像宿主 workspace 行。

6. **国际化（locales.ts）**——命名空间 `'subagent-tree'`，zh 为键集真值，en 完整对齐。通过 `ctx.locale.register(NS, {zh, en})` 注册（apply 内 `ctx.effect` 包裹），并用 `declare module` 扩展宿主 `LocaleNamespaceMap`。字典覆盖行标签、aria 文案、时间桶 11 个键。

7. **invariant companion（`src/invariant.ts`）**——DSH 的"包归属预约"机制：空 installer，仅 `ctx.invariants.register(PACKAGE_NAME, install)` 预约包名，无运行时不变量。`src/index.ts` 的 node-half apply 是空函数，只为在宿主 cordis.yml/Loader 中出现；真实 UI 经 `exports["./client"]` 被 dshClient 声明发现。

8. **数据契约与安全声明**——组件所有数据来自宿主 `sessions.subagentsByParent`（目录快照）与 `sessions.byId`（摘要），动作仅 `openSubagent` / `setSubagentCatalogOpen`。README 明确声明"不采集、不上传任何数据，无网络请求、无遥测"。

## 与 DeepSeek Harness 主仓库的集成点

- **插件 seam**：源码级集成（非打包产物）。需把 `packages/client/ui-subagent-tree/` 复制到 DSH monorepo 同路径，在 `tsconfig.client.json` 的 `references` 加项目引用，在 `apps/cli/config/web.cordis.yml` 的 `dshClient` 列表登记：
  ```yaml
      - id: ui-subagent-tree
        name: '@deepseek-ai/dsh-client-ui-subagent-tree'
  ```
  并在 `apps/cli/package.json` 的 dependencies 加 `"@deepseek-ai/dsh-client-ui-subagent-tree": "workspace:^"`，`pnpm install` 后 `pnpm --filter @deepseek-ai/dsh-client-ui-subagent-tree bundle` 产出 client bundle。
- **协议/挂载**：宿主必须已声明两个会话行扩展 hole（`sidebar.workspaces.sessionRow` 与 `sidebar.workspaces.sessionRow.branch`，对应官方 `ui-workspace` 包的扩展点）。插件向这两个 keyed slot 注册组件（key=`'subagent-tree'`）。无 config、纯 UI。
- **依赖包**：peer/dev 依赖 `@deepseek-ai/dsh-client-runtime`、`-locale`、`-ui-workspace`、`-ui-primitives`、`-ui-slots`、`-test-runtime`、`dsh-invariants`（均源码级 workspace，未发 npm）。
- **关联 issue**：`dsh-external/issues#44`（`[feature][web] subagent 执行过程不可见`）——本插件为该诉求的社区实现。

## 亮点与风险

**亮点**
1. **架构清晰、纯函数可测**：`tree.ts` 把"目录快照→行树"做成无副作用纯函数，组件层只渲染；测试用例直接断言纯函数输出，覆盖降级链、递归聚合、诊断过滤。22 项单测覆盖推导/行内动作/分支/键盘导航/apply 注册/HMR 释放。
2. **正确处理插件加载竞态**：`deferRegistration` 等 hole 声明落账后再注册，避免 ui-workspace 与本插件激活顺序不确定导致的注册丢失（apply.spec.ts 显式验证）。
3. **资源释放严谨**：分支展开用 `useEffect` cleanup 在折叠/卸载时调 `setSubagentCatalogOpen(id, false)` 释放目录订阅，防泄漏；store 句柄在 apply 内创建而非模块级，避免 HMR 钉死身份。
4. **无障碍与 i18n 到位**：`treeitem` 角色、aria 属性、键盘导航（Enter/Space/Arrow）、中英双字典 + 命名空间扩展。

**风险**
1. **强耦合宿主内部包且未发布**（`packages/client/ui-subagent-tree/package.json:36-49`）：peer/dev 依赖大量 `@deepseek-ai/dsh-*` 的 `^0.0.1`，均未发 npm，只能在 DSH 源码 workspace 内构建。宿主版本漂移（API 变更）会直接破坏插件，且无 lockfile 锁定。
2. **强依赖宿主声明会话行 hole**（`src/client/index.ts:34-43`、README"已知限制"）：若官方 `ui-workspace` 移除或改名这两个 slot，组件静默不注册（用户侧表现为"装了没反应"，无报错、无降级提示）。
3. **目录水合期降级行为可能误导**（`src/client/tree.ts:31-45`）：summary 投影的加载行 `mode` 硬编码为 `'one-shot'`，但真实续接模式要等目录水合才知；用户在水合期点击会被以 one-shot 地址打开，可能与真实模式不符（理论风险，无显式处理）。
4. **fork 分支不继承父会话子代理目录**（README"已知限制"+ 宿主血缘设计）：fork 出的会话不会显示其源会话的子代理，属宿主行为但用户可能误以为是 bug。
5. **`Date.now()` 直接调用**（`src/client/SubagentNodeItem.tsx:81`）：相对时间分桶用 `Date.now() - updatedAt`，非时间旅行测试友好（测试需固定时间或断言放宽）；非生产风险，仅测试鲁棒性。

## 维护状态

- **default_branch**：`main`
- **创建/最近 push**：均 2026-08-04（创建 18:30:03Z，push 18:41:17Z）——**当天新建仓库**，极早期。
- **提交活跃度**：仅 2 次提交，全部来自作者 `vlln`：
  - `451d0d7`（18:30:40Z）`feat: workspace sidebar subagent branch plugin (source-shared)`
  - `c427938`（18:41:14Z）`docs: link issue #44 and show result screenshot`
  无后续迭代、无 issue/PR、无 contributor。
- **README 质量**：**优秀**。仓库根 README 含特性、截图、目录结构、详细安装步骤（含 cordis.yml/package.json 片段）、隐私声明、已知限制、开发命令；插件包内 README 双语（英/中）+ i18n yaml。文档密度高于代码量。
- **size**：GitHub 报 0KB（私有仓库元数据未统计），实际 clone 含 11 源文件 + 6 测试，约 30KB 源码。
- **状态结论**：v0.0.1 首发源码共享版，作者声明"内测共享"，文档完备但需宿主同快照（官方 0804）才能构建运行。

## 备注

- **非官方性质**：仓库属 `dsh-external` 组织（DSH 内测社区），README 与描述反复声明"版权归作者本人所有；官方不保证公开发布后该组织仍然存在，请自行保留副本"——属于社区第三方插件，非 DeepSeek 官方维护。
- **双许可证**：插件本体 BSD-3-Clause（`package.json`），仓库说明文档层 MIT（根 LICENSE）——分发时需分别对待代码与文档。
- **解决的痛点明确**：对应 `dsh-external/issues#44`，是 DSH Web 端"子代理执行过程在侧栏不可见"这一 UX 缺口的社区补丁，产品价值清晰。
- **无可执行验证**：因依赖未发布的 DSH workspace 包，无法在隔离环境跑测试/构建；调研仅基于源码与测试用例静态分析。测试用例本身设计严谨（断言具体行为而非实现），可信度较高。
