# dsh-external 生态超级调研：聚合报告

> ⚠️ **快照声明**：本报告为 2026-08-05 首轮 15 仓基线聚合，当前 org 已 134 仓；最新全景见 reports/latest/mainline-compat.md（每日更新）。

> 本报告由 15 个并行调研摘要（`/mnt/shared/_Projects/dsh-plugin-radar/research/*.md`）与旧 session 上下文归档（`/mnt/shared/_Projects/dsh-plugin-radar/context/session-019fc8ab-summary.md`）聚合而成。
> 所有论断均可在对应摘要文件中追溯（标注 `research/<仓库>.md`）；每个仓库至少出现一次。
> 调研基准日：2026-08-05。

---

## 0. 调研范围与方法

- **调研对象**：`dsh-external` 组织下 15 个仓库（私有，内测白名单可见）。每个仓库由独立 scout 子代理只读调研，手段包括 `git clone --depth 1`、`gh api` 元数据/contents/branches/readme 查询、源码/测试/README 静态分析；每份摘要遵循统一契约（一句话定位 / 技术栈 / 文件结构 / 核心功能附关键文件与行号 / 集成点 / 亮点与风险 / 维护状态 / 备注），见 `research/*.md`。
- **背景上下文**：旧 session（019fc8ab）在 deepseek-harness 快照仓库（分支 `snapshots/20260804T143803Z-6feab99fdf`）上的磁盘 I/O 静态调研、远端部署测试、版本差异分析（770 files changed / 12,564 insertions / 30,749 deletions）与群聊对齐结论，归档于 `context/session-019fc8ab-summary.md`。
- **时效声明**：基准日 2026-08-05。多数仓库以 depth=1 浅克隆调研，只能看到最近一次提交，"提交活跃度"结论以摘要文件可见证据为准；推断性内容（如 sandbox-mxc 的 MXC 语义、dsh-coding-receipt 的预期功能）在原文已以 `[INFERENCE]` 标注，本报告按推断处理并保留不确定性。
- **证据规范**：本报告每一论断均标注来源（`research/<仓库>.md` / `context/session-019fc8ab-summary.md`），可直接抽查；凡摘要之间出现的不一致（如 toybox 色数 60 vs 61、group-chat-diary 的 README 与数据指向不同 issue 仓库），本报告如实并列并给出处理建议。

---

## 1. 生态全景：15 仓库分类

`dsh-external` 组织（DSH 内测期私有组织）下被调研的 15 个仓库按"是否承载代码资产 + 承担的产品角色"分为五类：

### 1.1 插件生态（2 个）——插件的"格式规范"与"集合"

- **plugin-registry**（`research/plugin-registry.md`）：DSH 第三方本地插件系统，以 `dsh.plugin.json` 清单协议驱动安装/启停/校验/脚手架/tarball 分发，配 Web 管理面板——是插件生态的"协议层 + 治理层"，被定位为 cordis.yml 官方树之上的第二层。
- **toybox**（`research/toybox.md`）：整活插件玩具箱，8 个已落地插件（3 个 skill + 5 个 MCP），走官方 `.dsh-plugin/package.json` 静态格式，与"正经通用插件"仓库 dsh-hub 互补。

### 1.2 IM 远程通道（2 个）——把 IM 变成 agent 对话界面

- **tg-bot**（`research/tg-bot.md`）：Telegram 远程通道插件（源码形态分发 + host patch），长轮询 + 复用宿主 ApiProxy RPC 面，含 ask-user-question 内联键盘交互。
- **qqbot**（`research/qqbot.md`）：QQ Bot API v2 远程通道插件（零运行时依赖、宿主端插件），WS 网关 + 扫码绑定，国内用户向。

### 1.3 Web UI 扩展（5 个）——在 DSH Web 官方扩展点上叠加能力

- **web-components**（`research/web-components.md`）：与 React 渲染器平行的原生 Custom Elements 渲染臂（`webComponent` 服务 + slot descriptor 协议）。
- **skins**（`research/dsh-skins.md`）：换肤插件，4 个皮肤全部走官方 `ThemeService.register` + `--dsw-alias-*` token 覆盖，零核心改动。
- **subagent-tree**（`research/dsh-subagent-tree.md`）：工作区侧栏子代理树插件（对应 issues#44 诉求），注册会话行两个扩展 hole。
- **live-stats**（`research/dsh-live-stats.md`）：实时 token/TPS 统计行，服务端 projection + 客户端 `conversation.composer.dock` 插槽。
- **working-activity**（`research/dsh-working-activity.md`）：模型工作状态行插件，TUI prompt 槽位 + Web 状态标签双出口。

### 1.4 工具链（2 个）——生态支撑类资产

- **issues**（`research/issues.md`）：纯 Issue Tracker 承载仓库，308 个 issue，DSH 内测期的反馈漏斗与缺陷台账（无代码）。
- **group-chat-diary**（`research/group-chat-diary.md`）：DSH 内测微信群每日归档，零依赖单文件 HTML（群聊精选/成员画像/Issue 汇总），内测时间轴索引层。

### 1.5 占位未启动（4 个）——仅有名称/描述，无任何代码

- **sandbox-mxc**（`research/sandbox-mxc.md`）：描述"微软跨平台沙盒支持"，0 commit。
- **dsh-opencode-server**（`research/dsh-opencode-server.md`）：描述"把dsh的tui换成opencode！"，0 commit，与 TUI 移除强相关。
- **ex-setting**（`research/ex-setting.md`）：描述"DSH 的设置扩展"，0 commit，org 内唯一完全空置仓库。
- **dsh-coding-receipt**（`research/dsh-coding-receipt.md`）：描述"将 DeepSeek Harness 会话日志转换为本地可分享的 coding receipt"，0 commit。

> 结论：**11 个仓库有实质内容（含纯流程型 issues 与纯产物型 group-chat-diary），4 个为空占位**。占位仓库不应计入"已落地能力"。

### 1.6 逐仓库速览表（关键事实速查）

| 仓库 | 定位 | 技术栈 | 集成方式 | 测试 | 最近 push |
|---|---|---|---|---|---|
| issues | 内测反馈漏斗，308 issue | 无代码（README 547B） | 流程层（标题前缀对应主仓库子系统） | 无 | 2026-08-01（代码）/08-04（issue） |
| toybox | 整活插件玩具箱（8 插件） | TS(.mts) + 零依赖单文件 ESM MCP | 官方 `.dsh-plugin` 静态格式 + `repository-plugins` 挂载 | vitest + MCP 协议冒烟 + CI | 2026-08-05 |
| plugin-registry | 第三方插件系统（dsh.plugin.json 协议） | TS + cordis + schemastery + semver + tar | 复制进 monorepo + 1061 行补丁（0804） | 8 spec + apiproxy 150 行 | 2026-08-04 |
| tg-bot | Telegram 远程通道 | TS(ESM) + fetch 长轮询 | 源码 cp + host patch（锚定 fa3d357）+ cordis overlay | 6 vitest spec | 2026-08-05 |
| qqbot | QQ Bot API v2 远程通道 | 纯 JS ESM 零运行时依赖 | 宿主插件：`~/.dsh/plugins` + 软链 + config.yaml insert | node:test 2 spec | 2026-08-05 |
| web-components | 原生 Custom Elements 渲染臂 | TS + cordis + Shadow DOM | 复制进 monorepo + 54KB 补丁（锚定 b4b67f0） | vitest（mount.spec 36.7KB + loader-composition） | 2026-08-04 |
| dsh-skins | Web GUI 换肤（4 皮肤） | TS + React + CSS Modules | 客户端插件契约（dshClient）+ 零补丁 | vitest 5 spec + vm 冒烟 + i18n 门禁 | 2026-08-05 |
| dsh-subagent-tree | 侧栏子代理树 | TS + React 18 | 客户端插件契约（双 slot 注册） | vitest 22 项 | 2026-08-04 |
| dsh-live-stats | 实时 token/TPS 统计 | TS + cordis + React 18 | projection seam + composer.dock 插槽 | vitest 2 spec | 2026-08-04 |
| dsh-working-activity | 模型工作状态行 | TS + cordis | 复制进 monorepo + 27.8KB 补丁（0804） | vitest 4 spec（34 项） | 2026-08-04/05 |
| group-chat-diary | 内测群每日归档 | 零依赖单文件 HTML | 归档/旁观层（无代码 seam） | 无（产物型） | 2026-08-05 |
| sandbox-mxc | 占位：微软跨平台沙盒 | 无 | 无 | 无 | 2026-08-04（创建 2 秒后） |
| dsh-opencode-server | 占位：opencode 换 TUI | 无 | 无 | 无 | 2026-08-04（创建 1 秒后） |
| ex-setting | 占位：DSH 设置扩展 | 无 | 无 | 无 | 无（git ls-remote 空） |
| dsh-coding-receipt | 占位：session log → receipt | 无 | 无 | 无 | 2026-08-04（创建 1 秒后） |

