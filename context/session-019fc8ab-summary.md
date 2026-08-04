# 旧 session 019fc8ab 调研上下文归档

> 来源：`omp --resume 019fc8ab-0b11-7000-a24f-eb6cb8b80fb0`
> 会话文件：`/home/adam/.omp/agent/sessions/--mnt-shared-_Projects-test-AdamPlatin123--/2026-08-03T17-28-00-529Z_019fc8ab-0b11-7000-a24f-eb6cb8b80fb0.jsonl`
> 归档日期：2026-08-05

## 会话任务概述

在 deepseek-harness 快照仓库（test-AdamPlatin123，分支 `snapshots/20260804T143803Z-6feab99fdf`，commit `02d7555`）上执行的多阶段调研：

1. **磁盘 I/O 静态调研**：追踪事件、模型请求、工具调用、查询、轮询、并发请求是否把文件/数据库操作带入高频路径
2. **远端部署与端到端测试**：代码库+调研内容复制迁移到 `ssh -tt -p 2222 adam@127.0.0.1 'bash -lc "herdr"'`，自动化安装部署，端到端查询、边缘情况测试，准备原子化 issue 列表
3. **版本差异分析**：拉取最新版本，对比旧快照（770 files changed, 12,564 insertions, 30,749 deletions）
4. **群聊讨论对齐**：参考 127.0.0.1:5030 MCP 的 DSH 讨论内容，核验代码库中被 ban、已解决、已 issue 未解决的操作

## 关键产出 1：磁盘 I/O 调研结论

报告文件：`test-AdamPlatin123/.scratch/disk-io-investigation.md`（178 行，静态源码追踪，未运行测量）

### 四类确认的高频产品写盘路径

| 风险 | 路径 | 触发与复杂度 |
|---|---|---|
| 高 | 会话持久化检查点 | `session-checkpoint-policy` 在每个模型请求、顶层工具执行、agent step 边界调 `ctx.sessions.flush`；JSONL 每批次 fsync，SQLite 每批次一个事务 |
| 高 | JSON KV 与会话投影缓存 | `storage-json` 每次单记录更新整文件原子重写（临时文件+fsync+rename+目录 sync）；`session-projection-cache` 事件数/时间节流但 JSON 后端放大为整文件重写 |
| 高 | SQLite 会话全文查询 | 每次搜索先 `_reconcile`：全表 SELECT + 两次 `listSnapshots` + 活跃会话复制/建文档/SHA-256；翻页每页重复；全部排在单一 Promise 尾部 |
| 高 | 开发 HMR / TUI 补全 / Web 静态服务 | HMR 默认 500ms × bundle 数 × `statSync`（仅 dev）；TUI `@` 查询最多遍历 10,000 条目且工具结果使索引失效；静态服务每请求 `readFile` 无缓存 |

### 跨包写放大链

```
session/event → coordinator 批量 drain → JSONL appendLines(open+stat+write+sync)
                                       → SQLite appendBatch(BEGIN + N×INSERT + COMMIT)
llm/stream / tools/execute / agent/step → checkpoint-policy flush（等待 pending 落盘）

tool-session-query 翻页 → searchSessions → _serialized 单尾队列 → _reconcile
  → 两张索引表全表 SELECT → listSnapshots(before) → 脏会话 inspect+clone+SHA-256
  → listSnapshots(after) → BEGIN IMMEDIATE 删+重建 FTS5 文档 → MATCH

session/event → projection-cache dirty → writeEveryEvents/Interval 或 turn/end
  → sessions.flush → put → storage-domain 写链 → JSON 整文件重写（若路由 JSON）
```

### 待实测假设

HMR invariant 是否覆盖自身轮询器、workspace.status 是否被 UI 周期调用、webserver 无缓存是否成热点、settings/credentials watcher 真实轮询量、JSON 后端是否 projection-cache 部署路由、查询 reconcile 真实规模、spill 缺少 fsync 的崩溃丢失窗口。

### 观测命令建议

`strace -f -ttt -e trace=openat,close,read,write,fsync,fdatasync,rename,getdents64 -p <PID>`、`iostat -xz 1`、`lsof -p <PID>`。

## 关键产出 2：版本差异（旧快照 25b2ad4f67 → 新快照 6feab99fdf）

- **TUI 产品包整体移除**：`packages/ui/tui` 删除、CLI 中 TUI 配置/入口/向导删除、`--interface=tui` 选项移除；SDK 只保留 `acp` 和 `embed`。依据 Agent Note `2026-08-04-remove-tui-package.md`：Web 是保留的交互式产品
- **Web 连接层改 WebSocket 下行**：`packages/client/connection/src/client/websocket-downlink.ts`，上行 HTTP 不变，两条下行流承载 mux 和 host 数据
- **九项发布说明均有源码证据**：内置 ripgrep（`packages/fs/tool-fs-search/src/search-core.ts`）、回合运行时长、`web_search` 完整结果滚动、长输入光标、信号退出与遥测收尾、Thinking 尾部跟随滚动、长对话切换滚动位置保持、侧边栏滚动条统一

### 对齐结论（只读，未运行验证）

- Web 端近期修复有代码+Agent Note+测试覆盖
- "历史加载已优化"只解决首屏返回上限，**未解决超大会话端到端内存与全量读取问题**
- 群聊宣称的 `dsh.plugin.json` 插件系统不在快照中；实际只有受限的 `.dsh-plugin/package.json` 格式（注：现 dsh-external/plugin-registry 已实现该协议，见 research/plugin-registry.md）
- 安全边界、审计日志、压缩保真、后台任务资源上限仍有源码证据问题

## 关键产出 3：backlog issue 草案（local/backlog-issues.md）

- **#47 [proposal][protocol] ContentBlock 语义分裂**：harness/MCP/ACP 三协议同名不同物（`ContentBlockMap` text 系 vs MCP 封闭 union 多模态 vs ACP 能力声明制）；MCP 入口有损投影（`[image: png, content discarded]`）、ACP 入口直接拒绝、harness 无多模态类型、存储不可重构——"Model-visible ⟺ logged" 不变量被击穿；建议双向映射层 + 多模态核心类型 + 协议能力对齐
- **#58 [proposal][persistence] 流式 Delta 事件持久化改造**：`assistant/chunk` 全量落盘导致写放大 O(tokens)；方案为事件持久性分级（瞬时事件不落盘，仅内存分发），`assistant/message` 组装后一次写入；可选 `stream/replay` 聚合事件兜底
- **#79 [web][suggestion] 交互设计建议汇总**：11 个功能点（undo/fork/edit/图片上传/排队消息/活动面板/工作区浏览/中止命令/中止子 Agent/context 预警），7 个部分已有、4 个新增

## 对本次超级调研的衔接价值

1. **issue 仓库地址变化**：旧 session 发布到 `dsh2026/issues`；现 org 名为 `dsh-external`，issues 仓库已迁移（README 指向 dsh-external/issues）
2. **磁盘 I/O 四类热点**是评估各插件（live-stats、working-activity 等）与主仓库持久化交互的背景基线
3. **插件格式演进**：旧 session 发现主仓库只有 `.dsh-plugin/package.json`；plugin-registry 仓库的 `dsh.plugin.json` 是下一形态——两代格式并存是生态分析的关键事实
4. **TUI 移除**解释了 dsh-opencode-server 仓库的动机（用 opencode 换 TUI）
