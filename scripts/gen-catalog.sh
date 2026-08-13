#!/usr/bin/env bash
# 生成 README「分类目录」章节——顶层按功能领域分类（非仓库类型）
# 渲染规则：
#   - 顶层 = 功能领域（webui/agent/coding/comm/data/fun/infra/edu/other），每类 <details> 折叠、h3 大标题 + 描述
#   - 每条带类型标签（插件/技能/合集/渠道/基建/研究/社区），来自 catalog 的 category
#   - 每类显示前 10 条；第 11 条起嵌套折叠「展开全部」
#   - DOMAIN_MAP 全量重分类（275 条，人工审校）；未映射归 other
# 数据源：hub catalog.json（gh api 实时拉取）；渲染由 python3 完成
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2
GH="$HOME/.local/bin/gh"

CATALOG="$(mktemp)"
timeout 90 "$GH" api "repos/dsh-external/hub/contents/catalog.json" --jq '.content' 2>/dev/null | base64 -d 2>/dev/null > "$CATALOG"
[ -s "$CATALOG" ] || { echo "[gen-catalog] hub catalog 拉取失败，跳过"; rm -f "$CATALOG"; exit 0; }

python3 - "$CATALOG" <<'PYEOF'
import json, sys

catalog = json.load(open(sys.argv[1], encoding="utf-8"))
repos = catalog.get("repos", [])

# 领域体系：key -> (emoji 标题, 描述)。顺序即渲染顺序。
DOMAIN_META = [
    ("webui", "🔌 Web UI 增强", "界面与交互增强插件：侧边栏、输入框、皮肤主题、面板 dock、消息显示、状态栏与可视化，让 Web 界面更顺手更好看"),
    ("agent", "🤖 Agent 能力", "增强 agent 本身的能力：子代理管理、记忆与上下文、会话控制、规划执行、唤醒/睡眠、提示词与技能注入"),
    ("coding", "💻 编码开发", "面向编程场景的工具：代码操作、git 集成、终端、diff 与编辑器、文档生成、语言支持与构建辅助"),
    ("comm", "📡 消息通讯", "把 dsh 接入各类沟通渠道：微信/QQ/Telegram/飞书机器人、桌面通知、消息分享与跨端回复"),
    ("data", "🗂 文件数据", "文件与数据处理：读写与格式转换、爬取抓取、数据库、编码识别、文档解析与知识库"),
    ("fun", "🎮 娱乐生活", "摸鱼与趣味：小游戏、桌面宠物、表情包、音乐、股票行情与旅行"),
    ("infra", "🛠 基建部署", "运行环境与分发：桌面/移动客户端、远程主机、浏览器桥、沙箱隔离、插件管理、更新与监控"),
    ("edu", "📚 学习研究", "学习与探索：技能包、插件开发指南、文档导航、评测基准与社区 onboarding"),
    ("other", "❓ 其他", "描述缺失或暂未归类的仓库，补充信息后将细分"),
]

# 类型标签：catalog category -> 展示标签
TYPE_LABEL = {
    "plugin": "插件", "skill": "技能", "collection": "合集", "channel": "渠道",
    "infra": "基建", "research": "研究", "community": "社区",
}