---

## 2. 主题聚类分析

### 2.1 插件格式演进：`.dsh-plugin/package.json` → `dsh.plugin.json` 两代格式

**第一代：官方静态交付格式 `.dsh-plugin/package.json`**

- 旧 session 调研确认：主仓库（20260804 快照）只支持受限的 `.dsh-plugin/package.json` 格式——静态 skills + MCP 配置，**不支持任意 JS 工具/命令/hooks**（`context/session-019fc8ab-summary.md`）。
- **toybox** 是这一代的完整实践：每个插件目录下 `.dsh-plugin/` 含 `package.json`（`dsh.skills` / `dsh.mcpServers` 字段）、`prepare.js`（官方 0804 prepare 的 133KB 拷贝，全插件共用同一份）、`.mcp.json`（stdio 单文件 ESM server）。加载走 DSH 的 `@deepseek-ai/dsh-repository-plugin`，用户 `~/.dsh/config.yaml` 里 `repository-plugins` 挂 `github:dsh-external/toybox#<40位commit>&path:/plugins/<id>/.dsh-plugin`——**不可变身份 = 完整 40 位 commit ref**（`research/toybox.md`）。
- 该格式的能力边界被多仓库反复确认：`CONTRIBUTING.md` 明说 JS 工具/命令/hooks 要走开发层；tg-bot 的 README 也解释"当前 external repo 格式只支持静态 skill 和 MCP 配置，不支持任意 Cordis 服务端/Web UI 代码，因此以源码分发"（`research/tg-bot.md`）。

**第二代：`dsh.plugin.json` 清单协议（plugin-registry 独立演进）**

- **plugin-registry** 用独立的 `dsh.plugin.json`（与 `package.json` 解耦、不受旧格式约束）：字段 `id`（强制 `publisher/name` 正则）、`version`、`main`、`engines.dsh`（semver 范围）、`contributes.{tools,skills}`——声明即契约，`contributes.tools` 未注册则挂载失败并回滚 fiber（`research/plugin-registry.md`）。
- 带完整生命周期：`dsh plugin install/create/list/enable/disable/uninstall` CLI + Web 面板 + tarball（`strict: true` 防路径穿越）+ 本地 catalog（模仿 Obsidian 社区插件 shape，`source` 目前是本地路径、预留远程化）。
- 它**不是替代 cordis.yml**，而是其上的第二层：官方树由 Loader 静态加载，registry 插件由 `plugin-local` 在运行时 `ctx.plugin()` 动态挂载，不进 `dump-config` 输出。

**主仓库现状与演进判断**

- 主仓库 20260804 快照中仍只有第一代格式；旧 session 明确"群聊宣称的 `dsh.plugin.json` 插件系统不在快照中"（`context/session-019fc8ab-summary.md`）——plugin-registry 的 `dsh.plugin.json` 是**社区先行实现**，两代格式并存是当前生态的关键事实。
- 社区对"插件分发/贡献协议"的关注度最高：issues#171「插件系统暴露标准入口」是全部 308 个 issue 中评论最多的一条（7 评论，涉及 cordis 底座与 `ctx.tools/llm/skills/web/subagents` 扩展点统一入口）（`research/issues.md`）。
- 集成路径汇总：toybox/皮肤/MCP 类走 `repository-plugins` 静态格式；tg-bot/qqbot/live-stats/working-activity/subagent-tree/web-components/plugin-registry 走**源码级（复制进 monorepo / 克隆到 plugins 目录）**；qqbot 是唯一走 `~/.dsh/plugins` + `config.yaml` insert 的免补丁宿主插件。

#### 各仓库的实际接入路径对比

| 仓库 | 接入路径 | 是否改宿主源码 | 激活方式 |
|---|---|---|---|
| toybox | 用户 `~/.dsh/config.yaml` 加 `repository-plugins` 条目（`github:dsh-external/toybox#<40位commit>&path:...`） | 否 | DSH `@deepseek-ai/dsh-repository-plugin` 拉取 + `prepare.js` 生成 assets |
| plugin-registry | 复制 `packages/plugin/` + UI 包进 monorepo + `git apply` 1061 行补丁 | 是（base.cordis.yml / CLI / apiproxy） | `dsh plugin install/enable` 或 Web 面板 |
| tg-bot | 复制 `packages/experimental/tg-bot` + `ui-tg-bot` + `git apply` 2KB 补丁 + cordis overlay | 是（`PRODUCT_SETTINGS_NAMESPACES`） | `dsh web --config web-tg.cordis.yml` |
| qqbot | 克隆到 `~/.dsh/plugins/dsh-qqbot/` + 软链 `@dsh-local/dsh-qqbot` + config.yaml insert | 否 | 宿主 HMR 热重载 |
| web-components | 复制 `packages/client/web-component/` + `git apply` 54KB 补丁 | 是（slots.ts host / descriptor.ts） | Web composition roster 登记 |
| dsh-skins | `pnpm add link:<clone>/packages/dsh-web-skins` + config.yaml insert 行 | 否 | `dsh web` 重启 / bundle HMR |
| dsh-subagent-tree | 复制 `packages/client/ui-subagent-tree/` + tsconfig 引用 + `web.cordis.yml` 登记 | 否（仅构建配置） | `dsh web` 客户端 bundle |
| dsh-live-stats | devDeps `link:../../deepseek-harness`（兄弟目录）+ `cordis.yml` 挂载 | 否 | `dsh web --config cordis.yml` |
| dsh-working-activity | 复制 `packages/activity/working-activity/` + `git apply` 27.8KB 补丁 | 是（client runtime / ui-conversation） | `cordis.yml` 启用 `working-activity` |
| group-chat-diary | 无（纯产物 HTML） | 否 | 浏览器双击打开 |

#### 为什么需要补丁：官方扩展点的能力缺口

把"需要改宿主"的仓库按缺口归类，可以看到当前官方扩展面缺什么：

1. **客户端渲染臂缺失**（web-components）：官方只有 React 渲染器，slot 树的 `host()` 面不开放给非 installed-renderer 适配器——补丁给 `SlotsService` 加 `host(): SlotRendererHost` 方法才打通。
2. **设置项写权限缺失**（tg-bot）：settings namespace 可以注册 schema，但要让浏览器写入某 namespace，必须把名字加进 host 的 `PRODUCT_SETTINGS_NAMESPACES` 白名单——这是"产品设置 vs 插件设置"的边界。
3. **动态插件挂载缺失**（plugin-registry）：官方 cordis.yml 是静态组合，运行时 `ctx.plugin()` 挂载、CLI 子树、apiproxy RPC 域都得由补丁接线。
4. **会话事件的自定义消费/渲染缺失**（working-activity）：官方 ui-conversation 不认识 `activity/status` 这类自定义 log-only 事件，需要补丁在 client runtime 加 wire 类型并在组件里渲染。
5. **私有快照依赖**（skins/live-stats）：不需要补丁的仓库用"inline 平台模块表 + link 兄弟目录"绕开构建期依赖，但代价是无法独立构建。

> 结论：**客户端扩展面（slot/ThemeService/projection/dshClient）已经足够开放，服务端扩展面（动态挂载、设置写权限、渲染管线）仍有缺口**——这正是"哪些能力该回灌主仓库"的决策依据。

### 2.2 补丁集成模式："复制 + git apply 锚定 0804 快照补丁"

至少 5 个仓库以"把代码复制进 DSH monorepo（或兄弟目录）+ 应用一份锚定 0804 快照的补丁"的方式集成：

