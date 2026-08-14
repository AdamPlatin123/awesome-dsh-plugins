#!/usr/bin/env python3
"""render-readme-from-snapshot.py — Bot B：从已合并快照渲染 README（仓库内运行，零外部依赖）。

契约：只读 data/snapshots/*.json（取 run_id 最新），绝不访问网络/指标流。
渲染面：三徽章 + 证据层运行级行 + AUTO:pipeline 活数字图 + 「数据截至」锚。
幂等：同快照重复渲染输出逐字节一致。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAP_DIR = ROOT / "data" / "snapshots"
README = ROOT / "README.md"

DIAGRAM = """```mermaid
flowchart TB
    subgraph Discovery["🔍 发现（每 {discover_hours} 小时 · probe {probe} 巡检触发）"]
        A1["GitHub Search<br/>topic ×{topic_n} + keyword ×{kw_n}<br/>候选 {cand} · 龄 {age}m"]
        A2["本地库补全 · 去重 repo id"]
        A3["🚫 私有 org 仓排除<br/>{spacing}s 错峰 · 403 退避 · dshow 黑名单"]
    end
    subgraph Validation["📋 验证（driver 20s 流式循环）"]
        B1{{"package.json<br/>name + main/exports/dsh?"}}
    end
    B1 -->|"插件 {plugins}"| C1["k8s 运行级测试<br/>一插件一 pod · 并发 {cap}<br/>dsh agent + Qwen（de-stream）"]
    B1 -->|"非插件（累计删 {nonplugin}）"| B3["❌ 即删省空间"]
    C1 --> D1{{"判定 · 总 {total}"}}
    D1 -->|"✅ {pass} / ❌ {fail}"| E1["聚合 + README 分类统计"]
    D1 -->|"⚠️ {inc} 环境类重试"| C1
    E1 --> E2["cadence 交付<br/>本周期增量 {delta}/{batch}<br/>双仓 bot PR（幂等 supersede）"]
    S["⚖️ 静态四维轨（每日 02:00）"] -.-> E1
    M["🛡 radar-probe {probe} 自愈<br/>{streams} 指标流 × {stream_sec}s · 完成累计 {done}"] -.-> A1
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


def fmt(x):
    return "—" if x is None else str(x)


def main():
    snap = latest_snapshot()
    if not snap or not str(snap.get("schema", "")).startswith("radar-snapshot/"):
        print("[render] 无有效快照（radar-snapshot/1）— 保持 README 现状（安全停旧）")
        return 0

    v, d, c, t, dl = (snap[k] for k in ("verdict", "discovery", "clone", "test", "deliver"))
    topo = snap.get("topology", {})

    t_readme = README.read_text()

    # ① 三徽章
    t_readme = re.sub(r"badge/confirmed-\d+", f"badge/confirmed-{fmt(c.get('plugins'))}", t_readme)
    t_readme = re.sub(r"badge/tested-\d+", f"badge/tested-{fmt(v.get('total'))}", t_readme)

    # ② 证据层运行级行
    # 整行替换（历史版本曾因 [^|]* 在含管道行上只换首段导致行膨胀）
    t_readme = re.sub(
        r"^\| 运行级实测 .*$",
        f"| 运行级实测 | ✅{v.get('pass')} 可用 · {v.get('fail')} 不兼容 · {v.get('inc')} 待定"
        f"（共 {v.get('total')} 个，k8s agent 口径）|",
        t_readme, count=1, flags=re.M)

    # ③ AUTO:pipeline 活数字图
    params = {
        "discover_hours": topo.get("discover_hours", 6), "probe": topo.get("probe", "*/15"),
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
    block = DIAGRAM.format(**params).replace("{{", "{").replace("}}", "}")
    a, b = "<!-- AUTO:pipeline:START -->", "<!-- AUTO:pipeline:END -->"
    if a in t_readme and b in t_readme:
        i, j = t_readme.find(a), t_readme.find(b) + len(b)
        t_readme = t_readme[:i] + a + "\n" + block + "\n" + b + t_readme[j:]
    else:
        m = re.search(r"```mermaid\s*\n.*?```", t_readme, re.S)
        if m:
            t_readme = t_readme.replace(m.group(0), a + "\n" + block + "\n" + b, 1)

    # ④ 数据截至锚（数字对齐的显式凭证）
    anchor_line = f"> 📌 数据截至快照 `{snap['run_id']}`（{snap.get('generated_at','')} · 分类器 {snap.get('classifier','')}）"
    # 坍缩式重插：先清旧锚（含其后空行），再把标题后的任意换行序列规整为 定长两段 —— 保证幂等
    t_readme = re.sub(r"> 📌 数据截至快照 `[^\n]*\n+", "", t_readme)
    t_readme = re.sub(r"(## 工作原理\n)\n+", "\\1\\n" + anchor_line.replace("\\", "\\\\") + "\\n\\n", t_readme, count=1)

    # ④b 开头数字面（保留人工措辞，仅替换数字）：
    #    口号候选数（2500+ 样式，向下取整百）/ 导语收录数与索引数 / 证据层自动收录行 / scan 徽章节奏
    cand_n = d.get("candidates") or 0
    slogan_n = (int(cand_n) // 100) * 100 if cand_n else None
    if slogan_n:
        t_readme = re.sub(r"(自动发现 )\d+\+?( 候选)", rf"\g<1>{slogan_n}+\g<2>", t_readme, count=1)
    if c.get("plugins"):
        t_readme = re.sub(r"(收录 )\d+( 个)", rf"\g<1>{c['plugins']}\g<2>", t_readme, count=1)
        t_readme = re.sub(r"(索引到)\d+( ?个? ?repos)", rf"\g<1>{cand_n}\g<2>", t_readme, count=1)
        t_readme = re.sub(r"^\| 自动收录 \| \d+ 个仓库 \|$", f"| 自动收录 | {c['plugins']} 个仓库 |",
                          t_readme, count=1, flags=re.M)
    dh = topo.get("discover_hours", 6)
    t_readme = re.sub(r"badge/scan-every_\d+h", f"badge/scan-every_{dh}h", t_readme, count=1)

    # ④c 目录对账：快照携带全量条目 → 补缺行 + 坍缩计数单值
    try:
        import sys as _sys
        _sys.path.insert(0, str(Path(__file__).resolve().parent))
        from reconcile_catalog import reconcile_catalog
        t_readme = reconcile_catalog(t_readme, snap.get("catalog_entries") or [])
    except Exception as _e:
        print(f"[render] WARN 目录对账跳过: {_e}")

    # ④d 生态快照块：头行时间戳 / 静态轨行（读仓内最新 mainline-compat）/ 跟踪 PR / 报告链接
    t_readme = re.sub(r"更新于 [0-9-]+ [0-9:]+ · 每 \d+ 小时刷新[^\n]*",
                      f"渲染于快照 {snap['run_id']}（{snap['generated_at'][:16]}）· 数据源 data/snapshots/（渲染即对齐）",
                      t_readme, count=1)
    # 静态轨：快照携带（Bot A 从远程最新 mainline-compat 读取入快照）
    st = snap.get("static") or {}
    if st.get("summary"):
        t_readme = re.sub(r"^\| 静态综合判定 \|.+$",
                          f"| 静态综合判定 | {st['summary']}（静态轨 {st.get('date','')} · 经快照入仓） |",
                          t_readme, count=1, flags=re.M)
    if dl.get("open_bot_prs") is not None:
        t_readme = re.sub(r"^\| 正在跟踪的 PR \|.+$",
                          f"| 正在跟踪的 PR | {dl.get('open_bot_prs')}（快照 deliver 口径） |",
                          t_readme, count=1, flags=re.M)
    # 报告链接指向最新日期目录
    rd = sorted([d.name for d in (ROOT / "reports").iterdir() if d.is_dir() and d.name[:2] == "20"])
    if rd:
        d_latest = rd[-1]
        t_readme = re.sub(r"\[完整索引\]\(reports/[0-9-]+/index\.md\)", f"[完整索引](reports/{d_latest}/index.md)", t_readme)
        t_readme = re.sub(r"\[静态矩阵\]\(reports/[0-9-]+/mainline-compat\.md\)", f"[静态矩阵](reports/{d_latest}/mainline-compat.md)", t_readme)
        t_readme = re.sub(r"\[编译实验\]\(reports/[0-9-]+/compile-compat\.md\)", f"[编译实验](reports/{d_latest}/compile-compat.md)", t_readme)
        t_readme = re.sub(r"\[运行实测\]\(reports/[0-9-]+/[^)]*\.md\)", f"[运行实测](reports/{d_latest}/agent-test.md)", t_readme)

    # ⑤ CHANGELOG 运行级条目（快照模式下的唯一写入者；按 run_id 幂等）
    cl = ROOT / "CHANGELOG.md"
    if cl.exists():
        ct = cl.read_text()
        entry_tag = f"<!-- snapshot:{snap['run_id']} -->"
        if entry_tag not in ct:
            entry = (f"## {snap['generated_at'][:10]}（运行级 · {snap['run_id']}）{entry_tag}\n"
                     f"- 运行级实测：总 {v.get('total')}：✅可用 {v.get('pass')} / ❌真不兼容 {v.get('fail')} / "
                     f"⚠️待定 {v.get('inc')}（k8s agent · 公有生态口径）\n"
                     f"- 快照：data/snapshots/{snap['run_id']}.json（本条目与其同源）\n\n")
            ct = re.sub(r"<!-- snapshot:[^>]+>\n## [^\n]*\n(?:- [^\n]*\n){2}\n?", "", ct)
            i2 = ct.find("## ")
            cl.write_text(ct[:i2] + entry + ct[i2:] if i2 >= 0 else entry + ct)

    README.write_text(t_readme)
    print(f"[render] run_id={snap['run_id']} · 徽章 confirmed-{c.get('plugins')}/tested-{v.get('total')} · "
          f"判定 ✅{v.get('pass')}/❌{v.get('fail')}/⚠️{v.get('inc')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
