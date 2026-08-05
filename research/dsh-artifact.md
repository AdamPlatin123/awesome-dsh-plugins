# dsh-external/dsh-artifact

## 一句话定位
dsh 的**文件交付协议插件**：注册一个 `send_artifact(path, caption?)` 工具，让模型把写完的文件通过 `tool/result` 事件的标准 `meta` 字段正式交付给客户端——任何消费 `events.mux` 的前端（桌面壳、IM 机器人、Web、headless）都能拿到结构化描述子并各自渲染，不引入自定义传输通道。

## 技术栈与依赖
- **语言/构建**：TypeScript 5.9（`target: ES2024`，`moduleResolution: bundler`，`strict`），编译产物 `lib/index.js` + `lib/types/*.d.ts` 入库。
- **运行时**：Node.js（`node:fs/promises`、`node:path`、`node:os`），ESM（`"type": "module"`）。
- **插件框架**：[Cordis](https://cordis.js.org/) 4.0.0-rc.7（`ctx.plugin()`、`ctx.effect()`、`inject: ['tools', 'systemPrompt']`）。
- **dsh 宿主 peer 依赖**：`@deepseek-ai/dsh-tools ^0.0.1`、`@deepseek-ai/dsh-system-prompt ^0.0.1`，均以软链接方式接到 dsh 主 checkout（`packages/core/tools` 等）。
- **测试**：Vitest（4 个 spec，真实 Cordis 组合 + 临时文件，无 mock 桩）。
- **License**：BSD-3-Clause；`engines.dsh >= 0.0.1`。

## 文件结构概览
```
dsh-artifact/
├── src/index.ts          # 唯一源文件（~150 LOC）：describeArtifact + apply()
├── lib/index.js          # tsc 编译产物（已入库，运行时加载点）
├── lib/types/index.d.ts  # 类型声明（入库）
├── tests/plugin.spec.ts  # 4 个集成 spec
├── scripts/build.sh      # 链接宿主依赖 + 调用 dsh 检出内的 tsc
├── dsh.plugin.json       # 插件清单（id/version/contributes）
├── package.json          # @dsh-external/dsh-artifact 0.1.0
├── tsconfig.json
└── README.md             # 安装/接入指南
```

## 核心功能与实现要点
1. **`send_artifact` 工具注册**（`src/index.ts:80-130`）：通过 `ctx.tools.register(defineTool({...}))` 注册；参数 `path`（必填，必须绝对路径）+ `caption`（可选）；`isConcurrencySafe: () => true` 表示可与其他工具并发。
2. **结构化描述子 `ArtifactDescriptor`**（`src/index.ts:24-33`）：字段 `kind: 'artifact'`（判别字段）、`artifactKind`（image/video/audio/pdf/markdown/html/text/other）、`path`、`name`、`mimeType`、`caption`、`sizeBytes`。
3. **扩展名 → 类型分类表 `KIND_BY_EXT`**（`src/index.ts:35-60`）：覆盖图片/视频/音频/pdf/常见文本格式；未知扩展名安全回退到 `other` + `application/octet-stream`。**不读 magic bytes**，仅按扩展名判定。
4. **纯函数 `describeArtifact()`**（`src/index.ts:63-73`）：导出给测试与客户端作者复用，是分类与描述子构造的单一来源。
5. **校验与执行**（`src/index.ts:104-117`）：`execute` 阶段强制绝对路径、`stat` 文件存在性、拒绝非普通文件（目录/设备节点），并把真实 size 写入 `sizeCache` 供 meta 投影读取。
6. **meta 投影**（`src/index.ts:90-98`）：`output.presentationMeta` 是 args 的纯函数（lazy 读 `sizeCache`），把描述子塞进 `tool/result` 的呈现元数据——这是与所有客户端的"协议契约"。
7. **系统提示注入**（`src/index.ts:75-77` + `PROMPT_TEXT`）：以 `order: 117` 注入 `tool:dsh-artifact` 段，教模型"产出文件后调用 `send_artifact` 交付；只写盘不交付用户看不到；终稿交付一次，不发中间产物"。
8. **构建链路**（`scripts/build.sh`）：从 `command -v dsh` 反查主 checkout，把 `cordis/cosmokit/schemastery` 与 `@deepseek-ai/dsh-{llm,scope,session,system-prompt,tools,brand}` 软链到本地 `node_modules`，再调用宿主 `tsc` 编译——保证类型检查与运行时 dsh 同源。

## 与 DeepSeek Harness 主仓库的集成点
- **Cordis 服务消费**：`inject: ['tools', 'systemPrompt']`——依赖主仓库的 `ToolRegistry`（`packages/core/tools`）和 `SystemPrompt`（`packages/core/system-prompt`）。
- **工具定义复用**：从 `@deepseek-ai/dsh-tools` 导入 `defineTool`，遵循主仓库的工具 schema/output/meta 协议。
- **标准事件流出口**：不新建通道，描述子经主仓库 `events.mux` 的 `tool/result` 事件透传给所有客户端。
- **挂载方式**：原生 `~/.dsh/config.yaml` 个人覆盖层 `insert` 指令，或 `dshx install` / `dsh plugin install`；Dsh Companion 应用已自带。
- **类型与符号同源**：通过 `build.sh` 软链 `packages/core/*`、`vendor/cordis`、`packages/llm/llm` 等到 `node_modules`，与主仓库 vendor 布局严格对齐（参考 `marisa#2` 的链接修复背景）。

## 亮点与风险
- **亮点（精简、协议化）**：单文件 ~150 行实现，零运行时依赖（仅 Node 内建 + Cordis + dsh peer），把"文件交付"抽象成"事件 meta 中的结构化描述子"——客户端零耦合、可独立演进，是一个干净的协议设计。
- **亮点（测试真实）**：`tests/plugin.spec.ts` 用真实 Cordis 上下文 + `SessionStore + SystemPrompt + ToolRegistry` 组合，断言 model-visible 字符串、meta 描述子、错误路径与系统提示注入 4 个面，无 mock 桩。
- **风险 1（`sizeCache` 是模块级 Map，无界增长）**——`src/index.ts:122-124` 与 `src/index.ts:92`：每次 `execute` 写入 `path → size`，永不清理；长生命周期进程里会累积所有交付过的绝对路径，存在轻微内存与隐私泄漏面。注释只解释了"桥接 async fs 到纯 meta 投影"，未提及清理策略。
- **风险 2（meta 投影在错误路径下也会执行）**——`src/index.ts:90-98` 与 `src/index.ts:101-103`：`presentationMeta` 不校验 `path`，对空字符串会构造一个退化描述子（`name: ''`、`sizeBytes: 0`）并以 `as unknown as Record<string, never>` 强转绕过框架 meta 类型；当 args 非法导致 `execute` 抛错时，客户端仍可能在错误 `tool/result` 上收到一个伪描述子。
- **风险 3（扩展名判定无 magic-byte 兜底）**——`src/index.ts:35-60`：扩展名缺失或被人为篡改（`.png` 实为文本）会得到错误 `mimeType/artifactKind`，对安全敏感的客户端（如直接转发文件的 IM 桥）是潜在误判点。
- **风险 4（安装路径依赖宿主依赖符号链接）**——`README.md` 第 2 步与 `marisa#2`：pnpm 布局下必须手工把 `@deepseek-ai/dsh-tools` 链到宿主 checkout，marisa#2 修复前是已知摩擦点。
- **风险 5（极新仓库）**：创建于 2026-08-05，仅 2 个提交，0.1.0，0 star / 0 fork——属于刚发布的实验性协议插件，API 与描述子形状未来可能变。

## 维护状态
- 提交数：2（最近一次 `dd5727f 2026-08-05 README: native config.yaml mount is the default install path`）。
- 仓库创建/最近推送：2026-08-05（与本次调研同日）；仓库体积 10 KB；默认分支 `main`。
- 版本：`0.1.0`（`package.json` / `dsh.plugin.json` 一致）。
- 无 CI 配置文件、无 issue/PR 模板、无 changelog——单人维护、早期阶段。
- 测试需要在 dsh 主 checkout 下用其 vendored vitest 运行（`<dsh-checkout>/node_modules/.bin/vitest run --root .`）。

## 备注
- 仓库元数据描述与 README 一致，是 dsh 第二批外置插件中"客户端呈现层协议"的关键拼图：与 `dsh-companion`（已内置）、`marisa`（插件管理器）、各 IM 机器人（feishu/wecom/telegram/weixin 等）共同构成"模型产出 → 用户收到"的完整链路。
- 与本批次其他仓库（如 `dsh-pi-adapter`、`dsh-vision`、`dsh-tool-browser`）属于平行关系：它们提供"能力"，本仓库提供"交付协议"。
- 客户端接入指南在 README 末尾：监听 `session/event`，事件 `type == "tool/result"` 且（经 `tool/call` 配对得到的）工具名为 `send_artifact` 时，读 `event.data.meta`，以 `kind: "artifact"` 作为判别字段。