| 仓库 | 补丁 | 锚定基线 | 补丁内容 |
|---|---|---|---|
| web-components | `patches/web-component-plugin.patch`（54KB） | DSH master `b4b67f0`（官方 0804 snapshot） | `SlotsService.host()` seam、ui-slots descriptor.ts 新增 264+ 行 typed 协议、docs/config-catalog、测试适配 |
| plugin-registry | `patches/dsh-plugin-registry.patch`（1061 行） | 官方 0804 快照 `20260804T143803Z` | 改 30 个文件：base.cordis.yml 挂 `plugin-local`、CLI 子树、apiproxy 五个 method + zod schema、TS project refs |
| working-activity | `patches/webui-working-activity.patch`（27.8KB） | 官方 0804 快照 `20260804T143803Z` | 改 12 个文件：client runtime 新增 `ActivityStatusView` wire 类型、ui-conversation 渲染进 WorkingLine/TurnStatus |
| tg-bot | `integration/deepseek-harness.patch`（2.0KB） | DSH commit `fa3d357fc66102d82f0ddbf67fd3d5d70944d8f7` | `PRODUCT_SETTINGS_NAMESPACES` 加 `'tg-bot'`、package.json 依赖、pnpm-workspace allowBuilds 收紧、tsconfig 引用 |
| skins | 无 git apply，但 vendored 官方 tsdown 预设（inline 平台模块表） | 私有快照 `20260804T143803Z`（commit `f1792735`） | `packages/client/tsdown.client.ts` 平台模块表写死 inline 常量；另 `link:` 指向兄弟目录 `fulltest-wt/` 快照 |

**共性**：

1. **同源同基线**：补丁全部锚定 2026-08-04 的官方快照（`20260804T143803Z` / `b4b67f0` / `fa3d357`），说明 0804 是生态的"事实基线"——所有仓库与主仓库同一时刻对齐。
2. **集成动作同构**：cp（或 link）→ git apply → tsconfig 引用 + package.json 依赖 → pnpm install → build，README 都把安装流程写成 4-5 步。
3. **补丁即协议扩展**：补丁不只是接线，还携带协议定义（web-components 的 descriptor 协议、plugin-registry 的 apiproxy plugins 域、tg-bot 的 settings namespace 白名单），说明**当前官方扩展点不足以支撑这些能力，必须改宿主**。
4. **兼容性声明诚实但脆弱**：tg-bot README 明说"pre-release，不承诺 ABI 稳定"；skins 通过 inline 预设 + link 兄弟快照规避构建期漂移。

**风险**：

1. **锚点漂移 = 集成失效**：DSH 主仓库基线一更新，所有补丁都可能需要 `--3way` 或手工对齐；无任何仓库配置自动 rebase 检查（CI 只测自身，不测与最新主仓库的兼容性）。
2. **补丁是"一次性快照债"**：交付物绑死单一 commit，而主仓库 770 files changed / 12,564 insertions / 30,749 deletions 的版本差异（旧 session 实测）说明漂移速度很快（`context/session-019fc8ab-summary.md`）。
3. **双重来源不一致风险**：skins 同时依赖"inline 预设 + 兄弟目录 link"，`pnpm install` 缺快照直接失败（`research/dsh-skins.md`）；web-components 独立 clone 后 `tsdown.client.ts` 缺失导致无法构建（`research/web-components.md`）。
4. **补丁内嵌绝对路径泄漏**：web-components 顶层 README 残留 `/home/raum/deepseek-harness/...` 开发机路径，未脱敏（`research/web-components.md`）。

### 2.3 扩展点利用：各仓库使用的官方 seam 全景

DSH 主仓库的扩展面（cordis 底座 + `ctx.*` 服务 + 事件流 + Web 客户端契约）被各仓库以不同组合复用：

| 官方 seam | 使用仓库 | 用法要点 |
|---|---|---|
| **slot（客户端插槽）** | skins（`settings.general.item`，order 20）；live-stats（`conversation.composer.dock`，order 1）；subagent-tree（`sidebar.workspaces.sessionRow` + `sidebar.workspaces.sessionRow.branch`，双 hole）；working-activity（TUI `tuiPrompt.register('activity')` 槽位）；web-components（`ctx.slots.register(..., descriptor)` + 补丁新增 `slots.host()`） | 全部用 `ctx.slots.register` / `deferRegistration` 处理宿主声明时序竞态（subagent-tree 专门验证了该竞态） |
| **ThemeService** | skins（`ctx.theme.register({id, colorScheme, tokens})` + `setTheme` + `theme/change` 订阅） | 只追加 `body[data-ds-skin]` 与自己的 `<style data-plugin>`，不碰官方 ThemePresenter 的 DOM |
| **projection（可回放投影）** | live-stats（`ctx.sessionProjections.register('liveTokenUsage')`，key 必须匹配客户端 `LiveTokenUsageProjection` 契约） | replayable 状态机：同一事件日志可重放，支持时间旅行与崩溃恢复 |
| **settings namespace** | tg-bot（`settingsNamespace('tg-bot')` schema + host patch 加入 `PRODUCT_SETTINGS_NAMESPACES`）；qqbot（绕开 settings，直接行级改写 `~/.dsh/config.yaml` 并依赖 HMR） | 前者是标准 seam，后者是"免补丁"取巧但落盘格式脆弱 |
| **session 事件流** | live-stats（消费 `step/start`、`request/header`、`assistant/chunk`、`assistant/message`、`step/end`、`turn/end`、surface 事件）；working-activity（`ctx.on('session/event')` 消费 turn/assistant/tool 事件 + `session.append('activity/status')` 产出 **log-only 事件**，模型不可见、不进 surfaceOp、回放忽略）；qqbot（`ctx.on('session/event')` + `session/event` 回送回复）；tg-bot（经 `apiProxy.events.mux` 订阅 RPC 流） | 事件流是远程通道与状态类插件的主干 seam |
| **agent 服务** | qqbot（`ctx.agents.{get,create,resume}` + `ctx.get('sessionPersistence')` + `ctx.commands.register` + `ctx.on('agent/status')`）；working-activity（`agent/status` 事件） | qqbot 直接消费宿主 agent 生命周期，tg-bot 则经 ApiProxy RPC 间接访问 |
| **systemPrompt section** | working-activity（`ctx.systemPrompt.section({name, order:60, text})` 注入 `⏵` 自述约定） | 影响模型行为的唯一插件（其余都是旁观/渲染） |
| **invariants（不变量伴侣）** | web-components / working-activity / tg-bot / subagent-tree / plugin-registry / qqbot 系均注册 | 多数为**空实现占位**（仅预约包名），只有 working-activity 与 web-components 有真实校验 |
| **dshClient 客户端契约** | skins / subagent-tree / web-components / live-stats / plugin-registry UI / tg-bot UI | `dshClient: {inject, platform:'web'}` + `exports['./client']` + `window.__ModuleLoader__.load({id, factory})` closure-factory bundle 协议 |

**观察**：客户端插件契约（slot + ThemeService + dshClient bundle）已经足够成熟，5 个 Web UI 扩展类仓库全部零补丁或仅轻补丁即可接入；而**服务端能力（任意 Cordis 插件、settings 写权限、动态挂载）仍缺官方通道**，导致 tg-bot/plugin-registry 需要改宿主源码，qqbot 需要直接编辑 config.yaml——这是"扩展点利用"的主要瓶颈。

### 2.4 远程通道族：tg-bot vs qqbot 对比

两个仓库是同 org 内对等的"IM 远程通道"兄弟实现，架构对称（每聊天一个持久化会话、流式回送、与 Web GUI 共享会话），差异集中在协议层与集成方式：

