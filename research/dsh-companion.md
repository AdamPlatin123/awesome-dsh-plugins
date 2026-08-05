# dsh-companion 调研摘要

## 一句话定位
**Cetus 的 DeepSeek Harness 发行版**——一个基于 Tauri 2 + Next.js 的 macOS 常驻桌面助手外壳，把 `dsh web` 宿主包成一个全局可唤起、支持定时自动化、屏幕感知、看板审阅的桌面 agent；会话引擎完全由 dsh 驱动，Cetus 提供 dsh 之外的整个"助手层"。源自开源项目 `drewnekota/cetus`（README.md:1 `Cetus · make dsh your desktop companion`），本仓库是其在 `dsh-external` 组织下的 DSH 专属分叉。

## 技术栈与依赖
- **外壳**：Tauri 2（Rust 后端，productName `Cetus`，identifier `dev.dsh.companion`，版本 0.3.52）
- **前端**：Next.js 16.2.6 静态导出 + React 19 + TypeScript 5.7；UI 用 Tailwind 4 / radix-ui / shadcn；状态用 zustand；终端用 `@xterm/xterm`；Markdown 用 `react-markdown` + `rehype-katex` + `remark-gfm/math`
- **包管理**：pnpm 10.27 + bun（构建 pi sidecar，本发行版已移除 pi runtime）
- **会话引擎**：DeepSeek Harness（`dsh` CLI 在 PATH 上，默认模型 deepseek-v4-flash）
- **dsh 桥**：cordis 4 插件 `@dsh-external/dsh-companion-bridge`（peerDeps：`@deepseek-ai/dsh-host-apiproxy`、`dsh-tools`、`dsh-system-prompt`），schema 用 schemastery
- **自带插件**：`dsh-vision`（view_image，OpenAI 兼容 VLM 桥）、`dsh-artifact`（send_artifact 文件交付）
- **License**：MIT
- 仓库私有、组织 `dsh-external`、2026-08-05 创建并当天推送（`gh repo view` 实测）

## 文件结构概览
```
dsh-companion/
├── README.md / README.zh-CN.md      # 英文=DSH 发行版说明；中文=上游 Cetus 通用说明
├── package.json                      # name "cetus"，pnpm scripts: dev/build/tauri/app
├── src/                              # Next.js 前端
│   ├── app/page.tsx (141KB)          # 主聊天 UI
│   ├── lib/tauri.ts (31KB)           # 全部 Tauri 命令绑定（含 dsh_plugins_* / dsh bridge）
│   ├── lib/types.ts (40KB)           # BackendId 含 "dsh"；CliAgentSettings 含 dshEnabled
│   └── components/                   # chat / quick / settings / plugins / screen-history 等
├── src-tauri/
│   ├── tauri.conf.json               # 5 个窗口：main / quick / snip / voice / meeting
│   ├── src/                          # 60+ Rust 模块（commands.rs 102KB、store.rs 77KB 等）
│   │   ├── cli_backend.rs            # CLI 后端编排；spawn_dsh_session 在 cetus-bridge 里
│   │   └── plugin_market.rs          # 读写 ~/.dsh/config.yaml，git 安装外部插件
│   └── cetus-bridge/                 # 产品无关的 Rust crate（host/extension 桥运行时）
│       ├── src/cli_agent.rs (428KB)  # spawn_dsh_session、dsh web 宿主生命周期、EventTranslator
│       └── examples/minimal_host.rs  # 最小集成示例
├── dsh-bridge/                       #  cordis 插件源码（编译产物 lib/ 随仓库分发）
│   ├── package.json                  # @dsh-external/dsh-companion-bridge
│   ├── src/index.ts                  # HTTP + SSE 网关 + 注册 create_automation 等工具
│   └── scripts/build.sh              # 用 dsh 检出里的 tsc 编译，符号链接到 vendored 包
├── packages/cetus-bridge-protocol/   # @cetus/bridge-protocol TS 包：HOST_TUNNELS/callHost
├── plugins/
│   ├── dsh-vision/                   # view_image 工具（dsh.plugin.json 声明 contributes.tools）
│   └── dsh-artifact/                 # send_artifact 工具
└── scripts/                          # 打包/签名/发布脚本（build-release.sh、macos-sign.sh 等）
```

