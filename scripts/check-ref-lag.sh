#!/usr/bin/env bash
# ============================================================
# check-ref-lag.sh — 发布 ref 与仓库 HEAD 对比
#
# 对比"已发布的插件 ref"与"仓库当前 HEAD"，检测发布内容是否滞后于最新提交。
# 策略按仓库分派：
#   toybox    —— catalog.json 中 plugins[].source 的 #<40位commit>&path（jq 提取）
#                 + README.md <!-- INSTALL --> 块内的 #<40位commit>&path（正则提取）
#   dsh-skins —— catalog.json 中 plugins[].ref（pin）
# 对比目标为仓库远端 HEAD（git ls-remote 实时获取；离线显式报错）。
#
# 依赖：bash / git（必需）；jq（可选——有则用 jq 解析 catalog.json，
#       无则自动回退为正则提取，保证在未装 jq 的机器上也能跑）。
# 安全：失败日志输出前对 URL 做脱敏（user:pass@ → ***@；token 类查询参数打码）；
#       临时文件登记后由 EXIT trap 统一清理。
#
# 退出码：
#   0 = 无滞后（全部发布 ref 等于 HEAD）
#   1 = 有滞后（存在发布 ref 不等于 HEAD）
#   2 = 解析失败（无法解析的仓库 SKIP 并给出原因）
#   3 = 离线 / 网络错误
# 优先级：1（滞后）> 2（解析失败）> 0
#
# 用法：scripts/check-ref-lag.sh [--dry-run] [--clones-dir DIR] [repo...]
#   --dry-run        只读检查，跳过 git fetch（默认 best-effort fetch 刷新克隆）
#   --clones-dir DIR 克隆根目录（默认 <仓库根>/.clones）
#   repo...          要检查的仓库名（默认：toybox dsh-skins）
# ============================================================
set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLONES_DIR="${SCRIPT_DIR}/../.clones"
DRY_RUN=0
REPOS=(toybox dsh-skins)

usage() {
  cat <<'EOF'
用法：scripts/check-ref-lag.sh [--dry-run] [--clones-dir DIR] [repo...]

  --dry-run         只读检查，跳过 git fetch（默认会 best-effort fetch 刷新克隆）
  --clones-dir DIR  克隆根目录（默认 <仓库根>/.clones）
  repo...           要检查的仓库名（默认：toybox dsh-skins）

退出码：0=无滞后  1=有滞后  2=解析失败（SKIP）  3=离线/网络错误
EOF
}

# ---- 脱敏：URL 中的 user:pass@ → ***@；token 样式的查询参数打码 ----
# 失败日志输出前调用，防止 HTTPS user:token 或凭据类查询参数泄密
sanitize_text() {
  local s="$1"
  # 认证信息（user:pass@ 或 user@）→ ***@
  s=$(printf '%s' "$s" | sed -E 's#(://)[^/@[:space:]]*@#\1***@#g')
  # token 样式查询参数打码
  s=$(printf '%s' "$s" | sed -E 's#([?&](token|access_token|auth|api_key|apikey|key|secret|signature)=)[^&[:space:]]*#\1***#g')
  printf '%s' "$s"
}

# ---- 临时文件登记与退出清理（trap 兜底，防止中断残留） ----
TMP_FILES=()
cleanup() {
  local f
  for f in "${TMP_FILES[@]:-}"; do
    [ -n "$f" ] && rm -f -- "$f"
  done
}
trap cleanup EXIT

# ---- 参数解析 ----
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --clones-dir)
      [ $# -ge 2 ] || { echo "错误：--clones-dir 缺少参数" >&2; exit 2; }
      CLONES_DIR="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    -*) echo "错误：未知参数 $1（--help 查看用法）" >&2; exit 2 ;;
    *) REPOS=("$@"); break ;;
  esac
done

# ---- 依赖预检：bash / git 必需；jq 可选（有则用，无则正则回退） ----
missing=0
for cmd in bash git; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "错误：缺少依赖 '$cmd'（本脚本需要 bash / git）" >&2
    missing=1
  fi
done
[ "$missing" -ne 0 ] && exit 2

HAVE_JQ=0
if command -v jq >/dev/null 2>&1; then
  HAVE_JQ=1
else
  echo "提示：未检测到 jq，将使用正则（grep/sed）回退提取 catalog.json 中的 ref"
fi

# 已收集的发布 ref（去重）
FOUND=()

