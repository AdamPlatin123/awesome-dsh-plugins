#!/usr/bin/env python3
"""哨兵校验（B3 / 实施序 0.5 步）。

对比 results 目录与 sentinel-baseline.json 的已知结论集。
任何 mismatch → exit 1（调用方语义：阻断墓碑与发布——⑥熔断的哨兵臂）。

用法：python3 data/sentinel/sentinel-check.py [--results DIR] [--baseline FILE]
  --results 默认从环境 RADAR_RESULTS_DIR 或 <repo>/.rt-agent-v2/results 推断。
"""
import json
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
BASELINE = HERE / "sentinel-baseline.json"

# 基线 expect → results 可接受 status/result 映射（弹性预期展开）
ACCEPT = {
    "pass": [("status", "pass")],
    "fail": [("status", "fail")],
    "skipped": [("status", "skipped")],
    # 弹性：放行机制产物（旧口径 pass / 新口径 blocked→approved）
    "pass_or_gate": [("status", "pass"), ("result_prefix", "PASS: web-load")],
    "pass_or_webgate": [("status", "pass"), ("result_prefix", "PASS: web-load")],
    "web_gate": [("result_prefix", "env-needs-web-host"), ("result_prefix", "PASS: web-load")],
    "clone_fail_or_pass": [("status", "pass"), ("result_prefix", "pod-clone failed")],
}


def load_results(results_dir: pathlib.Path) -> dict:
    out = {}
    for p in results_dir.glob("*.json"):
        try:
            d = json.loads(p.read_text())
        except Exception:
            continue
        if d.get("evidence_kind") == "runner":
            out[d.get("local_key", "")] = d
    return out


def entry_ok(entry: dict, result: dict | None) -> tuple[bool, str]:
    if result is None:
        return False, "missing-verdict"
    expect = entry["expect"]
    ok_set = ACCEPT.get(expect)
    if ok_set is None:
        return False, f"unknown-expect:{expect}"
    for kind, val in ok_set:
        if kind == "status" and result.get("status") == val:
            return True, ""
        if kind == "result_prefix" and (result.get("result") or "").startswith(val):
            return True, ""
    return False, f"verdict={result.get('status')}/{(result.get('result') or '')[:30]}"


def main() -> int:
    results_dir = None
    args = sys.argv[1:]
    if "--results" in args:
        results_dir = pathlib.Path(args[args.index("--results") + 1])
    else:
        env = os.environ.get("RADAR_RESULTS_DIR")
        if env:
            results_dir = pathlib.Path(env)
    baseline = BASELINE
    if "--baseline" in args:
        baseline = pathlib.Path(args[args.index("--baseline") + 1])

    bl = json.loads(baseline.read_text())
    if results_dir is None:
        print("[sentinel] 未指定 --results/RADAR_RESULTS_DIR，且本机无远端 results——"
              "只做基线自检", file=sys.stderr)
        ok = all(e["expect"] in ACCEPT for e in bl["entries"])
        print(f"[sentinel] baseline self-check: {'OK' if ok else 'UNKNOWN-EXPECT'} "
              f"({len(bl['entries'])} entries)")
        return 0 if ok else 1

    results = load_results(results_dir)
    mismatches = []
    for e in bl["entries"]:
        ok, why = entry_ok(e, results.get(e["local_key"]))
        if not ok:
            mismatches.append((e["local_key"], e["shape"], why))
    print(f"[sentinel] {len(bl['entries'])} 条基线 | {len(mismatches)} mismatch")
    for lk, shape, why in mismatches:
        print(f"  MISMATCH {lk} [{shape}] {why}")
    if mismatches:
        print("[sentinel] ACTION: block_tombstone_and_publish（环境疑似漂移，"
              "先查 runner/镜像/dsh/pnpm/Qwen 再发布）")
        return 1
    print("[sentinel] ALL GREEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
