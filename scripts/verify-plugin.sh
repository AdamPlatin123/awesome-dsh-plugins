#!/usr/bin/env bash
# 验证仓库是否为「能安装的 dsh 插件」（不是所有打标仓库都是插件）
# 判定（全部满足）：
#   1. package.json 存在
#   2. name 字段非空
#   3. 有可解析入口：main / exports 之一，或有 dsh.bundle / cordis 集成字段
#   4. 排除名单：awesome 列表仓库、合影、placeholder、官方主仓（非插件仓库）
# 输出：每行 "<full_name>|PASS|<入口类型>" 或 "<full_name>|FAIL|<原因>"
# 用法：verify-plugin.sh <repos文件> [输出文件]
set -uo pipefail
GH="$HOME/.local/bin/gh"
JQ="$HOME/.local/bin/jq"
IN="${1:?用法: verify-plugin.sh <repos文件>}"
OUT="${2:-/dev/stdout}"

verify_one() {
  local full="$1" bare="${1##*/}"
  # 排除名单（名字模式）
  case "$bare" in
    *awesome*) echo "$full|FAIL|awesome 列表仓库（非插件）"; return ;;
    *group-photo*) echo "$full|FAIL|合影仓库（非插件）"; return ;;
    *placeholder*) echo "$full|FAIL|占位仓库（非插件）"; return ;;
    deepseek-harness) echo "$full|FAIL|官方主仓（非插件）"; return ;;
  esac
  # package.json 存在性 + name/main/exports/dsh
  local pkg
  pkg="$(timeout 30 "$GH" api "repos/$full/contents/package.json" --jq '.content' 2>/dev/null | base64 -d 2>/dev/null || echo "")"
  if [ -z "$pkg" ]; then
    echo "$full|FAIL|无 package.json"
    return
  fi
  local name main exports dsh
  name="$(printf '%s' "$pkg" | "$JQ" -r .name 2>/dev/null || echo "")"
  main="$(printf '%s' "$pkg" | "$JQ" -r '.main // empty' 2>/dev/null || echo "")"
  exports="$(printf '%s' "$pkg" | "$JQ" -r '.exports // empty' 2>/dev/null || echo "")"
  dsh="$(printf '%s' "$pkg" | "$JQ" -r '.dsh // empty' 2>/dev/null || echo "")"
  [ -n "$name" ] || { echo "$full|FAIL|package.json 无 name"; return; }
  if [ -n "$main" ] || [ -n "$exports" ]; then
    echo "$full|PASS|main/exports"
  elif [ -n "$dsh" ]; then
    echo "$full|PASS|dsh 集成字段"
  else
    echo "$full|FAIL|无 main/exports/dsh 入口"
  fi
}

export -f verify_one
export GH JQ
while IFS= read -r full; do
  [ -n "$full" ] || continue
  verify_one "$full"
done < "$IN" | tee "$OUT"
exit 0
