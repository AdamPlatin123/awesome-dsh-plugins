#!/usr/bin/env python3
"""dashboard.py v3 — 雷达控制塔（静态页 + JSON 接口，2026-08-26 重做）。

架构：单文件 Python http.server（零依赖，systemd 直跑）。
  GET /                      静态页（内嵌 HTML/CSS/JS，前端 10s 轮询接口）
  GET /api/summary.json      状态带 + 实时审计 + 近 24h 计数
  GET /api/verdicts.json     判定分页（offset/limit/status/reason/q）
  GET /api/verdict/<lk>.json 单条全量详情（行展开用）
  GET /api/trend.json        近 24h 小时级聚合（结果时间戳，零 metrics 依赖）
  GET /healthz               轻量健康端点

数据源（全只读）：
  ~/dsh-k8s/state/pipeline-state.json   活管线状态（driver 实际写入处）
  ~/dsh-k8s/state/repo-map.json         身份账本
  ~/dsh-k8s/state/monitor-report.json   监控脚本 30min 报告（含抽查）
  REPO/.rt-agent-v2/results/*.json      判定结果（内存索引，mtime 失效缓存）
"""
import json
import os
import re
import threading
import time
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

HOME = Path.home()
STATE_ROOT = Path(os.environ.get("RADAR_STATE_DIR", str(HOME / "dsh-k8s")))
REPO = Path(os.environ.get("RADAR_REPO_DIR", str(HOME / "dsh-external-research")))
RESULTS = REPO / ".rt-agent-v2/results"
STATE = STATE_ROOT / "state/pipeline-state.json"
REPO_MAP = STATE_ROOT / "state/repo-map.json"
MONITOR_REPORT = STATE_ROOT / "state/monitor-report.json"
PORT = int(os.environ.get("RADAR_DASH_PORT", "8898"))
NEW_ERA = "2026-08-26T10:08"  # 确定性启动探测上线（时代穿越检测基准）

ENV_ERR_RE = re.compile(r"readonly|EACCES|只读|permission denied|EPERM|权限|沙箱|禁止写入|denied", re.I)
TRANSPORT_RE = re.compile(
    r"TRANSPORT|STREAM_CLOSED|EMPTY_RESPONSE|ECONNREFUSED|ECONNRESET|ETIMEDOUT"
    r"|socket hang up|fetch failed", re.I)
KNOWN_SKIP = {"no-plugin-structure", "env-needs-web-host", "pod-clone failed",
              "repo-gone", "source missing at /plugin-src"}
KNOWN_INCONCL = {"transport-or-unconverged", "boot-probe-inconclusive",
                 "model-endpoint-unavailable (l3b deferred)", "interrupted"}
KNOWN_FAIL_PREFIX = ("fail: load-crash", "fail: activation-failed",
                     "install-failed", "load-failed", "fail:")


def read_json(p, default=None):
    try:
        return json.loads(Path(p).read_text())
    except (OSError, ValueError):
        return default


_JSON_CACHE = {}
_JSON_CACHE_LOCK = threading.Lock()


def read_json_cached(p, ttl=2.0):
    """mtime+TTL 双失效缓存：1s 轮询下 repo-map(1.3万条)/pipeline-state 不再每请求重解析。"""
    key = str(p)
    now = time.time()
    with _JSON_CACHE_LOCK:
        hit = _JSON_CACHE.get(key)
    try:
        mtime = Path(p).stat().st_mtime
    except OSError:
        return None
    if hit and hit[0] == mtime and now - hit[1] < ttl:
        return hit[2]
    doc = read_json(p)
    if doc is not None:
        with _JSON_CACHE_LOCK:
            _JSON_CACHE[key] = (mtime, now, doc)
    return doc


def iso_ts(s):
    try:
        t = datetime.fromisoformat(s)
        return t.timestamp() if t.tzinfo else t.replace(tzinfo=timezone.utc).timestamp()
    except (ValueError, TypeError):
        return 0.0


