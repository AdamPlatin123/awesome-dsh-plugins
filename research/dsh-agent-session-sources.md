# dsh-agent-session-sources 调研摘要

## 一句话定位
DeepSeek Harness 工作区扩展包，把一个 Harness agent 变成现有 Claude Code / Codex CLI 会话的"监督者"：注册一批模型可见的 `claude_session_*` / `codex_session_*` 工具，可发现、读取、增量 tail 这些外部 CLI 的持久化 transcript，并往同一会话注入下一条指令；同时附带只读的 Web 浮窗用于在对话头部查看两家 provider 的会话内容。

## 技术栈与依赖
- TypeScript（ESM），按 DSH workspace 多包布局组织； Cordis（`^4.0.0-rc.7`）作为插件框架，schemastery（`^3.18.0`）做配置 schema；UI 用 React + CSS Modules。
- 构建用 `tsdown`，单元测试用 vitest 风格 spec（`*.spec.ts(x)`）外加 `*.e2e.ts` 端到端用例与 `mock-codex.mjs` 等夹具。
- License：BSD-3-Clause（沿用 DSH workspace 许可）。
- 关键 peer 依赖（来自主仓）：`@deepseek-ai/dsh-invariants`、`@deepseek-ai/dsh-tools`（`defineTool`）、`@deepseek-ai/dsh-llm`（`ContentBlock` 类型）、`@deepseek-ai/dsh-subprocess`（spawn 契约）、`@deepseek-ai/dsh-subagent-claude-code`（Claude run 驱动）；客户端侧依赖 `@deepseek-ai/dsh-client-runtime`、`dsh-client-ui-conversation`、`dsh-client-locale`、`dsh-client-ui-slots`、`dsh-client-connection`。
- 不含 `lib/` 产物与 `node_modules`——源码仓库，需复制进 Harness checkout 后 `pnpm install`。

## 文件结构概览
```
README.md / README.zh.md        顶层说明（含工具表、推荐监督循环、YAML 挂载示例）
packages/
  claude-session/
    claude-session/             Claude transcript 服务（list/read/tail/resolve）
    tool-claude-session/        Claude 5 个模型工具 + drill 模板
  codex-session/
    codex-session/              Codex rollout 服务（byte-range 读取）
    tool-codex-session/         Codex 4 个模型工具 + 自带 codex resume driver
  client/
    ui-agent-session/           浮窗主体（provider 注册表 + AgentSessionsPanel）
    ui-agent-session-claude/    绑定 host claudeSession.* wire API
    ui-agent-session-codex/     绑定 host codexSession.* wire API
每个包：src/{index.ts,invariant.ts[,driver.ts]} + tests/ + README{,.zh}.md + package.json + tsconfig + tsdown.config
```

## 核心功能与实现要点
1. **Claude transcript 服务**（`packages/claude-session/claude-session/src/index.ts`）：`ClaudeSessionService extends Service`，serviceKey 为 `claudeSession`。默认根目录 `~/.claude/projects`，按项目 realpath slug（`projectSlug()` 把 `/Users/me/proj` 映射为 `-Users-me-proj`）解析 transcript 文件。提供 `resolveSessionFile / listSessions / transcript / tail`，全同步文件 I/O。`parseClaudeSessionLine` 只识别 `user`/`assistant`/`summary` 三类 record，提取 `text`、`tool_use` 名字、`tool_result` 短回显（200 字截断）；`isSidechain` 标记 subagent 流量。默认 256KB / 500 事件上限（`DEFAULT_MAX_TRANSCRIPT_BYTES/EVENTS`）。

2. **Codex rollout 服务**（`packages/codex-session/codex-session/src/index.ts`，558 行）：`CodexSessionService`，默认根 `~/.codex/sessions/<yyyy>/<mm>/<dd>/rollout-<id>.jsonl`。**关键差异：所有读取都是字节范围读取**（`openSync/readSync` 手写 `readRange`），因为 Codex rollout 文件常达数十 MB。`listSessions` 仅读每个文件的 `session_meta` 首行 + 64KB head/tail 窗口提取首/末用户消息；`session_meta.cwd` 用 `sameProject()` 做 realpath 规范比较。sessionId 从文件名末尾的 UUID（`rollout-<timestamp>-<uuid>.jsonl`）解析。

