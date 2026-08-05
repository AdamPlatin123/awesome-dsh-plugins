# dsh-skills-manager 调研摘要

## 一句话定位
面向 DeepSeek Harness（DSH）Web GUI 的「技能管理器」插件——在设置面板里集中浏览/搜索/筛选全部技能，一键禁用/启用，添加自定义技能目录，并以类 VS Code 的三栏界面查看与编辑技能文件。

## 技术栈与依赖
- **运行时**：宿主端 `lib/index.js` 为纯 ESM JavaScript、**零运行时依赖**（仅用 Node 内置 `fs/promises`、`os`、`url`、`path`），所有平台能力从 cordis 上下文注入（`ctx.skills`、`ctx.httpServer`、`ctx.workspace`）。
- **客户端**：TypeScript + React（函数组件 + hooks），构建为单文件 CJS bundle `lib/client.js`；样式为普通 CSS（`sb-` 前缀），全部走 DSH 的 `--dsw-*` 设计 token。
- **构建**：`scripts/build.mjs` 用 esbuild（从 DSH 源码 checkout 的 pnpm store 里解析），把 `react`、`@deepseek-ai/dsh-*` 平台模块全部 `external`，产物包成 `window.__ModuleLoader__.load({ id, factory })` 线缆格式。
- **`package.json` 关键字段**：`name: dsh-skills-manager`、`version: 0.2.0`、`private: true`、`type: module`、`main: lib/index.js`；`dshClient.inject` 声明 `@deepseek-ai/dsh-client-runtime` + `@deepseek-ai/dsh-client-ui-settings`、`platform: web`；导出 `.`、`./client`、`./package.json` 子路径。
- 许可证 MIT。

## 文件结构概览
```
dsh-skills-manager/
├── README.md                      安装/使用/数据与存储/构建说明（4.9KB）
├── SPEC.md                        前端实现规格（11.9KB，给代码生成器的硬约束 + i18n 字典 + 布局）
├── LICENSE                        MIT
├── package.json                   插件清单（809B）
├── tsconfig.template.json         含 __DSH_SOURCE__ 占位的 tsconfig 模板，构建时替换
├── ui.png                         界面截图（635KB）
├── .gitignore                     排除 state.json、lib/client.js 等本地状态/产物
├── scripts/
│   └── build.mjs                  esbuild 构建脚本（4.1KB）
├── src/client/                    客户端源码
│   ├── index.ts                   入口：注册 settings.section + locale + 样式（9.4KB）
│   ├── SkillsBrowser.tsx          主 UI：技能列表/目录树/编辑器三栏（49.5KB）
│   ├── settings-enhancer.ts       设置弹窗全屏 + 拖拽缩放增强（7.9KB）
│   ├── contract.ts                客户端/宿主端共享 TypeScript 线缆类型（2.5KB）
│   ├── styles.css                 全部样式，sb- 前缀（22.3KB）
│   └── css.d.ts                   esbuild `.css:text` 的类型声明
└── lib/                           构建产物（已提交）
    ├── index.js                   宿主端入口（30.9KB，828 行）
    └── client.js                  客户端 bundle（88.4KB）
```

## 核心功能与实现要点
1. **HTTP API（宿主端 `lib/index.js`，路由前缀 `/skills-manager/api`）**：`GET /skills`（返回 `skills[]` + 可浏览 `roots[]` + `cwd`）、`POST /skills/disable`、`POST /skills/enable`、`GET /dirs`、`POST /dirs`、`DELETE /dirs`、`GET /browse`、`GET /read`、`PUT /write`。所有读写都经过 `resolveInside()` realpath + `isInsideRoot()` 越界校验，单文件读上限 `MAX_READ_BYTES = 512 KiB`、写上限 `MAX_WRITE_BYTES = 1 MiB`、toggle 请求体上限 4 KiB（`lib/index.js:33-45, 200-260`）。

2. **禁用/启用 = 运行时影子注册**：禁用某技能时，`reconcileOnce()` 调 `ctx.skills.get(name)` 拿到真技能，再用 `ctx.skills.register()` 注册一份 `invocation: { modelInvocable: false, userInvocable: true }` 的影子；运行时 provider rank=250 高于 custom/user/bundled 但低于 project，因此 project 系技能**结构上无法被禁用**（`isProtectedSource` 仅作双保险，`lib/index.js:313-385`）。模型侧目录按 `modelInvocable` 过滤，影子技能随即从 `<available_skills>` 消失，`skill` 工具也会拒绝加载；UI 仍以灰显状态显示供重新启用。

