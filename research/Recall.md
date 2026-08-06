# Recall（dsh-external/Recall）调研摘要

## 一句话定位

Recall 是一个 **local-first 的 Rust CLI/TUI**，把本机所有 AI 编码 CLI（Claude Code、Codex、OpenCode、Cursor、Grok、Gemini、Copilot、Cline、Kiro、Antigravity、Pi）产生的会话统一索引到一个本地 SQLite 库中，提供全文/语义搜索、用量追踪、JSONL 导出/导入、会话分享与跨工具续接。上游为 `samzong/Recall`，`dsh-external/Recall` 是其在 dsh-external org 下的浅镜像（depth 1，仅 1 条 commit 可见）。

## 技术栈与依赖

- **语言/edition**：Rust 2024 edition；workspace 模式，主 crate `recall` v0.3.0 + 两个扩展 crate（`recall-probe`、`recall-reflect`）。
- **CLI**：`clap` v4（derive）+ `clap_complete`（shell 补全）。
- **存储**：`rusqlite` 0.32（bundled SQLite），向量用 `sqlite-vec` 0.1（通过 `sqlite3_auto_extension` 注册），全文用 SQLite FTS5。
- **语义向量**：`candle-core/nn/transformers` 0.10（macOS 走 Metal feature，非 macOS 默认 CPU，可选 `cuda` feature），模型固定 `intfloat/multilingual-e5-small`，经 `hf-hub`（ureq 后端）+ `tokenizers` 0.22 下载加载。
- **TUI**：`ratatui` 0.29 + `crossterm` 0.28 + `unicode-width`。
- **其它**：`walkdir`/`globset`（文件扫描）、`flate2`/`tar`/`zip`（打包）、`pulldown-cmark`（Markdown）、`kitup` 0.1.1（bundled agent skill 安装器）、`fs2`（文件锁）、`tracing`/`tracing-subscriber`。
- **发布**：`cargo-release` 驱动打 `v*` tag，GitHub Actions 矩阵构建 linux/macos/windows 二进制；Homebrew tap `samzong/tap/recall`；`publish = false`（不发 crates.io）。
- **文档站**：`website/` 是独立的 Next.js 16 + fumadocs + pnpm 项目，与 Rust crate 解耦。
- **基准**：`benches/recall.rs`（divan，经 `codspeed-divan-compat` 包装），由 `bench` feature 暴露 `src/bench_api.rs`，CodSpeed CI 跑。

## 文件结构概览

```
Recall/
├── Cargo.toml                # workspace 根，主 crate + 2 扩展成员
├── Makefile                  # make check = fmt --check → clippy -D warnings → test
├── AGENTS.md                 # 给 AI 编码 agent 的总指南（架构 + 边界）
├── DEVELOPMENT.md            # 加新 source adapter 的完整流程
├── README.md / README.zh-CN.md
├── src/
│   ├── lib.rs / main.rs      # 只暴露 init() + run()；其余 pub(crate)
│   ├── cli.rs                # clap 子命令派发（含 ext 外部子命令）
│   ├── adapters/             # 11 个工具适配器 + SourceAdapter trait
│   ├── db/                   # store/schema(migrate v1..v11)/search(FTS5+vec)/session_store...
│   ├── sync.rs               # 增量同步（35KB）
│   ├── session.rs            # session 子命令（33KB）
│   ├── share/                # HTML 渲染 + Cloudflare Pages 发布
│   ├── extension.rs          # 扩展宿主：catalog/install/dispatch（22KB）
│   ├── embedding.rs / semantic.rs   # candle 本地向量
│   ├── export.rs / import.rs        # JSONL 导入导出（schema v3 无损）
│   ├── usage.rs / handoff.rs / repo_identity.rs / skill_audit.rs / info.rs ...
│   ├── tui/                  # ratatui app + 后台搜索 worker
│   ├── integration/          # regression + eval_harness 测试
│   └── bench_api.rs          # 仅 bench feature 下编译
├── extensions/
│   ├── recall-probe/         # 官方参考扩展（无业务逻辑，验证 host 协议）
│   └── recall-reflect/       # 时间线反思扩展（recall reflect ...）
├── skills/
│   ├── recall/SKILL.md       # 嵌入二进制，recall skill install 安装（17KB）
│   └── reflect/SKILL.md      # 配 reflect 扩展
├── website/                  # Next.js + fumadocs 文档站
├── docs/                     # session.md / extensions.md（扩展契约设计文档）
├── benches/recall.rs
└── .github/workflows/        # ci / release / extension-release / pages / codspeed
```

