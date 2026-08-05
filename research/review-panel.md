# review-panel 调研摘要

## 一句话定位

为 DeepSeek Harness Web 客户端新增原生的「审阅」视图：在会话侧边以工作区（Git 工作树）和本次会话（已完成工具结果）两个只读数据源展示统一差异，不引入第二个 agent 运行时、变更日志、Git 写服务或对模型可见的状态。

## 技术栈与依赖

- 仓库本身只是「交付物载体」：`README.md` + `.gitattributes`（`*.patch -whitespace`）+ 两张渲染截图（`docs/review-panel-desktop.png`、`docs/review-panel-mobile.png`）+ 一枚 152 KB 的 git 邮件补丁 `integration/0001-feat-web-add-review-panel.patch`。
- 补丁来源：基于 `dsh2026/test-echoVic`，base `ac8cc1e1e837ac06b37117af3c93025e6909284d`，集成分支 `codex/review-panel`，集成的 truth-source commit `e770f95ead2105fd2ffe50cf465d44af41f22838`。仓库明示这是「可评审的内测交付件，不是长期下游 fork」。
- 补丁新增的客户端包 `@deepseek-ai/dsh-client-ui-review`（`packages/client/ui-review/package.json`）：
  - 运行时 peer：`@deepseek-ai/dsh-client-connection`、`@deepseek-ai/dsh-client-runtime`、`@deepseek-ai/dsh-invariants`、`@deepseek-ai/dsh-client-ui-primitives`、`cordis ^4.0.0-rc.7`、`react ^18.2.0`。
  - 运行时 dep：`@deepseek-ai/dsh-host-apiproxy`、`diff ^9.0.0`（用于 `diffLines` 把会话里 `oldText/newText` 投影成 hunk）。
  - `dshClient.platform = "web"`，`inject = ["@deepseek-ai/dsh-client-runtime", "@deepseek-ai/dsh-client-ui-conversation"]`，license BSD-3-Clause，`private: true`，version 0.0.1。
- Host 侧变更集中在 `@deepseek-ai/dsh-host-apiproxy`，新增了对 `subprocess` 服务的依赖（`ApiProxyService.static inject` 多了 `'subprocess'`），并通过 `Config` 暴露 5 个 Git 审阅边界参数（见下）。
- 构建链：tsdown（`tsdown.config.ts` 复用 `clientBundle`）、tsconfig、pnpm-lock 全部同步更新。

## 文件结构概览

仓库根（仅 4 类文件）：

```
review-panel/
├── .gitattributes                              # *.patch -whitespace
├── README.md                                   # 定位 + 应用方式 + 集成足迹 + 验证
├── docs/
│   ├── review-panel-desktop.png                # 桌面分栏截图
│   └── review-panel-mobile.png                 # 窄屏堆叠截图
└── integration/
    └── 0001-feat-web-add-review-panel.patch    # 3225 行补丁，单一交付件
```

补丁触及主仓的 39 个文件，其中「真正新增的实现」集中在：

- `packages/client/ui-review/`（新包，15 个文件）：`package.json`、`tsdown.config.ts`、`tsconfig.json`、`src/index.ts`、`src/invariant.ts`、`src/css-modules.d.ts`、`src/client/{index.ts, ReviewView.tsx, review-model.ts, session-review.ts, workspace-review-source.ts, review.module.css}`、`tests/{review-model.spec.ts, review-view.spec.tsx, workspace-review-source.spec.ts}`、`README.md`/`README.zh.md`/`README.i18n.yaml`。
- `packages/host/apiproxy/src/workspace-review-git.ts`（新文件，279 行）+ 配套 `tests/workspace-review-git.spec.ts`。
- `packages/host/apiproxy/src/api/workspace.ts`、`api/rpc-map.ts`、`fetch/client.ts`、`fetch/handler.ts`、`api-proxy.ts`、`src/index.ts`：新增 `workspace.review` RPC 与 5 个 `review*` 配置项。
- `apps/cli/config/web.cordis.yml`、`apps/cli/package.json`：在 Web 组合里挂载新包。
- `apps/web/tests/review-panel.e2e.ts`（新文件）+ 新增 golden `apps/web/tests/snapshots/review-panel/workspace.expected.md`，外加 14 个现有 e2e 快照 md 的批量微调（多为新增审阅 tab 相关节点）。
- `tsconfig.{base,client,host}.json`、`pnpm-lock.yaml`、`docs/config-catalog.md`、`docs/cordis-catalog/services.md`、`packages/client/{README.md,README.zh.md}`、`packages/host/apiproxy/{README.md,README.zh.md}`、`scripts/verify-package-readme-model-experience.ts`、`.agents/notes/implemented/feature/2026-08-05-web-review-panel.{md,zh.md,i18n.yaml}`。

