# marisa 调研摘要

## 一句话定位

**Marisa（魔理沙，内部代号 `dshx`）** 是 DeepSeek Harness 的**外部插件管理器**——以"寄生"方式注入到已安装的 dsh 中，零主仓库改动，提供 CLI（`dshx`/`marisa`）+ Web 面板双通道来安装、启用、更新、回滚、卸载第三方 Cordis 插件；自身也是 dsh-external 生态的"包管理器/registry 客户端"。

## 技术栈与依赖

- **语言/运行时**：TypeScript 5.9 + Node.js ESM（`engines.node >= 22.19 || >=24`），`package.json` `type: module`，相对 import 全用 `.js` 后缀。
- **运行时依赖（极简）**：仅 `semver@^7.6.3` 与 `tar@^7.4.3`（取代早期手写实现），二者会在 store 初始化时被 provision 到 `$DSH_HOME/marisa/node_modules/`。
- **devDependencies**：`typescript`、`@types/node`、`@types/semver`；面板额外用 `react@18`、`cordis@4-rc`、`tsdown`、`@deepseek-ai/dsh-client-ui-slots`。
- **插件协议**：标准 **Cordis** 插件（`name`/`inject`/`Config`/`apply` 命名导出）；规格来源支持纯 `package.json`（推荐）或旧版 `dsh.plugin.json`（仍兼容）。
- **构建**：自写 `scripts/build.js`（tsc typecheck + bundle），`scripts/check-drift.js` 强制 `lib/` 与 `src/` 一致（源码是唯一事实来源）；面板用 tsdown 产出 `__ModuleLoader__` bundle。
- **测试**：`node --test` 跑 `host/tests/*.test.ts`（manager/store/manifest/security/catalog/api，~70KB 测试代码），加 `scripts/ci-fixture.ts` 做 cordis fixture 闭环。
- **安装器**：POSIX `install.sh`（Linux/macOS）+ `install.ps1`（Windows cmd shim），三端覆盖。

## 文件结构概览

```
marisa/
├── dshx                        # 入口 shim（#!/usr/bin/env node → import lib/cli.js）
├── package.json                # name: dshx, version 0.2.0
├── src/
│   ├── cli.ts                  # CLI 主逻辑（1051 行，所有子命令 + --json envelope）
│   └── scaffold-sdk.ts         # dshx create --sdk 骨架生成
├── host/                       # PluginManager 深模块（CLI/API/面板共用）
│   ├── src/
│   │   ├── manager.ts          # 1745 行核心：plan/apply/事务/回滚
│   │   ├── store.ts            # $DSH_HOME/marisa 稳定存储 + journal
│   │   ├── manifest.ts         # 规格解析（package.json / dsh.plugin.json）
│   │   ├── catalog.ts          # 多源 catalog（hub/marisa-list/topic/本地）
│   │   ├── verify.ts           # ESM import 探针 + peer projection
│   │   ├── security.ts         # encodeId / assertInside（防 zip-slip）
│   │   ├── adapters.ts         # checkout 定位 / harness 版本探测
│   │   ├── overlay.ts          # ~/.dsh/config.yaml 受管块读写
│   │   ├── core.ts             # 兼容层（旧调用 → manager 委托）
│   │   ├── doctor.ts           # 诊断
│   │   └── index.ts            # dshx-host：/api/dshx/* JSON API
│   ├── dsh.plugin.json         # id: dshx-host（系统保护）
│   ├── package.json            # @dsh-external/dshx-host
│   └── tests/                  # 6 个 .test.ts（~70KB）
├── marisa-panel/               # dsh web 设置页面板（双面插件）
│   ├── src/
│   │   ├── index.ts            # 宿主半身（no-op）
│   │   └── client/             # 浏览器半身（React + dsh-client-ui-slots）
│   ├── lib/client.js           # 预构建产物（23KB）
│   └── dsh.plugin.json         # id: marisa-panel（系统保护）
├── skills/dshx-pull/SKILL.md   # 拉取 dsh-external 仓库并安装插件的技能
├── demo-plugins/               # dshx-hello、hmr-probe 示例插件
├── docs/                       # plugin-format.md / publishing.md / plugins.md
├── scripts/                    # build/typecheck/check-drift/ci-fixture/contract
├── install.sh / install.ps1    # 寄生注入安装器
├── probe.ts / hmr-live.ts / skillprobe.ts / webprobe.ts  # 集成探针脚本
└── assets/marisa.png           # Logo（东方 Project 雾雨魔理沙）
```

