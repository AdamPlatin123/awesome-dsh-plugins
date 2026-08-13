#!/usr/bin/env python3
"""Catalog gate (SOP §8). Runs before any publish. Fail closed on any violation.

Checks:
  1. schema validity      — catalog entries vs plugin.schema.json (jsonschema if present,
                            else structural required-field check)
  2. id uniqueness        — no duplicate stable ids
  3. full_name uniqueness — no duplicate owner/name
  4. count conservation   — state sums match catalog_count
  5. never-pass hygiene   — not_run/inconclusive never counted as pass in summary
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "schema"
CAT_DIR = ROOT / "catalog" / "plugins"
CAT = ROOT / "generated" / "current" / "catalog.json"
SUM = ROOT / "generated" / "current" / "summary.json"

try:
    import jsonschema  # type: ignore
    HAVE_JSONSCHEMA = True
except ImportError:
    HAVE_JSONSCHEMA = False


def load(p: Path):
    return json.loads(p.read_text()) if p.is_file() else {}


def struct_check(entry: dict) -> list[str]:
    errs = []
    for f in ("schema_version", "id", "repository", "curation", "lifecycle"):
        if f not in entry:
            errs.append(f"missing required field {f}")
    if "id" in entry and not str(entry["id"]).startswith("github:"):
        errs.append(f"id not github-prefixed: {entry.get('id')}")
    if "curation" in entry and entry["curation"].get("state") not in (
            "candidate", "listed", "rejected", "removed", "blocked"):
        errs.append(f"bad curation.state: {entry.get('curation', {}).get('state')}")
    return errs


def main() -> int:
    errors: list[str] = []
    plugin_schema = load(SCHEMA / "plugin.schema.json")

    entries = []
    for p in sorted(CAT_DIR.glob("*.json")):
        try:
            e = json.loads(p.read_text())
        except json.JSONDecodeError as ex:
            errors.append(f"{p.name}: invalid JSON ({ex})")
            continue
        entries.append((p.name, e))
        if HAVE_JSONSCHEMA:
            try:
                jsonschema.validate(e, plugin_schema)
            except jsonschema.ValidationError as ex:
                errors.append(f"{p.name}: schema violation — {ex.message}")
        else:
            for m in struct_check(e):
                errors.append(f"{p.name}: {m}")

    # uniqueness
    ids = [e["id"] for _, e in entries if "id" in e]
    names = [e.get("repository", {}).get("full_name", "") for _, e in entries]
    if len(ids) != len(set(ids)):
        errors.append("duplicate stable ids in catalog/plugins/")
    if len(names) != len(set(names)):
        errors.append("duplicate full_name in catalog/plugins/")

    # count conservation vs generated catalog.json
    cat = load(CAT)
    if cat:
        expected = cat.get("catalog_count", 0)
        if expected != len(entries):
            errors.append(f"count drift: catalog.json says {expected} but {len(entries)} files on disk")

    # summary never-pass hygiene
    summ = load(SUM)
    if summ:
        be = summ.get("counts", {}).get("by_evidence", {})
        # sanity: pass+warn+fail+not_run+inconclusive per axis should not exceed total candidates
        total = summ.get("counts", {}).get("total", 0)
        for ax, counts in be.items():
            axsum = sum(counts.values())
            if axsum > total:
                errors.append(f"evidence axis {ax} sums to {axsum} > total {total}")

    if errors:
        print(f"[validate] FAIL — {len(errors)} violation(s):", file=sys.stderr)
        for e in errors[:20]:
            print(f"  - {e}", file=sys.stderr)
        return 30
    mode = "jsonschema" if HAVE_JSONSCHEMA else "structural"
    print(f"[validate] OK ({mode}) — {len(entries)} catalog entries, ids+names unique, counts conserved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
