# dsh-pty-windows 调研摘要

## 一句话定位
DeepSeek Harness PTY 子系统的 Windows 进程检查器插件——在 win32 主机上以 PowerShell CIM 枚举进程表、用 `kill(pid, 0)` 做存活探针，为 `@deepseek-ai/dsh-pty-local` 提供 `ProcessInspector` 的 Windows 实现；非 win32 平台自动 no-op。

## 技术栈与依赖
- **运行时**：纯 ESM（`index.mjs`），无运行时依赖、无构建步骤；TypeScript 类型由旁路的 `index.d.mts` 提供（仅供测试导入用类型）。
- **包名**：`@dsh-external/dsh-pty-windows` v0.1.0，`private: true`，`type: module`，`main: ./index.mjs`。
- **devDependencies**（package.json:11-16）：`@types/node ^22`、`typescript ~5.9.0`、`vite-tsconfig-paths ^5`、`vitest ^3`。无 runtime dependencies。
- **工具链**：pnpm（lockfileVersion 9.0，`.npmrc` 设 `auto-install-peers=false`，`pnpm-workspace.yaml` 仅放行 esbuild）。
- **测试**：vitest（`pool: 'forks'`），通过 `vite-tsconfig-paths` 的 `loose: true` 让非 TS 的 `index.mjs` 也能解析 `@deepseek-ai/dsh-pty` 路径映射（vitest.config.ts:1-15）。
- **类型检查**：`tsconfig.vitest.json` extends `../test-LoserFox/tsconfig.base.json`（即 harness 仓库的 vendored 基础 tsconfig），关掉 `noUncheckedIndexedAccess`/`exactOptionalPropertyTypes` 以兼容 vendored harness 类型。

## 文件结构概览
共 13 个被 git 跟踪的文件，结构极简：
```
dsh-pty-windows/
├── README.md               # 中文文档（契约、安装、开发、测试布局）
├── package.json            # 包元数据 + devDependencies
├── dsh.plugin.json         # 插件清单：id/version/main/engines/contributes
├── index.mjs               # 主入口（全部实现，约 100 行）
├── index.d.mts             # 类型声明（供 TS 测试导入）
├── tsconfig.vitest.json    # 仅测试用的 tsconfig
├── vitest.config.ts        # vitest + tsconfig-paths 配置
├── pnpm-lock.yaml          # 锁文件
├── pnpm-workspace.yaml     # allowBuilds: esbuild
├── .npmrc                  # auto-install-peers=false
├── .gitignore              # node_modules/ *.tsbuildinfo .vite/
└── tests/
    ├── unit.spec.ts           # 纯单元测试（fake ProcessInspectorInternals）
    └── integration.win.spec.ts # 仅 win32 跑的真实集成烟雾测试
```

## 核心功能与实现要点

1. **Cordis 插件契约**（index.mjs:88-91 `apply`）：仅当 `process.platform === 'win32'` 时 `ctx.provide('ptyInspectorWindows', factory)`，否则直接 return，保证 POSIX 主机零开销、无副作用。`factory = { create: createWindowsProcessInspector }`。

2. **PowerShell CIM 进程表枚举**（index.mjs:14-37 `windowsProcessTable`）：调用 `powershell.exe -NoProfile -NonInteractive -Command "Get-CimInstance Win32_Process | ForEach-Object { ... }"`，输出 `pid;ppid;CreationDate` 三段式。逐行解析时严格校验：`pid`、`parentPid` 必须是 safe integer 且 `pid > 0`，缺 `started` 字段（如 `100;200`）整行丢弃；解析失败/PowerShell 缺失 → 返回空数组（不抛错，保证 teardown 不挂）。

