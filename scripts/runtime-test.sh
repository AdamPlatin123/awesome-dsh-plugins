#!/usr/bin/env bash
# 运行级真实测试：插件安装进 DSH（final 版 workspace）→ Qwen（内网零费用）拉起服务
# → headless 任务触发插件工具 → 观察报错
# SOP 1（跳过）：插件 HEAD 与 mainline 快照均未变 → 跳过该版本（沿用上次结果）
# SOP 2（支持性）：每个 repo 持续记录支持性（.support-status.json），报告从中生成
# 判定：✅ 可用 / ⚠️ 加载失败 / ❌ 工具调用失败 / ⏭️ 跳过（双未更新）
# 用法：runtime-test.sh [--limit N] [插件名...]
set -uo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
DATE="$(date +%Y-%m-%d)"
CLONES="$REPO_DIR/.clones"
BUILD="$REPO_DIR/.mainline-build"
QW_BASE="http://10.123.45.18:8080/v1"
NODE_BIN="$HOME/.nvm/versions/node/v24.14.1/bin"
export PATH="$NODE_BIN:$PATH"
STATE="$REPO_DIR/.runtime-test-state.json"
SUPPORT="$REPO_DIR/.support-status.json"
LIMIT=99999
CANDIDATES=()
for a in "$@"; do
  [[ "$a" =~ ^[0-9]+$ ]] && LIMIT="$a" && continue
  [ "$a" = "--limit" ] && continue
  CANDIDATES+=("$a")
done

echo "=== $(date -Is) runtime-test 开始（limit=$LIMIT） ==="
MAINLINE_HEAD="$(cd "$BUILD" && git rev-parse HEAD 2>/dev/null | cut -c1-12)"
[ -f "$STATE" ] || echo '{}' > "$STATE"
[ -f "$SUPPORT" ] || echo '{}' > "$SUPPORT"