3. **自定义技能目录 = 自带 provider**：插件注册一个名为 `skill-manager` 的 provider（source=`custom`、rank=300，与 `skill-local` 配置型 custom 目录同优先级），扫描 `state.customDirs` 里 `<dir>/<skill>/SKILL.md` 或 `<dir>/<name>.md` 两种 1–2 层布局；自带极简 YAML frontmatter 解析器（`splitFrontmatter` + `frontmatterField`，仅支持单行标量，多行/folded 一律软失败跳过，`lib/index.js:170-230`）。添加目录时做 realpath + 与现有 roots 的 `isInsideRoot` 双向重叠校验，避免重复候选（`lib/index.js:515-555`）。

4. **状态持久化与协调**：`state.json`（位于插件根，可被环境变量 `SKILL_BROWSER_STATE_FILE` 覆盖）原子写入（tmp + rename）保存 `{ disabled: string[], customDirs: string[] }`；监听 `skills/change` 事件驱动 `reconcile()`，用 `reconciling`/`reconcileAgain` 双 latch 串行化避免抖动（`lib/index.js:386-440`）。

5. **客户端入口 `src/client/index.ts`**：通过 `deferRegistration(ctx.slots, 'settings.section', …)` 在 `settings.section` 槽位注册 id=`skills`、order=20 的「技能管理器」面板；自带 `skills-manager` locale 命名空间（zh/en 双语字典各 60+ key，英文版 `satisfies Record<keyof typeof zh, string>` 强制对齐）；样式以 `<style data-skills-manager-css>` 注入一次；并调用 `enhanceSettingsPanels()` 给设置弹窗加全屏/还原按钮与右下角拖拽缩放手柄。

6. **主 UI `src/client/SkillsBrowser.tsx`（49.5KB）**：三栏布局（技能列表 240px / 目录树 280px / 编辑器 flex），搜索 + 来源筛选 + 状态筛选 + 每页 20 条分页；目录树懒加载并用内存 Map 缓存、AbortController 防竞态；编辑器支持行号、Ctrl/Cmd+S 保存、未保存确认弹窗；localStorage 记忆上次选中态（key `skill-browser.state.v1`）。

7. **文本嗅探**：`looksLikeText()` 拒绝含 NUL 或 U+FFFD 的内容，并统计前 4096 字符的控制字符比例；`SKIP_EXTENSIONS` 屏蔽二进制/产物扩展名；`TEXT_EXTENSIONS` 白名单兜底（`lib/index.js:120-160`）。

## 与 DeepSeek Harness 主仓库的集成点
- **插件加载协议**：以「永久 DSH Web 插件」形式接入——克隆到 `~/.dsh/plugins/dsh-skills-manager/`，软链到 `~/node_modules/@dsh-local/skills-manager`，再在 `~/.dsh/config.yaml` 的插件清单里追加 `{ id: skills-manager, name: '@dsh-local/skills-manager' }`；客户端 bundle 用 `window.__ModuleLoader__.load({ id, factory: (require) => … })` 的线缆格式，id 必须与 config.yaml 里的 `name` **完全一致**（`scripts/build.mjs:14, 60-67`）。
- **cordis 服务依赖**：宿主端 `inject = ['skills']`，再在 `apply()` 内用 `ctx.inject(['httpServer', 'workspace'], …)` 惰性注入 Web 专属服务——从而在 TUI 等无 httpServer 的 surface 上也能无害加载；客户端 `inject = ['slots', 'locale']`，依赖 DSH 的 `settings.section` 槽位、`locale` 翻译服务与 `deferRegistration`。
- **复用主仓库的技能注册表语义**：直接消费 `ctx.skills.list/get/register/registerProvider`、`skills/change` 事件，以及 `invocation.modelInvocable` / source rank 这些主仓库注册表契约——禁用机制完全依赖 rank 优先级，**没有另起一套**。
- **平台模块外置**：`dshClient.inject` 声明 `@deepseek-ai/dsh-client-runtime`、`@deepseek-ai/dsh-client-ui-settings`；构建时 `react`、`react-dom`、`cordis`、`@deepseek-ai/dsh-client-ui-{slots,primitives,web-react}`、`@deepseek-ai/dsh-client-schema-form`、`@deepseek-ai/dsh-client-runtime/client` 全部 external，由 loader 注入的 `require` 解析（`scripts/build.mjs:16-29`）。
- **类型对齐**：`src/client/contract.ts` 把 `SkillResourceBase`、`SkillSummary`、`BrowseResponse`、`ReadResponse`、`WriteResponse` 等线缆形状镜像宿主端；并 `import type { Translate } from '@deepseek-ai/dsh-client-ui-slots'` 复用主仓库的 i18n 函数类型。
- **构建期耦合**：`scripts/build.mjs` 与 `tsconfig.template.json` 都依赖 DSH 源码 checkout 路径（默认 `~/.dsh/source/current`，可用 `DSH_SOURCE` 覆盖）——esbuild 从该 checkout 的 pnpm store 解析，tsc 也用该 checkout 的类型产物做 `--noEmit` 检查。

