#!/usr/bin/env bash
# auto-merge-render.sh — Bot B 渲染 PR 自动合并（白名单守卫 + 直合并回退）
# 由 readme-render-watch.sh 在 PR 创建后调用
set -uo pipefail
export PATH=$HOME/.local/bin:$PATH
REPO=dsh-external/awesome-dsh-plugins
BR="${1:?用法: auto-merge-render.sh <branch>}"

N=$(gh pr list --repo "$REPO" --state open --head "$BR" --json number --jq '.[0].number' 2>/dev/null)
[ -n "$N" ] || { echo "[auto-merge] 无 open PR"; exit 0; }

# 白名单：渲染 PR 只允许 README.md + CHANGELOG.md
BAD=$(gh pr view --repo "$REPO" "$N" --json files \
  --jq '[.files[].path | select((. == "README.md" or . == "CHANGELOG.md") | not)] | length' 2>/dev/null)

if [ "${BAD:-1}" != "0" ]; then
  echo "[auto-merge] PR #$N 含白名单外文件（$BAD 处），留人工审"
  exit 0
fi

# 尝试 --auto（org 可能不开），失败回退直合并
gh pr merge --repo "$REPO" "$N" --auto --merge >/dev/null 2>&1
sleep 3
STATE=$(gh pr view --repo "$REPO" "$N" --json state --jq '.state' 2>/dev/null)
if [ "$STATE" = "OPEN" ]; then
  gh pr merge --repo "$REPO" "$N" --merge >/dev/null 2>&1
  sleep 3
  STATE=$(gh pr view --repo "$REPO" "$N" --json state --jq '.state' 2>/dev/null)
fi

if [ "$STATE" = "MERGED" ]; then
  echo "[auto-merge] PR #$N 已自动合并 ✓"
else
  echo "[auto-merge] PR #$N 未能合并（state=$STATE），留人工"
fi