## 核心功能与实现要点

1. **寄生注入，零主仓库改动**（`install.sh:90-130`）：通过 `command -v dsh` → 解析符号链接链 → 定位 dsh checkout；把 dshx 源码拷进 `$DSH_HOME/dshx/`（`~/.dsh/dshx/`），launcher 软链到 `$DSH_BIN_DIR/dshx` 与 `marisa`（同名别名）。注入点选在 harness home 与 bin dir——**这两个目录不参与 dsh 升级 staging 轮转**，因此 dsh 升级不会破坏 dshx。

2. **PluginManager 深模块**（`host/src/manager.ts`）：CLI、host API、面板三者唯一的 mutation 入口。接口仅 `state() / plan(request) / apply(planId) / doctor()`。每个变更走两步：`plan` 生成 `OperationPlan`（含信任摘要、兼容性、变更列表、回滚点、确认门、changelog）并落盘成 transaction；`apply` 仅在 plan 未过期（TTL 10 分钟）且 state fingerprint 未变时执行，否则拒（`TAMPERED`/`EXPIRED`）。所有文件/状态/覆盖层写入经 journal，崩溃后下次 open 自动回滚到上一致状态。

3. **稳定存储 + 不可变 revision**（`host/src/store.ts:1-30`）：插件本体放在 `$DSH_HOME/marisa/revisions/<encodeId(id)>/<digest>/`，不就地覆盖；旧版本默认保留最近两个成功 revision 作为回滚点。`state.json` 是 registry 事实来源（desired enabled、activeRevision、source、peerLinks…）；覆盖层 `~/.dsh/config.yaml` 的受管块（`# >>> dshx managed block`）只镜像挂载条目。`dshx migrate` 把旧 `.external-plugins/` 安装迁入新存储。

4. **规格、宿主依赖与真实 ESM 探针**（`host/src/manifest.ts`、`host/src/verify.ts`）：支持两种规格——纯 cordis `package.json`（推荐，id 取去 scope 名）与旧版 `dsh.plugin.json`。`peerDependencies` 被显式解析：按 workspace/vendor/根 node_modules/pnpm 虚拟 store 索引，semver 校验后在 revision 内建 `node_modules/<peer>` 链接（修复了 marisa#2 的旧承诺）。`dshx verify` 对入口做真实 ESM `import()` 探针（不调 `apply()`），错误指名道姓指向具体依赖。tarball 安装先列条目，拒绝绝对路径/`..` 穿越/越界链接/多根（防 zip-slip，`host/src/security.ts`）。

5. **Web 面板（双面插件）**（`marisa-panel/`、`host/src/index.ts`）：`dshx web` 安装后 dsh web 设置页出现"插件" section，使用原生 `--dsw-*` 设计令牌。host 半身 `dshx-host` 注册 `/api/dshx/{state,list,catalog,diagnostics,updates,plan,apply,repair}` JSON API；mutation 强制 `application/json` + 同源（loopback 绑定）。**安装必须先展示 plan**（来源/commit/digest/入口/宿主依赖/client half/兼容警告/信任提示）再确认。状态分 Installed / Configured / Loaded / Broken / Unknown 五类，永不合并成一个 flag。

6. **多源 catalog + GitHub topic 自动发现**（`host/src/catalog.ts`）：四源合并去重——dsh-external/hub 的 `plugins.json`（默认）、marisa 仓库 `plugin-list` 分支（兜底）、`org:dsh-external topic:marisa-plugin` GitHub Search（H 方案，需 gh token）、本地 `dshx-catalog.json`。带 Etag/commit 指纹的 last-good 缓存（`catalog-cache.json`），离线/auth 失败继续服务并标 stale。**浏览 catalog 不 clone、不 import、不执行任何仓库代码**——只有用户请求 install plan 时才拉取源。

7. **事务化 + HMR + 信任边界**：所有变更事务化（journal + rollback）；TUI 面对 config.yaml 的改动热生效（HMR 行默认开），Web 面需手动启用 HMR 行（`hmr-live.ts` 是该场景的探针）。新安装**默认停用**，`--enable`/面板显式确认才挂载。每次安装/更新前必须核对信任摘要——挂载的插件是宿主进程内代码，拥有完整 OS 权限与全部服务访问权。

