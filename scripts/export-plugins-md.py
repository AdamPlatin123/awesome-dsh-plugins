#!/usr/bin/env python3
"""Export PLUGINS.md entries as a radar input manifest.

Radar (AdamPlatin123/dsh-plugin-radar) discovers plugins via GitHub topic
scan (topic:dsh-plugin etc.). Entries manually registered in PLUGINS.md
whose repos carry no topic never enter that scan. This script exports the
registered repo list so radar's clone step can merge it as an extra source.

Output: generated/plugins-md-repos.json
    { "generated_at": "...", "count": N, "repos": ["owner/repo", ...] }

The export excludes the template example row. Repos already covered by the
topic scan are harmless duplicates: radar dedupes by GitHub numeric repo id
(catalog/policy.json discovery.dedupe_key).

Usage:
    python3 scripts/export-plugins-md.py [--dry-run]
"""
import argparse
import json
import os
import re
from datetime import datetime, timezone

REPO_RE = re.compile(r'\[([^\]]+)\]\(https://github\.com/([^/)]+/[^/)]+?)(?:/[^\)]*)?\)')
TEMPLATE_MARKERS = ('你的账号', 'my-plugin)')


def parse_plugins_md(filepath):
    """Extract (plugin_name, owner/repo) pairs from PLUGINS.md table rows."""
    repos = []
    seen = set()
    for line in open(filepath, encoding='utf-8'):
        line = line.strip()
        if not line.startswith('|') or '---' in line or '<!--' in line:
            continue
        for label, full in REPO_RE.findall(line):
            if any(m in line for m in TEMPLATE_MARKERS):
                continue
            if full not in seen:
                seen.add(full)
                repos.append(full)
    return repos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    repos = parse_plugins_md('PLUGINS.md')
    manifest = {
        'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'source': 'PLUGINS.md',
        'count': len(repos),
        'repos': sorted(repos),
    }

    out = 'generated/plugins-md-repos.json'
    print(f"PLUGINS.md → radar manifest: {len(repos)} repos")
    if args.dry_run:
        print(json.dumps(manifest, ensure_ascii=False, indent=2)[:500])
        return

    os.makedirs('generated', exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