collect() {
  local r="$1" x
  for x in "${FOUND[@]:-}"; do
    [ "$x" = "$r" ] && return 0
  done
  FOUND+=("$r")
}

# 从 catalog.json 提取 source 中的 #<40位commit>&path（jq 优先；JSON 解析失败才回退正则）
extract_source_refs() {
  local file="$1" out
  if [ "$HAVE_JQ" -eq 1 ]; then
    if out="$(jq -r '.plugins[]?.source | capture("(?:.*)#(?<c>[0-9a-f]{40})&path:.*")? | .c' "$file" 2>/dev/null)"; then
      # jq 解析成功（可能无匹配，输出为空也是合法结果）→ 不回退正则
      printf '%s' "$out" | grep -v '^$'
      return 0
    fi
    echo "[提示] jq 解析 $file 失败（非法 JSON），回退正则提取" >&2
  fi
  grep -oE '#[0-9a-f]{40}&path' "$file" | sed 's/^#//; s/&path$//'
}

# 从 catalog.json 提取 pin 的 ref（plugins[].ref，jq 优先；JSON 解析失败才回退正则）
extract_pin_refs() {
  local file="$1" out
  if [ "$HAVE_JQ" -eq 1 ]; then
    if out="$(jq -r '.plugins[]?.ref? // empty' "$file" 2>/dev/null)"; then
      printf '%s' "$out" | grep -E '^[0-9a-f]{40}$'
      return 0
    fi
    echo "[提示] jq 解析 $file 失败（非法 JSON），回退正则提取" >&2
  fi
  grep -oE '"ref"[[:space:]]*:[[:space:]]*"[0-9a-f]{40}"' "$file" \
    | sed -E 's/.*"([0-9a-f]{40})".*/\1/'
}

# ---- toybox 策略：catalog.json source + README INSTALL 块（两来源必须同时可解析，任一失败即 SKIP） ----
check_toybox() {
  local dir="$1" repo="$2"
  local cat="$dir/catalog.json" readme="$dir/README.md"
  local refs got_cat=0 got_readme=0
  FOUND=()

  # 来源 1：catalog.json 的 plugins[].source（#<40位commit>&path）
  if [ ! -f "$cat" ]; then
    echo "[$repo] 来源 catalog.json 缺失（$cat）"
  else
    refs=$(extract_source_refs "$cat" | sort -u)
    if [ -n "$refs" ]; then
      while IFS= read -r r; do collect "$r"; done <<<"$refs"
      got_cat=1
      echo "[$repo] catalog.json source：提取到 $(wc -l <<<"$refs" | tr -d ' ') 个发布 ref"
    else
      echo "[$repo] 来源 catalog.json 未匹配到 #<40位commit>&path 形式的 ref（内容不符或无法解析）"
    fi
  fi

  # 来源 2：README.md <!-- INSTALL --> 块（正则 #<40位commit>&path）
  if [ ! -f "$readme" ]; then
    echo "[$repo] 来源 README.md 缺失（$readme）"
  else
    refs=$(awk '/<!-- INSTALL -->/{f=1;next} /<!-- \/INSTALL -->/{f=0} f' "$readme" \
      | grep -oE '#[0-9a-f]{40}&path' | sed 's/^#//; s/&path$//' | sort -u)
    if [ -n "$refs" ]; then
      while IFS= read -r r; do collect "$r"; done <<<"$refs"
      got_readme=1
      echo "[$repo] README INSTALL 块：提取到 $(wc -l <<<"$refs" | tr -d ' ') 个发布 ref"
    else
      echo "[$repo] 来源 README INSTALL 块未匹配到 #<40位commit>&path（未发布或块缺失）"
    fi
  fi

  # 两来源任一失败（文件缺失 / 无法解析 / 无 ref）→ SKIP，不以另一来源单向通过（避免漏检滞后）
  if [ "$got_cat" -ne 1 ] || [ "$got_readme" -ne 1 ]; then
    echo "[$repo] SKIP：catalog.json 与 README INSTALL 块两个来源必须同时可解析（解析失败）"
    return 2
  fi
  return 0
}

