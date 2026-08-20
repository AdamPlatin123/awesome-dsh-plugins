#!/usr/bin/env python3
"""render-readme-from-snapshot.py — Bot B：从已合并快照渲染 README（仓库内运行，零外部依赖）。

契约：只读 data/snapshots/*.json（取 run_id 最新），绝不访问网络/指标流。
渲染面（中英两版 README 同步渲染；语言专属正则不命中即安全跳过）：
  三徽章 + 证据层运行级行 + AUTO:pipeline 活数字图（中文版）+ 「数据截至」锚（中文版）
  + 头部数字面 + 目录对账 + 生态快照块头行/报告链接。
时间戳统一输出北京时间（UTC+8）。
幂等：同快照重复渲染输出逐字节一致。
"""
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAP_DIR = ROOT / "data" / "snapshots"

DIAGRAM = """```mermaid
flowchart TB
    subgraph Discovery["发现（每 {discover_hours} 小时 · probe {probe} 巡检触发）"]
        A1["GitHub Search<br/>topic ×{topic_n} + keyword ×{kw_n}<br/>候选 {cand} · 龄 {age}m"]
        A2["本地库补全 · 去重 repo id"]
        A3["私有 org 仓排除<br/>{spacing}s 错峰 · 403 退避 · dshow 黑名单"]
    end
    subgraph Validation["验证（driver 20s 流式循环）"]
        B1{{"package.json<br/>name + main/exports/dsh?"}}
    end
    B1 -->|"插件 {plugins}"| C1["k8s 运行级测试<br/>一插件一 pod · 并发 {cap}<br/>dsh agent + Qwen（de-stream）"]
    B1 -->|"非插件（累计删 {nonplugin}）"| B3["即删省空间"]
    C1 --> D1{{"判定 · 总 {total}"}}
    D1 -->|"{pass} / {fail}"| E1["聚合 + README 分类统计"]
    D1 -->|"{inc} 环境类重试"| C1
    E1 --> E2["cadence 交付<br/>本周期增量 {delta}/{batch}<br/>双仓 bot PR（幂等 supersede）"]
    M["radar-probe {probe} 自愈<br/>{streams} 指标流 × {stream_sec}s · 完成累计 {done}"]
    M -.-> A1
    M -.-> C1
```"""


DIAGRAM_EN = """```mermaid
flowchart TB
    subgraph Discovery["Discovery (every {discover_hours}h · probe {probe})"]
        A1["GitHub Search<br/>topic ×{topic_n} + keyword ×{kw_n}<br/>candidates {cand} · age {age}m"]
        A2["Local DB merge · dedupe by repo id"]
        A3["Private org repos excluded<br/>{spacing}s stagger · 403 backoff · dshow blocklist"]
    end
    subgraph Validation["Validation (driver 20s streaming loop)"]
        B1{{"package.json<br/>name + main/exports/dsh?"}}
    end
    B1 -->|"plugins {plugins}"| C1["k8s runtime test<br/>1 pod per plugin · concurrency {cap}<br/>dsh agent + Qwen (de-stream)"]
    B1 -->|"non-plugins (dropped {nonplugin})"| B3["dropped to save space"]
    C1 --> D1{{"verdict · total {total}"}}
    D1 -->|"{pass} / {fail}"| E1["aggregate + README stats"]
    D1 -->|"{inc} env retries"| C1
    E1 --> E2["cadence deliver<br/>delta this cycle {delta}/{batch}<br/>dual-repo bot PRs (idempotent)"]
    M["radar-probe {probe} self-heal<br/>{streams} metric streams × {stream_sec}s · done {done}"]
    M -.-> A1
    M -.-> C1
```"""

def latest_snapshot():
    if not SNAP_DIR.exists():
        return None
    snaps = sorted(SNAP_DIR.glob("*.json"))
    for p in reversed(snaps):
        try:
            return json.loads(p.read_text())
        except json.JSONDecodeError:
            continue
    return None


def bj(iso_str, fmt="%Y-%m-%d %H:%M:%S"):
    """ISO 时间串 → 北京时间显示（UTC+8）；带时区偏移按原偏移换算，避免二次加 8；解析失败原样返回。"""
    try:
        dt = datetime.fromisoformat(str(iso_str).replace("Z", "+00:00"))
    except ValueError:
        return str(iso_str)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone(timedelta(hours=8))).strftime(fmt) + " UTC+8"


def fmt(x):
    return "—" if x is None else str(x)