# 全量领域映射（275 条，人工审校重分类；未列出归 other）
DOMAIN_MAP = {
'7d7d': 'webui', 'chat-width': 'webui', 'dsh-ads': 'webui', 'dsh-aigc-canvas': 'webui', 'dsh-annotation': 'webui',
    'dsh-anti-ads': 'webui', 'dsh-chat': 'webui', 'dsh-custom-css': 'webui', 'dsh-deepcel': 'webui', 'dsh-drag-and-drop': 'webui',
    'dsh-genui': 'webui', 'dsh-input-history': 'webui', 'dsh-live-stats': 'webui', 'dsh-message-edit': 'webui', 'dsh-paste-input': 'webui',
    'dsh-question-collapse': 'webui', 'dsh-skins': 'webui', 'dsh-split-panes': 'webui', 'dsh-tavern-plugin': 'webui', 'dsh-tps': 'webui',
    'dsh-ui-webview': 'webui', 'dsh-ultra-ui': 'webui', 'dsh-vision': 'webui', 'dsh-voice-chat': 'webui', 'dsh-web': 'webui',
    'dsh-web-panel': 'webui', 'dsh-web-review': 'webui', 'dsh-web-ui': 'webui', 'dsh-browser-panel': 'webui', 'dsh-island': 'webui',
    'DSH-UI4A': 'webui', 'ex-setting': 'webui', 'group-chat-diary': 'webui', 'review-panel': 'webui', 'show-bash-command': 'webui',
    'turtle-ui': 'webui', 'ui-status-label': 'webui', 'web-components': 'webui', 'zephyr': 'webui', 'DSH-better-sidebar': 'webui',
    'dsh-side-panel': 'webui', 'ya-workspace-sidebar': 'webui', 'dsh-selection-chat': 'webui', 'dsh-visualize': 'webui',
    'dsh-a2a': 'agent', 'dsh-agent-budget': 'agent', 'dsh-agent-rp': 'agent', 'dsh-alphasolve': 'agent', 'dsh-auto-approval': 'agent',
    'dsh-checkpoint': 'agent', 'dsh-client-ui-plan-execute': 'agent', 'dsh-cot-summary': 'agent', 'dsh-deeplink': 'agent',
    'dsh-design': 'agent', 'dsh-easy-ctx-manager': 'agent', 'dsh-engram-relay': 'agent', 'dsh-evolve': 'agent', 'dsh-explain': 'agent',
    'dsh-focus-chat': 'agent', 'dsh-inspect': 'agent', 'dsh-issue-like-skill': 'agent', 'dsh-kimi-bridge': 'agent', 'dsh-llm-fallbacks': 'agent',
    'dsh-mega': 'agent', 'dsh-memory': 'agent', 'dsh-mnemon': 'agent', 'dsh-nowledge-mem': 'agent', 'dsh-openmaic': 'agent',
    'dsh-plan-execute': 'agent', 'dsh-prompt-studio': 'agent', 'dsh-reuse-first': 'agent', 'dsh-rewind': 'agent', 'dsh-scout': 'agent',
    'dsh-self-control-guard': 'agent', 'dsh-session-cluster': 'agent', 'dsh-session-health': 'agent', 'dsh-session-hub': 'agent',
    'dsh-session-repair-skill': 'agent', 'dsh-skill-session-recovery': 'agent', 'dsh-skill-stats': 'agent', 'dsh-skills-manager': 'agent',
    'dsh-sleep': 'agent', 'dsh-slice-agent-loop': 'agent', 'dsh-subagent-tree': 'agent', 'dsh-super-injector': 'agent',
    'dsh-superpowers': 'agent', 'dsh-track': 'agent', 'dsh-turn-navigator': 'agent', 'dsh-turn-rewind': 'agent', 'dsh-ui-progress': 'agent',
    'dsh-web-workflow-visualizer': 'agent', 'mstar-workflow': 'agent', 'session-teleport': 'agent', 'yet-another-subagent': 'agent',
    'dsh_workflow': 'agent', 'distill': 'agent', 'dsh-agent-session-sources': 'agent', 'dsh-activity-plugin': 'agent', 'Recall': 'agent',
    'Qwen-MM-Plugins': 'agent', 'deep-standard-skill': 'agent', 'dsh-qq2006': 'agent',
    'cross-harness-cite': 'coding', 'dsh_ide': 'coding', 'dsh-auto-blame': 'coding', 'dsh-better-sidebar-plugin-office': 'coding',
    'dsh-build': 'coding', 'dsh-cc-tui': 'coding', 'dsh-code': 'coding', 'dsh-code-map': 'coding', 'dsh-codex-bridge': 'coding',
    'dsh-grok-tui': 'coding', 'dsh-interpreters': 'coding', 'dsh-latex': 'coding', 'dsh-memory-evolve': 'coding', 'dsh-my-rsi': 'coding',
    'dsh-pi-adapter': 'coding', 'dsh-spec-kit': 'coding', 'dsh-tool-browser': 'coding', 'dsh-tool-calculator': 'coding',
    'dsh-tool-search': 'coding', 'dsh-tool-stat': 'coding', 'dsh-tool-time': 'coding', 'dsh-trace': 'coding', 'dsh-tui': 'coding',
    'dsh-tui-front-door': 'coding', 'dsh-vscode': 'coding', 'dsh-working-activity': 'coding', 'official-plugins-port': 'coding',
    'dsh-gh-bridge': 'coding', 'dsh-git-identity': 'coding', 'dsh-github-integration': 'coding', 'dsh-bash-encoding': 'coding',
    'dsh-cc-connect': 'coding', 'dsh-office': 'coding', 'zotero-wave-rag': 'coding', 'dsh-pty-windows': 'coding', 'dsh-shell-windows': 'coding',
    'dsh-chat-thumb': 'comm', 'dsh-coding-receipt': 'comm', 'dsh-feishu-bot': 'comm', 'dsh-feishu-notify': 'comm', 'dsh-ica': 'comm',
    'dsh-share': 'comm', 'dsh-suggested-replies': 'comm', 'dsh-web-ui-notify': 'comm', 'dsh-webbridge': 'comm', 'dsh-wecom-bot': 'comm',
    'dsh-weixin-bot': 'comm', 'qqbot': 'comm', 'telegram': 'comm', 'tg-bot': 'comm', 'issues': 'comm', 'dsh-club': 'comm', 'dsh-teamwork': 'comm',
    'dsh-deep-research': 'comm',
    'context-doctor': 'data', 'dsh-advisor': 'data', 'dsh-artifact': 'data', 'dsh-context7': 'data', 'dsh-cyber-sec': 'data',
    'dsh-data-agent': 'data', 'dsh-diff-viewer': 'data', 'dsh-issue-filer': 'data', 'dsh-kb-sieve': 'data', 'dsh-loop': 'data',
    'dsh-mineru': 'data', 'dsh-multimedia-webui-input': 'data', 'dsh-navbar': 'data', 'dsh-notebooks': 'data', 'dsh-openpencil': 'data',
    'dsh-profile-bundle-example': 'data', 'dsh-task-status': 'data', 'dsh-tool-csv': 'data', 'dsh-tool-diff': 'data',
    'dsh-tool-encoding': 'data', 'dsh-tool-json': 'data', 'dsh-tool-markdown': 'data', 'dsh-tool-regex': 'data',
    'dsh-tool-schema': 'data', 'dsh-toolkit': 'data', 'dsh-vision-toolkit': 'data', 'dsh-web-archive': 'data',
    'session-persistence-rdb': 'data', 'Top': 'data', 'ds_web_craw': 'data', 'session-chatlog': 'data', 'dsh-stock-market': 'data',
    'tonghuashun-harness': 'data', 'dsh-find-plugins': 'data',
    'dsh-auto-chess': 'fun', 'dsh-d399': 'fun', 'dsh-deep-whale': 'fun', 'dsh-emoji': 'fun', 'dsh-gomoku': 'fun', 'dsh-lazyfish': 'fun',
    'dsh-meme': 'fun', 'dsh-minigames': 'fun', 'dsh-music-player': 'fun', 'dsh-pet': 'fun', 'dsh-pet-rs': 'fun', 'dsh-sfw': 'fun',
    'dsh-travel-plugin': 'fun', 'dsh-ui-whale': 'fun', 'whale-girl': 'fun', 'toybox': 'fun', 'oh-my-dsh': 'fun', 'dsh-stickers': 'fun',
    'browser4-dsh': 'infra', 'deepseek-harness-desktop': 'infra', 'deepseek-harness-distro': 'infra', 'dsh-acp': 'infra',
    'dsh-android': 'infra', 'dsh-browser': 'infra', 'dsh-browser-bridge': 'infra', 'dsh-companion': 'infra', 'dsh-computer-use': 'infra',
    'dsh-desktop': 'infra', 'dsh-desktop-electron': 'infra', 'dsh-desktop-mac': 'infra', 'dsh-desktop-tools': 'infra',
    'dsh-harness-ops': 'infra', 'dsh-hub': 'infra', 'dsh-kimi-browser': 'infra', 'dsh-mobile': 'infra', 'dsh-mobileweb-adapter': 'infra',
    'dsh-ohos-patch': 'infra', 'dsh-opencode-server': 'infra', 'dsh-plugin-check': 'infra', 'dsh-plugin-radar': 'infra',
    'dsh-public-repo-monitor': 'infra', 'dsh-remote': 'infra', 'dsh-session-search': 'infra', 'dsh-win-port': 'infra',
    'dshx-update-check': 'infra', 'ego-browser': 'infra', 'fabric': 'infra', 'marisa': 'infra', 'oh-dsh-desktop': 'infra',
    'oh-my-dsh-distribution': 'infra', 'oh-my-deepseek': 'infra', 'plugin-registry': 'infra', 'plugin-template': 'infra',
    'repo-visibility-guard': 'infra', 'sandbox-micro': 'infra', 'sandbox-mxc': 'infra', 'sandbox-nono': 'infra',
    'dsh-multica-runtime': 'infra', 'dsh-paseo': 'infra', 'dsh-security': 'infra', 'dsh-security-audit': 'infra', 'dsh-sonar': 'infra',
    'deepseek-manners': 'edu', 'dsh-101': 'edu', 'dsh-cordis-examples': 'edu', 'dsh-cordis-rocks': 'edu', 'dsh-deepresearch': 'edu',
    'dsh-edu': 'edu', 'dsh-humanize': 'edu', 'dsh-plugin-dev': 'edu', 'dsh-plugin-guide': 'edu', 'dsh-plugin-skills': 'edu',
    'dsh-scholar': 'edu', 'dshfind': 'edu', 'onboarding': 'edu', 'savemoneybenchmark': 'edu', 'zotero-harvest': 'edu', 'dsh-plus': 'edu',
}
def short_desc(repo):
    d = repo.get("description") or ""
    if d == "null" or not d.strip():
        return "—"
    d = d.split("。")[0].strip()
    if not d:
        d = d.split(".")[0].strip()
    return d[:48] if d else "—"

