#!/usr/bin/env python3
"""刷新 README 精选插件榜（Featured Top 50，人工策展 + 自动刷新星标）。

成员与分类来自 data/awesome-50.json（人工策展，本脚本只读不改成员）；
逐仓库 REST 查询星标（跟随改名重定向），按 JSON 的 11 类顺序渲染分类表格，
重写两份 README 的 AUTO:featured 块。任一策展成员不可达或查询失败即中止
（成员是固定名单，消失/失联是异常信号，不写半截榜单）。

依赖：环境变量 GH_TOKEN（GitHub token，读公开仓库）；curl；python3。
用法：GH_TOKEN=... python3 scripts/refresh-featured.py [--dry]
"""
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = '--dry' in sys.argv
CURATED = os.path.join(ROOT, 'data', 'awesome-50.json')
REFRESH_LABEL = '每 6 小时自动刷新'
VERDICT_MARK = {'ok': '✅', 'pending': '待定', 'incompatible': '需适配', 'untested': '未测', None: '—'}

TOKEN = os.environ.get('GH_TOKEN') or subprocess.run(
    ['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
if not TOKEN:
    sys.exit('[错误] 缺少 GH_TOKEN（且 gh auth token 不可用）')


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
    data = json.load(open(CURATED, encoding='utf-8'))
    cats = data['categories']
    repos = [p['repo'] for c in cats for p in c['plugins']]
    # 成员数随实测口径动态变化（rc.8 重测通过者）；下限防 JSON 误删，去重防误加
    if len(repos) < 20:
        sys.exit(f'[中止] 策展成员仅 {len(repos)} 个（<20），疑似 JSON 损坏，需人工校对')
    if len(set(repos)) != len(repos):
        sys.exit('[中止] 策展成员存在重复仓库，JSON 需人工校对')

    with ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(fetch, repos))
    stars, fails = {}, []
    for repo, r in zip(repos, results):
        if r is None:
            fails.append(f'{repo}(不可达/私有/归档)')
        elif r[0] == 'RETRY_FAIL':
            fails.append(f'{repo}(网络失败)')
        else:
            stars[repo] = r[1]
    print(f'[fetch] 成功 {len(stars)}/50')
    if fails:
        sys.exit(f'[中止] 策展成员查询失败 {len(fails)} 个: {fails[:5]}')

    ts = datetime.now(ZoneInfo('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')
    total = sum(len(c['plugins']) for c in cats)
    parts = [
        '<!-- AUTO:featured:START -->', '',
        f'> 人工策展 {total} 款 rc.8 实测可用插件（v4flash 全量重测通过者，2026-08-21），类序与类内均按星标降序；'
        f'星标{REFRESH_LABEL}（成员调整请提 PR 修改 data/awesome-50.json）。数据截至 {ts}（UTC+8）。',
        '',
    ]
    for c in cats:
        ranked = sorted(c['plugins'], key=lambda p: (-stars[p['repo']], p['repo'].lower()))
        parts.append(f"### {c['name']}（{len(ranked)}）")
        parts.append('')
        parts.append('| 插件 | ⭐ | 实测 | 说明 |')
        parts.append('|---|---:|---|---|')
        for p in ranked:
            desc = p['desc'].replace('|', '\\|')
            parts.append(f"| [{p['name']}](https://github.com/{p['repo']}) | {stars[p['repo']]} |"
                         f" {VERDICT_MARK.get(p.get('verdict'), '—')} | {desc} |")
        parts.append('')
    parts.append('> 实测 = rc.8 + v4flash 标准安装与单任务验证（2026-08-21 对 50 仓全量重测，仅收录通过者；逐仓日志见 data/rc8-retest-20260821/）；雷达 k8s 历史判定见 [PLUGINS-ALL.md](PLUGINS-ALL.md)；安装第三方插件前请审查源码并固定 commit。')
    block = '\n'.join(parts) + '\n\n<!-- AUTO:featured:END -->'

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
    top = max(repos, key=lambda r: stars[r])
    print(f'[done] 11 类 50 个 · 最高星 {top} {stars[top]}⭐')


if __name__ == '__main__':
    main()
