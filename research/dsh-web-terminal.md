# dsh-web-terminal 调研摘要

## 一句话定位
`@dsh-external/dsh-web-terminal` 是 DeepSeek Harness Web UI 的非官方插件，把 xterm.js + node-pty 驱动的交互式 shell 以「底部嵌入式 dock」的形式挂在居中会话栏的末尾，展开时挤压会话流而非覆盖它，零核心改动。

## 技术栈与依赖
- 语言/构建：TypeScript（`strict` + `exactOptionalPropertyTypes` + `noUncheckedIndexedAccess`），`tsdown` 打包，`vitest` 测试。
- 服务端：Node.js（ESM，target `es2024`），`node-pty` 1.1+、`ws` 8.21+、`cordis` ^4.0.0-rc.7（均为 `peerDependencies`，运行时从 harness 依赖闭包解析）。
- 客户端：React 18、`@xterm/xterm` v6、`@xterm/addon-fit`、`@deepseek-ai/dsh-client-ui-primitives`（仅取图标）、lightningcss 编译 CSS Modules。
- 包元数据关键字段：`dshClient: { inject: ['@deepseek-ai/dsh-client-runtime'], platform: 'web' }`、`exports: { '.': './lib/index.js', './client': './lib/client.js' }`、`files: ['lib']`（构建产物 `lib/index.js` 与 `lib/client.js` 随源码提交）。
- License：BSD-3-Clause；维护者署名 `zevorn`。关联 issue：`dsh-external/issues#111`。

