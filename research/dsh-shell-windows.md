# dsh-shell-windows 调研摘要

## 一句话定位
DeepSeek Harness 的 Windows PowerShell 外壳适配器——一个零运行时依赖的 Marisa（dshx）外部插件，仅在 win32 上注册 `ctx.shell`（`PlatformShell` 契约），为一次性命令、持久交互式 PTY、输出规范化和面向模型的工具描述提供 PowerShell 方言；在 POSIX 主机上是空操作，从而允许一个共享的 `cordis.yml` 同时挂载本插件与原版 POSIX 外壳适配器。

## 技术栈与依赖
- 语言：纯 JavaScript（ESM，`index.mjs`，附 `index.d.mts` 类型镜像），无构建步骤。
- 运行时：仅依赖 Node 内置（`node:fs`）；运行时由宿主 checkout 的 `node_modules` 向上解析 `cordis` 与 `@deepseek-ai/*`。
- `package.json`（`/tmp/dsh-ext-research2/dsh-shell-windows/package.json`）：`@dsh-external/dsh-shell-windows` v0.1.0，`private: true`，`type: module`，`main: ./index.mjs`。
- 仅 dev 依赖：`@types/node ^22`、`typescript ^5.8`、`vite-tsconfig-paths ^5`、`vitest ^3`。
- 测试：Vitest（`forks` 池），通过 `tsconfig.vitest.json` 路径映射解析 harness 源码。
- 包管理：pnpm（含 `pnpm-lock.yaml`、`pnpm-workspace.yaml`）。
- 无 lint/format 配置文件。

## 文件结构概览
```
dsh-shell-windows/
├── dsh.plugin.json         # Marisa/dshx 插件清单（id/version/main/engines/contributes）
├── index.mjs               # 全部实现（~190 行）：导出 name、resolvePowerShellPath、WindowsPlatformShell、apply
├── index.d.mts             # 上述 ESM 导出的 TypeScript 类型镜像
├── package.json            # @dsh-external/dsh-shell-windows，私有，仅 dev 依赖
├── pnpm-lock.yaml          # 锁文件（~33KB）
├── pnpm-workspace.yaml
├── tsconfig.vitest.json    # 继承 ../test-LoserFox/tsconfig.base.json
├── vitest.config.ts        # forks 池，include tests/**/*.spec.ts
├── README.md               # 中文说明（功能表 + 安装/测试）
├── .gitignore              # node_modules/、*.tsbuildinfo、.vite/
└── tests/
    ├── unit.spec.ts            # 跨平台单元测试（~20 例）
    └── integration.win.spec.ts # 仅 win32，挂载真实 Context 跑 PowerShell
```

## 核心功能与实现要点
1. **平台门控注册**（`index.mjs` 的 `apply(ctx)`）：`if (process.platform !== 'win32') return`；仅在 win32 调用 `ctx.provide('shell', new WindowsPlatformShell())`。这是「双平台共存」的关键——POSIX 上由原版 `@deepseek-ai/dsh-shell-local` 占有 `ctx.shell`。
2. **PowerShell 路径解析**（`resolvePowerShellPath(env, fileExists)`，`index.mjs:38`）：按优先级探测——pwsh 7 安装根（`%ProgramFiles%\PowerShell\7\pwsh.exe`）→ PATH 上的 `pwsh.exe` → Windows PowerShell 5.1（`%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe`）→ 裸 `powershell.exe` 兜底。`env` 与 `fileExists` 作为测试缝（test seam）注入，便于单测模拟。
3. **一次性命令 argv 组装**（`WindowsPlatformShell.argv(command)`，`index.mjs:99`）：返回 `[shellPath, -NoProfile, -NonInteractive, -Command, <前导码+命令+后置码>]`。前导码 `WINDOWS_POWER_SHELL_PREAMBLE` 强制 `[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)`，解决 Windows PowerShell 5.1 默认 OEM 代码页导致非 ASCII 输出乱码的问题；后置码 `WINDOWS_POWER_SHELL_EPILOGUE`（`; exit $LASTEXITCODE`）把上一条原生命令的退出码传播为进程退出码，对齐 `bash -c` 语义。
4. **交互式 PTY 默认值替换**（`resolveInteractive(shellPath, shellArgs)`，`index.mjs:115`）：当且仅当 `shellPath === '/bin/bash'`（PTY 配置的未配置哨兵）时，替换为已解析的 PowerShell 路径与 `[-NoLogo, -NoProfile]`；其他显式值原样透传。
5. **输出规范化**（`normalizeOutput(text)`，`index.mjs:127`）：`text.replace(/\r\n/g, '\n')`，把 Windows 原生工具的 CRLF 折叠为跨平台 LF。
6. **面向模型的方言教学**（`toolOpener()`，`index.mjs:132`）：返回一段提示文本，告知模型「Windows 无 bash，须用 PowerShell 语法（`$env:VAR`、`Get-ChildItem`、`;` 分隔；5.1 无 `&&`/`||` 与 POSIX 重定向；原生退出码读 `$LASTEXITCODE`）」。
7. **测试矩阵**：`tests/unit.spec.ts` 覆盖 preamble/epilogue 内容、argv 顺序、哨兵替换与透传、CRLF 折叠、路径解析四态、工具描述关键短语；`tests/integration.win.spec.ts` 在真实 `cordis` Context 中挂载 `LocalSubprocessService` + 本插件 + `LocalBashExecutor`，实跑 `Write-Output`、`cmd /c exit 7`（验证退出码传播）、`中文输出`（验证 UTF-8）、`Get-Location`（验证 workdir）、`Write-Error`（验证 stderr）。

