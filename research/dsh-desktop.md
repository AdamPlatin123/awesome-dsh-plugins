# dsh-desktop 调研摘要

## 一句话定位
dsh-desktop 是一个纯 Go 编写的 Wails v3 桌面壳程序，把 `dsh web` 后端封装成不依赖外部浏览器的桌面窗口（Windows WebView2 / Linux WebKitGTK / macOS WKWebView），壳本身就是后端的守护进程——启动、监控、退避重启并在退出时按进程树清理。

## 技术栈与依赖
- 语言/模块：Go 1.25.0（`go.mod`，模块名 `dsh-desktop`），单一 `package main`
- 核心依赖：`github.com/wailsapp/wails/v3 v3.0.0-beta.3`（Wails v3 beta，提供 WebviewWindow / SystemTray / Autostart / 事件系统）
- 间接依赖：`adrg/xdg`、`coder/websocket`、`go-ole/go-ole`、`godbus/dbus/v5`、`jchv/go-winloader`、`mattn/go-{colorable,isatty}`、`golang.org/x/sys`（均为 Wails 传递依赖）
- 构建工具：`just`（justfile，但默认 target 仍在仓库根用 `go build`）、GitHub Actions（Windows runner 出 `dsh-shell.exe` + `icon.ico` 的 zip）
- 运行时依赖：用户环境里的 `dsh`（PATH 上）+ 已 `pnpm run build` 的检出；Windows 11 自带 WebView2，Win10 需 Evergreen Runtime；Linux/WSLg 需 WebKitGTK + Wayland/X11
- 资源：`assets/icon.{png,ico,svg}`、`landing.html`（启动页，经 `//go:embed` 嵌入）

## 文件结构概览
```
dsh-desktop/
├── main.go              # 入口：env 解析、app/窗口创建、supervise 守护 goroutine、退出收口
├── command.go           # webCommandLine/parseCommandLine：DSH_WEB_CMD 解析与 {port} 替换
├── command_test.go      # 上述两个函数的单元测试
├── server_unix.go       # POSIX 后端管理：source rc → exec dsh，Setpgid 独立进程组，SIGTERM→SIGKILL
├── server_windows.go    # Windows 后端管理：taskkill /T 树杀（无信号语义），环境直接继承
├── tray.go              # 系统托盘：左键切换显隐、菜单（打开 dsh / 开机自启 / 退出）、关窗转最小化
├── webview_ready.go     # 竞态护栏：等 WebView2/WKWebView 首次导航完成再 SetURL（Linux 无此竞态）
├── landing.html         # 内嵌启动页（"正在启动本地服务…" 动画），替代 Wails 默认空白页
├── go.mod / go.sum      # 模块定义与校验
├── justfile             # dsh-win-port 风格的 build-windows / run recipes
├── run.sh               # WSLg 启动器：强制 Wayland + llvmpipe 软件渲染 + WebKit SHM 绕过 DRI3 bug
├── run-windows.cmd      # Windows 启动器：启动 build/dsh-shell.exe
├── scripts/
│   └── install-desktop-windows.ps1   # 一键安装器：本地或 gh release 下载 exe + 创建快捷方式
├── .github/workflows/build.yml       # CI：push 出 artifact，v* tag 出 Release
├── assets/icon.{png,ico,svg}         # 托盘/任务栏/快捷方式图标
├── README.md / README.zh.md          # 双语说明
└── .gitignore
```