## 核心功能与实现要点

1. **统一适配器抽象**（`src/adapters/mod.rs`）：`SourceAdapter` trait 定义 `id()/label()/scan()->Vec<RawSession>` 以及可选的 `scan_for_sync()`（增量）、`usage_parser_version()`、`resume_command()`、`app_command()`。所有 11 个适配器在 `all_adapters()`（`src/adapters/mod.rs:152-164`）注册一处即可被 DB schema、搜索、TUI 过滤、CLI `--source` 全部接管。`RawSession` 支持 builder 链式 `with_usage()`/`with_events()` 把 token/事件挂到同一会话上——**用量不是独立适配器**。

2. **增量同步 + SQLite 存储**（`src/sync.rs`、`src/db/schema.rs`）：扫描结果写入本地 `recall.db`，schema 已演进到 v11（`src/db/schema.rs:5`，逐版本 `migrate_v1..v11`）。存储按域拆分：`session_store`(41KB)、`event_store`、`usage_store`、`semantic_store`、`project_store`、`skill_audit_store`、`search`。后台 worker 由隐藏子命令 `__background-worker` 驱动。

3. **混合搜索**：FTS5 关键词 + `sqlite-vec` 向量（`src/db/search.rs`、`src/semantic.rs`）。向量由本地 candle 跑 e5-small 生成（`src/embedding.rs`），query/document 分别加 `"query: "/"passage: "` 前缀，mean-pool + L2 归一化（`src/embedding.rs:68-95`）。设备选择 CUDA→Metal→CPU（`select_device()`）。

4. **稳定 CLI JSON/JSONL 协议**（`src/lib.rs:27` `PROTOCOL_VERSION = 1`）：`recall info/session list/session show/search/export --format json|jsonl` 是机器接口，stdout 只出数据、进度走 stderr，字段只加不删改义。`recall export` 自 schema v3 起对索引无损，含 `source_file_path`、`parser_version`、`raw_usage_json`、`attrs_json`；`recall import` 接受 schema v2/v3 并按 `(source, source_id)` 去重。

5. **外部子命令式扩展系统**（`src/extension.rs`、`docs/extensions.md`）：扩展是独立二进制 `recall-<name>`，`recall <name>` 派发；必须应答 `--recall-extension-manifest` 输出 `{name,version,protocol,min_recall}`。扩展**只能**消费 CLI JSON 协议，禁止读 `recall.db` 或链 `recall` crate。核心/扩展边界明确：写索引/数据面/schema 归核心，纯消费协议的归扩展。`extensions/recall-probe` 是最小参考实现（`extensions/recall-probe/src/main.rs`），`recall-reflect` 是首个真业务扩展。catalog 在 `website/public/extensions/catalog.json`（CI 生成，禁手改）。

6. **会话分享到 Cloudflare Pages**（`src/share/publish.rs`、`src/share/render.rs` 44KB）：`recall share init` 配置一次，`recall session share --id ...` 把会话渲染成静态 HTML 发布到 Cloudflare Pages（wrangler）。支持 `--tldr-file` 附摘要、`--dry-run` 预览、`--copy-url`/`--open`。单资产上限 25 MiB（`src/share/publish.rs:17`）。

7. **跨工具续接 / handoff**（`src/handoff.rs`）：原生 `resume_command()` 调原工具 resume；不支持时走 handoff——把会话渲染成纯文本 prompt 喂给 codex/grok/claude/opencode 新会话（`src/handoff.rs:22-37`）。`repo_identity.rs` 用 git `remote get-url origin` 做 repo 身份解析缓存，支持 `--repo` 跨 worktree 过滤。

8. **Bundled Agent Skill**（`skills/recall/SKILL.md`）：经 `include_bytes!` 编入二进制，`recall skill install` 通过 kitup 安装到检测到的 agent。该 skill 把 Recall 当作"项目记忆层"：意图路由（分享/续接/查找/审查/反思）、项目作用域默认（含 repo identity 跨 worktree）、深度分级（quick scan / standard / deep export）、输出协议（历史事实→重复风险→失败路径→偏好→待验证假设→下一步）。

