#!/usr/bin/env python3
"""gen-plugins-all.py — 全量插件清单生成器（PLUGINS-ALL.md）。

数据：data/snapshots/ 全部快照按 run_id 新→旧合并 ⊕ data/repo-map.json（v2 local_key → 真实仓库）
⊕ data/locate-cache.json 定位复核（含实时 star）⊕ PLUGINS.md 登记表兜底（登记轨 ⊕ 快照轨并集：
登记有而快照无的仓补 [未测] 行，API 判消亡的进空仓监测——#189）。
合并主键以 GitHub 仓库全名（repo-map / 真实 URL / locate-cache 三源归一）为准，同一仓库的
v1 键（纯仓库名）与 v2 键（owner-repo local_key）合并为单条：URL 取真实值、star 取最大/实时值、
判定冲突（如 v1 vs v2）降级为 [待定] 并记录冲突详情；展示名优先纯仓库名。
呈现：分组列表（文字标签状态 · 名称  · 一句话说明），零表格；监测中条目不显示对错判定。
被 render-readme-from-snapshot.py 每轮渲染调用；也可独立运行。
"""
import glob
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'PLUGINS-ALL.md'
LOCATE_CACHE = ROOT / 'data' / 'locate-cache.json'
DESC_CACHE = ROOT / 'data' / 'desc-cache.json'
REPO_MAP = ROOT / 'data' / 'repo-map.json'
URL_AUDIT = ROOT / 'data' / 'url-audit.json'

REAL_URL_RE = re.compile(r'github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)')
# 互斥判定（✅/❌ 矛盾才降待定；待定/未测属非结论性，不参与冲突）
CONFLICTING_VERDICTS = ('✅ 运行级可用', '❌ 运行级不兼容')

# 四档文本标记（机器可解析——export-data.py 的 dsh-radar/v1 稳定接口依赖此格式，勿改图形标记）
MARK = {'✅ 运行级可用': '🟩 `[可用]`', '❌ 运行级不兼容': '🟨 `[不兼容]`',
        '⚠️ 待定': '⬜ `[待定]`', '⏳ 未测': '⬜ `[未测]`'}
DOMAIN_ORDER = ['🎓 技能包', '🧠 记忆增强', '🎨 主题皮肤', '🛒 市场与管理',
                '🔌 Web UI 增强', '💻 编码开发', '🤖 Agent 能力', '📡 消息通讯',
                '🗂 文件数据', '🎮 娱乐生活', '🛠 基建部署', '📚 学习研究', '❓ 其他']

try:
    from classify import classify
except ImportError:
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from classify import classify


def bj(iso):
    """ISO 时间串 → 北京时间（UTC+8）；带时区偏移的输入按原偏移换算，避免二次加 8。"""
    dt = datetime.fromisoformat(str(iso).replace('Z', '+00:00'))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M') + ' UTC+8'


def load_snapshots():
    """全部快照新→旧；同名+URL 同键以最新轮覆盖。返回 (合并条目, [轮次信息])。"""
    files = sorted(glob.glob(str(ROOT / 'data' / 'snapshots' / '*.json')), reverse=True)
    merged, rounds = {}, []
    for fp in files:
        try:
            d = json.loads(Path(fp).read_text())
        except (json.JSONDecodeError, UnicodeDecodeError, OSError):
            continue   # 单文件截断/损坏跳过（镜像仓实测案例），不阻断清单生成
        if not str(d.get('schema', '')).startswith('radar-snapshot/'):
            continue
        rounds.append((d['run_id'], d.get('generated_at', '')))
        for e in d.get('catalog_entries') or []:
            merged.setdefault((e['name'], e.get('url', '')), dict(e))
    return list(merged.values()), rounds


def canonical_key(e, repo_map, locate):
    """条目 → 规范主键。真实 URL > repo-map local_key > locate-cache；均无则退回原始键。"""
    url = e.get('url') or ''
    if 'search?q=' not in url:
        m = REAL_URL_RE.search(url)
        if m:
            return ('repo', f"{m.group(1)}/{m.group(2)}".lower())
    name = e['name']
    r = repo_map.get(name)
    if r and r.get('full_name'):
        return ('repo', r['full_name'].lower())
    lc = locate.get(name) or {}
    if lc.get('status') == 'found' and lc.get('full_name'):
        return ('repo', lc['full_name'].lower())
    return ('raw', name.lower(), url)


