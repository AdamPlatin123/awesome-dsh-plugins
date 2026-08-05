# dsh-external/dsh-session-search 调研摘要

## 一句话定位
DeepSeek Harness 的**外部 Cordis 插件**，为本机 dsh、Codex、Claude Code、pi、OpenCode 五种 agent 的历史会话建立 SQLite FTS5（trigram 分词）全文索引，并向模型暴露 `agent_session_search` / `agent_session_read` 两个工具；只读、跨源、子串级匹配（含中文）。

## 技术栈与依赖
- **语言/编译**：TypeScript 5.9，`scripts/build.sh` 用 dsh 主 checkout 的 tsc 编译 `src/` → `lib/`（`lib/` 提交进 git），ESM。
- **运行时**：Node.js（依赖 Node 22.13+ 的 `node:sqlite` `DatabaseSync` 和 `node:zlib` `zstdDecompressSync`），通过 Cordis `Context` + `ctx.tools.register` / `ctx.systemPrompt.section` 注入。
- **peerDependencies（由宿主 dsh 提供）**：`@deepseek-ai/dsh-session`、`@deepseek-ai/dsh-system-prompt`、`@deepseek-ai/dsh-tools`、`cordis ^4.0.0-rc.7`。
- **直接 dependencies**：仅 `schemastery ^3.18.0`（配置 schema）。
- **包名**：`@dsh-external/dsh-session-search`，私有包，license BSD-3-Clause，`engines.dsh >= 0.0.1`。
- **dshx contribution**：声明贡献 `tools: ["agent_session_search", "agent_session_read"]`，无 skills。

## 文件结构概览
```
dsh-session-search/
├── package.json              # 包定义 + dshx contribution
├── tsconfig.json
├── README.md / README.en.md  # 中英双语说明
├── scripts/build.sh          # 借 dsh checkout 的 tsc 编译，建立符号链接到 vendored 依赖
├── src/                      # TypeScript 源码
│   ├── index.ts              # 插件入口：注册工具 + 系统提示
│   ├── types.ts              # AgentSessionRecord / AgentMessageRecord / AgentSearchHit
│   ├── discovery.ts          # 五源文件发现 + 默认根目录
│   ├── parsers.ts            # 五源解析器（dsh zstd 多帧、codex/claude/pi JSONL、opencode SQLite）
│   └── db.ts                 # SQLite 索引层：schema、增量索引、FTS5 trigram 检索
├── lib/                      # 编译产物（已提交）
│   ├── *.js + types/*.d.ts
└── tests/                    # 7 个 .mjs 测试
    ├── smoke.mjs             # 索引真实会话并搜索的冒烟
    ├── query-safety.mjs      # FTS5 注入防御
    ├── parser-correctness.mjs
    ├── dsh-frames.mjs        # zstd 多帧扫描
    ├── index-lifecycle.mjs   # 增量/清理
    ├── query-bounds.mjs      # maxMatchRows 边界
    └── schema-reset.mjs      # schema 版本重置
```

## 核心功能与实现要点

1. **跨源全文搜索工具**（`src/index.ts:140-220`）：注册 `agent_session_search`（按会话分组的命中 + 最强匹配消息 + snippet + 上下文窗口）和 `agent_session_read`（单会话元数据 + 可定位 `aroundSeq` 的消息窗口）。参数支持 `sources`/`cwd`/`sort`/`limit`，输出统一 JSON 文本，长消息 `clip()` 到 600 字符。

2. **五源会话发现**（`src/discovery.ts:60-130`）：默认根目录基于 `homedir()`，可用 `roots` 配置覆盖；dsh 走 `~/.dsh/sessions/**`（depth ≤4），codex 走 `~/.codex/sessions` 与 `archived_sessions`，claude 走 `~/.claude/projects`（显式跳过 `agent-` 前缀的 subagent 转录），pi 走 `~/.pi/agent/sessions`，opencode 直接定位 `~/.local/share/opencode/opencode.db` 单文件。

3. **FTS5 trigram 索引**（`src/db.ts:130-200`）：schema 包含 `sessions` / `messages` / `messages_fts`（`tokenize='trigram'`）/ `artifacts` 四张表；trigram 让中英文都能做子串匹配（unicode61 无法匹配中文子串）。schema 版本当前为 3，`user_version` 升级触发原地重置。

4. **dsh 多帧 zstd 解码**（`src/parsers.ts:135-260`）：dsh 会话日志是「每批事件一帧」拼接的 zstd 流，Node 的 `zstdDecompressSync` 只解首帧。插件自行实现 `scanZstdFrames()` 结构化扫描帧边界（magic 0xfd2fb528、frame header、block header、checksum），逐帧解码，遇到末尾撕裂帧（写入中断）跳过等下次索引补上；该扫描逻辑显式镜像主仓库 `dsh-session-persistence-jsonl` 的容器格式，保持单向兼容。

5. **增量索引 + 显式 FTS 维护**（`src/db.ts:240-310`）：按 `(mtime, size)` 跳过未变文件，消失的会话/artifact 自动清理；FTS5 同步显式按 `rowid` INSERT/DELETE（注释明确：FTS5 `'delete'` 特殊命令在部分 SQLite 构建上不可靠）。索引前后再次 `stat` 比对，规避并发写入竞争。

6. **查询安全**（`src/db.ts:80-100` quoteFtsQuery）：用户输入 `"` 加倍后整体包成 FTS5 phrase，使 `-`/`:`/`*` 等全部当作字面数据；短查询（`searchableChars < 3`）退化为 `unicode_contains` 自定义函数的 LIKE 匹配，snippet 回退为命中消息正文。`maxMatchRows`（默认 1000）限制单次物化的会话级结果上限。

