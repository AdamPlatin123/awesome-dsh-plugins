# dsh-gh-bridge 调研摘要

## 一句话定位
DeepSeek Harness 的 macOS 专用 Cordis 插件（npm 包 `@dsh-external/gh-bridge`）：在主机进程中读取 macOS Keychain 里的 GitHub token，写入 `~/.config/gh/hosts.yml`，使沙箱内被阻断 Keychain 的 `gh` CLI 重新可用，且 token 永不进入任何模型可见输出。

## 技术栈与依赖
- 语言：TypeScript（ESM，`target`/`lib` 均为 ES2022，`strict` + `noUncheckedIndexedAccess` + `verbatimModuleSyntax`），Node `>=22`。
- 插件框架：`cordis@^4.0.0-rc.7`（DSH 主仓库同款 ctx 模型）。
- 配置 schema：`schemastery@^3.18.0`；YAML 读写：`yaml@^2.5.0`。
- 进程执行：`node:child_process` 的 `execFile`（promisified），无外部执行库。
- 测试：`vitest@^2.1.0`；类型/构建：`typescript@^5.6.0`、`tsx@^4.19.0`。包管理器 pnpm。
- 仅运行时依赖上述三个 npm 包；刻意不依赖 DSH monorepo，主仓库服务通过 `ctx.get(name)` 取得（`package.json:18-27`）。

## 文件结构概览
```
.
├── src/
│   ├── index.ts        # apply()：注册 gh_bridge 工具、系统提示段、autoBridge 钩子；Schemastery Config
│   ├── bridge.ts       # inspectGhCredential / writeGhBridge：检查 + 写入 + 回读校验的核心逻辑
│   ├── hosts.ts        # hosts.yml 读写、hostToken/hostLogin/setHostToken（保留无关 host 与字段）
│   ├── types.ts        # 对 DSH 服务的最小结构化视图（ToolsRegistry/ApprovalService/SystemPromptService/BridgeDeps）
│   └── events.d.ts     # 重新声明 agent/session-start 事件（独立插件不能 import 主仓库的事件合并）
├── tests/
│   ├── bridge.spec.ts  # inspect/write 的状态机单测（no-gh/no-token/no-login/already/needs-bridge）
│   ├── index.spec.ts   # apply 装配、审批门、autoBridge、token 不外漏
│   └── hosts.spec.ts   # hosts.yml 序列化与异常容错
├── scripts/smoke.mjs   # 真实 gh + 真实 hosts.yml 的端到端冒烟（备份/剥离/桥接/恢复）
├── cordis.sample.yml   # cordis.yml 配置样例
├── package.json        # name=@dsh-external/gh-bridge, BSD-3-Clause
├── tsconfig.json / tsconfig.build.json
└── README.md
```

## 核心功能与实现要点
1. **问题与方案**：macOS 上 `gh` 把 oauth token 存在系统 Keychain；DSH 沙箱阻断 Keychain 访问，沙箱内 `gh` 报 `token is invalid`，迫使用户手动 `gh auth token > /tmp/...`（凭据泄漏）。插件在主机进程跑 `gh`（Keychain 可达），把 token 写入沙箱可读的 `hosts.yml`（`README.md:1-29`，`src/bridge.ts:1-15`）。
2. **inspectGhCredential 状态机**（`src/bridge.ts:46-100`）：依次 `gh --version`→`gh auth token`→读 `hosts.yml` 比较→解析 login；产出五种结果 `no-gh / no-token / no-login / already / needs-bridge`，是工具调用的决策核心。
3. **login 解析降级链**（`src/bridge.ts:102-118`）：优先 `security find-generic-password -s gh:<host>` 取 Keychain `acct` 属性（本地、离线、macOS 专属）；失败再 `gh api user --jq .login`（需网络）。这是 macOS-only 限制的来源。
4. **writeGhBridge + 回读校验**（`src/bridge.ts:135-159`）：写入后立刻 `readHostsDoc` 比对 token，不一致返回 `verify-failed`；`saveHostsDoc` 强制 `mode: 0o600`（`src/hosts.ts:42-46`），保留无关 host 与字段（`setHostToken` 仅覆盖目标条目，`src/hosts.ts:91-115`）。
5. **审批门 fail-closed**（`src/index.ts:152-179`）：`policy: ask` 默认走 `ctx.get('approval').request(...)`，理由文案明确告知"token 不会显示"；非 `allowed-once` 一律 `rejected`；approval 服务缺失时也 `rejected`，绝不静默写入。
6. **autoBridge（opt-in）**（`src/index.ts:198-210`）：仅在 `policy: allow` 下生效，监听 `agent/session-start` 事件，会话开始即静默桥接所有配置 host；与 `ask` 组合在装载期就抛错（`src/index.ts:118-121`），因为审批无法在会话启动时执行。
7. **零泄漏约束**：`renderResult` 只输出中文标签 + host + detail，token 永不出现在工具结果；有专门单测 `never leaks the token into the rendered model text`（`tests/index.spec.ts:230-236`）。
8. **DSH 工具契约完整对齐**：`tools.register({name, description, parameters(JSON Schema), output:{schema, render}, execute})`，与主仓库 `dsh-tools` 的 `ToolDefinition` 结构一致；并提供 `systemPrompt.section({name:'tool:gh-bridge', order:130, ...})` 引导模型在 gh 报错时主动调用（`src/index.ts:186-191`）。

