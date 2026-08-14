#!/usr/bin/env python3
"""aggregate-agent-test.py — 把 .rt-agent/<plugin>.json 聚合成报告 + 计数。

输入：.rt-agent/*.json（每个插件一条，test-plugin-agent.sh 写入）
输出：
  reports/<日期>/agent-test.md        人工可读报告（按 ✅可用/❌不兼容/⏭️跳过 分组，含原因）
  generated/current/agent-results.json  机读汇总（README/后续精选目录消费）
  stdout：计数总览

用法：python3 aggregate-agent-test.py [--date YYYY-MM-DD]
"""
from __future__ import annotations
import json
import os
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RT = ROOT / ".rt-agent"


def classify(result: str) -> str:
    r = (result or "").strip()
    if r.startswith("✅"):
        return "pass"
    if r.startswith("❌"):
        return "fail"
    if r.startswith("⏭️") or "跳过" in r:
        return "skip"
    return "unknown"


def main() -> int:
    today = date.today().isoformat()
    for i, a in enumerate(sys.argv):
        if a == "--date" and i + 1 < len(sys.argv):
            today = sys.argv[i + 1]

    rows = []
    for p in sorted(RT.glob("*.json")):
        try:
            d = json.loads(p.read_text())
        except json.JSONDecodeError:
            continue
        plugin = d.get("plugin", p.stem)
        result = d.get("result", "")
        rows.append({
            "plugin": plugin,
            "category": classify(result),
            "result": result,
            "last_error": d.get("last_error", ""),
            "date": d.get("date", ""),
            "tries": d.get("tries"),
        })

    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r["category"]].append(r)

    # 机读汇总
    summary = {
        "run_date": today,
        "total": len(rows),
        "counts": {c: len(by_cat[c]) for c in ("pass", "fail", "skip", "unknown")},
        "results": rows,
    }
    out_json = ROOT / "generated" / "current" / "agent-results.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2))

    # 人工可读报告
    report_dir = ROOT / "reports" / today
    report_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Agent 运行级测试（%s · dsh + Qwen3.6-35B · k8s 5 分片）" % today,
        "",
        "- 方法：容器内 dsh（agent）经 de-stream 代理用 Qwen 读插件 README → 自主导入 → 验证；3 次重试，全败判不兼容。",
        "- 总计 %d：✅可用 %d / ❌不兼容 %d / ⏭️跳过 %d / 未知 %d"
        % (len(rows), len(by_cat["pass"]), len(by_cat["fail"]),
           len(by_cat["skip"]), len(by_cat["unknown"])),
        "",
    ]
    for cat, title, emoji in (("pass", "可用", "✅"), ("fail", "不兼容", "❌"), ("skip", "跳过", "⏭️"), ("unknown", "未知", "❓")):
        items = by_cat[cat]
        if not items:
            continue
        lines.append("## %s %s（%d）" % (emoji, title, len(items)))
        lines.append("")
        lines.append("| 插件 | 结论 | 原因 |")
        lines.append("|---|---|---|")
        for r in sorted(items, key=lambda x: x["plugin"].lower()):
            err = (r["last_error"] or "").replace("|", "\\|").replace("\n", " ")[:140]
            lines.append("| %s | %s | %s |" % (r["plugin"], r["result"].split("（")[0], err))
        lines.append("")
    (report_dir / "agent-test.md").write_text("\n".join(lines))

    print("[aggregate] total=%d ✅pass=%d ❌fail=%d ⏭️skip=%d ?=%d"
          % (len(rows), len(by_cat["pass"]), len(by_cat["fail"]),
             len(by_cat["skip"]), len(by_cat["unknown"])))
    print("[aggregate] report → %s" % (report_dir / "agent-test.md").relative_to(ROOT))
    print("[aggregate] json   → %s" % out_json.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