## 核心功能与实现要点

1. **一个 conversation.view 贡献**（`packages/client/ui-review/src/client/index.ts`）。`apply(ctx)` 通过 `ctx.slots.register({ name: 'conversation.view', id: 'review', order: 20, label: '审阅', inject })` 注册一个会话级 tab，按 `sessionId` 懒创建 `WorkspaceReviewSource`，并在 `ctx.effect` 清理时统一 `dispose()` + `abort()`。`inject` 把 `history` 和 `workspaceReview` store 连同 `loadAllHistory`/`refreshWorkspace` 回调喂给视图。

2. **双数据源视图**（`src/client/ReviewView.tsx`，188 行）。React 组件提供「工作区 / 本次会话」分段切换、按路径模糊筛选（小写、空白分词、AND）、文件列表 + 差异主面板的分栏（≤720px 改为单列堆叠，见 `review.module.css: @media (max-width: 720px)`）。状态文案全中文（`STATUS_LABEL`：新增/修改/删除/重命名/复制/冲突；空仓、加载中、错误、截断等均有专门分支）。差异由内联子组件 `DiffFile` 渲染：二进制或空 hunk 走占位文案，否则按 `@@ -o,ol +n,nl @@` 头 + 行级 `kind: added/deleted/context` 渲染。

3. **会话源 = 已完成 diff 卡的纯投影**（`src/client/session-review.ts`，58 行）。`deriveSessionReview(nodes)` 遍历会话历史节点，只挑 `node.kind === 'tool-result' && !node.isError && node.resultView?.card === 'diff'`，按路径 fold 出 `SessionReviewFile`，统计 added/deleted 行数。注释明示「不发明第二个 mutation log」。再经 `review-model.ts` 的 `sessionReviewFiles()` 用 `diffLines(..., { oneChangePerToken: true })` 把 `oldText/newText` 转成与 Git 审阅完全相同的 `WorkspaceReviewHunk`/`WorkspaceReviewLine`，复用同一渲染层。

4. **工作区源 = 单一新增 RPC + 浏览器端 store**（`src/client/workspace-review-source.ts`，73 行）。`createWorkspaceReviewSource(api, sessionId)` 返回一个 `SnapshotStore<WorkspaceReviewState>`，`refresh(signal)` 用「最新一代获胜」策略：每次自增 `generation`，前置 `AbortController` 互斥，`AbortSignal.any` 合并外部信号，`transportError` 兜底异常。这是 `api.workspace.review({ sessionId }, signal)` 的唯一调用点。

5. **Host 侧 `workspace.review` RPC**（`packages/host/apiproxy/src/api/workspace.ts` 新增 46 行类型 + `rpc-map.ts`/`fetch/client.ts`/`fetch/handler.ts` 的 1 行映射）。新增 `WorkspaceReviewSnapshot`（`repository: { root, branch, head } | null` + `files[]` + `added/deleted/truncated`）和 `WorkspaceApi.review()` 签名，注释强调「side-effect free, never creates or resumes an agent」。`workspace.schema.ts` 同步加入 schema，`rpc-schemas.spec.ts` 覆盖。