8. **生态友好工具链**：`dshx create [--sdk] <id>` 生成纯 cordis 或 `@deepseek-harness/sdk` 骨架；`dshx test/dev/pack` 提供最小 fixture 校验、开发投影、可复现 tarball（附 SHA-256）；`dshx profile export/plan/apply` 导出/对比/应用插件档案；`dshx-pull` 技能（首次运行自动同步到用户技能根）教模型如何从 dsh-external 拉取并安装插件。`dshx doctor` 只报告不改动，`dshx repair` 重建 staging 轮转后失效的 peer 链接与客户端投影。

## 与 DeepSeek Harness 主仓库的集成点

**核心契约（seam）：完全寄生，零主仓库改动**。所有集成通过 dsh 已有的公开扩展点达成：

1. **个人覆盖层 `~/.dsh/config.yaml`**：dshx 在其中维护受管块（`# >>> dshx managed block (do not edit)` … `# <<< dshx managed block`），写入 `- insert: [{ id, name: '<revision 绝对入口路径>' }]` 形式的条目。dsh 启动时（TUI/Web）按 cordis overlay 加载这些条目；HMR 行开启时改动热生效，headless 启动时读取。这是**唯一的运行时挂载协议**。

2. **dsh checkout 的 `node_modules`（peer 解析 + 客户端投影）**：插件声明的 `peerDependencies`（如 `cordis`、`@deepseek-ai/dsh-host-webserver`、`@deepseek-ai/dsh-app-boot`）由 dshx 从 checkout 解析并链接进 revision；带 `dshClient` 声明的插件在 `<checkout>/node_modules/@dsh-external/<id>` 建立可重建投影（链接指向稳定 revision）。`dshx doctor` 识别 staging 轮转失效，`dshx repair` 重建。

3. **dsh webserver 服务**：`dshx-host` 插件**不硬 inject** `@deepseek-ai/dsh-host-webserver`（避免与非 web 树竞态/失败），改用"服务存在时附加"策略——通过 `ctx.get('webserver')` 探测，注册 `/api/dshx/*` 前缀路由。

4. **dsh web 设置页 slot**：`marisa-panel` 通过 `dshClient.inject: ['@deepseek-ai/dsh-client-ui-slots']` 注入到 dsh web 设置页，client bundle 用 `__ModuleLoader__` 格式（`react`/`cordis`/`ui-slots` 是平台种子词，直接 require）。

5. **dsh toolchain 复用**：`dshx create --sdk` 生成的 SDK 插件用 dsh checkout 的 `tsc` + `tsdown` 构建（无需 npm install），产物自包含。本仓库自身的 `scripts/build.sh` 也走同一思路。

6. **dsh 启动器 PATH 解析**：`install.sh` 的 `locate_dsh()` 通过 `command -v dsh` + POSIX readlink 循环解析符号链接链定位 checkout；找不到则提示先装 Harness。

7. **集成探针**：`probe.ts`（用 `@deepseek-ai/dsh-app-boot` 的 `boot` + `loadPersonalPatches` 启动真实 dsh 组合，断言工具注册）、`hmr-live.ts`（启用 web HMR 行 + watchPersonalPatches 验证热挂载/卸载）、`skillprobe.ts`、`webprobe.ts`。

**无 patch、无 fork、无 manifest schema 改动**——这是 README 显眼徽章 "parasitic: zero harness changes" 的含义。

## 亮点与风险

**亮点**

- 深模块设计干净：`PluginManager` 单一 boundary，CLI/API/面板共享同一组类型、错误码与 plan/apply 协议（`host/src/types.ts:1-5` 注释明确"CLI, host API, and panel all project the same shapes, including the same error codes"）。
- 事务化做得彻底：plan/apply 两步 + journal + fingerprint + TTL + cross-process lock（`host/src/store.ts` 的 `TransactionRecord`、`acquireLock`），任意阶段崩溃都可恢复，符合"任意阶段失败都不改变旧 revision、enabled state 或用户 overlay"。
- 安全姿态认真：tarball zip-slip 防护（`security.ts` 的 `assertInside`）、id 编码避免 scoped 名直拼可删除路径、mutation 同源 + JSON-only、loopback 绑定、远程 tgz 强制 sha512 校验后再解压（`docs/plugin-format.md` §4）。
- catalog 浏览零代码执行（`catalog.ts:1-12` 注释明确），信任边界清晰（"挂载的插件是宿主进程内代码"）。
- 生态自举：dshx 自身（`dshx-host`、`marisa-panel`）就是两个 protected 插件，用自己的挂载机制管理自己。
- 文档非常完整：`docs/plugin-format.md`（13.8KB 规范 v0.4）、`docs/publishing.md`（6.8KB 发布指南）、`docs/plugins.md`（生态清单）、README（6.6KB）；命名/品牌（东方 Project 雾雨魔理沙"收集魔法道具"）考究。

