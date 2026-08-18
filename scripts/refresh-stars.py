#!/usr/bin/env python3
"""每日全量刷新 PLUGINS-ALL.md 行内星数。

候选 = PLUGINS-ALL.md 全部 GitHub 引用（列表行含无数字兜底行 + 兼容旧表格行）；GraphQL 每 50 仓一批查 stargazerCount
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

# 列表行格式（PLUGINS-ALL 现行统一口径）：- `[判定]` [name](url) 123 — desc
# 数字段可省（星数未知——登记兜底行渲染留空）：缺数字时首次刷新补入，此后与普通行同刷。
# 分组：1=前缀 2=owner 3=repo 4=可选数字 5=尾部（—）
LIST_RE = re.compile(
    r'- `\[([^\]]+)\]` \[([^\]]+)\]\(https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)\)[ \t]*'
    r'(?:(\d+)[ \t]*)?(—)')
# 兼容旧表格行：| [name](url) | 123 |（分组：1=前缀 3=owner 4=repo 5=数字 6=尾部）
TABLE_RE = re.compile(
    r'(\|[ \t]*\[([^\]]+)\]\(https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)\)[ \t]*\|[ \t]*)'
    r'(\d+)([ \t]*\|)')


GQL_RENAMES = {}   # GraphQL 名实不符的改名映射（请求名lower → 解析出的新全名）


def gql_batch(repos):
    """一批 GraphQL 查询：{o}/{n} -> stargazerCount；返回 {full_name_lower: stars}。"""
    parts = []
    for i, (o, n) in enumerate(repos):
        parts.append(
            f'r{i}: repository(owner:"{o}",name:"{n}")'
            '{ stargazerCount nameWithOwner }')
    query = '{ ' + ' '.join(parts) + ' }'
    data = None
    for _attempt in (1, 2):  # 代理下批量查询偶发整批失败：重试一次
        p = subprocess.run(
            ['curl', '-sL', '--max-time', '30',
             '-H', f'Authorization: Bearer {TOKEN}',
             '-H', 'Content-Type: application/json',
             '-d', json.dumps({'query': query}),
             'https://api.github.com/graphql'],
            capture_output=True, text=True)
        try:
            payload = json.loads(p.stdout)
            data = payload.get('data') or {}
            if data:
                break
            if payload.get('errors'):
                print('[gql-diag] errors:', str(payload['errors'])[:300], file=sys.stderr)
            elif not p.stdout.strip():
                print(f'[gql-diag] empty stdout, curl rc={p.returncode}', file=sys.stderr)
        except Exception as exc:
            print(f'[gql-diag] parse fail: {exc}; rc={p.returncode}; body[:200]={p.stdout[:200]}', file=sys.stderr)
            data = None
    if data is None:
        return {}
    out = {}
    for i, (o, n) in enumerate(repos):
        node = data.get(f'r{i}')
        if node is not None:
            key = f'{o}/{n}'.lower()
            out[key] = node.get('stargazerCount')
            full = (node.get('nameWithOwner') or '').strip()
            if full and full.lower() != key:
                GQL_RENAMES[key] = full   # GraphQL 解析名与请求名不符 = 已改名
    return out


def main():
    text = open(TARGET, encoding='utf-8').read()
    entries = []  # (owner, name)
    seen = set()
    for m in LIST_RE.finditer(text):
        key = (m.group(3), m.group(4))
        if key not in seen:
            seen.add(key)
            entries.append(key)
    for m in TABLE_RE.finditer(text):
        key = (m.group(3), m.group(4))
        if key not in seen:
            seen.add(key)
            entries.append(key)
    if not entries:
        sys.exit('[错误] PLUGINS-ALL.md 未解析到任何条目')

    stars = {}
    for i in range(0, len(entries), BATCH):
        stars.update(gql_batch(entries[i:i + BATCH]))

    # REST 301 回退（改名仓）：GraphQL repository(owner,name) 对旧名返回 null（不跟 301）；
    # REST /repos/<old> 跟随重定向取新 full_name + stargazers_count——补星数并记改名映射
    renames = {}
    for o, n in [(o, n) for o, n in entries if f'{o}/{n}'.lower() not in stars]:
        p = subprocess.run(['curl', '-sL', '--max-time', '15',
                            '-H', f'Authorization: Bearer {TOKEN}',
                            f'https://api.github.com/repos/{o}/{n}'],
                           capture_output=True, text=True)
        try:
            d = json.loads(p.stdout)
        except Exception:
            continue
        full, sc = d.get('full_name'), d.get('stargazers_count')
        if not full or not isinstance(sc, int):
            continue
        key = f'{o}/{n}'.lower()
        stars[key] = sc
        if full.lower() != key:
            renames[key] = full
    renames.update(GQL_RENAMES)   # GraphQL 侧捕获的改名并入（REST 回退仅兜 null 场景）
    if renames:
        print(f'[stars] REST 回退改名仓 {len(renames)} 个：' +
              ', '.join(f'{k} → {v}' for k, v in list(renames.items())[:5]))

    resolved = sum(1 for o, n in entries if f'{o}/{n}'.lower() in stars)
    if resolved < len(entries) * MIN_RESOLVE_RATIO:
        sys.exit(f'[中止] GraphQL 解析率过低：{resolved}/{len(entries)}')

    changed = [0]

    def sub_list(m):
        # 分组：1=判定 2=名称 3=owner 4=repo 5=可选数字 6=—
        key = f'{m.group(3)}/{m.group(4)}'.lower()
        cur = int(m.group(5)) if m.group(5) is not None else None
        if key not in stars:
            return m.group(0)
        if key in renames:
            full = renames[key]
            o2, n2 = full.split('/')
            name = n2 if m.group(2).lower() == m.group(4).lower() else m.group(2)
            changed[0] += 1
            return f'- `[{m.group(1)}]` [{name}](https://github.com/{full}) {stars[key]} {m.group(6)}'
        if stars[key] != cur:
            changed[0] += 1
            return f'- `[{m.group(1)}]` [{m.group(2)}](https://github.com/{m.group(3)}/{m.group(4)}) {stars[key]} {m.group(6)}'
        return m.group(0)

    def sub_table(m):
        key = f'{m.group(3)}/{m.group(4)}'.lower()
        if key in stars and stars[key] != int(m.group(5)):
            changed[0] += 1
            return f'{m.group(1)}{stars[key]}{m.group(6)}'
        return m.group(0)

    new_text = LIST_RE.sub(sub_list, text)
    new_text = TABLE_RE.sub(sub_table, new_text)
    print(f'[stars] 候选 {len(entries)} | 解析 {resolved} | 星数变化 {changed[0]}')
    if changed[0] == 0 or DRY:
        return
    open(TARGET, 'w', encoding='utf-8').write(new_text)


if __name__ == '__main__':
    main()
