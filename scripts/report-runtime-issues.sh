#!/usr/bin/env bash
# 谨慎提 issue：仅提证据充分类（A 包名漂移/scope 冲突 + B 缺依赖声明 + 元数据缺失）
# 每个 issue 附复现命令 + 完整错误 + mainline 版本
# 用法：report-runtime-issues.sh [--apply]
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
GH="$HOME/.local/bin/gh"
ML_HEAD="$(cd .mainline-build && git rev-parse --short HEAD 2>/dev/null)"
APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1

gen_body() {
  local name="$1" kind="$2"
  case "$kind" in
    schemastery)
      printf '## 现象\n\n在 mainline 快照 %s（final 版）上加载本插件报错：\n\n```\nCannot find package '\''schemastery'\'' imported from .../lib/index.js\n```\n\n## 根因\n\nmainline 已将 cordis 生态 vendor 化并改 scope：`schemastery` → `@deepseek-ai/schemastery`（vendor/schemastery）。本插件 import 裸名 `schemastery`，运行时解析失败。\n\n## 复现\n\n```bash\ndsh --profile headless --patch <(printf -- '\''- insert:\\n    - id: %s\\n      name: @dsh-external/%s\\n'\'') "hi"\n```\n\n## 建议修复\n\nimport 改为 `@deepseek-ai/schemastery`，或 package.json 加 alias。\n\n报告方：awesome-dsh-plugins 运行级兼容性测试（Qwen3.6-35B 驱动，零 LLM 断言）\n' "$ML_HEAD" "$name" "$name"
      ;;
    dsh-root-import)
      printf '## 现象\n\nmainline %s 加载本插件：\n\n```\nCannot find package '\''@deepseek-ai/dsh-root'\'' imported from .../lib/index.js\n```\n\n## 根因\n\n`@deepseek-ai/dsh-root` 是仓库根包，不参与发布。import 该路径的插件在真实安装环境必失败。\n\n## 建议修复\n\n移除对 dsh-root 的 import（如需引用仓库级常量，复制或走已发布包）。\n\n报告方：awesome-dsh-plugins 运行级兼容性测试\n' "$ML_HEAD"
      ;;
    dep)
      printf '## 现象\n\nmainline %s 加载本插件：\n\n```\nCannot find package '\''%s'\'' imported from .../lib/index.js\n```\n\n## 根因\n\n`%s` 未声明在 package.json 的 dependencies/peerDependencies。\n\n## 建议修复\n\n把 `%s` 加入 dependencies（或 peerDependencies 若由宿主提供），重新发布。\n\n报告方：awesome-dsh-plugins 运行级兼容性测试\n' "$ML_HEAD" "$3" "$3" "$3"
      ;;
    no-main)
      printf '## 现象\n\nmainline %s 加载本插件：\n\n```\nCannot find package '\''.../node_modules/@dsh-external/%s/index.js'\''\n```\n\n## 根因\n\npackage.json 缺少 `main`/exports 字段（或指向不存在的入口文件）。\n\n## 建议修复\n\n补 `"main": "lib/index.js"`（或 exports 映射），确保发布产物含该入口。\n\n报告方：awesome-dsh-plugins 运行级兼容性测试\n' "$ML_HEAD" "$name"
      ;;
    scope-conflict)
      printf '## 现象\n\nmainline %s 加载本插件：\n\n```\nCannot find package '\''@deepseek-ai/dsh-tui'\''（=本插件 package.json 的 name）\n```\n\n## 根因\n\n本插件 package.json `name` 使用 `@deepseek-ai/*` scope，与 mainline 官方命名空间冲突（该 scope 为 restricted，外部无法发布，运行时也解析到 mainline 工作树而找不到本插件）。\n\n## 建议修复\n\nname 改为 `@dsh-external/turtle-ui`（与 repo 名一致），更新 cordis.yml/patch 引用。\n\n报告方：awesome-dsh-plugins 运行级兼容性测试\n' "$ML_HEAD"
      ;;
  esac
}

COUNT=0
while IFS='|' read -r name kind dep; do
  title=""
  case "$kind" in
    schemastery) title="[兼容性] import 'schemastery' 裸名解析失败——mainline 已 vendor 化为 @deepseek-ai/schemastery" ;;
    dsh-root-import) title="[兼容性] import @deepseek-ai/dsh-root 失败——根包不发布" ;;
    dep) title="[依赖声明] 缺 '$dep'——加载即失败" ;;
    no-main) title="[元数据] package.json 缺 main/exports——包入口不可解析" ;;
    scope-conflict) title="[包名] name 误用 @deepseek-ai scope——与 mainline 命名空间冲突" ;;
    *) continue ;;
  esac
  body="$(gen_body "$name" "$kind" "$dep")"
  if [ "$APPLY" = "1" ]; then
    if "$GH" issue create --repo "dsh-external/$name" --title "$title" --body "$body" >/dev/null 2>&1; then
      echo "[已提] $name"
      COUNT=$((COUNT+1))
    else
      echo "[失败] $name（repo 不存在/无权限/已有关联 issue）"
    fi
  else
    echo "[预览] $name：$title"
    COUNT=$((COUNT+1))
  fi
done << 'LIST'
distill|schemastery|
dsh-alphasolve|schemastery|
dsh-session-search|schemastery|
dsh-vision|schemastery|
session-chatlog|schemastery|
telegram|schemastery|
dsh-code|dsh-root-import|
dsh-cc-tui|dep|react
dsh-companion|dep|cetus
turtle-ui|scope-conflict|
dsh-tool-browser|no-main|
dsh-tool-encoding|no-main|
dsh-github-integration|no-main|
dsh-ohos-patch|no-main|
dsh-subagent-tree|no-main|
dsh-working-activity|no-main|
tg-bot|no-main|
dsh-agent-session-sources|no-main|
LIST

echo "共 $COUNT 个（${APPLY:+已提}${APPLY:-预览}）"
exit 0
