#!/usr/bin/env python3
"""每日全量刷新 PLUGINS-ALL.md 行内星数。

候选 = PLUGINS-ALL.md 全部 GitHub 引用；GraphQL 每 50 仓一批查 stargazerCount
（REST 逐仓会超 GITHUB_TOKEN 每小时限额）。仅改写行内星数数字，其余文本不动；
查不到（私有/删除/改名）的条目保留原值。成功解析低于候选半数时中止（防
token 失效产生大面积误写）。

依赖：环境变量 GH_TOKEN；curl；python3。
用法：GH_TOKEN=... python3 scripts/refresh-stars.py [--dry]
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = '--dry' in sys.argv
TARGET = os.path.join(ROOT, 'PLUGINS-ALL.md')
BATCH = 50
MIN_RESOLVE_RATIO = 0.5  # 解析成功率守门

TOKEN = os.environ.get('GH_TOKEN') or subprocess.run(
    ['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
if not TOKEN:
    sys.exit('[错误] 缺少 GH_TOKEN（且 gh auth token 不可用）')

# 行内格式：[name](https://github.com/owner/repo) 123 — desc（星数可空，空则跳过不改）
LINE_RE = re.compile(
    r'(\[([^\]]+)\]\(https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)\)) (\d+)( —)')


def gql_batch(repos):
    """一批 GraphQL 查询：{o}/{n} -> stargazerCount；返回 {full_name_lower: stars}。"""
    parts = []
    for i, (o, n) in enumerate(repos):
        parts.append(
            f'r{i}: repository(owner:"{o}",name:"{n}")'
            '{ stargazerCount }')
    query = '{ ' + ' '.join(parts) + ' }'
    p = subprocess.run(
        ['curl', '-sL', '--max-time', '30',
         '-H', f'Authorization: Bearer {TOKEN}',
         '-H', 'Content-Type: application/json',
         '-d', json.dumps({'query': query}),
         'https://api.github.com/graphql'],
        capture_output=True, text=True)
    try:
        data = json.loads(p.stdout)
    except Exception:
        return {}
    out = {}
    for i, (o, n) in enumerate(repos):
        node = (data.get('data') or {}).get(f'r{i}')
        if node is not None:
            out[f'{o}/{n}'.lower()] = node.get('stargazerCount')
    return out


def main():
    text = open(TARGET, encoding='utf-8').read()
    entries = []  # (owner, name)
    seen = set()
    for m in LINE_RE.finditer(text):
        key = (m.group(3), m.group(4))
        if key not in seen:
            seen.add(key)
            entries.append(key)
    if not entries:
        sys.exit('[错误] PLUGINS-ALL.md 未解析到任何带星数的条目')

    stars = {}
    for i in range(0, len(entries), BATCH):
        stars.update(gql_batch(entries[i:i + BATCH]))
    resolved = sum(1 for o, n in entries if f'{o}/{n}'.lower() in stars)
    if resolved < len(entries) * MIN_RESOLVE_RATIO:
        sys.exit(f'[中止] GraphQL 解析率过低：{resolved}/{len(entries)}')

    changed = [0]

    def sub(m):
        key = f'{m.group(3)}/{m.group(4)}'.lower()
        if key in stars and stars[key] != int(m.group(5)):
            changed[0] += 1
            return f'{m.group(1)} {stars[key]}{m.group(6)}'
        return m.group(0)

    new_text = LINE_RE.sub(sub, text)
    print(f'[stars] 候选 {len(entries)} | 解析 {resolved} | 星数变化 {changed[0]}')
    if changed[0] == 0 or DRY:
        return
    open(TARGET, 'w', encoding='utf-8').write(new_text)


if __name__ == '__main__':
    main()
