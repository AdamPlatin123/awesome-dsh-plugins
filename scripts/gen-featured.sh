#!/usr/bin/env bash
# 生成 README「热门插件」节（Star Top 20，自动更新）
# 数据源：GitHub API（批量拉 star 数）+ desc-cache.json（描述）
# 由 update-readme.sh 或 cron-check.sh 调用；每次 cron 刷新 star 排名
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

python3 - <<'PYEOF'
import json, os, re, subprocess, urllib.request

# 读 desc-cache 获取全量仓库列表（含 EXTRA）
cache_file = "desc-cache.json"
if not os.path.isfile(cache_file):
    print("[gen-featured] desc-cache.json 不存在，跳过")
    raise SystemExit(0)

# 从 catalog + EXTRA_REPOS 构建仓库 URL 映射
catalog = {}
try:
    import tempfile
    token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    req = urllib.request.Request(
        "https://api.github.com/repos/dsh-external/hub/contents/catalog.json",
        headers={"Authorization": f"token {token}", "User-Agent": "featured"},
    )
    import base64
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
        cat = json.loads(base64.b64decode(data["content"]))
        for r in cat.get("repos", []):
            catalog[r["name"]] = r.get("url", f"https://github.com/dsh-external/{r['name']}")
except Exception as e:
    print(f"[gen-featured] catalog 拉取失败: {e}，用 desc-cache 键名")
    catalog = {}

# EXTRA_REPOS（与 gen-catalog.sh 同步维护）
EXTRA = {
    "dsh-review-skills": "https://github.com/ben7am1n/dsh-review-skills",
    "dsh-security-scan": "https://github.com/ben7am1n/dsh-security-scan",
    "dsh-telegram": "https://github.com/ben7am1n/dsh-telegram",
    "dsh-oauth-mcp-client": "https://github.com/springbrand-lab/dsh-oauth-mcp-client",
    "dsh-balance": "https://github.com/TwotwoPiggy/dsh-balance",
    "falsify-dsh": "https://github.com/shi275773124/falsify-dsh",
    "billion-context-dsh": "https://github.com/Tyan66666/billion-context-dsh",
    "deepseek-harness-desktop": "https://github.com/chyra-moon/deepseek-harness-desktop",
    "dsh-web-search-firecrawl": "https://github.com/yangzhe1003/dsh-web-search-firecrawl",
    "dsh-claude-move": "https://github.com/PerryLink/dsh-claude-move",
    "dsh-chat-import": "https://github.com/Nwflower/dsh-chat-import",
    "dsh-test-runner": "https://github.com/suimi8/dsh-test-runner",
    "dsh-event-auditor": "https://github.com/qing3a/dsh-event-auditor",
    "dsh-turn-index": "https://github.com/Simon314620/dsh-turn-index",
    "dsh-remote-sandbox": "https://github.com/weijiafu14/dsh-remote-sandbox",
    "dsh-tray": "https://github.com/qing3a/dsh-tray",
    "dsh-TUI": "https://github.com/ccch1mneyyy/dsh-TUI",
}
catalog.update(EXTRA)

# 如果 catalog 拉取失败，用 desc-cache 键名 + 默认 org URL
desc_cache = json.load(open(cache_file, encoding="utf-8"))
if not catalog:
    for name in desc_cache:
        catalog[name] = f"https://github.com/dsh-external/{name}"

# 排除非插件仓库（基建/模板/issue tracker）
EXCLUDE = {"issues", "plugin-template", "plugin-registry", "onboarding",
           "review-panel", "group-chat-diary", "Top", "hub", "marisa",
           "repo-visibility-guard", "__perm_probe__", "plugin-template"}

# 批量拉 star（顺序调用，带 token）
token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
results = []
for name, url in catalog.items():
    if name in EXCLUDE:
        continue
    parts = url.replace("https://github.com/", "").strip("/")
    star = 0
    try:
        req = urllib.request.Request(
            f"https://api.github.com/repos/{parts}",
            headers={"Authorization": f"token {token}", "User-Agent": "featured"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            star = data.get("stargazers_count", 0)
    except Exception:
        pass
    desc = desc_cache.get(name, "") or ""
    if not desc:
        # 从 catalog description 兜底
        for r in cat.get("repos", []):
            if r["name"] == name:
                desc = r.get("description") or ""
                break
    # 截断描述
    desc = desc.split("。")[0].strip()[:60] or "—"
    results.append((star, name, url, desc))

# 排序取 Top 20
results.sort(key=lambda x: -x[0])
top20 = results[:20]

# 渲染 AUTO:featured 块
out = []
out.append("<!-- AUTO:featured:START -->")
out.append("")
out.append(f"> 按 GitHub star 数排序，每 8 小时自动刷新。数据截至 {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}。")
out.append("")
out.append("| # | 插件 | ⭐ | 说明 |")
out.append("|---|---|---|---|")
for i, (star, name, url, desc) in enumerate(top20, 1):
    short = name if len(name) <= 28 else name[:26] + "…"
    out.append(f"| {i} | [{short}]({url}) | {star} | {desc} |")
out.append("")
out.append("<!-- AUTO:featured:END -->")

block = "\n".join(out)

# 写入 README（替换 AUTO:featured 块或插入到分类目录前）
p = "README.md"
s = open(p, encoding="utf-8").read()
start = "<!-- AUTO:featured:START -->"
end = "<!-- AUTO:featured:END -->"
if start in s:
    i = s.index(start)
    j = s.index(end) + len(end)
    s = s[:i] + block + s[j:]
else:
    anchor = "## 分类目录"
    i = s.index(anchor)
    header = "## 🔥 热门插件（Star Top 20）\n\n"
    s = s[:i] + header + block + "\n\n" + s[i:]
open(p, "w", encoding="utf-8").write(s)
print("FEATURED_BLOCK_UPDATED")
PYEOF
exit 0