| 维度 | tg-bot（Telegram） | qqbot（QQ） |
|---|---|---|
| **传输协议** | Telegram Bot API **HTTP 长轮询**（`getUpdates`，默认 25s/上限 50s，纯 outbound，零新增攻击面）；无 SDK，直接 `fetch` | QQ Bot API v2 **WS 网关**（`api.sgroup.qq.com` REST 换 token → `/gateway` → op 10 Hello/2 Identify/6 Resume/1 心跳/0 Dispatch）+ REST；零运行时依赖（Node 内置 WebSocket/fetch/crypto） |
| **集成方式** | **源码 cp + host patch**（`PRODUCT_SETTINGS_NAMESPACES`）+ cordis overlay `web-tg.cordis.yml`；patch 锚定 commit `fa3d357` | **宿主端插件**：克隆到 `~/.dsh/plugins/dsh-qqbot/` + 软链 + `config.yaml` insert 条目，**无补丁、无源码改动**，靠 HMR 热重载 |
| **host 访问面** | 复用 **ApiProxy RPC 面**：`sessions.create/prompt`、`events.mux`（RPC 流）、`respond`（提交问答应答）——与 Web 客户端**等权**，没有单开特权通道 | 直接消费宿主服务：`ctx.agents.{get,create,resume}`、`sessionPersistence`、`ctx.on('session/event')`、`ctx.commands.register` |
| **会话模型** | 每 chat 一个 session，id `tg-<chatId>-<randomUUID>`，映射持久化 `$DSH_HOME/tg-bot/chats.json`（versioned、原子写、fail loud）；`/new` 强制新 session | 每 chat 一个 session，id `qq-<kind>-<chatId>`（`/new` 后追加 `-g<n>` 代数归档旧会话）；重启后 `resume` 续上 |
| **交互能力** | **ask-user-question → inline keyboard**：单选即点即答、多选 toggle + "完成"、自由文本项等待下一条消息、取消结算；dispose 时自动 cancelled 防 agent 永久阻塞 | **无内联键盘**（`INTERACTION_CREATE` 未处理），跨端审批按钮/更新确认不可用——已标注为通道能力短板 |
| **鉴权/凭据** | `allowedChatIds` 白名单 fail-closed；token `role('secret')` + UI `type=password` + wire 只回 `tokenSet` boolean（**write-only**）；但 token 明文落盘 settings 文件 + 进程环境 | 私聊/群聊双策略 `open|allowlist|disabled` + `ownerIds` 兜底；扫码绑定（`/qq bind`）AES-256-GCM 传输 client_secret，但解密后**明文写回 `~/.dsh/config.yaml`**（无 chmod 600） |
| **连接韧性** | 401 停止、retryAfter 退避、400 幂等 no-op；但 mux 流断开后只 log，prompt 仍进 agent 而回复永不显示 | 关闭码分类（FATAL/SESSION_INVALID/token 失效/限流）+ 退避序列 + 快速断开熔断 + 进程级单连接守卫 + 跨实例持久化去重（HMR 双连安全） |
| **分块/渲染** | 4096 字符边界感知切分（段落→行→词→硬切）；800ms 节流编辑；`assistant/message` 覆盖 chunk 去重 | 4000 字上限按 `\n`/`。` 断行；Markdown（msg_type=2）被拒时自动降级纯文本重发；C2C 发"输入中" |
| **已知短板** | 媒体消息（照片/语音/文档）**静默忽略**无提示；`chatForSession` O(n) 线性反查；服务端文案硬编码中文 | 频道（guild）媒体上传 v1 不支持；`/models` 输出硬截前 20 条；Identify `$os` 硬编码 `'darwin'`；License 声明与文件不一致（package.json BSD-3-Clause vs LICENSE MIT） |
| **维护状态** | 1 commit（2026-08-05，作者昵称已脱敏），单次首发 | 1 commit（2026-08-05，org 账号提交），单次首发 |

**结论**：tg-bot 胜在交互协议完备（inline keyboard）与"零新增攻击面"的 outbound 长轮询；qqbot 胜在零依赖、免补丁热重载接入与生产级重连韧性。**两者可叠加部署**（各自独立插件 id），但都处于"单次提交首发"的极早期，无迭代历史可观察维护节奏。

### 2.5 已落地仓库亮点摘录（按仓库）

- **toybox**（`research/toybox.md`）：工程纪律扎实——整活归整活，每插件都要过官方 prepare + 真实 MCP 协议冒烟（initialize → tools/list → 每工具 call）+ skill frontmatter 校验，CI 全门禁；MCP 服务器零依赖单文件，最终用户零安装成本；"诚实标注"是明文纪律（判断类技能强制 `文件:行` 证据链，娱乐类插件自认"简化算法仅供娱乐"）；`publish.mjs` 一键 pin 40 位 commit ref 并重写 README 安装块与 catalog，杜绝手抄 ref。
- **plugin-registry**（`research/plugin-registry.md`）：声明即契约 + 回滚保证（contributes.tools 未注册则挂载失败、fiber 回滚、enabled 不持久化）；原子注册表（index 以 tmp+rename 提交，读者永不见截断）与 per-home Promise 链串行化；tarball `strict: true` 防路径穿越；信任边界 = 默认禁用 + 显式启用；文档极完整（双层对比、能力面 vs 声明面辨析、Known Limitations 自报家门）。
- **tg-bot**（`research/tg-bot.md`）：零新增攻击面——纯 outbound 长轮询，prompt/respond/events 全走宿主既有 ApiProxy 面，与 Web 客户端等权；流式渲染工程严谨（800ms 节流、4096 字符边界感知切分、`assistant/message` 覆盖 chunk 做权威去重、turn 结束 overflow 多消息保证最终转录是完整文本精确 chunk 序列）；状态持久化 fail loud（versioned、未知版本抛错而非静默开新会话）；token write-only（wire 只回 `tokenSet` boolean）。
- **qqbot**（`research/qqbot.md`）：真正的零运行时依赖（WS 协议、token 刷新、AES-GCM 解密、YAML 行级改写全用 Node 内置 API）；扫码绑定免开放平台操作（`/qq bind` 一条命令拿二维码，解密密钥只在本机生成、从不外传）；生产级连接韧性（关闭码分类/退避/快速断开熔断/进程级单连接守卫/跨实例持久化去重，把 HMR 双连、重放、错配都考虑到了）；测试无网络依赖（FakeWebSocket + Fake fetch）。
- **web-components**（`research/web-components.md`）：架构定位清晰——明确是 `web-react` 的"原生孪生"而非移植，复用同一 slot/runtime 数据源与组合 API 但不共享呈现 API；类型安全到 register 调用点（descriptor 协议编译期推导 + 运行期 shape 校验双重护栏）；失败隔离（单条目失败降级为 `[data-dsh-slot-diagnostic]` 诊断元素）与不变量伴侣（tag 注册表一致性断言）；loader-composition 用真实 vendored Loader 端到端验证组装树/会话切换/dispose 级联。
- **dsh-skins**（`research/dsh-skins.md`）：零核心改动的范式样本——主题注册走官方 `ctx.theme.register`、设置页复用官方 `settings.general.item` slot、DOM 镜像只回收自己写的东西，卸载无残留；AI 生图背景以 data URL 内联自包含（无外部托管、无仓库二进制），CSS 仅限 `background-*` 类属性（Safe CSS 门禁）；质量门禁最严（vm 沙箱跑 client.js 冒烟、i18n 双语结构签名门禁、单一发布脚本 pin commit）。
- **dsh-subagent-tree**（`research/dsh-subagent-tree.md`）：纯函数可测——`tree.ts` 把"目录快照→行树"做成无副作用投影，测试直接断言输出（覆盖三级标签降级链、递归聚合、诊断过滤）；正确处理插件加载竞态（`deferRegistration` 等 hole 落账后再注册）；资源释放严谨（展开/卸载时 `setSubagentCatalogOpen` 释放目录订阅，store 句柄在 apply 内创建避免 HMR 钉死身份）；无障碍与 i18n 到位（treeitem 角色、键盘导航、中英双字典）。
- **dsh-live-stats**（`research/dsh-live-stats.md`）：关注点分离干净（estimator 纯函数零副作用 / projection 不可变状态机天然 replayable / React 视图仅消费快照）；双精度策略——流式期间字符密度近似实时刷新，provider usage 到达后 `exactStep` 整体替换 buckets 并置 `estimated` 标志透明告知用户；重试与中断感知（`addReplacing` 以 (turn, step) 复合键防重复计数，abort 场景回滚估算样本）；配置严格校验 fail-fast。
- **dsh-working-activity**（`research/dsh-working-activity.md`）：隐私友好——不采集、不上传、无网络请求、无遥测，`activity/status` 是 log-only 事件（模型看不见、不进 surfaceOp、回放忽略）；状态机纯函数化 + 时钟注入，测试完全确定性；publish 节流设计扎实（live phase 节流刷新耗时、idle/done 仅 line 变化才发）；双端独立窄化（host 与 client runtime 各自维护 wire 类型校验，规避 cordis Context 类型合并冲突）。
- **group-chat-diary**（`research/group-chat-diary.md`）：零运行时依赖、纯静态、可永久归档（273KB 单文件 HTML，几年后打开仍可用）；证据可追溯性做得严肃——每条 chronicle 带 `message_id` 和 `source_ref: sha256:...` 指纹，`quality` 字段公开采集方法学，明确"不用 LLM 给身份/信号打分"；隐私分级清晰（原始记录留本机，公开层只发聚合 + 精选）。
- **issues**（`research/issues.md`）：反馈密度极高（4 天 308 个 issue 加速放量）；统一的标题前缀约定（`[类别][子系统]` 范式可机器解析、可统计，事实上承担了 label 的角色）；自动化 P1 台账（#147 每 20 分钟重建勾选清单）；README 安全提示到位（要求清除 API Key/令牌/个人信息）。