groups = {key: [] for key, _, _ in DOMAIN_META}
for r in repos:
    domain = DOMAIN_MAP.get(r.get("name", ""), "other")
    groups.setdefault(domain, []).append(r)

out = []
out.append("<!-- AUTO:catalog:START -->")
out.append("")
out.append("> 按功能领域分类（重分类修正，数据源 [dsh-external/hub](https://github.com/dsh-external/hub) catalog）。每类显示前 10 条，其余折叠；点击标题展开。")
out.append("")
for key, title, desc in DOMAIN_META:
    items = groups.get(key, [])
    n = len(items)
    out.append("<details>")
    out.append(f"<summary><h3>{title}（{n}）</h3></summary>")
    out.append("")
    out.append(f"*{desc}*")
    out.append("")
    out.append("| 插件 | 类型 | 说明 |")
    out.append("|---|---|---|")
    if n == 0:
        out.append("| （暂无） | — | — |")
    else:
        for r in items[:10]:
            t = TYPE_LABEL.get(r.get("category", ""), "插件")
            out.append(f"| [{r['name']}]({r.get('url', '')}) | {t} | {short_desc(r)} |")
        if n > 10:
            out.append("")
            out.append("<details>")
            out.append(f"<summary>展开全部（剩余 {n - 10} 条）</summary>")
            out.append("")
            out.append("| 插件 | 类型 | 说明 |")
            out.append("|---|---|---|")
            for r in items[10:]:
                t = TYPE_LABEL.get(r.get("category", ""), "插件")
                out.append(f"| [{r['name']}]({r.get('url', '')}) | {t} | {short_desc(r)} |")
            out.append("</details>")
    out.append("</details>")
    out.append("")
    # 描述第二遍：块外持续显示（默认可见，不随折叠消失）
    out.append(f"*{desc}*")
    out.append("")
out.append("<!-- AUTO:catalog:END -->")

block = "\n".join(out)
p = "README.md"
s = open(p, encoding="utf-8").read()
start = "<!-- AUTO:catalog:START -->"
end = "<!-- AUTO:catalog:END -->"
if start in s:
    i = s.index(start)
    j = s.index(end) + len(end)
    s = s[:i] + block + s[j:]
else:
    anchor = "## 当前生态快照"
    i = s.index(anchor)
    s = s[:i] + "## 分类目录\n\n" + block + "\n" + s[i:]
open(p, "w", encoding="utf-8").write(s)
print("CATALOG_BLOCK_UPDATED")
PYEOF
rm -f "$CATALOG"
exit 0