# ---------------------------------------------------------------- 结果索引缓存
class VerdictIndex:
    """结果目录内存索引：mtime 变化触发后台重扫，期间继续供旧数据（stale-while-revalidate）。
    1s 轮询下不能同步扫盘（万级文件在机械盘上秒级耗时会阻塞请求）。"""

    def __init__(self, path: Path):
        self.path = path
        self._lock = threading.Lock()
        self._rows = []
        self._stamp = None
        self._scanning = False

    def _scan(self):
        rows = []
        for f in self.path.glob("*.json"):
            try:
                x = json.loads(f.read_text())
            except (OSError, ValueError):
                continue
            rows.append({
                "local_key": x.get("local_key", f.stem),
                "status": x.get("status", "?"),
                "result": (x.get("result") or "")[:120],
                "observed_at": x.get("observed_at", ""),
                "npm_status": x.get("npm_status", ""),
                "attempt": x.get("attempt", 0),
                "tries": x.get("tries", 0),
                "stages": [(s.get("stage"), bool(s.get("ok")), s.get("error", ""))
                           for s in x.get("stages", [])],
                "last_error": (x.get("last_error") or "")[:600],
                "ts": x.get("observed_at", ""),
            })
        rows.sort(key=lambda r: r["ts"], reverse=True)
        with self._lock:
            self._rows = rows
            self._stamp = self._scan_stamp
            self._scanning = False

    def rows(self):
        try:
            stamp = self.path.stat().st_mtime
        except OSError:
            return []
        with self._lock:
            if stamp == self._stamp or self._scanning:
                return self._rows
            first = self._stamp is None
            self._scanning = True
            self._scan_stamp = stamp
        if first:  # 首次同步扫，避免首屏空表
            self._scan()
        else:
            threading.Thread(target=self._scan, daemon=True).start()
        return self._rows


IDX = VerdictIndex(RESULTS)


def reason_of(row):
    r = (row["result"] or "").strip()
    rl = r.lower()
    s = row["status"]
    if s == "pass":
        return "pass"
    if s == "fail":
        if rl.startswith(("install-failed", "load-failed")):
            return r.split("(")[0].split(":")[0].strip()[:22]
        if rl.startswith("fail:"):
            return (r[5:].split("(")[0].strip() or "fail")[:22]
        return "fail-其他"
    if s == "skipped":
        return r if r in KNOWN_SKIP else ("skip-" + r[:16])
    if s == "inconclusive":
        return r if r in KNOWN_INCONCL else ("inconcl-" + r[:16])
    return "?"


def audit_scan(rows):
    """看板端实时归因审计（纯本地正则，无网络），窗口近 6 小时。"""
    cut = time.time() - 6 * 3600
    suspects, unknown, webhost_new, inconcl = [], [], [], 0
    for r in rows:
        if iso_ts(r["ts"]) < cut:
            continue
        blob = r["result"] + " " + r["last_error"]
        s, rr = r["status"], (r["result"] or "").strip()
        rl = rr.lower()
        if s == "fail" and ENV_ERR_RE.search(blob):
            suspects.append({"lk": r["local_key"], "kind": "fail带环境痕迹(疑沙箱/权限)",
                             "ts": r["ts"], "detail": (r["last_error"] or rr)[:90]})
        elif s == "fail" and TRANSPORT_RE.search(blob):
            suspects.append({"lk": r["local_key"], "kind": "fail带传输痕迹(应为待定)",
                             "ts": r["ts"], "detail": (r["last_error"] or rr)[:90]})
        elif s == "pass" and r["last_error"] and \
                re.search(r"error|fatal|failed", r["last_error"], re.I) and \
                not TRANSPORT_RE.search(r["last_error"]):
            suspects.append({"lk": r["local_key"], "kind": "pass带错误痕迹(可疑通过)",
                             "ts": r["ts"], "detail": r["last_error"][:90]})
        if (s == "skipped" and rl not in KNOWN_SKIP and rr) or \
           (s == "fail" and not rl.startswith(KNOWN_FAIL_PREFIX) and not
                ENV_ERR_RE.search(blob)) or \
           (s == "inconclusive" and rl not in KNOWN_INCONCL):
            unknown.append({"lk": r["local_key"], "status": s, "ts": r["ts"],
                            "result": rr[:90]})
        if rr.startswith("env-needs-web-host") and r["ts"] >= NEW_ERA:
            webhost_new.append({"lk": r["local_key"], "ts": r["ts"]})
        if s == "inconclusive":
            inconcl += 1
    return {"suspects": suspects[:12], "unknown": unknown[:12],
            "webhost_new_era": webhost_new[:12], "inconcl_6h": inconcl}