3. **WindowsProcessInspector 类**（index.mjs:50-77）实现 `ProcessInspector` 契约：
   - `processTree(rootPid)`：复用从 `@deepseek-ai/dsh-pty` 导入的 `processTree(table, rootPid)` 工具，返回后代优先的进程列表（unit 测试验证了环检测——每个 pid 只访问一次，tests/unit.spec.ts:103-110）。
   - `isAlive(identity)`：`kill(pid, 0)` 探针——在 Windows 上是存在性检查而非真杀进程；抛错即视为已死。
   - `signalProcess(identity, signal)`：先 `isAlive` 再 `kill(pid, signal)`，避免对死进程发信号。
   - `foregroundPgid`/`isStdinWaiting`：恒返 `undefined`/`false`（Windows 无 POSIX 进程组/前台 pgid 概念）。
   - `signalGroup`：显式 no-op（注释说明仅在调用方伪造 pgid 时到达）。

4. **工厂 + 测试缝**（index.mjs:80-86 `createWindowsProcessInspector`）：`platform` 默认 `process.platform`、`internals` 默认 `DEFAULT_INTERNALS`（均从 `@deepseek-ai/dsh-pty` 导入）；非 win32 返回 `undefined`，使主仓库能在同一调用点优雅回退到 POSIX 检查器。`ProcessInspectorInternals` 是注入 `exec`/`kill`/`readFile` 等系统调用的测试缝接口，让单元测试完全脱离真实 OS。

5. **插件清单**（dsh.plugin.json）：`engines.dsh >= 0.0.1`，`contributes.tools/skills` 均为空数组——确认本插件只贡献"服务槽位"（`ptyInspectorWindows`），不贡献工具或技能。

6. **测试覆盖**：
   - `tests/unit.spec.ts`（7.3KB，纯 mock）：CIM 行解析（含 malformed/pid≤0/小数 pid/缺字段的边界）、PowerShell 失败回退、进程树（含环检测、未知 root）、isAlive 双路径、signalProcess 仅对活进程发信号、createWin 工厂的平台分支。
   - `tests/integration.win.spec.ts`（`describe.skipIf(platform !== 'win32')`）：真实 Cordis `Context` 注册、工厂在非 win32 返回 undefined、`DEFAULT_INTERNALS` 下 CIM 表能包含 `process.pid`。

## 与 DeepSeek Harness 主仓库的集成点

- **服务槽位契约（seam）**：本插件在 win32 上 `ctx.provide('ptyInspectorWindows', factory)`；消费方是 `@deepseek-ai/dsh-pty-local`，它在插件加载时调用 `resolveInspector(ctx.get('ptyInspectorWindows'), process.platform)`（README.md:8-10）。槽位缺失或工厂返回 undefined（POSIX 情况）→ pty-local 回退到自己的 POSIX 检查器。这是单向查询、运行时松耦合的"服务发现"缝。
- **共享类型/工具包**：入口 `import { DEFAULT_INTERNALS, processTree } from '@deepseek-ai/dsh-pty'`（index.mjs:11）；类型声明 `import type { ProcessIdentity, ProcessInspector, ProcessInspectorInternals, PtySignal } from '@deepseek-ai/dsh-pty'`（index.d.mts:6-12）。`@deepseek-ai/dsh-pty` 是主仓库对外暴露的 PTY 缝包；本插件运行时通过从宿主 checkout 的 `node_modules` 向上解析获得（README.md 安装段），**无 npm 安装、无打包**。
- **Cordis 插件协议**：导出标准 `apply(ctx)` + `name`，由 harness 的 `dshx install` 机制加载。
- **插件清单**：`dsh.plugin.json` 的 `engines.dsh` 与 `contributes`（空 tools/skills）表明本插件只占服务槽位，不主动贡献工具或技能。
- **vendored tsconfig**：`tsconfig.vitest.json` extends `../test-LoserFox/tsconfig.base.json`——即 monorepo 邻座（test-LoserFox）的 harness 基础 tsconfig，说明此仓与 harness 主仓库处于同一 checkout 工作区。

## 亮点与风险

