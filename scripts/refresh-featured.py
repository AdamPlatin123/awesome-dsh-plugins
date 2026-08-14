#!/usr/bin/env python3
"""刷新 README 星标榜（Star Top 20）。

候选池 = README.md / README.en-US.md / PLUGINS.md 的 GitHub 引用 + catalog/plugins/*.json。
逐仓库 REST 查询（跟随改名重定向），剔除私有/已删除/非插件后按 star 排序取前 20，
重写两份 README 的 AUTO:featured 块。星数不足 20 或候选过少时中止（不写半成品榜单）。

依赖：环境变量 GH_TOKEN（GitHub token，读公开仓库 + 推送）；curl；python3。
用法：GH_TOKEN=... python3 scripts/refresh-featured.py [--dry]
"""
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = '--dry' in sys.argv
TOP_N = 20
MIN_CANDIDATES = 120  # 候选池低于此值视为数据异常，中止
REFRESH_LABEL = '每 20 分钟自动刷新'

# 非插件类仓库不进插件星标榜（社区网站 / 市场网站 / 本仓库自身）
EXCLUDE = {
    'hikariming/dshfind',
    'bradeGithub/DSH-Plugins-Marketplace',
    'AdamPlatin123/awesome-dsh-plugins',
    'dsh-external/awesome-dsh-plugins',
}

TOKEN = os.environ.get('GH_TOKEN') or subprocess.run(
    ['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
if not TOKEN:
    sys.exit('[错误] 缺少 GH_TOKEN（且 gh auth token 不可用）')


def collect_candidates():
    repos = set()
    for name in ['README.md', 'README.en-US.md', 'PLUGINS.md']:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            continue
        text = open(path, encoding='utf-8').read()
        for m in re.finditer(r'https://github\.com/([^\s\)\]"]+)', text):
            parts = m.group(1).split('/')
            if len(parts) >= 2 and parts[0] not in ('features', 'actions', 'topics', 'about'):
                repos.add('/'.join(parts[:2]))
    for entry in sorted(os.listdir(os.path.join(ROOT, 'catalog', 'plugins'))):
        if entry.endswith('.json'):
            d = json.load(open(os.path.join(ROOT, 'catalog', 'plugins', entry), encoding='utf-8'))
            full = d.get('repository', {}).get('full_name', '')
            if full.count('/') == 1:
                repos.add(full)
    return repos - EXCLUDE


def fetch(repo):
    """REST 查询单个仓库；跟随改名，返回 canonical full_name/star/描述，不可达返回 None。"""
    for attempt in range(2):
        p = subprocess.run(
            ['curl', '-sL', '--max-time', '25',
             '-H', f'Authorization: Bearer {TOKEN}',
             '-H', 'Accept: application/vnd.github+json',
             f'https://api.github.com/repos/{repo}'],
            capture_output=True, text=True)
        try:
            d = json.loads(p.stdout)
        except Exception:
            time.sleep(1)
            continue
        if 'id' in d and 'full_name' in d:
            if d.get('private') or d.get('archived'):
                return None
            return d['full_name'], d.get('stargazers_count', 0), (d.get('description') or '').strip()
        if d.get('message') == 'Not Found':
            return None
        time.sleep(1)
    return 'RETRY_FAIL', repo, ''


def main():
    candidates = collect_candidates()
    print(f'[candidates] {len(candidates)} 个')
    if len(candidates) < MIN_CANDIDATES:
        sys.exit(f'[中止] 候选 {len(candidates)} < {MIN_CANDIDATES}，疑似引用解析异常')

    with ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(fetch, sorted(candidates)))
    stats = {}
    failures = []
    for r in results:
        if r is None:
            continue
        if r[0] == 'RETRY_FAIL':
            failures.append(r[1])
            continue
        stats[r[0]] = {'stars': r[1], 'desc': r[2]}
    print(f'[fetch] 可达 {len(stats)}，不可达(私有/删除) {len(results) - len(stats) - len(failures)}，网络失败 {len(failures)}')
    if len(stats) < MIN_CANDIDATES:
        sys.exit(f'[中止] 可达仓库 {len(stats)} < {MIN_CANDIDATES}，疑似 API 异常')
    if failures:
        sys.exit(f'[中止] 网络失败 {len(failures)} 个: {failures[:5]}')

    top = sorted(stats.items(), key=lambda kv: (-kv[1]['stars'], kv[0]))[:TOP_N]
    if len(top) < TOP_N:
        sys.exit(f'[中止] 有效条目 {len(top)} < {TOP_N}')

    ts = time.strftime('%Y-%m-%d %H:%M')
    rows = []
    for i, (repo, v) in enumerate(top, 1):
        name = repo.split('/')[1]
        desc = v['desc'].replace('|', '\\|')
        if len(desc) > 55:
            desc = desc[:55] + '…'
        rows.append(f'| {i} | [{name}](https://github.com/{repo}) | {v["stars"]} | {desc} |')
    block = ('<!-- AUTO:featured:START -->\n\n'
             f'> 按 GitHub star 数排序，{REFRESH_LABEL}。数据截至 {ts}。\n\n'
             '| # | 插件 | ⭐ | 说明 |\n|---|---|---|---|\n'
             + '\n'.join(rows) + '\n\n<!-- AUTO:featured:END -->')

    changed = False
    for name in ['README.md', 'README.en-US.md']:
        path = os.path.join(ROOT, name)
        text = open(path, encoding='utf-8').read()
        new = re.sub(r'<!-- AUTO:featured:START -->[\s\S]*?<!-- AUTO:featured:END -->',
                     lambda _: block, text, count=1)
        if new != text:
            if not DRY:
                open(path, 'w', encoding='utf-8').write(new)
            changed = True
            print(f'[write] {name}')
    if not changed:
        print('[noop] 榜单无变化')
    print(f'[done] Top1 {top[0][0]} {top[0][1]["stars"]}⭐')


if __name__ == '__main__':
    main()