def _ok_desc(d):
    d = (d or '').strip()
    return bool(d) and d != '—' and not d.startswith('http')


def merge_entry(a, b):
    """同 canonical 的更旧轮次 b 补齐/仲裁 a：URL 取真实、star 取大、desc 取有效、判定冲突降待定。"""
    out = dict(a)
    if 'search?q=' in (out.get('url') or '') and 'search?q=' not in (b.get('url') or ''):
        out['url'] = b['url']
    if (out.get('star') or 0) < (b.get('star') or 0):
        out['star'] = b['star']
    if not out.get('bundle') and b.get('bundle'):
        out['bundle'] = b['bundle']
    if not _ok_desc(out.get('desc')) and _ok_desc(b.get('desc')):
        out['desc'] = b['desc']
    if not out.get('domain') and b.get('domain'):
        out['domain'] = b['domain']
    va, vb = out.get('verdict'), b.get('verdict')
    if va != vb:
        if vb in CONFLICTING_VERDICTS and va not in CONFLICTING_VERDICTS:
            out['verdict'] = vb
        elif va in CONFLICTING_VERDICTS and vb not in CONFLICTING_VERDICTS:
            pass
        elif va in CONFLICTING_VERDICTS and vb in CONFLICTING_VERDICTS:
            out['verdict'] = '⚠️ 待定'
            out['verdict_conflict'] = f'{va} ↔ {vb}'
    return out


def canonical_merge(entries, repo_map, locate):
    """按 canonical 主键归并（load_snapshots 产出的条目序近似新→旧）。返回 (归并条目, 统计)。"""
    groups, order, plain = {}, [], {}
    for e in entries:
        k = canonical_key(e, repo_map, locate)
        if k not in groups:
            groups[k] = dict(e)
            order.append(k)
        else:
            groups[k] = merge_entry(groups[k], e)
        if k[0] == 'repo':
            repo_part = k[1].split('/')[1]
            if e['name'].lower() == repo_part:
                plain.setdefault(k, e['name'])
    final = []
    for k in order:
        g = groups[k]
        if k in plain:
            g['name'] = plain[k]
        final.append(g)
    n_dedup = len(entries) - len(final)
    n_conflict = sum(1 for g in final if g.get('verdict_conflict'))
    return final, (n_dedup, n_conflict)


def pr_registered_names():
    names = set()
    for fp in glob.glob(str(ROOT / 'catalog' / 'plugins' / '*.json')):
        d = _read_json_safe(fp, None)
        if not isinstance(d, dict):
            continue
        full = d.get('repository', {}).get('full_name', '')
        if full:
            names.add(full.split('/')[-1])
    return names


def _read_json_safe(p, default):
    """缓存文件损坏（截断/无效 UTF-8/坏 JSON）时降级返回默认值，不阻断清单生成。"""
    try:
        return json.loads(Path(p).read_text())
    except (json.JSONDecodeError, UnicodeDecodeError, OSError):
        return default


