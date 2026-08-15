#!/usr/bin/env python3
"""reconcile-catalog.py — 渲染器目录对账模块（被 render-readme-from-snapshot.py 调用）。

输入：快照 catalog_entries（Bot A 侧已分类全量条目）+ README AUTO:catalog 段。
行为：
  ① 每分类表追加缺失条目（按名称对账，已有行不动——保留人工策展与 star/判定刷新成果）
  ② h3 计数坍缩为单值（去掉「N + M」扩充痕迹）
幂等：同一快照重复对账逐字节一致。
"""
import re

DOMAIN_ORDER = ["🔌 Web UI 增强", "🤖 Agent 能力", "💻 编码开发", "📡 消息通讯",
                "🗂 文件数据", "🎮 娱乐生活", "🛠 基建部署", "📚 学习研究", "❓ 其他"]
VERDICT_ORDER = {"✅": 0, "⏳": 1, "⚠️": 2, "❌": 3}


def reconcile_catalog(readme_text: str, entries: list) -> str:
    """entries: [{name, url, star, verdict, domain, desc}]"""
    if not entries:
        return readme_text
    by_domain = {}
    existing_names = set()
    for e in entries:
        by_domain.setdefault(e["domain"], []).append(e)

    lines = readme_text.splitlines(keepends=True)
    i_start = next(i for i, l in enumerate(lines) if "AUTO:catalog:START" in l)
    i_end = next(i for i, l in enumerate(lines) if "AUTO:catalog:END" in l)

    for title in DOMAIN_ORDER:
        h3pat = re.compile(r"<summary><h3>" + re.escape(title) + r"（[^<）]*）</h3></summary>")
        for i in range(i_start, i_end):
            m = h3pat.search(lines[i])
            if not m:
                continue
            # 块界：h3 行到 </details>
            j = i
            while j < len(lines) and not lines[j].startswith("</details>"):
                j += 1
            block_names = set()
            k = i
            while k < j:
                rm = re.match(r"\|\s*\[([^\]]+)\]\(([^)]*)\)", lines[k])
                if rm:
                    block_names.add(rm.group(1).strip())
                k += 1
            existing_names |= block_names
            # 表尾行
            last_pipe = j - 1
            while last_pipe > i and not lines[last_pipe].startswith("|"):
                last_pipe -= 1
            new_items = [e for e in by_domain.get(title, []) if e["name"] not in block_names]
            new_items.sort(key=lambda e: (VERDICT_ORDER.get(e["verdict"][0] if e["verdict"] else "⏳", 9), e["name"].lower()))
            rows = [f"| [{e['name']}]({e['url']}) | 社区 | {e['star']} | {e['verdict']} | {e['desc']} |\n"
                    for e in new_items]
            if rows:
                lines[last_pipe + 1:last_pipe + 1] = rows
                i_end += len(rows)
                j += len(rows)
            # 计数坍缩单值（= 现在实际行数）
            cnt = sum(1 for l in lines[i:j] if l.startswith("| ["))
            lines[i] = h3pat.sub(f"<summary><h3>{title}（{cnt}）</h3></summary>", lines[i])
            break

    # ②b 已有行刷新：star 数值化更新 + 判定仅更新「运行级口径」单元格（兼容/关注/需适配等策展标签不动）
    ent = {e["name"]: e for e in entries}
    for i in range(i_start, i_end):
        # 兼容 4 列（插件|类型|兼容性|说明）与 5 列（+⭐）两种行格式
        raw = lines[i].rstrip("\n")
        m5 = re.match(r"\|\s*\[([^\]]+)\]\(([^)]*)\)\s*\|\s*([^|]+)\|\s*([^|]*)\|\s*([^|]*)\|\s*(.*?)\|\s*$", raw)
        m4 = re.match(r"\|\s*\[([^\]]+)\]\(([^)]*)\)\s*\|\s*([^|]+)\|\s*([^|]*)\|\s*(.*?)\|\s*$", raw)
        m = m5 or m4
        if not m:
            continue
        name = m.group(1).strip()
        if name not in ent:
            continue
        e = ent[name]
        if m5:
            typ, star, verdict, desc = m.group(3).strip(), m.group(4).strip(), m.group(5).strip(), m.group(6)
        else:
            typ, verdict, desc = m.group(3).strip(), m.group(4).strip(), m.group(5)
            star = None
        new_star = str(e.get("star", "—")) if star is not None else None
        new_verdict, new_url = verdict, m.group(2)
        was_pending = verdict == "待调研"
        if (verdict and verdict[0] in "✅❌⚠️⏳") or was_pending:
            new_verdict = e["verdict"]
            if was_pending and e.get("url"):
                new_url = e["url"]  # 待调研策展行获得实测证据时，指向被测公有仓
        new_desc = desc
        e_desc = (e.get("desc") or "").strip()
        if e_desc and e_desc != "—" and typ == "社区":
            new_desc = e_desc  # 社区行描述随快照同步（GitHub 仓库描述变更）
        changed = (new_verdict != verdict) or (new_star is not None and star is not None and new_star != star) or new_url != m.group(2) or new_desc != desc
        if changed:
            lines[i] = (f"| [{name}]({new_url}) | {typ} |" +
                        (f" {new_star} |" if star is not None else "") +
                        f" {new_verdict} | {new_desc} |\n")

    return "".join(lines)