3. **Claude 工具插件**（`packages/claude-session/tool-claude-session/src/index.ts`）：`inject = ['tools', 'claudeSession', 'subprocess']`，注册 5 工具——`claude_session_list/read/tail/send` + `claude_supervisor_drill`。`send` 复用 host 的 `@deepseek-ai/dsh-subagent-claude-code` 的 `startClaudeRun`（headless `claude --resume`），支持 `fork: true`（`--fork-session`）把 context 延续到新 sessionId 以避免与交互进程并发写入冲突。每次注入自动追加 `guardSuffix`（完成卫语句），未正常完成则抛错并把部分回答塞进 isError 工具结果。`drill` 工具按 6 种任务类型（`feature/bug-fix/refactor/investigation/docs/generic`）返回质询问题模板（`DRILL_TEMPLATES`，可经 `drillTemplates` 配置覆盖；未知 key 在加载期抛错）。

4. **Codex 工具插件 + 自带 driver**（`tool-codex-session/src/index.ts` + `driver.ts`）：4 工具，无 drill。`send` 不复用 host 驱动，而是包内自带 `startCodexResume`：spawn `codex exec resume <id> <prompt> --json --skip-git-repo-check`，按 JSONL 事件流解析（`parseCodexLine` 处理 `item.completed`+`agent_message`、`turn.completed`、`error`），只把最终 assistant 文本回填给父 agent。支持每轮 `model` / `effort`（`minimal/low/medium/high/xhigh`）覆盖（`-c model=…`、`-c model_reasoning_effort=…`）；`bypassApprovals` 映射 `--dangerously-bypass-approvals-and-sandbox`。`disposeCodexChild` 走 SIGTERM → graceMs → 强杀的拆卸梯子（与 claude-code 后端同模板，driver 各自保留）。

5. **Web 浮窗（client/ui-agent-session）**：provider-neutral 的 React 浮窗（`AgentSessionsPanel.tsx`），挂到 `conversation.session.header.actions` slot（`order: 10`）。通过 `SourceRegistry`（实现 `HostObservable`）让独立挂载的 `ui-agent-session-claude/codex` 各自注册一个 `AgentSessionProvider`（`bind(sessionId) → {list, transcript, tail}` RPC verbs）。每 5 秒轮询 tail，single-flight，provider/会话切换时丢弃迟到结果。Node 半 `apply()` 为空——纯浏览器插件。Provider 未挂载或声明 unavailable 时浮窗整体隐藏，不伪造空列表。

6. **统一 record schema**：`ClaudeSessionEvent` 与 `CodexSessionEvent` 字段完全一致（`seq/timestamp?/type/sidechain/text/toolUses/toolResults`），因此同一个 Web 浮窗可渲染两家；`formatTranscript` 渲染为 `[user] … / [assistant] [tools: …] … / [other] …` 文本。

7. **推荐监督循环**（README）：`*_session_list → *_session_read → (claude_supervisor_drill) → *_session_send → *_session_tail`，强调"先读后驱、驱后再读"的验证闭环。

## 与 DeepSeek Harness 主仓库的集成点
- **不是独立工具，是 DSH workspace 扩展**。挂载方式：把这 7 个包目录复制进 Harness checkout 的对应 `packages/` 路径，再 `pnpm install`，然后在 Harness 插件配置里按 README 的 YAML 片段挂载（service plugin + tool plugin + UI plugin + 两个 provider contribution）。
- **Seam（依赖注入）**：
  - 工具插件 `inject = ['tools', 'claudeSession'|'codexSession', 'subprocess']`——缺任一服务挂载直接失败（不静默省略工具）。
  - Claude `send` 复用 host 的 `subagent-claude-code` 包（`startClaudeRun`、`ClaudeRunSpec`、`PermissionMode`、`DEFAULT_DISPOSE_GRACE_MS`）。
  - Codex `send` 走 host `subprocess.spawn`（`SubprocessSpawnSpec`/`SubprocessHandle`）但驱动自实现。
  - Web 浮窗 `inject = ['slots', 'conversation', 'locale']`，注册到 `conversation.session.header.actions` slot；UI provider 通过 host ApiProxy 的既有 `claudeSession.*` 与 `codexSession.*` 域名通信，host 必须已暴露这两个 ApiProxy 域。
