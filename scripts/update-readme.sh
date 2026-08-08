#!/usr/bin/env bash
# 更新 README 自动状态节（<!-- AUTO:ecosystem --> 标记块）：
#   兼容性汇总（最新报告）+ 正在跟踪的 org open PR 列表
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

# 2. org open PR 列表（search API，全部仓库）
PR_TOTAL="0"
PR_ROWS=""
if command -v gh >/dev/null 2>&1; then
  PR_TOTAL="$(timeout 60 gh api "search/issues?q=org:dsh-external+type:pr+state:open&per_page=1" --jq '.total_count' 2>/dev/null || echo 0)"
  while IFS=$'\t' read -r repo num title updated; do
    [ -n "$repo" ] || continue
    PR_ROWS+="| [$repo](https://github.com/dsh-external/$repo) | [#$num](https://github.com/dsh-external/$repo/pull/$num) | $title | $updated |"$'\n'
  done < <(timeout 90 gh api "search/issues?q=org:dsh-external+type:pr+state:open&per_page=100" 2>/dev/null \
    | jq -r '.items[] | [((.repository_url | split("/") | .[length-1])), (.number|tostring), .title, (.updated_at[0:10])] | @tsv' 2>/dev/null)
fi
[ -z "$PR_ROWS" ] && PR_ROWS="| （暂无 open PR） | | | |"$'\n'

# 3. 组装标记块
BLOCK="<!-- AUTO:ecosystem:START -->
> 自动更新：$(date +%Y-%m-%d_%H%M)（cron 每 8 小时；源码见 scripts/update-readme.sh）

**兼容性汇总**（报告日 $DATE · mainline \`$MAINLINE\`）：${SUMMARY:-（暂无报告）}

**正在跟踪的 open PR**（org 共 $PR_TOTAL 个）：

| 仓库 | PR | 标题 | 更新 |
|---|---|---|---|
${PR_ROWS}<!-- AUTO:ecosystem:END -->"

# 4. 替换 README 标记块（不存在则追加到末尾）
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
print('README 自动节已更新')
PYEOF
exit 0