## 与 DeepSeek Harness 主仓库的集成点
- **加载方式**：标准 cordis 函数插件——导出 `name='gh-bridge'`、`inject=['tools']`、`Config`（Schemastery schema）、`apply(ctx, config, internals)`，由主仓库 Loader 经 `cordis.yml` 加载（`src/index.ts:60-117`，`cordis.sample.yml`）。
- **服务消费（seam）**：通过 `ctx.get('tools' | 'approval' | 'systemPrompt')` 取主仓库服务，全部用 `src/types.ts` 里的最小结构化 interface 镜像（`ToolDefinition`↔`dsh-tools`、`ApprovalService`↔`dsh-user-approval`、`SystemPromptService`↔`dsh-system-prompt`），刻意不 import 主仓库类型，从而独立 build/test。
- **事件订阅**：`agent/session-start`（autoBridge 用），由 `src/events.d.ts` 通过 `declare module 'cordis'` 在本地补声明（注释说明独立插件不能 merge 主仓库的事件 map）。
- **关联 issue**：README 与 src/bridge.ts 注释引用 `dsh-external/issues#318`（沙箱内 gh 不可用的工单）作为立项依据。
- **跨平台行为**：Linux 上 token 本就明文存于 `hosts.yml`，inspect 直接返回 `already`，无需桥接；插件不会改 Linux 上的 gh 状态。

## 亮点与风险
**亮点**
- 安全模型严谨：默认 `ask` 审批 + `0600` 权限 + 回读校验 + token 零外漏 + fail-closed，多层防御（`src/index.ts:152-184`、`src/bridge.ts:149-158`、`src/hosts.ts:42-46`）。
- 解耦干净：仅依赖公共 `cordis` 包，所有主仓库服务经 `ctx.get` 取得，可在 monorepo 外独立构建与单测（`README.md` Development 节，`src/types.ts:1-8` 注释）。
- 测试覆盖完整：状态机五种 outcome、写入失败、回读不一致、审批拒绝、autoBridge 触发/不触发、token 不外漏均有用例（`tests/bridge.spec.ts`、`tests/index.spec.ts`）。
- 附真实环境冒烟脚本 `scripts/smoke.mjs`，用 `finally` 保证 `hosts.yml` 必被还原。

**风险**
- 单一初始提交（commit `ceecc43`，2026-08-05），无迭代历史，成熟度未知。
- 平台耦合：login 解析依赖 macOS 专属的 `security` CLI（`src/bridge.ts:108`），fallback `gh api user` 需联网，离线 + 非 macOS 场景会落到 `no-login`。
- `autoBridge: true` 与 `policy: allow` 组合绕过模型/用户参与，凭据写入完全静默——虽是 opt-in，但默认配置失误有静默改写凭据文件的风险（`src/index.ts:198-210`）。
- `noUncheckedIndexedAccess` 下多处 `cfg.hosts[0]!` 非空断言（`src/index.ts:166`），装载期已用 `hosts.length === 0` 抛错兜底，逻辑闭环但依赖运行时检查。
- 仅处理单一主仓库 issue（#318），与主仓库无版本契约/接口漂移防护（依赖结构化类型duck typing，主仓库改 `ToolDefinition` 形状时无编译期告警）。

## 维护状态
- 全新仓库：仅 1 次提交（`ceecc43 feat: DSH plugin bridging macOS Keychain GitHub token into gh hosts.yml for sandbox use`），提交日期 2026-08-05（调研当天），作者 `justynchen`。
- LICENSE：BSD-3-Clause（Copyright 2026 dsh-external contributors）。
- 无 CI 配置文件、无 CHANGELOG、无 release tag、无 git tag（基于 depth=1 clone 的可见信息）。
- 已发布意图明确（包名 `@dsh-external/gh-bridge`、`files: ["lib"]`、`main`/`types`/`exports` 齐备），但当前阶段更像首版交付。

## 备注
- 与同期调研的 `dsh-update-check`、`dsh-issue-filer` 等同为 DSH 第三方插件矩阵的一员，定位是"修复沙箱对 macOS Keychain 凭据的副作用"，是 DSH 在 macOS 用户体验上的关键补丁，非可选增强。
- 配置装载契约：`cordis.yml` 加 `id: gh-bridge / name: '@dsh-external/gh-bridge' / config: {policy, hosts, hostsYmlPath, autoBridge}`，`hostsYmlPath` 默认 `~/.config/gh/hosts.yml`（`src/index.ts:111-113`）。
- 工具调用示例输出（中文，模型可见）：`gh 凭据（github.com）：已桥接。已将 Keychain token 桥接到 hosts.yml，沙箱内 gh 可用`（`src/index.ts:46-58`）。
- 调研证据：本地 `git clone --depth 1` 成功；上述所有文件:行号引用均来自克隆副本 `/tmp/dsh-ext-research2/dsh-gh-bridge/`。