# 1. 候选：显式指定；否则取需适配+关注清单
if [ ${#CANDIDATES[@]} -eq 0 ]; then
  LATEST="$(ls -d "$REPO_DIR"/reports/*/mainline-compat.md 2>/dev/null | sort | tail -1)"
  while IFS= read -r name; do
    CANDIDATES+=("$name")
  done < <(grep -E '^\| .* \| (需适配|关注)' "$LATEST" 2>/dev/null | awk -F'|' '{gsub(/ /,"",$2); print $2}' | head -"$LIMIT")
fi
echo "[候选] ${#CANDIDATES[@]} 个：${CANDIDATES[*]}"
echo "[mainline] $MAINLINE_HEAD"

# 2. symlink + install
mkdir -p "$BUILD/packages/tools"
LINKED=0
for name in "${CANDIDATES[@]}"; do
  [ -d "$CLONES/$name" ] || continue
  [ -e "$BUILD/packages/tools/$name" ] || { ln -sfn "$CLONES/$name" "$BUILD/packages/tools/$name" 2>/dev/null && LINKED=$((LINKED+1)); }
done
[ "$LINKED" -gt 0 ] && ( cd "$BUILD" && timeout 180 pnpm install --frozen-lockfile >/dev/null 2>&1 || timeout 300 pnpm install >/dev/null 2>&1 )

# 3. 逐插件测试
PASS=0; LOAD_FAIL=0; TOOL_FAIL=0; SKIP=0
declare -a RESULTS=()
N=0
for name in "${CANDIDATES[@]}"; do
  [ "$N" -ge "$LIMIT" ] && break
  N=$((N+1))
  [ -d "$CLONES/$name" ] || continue
  PLUGIN_HEAD="$(cd "$CLONES/$name" && git rev-parse --short HEAD 2>/dev/null || echo ?)"
  PREV="$(jq -r --arg n "$name" '.[$n].pluginHead // ""' "$STATE" 2>/dev/null)"
  PREV_ML="$(jq -r --arg n "$name" '.[$n].mainlineHead // ""' "$STATE" 2>/dev/null)"
  PREV_RESULT="$(jq -r --arg n "$name" '.[$n].result // ""' "$STATE" 2>/dev/null)"
  # SOP 1：双未更新 → 跳过
  if [ "$PLUGIN_HEAD" = "$PREV" ] && [ "$MAINLINE_HEAD" = "$PREV_ML" ] && [ -n "$PREV_RESULT" ]; then
    SKIP=$((SKIP+1)); RESULTS+=("$name|⏭️ 跳过（沿用：$PREV_RESULT）")
    echo "[跳过] $name"
    continue
  fi

  TASK="如果插件 $name 已加载，请调用它注册的工具（若有）并回复结果；若没有可调用工具，只回复：插件已加载 $name"
  echo "[测试] $name ..."
  OUT="$(cd "$BUILD" && timeout 240 env \
    DEEPSEEK_BASE_URL="$QW_BASE" DEEPSEEK_API_KEY="none" \
    node --import tsx packages/examples/cli-demo/src/bin.ts --config examples/headless-agent/cordis.yml "$TASK" 2>&1)"
  RC=$?
  if printf '%s' "$OUT" | grep -qiE "Cannot find module|failed to load|Error loading plugin|not found.*plugin|ENOENT"; then
    RESULT="⚠️ 加载失败"; LOAD_FAIL=$((LOAD_FAIL+1))
  elif [ $RC -ne 0 ]; then
    RESULT="❌ 运行报错（rc=$RC）"; TOOL_FAIL=$((TOOL_FAIL+1))
  else
    RESULT="✅ 可用"; PASS=$((PASS+1))
  fi
  RESULTS+=("$name|$RESULT")
  # SOP 2：写状态 + 支持性记录（每 repo 一条，持续更新）
  jq --arg n "$name" --arg ph "$PLUGIN_HEAD" --arg ml "$MAINLINE_HEAD" --arg r "$RESULT" --arg d "$DATE" \
    '.[$n] = {pluginHead: $ph, mainlineHead: $ml, result: $r, date: $d}' "$STATE" > "$STATE.tmp" && mv "$STATE.tmp" "$STATE"
  jq --arg n "$name" --arg s "${RESULT%%（*}" --arg d "$DATE" \
    '.[$n] = {support: $s, lastTest: $d}' "$SUPPORT" > "$SUPPORT.tmp" && mv "$SUPPORT.tmp" "$SUPPORT"
done

echo "[结果] 可用 $PASS / 加载失败 $LOAD_FAIL / 运行报错 $TOOL_FAIL / 跳过 $SKIP"

# 4. 报告（从支持性状态生成全量视角）
REPORT="$REPO_DIR/reports/$DATE/runtime-test.md"
mkdir -p "$REPO_DIR/reports/$DATE"
{
  echo "# 运行级真实测试（$DATE · Qwen3.6-35B 驱动 · mainline $MAINLINE_HEAD）"
  echo ""
  echo "- 方法：插件安装进 final 版 workspace → Qwen 拉起 dsh → headless 任务触发插件"
  echo "- SOP：插件与主仓库均未更新 → 跳过该版本；每 repo 支持性持续记录于 \`.support-status.json\`"
  echo ""
  echo "## 本轮结果"
  echo ""
  echo "| 插件 | 判定 |"
  echo "|---|---|"
  for r in "${RESULTS[@]:-}"; do
    echo "| ${r%%|*} | ${r#*|} |"
  done
  echo ""
  echo "## 支持性总览（持续跟踪，共 $(jq 'length' "$SUPPORT" 2>/dev/null) 个已测）"
  echo ""
  echo "| 插件 | 支持性 | 最后测试 |"
  echo "|---|---|---|"
  jq -r 'to_entries | sort_by(.key) | .[] | "| \(.key) | \(.value.support) | \(.value.lastTest) |"' "$SUPPORT" 2>/dev/null
  echo ""
  echo "## 汇总"
  echo ""
  echo "- 可用 $PASS / 加载失败 $LOAD_FAIL / 运行报错 $TOOL_FAIL / 跳过 $SKIP"
} > "$REPORT"
echo "[runtime-test] 报告已写入 $REPORT"
exit 0
