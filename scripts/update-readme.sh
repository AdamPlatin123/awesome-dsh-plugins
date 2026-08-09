#!/usr/bin/env bash
# 更新 README 自动仪表盘节（<!-- AUTO:ecosystem --> 标记块），A 方向「仪表盘优先」：
#   徽章行 → 今日新增/修改仓库表 → 需适配表 → 跟踪中的 open PR 表
# 数据源：.last-changes.json（cron-check 写入的本次新增/修改）+ 最新报告 + gh PR 查询
# cron-check.sh 每次运行后调用；README 变化由 cron-check 统一 commit/push。
# 依赖：bash/git/gh/jq（gh 认证）
set -uo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
README="README.md"
[ -f "$README" ] || { echo "[错误] 找不到 README.md"; exit 2; }

# 1. 最新报告汇总（reports/<最新日期>/mainline-compat.md 首行兼容性）
LATEST_REPORT="$(ls -d reports/20*/ 2>/dev/null | sort | tail -1 | sed 's#/$##')"
DATE="$(basename "${LATEST_REPORT:-reports/unknown}")"
SUMMARY=""
if [ -n "$LATEST_REPORT" ] && [ -f "$LATEST_REPORT/mainline-compat.md" ]; then
  SUMMARY="$(grep -m1 '^- 兼容性：' "$LATEST_REPORT/mainline-compat.md" | sed 's/^- //' || true)"
fi
MAINLINE="$(jq -r '.lastMainlineCommit // "?"' .mainline-state.json 2>/dev/null | cut -c1-7)"
[ -z "$MAINLINE" ] && MAINLINE="?"

# 解析汇总数字：兼容性：X/Y 无需适配，Z 需适配（...）；其中关注 A、占位 B、不适用 C、已删除 D
COMPAT="?"; TOTAL="?"; ADAPT="?"; WATCH="?"; PLACE="?"; NA="?"; GONE="?"
if [ -n "$SUMMARY" ]; then
  COMPAT="$(printf '%s' "$SUMMARY" | sed -E 's#兼容性：([0-9]+)/[0-9]+.*#\1#')"
  TOTAL="$(printf '%s' "$SUMMARY" | sed -E 's#兼容性：[0-9]+/([0-9]+).*#\1#')"
  ADAPT="$(printf '%s' "$SUMMARY" | sed -E 's#.*，([0-9]+) 需适配.*#\1#')"
  WATCH="$(printf '%s' "$SUMMARY" | sed -E 's#.*关注 ([0-9]+).*#\1#')"
  PLACE="$(printf '%s' "$SUMMARY" | sed -E 's#.*占位 ([0-9]+).*#\1#')"
  NA="$(printf '%s' "$SUMMARY" | sed -E 's#.*不适用 ([0-9]+).*#\1#')"
  GONE="$(printf '%s' "$SUMMARY" | sed -E 's#.*已删除 ([0-9]+).*#\1#')"
  # 汇总数字校验：sed 提取结果必须匹配 ^[0-9]+$（sed 未命中时原样返回整行，非数字）
  # 任一数字非法 → 全部置 "?"（全部数字有效才渲染真实值，杜绝半成品数字上 README）
  valid=1
  for v in COMPAT TOTAL ADAPT WATCH PLACE NA GONE; do
    [[ "${!v}" =~ ^[0-9]+$ ]] || valid=0
  done
  if [ "$valid" -eq 0 ]; then
    COMPAT="?"; TOTAL="?"; ADAPT="?"; WATCH="?"; PLACE="?"; NA="?"; GONE="?"
  fi
fi

# 2. 今日新增/修改仓库（.last-changes.json；无则取空）
NEW_LIST=""; MOD_LIST=""
if [ -f .last-changes.json ]; then
  NEW_LIST="$(jq -r '.new_repos[]?' .last-changes.json 2>/dev/null || true)"
  MOD_LIST="$(jq -r '.changed_repos[]?' .last-changes.json 2>/dev/null || true)"
fi
NEW_ROWS=""; MOD_ROWS=""
[ -n "$NEW_LIST" ] && NEW_ROWS="$(printf '%s\n' "$NEW_LIST" | while IFS= read -r n; do [ -n "$n" ] && printf '| [%s](https://github.com/dsh-external/%s) | 🆕 新增 |\n' "$n" "$n"; done)"
[ -z "$NEW_ROWS" ] && NEW_ROWS=$'| （今日无新增） | |\n'
[ -n "$MOD_LIST" ] && MOD_ROWS="$(printf '%s\n' "$MOD_LIST" | while IFS= read -r n; do [ -n "$n" ] && printf '| [%s](https://github.com/dsh-external/%s) | ✏️ 修改 |\n' "$n" "$n"; done)"
[ -z "$MOD_ROWS" ] && MOD_ROWS=$'| （今日无修改） | |\n'

