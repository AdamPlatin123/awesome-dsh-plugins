#!/usr/bin/env bash
# test-plugin-agent.sh — dsh（agent 框架，原生 Qwen）驱动的插件导入测试
#
# 容器内：dsh --profile headless（DEEPSEEK_BASE_URL→内网 Qwen3.6-35B）读插件 repo 的
# README/package.json，自主按 repo 文档把插件导入并验证加载。导入尝试最多 3 次，
# 任一次成功→✅可用；3 次全败→❌不兼容。无需任何桥（dsh 原生说 Qwen）。
#
# 用法：test-plugin-agent.sh <plugin_dir_name>
#   插件源码挂载在 /clones/<plugin_dir_name>；dsh profile 挂载在 $DSH_HOME（来自宿主 ~/.dsh）
set -uo pipefail

PLUGIN="${1:?用法: test-plugin-agent.sh <plugin_dir_name>}"
CLONE="/clones/$PLUGIN"
OUT_DIR="/radar/.rt-agent"
mkdir -p "$OUT_DIR"
MAX_TRIES=3
RESULT="❌ 不兼容"
LAST_ERR=""

[ -d "$CLONE" ] || { echo "[$PLUGIN] ⏭️ 跳过（clone 不存在）"; RESULT="⏭️ 跳过"; exit 0; }
export DEEPSEEK_API_KEY="${DEEPSEEK_API_KEY:-none}"
# dsh 组合 profile 需写 node_modules——把只读 /dsh-home 复制到可写私有目录
export DSH_HOME="${DSH_HOME:-/home/node/.dsh}"
if [ -d /dsh-home ] && [ ! -d "$DSH_HOME" ]; then cp -r /dsh-home "$DSH_HOME" 2>/dev/null || true; fi
# de-stream 代理：vLLM 流式 tool_call 的 name 为 null（bug），非流式则完整。
# 本地起 destream-proxy（dsh stream=True → Qwen stream=False → 重包 SSE），dsh 经它拿完整 tool name。
PROXY_PORT="${PROXY_PORT:-18093}"
mkdir -p "$OUT_DIR/../logs"
if ! curl -sf -m 2 http://127.0.0.1:$PROXY_PORT/v1/models >/dev/null 2>&1; then
  nohup python3 /usr/local/bin/destream-proxy.py >>"$OUT_DIR/../logs/destream.log" 2>&1 &
  for _ in 1 2 3 4 5 6 7 8; do curl -sf -m 2 http://127.0.0.1:$PROXY_PORT/v1/models >/dev/null 2>&1 && break; sleep 2; done
fi
export DEEPSEEK_BASE_URL="http://127.0.0.1:$PROXY_PORT/v1"
curl -sf -m 3 http://127.0.0.1:$PROXY_PORT/v1/models >/dev/null 2>&1 || echo "[$PLUGIN] ⚠️ de-stream 代理未就绪"

for try in $(seq 1 "$MAX_TRIES"); do
  WS="/home/node/ws-$PLUGIN-try$try"
  rm -rf "$WS"; mkdir -p "$WS"
  echo "[$PLUGIN] 第 $try/$MAX_TRIES 次尝试"
  PROMPT="测试一个 dsh 插件能否加载。源码在 $CLONE。步骤要少而快（控制在 ~8 步内）：
1) 读 $CLONE/package.json 和 README.md（各读一次即可，别反复）。
2) 尝试一次导入/安装（按 README 的方式；装依赖用一次 bash）。
3) 验证能否加载（一次 dsh 启动或 node -e require 即可）。
重要：步骤越少越好，不要过度调查。完成 3 步后立刻输出结论，严格一行：
PASS（能加载）或 FAIL: <一句话原因>（不能加载）。立即给结论，不要继续调用工具。"

  # dsh 非交互：answer one task, print result, exit（原生 Qwen，无桥）
  RAW="$(timeout 300 dsh --profile headless "$PROMPT" 2>&1)"
  LINE="$(printf '%s' "$RAW" | grep -iE '^(PASS|FAIL)' | tail -1)"
  [ -z "$LINE" ] && LINE="$(printf '%s' "$RAW" | tail -1)"

  if printf '%s' "$LINE" | grep -qi '^PASS'; then
    RESULT="✅ 可用（第 $try 次成功）"
    LAST_ERR=""
    break
  else
    LAST_ERR="$LINE"
    printf '%s\n' "$RAW" | tail -10 > "$OUT_DIR/../logs/$PLUGIN.try$try.log" 2>/dev/null || true
    mkdir -p "$OUT_DIR/../logs"
    printf '%s\n' "$RAW" | tail -10 > "$OUT_DIR/../logs/$PLUGIN.try$try.log"
    echo "[$PLUGIN] 第 $try 次失败：$LINE"
  fi
done

# 写聚合记录
python3 - "$OUT_DIR/$PLUGIN.json" "$PLUGIN" "$RESULT" "${LAST_ERR:-(无)}" << 'PY'
import sys, json, os, datetime
path, plugin, result, err = sys.argv[1:5]
d = {}
if os.path.isfile(path):
    try: d = json.load(open(path))
    except Exception: pass
d.update({"plugin": plugin, "result": result, "last_error": err,
          "date": datetime.date.today().isoformat(), "tries": 3})
json.dump(d, open(path, "w"), ensure_ascii=False, indent=2)
PY
echo "[$PLUGIN] $RESULT"
