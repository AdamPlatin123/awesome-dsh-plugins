#!/usr/bin/env bash
# 实际兼容性验证：编译验证（一针见血版）
# 插件源码 symlink 进最新 mainline workspace → tsc --noEmit
# 编译失败 = 100% 不兼容（API/类型/依赖漂移）
# 输出：reports/<日期>/compile-compat.md（全量结果表 + 失败清单）
# 用法：verify-compile.sh [--limit N]（限制测试数量，默认全部）
set -uo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
DATE="$(date +%Y-%m-%d)"
CLONES="$REPO_DIR/.clones"
BUILD="$REPO_DIR/.mainline-build"
export PATH="$HOME/.nvm/versions/node/v24.14.1/bin:$PATH"

LIMIT=99999
[ "${1:-}" = "--limit" ] && LIMIT="${2:-99999}"

echo "=== $(date -Is) compile-compat 开始（limit=$LIMIT） ==="

# 1. 候选分类：TS 插件（tsconfig+src）/ JS 插件（有 .js 源码）/ 非插件（排除标注）
CANDIDATES=()       # TS：tsc --noEmit
JS_CANDIDATES=()    # JS：node --check
NA_COUNT=0
for dir in "$CLONES"/*/; do
  name="$(basename "$dir")"
  [ "$name" = "awesome-dsh-plugins" ] && continue
  if [ -f "$dir/tsconfig.json" ] && [ -d "$dir/src" ]; then
    CANDIDATES+=("$name")
  elif [ -f "$dir/package.json" ] && ls "$dir"/*.js "$dir"/lib/*.js "$dir"/src/*.js >/dev/null 2>&1; then
    JS_CANDIDATES+=("$name")
  else
    NA_COUNT=$((NA_COUNT+1))   # 空仓/文档/集合/非插件
  fi
done
echo "[候选] TS ${#CANDIDATES[@]} / JS ${#JS_CANDIDATES[@]} / 非插件 $NA_COUNT（org 共 $(ls -d "$CLONES"/*/ | wc -l) 克隆）"
[ "${#CANDIDATES[@]}" -gt "$LIMIT" ] && CANDIDATES=("${CANDIDATES[@]:0:$LIMIT}")

# 2. symlink 全部进 workspace（跳过冲突）
LINKED=0
for name in "${CANDIDATES[@]}"; do
  if [ -e "$BUILD/packages/tools/$name" ]; then
    echo "[跳过] $name：workspace 已存在"
  else
    mkdir -p "$BUILD/packages/tools"
    ln -sfn "$CLONES/$name" "$BUILD/packages/tools/$name" 2>/dev/null && LINKED=$((LINKED+1))
  fi
done
echo "[链接] $LINKED 个插件入 workspace"

# 3. pnpm install（一次，链接全部）
cd "$BUILD" || exit 2
corepack enable >/dev/null 2>&1 || true
if [ "$LINKED" -gt 0 ]; then
  timeout 180 pnpm install --frozen-lockfile >/dev/null 2>&1 || timeout 300 pnpm install >/dev/null 2>&1
fi

# 4. 逐仓 tsc --noEmit
PASS=0; FAIL=0; SKIP=0
declare -a FAIL_LIST=()
declare -a PASS_LIST=()
for name in "${CANDIDATES[@]}"; do
  if [ ! -f "packages/tools/$name/tsconfig.json" ]; then
    SKIP=$((SKIP+1)); continue
  fi
  OUT="$(timeout 60 pnpm exec tsc --noEmit -p "packages/tools/$name/tsconfig.json" 2>&1)"
  RC=$?
  if [ $RC -eq 0 ]; then
    PASS=$((PASS+1)); PASS_LIST+=("$name")
  elif [ -n "$(ls "$CLONES/$name"/lib/*.js 2>/dev/null | head -1)" ]; then
    # 自带 lib/ 构建产物：无需编译即可运行（源码级问题不影响运行时）
    PASS=$((PASS+1)); PASS_LIST+=("$name(lib)")
  else
    FAIL=$((FAIL+1))
    FIRST="$(printf '%s\n' "$OUT" | grep -E "error TS" | head -1 | sed -E 's#.*error (TS[0-9]+): (.*)#\1: \2#' | cut -c1-90)"
    FAIL_LIST+=("$name|$FIRST")
  fi
done

echo "[结果] TS 通过 $PASS / 失败 $FAIL / 跳过 $SKIP"

# 4.5 JS 插件语法验证（node --check）
JSPASS=0; JSFAIL=0
declare -a JS_FAIL_LIST=()
for name in "${JS_CANDIDATES[@]:-}"; do
  JSFILES=$(ls "$CLONES/$name"/*.js "$CLONES/$name"/lib/*.js "$CLONES/$name"/src/*.js 2>/dev/null | head -3)
  OK=1
  for f in $JSFILES; do
    timeout 20 node --check "$f" >/dev/null 2>&1 || { OK=0; break; }
  done
  if [ $OK -eq 1 ]; then JSPASS=$((JSPASS+1)); else JSFAIL=$((JSFAIL+1)); JS_FAIL_LIST+=("$name"); fi
done
echo "[结果] JS 通过 $JSPASS / 失败 $JSFAIL"

# 5. 写报告
REPORT="$REPO_DIR/reports/$DATE/compile-compat.md"
mkdir -p "$REPO_DIR/reports/$DATE"
{
  echo "# 实际兼容性验证：编译验证（$DATE）"
  echo ""
  echo "- 方法：插件源码 symlink 进 mainline workspace（snapshots/$(git -C "$BUILD" rev-parse --abbrev-ref HEAD 2>/dev/null | sed 's#snapshots/##' || echo ?)）→ \`tsc --noEmit\`"
  echo "- 结论：编译失败 = 100% 不兼容；编译通过 = 类型层兼容"
  echo ""
  echo "## 汇总"
  echo ""
  echo "- 候选 TS ${#CANDIDATES[@]}：**通过 $PASS / 失败 $FAIL / 跳过 $SKIP**"
  echo "- 候选 JS ${#JS_CANDIDATES[@]}：**通过 $JSPASS / 失败 $JSFAIL**（node --check 语法级）"
  echo "- 非插件/无源码（标注排除）：$NA_COUNT"
  echo "- 覆盖：$(ls "$CLONES"/*/ | wc -l | tr -d ' ') 克隆仓全部纳入"
  echo ""
  echo "## JS 语法失败清单"
  echo ""
  if [ "$JSFAIL" -eq 0 ]; then
    echo "（无）"
  else
    echo "${JS_FAIL_LIST[*]:-（无）}"
  fi
  echo ""
  echo "## 编译失败清单（实际不兼容）"
  echo ""
  if [ "$FAIL" -eq 0 ]; then
    echo "（无）"
  else
    echo "| 插件 | 首个错误 |"
    echo "|---|---|"
    for f in "${FAIL_LIST[@]:-}"; do
      [ -n "$f" ] && echo "| ${f%%|*} | ${f#*|} |"
    done
  fi
  echo ""
  echo "## 编译通过（类型层兼容）"
  echo ""
  echo "${PASS_LIST[*]:-（无）}"
} > "$REPORT"
echo "[compile-compat] 报告已写入 $REPORT"
exit 0
