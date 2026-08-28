#!/usr/bin/env bash
# 插件修复自动化（低风险项）：
#   1. TS5101 baseUrl 弃用 → 删除 baseUrl（paths 改相对）
#   2. TS2688 缺类型包 → 识别并提示 pnpm add -D <@types/pkg>
#   3. 第三方依赖缺失（TS2307 非 @deepseek-ai）→ 识别缺失包名提示 pnpm add
# 高风险（TS2339 API 漂移）不自动修——输出"需人工"清单。
# 用法：fix-plugin.sh [--apply] [--limit N]   （默认 dry-run 只出 diff/建议）
# 输出：reports/<日期>/plugin-fix.md
set -uo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
DATE="$(date +%Y-%m-%d)"
CLONES="$REPO_DIR/.clones"
BUILD="$REPO_DIR/.mainline-build"
APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1
LIMIT=99999
for a in "$@"; do [ "$a" = "--limit" ] && APPLY=0; done
[ "${1:-}" = "--limit" ] && LIMIT="${2:-99999}"

echo "=== $(date -Is) plugin-fix 开始（apply=$APPLY） ==="

declare -a FIXED_BASEURL=()
declare -a SUGGEST_TYPES=()
declare -a SUGGEST_DEPS=()
declare -a MANUAL=()

# 扫描 TS 插件 tsconfig 的 baseUrl 弃用（TS5101）
N=0
for t in "$CLONES"/*/tsconfig.json; do
  [ -f "$t" ] || continue
  name="$(basename "$(dirname "$t")")"
  [ "$N" -ge "$LIMIT" ] && break
  if grep -q '"baseUrl"' "$t" 2>/dev/null; then
    N=$((N+1))
    # 检查 baseUrl 值是否为旧式根目录引用
    BASEURL_VAL="$(python3 -c "import json;print(json.load(open('$t')).get('compilerOptions',{}).get('baseUrl',''))" 2>/dev/null)"
    if [ "$APPLY" -eq 1 ]; then
      python3 - "$t" << 'EOF'
import json, sys
p = sys.argv[1]
d = json.load(open(p))
co = d.get("compilerOptions", {})
co.pop("baseUrl", None)
# paths 若以 baseUrl 为根 → 改为相对 src
paths = co.get("paths", {})
if paths:
    for k in paths:
        paths[k] = [v[3:] if v.startswith("./") else v for v in paths[k]]
co["paths"] = paths
d["compilerOptions"] = co
json.dump(d, open(p, "w"), indent=2, ensure_ascii=False)
EOF
      FIXED_BASEURL+=("$name")
    else
      FIXED_BASEURL+=("$name(baseUrl=$BASEURL_VAL)")
    fi
  fi
done

# 分析已知编译失败：缺 types 与第三方依赖（从 compile-compat 报告的错误）
COMPAT="$REPO_DIR/reports/$DATE/compile-compat.md"
[ -f "$COMPAT" ] || COMPAT="$(ls "$REPO_DIR"/reports/*/compile-compat.md 2>/dev/null | tail -1)"
if [ -n "$COMPAT" ]; then
  while IFS= read -r line; do
    name="$(printf '%s' "$line" | cut -d'|' -f2 | tr -d ' ')"
    err="$(printf '%s' "$line" | grep -oE "TS[0-9]+: .*" | head -1)"
    case "$err" in
      *"Cannot find type definition file for"*)
        pkg="$(printf '%s' "$err" | sed -E "s#.*for '([^']+)'.*#\1#")"
        SUGGEST_TYPES+=("$name → @types/$pkg") ;;
      *"Cannot find module '"*)
        mod="$(printf '%s' "$err" | sed -E "s#.*Cannot find module '([^']+)'.*#\1#")"
        case "$mod" in
          @deepseek-ai/*|cordis|schemastery|react|electron) ;;  # 环境类，不自动修
          *) SUGGEST_DEPS+=("$name → $mod") ;;
        esac ;;
      TS2339*|TS2345*|TS2322*)
        MANUAL+=("$name → $err") ;;
    esac
  done < <(grep -E '^\| ' "$COMPAT" 2>/dev/null | grep -v '^|--' | sed -n '2,200p')
fi

# 写报告
REPORT="$REPO_DIR/reports/$DATE/plugin-fix.md"
mkdir -p "$REPO_DIR/reports/$DATE"
MODE="DRY-RUN（未写入）"
[ "$APPLY" -eq 1 ] && MODE="APPLY（已写入）"
{
  echo "# 插件修复自动化报告（$DATE）"
  echo ""
  echo "- 模式：$MODE"
  echo ""
  echo "## 1. baseUrl 弃用（TS5101）——自动修复 ${#FIXED_BASEURL[@]}"
  echo ""
  [ ${#FIXED_BASEURL[@]} -eq 0 ] && echo "（无）" || printf '%s\n' "${FIXED_BASEURL[@]}" | sed 's/^/- /'
  echo ""
  echo "## 2. 缺类型包（TS2688）——建议 ${#SUGGEST_TYPES[@]}"
  echo ""
  [ ${#SUGGEST_TYPES[@]} -eq 0 ] && echo "（无）" || printf '%s\n' "${SUGGEST_TYPES[@]}" | sed 's/^/- pnpm add -D /'
  echo ""
  echo "## 3. 第三方依赖缺失（TS2307）——建议 ${#SUGGEST_DEPS[@]}"
  echo ""
  [ ${#SUGGEST_DEPS[@]} -eq 0 ] && echo "（无）" || printf '%s\n' "${SUGGEST_DEPS[@]}" | sed 's/^/- pnpm add /'
  echo ""
  echo "## 4. 需人工修复（API 漂移类）${#MANUAL[@]}"
  echo ""
  [ ${#MANUAL[@]} -eq 0 ] && echo "（无）" || printf '%s\n' "${MANUAL[@]}" | sed 's/^/- /'
} > "$REPORT"
echo "[fix] 报告已写入 $REPORT"
exit 0
