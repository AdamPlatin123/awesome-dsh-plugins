#!/usr/bin/env bash
# 每 8 小时自动运行（cron）：
#   1) 动态发现 dsh-external org 新仓库（gh api），与已知仓库合并为检测范围
#   2) 检测 mainline + 全部仓库 HEAD 变化
#   3) 有变化（或 --full 强制）→ 运行 mainline 兼容索引（--scope 动态清单）
#   4) 更新报告/CHANGELOG/README 并推送回 org repo
# 用法：cron-check.sh [--full]  — --full 跳过变化检测，全量索引所有仓库（cron 02:00 班次）
# 依赖：bash/git/gh/jq（gh 已认证，git credential 走 gh auth setup-git）
set -uo pipefail

# 互斥：flock 防止 hook 触发与 cron 定时班并发（曾实测 3 个 --full 同时跑竞态）
LOCK_FD=9
exec 9>/tmp/dsh-cron-check.lock
if ! flock -n 9; then
  echo "[互斥] 已有 cron-check 在运行，本轮退出"
  exit 0
fi

FULL=0
for _arg in "$@"; do [ "$_arg" = "--full" ] && FULL=1; done

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
mkdir -p logs
LOG="logs/cron-$(date +%Y%m%d).log"
exec >> "$LOG" 2>&1

[ "$FULL" -eq 1 ] && echo "=== $(date -Is) cron-check 开始（--full 全量模式） ===" || echo "=== $(date -Is) cron-check 开始 ==="

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
SELF_REPO="awesome-dsh-plugins"   # 本仓库自身，不纳入索引

# 动态拉取 org 全部仓库名（失败则回退已知列表，不误报离线）
ORG_REPOS="$(timeout 60 gh api "orgs/dsh-external/repos?per_page=100&type=all" --paginate --jq '.[].name' 2>/dev/null || echo "")"
# 动态发现的新仓库（在 gh api 调用前初始化空数组，避免 set -u 下未定义引用）
NEW_REPOS=()
if [ -z "$ORG_REPOS" ]; then
  echo "[提示] gh api 获取 org 仓库失败，回退已知列表"
  SCOPE_REPOS=( "${KNOWN_REPOS[@]}" )
else
  SCOPE_REPOS=( "${KNOWN_REPOS[@]}" )
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

# 远端 HEAD 探测：mainline 取最新快照分支（与 compare-mainline.sh 实际索引的快照一致），
# 其余仓库取 HEAD。快照分支名含 ISO 时间戳，字典序即时间序。
remote_head() { # $1=仓库名 $2=远端 URL → 输出当前 commit（失败为空）
  local name="$1" url="$2"
  if [ "$name" = "mainline" ]; then
    timeout 20 git ls-remote "$url" 'refs/heads/snapshots/*' 2>/dev/null \
      | LC_ALL=C sort -k2 | tail -1 | awk '{print $1}'
  else
    timeout 20 git ls-remote "$url" HEAD 2>/dev/null | awk '{print $1}'
  fi
}

# 3. 检测 mainline + 全部 scope 仓库的 HEAD 变化
STATE=".cron-state.json"
CHANGED=""
declare -a REPOS=()
REPOS+=( "mainline|https://github.com/dsh2026/test-AdamPlatin123" )
for r in "${SCOPE_REPOS[@]}"; do
  REPOS+=( "$r|https://github.com/dsh-external/$r" )
done

if [ "$FULL" -eq 1 ]; then
  echo "[全量] --full 模式：跳过变化检测，强制全量索引（最新 mainline + 全部仓库）"
  CHANGED="all(全量)"
elif [ -f "$STATE" ]; then
  for entry in "${REPOS[@]}"; do
    name="${entry%%|*}"; url="${entry#*|}"
    prev="$(jq -r --arg n "$name" '.[$n] // ""' "$STATE" 2>/dev/null || echo "")"
    cur="$(remote_head "$name" "$url")"
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
if [ "$FULL" -eq 1 ]; then
  # 全量模式：逐 repo commit 全部 scope 仓库详情
  CHANGED_REPOS=( "${SCOPE_REPOS[@]:-}" )
