#!/usr/bin/env python3
"""backfill_desc.py — GitHub 描述回填器。

对快照 catalog_entries 中 desc 为空/占位但已有真实 URL 的条目，GraphQL 批量拉取
仓库 description，写入 data/desc-cache.json（owner/repo → description，增量幂等）。
被 gen_plugins_all 链路消费：无 desc 条目用回填描述参与分类与展示。
依赖：gh 认证 token + curl。
"""
import glob
import json
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / 'data' / 'desc-cache.json'
BATCH = 60

_token = None


def token():
    global _token
    if not _token:
        _token = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
    return _token


def entries():
    merged = {}
    for fp in sorted(glob.glob(str(ROOT / 'data' / 'snapshots' / '*.json')), reverse=True):
        try:
            d = json.loads(Path(fp).read_text())
        except json.JSONDecodeError:
            continue
        for e in d.get('catalog_entries') or []:
            merged.setdefault((e['name'], e.get('url', '')), dict(e))
    return list(merged.values())


def run_batch(repos):
    defs = ', '.join(f'$r{j}: String!' for j in range(len(repos)))
    parts = ' '.join(f'q{j}: repository(owner: "{r.split("/")[0]}", name: "{r.split("/")[1]}") {{ description }}'
                     for j, r in enumerate(repos))
    q = f'query ({defs}) {{ {parts} }}'
    for _ in range(3):
        p = subprocess.run(['curl', '-s', '--max-time', '50',
                            '-H', f'Authorization: Bearer {token()}',
                            '-H', 'Content-Type: application/json',
                            '-X', 'POST', 'https://api.github.com/graphql',
                            '-d', json.dumps({'query': q})],
                           capture_output=True, text=True)
        try:
            data = json.loads(p.stdout).get('data') or {}
        except Exception:
            data = {}
        if len(data) >= len(repos) * 0.8:
            return {repos[j]: ((data.get(f'q{j}') or {}).get('description') or '')
                    for j in range(len(repos))}
        time.sleep(3)
    return {}


def main():
    cache = {}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text())
        except json.JSONDecodeError:
            pass

    todo = []
    for e in entries():
        url = e.get('url', '')
        desc = (e.get('desc') or '').strip()
        if 'github.com/' not in url or 'search?q=' in url:
            continue
        full = url.split('github.com/')[1].strip('/')
        if full.count('/') != 1:
            continue
        if desc and desc != '—' and not desc.startswith('http'):
            cache.setdefault(full, desc)  # 已有描述也缓存（统一事实源）
            continue
        if full not in cache:
            todo.append(full)

    todo = sorted(set(todo))
    print(f'[backfill-desc] 待回填 {len(todo)} 个（缓存已有 {len(cache)}）')
    if not todo:
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0))
        return

    for i in range(0, len(todo), BATCH):
        batch = todo[i:i + BATCH]
        got = run_batch(batch)
        cache.update(got)
        print(f'  {min(i + BATCH, len(todo))}/{len(todo)}', flush=True)
        time.sleep(2)

    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0))
    filled = sum(1 for k in todo if cache.get(k))
    print(f'[backfill-desc] 回填成功 {filled}/{len(todo)} → {CACHE.name}（合计 {len(cache)}）')


if __name__ == '__main__':
    main()
