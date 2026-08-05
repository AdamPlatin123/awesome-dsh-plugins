# dsh-github-integration 调研摘要

## 一句话定位

DeepSeek Harness（以下简称 DSH 主仓库）的深度 GitHub 集成项目：以「可挂载的 skill 插件 + 三包工具源码」两层形态，给模型提供 11 个结构化 `github_*` issue/PR 工具，并配套一条「快照制开源协作」修复战役工作流 skill。仓库自述为 plugin-only，不含 DSH 上游源码，版权归 mattheliu，当前为 dsh-external 组织下供 beta 成员使用的私有仓库。

## 技术栈与依赖

- 语言/运行时：TypeScript（ESM），Node 内置 `fetch` 作传输层，无 CLI/编译产物入库（`.gitignore` 排除 `lib/`、`dist/`）。
- 包管理/构建：pnpm workspace（`@deepseek-ai/*` workspace 协议），tsc + `tsconfig.host.json` 聚合，schemastery 做配置校验，vitest 跑单测。
- 框架：cordis（`^4.0.0-rc.7`）——DSH 的插件/服务容器，工具通过 `Service` 子类注册为 `ctx.github`。
- 与 DSH 的强耦合依赖（均为 `peerDependencies` + `workspace:^`）：
  - `@deepseek-ai/dsh-credentials`（token 解析，`credentialRef`）
  - `@deepseek-ai/dsh-invariants`（契约校验，每个包都有一个 `invariant.ts`）
  - `@deepseek-ai/dsh-tools`（`defineTool` / `ToolDefinition`，仅 tool-github 依赖）
- 无第三方 HTTP 客户端、无 GraphQL、无 octokit——REST 路径与 query 全部手写在 `resolve.ts`。

## 文件结构概览

```
dsh-github-integration/
├── README.md / README.zh.md            顶层说明（安装两步法 + 工具表 + 路线图）
├── catalog.json                        toybox 风格插件索引，pin 到 commit 19158db
├── LICENSE                             BSD-3-Clause
├── plugins/github-integration/
│   └── .dsh-plugin/                    ← 唯一被挂载的目录
│       ├── package.json                dsh: { skills: ["skills"] }
│       ├── prepare.js                  prepare 钩子
│       └── skills/github-issue-pr/SKILL.md   战役工作流 skill（5.4 KB）
└── packages/github/                    ← 工具源码包，需拷进 DSH checkout 编译
    ├── github/                         @deepseek-ai/dsh-github（seam）
    │   └── src/{index,types,client,invariant}.ts
    ├── github-local-rest/              @deepseek-ai/dsh-github-local-rest（实现）
    │   └── src/{index,resolve,invariant}.ts
    └── tool-github/                    @deepseek-ai/dsh-tool-github（消费者/工具）
        └── src/{index,issue-tools,pr-tools,shared,anchor,invariant}.ts
```

git 追踪文件共 41 个；shallow clone 仅见最新一笔 commit `8786280`（2026-08-05，即今天）。

## 核心功能与实现要点

1. **三层 capability-seam 架构**（`packages/github/README.md`）：`github/` 定义抽象 seam（`ctx.github`），`github-local-rest/` 是 Node fetch 实现，`tool-github/` 是 11 个模型工具的消费者。三层各自一个独立 npm 包，按 DSH 仓库既有的「seam/实现/消费者」惯例拆分（`packages/github/README.md:1-20`）。

2. **请求/规格分离**（`packages/github/github/src/types.ts:50-110`、`github-local-rest/src/resolve.ts:23-83`）：模型面的是 `GithubRequest`（带 `kind` 枚举 11 种 + owner/repo + 可选过滤字段），`resolveGithubRequest` 是纯函数把它映射成 `GithubSpec`（method/path/query/body）。把「意图」与「REST 细节」解耦，使解析逻辑可脱离服务实例单测。

