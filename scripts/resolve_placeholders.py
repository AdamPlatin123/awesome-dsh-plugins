#!/usr/bin/env python3
"""resolve-placeholders.py — 占位 URL 定位复核器。

对快照 catalog_entries 中 search?q= 占位条目做 GitHub 反查（GraphQL 变量法，三级匹配），
结果写入 data/locate-cache.json（增量合并，幂等）。手动或定期运行；gen-plugins-all.py 消费。
依赖：gh 认证 token + curl。
"""
import glob
import json
import re
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / 'data' / 'locate-cache.json'
BATCH = 40

_token = None


def token():
    global _token
    if not _token:
        _token = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
    return _token


def placeholder_names():
    names = set()
    for fp in sorted(glob.glob(str(ROOT / 'data' / 'snapshots' / '*.json'))):
        try:
            d = json.loads(Path(fp).read_text())
        except json.JSONDecodeError:
            continue
        for e in d.get('catalog_entries') or []:
            if 'search?q=' in (e.get('url') or ''):
                names.add(e['name'])
    return sorted(names)


def match(name, repos):
    low = name.lower()
    exact = [r for r in repos if r.split('/')[1].lower() == low]
    if len(exact) == 1:
        return {'status': 'found', 'full_name': exact[0]}
    if len(exact) > 1:
        return {'status': 'ambiguous', 'candidates': exact[:3]}
    joined = [r for r in repos if r.lower().replace('/', '-') == low]
    if len(joined) == 1:
        return {'status': 'found', 'full_name': joined[0]}
    if len(joined) > 1:
        return {'status': 'ambiguous', 'candidates': joined[:3]}
    if len(repos) == 1:
        return {'status': 'found', 'full_name': repos[0], 'fuzzy': True}
    return {'status': 'ambiguous', 'candidates': repos[:3]} if repos else {'status': 'not_found'}


def run_batch(batch, out):
    defs = ', '.join(f'$q{j}: String!' for j in range(len(batch)))
    sel = ' '.join(f's{j}: search(query: $q{j}, type: REPOSITORY, first: 5) {{ nodes {{ ... on Repository {{ nameWithOwner }} }} }}'
                   for j in range(len(batch)))
    q = f'query ({defs}) {{ {sel} }}'
    vars = {f'q{j}': f'"{n}" in:name' for j, n in enumerate(batch)}
    for _ in range(3):
        p = subprocess.run(['curl', '-s', '--max-time', '50',
                            '-H', f'Authorization: Bearer {token()}',
                            '-H', 'Content-Type: application/json',
                            '-X', 'POST', 'https://api.github.com/graphql',
                            '-d', json.dumps({'query': q, 'variables': vars})],
                           capture_output=True, text=True)
        try:
            data = json.loads(p.stdout).get('data') or {}
        except Exception:
            data = {}
        if len(data) >= len(batch) * 0.8:
            for j, n in enumerate(batch):
                nodes = (data.get(f's{j}') or {}).get('nodes') or []
                out[n] = match(n, [x['nameWithOwner'] for x in nodes])
            return True
        time.sleep(3)
    return False


def main():
    cache = {'resolved_at': '', 'entries': {}}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text())
        except json.JSONDecodeError:
            pass
    known = cache['entries']

    names = [n for n in placeholder_names() if n not in known or known[n].get('status') == 'error']
    print(f'[resolve] 待复核 {len(names)} 个（缓存已有 {len(known)}）')
    if not names:
        return

    failed = []
    for i in range(0, len(names), BATCH):
        batch = names[i:i + BATCH]
        if run_batch(batch, known):
            print(f'  {min(i + BATCH, len(names))}/{len(names)}', flush=True)
        else:
            failed.extend(batch)
        time.sleep(2)

    for n in failed:
        known.pop(n, None)
    cache['resolved_at'] = time.strftime('%Y-%m-%d')
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0))
    from collections import Counter
    sc = Counter(v['status'] for v in known.values())
    print(f'[resolve] 缓存合计 {len(known)}：{dict(sc)}（失败 {len(failed)} 可重跑）')


if __name__ == '__main__':
    main()