## 与 DeepSeek Harness 主仓库的集成点

**无直接集成**。Recall 是通用的本机会话索引工具，上游为独立的 `samzong/Recall` 项目，被镜像到 `dsh-external/Recall`。它与 DeepSeek Harness 主仓库的关系仅是：可被 harness 用户当作**外部工具**安装使用（`brew install samzong/tap/recall` + `recall skill install`），由其 bundled skill 在 agent 内部以 shell 调用 `recall ...` 的方式查询本地索引。没有任何 Rust/JS API、共享 schema、共享配置或构建依赖将其与 harness 主仓绑定。注意：源码里的 `src/adapters/pi.rs` 中的 "Pi" 是另一个 AI 编码工具（Pi CLI），与 omp/pi-adapter 无关。

## 亮点与风险

**亮点**

- **边界纪律严**：核心只暴露 `init()/run()`，内部一律 `pub(crate)`；`publish=false`、`protocol_version` 显式稳定、SQLite schema 显式不稳定、扩展走外部子命令而非 dylib/WASM——`docs/extensions.md` 把选型理由（cargo/gh 风格外部子命令 vs Nushell provider / WASM / dylib / cargo features）记录在案。
- **文档完备**：`AGENTS.md`（根 + adapters/db/tui/extensions/skills/website 各一份）、`DEVELOPMENT.md`（加适配器全流程 + CI 说明）、`docs/extensions.md`（442 行扩展设计 + 稳定性规则 + 高频消费者未来路径）、`docs/session.md`、中英双语 README。
- **本地优先 + 隐私**：所有索引、向量、模型权重都落本地；分享是显式动作并提示可能泄密。
- **CI 即本地**：`make check` 与 CI 同命令（fmt → clippy -D warnings → test），无 CI-only 逻辑；CodSpeed 性能回归监控；DCO signoff hook（`.githooks/prepare-commit-msg`）。
- **适配器覆盖广**：11 个工具全覆盖搜索/全索引/增量/语义/导出，用量追踪 7 个，resume 8 个。

**风险**

- **依赖体积/构建成本**：candle + tokenizers + sqlite-vec(bundled) + rusqlite(bundled) 让二进制偏重，首次语义搜索需下载 e5-small 权重（`src/embedding.rs:106`）。
- **schema 漂移**：已到 v11（`src/db/schema.rs:5`），迁移频繁；`publish=false` + SQLite schema 显式不稳定，任何第三方直读 `recall.db` 都可能被破坏。
- **外部依赖**：分享硬绑 Cloudflare Pages + wrangler（`src/share/publish.rs`），模型下载依赖 hf-hub/ureq 直连 huggingface.co。
- **macOS 偏置**：candle 在 macOS 默认 Metal feature，非 macOS 才是 CPU/CUDA，Linux/Windows 上语义搜索性能取决于 CPU。
- **上游单维护者**：`samzong/Recall` 单人维护（PR 编号到 #117），dsh-external 仅是浅镜像，无独立 roadmap；如需定制需自行 fork 或上游提 PR。
- **catalog 文件易误改**：`website/public/extensions/catalog.json` 由 release CI 生成，但物理上是普通 JSON，手改不会触发告警。

## 维护状态

**活跃**。上游 `samzong/Recall` 最新 commit `2026-08-02`（feat(bench): add CodSpeed performance benchmarks, #117），距今 4 天；当前版本 v0.3.0；CI（ci.yml/release.yml/extension-release.yml/pages.yml/codspeed.yml）齐全；Homebrew tap 可装。`dsh-external/Recall` 是 depth=1 的浅镜像，仅含 1 条 commit，无独立开发活动。

## 备注

- LICENSE: MIT。
- dsh-external 仓与上游 `samzong/Recall` 的同步策略未知（浅克隆看不出 mirror 配置）；如要追踪，建议以上游为准。
- 与 dsh harness 主仓无任何代码/配置耦合，归类应放在"外部可选工具"而非"集成的子项目"。
- 调研基于 `git clone --depth 1` 的快照（HEAD = 29bbdde, 2026-08-02），未跑 `cargo build`（只读调研，且本机无 Rust toolchain 验证计划）。
