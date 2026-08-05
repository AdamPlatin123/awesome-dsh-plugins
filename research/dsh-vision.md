# dsh-vision 调研摘要

## 一句话定位
给纯文本的 DeepSeek（deepseek-v4 等不具备视觉能力的模型）"加上眼睛"的 dsh 插件：注册一个 `view_image` 工具，把模型对图片的提问转发给任意 OpenAI 兼容的视觉语言模型（VLM）端点，答案以纯文本返回，从而让 dsh 的所有入口（web、TUI、远程通道）一键获得视觉能力。

## 技术栈与依赖
- **语言/形态**：零依赖 TypeScript（仅运行时依赖 `schemastery` 做配置 schema），原生 Cordis 插件形态，不引入 Python/uv/MCP。
- **peerDependencies**（宿主侧提供，仅在编译/类型检查时需要）：
  - `@deepseek-ai/dsh-system-prompt ^0.0.1`
  - `@deepseek-ai/dsh-tools ^0.0.1`
  - `cordis ^4.0.0-rc.7`
- **dependencies**：`schemastery ^3.18.0`
- **devDependencies**：`typescript ^5.9.0`（实际用 dsh 主 checkout 内的 tsc 编译）
- **测试**：Vitest（17 个 spec），真实 Cordis 组合 + 注入 fetch 作为测试缝
- **运行时**：Node.js 全球 `fetch`，无其它运行时依赖
- **构建产物**：`lib/`（JS + 类型声明）已入库；通过 `scripts/build.sh` 用 dsh 检出的 tsc 编译
- **License**：BSD-3-Clause
- **package.json `engines.dsh`**：`>=0.0.1`

## 文件结构概览
```
dsh-vision/
├── README.md              8.1KB   详尽文档 + 实测矩阵（4 厂商 10 模型）
├── LICENSE                1.5KB   BSD-3-Clause
├── package.json           984B    @dsh-external/dsh-vision 0.1.0
├── dsh.plugin.json        324B    dsh 插件清单（contributes.tools = ["view_image"]）
├── tsconfig.json          359B
├── .gitignore             30B
├── src/                          源码（TS）
│   ├── index.ts           6.2KB  插件主体：注册工具 + 系统提示片段
│   └── vlm.ts             5.1KB  OpenAI 兼容 VLM 客户端
├── lib/                          编译产物（已入库）
│   ├── index.js / vlm.js
│   └── types/                    .d.ts 类型声明
├── tests/                        Vitest 测试
│   ├── plugin.spec.ts     6.2KB  端到端：Cordis 组合 + 工具注册调用
│   └── vlm.spec.ts        5.1KB  VLM 客户端单测（注入 fetch）
├── scripts/
│   └── build.sh           2.3KB  链接 dsh checkout 依赖并 tsc 编译
└── assets/
    ├── demo-input.jpeg    27.6KB 测试图（BURGA 樱花手机壳）
    └── demo-session.png   413KB  dsh web 真实调用截图
```

## 核心功能与实现要点

1. **单一 `view_image` 工具**（`src/index.ts:60-95`）：通过 `ctx.tools.register(defineTool(...))` 注册名为 `view_image` 的工具；参数 `source`（本地绝对路径 / http(s) URL / data: URL）和可选 `question`；输出 schema 为 `{ type: 'string' }`，渲染为单一 text 块。`isConcurrencySafe` 恒为 `true`，`timeoutMs` 取自配置（默认 60s），`exec.signal` 全程透传到 fetch 请求，支持取消即中断。

2. **OpenAI 兼容 VLM 客户端**（`src/vlm.ts:62-110` 的 `visionChat`）：用一套请求体覆盖所有后端——POST `{baseURL}/chat/completions`，body 内 `messages[0].content` 为 `[{type:'image_url', image_url:{url}}, {type:'text', text:question}]`。响应解析支持 string 与 array-of-parts 两种 `content` 形态（`extractText`，`src/vlm.ts:48-60`）。

