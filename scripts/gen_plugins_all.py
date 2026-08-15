#!/usr/bin/env python3
"""gen-plugins-all.py — 全量插件清单生成器（PLUGINS-ALL.md）。

数据：data/snapshots/ 全部快照按 run_id 新→旧合并（同键以最新轮为准）⊕ data/locate-cache.json 定位复核。
呈现：分组列表（文字标签状态 · 名称 ★ · 一句话说明），零表格；监测中条目不显示对错判定。
被 render-readme-from-snapshot.py 每轮渲染调用；也可独立运行。
"""
import glob
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'PLUGINS-ALL.md'
LOCATE_CACHE = ROOT / 'data' / 'locate-cache.json'

MARK = {'✅ 运行级可用': '`[可用]`', '❌ 运行级不兼容': '`[不兼容]`',
        '⚠️ 待定': '`[待定]`', '⏳ 未测': '`[未测]`'}
DOMAIN_ORDER = ['🔌 Web UI 增强', '🤖 Agent 能力', '💻 编码开发', '📡 消息通讯', '🗂 文件数据',
                '🎮 娱乐生活', '🛠 基建部署', '📚 学习研究', '❓ 其他']


def bj(iso):
    return (datetime.fromisoformat(str(iso).replace('Z', '+00:00')) + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M') + ' UTC+8'


def load_snapshots():
    """全部快照新→旧；同名+URL 同键以最新轮覆盖。返回 (合并条目, [轮次信息])。"""
    files = sorted(glob.glob(str(ROOT / 'data' / 'snapshots' / '*.json')), reverse=True)
    merged, rounds = {}, []
    for fp in files:
        try:
            d = json.loads(Path(fp).read_text())
        except json.JSONDecodeError:
            continue
        if not str(d.get('schema', '')).startswith('radar-snapshot/'):
            continue
        rounds.append((d['run_id'], d.get('generated_at', '')))
        for e in d.get('catalog_entries') or []:
            merged.setdefault((e['name'], e.get('url', '')), dict(e))
    return list(merged.values()), rounds


def pr_registered_names():
    names = set()
    for fp in glob.glob(str(ROOT / 'catalog' / 'plugins' / '*.json')):
        d = json.loads(Path(fp).read_text())
        full = d.get('repository', {}).get('full_name', '')
        if full:
            names.add(full.split('/')[-1])
    return names


def main():
    entries, rounds = load_snapshots()
    locate = json.loads(LOCATE_CACHE.read_text()).get('entries', {}) if LOCATE_CACHE.exists() else {}
    pr_names = pr_registered_names()

    n_fix = n_empty = n_amb = n_unresolved = 0
    for e in entries:
        if 'search?q=' in (e.get('url') or ''):
            r = locate.get(e['name'], {})
            if r.get('status') == 'found':
                e['url'] = f"https://github.com/{r['full_name']}"
                e['locate'] = 'located'
                n_fix += 1
            elif r.get('status') == 'not_found':
                e['locate'] = 'empty_watch'
                n_empty += 1
            elif r.get('status'):
                e['locate'] = 'ambiguous_watch'
                n_amb += 1
            else:
                e['locate'] = 'unresolved'   # 新占位且无复核缓存
                n_unresolved += 1
        else:
            e['locate'] = 'located'

    vc = Counter(e['verdict'] for e in entries if e['locate'] == 'located')
    src = ' ⊕ '.join(f'`{rid}` {bj(ts)}' for rid, ts in rounds[:3])
    if len(rounds) > 3:
        src += f' 等 {len(rounds)} 轮'

    L = []
    L.append('# 全量插件清单（统一四档口径）')
    L.append('')
    L.append(f'> 数据源：radar 快照并集（{src}）⊕ GitHub 定位复核缓存（data/locate-cache.json）。')
    L.append('> 呈现：分组列表（状态 · 名称 ★ · 一句话说明），不使用大表格。')
    L.append('')
    L.append('## 统一度量衡')
    L.append('')
    L.append(f'**判定维度**（运行级四档，仅已定位条目 {sum(vc.values())} 个进入统计；测试：dsh 容器 agent + Qwen3.6-35B · k8s 5 分片 · run_id 锚定轮次）：')
    L.append('')
    L.append(f'- `[可用]`（{vc.get("✅ 运行级可用", 0)}）/ `[不兼容]`（{vc.get("❌ 运行级不兼容", 0)}）/ `[待定]`（{vc.get("⚠️ 待定", 0)}）/ `[未测]`（{vc.get("⏳ 未测", 0)}）')
    L.append('')
    L.append('**定位维度**（与判定正交；监测类不显示对错判定，原始结果保留于快照层）：')
    L.append('')
    L.append(f'- `[空仓监测]`（{n_empty}）— GitHub 复核无此仓库；待重现后恢复判定显示')
    L.append(f'- `[歧义监测]`（{n_amb}）— 同名多仓无法锁定本体；锁定前不展示')
    if n_unresolved:
        L.append(f'- `[未定位]`（{n_unresolved}）— 新占位条目，待下一轮定位复核（scripts/resolve_placeholders.py）')
    L.append(f'- 定位复核累计修复 {n_fix} 个占位 URL')
    L.append('')
    L.append('> 〔PR〕= 经已合并 PR 正式登记；收录 ≠ 兼容 ≠ 运行可用 ≠ 安全审计。')
    L.append('')
    L.append(f'## 汇总：{len(entries)} 条（已定位 {sum(vc.values())} · 监测/未定位 {len(entries) - sum(vc.values())}）· PR 登记 {len(pr_names)} 个')
    L.append('')

    for dom in DOMAIN_ORDER:
        group = sorted([e for e in entries if e.get('domain') == dom], key=lambda x: -(x.get('star') or 0))
        if not group:
            continue
        L.append(f'## {dom}（{len(group)}）')
        L.append('')
        for e in group:
            name, star = e['name'], e.get('star') or 0
            desc = (e.get('desc') or '—').strip()
            if desc.startswith('http'):
                desc = '—'
            pr = ' 〔PR〕' if name in pr_names else ''
            loc = e.get('locate')
            if loc == 'empty_watch':
                L.append(f'- `[空仓监测]` **{name}** — GitHub 无此仓库，判定暂不展示{pr}')
            elif loc == 'ambiguous_watch':
                L.append(f'- `[歧义监测]` **{name}** — 同名多仓，判定暂不展示{pr}')
            elif loc == 'unresolved':
                L.append(f'- `[未定位]` **{name}** — 占位待复核，判定暂不展示{pr}')
            else:
                L.append(f'- {MARK.get(e.get("verdict"), "`[未测]`")} [{name}]({e["url"]}) ★{star} — {desc}{pr}')
        L.append('')

    L.append('## 附录')
    L.append('')
    L.append('- 判定与定位正交；监测类条目的原始判定保留于 data/snapshots/，定位成功后自动恢复展示。')
    L.append('- 占位 URL 由发现管线 clone 库通道产生；定位复核：`python3 scripts/resolve_placeholders.py`（结果写 data/locate-cache.json）。')
    L.append('- 同名覆盖与 URL 占位为快照原生限制，主键以 GitHub repo id 为准。')
    L.append('')

    OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'[gen-plugins-all] {len(entries)} 条 → {OUT.name}（定位修复 {n_fix} / 空仓 {n_empty} / 歧义 {n_amb} / 未定位 {n_unresolved}）')
    # 汇总卡数据（供 render 的目录摘要用）：返回每类分布
    return {dom: {'total': sum(1 for e in entries if e.get('domain') == dom),
                  'ok': vc_local(entries, dom, '✅ 运行级可用'),
                  'bad': vc_local(entries, dom, '❌ 运行级不兼容'),
                  'inc': vc_local(entries, dom, '⚠️ 待定'),
                  'un': vc_local(entries, dom, '⏳ 未测'),
                  'watch': sum(1 for e in entries if e.get('domain') == dom and e.get('locate') != 'located')}
            for dom in DOMAIN_ORDER}


def vc_local(entries, dom, verdict):
    return sum(1 for e in entries if e.get('domain') == dom and e.get('locate') == 'located' and e.get('verdict') == verdict)


if __name__ == '__main__':
    main()