## 亮点与风险
- **亮点 1：禁用机制是结构性的而非 UI 层屏蔽**。用 rank=250 的运行时影子 + `modelInvocable:false`，从模型目录与 `skill` 工具两侧同时摘除，project 系技能因 rank 更高而天然受保护——这是依赖主仓库注册表优先级的优雅设计（`lib/index.js:325-340`）。
- **亮点 2：零运行时依赖 + 双面结构**。宿主端纯 Node 内置模块，客户端单 bundle，安装只需复制目录 + 软链 + 改 config.yaml 三步，热加载友好。
- **亮点 3：i18n 字典以 `satisfies Record<SkillBrowserKey, string>` 强制 zh/en 对齐**，缺 key 编译期即报错（`src/client/index.ts` 字典定义处）。
- **风险 1：rank 语义属隐式契约**。禁用正确性强依赖「runtime provider rank=250 高于 custom/user/bundled 但低于 project」这一未在公开类型里固化的优先级；若主仓库调整 rank 表，project 技能可能被误禁用或自定义技能无法被屏蔽。
- **风险 2：自带 YAML frontmatter 解析器是严格子集**。`splitFrontmatter`/`frontmatterField` 仅认单行标量与 `---` 围栏，多行/folded/block scalar 一律软失败跳过（`lib/index.js:170-200`）；用户若用 `description: |` 多行写法，技能会被静默丢弃。
- **风险 3：自定义目录重叠检测存在 TOCTOU**。`addCustomDir` 在 check roots 与 `commitDirChange` 之间未持锁，若并发添加或 roots 在窗口期内变化，理论上可注册重叠目录产生重复候选（`lib/index.js:515-555`）。
- **风险 4：插件 id 字符串强约束**。`PLUGIN_ID = '@dsh-local/skills-manager'` 必须与 `~/.dsh/config.yaml` 的 `name` 字段、软链路径三者完全一致，否则 loader 报错且无 fallback（`scripts/build.mjs:14`、README 安装步骤 1–3）。
- **风险 5：客户端 bundle 与产物已提交进 lib/**。`lib/client.js`（88KB）与 `lib/index.js` 都在仓库里，二次开发若忘记 `node scripts/build.mjs` 就提交，会出现源码与产物不一致。

## 维护状态
- 活跃维护中。仓库 metadata（由协调端 gh api 复核）：`size ≈ 636KB`、默认分支 `main`、最近一次 push `2026-08-05T05:12`（即本调研当日）；`package.json` 版本 `0.2.0`。
- 仓库对外为**私有**（公开匿名访问 404，需 AdamPlatin123 的 gh 认证才可见），与 dsh-external org 其他仓库一致。
- 文档完整度高：README 含安装/数据存储/构建/已知限制/截图，SPEC.md 是可直接喂给代码生成器的前端实现规格。

## 备注
- 本调研无本机 bash/gh 工具，匿名 GitHub API + DeepWiki 均返回 404（仓库私有），最终由 Main 协助认证 clone 到 `/tmp/dsh-ext-research2/dsh-skills-manager/`，再读取本地源码撰写本摘要。
- 与第一轮已调研的同类 DSH 插件相比，本仓库的特点是「**改写模型可见技能目录**」——大多数 DSH 插件只是新增能力，而它通过影子注册直接塑造模型端的 `<available_skills>`，对 prompt 上下文预算有实际影响。
- 「技能管理器」与主仓库自带的 `skill-local` provider 在「自定义目录」能力上重叠（同 source=`custom`、同 rank=300），区别在于本插件是 Web UI 驱动 + state.json 持久化，而 skill-local 是 `~/.dsh/config.yaml` 驱动；二者可共存，但同名技能会按注册表优先级二选一（README「已知限制」已提示）。
