#!/usr/bin/env python3
"""tile_assets.py — 三态磁贴 SVG 资产生成器（仓库本地，替代 11980 次 shields 请求）。

与 README 磁贴同体系：左段状态色 3 字词（绿 97CA00 / 黄 DFB317 / 灰 9F9F9F）、
右段中性深灰版本号；版本源 = 最新快照 verdict.cur_image（runner 返回正源），
回落 data/radar-env.json。每次清单生成幂等重写——runner 升版即全站磁贴换新。
被 gen_plugins_all.py 每轮调用；也可独立运行。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAP_DIR = ROOT / 'data' / 'snapshots'
STATES = {'ok': ('已兼容', '#97CA00'), 'adapt': ('需适配', '#DFB317'), 'test': ('待测试', '#9F9F9F')}

_SVG_TMPL = '''<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="20" role="img" aria-label="{label}: {ver}">
<title>{label}: {ver}</title>
<g shape-rendering="crispEdges"><rect width="{lw}" height="20" fill="{color}"/><rect x="{lw}" width="{rw}" height="20" fill="#555555"/></g>
<g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
<text x="{lx}" y="14">{label}</text><text x="{rx}" y="14">{ver}</text></g>
</svg>
'''


def current_version():
    try:
        for fp in sorted(SNAP_DIR.glob('*.json'), reverse=True):
            d = json.loads(fp.read_text())
            img = str((d.get('verdict') or {}).get('cur_image', '') or '')
            if img:
                return img.split(':', 1)[1] if ':' in img else img
    except Exception:
        pass
    try:
        return json.loads((ROOT / 'data' / 'radar-env.json').read_text())['dsh_version']
    except Exception:
        return ''


def write_tiles(ver=None):
    """幂等写 assets/tile-{ok,adapt,test}.svg；返回 {key: (文件路径, 总宽)}。"""
    ver = ver or current_version()
    out = {}
    for key, (label, color) in STATES.items():
        lw = 44                                    # 3 字 CJK + 内边距
        rw = int(len(ver) * 6.6 + 12)              # 版本串宽（Verdana 11px 近似）
        svg = _SVG_TMPL.format(total=lw + rw, lw=lw, rw=rw, lx=lw / 2, rx=lw + rw / 2,
                               label=label, color=color, ver=ver)
        p = ROOT / 'assets' / f'tile-{key}.svg'
        p.parent.mkdir(exist_ok=True)
        p.write_text(svg)
        out[key] = (str(p.relative_to(ROOT)), lw + rw)
    return out


def tile_widths():
    """读既有 SVG 的总宽（供 refresh-featured 钉 <img> 宽度）；缺失返回空。"""
    out = {}
    for key in STATES:
        p = ROOT / 'assets' / f'tile-{key}.svg'
        if p.exists():
            m = re.search(r'<svg[^>]*width="(\d+)"', p.read_text())
            if m:
                out[key] = int(m.group(1))
    return out


if __name__ == '__main__':
    v = current_version()
    print(f'[tile-assets] 版本 {v}')
    for key, (rel, w) in write_tiles(v).items():
        print(f'  {rel} → {w}px')
