#!/usr/bin/env bash
# 起草已收录插件的收录通知 issue（先起草：正文写到 .draft-issues/<name>.md，不直接提）
# 口径：开放收录——打 dsh-plugin topic 即纳入扫描，无需迁入任何 org
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
  [dsh-work]=vibeinging/dsh-work
  [dsh-tianshu-tui]=huiliyi37/dsh-tianshu-tui
)

TITLE_TMPL="已被 Awesome DSH Plugins 收录 ✨"

for name in "${!REPOS[@]}"; do
  repo="${REPOS[$name]}"
  BODY="## 收录通知

你的插件 **$name** 已被 [Awesome DSH Plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) 收录（[PLUGINS.md](https://github.com/AdamPlatin123/awesome-dsh-plugins/blob/main/PLUGINS.md) 登记）。

**收录与跟踪规则（开放）**：仓库打 \`dsh-plugin\` topic 即自动纳入每日扫描——mainline 快照四维兼容性对比、运行级实测（Agent + 人工复核）、需适配清单、开放 PR 跟踪，无需迁入任何组织。

本插件已打标，会自动持续跟踪。若想更快被收录或补充元数据，可在目录仓库提一个 PR（按 [PR 模板](https://github.com/AdamPlatin123/awesome-dsh-plugins/blob/main/.github/PULL_REQUEST_TEMPLATE.md) 在 PLUGINS.md 追加一行）。

报告方：Awesome DSH Plugins（自动化目录，本条为简单通知，可关闭）"
  F=".draft-issues/$name.md"
  printf '%s\n' "$BODY" > "$F"
  if [ "$APPLY" = "1" ]; then
    # 幂等：已存在同标题 open issue 则跳过（避免重复发送）
    if "$GH" issue list --repo "$repo" --state open --json title --jq ".[].title" 2>/dev/null | grep -qF "$TITLE_TMPL"; then
      echo "[跳过] $name（$repo）已提过，幂等跳过"
    elif "$GH" issue create --repo "$repo" --title "$TITLE_TMPL" --body-file "$F" >/dev/null 2>&1; then
      echo "[已提] $name（$repo）"
    else
      echo "[失败] $name（$repo）"
    fi
  else
    echo "[起草] $name（$repo）→ .draft-issues/$name.md"
  fi
done
exit 0
