# dsh-win-port 调研摘要

## 一句话定位
DeepSeek Harness（`dsh`）的 Windows 原生移植**分发仓库**——不含任何 harness 源码，所有 harness 侧改动以 9 个 `git format-patch` 补丁（0001–0009）形式流转，配 PowerShell 安装器与双语使用指南。

## 技术栈与依赖
- **载体语言**：PowerShell（GitHub 识别为主语言）；补丁内容则覆盖 TypeScript（harness 主体）。
- **运行前置**（消费侧）：git、Node `^22.19.0 || >=24`、pnpm；bash 系工具需 Git for Windows（`bash.exe` 自动探测）或 PATH 上的 bash。
- **构建前置**（桌面壳，独立仓库 `dsh-desktop`）：Go 工具链 + WebView2（Win11 自带，Win10 装 Evergreen Runtime）。
- **应用方式**：`git am --3way patches/windows-port/*.patch`，无 npm 包发布、无二进制 release。
- **补丁基线**：20260804 快照 `43086bf`，已验证可干净应用到 `feat/dsh-desktop` @ `de2e6f0`。

## 文件结构概览
```
dsh-win-port/
├── README.md / README.zh.md                      双语总览（仓库内容/快速开始/与 harness 关系/许可）
├── .gitignore                                    node_modules/、desktop/build/、*.tsbuildinfo、.vite/、.tmp/
├── scripts/
│   ├── apply-windows-patches.ps1   (1.5KB)       把补丁系列 git am 到 harness 检出
│   └── install-windows.ps1         (11.5KB)      POSIX install.sh 的 PowerShell 对应版
├── patches/windows-port/
│   ├── PATCHES.md / PATCHES.zh.md                补丁清单/基线/已知冲突点/应用后验证
│   ├── 0001-...launcher-and-PowerShell-ins...patch (17.4KB)
│   ├── 0002-...resolve-bash-path-per-platform...patch (14.7KB)
│   ├── 0003-...widen-kills-type-for-kill-pid-0...patch (1.0KB)
│   ├── 0004-...run-bash-and-PTY-tools-on-real-Windows-CI...patch (7.2KB)  *
│   ├── 0005-...native-PowerShell-shell...patch (32.7KB)
│   ├── 0006-...document-the-native-PowerShell-shell...patch (38.0KB)
│   ├── 0007-...extract-platform-shell-and-Windows-insp...patch (145.3KB)  ← 最大
│   ├── 0008-...document-the-platform-shell-and-inspect...patch (35.7KB)
│   └── 0009-...announce-the-no-sandbox-posture.patch (9.2KB)
└── docs/
    ├── windows-port.md / windows-port.zh.md      完整 Windows 使用指南（双语）
```
\* 注：文件名里出现 "run-bash-and-PTY-tools"，与 PATCHES.md 表中 0004 "真实 Windows CI" 描述措辞略有出入，但 PATCHES.md 表是权威清单（windows-2025 job、vitest win32 排除策略）。

## 核心功能与实现要点
1. **九补丁系列 = 完整 Windows 运行时**（`patches/windows-port/PATCHES.md`）：
   - 0001（P0）：`bin/dsh.cmd` 启动器 + `scripts/install-windows.ps1` + README Windows 章节。
   - 0002（P1）：`resolveBashPath` 按平台解析 bash、`WindowsProcessInspector`、`spawn-helper.exe`，让 PTY win32 可加载。
   - 0003（P1b）：放宽 `kill(pid, 0)` 类型，支持进程存在性探测。
   - 0004（P2）：真实 Windows CI（windows-2025 job + vitest win32 排除策略）。
   - 0005（P3）：原生 PowerShell shell 通道——`resolveShellPath`、`-Command` argv、UTF-8 输出解码 preamble、`$LASTEXITCODE` 尾声、CRLF→LF 归一化、按平台工具描述。
   - 0007（P4，最大补丁 145KB）：把平台 shell 与 Windows 检查器**插件化**——新增 `packages/shell/shell`（契约）、`packages/shell/shell-local`（POSIX bash 适配器）、`packages/shell/shell-windows`（PowerShell 适配器）、`packages/pty/pty-windows`（`WindowsProcessInspector` + CIM 进程表枚举）；消费方（bash-local / bash-sandbox / pty-local / tool-bash）改注入 `ctx.shell`，不再按平台分支。
   - 0009：Windows 沙箱姿态公告——`WINDOWS_SANDBOX_NOTICE`（win32 启动提示：无 OS 级沙箱，受限模式 fail-closed）。

