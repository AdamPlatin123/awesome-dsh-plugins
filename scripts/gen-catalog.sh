#!/usr/bin/env bash
# 生成 README「分类目录」章节（参考 dsh-external/hub 的九类体系）
# 数据源：hub catalog.json（gh api 实时拉取）；渲染为 AUTO:catalog 折叠块
# 每类 <details> 内紧凑列出：仓库链接 + 一句话说明（截断）
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
GH="$HOME/.local/bin/gh"
JQ="$HOME/.local/bin/jq"

CATALOG="$(mktemp)"
timeout 90 "$GH" api "repos/dsh-external/hub/contents/catalog.json" --jq '.content' 2>/dev/null | base64 -d 2>/dev/null > "$CATALOG"
[ -s "$CATALOG" ] || { echo "[gen-catalog] hub catalog 拉取失败，跳过"; rm -f "$CATALOG"; exit 0; }

declare -A CATS=(
  [community]="💬 社区"
  [skill]="🎓 技能"
  [plugin]="🔌 单插件"
  [collection]="🧰 插件集"
  [channel]="📡 远程渠道"
  [infra]="🛠 基础设施"
  [research]="🔬 研究"
  [uncategorized]="❓ 未分类"
)

BLOCK='<!-- AUTO:catalog:START -->'
BLOCK+=$'\n'
BLOCK+='> 分类参考 [dsh-external/hub](https://github.com/dsh-external/hub)（catalog v0.1），每日随全量扫描刷新。'
BLOCK+=$'\n\n'
for key in community skill plugin collection channel infra research uncategorized; do
  title="${CATS[$key]}"
  cnt="$("$JQ" -r "[.repos[] | select((.category // \"uncategorized\") == \"$key\")] | length" "$CATALOG" 2>/dev/null || echo 0)"
  rows="$("$JQ" -r ".repos[] | select((.category // \"uncategorized\") == \"$key\") | \"- [\(.name)](\(.url))\" + (if .description then \" — \" + (.description | split(\"。\")[0] | .[0:48]) else \"\" end)" "$CATALOG" 2>/dev/null | head -60)"
  [ -z "$rows" ] && rows="- （暂无）"
  BLOCK+="<details>"
  BLOCK+=$'\n'
  BLOCK+="<summary>$title（$cnt）</summary>"
  BLOCK+=$'\n\n'
  BLOCK+="$rows"
  BLOCK+=$'\n\n'
  BLOCK+='</details>'
  BLOCK+=$'\n\n'
done
BLOCK+='<!-- AUTO:catalog:END -->'

# 替换 README 中的 AUTO:catalog 块（无则插到「## 当前生态快照」前）
python3 - "$BLOCK" <<'PYEOF'
import sys
block = sys.argv[1]
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
