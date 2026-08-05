# dsh-tool-json 调研摘要

## 一句话定位

DSH（DeepSeek Harness）JSON 查询工具插件：在 agent 工具管线中注册名为 `json` 的工具，用零依赖、纯函数的手写递归下降解析器执行 JMESPath 核心子集查询，替代 `jq`/`node -e` 进程，对 API 响应、配置文件等 JSON 数据做结构化路径提取。

## 技术栈与依赖

- **语言**：TypeScript（`target: ES2022`，`module: esnext`，`moduleResolution: bundler`，`strict: true`），ESM（`"type": "module"`）
- **运行时依赖**：零运行依赖；仅 `cordis`（peer，宿主提供）和 `@deepseek-ai/dsh-tools`（peer，DSH monorepo workspace 提供）
- **开发依赖**：仅 `vitest@^2.0.0`
- **包名**：`@dsh-external/dsh-tool-json`（package.json）/ 插件注册名 `@deepseek-ai/dsh-tool-json`（Cordis `name` 导出）—— 两者不一致，参见风险
- **构建产物**：`lib/index.js` + `lib/index.d.ts`（`tsbuildinfo` 已 gitignore）；`pnpm-lock.yaml` 和 `pnpm-workspace.yaml` 也被 gitignore，说明本仓只作为 DSH monorepo workspace 子包使用，不独立 lock
- **许可**：MIT，版权 `2026 whiteicey`（昵称）

## 文件结构概览

```
dsh-tool-json/
├── src/
│   ├── index.ts        # 49 行：Cordis 插件入口，注册 json 工具
│   └── query.ts        # 160 行：解析器 + 执行器 + normalizeInput
├── tests/
│   └── query.spec.ts   # 198 行：功能/错误/攻击载荷用例（vitest）
├── tsconfig.json       # 独立 TS 配置（host 通过 references 引用）
├── package.json        # 单脚本 `test: vitest run`
├── README.md           # 7.3KB，文档完整
├── LICENSE             # MIT
└── .gitignore          # lib/, node_modules/, *.tsbuildinfo, DESIGN.md
```

总计约 407 行（src + tests）。规模极小，聚焦单一工具。

## 核心功能与实现要点

1. **工具注册（`src/index.ts:13-46`）**：通过 Cordis `ctx.tools.register(defineTool({...}))` 注册名为 `json` 的工具，`name`/`inject:['tools']`/`apply(ctx)` 是标准 Cordis 插件三件套。参数声明 `input: { type: 'json', required: true }` + `query: { type: 'string', required: true }`；输出 `schema: { type: 'json' }` 配合 `render` 序列化为文本——Code Mode 直接拿对象、Model Context 拿 `JSON.stringify` 文本。

2. **JMESPath 子集解析器（`src/query.ts:25-89` `parseQuery`）**：手写递归下降，输出 `QueryStep[]` AST，支持四类步骤：`dot`（`foo.bar`）、`bracket`（`items['key']` 单引号 / `items["key"]` 双引号兼容）、`index`（`items[0]`）、`wildcard`（`items[*]`）。支持组合嵌套（`a.b[0].c.d`），起始位置允许裸标识符。不支持：过滤器 `[?...]`、管道 `|`、函数调用、多级通配扁平化（`items[*].tags[*]` 返回嵌套数组而非扁平）。

3. **执行器（`src/query.ts:92-138` `executeQuery`）**：逐步骤求值；通配符为终态，对数组元素 `filter(对象)` + `map(executeQuery(剩余路径))` + `filter(非 null)`，缺失属性按 JMESPath 语义跳过。空查询（`''`）返回整体输入；标量 / 布尔 / null / Unicode key 均支持。

4. **输入归一化（`src/query.ts:143-152` `normalizeInput`）**：`input` 双形态——对象直传（agent 参数管线 lossless）或字符串（`JSON.parse` 解析，失败抛 `invalid JSON input`）。

5. **安全模型（贯穿 `query.ts`）**：无 `eval` / `new Function`；属性读取只走 `Object.hasOwn`，`constructor`/`__proto__`/`prototype` 不触发原型链；通配符遍历用 `Object.keys` 语义，不走 `for...in`；硬限制查询深度 20 层（`MAX_DEPTH`）、长度 200 字符（`MAX_LENGTH`）；引号注入在词法层被拒绝（未闭合引号即抛错）；`eval` 作为 key 仅是普通字符串。`timeoutMs: 1000` 兜底。

6. **测试覆盖（`tests/query.spec.ts`）**：约 35+ 用例，分三类——功能用例（点号 / 索引 / bracket 单双引号 / 通配 / Unicode / 深嵌套 / 标量返回）、错误用例（属性不存在 / 越界 / 通配用于非数组 / null 中间值）、攻击载荷用例（原型链防护 / 深度上限 / 长度上限 / 引号注入 / `eval` 作为普通 key）。评审补充用例 T1-T4 覆盖空数组、JSON 字符串输入、属性缺失跳过、多级通配嵌套语义。

7. **错误语义对齐 DSH**：所有错误抛 `Error`，由 DSH 工具管线统一转为 `isError` 结果，agent 从错误信息学习（设计明确，README "错误语义"段落）。

## 与 DeepSeek Harness 主仓库的集成点

本插件**不是独立工具**，而是 DSH monorepo 的 workspace 子包，集成走标准 DSH 工具插件协议：

