# 插件分类标准（taxonomy v2 · 固定版）

> 本标准是 bot 提 PR、人工登记与自动分类器的**唯一分类依据**。13 类按下列顺序声明，规则引擎按声明顺序首个命中者胜。改动本文件需同步 `scripts/classify.py`（规则同源）。

## 类目与判定规则

| 顺序 | 类目 | 定义 | 关键词规则（名称/描述，不区分大小写） |
|---|---|---|---|
| 1 | 🎓 技能包 | 以 skill 形态提供能力：技能集合、技能分发、技能搜索 | `skill / 技能` |
| 2 | 🧠 记忆增强 | 跨会话/长期记忆、检索、蒸馏 | `mem(memory/memories) / 记忆 / recall / 遗忘 / 蒸馏 / distill` |
| 3 | 🎨 主题皮肤 | 仅改观感不改功能：主题、皮肤、CSS、像素装饰、贴纸表情 | `theme / skin / 皮肤 / 主题 / 像素 / 壁纸 / 外观 / css / sticker / 贴纸 / 表情包 / emoji` |
| 4 | 🛒 市场与管理 | 插件市场、包管理、健康检查、装卸载 | `market / store / registry / manager / 市场 / 商店 / 工坊 / workshop / health check / 健康检查 / 卸载 / installer / 包管理 / 插件浏览` |
| 5 | 🔌 Web UI 增强 | Web/TUI 界面功能：侧栏、输入、面板、批注、状态栏 | `web ui / webui / sidebar / 侧边栏 / 输入框 / input / 面板 / panel / 批注 / 状态栏 / dock / 气泡 / toast / 导航 / navbar` |
| 6 | 💻 编码开发 | 编码场景：代码、git、diff、终端、语言、构建、测试 | `code / 编码 / git / github / diff / 终端 / terminal / shell / lsp / 编译 / build / 测试 / test / review` |
| 7 | 🤖 Agent 能力 | agent 本体：子代理、规划执行、上下文、唤醒睡眠、审批 | `agent / 子代理 / subagent / 规划 / plan / 上下文 / context / 唤醒 / 自治 / loop / 预算 / budget / 审批 / approv` |
| 8 | 📡 消息通讯 | IM 与消息通道：微信/QQ/TG/飞书 bot、通知、消息 | `微信 / wechat / wecom / 飞书 / feishu / telegram / tg / qq / bot / 通知 / notify / 消息 / message / chat` |
| 9 | 🗂 文件数据 | 文件与数据：读写、爬取、数据库、文档解析、知识库 | `文件 / file / 数据 / data / 爬 / crawl / 数据库 / sqlite / 文档 / pdf / 知识库 / kb / rag / 索引 / ocr / csv` |
| 10 | 🎮 娱乐生活 | 摸鱼与趣味：游戏、宠物、音乐、行情 | `游戏 / game / 宠物 / pet / 鲸鱼 / whale / 音乐 / 股票 / 行情 / 摸鱼 / 旅行` |
| 11 | 🛠 基建部署 | 运行环境与分发：沙箱、远程、代理、监控、桌面端 | `沙箱 / sandbox / 部署 / deploy / 远程 / remote / ssh / docker / k8s / 监控 / monitor / 桌面 / desktop / 托盘 / tray / 更新 / update / 代理 / proxy / mcp` |
| 12 | 📚 学习研究 | 学习与探索：教程、指南、评测、研究 | `教程 / tutorial / 指南 / guide / 评测 / benchmark / 基准 / 研究 / research / 论文 / 学习` |
| 13 | ❓ 其他 | 兜底。提 PR 时请尽量避免使用 | — |

## 边界归属（常见争议）

- **技能 vs 插件**：以 skill 形态分发（.dsh/skills 目录、技能注册）→ 技能包；以 npm 包/plugin 形态 → 按功能归 5-12。
- **主题 vs UI 增强**：只换外观（皮肤/CSS/像素）→ 主题皮肤；增改功能（新面板/新交互）→ Web UI 增强。
- **通知 vs 消息通讯**：出站推送（notify）与 IM bot 统归消息通讯（生态内两者高度重叠，不拆）。
- **MCP/模型接入**：接入外部模型或 MCP 服务 → 基建部署；模型输出处理（vision/OCR 文档）→ 文件数据。
- **市场 vs 基建**：管理「插件本身」的装卸载/市场 → 市场与管理；运行环境/分发 → 基建部署。

## Bot 提 PR 时的提前归类流程

1. 登记 PR 前运行预归类器：`python3 scripts/classify.py "<插件名>" "<一句话描述>"`
2. 将输出的「建议分类」填入 PR 模板的**分类**字段；命中规则为空（兜底其他）时人工复核改名。
3. 规则与本文档同源（`scripts/classify.py` 的 `RULES`）；修改分类标准 = 改本文档 + 同步规则并重跑 `python3 scripts/render-readme-from-snapshot.py`。
