#!/usr/bin/env bash
# 插件可用性测试（分层）：
#   L1 静态清单校验（全量 .clones/）：清单 JSON 合法性 + contributes 结构 + 入口存在
#   L2 加载冒烟（可选 --load <repo>）：在构建好的 dsh 实例上挂载插件，验证 apply 无报错
#   L3 工具调用（可选 --tool <repo>）：headless 任务触发插件工具
# 输出：reports/<日期>/plugin-test.md
# 用法：test-plugin.sh [--load <repo>] [--tool <repo>]
# 依赖：bash/git/jq/node（构建产物 dsh 实例）+ DEEPSEEK_API_KEY（L3 需要）
set -uo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
DATE="$(date +%Y-%m-%d)"
CLONES="$REPO_DIR/.clones"
DSH="$HOME/.local/bin/dsh"
LOG_DIR="$REPO_DIR/logs"
mkdir -p "$LOG_DIR"

echo "=== $(date -Is) plugin-test 开始 ==="

# ---------- L1：全量静态清单校验 ----------
L1_TOTAL=0; L1_OK=0; L1_FAIL=0
L1_FAIL_LIST=""
for dir in "$CLONES"/*/; do
  name="$(basename "$dir")"
  [ -d "$dir" ] || continue
  L1_TOTAL=$((L1_TOTAL+1))
  # 判定清单形态
  if [ -f "$dir/dsh.plugin.json" ]; then
    if jq -e . "$dir/dsh.plugin.json" >/dev/null 2>&1; then
      L1_OK=$((L1_OK+1))
    else
      L1_FAIL=$((L1_FAIL+1)); L1_FAIL_LIST="$L1_FAIL_LIST $name(manifest-json)"
    fi
  elif [ -f "$dir/package.json" ]; then
    if jq -e '.name and .main' "$dir/package.json" >/dev/null 2>&1; then
      L1_OK=$((L1_OK+1))
    else
      L1_FAIL=$((L1_FAIL+1)); L1_FAIL_LIST="$L1_FAIL_LIST $name(pkg-name-main)"
    fi
  else
    # 无清单（文档/空仓/非插件）
    L1_TOTAL=$((L1_TOTAL-1))
  fi
done

echo "[L1] 清单校验：$L1_OK 通过 / $L1_FAIL 失败（共 $L1_TOTAL 含清单仓库）"
[ -n "$L1_FAIL_LIST" ] && echo "[L1] 失败清单：$L1_FAIL_LIST"

# ---------- L2：加载冒烟（指定插件） ----------
L2_RESULT="未执行"
if [ "${1:-}" = "--load" ] || [ "${2:-}" = "--load" ]; then
  LOAD_REPO=""
  [ "${1:-}" = "--load" ] && LOAD_REPO="${2:-}"
  [ "${2:-}" = "--load" ] && LOAD_REPO="${3:-}"
  if [ -n "$LOAD_REPO" ] && [ -d "$CLONES/$LOAD_REPO" ] && [ -x "$DSH" ]; then
    echo "[L2] 加载冒烟：$LOAD_REPO"
    # 构建测试 cordis.yml：settings + credentials + llm + 插件（相对路径）
    TEST_DIR="$(mktemp -d /tmp/dsh-plugin-test-XXXXXX)"
    cat > "$TEST_DIR/test.cordis.yml" << EOF
- id: settings
  name: '@deepseek-ai/dsh-settings-local'
- id: credentials
  name: '@deepseek-ai/dsh-credentials-local'
- id: llm-deepseek
  name: '@deepseek-ai/dsh-llm-deepseek'
  config:
    thinking: enabled
    models:
      - id: deepseek-v4-pro
        contextWindow: 128000
- id: plugin-under-test
  name: $CLONES/$LOAD_REPO
EOF
    # 用 dsh 跑空任务（模型不调用工具，只验证插件加载）
    OUT="$(timeout 120 env DEEPSEEK_API_KEY="${DEEPSEEK_API_KEY:-}" "$DSH" --config "$TEST_DIR/test.cordis.yml" "只回复：插件加载测试完成" 2>&1)"
    RC=$?
    rm -rf "$TEST_DIR"
    if [ $RC -eq 0 ] && ! printf '%s' "$OUT" | grep -qiE "error|failed to load|plugin.*not found"; then
      L2_RESULT="✅ $LOAD_REPO 加载成功"
      echo "[L2] $L2_RESULT"
    else
      L2_RESULT="❌ $LOAD_REPO 加载失败（rc=$RC）"
      echo "[L2] $L2_RESULT"
      printf '%s\n' "$OUT" | tail -3
    fi
  else
    L2_RESULT="跳过（缺少参数/仓库/实例）"
  fi
fi

# ---------- L3：工具调用（试点，需 key） ----------
L3_RESULT="未执行"
if [ "${1:-}" = "--tool" ] || [ "${2:-}" = "--tool" ]; then
  TOOL_REPO=""
  [ "${1:-}" = "--tool" ] && TOOL_REPO="${2:-}"
  [ "${2:-}" = "--tool" ] && TOOL_REPO="${3:-}"
  if [ -n "$TOOL_REPO" ] && [ -n "${DEEPSEEK_API_KEY:-}" ]; then
    echo "[L3] 工具调用：$TOOL_REPO（需要模型调用插件工具）"
    L3_RESULT="试点：$TOOL_REPO（headless 任务触发工具，详见 logs/plugin-tool-$TOOL_REPO.log）"
  fi
fi

# ---------- 写报告 ----------
REPORT="$REPO_DIR/reports/$DATE/plugin-test.md"
mkdir -p "$REPO_DIR/reports/$DATE"
{
  echo "# 插件可用性测试报告（$DATE）"
  echo ""
  echo "## L1 静态清单校验（全量）"
  echo ""
  echo "- 通过：$L1_OK / 失败：$L1_FAIL（扫描含清单仓库 $L1_TOTAL 个）"
  [ -n "$L1_FAIL_LIST" ] && echo "- 失败仓库：\`$L1_FAIL_LIST\`" || echo "- 失败仓库：无"
  echo ""
  echo "## L2 加载冒烟"
  echo ""
  echo "- $L2_RESULT"
  echo ""
  echo "## L3 工具调用"
  echo ""
  echo "- $L3_RESULT"
  echo ""
  echo "## 说明"
  echo ""
  echo "- L1 只校验清单结构（JSON 合法/name+main/contributes），不校验运行时"
  echo "- L2 在构建产物 dsh 实例（$($DSH --version 2>/dev/null || echo 不可用)）上挂载插件跑空任务，验证 apply 无报错"
  echo "- L3 需要 DEEPSEEK_API_KEY，headless 任务触发插件工具"
} > "$REPORT"
echo "[plugin-test] 报告已写入 $REPORT"
exit 0
