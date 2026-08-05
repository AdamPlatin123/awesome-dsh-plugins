# dsh-tool-calculator 调研摘要

## 一句话定位

DSH 计算器工具插件：以零依赖、零进程、纯函数的手写递归下降解析器对数学表达式进行安全求值，向 DSH Agent 注册名为 `calculator` 的工具，弥补 LLM 算术不稳定与 bash 算术函数不全的问题。

## 技术栈与依赖

- 语言/编译：TypeScript（`target: ES2022`，`module: esnext`，`moduleResolution: bundler`，`strict: true`），输出到 `lib/`（declaration + `.tsbuildinfo`）
- 运行时：Node.js（ESM，`"type": "module"`）
- 测试：`vitest ^2.0.0`（唯一 devDependency）
- 隐式依赖（通过 DSH monorepo workspace 解析，**未在 package.json 中声明**）：`cordis`（`Context` 类型）、`@deepseek-ai/dsh-tools`（`defineTool` 帮手）
- 包名：package.json 中为 `@dsh-external/dsh-tool-calculator`，但 `src/index.ts` 的 `name` 常量与 README 接入示例均写作 `@deepseek-ai/dsh-tool-calculator`（见"亮点与风险"）
- 许可：MIT（Copyright 2026 whiteicey）

## 文件结构概览

```
dsh-tool-calculator/
├── .gitignore              # 忽略 lib/、node_modules/、*.tsbuildinfo、DESIGN.md、pnpm-lock.yaml、pnpm-workspace.yaml
├── LICENSE                 # MIT
├── README.md      ~6.0KB   # 动机/安全模型/架构图/工具声明/接入步骤/已知限制
├── package.json   ~489B    # 包元数据；仅 vitest 一个 devDep
├── tsconfig.json  ~303B    # 仅编译 src/，排除 tests/、lib/
├── src/
│   ├── index.ts    ~1.2KB  # Cordis 插件入口，注册 calculator 工具
│   └── evaluate.ts ~4.8KB  # tokenize() + parse() 递归下降求值器（公开 evaluate(expr): number）
└── tests/
    └── evaluate.spec.ts ~3.2KB  # vitest 用例：功能 + 攻击载荷
```

## 核心功能与实现要点

1. **零依赖递归下降求值器**（`src/evaluate.ts:1-136`）：完整实现词法层 `tokenize()`（`src/evaluate.ts:24-46`）与按优先级分层的语法分析 `parse()`（`src/evaluate.ts:49-127`）。优先级层次为：加减（`parseAdd`）→ 乘除模（`parseMul`）→ 一元正负（`parseUnary`）→ 幂（`parsePower`，右结合：`2 ** 3 ** 2 == 512`）→ 原子（`parsePrimary`：数字/常量/函数调用/括号）。

2. **白名单求值模型**（`src/evaluate.ts:13-22`）：`FUNCTIONS` 表暴露 15 个函数 `abs/ceil/floor/round/sqrt/pow/log/log2/log10/exp/sin/cos/tan/max/min`；`CONSTANTS` 表暴露 `PI`、`E`。标识符按名查找，命中常量禁止后跟 `(`，命中函数必须后跟 `(` 与以 `,` 分隔的实参；查不到即抛 `Unknown identifier`。

3. **多重安全护栏**：
   - 词法层只识别数字字面量、白名单标识符、`+-*/%(),` 与 `**`；引号、分号、反引号、`{}`、`[]`、`.` 等一律在 `tokenize()` 抛 `Invalid character`（`src/evaluate.ts:43-45`），从源头阻断 `constructor.constructor`、`process.exit(0)`、`globalThis`、`String.fromCharCode`、引号注入、分号语句、`__proto__` 等载荷
   - `evaluate()` 强制 `Number.isFinite(result)`，NaN/Infinity（除零、负数开方）一律拒绝（`src/evaluate.ts:131-134`）
   - 表达式长度上限 500 字符，超长抛 `Expression too long`（`src/evaluate.ts:128-130`）
   - README 明确论证：`new Function` + 正则白名单不安全（`constructor.constructor(...)()` 可达任意代码、`process.exit(0)` 可杀宿主），故不走任何代码求值捷径

4. **Cordis 插件入口**（`src/index.ts:1-38`）：导出 `name`/`inject = ['tools']`/`apply(ctx)`，在 `apply` 内通过 `ctx.tools.register(defineTool({...}))` 注册 `calculator` 工具；`timeoutMs: 1000`；`execute` 返回 `Promise.resolve(evaluate(...))` 以满足 `defineTool` 契约（latest commit 即为此修复）。

5. **工具契约**：参数 schema 为 `{ expression: string (required) }`；output schema 为 `{ type: 'number' }`，`render` 把数字转为单条 `text` 消息。Canonical 返回值是数字；Code Mode SDK 下可 `await tools.calculator({ expression })` 调用。

