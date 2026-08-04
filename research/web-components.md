# web-components 调研摘要

## 一句话定位
`@deepseek-ai/dsh-client-web-component` —— 从 DeepSeek Harness（DSH）`feat-web-components-renderer` 分支剥离出的独立 Cordis 客户端插件，提供一个 `webComponent` 服务，把注册好的 slot 树挂载为浏览器原生 Custom Elements（Web Components），是与 React 渲染器（`web-react`）平行的"原生渲染臂"。

## 技术栈与依赖（语言、框架、关键依赖）
- 语言：TypeScript（ESM，`type: "module"`），严格类型（descriptor 协议编译期 + 运行期双重校验）。
- 框架：Cordis 4.x（`cordis ^4.0.0-rc.7`，作为 client plugin 服务模型）；浏览器原生 `CustomElementRegistry` / Shadow DOM / `CustomEvent`。
- 构建：`tsdown`（`bundle` / `watch` 脚本），产物到 `lib/`。
- 测试：Vitest + jsdom（`loader-composition.spec.ts` 通过真实 vendored Loader 启动整套 fixture composition）。
- 关键 peer/workspace 依赖（全部是 DSH 内部包，**无法独立安装**）：
  - `@deepseek-ai/dsh-client-runtime`（被 `dshClient.inject` 声明依赖）
  - `@deepseek-ai/dsh-client-ui-slots`（slot 注册 API + descriptor 类型协议宿主）
  - `@deepseek-ai/dsh-client-locale`
  - `@deepseek-ai/dsh-invariants`（不变量伴侣）
  - `cordis`
- 包元信息：`version: 0.0.1`、`private: true`、`license: BSD-3-Clause`、`dshClient.platform: "web"`。

## 文件结构概览
```
web-components/
├── README.md                          # 顶层说明：定位、安装到 DSH 的 4 步、发布流程
├── .gitattributes                     # LF 强制 + patches/*.patch 的 trailing-space 豁免
├── patches/
│   └── web-component-plugin.patch     # 54KB：DSH 宿主接缝补丁（不含插件本体）
└── packages/client/web-component/     # 插件本体
    ├── package.json                   # @deepseek-ai/dsh-client-web-component
    ├── README.md / README.zh.md       # 双语协议说明（工作原理/原生视图契约/失败隔离/tag 生命周期/已知限制）
    ├── README.i18n.yaml
    ├── tsconfig.json
    ├── tsdown.config.ts               # 引用 ../tsdown.client.ts（宿主共享，本仓库未包含，见风险）
    ├── src/
    │   ├── index.ts                   # host loader entry（空 apply，无 host 行为）
    │   ├── invariant.ts               # 不变量伴侣：校验 tag-defined 事件与活注册表一致
    │   ├── client/
    │   │   ├── index.ts               # Cordis 插件入口（name='web-component'，inject=['slots']）
    │   │   ├── service.ts             # WebComponentService：mountRoot + TagRegistry + 事件桥
    │   │   ├── registry.ts            # TagRegistry：page-lifetime tag 所有权 + 冲突检测
    │   │   ├── descriptor.ts          # 运行期 descriptor 校验（tagName/构造器/绑定 shape）
    │   │   ├── bindings.ts            # 属性/事件绑定编译器（响应式订阅 + equality gate）
    │   │   ├── mount.ts               # SlotMount/EntryMount/RootMount：挂载与化身(reconcile/teardown)
    │   │   └── diagnostic.ts          # 失败隔离诊断元素 [data-dsh-slot-diagnostic]
    │   └── fixture/                   # 演示用 Custom Element roster（非生产组件）
    │       ├── elements.ts            # 7 个 HTMLElement 子类
    │       ├── roster.ts              # 用 ctx.slots.register 注册全部 slot 类型/作用域
    │       ├── sources.ts / runtime.ts / shell.ts
    └── tests/                         # vitest：mount(36KB)/registry/descriptor/types/invariant/shell + loader-composition
        └── fixtures/composition.cordis.yml
```

## 核心功能与实现要点
1. **提供 `webComponent` Cordis 服务（与 React 渲染器平行的原生臂）** — `src/client/service.ts`：`WebComponentService extends Service`，暴露 `mountRoot(target, ownerProps)`；通过 `ctx.get('slots').host()` 拿到 `SlotRendererHost`（host seam 由补丁加到 `SlotsService`）。挂载句柄由调用方 fiber 的 `ctx.effect` 持有，dispose 时移除整棵原生树。

