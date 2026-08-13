#!/usr/bin/env bash
# 生成 README「分类目录」章节（参考 dsh-external/hub 的八类体系）
# 渲染规则：
#   - 每类一个 <details> 折叠块，点击标题展开；标题为 h3 大字号 + 类别描述
#   - 每类显示前 10 条；第 11 条起放入嵌套折叠块「展开全部」
#   - REPO_OVERRIDES 修正 hub catalog 的错误分类（重分类）；未覆盖的用 catalog 原值
# 数据源：hub catalog.json（gh api 实时拉取）；渲染由 python3 完成
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
GH="$HOME/.local/bin/gh"

CATALOG="$(mktemp)"
timeout 90 "$GH" api "repos/dsh-external/hub/contents/catalog.json" --jq '.content' 2>/dev/null | base64 -d 2>/dev/null > "$CATALOG"
[ -s "$CATALOG" ] || { echo "[gen-catalog] hub catalog 拉取失败，跳过"; rm -f "$CATALOG"; exit 0; }

python3 - "$CATALOG" <<'PYEOF'
import json, sys

catalog = json.load(open(sys.argv[1], encoding="utf-8"))
repos = catalog.get("repos", [])

# 类别元信息：key -> (emoji 标题, 描述)。顺序即渲染顺序。
CATEGORY_META = [
    ("community",      "💬 社区",     "社群运营、内测反馈与公告类仓库"),
    ("skill",          "🎓 技能",     "模型技能包：提示词、工作流与可复用 skill"),
    ("plugin",         "🔌 单插件",   "单个功能插件：独立安装、单一能力"),
    ("collection",     "🧰 插件集",   "多插件合集、皮肤包与发行版"),
    ("channel",        "📡 远程渠道", "IM 与社交平台接入（微信、QQ、Telegram、飞书等）"),
    ("infra",          "🛠 基础设施", "桌面/移动客户端、沙箱、构建与部署基建"),
    ("research",       "🔬 研究",     "评测、基准与研究工具"),
    ("_uncategorized", "❓ 未分类",   "尚未归类的仓库（重分类后应清空）"),
]

# 重分类：hub catalog 分类错误的仓库 -> 修正类别
REPO_OVERRIDES = {
    # 未分类 10 个归位
    "dsh_ide": "plugin",
    "dsh_workflow": "plugin",
    "dsh-build": "infra",
    "dsh-code": "plugin",
    "dsh-fkin-vibe": "plugin",
    "dsh-hmz": "plugin",
    "dsh-remote": "plugin",
    "dsh-ui-webview": "plugin",
    "oh-my-deepseek": "collection",
    "Top": "infra",
    # collection 里的单插件/单工具归位
    "dsh-cot-summary": "plugin",
    "dsh-tool-browser": "plugin",
    "dsh-my-rsi": "plugin",
    "dsh-deepcel": "plugin",
    "dsh-deep-whale": "plugin",
    "dsh-serenity-plugin": "plugin",
    "dsh-plugin-guide": "skill",
    # infra 里的单工具归位
    "ds_web_craw": "plugin",
    "dsh-android": "plugin",
}

def effective_category(repo):
    name = repo.get("name", "")
    return REPO_OVERRIDES.get(name, repo.get("category", "_uncategorized"))

def short_desc(repo):
    d = repo.get("description") or ""
    if d == "null" or not d.strip():
        return "—"
    # 取首个句号前内容，限 48 字符
    d = d.split("。")[0].strip()
    if not d:
        d = d.split(".")[0].strip()
    return d[:48] if d else "—"

# 分组（应用 override）
groups = {key: [] for key, _, _ in CATEGORY_META}
for r in repos:
    cat = effective_category(r)
    groups.setdefault(cat, []).append(r)

out = []
out.append("<!-- AUTO:catalog:START -->")
out.append("")
out.append("> 分类参考 [dsh-external/hub](https://github.com/dsh-external/hub)（catalog v0.1，本页含重分类修正）。每类显示前 10 条，其余折叠；点击标题展开。")
out.append("")
for key, title, desc in CATEGORY_META:
    items = groups.get(key, [])
    n = len(items)
    out.append("<details>")
    out.append(f"<summary><h3>{title}（{n}）</h3></summary>")
    out.append("")
    out.append(f"*{desc}*")
    out.append("")
    out.append("| 插件 | 说明 |")
    out.append("|---|---|")
    if n == 0:
        out.append("| （暂无） | — |")
    else:
        for r in items[:10]:
            out.append(f"| [{r['name']}]({r.get('url', '')}) | {short_desc(r)} |")
        if n > 10:
            out.append("")
            out.append("<details>")
            out.append(f"<summary>展开全部（剩余 {n - 10} 条）</summary>")
            out.append("")
            out.append("| 插件 | 说明 |")
            out.append("|---|---|")
            for r in items[10:]:
                out.append(f"| [{r['name']}]({r.get('url', '')}) | {short_desc(r)} |")
            out.append("</details>")
    out.append("</details>")
    out.append("")
out.append("<!-- AUTO:catalog:END -->")

block = "\n".join(out)
p = "README.md"
s = open(p, encoding="utf-8").read()
start = "<!-- AUTO:catalog:START -->"
end = "<!-- AUTO:catalog:END -->"
if start in s:
    i = s.index(start)
    j = s.index(end) + len(end)
    s = s[:i] + block + s[j:]
else:
    anchor = "## 当前生态快照"
    i = s.index(anchor)
    s = s[:i] + "## 分类目录\n\n" + block + "\n" + s[i:]
open(p, "w", encoding="utf-8").write(s)
print("CATALOG_BLOCK_UPDATED")
PYEOF
rm -f "$CATALOG"
exit 0