**亮点**
- **单一职责、契约清晰**：100 行实现完整覆盖 Windows 进程检查需求，POSIX-only 操作显式 no-op 并注释说明，避免假装支持（index.mjs:60-77）。
- **优雅降级**：PowerShell 缺失/失败 → 空进程表；非 win32 → 工厂返回 undefined 让 pty-local 回退；teardown 永不因枚举挂起（index.mjs:21-23, 30-32）。
- **可测性高**：`ProcessInspectorInternals` 注入所有系统调用，单元测试无需真实 OS；win-only 集成测试用 `describe.skipIf` 精准门控（tests/integration.win.spec.ts:6）。
- **无构建、无 runtime deps**：纯 ESM，体积小、安装快、供应链面窄。
- **环检测**：`processTree` 借助 `@deepseek-ai/dsh-pty` 的工具实现"每 pid 访问一次"，对 CIM 表中可能出现的循环父子关系稳健（tests/unit.spec.ts 单独验证）。

**风险**
- **依赖宿主 PowerShell 可用**：目标 Windows 必须有 `powershell.exe`（PowerShell 5.x 随 Windows 内置）。若主机仅装 PowerShell 7（`pwsh.exe`）而无 `powershell.exe`，枚举直接返回空表——`foregroundPgid` 又恒 undefined，会导致信号/telemetry 部分功能静默失效（index.mjs:18-23）。注释虽提到"powershell.exe ships on every supported host"，但 nano server/容器场景需复核。
- **`kill(pid, 0)` 语义依赖**：注释明确"在 Windows 上是存在性检查而非 kill"（index.mjs:54-55），依赖 Node.js 在 win32 把 0 信号映射为 `OpenProcess` 存在性探针；Node 大版本若变更此行为会破坏 `isAlive`（误判存活 → signalProcess 可能对已死 pid 发信号）。
- **started 字段语义弱**：CIM `CreationDate` 仅作"相等比较的不透明身份"，不被解析（index.mjs:18-19 注释、tests 中用 `s1`/`s2` 占位）。若 pty-local 后续期望时间戳排序/比较，会受限于当前契约。
- **私有包、无 npm 发布**：`private: true`，只能通过 `dshx install <git-url|dir>` 部署；CI/分发链路必须走 git。
- **测试基线依赖 monorepo 邻座**：`tsconfig.vitest.json` extends `../test-LoserFox/...`，独立 clone 时该路径不存在，`tsc -p tsconfig.vitest.json --noEmit` 会失败——本仓不能脱离 harness checkout 独立类型检查/测试。

## 维护状态
- **极新**：git 历史仅 1 个 commit（shallow clone 所见），提交时间 `2026-08-05 07:18:49 +0800`（调研当日约 16 小时前），committer 为 `DSH Agent`（自动化署名）。
- 单次提交内容：`docs: single Chinese README (README.md), remove the English/zh pair`——表明 README 经历过至少一轮 i18n 收敛迭代。
- 无 issues/PR 数据可查（shallow clone 不含），无 CHANGELOG，版本号仍停在 0.1.0。
- 包注释、测试覆盖度、文档完整度均高于典型新仓，像是 dsh-external 扩展生态首批 Windows 支持的奠基件。

## 备注
- **平台门控是双层的**：`apply()` 在加载时按 `process.platform` 注册/跳过；`createWindowsProcessInspector()` 再按传入 platform 决定是否真正实例化——两层独立，集成测试据此验证"工厂注册了但对 darwin 仍返回 undefined"（tests/integration.win.spec.ts:18-22）。
- **与本轮同批次其它 PTY 仓的关系**（推断）：仓库名 `dsh-pty-windows` 对应 `@deepseek-ai/dsh-pty-local` 的 Windows 分支，与可能的 `dsh-pty-local`（POSIX）形成平台互补；槽位名 `ptyInspectorWindows` 是显式 reserved 字符串契约，主仓库 pty-local 通过 `ctx.get` 解析，改名即破坏集成。
- **未在摘要中出现作者邮箱/真实姓名**：committer 仅为 GitHub 风格化名 `DSH Agent`，符合脱敏要求。