def main():
    radar_ver = ''
    try:
        import tile_assets
        tile_assets.write_tiles()
        radar_ver = tile_assets.current_version()
    except Exception:
        pass
    entries, rounds = load_snapshots()
    locate = (_read_json_safe(LOCATE_CACHE, {}) or {}).get('entries', {}) if LOCATE_CACHE.exists() else {}
    repo_map = (_read_json_safe(REPO_MAP, {}) or {}).get('entries', {}) if REPO_MAP.exists() else {}
    desc_cache = _read_json_safe(DESC_CACHE, {}) if DESC_CACHE.exists() else {}
    pr_names = pr_registered_names()

    entries, (n_dedup, n_conflict) = canonical_merge(entries, repo_map, locate)
    print(f'[gen-plugins-all] canonical 归并：去重 {n_dedup} 条 · 判定冲突降待定 {n_conflict} 条')

    # 实时 star 映射（locate-cache 的 full_name → stargazerCount），对全部已定位条目生效
    live_star = {r['full_name'].lower(): r['star'] for r in locate.values()
                 if r.get('status') == 'found' and r.get('full_name') and isinstance(r.get('star'), int)}
    url_audit = (_read_json_safe(URL_AUDIT, {}) or {}).get('entries', {}) if URL_AUDIT.exists() else {}

    n_fix = n_empty = n_amb = n_unresolved = n_star = 0
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
        # 消亡仓库降级（url-audit 判 gone：已删除/改名/转私有 → 空仓监测，不呈现链接）
        m0 = REAL_URL_RE.search(e.get('url') or '')
        if e['locate'] == 'located' and m0 \
                and url_audit.get(f"{m0.group(1)}/{m0.group(2)}".lower(), {}).get('status') == 'gone':
            e['locate'] = 'empty_watch'
            n_empty += 1
        # 实时 star 覆盖（含真实 URL 条目与合并条目；快照层 star 陈旧或为 0）
        m = REAL_URL_RE.search(e.get('url') or '')
        if m:
            ls = live_star.get(f"{m.group(1)}/{m.group(2)}".lower())
            if ls is not None:
                e['star'] = ls
                n_star += 1

    # 登记表兜底（#189）：PLUGINS.md 表行有、已定位集合没有的仓，按登记信息补行（判定 [未测]；
    # url-audit 判 gone 的登记仓进空仓监测）。登记轨与快照轨在此并集，登记不再单向依赖测试覆盖。
    n_floor = n_floor_gone = 0
    reg_md = ROOT / 'PLUGINS.md'
    if reg_md.is_file():
        have = set()
        for e in entries:
            mh = REAL_URL_RE.search(e.get('url') or '')
            if mh:
                have.add(f"{mh.group(1)}/{mh.group(2)}".lower())
            have.add(e['name'].lower().replace('/', '-'))
        for line in reg_md.read_text().splitlines():
            rm = re.match(r'^\|\s*([^|]+?)\s*\|\s*\[[^\]]*\]\('
                          r'(https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)/?\)\s*\|\s*([^|]*)', line)
            if not rm:
                continue
            name, url, desc = rm.group(1).strip(), rm.group(2), rm.group(3).strip()
            full = url.split('github.com/')[1].strip('/').lower()
            if full in have:
                continue
            dom, _hit = classify(name, desc)
            fe = {'name': name or full.split('/')[1], 'url': f"https://github.com/{full}",
                  'star': live_star.get(full), 'verdict': '⏳ 未测',
                  'domain': dom, 'desc': desc or '—', 'locate': 'located'}
            if url_audit.get(full, {}).get('status') == 'gone':
                fe['locate'] = 'empty_watch'
                n_floor_gone += 1
            else:
                n_floor += 1
            entries.append(fe)
            have.add(full)
        if n_floor or n_floor_gone:
            print(f'[gen-plugins-all] 登记兜底：补 [未测] {n_floor} 行 · 空仓监测 {n_floor_gone} 行（PLUGINS.md ⊕ 快照并集）')

    # canonical 改名跟随（README 全覆盖轮）：repo-map（含 aliases 历史名）映射到引擎登记的最新全名，
    # 覆盖已定位行的链接；名称文本仅在等于旧仓名时同步改写。实时改名纠正由 refresh-stars 的 REST 301 回退日更承担。
    rm_canon = {}
    for v in repo_map.values():
        fn = (v.get('full_name') or '').strip()
        if not fn:
            continue
        for a in ([fn] + list(v.get('aliases') or [])):
            al = (a or '').strip().lower()
            if al and al != fn.lower():
                rm_canon[al] = fn
    n_rename = 0
    for e in entries:
        if e.get('locate') != 'located':
            continue
        m1 = REAL_URL_RE.search(e.get('url') or '')
        if not m1:
            continue
        cur = f"{m1.group(1)}/{m1.group(2)}".lower()
        canon = rm_canon.get(cur)
        if not canon or canon.lower() == cur:
            continue
        if e['name'].lower() == cur.split('/')[1]:
            e['name'] = canon.split('/')[1]
        e['url'] = f"https://github.com/{canon}"
        n_rename += 1
    if n_rename:
        print(f'[gen-plugins-all] canonical 改名跟随：{n_rename} 行（repo-map aliases）')

    # desc 回填（GitHub 描述缓存）+「其他」兜底重分类（taxonomy v2 规则，仅动其他类）
    n_desc = n_reclass = 0
    for e in entries:
        desc = (e.get('desc') or '').strip()
        if (not desc or desc == '—' or desc.startswith('http')) and e.get('locate') == 'located':
            full = e['url'].split('github.com/')[1].strip('/') if 'github.com/' in e.get('url', '') else ''
            if full.count('/') == 1 and desc_cache.get(full):
                e['desc'] = desc_cache[full]
                n_desc += 1
        if e.get('domain') == '❓ 其他':
            dom, _hit = classify(e['name'], e.get('desc') or '')
            if dom != '❓ 其他':
                e['domain'] = dom
                e['reclassed'] = True
                n_reclass += 1
    print(f'[gen-plugins-all] desc 回填 {n_desc} · 兜底重分类 {n_reclass}（taxonomy v2）')

    vc = Counter(e['verdict'] for e in entries if e['locate'] == 'located')
    v_all = Counter(e['verdict'] for e in entries)   # 全量口径：含监测/未定位条目的判定
    src = ' ⊕ '.join(f'`{rid}` {bj(ts)}' for rid, ts in rounds[:3])
    if len(rounds) > 3:
        src += f' 等 {len(rounds)} 轮'

    L = []
    L.append('# 全量插件清单（统一四档口径）')
    L.append('')
    L.append(f'> 数据源：radar 快照并集（{src}）⊕ GitHub 定位复核缓存（data/locate-cache.json）。')
    L.append('> 呈现：分组列表（状态 · 名称 · ★星标 · 一句话说明），不使用大表格；〔📦〕= 整合包（根 dsh.bundle / workspaces 多子包）。')
    L.append('')
    L.append('## 统一度量衡')
    L.append('')
    L.append('**判定维度**（运行级四档；测试：dsh 容器 agent + Qwen3.6-35B · k8s 5 分片 · run_id 锚定轮次）：')
    L.append('')
    if radar_ver:
        L.append(f'- 测试版本：`{radar_ver}`（runner 镜像 cur_image，烤入本页磁贴右段）')
    L.append(f'- 全量判定 {sum(v_all.values())}（全体条目，含监测/未定位；README 磁贴为单快照即时口径，与本清单并集归并口径的差源见附录）：'
             f'`[可用]`（{v_all.get("✅ 运行级可用", 0)}）/ `[不兼容]`（{v_all.get("❌ 运行级不兼容", 0)}）/ `[待定]`（{v_all.get("⚠️ 待定", 0)}）')
    L.append(f'- 已定位明细 {sum(vc.values())}（本列表展示口径，另 {len(entries) - sum(vc.values())} 条监测/未定位的判定暂不展示）：'
             f'`[可用]`（{vc.get("✅ 运行级可用", 0)}）/ `[不兼容]`（{vc.get("❌ 运行级不兼容", 0)}）/ `[待定]`（{vc.get("⚠️ 待定", 0)}）/ `[未测]`（{vc.get("⏳ 未测", 0)}）')
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

    dom_dir = ROOT / 'catalog' / 'all'
    dom_dir.mkdir(parents=True, exist_ok=True)
    for dom in DOMAIN_ORDER:
        # 组内排序：星标降序；[不兼容] 整体沉组尾（组内仍按星标）——排除信息不占组头
        group = sorted([e for e in entries if e.get('domain') == dom],
                       key=lambda x: (x.get('verdict') == '❌ 运行级不兼容', -(x.get('star') or 0)))
        if not group:
            continue
        dl = [f'# {dom}（{len(group)}）', '',
              f'> 数据源与口径见 [PLUGINS-ALL.md](../../PLUGINS-ALL.md)（索引页）；磁贴图例同 README。', '']
        for e in group:
            name = e['name']
            star = e.get('star')
            star_part = f'★{star} ' if isinstance(star, int) else ''   # 星数未知留空不印 0（防污染排序，bot 日更补齐）
            desc = (e.get('desc') or '—').strip()
            if desc.startswith('http'):
                desc = '—'
            pr = ' 〔PR〕' if name in pr_names else ''
            loc = e.get('locate')
            if loc == 'empty_watch':
                dl.append(f'- `[空仓监测]` **{name}** — GitHub 无此仓库，判定暂不展示{pr}')
            elif loc == 'ambiguous_watch':
                dl.append(f'- `[歧义监测]` **{name}** — 同名多仓，判定暂不展示{pr}')
            elif loc == 'unresolved':
                dl.append(f'- `[未定位]` **{name}** — 占位待复核，判定暂不展示{pr}')
            else:
                bundle_part = '〔📦〕' if e.get('bundle') else ''   # 整合包（dsh.bundle / workspaces 结构）
                dl.append(f'- {MARK.get(e.get("verdict"), "⬜ `[未测]`")} [{name}]({e["url"]}) {star_part}— {desc}{pr}{bundle_part}')
        dom_slug = dom.split(' ', 1)[-1]
        dom_file = dom_dir / f'{dom_slug}.md'
        dom_file.write_text('\n'.join(dl).replace('](assets/', '](../../assets/') + '\n', encoding='utf-8')
        g_ok = vc_local(entries, dom, '✅ 运行级可用')
        g_bad = vc_local(entries, dom, '❌ 运行级不兼容')
        g_inc = vc_local(entries, dom, '⚠️ 待定') + vc_local(entries, dom, '⏳ 未测')
        L.append(f'- **{dom}**（{len(group)}）— 🟩 {g_ok} · 🟨 {g_bad} · ⬜ {g_inc} — [明细]({dom_file.relative_to(ROOT)})')
    L.append('')

    L.append('## 附录')
    L.append('')
    L.append('- 判定与定位正交；监测类条目的原始判定保留于 data/snapshots/，定位成功后自动恢复展示。')
    L.append('- 占位 URL 由发现管线 clone 库通道产生；定位复核：`python3 scripts/resolve_placeholders.py`（结果写 data/locate-cache.json，命中附实时 star）。')
    L.append('- 合并主键以 GitHub 仓库全名为准（真实 URL / data/repo-map.json / 定位缓存三源归一）：同一仓库的不同命名键合并为单条，判定冲突降级 [待定] 待重测仲裁。')
    L.append('- 口径对齐说明：README 磁贴/徽章与「运行级实测」行为单快照即时全量口径；本清单为多轮快照并集归并口径（同名多键合一、判定冲突降 [待定]、刷新随日更）。两者存在时滞与归并差，属设计特性；判定真相以 data/snapshots/ 逐轮快照为准。')
    L.append('')

    OUT.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'[gen-plugins-all] {len(entries)} 条 → {OUT.name}（定位修复 {n_fix} / 空仓 {n_empty} / 歧义 {n_amb} / 未定位 {n_unresolved} / 实时星 {n_star}）')
    # 汇总卡数据（供 render 的目录摘要用）：每类分布 + 全局统计（磁贴「未测」=登记兜底口径，快照层不产 ⏳）
    return {'domains': {dom: {'total': sum(1 for e in entries if e.get('domain') == dom),
                  'ok': vc_local(entries, dom, '✅ 运行级可用'),
                  'bad': vc_local(entries, dom, '❌ 运行级不兼容'),
                  'inc': vc_local(entries, dom, '⚠️ 待定'),
                  'un': vc_local(entries, dom, '⏳ 未测'),
                  'watch': sum(1 for e in entries if e.get('domain') == dom and e.get('locate') != 'located')}
            for dom in DOMAIN_ORDER},
            'global': {'un': vc.get('⏳ 未测', 0), 'located': sum(vc.values()), 'all': len(entries)}}


def vc_local(entries, dom, verdict):
    return sum(1 for e in entries if e.get('domain') == dom and e.get('locate') == 'located' and e.get('verdict') == verdict)


if __name__ == '__main__':
    main()
