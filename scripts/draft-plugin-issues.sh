#!/usr/bin/env bash
# 起草已收录插件的收录通知 issue（先起草：正文写到 .draft-issues/<name>.md，不直接提）
# 用法：draft-plugin-issues.sh [--apply]
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
GH="$HOME/.local/bin/gh"
APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1
mkdir -p .draft-issues

declare -A REPOS=(
  [chat-width]=dsh-external/chat-width
  [dsh-artifact]=dsh-external/dsh-artifact
  [dsh-split-panes]=dsh-external/dsh-split-panes
  [dsh-question-collapse]=dsh-external/dsh-question-collapse
  [dsh-sentinel]=fuhefei/dsh-sentinel
)

TITLE_TMPL="已被 Awesome DSH Plugins 收录 ✨"

for name in "${!REPOS[@]}"; do
  repo="${REPOS[$name]}"
  is_org=1
  case "$repo" in dsh-external/*) is_org=1 ;; *) is_org=0 ;; esac
  if [ "$is_org" = "1" ]; then
    EXTRA="本插件在 dsh-external org 内，已在每日自动扫描范围内——兼容性会持续跟踪并出现在目录状态分群中。无需额外操作。"
  else
    EXTRA="本插件当前在个人账号下，自动扫描仅覆盖 dsh-external org 内仓库。建议把仓库迁入（或 fork 到）dsh-external org——迁入后次日 02:00 起自动进入兼容性跟踪；不迁入也可，目录登记保持有效。"
  fi
  BODY="## 收录通知

你的插件 **$name** 已被 [Awesome DSH Plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) 收录（[PLUGINS.md](https://github.com/AdamPlatin123/awesome-dsh-plugins/blob/main/PLUGINS.md) 登记）。

**目录提供**：每日 mainline 快照四维兼容性对比、运行级实测（Agent + 人工复核）、需适配清单、开放 PR 跟踪。

$EXTRA

报告方：Awesome DSH Plugins（自动化目录，本条为简单通知，可关闭）"
  F=".draft-issues/$name.md"
  printf '%s\n' "$BODY" > "$F"
  if [ "$APPLY" = "1" ]; then
    if "$GH" issue create --repo "$repo" --title "$TITLE_TMPL" --body-file "$F" >/dev/null 2>&1; then
      echo "[已提] $name（$repo）"
    else
      echo "[失败] $name（$repo）"
    fi
  else
    echo "[起草] $name（$repo）→ .draft-issues/$name.md"
  fi
done
exit 0
