#!/usr/bin/env python3
"""resolve-placeholders.py — 占位 URL 定位复核器 + 仓库存在性审计。

对快照 catalog_entries 中 search?q= 占位条目做 GitHub 反查（GraphQL 变量法，三级匹配），
结果写入 data/locate-cache.json（增量合并，幂等）。命中仓库同时记录实时 star（stargazerCount），
供 gen-plugins-all.py 渲染——快照层 star 为 0 的条目以此恢复真实值。
已 found 但缺 star 的缓存条目会被重新反查补齐（刷新路径）。
同时维护 data/url-audit.json：真实 URL 条目 ∪ 定位命中仓库 ∪ README/PLUGINS.md 手工区链接的
存在性审计（改名/删除/转私有判 gone，7 天 TTL 重查），gen-plugins_all.py 据此把消亡链接降为
空仓监测；手工区链接判 gone 仅输出告警（人工处置，不自动改文档）。
远程 resolve-watch 每日定时运行；也可手动执行。依赖：gh 认证 token + curl。
"""
import datetime
import glob
import json
import re
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / 'data' / 'locate-cache.json'
AUDIT = ROOT / 'data' / 'url-audit.json'
BATCH = 40
AUDIT_TTL_DAYS = 7
REAL_URL_RE = re.compile(r'github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)')

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


def real_url_fulls():
    """快照层真实 URL 条目的仓库全名（小写）——URL 存在性审计的对象池之一。"""
    out = set()
    for fp in sorted(glob.glob(str(ROOT / 'data' / 'snapshots' / '*.json'))):
        try:
            d = json.loads(Path(fp).read_text())
        except json.JSONDecodeError:
            continue
        for e in d.get('catalog_entries') or []:
            m = REAL_URL_RE.search(e.get('url') or '')
            if m and 'search?q=' not in (e.get('url') or ''):
                out.add(f"{m.group(1)}/{m.group(2)}".lower())
    return out


DOC_FILES = ('README.md', 'README.en-US.md', 'PLUGINS.md')


def doc_link_fulls():
    """README/PLUGINS.md 等手工区文档中的仓库链接（小写全名）——审计对象池，
    判 gone 只报告不自动修改（手工内容归人工维护）。"""
    out = set()
    for name in DOC_FILES:
        fp = ROOT / name
        if not fp.exists():
            continue
        for u in re.findall(r'\]\((https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/?\)', fp.read_text()):
            out.add(u.split('github.com/')[1].strip('/').lower())
    return out


def check_existence(batch):
    """GraphQL 直查仓库存在性；返回 {full_name_lower: bool}。失败批次返回空。"""
    defs = ', '.join(f'$o{j}: String! $n{j}: String!' for j in range(len(batch)))
    sel = ' '.join(f'r{j}: repository(owner: $o{j}, name: $n{j}) {{ id }}' for j in range(len(batch)))
    q = f'query ({defs}) {{ {sel} }}'
    vars = {}
    for j, full in enumerate(batch):
        o, n = full.split('/')
        vars[f'o{j}'], vars[f'n{j}'] = o, n
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
            return {full: data.get(f'r{j}') is not None for j, full in enumerate(batch)}
        time.sleep(3)
    return {}


def audit_urls(locate_known):
    """维护 data/url-audit.json：真实 URL 条目 ∪ 定位命中仓库 ∪ 手工区文档链接，
    缺失或超 TTL 的重查存在性；手工区链接判 gone 时输出告警（不自动改文档）。"""
    audit = {'checked_at': '', 'entries': {}}
    if AUDIT.exists():
        try:
            audit = json.loads(AUDIT.read_text())
        except json.JSONDecodeError:
            pass
    today = time.strftime('%Y-%m-%d')
    cutoff = (datetime.date.today() - datetime.timedelta(days=AUDIT_TTL_DAYS)).isoformat()
    doc_fulls = doc_link_fulls()
    universe = real_url_fulls() | doc_fulls | {
        (v.get('full_name') or '').lower() for v in locate_known.values()
        if v.get('status') == 'found' and v.get('full_name')}
    stale = sorted(u for u in universe
                   if u and audit['entries'].get(u, {}).get('checked', '') < cutoff)
    print(f'[audit] URL 存在性待查 {len(stale)} 个（缓存已有 {len(audit["entries"])}，TTL {AUDIT_TTL_DAYS} 天）')
    for i in range(0, len(stale), BATCH):
        res = check_existence(stale[i:i + BATCH])
        for full, ok in res.items():
            audit['entries'][full] = {'status': 'ok' if ok else 'gone', 'checked': today}
        if res:
            print(f'  {min(i + BATCH, len(stale))}/{len(stale)}', flush=True)
        time.sleep(2)
    audit['checked_at'] = today
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=0))
    from collections import Counter
    sc = Counter(v['status'] for v in audit['entries'].values())
    print(f'[audit] 缓存合计 {len(audit["entries"])}：{dict(sc)}')
    doc_gone = sorted(u for u in doc_fulls if audit['entries'].get(u, {}).get('status') == 'gone')
    if doc_gone:
        print(f'[audit] ⚠️ 手工区文档（README/PLUGINS.md）存在失效仓库链接 {len(doc_gone)} 个——人工处置：')
        for u in doc_gone:
            print(f'  gone: {u}')