def trend_24h(rows):
    """结果时间戳 → 近 24h 小时桶（旧→新排列）。"""
    now = datetime.now(timezone.utc)
    keys = [(now - timedelta(hours=h)).strftime("%m-%dT%H") for h in range(23, -1, -1)]
    buckets = {k: {"h": k.split("T")[1] + ":00", "pass": 0, "fail": 0,
                   "skipped": 0, "inconclusive": 0} for k in keys}
    for r in rows:
        try:
            t = datetime.fromisoformat(r["ts"])
        except (ValueError, TypeError):
            continue
        if t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
        k = t.strftime("%m-%dT%H")
        if k in buckets and r["status"] in buckets[k]:
            buckets[k][r["status"]] += 1
    return [buckets[k] for k in keys]


def summary():
    ps = read_json_cached(STATE) or {}
    rm = read_json_cached(REPO_MAP) or {"entries": {}, "quarantine": {}}
    entries = rm.get("entries", {})
    cls = {}
    for e in entries.values():
        c = e.get("classification", "unknown")
        cls[c] = cls.get(c, 0) + 1
    rows = IDX.rows()
    now = time.time()
    counts = {"pass": 0, "fail": 0, "skipped": 0, "inconclusive": 0}
    skip_comp = {}
    for r in rows:
        if iso_ts(r["ts"]) > now - 86400:
            counts[r["status"]] = counts.get(r["status"], 0) + 1
            if r["status"] == "skipped":
                k = reason_of(r)
                skip_comp[k] = skip_comp.get(k, 0) + 1
    tot = sum(counts.values()) or 1
    state_age = (now - STATE.stat().st_mtime) if STATE.exists() else None
    return {
        "now": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "phase": ps.get("phase"),
        "updated_at": ps.get("updated_at"),
        "state_age_s": state_age,
        "capacity": ps.get("capacity", {}),
        "due": (ps.get("current") or {}).get("due"),
        "cycle": ps.get("cycle", {}),
        "image": ps.get("image"),
        "pods": ps.get("pods_brief", []),
        "identity": {"canonical": len(entries),
                     "quarantine": len(rm.get("quarantine", {})), "class": cls},
        "last24h": counts,
        "real_share": round(counts["pass"] * 100 / tot),
        "skip_composition": dict(sorted(skip_comp.items(), key=lambda kv: -kv[1])),
        "total_results": len(rows),
        "audit_live": audit_scan(rows),
        "audit_monitor": read_json(MONITOR_REPORT),
        "k8s": ps.get("kubernetes", {}),
    }


