#!/usr/bin/env bash
# npm 发布探测：周期性查 @deepseek-ai/dsh 是否已发布到 npm
# 一旦可用（rc.3 或任何 version）→ 记录并触发告警/消费方式切换
# 用法：由 cron 每 30 分钟触发，与 watch-mainline 并行
set -uo pipefail
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
STATE="$REPO_DIR/.npm-publish.state"
PKG="@deepseek-ai/dsh"
# npm view 返回 version 字符串即已发布
VER="$(timeout 20 npm view "$PKG" version 2>/dev/null | tr -d ' \n')"
TS="$(date -Is)"
if [ -n "$VER" ]; then
  PREV="$(cat "$STATE" 2>/dev/null || echo '')"
  if [ "$VER" != "$PREV" ]; then
    echo "[$TS] 🎉 $PKG 已发布到 npm：$VER（之前：${PREV:-无}）→ dsh 进入 npm 消费阶段"
    echo "[$TS] 影响：运行级测试可改用 npm install 秒装（免 mainline 构建）；VM 并行方案变可行"
    echo "$VER" > "$STATE"
    # 记录到日报目录
    mkdir -p "$REPO_DIR/reports/$(date +%Y-%m-%d)"
    echo "- $PKG npm 发布检测：**$VER**（$TS）→ 消费方式可切换 npm" \
      >> "$REPO_DIR/reports/$(date +%Y-%m-%d)/npm-publish.md"
  else
    echo "[$TS] $PKG npm 已知版本 $VER（无变化）"
  fi
else
  echo "[$TS] $PKG 未发布到 npm（仍 404）→ 继续源码/快照仓消费"
  [ -f "$STATE" ] || echo "pending" > "$STATE"
fi
exit 0