def main():
    snap = latest_snapshot()
    if not snap or not str(snap.get("schema", "")).startswith("radar-snapshot/"):
        print("[render] 无有效快照（radar-snapshot/1）— 保持 README 现状（安全停旧）")

    v, d, c, t, dl = (snap[k] for k in ("verdict", "discovery", "clone", "test", "deliver"))
    topo = snap.get("topology", {})

    # ⓪ 全量清单随每轮快照重生成（PLUGINS-ALL.md），并取九类分布供目录摘要卡使用
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from gen_plugins_all import main as gen_all
        domain_stats = gen_all() or {}
    except Exception as _e:
        print(f"[render] WARN 清单生成跳过: {_e}")
        domain_stats = {}
    for path in (ROOT / "README.md", ROOT / "README.en-US.md"):
        is_zh = path.name == "README.md"
        t_readme = path.read_text()

        # ① 三徽章（两版通用）
        t_readme = re.sub(r"badge/confirmed-\d+", f"badge/confirmed-{fmt(c.get('plugins'))}", t_readme)
        t_readme = re.sub(r"badge/tested-\d+", f"badge/tested-{fmt(v.get('total'))}", t_readme)

        # ①b 四档磁贴（累积口径：catalog_entries 全量统计；含中英两组徽章 URL）
        vcnt = Counter(e.get("verdict", "") for e in (snap.get("catalog_entries") or []))
        n_ok = vcnt.get("✅ 运行级可用", 0) or vcnt.get("运行级可用", 0)
        n_bad = vcnt.get("❌ 运行级不兼容", 0) or vcnt.get("运行级不兼容", 0)
        n_inc = vcnt.get("⚠️ 待定", 0) or vcnt.get("待定", 0)
        n_un = vcnt.get("⏳ 未测", 0)
        for pat, val in ((r"(badge/(?:✅_)?运行级可用-)\d+", n_ok), (r"(badge/(?:✅_)?runtime_OK-)\d+", n_ok),
                         (r"(badge/(?:❌_)?运行级不兼容-)\d+", n_bad), (r"(badge/(?:❌_)?incompatible-)\d+", n_bad),
                         (r"(badge/(?:⚠️_)?待定-)\d+", n_inc), (r"(badge/(?:⚠️_)?pending-)\d+", n_inc),
                         (r"(badge/·_未测-)\d+", n_un), (r"(badge/untested-)\d+", n_un)):
            t_readme = re.sub(pat, rf"\g<1>{val}", t_readme)
        t_readme = re.sub(r"(（当前 `)[0-9A-Za-z]+(`)", rf"\g<1>{snap['run_id']}\g<2>", t_readme, count=1)
        t_readme = re.sub(r"(currently `)[0-9A-Za-z]+(`)", rf"\g<1>{snap['run_id']}\g<2>", t_readme, count=1)

        # ② 证据层运行级行（整行替换；两版该表均为中文）
        t_readme = re.sub(
            r"^\| 运行级实测 .*$",
            f"| 运行级实测 | {v.get('pass')} 可用 · {v.get('fail')} 不兼容 · {v.get('inc')} 待定"
            f"（共 {v.get('total')} 个，k8s agent 口径）|",
            t_readme, count=1, flags=re.M)
        # ③ AUTO:pipeline 活数字图（中文版专属块；英文版无该标记，自动跳过）
        params = {
            "discover_hours": topo.get("discover_hours", 6),
            "probe": ("每 15 分钟" if is_zh else "every 15 min") if "*/" in str(topo.get("probe", "")) else topo.get("probe", "每 15 分钟" if is_zh else "every 15 min"),
            "topic_n": topo.get("topic_n", 2), "kw_n": topo.get("kw_n", 3),
            "cand": fmt(d.get("candidates")), "age": fmt(d.get("age_min")),
            "plugins": fmt(c.get("plugins")), "nonplugin": fmt(c.get("nonplugin")),
            "cap": topo.get("cap", 10), "total": fmt(v.get("total")),
            "pass": fmt(v.get("pass")), "fail": fmt(v.get("fail")), "inc": fmt(v.get("inc")),
            "delta": fmt(dl.get("delta_since")), "batch": topo.get("batch", 100),
            "streams": topo.get("streams", 7), "stream_sec": topo.get("stream_sec", 60),
            "done": fmt(t.get("succeeded")),
            "spacing": topo.get("spacing", 35),
        }
        tmpl = DIAGRAM if is_zh else DIAGRAM_EN
        block = tmpl.format(**params).replace("{{", "{").replace("}}", "}")
        a, b = "<!-- AUTO:pipeline:START -->", "<!-- AUTO:pipeline:END -->"
        if a in t_readme and b in t_readme:
            i, j = t_readme.find(a), t_readme.find(b) + len(b)
            seg = t_readme[i:j]
            if '<img src="assets/pipeline-diagram' in seg:
                # 骨架版（mermaid 主显示或 SVG 主显示均适用）：仅替换围栏内活数字源码
                seg2, n = re.subn(r"```(?:mermaid)?\n[\s\S]*?\n```", block, seg, count=1)
                t_readme = t_readme[:i] + (seg2 if n else seg) + t_readme[j:]
            else:
                t_readme = t_readme[:i] + a + "\n" + block + "\n" + b + t_readme[j:]

        # ④ 数据截至锚（中英双版同步维护；对应标题不存在的版本正则不命中、安全跳过）
        anchor_line = f"> 数据截至快照 `{snap['run_id']}`（{bj(snap.get('generated_at', ''))} · 分类器 {snap.get('classifier', '')}）"
        anchor_en = f"> Data as of snapshot `{snap['run_id']}` ({bj(snap.get('generated_at', ''))} · classifier {snap.get('classifier', '')})"
        t_readme = re.sub(r">\s*数据截至快照 `[^\n]*\n+", "", t_readme)
        t_readme = re.sub(r">\s*Data as of snapshot `[^\n]*\n+", "", t_readme)
        t_readme = re.sub(r"(## 工作原理\n)\n+", "\\1\\n" + anchor_line.replace("\\", "\\\\") + "\\n\\n", t_readme, count=1)
        t_readme = re.sub(r"(## How it works\n)\n+", "\\1\\n" + anchor_en.replace("\\", "\\\\") + "\\n\\n", t_readme, count=1)

        # ④b 开头数字面（中文文案；英文头部走 EN 专属正则）
        cand_n = d.get("candidates") or 0
        slogan_n = (int(cand_n) // 100) * 100 if cand_n else None
        if slogan_n:
            # 口号与正文导语句共用动态候选数（百位取整 + 号后缀，README 全覆盖轮）
            t_readme = re.sub(r"(自动发现 )\d+\+?( 候选)", rf"\g<1>{slogan_n}+\g<2>", t_readme)
            t_readme = re.sub(r"(发现 )\d+\+?( 候选)", rf"\g<1>{slogan_n}+\g<2>", t_readme, count=1)
        if c.get("plugins"):
            t_readme = re.sub(r"(收录 )\d+( 个)", rf"\g<1>{c['plugins']}\g<2>", t_readme, count=1)
            t_readme = re.sub(r"(索引到)\d+( ?个? ?repos)", rf"\g<1>{cand_n}\g<2>", t_readme, count=1)
            t_readme = re.sub(r"^\| 自动收录 \| \d+ 个仓库 \|$", f"| 自动收录 | {c['plugins']} 个仓库 |",
                              t_readme, count=1, flags=re.M)
        dh = topo.get("discover_hours", 6)
        t_readme = re.sub(r"badge/scan-every_\d+h", f"badge/scan-every_{dh}h", t_readme, count=1)
        t_readme = re.sub(
            r"\*\*\d+ plugin repos indexed\*\*[^\n]*",
            f"**{fmt(c.get('plugins'))} plugin repos indexed** (manifest-level classification, v2 engine), "
            f"**{fmt(v.get('total'))} runtime-tested on the k8s track**.", t_readme, count=1)

        # ④c 目录对账：快照携带全量条目 → 补缺行 + 坍缩计数单值
        try:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            from reconcile_catalog import reconcile_catalog
            t_readme = reconcile_catalog(t_readme, snap.get("catalog_entries") or [])
        except Exception as _e:
            print(f"[render] WARN 目录对账跳过: {_e}")

        # ④d 生态快照块：头行时间戳 / 静态轨行 / 跟踪 PR / 报告链接（两版块内均中文）
        t_readme = re.sub(r"(更新于 [0-9-]+ [0-9:]+[^\n]*|渲染于快照 [0-9A-Za-z]+（[^\n]*）)",
                          f"渲染于快照 {snap['run_id']}（{bj(snap['generated_at'], '%Y-%m-%d %H:%M')}）· 数据源 data/snapshots/（渲染即对齐）",
                          t_readme, count=1)
        rd = sorted([x.name for x in (ROOT / "reports").iterdir() if x.is_dir() and x.name[:2] == "20"]) \
            if (ROOT / "reports").exists() else []
        if rd:
            d_latest = rd[-1]
            # 证据链只链现存资源：静态轨产物（index/mainline-compat/compile-compat）已随资产分离移除；
            # 运行实测指向当日实际存在的 agent-test*.md（bot 交付名为 agent-test-v2.md）
            agent = next((p.name for p in sorted((ROOT / "reports" / d_latest).glob("agent-test*.md"), reverse=True)), None)
            chain = ["[完整索引](PLUGINS-ALL.md)"]
            if agent:
                chain.append(f"[运行实测](reports/{d_latest}/{agent})")
            t_readme = re.sub(r"^\[完整索引\].*$", " · ".join(chain), t_readme, count=1, flags=re.M)

        def gh_slug(text):
            """GitHub 标题锚点：剥离 emoji/标点（保留其占位空格转连字符），对齐 github-slugger。"""
            t = re.sub(r'[^\w\u4e00-\u9fff\-\s]', '', str(text)).lower().lstrip('-')
            return re.sub(r'\s+', '-', t)

        # ④f 分类目录摘要卡：AUTO:catalog 整块重建为九类摘要列表（明细在 PLUGINS-ALL.md，根治大表格挤压）
        if domain_stats:
            if is_zh:
                cards = ["逐插件明细（判定 · 定位 · 星标）见 **[PLUGINS-ALL.md](PLUGINS-ALL.md)**。", ""]
                for dom, s in domain_stats.items():
                    if not s["total"]:
                        continue
                    anchor = gh_slug(dom + f'（{s["total"]}）')
                    cards.append(f'- **{dom}**（{s["total"]}）— 可用 {s["ok"]} · 不兼容 {s["bad"]} · '
                                 f'待定 {s["inc"]} · 未测 {s["un"]} · 监测 {s["watch"]} — [明细](PLUGINS-ALL.md#{anchor})')
            else:
                cards = ["Per-plugin details (verdict · location · stars) in **PLUGINS-ALL.md**.", ""]
                for dom, s in domain_stats.items():
                    if not s["total"]:
                        continue
                    anchor = gh_slug(dom + f'（{s["total"]}）')
                    cards.append(f'- **{dom}**（{s["total"]}）— OK {s["ok"]} · incompatible {s["bad"]} · '
                                 f'pending {s["inc"]} · untested {s["un"]} · watching {s["watch"]} — [details](PLUGINS-ALL.md#{anchor})')
            block = "<!-- AUTO:catalog:START -->\n\n" + "\n".join(cards) + "\n\n<!-- AUTO:catalog:END -->"
            t_readme = re.sub(r"<!-- AUTO:catalog:START -->[\s\S]*?<!-- AUTO:catalog:END -->",
                              lambda _: block, t_readme, count=1)

        path.write_text(t_readme)

    # ⑤ CHANGELOG 运行级条目（快照模式下的唯一写入者；按 run_id 幂等；两文件渲染后单次执行）
    cl = ROOT / "CHANGELOG.md"
    if cl.exists():
        ct = cl.read_text()
        entry_tag = f"<!-- snapshot:{snap['run_id']} -->"
        if entry_tag not in ct:
            entry = (f"## {bj(snap['generated_at'], '%Y-%m-%d')}（运行级 · {snap['run_id']}）{entry_tag}\n"
                     f"- 运行级实测：总 {v.get('total')}：可用 {v.get('pass')} / 真不兼容 {v.get('fail')} / "
                     f"待定 {v.get('inc')}（k8s agent · 公有生态口径）\n"
                     f"- 快照：data/snapshots/{snap['run_id']}.json（本条目与其同源）\n\n")
            ct = re.sub(r"<!-- snapshot:[^>]+>\n## [^\n]*\n(?:- [^\n]*\n){2}\n?", "", ct)
            i2 = ct.find("## ")
            cl.write_text(ct[:i2] + entry + ct[i2:] if i2 >= 0 else entry + ct)

    print(f"[render] run_id={snap['run_id']} · 徽章 confirmed-{c.get('plugins')}/tested-{v.get('total')} · "
          f"判定 {v.get('pass')}/{v.get('fail')}/{v.get('inc')} · 双文件渲染完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