PAGE = r"""<!doctype html><html lang=zh><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>DSH 插件雷达 · 控制塔</title>
<link rel=preconnect href=https://fonts.googleapis.com>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel=stylesheet>
<style>
:root{--bg:#0A0F1C;--panel:#0D1524;--panel2:#101B2E;--line:#1E2A3F;--line2:#243247;
--fg:#E6EDF6;--dim:#7C8CA3;--faint:#55647A;
--cy:#22D3EE;--ok:#34D399;--bad:#F87171;--warn:#F5A623;--skip:#8B98AB;
--mono:'JetBrains Mono',ui-monospace,Menlo,monospace}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font:14px/1.5 Inter,'Segoe UI',system-ui,sans-serif;padding:18px 22px}
.wrap{max-width:1440px;margin:0 auto}
header{display:flex;align-items:baseline;gap:14px;border-bottom:1px solid var(--line);padding-bottom:10px;flex-wrap:wrap}
h1{font-size:18px;font-weight:700;letter-spacing:.4px}
h1 small{font:600 10px var(--mono);color:var(--faint);letter-spacing:2.5px;margin-left:8px}
.chips{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap}
.chip{border:1px solid var(--line2);padding:2px 10px;border-radius:3px;font:11.5px var(--mono);color:var(--dim);display:inline-flex;gap:6px;align-items:center}
.chip b{color:var(--fg);font-weight:600}
.chip svg{vertical-align:-1px;margin:0 1px 0 7px}
.dot{width:7px;height:7px;border-radius:50%;background:var(--ok)}
@keyframes p{50%{opacity:.3}} .dot.live{animation:p 2s infinite}
@media(prefers-reduced-motion:reduce){.dot{animation:none!important}}
#audit{background:#1a0f14;border:1.5px solid #7F1D1D;border-radius:5px;padding:10px 14px;margin-top:12px}
#audit.ok{background:#0c1410;border-color:#1F4D33}
#audit h2{font:600 11px var(--mono);letter-spacing:2px;color:var(--bad);text-transform:uppercase;margin-bottom:6px}
#audit.ok h2{color:var(--ok)}
.au{font:12px var(--mono);padding:3px 0;border-bottom:1px dashed #2a1520;display:flex;gap:10px}
.au:last-child{border:none}
.au .k{color:#ffb4b0;min-width:225px}.au .lk{color:var(--cy);cursor:pointer;min-width:255px}
.au .d{color:var(--dim);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#audit .meta{font:10.5px var(--mono);color:var(--faint);margin-top:6px}
.pipe{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:14px}
.st{background:var(--panel);border:1px solid var(--line);border-top:2px solid var(--line2);padding:10px 13px}
.st.hot{border-top-color:var(--cy)}.st.ok{border-top-color:var(--ok)}.st.warn{border-top-color:var(--warn)}
.no{font:600 9.5px var(--mono);letter-spacing:2px;color:var(--cy);text-transform:uppercase}
.st b{display:block;font:700 26px/1.2 var(--mono);margin:3px 0 2px;font-variant-numeric:tabular-nums}
.st b small{font-size:12px;color:var(--dim);font-weight:600}
.cap{font:10.5px/1.5 var(--mono);color:var(--dim)}
.trendrow{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:14px}
.tr{background:var(--panel);border:1px solid var(--line);padding:9px 13px}
.tt{font:600 9.5px var(--mono);letter-spacing:2px;color:var(--faint);text-transform:uppercase}
.tv{font:700 20px var(--mono);margin:2px 0}
svg.bars{width:100%;height:34px;display:block}
h2.sec{font:600 10.5px var(--mono);letter-spacing:2.2px;text-transform:uppercase;color:var(--faint);margin:20px 0 8px;border-left:3px solid var(--cy);padding-left:9px}
.bar{display:flex;gap:8px;align-items:center;margin-bottom:9px;flex-wrap:wrap}
input,select{background:var(--panel2);border:1px solid var(--line2);color:var(--fg);font:12px var(--mono);padding:5px 9px;border-radius:3px;outline:none}
input:focus,select:focus{border-color:var(--cy)}
#q{min-width:220px}
.tab{background:var(--panel);border:1px solid var(--line);overflow:hidden}
table{border-collapse:collapse;width:100%}
th{font:600 10px var(--mono);letter-spacing:1.6px;text-transform:uppercase;color:var(--faint);text-align:left;padding:8px 11px;background:var(--panel2);border-bottom:1px solid var(--line2)}
td{padding:7px 11px;border-bottom:1px solid var(--line);font-size:12.5px;vertical-align:top}
td.lk{font:12px var(--mono);color:var(--cy);cursor:pointer;max-width:340px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
tr.sp td.lk{color:var(--ok)} tr.sf td.lk{color:#fda4af} tr.si td.lk,tr.ss td.lk{color:var(--dim)}
.st2{font:600 11px var(--mono);padding:1px 8px;border-radius:3px;display:inline-block}
tr.sp .st2{background:#0c2b1e;color:var(--ok)} tr.sf .st2{background:#2b0f13;color:var(--bad)}
tr.si .st2{background:#2b220c;color:var(--warn)} tr.ss .st2{background:#1a2230;color:var(--skip)}
.rsn{font:11.5px var(--mono);color:var(--dim)}
.tm{font:11.5px var(--mono);color:var(--faint);white-space:nowrap}
tr.fresh td{animation:fglow 6s ease-out}
@keyframes fglow{0%{background:#14303c}100%{background:transparent}}
tr.det td{background:var(--panel2);border-bottom:1px solid var(--line2)}
pre.ev{font:11px var(--mono);color:var(--dim);white-space:pre-wrap;word-break:break-all;margin:4px 0;max-height:180px;overflow:auto}
.kv{font:11.5px var(--mono);color:var(--dim);margin-right:14px;display:inline-block}
#more{display:block;width:100%;background:var(--panel2);border:none;border-top:1px solid var(--line2);color:var(--cy);font:600 12px var(--mono);padding:9px;cursor:pointer}
#more:hover{background:#152238}
.foot{font:10.5px var(--mono);color:var(--faint);margin-top:16px;display:flex;gap:16px;flex-wrap:wrap}
@media(max-width:1024px){.pipe{grid-template-columns:repeat(3,1fr)}.trendrow{grid-template-columns:1fr}}
@media(max-width:640px){.pipe{grid-template-columns:1fr}td.lk{max-width:150px}}
</style></head><body><div class=wrap>
<header>
<h1>DSH 插件雷达<small>CONTROL TOWER v3</small></h1>
<div class=chips id=chips></div>
</header>
<div id=audit><h2>异常与归因审计</h2><div id=au-body>加载中…</div><div class=meta id=au-meta></div></div>
<div class=pipe id=pipe></div>
<div class=trendrow id=trends></div>
<h2 class=sec>判定流 <span id=vcount></span></h2>
<div class=bar>
<input id=q placeholder="搜索插件名…">
<select id=fs><option value="">全部状态</option><option value=pass>通过</option><option value=fail>失败</option><option value=skipped>跳过</option><option value=inconclusive>待定</option></select>
<select id=fr><option value="">全部原因</option></select>
<span id=loadinfo style="font:11px var(--mono);color:var(--faint)"></span>
</div>
<div class=tab>
<table><thead><tr><th>插件</th><th style=width:64px>判定</th><th>原因</th><th style=width:130px>阶段</th><th style=width:96px>时间(UTC)</th></tr></thead>
<tbody id=tb></tbody></table>
<button id=more>加载更多</button>
</div>
<div class=foot><span>数据源: pipeline-state / repo-map / v2 results / monitor-report</span><span>1s 轮询 · 增量高亮</span><span>判定语义: 通过=安装+加载+激活（确定性探测）</span></div>
</div>
<script>
let S=null, rows=[], seen=new Set(), total=0, LIMIT=20, expanded=null, detFor=null;
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
async function j(u){const r=await fetch(u);if(!r.ok)throw new Error(u+' '+r.status);return r.json()}
const z=n=>n==null?'-':(n>=10000?(n/1000).toFixed(1)+'k':n);
const IC={
 pass:'<svg width=10 height=10 viewBox="0 0 10 10" aria-label=通过><path d="M1.5 5.5l2.5 2.5 4.5-5.5" fill="none" stroke="#34D399" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 fail:'<svg width=10 height=10 viewBox="0 0 10 10" aria-label=失败><path d="M2 2l6 6M8 2l-6 6" fill="none" stroke="#F87171" stroke-width="1.6" stroke-linecap="round"/></svg>',
 skip:'<svg width=10 height=10 viewBox="0 0 10 10" aria-label=跳过><path d="M1 2l3 3-3 3M5 2l3 3-3 3" fill="none" stroke="#8B98AB" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 pend:'<svg width=10 height=10 viewBox="0 0 10 10" aria-label=待定><circle cx="5" cy="5" r="3.6" fill="none" stroke="#F5A623" stroke-width="1.3"/><path d="M5 2.8V5l1.8 1.2" fill="none" stroke="#F5A623" stroke-width="1.3" stroke-linecap="round"/></svg>'
};
const STZH={pass:'通过',fail:'失败',skipped:'跳过',inconclusive:'待定'};

async function loadSummary(){
  try{S=await j('/api/summary.json')}catch(e){$('chips').innerHTML='<span class=chip style="color:#F87171">接口异常 '+esc(e.message)+'</span>';return}
  const a=S.state_age_s, fresh=a!=null&&a<300;
  $('chips').innerHTML=[
    `<span class=chip><i class="dot ${fresh?'live':''}" style="background:${fresh?'#34D399':'#F5A623'}"></i> ${esc(S.phase||'?')}</span>`,
    `<span class=chip>槽位 <b>${S.capacity?.used??'-'}/${S.capacity?.limit??'-'}</b></span>`,
    `<span class=chip>due <b>${z(S.due)}</b></span>`,
    `<span class=chip>24h ${IC.pass}<b>${S.last24h?.pass??0}</b>${IC.fail}<b>${S.last24h?.fail??0}</b>${IC.skip}<b>${S.last24h?.skipped??0}</b>${IC.pend}<b>${S.last24h?.inconclusive??0}</b></span>`,
    `<span class=chip>真实结论 <b>${S.real_share??0}%</b></span>`,
    `<span class=chip style="color:${fresh?'':'#F5A623'}">state ${a==null?'?':Math.round(a)+'s'}</span>`
  ].join('');
  renderAudit(); renderPipe();
}
function renderAudit(){
  const au=S.audit_live||{}, mon=S.audit_monitor||{};
  const items=[];
  (mon.misattributed_spots||[]).forEach(m=>items.push(['抽查矛盾: 判'+m.claimed+' 实测'+m.actual, m.lk, '']));
  (au.suspects||[]).forEach(x=>items.push([x.kind, x.lk, x.detail]));
  (au.unknown||[]).forEach(x=>items.push(['新形态文本('+x.status+')', x.lk, x.result]));
  (au.webhost_new_era||[]).forEach(x=>items.push(['web跳过出现于新探测时代', x.lk, '']));
  const el=$('audit'), body=$('au-body');
  if(!items.length){el.classList.add('ok');body.innerHTML='<div class=au style="color:#34D399">近 6 小时无归因可疑项、无新形态文本</div>'}
  else{el.classList.remove('ok');
    body.innerHTML=items.slice(0,10).map(i=>`<div class=au><span class=k>${esc(i[0])}</span><span class=lk data-lk="${esc(i[1])}">${esc(i[1])}</span><span class=d>${esc(i[2]||'')}</span></div>`).join('')}
  const parts=[];
  if(mon.ran_at)parts.push('monitor 30min 报告 @ '+esc((mon.ran_at||'').slice(11,19))+'Z');
  (mon.spot_checks||[]).forEach(s=>parts.push('抽查 '+s.lk+' → '+s.actual));
  parts.push('近6h待定 '+(au.inconcl_6h??0)+' 条');
  $('au-meta').textContent=parts.join(' ｜ ');
  body.querySelectorAll('.lk[data-lk]').forEach(e=>e.onclick=()=>{$('q').value=e.dataset.lk;$('fs').value='';$('fr').value='';loadVerdicts(false)});
}
function renderPipe(){
  const idt=S.identity||{}, c=S.cycle||{}, pods=S.pods||[];
  const runP=pods.filter(p=>p.runner==='running').length;
  const d24=(S.last24h?.pass??0)+(S.last24h?.fail??0)+(S.last24h?.skipped??0)+(S.last24h?.inconclusive??0);
  const cards=[
    ['① 身份',z(idt.canonical),'canonical 候选','plugin '+(idt.class?.plugin??'-')+' · 隔离 '+(idt.quarantine??'-'),''],
    ['② 容器',runP+'<small>/'+(S.capacity?.limit??'-')+'</small>','pod 运行中','promoted '+(c.promoted??0)+' / dispatched '+(c.dispatched??0),'hot'],
    ['③ 判定',z(S.total_results??0),'结果总数','24h 新增 '+d24,'ok'],
    ['④ 跳过',S.last24h?.skipped??0,'24h 跳过',Object.entries(S.skip_composition||{}).slice(0,3).map(([k,v])=>k+' '+v).join(' · ')||'-',''],
    ['⑤ 待定',S.last24h?.inconclusive??0,'24h 待定','30min 自动重试','warn'],
    ['⑥ 链路',S.k8s?.available?'API ✓':'API ✗','k8s','镜像 '+esc(String(S.image||'-').slice(0,24)),''],
  ];
  $('pipe').innerHTML=cards.map(c=>`<div class="st ${c[4]}"><div class=no>${c[0]}</div><b>${c[1]}</b><div class=cap>${c[3]}</div></div>`).join('');
}
async function loadTrend(){
  try{renderTrend(await j('/api/trend.json'))}catch(e){}
}
function renderTrend(t){
  if(!Array.isArray(t)||!t.length)return;
  const mk=(title,vals,color)=>{
    const mx=Math.max(1,...vals), w=100/vals.length;
    const bars=vals.map((v,i)=>v<=0?'':`<rect x="${(i*w+.4).toFixed(2)}" y="${(34-28*v/mx).toFixed(1)}" width="${Math.max(w-1,.8).toFixed(2)}" height="${(28*v/mx+.6).toFixed(1)}" fill="${color}" opacity="${(.3+.7*v/mx).toFixed(2)}"/>`).join('');
    const last=vals.slice(-6).reduce((a,b)=>a+b,0);
    return `<div class=tr><div class=tt>${title}</div><div class=tv style="color:${color}">${last}<small style="color:var(--dim);font-size:11px"> 近6h</small></div><svg class=bars viewBox="0 0 100 34" preserveAspectRatio=none>${bars}</svg></div>`;
  };
  $('trends').innerHTML=
    mk('判定吞吐 /h',t.map(b=>b.pass+b.fail+b.skipped+b.inconclusive),'#22D3EE')+
    mk('通过 /h',t.map(b=>b.pass),'#34D399')+
    mk('待定 /h',t.map(b=>b.inconclusive),'#F5A623');
}
async function loadVerdicts(append){
  const q=$('q').value.trim(), st=$('fs').value, rs=$('fr').value;
  const lim=append?LIMIT:Math.max(LIMIT,rows.length);
  const u=`/api/verdicts.json?offset=${append?rows.length:0}&limit=${lim}&status=${st}&reason=${encodeURIComponent(rs)}&q=${encodeURIComponent(q)}`;
  try{
    const d=await j(u); total=d.total;
    const news=d.rows.filter(r=>!seen.has(r.local_key));
    news.forEach(r=>seen.add(r.local_key));
    if(append){d.rows.forEach(r=>{if(!rows.some(x=>x.local_key===r.local_key))rows.push(r)})}
    else{
      const fresh=rows.length>0?news.map(r=>r.local_key):null;
      rows=d.rows;
      renderRows(fresh);
    }
    if(append)renderRows();
    $('loadinfo').textContent=`${rows.length}/${total}`;
    $('more').style.display=rows.length<total?'block':'none';
    const cur=$('fr').value;
    const reasons=d.reasons||[];
    if($('fr').dataset.sig!==String(reasons.length)){ $('fr').dataset.sig=String(reasons.length);
      $('fr').innerHTML='<option value="">全部原因</option>'+reasons.map(r=>`<option ${r===cur?'selected':''}>${esc(r)}</option>`).join(''); }
  }catch(e){$('loadinfo').textContent='加载失败 '+esc(e.message)}
}
function stageCell(r){
  if(!r.stages||!r.stages.length)return '<span class=rsn>—</span>';
  return r.stages.map(s=>`<span style="font:600 10px var(--mono);color:${s[1]?'#34D399':'#F87171'}">${esc(String(s[0]).split('-')[0].toUpperCase())}${s[1]?'✓':'✗'}</span>`).join(' ');
}
const rowHtml=r=>`<tr class="${r.status==='pass'?'sp':r.status==='fail'?'sf':r.status==='inconclusive'?'si':'ss'}" data-lk="${esc(r.local_key)}">
    <td class=lk>${esc(r.local_key)}</td>
    <td><span class=st2>${STZH[r.status]||r.status}</span></td>
    <td class=rsn>${esc((r.result||'—').slice(0,60))}</td>
    <td>${stageCell(r)}</td>
    <td class=tm>${esc((r.observed_at||'').slice(11,19))}</td></tr>`;
let lastSig='';
function renderRows(freshKeys){
  const fk=new Set(freshKeys||[]);
  if(fk.size){ // 增量：仅插入新行，先移除同 key 旧行防重复；不触碰展开行
    fk.forEach(lk=>{const t=$('tb').querySelector('tr[data-lk="'+lk.replace(/"/g,'\\"')+'"]');if(t&&t!==expanded)t.remove()});
    const fresh=rows.filter(r=>fk.has(r.local_key));
    if(!expanded)$('tb').insertAdjacentHTML('afterbegin',fresh.map(r=>`<tr class="${r.status==='pass'?'sp':r.status==='fail'?'sf':r.status==='inconclusive'?'si':'ss'} fresh" data-lk="${esc(r.local_key)}">
    <td class=lk>${esc(r.local_key)}</td>
    <td><span class=st2>${STZH[r.status]||r.status}</span></td>
    <td class=rsn>${esc((r.result||'—').slice(0,60))}</td>
    <td>${stageCell(r)}</td>
    <td class=tm>${esc((r.observed_at||'').slice(11,19))}</td></tr>`).join(''));
    $('vcount').textContent=`（${rows.length}/${total}）`;
    bindRows(); lastSig='';
    return;
  }
  const sig=rows.slice(0,60).map(r=>r.local_key+r.status).join('|');
  if(expanded||sig===lastSig)return; // 展开详情时冻结重渲染；无变化不重绘
  lastSig=sig;
  $('tb').innerHTML=rows.map(rowHtml).join('');
  $('vcount').textContent=`（${rows.length}/${total}）`;
  bindRows();
}
function bindRows(){
  $('tb').querySelectorAll('tr[data-lk]').forEach(tr=>{
    if(tr.dataset.bound)return;tr.dataset.bound=1;
    tr.onclick=async ev=>{
      if(ev.target.closest('pre'))return;
      const lk=tr.dataset.lk;
      if(expanded){const old=expanded;expanded=null;old.remove();if(old.dataset.lk===lk)return}
      let d;try{d=await j('/api/verdict/'+encodeURIComponent(lk)+'.json')}catch(e){return}
      const det=document.createElement('tr');det.className='det';det.dataset.lk=lk;
      det.innerHTML=`<td colspan=5>
        <span class=kv>attempt ${d.attempt??'-'} · tries ${d.tries??'-'} · npm ${esc(d.npm_status||'-')}</span>
        <span class=kv>input ${esc(String(d.input_hash||'').slice(0,16))}…</span>
        <span class=kv>observed ${esc(d.observed_at||'')}</span>
        <pre class=ev>${esc(d.last_error||d.result||'(无错误详情)')}</pre></td>`;
      tr.after(det);expanded=det;
    };
  });
}
$('more').onclick=()=>loadVerdicts(true);
let deb;$('q').oninput=()=>{clearTimeout(deb);deb=setTimeout(()=>loadVerdicts(false),300)};
$('fs').onchange=$('fr').onchange=()=>loadVerdicts(false);
async function tick(){await Promise.all([loadSummary(),loadTrend()]);if($('q').value.trim()===''&&$('fs').value==='')loadVerdicts(false)}
loadSummary();loadTrend();loadVerdicts(false);
setInterval(tick,1000);
</script></body></html>"""


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _json(self, doc, code=200):
        body = json.dumps(doc, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/healthz":
            ps = read_json_cached(STATE) or {}
            self._json({"ok": True,
                        "state_age_s": (time.time() - STATE.stat().st_mtime)
                        if STATE.exists() else None,
                        "phase": ps.get("phase"),
                        "due": (ps.get("current") or {}).get("due"),
                        "capacity_used": (ps.get("capacity") or {}).get("used")})
            return
        if u.path in ("/", "/index.html"):
            body = PAGE.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if u.path == "/api/summary.json":
            try:
                self._json(summary())
            except Exception as e:  # noqa: BLE001 — 看板接口需兜底不崩服务
                self._json({"error": str(e)}, 500)
            return
        if u.path == "/api/trend.json":
            self._json(trend_24h(IDX.rows()))
            return
        if u.path == "/api/verdicts.json":
            q = parse_qs(u.query)
            off = int(q.get("offset", ["0"])[0])
            lim = min(int(q.get("limit", ["20"])[0]), 200)
            st = q.get("status", [""])[0]
            reason = q.get("reason", [""])[0]
            kw = q.get("q", [""])[0].lower()
            rows = IDX.rows()
            filt = rows
            if st:
                filt = [r for r in filt if r["status"] == st]
            if reason:
                filt = [r for r in filt if reason_of(r) == reason]
            if kw:
                filt = [r for r in filt if kw in r["local_key"].lower()]
            self._json({"total": len(filt), "offset": off, "rows": filt[off:off + lim],
                        "reasons": sorted({reason_of(r) for r in rows})})
            return
        m = re.match(r"^/api/verdict/([^/]+)\.json$", u.path)
        if m:
            lk = m.group(1)
            if "/" in lk or ".." in lk:
                self._json({"error": "bad-key"}, 400)
                return
            p = RESULTS / f"{lk}.json"
            if not p.exists():
                self._json({"error": "not-found"}, 404)
                return
            self._json(read_json(p, {"error": "read-failed"}))
            return
        self.send_response(404)
        self.end_headers()


if __name__ == "__main__":
    print(f"dashboard v3 on 0.0.0.0:{PORT}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