## 核心功能与实现要点
1. **壳即守护进程**（`main.go:39-117` `startServer`/`supervise`）：壳启动用户 PATH 上的 `dsh web --port 0`（端口 OS 分配），从后端 stdout 逐行扫描 `dsh web: http://127.0.0.1:<port>` 前缀，解析出实际监听地址；超时 30s（`urlTimeout`）未出现则报错。`supervise` 用 `for` 循环 + 指数退避（初值 1s，封顶 30s，`restartBackoff`/`maxRestartWait`）自动重启异常退出的后端，并重新 `SetURL` 指向新地址。
2. **命令行解析**（`command.go:14-38`）：`DSH_WEB_CMD` 环境变量可覆盖整条后端命令行，`{port}` 占位符替换为实际端口；`parseCommandLine` 是极简引号规则（仅处理双引号包裹的空格），覆盖 `dsh web --port 0` 与带空格的可执行路径。`command_test.go` 用表驱动测试覆盖正常/带空格路径/空串等用例。
3. **POSIX 进程管理**（`server_unix.go:38-58` `serverCommand`）：经用户 `$SHELL` 执行 `source ~/.bashrc|~/.zshrc >/dev/null 2>&1; exec <cmd>`，让后端继承用户终端里 export 的环境（如 API key）；`exec` 保持同一 PID 不破坏 wait 语义；`SysProcAttr.Setpgid=true` 放入独立进程组，退出时 `kill -PGID` 整组清理。
4. **Windows 进程管理**（`server_windows.go:17-30`）：不 source rc，环境直接继承自壳进程；终止用 `taskkill /PID <pid> /T`（先不带 `/F` 请求退出，宽限期后 `/F` 强制），语义对齐 POSIX 的 SIGTERM→SIGKILL 阶梯。`stopServer` 在两种平台上都按 `serverStopGrace=5s` 等待 `exitCh` 收口。
5. **托盘常驻 + 关窗不退出**（`tray.go:25-69` `setupTray`/`registerCloseToTray`）：`ApplicationShouldTerminateAfterLastWindowClosed=false`（Mac）+ `RegisterHook(WindowClosing)` 拦截关闭（Cancel+Hide），左键单击切换显隐，菜单含"打开 dsh/开机自启复选框/退出"，只有"退出"触发 `app.Quit()` → `cancel()` → supervise 终止后端。开机自启走 `app.Autostart.Enable/Disable`（Windows 写 HKCU\…\Run）。
6. **WebView 就绪护栏**（`webview_ready.go:24-49` `awaitWebviewReady`）：Wails v3 beta 的 WebView2 控制器异步创建，未就绪时 `SetURL` 会 panic（"catastrophic failure"）。该函数监听 `Windows.WebViewNavigationCompleted` / `Mac.WebViewDidFinishNavigation` 事件，阻塞到首次导航完成或 30s 超时（Linux GTK WebKit 无此竞态直接返回 nil）。
7. **WSLg 软件渲染绕过**（`run.sh`）：设置 `LIBGL_ALWAYS_SOFTWARE=1`、`GALLIUM_DRIVER=llvmpipe`、`GSK_RENDERER=cairo`、`WEBKIT_DISABLE_{COMPOSITING_MODE,DMABUF_RENDERER}=1`、`WEBKIT_DMABUF_RENDERER_FORCE_SHM=1`、`GDK_BACKEND=wayland` 等绕过 Xwayland+DRI3 合成 bug；自动启动 D-Bus session 供 WebKit 辅助进程使用。
8. **CI 与安装器**（`.github/workflows/build.yml`、`scripts/install-desktop-windows.ps1`）：push 到 main 上传 artifact，`v*` tag 自动发布 `dsh-desktop-windows-amd64.zip` 到 Release；PowerShell 安装器优先用本地 `build/dsh-shell.exe`，否则用 `gh release download`（私有仓库认证）下载最新 Release 解压，安装到 `%LOCALAPPDATA%\dsh-desktop` 并创建开始菜单/桌面快捷方式。

## 与 DeepSeek Harness 主仓库的集成点
- **运行时依赖而非代码依赖**：壳不在源码层引用主仓库，运行时通过 PATH 调用 `dsh web`（默认）或 `DSH_WEB_CMD` 指定的命令。主仓库必须先 `pnpm run build`（至少 `build:web`），其 `bin/dsh` 在 PATH 上，壳才能拉起后端。
- **协议契约**（关键 seam）：壳与后端之间唯一的耦合是后端 stdout 必须打印一行 `dsh web: http://127.0.0.1:<port>` 前缀的地址（`main.go:65-72`）。一旦主仓库改动这条日志格式，壳会一直等到 30s 超时再退避重启，无法加载窗口——这是脆点。
- **配套仓库链**（README 明示）：Windows 平台支持走两条独立私仓：①`dsh-win-port`（主仓库的 9 个 Windows 补丁系列，壳运行时不依赖）；②`dsh-pty-windows` + `dsh-shell-windows`（Marisa/dshx 插件，由 `dshx install` 挂载到主仓库检出，壳本身不挂载）。
- **环境变量继承**：POSIX 下 source `~/.bashrc`/`~/.zshrc`，主仓库依赖的 API key 等导出变量从用户终端流入后端进程；Windows 直接继承系统/用户环境。
- **无直接 git/代码补丁关系**：壳是纯客户端，主仓库无任何对应改动。