2. **PowerShell 安装器 = POSIX `install.sh` 的镜像**（`scripts/install-windows.ps1:1-260`）：
   - 布局完全对齐：`%USERPROFILE%\.dsh\source\master`（master 克隆/采用检出）+ `staging-<UTC时间戳>` git worktree + `current` **junction**（Win 普通用户无符号链接权限）+ `dsh.cmd` shim 经 `current` 调用。
   - 在检出内运行会**采用**该检出（绝不克隆、绝不动工作树）；检出外运行则克隆 `DSH_REPO @ DSH_REF`。
   - 依赖检查含 Node 版本号解析（`^22.19.0 || >=24`），pnpm 缺失可经 corepack/npm 自动装。
   - 凭据写 `%USERPROFILE%\.dsh\.env`，只占 `DEEPSEEK_API_KEY`/`DEEPSEEK_BASE_URL` 两行、保留用户其余行；用 `icacls /inheritance:r` 做 Win 版 `chmod 600`。

3. **补丁应用器**（`scripts/apply-windows-patches.ps1:1-44`）：参数 `-Checkout` 指向 harness 检出，内部跑 `git -C $Checkout am --3way *.patch`；冲突时给出 PATCHES.md 引用与 `git am --continue` 提示。

4. **双实现明确分工**（`docs/windows-port.md`）：
   - **CLI（win-port）**：本仓库的补丁系列，给开发者在终端跑 `dsh`。
   - **桌面应用**：独立仓库 `dsh-desktop`，Wails(Go) 窗口壳，从用户环境启动 `dsh web` 嵌入 WebView2——不内嵌运行时、不调 CLI、HTTP 通信；安装互不依赖。

5. **平台插件推荐挂载**（README/0007 后续 README 更新）：
   ```powershell
   dshx install dsh-shell-windows https://github.com/dsh-external/dsh-shell-windows
   dshx install dsh-pty-windows   https://github.com/dsh-external/dsh-pty-windows
   ```
   - 不挂 shell-windows：等 `shell` 服务的工具会一直 pending。
   - 不挂 pty-windows：teardown 退回到更不可靠的枚举。
   - 补丁包用户（0007）已在树内拿到两个包，重复挂载会重复注册服务。

6. **第三方公告生成器 bug 修复**（0007 附带）：pnpm v11 截断的 virtual-store 名（长包名带内容哈希后缀）让前缀匹配漏掉 `@opentelemetry/exporter-logs-otlp-http` 等条目；补丁顺手修了 `scripts/gen-third-party-notices.ts`。但 PATCHES.md 提醒：**新基线已内置 `virtualManifest` 兜底，不要再采纳补丁对该文件的修改**。

## 与 DeepSeek Harness 主仓库的集成点
- **协议/seam**：补丁 0007 定义两条契约——
  - `PlatformShell`（argv / `resolveInteractive` / `normalizeOutput` / `toolOpener`），经 `ctx.shell` 注入；POSIX 由 `shell-local` 注册，Windows 由 `shell-windows` 注册（按宿主自选，单一 cordis.yml 双平台通用）。
  - `ProcessInspector`（移入 pty seam），`pty-windows` 注册为可选 `ctx.ptyInspectorWindows` 工厂；`pty-local` 经 `ctx.get` 咨询，POSIX 兜底失败即大声报错。
- **应用流程**：`git am --3way patches/windows-port/*.patch` 应用到 harness 检出；之后跑 harness 自有流程（`pnpm install` → `bin\dsh.cmd`）。harness 仓库 `feat/dsh-desktop` 分支是开发线，本仓库是分发/消费之家。
- **配置挂载**：补丁 0007 改动 `apps/cli/config/base.cordis.yml`、`core-web.cordis.yml`，以及多个 `examples/*/*.cordis.yml`，挂载两个 shell 适配器（+pty-windows）。
- **CI**：补丁 0004 在 `.github/workflows/ci.yml` 加 windows-2025 job、设 vitest win32 排除策略。
- **沙箱姿态**：补丁 0009 在 win32 启动时打印 `WINDOWS_SANDBOX_NOTICE`，受限模式（`read-only`/`workspace-write`）抛 `SANDBOX_UNAVAILABLE` fail-closed，只有 `danger-full-access` 能跑。
- **独立工具/不在本补丁包内**：桌面层（Wails 壳 + SEA 组装 + `run-windows.cmd`，随 `feat/dsh-desktop` 分支交付）；定制插件（如 `dsh-distill`、`dsh-tool-session-chatlog` 在独立插件仓库）；两者**零 patch 依赖**，原版/补丁后双基线均可挂。

