#!/usr/bin/env bash
# 分片并行运行级测试——独立于 runtime-test.sh（避免版本漂移）
# 用法：run-shard.sh <shard_id> <插件名...>
# 每插件：生成 patch → dsh --profile headless --patch 跑 → 判定 → 记录独立状态
set -uo pipefail
[ -f "$HOME/.dsh-radar.env" ] && . "$HOME/.dsh-radar.env"
SHARD_ID="$1"; shift
PLUGINS=("$@")
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CLONES="$REPO_DIR/.clones"
BUILD="$REPO_DIR/.mainline-build"
QW_BASE="${DSH_QWEN_BASE_URL:-http://127.0.0.1:1/v1}"
export PATH="$HOME/.nvm/versions/node/v24.14.1/bin:$PATH"
STATE="$REPO_DIR/.runtime-test-state.shard$SHARD_ID.json"
DATE="$(date +%Y-%m-%d)"
[ -f "$STATE" ] || echo '{}' > "$STATE"
MAINLINE_HEAD="$(cd "$BUILD" && git rev-parse HEAD 2>/dev/null | cut -c1-12)"

echo "[shard-$SHARD_ID] $(date +%H:%M:%S) 开始 ${#PLUGINS[@]} 个：${PLUGINS[*]}"
for name in "${PLUGINS[@]}"; do
  [ -d "$CLONES/$name" ] || { echo "[shard-$SHARD_ID] 跳过 $name（无 clone）"; continue; }
  PKG_NAME="$(jq -r .name "$CLONES/$name/package.json" 2>/dev/null || echo "@dsh-external/$name")"
  PATCH="/tmp/dsh-shard-$SHARD_ID-$name.yml"
  printf -- "- insert:\n    - id: %s\n      name: '%s'\n" "$name" "$PKG_NAME" > "$PATCH"
  TASK="如果插件 $name 已加载，请调用它注册的工具（若有）并回复结果；若没有可调用工具，只回复：插件已加载 $name"
  OUT="$(cd "$BUILD" && timeout 200 env DEEPSEEK_BASE_URL="$QW_BASE" DEEPSEEK_API_KEY=none \
    node apps/cli/lib/bin.js --profile headless --patch "$PATCH" "$TASK" 2>&1)"
  RC=$?
  rm -f "$PATCH"
  # 判定：加载失败=明确模块/插件解析错误；运行报错=退出码非0但非加载类；可用=其余
  if printf '%s' "$OUT" | grep -qiE "Cannot find module|ERR_MODULE_NOT_FOUND|failed to load.*plugin|plugin.*not registered|Cannot resolve"; then
    RESULT="⚠️ 加载失败"
  elif [ $RC -ne 0 ]; then
    RESULT="❌ 运行报错(rc=$RC)"
  else
    RESULT="✅ 可用"
  fi
  ERR="$(printf '%s' "$OUT" | grep -iE "Cannot find module|ERR_MODULE_NOT_FOUND|Error:" | head -1 | cut -c1-80)"
  echo "[shard-$SHARD_ID] $name → $RESULT ${ERR:+| $ERR}"
  jq --arg n "$name" --arg r "$RESULT" --arg e "$ERR" --arg d "$DATE" \
    '.[$n] = {result: $r, err: $e, date: $d}' "$STATE" > "$STATE.tmp" && mv "$STATE.tmp" "$STATE"
done
echo "[shard-$SHARD_ID] $(date +%H:%M:%S) 完成"
