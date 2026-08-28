# 稳定数据接口（schema `dsh-radar/v1`）

供第三方（插件市场、导航站、下游工具）消费的机器可读清单。raw.githubusercontent.com 即稳定 CDN，无需自建服务。

## 端点

| 文件 | 内容 | 更新节奏 |
|---|---|---|
| [`data/latest.json`](../data/latest.json) | 快照指针 + 七档统计（小文件，可高频轮询） | 随每次渲染（至少每日） |
| [`data/plugins-all.json`](../data/plugins-all.json) | 全量扁平清单（repo/verdict/stars/desc） | 随每次渲染（至少每日） |
| `data/snapshots/*.json` | 原始快照（15 分钟粒度，滚动） | 不承诺保留窗口 |

消费示例：

```sh
curl -s https://raw.githubusercontent.com/AdamPlatin123/dsh-plugin-radar/main/data/latest.json
```

## 字段

`latest.json`：

- `generated_at` — 导出时间（UTC）
- `snapshot_run_id` — 锚定的雷达快照轮次
- `stats` — 七档统计：`ok`（运行级可用）/ `incompatible` / `pending` / `untested` / `gone`（空仓监测）/ `ambiguous`（歧义监测）/ `unlocated`
- `total_listed` — 清单条目总数

`plugins-all.json` → `plugins[]`：

- `repo` — `owner/name`（GitHub canonical）
- `name` — 展示名
- `verdict` — 七档之一，语义同上
- `stars` — 星数；**`null` 表示未知（缺值，非 0）**，排序时请跳过 null 而非按 0 处理
- `desc` — 一句话描述（可为空串）

## 兼容承诺

v1 字段**只增不删**；语义变更会新增字段并保留旧字段至少一个过渡期，变更公告见 [CHANGELOG](../CHANGELOG.md)。判定口径详见 [PLUGINS-ALL.md](../PLUGINS-ALL.md) 头部说明——**收录 ≠ 兼容 ≠ 运行可用**，请按 verdict 过滤后再展示。
