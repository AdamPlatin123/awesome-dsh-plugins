#!/usr/bin/env bash
# shard-runner.sh — 一个 pod 跑一个分片：把 /clones 里的插件按取模分片，逐个 agent 导入测试。
# 由 k8s indexed Job 注入 JOB_COMPLETION_INDEX（0..TOTAL-1）。
set -uo pipefail
TOTAL="${TOTAL:-5}"
IDX="${JOB_COMPLETION_INDEX:-0}"
echo "[shard $IDX/$TOTAL] 启动 @ $(date -Is)"

# 合格插件 = clone 里有 package.json（且非占位）
mapfile -t ALL < <(for d in /clones/*/; do
    [ -f "${d}package.json" ] || continue
    basename "$d"
  done | sort)

plugins=()
for i in "${!ALL[@]}"; do
  (( i % TOTAL == IDX )) && plugins+=("${ALL[$i]}")
done
echo "[shard $IDX/$TOTAL] 分到 ${#plugins[@]} 个：${plugins[*]}"

ok=0; bad=0; skip=0
for p in "${plugins[@]}"; do
  out="$(test-plugin-agent.sh "$p" 2>&1 | tail -1)"
  echo "$out"
  case "$out" in
    *✅*) ok=$((ok+1));;
    *❌*) bad=$((bad+1));;
    *⏭️*) skip=$((skip+1));;
  esac
done
echo "[shard $IDX/$TOTAL] 完成：可用 $ok / 不兼容 $bad / 跳过 $skip / 共 ${#plugins[@]}"
