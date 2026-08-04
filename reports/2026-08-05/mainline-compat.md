# mainline 兼容性报告（2026-08-05）

- mainline：`02d7555`（snapshots/20260804T143803Z）
- 上次对比：`02d755595816a6d384033c96fb67a1fda3b28228`
- 兼容性：14/15 无需适配，1 需适配（dsh-working-activity）；其中关注 0、占位 4、不适用 2

## 兼容性矩阵

| 仓库 | 锚定 | 补丁 | seam | peerDeps | 综合判定 |
|---|---|---|---|---|---|
| issues | 未知 | 不适用 | 不适用 | 不适用 | 不适用 |
| dsh-live-stats | 未知 | 无补丁 | 缺: tuiPrompt | 7 项匹配 | 兼容 |
| dsh-working-activity | 未知（非 commit 锚定: 20260804T143803Z） | CONFLICT（1 个补丁中 0 个 OK） | 缺: tuiPrompt | 4 项匹配 | 需适配 |
| plugin-registry | 未知（非 commit 锚定: 20260804T143803Z） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 11 项匹配 | 兼容 |
| sandbox-mxc | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| web-components | 未知（不同谱系） | OK（1 个补丁全部干净应用） | 缺: tuiPrompt | 4 项匹配 | 兼容 |
| dsh-opencode-server | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| toybox | 未知（catalog ref，非 mainline 锚定） | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| ex-setting | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| tg-bot | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 12 项匹配 | 兼容 |
| group-chat-diary | 未知 | 不适用 | 不适用 | 不适用 | 不适用 |
| dsh-skins | 未知（不同谱系） | 无补丁 | 缺: tuiPrompt | 5 项匹配 | 兼容 |
| dsh-coding-receipt | 未知 | 不适用（空仓库） | 不适用（空仓库） | 不适用 | 占位 |
| qqbot | 未知 | 无补丁 | 缺: tuiPrompt | 无 dsh-* 依赖 | 兼容 |
| dsh-subagent-tree | 未知 | 无补丁 | 缺: tuiPrompt | 6 项匹配 | 兼容 |

## mainline 变更分析（02d755595816a6d384033c96fb67a1fda3b28228 → 02d7555）

### 关键变更

- **WebSocket 下行通道新增**：packages/client/connection/src/websocket-downlink.ts 及其测试进入 mainline（架构 note 2026-08-04-websocket-downlink-carrier），远程通道类插件可对齐。
- **包级变化**：packages/ 下删除 0 个包目录、新增 0 个文件（diffstat 见下）。

### 删除 / 新增包

删除的包目录：

新增文件：
```

```

### seam 符号变化

| 符号 | prev 文件数 | cur 文件数 | 变化 |
|---|---|---|---|
| `ThemeService` | 26 | 26 | 存在 → 存在（稳定） |
| `settingsNamespace` | 16 | 16 | 存在 → 存在（稳定） |
| `sessionProjections` | 21 | 21 | 存在 → 存在（稳定） |
| `tuiPrompt` | 0 | 0 | 缺失 → 缺失 |
| `slots` | 15 | 15 | 存在 → 存在（稳定） |
| `session/event` | 48 | 48 | 存在 → 存在（稳定） |

### diffstat（packages/ patches/ workspace）

```

```

## 破坏性变更清单

- 本日快照未发现 seam 符号级破坏。

## 插件侧建议（按仓库）

### issues
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### dsh-live-stats
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-working-activity
- 需适配：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁状态「CONFLICT（1 个补丁中 0 个 OK）」；建议以当日 snapshot HEAD（02d7555）为新基线重新锚定/rebuild 补丁。
- 补丁冲突/缺文件点集中在 mainline 变更分析节列出的破坏面，优先把集成改到稳定 seam（slots/sessionProjections/ThemeService）上。
### plugin-registry
- 兼容：锚定 20260804T143803Z（未知（非 commit 锚定: 20260804T143803Z））、补丁「OK（1 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 20260804T143803Z 显式记录到 README/补丁头，快照一漂即可自动预警。
### sandbox-mxc
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### web-components
- 兼容：锚定 b4b67f0（未知（不同谱系））、补丁「OK（1 个补丁全部干净应用）」，当日 mainline 可干净集成。
- 建议把补丁基线从 b4b67f0 显式记录到 README/补丁头，快照一漂即可自动预警。
### dsh-opencode-server
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
- 定位与 TUI 移除直接相关（opencode 替换 TUI），值得跟踪首 commit。
### toybox
- 兼容：锚定 未知（未知（catalog ref，非 mainline 锚定））、补丁「无补丁」，当日 mainline 可干净集成。
### ex-setting
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
### tg-bot
- 兼容：锚定 fa3d357fc66102d82f0ddbf67fd3d5d70944d8f7（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### group-chat-diary
- 非代码仓库（issue 跟踪 / 归档产物），无代码级集成，不参与补丁/seam 对比。
### dsh-skins
- 兼容：锚定 f1792735（未知（不同谱系））、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-coding-receipt
- 占位仓库（0 commit），无集成点可对比；建议首个 commit 落地后再纳入兼容跟踪。
- 输入来自 DSH session log，建议在 mainline 会话持久化格式稳定后实现。
### qqbot
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。
### dsh-subagent-tree
- 兼容：锚定 未知（未知）、补丁「无补丁」，当日 mainline 可干净集成。

## 主仓库侧建议

### 主仓库侧（dsh2026/test-AdamPlatin123）
- 快照分支与 master 不同谱系（如 web-components 锚定的 master b4b67f0 不在 snapshots 分支历史内），外围仓库无法自动判定前后关系；建议在每个快照分支 README/发布说明中公告 HEAD commit 与变更清单。
- seam 公共面本日保持稳定（slots/sessionProjections/ThemeService/settingsNamespace/session event 全部存在）；建议把公共 seam 面列入快照 release notes 的稳定性承诺。
- TUI 移除属破坏性变更（packages/ui/tui 全删、pi-tui 补丁移除、tuiPrompt 符号消失）；建议在快照说明中列出删除的公共包与替代面，供外围仓库提前适配。
- 新增 WebSocket 下行通道（connection/websocket-downlink）；建议补充协议文档，供 qqbot/tg-bot 等远程通道插件对齐。
