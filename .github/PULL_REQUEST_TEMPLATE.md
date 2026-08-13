<!--
  插件登记 PR 模板 —— 按此格式提交，合并后立即进入目录。
  目标文件：PLUGINS.md（表格追加一行即可）。
-->

> 📌 **标题格式**：`docs: 登记 <插件名>`（示例：`docs: 登记 dsh-balance`）——请勿使用其他标题格式。
>
> 🛠 **合并小贴士（重要）**：请让维护者能帮你 rebase——两种方式任选其一：
> 1. 提交 PR 后，在 PR 页面右侧勾选 **Allow edits from maintainers**；
> 2. 或在自己 fork 仓库的 Settings → General 勾选 **Allow edits and access to secrets by maintainers**（一次开启，以后所有 PR 自动允许）。
>
> 🙏 **致歉说明**：最近 README/PLUGINS.md 正在高速更改中（每日快照更新 + 分类体系重构），多个 PR 同时登记同一区域时可能产生冲突，处理可能稍显延迟，请见谅。

## 插件信息

| 项 | 值 |
|---|---|
| 插件名 | <!-- 与 repo 名一致，如 my-plugin --> |
| 仓库 | <!-- 如 https://github.com/dsh-external/my-plugin --> |
| 一句话说明 | <!-- 功能描述 --> |
| 版本 | <!-- 如 0.0.1 --> |

## 自检清单（提交前逐项确认）

- [ ] package.json `name` 使用 `@dsh-external/*` scope（未占用 `@deepseek-ai/*` 保留命名空间）
- [ ] 仓库已打 `dsh-plugin` topic
- [ ] 已在 PR 页面勾选 **Allow edits from maintainers**（或已在 fork Settings → General 开启同项，一次开启后续自动生效）
- [ ] 所有运行时依赖已声明（`dependencies` / `peerDependencies`）
- [ ] 已按自检三步实测通过：

```bash
# 1. 安装最新 dsh 并加载你的插件
dsh --profile headless --patch <(printf -- '- insert:\n    - id: my-plugin\n      name: @dsh-external/my-plugin\n') "hi"
# 2. 无报错即通过加载级；有报错按提示修依赖声明
# 3. 声明所有运行时依赖（react 等）到 package.json dependencies
```

- [ ] 自检结果贴这里：<!-- 如「加载成功，工具 X 调用正常」或贴报错说明 -->

## 改动内容

<!-- PLUGINS.md 追加的行（直接贴出）：-->

| 插件 | 仓库 | 说明 |
|---|---|---|
| <!-- 插件名 --> | <!-- 仓库链接 --> | <!-- 说明 --> |

## 备注

<!-- 可选：已知问题、待适配项、想被雷达重点跟踪的维度等 -->