## 文件结构概览
```
dsh-web-terminal/
├── src/
│   ├── index.ts                  # 服务端 host half：注册 WS upgrade 路由
│   ├── protocol.ts               # 线协议（client/server 消息、上限、编解码）
│   ├── pty-session.ts            # 一连接↔一 PTY 会话生命周期
│   ├── shell.ts                  # 跨平台 shell 解析（$SHELL / COMSPEC + 兜底）
│   └── client/
│       ├── index.tsx             # 浏览器 half：mount dock + trigger、MutationObserver 重排
│       ├── TerminalPanel.tsx     # dock 外壳（tab 栏、resize 拖拽、Ctrl+` 切换）
│       ├── TerminalView.tsx      # 单 tab：xterm 实例 + socket + fit/resize
│       ├── terminal-socket.ts    # 浏览器 WS 客户端（connect/ready/closed）
│       ├── terminal-theme.ts     # 从 --dsw-* token 解析 xterm 主题
│       ├── panel-store.ts        # dock 状态机（reducer + 持久化）
│       ├── TerminalTriggers.tsx  # 右上角 shell 触发按钮
│       └── terminal-panel.module.css
├── tests/                        # 8 个 spec，约 51 个用例（README 自陈）
├── lib/{index.js, client.js}     # 提交的构建产物
├── tsdown.config.ts              # 自包含双产物打包配置
├── package.json / pnpm-lock.yaml / pnpm-workspace.yaml
├── README.md / INSTALL.md / LICENSE
└── scripts/ensure-spawn-helper.mjs  # postinstall：修 node-pty macOS spawn-helper 执行位
```

## 核心功能与实现要点
1. **双半插件架构**：服务端 `src/index.ts:43-86` 通过 `ctx.httpServer.registerUpgrade('/dsh-web-terminal/ws')` 注册 WebSocket upgrade 路由（`@deepseek-ai/dsh-host-webserver` 仅作类型增强）；浏览器半 `src/client/index.tsx` 通过 `window.__ModuleLoader__.load({ id, factory })` 注入，平台模块（react/cordis/ui-primitives）走 loader 冻结模块表外置，其余全部内联。
2. **一连接一 PTY 会话**：`src/pty-session.ts` 的 `TerminalSession` 是显式状态机（`idle → running → exited/disposed`），spawn 在 `start` 帧，input/resize/kill 转发，socket 关闭即 `dispose()` 杀进程；node-pty 以 `PtySpawn` 接口注入便于测试用 fake 替身。
3. **协议级防御**：`src/protocol.ts:88-145` 的 `parseClientFrame` 强制帧上限 `MAX_FRAME_BYTES = 128 KiB`、输入上限 `MAX_INPUT_BYTES = 64 KiB`、终端尺寸上限 `1000×500`，二进制/非对象/未知 type/超大帧 → 抛错 → `src/index.ts:60-66` 回 `error` 帧并以 `ws.close(1008, 'protocol violation')` 关连接。
4. **嵌入式布局（核心卖点）**：dock 渲染为居中会话栏 `[data-phase]` 根的父级（AppFrame `centerCol`）的最后一个 flex 子，展开用页内空间向上顶；`src/client/index.tsx:55-91` 的 `MutationObserver` 在用户新建会话导致宿主插入新会话根时把已有 dock 移回末尾位置，**不重挂载 React 树、不重连 shell**。
5. **主题同步**：`src/client/terminal-theme.ts:60-90` 从 `<body>` 的计算样式读 `--dsw-alias-bg-layer-1`/`--dsw-alias-label-primary`/`--dsw-alias-interactive-bg-active` 等 alias token，按背景亮度（luminance > 140）在两套预置 ANSI 16 色板间切换；`TerminalView.tsx` 用 `MutationObserver` 监听 `body[data-ds-dark-theme]/style/class` 与 `<html>` 的 `style/class` 实时刷新。
6. **跨平台 shell 解析**：`src/shell.ts:33-55` 优先 `$SHELL`（unix）/`COMSPEC`（win），兜底 darwin→`/bin/zsh`、linux→`/bin/bash`、win→`powershell.exe -NoLogo`；客户端 `start` 帧可传 `shell`/`cwd` 覆盖，但不存在的绝对路径或非目录 cwd 一律回退到默认，**永不让陈旧偏好导致 session 不可用**。
7. **状态持久化与迁移**：`src/client/panel-store.ts:108-135` 把 `collapsed/size` 写 `localStorage`（key `dsh-external.dsh-web-terminal`），并兼容历史格式（0.1.0 `{open,dock,size}`、0.3.0 per-orientation `.bottom` key）；tab 列表不持久化（活会话无法跨刷新存活）。
8. **首屏整洁**：服务端在 PTY env 里强制 `PROMPT_EOL_MARK=''`（去 zsh 反视频 `%`）、`BASH_SILENCE_DEPRECATION_WARNING=1`（去 macOS bash 迁移横幅）——见 `src/index.ts:48-58`。

## 与 DeepSeek Harness 主仓库的集成点
- **HTTP/WS 路由**：`ctx.httpServer.registerUpgrade({ path: '/dsh-web-terminal/ws', ... })` —— 依赖 `@deepseek-ai/dsh-host-webserver` 暴露的 upgrade 注册能力，**要求 DSH 0804+ 构建快照**（0803 及更早缺此 API，INSTALL.md 明确声明）。
- **客户端挂载点**：通过 DOM 选择器 `[data-phase]` 的父元素（AppFrame 居中栏）外挂渲染，不修改任何核心 React 树；图标复用 `@deepseek-ai/dsh-client-ui-primitives` 的 `IconPanelLeftOutline16` 旋转 90°。
- **插件注册**：用户在 `~/.dsh/config.yaml` 加 `- insert: [{ id: dsh-web-terminal, name: '@dsh-external/dsh-web-terminal' }]`，然后 `pnpm add -w link:...` 进 harness 依赖图，重启 `dsh web` 生效。
- **主题协议**：消费宿主的 `--dsw-*` 设计 token 体系（`body[data-ds-dark-theme]` + body inline style 投影 alias token）。
- **运行时依赖闭包**：`node-pty@1.1.0` 与 `ws@8.21.0` 不在本包 `node_modules`，从 harness 主树解析（官方树已含）；`cordis` 走 `link:../.dsh/source/current/vendor/cordis`。
- **打包契约**：`tsdown.config.ts` 内联了官方 `packages/client/tsdown.client.ts`（0805 快照）的预设：`window.__ModuleLoader__.load({ id, factory: (require) => {...} })` 包裹 + CSS Modules 经 lightningcss 编译为 `<style data-plugin>` 自动注入。

## 亮点与风险（附文件:行号）
- **亮点｜协议安全边界清晰**：`src/protocol.ts:88-145` + `src/index.ts:60-66`，所有越界/畸形输入都转为 `error` 帧 + 1008 关闭，可恢复错误（如 `input before start`）只发 `error` 不关连接。
- **亮点｜跨新会话不重连 shell**：`src/client/index.tsx:55-91`，`ensureDockAtEnd` 重排而非重挂载，保护已建立的 PTY 会话。
- **亮点｜完整测试覆盖**：8 个 spec、约 51 用例覆盖协议解析、PTY 会话状态机、shell 解析、主题、socket、reducer、客户端布局、产物包含 xterm 样式；`node-pty` 通过依赖注入做 fake 测试（`tests/pty-session.spec.ts`）。
- **风险｜WS 端点无鉴权**：`src/index.ts:72-80` 注册的 upgrade 路由与宿主其他 `ctx.httpServer` 路由一致不做额外认证；shell 以 `dsh web` 进程身份运行、**不沙箱、不清洗 env**。README Security 节自陈：仅因 `dsh web` 默认绑 `127.0.0.1` 才安全，若暴露到网络则终端端点同样可达。
- **风险｜会话不持久**：`README.md` Known limitations —— `dsh web` 重启会断所有 WS、杀全部 PTY；折叠态也不保活。
- **风险｜强耦合特定 DSH 快照**：要求 0804+ 且 `~/.dsh/source/current` 指向含 `lib/` 的构建快照（`devDependencies` 全部 `link:../.dsh/source/current/...`），早期快照无法构建/运行。
- **风险｜可见历史仅 1 个 squash commit**（`73cc29d fix: stabilize embedded terminal layout and docs`，2026-08-05），但代码里存在 0.1/0.2/0.3 的存储迁移逻辑（`src/client/panel-store.ts:34,38`），说明公开发布前有内部版本演进史未对外暴露。

## 维护状态
- 仓库当前 `--depth 1` 可见 1 个 commit（2026-08-05），`package.json` 版本 `0.1.0`，`private: true`。
- 测试、typecheck、build、postinstall 脚本齐全；`lib/` 产物随源码提交（即装即用、无需 build）。
- 关联 `dsh-external/issues#111`，处于「首批公开发布」阶段，活跃维护中。

## 备注
- 与同批其他仓库相比，本仓库是**最完整的「双半客户端插件」范本**：服务端仅一个 upgrade 路由 + 一个 PTY 会话类，客户端通过 DOM 外挂 + MutationObserver 自举入宿主布局，不改动任何核心文件，可作为撰写「DSH 第三方插件开发指南」的参考实例。
- 安装路径见 `/tmp/dsh-ext-research2/dsh-web-terminal/INSTALL.md`；README 截图位于 `/tmp/dsh-ext-research2/dsh-web-terminal/docs/term-*.png`。
- 调研产物：`/tmp/dsh-ext-research2/dsh-web-terminal/`（克隆）、本摘要 `/tmp/dsh-ext-research2/dsh-web-terminal.md`。
