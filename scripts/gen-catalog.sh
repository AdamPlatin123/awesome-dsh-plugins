#!/usr/bin/env bash
# 生成 README「分类目录」章节（参考 dsh-external/hub 的九类体系）
# 渲染规则：
#   - 表格列出（插件 | 说明）
#   - 每类显示前 10 条；第 11 条起放入嵌套折叠块「展开全部」
#   - 「单插件」类默认展开（open），其余类别默认收起
# 数据源：hub catalog.json（gh api 实时拉取）；渲染全部由 jq 完成（避免 bash 多行循环）
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
GH="$HOME/.local/bin/gh"
JQ="$HOME/.local/bin/jq"

CATALOG="$(mktemp)"
timeout 90 "$GH" api "repos/dsh-external/hub/contents/catalog.json" --jq '.content' 2>/dev/null | base64 -d 2>/dev/null > "$CATALOG"
[ -s "$CATALOG" ] || { echo "[gen-catalog] hub catalog 拉取失败，跳过"; rm -f "$CATALOG"; exit 0; }

BLOCK='<!-- AUTO:catalog:START -->'
BLOCK+=$'\n'
BLOCK+='> 分类参考 [dsh-external/hub](https://github.com/dsh-external/hub)（catalog v0.1）。每类显示前 10 条，其余折叠；「单插件」默认展开。'
BLOCK+=$'\n\n'

render_cat() { # $1=key $2=title $3=open标记
  local key="$1" title="$2" open="$3" cnt rows10 rows_rest
  cnt="$("$JQ" -r "[.repos[] | select((.category // \"uncategorized\") == \"$key\")] | length" "$CATALOG" 2>/dev/null)"
  [ -n "$cnt" ] || cnt=0
  rows10="$("$JQ" -r ".repos[] | select((.category // \"uncategorized\") == \"$key\") | \"| [\(.name)](\(.url)) | \((.description // \"\") | split(\"。\")[0] | .[0:48] | if . == \"\" then \"—\" else . end) |\"" "$CATALOG" 2>/dev/null | head -10)"
  BLOCK+="<details$open>"$'\n'
  BLOCK+="<summary>$title（$cnt）</summary>"$'\n\n'
  BLOCK+='| 插件 | 说明 |'$'\n|---|---|'$'\n'
  if [ -n "$rows10" ]; then BLOCK+="$rows10"$'\n'; else BLOCK+='| （暂无） | — |'$'\n'; fi
  if [ "$cnt" -gt 10 ]; then
    rows_rest="$("$JQ" -r ".repos[] | select((.category // \"uncategorized\") == \"$key\") | \"| [\(.name)](\(.url)) | \((.description // \"\") | split(\"。\")[0] | .[0:48] | if . == \"\" then \"—\" else . end) |\"" "$CATALOG" 2>/dev/null | tail -n +11)"
    BLOCK+=$'\n<details>'$'\n'
    BLOCK+="<summary>展开全部（剩余 $((cnt-10)) 条）</summary>"$'\n\n'
    BLOCK+='| 插件 | 说明 |'$'\n|---|---|'$'\n'
    BLOCK+="$rows_rest"$'\n'
    BLOCK+='</details>'$'\n'
  fi
  BLOCK+='</details>'$'\n\n'
}

render_cat community "💬 社区" ""
render_cat skill "🎓 技能" ""
render_cat plugin "🔌 单插件" " open"
render_cat collection "🧰 插件集" ""
render_cat channel "📡 远程渠道" ""
render_cat infra "🛠 基础设施" ""
render_cat research "🔬 研究" ""
# hub catalog 数据中的未分类 key 是 _uncategorized（非 uncategorized），必须一致否则 10 仓丢失
render_cat _uncategorized "❓ 未分类" ""
BLOCK+='<!-- AUTO:catalog:END -->'

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