2. **同一组合 API，descriptor 代替组件** — 注册走 `ctx.slots.register({name,children,store,locale,inject}, descriptor)`，descriptor 形如 `{renderer:'web-component', tagName, constructor, properties, events, outlets}`。类型协议放在 `dsh-client-ui-slots/src/descriptor.ts`（补丁新增），特性包无需 import 本包即可构造；本包拥有运行期解释（`src/client/descriptor.ts` 的 `validateDescriptor`）。

3. **DSH 输入以 JS 属性跨边界（绝不序列化为 attribute）；输出走声明式 CustomEvent** — `src/client/bindings.ts`：`compileProperty` 区分静态绑定（owner/inject/actions/provide-prop/matched，每次化身解析一次）与响应式绑定（standard/provide-hook/projection/store/inject-hook/locale/locale-text，订阅裸源 + 可选 `eq` 相等门）；`compileEvent` 只处理 `CustomEvent`，把 `detail` 转发给解析出的普通回调。元素永远不接收 `ctx`、服务、裸 store 或裸 observable。

4. **作用域用"元素化身（incarnation）"建模，而非 provider** — `src/client/mount.ts`：root 作用域跨会话存活；严格 session 在无会话时缺席、会话 id 变化时换新元素；`session-maybe` 在无会话状态存在并采纳首个会话。`SlotMount.reconcile()` 订阅 slot 变更与 `sessions.provideInfo`，按化身重建 `EntryMount`。

5. **失败隔离 + page-lifetime tag 所有权** — `src/client/diagnostic.ts`：descriptor 校验/元素创建/属性赋值/事件回调/selector/outlet 失败只把该条目替换为 `[data-dsh-slot-diagnostic]` 诊断 div，不影响兄弟树（但 `connectedCallback`/`disconnectedCallback` 内的异常仍是响亮的浏览器错误，不等于 React error boundary）。`src/client/registry.ts` 的 `TagRegistry`：缺 tag 定义成功，同 tag 同 constructor 幂等，同 tag 不同 constructor 抛 `TagConflictError`（要求刷新页面）。

6. **不变量伴侣（invariant companion）** — `src/invariant.ts`：监听 `web-component/tag-defined` 事件，断言活注册表持有且仅持有记录的 constructor；替换 constructor 会 fail（防止"刷新成功的假象下跑旧代码"）。

7. **fixture roster 演示全部绑定种类（非生产组件）** — `src/fixture/elements.ts` + `roster.ts` 注册 7 个真实 Custom Element：`dsh-fixture-frame`（root）、`dsh-fixture-status`（session+store+事件）、`dsh-fixture-tool`（list/keyed，inject）、`dsh-fixture-mode`（chain matched）、`dsh-fixture-greeting`（session-maybe + locale）、`dsh-fixture-projection`（projection cell）、`dsh-fixture-hook`（inject-hook）。`tests/loader-composition.spec.ts` 通过真实 vendored Loader + Include 启动 `composition.cordis.yml`，断言组装树、会话切换、dispose 级联。

8. **外壳通过一行 `ctx.webComponent.mountRoot(document.body, {})` 挂根** — `src/fixture/shell.ts` 是 React shell `ctx.slots.renderSlot('root', {})` 的原生孪生。

## 与 DeepSeek Harness 主仓库的集成点
**强集成（需应用 `patches/web-component-plugin.patch`，54KB）**，基线为 DSH `master` `b4b67f0`（官方 0804 snapshot）。补丁关键 seam：
- `packages/client/runtime/src/client/slots.ts`：给 `SlotsService` 加 `host(): SlotRendererHost` 方法（让非 installed-renderer 的适配器服务能拿到原本只给 React renderer 的 host 面）。
- `packages/client/ui-slots/src/descriptor.ts`（新增 264+ 行）：typed Web Component descriptor 协议（types only，运行期解释归本包），含 `WebComponentDescriptor`/各 binding 类型与 register 重载推导。
- `docs/config-catalog.md`：把 `@deepseek-ai/dsh-client-web-component` 加入无 config 的 client 插件清单。
- `ui-conversation/tests/views-type-chain.spec.tsx` 等：调整 `@ts-expect-error` 位置以适配新 register 重载。
- 安装流程（顶层 README）：① `cp -a packages/client/web-component packages/client/`；② `git apply patches/web-component-plugin.patch`；③ 在 `apps/cli/package.json` 加 `"@deepseek-ai/dsh-client-web-component": "workspace:^"` 并在 Web composition roster 加 `id: web-component` 行；④ `pnpm install && pnpm --filter @deepseek-ai/dsh-client-web-component bundle`。
- 与 Markdown/WebBlock 渲染层的关系：**没有直接关系**——它是 slot 树 → DOM 的渲染臂，与 React 臂同层；不参与 Markdown/WebBlock 内容渲染。