3. **本地图片自动 base64 内联**（`src/vlm.ts:24-45` 的 `toImageUrl`）：http(s)/data: URL 直通；本地文件按扩展名映射 MIME（png/jpg/jpeg/webp/gif/bmp/tif/tiff/heic），超出 `maxImageBytes`（默认 10MB）或扩展名不支持时抛出可操作错误。

4. **多后端 + 免费/付费/离线全覆盖**（`README.md` 后端表 + `src/index.ts:26-34` 默认值）：默认指向智谱 BigModel `https://open.bigmodel.cn/api/paas/v4` 的 `glm-4.6v-flash`（免费、128K 上下文）；可切换 DashScope `qwen3-vl-flash`、火山方舟豆包、Ollama 本地（`localhost:11434/v1`，无需 key），并预留未来 DeepSeek 官方识图 API。API key 解析链：插件配置 → `$DSH_VISION_API_KEY` → `$ZHIPUAI_API_KEY` → `$DASHSCOPE_API_KEY`（`src/index.ts:54-63`）。

5. **免费档自动降级链**（`src/index.ts:30-31, 44-47, 99-106`）：智谱免费模型偶发 429（code 1305），默认配置下依次降级 `glm-4.6v-flash` → `glm-4.1v-thinking-flash` → `glm-4v-flash`；判定可重试的正则 `RETRIABLE = /returned (?:429|404|5\d\d)/`，自定义端点或自定义 `fallbackModels` 时不自动套用默认链。

6. **`<think>` 推理块剥离**（`src/vlm.ts:115-122` 的 `stripThink`）：thinking 系模型（glm-4.1v-thinking 等）会把推理混进正文，先剥掉成对 `<think>…</think>`；若只剩未闭合的 `<think>`（推理吃光 token 预算），返回空，由上层抛出 "only reasoning" 错误，提示调大 `maxTokens`。

7. **系统提示注入**（`src/index.ts:36-38, 116-121`）：通过 `ctx.systemPrompt.section({ name: 'tool:dsh-vision', order: 116, text: PROMPT_TEXT })` 注册一段提示，教模型"自己看不见图，但可以调 view_image"——这是让纯文本模型"自主"发起视觉调用的关键 seam。order=116 在工具类提示段中定位明确。

8. **错误脱敏**（`src/vlm.ts:71, 80-95`）：所有抛出错误前用 `redact()` 把 `apiKey` 替换为 `***`，避免 key 泄漏到日志或返回给模型；本地端点（localhost/127.0.0.1/[::1]）无需 key，header 也省略 `authorization`（`src/vlm.ts:75-78`）。

## 与 DeepSeek Harness 主仓库的集成点

- **协议契约**：本插件是 dsh "external plugin" 标准形态——通过 `dsh.plugin.json`（`contributes.tools: ["view_image"]`）声明贡献，通过 `package.json` 的 `peerDependencies` 锁定宿主 API 版本（`@deepseek-ai/dsh-tools`、`@deepseek-ai/dsh-system-prompt`、`cordis`），运行时由 dsh 主程序的 Cordis 容器加载。
- **三个 seam**：
  1. `ctx.tools.register(defineTool(...))` —— 注册工具到 dsh 工具注册表（`src/index.ts:66`）。
  2. `ctx.systemPrompt.section({...})` —— 注入系统提示片段（`src/index.ts:116`）。
  3. `inject: ['tools', 'systemPrompt']` —— 声明依赖的 Cordis service（`src/index.ts:18`）。
- **安装挂载**：dsh 主程序自带 `~/.dsh/config.yaml` 个人覆盖层，三步原生挂载（clone + 链接宿主依赖 + 写 `- insert:` 配置项），不依赖第三方插件管理器；也可经 Marisa / plugin-registry / DSH Companion 安装。`scripts/build.sh` 复刻 dsh 主 checkout 的 pnpm 布局，把 `cordis/cosmokit/schemastery/@deepseek-ai/*` 等以 symlink 接到 `node_modules`，再用 dsh 自带的 tsc 编译——保证类型检查与运行时 dsh 同源。
- **`marisa#2` 依赖**：README 显式说明"在 marisa#2 修复前，装完仍需手工链接宿主依赖"——这是与 dsh-external/marisa 仓库的已知集成缺口。

