# 目录 × 运行级 矛盾审计（2026-08-14）

口径：README 兼容性列为静态四维编辑口径；运行级为 k8s agent 实测（公有生态）。
交集 116 / 目录 130。改写目录行属人工策展，本报告仅呈证据。

## 🔴 README 标「兼容」但运行级 ❌（3）

| 插件 | 分类 | 静态结论 | 运行级原因 |
|---|---|---|---|
| dsh-track | 🤖 Agent 能力 | 兼容 | FAIL: 缺少 DSH 平台依赖（~/.dsh/source/current 不存在、peerDependencies 为内部 @deepseek-ai 包、 |
| dsh-diff-viewer | 🗂 文件数据 | 兼容 | FAIL: 源码未编译（lib/ 目录不存在），且 devDependencies 中的 link: 本地路径依赖在当前环境无法解析 |
| session-persistence-rdb | 🗂 文件数据 | 兼容 | FAIL: peer dependencies on internal @deepseek-ai packages are not resolvable; Ty |

## 🟢 README 标「需适配/关注」但运行级 ✅（6）

| 插件 | 分类 | 静态结论 |
|---|---|---|
| dsh-split-panes | ❓ 其他 | 需适配 |
| dsh-slice-agent-loop | 🤖 Agent 能力 | 关注 |
| dsh-artifact | 🗂 文件数据 | 关注 |
| dsh-tool-encoding | 🗂 文件数据 | 关注 |
| dsh-companion | 🛠 基建部署 | 关注 |
| fabric | ❓ 其他 | 需适配 |

## 未覆盖

目录中 14 条无运行级数据（多为私有 org 仓，不在公有测试口径）。
