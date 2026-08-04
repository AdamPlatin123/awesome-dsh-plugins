#!/usr/bin/env bash
# 每 8 小时自动运行（cron）：检测 dsh-external org 仓库与 mainline 变化，
# 有变化的仓库触发 mainline 兼容索引，更新报告/CHANGELOG 并推送回 org repo。
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
git pull dsh-ext main --ff-only 2>&1 | tail -2 || echo "[提示] git pull 失败（可能离线或已最新），继续"

# 2. 检测 mainline + 15 个 org 仓库的 HEAD 变化
STATE=".cron-state.json"
CHANGED=""
declare -a REPOS=(
  "mainline|https://github.com/dsh2026/test-AdamPlatin123"
  "issues|https://github.com/dsh-external/issues"
  "dsh-live-stats|https://github.com/dsh-external/dsh-live-stats"
  "dsh-working-activity|https://github.com/dsh-external/dsh-working-activity"
  "plugin-registry|https://github.com/dsh-external/plugin-registry"
  "sandbox-mxc|https://github.com/dsh-external/sandbox-mxc"
  "web-components|https://github.com/dsh-external/web-components"
  "dsh-opencode-server|https://github.com/dsh-external/dsh-opencode-server"
  "toybox|https://github.com/dsh-external/toybox"
  "ex-setting|https://github.com/dsh-external/ex-setting"
  "tg-bot|https://github.com/dsh-external/tg-bot"
  "group-chat-diary|https://github.com/dsh-external/group-chat-diary"
  "dsh-skins|https://github.com/dsh-external/dsh-skins"
  "dsh-coding-receipt|https://github.com/dsh-external/dsh-coding-receipt"
  "qqbot|https://github.com/dsh-external/qqbot"
  "dsh-subagent-tree|https://github.com/dsh-external/dsh-subagent-tree"
)

if [ -f "$STATE" ]; then
  for entry in "${REPOS[@]}"; do
    name="${entry%%|*}"; url="${entry#*|}"
    prev="$(jq -r --arg n "$name" '.[$n] // ""' "$STATE" 2>/dev/null || echo "")"
    cur="$(timeout 20 git ls-remote "$url" HEAD 2>/dev/null | awk '{print $1}')"
    if [ -z "$cur" ]; then
      echo "[跳过] $name：ls-remote 失败（离线/网络），保留上次状态"
    elif [ -n "$prev" ] && [ "$cur" != "$prev" ]; then
      CHANGED="$CHANGED $name"
      echo "[变化] $name: $prev -> $cur"
    fi
  done
else
  echo "[首次运行] 无状态文件，执行全量索引"
  CHANGED="all(首次)"
fi

# 3. 有变化 → 运行 mainline 兼容索引
if [ -n "$CHANGED" ]; then
  echo "[索引] 变化仓库:$CHANGED"
  ./scripts/compare-mainline.sh
  rc=$?
  echo "[索引] compare-mainline.sh 退出码 $rc"

  # 4. 提交报告/CHANGELOG/状态并推送回 org repo
  if git diff --quiet && git diff --cached --quiet; then
    echo "[提交] 无新内容，跳过 commit"
  else
    git add -A
    git -c user.name="dsh-ecosystem-bot" -c user.email="bot@dsh-external.local" \
      commit -m "chore: 自动索引更新 $(date +%Y-%m-%d_%H%M) — 变化:$CHANGED" || echo "[提示] commit 失败"
    git push dsh-ext main 2>&1 | tail -2 || echo "[提示] push 失败（网络），下次 cron 重试"
  fi
else
  echo "[无变化] 15 仓库 + mainline HEAD 均未变，跳过索引"
fi

# 5. 更新状态文件（记录当前 HEAD）
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