def match(name, repos):
    """repos: [(nameWithOwner, stargazerCount)]；返回定位结果，found 附带实时 star。"""
    low = name.lower()
    exact = [r for r in repos if r[0].split('/')[1].lower() == low]
    if len(exact) == 1:
        return {'status': 'found', 'full_name': exact[0][0], 'star': exact[0][1]}
    if len(exact) > 1:
        return {'status': 'ambiguous', 'candidates': [r[0] for r in exact[:3]]}
    joined = [r for r in repos if r[0].lower().replace('/', '-') == low]
    if len(joined) == 1:
        return {'status': 'found', 'full_name': joined[0][0], 'star': joined[0][1]}
    if len(joined) > 1:
        return {'status': 'ambiguous', 'candidates': [r[0] for r in joined[:3]]}
    if len(repos) == 1:
        return {'status': 'found', 'full_name': repos[0][0], 'star': repos[0][1], 'fuzzy': True}
    return {'status': 'ambiguous', 'candidates': [r[0] for r in repos[:3]]} if repos else {'status': 'not_found'}


def run_batch(batch, out):
    defs = ', '.join(f'$q{j}: String!' for j in range(len(batch)))
    sel = ' '.join(f's{j}: search(query: $q{j}, type: REPOSITORY, first: 5) {{ nodes {{ ... on Repository {{ nameWithOwner stargazerCount }} }} }}'
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
                out[n] = match(n, [(x['nameWithOwner'], x.get('stargazerCount') or 0) for x in nodes])
            return True
        time.sleep(3)
    return False


def fetch_stars(batch):
    """GraphQL 批量查 stargazerCount；返回 {full_name_lower: stars}。失败批次返回空。"""
    defs = ', '.join(f'$o{j}: String! $n{j}: String!' for j in range(len(batch)))
    sel = ' '.join(f'r{j}: repository(owner: $o{j}, name: $n{j}) {{ stargazerCount }}' for j in range(len(batch)))
    q = f'query ({defs}) {{ {sel} }}'
    vars = {}
    for j, full in enumerate(batch):
        o, n = full.split('/')
        vars[f'o{j}'], vars[f'n{j}'] = o, n
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
            return {full: (data.get(f'r{j}') or {}).get('stargazerCount')
                    for j, full in enumerate(batch) if data.get(f'r{j}') is not None}
        time.sleep(3)
    return {}


def reg_star_backfill(known):
    """登记轨星数回填（#189 兜底行星数失真）：PLUGINS.md 链接仓库缺星记录的（locate-cache 以
    full_name 为键，与占位 local_key 键不冲突），批量查 stargazerCount 写入——渲染端 live_star 直接消费。"""
    reg_md = ROOT / 'PLUGINS.md'
    if not reg_md.is_file():
        return
    fulls = sorted({u.split('github.com/')[1].strip('/').lower()
                    for u in re.findall(r'\]\((https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/?\)',
                                        reg_md.read_text())})
    todo = [f for f in fulls
            if f.count('/') == 1 and not isinstance(known.get(f, {}).get('star'), int)]
    print(f'[reg-stars] 登记轨仓库待补星 {len(todo)} 个（登记链接 {len(fulls)}）')
    n = 0
    for i in range(0, len(todo), BATCH):
        res = fetch_stars(todo[i:i + BATCH])
        for full, stars in res.items():
            if isinstance(stars, int):
                known[full] = {'status': 'found', 'full_name': full, 'star': stars, 'src': 'registry'}
                n += 1
        if res:
            print(f'  {min(i + BATCH, len(todo))}/{len(todo)}', flush=True)
        time.sleep(2)
    print(f'[reg-stars] 回填 {n} 条（locate-cache full_name 键）')


def main():
    cache = {'resolved_at': '', 'entries': {}}
    if CACHE.exists():
        try:
            cache = json.loads(CACHE.read_text())
        except json.JSONDecodeError:
            pass
    known = cache['entries']

    names = [n for n in placeholder_names()
             if n not in known or known[n].get('status') == 'error'
             or (known[n].get('status') == 'found' and not isinstance(known[n].get('star'), int))]
    print(f'[resolve] 待复核/补星 {len(names)} 个（缓存已有 {len(known)}）')

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
    reg_star_backfill(known)
    cache['resolved_at'] = time.strftime('%Y-%m-%d')
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0))

    audit_urls(known)
    from collections import Counter
    sc = Counter(v['status'] for v in known.values())
    print(f'[resolve] 缓存合计 {len(known)}：{dict(sc)}（失败 {len(failed)} 可重跑）')


if __name__ == '__main__':
    main()