## 亮点与风险
**亮点**
- 干净的"补丁即分发"模型：不携带任何原始源码，私有仓库只需接收补丁系列即可获得移植（`README.md:7-9`）。
- 冲突点完全透明：`patches/windows-port/PATCHES.md` 列出 6 个已知冲突点 + 各自修复命令（如 `pnpm run verify-translation-pairing --write` 重录配对哈希、`pnpm run gen-third-party-notices` 重新生成）。
- 安装器布局跨平台对称：PowerShell 版严格镜像 POSIX `install.sh` 的 master/staging/current 三段式（`scripts/install-windows.ps1:1-30` 注释明确）。
- 安全 fail-closed 设计：无 OS 级沙箱时受限模式直接抛错而非降级静默（`docs/windows-port.md` Security posture）。

**风险**
- **基线漂移**：补丁系列钉死在 20260804 快照（`43086bf`）；harness 主分支推进后必须靠 `git am --3way` 三方合并，6 个已知冲突点会反复出现（`patches/windows-port/PATCHES.md` "基线/已知冲突点"节）。
- **沙箱缺口**：Windows 没有 OS 级沙箱后端（AppContainer/restricted-token 方案是 deferred phase），目前只能跑 `danger-full-access`（`docs/windows-port.md` Security posture；补丁 0009）。
- **PTY 不完整**：交互式 PTY 后端可加载但**无信号/进程组支持**（`patches/windows-port/0001-...patch:50-53` README Windows 段）。
- **Python SDK 不在列**：Python SDK 运行时未做 Windows 构建（同上）。
- **MCP SDK 上游缺陷**：`@modelcontextprotocol/sdk` 的 exports 根入口在其上游 tarball 中缺失；SEA materialize 已按 `.pnpm` store 实体化兜底，但 SEA 之外静态 import 该包根入口需另作处理（`patches/windows-port/PATCHES.md` 末注）。
- **新基线重复修复**：补丁 0007 对 `scripts/gen-third-party-notices.ts` 的修改与主仓库后续内置 `virtualManifest` 兜底重复，应用时需主动丢弃该文件改动（`PATCHES.md` 已知冲突点）。
- **tui.snapshot.ts 已删**：补丁中对该文件的修改在新基线上随删除丢弃（`git rm`），同上。

## 维护状态
- **极早期**：仓库创建于 2026-08-04 22:55 UTC，全部 6 个提交集中在 2026-08-04 当天（4 分钟内 22:55–22:59），最新提交 `bacc53d` "readme: recommend mounting the Windows platform plugins in quick start"。
- **单一作者**：所有提交署名 `LoserFox`（GitHub 用户名，无真实姓名/邮箱泄漏）。
- **可见性 private**，0 star / 0 fork / 0 issue / 0 PR；默认分支 `main`；仓库体积 156KB（确属"纯补丁+脚本+文档"，无源码）。
- **未归档/未禁用**；与第一轮调研中 `dsh-desktop`、`dsh-pty-windows`、`dsh-shell-windows` 等独立仓库互为引用，构成 Windows 移植生态。

## 备注
- 本仓库是"消费侧入口"——它本身没有可编译/可测试的代码，验证流程是"打到 harness 检出里再跑 `bin\dsh.cmd -p echo-hi`"，因此调研以补丁元数据 + 脚本逻辑 + 文档为主。
- 调研来源：本地浅克隆 `/tmp/dsh-ext-research2/dsh-win-port/`（depth=1，最新提交 `bacc53d`）+ `gh api repos/dsh-external/dsh-win-port`（元数据与提交列表）。
- 与第一轮调研关系：本仓库在 dsh-external 生态中处于"Windows 移植分发中枢"位置，向上承接 harness 主仓库（`feat/dsh-desktop` 开发线），向下指向 `dsh-desktop`/`dsh-pty-windows`/`dsh-shell-windows` 三个独立插件/壳仓库。
- 脱敏：摘要中仅出现 GitHub 用户名 `LoserFox`，未包含邮箱或真实姓名。