### 2.6 生态内协作与分工观察

- **两个"正经 vs 整活"分工轴**：toybox README 明确与 `dsh-hub`（`ohmyd-dev/dsh-hub`）分工——dsh-hub 收"正经通用插件"（git 提交信息、代码规范等），toybox 只收"有梗的"（`research/toybox.md`）；plugin-registry 与 pi-mono 的对比则是"能力面覆盖 + 补上安装/启停/校验/分发"的横向分工（`research/plugin-registry.md`）。
- **同一作者横跨多仓库**：某位作者（GitHub 用户名已脱敏）同时是 toybox（整活插件箱）与 dsh-skins（换肤）的作者，两个仓库共用同一套"catalog + publish 脚本 + 不可变 ref + CI 门禁"工程范式，说明这两个仓库事实上是同一套生态工程标准的孪生实现；另一位用户（用户名已脱敏）既是 issues 仓库 Top 6 反馈者（15 条）又是 dsh-subagent-tree 作者，是"反馈者转化为贡献者"的案例（`research/dsh-skins.md`、`research/toybox.md`、`research/issues.md`）。
- **署名习惯混乱是生态早期特征**：plugin-registry 作者本地未配置 GitHub 邮箱（commit 邮箱为含本机主机名的本地邮箱，已脱敏）；live-stats 的 LICENSE 署名与提交作者不一致（用户名均已脱敏）；group-chat-diary 的 commit author 与 HTML 内 `self:true` 标记的维护者昵称不一致（身份均已脱敏）——维护者归属不透明，外部读者难以判断（`research/plugin-registry.md`、`research/dsh-live-stats.md`、`research/group-chat-diary.md`）。
- **风格致敬链**：working-activity 明示对齐 `pi-working-activity` 文案风格（`phrases.ts` 头注）；dsh-skins 参考 [Fei-Away/Codex-Dream-Skin]（MIT）的"一图一情绪"思路但声明是独立实现——DSH 生态在向其它 agent 产品（pi、opencode、Codex）取经（`research/dsh-working-activity.md`、`research/dsh-skins.md`）。
- **群聊与代码库的双向印证**：group-chat-diary 纪事里的 `snapshot-*` tag（8/01→8/02→8/03 三条）构成主仓库内测版本轴，8/03 22:43 的 snapshot 附完整功能清单（远程 Markdown 图片、TUI `/details` 命令、失败 Bash 展开等）——与旧 session 的版本差异分析互为佐证（`research/group-chat-diary.md`）。

---

## 3. 风险热区

### 3.1 主仓库核心红线（来自 issues 仓库 308 个 issue）

issues 仓库（`research/issues.md`）是 4 天内（8/01→8/04，10→31→105→162 加速放量）形成的内测缺陷台账，其中最需要优先上报的红线：

**安全/审计类（最高优先级）**

- **#302** `[bug][core]`：AGENTS.md 无信任门槛自动升级为 system-reminder——注入封套与真实提醒逐字节相同，无同意环节。
- **#300** `[bug][core]`：Agent 可删除自身会话审计日志——无沙箱、无篡改检测、exit 0 无诊断。
- **#301** `[bug][core]`：`/compact` 压缩对摘要零保真校验，含用户硬约束的历史被压成 "else."，红线静默消失。
- **#176** `[bug][core]`：torn zstd 帧静默恢复，尾部事件丢失且日志被改写为 "interrupted"。
- **#73** `[bug][core]`：OutputCollector spill 写入失败（writeSync）未捕获，ENOSPC 时整个进程崩溃。

**并发/持久化数据完整性**

- **#118 / #20** `[bug][core][persistence]`：WebUI 与 TUI 两个进程并发写同一会话，JSONL seq 冲突后无法加载（corrupt session log: seq gap）。
- **#88**：被中断回合的流晚写导致 compact 卡死，会话在 1M 上下文处死锁。

**流式/UI 资源泄漏**

- **#7**：Web 内存持续增长至 1.4GB+，SSE ReadableStream queue 无限堆积（客户端停读 + enqueue 无背压）。
- **#106**：临时插件卸载后 httpServer 资源未清理（route/tapIndex 残留）。

**子代理生命周期高频痛点**（#11/#44/#85/#96/#99/#307）：调度串行化（#99：9 个并行调用实际逐个串行）、子会话归类错乱（#11/#96 进"未分组"）、父子 turn 感知断裂（#85）——其中 #44（subagent 执行过程不可见）已有社区实现（subagent-tree 插件）。

**治理观察**：308 个 issue 中 286 open / 22 closed（close rate ≈ 7.1%）；22 个 closed 中有相当一批在 2026-08-04 14:48 一分钟内批量关闭（疑为脚本清账，需确认是否真验证修复）；全部 308/308 无平台 label，分类靠标题前缀正则，任何书写偏差都会漏统——建议主仓库补 label 体系。issue 主题分布：WebUI 158（~51%）、Core 44、TUI 30、A11y 14、Goal 9。

### 3.2 插件仓库共性风险

把 11 个有内容的仓库的风险项横向归并，出现五类系统性风险：

1. **同进程任意代码执行，无沙箱**：
   - plugin-registry：插件 `apply(ctx)` 拿到完整 Cordis context，可注册工具/事件/服务/命令/系统提示/TUI 覆盖层；README 直言"sandbox 限制的是工具调用不是插件；无签名、无发布者身份、无审核"；enable 即 `import(entryUrl)` 动态加载无签名校验（`service.ts:75`）；catalog `source` 是任意本地路径，文件被篡改可指向任意目录（`catalog.ts:54-58`）（`research/plugin-registry.md`）。
   - tg-bot / qqbot / working-activity 均为同进程 cordis 插件，与主进程零隔离；qqbot 甚至直接编辑用户 `~/.dsh/config.yaml`。
2. **凭据明文落盘**：
   - qqbot：`clientSecret` 以 JSON 明文写进 `~/.dsh/config.yaml`，`writeFile` 无显式 `chmod 600`（`lib/credentials.js` 行 ~110）（`research/qqbot.md`）。
   - tg-bot：token 明文落盘 settings 文件 + 进程环境（README 自警"treat the local settings file and process environment as sensitive storage"）（`research/tg-bot.md`）。
   - toybox time-capsule：胶囊消息明文 JSON 落地 `~/.dsh-capsules/*.json`，只防"未到期经 API 读取"，不防"直接 cat 文件"（`src/time-capsule.mts:38,60-66`）（`research/toybox.md`）。
3. **补丁锁定单 commit**（见 §2.2）：web-components（`b4b67f0`）、plugin-registry（`20260804T143803Z`）、working-activity（`20260804T143803Z`）、tg-bot（`fa3d357`）四份补丁全部锚定 0804；skins 以 inline 预设 + link 兄弟快照规避但同样绑定私有快照。
4. **私有快照依赖**：skins 5 个 `@deepseek-ai/dsh-client-*` 走 `link:../../../fulltext-wt/...`（对应私有镜像，镜像名含个人用户名，已脱敏），CI 也依赖能 clone 私有仓库；live-stats devDeps 全部 `link:../../deepseek-harness/...`，要求插件 checkout 与 harness 兄弟目录布局——离开 dsh-external 组织完全无法构建。
5. **catalog ref 滞后于 HEAD**（发布纪律断裂）：
   - toybox：README 安装块与 `catalog.json` 仍 pin `c02a31be…`，HEAD 已是 `7acd885`（`research/toybox.md`）。
   - skins：`catalog.json` pin `083d4c7a…`（2026-08-04T17:26:22Z），HEAD 已是 `07238b2`（2026-08-05T02:29:32+08:00）——下游按 catalog ref 安装拿不到最新测试与修复（`research/dsh-skins.md`）。
   - 两仓库都有 `publish.mjs` 一键 pin 脚本，但"提交后未重跑 publish"成为系统性纪律问题。