- **服务键**：`ctx.claudeSession`、`ctx.codexSession`、`ctx.agentSessionSources`（通过 `declare module 'cordis'` 接口合并）。
- **无补丁、无 fork**——纯插件叠加；外部 CLI（claude/codex）保持自有进程与会话格式，Harness 仅以监督者身份 attach。

## 亮点与风险
- **亮点**
  - 设计干净的"读/tail/驱"三段监督原语，统一了两家 CLI 的 record schema，复用同一 Web 浮窗。
  - Codex rollout 字节范围读取（`readRange` + 64KB head/tail 窗口）针对数十 MB 文件做了显式优化（`packages/codex-session/codex-session/src/index.ts:217-247, 313-355`）。
  - 完成卫语句 `guardSuffix` 默认注入每条指令，防止被驱会话提前宣告完成（`tool-claude-session/src/index.ts:101-109`、`tool-codex-session/src/index.ts:51-57`）。
  - 错误显式化：未找到 session、不可读 transcript、spawn 失败、取消、子进程异常结束都转成 `isError` 工具结果并保留部分答案（`tool-codex-session/src/index.ts:184-198`）。
  - 大量 `v8 ignore`/`jscpd:ignore` 注释表明做过覆盖率与重复块治理，附 `*.e2e.ts` 与 `mock-codex.mjs`。
- **风险**
  - `claude_session_send` 与 `codex_session_send` 会让外部 CLI 在工作区里改文件/跑命令——`bypassPermissions`/`bypassApprovals: true` 仅应在独立沙箱里启用（README "Safety and failure behavior"）。
  - Claude `send` 与交互式 Claude 进程并发写入同一 transcript 会交错，README 明确说"unsupported by Claude Code"（`tool-claude-session/README.md` "Known Limitations"）。
  - Codex `effort` 参数本地不校验，非法值会以 opaque upstream provider error 形式返回（`tool-codex-session/src/index.ts:166`）。
  - Transcript 工具结果会原样回显外部会话中已存在的源码/命令输出/密钥，并进入监督模型上下文（README 安全说明）。
  - 仅源码分发，强耦合 DSH 主仓 peer 包的特定版本（`^0.0.1`），独立构建不可行——必须放进 workspace。

## 维护状态
- 仓库活跃：最新提交 `5f67fb2 docs: publish under dsh-external org`（2026-08-05，今天），上一个 `4221e2a feat: include model-facing session tools`（同日）。可见刚从内部仓迁出/改发布渠道。
- 提交者 GitHub 用户名：FSMargoo（昵称类，保留）。无作者邮箱/真实姓名泄露。
- 无 CI 配置文件、无 CHANGELOG、无 LICENSE 文件（license 仅写在各 `package.json` 的 `license: BSD-3-Clause`）；`.gitignore` 仅 91B（典型排除 `lib/`、`node_modules/`）。

## 备注
- 调研来源：`git clone --depth 1` 到 `/tmp/dsh-ext-research2/dsh-agent-session-sources/`，本地读取 README.md / README.zh.md / 全部 7 个包的 `package.json`、`src/index.ts`、`src/driver.ts`、`src/client/index.ts`、`src/client/slots.ts`、`src/client/index.ts` 及各包 README。
- 该仓与第一轮调研中的 `dsh-external/dsh-subagent-claude-code`（被本仓 Claude send 复用）有直接依赖关系，建议交叉参照。
- 验证方式（README "Verification"）：复制进 Harness checkout 后跑 7 个包的单元测试 + 主仓 build/type check；本仓不含 `lib/` 产物。
