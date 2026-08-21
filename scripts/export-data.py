#!/usr/bin/env python3
"""export-data.py — 稳定数据接口导出（issue #252）。

从 PLUGINS-ALL.md 单一事实源导出两个稳定 JSON 清单，供第三方（插件市场等）消费：
  - data/latest.json      快照指针 + 四档统计（小、可高频轮询）
  - data/plugins-all.json 全量扁平清单（repo/verdict/stars/desc）

口径承诺（schema dsh-radar/v1）：字段只增不删；stars 为 null 表示未知（不参与排序的
缺值，非 0）；verdict ∈ ok / incompatible / pending / untested / gone / ambiguous /
empty-monitor（与 PLUGINS-ALL 判定档位一一对应）。

用法：python3 scripts/export-data.py <repo-root>   （渲染链每次提交后调用）
"""
import json
import re
import sys
import time
from pathlib import Path

SCHEMA = 'dsh-radar/v1'
VERDICT_MAP = {
    '可用': 'ok', '不兼容': 'incompatible', '待定': 'pending', '未测': 'untested',
    '空仓监测': 'gone', '歧义监测': 'ambiguous', '未定位': 'unlocated',
}
# - `[可用]` [name](url) 31 — desc   （desc 可为空：行尾为 " —" 或无 " —"）
ROW_RE = re.compile(
    r'^- `\[([^\]]+)\]` \[([^\]]+)\]\((https://github\.com/[^\s)]+)\)(?: (\d+))?(?: — ?(.*))?$')
STAT_RE = re.compile(r'`\[([^\]]+)\]`（(\d+)）')
ANCHOR_RE = re.compile(r'`(\d{8}T\d{6}Z)`')


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    text = (root / 'PLUGINS-ALL.md').read_text(encoding='utf8')
    generated_at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())

    stats = {VERDICT_MAP[k]: int(v) for k, v in STAT_RE.findall(text)}
    anchor = ANCHOR_RE.search(text)

    plugins = []
    for line in text.splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        verdict_cn, name, url, stars, desc = m.groups()
        plugins.append({
            'repo': url.split('github.com/')[1],
            'name': name,
            'verdict': VERDICT_MAP.get(verdict_cn, verdict_cn),
            'stars': int(stars) if stars else None,
            'desc': (desc or '').strip(),
        })

    latest = {
        'schema': SCHEMA,
        'generated_at': generated_at,
        'snapshot_run_id': anchor.group(1) if anchor else None,
        'stats': stats,
        'total_listed': len(plugins),
        'data': {
            'plugins_all': 'data/plugins-all.json',
            'snapshots_dir': 'data/snapshots/',
        },
    }
    (root / 'data').mkdir(exist_ok=True)
    (root / 'data' / 'latest.json').write_text(
        json.dumps(latest, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    (root / 'data' / 'plugins-all.json').write_text(
        json.dumps({'schema': SCHEMA, 'generated_at': generated_at, 'plugins': plugins},
                   ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(f'[export] latest.json 统计={stats}｜plugins-all.json {len(plugins)} 条')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