**次要但值得记录**：live-stats 的 CJK token 低估（默认 4 chars/token，中文约 1.5-2）与 TPS 无平滑、surface replace 抛异常会崩整个 projection；working-activity 多会话节流闭包单例、文案池无 i18n 机制；tg-bot env overlay 拒绝负数 chat id（群组 id 常为负，与设置面板允许负数不一致）；web-components 的 `session-maybe` 无会话时不运行 selector（潜在空值 bug）、`connectedCallback` 异常不隔离。

### 3.3 安全面专项

- **qqbot 凭据 chmod**：扫码绑定（AES-256-GCM 传输）设计良好，但解密后的 client_secret 明文落 `~/.dsh/config.yaml` 且无权限收紧；依赖"配置文件不被他人读取"的隐性假设。建议至少 `chmod 600` + OS keychain 优先。
- **tg-bot token write-only**：这是**正面范例**——`z.string().role('secret')` + UI `type=password` + wire 只回 `tokenSet: boolean`，patch 注释强调"token never rides the wire back to the browser"；但其存储端仍明文，与 qqbot 同病。
- **group-chat-diary PII**：单文件 HTML 内嵌 `__DSH_SNAPSHOT__` 全量数据（`DSH内测群每日档案-0804.html:266`），含 109 名成员真实微信昵称、角色定性、代表性发言原文（部分含主观评判）；README 承认"private 仓库无法阻止已授权者下载外传"。同时存在**数据源不一致**：README 写 `dsh-external/issues`，而 snapshot 内 `issues.source.repository = "dsh2026/issues"`、issue URL 指向 `github.com/dsh2026/issues`——旧 session 确认 issues 仓库已从 dsh2026 迁移到 dsh-external，该档案数据滞后于迁移（`research/group-chat-diary.md` + `context/session-019fc8ab-summary.md`）。

### 3.4 issues 仓库的运营情报（聚合报告的决策输入）

- **Top 反馈者集中**：头部 6 名反馈者（GitHub 用户名已脱敏）的 issue 数分别为 64 / 27 / 23 / 16 / 15 / 14，合计 159 条，约占全部 issue 的 51%，建议主仓库维护者优先与这批用户建立直接沟通通道（`research/issues.md`）。其中一人同时是 dsh-subagent-tree 的作者（对应 issues#44），是"社区开发者 + 头部反馈者"双重身份的代表。
- **评论量低、单点热度极高**：102 条评论 / 平均 0.33 条每条；最热 #171（插件系统暴露标准入口，7 评论）说明插件分发/贡献协议是内测期最关注的架构级议题（`research/issues.md`）。
- **主题聚类**：WebUI 158（~51%）、Core 44、TUI 30、A11y 14、Goal 9、其余（Models/Connection/Session/History/Persistence/Subagent/Headless/Plugin/Protocol）约 25；其中 A11y（WAI-ARIA Dialog、SVG accessible name、aria-live、键盘聚焦、屏幕阅读器）是一条独立主线，但本生态 11 个仓库中**无一对 A11y 有专门投入**——是生态空白（`research/issues.md`）。
- **issue 闭环率低**：286 open / 22 closed（close rate ≈ 7.1%），大量 P1 仍 open；若需要"内测期最受关注的 10 个缺陷/特性"，直接以 #147 自动清单为主键、按 `P1 + core/web/tui` 分组取头部（`research/issues.md`）。

---

## 4. 与旧 session 调研的衔接

旧 session（019fc8ab，`context/session-019fc8ab-summary.md`）在 deepseek-harness 快照仓库上做了磁盘 I/O 静态调研、远端部署测试与版本差异分析，对本生态调研有四条衔接价值：

1. **磁盘 I/O 四类热点是插件评估的背景基线**：
   - 会话持久化检查点（`session-checkpoint-policy` 在每个模型请求/顶层工具执行/agent step 边界 flush；JSONL 每批次 fsync，SQLite 每批次事务）；
   - JSON KV 与会话投影缓存（`storage-json` 每次单记录更新整文件原子重写；`session-projection-cache` 事件数/时间节流但 JSON 后端放大为整文件重写）；
   - SQLite 会话全文查询（每次搜索先 `_reconcile` 全表 SELECT + 快照克隆 + FTS5 重建）；
   - 开发 HMR / TUI 补全 / Web 静态服务（HMR 默认 500ms × bundle 数 × statSync；TUI `@` 查询最多遍历 10,000 条目；静态服务每请求 readFile 无缓存）。
   - **对插件的意义**：live-stats 的 projection 依赖 session 事件持久化（replay 语义），working-activity 的 `activity/status` 刻意设计为 log-only（不落 surface、不进派生模型历史）正是对写放大成本的回应；任何订阅 `session/event` 的插件（qqbot/tg-bot/working-activity）都运行在上述写链之上，评估其开销必须考虑 checkpoint flush 与投影缓存的放大效应。
2. **issue 仓库迁移 dsh2026 → dsh-external**：旧 session 发布 issue 到 `dsh2026/issues`，现 org 已更名/迁移为 `dsh-external/issues`；group-chat-diary 的数据仍指向旧地址（见 §3.3），属迁移后未同步的遗留。
3. **TUI 移除解释 opencode-server 动机**：版本差异分析确认 `packages/ui/tui` 整体删除、CLI 的 TUI 配置/入口/向导删除、`--interface=tui` 移除、SDK 只保留 `acp` 和 `embed`（依据 Agent Note `2026-08-04-remove-tui-package.md`，Web 是保留的交互式产品）；`dsh-opencode-server`（描述"把dsh的tui换成opencode！"）正是这一决策的替代方案占位——当前 0 commit，未启动。
4. **两代插件格式的时间线印证**：旧 session 断言"群聊宣称的 `dsh.plugin.json` 插件系统不在快照中；实际只有受限的 `.dsh-plugin/package.json` 格式"；本调研确认 plugin-registry 已把 `dsh.plugin.json` 做成独立仓库实现（§2.1），两代格式并存是生态演进的事实状态。
5. **版本差异的九项发布说明都有源码证据**（旧 session 在 25b2ad4f67 → 6feab99fdf 差异中核验）：内置 ripgrep、回合运行时长、`web_search` 完整结果滚动、长输入光标、信号退出与遥测收尾、Thinking 尾部跟随滚动、长对话切换滚动位置保持、侧边栏滚动条统一；Web 连接层改 WebSocket 下行（`websocket-downlink.ts`，上行 HTTP 不变，两条下行流承载 mux 和 host 数据）。对插件生态的直接含义：主仓库 Web 面正在高频演进，任何补丁类集成（§2.2）的窗口期都在缩短。
6. **旧 session 的 backlog issue 草案是插件评估的参考系**：
   - #47 [proposal][protocol] ContentBlock 语义分裂（harness/MCP/ACP 三协议同名不同物，MCP 入口有损投影）——与 web-components/skins 等客户端渲染臂的"输入以 JS 属性跨边界"设计直接相关；
   - #58 [proposal][persistence] 流式 Delta 事件持久化改造（`assistant/chunk` 全量落盘导致写放大 O(tokens)）——与 §4.1 的磁盘 I/O 热点互相印证，也是 live-stats projection 重放与 working-activity log-only 事件设计要面对的存储形态；
   - #79 [web][suggestion] 交互设计建议汇总（11 个功能点，7 个已有、4 个新增）——可作为 Web UI 扩展类仓库（skins/subagent-tree/live-stats）后续选题清单。
7. **群聊对齐结论**：Web 端近期修复有代码 + Agent Note + 测试三方覆盖；"历史加载已优化"只解决首屏返回上限，**未解决超大会话端到端内存与全量读取问题**；安全边界、审计日志、压缩保真、后台任务资源上限仍有源码证据问题——这些与 issues 仓库的核心红线（#302/#300/#301/#176）互相印证，说明内测反馈与代码现状高度一致。

---

## 5. 维护状态矩阵

