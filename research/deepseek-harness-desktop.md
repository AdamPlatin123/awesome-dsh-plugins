# deepseek-harness-desktop 调研摘要

## 一句话定位

把 DeepSeek Harness 整套（cordis 插件树 + `dsh web` HTTP 服务 + Web 前端）打包成
**自包含、不依赖外部浏览器/Node 环境**的 macOS / Linux 桌面应用：Wails v3 壳
（`dsh-shell`）+ Node SEA 单文件后端（`dsh-server`，内嵌 node v26.5.0）+ WebView
内嵌前端三层架构。

## 技术栈与依赖

- **壳层（Go）**：Wails v3 `v3.0.0-beta.3`（`apps/dsh-desktop/go.mod`）；Go 1.26.5；
  间接依赖 adrg/xdg、coder/websocket、godbus/dbus、go-winloader 等 Wails 传递依赖。
- **后端（Node SEA）**：通过 `tsdown` 的 `--build-sea` 把
  `deepseek-harness/apps/cli/lib/types/bin.js` 内联为单文件可执行（`target/sea/bin/dsh`），
  内嵌 Node v26.5.0，启动参数 `--expose-internals`（`tsdown.sea.config.ts`）。
- **构建工具链**：[nub](https://github.com/node-encapsulation/nub)（packageManager，
  `^0.6.0`）、[just](https://github.com/casey/just)、[zx](https://github.com/google/zx)
  `^8.8.5`（写构建脚本）、`tsdown` `^0.22.14`、`sharp` `^0.35.3`（Linux 图标渲染）、
  `@resvg/resvg-js` `^2.6.2`。工具版本由 `mise.toml` 锁定（`just/go/nub` = latest）。
- **运行时资源（外置，非内联）**：cordis 配置树（`apps/cli/config/*.cordis.yml`）、
  `package.json`、`node_modules`（workspace + vendor + npm 闭包，由
  `scripts/sea-materialize.mts` 实体化），均放在 SEA 可执行文件旁的目录中，靠
  `new URL('../config/…', import.meta.url)` 解析。
- **唯一上游补丁**：`node-pty@1.1.0`（`package.json` 的 `patchedDependencies`，
  补丁文件 `deepseek-harness/patches/node-pty@1.1.0.patch`）。
- **平台**：macOS（产物 `target/DSH.app`，图标走 `sips` + `iconutil`）与 Linux
  （产物 `target/linux/DSH/`，图标走 `sharp` 渲染 freedesktop hicolor 多尺寸集）。
  **不支持 Windows**，且不支持交叉编译（SEA 与 Wails cgo WebKitGTK 都要求本机构型）。

## 文件结构概览

```
deepseek-harness-desktop/
├── README.md                 顶层架构说明（三层架构 / 快速开始 / 构建说明 / 环境变量）
├── AGENTS.md                 agent 工作守则：严禁修改 deepseek-harness/ 下文件
├── package.json              workspace 根（workspaces 指向 deepseek-harness/* 子树）
├── mise.toml                 工具链：just/go/nub
├── justfile                  构建入口（sync/dep/build-libs/sea/icon/
│                             bundle-{macos,linux}-app/build-{macos,linux}-app）
├── tsdown.sea.config.ts      SEA 打包配置（entry=cli bin.js，alwaysBundle=/./）
├── go.mod                    顶层 Go module（go 1.26.5，无依赖）
├── nub.lock                  nub 锁文件（502KB，含全量 npm 闭包）
├── apps/
│   └── dsh-desktop/          Wails 壳（Go）
│       ├── main.go           应用装配：环境变量、窗口、信号、退出收口
│       ├── supervise.go      后端守护循环：启动→就绪→退避重启→退出收口
│       ├── server/server.go  SEA 后端进程生命周期（Start/Stop/Exit、URL 解析）
│       ├── landing.html      内嵌启动页 HTML（替代 Wails 默认空白页）
│       ├── go.mod / go.sum   Wails v3 beta.3 + 间接依赖
│       ├── README.md         壳层详细文档（架构 / 代码结构 / 构建 / 环境变量）
│       └── assets/icon.svg   应用图标源（蓝色 SVG，macOS/Linux 渲染源头）
├── scripts/                  TypeScript + zx 构建脚本
│   ├── sea-materialize.mts   SEA 运行时资源实体化（config/package.json/node_modules）
│   ├── make-macos-app.mts    组装 DSH.app（拷贝 SEA 产物、写 Info.plist）
│   ├── make-linux-app.mts    组装 linux/DSH/（freedesktop 图标集 + tar.gz）
│   └── icon.mts              macOS 图标生成（sips→sharp→iconutil）
└── deepseek-harness/         上游 vendored 子目录（已 gitignore，just sync 拉取）
```

## 核心功能与实现要点

1. **三层架构是 dsh 运行机制的必然结果**（`README.md`）：dsh 是跑在 Node 上的 cordis
   插件化 harness，插件在运行时按字符串包名 `import()`、依赖 npm 闭包——只能跑在 Node，
   不能移植到 Go；`dsh web` 又以 HTTP 伺服前端（注入 `__DSH_BOOT__`），WebView 必须
   经 HTTP 加载；Node 不提供原生窗口——所以必须壳 + 后端 + 前端三层。

2. **壳是唯一入口与守护进程**（`apps/dsh-desktop/main.go`、`supervise.go`）：
   - 启动同目录 `dsh-server web --port 0`（端口 OS 分配），从 stdout 解析
     `dsh web: http://127.0.0.1:<port>` 得到实际地址，用 `WebviewWindow.SetURL` 加载
     （`server/server.go:24,173-180`）。
   - 异常退出退避重启：初值 1s、倍增、上限 30s（`supervise.go:13-15,62-72`）。
   - 退出收口：cancel ctx → supervise 终止后端进程组 → main `<-done` 等收口，避免
     Go 进程退出强杀 goroutine 留下孤儿 node（`main.go:153-167`）。

3. **进程组终止不留孤儿**（`server/server.go:118-145`）：`Setpgid: true` 把后端放进
   独立进程组；`Stop()` 先 `SIGTERM`（负 PID 杀整组），5s 宽限期内未退则 `SIGKILL`
   兜底；这是为了对付 SEA 内嵌 node + 未来可能 spawn 的子进程。

4. **stdout 管道必须排空到 EOF**（`server/server.go:181-198`）：解析出 URL 后仍持续
   读 stdout 直到 EOF——后端 agent 运行时会持续写日志，管道缓冲填满会阻塞在 write，
   拖住 SIGTERM handler 里的 dispose（也写 stdout），进而拖住 `Process.Stop` 收口。

5. **Linux 显式钉死 WebKitGTK 硬件加速**（`main.go:118-122`）：`WebviewGpuPolicyAlways`
   ——Wails 注释（issue #2977）称默认可能为 Never、GTK3 分支默认 OnDemand，显式 Always
   保证走 GPU 合成避免 CPU 开销。macOS WKWebView 默认硬件加速无需设置。

6. **用户 shell 环境继承**（`server/server.go:81-115`）：启动后端前按 `$SHELL` source
   `~/.bashrc` 或 `~/.zshrc`，输出重定向到 `/dev/null` 不污染 stdout URL 行；用 `exec`
   保持同一 PID，守护 wait 语义不变；让后端继承用户终端里 export 的 `DEEPSEEK_API_KEY`
   等凭据。

7. **SEA 资源实体化算法**（`scripts/sea-materialize.mts`）：tsdown exe 只内联 JS 依赖，
   两类运行时依赖必须外置——(a) 资源文件 `../config/*.cordis.yml` + `../package.json`，
   代码以 `new URL('../…', import.meta.url)` 从 exe 上一级解析；(b) cordis 插件包
   （base.cordis.yml 声明的上百个插件，loader 运行时按包名 `import()`），需要可解析的
   `node_modules`。脚本遍历 `packages/*/*`（@deepseek-ai/* workspace 包）、`vendor/*`
   （cordis/cosmokit 等）、`apps/web`（dsh-frontend），复制 lib/dist/assets + package.json，
   再从 nub 的 `.store` BFS 复制 npm 依赖闭包。

8. **窗口关闭走自定义收口而非 Wails 委托**（`main.go:131-140`）：实测
   `ApplicationShouldTerminateAfterLastWindowClosed` 在部分环境不生效（窗口关了事件循环
   不退），改为直接监听 `events.Mac.WindowShouldClose` + `events.Common.WindowClosing`
   主动 `quit()`。

## 与 DeepSeek Harness 主仓库的集成点

- **集成方式**：上游 deepseek-harness 作为 vendored 子目录
  （`./deepseek-harness/`，已加 `.gitignore`），由 `just sync` 通过
  `git clone --depth 1 $DEEPSEEK_HARNESS_REPO` 拉取。**严禁修改上游**
  （`AGENTS.md` 明文规定）。
- **SEA 入口（执行缝）**：`deepseek-harness/apps/cli/lib/types/bin.js`
  —— `dsh web` 的 cli 入口（`tsdown.sea.config.ts:13`），打包成 `target/sea/bin/dsh`。
- **运行时资源（外置）**：cordis 配置树 `deepseek-harness/apps/cli/config/*.cordis.yml`、
  `apps/cli/package.json`、`apps/web/dist`（前端 dist，dsh web 经
  `require.resolve('@deepseek-ai/dsh-frontend/dist/index.html')` 解析）。
- **协议契约（壳 ↔ 后端）**：后端就绪时把 `dsh web: http://127.0.0.1:<port>` 打到
  stdout，壳逐行解析此前缀（`server/server.go:24-25`）。这是跨语言进程间通信的
  唯一约定。
- **补丁**：`node-pty@1.1.0`（`package.json` patchedDependencies，
  补丁位于 `deepseek-harness/patches/node-pty@1.1.0.patch`），随上游仓库同步。
- **前端契约**：`dsh web` 经 HTTP 注入 `__DSH_BOOT__` 引导前端，因此 WebView 必须
  走 HTTP 不能直接加载本地 HTML——这是必须走 HTTP 的根因（`README.md`）。
- **构建链上游 `build-libs`**：复刻上游 `pnpm run build`（`tsc -b` + `tsdown` +
  `vite build apps/web`），缺失 `apps/web/dist` 时 `dsh web` 启动即报
  `frontend dist not built` 退出（`justfile` 的 `build-libs` recipe 注释）。
- **环境变量透传**：壳读 `DSH_APP_WORKSPACE`、`DSH_APP_PORT`；后端继承
  `DSH_HOME`、`DEEPSEEK_API_KEY`、`DEEPSEEK_BASE_URL`（也可放调用目录 `.env`）。

## 亮点与风险

**亮点**

- **架构论证极其充分**：根 README 与 dsh-desktop README 用「为什么是三层」详细论证
  了每一层的不可替代性（Node 必需 / HTTP 必需 / 壳必需），把所有架构决策的根因都
  固化在文档里，未来重构有据可依。
- **进程生命周期处理工业级**：进程组终止 + SIGTERM/SIGKILL 兜底 + stdout 排空防阻塞 +
  信号捕获走同一收口路径 + main 等守护协程收口才退——每一处都针对「不留孤儿 node」
  这个核心失败模式，且每处都有详细注释解释为什么（`server/server.go`、`main.go`）。
- **server 子包与 Wails 解耦**：注释明说「不依赖 Wails，可独立测试」
  （`server/server.go:1-5`），壳的守护逻辑可以单测。
- **跨平台图标渲染策略分流**：macOS 用 `sips`（黑色 fill 可靠，蓝色有缺陷）+
  `sharp`（缩放合成）+ `iconutil` 三段链路；Linux 用 `sharp`（libvips + librsvg）
  单段链路渲染 hicolor 9 尺寸集；选型有据可循（`scripts/icon.mts:1-15`、
  `scripts/make-linux-app.mts:32-46`）。
- **SEA 资源实体化算法**（`scripts/sea-materialize.mts`）：清晰处理了 tsdown exe
  无法内联的运行时依赖（cordis 插件运行时 `import()`），分 workspace / vendor /
  frontend / npm 闭包四类实体复制。

**风险**

- **极新仓库，仅 2 个 commit**（`bf8ffc4` Morlay「fix: sync should delete before clone」
  与 `18e992e`「Screen Context: single combined GIF」，均 2026-08-05），尚未稳定，
  构建链路大概率还有变更（`package.json` version 仅 `0.0.1`）。
- **强依赖未发布的工具链**：Node v26.5.0、Go 1.26.5、Wails v3 beta.3、nub `^0.6.0`、
  tsdown `^0.22.14`、typescript `^6.x`——全部是 bleeding edge，构建复现环境脆弱。
- **不支持 Windows，且不支持交叉编译**：Linux 产物必须在 Linux 主机执行（SEA
  `--build-sea` + Wails cgo WebKitGTK 都不能交叉），CI/分发链路复杂；Windows 用户
  需要另走 `dsh-desktop` 仓库（见下）。
- **资源实体化算法遍历 `packages/*/*`、`vendor/*`**（`sea-materialize.mts:60-87`）：
  硬编码了上游目录结构，上游若重组 monorepo 布局，脚本静默漏拷。
- **SEA 内嵌 node 的 `__DSH_BOOT__` 注入 + `new URL('../config/…', import.meta.url)`
  资源解析**：依赖 Node SEA 对 `import.meta.url` 的具体行为，Node SEA 升级可能破坏。
- **README 把 dsh 称作「跑在 node 上的 cordis 插件化 harness」并提到「上游源代码在
  deepseek-harness 下，我们将为 deepseek-harness 打包为 desktop app」**——这暗示本仓库
  是 dsh-external org 的官方桌面分发渠道，但与同 org 的 `dsh-desktop` 并存且分工模糊
  （见维护状态/备注），有重复维护风险。
- **`workspaces` 字段指向 `deepseek-harness/vendor/*`、`packages/*/*`、`apps/*`、
  `website`**（`package.json:5-10`）：本仓库根 package.json 实际上「接管」了上游的
  workspace，nub install 会在本仓库根装上游全部依赖——上游版本漂移会直接影响本仓库
  构建可重复性。

## 维护状态

- **创建时间**：2026-08-05 01:33:52 UTC（GitHub API `created_at`），晚于
  `dsh-desktop` 约 2.5 小时。
- **提交历史**：仅 2 个 commit，作者 Morlay（GitHub 用户名）；最新提交
  2026-08-05 12:45 +0800。
- **活跃度**：4 stars、0 forks、未归档、不空、有 4 个 topics
  （`deekseek-harness`/`desktop-app`/`linux`/`macos`，注意 `deekseek` 拼写错误）。
- **CI**：本仓库根未见 `.github/workflows`（仅有 `.gitignore` / `AGENTS.md`）——
  目前没有自动化构建发布流，全部本地 `just build-{macos,linux}-app` 手工产出。
- **仓库体积**：GitHub 报 153 KB（不含 vendored `deepseek-harness/`，因后者已 gitignore）。
- **结论**：处于早期实验/原型阶段，架构设计成熟但产物链路尚未固化。

## 备注

### 与 `dsh-external/dsh-desktop` 的关系（**这是两个不同的仓库**）

dsh-external org 同时存在两个高度相关但定位不同的桌面仓库：

| 维度 | `dsh-desktop` | `deepseek-harness-desktop`（本仓库） |
|---|---|---|
| 创建时间 | 2026-08-04 22:55:48 UTC（早 2.5h） | 2026-08-05 01:33:52 UTC |
| 作者 | LoserFox | Morlay |
| GitHub 体积 | 54 KB | 153 KB |
| 主语言 | Go | TypeScript（构建脚本；壳仍是 Go） |
| 描述 | 无 | `DSH 桌面应用` |
| Stars | 0 | 4 |
| 平台 | **Windows**（POSIX 也兼容） | **macOS + Linux**（无 Windows） |
| 后端来源 | 用户自备：从 PATH 启动 `dsh web --port 0`（依赖用户装好 dsh/Node） | **自包含**：SEA 内嵌 node v26.5.0，一切随 app 分发 |
| 关键变量 | `DSH_WEB_CMD`（可覆盖整条命令行） | `DSH_APP_WORKSPACE` / `DSH_APP_PORT` |
| 托盘常驻 | **有**（`tray.go`：关窗隐藏到托盘、开机自启、退出菜单） | **无**（关窗即走收口退出） |
| Windows 安装器 | 有（`scripts/install-desktop-windows.ps1`，含 gh CLI 下载 release 资产） | 无 |
| 单测 | 有（`command_test.go`） | 无（但 `server/` 子包注释自陈可独立测试） |
| CI | 有 `.github/workflows`（push 到 `v*` tag 出 release） | 无 |
| 上游关系 | 与 `dsh-win-port` patch series 平行，运行时不依赖 | 把上游 vendored 整个 `just sync` 进来打包 |
| 模块路径 | `module dsh-desktop` | `module github.com/dsh-external/deepseek-harness-desktop` |
| 双语 README | 有（`README.md` + `README.zh.md`） | 仅中文 `README.md` |

**共享的契约**（同源演化的证据）：

- 同样用 Wails v3 `v3.0.0-beta.3` + `WebviewWindow` 内嵌加载。
- 同样的进程间协议：壳从后端 stdout 解析 `dsh web: http://127.0.0.1:<port>`。
- 同样的退避重启策略：1s 起步、倍增、30s 上限。
- 同名启动页 `landing.html`（DeepSeek 蓝色 logo + 三点脉冲动画，内容几乎逐字一致）。
- 同名壳可执行 `dsh-shell`、同名的窗口标题、同样的最小窗口尺寸 800×600 / 默认 1280×800。

**定位差异**：

- `dsh-desktop` = **瘦壳 / 开发者向**：仅一个 `dsh-shell.exe`，依赖用户已装 dsh/Node，
  走 PATH 拉起后端，主打 Windows + 托盘常驻 + 一键安装器；适合已经搭好 dsh 环境的人。
- `deepseek-harness-desktop` = **胖壳 / 终端用户向**：内嵌 Node v26.5.0 + 全套 cordis
  插件 + 前端 dist，零环境依赖一键分发；主打 macOS/Linux，**无 Windows 无托盘**，
  走 `DSH.app` / `DSH.tar.gz` 形态分发。

两者目前**并存且不互相 import**，分别由不同作者维护、覆盖不同平台，可视为
dsh-external org 的「双轨桌面分发方案」。功能重叠（壳逻辑、URL 解析、退避重启）
但代码并未共享，存在重复维护风险。本仓库（`deepseek-harness-desktop`）是更新、
更被推广（4 stars、有 topics、有 description）的那一个。
