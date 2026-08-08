#!/usr/bin/env bash
# 每 8 小时自动运行（cron）：
#   1) 动态发现 dsh-external org 新仓库（gh api），与已知 15 仓合并为检测范围
#   2) 检测 mainline + 全部仓库 HEAD 变化
#   3) 有变化（或发现新仓库）→ 运行 mainline 兼容索引（--scope 动态清单）
#   4) 更新报告/CHANGELOG 并推送回 org repo
# 依赖：bash/git/gh/jq（gh 已认证，git credential 走 gh auth setup-git）
set -uo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
mkdir -p logs
LOG="logs/cron-$(date +%Y%m%d).log"
exec >> "$LOG" 2>&1

echo "=== $(date -Is) cron-check 开始 ==="

# 0. 依赖预检
for dep in bash git gh jq; do
  command -v "$dep" >/dev/null 2>&1 || { echo "[错误] 缺少依赖: $dep"; exit 2; }
done

# 1. 拉取自身最新（引擎/脚本/README 更新随 org repo 同步）
git pull dsh-ext main --ff-only 2>&1 | tail -1 || echo "[提示] git pull 失败（可能离线或已最新），继续"

# 2. 已知仓库（调研基线 15 仓）+ 动态发现新仓库
# 已知仓库 = 已调研摘要清单（research/*.md 文件名，新增摘要自动同步；不再手工维护）
KNOWN_REPOS=()
for _f in research/*.md; do
  [ -f "$_f" ] || continue
  _n="${_f##*/}"; _n="${_n%.md}"
  [ -n "$_n" ] && KNOWN_REPOS+=( "$_n" )
done
SELF_REPO="dsh-external-research"   # 本仓库自身，不纳入索引

# 动态拉取 org 全部仓库名（失败则回退已知列表，不误报离线）
ORG_REPOS="$(timeout 60 gh api "orgs/dsh-external/repos?per_page=100&type=all" --paginate --jq '.[].name' 2>/dev/null || echo "")"
if [ -z "$ORG_REPOS" ]; then
  echo "[提示] gh api 获取 org 仓库失败，回退已知列表"
  SCOPE_REPOS=( "${KNOWN_REPOS[@]}" )
else
  SCOPE_REPOS=( "${KNOWN_REPOS[@]}" )
  NEW_REPOS=()
  while IFS= read -r name; do
    [ -n "$name" ] || continue
    [ "$name" = "$SELF_REPO" ] && continue
    found=0
    for k in "${KNOWN_REPOS[@]}"; do [ "$k" = "$name" ] && found=1 && break; done
    if [ "$found" -eq 0 ]; then
      NEW_REPOS+=( "$name" )
      SCOPE_REPOS+=( "$name" )
    fi
  done <<< "$ORG_REPOS"
  if [ "${#NEW_REPOS[@]}" -gt 0 ]; then
    echo "[新仓库] 发现 ${#NEW_REPOS[@]} 个未索引仓库: ${NEW_REPOS[*]}"
  else
    echo "[新仓库] 无新增仓库（org 共 $(echo "$ORG_REPOS" | wc -l | tr -d ' ') 个）"
  fi
fi

# 写入动态 scope 清单（引擎 --scope 契约：每行一个仓库名）
: > .scope-current.txt
for r in "${SCOPE_REPOS[@]}"; do echo "$r" >> .scope-current.txt; done

# 3. 检测 mainline + 全部 scope 仓库的 HEAD 变化
STATE=".cron-state.json"
CHANGED=""
declare -a REPOS=()
REPOS+=( "mainline|https://github.com/dsh2026/test-AdamPlatin123" )
for r in "${SCOPE_REPOS[@]}"; do
  REPOS+=( "$r|https://github.com/dsh-external/$r" )
done

if [ -f "$STATE" ]; then
  for entry in "${REPOS[@]}"; do
    name="${entry%%|*}"; url="${entry#*|}"
    prev="$(jq -r --arg n "$name" '.[$n] // ""' "$STATE" 2>/dev/null || echo "")"
    cur="$(timeout 20 git ls-remote "$url" HEAD 2>/dev/null | awk '{print $1}')"
    if [ -z "$cur" ]; then
      echo "[跳过] $name：ls-remote 失败（离线/网络），保留上次状态"
    elif [ -z "$prev" ]; then
      CHANGED="$CHANGED $name"
      echo "[新增] $name：首次纳入检测（HEAD $cur）"
    elif [ "$cur" != "$prev" ]; then
      CHANGED="$CHANGED $name"
      echo "[变化] $name: $prev -> $cur"
    fi
  done