## 亮点与风险
**亮点**
- 单一可执行文件 + 单 `package main`，约 600 行 Go 解决跨平台桌面封装，无 Node 运行时打包，体积极小。
- 守护语义完整：进程组/taskkill 树杀保证无孤儿 node，`main.go:175-185` 显式 `cancel()`+`<-done` 等 supervise 收口才返回，避免 Go 退出抢杀 goroutine 导致清理来不及。
- Wails v3 beta 的 WebView2 异步创建竞态有显式护栏（`webview_ready.go`），是踩过坑后的修复痕迹。
- WSLg 的 WebKit/DRI3 合成 bug 在 `run.sh` 用一整套环境变量绕过，体现实战部署经验。

**风险**
- **stdout 协议脆性**（`main.go:65` `strings.HasPrefix(line, "dsh web: ")`）：后端日志格式任何变动（i18n、加前缀、改 level）都会让壳静默挂死到超时；没有版本握手或健康检查。
- **Wails v3 beta 锁定**（`go.mod:3` `v3.0.0-beta.3`）：beta API 不稳定，`WebviewWindow`/`SystemTray`/`Autostart`/`RegisterHook` 签名可能变；升级需全面回归。
- **macOS 托盘缺口**：`tray.go` 调用 `app.SystemTray.New()`，但 README 与代码只验证 Windows/WSLg；macOS 托盘在 Wails v3 beta 下的行为（菜单栏图标、`ApplicationShouldTerminateAfterLastWindowsClosed` 与 `WindowClosing` hook 的协同）未在仓内有测试或文档覆盖。
- **固定 30s 超时**（`urlTimeout`，`main.go:33`）：慢机或冷启 Node 大仓后端可能误判失败触发重启循环。
- **私有仓库 + gh 认证耦合**：安装器在私有阶段强依赖 `gh` CLI 已登录（`install-desktop-windows.ps1:62-71`），公开前用户体验受影响。
- **`parseCommandLine` 引号规则极简**（`command.go:32-56`）：不处理嵌套/转义引号，复杂命令行必须改用 shell 包装形式，否则解析错误。

## 维护状态
- 浅克隆可见最新提交 `32e58e3 installer: download release assets via gh CLI for the private repo`，作者 LoserFox（昵称），提交时间 2026-08-05（调研当天），表明仓库处于活跃维护。
- README/代码注释双语完善，`justfile` 引用 `dsh-win-port` 的工作流，CI（GitHub Actions）端到端覆盖构建+测试+发布，说明这是 dsh-external 生态中的一等公民项目而非实验品。
- 全仓只有一条历史可见（shallow clone 限制），无法判断长期提交节奏；但 README 明确所有兄弟仓库（dsh-win-port、dsh-pty-windows、dsh-shell-windows）均"private"，与本仓同步演进。

## 备注
- 仓库非空，主分支已就绪，CI 产物可直接下载使用，无需本地 Go 工具链（README「Download」节）。
- 调研覆盖范围：`README.md` 全文 + 全部 `.go` 源码 + `justfile`/`run.sh`/`run-windows.cmd` + `scripts/install-desktop-windows.ps1` + `.github/workflows/build.yml` + `go.mod`。
- 与第一轮调研惯例一致：本摘要不出现作者邮箱/真实姓名，GitHub 用户名（LoserFox）按契约保留。
- 关键文件:行号引用：守护逻辑 `main.go:117-167`；进程组清理 `server_unix.go:60-83`；托盘常驻 `tray.go:88-95`；stdout 协议 `main.go:65`；WebView 竞态护栏 `webview_ready.go:24-49`；命令行解析 `command.go:14-56`。