| 仓库 | 最近 push（代码层） | 提交数（浅克隆可见） | 活跃度 | 成熟度 |
|---|---|---|---|---|
| issues | 2026-08-01（README 单次提交）；issue 活动至 2026-08-04 | 1 | issue 极活跃：4 天 308 个、#147 每 20 分钟自动刷新 P1 清单 | 运营中（纯 tracker） |
| toybox | 2026-08-05 | ≥1 | 积极迭代：8 插件全过官方 prepare + 协议冒烟，CI 全门禁 | 已落地（生态最完整） |
| plugin-registry | 2026-08-04 | 1 | 首发，8 个 spec + 补丁 150 行 apiproxy 测试 | 已落地（0.0.1，协议完整） |
| tg-bot | 2026-08-05 | 1 | 单次首发，6 个 vitest spec | 已落地（实验性，patch 集成） |
| qqbot | 2026-08-05 | 1 | 单次首发，node:test 两 spec | 已落地（零依赖宿主插件） |
| web-components | 2026-08-04 | 1 | 单次剥离快照，测试扎实（mount.spec 36.7KB + loader-composition） | 已落地（需宿主构建） |
| working-activity | 2026-08-04/05（docs 提交） | 2 | 刚发布到 org，4 个 spec 34 项测试 | 已落地（0.0.1） |
| skins | 2026-08-05（=08-04 18:29 UTC，测试补齐） | 1（浅） | 紧跟官方 snapshot 高频迭代（README 列 0803→0804 delta） | 已落地（4 皮肤 + CI 门禁） |
| subagent-tree | 2026-08-04 | 2 | 当天新建（18:30 创建/18:41 文档），22 项测试 | 已落地（对应 issues#44） |
| live-stats | 2026-08-04 | 1 | 新立项单提交，2 个 spec | 已落地（新立项） |
| group-chat-diary | 2026-08-05 | 1 | 初期上线（每日 05:00 生成 + 人工提交，暂无自动链路） | 已落地（档案型） |
| sandbox-mxc | 2026-08-04（创建 2 秒后） | 0 | 无 | 占位未启动 |
| dsh-opencode-server | 2026-08-04（创建 1 秒后） | 0 | 无 | 占位未启动（TUI 替代动机明确） |
| ex-setting | 无 push 可查（git ls-remote 空） | 0 | 无 | 占位未启动（org 内唯一完全空置） |
| dsh-coding-receipt | 2026-08-04（创建 1 秒后） | 0 | 无 | 占位未启动 |

**总体判断**：已落地仓库全部集中在 2026-08-04 ~ 08-05 两天内创建/首发——这是 DSH 0804 官方快照发布后的一轮"生态圈地潮"；除 toybox/skins 外均为单次提交，无迭代历史可判断长期维护节奏。**四个占位仓库（sandbox-mxc、dsh-opencode-server、ex-setting、dsh-coding-receipt）创建于同一窗口（08-04 16:02~18:03），创建与 push 间隔 1-2 秒，是典型"先建仓占名"模式**。

**耦合关系观察**：11 个已落地仓库对主仓库快照的依赖呈"星形"——全部直接依赖同一份 0804 快照（补丁锚定 / link 兄弟目录 / inline 预设 / peer `^0.0.1`），仓库之间**几乎不互相依赖**（唯一例外是 subagent-tree 对 issues#44 的"产品需求级"引用）。这意味着：①生态整体健康状况 = 主仓库快照的稳定性；②任何一个仓库的集成失效不会传导到其它仓库（解耦良好）；③但也没有共享的"生态 CI"来统一守护快照兼容性——各仓库 CI 只能自证，不能互证。

---

## 6. 洞察与建议

面向"接下来做什么"，综合全部 15 个仓库：

1. **插件协议路线需尽快对齐，避免两代格式长期分裂**：`.dsh-plugin/package.json`（toybox 采用）与 `dsh.plugin.json`（plugin-registry 采用）目前互不兼容；issues#171（插件系统暴露标准入口）是社区最关注的架构议题。建议以 plugin-registry 的协议（id/engines.dsh/contributes 声明即契约 + 生命周期管理）为蓝本，推动主仓库正式接纳或明确路线图，否则生态会继续出现 tg-bot 那种"官方格式不够用只好打补丁/改 config"的绕行实现。

2. **补丁集成模式是最大的系统性运维债务，应建立 rebase 检查机制**：5 个仓库锚定 0804 快照，主仓库每次大版本（旧 session 实测 770 files changed）都会造成批量失效。建议：①各仓库 CI 增加"对最新主仓库基线执行 `git apply --check`"的守护任务；②推动主仓库提供 ABI 版本协商（而不是 `^0.0.1` 的 pre-1.0 依赖）；③对纯客户端能力（skin/slot/projection 类）优先走官方 seam，把补丁需求压到最少——skins 已证明零补丁可行，是值得推广的范式。

3. **值得深挖的仓库（按价值排序）**：
   - **plugin-registry**：协议最完整、测试最扎实、是插件生态的枢纽；其 tarball strict 解压、原子注册表、mount 后置 enabled 的信任边界设计可直接复用。建议下一步验证 `dsh.plugin.json` 与主仓库 `repository-plugin` 静态格式的互操作或迁移路径。
   - **qqbot**：零依赖 + 生产级连接韧性（关闭码分类/熔断/跨实例去重）是远程通道的参考实现；补上 `INTERACTION_CREATE`（内联键盘）后能力可追平 tg-bot，适合作为国内 IM 通道主推。
   - **live-stats**：projection seam 的完整范例（可回放状态机 + exact 校正 + abort 回滚），是理解 DSH 会话事件模型的最佳教学材料。
   - **skins**：零核心改动范式 + 最严 CI 门禁（vm 冒烟、Safe CSS、i18n 结构签名），其 `publish.mjs` 纪律（不可变 commit ref）值得 toybox 等仓库效仿。

4. **四个占位仓库不应计入能力清单，但有两个值得跟踪**：sandbox-mxc（微软跨平台沙盒）与 ex-setting 目前无任何信息可判断；**dsh-opencode-server 与 TUI 移除直接相关**（旧 session 确认 `packages/ui/tui` 已删），是"下一代交互前端"的候选信号，建议监控首次 commit（触发条件：`gh api repos/dsh-external/dsh-opencode-server/commits` 非空）；dsh-coding-receipt 的"session log → 可分享 receipt"概念与主仓库会话产物天然耦合，落地后需重点审查脱敏实现。

5. **安全红线优先上报（主仓库侧）**：#302（AGENTS.md 注入）、#300（审计日志可删）、#301（压缩丢硬约束）、#176（zstd 静默恢复）、#73（ENOSPC 崩溃）、#118/#20（并发写 corrupt）——其中 #302/#300/#301 属于"信任边界被击穿"级缺陷，且 22 个 closed issue 中存在一分钟批量关闭的疑点，建议主仓库维护者对这批关闭逐条复核。

6. **插件侧安全与隐私整改清单**：qqbot 凭据 `chmod 600`/keychain（当前明文 config.yaml）；tg-bot token 存储端加密；toybox time-capsule 加显式加密或至少文档警示（当前"密封即密封"只在 API 层成立）；group-chat-diary 的 PII 外传风险需要机制化（内嵌快照可考虑成员名脱敏开关），并**修正 issues.source 指向 dsh2026/issues 的过期数据**（README 与数据不一致会误导读者）。

7. **发布纪律必须制度化**：toybox 与 skins 的 catalog/README 安装块双双落后 HEAD（"更新插件=换 ref"纪律未被遵守）。建议把 `publish.mjs` 接入 CI（每次 push 自动重跑并校验 catalog ref == HEAD），或在 CI 加"catalog ref 落后即失败"的守卫——这是 4 行脚本能消灭的一类系统性 bug。

8. **利用已有资产做下一步调研**：group-chat-diary 是内测时间轴与人脉图索引层（版本轴 snapshot-20260801/02/03，8/03 22:43 的 snapshot 附完整功能清单），issues#147 是 P1 优先级权威源（每 20 分钟刷新）；结合旧 session 的磁盘 I/O 基线，下一个高价值主题是"把 issues 的 308 个 issue 按子系统聚类成主仓库修复路线图"（建议以 #147 为主键 + `P1 + core/web/tui` 分组取头部 issue）。

---

## 附录 A：证据索引（摘要文件 ↔ 仓库 ↔ 关键事实）