else
  for _c in $CHANGED; do
    [ "$_c" = "all(首次)" ] && continue
    [ "$_c" = "all(全量)" ] && continue
    _is_new=0
    for _n in "${NEW_REPOS[@]:-}"; do [ "$_n" = "$_c" ] && _is_new=1 && break; done
    [ "$_is_new" -eq 0 ] && CHANGED_REPOS+=( "$_c" )
  done
fi
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

echo "[状态] .last-changes.json 已记录（新增 ${#NEW_REPOS[@]} / 修改 ${#CHANGED_REPOS[@]}）"

# 4. 有变化 → 运行 mainline 兼容索引（动态 scope）
if [ -n "$CHANGED" ]; then
  echo "[索引] 变化仓库:$CHANGED"
  ./scripts/compare-mainline.sh --scope .scope-current.txt
  rc=$?
  echo "[索引] compare-mainline.sh 退出码 $rc"

  # 引擎失败（退出码 >1 = 脚本错误/离线）→ 不 commit、不更新 README、不写状态文件，
  # 原样退出，留待下次 cron 重试（避免把失败误当成功推进基线）
  if [ "$rc" -gt 1 ]; then
    rm -f .last-changes.json   # 撤销本次生成的仪表盘数据，README 不引用失败结果
    echo "[错误] compare-mainline.sh 失败（退出码 $rc），跳过提交/README/状态写入，下次 cron 重试"
    exit "$rc"
  fi

  # 4.6 引擎完成后：LLM 生成开发者摘要（deepseek-v4-flash，异步）
echo "[LLM] 生成开发者摘要（后台）..."
setsid nohup bash -lc "cd '$REPO_DIR' && ./scripts/report-llm.sh" >> logs/llm.log 2>&1 < /dev/null &

# 4.5 全量模式（或 hook 触发）下：索引后异步构建最新 mainline，验证可编译性
#     构建产物 mainline-build.md 由下一轮 cron 随报告提交（不阻塞本轮）
if [ "$FULL" -eq 1 ] && [ -x ./scripts/build-mainline.sh ]; then
  echo "[构建] 启动 mainline 自动构建（后台，结果写入 reports/ 并随下轮提交）..."
  setsid nohup bash -lc "cd '$REPO_DIR' && ./scripts/build-mainline.sh" >> logs/build.log 2>&1 < /dev/null &
fi

# 5. 提交：逐 repo 独立 commit + 聚合产物一个 commit，一次 push
DATE_DIR="reports/$(date +%Y-%m-%d)"
REPO_COMMITS=0
# 5.1 变化仓库的详情文件逐个 commit（追踪每 repo 兼容性变化）
for _n in ${CHANGED_REPOS[@]:-}; do
  _f="$DATE_DIR/$_n.md"
  if [ -f "$_f" ] && ! git diff --quiet -- "$_f"; then
    git add "$_f"
    git -c user.name="dsh-ecosystem-bot" -c user.email="bot@dsh-external.local" \
      commit -q -m "index: $_n 兼容性更新（$(date +%Y-%m-%d_%H%M)）" && REPO_COMMITS=$((REPO_COMMITS+1))
  fi
done
# 5.2 聚合产物（主报告/索引/CHANGELOG/README/状态）一个 commit
if git diff --quiet && git diff --cached --quiet; then
  echo "[提交] 无新内容，跳过 commit"
else
  git add -A
  git -c user.name="dsh-ecosystem-bot" -c user.email="bot@dsh-external.local" \
    commit -q -m "chore: 聚合产物更新 $(date +%Y-%m-%d_%H%M) — 变化:$CHANGED（repo 级 $REPO_COMMITS 个）" \
    && echo "[提交] repo 级 $REPO_COMMITS 个 + 聚合 1 个"
fi
git push dsh-ext main 2>&1 | tail -2 || echo "[提示] push 失败（网络），下次 cron 重试"
git push origin main 2>&1 | tail -1 || echo "[提示] origin 备份 push 失败，下次重试"
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
    cur="$(remote_head "$name" "$url")"
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
