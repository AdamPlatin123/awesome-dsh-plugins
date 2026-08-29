#!/usr/bin/env python3
"""刷新 README 精选插件榜 + 整合包节（人工策展 + 自动刷新星标）。

精选榜成员来自 data/awesome-50.json、整合包来自 data/bundles.json（均人工策展，
本脚本只读不改成员）；逐仓库 REST 查询星标（跟随改名重定向），渲染分类表格，
重写两份 README 的 AUTO:featured 与 AUTO:bundles 块。任一策展成员不可达或
查询失败即中止（成员是固定名单，消失/失联是异常信号，不写半截榜单）。

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
BUNDLES = os.path.join(ROOT, 'data', 'bundles.json')
SNAP_DIR = os.path.join(ROOT, 'data', 'snapshots')
REFRESH_LABEL = '每 6 小时自动刷新'
VERDICT_MARK = {'ok': '✅', 'pending': '待定', 'incompatible': '需适配', 'untested': '未测', None: '—'}
# 快照四档 → 榜单判定键（渲染期覆盖 JSON 种子值；快照缺失/未定位时回落种子）
SNAP_VERDICT = {'✅ 运行级可用': 'ok', '运行级可用': 'ok', '❌ 运行级不兼容': 'incompatible',
                '运行级不兼容': 'incompatible', '⚠️ 待定': 'pending', '待定': 'pending',
                '⏳ 未测': 'untested', '未测': 'untested'}


def radar_verdicts():
    """最新快照 catalog_entries → {owner/repo 小写: 判定键}；无快照返回空表（渲染回落 JSON 种子）。"""
    try:
        snaps = sorted(f for f in os.listdir(SNAP_DIR) if f.endswith('.json'))
        data = json.load(open(os.path.join(SNAP_DIR, snaps[-1]), encoding='utf-8'))
        out = {}
        for e in data.get('catalog_entries') or []:
            url = str(e.get('url', ''))
            if 'github.com/' in url:
                repo = url.split('github.com/', 1)[1].strip('/').lower()
                v = SNAP_VERDICT.get(str(e.get('verdict', '')).strip())
                if repo and v:
                    out[repo] = v
        return out
    except Exception as e:
        print(f'[warn] 快照判定加载失败，回落 JSON 种子: {e}')
        return {}


def wbr(s):
    """在 ASCII 长词内注入 <wbr> 断点（连字符/斜杠/点后）。
    统一各表换行逻辑：GitHub 表格超宽时按可断行性压缩列宽，长词不可断会使不同表的
    列宽谈判结果不同、挤压磁贴列；统一断点后所有表行为一致（<wbr> 在 sanitize 白名单内）。"""
    return re.sub(r'([\-/.])(?=[A-Za-z0-9])', r'\1<wbr>', s)


def radar_version():
    """runner 测试版本：优先取最新快照 verdict.cur_image（runner 返回的正源，如 dsh-test-runner:0.1.1-rc.2），
    缺失时回落 data/radar-env.json（人工维护的镜像钉定锚）。"""
    try:
        snaps = sorted(f for f in os.listdir(SNAP_DIR) if f.endswith('.json'))
        data = json.load(open(os.path.join(SNAP_DIR, snaps[-1]), encoding='utf-8'))
        img = str(data.get('verdict', {}).get('cur_image', '') or '')
        if ':' in img:
            return img.split(':', 1)[1]
        if img:
            return img
    except Exception:
        pass
    try:
        return json.load(open(os.path.join(ROOT, 'data', 'radar-env.json'), encoding='utf-8'))['dsh_version']
    except Exception:
        return ''


_TILE_W = {}


def _probe_width(url):
    """探测 shields SVG 的 intrinsic 宽度（按 URL 缓存），用于钉死 <img> 尺寸防 GitHub 表格自动缩放。"""
    if url not in _TILE_W:
        try:
            p = subprocess.run(['curl', '-s', '--max-time', '15', url],
                               capture_output=True, text=True)
            m = re.search(r'<svg[^>]*width="(\d+)"', p.stdout)
            _TILE_W[url] = int(m.group(1)) if m else 108
        except Exception:
            _TILE_W[url] = 108
    return _TILE_W[url]


def tile(verdict_key, ver):
    """三态磁贴：左半兼容状态（绿=已兼容 · 黄=需适配 · 灰=待测试），右半该轮测试版本。
    三词统一 3 字以确保等宽；labelColor 把状态色赋给左段、右段固定中性灰；
    以 <img width height> 输出——markdown 图片在 GitHub 表格中会被自适应缩放，显式钉尺寸可免疫。"""
    from urllib.parse import quote
    v = ver.replace('-', '--').replace('_', '__').replace(' ', '_')
    if verdict_key == 'ok':
        label, lc = '已兼容', '97CA00'    # brightgreen
    elif verdict_key == 'incompatible':
        label, lc = '需适配', 'DFB317'    # yellow
    else:
        label, lc = '待测试', '9F9F9F'    # lightgrey
    url = (f'https://img.shields.io/badge/{quote(label)}-{v}-555555'
           f'?style=flat-square&labelColor={lc}')
    w = _probe_width(url)
    return f'<img src="{url}" alt="{label}" width="{w}" height="20">'

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
    bdata = json.load(open(BUNDLES, encoding='utf-8'))
    rv = radar_verdicts()
    ver = radar_version()
    print(f'[verdict] 快照判定映射 {len(rv)} 条（渲染期覆盖，缺者回落 JSON 种子）· 测试版本 {ver}')
    cats = data['categories']
    forms = bdata['forms']
    repos = [p['repo'] for c in cats for p in c['plugins']]
    brepos = [p['repo'] for f in forms for p in f['plugins']]
    # 成员数随实测口径动态变化（rc.8 重测通过者）；下限防 JSON 误删，去重防误加
    if len(repos) < 20:
        sys.exit(f'[中止] 策展成员仅 {len(repos)} 个（<20），疑似 JSON 损坏，需人工校对')
    if len(set(repos)) != len(repos):
        sys.exit('[中止] 策展成员存在重复仓库，JSON 需人工校对')
    if len(brepos) < 5:
        sys.exit(f'[中止] 整合包成员仅 {len(brepos)} 个（<5），疑似 JSON 损坏，需人工校对')
    if len(set(brepos)) != len(brepos):
        sys.exit('[中止] 整合包成员存在重复仓库，JSON 需人工校对')

    with ThreadPoolExecutor(max_workers=16) as ex:
        results = list(ex.map(fetch, repos + brepos))
    stars, fails = {}, []
    for repo, r in zip(repos + brepos, results):
        if r is None:
            fails.append(f'{repo}(不可达/私有/归档)')
        elif r[0] == 'RETRY_FAIL':
            fails.append(f'{repo}(网络失败)')
        else:
            stars[repo] = r[1]
    print(f'[fetch] 成功 {len(stars)}/{len(repos) + len(brepos)}')
    if fails:
        sys.exit(f'[中止] 策展成员查询失败 {len(fails)} 个: {fails[:5]}')

    ts = datetime.now(ZoneInfo('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')
    total = sum(len(c['plugins']) for c in cats)
    parts = [
        '<!-- AUTO:featured:START -->', '',
        f'> 人工策展 {total} 款插件，按 11 类分组、类内按星标排序；星标{REFRESH_LABEL}'
        f'（成员调整请提 PR 修改 data/awesome-50.json）。数据截至 {ts}（UTC+8）。',
        '',
    ]
    for c in cats:
        ranked = sorted(c['plugins'], key=lambda p: (-stars[p['repo']], p['repo'].lower()))
        parts.append(f"### {c['name']}（{len(ranked)}）")
        parts.append('')
        # 列表布局（非表格）：GitHub 表格对单元格图片强制 max-width:100%+height:auto 缩放无法规避；
        # 列表行内图片保持原尺寸，磁贴开头统一 108px 亦使全页文本列自然对齐
        for p in ranked:
            t = tile(rv.get(p['repo'].lower(), p.get('verdict')), ver)
            parts.append(f"- {t} **[{p['name']}](https://github.com/{p['repo']})** · {stars[p['repo']]}★"
                         f" — {p['desc'].replace('|', '\\|')}")
        parts.append('')
    parts.append('> 兼容状态磁贴 = 雷达 k8s 运行级判定（🟩 已兼容 · 🟨 需适配 · ⬜ 待测试，三态等宽；四档口径见下文），'
                 '右半为该轮 runner 测试版本（与 [data/radar-env.json](data/radar-env.json) 同源），'
                 '**本列由 bot 按最新快照自动回写**，榜内成员走插队重测通道优先轮测；'
                 'rc.8 + v4flash 源码路径重测（2026-08-21，50 仓 + 对方清单高星 22 仓）证据见 '
                 '[data/rc8-retest-20260821/](data/rc8-retest-20260821/) 与 [PLUGINS-ALL.md](PLUGINS-ALL.md)；'
                 '安装第三方插件前请审查源码并固定 commit。')
    block = '\n'.join(parts) + '\n\n<!-- AUTO:featured:END -->'

    # ── 整合包节（AUTO:bundles）：四形态，类内星标降序 ──
    btotal = len(brepos)
    bparts = [
        '<!-- AUTO:bundles:START -->', '',
        f'> 人工策展 {btotal} 个整合包：内测成员作品置顶，其下按预设套件 / 能力合集 / 发行版 / 配方管理器四形态分组，'
        f'类内按星标排序；星标{REFRESH_LABEL}（成员调整请提 PR 修改 data/bundles.json）。数据截至 {ts}（UTC+8）。',
        '',
    ]
    for f in forms:
        ranked = sorted(f['plugins'], key=lambda p: (-stars[p['repo']], p['repo'].lower()))
        bparts.append(f"### {f['name']}（{len(ranked)}）")
        bparts.append('')
        for p in ranked:
            t = tile(rv.get(p['repo'].lower(), p.get('verdict')), ver)
            bparts.append(f"- {t} **[{p['name']}](https://github.com/{p['repo']})** · {stars[p['repo']]}★"
                          f" — {p['desc'].replace('|', '\\|')}")
        bparts.append('')
    bparts.append('> 磁贴口径同精选榜（三态 · 右半 runner 版本）；整合包安装方式以各仓库 README 为准（预设类多为 `dsh plugin add` 后在设置中启用，发行版类需按其自身安装器操作）。')
    bblock = '\n'.join(bparts) + '\n\n<!-- AUTO:bundles:END -->'

    changed = False
    for name in ['README.md', 'README.en-US.md']:
        path = os.path.join(ROOT, name)
        text = open(path, encoding='utf-8').read()
        new = re.sub(r'<!-- AUTO:featured:START -->[\s\S]*?<!-- AUTO:featured:END -->',
                     lambda _: block, text, count=1)
        new = re.sub(r'<!-- AUTO:bundles:START -->[\s\S]*?<!-- AUTO:bundles:END -->',
                     lambda _: bblock, new, count=1)
        if new != text:
            if not DRY:
                open(path, 'w', encoding='utf-8').write(new)
            changed = True
            print(f'[write] {name}')
    if not changed:
        print('[noop] 榜单无变化')
    top = max(repos, key=lambda r: stars[r])
    btop = max(brepos, key=lambda r: stars[r])
    print(f'[done] 精选 {len(repos)} 款 · 整合包 {len(brepos)} 个 · 榜首 {top} {stars[top]}⭐ · 整合包之首 {btop} {stars[btop]}⭐')


if __name__ == '__main__':
    main()