else
  echo "[首次运行] 无状态文件，执行全量索引"
  CHANGED="all(首次)"
fi

# 3.5 记录本次新增/修改仓库（供 README 自动仪表盘渲染）
#     新增 = 本次发现的 NEW_REPOS；修改 = CHANGED 中非新增的已知仓库
CHANGED_REPOS=()
for _c in $CHANGED; do
  [ "$_c" = "all(首次)" ] && continue
  _is_new=0
  for _n in "${NEW_REPOS[@]:-}"; do [ "$_n" = "$_c" ] && _is_new=1 && break; done
  [ "$_is_new" -eq 0 ] && CHANGED_REPOS+=( "$_c" )
done
{
  printf '{"date":"%s","new_repos":[' "$(date +%Y-%m-%d)"
  _first=1
  for _n in "${NEW_REPOS[@]:-}"; do
    [ $_first -eq 0 ] && printf ','
    printf '"%s"' "$_n"
    _first=0
  done
  printf '],"changed_repos":['
  _first=1
  for _c in "${CHANGED_REPOS[@]:-}"; do
    [ $_first -eq 0 ] && printf ','
    printf '"%s"' "$_c"
    _first=0
  done
  printf ']}'
} > .last-changes.json.tmp && mv .last-changes.json.tmp .last-changes.json

echo "[状态] .last-changes.json 已记录（新增 ${#NEW_REPOS[@]:-0} / 修改 ${#CHANGED_REPOS[@]}）"

# 4. 有变化 → 运行 mainline 兼容索引（动态 scope）
if [ -n "$CHANGED" ]; then
  echo "[索引] 变化仓库:$CHANGED"
  ./scripts/compare-mainline.sh --scope .scope-current.txt
  rc=$?
  echo "[索引] compare-mainline.sh 退出码 $rc"

  # 5. 提交报告/CHANGELOG/状态并推送回 org repo
  if git diff --quiet && git diff --cached --quiet; then
    echo "[提交] 无新内容，跳过 commit"
  else
    git add -A
    git -c user.name="dsh-ecosystem-bot" -c user.email="bot@dsh-external.local" \
      commit -m "chore: 自动索引更新 $(date +%Y-%m-%d_%H%M) — 变化:$CHANGED" || echo "[提示] commit 失败"
    git push dsh-ext main 2>&1 | tail -2 || echo "[提示] push 失败（网络），下次 cron 重试"
  fi
else
  echo "[无变化] 全部仓库 HEAD 未变，跳过索引"
fi

# 5.5 每次运行后更新 README 自动状态节（兼容性汇总 + 跟踪中的 PR）
#     PR 状态变化也 commit——README 是每日状态视图，不依赖仓库 HEAD 变化
echo "[README] 更新自动状态节..."
if ./scripts/update-readme.sh >/dev/null 2>&1; then
  if ! git diff --quiet -- README.md; then
    git add README.md
    git -c user.name="dsh-ecosystem-bot" -c user.email="bot@dsh-external.local" \
      commit -m "chore: README 生态状态更新 $(date +%Y-%m-%d_%H%M)（兼容性汇总 + PR 跟踪）" || echo "[提示] README commit 失败"
    git push dsh-ext main 2>&1 | tail -1 || echo "[提示] README push 失败，下次 cron 重试"
  else
    echo "[README] 无变化（状态与 PR 列表未变）"
  fi
else
  echo "[README] 更新失败（gh 离线或解析错误），下次重试"
fi

# 6. 更新状态文件（记录当前 HEAD）
{
  echo "{"
  first=1
  for entry in "${REPOS[@]}"; do
    name="${entry%%|*}"; url="${entry#*|}"
    cur="$(timeout 20 git ls-remote "$url" HEAD 2>/dev/null | awk '{print $1}')"
    [ -z "$cur" ] && cur="$(jq -r --arg n "$name" '.[$n] // ""' "$STATE" 2>/dev/null || echo "")"
    [ $first -eq 0 ] && echo ","
    printf '  "%s": "%s"' "$name" "$cur"
    first=0
  done
  echo ""
  echo "}"
} > "$STATE.tmp" && mv "$STATE.tmp" "$STATE"

echo "=== $(date -Is) cron-check 结束 ==="
exit 0