**风险**

- **`host/src/manager.ts` 单文件 1745 行**（`src/cli.ts` 1051 行）：深模块边界正确，但内部 plan 实现（planInstall/planUpdate/planToggle/planRemove/planRollback/planMigrate/planRepair）全部集中在一个类，可维护性随操作种类增长会下降。
- **依赖 dsh 内部 API**：`@deepseek-ai/dsh-app-boot` 的 `boot`/`loadPersonalPatches`/`watchPersonalPatches`、`@deepseek-ai/dsh-host-webserver` 的 `register`、`@deepseek-ai/dsh-client-ui-slots` 等都是 dsh 私有包（版本 `^0.0.1`），dsh 升级若改这些 seam 会同步破坏 dshx——这是"零主仓库改动"代价的另一方面。
- **peer 链接对 staging 轮转敏感**：dsh 升级轮转 worktree 后，`dshx doctor` 必须能识别失效并 `dshx repair` 重建，否则已启用插件会 broken。逻辑路径多，是故障高发区。
- **catalog 的 GitHub topic 自动发现依赖 gh token**（`catalog.ts` 的 `githubToken()` 探测 `DSHX_GH_TOKEN` → `gh auth token` → WSL `gh` → 公开 HTTPS），私有 org 没有 token 时 H 方案完全不可用，回退到静态清单（A 方案）。
- **新安装默认停用 + plan 必看**对终端用户是更安全的默认，但相比"装上即用"的体验多两步操作；面板与 CLI 都需要显式 `--enable`/确认。
- **`dshx create --sdk` 路径探测**（`--sdk-path` > `DSHX_SDK_PATH` > 常见布局）在非标准安装机器上可能命中失败；显式路径无效时报错而非静默回退（这是优点也是用户需感知的约束）。

## 维护状态

- **活跃维护**：最新 commit `af40dd9` 时间 **2026-08-05 18:51 +0800（即本调研日）**，提交信息 `feat(sources): remote tgz install with sha512 integrity + re-source updates + exports entry fallback (PR #5 compatible parts)`——PR #5 兼容部分刚合入。
- **版本**：`package.json` 0.2.0；插件格式规范已迭代到 v0.4（"Marisa 稳定底座"）；`state.json` `formatVersion: 2`、`schemaVersion: 1`。
- **测试覆盖**：6 个测试文件覆盖 manager/store/manifest/security/catalog/api，加 ci-fixture 闭环；`npm run check` = typecheck + test + drift 检查，是 CI 守门人。
- **生态规模**：`docs/plugins.md` 已登记 7 个 dsh-external 插件（telegram、distill、dsh-vision、chat-width、dsh-tool-calculator、dsh-tool-json、session-chatlog），完整列表以 hub 的 `plugins.json` 为准。
- **License**：MIT，Copyright © 2026 dsh-external。

## 备注

- **命名**：`marisa` 是正式项目名（取自东方 Project 雾雨魔理沙，"收集魔法道具"喻指管理插件）；`dshx` 是 CLI 命令名与内部代号（"*external*" 缩写），二者指同一工具——`install.sh` 同时软链 `dshx` 与 `marisa` 两个 launcher。
- **品牌一致性**：与同属 dsh 生态的 `koishi`（古明地恋）一样来自幻想乡。
- **空仓库判断**：本仓库**非空**，clone 成功，文件结构完整（120 个顶层条目，含 `assets/marisa.png` Logo）。
- **本调研为只读**：`git clone --depth 1` 完成，未对远程仓库做任何修改。
- **关键引用文件**（供后续 agent 深入）：
  - `/tmp/dsh-ext-research2/marisa/docs/plugin-format.md`（规范 v0.4，13.8KB）
  - `/tmp/dsh-ext-research2/marisa/host/src/manager.ts`（深模块，1745 行）
  - `/tmp/dsh-ext-research2/marisa/host/src/types.ts`（共享类型契约，424 行）
  - `/tmp/dsh-ext-research2/marisa/host/src/index.ts`（dshx-host，/api/dshx/* 路由）
  - `/tmp/dsh-ext-research2/marisa/install.sh`（寄生注入逻辑）
  - `/tmp/dsh-ext-research2/marisa/src/cli.ts`（CLI 全部子命令）