- **Seam（协议）**：依赖 `@deepseek-ai/dsh-tools` 导出的 `defineTool`、`JsonValue` 类型（`src/index.ts:8-10`）；运行时通过 Cordis `ctx.tools.register(...)` 注册，依赖宿主 `tools` 服务（`inject: ['tools']`）。无运行时 patch、无 fork，纯协议接入。
- **接入步骤**（README "接入方式"明确，五步）：
  1. 复制到 `~/.dsh/source/master/packages/tools/dsh-tool-json` —— 必须放 `packages/tools/` 下，匹配 DSH `packages/*/*` 两层 workspace 模式
  2. `apps/cli/package.json` 加 `"@deepseek-ai/dsh-tool-json": "workspace:^"`
  3. `apps/cli/config/base.cordis.yml` 加 `- id: tool-json, name: '@deepseek-ai/dsh-tool-json'`
  4. `tsconfig.host.json` 的 `references` 加 `{ "path": "./packages/tools/dsh-tool-json" }`
  5. `pnpm install && pnpm run build` 后 `dsh -p ...` 验证
- **前置条件**：DSH monorepo `snapshot-20260803T142347Z-25b2ad4f67` 或更新
- **命名约定**：Cordis 插件 `name` 用 `@deepseek-ai/` 前缀（与 DSH 内部命名空间一致），即便 package.json 用 `@dsh-external/` —— 接入时以 `src/index.ts` 的 `name` 为准

## 亮点与风险

**亮点**：

- **零依赖、纯函数**：仅 `vitest` devDep，运行时无任何 npm 依赖；`query.ts` 完全自包含，可独立移植（`src/query.ts:1-160`）
- **安全设计扎实**：原型链防护（`Object.hasOwn` + `Object.keys`）、深度 / 长度硬上限、词法层拒绝引号注入、无 `eval`/`Function`——并有专门攻击载荷测试（`tests/query.spec.ts` "攻击载荷" 段）
- **双形态 input**：`type: 'json'` 让 agent 直接生成对象参数零转义，同时兼容 bash/read 字符串透传，`normalizeInput` 统一（`src/query.ts:143`）
- **文档质量高**：README 含动机、使用场景、安全模型、架构图、完整接入步骤、已知限制——可读性远超仓库规模
- **错误驱动 agent**：错误信息直接进 isError 结果，明确支持 agent 从错误学习（README "错误语义"）

**风险**：

- **包名不一致**：`package.json` 是 `@dsh-external/dsh-tool-json`，但 `src/index.ts:11` 的 Cordis `name` 导出是 `@deepseek-ai/dsh-tool-json`，README 的接入示例也用 `@deepseek-ai/` —— 接入时 workspace 依赖名需与 `src/index.ts` 的 `name` 对齐，否则 Cordis 加载不到。这是个容易踩的命名裂缝（`package.json:2` vs `src/index.ts:11`）
- **多级通配非标准**：`items[*].tags[*]` 返回嵌套数组而非 JMESPath 标准扁平化（`tests/query.spec.ts` "T4" 用例明确记录此偏差）—— 在 agent 链式查询时可能产生预期外结构，README 已声明限制
- **无过滤器 / 管道 / 函数**：`[?downloads > 1000]`、`|`、函数调用均不支持，复杂查询需 bash + node 兜底（README "已知限制 #3"）
- **分发链路私有**：`@deepseek-ai/dsh-tools` 未发布 npm，本插件必须放入 DSH monorepo 走 workspace 解析，无法独立 install（README "已知限制 #1"）
- **只读**：不能修改 JSON 字段，原地修改需 `str_replace_editor`/`write`（README "已知限制 #2"）
- **代码量极小但单 commit**：仅 1 个 commit（`5b4cd34 feat: JSON query tool plugin for DSH (JMESPath subset)`），无迭代历史，无 CHANGELOG，无 CI 配置——成熟度处于"首版完成、待实战"阶段
- **`DESIGN.md` 被 gitignore**：设计文档本地维护未入库（`.gitignore` 含 `DESIGN.md`），README 提到"完整用例清单见本地维护的设计文档"——评审追溯链路不完整

## 维护状态

- **提交历史**：单 commit（`5b4cd34`，2026 年），无后续迭代；仅 `main` 分支
- **作者**：whiteicey（昵称，来自 LICENSE；GitHub 用户名未在仓内显式标注）
- **CI/CD**：无（无 `.github/workflows/`，无任何 hook），仅本地 `pnpm test`
- **版本**：`0.1.0`（`package.json:3`），处于首版
- **活跃度**：无法从单 commit 推断；当前形态是"功能完备的首版插件，测试齐全"，未观察到 bugfix 或迭代痕迹
- **可维护性**：代码极简（160 行核心 + 49 行入口），零依赖，纯函数——后续维护成本低，但缺少 CI 兜底回归

## 备注

- **调研方法**：`git clone --depth 1` 成功（直连 GitHub），全量阅读 README / package.json / tsconfig / LICENSE / .gitignore / `src/index.ts` / `src/query.ts` / `tests/query.spec.ts`，并跑 `git log --oneline -20` / `git branch -a` / `wc -l` / `git rev-list --count` 确认历史与规模。
- **与同类工具的关系**：DSH 已有内置 `grep`（正则字符串匹配）和 `str_replace_editor`/`write`（修改文件）；本插件填补"结构化只读 JSON 查询"空缺，定位清晰、不与现有工具重叠。
- **典型场景验证**：README 给的四个场景（API 响应提取、配置定点读取、通配投影、存在性判断）都能直接由 `query.ts` 现有语法覆盖——实现与宣传一致。
- **未运行测试**：本仓是 DSH workspace 子包，独立 `pnpm test` 会因缺 `cordis` / `@deepseek-ai/dsh-tools` peer 失败；但 `query.ts` 和测试只依赖 `vitest` + 自身，理论上剥离 peer 后可独立跑通（未实测）。