# 3. 需适配仓库（从最新报告矩阵提取状态=需适配的行）
ADAPT_ROWS=""
if [ -n "$LATEST_REPORT" ] && [ -f "$LATEST_REPORT/mainline-compat.md" ]; then
  ADAPT_ROWS="$(grep -E '^\| .* \| 需适配[^|]* \|$' "$LATEST_REPORT/mainline-compat.md" | sed -E 's#^\| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$#| [\1](https://github.com/dsh-external/\1) | \2 | \6 |#' | head -20)"
fi
[ -z "$ADAPT_ROWS" ] && ADAPT_ROWS=$'| （暂无） | | |\n'

# 4. org open PR 列表（search API，全部仓库）
#    查询失败（gh/jq 缺失、超时、返回空）→ 不覆盖 README，echo 错误并 exit 1（不渲染假"暂无"）
PR_TOTAL="0"
PR_ROWS=""
for dep in gh jq; do
  command -v "$dep" >/dev/null 2>&1 || { echo "[错误] 缺少依赖: $dep（无法查询 open PR，跳过 README 更新）"; exit 1; }
done
PR_TOTAL="$(timeout 60 gh api "search/issues?q=org:dsh-external+type:pr+state:open&per_page=1" --jq '.total_count' 2>/dev/null || true)"
if ! [[ "$PR_TOTAL" =~ ^[0-9]+$ ]]; then
  echo "[错误] gh 查询 open PR 总数失败（超时/网络/认证），不覆盖 README（exit 1）"
  exit 1
fi
PR_LIST="$(timeout 90 gh api "search/issues?q=org:dsh-external+type:pr+state:open&per_page=100" 2>/dev/null || true)"
if [ -z "$PR_LIST" ]; then
  echo "[错误] gh 查询 open PR 列表失败（超时/网络/认证），不覆盖 README（exit 1）"
  exit 1
fi
while IFS=$'\t' read -r repo num title updated; do
  [ -n "$repo" ] || continue
  PR_ROWS+="| [$repo](https://github.com/dsh-external/$repo) | [#$num](https://github.com/dsh-external/$repo/pull/$num) | $title | $updated |"$'\n'
done < <(printf '%s' "$PR_LIST" | jq -r '.items[] | [((.repository_url | split("/") | .[length-1])), (.number|tostring), .title, (.updated_at[0:10])] | @tsv' 2>/dev/null)
if [ "$PR_TOTAL" -gt 0 ] && [ -z "$PR_ROWS" ]; then
  echo "[错误] open PR 总数非 0 但列表解析为空（jq 解析失败），不覆盖 README（exit 1）"
  exit 1
fi
[ -z "$PR_ROWS" ] && PR_ROWS="| （暂无 open PR） | | | |"$'\n'

# 5. 组装标记块（A 方向：仪表盘优先）
BLOCK="<!-- AUTO:ecosystem:START -->
> 自动更新：$(date +%Y-%m-%d_%H%M)（cron 每 8 小时 · 报告日 $DATE · mainline \`$MAINLINE\`）

**生态仪表盘**

| 指标 | 值 |
|---|---|
| 仓库总数 | $TOTAL |
| ✅ 无需适配 | $COMPAT |
| ⚠️ 需适配 | $ADAPT |
| 关注 / 占位 / 不适用 / 已删除 | $WATCH / $PLACE / $NA / $GONE |
| 🐙 开放 PR | $PR_TOTAL |

📄 **最新报告**：[mainline-compat.md](reports/$DATE/mainline-compat.md) · [当日索引](reports/$DATE/index.md)（完整矩阵 + 双方建议）

**今日新增 / 修改仓库**

| 仓库 | 类型 |
|---|---|
${NEW_ROWS}
${MOD_ROWS}
**需适配（补丁基线 / seam 变化）**

| 仓库 | 锚定 | 判定 |
|---|---|---|
${ADAPT_ROWS}
**正在跟踪的 open PR**

| 仓库 | PR | 标题 | 更新 |
|---|---|---|---|
${PR_ROWS}<!-- AUTO:ecosystem:END -->"

# 6. 替换 README 标记块（不存在则追加到末尾）
python3 - "$README" "$BLOCK" <<'PYEOF'
import sys
path, block = sys.argv[1], sys.argv[2]
with open(path, encoding='utf-8') as f:
    content = f.read()
start_marker = '<!-- AUTO:ecosystem:START -->'
end_marker = '<!-- AUTO:ecosystem:END -->'
if start_marker in content:
    start = content.index(start_marker)
    end = content.index(end_marker) + len(end_marker)
    new = content[:start] + block + content[end:]
else:
    new = content.rstrip() + '\n\n## 生态状态（自动更新）\n\n' + block + '\n'
with open(path, 'w', encoding='utf-8') as f:
    f.write(new)
print('README 自动仪表盘已更新')
PYEOF
exit 0
