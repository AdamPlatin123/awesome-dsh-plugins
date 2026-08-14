#!/usr/bin/env python3
"""Sync agent runtime test results into catalog JSON, PLUGINS.md, and README stats.

Usage:
    python3 scripts/sync-runtime.py reports/2026-08-14/agent-test.md [--dry-run]
"""
import json
import glob
import os
import re
import sys
import argparse
from datetime import datetime


def parse_agent_test(filepath):
    """Parse the agent-test.md report into {repo_name: {status, reason}}."""
    results = {}
    section = None
    for line in open(filepath, encoding='utf-8'):
        line = line.strip()
        if not line.startswith('|'):
            # Check section headers
            if '✅ 可用' in line and '##' in line:
                section = 'pass'
            elif '❌' in line and '##' in line:
                section = 'fail'
            continue
        if '---' in line or line.startswith('| 插件'):
            continue
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 4 and parts[1] and parts[1] != '插件':
            name = parts[1]
            reason = parts[3] if len(parts) > 3 else ''
            if section:
                results[name] = {
                    'status': 'pass' if section == 'pass' else 'fail',
                    'reason': reason,
                }
    return results


def extract_repo_short_name(full_name):
    """Extract short repo name from 'owner/repo' or return as-is."""
    return full_name.split('/')[-1] if '/' in full_name else full_name


def update_catalog(results, dry_run=False):
    """Update catalog/plugins/*.json with runtime test results."""
    updated = 0
    created = 0
    for json_file in sorted(glob.glob('catalog/plugins/*.json')):
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)
        repo_full = data.get('repository', {}).get('full_name', '')
        repo_short = extract_repo_short_name(repo_full)

        # Try exact match on full_name or short name
        match = None
        for test_name in results:
            if test_name == repo_full or test_name == repo_short:
                match = test_name
                break

        if match:
            r = results[match]
            data['runtime_test'] = {
                'status': r['status'],
                'reason': r['reason'][:200],
                'tested_at': '2026-08-14',
            }
            if not dry_run:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                    f.write('\n')
            updated += 1
            print(f"  catalog: {repo_short} → {r['status']}")

    # Count how many test results don't have catalog entries
    catalog_names = set()
    for json_file in glob.glob('catalog/plugins/*.json'):
        with open(json_file, encoding='utf-8') as f:
            d = json.load(f)
        catalog_names.add(extract_repo_short_name(d.get('repository', {}).get('full_name', '')))

    unmatched = [n for n in results if extract_repo_short_name(n) not in catalog_names]
    print(f"\n  Catalog: {updated}/{len(glob.glob('catalog/plugins/*.json'))} updated")
    print(f"  Test results without catalog entry: {len(unmatched)}")
    return updated, len(unmatched)


def update_plugins_md(results, dry_run=False):
    """Update PLUGINS.md '运行级' column."""
    filepath = 'PLUGINS.md'
    lines = open(filepath, encoding='utf-8').readlines()
    updated = 0

    for i, line in enumerate(lines):
        if not line.strip().startswith('|'):
            continue
        parts = line.split('|')
        if len(parts) < 4:
            continue
        plugin_name = parts[1].strip()
        # Try to match
        for test_name in results:
            test_short = extract_repo_short_name(test_name)
            if plugin_name == test_name or plugin_name == test_short:
                r = results[test_name]
                new_status = '✅' if r['status'] == 'pass' else '❌'
                old_status = parts[-2].strip()
                if old_status != new_status:
                    parts[-2] = f' {new_status} '
                    lines[i] = '|'.join(parts)
                    updated += 1
                    print(f"  PLUGINS.md: {plugin_name} {old_status} → {new_status}")
                break

    if updated > 0 and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    print(f"\n  PLUGINS.md: {updated} entries updated")
    return updated


def update_readme_stats(results, dry_run=False):
    """Update README.md runtime test statistics if present."""
    pass_count = sum(1 for r in results.values() if r['status'] == 'pass')
    fail_count = sum(1 for r in results.values() if r['status'] == 'fail')
    total = len(results)
    print(f"\n  Runtime stats: {total} total, {pass_count} ✅, {fail_count} ❌")

    # Find and update stats in README if there's a runtime test line
    for filepath in ['README.md', 'README.en-US.md']:
        if not os.path.exists(filepath):
            continue
        content = open(filepath, encoding='utf-8').read()
        # Look for runtime test stat patterns
        # Add or update a line like "运行级实测: 555 可用 / 138 失败 (共 1076 个)"
        old_pattern = r'运行级实测[：:]\s*\d+\s*可用\s*/\s*\d+\s*失败'
        new_text = f'运行级实测：{pass_count} 可用 / {fail_count} 失败（共 {total} 个）'
        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_text, content)
            if not dry_run:
                open(filepath, 'w', encoding='utf-8').write(content)
            print(f"  {filepath}: stats updated")
        else:
            print(f"  {filepath}: no runtime stats line found (skipped)")


def main():
    parser = argparse.ArgumentParser(description='Sync agent runtime test results')
    parser.add_argument('report', help='Path to agent-test.md')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    args = parser.parse_args()

    if not os.path.exists(args.report):
        print(f"Error: {args.report} not found")
        sys.exit(1)

    print(f"{'=' * 60}")
    print(f"Syncing runtime test results from: {args.report}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'WRITE'}")
    print(f"{'=' * 60}\n")

    # Step 1: Parse report
    results = parse_agent_test(args.report)
    print(f"Parsed {len(results)} plugin results")
    pass_count = sum(1 for r in results.values() if r['status'] == 'pass')
    fail_count = sum(1 for r in results.values() if r['status'] == 'fail')
    print(f"  ✅ {pass_count} / ❌ {fail_count}\n")

    # Step 2: Update catalog
    print("--- Catalog Update ---")
    update_catalog(results, args.dry_run)

    # Step 3: Update PLUGINS.md
    print("\n--- PLUGINS.md Update ---")
    update_plugins_md(results, args.dry_run)

    # Step 4: Update README stats
    print("\n--- README Stats ---")
    update_readme_stats(results, args.dry_run)

    print(f"\n{'=' * 60}")
    print("Done!")


if __name__ == '__main__':
    main()