## 亮点与风险
### 亮点
- **架构定位清晰**：明确声明是 `web-react` 的"原生孪生"而非移植，复用同一 slot/runtime 数据源与组合 API，但不共享任何呈现 API；输入只走 JS 属性、输出只走声明式 CustomEvent，元素永不接触 `ctx`/服务/裸源。
- **类型安全到 register 调用点**：descriptor 协议在 `ui-slots` 做编译期推导（owner/scope/store/inject/locale/matched/children 约束推导出 descriptor 可接受输入），非法样本在 register 处即编译错误；运行期再做 shape 校验（`validateDescriptor`）。
- **失败隔离与不变量双重护栏**：单条目失败只降级为诊断元素；invariant companion 持续校验 tag 注册表一致性。
- **测试覆盖扎实**：`tests/mount.spec.ts` 单文件 36.7KB，外加 loader-composition 用真实 Loader 跑端到端组装断言；fixture roster 覆盖全部 slot kind/scope 与全部 binding kind。

### 风险
- **独立仓库无法直接构建**：`packages/client/web-component/tsdown.config.ts` 第 1 行 `import { clientBundle } from '../tsdown.client.ts'`，而 `packages/client/tsdown.client.ts` 在本仓库**不存在**（只有 `packages/client/web-component/`）。`pnpm bundle` 在脱离 DSH 宿主时会失败——这是设计如此（按 README 流程复制进宿主后才能构建），但作为独立 GitHub 仓库对随机消费者是个坑。文件:`packages/client/web-component/tsdown.config.ts:1`。
- **peerDependencies 全是 DSH 内部 workspace 包**（`@deepseek-ai/dsh-client-runtime/locale/ui-slots/dsh-invariants`），且 `private: true`——纯发布/拆分用途，npm 公网不可装、不可独立运行。
- **缺 LICENSE 文件**：顶层 README 说"沿用 BSD-3-Clause 许可"，但仓库根没有 `LICENSE` 文件（README 自身也提示"发布到组织仓库时请补充仓库级 LICENSE 和版权信息"）。
- **已知架构限制（README 明列）**：① 不支持同 tag constructor HMR（页面级 tag 定义需刷新页面）；② 子 owner/entryKey/only 推导按父化身静态，owner 更新不重新派发，要等父重新化身；③ 无会话时 `session-maybe` 的 provide 绑定直接赋 `undefined`，**不运行 selector**——为已存在快照写的 selector 永不在缺席值上跑（潜在空值 bug 隐患）。
- **`connectedCallback`/`disconnectedCallback` 异常不隔离**：README 明确声明这些浏览器回调体跑在适配器调用边界之外，异常是响亮浏览器错误，**不是** React error boundary 的等价物——消费者若在回调里抛错会冒泡。

## 维护状态
- **default_branch**：`main`（`.git/HEAD` 指向 `refs/heads/main`）。
- **最近 push**：2026-08-04（与任务描述一致；README 标注"官方 0804 snapshot 对应的 DSH master b4b67f0"）。
- **提交活跃度**：极低——depth 1 clone 下只有一条 clone 记录，仓库本身是 2026-08-04 首次剥离发布的快照（顶层 README 自述"目前只完成本地整理，没有配置远程仓库，也没有推送"，但实际已推到 `dsh-external/web-components`）。
- **README 质量**：很高。顶层 README 给出完整安装四步与发布流程；插件 README 双语（EN/中），详尽描述工作原理、原生视图契约、失败隔离、tag 生命周期、fixture composition 与已知限制。

## 备注
- 任务描述里的"0KB / TypeScript"中"0KB"应理解为 GitHub 仓库 size 字段（仅 README 与少量元信息可见时的占位），实际 clone 后代码体量约 130KB+（mount.ts 单文件 28.5KB），是个**有实质实现**的仓库，不是空仓库。
- 顶层 README 第 50-60 行的发布命令残留了绝对路径 `/home/raum/deepseek-harness/web-component-plugin`，说明仓库是从某开发机的 DSH 工作树直接 `git init` 推上来的，未做路径脱敏。
- 仓库**没有** `.gitignore`、没有 CI 配置、没有 `CHANGELOG`——纯一次性剥离发布形态。