# ---- dsh-skins 策略：catalog.json 的 plugins[].ref（pin） ----
check_skins() {
  local dir="$1" repo="$2"
  local cat="$dir/catalog.json" refs
  FOUND=()

  if [ ! -f "$cat" ]; then
    echo "[$repo] SKIP：缺少 catalog.json（$cat）"
    return 2
  fi
  refs=$(extract_pin_refs "$cat" | sort -u)
  if [ -z "$refs" ]; then
    echo "[$repo] SKIP：catalog.json 无法解析或未找到 plugins[].ref（pin）"
    return 2
  fi
  while IFS= read -r r; do collect "$r"; done <<<"$refs"
  echo "[$repo] catalog.json pin ref：$(wc -l <<<"$refs" | tr -d ' ') 个"
  return 0
}

# ---- 对比发布 ref 与仓库远端 HEAD ----
compare_head() {
  local dir="$1" repo="$2"
  local remote err head_sha r lagged=0

  remote=$(git -C "$dir" config --get remote.origin.url 2>/dev/null) || true
  [ -n "$remote" ] || remote="https://github.com/dsh-external/$repo.git"

  if [ "$DRY_RUN" -eq 0 ]; then
    git -C "$dir" fetch origin --quiet >/dev/null 2>&1 || true
  fi

  err=$(mktemp) || { echo "错误：无法创建临时文件" >&2; exit 2; }
  TMP_FILES+=("$err")
  head_sha=$(git ls-remote "$remote" HEAD 2>"$err" | awk '{print $1}')
  if [ -z "$head_sha" ]; then
    if [ -s "$err" ]; then
      local errtext
      errtext="$(tr -d '\n' <"$err")"
      # 404/无权限：仓库不存在或无权访问 → 状态"未知"，退出码 2（解析失败类），非离线
      if printf '%s' "$errtext" | grep -qiE 'repository not found|not found|404|access denied|permission denied|not authorized|403'; then
        echo "[$repo] 未知：远程不可访问（404/无权限）——$(sanitize_text "$errtext")"
        return 2
      fi
      # 输出前脱敏：remote 可能含 user:token，git stderr 也可能回显完整 URL
      echo "[$repo] 错误：无法访问远程 $(sanitize_text "$remote") —— 疑似离线（$(sanitize_text "$errtext")）"
      return 3
    fi
    echo "[$repo] SKIP：远程仓库无任何提交（HEAD 为空），无法对比"
    return 2
  fi

  echo "[$repo] 仓库 HEAD：$head_sha"
  for r in "${FOUND[@]}"; do
    if [ "$r" != "$head_sha" ]; then
      echo "[$repo] 滞后：发布 ref $r  !=  HEAD $head_sha"
      lagged=1
    fi
  done
  if [ "$lagged" -eq 0 ]; then
    echo "[$repo] 无滞后：全部 ${#FOUND[@]} 个发布 ref 均等于 HEAD"
  else
    echo "[$repo] 警告：发布内容落后于仓库最新提交，需重新发布（更新 catalog / INSTALL 块）"
  fi
  return "$lagged"
}

# ---- 主流程 ----
overall=0
any_skip=0

for repo in "${REPOS[@]}"; do
  dir="$CLONES_DIR/$repo"
  echo "== $repo =="

  if [ ! -d "$dir" ]; then
    echo "[$repo] SKIP：克隆目录不存在（$dir）"
    any_skip=1
    continue
  fi

  rc=0
  case "$repo" in
    toybox)    check_toybox "$dir" "$repo"; rc=$? ;;
    dsh-skins) check_skins "$dir" "$repo"; rc=$? ;;
    *)
      echo "[$repo] SKIP：无对比策略（仅支持 toybox / dsh-skins）"
      any_skip=1
      continue ;;
  esac

  if [ "$rc" -eq 2 ]; then
    any_skip=1
    continue
  fi

  compare_head "$dir" "$repo"
  rc=$?
  if [ "$rc" -eq 3 ]; then
    echo "错误：离线或网络不可达（退出码 3）" >&2
    exit 3
  fi
  if [ "$rc" -eq 2 ]; then
    # SKIP / 未知（404、无提交、无法解析）→ 计入 any_skip，最终退出码 2
    any_skip=1
    continue
  fi
  [ "$rc" -eq 1 ] && overall=1
done

echo
if [ "$overall" -eq 1 ]; then
  echo "结论：存在发布 ref 滞后，需要重新发布（退出码 1）"
  exit 1
fi
if [ "$any_skip" -eq 1 ]; then
  echo "结论：部分仓库解析失败被跳过，请人工检查（退出码 2）"
  exit 2
fi
echo "结论：全部发布 ref 均无滞后（退出码 0）"
exit 0