3. **平台卫生客户端库**（`packages/github/github/src/client.ts:10-95`）：`parseRateLimit`/`isRateLimited`/`retryAfterSeconds`/`backoffMs`（带抖动的指数退避）/`parseLinkNext` 全是对 header map 的纯函数，供实现层复用。区分了主限流（403 + `X-RateLimit-Remaining: 0`）与次级限流（429 或 `Retry-After`）。

4. **逐调用 token 解析**（`packages/github/github-local-rest/src/index.ts:115-135`）：每次 `call` 经 `ctx.credentials.resolve(credentialRef('GH_TOKEN'))` 取 token，**不缓存**——轮换 token 下一调用即生效；credentials seam 缺失时回退到 `process.env`，再缺则抛 `GithubTransportError`。HTTP 4xx/5xx **不抛**（作为普通 `GithubCallResult` 返回），只有传输/凭据失败才 reject（`packages/github/github/src/index.ts:55-75`）。

5. **11 个 `github_*` 工具**（`packages/github/tool-github/src/index.ts:18-24`、`issue-tools.ts`、`pr-tools.ts`）：issue 6 个（list/view/comments/comment/create/update）+ pr 5 个（list/view/diff/create/comment）。每个工具同时返回「无损结构化 JSON + 文本 render」；`github_pr_diff` 原始 diff 上限 200 KB 并带 `truncated` 标志；`github_pr_create` 对任意快照 base 创建、PR 号即时返回、单项失败不中断批量（`packages/github/tool-github/README.md:9-26`）。

6. **锚点插入式跟踪表维护**（`packages/github/tool-github/src/anchor.ts:16-40`）：`github_issue_update` 除整体替换正文外，支持 `anchorInsert`——按精确匹配的 marker 行（如 `## 维护约定`）在其前/后插入若干行，**不动其他段落**；marker 缺失即报错。专门服务「快照制协作」里那张跨仓跟踪总表。

7. **修复战役 skill**（`plugins/.../skills/github-issue-pr/SKILL.md`）：把快照制协作标准化为 7 步——拉 issue 批次 → 筛选排序（P0/P1/P2）→ 逐条修复 → 批量建 PR（base 永远是 `snapshots/<hash>`，PR 永不合并是设计）→ 锚点维护总表 → 上游挂「已修」链接 → 状态流转与交接。明确告诫「凭据不经 `git credential fill`」（无 tty 子进程下返回空）。

8. **验证状态**（`README.md` 末尾）：自述 45 个单测 × 3 轮全绿；本次实测 `grep -rE '^\s*(it|test)\('` 命中 45 处，与 README 数字一致（client 14 / resolve 11 / call 9 / tools 11 / anchor 5）；typecheck/lint/build clean；做过真实 API 冒烟（200 / rate-limit header / 404 路径）。

## 与 DeepSeek Harness 主仓库的集成点

本项目是 DSH 的**外挂插件**，不含上游源码，集成走两条 seam：

- **Skill 层（热重载、声明式）**：在 `~/.dsh/config.yaml` 的 `repository-plugins` 条目里写入 `github:dsh-external/dsh-github-integration#<commit-sha>&path:/plugins/github-integration/.dsh-plugin`，DSH 的 repository-plugin loader 挂载该目录，模型即获得 `github-issue-pr` skill。**约束**：`.dsh-plugin` 清单只能声明 `skills` / `mcpServers`，工具代码无法由此分发（`README.md` Step 1）。
- **工具层（一次性、需编译）**：把 `packages/github/` 下三个包拷进 DSH checkout 的 `packages/`，在 `tsconfig.host.json` 注册三个包目录，向 `tsconfig.base.json` 的 `paths` 追加 9 条 `@deepseek-ai/dsh-github*` / `dsh-tool-github*` 映射，`pnpm install && pnpm run build`，在 `cordis.yml` 组合 `github-local-rest` + `tool-github` 两个插件，最后配置 `GH_TOKEN`（`README.md` Step 2）。
- **运行时契约**：`github/` 的 `index.ts` 通过 `declare module 'cordis'` 给 `Context` 打了 `github: GithubService` 补丁；实现包 `LocalGithubRest extends GithubService` 注册服务；工具包 `inject: ['tools']` 且消费 `ctx.github`，seam 缺失时工具不注册并在调用时 fail loud 带 compose 提示（`tool-github/src/index.ts:18-24`）。token 经 `@deepseek-ai/dsh-credentials` 的 `credentialRef('GH_TOKEN')` 解析，与 DSH 凭据体系贯通。