## 核心功能与实现要点
1. **统一桌面壳，多 runtime 选择器**：UI 把 `dsh`、`claude-code`、`codex`、`opencode`、`grok`、`kimi` 抹成统一的 RuntimeEvent 事件流，dsh 默认开启（`src/lib/runtime-settings.ts:20` `dshEnabled:true`、`runtimeOrder:["dsh",...]`）；pi runtime 已从本发行版移除（`runtime-settings.ts:44` 注释）。
2. **dsh 会话通过共享宿主 + HTTP/SSE 桥驱动**：每个对话对应一个 dsh session；事件经 `EventTranslator`（`CliBackend::Dsh`）翻译为前端 `chatReducer` 已消费的 PiEvent 流（`src-tauri/cetus-bridge/src/cli_agent.rs:9420` `EventTranslator::new(CliBackend::Dsh)`）。整个 app 生命周期共享一个 `dsh web` 进程，PID 存在 `static DSH_HOST_PID`（cli_agent.rs:8859），退出时 SIGTERM 整个进程组。
3. **dsh-bridge 网关插件**：`dsh-bridge/src/index.ts` 起一个 127.0.0.1 HTTP 服务，三个端点：`GET /events`（SSE，把 `apiProxy.events.mux` 和 `.host` 双流逐帧转发）、`POST /call`（按 `domain.method` 反射调用 apiProxy，`path:"respond"` 走问答/审批）、`POST /rpc-result`（companion 反向 RPC 应答）。token 鉴权（`x-companion-token` header 或 `?token=`）；端口/令牌从 `DSH_COMPANION_BRIDGE_PORT/TOKEN` 读，shell 启动宿主时注入。同时 `inject:['apiProxy','tools','systemPrompt']` 注册 `create_automation`、`list_automations`、`search_screen_history`、`screen_timeline` 四个工具，并在系统提示词 order=118 注入"Cetus desktop app"小节（dsh-bridge/src/index.ts 末段）。
4. **全局唤起 / 快捷回复 / 屏幕感知 / 会议记忆**：双击左右 ⌘ 触发 Quick Launcher（`src-tauri/src/quick.rs` 59KB）；任意聊天界面双击右 ⌥ 触发读屏起草回复（`quick_reply.rs`，对 dsh 后端走 `spawn_dsh_session`，quick_reply.rs:185）；Screen Context 端上 Apple Vision OCR（`ocr.rs`、`capture.rs`）；会议记忆走系统 Speech 框架设备端转写（`meeting.rs`）。这些都通过 dsh-bridge 反向 RPC（`companionCall`）回灌给桌面壳。
5. **定时自动化**：cron / interval / daily / once 四种调度（`src-tauri/src/automation.rs` + `scheduler.rs`），agent 在对话里调用 `create_automation` 工具即可建任务；模型推荐用 v4-flash，"高频、碎片、即时"场景（README.md 中段论述）。
6. **插件市场**：`plugin_market.rs` 读写 `~/.dsh/config.yaml`（与 Marisa 的 `dshx` 同一挂载面，注释明确指出 plugin_market.rs:2-5），git 安装时克隆到 dsh 检出的 `.external-plugins/`，按 peerDependencies 符号链接宿主包（注释称"works around marisa#2 until it is fixed upstream"）。前端 `dshPluginsList` / `dshPluginSetEnabled` / `dshPluginInstall`（`src/lib/tauri.ts:431-440`）。
7. **可复用 bridge 包**：`src-tauri/cetus-bridge` Rust crate 与 `packages/cetus-bridge-protocol` TS 包都标注"产品无关、无 Cetus/DeepSeek 专属代码"，其他 agent host 可复用，附 `examples/minimal_host.rs`。
8. **自定义 DeepSeek base URL**：设置项把所有 DeepSeek 流量（agent 本体 + 标题/dream/技能复盘/会议纪要）改走用户自定的 OpenAI 兼容地址（`src/lib/i18n/messages/settings.ts:159-161`，对应 Tauri 命令 `get/set_deepseek_base_url_cmd`）。

## 与 DeepSeek Harness 主仓库的集成点
**强集成（直接消费 dsh 内部包/协议）**：
- **协议层 seam**：`dsh-bridge/` 是一个标准 cordis 插件，peerDependencies 限定 `@deepseek-ai/dsh-host-apiproxy ^0.0.1`、`@deepseek-ai/dsh-system-prompt ^0.0.1`、`@deepseek-ai/dsh-tools ^0.0.1`、`cordis ^4.0.0-rc.7`；运行时 `inject ['apiProxy','tools','systemPrompt']` 直接复用 dsh host 的 ApiProxy、ToolRegistry、SystemPrompt 三大服务（dsh-bridge/package.json、dsh-bridge/src/index.ts:30）。构建脚本 `dsh-bridge/scripts/build.sh` 显式要求 `dsh` 在 PATH，把 dsh 检出里的 `packages/host/apiproxy`、`packages/core/*`、`packages/llm/llm`、`vendor/cordis|cosmokit|schemastery` 全部符号链接进插件 node_modules，用检出里的 tsc 编译——**插件版本与 dsh 检出版本完全锁死**。
- **进程编排 seam**：`spawn_dsh_session`（cli_agent.rs:9336）守护一个共享的 `dsh web` 宿主；首次启动调用 `dsh_ensure_bridge_mounted`（cli_agent.rs:8967），向 `~/.dsh/config.yaml` 追加一个标记块挂载 `dsh-companion-bridge` 与自带插件（dsh-vision / dsh-artifact），用户已有同名挂载优先；就绪探测 90s 超时（cli_agent.rs:9081）。
- **配置覆盖层 seam**：`plugin_market.rs` 与 `dsh_ensure_bridge_mounted` 都直接读写 `~/.dsh/config.yaml`——这是 dsh 官方的个人覆盖层，与 `dshx`（Marisa 仓）共管同一文件，存在多写入者竞争风险。
- **运行时注册**：`CliBackend::Dsh` 在 cetus-bridge 的 cli_agent 枚举里和 claude-code/codex/opencode/grok/kimi 平级（cli_agent.rs:52、63、76），dsh 在发行版里被设为默认且唯一开启的 runtime。
- **插件契约**：自带两个插件 `dsh-vision`、`dsh-artifact` 都通过 `dsh.plugin.json` 的 `engines.dsh >= 0.0.1` + `contributes.tools`（view_image / send_artifact）声明，遵循 dsh 插件规范。