## 与 DeepSeek Harness 主仓库的集成点
- **seam：`ctx.shell`（Cordis 服务 `provide('shell', ...)`）**。本插件实现主仓库（及上游 `@deepseek-ai/dsh-bash-local` 的 `LocalBashExecutor`、`@deepseek-ai/dsh-subprocess-local`）约定的 `PlatformShell` 契约：`argv / resolveInteractive / normalizeOutput / toolOpener` 四方法。集成测试（`tests/integration.win.spec.ts:11-32`）即以 `LocalBashExecutor` + `LocalSubprocessService` 作为消费方来验证。
- **挂载方式**：通过 `dshx install dsh-shell-windows <路径或 git-url>` 安装，并在共享 `cordis.yml` 中与本插件同时挂载 POSIX 外壳适配器；每个适配器只在自己平台上激活（README「双平台说明」）。
- **运行时符号解析**：`@deepseek-ai/*` 与 `cordis` 不在依赖列表，而是「mounted at runtime so ... resolve from the host checkout's node_modules via upward resolution」（`index.mjs` 文件头注释）；测试侧则通过 `tsconfig.vitest.json` 的 `paths`（继承自 `../test-LoserFox/tsconfig.base.json`）解析 harness 源码，无需构建。
- **清单契约**：`dsh.plugin.json` 声明 `engines.dsh: ">=0.0.1"`、`contributes: { tools: [], skills: [] }`（本插件不贡献工具/技能，仅提供服务）。
- **非补丁、非侵入**：独立仓库、独立插件，对主仓库源码零修改；POSIX 行为完全不变。

## 亮点与风险
- **亮点**
  - 零运行时依赖，单一源文件，关注点清晰；前导码/后置码常量、路径解析、平台门控各自独立可测。
  - 路径解析与测试通过 `env` / `fileExists` 注入完全解耦，单测无需 Windows 即可覆盖四条解析分支（`tests/unit.spec.ts:113-158`）。
  - UTF-8 前导码 + `$LASTEXITCODE` 后置码直击 Windows PowerShell 5.1 的两大真实痛点（OEM 代码页乱码、cmdlet 错误不传播退出码），并在集成测试中以 `中文输出`、`cmd /c exit 7` 实证（`tests/integration.win.spec.ts`）。
- **风险**
  - **极新仓库、单次提交**：`git log` 仅 1 个 commit（`b43a32c`，作者 `DSH Agent`，2026-08-05，即本日）；无历史可追溯演进，尚无外部用户验证。
  - **对兄弟仓库的硬路径依赖**：`tsconfig.vitest.json:2` 继承 `../test-LoserFox/tsconfig.base.json`——独立 checkout（缺少同目录下的 test-LoserFox）会导致类型检查/测试失败，需在同构 monorepo 布局下使用。
  - **路径解析「找不到则返回裸 `powershell.exe`」**（`index.mjs:84`）：注释声称「缺失会以正常 spawn『command not found』失败，绝不静默替换」，但裸字符串落到非 win32 的 `apply` 早期返回后其实不可达，仅作为兜底契约存在。
  - **`resolveInteractive` 对哨兵的 args 丢弃语义**（`tests/unit.spec.ts:99-105` 注释）：当 `shellPath === '/bin/bash'` 时，即便用户给了 `['-i','-l']` 也会被 PowerShell 默认 args 覆盖——这是有意设计但易被误读为 bug。
  - **私有仓库**：`gh api /orgs/dsh-external/repos` 返回空（org `public_repos: 0`），所有仓均私有，外网无 README 直读；克隆须凭 `gh` 已认证凭据。

## 维护状态
- 全新仓库：1 个 commit（2026-08-05），单分支 `main`，作者署名 `DSH Agent`（脱敏：无个人邮箱/真实姓名泄露，GitHub 用户名层面仅见组织账号 `dsh-external` 与作者 `DSH Agent`）。
- 无 Issues/PR/Release/CI workflow 文件（仓库内无 `.github/`），无 CHANGELOG。
- 与同批 41 个新仓一同爆发式出现，疑似 DSH 外部插件矩阵化建设的产物；本插件已是其声明的功能完整形态（4 方法契约 + 单测 + 集成测）。

## 备注
- 调研方式：因当前会话无 bash 直连，经 `hub start` 调用 `gh repo clone dsh-external/dsh-shell-windows` 完成 `--depth 1` 克隆至 `/tmp/dsh-ext-research2/dsh-shell-windows/`（克隆成功，非空）。
- 与 `dsh-shell-local`（POSIX，原版 harness 提供）互补：本插件只覆盖 win32，二者可同挂一份 `cordis.yml`。
- 关键文件行号引用：`apply` 平台门控 `index.mjs:170`；`resolvePowerShellPath` `index.mjs:38`；`argv` `index.mjs:99`；`resolveInteractive` `index.mjs:115`；`normalizeOutput` `index.mjs:127`；`toolOpener` `index.mjs:132`；tsconfig 继承 `tsconfig.vitest.json:2`。
