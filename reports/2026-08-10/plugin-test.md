# 插件可用性测试报告（2026-08-10）

## L1 静态清单校验（全量）

- 通过：109 / 失败：19（扫描含清单仓库 128 个）
- 失败仓库：` deepseek-harness-desktop(pkg-name-main) deepseek-harness-distro(pkg-name-main) dsh-agent-budget(pkg-name-main) dsh-club(pkg-name-main) dsh-companion(pkg-name-main) dsh-crew(pkg-name-main) dsh-grok-tui(pkg-name-main) dsh-my-rsi(pkg-name-main) dsh-opencode-server(pkg-name-main) dsh-paseo(pkg-name-main) dsh-plus(pkg-name-main) dsh-web-ui(pkg-name-main) dshx-update-check(pkg-name-main) group-chat-diary(pkg-name-main) marisa(pkg-name-main) oh-my-dsh(pkg-name-main) repo-visibility-guard(pkg-name-main) session-persistence-rdb(pkg-name-main) toybox(pkg-name-main)`

## L2 加载冒烟

- 未执行

## L3 工具调用

- 未执行

## 说明

- L1 只校验清单结构（JSON 合法/name+main/contributes），不校验运行时
- L2 在构建产物 dsh 实例（0.0.1）上挂载插件跑空任务，验证 apply 无报错
- L3 需要 DEEPSEEK_API_KEY，headless 任务触发插件工具