## 亮点与风险

**亮点**
- 设计极简：单工具、单文件客户端、零运行时依赖，配置项仅 7 个，覆盖"免费/付费/离线/未来官方"四档场景。
- 工程质量高：17 个 Vitest spec 同时覆盖端到端 Cordis 组合（plugin.spec.ts）和 VLM 客户端边界（vlm.spec.ts：URL 直通、base64、超限、未知扩展名、429 降级、`<think>` 剥离、key 脱敏、本地端点免 key）。
- 文档翔实：README 含真实 dsh web 会话截图与 4 厂商 10 模型的实测延迟/质量矩阵（`README.md` 后端表 + 实测表）。
- 巧妙的"系统提示 + 工具"组合让纯文本模型自主发起视觉调用，而非用户手动触发。
- 安全细节到位：API key 在所有错误消息中自动脱敏（`src/vlm.ts:71`）。

**风险**
- **重度依赖外部 VLM 端点**：默认免费档（智谱公共容量池）存在 429 限流，生产环境稳定性取决于第三方；离线方案（Ollama）需用户自备 GPU。
- **`marisa#2` 未修复前的安装摩擦**：用户必须手工 symlink 宿主依赖（README 第 2 步），门槛偏高；对非 dsh checkout 用户尤其麻烦。
- **`peerDependencies` 版本范围过宽（`^0.0.1`）**：宿主 API 任意 minor/patch 变更都可能破坏类型契约；版本锁定粒度不足。
- **图片以 base64 data URL 内联**：`src/vlm.ts:42` 对大图会显著放大请求体（约 +33%），仅靠 `maxImageBytes` 软限；某些后端可能对 inline data URL 有大小限制。
- **降级链仅在默认端点生效**：自定义 `baseURL` 即便用智谱模型，也不会套用免费档降级链（`src/index.ts:44-47` 的判定），用户需自行配置 `fallbackModels`。
- **`stripThink` 较朴素**：仅识别成对闭合或起始的 `<think>`，对其它推理标记（如部分模型的 `<reasoning>`）无效——但目前主流 thinking VLM 兼容。

## 维护状态
- **全新仓库**：GitHub `dsh-external/dsh-vision`，2026-08-05 当天集中创建并提交（8 个 commit 全部集中在 2026-08-05 02:34–07:37 UTC），单日推送、单作者（gh 用户名为 GitHub 标识，昵称信息已脱敏）。
- **未归档**（`archived: false`），默认分支 `main`，0 issue、0 star、0 fork（截至调研时刻）。
- **commit 节奏**：从初版 `0ea41d5 dsh-vision: view_image tool bridging any OpenAI-compatible VLM` 起步，2 小时内连续迭代到当前版本（默认模型更新到 2026-08 一代的 `glm-4.6v-flash`、补 `<think>` 剥离与降级链、扩充实测矩阵）——活跃度极高但极早期。
- **未发布 tag / release**；版本号 `0.1.0`，处于早期可用阶段。

## 备注
- **与 dsh-vision 相关的仓库生态**：本插件与 `dsh-external/marisa`（插件管理器，依赖 issue #2 修复）、`dsh-external/dsh-companion`（应用自带本插件）、`dsh-external/plugin-registry`（可选安装渠道）形成上下文。
- **桥接抽象与 Qwen 官方 [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) 的 `vision_chat` 一致**（同为 OpenAI 兼容 `/chat/completions` + `image_url`），但本插件是零依赖 TS、原生 cordis 形态，不引入 Python/uv/MCP——迁移成本接近零。
- **隐私考量**：调用外部 VLM 端点意味着图片内容会离开本机，对敏感截图场景需提示用户切换 Ollama 本地后端（README 已列出该选项）。
- 调研证据：本机 clone（`/tmp/dsh-ext-research2/dsh-vision`）+ `gh api repos/dsh-external/dsh-vision`（返回 `description`、`license` BSD-3-Clause、`archived:false`）+ `gh api .../commits`（8 条提交时间线）。