## 亮点与风险

亮点：

- **seam 抽象干净**：请求/规格拆分 + 纯函数 resolver + 平台卫生纯函数库，三层职责清晰、可独立单测；想换传输（如 GitHub App JWT、GraphQL）只需新增一个 `GithubService` 子类。
- **逐调用 token、HTTP 错误不抛**：对长跑 agent 友好——token 轮换即时生效，4xx/5xx 作为数据返回供模型决策，仅传输/凭据失败中断。
- **快照制工作流的原生支持**：PR 号即时返回、批量逐项失败不中断、锚点插入保留非目标段落、`mergedAt` 缺失即「未吸收」——都是踩过坑后的设计（`SKILL.md` 「关键约定」6 条）。
- **双语 + 文档质量高**：每个包 README 都有中英双版，JSDoc 详尽，路线图与已知限制透明。

风险：

- **两层安装是手动的、易碎**：工具包无法走 `.dsh-plugin` 分发，每次升级要重新「拷包 + 改 tsconfig paths + 编译」（`README.md` Step 2）。`tsconfig.base.json` 的 9 条 `paths` 全靠人手追加，DSH 侧 base 配置一变就可能漂移；`catalog.json` 只 pin skill 插件的 commit，工具包版本与 DSH workspace 的对齐没有自动化校验。
- **认证仅 token-first**：GitHub App 安装令牌刷新（JWT→access token）与 OAuth PKCE 均未实现（`packages/github/README.md` Known Limitations），自动化/长跑 agent 场景受限；`GH_TOKEN` 是个人访问令牌，权限边界粗。
- **roadmap 缺口大**：无 `github_pr_review`（分级审查）、无 search/CI/repo-tree 工具、无 webhook 入站（事件驱动自动化缺位）；代码搜索 10 req/min 的限流需要先做缓存才能发工具（同上）。
- **快照制假设强**：「PR 永不合并、等下个快照吸收」是该社区特定协作模式；对标准「PR 合并进 main」的上游不适用，工具语义（如把 `mergedAt` 缺失当常态）会让外部使用者困惑。
- **私有仓库 + 单一版权方**：归 mattheliu 个人、dsh beta 成员内部使用、不得公开再分发（`README.md` Copyright）；治理与长期维护责任集中在单人。

## 维护状态

活跃。shallow clone 最新一笔 commit `8786280`「chore(catalog): pin plugin ref to i18n commit」时间戳 2026-08-05 07:05 +0800（即调研当天）；`catalog.json` 的 `updated` 字段亦为 `2026-08-05T07:10:00Z`。Wave 1（seam + REST 实现 + 11 工具 + 战役 skill）标记完成，Wave 2/3/4（PR review agent、webhook gateway、GitHub App/OAuth、search/CI 工具）在路线图上未勾选。45 个单测自述 3 轮全绿，typecheck/lint/build 自述 clean。

## 备注

- 顶层 `README.md`（4.7 KB）信息密度高、结构完整，是本项目最主要的入门材料；调研时直接引用其安装步骤与工具表即可，无需重复 Read 源码。
- 调研方法：因 github.com 页面 404（需 JS），改用 `git clone --depth 1`（成功，exit 0）+ 直接 Read 本地文件；用一次 `bash` 子进程核了 commit 时间、文件数与测试数（45，与 README 一致）。未运行 `pnpm build` / `vitest`（只读调研，且需要 DSH checkout 环境）。
- 本仓库与同批调研中的 `dsh-github-bridge`/`dsh-issue-filer` 等可能存在职能重叠（均涉及 GitHub issue/PR），主仓集成时需注意区分：本仓库是「结构化 GitHub 工具 + 战役 skill」，偏模型面工具；其余仓库偏具体通知/桥接。
