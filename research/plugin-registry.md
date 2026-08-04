# plugin-registry 调研摘要

## 一句话定位

DeepSeek Harness 的**第三方本地插件系统**：在 DSH 主仓库 cordis.yml 官方插件树之上再加一层——以 `dsh.plugin.json` 清单协议驱动的安装 / 启停 / 校验 / 脚手架 / tarball 分发，配一个可热挂载的 Web 管理面板，把"放文件即用"升级为"带生命周期、可校验、可管理的分发生态"。

## 技术栈与依赖

- **语言**：TypeScript（ESM，`"type": "module"`），Node ≥ 带 `node:fs/promises`、`node:url`、`node:os` 的版本。
- **运行时**：[Cordis 4.0.0-rc.7](https://www.npmjs.com/package/cordis)（DSH 全家桶底座：Plugin / Service / Fiber / Context）。
- **核心包** `@deepseek-ai/dsh-plugin`（私有，BSD-3-Clause，`packages/plugin/plugin/`）依赖：
  - `schemastery ^3.18.0` —— 清单 schema 校验
  - `semver ^7.8.4` —— `engines.dsh` 兼容范围
  - `tar ^7.5.22` —— tarball 解压（`strict: true` 防穿越）
- **peer 依赖**（来自 DSH 主仓库）：`@deepseek-ai/dsh-invariants`、`dsh-paths`、`dsh-tools`、`cordis`。
- **Web 面板包** `@deepseek-ai/dsh-client-ui-plugin-manager`（`packages/ui-plugin-manager/`）：
  - React 18 + `dsh-client-ui-primitives`（Button/Input）、`dsh-client-ui-slots`（`PropsRuntime<'settings.section'>`）、`dsh-client-web-react`、`dsh-host-apiproxy`（`PluginEntryView` 类型）。
  - `dshClient` 声明（`inject: ['@deepseek-ai/dsh-client-connection', '@deepseek-ai/dsh-client-runtime']`, `platform: 'web'`）—— DSH 标准 client 双面插件（node 半空 `apply` 占位、browser 半通过 `exports['./client']` 暴露 React 面板）。
- **构建**：`tsdown`（仅 UI 包），核心包无 build script（靠 monorepo 编排）。

## 文件结构概览

```
plugin-registry/
├── README.md                        # 顶层总览（含与 pi-mono / cordis.yml 两层插件对比）
├── packages/
│   ├── plugin/plugin/               # @deepseek-ai/dsh-plugin 核心包
│   │   ├── src/
│   │   │   ├── types.ts             # 协议类型：PluginManifest / PluginEngines / PluginContributes / InstalledRecord / PluginIndex / CatalogEntry
│   │   │   ├── manifest.ts          # Schemastery schema + parseManifest + readManifest + checkEngine
│   │   │   ├── registry.ts          # 文件系统注册表：install/setEnabled/uninstall/listPlugins + 原子写 + per-home 串行锁 + 回滚
│   │   │   ├── service.ts           # PluginLocalService（ctx.plugins）：mount/unmount/reconcile + contributes 校验
│   │   │   ├── load.ts              # normalizePlugin：default ?? module + 形状校验
│   │   │   ├── scaffold.ts          # dsh plugin create：生成 dsh.plugin.json + index.mjs + README
│   │   │   ├── tarball.ts           # .tgz/.tar.gz 安装：strict 解压 + locatePluginRoot
│   │   │   ├── catalog.ts           # plugins-catalog.json：Obsidian 风格本地市场数据源
│   │   │   ├── invariant.ts         # @deepseek-ai/dsh-invariants 包级 invariant 注册（空实现，仅占包名）
│   │   │   └── index.ts             # apply：构造 service + reconcile（载入已启用集）
│   │   └── tests/                   # 8 个 spec：manifest/registry/registry-consistency/service/tarball/scaffold/catalog/load
│   └── ui-plugin-manager/           # @deepseek-ai/dsh-client-ui-plugin-manager
│       ├── src/
│       │   ├── index.ts             # node 半：apply 空函数（仅占 Loader 名额）
│       │   ├── client/index.ts      # browser 半入口
│       │   ├── client/PluginPanel.tsx     # 浏览/搜索/安装/启停/卸载面板
│       │   ├── client/PluginPanel.module.css
│       │   └── invariant.ts         # 包级 invariant 注册
│       └── tests/plugin-panel.spec.tsx
├── examples/
│   ├── README.md                    # 从零开发指南
│   └── greeter/                     # 可直接安装示例：dsh.plugin.json + index.mjs（注册 greet 工具）
├── skills/plugin-registry-create/SKILL.md  # Agent Skill：选 id → 脚手架 → 写入口 → 同步 contributes → 安装验证
├── patches/dsh-plugin-registry.patch      # 1061 行、~30 文件的 DSH 主仓库接线补丁
└── screenshots/                     # 插件面板运行截图 ×2
```

## 核心功能与实现要点

### 1. 清单协议 `dsh.plugin.json`（声明即契约）
- 文件：`packages/plugin/plugin/src/types.ts`、`manifest.ts`。
- 字段：`id`（正则 `^[a-z0-9][a-z0-9-]*\/[a-z0-9][a-z0-9-]*$`，即 `publisher/name`）、`version`（semver）、`main`（相对入口路径）、`description`、`engines.dsh`（semver range，默认 `>=0.0.1`）、`contributes.{tools,skills}`（声明数组，默认空）。
- 用 `schemastery` 做 schema 校验；`parseManifest(text, source)` JSON 解析失败显式抛出含位置的错误；`checkEngine` 用 `semver.satisfies(runningVersion, engines.dsh)` 否则抛 `plugin requires dsh X, running Y`。

### 2. 安装/启停流程（文件系统事实 + 串行锁 + 回滚）
- 文件：`packages/plugin/plugin/src/registry.ts`、`service.ts`。
- 路径：`<dshHome>/plugins/<id>/`（每插件一目录）+ `<dshHome>/plugins/index.json`（`{ id: { version, enabled, installedAt } }`）。
- **install**（`installPluginLocked`）：读清单 → `checkEngine` → 查重（已装抛错）→ 清崩溃残留目录 → 校验 `main` 存在 → `cp -r` → **以 index 原子写为提交点**：tmp 文件 + rename；写失败则 `rm -rf` 回滚复制的目录。`enabled` 恒为 `false`（信任边界：默认禁用）。
- **enable/disable**（service 层 `enable/disable`）：先 `mount/unmount`（Cordis fiber），**mount 成功后才** `setEnabled` 持久化——坏插件永不会被标记 enabled。
- **reconcile**：服务启动时遍历 index，所有 `enabled: true` 的逐个 mount（载入时扫描）。
- 并发安全：`withRegistryLock` 用 per-`dshHome` 的 Promise 链串行化所有读改写，错误吞掉以免阻塞后续任务（`registry.ts:236-256`）。
- 原子性：`writeIndex` 用同目录 tmp + rename，读者永不见截断的 index（`registry.ts:91-100`）。

### 3. 运行时挂载与 contributes 声明校验
- 文件：`packages/plugin/plugin/src/service.ts`、`load.ts`。
- 所有挂载的插件是同一 group fiber 的子 fiber，service dispose 时一锅端。
- `mount(id)`：`pathToFileURL(import).href` 动态 import 入口 → `normalizePlugin`（`module.default ?? module`，校验是 function/class/带 apply 的对象）→ `ctx.plugin(plugin)` → `fiber.await()` → **`verifyContributions`**：从根 context 拿 `tools` 服务（不抛错，没装就跳过），用 `tools.schemas()` 收集已注册工具名集合，清单里 `contributes.tools` 中**没注册的**算违规，列出缺失名并 `fiber.dispose()` 回滚挂载（`service.ts:88-129`）。
- 注意 `contributes.skills` 目前**不校验**（README 已声明限制），只 `tools` 在挂载时强制对账——这是"声明即契约"的当前实际范围。

### 4. Web 管理面板（dshClient 双面插件）
- 文件：`packages/ui-plugin-manager/src/{index.ts,client/PluginPanel.tsx,client/PluginPanel.module.css}`。
- node 半 `apply()` 空（占 Loader 名额）；browser 半由 `package.json#dshClient` 声明 + `exports['./client']` 暴露。
- `PluginPanel`：`useState` 维护列表 + 搜索词 + busy；`api.plugins.list/install/enable/disable/uninstall` 走 RPC；按 `installed/enabled` 派生按钮（未安装→安装、已启用→禁用+卸载、已禁用→启用+卸载）；搜索按 `id` 与 `description` 大小写不敏感过滤；操作后 `refresh()` 重拉。状态徽章三色（已启用绿/已禁用/未安装）。
- 主机端 RPC 由补丁注入 `dsh-host-apiproxy`：新增 `plugin.{list,install,enable,disable,uninstall}` 五个 method、`PluginsApi` 接口、`PluginEntryView` 类型、`pluginEntryViewSchema` 等 zod schema；`createApiProxy` 用 `ctx.get('plugins')` 取服务，没装返回友好错误 `"plugin registry is absent: this deployment does not mount @deepseek-ai/dsh-plugin ..."`（`patches/...:441-454`）。

### 5. 脚手架 `dsh plugin create <id>`
- 文件：`packages/plugin/plugin/src/scaffold.ts`。
- `id` 必须含 `/`（schema 强制）；在 `cwd/<name>/` 生成三件套：`dsh.plugin.json`（默认 `version=0.1.0`、`main=./index.mjs`、`engines.dsh=">=0.0.1"`、`contributes={tools:[],skills:[]}`）+ `index.mjs`（带 `inject:[]`、`apply(ctx){}` 的 Cordis 模板，注释示范 `ctx.tools.register`）+ `README.md`。
- 写文件前先 `parseManifest(JSON.stringify(...))` 自校验，保证脚手架出来的根目录直接可装。

### 6. tarball 分发 `.tgz` / `.tar.gz`
- 文件：`packages/plugin/plugin/src/tarball.ts`。
- `isTarball` 看后缀；`installFromTarball`：`stat` 文件 → `mkdtemp` 临时目录 → `tar.x({ file, cwd: staging, strict: true })`（**strict 模式拒绝路径穿越**）→ `locatePluginRoot`：先看 staging 根有无 `dsh.plugin.json`，否则遍历顶层目录（跳过 `node_modules`）找唯一含清单的子目录，找不到抛错 → 复用 `installPlugin` 走与目录安装同样的清单/引擎校验。`finally` 永远 `rm -rf staging`。

### 7. 本地 catalog（市场数据源）
- 文件：`packages/plugin/plugin/src/catalog.ts`、`service.ts:list()`。
- `<dshHome>/plugins-catalog.json`，schema `{id, version, description, source}[]`（Obsidian 社区插件 shape）。`list()` 把 catalog 与已装 index 按 id 合并：catalog 有的显示为"未安装/已安装+启停"，index 有但 catalog 没有的也补出来。后缀形如远程 registry 预留——以后换远程源不动 API/UI。

### 8. CLI 子命令（接线在 DSH 主仓库）
- 文件：`patches/dsh-plugin-registry.patch` 内 `apps/cli/src/{args.ts,bin.ts,plugin.ts}`。
- `dsh plugin install <dir|tgz>` / `create <id>` / `list` / `enable <id>` / `disable <id>` / `uninstall <id>`，全部走本包 API；`runPlugin` 把领域错误打到 stderr 并设 `process.exitCode=1`，不抛栈。

## 与 DeepSeek Harness 主仓库的集成点

**集成方式**：复制两个包到 DSH monorepo 对应路径（`packages/plugin/`、`packages/client/ui-plugin-manager/`），然后 `git apply patches/dsh-plugin-registry.patch`（基于官方 0804 快照 `20260804T143803Z`，改 30 个文件）。

**集成 seam（关键挂载点）**：

1. **Cordis 插件挂载**（`apps/cli/config/base.cordis.yml`）：在官方树静态组合里追加
   ```yaml
   - id: plugin-local
     name: '@deepseek-ai/dsh-plugin'
   ```
   提供 `ctx.plugins` 服务。Web 组合 `web.cordis.yml` 再挂 `ui-plugin-manager`。

2. **CLI 路由**（`apps/cli/src/{args.ts,bin.ts,plugin.ts}`）：新增 `PluginInvocation` 类型、`dsh plugin` commander 子树、`runPlugin` 实现。

3. **apiproxy RPC 域**（`packages/host/apiproxy/src/{api/{plugins.ts,plugins.schema.ts,index.ts,rpc-map.ts},fetch/{client.ts,handler.ts},index.ts}`）：新增 `plugins` 域五个 method、`PluginsApi`/`PluginEntryView` 类型、zod schema、handler 路由表项；`createApiProxy` 通过 `ctx.get('plugins')` 取服务，缺失返回友好 `RpcError`。

4. **TS project refs**：`apps/cli/tsconfig.json`、`packages/host/apiproxy/tsconfig.json` 各加一项指向 `../../packages/plugin/plugin`。

**与主仓库 plugin 机制的关系（关键边界）**：

- **不是替代 cordis.yml**，而是其上的**第二层**。官方树（agent-loop / llm / tools / fs / skill-local / ui-* 等）由 Loader 按 `cordis.yml` 静态加载；registry 插件由 `plugin-local` 扫描 `<dshHome>/plugins` 在运行时通过 `ctx.plugin()` 动态挂载——**不进 Loader 配置树**，因此不出现在 `dump-config` / cordis.yml 组合输出里。
- 旧 session 提到主仓库"只有受限的 `.dsh-plugin/package.json` 格式"——本仓库用独立的 `dsh.plugin.json`（与 `package.json` 解耦），不受旧格式约束，是**独立演进**的协议；插件包名仍走 `@deepseek-ai/dsh-plugin` 命名空间。
- 同进程同 context：第三方插件可 `inject` 官方树服务（`tools`/`skills`/`commands`/`tasks`/`workflows`...），但**不能** `provide` 与内置服务同名的服务（注册冲突）。
- 浏览器 bundle 不进 `__DSH_BOOT__`：client 类型插件应走独立 `dsh-client-*` 包通道（README 与 SKILL 均明确）。
- `dsh-invariants` 包级注册：`invariant.ts` 仅 `ctx.invariants.register(PACKAGE_NAME, () => {})` 占位，无运行时检查（README 注释说明：注册表是文件系统事实、挂载是 caller fiber 的副作用，二者都没有"权威事件流"可供运行时断言）。

## 亮点与风险

### 亮点

1. **声明即契约 + 回滚保证**：清单声明的工具未注册则挂载失败、fiber 回滚、`enabled` 不持久化，作者不会留下"半挂载"状态（`service.ts:88-129`）。
2. **原子性 + 串行化的注册表**：index 用 tmp+rename 原子写，所有 mutation 用 per-home Promise 链串行化，install 失败回滚目录、uninstall 目录删除幂等可重试——一致性契约写得相当扎实（`registry.ts:34-58,236-256`）。
3. **tarball strict 模式防穿越**：`tar.x({ strict: true })` 拒绝路径穿越条目，定位根目录时显式跳过 `node_modules`（`tarball.ts:43,55`）。
4. **信任边界 = 默认禁用 + 显式启用**：install 永远 `enabled:false`，只有 enable 才挂载执行；Web 面板状态徽章直观，面板动作与 CLI 等价。
5. **文档极完整**：README 含与 pi-mono / cordis.yml 双层对比、能力面 vs 声明面辨析、所有"已知限制"自报家门；自带 Agent Skill 与示例插件，端到端 onboarding 路径清晰。

### 风险

1. **第三方插件 = 进程内任意代码执行，无沙箱**：插件 `apply(ctx)` 拿到完整 Cordis context，可注册工具/事件/服务/命令/系统提示/TUI 覆盖层；README 直言"sandbox 限制的是工具调用不是插件；无签名、无发布者身份、无审核"（`packages/plugin/plugin/README.md` "Known Limitations"）。enable 即同进程代码执行。
2. **动态 `import(entryUrl)` 无签名校验**（`service.ts:75`）：任意本地目录被 install 后，enable 即 `import` 其 `main`——若 `<dshHome>/plugins` 被篡改（如多用户共享 home、或恶意 catalog `source` 路径指向任意目录），无机制阻止恶意代码加载。
3. **catalog `source` 是任意本地路径**（`catalog.ts:54-58`、`types.ts:53`）：`installFromCatalog` 直接 `installPlugin(entry.source, ...)`——catalog 文件若被攻击者写入，可指向系统任意目录（虽仍需通过清单校验，但无路径白名单）。
4. **`installPlugin` 全目录复制含 `node_modules` 与构建产物**（`registry.ts:108`，README 已自承）：无依赖解析、无剪枝，可能复制大体积或敏感文件进入 `<dshHome>/plugins`；空间/隐私双重隐患。
5. **`contributes.skills` 不校验**（`service.ts:130-139` 仅校验 `tools`，README 自承）：声明面与能力面有缺口，作者可能误以为 skills 也"声明即契约"。
6. **per-home 锁是进程内 Promise 链，非跨进程**（`registry.ts:240` `registryQueues: Map<string, Promise>`）：多个 dsh 进程共享同一 `$DSH_HOME` 时（如 Web + CLI 并发），仍可能 index 互覆盖——注释也未声称跨进程安全。
7. **`PluginLocalService.dispose()` 在 `Service` 父类约定上应是同步/无返回值，此处返回 `Promise<void>`**（`service.ts:217-221`）：与 Cordis `Service.dispose(): void` 约定可能不一致，需结合 cordis 版本验证（[INFERENCE]——未读 cordis 源码确认）。
8. **补丁锚点漂移风险**：`patches/dsh-plugin-registry.patch` 1061 行基于 0804 快照锚定 30 个文件，DSH 主仓库基线更新后可能需要 `--3way` 或手工对齐（README 已声明，但交付物绑死单一快照是运维负担）。

## 维护状态

- **default_branch**：`main`（HEAD `472e2296f33504511b32d47cb1f4817b4e9bca32`）。
- **最近 push**：2026-08-04（与 DSH 0804 官方快照对齐，clone 时间戳 `1785869330` 即 2026-08-04 +0800）。
- **提交活跃度**：本次为 `--depth 1` 浅克隆，仅 1 个 commit 可见；无历史趋势数据。作者署名 `Adam（本地邮箱已脱敏）`，本地未配置 GitHub 邮箱——是个人/小团队内测仓库（README 版权段也声明"供 dsh-external 组织内测成员使用，未经许可请勿公开分发"）。
- **README 质量**：极高。顶层 README（9.1KB）覆盖定位、目录、能力对比（pi-mono 横向对比 + 与 cordis.yml 两层插件纵向对比 + 能力面 vs 声明面辨析）、集成步骤、CLI 用法、快速开发、Agent Skill 介绍。子包 README（5.7KB 英文 + 5.3KB 中文 + i18n yaml）含 Known Limitations 自报短板。examples/README.md 是人类向从零教程。SKILL.md 给 agent 用结构化 workflow + gotchas。
- **测试覆盖**：8 个 spec 覆盖 manifest / registry / registry-consistency / service / tarball / scaffold / catalog / load；补丁里还附 apiproxy 端 150 行 api-proxy-plugins.spec.ts + UI 端 plugin-panel.spec.tsx + args.spec.ts 路由测试。质量与文档看齐。
- **版本**：两个包均 `0.0.1` `private: true`——处于内测/前置发布阶段，未上 npm。

## 备注

- **与官方 cordis 工具集命名区分**：SKILL.md frontmatter 显式声明"community plugin-registry skill — not the official harness cordis toolset"，避免 agent 把本仓库的 `plugin-registry-create` skill 与官方 `dsh-*` skills / `cordis` 工具集混淆。
- **本地 catalog 远程化预留**：catalog 文件 shape 刻意模仿 Obsidian 社区插件市场（id/version/description/source），README 与 catalog.ts 注释都指出"以后换远程 registry 不动 API 与 UI"——目前 `source` 是本地目录，未来是远程 URL 的扩展点。
- **pi-mono 横向对比要点**：能力面（events/hooks/tools/commands/systemPrompt）覆盖 pi-mono，并补上 pi 没有的安装/启停/校验/分发；但 TUI 表面 dsh 是**受限覆盖层**（`ctx.tui.openOverlay()` 只给 viewport/主题/重绘/关闭，不给底层组件树），pi 则开放 pi-tui 组件树——这是 dsh 的安全取舍。
- **未实现的"分发"半边**：tarball 安装是单文件分发单元，但**无在线市场、无更新命令、无 Web 客户端 bundle 分发路径**（README Known Limitations 显式列出三项）——所谓"tarball 分发"目前是手动拷贝 + CLI 安装，不是端到端市场。
- **依赖 DSH 主仓库 monorepo 布局**：`peerDependencies` 全是 `@deepseek-ai/dsh-*` workspace 包，独立 clone 出来无法直接 build/run——必须套用补丁、放进 DSH monorepo 才能工作；这是设计使然（私有生态插件），也意味着评估本仓库必须连带评估主仓库快照。