**结论**：不是独立工具，而是 dsh 的官方桌面壳；与主仓的耦合面是 (a) ApiProxy/cordis 插件协议、(b) `dsh web` 子进程 + 进程组、(c) `~/.dsh/config.yaml` 个人覆盖层、(d) dsh 插件规范。

## 亮点与风险
- **亮点**
  - 把 dsh 从终端搬到桌面：全局热键唤起、定时自动化、看板审阅、屏幕记忆、会议纪要、快捷回复，端上 OCR/ASR 全本地（README.md 列出的八大能力均有对应实现模块）。
  - 桥以 127.0.0.1 HTTP + SSE 暴露 ApiProxy，让非 Node 进程（Rust/Tauri）也能驱动 dsh 会话；token 鉴权 + 1MB body 上限 + 双流（mux/host）SSE 设计清晰（dsh-bridge/src/index.ts:1-300）。
  - 产品逻辑与 dsh host 解耦：`cetus-bridge` crate 和 `@cetus/bridge-protocol` 都剥离了 Cetus/DeepSeek 专属类型，附 `examples/minimal_host.rs`，可被其他 agent host 复用（src-tauri/cetus-bridge/README.md）。
- **风险**
  - **构建期与 dsh 检出强绑定**：`dsh-bridge/scripts/build.sh` 必须能定位 dsh 安装、必须能符号链接到 vendored 包；dsh 内部包路径（如 `packages/host/apiproxy`）一旦改名/迁移，插件立刻编译失败。
  - **`~/.dsh/config.yaml` 多写入者**：本插件、`dshx`（Marisa）、用户手动都可能改这个文件；`dsh_ensure_bridge_mounted` 用 `contains("dsh-companion-bridge")` 字符串去重（cli_agent.rs:8975），并不解析 YAML，已有同名挂载的格式差异会导致重复挂载。
  - **巨型单文件**：`src-tauri/cetus-bridge/src/cli_agent.rs` 高达 428KB（六种 backend 全在一个文件里），`commands.rs` 102KB、`store.rs` 77KB——长期维护成本高。
  - **平台单一**：仅 macOS 13+ Apple Silicon 实测可用；Screen Context、会议记忆、Apple Vision OCR、System Speech 都强依赖 macOS 私有 API（`tauri.conf.json` 开了 `macOSPrivateApi:true`）。
  - **默认 `bypass_approvals:true`**：headless CLI runtime 默认开 `--dangerously-skip-permissions`（cli_backend.rs:33-40 注释），用户不察时风险较高。
  - **依赖外部 VLM**：`dsh-vision` 默认走智谱免费档（README.md "视觉"段），免费档可用性/速率/隐私是潜在隐患。

## 维护状态
- **活跃**：仓库 2026-08-05 创建并当天推送（实测 `gh repo view` `pushedAt 2026-08-05T11:09:55Z`），README 自述"聊天主链路、模型与 effort 调优、Quick Launcher、快捷回复、定时自动化、插件管理、文件交付与视觉插件均已接通并实测；进行中：打包分发（signed .app）、问答卡多问题体验打磨"。
- **上游来源**：fork 自 `drewnekota/cetus`（README 顶部徽章仍指向 `drewnekota/cetus/releases/latest`），版本号沿用上游 0.3.52。
- **私有仓**：`dsh-external` 组织下，0 stars / 0 forks（实测），可见性 private。
- **License**：MIT，与上游 pi/dsh 一致。

## 备注
- 调研产物：本地浅克隆 `/tmp/dsh-ext-research2/dsh-companion/`（`git clone --depth 1`，单 commit `e08f9f4`）。
- dsh-bridge 编译产物 `dsh-bridge/lib/index.js` 已随仓库分发（13.7KB），桌面壳默认走它（可被 `DSH_COMPANION_BRIDGE_LIB` 覆盖，README.md "运行"段）。
- 与同批调研仓的关联：本仓多次引用 `dsh-vision`、`dsh-artifact`（同 org 下的独立仓），并通过 `dsh_plugin_install` 支持从任意 git URL 装 dsh 插件——是 dsh-external 生态里"桌面入口 + 插件消费者"的角色。
- 脱敏：摘要中未出现作者邮箱/真实姓名；GitHub 用户名 `drewnekota`、`dsh-external` 为可公开标识符。