7. **opencode 只读访问**（`src/parsers.ts:500-598`）：用 `DatabaseSync` 打开 opencode.db，开启 `PRAGMA query_only`，从 `session` / `message` / `part` 三表拼装会话与消息；任何解析异常整体返回 `undefined`，跳过该 artifact。

8. **系统提示注入**（`src/index.ts:107-118`）：注册 `systemPrompt.section`（order=115，name `tool:dsh-session-search`），引导模型在跨会话语境时调用这两个工具。

## 与 DeepSeek Harness 主仓库的集成点
- **插件挂载**：通过 `dshx install` 或手动在 `~/.dsh/config.yaml` 添加 `Loader` 节点，`main` 指向 `lib/index.js`；与主仓库共享 Cordis 容器与 `ctx.tools` / `ctx.systemPrompt` 服务（`inject: ['tools', 'systemPrompt']`）。
- **依赖**：以 peerDependency 形式依赖主仓库的 `@deepseek-ai/dsh-tools`（`defineTool`）、`@deepseek-ai/dsh-system-prompt`（类型 augmentation）、`@deepseek-ai/dsh-session`、`cordis`；构建脚本 `scripts/build.sh:35-55` 通过符号链接到 dsh checkout 的 `packages/core/*` 与 `vendor/*` 复用其 node_modules。
- **格式兼容**：dsh 解析器显式声明「镜像 `dsh-session-persistence-jsonl` 的 `scanZstdFrames()`」，与主仓库会话日志的容器格式保持单向兼容；schema 设计声称沿用「pi 的 session-search extension」已验证的 schema。
- **与「session-query」的关系**：本仓库无任何对「session-query」的引用。`package.json` 中无该名 peerDep，源码无 import。结论：此插件与主仓库可能的 `session-query` 模块**没有直接耦合**——它是独立的跨 agent 索引/检索层，仅通过 dsh 工具注册机制与主仓库会话格式对接。功能上若主仓库有内置 session 查询能力，本插件可视为其**跨源外扩**（把 codex/claude/pi/opencode 也纳入同一索引）。

## 亮点与风险
- **亮点**：trigram + phrase 转义彻底防 FTS5 注入（`src/db.ts:80-100`）；增量索引 + 二次 stat 比对规避并发写入（`src/db.ts:262-280`）；dsh 多帧 zstd 结构化扫描优雅处理拼接流与撕裂末帧（`src/parsers.ts:135-260`）；五源**严格只读**（opencode `query_only`，其它源仅 `readFile`/流式 readline），索引独立 DB `$DSH_HOME/session-search.db`。
- **风险 1（依赖前沿 Node API）**：硬依赖 `node:sqlite` `DatabaseSync`（Node 22.13+ 才稳定）与 `node:zlib` `zstdDecompressSync`，老版本 Node / 非官方构建会直接不可用（`src/db.ts:120`、`src/parsers.ts:18`）。
- **风险 2（默认全量索引）**：`indexOnSearch=true` + 五源默认全开，每次搜索前都会扫描全部根目录并触发增量索引，会话规模大时首搜延迟与 I/O 压力可观（`src/index.ts:80-84`）。
- **风险 3（单例 + 同步阻塞）**：`SessionSearchDb` 单连接、`zstdDecompressSync` 同步解压，长会话索引时可能阻塞事件循环；虽有 `MAX_FILE_BYTES=64MB` / `MAX_DECOMPRESSED_BYTES=64MB` 上限（`src/parsers.ts:22-30`），但仍是粗粒度。
- **风险 4（opencode 模式脆弱）**：opencode 任意行 JSON 解析失败会令整 artifact 返回 `undefined` 跳过（`src/parsers.ts:555-560`），单条损坏 part 会让该 db 整体不进索引。
- **风险 5（新仓、未稳定）**：仓库 2026-08-05 当天 7 个 commit 全部集中创建（见维护状态），尚无外部使用反馈。

## 维护状态
- **创建时间**：2026-08-05（与第二批调研同日新建）。
- **提交历史（共 7 次提交，全部 2026-08-05）**：
  - `c203b2a` feat: cross-agent session full-text search plugin（功能首落）
  - `528a092` fix: treat search queries as literal FTS5 phrases
  - `528ee00` fix: decode all concatenated zstd frames in dsh session logs
  - `d487648` fix: preserve parser isolation and valid indexes
  - `4b3bbaf` fix: make indexing incremental and atomic
  - `6721d44` fix: bound search rows and honor windows
  - `f538ab6` fix: compute per-hit FTS5 snippets in the main query（HEAD）
- 单日密集修复，6 个后续 fix 都在收口首版发现的边界问题；说明作者活跃但仓库刚起步、尚未发布稳定 tag。
- **无 LICENSE 文件**（package.json 声明 BSD-3-Clause 但仓库根目录无 LICENSE 文本）。
- **无 CI 配置**（无 `.github/workflows`）。

## 备注
- 仓库空状态：否，源码完整可编译，lib/ 已提交编译产物。
- 脱敏：无作者邮箱/真名字段进入本摘要。
- 与 dsh 主仓库关系定位清晰：外部插件（External Plugin），通过 dshx/Loader 挂载，与主仓库松耦合；非主仓库子模块。
- 与「session-query」：本仓库代码与 package.json 中**无任何 session-query 字样**；如主仓库存在同名模块，二者无直接依赖或调用关系。
- 测试覆盖范围（7 个 `.mjs`）较扎实：query 安全覆盖 FTS5 注入、parser 正确性、dsh 多帧、索引生命周期、查询边界、schema 重置、冒烟。