6. **有界、只读的 Git 检查**（`packages/host/apiproxy/src/workspace-review-git.ts`，279 行，核心）。`inspectWorkspaceReview(subprocess, cwd, config, signal)`：
   - 经托管 `SubprocessService` 跑 `git`，固定 `-c core.quotepath=false -c color.ui=false` 和 `GIT_OPTIONAL_LOCKS=1` 环境，`stdin: 'ignore'`，stdout/stderr 用 `maxBytes = maxPatchBytes + 1` 的 collect buffer做截断检测，`AbortSignal.timeout(timeoutMs)` 与外部信号合并，`graceMs` 给终止宽限。
   - 流程：`rev-parse --show-toplevel` 探根目录（非仓则返回 `repository: null` 的空快照）→ 并行 `symbolic-ref --short -q HEAD` / `rev-parse --short HEAD` / `status --porcelain=v1 -z --untracked-files=all` / `diff HEAD --no-ext-diff --no-textconv --no-color --find-renames --unified=3 --`。
   - `parseStatus` 按 NUL 分段解 porcelain v1，`statusOf(x, y)` 把 XY 字符映射到 `added/modified/deleted/renamed/copied/conflicted`，识别 `R/C` 后跟随的 oldPath；`diff` 输出用 `parsePatch` 解析为 hunk，`reviewLines` 把 `\` no-newline 行跳过。
   - 未被 diff 覆盖的 untracked 文件，走 `untrackedFile()`：先 `relative(root, path)` 拒绝逃逸路径，`lstat` 排除目录/符号链接，按 `maxFileBytes` 直读文件首块，含 NUL 或超长则标 `binary: true`，否则把整文件当作单 hunk 的全 added 行。
   - 截断语义：`truncated = (allStatuses.length > maxFiles) || patchResult.truncated || patchBytes > maxPatchBytes`，并在状态/patch 超限时直接 `throw` 业务错误。

7. **5 个有界的部署参数**（`packages/host/apiproxy/src/index.ts` 的 `Config`）。新增 `reviewTimeoutMs`/`reviewTerminationGraceMs`/`reviewMaxFiles`/`reviewMaxPatchBytes`/`reviewMaxFileBytes`，全部 `z.natural().min(1).default(DEFAULT_WORKSPACE_REVIEW_CONFIG.*)`，由 `docs/config-catalog.md` 文档化。`ApiProxyService.static inject` 因此新增 `'subprocess'`，`config-catalog` 同步加上该 requires 行。

8. **验证矩阵**（README「Verification」+ `apps/web/tests/review-panel.e2e.ts`）。单元测试覆盖 review modeling、view 交互、请求取消、RPC 校验、有界 Git 收集（`packages/client/ui-review/tests/*` 与 `packages/host/apiproxy/tests/workspace-review-git.spec.ts`）；E2E 是 keyless 组装 Web + Playwright Chromium + 真实临时 Git 仓库（`git init -b feature/review-panel` → 提交 baseline → 修改 `review.ts`、新增 `notes.md`），打开持久化 Session 后点「审阅」tab，固定 branch、+3/-1 totals、行级 `export const state = "before"`/`export const reviewed = true`，并对比 golden `snapshots/review-panel/workspace.expected.md`，console tripwire 断言无 warning/pageError。另用 `ego-browser` 在 1440×1000 与 390×844 下做过渲染回归。

## 与 DeepSeek Harness 主仓库的集成点

- **Seam 1（浏览器扩展点）**：新包以标准 `dshClient` 协议（`platform: web`、`inject` 声明、`apply(ctx)` + `src/index.ts` 占位 + `src/invariant.ts` 通过 `ctx.invariants.register(PACKAGE_NAME, install)`）挂入，仅注册一个 `conversation.view` 贡献，不新增协议面、不写持久化。需要在 `apps/cli/config/web.cordis.yml` 和 `apps/cli/package.json` 把 `@deepseek-ai/dsh-client-ui-review` 加进 Web 组合（补丁已改）。
- **Seam 2（RPC 协议）**：Host 侧新增一条只读一元 RPC `workspace.review({ sessionId }) → WorkspaceReviewSnapshot`，贯穿 `api/workspace.ts`（类型）→ `api/rpc-map.ts`（`RpcMethodMap`）→ `api/workspace.schema.ts`（zod）→ `fetch/client.ts`（client stub）→ `fetch/handler.ts`（dispatch）→ `api-proxy.ts`（注册）。客户端 connection 包的 `api.ts`/`fixture.ts`/`tests/fake-api.ts` 同步加 `workspace.review` 行。
- **Seam 3（Host 服务依赖）**：`ApiProxyService` 新增对 `subprocess` 服务的依赖，所有 Git 调用走既有的托管子进程服务（带时间、输出、文件数、目录围栏、二进制围栏）。
- **Seam 4（既有 UI 约定）**：复用 `@deepseek-ai/dsh-client-ui-primitives` 的 `IconBranchOutline16/IconCodeOutline16/IconRefreshOutline16/IconSearchOutline16` 和 `Tooltip`；复用 `@deepseek-ai/dsh-client-runtime` 的 `createSnapshotStore`/`SessionHistoryFace`；复用 `@deepseek-ai/dsh-client-ui-slots` 的 `InjectFace`。所有 hook 形态（`useHistory`/`useWorkspaceReview`）走 `ConvViewProps`。
- **明示未改**：agent loop 行为、模型请求、工具、批准、Session 事件均不动；无写命令、无批准路径、无模型输入。
- **应用方式**：在兼容的 DeepSeek Harness checkout 内 `git am integration/0001-feat-web-add-review-panel.patch`；integrated 分支才是 truth source。

## 亮点与风险

亮点：

- 设计纪律强：README「Integration footprint」与实现严格一致——零新增协议面（除一条只读 RPC）、零新增持久化、零模型可见状态，会话源是已完成 diff 卡的纯函数投影，避免双 log。
- Git 检查是真有界：时间（`AbortSignal.timeout`）、终止宽限（`graceMs`）、文件数（`maxFiles`）、patch 字节（`maxPatchBytes`，且 +1 检测截断）、单文件字节（`maxFileBytes`）、目录围栏（`relative(root, path)` 拒绝 `..`/绝对路径）、二进制识别（NUL 字节/超长）一并落地（`workspace-review-git.ts:152-279`、`untrackedFile` 的路径校验在 `:226-232`）。
- 测试链完整：单元 + keyless 真 Git E2E + 双分辨率渲染回归。

风险：

- **Patch 是唯一交付件**：3225 行补丁绑死 base `ac8cc1e1...`，主仓一前进就可能冲突；仓库自述「不是长期下游 fork」，需要持续 rebase 或合并到主线才能稳定。
- **Apiproxy 多了 `subprocess` 强依赖**：`static inject` 加 `'subprocess'` 意味着任何挂载 apiproxy 的部署都必须同时提供 subprocess 服务；存量组合若未声明会直接启动失败（`packages/host/apiproxy/src/index.ts:60`）。
- **截断语义对用户可见但不可恢复**：超 `maxFiles` 直接 `slice(0, maxFiles)` 且只置一个 `truncated: true`；状态行/patch 超限则直接抛错（`workspace-review-git.ts:255-262`、`266-269`）——大仓库体验会突变。
- **初生仓静默空快照**：`rev-parse --show-toplevel` 失败（含无首提交的 unborn repo）直接返回 `repository: null` 的空 snapshot，前端显示「当前目录不是 Git 仓库」，与「刚 init 还没 commit」难以区分（`workspace-review-git.ts:259-263`）。
- **untracked 文件直读**：绕过 git，用 `fs.open` 直读首 `maxFileBytes` 做文本预览（`workspace-review-git.ts:262-285`）；围栏已到位，但仍意味着 review RPC 会读宿主文件内容，部署时需评估信任边界。
- **14 个现有 e2e golden 被批量改动**：补丁顺带改了 `bash-abort-row`、`code-mode-round`、`cordis-tool-round`、`fresh-round-trip`、`lifecycle-chrome/reloaded`、`live-interactions/{cancel,error-auth,loading,retry}`、`markdown-images`、`message-actions`、`plan-review/approved`、`question-composer/answered`、`queue-actions/{collapsed,editing,layout,preserved,ui}`、`seeded-history/{command-row,ui}`、`steering/{mid-steer,settled}`、`subagent-conversation/{nested,ui}`、`web-search-round/ui` 的 `ui.expected.md`——评审时需确认这些只是新增审阅 tab 的 aria 节点而非行为回归。
- **隐私/数据**：客户端补丁本身不涉及用户邮箱或真实姓名；仓库 commit 作者用昵称「青雲」，无敏感信息泄露。

## 维护状态

- 单 commit 仓库：`9afcfaf feat: publish internal review panel beta`（作者「青雲」，2026-08-05 03:04:38 +0800，与今日同日）。无 issue/PR/CI 配置（仓库内无 `.github/`）。
- README 自述「Internal beta. This repository is private and is not a public compatibility commitment.」——即：内测交付，不对外做兼容承诺，集成请以 `dsh2026/test-echoVic` 的 `codex/review-panel` 集成分支为准。

## 备注

- 仓库不是空占位：含完整 README、双分辨率截图、152 KB 可应用补丁，与本轮其它「空仓/纯 README 占位」仓库不同。
- 关联第一轮调研：本补丁正是「dsh-external/* 工具扩展」中 ui-* 系列的典型代表——一个走 `dshClient` web 扩展点、零侵入主 agent loop 的纯 UI 包；可作为「dsh web 端扩展该怎么写」的样板参考（`src/index.ts` 的 `apply`/`inject`、`src/invariant.ts` 的 invariant 注册、`tsdown.config.ts` 的 `clientBundle` 用法都值得复用）。
- 应用前应在主仓 `apps/cli/config/web.cordis.yml`、`tsconfig.{base,client,host}.json`、`pnpm-lock.yaml` 的同步改动上做一次干净 review；若主仓已偏离 base `ac8cc1e1` 较远，建议以集成 commit `e770f95e` 为参考手改而非盲 `git am`。
