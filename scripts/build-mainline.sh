#!/usr/bin/env bash
# 自动构建 deepseek-harness 最新快照，验证最新版本可编译性。
# 输出：reports/<日期>/mainline-build.md（commit/install rc/build rc/耗时/错误摘要）
# 由 cron-check.sh --full 调用（构建在索引后异步执行，不阻塞报告生成）。
# 用法：build-mainline.sh [--skip-install]  ；SKIP_BUILD=1 环境变量跳过整个构建
# 依赖：bash/git/node（nvm v24）/corepack
set -uo pipefail

[ "${SKIP_BUILD:-0}" = "1" ] && { echo "[构建] SKIP_BUILD=1，跳过"; exit 0; }

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR" || exit 2
DATE="$(date +%Y-%m-%d)"
BUILD_DIR="$REPO_DIR/.mainline-build"
LOG_DIR="$REPO_DIR/logs"
mkdir -p "$BUILD_DIR" "$LOG_DIR"

# 0. 依赖预检
command -v git >/dev/null 2>&1 || { echo "[构建] 缺 git"; exit 2; }
NODE_BIN="$HOME/.nvm/versions/node/v24.14.1/bin"
[ -x "$NODE_BIN/node" ] || NODE_BIN="$(dirname "$(command -v node 2>/dev/null || echo /nonexistent)")"
export PATH="$NODE_BIN:$PATH"

# 1. 拉取最新快照引用
SNAP="$(timeout 60 git ls-remote https://github.com/dsh2026/test-AdamPlatin123 "refs/heads/snapshots/*" 2>/dev/null | sort -k2 | tail -1)"
COMMIT="$(printf '%s\n' "$SNAP" | awk '{print $1}')"
LABEL="$(printf '%s\n' "$SNAP" | awk '{print $2}' | sed 's#refs/heads/##')"
[ -z "$COMMIT" ] && { echo "[构建] 拉取快照引用失败（离线）"; exit 3; }

echo "[构建] 目标：$LABEL（$COMMIT）"

# 2. 拉取源码（复用构建目录）
if [ ! -d "$BUILD_DIR/.git" ]; then
  timeout 300 git clone --depth 1 --branch "$LABEL" https://github.com/dsh2026/test-AdamPlatin123 "$BUILD_DIR" >/dev/null 2>&1 \
    || { echo "[构建] clone 失败"; exit 2; }
else
  timeout 300 git -C "$BUILD_DIR" fetch --depth 1 origin "$LABEL" >/dev/null 2>&1 \
    && git -C "$BUILD_DIR" checkout -q FETCH_HEAD 2>/dev/null \
    || { echo "[构建] fetch 失败"; exit 2; }
fi
cd "$BUILD_DIR" || exit 2
CUR="$(git rev-parse --short HEAD 2>/dev/null)"

# 3. 启用 pnpm 并构建
corepack enable >/dev/null 2>&1 || true
corepack prepare pnpm@latest --activate >/dev/null 2>&1 || true
PNPM="$(command -v pnpm || echo "$NODE_BIN/pnpm")"
[ -x "$PNPM" ] || { echo "[构建] pnpm 不可用"; exit 2; }

START="$(date +%s)"
echo "[构建] pnpm install（开始 $(date +%H:%M:%S)）..."
"$PNPM" install --frozen-lockfile > "$LOG_DIR/build-install.log" 2>&1
INSTALL_RC=$?
if [ "$INSTALL_RC" -ne 0 ]; then
  echo "[构建] install 失败 rc=$INSTALL_RC（详见 logs/build-install.log）"
  ERR_SUM="$(grep -E "error|ERR|failed" "$LOG_DIR/build-install.log" | head -5)"
else
  echo "[构建] pnpm run build（开始 $(date +%H:%M:%S)）..."
  "$PNPM" run build > "$LOG_DIR/build-build.log" 2>&1
fi
BUILD_RC=$?
END="$(date +%s)"
DURATION=$((END-START))
echo "[构建] 完成 rc=install:$INSTALL_RC build:${BUILD_RC:-99} 耗时 ${DURATION}s"

# 4. 写报告
REPORT="$REPO_DIR/reports/$DATE/mainline-build.md"
mkdir -p "$REPO_DIR/reports/$DATE"
{
  echo "# mainline 构建报告（$DATE）"
  echo ""
  echo "- 快照：\`$LABEL\`（commit \`$CUR\`）"
  echo "- 构建时间：$(date +%Y-%m-%d_%H%M%S)（${DURATION}s）"
  echo "- install：$( [ "$INSTALL_RC" -eq 0 ] && echo '✅ 成功' || echo "❌ 失败 rc=$INSTALL_RC" )"
  echo "- build：$( [ "${BUILD_RC:-99}" -eq 0 ] && echo '✅ 成功' || echo "❌ 失败 rc=${BUILD_RC:-99}" )"
  echo ""
  echo "## 结论"
  if [ "$INSTALL_RC" -eq 0 ] && [ "${BUILD_RC:-99}" -eq 0 ]; then
    echo "**最新 mainline 可正常构建**——插件生态的构建基线有效。"
  else
    echo "**⚠️ 最新 mainline 构建失败**——需关注（错误摘要如下）。"
  fi
  echo ""
  echo "## 错误摘要"
  if [ "$INSTALL_RC" -ne 0 ]; then
    echo '```'
    grep -E "error|ERR|failed" "$LOG_DIR/build-install.log" | head -8
    echo '```'
  elif [ "${BUILD_RC:-99}" -ne 0 ]; then
    echo '```'
    grep -E "error|ERR|failed" "$LOG_DIR/build-build.log" | head -8
    echo '```'
  else
    echo "无错误。"
  fi
} > "$REPORT"
echo "[构建] 报告已写入 $REPORT"
exit 0