6. **完整测试覆盖**（`tests/evaluate.spec.ts:1-106`）：功能用例（优先级、括号、右结合幂、多参函数 `pow/max/min`、常量 `PI/E`、一元正负）+ 错误用例（尾随 token、缺右括号、未知标识符）+ 11 类攻击载荷用例（`constructor.constructor`、`process.exit`、`globalThis`、单/双引号注入、分号语句、`String.fromCharCode`、`eval`、`Function` 构造器、`__proto__`、超长表达式）。`pnpm test` 即 `vitest run`。

## 与 DeepSeek Harness 主仓库的集成点

- **Seam 协议**：消费 `@deepseek-ai/dsh-tools` 的 `defineTool` 帮手与 `cordis` 的 `Context`/`ctx.tools.register()` 接口——与 DSH 其它工具插件同款注册范式。
- **分发约束**：`@deepseek-ai/dsh-tools` 是 DSH monorepo 私有包（未发 npm），本插件**必须放入 monorepo** `packages/tools/dsh-tool-calculator/` 走 workspace 解析，无法独立安装。
- **接入清单**（README）：① 拷贝到 `~/.dsh/source/master/packages/tools/dsh-tool-calculator`；② 在 `apps/cli/package.json` 加 `"@deepseek-ai/dsh-tool-calculator": "workspace:^"`；③ 在 `apps/cli/config/base.cordis.yml` 加 `- id: tool-calculator, name: '@deepseek-ai/dsh-tool-calculator'`；④ 在 `tsconfig.host.json` 的 `references` 追加该路径；⑤ `pnpm install && pnpm run build`；⑥ 验证 `dsh -p "...用calculator工具计算"`。
- **前置版本**：DSH monorepo `snapshot-20260803T142347Z-25b2ad4f67` 或更新。
- 无打补丁/无源码修改主仓，纯外挂插件。

## 亮点与风险

**亮点**
- 安全模型扎实：词法层直接拒绝非白名单字符，绕过了"正则白名单 + 动态求值"的常见反模式；测试覆盖真实攻击载荷（含 README 中已实测复现的 `constructor.constructor` 与 `process.exit(0)`）。
- 零运行时依赖、零进程开销，毫秒级返回，特别针对 Windows 上 bash 进程创建昂贵的问题。
- 求值器优先级层次清晰、代码紧凑（136 行实现完整功能）。

**风险 / 缺陷**
- **包名不一致**：`package.json` 名为 `@dsh-external/dsh-tool-calculator`（`package.json:2`），而 `src/index.ts` 的 `name` 常量、README 接入示例、cordis.yml 示例均为 `@deepseek-ai/dsh-tool-calculator`（`src/index.ts:9`、`README.md` 接入章节）。按 README 步骤 ② 写 workspace 依赖时若取 `package.json` 的实际包名，会与步骤 ③ `cordis.yml` 的 `name` 字段对不上，导致插件加载失败。
- **隐式依赖未声明**：`cordis`、`@deepseek-ai/dsh-tools` 都未在 `package.json` 列出，仅靠 monorepo 环境提供；脱离 DSH monorepo（如独立构建或 lint）会缺类型/符号。
- **README 描述与实现不完全同步**：README 安全模型章节称"18 个函数 + 2 个常量"，实际 `FUNCTIONS` 表只有 15 个函数（缺 `atan2`/`hypot`/`sign` 等，或文档过时/笔误）。
- **`.ts` 后缀的相对导入**（`src/index.ts:10`：`from './evaluate.ts'`、`tests/evaluate.spec.ts:2`）依赖 `moduleResolution: bundler`；若主仓 `tsconfig.host.json` 用其他 resolution 可能报错。
- **不支持大整数与科学计数法**（IEEE 754 double、词法层拒 `1e5`）——已知限制，但调用方需注意。
- 单 commit 仓库，无 CHANGELOG/CI 配置（`.github/` 不存在），`pnpm-lock.yaml` 与 `pnpm-workspace.yaml` 被 gitignore（仅本地维护）。

## 维护状态

- 仓库状态：单分支 `main`，**仅 1 个 commit** `90e1276 fix: execute must return a Promise per defineTool contract`（即初始提交即包含上述修复）。
- 仓库整体偏"首发即定型"：源码、测试、文档一次性提交完毕；无 issue/PR/CI 痕迹（仓库克隆结果未发现 `.github/`、`CHANGELOG.md`）。
- 时间戳：文件 mtime 为 2026-08-05（克隆时间），LICENSE 落款 2026。
- 无后续迭代迹象，但代码完成度高、可工作。

## 备注

- LICENSE 持有者为 `whiteicey`（GitHub 用户名/昵称级别，无真实姓名/邮箱），符合脱敏要求。
- README 提及"完整用例清单见本地维护的设计文档"，但 `DESIGN.md` 已被 `.gitignore` 排除，未随仓库分发——如需追溯设计依据需联系作者。
- 工具名 `calculator` 满足 DSH 函数名约束（≤64 字符、`[A-Za-z0-9_-]`），注册后自动进入 Code Mode SDK。
- 与第一轮调研其它工具插件（如 `dsh-tool-json`、`dsh-tool-browser`）属于同一系列外部插件，接入范式一致，可作模板参考。