| 摘要文件（research/） | 对应仓库 | 本报告引用的关键事实锚点 |
|---|---|---|
| issues.md | dsh-external/issues | 308 issue / 286 open / #302 #300 #301 #118 #20 #176 #73 #7 #106 / #147 台账 / #171 热帖 / Top 反馈者 |
| toybox.md | dsh-external/toybox | `.dsh-plugin` 静态格式 / 8 插件 / prepare.js 133KB / 不可变 commit ref / catalog 滞后 |
| plugin-registry.md | dsh-external/plugin-registry | `dsh.plugin.json` 协议 / 1061 行补丁 / 声明即契约 / 无沙箱 / catalog 本地路径 |
| tg-bot.md | dsh-external/tg-bot | 长轮询 / ApiProxy 复用 / settings namespace / inline keyboard / patch 锚定 fa3d357 |
| qqbot.md | dsh-external/qqbot | WS 网关 / 零依赖 / 扫码绑定 / 凭据明文无 chmod / 无内联键盘 |
| web-components.md | dsh-external/web-components | 原生渲染臂 / descriptor 协议 / 54KB 补丁锚定 b4b67f0 / 无法独立构建 |
| dsh-skins.md | dsh-external/dsh-skins | ThemeService 4 皮肤 / 零补丁 / catalog 滞后 / 私有快照 link |
| dsh-subagent-tree.md | dsh-external/dsh-subagent-tree | 双 hole 注册 / deferRegistration / 对应 issues#44 |
| dsh-live-stats.md | dsh-external/dsh-live-stats | projection seam / composer.dock / CJK 低估 / TPS 无平滑 |
| dsh-working-activity.md | dsh-external/dsh-working-activity | activity/status log-only / TUI 槽位 / ⏵ 叙述 / 27.8KB 补丁 |
| group-chat-diary.md | dsh-external/group-chat-diary | 单文件 HTML / 109 成员 PII / dsh2026 数据源不一致 |
| sandbox-mxc.md | dsh-external/sandbox-mxc | 空仓库 / 描述"微软跨平台沙盒支持" / 0 commit |
| dsh-opencode-server.md | dsh-external/dsh-opencode-server | 空仓库 / "把dsh的tui换成opencode！" / 0 commit |
| ex-setting.md | dsh-external/ex-setting | 空仓库 / "DSH 的设置扩展" / git ls-remote 空 |
| dsh-coding-receipt.md | dsh-external/dsh-coding-receipt | 空仓库 / "session log → coding receipt" / 0 commit |
| context/session-019fc8ab-summary.md | —（deepseek-harness 快照调研） | 磁盘 I/O 四类热点 / TUI 移除 / dsh2026→dsh-external 迁移 / 版本差异 9 项 |

## 附录 B：术语表（本报告使用的生态词汇）

- **cordis**：DSH 主仓库的插件底座框架（4.0.0-rc.7），插件 = `apply(ctx, config)` + `inject` 声明式服务注入；`ctx.plugin()` 运行时挂载。
- **seam（扩展点/接缝）**：DSH 官方对外开放的集成面，如 `ctx.slots.register`（插槽）、`ctx.theme.register`（主题）、`ctx.sessionProjections.register`（投影）、`settingsNamespace`（设置域）、`ctx.on('session/event')`（事件流）、`dshClient` 客户端契约。
- **slot（插槽）**：客户端 UI 扩展点，形如 `settings.general.item`、`conversation.composer.dock`、`sidebar.workspaces.sessionRow(.branch)`；`deferRegistration` 用于规避宿主声明时序竞态。
- **projection（可回放投影）**：以 `SessionEvent` 流为输入、产出派生快照的状态机；同日志可重放，支持时间旅行与崩溃恢复；live-stats 的 `liveTokenUsage` 是唯一实例。
- **settings namespace**：`@deepseek-ai/dsh-settings` 提供的配置域；浏览器写某 namespace 需 host 将其列入 `PRODUCT_SETTINGS_NAMESPACES`。
- **ApiProxy**：`@deepseek-ai/dsh-host-apiproxy` 提供的 RPC 面（`sessions.create/prompt`、`events.mux`、`respond`），Web 客户端与 tg-bot 共用。
- **log-only 事件**：写入会话事件流但不进入派生模型历史、回放忽略的事件（如 `activity/status`、`todo/write`、`plan/mode`）。
- **repository-plugin / `.dsh-plugin` 静态格式**：官方静态交付格式（skills + MCP 配置），经 `~/.dsh/config.yaml` 的 `repository-plugins` 挂载，身份为完整 40 位 commit ref。
- **`dsh.plugin.json`**：plugin-registry 定义的下一代插件清单协议（id/version/main/engines.dsh/contributes），带安装/启停/校验生命周期。
- **0804 快照（20260804T143803Z）**：DSH 主仓库 2026-08-04 的官方快照，是生态各仓库补丁/预设/link 的公共基线。
- **HMR**：DSH 的热重载机制（配置文件/插件变更即时生效），qqbot 依赖它实现免重启激活。
- **invariant companion（不变量伴侣）**：`@deepseek-ai/dsh-invariants` 的包所有权登记约定，多数仓库为空实现占位。

## 附录 C：本报告的局限

- 多数仓库以 `--depth 1` 浅克隆调研，只能观察最近一次提交；"提交活跃度/迭代节奏"结论不完整。
- 被调研仓库全部私有，star/fork/license 等公开元数据意义有限；sandbox-mxc/ex-setting 连 GitHub API 都不可达（404），只能依赖本地 clone 结果。
- 依赖未发布 `@deepseek-ai/dsh-*` workspace 包的仓库（web-components/skins/subagent-tree 等）无法在隔离环境构建验证，分析基于源码与测试用例静态审查。
- 旧 session 的磁盘 I/O 结论为静态源码追踪（未运行测量），其"待实测假设"（HMR 轮询量、JSON 后端路由、查询 reconcile 真实规模等）仍是开放问题。
- 占位仓库（sandbox-mxc/ex-setting/dsh-coding-receipt/dsh-opencode-server）的任何功能预期均为命名/描述推断，首次 commit 出现前不应作为事实引用。

## 附录 D：调研中发现的文档/数据不一致清单

以下不一致均来自摘要文件原文，聚合报告如实并列并给出建议：

1. **group-chat-diary：README 与内嵌数据指向不同 issue 仓库**——README 写 `dsh-external/issues`，snapshot 内 `issues.source.repository = "dsh2026/issues"`、issue URL 指向 `github.com/dsh2026/issues`（数据滞后于 dsh2026→dsh-external 迁移）。建议修正数据源或注明迁移。（`research/group-chat-diary.md`）
2. **toybox：中国传统色色数标注不一致**——README 住户表"61 色库"，`catalog.json` 描述"60 色库"；同时 README 安装块与 catalog 的发布 ref（`c02a31be…`）落后 HEAD（`7acd885`）。（`research/toybox.md`）
3. **dsh-skins：catalog.json 发布 ref 落后 HEAD**——pin `083d4c7a…`（08-04T17:26:22Z），HEAD 已是 `07238b2`（08-05T02:29:32+08:00），最新测试与修复未进 catalog。（`research/dsh-skins.md`）
4. **qqbot：License 声明不一致**——package.json 声明 BSD-3-Clause，仓库根 LICENSE 文件实为 MIT 文本；`Identify` 的 `$os` 硬编码 `'darwin'` 与实际 OS 不符。（`research/qqbot.md`）
5. **tg-bot：env 配置与设置面板的 chat id 规则相反**——`web-tg.cordis.yml` 的 filter 拒绝负数 chat id（群组 id 常为负），而设置面板 `parseChatIds` 与 locales 示例允许负数（`-1001234567890`），env 配置群组场景会静默丢授权。（`research/tg-bot.md`）
6. **web-components：GitHub 元数据 size 0KB 与实际代码量不符**——实际 clone 后 mount.ts 单文件 28.5KB、总量约 130KB+；README 声称"未配置远程仓库"但实际已推送到 dsh-external。（`research/web-components.md`）
7. **working-activity：最近提交日期在两份来源间表述不一**——任务元数据/摘要正文为 2026-08-04，个别字段带 08-05 时间戳；不影响功能结论，但引用日期时需注明基准。（`research/dsh-working-activity.md`）
8. **group-chat-diary：仓库描述"72KB"与实际 273KB 不符**——描述字段滞后，不影响使用。（`research/group-chat-diary.md`）

> 这类不一致集中出现在"创建当天一次性推送"的仓库，属于生态早期缺乏发布纪律（发布脚本未与提交钩子/CI 绑定）的副作用，与 §6 建议 7 直接呼应。
