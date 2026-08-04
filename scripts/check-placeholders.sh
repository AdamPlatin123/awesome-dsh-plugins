#!/usr/bin/env bash
# ============================================================
# check-placeholders.sh — 占位仓库三态检查
#
# 跟踪两个"有跟踪价值"的占位仓库（已建立调研摘要，等待出现代码）：
#   - dsh-external/dsh-opencode-server
#   - dsh-external/dsh-coding-receipt
#
# 三态判定：
#   404    —— gh api 返回 404，仓库不存在（可能已删除/改名）
#   空仓   —— 仓库存在但无任何提交（git ls-remote 返回空）
#   有提交 —— 仓库出现提交（引用非空），触发"重新调研"提示
#
# 退出码：
#   0 = 无新提交（仍为占位，无需重新调研）
#   1 = 有仓库出现了提交（需要重新调研）
#   2 = 依赖缺失（bash/git/gh）
#   3 = 离线 / gh 未认证
#
# 用法：scripts/check-placeholders.sh
# ============================================================
set -u

ORG="dsh-external"
REPOS=(dsh-opencode-server dsh-coding-receipt)

# ---- 依赖预检：bash / git / gh ----
missing=0
for cmd in bash git gh; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "错误：缺少依赖 '$cmd'（本脚本需要 bash / git / gh）" >&2
    missing=1
  fi
done
[ "$missing" -ne 0 ] && exit 2

# ---- gh 认证检查 ----
if ! gh auth status >/dev/null 2>&1; then
  echo "错误：gh 未认证（或不可用），请先执行 'gh auth login'（退出码 3）" >&2
  exit 3
fi

# ---- 网络预检（区分"离线"与"未认证"） ----
if ! gh api rate_limit >/dev/null 2>&1; then
  echo "错误：网络不可达（GitHub API 调用失败），请检查网络/代理后重试（退出码 3）" >&2
  exit 3
fi

tmp=$(mktemp) || { echo "错误：无法创建临时文件" >&2; exit 2; }
trap 'rm -f "$tmp"' EXIT

has_commits=0

for repo in "${REPOS[@]}"; do
  printf '[%s] ' "$repo"

  # 状态一：404（仓库不存在）
  if ! gh api "repos/$ORG/$repo" --jq '.size' >/dev/null 2>"$tmp"; then
    if grep -q 'HTTP 404' "$tmp"; then
      echo '404 —— 仓库不存在（可能已删除或改名），继续占位跟踪'
    else
      echo "gh api 调用失败：$(tr -d '\n' <"$tmp") —— 按离线处理（退出码 3）"
      exit 3
    fi
    continue
  fi

  # 状态二/三：空仓 or 有提交（git ls-remote 是否返回任何引用；
  # 引用非空即存在指向 commit 的 ref，说明仓库已有提交）
  if ! refs=$(git ls-remote "https://github.com/$ORG/$repo.git" 2>"$tmp"); then
    echo "git ls-remote 失败：$(tr -d '\n' <"$tmp") —— 按离线处理（退出码 3）"
    exit 3
  fi

  if [ -n "$refs" ]; then
    echo '有提交 —— 仓库已出现代码，需要重新调研！'
    has_commits=1
  else
    echo '空仓 —— 仓库存在但无任何提交，继续占位跟踪'
  fi
done

echo
if [ "$has_commits" -ne 0 ]; then
  echo "结论：有占位仓库出现了提交，需要重新调研（退出码 1）"
  exit 1
fi
echo "结论：两个占位仓库均无新提交，保持现状即可（退出码 0）"
exit 0
