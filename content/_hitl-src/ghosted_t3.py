#!/usr/bin/env python3
# TIER 3 - WHY COLD EMAILS DIE (slug: ghosted), rebuilt to the WIRE-ITS-EYES / AI-BODY bar:
# each of the 8 panels is a UNIQUE hand-built coded scene filling a clean rounded card, a title +
# one-line mono caption, NO generic stat-chip strip, NO clip-path cuts, NO extruded walls.
# Warm palette: accent rgb(212,162,127), ivory-accent #96562d, muted red rgb(200,70,35) for
# dead/bounced states only. Cost zero. Overwrites models_clay/ghosted/*.png.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def ititle(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SENT - split fate: two identical drafts, one lands INBOX, one goes SPAM. Envelope scene.
def sent():
    def env(col): return (f'<svg width="66" height="50" viewBox="0 0 66 50"><rect x="2" y="3" width="62" height="44" rx="8" fill="none" stroke="{col}" stroke-width="2.6"/>'
        f'<path d="M5 8 L33 30 L61 8" fill="none" stroke="{col}" stroke-width="2.6" stroke-linecap="round"/></svg>')
    def lines(): return ('<div style="margin-top:16px">'
        + "".join(f'<div style="height:8px;border-radius:4px;background:rgba(250,250,247,.12);margin-bottom:9px;width:{w}"></div>' for w in ("100%","100%","72%"))
        + '</div>')
    def col(col,lit,badge,ico,bg,bd):
        return (f'<div style="flex:1;background:{bg};border:1.5px solid {bd};border-radius:20px;padding:24px 24px 22px">'
          f'{env(col)}{lines()}'
          f'<div style="display:flex;align-items:center;gap:10px;margin-top:20px;background:{lit};border-radius:12px;padding:11px 16px">'
          f'{ico}<span style="font-family:\'DM Sans\';font-weight:900;font-size:19px;color:{col};letter-spacing:.02em">{badge}</span></div></div>')
    chk=f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
    ex=f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({RED})" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
    left=col(f"rgb({ACC})","rgba(212,162,127,.12)","INBOX",chk,"linear-gradient(160deg,#332f2a,#221e1a)","rgba(212,162,127,.3)")
    right=col(f"rgb({RED})","rgba(200,70,35,.12)","SPAM",ex,"linear-gradient(160deg,#2a2320,#201917)","rgba(200,70,35,.28)")
    mid=('<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;justify-content:center;width:96px;align-self:center">'
      f'<div style="width:52px;height:52px;border-radius:50%;border:1.5px solid rgba(255,255,255,.14);display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:26px;color:#c9c3b8">=</div>'
      '<div style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.12em;color:#7a746a;margin-top:10px;text-align:center">SAME<br>COPY</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Identical copy, split fate","SAME DRAFT")}
      <div style="display:flex;align-items:stretch;gap:8px">{left}{mid}{right}</div>
      {cap("word for word the same send. the difference was never the writing.")}</div>'''

# 2. OPENS - vanity vs real: fat OPENS bar (greyed, tracked) over a thin REPLIES bar (accent),
# with a crossed-out tracking-pixel chip that costs inbox placement.
def opens():
    def bar(label,pct,val,fill,txt,tag,tagcol):
        return (f'<div style="margin-bottom:22px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:9px">'
          f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#e6e1d6">{label} <span style="font-family:\'DM Mono\';font-size:13px;color:{tagcol};margin-left:6px">{tag}</span></span>'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:30px;color:{txt}">{val}</span></div>'
          f'<div style="height:34px;border-radius:9px;background:rgba(250,250,247,.06);overflow:hidden">'
          f'<div style="height:100%;width:{pct};background:{fill};border-radius:9px"></div></div></div>')
    b1=bar("Opens","61%","61%","linear-gradient(90deg,rgba(250,250,247,.22),rgba(250,250,247,.34))","#9a9488","VANITY","#7a746a")
    b2=bar("Replies","5%","2.9%",f"linear-gradient(90deg,#9a5a35,rgb({ACC}))",f"rgb({ACC})","REAL",f"rgb({ACC})")
    pixel=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(200,70,35,.06);border:1px dashed rgba(200,70,35,.4);border-radius:14px;padding:14px 18px">'
      f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.12em;color:rgb({RED});flex-shrink:0">TRACKING PIXEL</span>'
      f'<span style="font-family:\'DM Sans\';font-size:17px;color:#a8a296;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">1x1 open beacon in every email</span>'
      f'<span style="margin-left:auto;font-family:\'DM Mono\';font-size:13px;color:rgb({RED});flex-shrink:0">-18% inbox</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Opens flatter. Replies pay.","VANITY VS REAL")}
      {b1}{b2}
      <div style="margin-top:6px">{pixel}</div>
      {cap("the pixel that counts your opens is the same pixel that sinks your placement.")}</div>'''

# 3. FRESH - IVORY: arc sender-score gauge pinned in the red, feeding a blast that lands in
# the promotions folder. (gauge = distinct form)
def fresh():
    cx,cy,R=270,250,180
    val=12
    def pt(v,rad):
        th=math.radians(180-(v/100)*180)
        return cx+rad*math.cos(th), cy-rad*math.sin(th)
    vx,vy=pt(val,R); nx,ny=pt(val,R*0.9)
    track=f'M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}'
    valarc=f'M{cx-R} {cy} A{R} {R} 0 0 1 {vx:.1f} {vy:.1f}'
    ticks=""
    for v in (0,25,50,75,100):
        ox,oy=pt(v,R+2); ix,iy=pt(v,R-16)
        ticks+=f'<line x1="{ix:.1f}" y1="{iy:.1f}" x2="{ox:.1f}" y2="{oy:.1f}" stroke="rgba(120,90,55,.4)" stroke-width="2.5"/>'
    flow=(f'<div style="display:flex;align-items:center;gap:14px;margin-top:6px">'
      f'<div style="background:#fff;border:1px solid rgba(150,90,45,.28);border-radius:14px;padding:13px 18px"><div style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:#2a2016">Fresh domain</div><div style="font-family:\'DM Mono\';font-size:12px;color:#8a745a">3 days old</div></div>'
      f'<div style="display:flex;flex-direction:column;align-items:center"><span style="font-family:\'DM Mono\';font-size:12px;color:#96562d">500 / day</span><svg width="70" height="18" viewBox="0 0 70 18" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9h56M52 3l8 6-8 6"/></svg></div>'
      f'<div style="background:rgba(200,70,35,.1);border:1px solid rgba(200,70,35,.4);border-radius:14px;padding:13px 18px"><div style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:rgb({RED})">Promotions</div><div style="font-family:\'DM Mono\';font-size:12px;color:#b06a4a">forever</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {ititle("Cold domain, hot volume","SENDER SCORE")}
      <div style="display:flex;align-items:center;gap:30px">
        <svg width="{cx+R+20}" height="{cy+30}" viewBox="0 0 {cx+R+20} {cy+30}" style="flex-shrink:0">
          <path d="{track}" fill="none" stroke="rgba(150,110,70,.16)" stroke-width="24" stroke-linecap="round"/>
          {ticks}
          <path d="{valarc}" fill="none" stroke="rgb({RED})" stroke-width="24" stroke-linecap="round"/>
          <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#2a2016" stroke-width="6" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="12" fill="#2a2016"/>
          <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#2a2016">{val}</text>
          <text x="{cx}" y="{cy-28}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#96562d">/ 100 REPUTATION</text>
        </svg>
        <div style="flex:1">{flow}</div>
      </div>
      {cap("no history plus max volume is a one-way ticket to the promotions tab.","#8a745a")}</div>'''

# 4. ONEDOMAIN - single load-bearing pillar carrying the whole pipeline, cracking; a dim
# 3-pillar "spread" alternative beside it. (architectural silhouette = distinct)
def onedomain():
    W,H=800,430
    weights="".join(f'<g><line x1="{x}" y1="34" x2="{x}" y2="70" stroke="rgba(212,162,127,.5)" stroke-width="3"/><path d="M{x-6} 62 L{x} 72 L{x+6} 62" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3" stroke-linecap="round"/></g>' for x in (130,230,330,430))
    segs=["leads","demos","deals","renewals","referrals"]
    chips=""
    for i,s in enumerate(segs):
        chips+=f'<text x="{92+i*80}" y="102" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#cfc9bd">{s}</text>'
    ghost=""
    for i in range(3):
        gx=610+i*52
        ghost+=(f'<rect x="{gx}" y="250" width="34" height="120" rx="7" fill="#211f1b" stroke="rgba(212,162,127,.28)" opacity="0.8"/>'
          f'<rect x="{gx-4}" y="368" width="42" height="12" rx="3" fill="rgba(212,162,127,.22)"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One pillar, whole pipeline","SINGLE POINT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block">
        <defs>
          <linearGradient id="pil" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#4a423a"/><stop offset="50%" stop-color="#332e28"/><stop offset="100%" stop-color="#211d19"/></linearGradient>
          <linearGradient id="slab" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#26221e"/></linearGradient>
        </defs>
        {weights}
        <rect x="52" y="76" width="456" height="46" rx="10" fill="url(#slab)" stroke="rgba(255,255,255,.1)"/>
        {chips}
        <rect x="250" y="122" width="60" height="240" rx="8" fill="url(#pil)" stroke="rgba(255,255,255,.09)"/>
        <path d="M280 150 L268 210 L292 236 L272 300 L286 358" fill="none" stroke="rgb({RED})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="330" y="250" font-family="DM Mono" font-size="13" fill="rgb({RED})">one bad batch</text>
        <text x="330" y="270" font-family="DM Mono" font-size="13" fill="rgb({RED})">burns it all</text>
        <rect x="214" y="362" width="132" height="20" rx="5" fill="#3a352f" stroke="rgba(255,255,255,.08)"/>
        <text x="280" y="404" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#eae4d8">acme-sales.com</text>
        <line x1="565" y1="150" x2="565" y2="380" stroke="rgba(255,255,255,.08)" stroke-dasharray="4 8"/>
        {ghost}
        <text x="662" y="404" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".06em" fill="#9a9488">spread: 3 domains</text>
      </svg>
      {cap("the sending domain is the only asset you truly own. never bet it on one blast.")}</div>'''

# 5. SPIKE - two send patterns as bar timelines: a steady ramp that lives vs a 0-to-500 blast
# that burns. (bar chart = distinct)
def spike():
    def chart(title,vals,cols,led,ledtxt,ledcol):
        base=250; maxh=190; mx=max(vals)
        bars=""
        bw=46; gap=18; x0=8
        for i,(v,c) in enumerate(zip(vals,cols)):
            h=max(8,v/mx*maxh); x=x0+i*(bw+gap)
            bars+=(f'<rect x="{x}" y="{base-h:.0f}" width="{bw}" height="{h:.0f}" rx="6" fill="{c}"/>'
              f'<text x="{x+bw/2:.0f}" y="{base+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{v}</text>')
        w=x0+len(vals)*(bw+gap)
        return (f'<div style="flex:1;background:linear-gradient(160deg,#2a2723,#201d1a);border:1.5px solid rgba(255,255,255,.08);border-radius:20px;padding:20px 22px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">'
          f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:#e6e1d6">{title}</span>'
          f'<span style="display:flex;align-items:center;gap:8px"><span style="width:11px;height:11px;border-radius:50%;background:{led};box-shadow:0 0 12px {led}"></span><span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.1em;color:{ledcol}">{ledtxt}</span></span></div>'
          f'<svg width="{w}" height="285" viewBox="0 0 {w} 285"><line x1="0" y1="250" x2="{w}" y2="250" stroke="rgba(255,255,255,.12)"/>{bars}<text x="4" y="278" font-family="DM Mono" font-size="11" fill="#6f6a60">sends / day</text></svg></div>')
    ramp=chart("Ramp",[40,60,90,140,210],[f"rgb({ACC})"]*5,"#7fd39a","ALIVE","#7fd39a")
    blast=chart("Blast",[0,0,0,20,500],["rgba(250,250,247,.14)","rgba(250,250,247,.14)","rgba(250,250,247,.14)","rgba(250,250,247,.2)",f"rgb({RED})"],f"rgb({RED})","BURNED",f"rgb({RED})")
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ramps live, blasts die","SEND PATTERN")}
      <div style="display:flex;gap:18px">{ramp}{blast}</div>
      {cap("mailbox providers read the curve. a cliff of 500 reads as an attack.")}</div>'''

# 6. CATCHALL - address dot field: verified sends vs catch-all/invalid ones that poison the batch.
# (dot field = distinct)
def catchall():
    cols,rows=20,12; total=cols*rows
    reds=set(); s=17
    while len(reds)<47:
        s=(s*29+13)%total; reds.add(s)
    cell,gap=20,8
    dots=""
    for i in range(total):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in reds:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="rgb({RED})" filter="url(#rg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="rgba(212,162,127,.42)"/>'
    fw=cols*(cell+gap)-gap; fh=rows*(cell+gap)-gap
    legend=(f'<div style="display:flex;gap:26px;margin-top:2px">'
      f'<span style="display:flex;align-items:center;gap:9px;font-family:\'DM Sans\';font-size:16px;color:#c9c3b8"><span style="width:14px;height:14px;border-radius:4px;background:rgba(212,162,127,.42)"></span>verified</span>'
      f'<span style="display:flex;align-items:center;gap:9px;font-family:\'DM Sans\';font-size:16px;color:#c9c3b8"><span style="width:14px;height:14px;border-radius:4px;background:rgb({RED})"></span>catch-all / invalid</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">Catch-alls poison the batch</span>
        <div style="text-align:right"><span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:rgb({RED})">47</span><span style="font-family:'DM Mono';font-size:13px;color:#8f8f85;margin-left:8px">of 240 unverified</span></div></div>
      <div style="display:flex;align-items:center;gap:36px">
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="flex-shrink:0">
          <defs><filter id="rg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({RED})" flood-opacity="0.9"/></filter></defs>
          {dots}</svg>
        <div style="flex:1">{legend}
          <div style="font-family:'DM Sans';font-size:18px;color:#a8a296;line-height:1.5;margin-top:20px">A hard bounce on an invalid address flags the <span style="color:rgb({ACC})">whole send</span>. The 193 real prospects pay for the 47 you never checked.</div></div>
      </div>
      {cap("verify the list first. one dead address drags every clean one down with it.")}</div>'''

# 7. INFRA - autopilot console: three infra rows running green with mini sparklines + uptime.
# (status console = distinct)
def infra():
    def spark(pts,col):
        p=" ".join(f'{i*16},{34-v}' for i,v in enumerate(pts))
        return f'<svg width="{len(pts)*16}" height="38" viewBox="0 0 {len(pts)*16} 38" fill="none" stroke="{col}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="{p}"/></svg>'
    rows=[("Warm-up schedule","domains aged 21 days before first send",[6,10,14,18,22,26,30],"running"),
          ("Send ramp","60 to 400 / day, step +20 daily",[8,12,10,16,20,24,28],"on track"),
          ("Spam-rate watch","0.02% complaints, alarms armed",[10,9,11,8,10,9,10],"healthy")]
    body=""
    for nm,sub,pts,st in rows:
        body+=(f'<div style="display:flex;align-items:center;gap:20px;background:linear-gradient(158deg,#332f2a,#221e1a);border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:16px 20px;margin-bottom:14px">'
          f'<span style="width:12px;height:12px;border-radius:50%;background:#7fd39a;box-shadow:0 0 12px #7fd39a;flex-shrink:0"></span>'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8f8f85;margin-top:1px">{sub}</div></div>'
          f'<div style="flex-shrink:0;opacity:.85">{spark(pts,f"rgb({ACC})")}</div>'
          f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.06em;color:#7fd39a;flex-shrink:0;width:70px;text-align:right">{st}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">The infra runs itself</span>
        <span style="display:flex;align-items:center;gap:10px;background:rgba(127,211,154,.12);border:1px solid rgba(127,211,154,.32);border-radius:999px;padding:7px 16px">
          <span style="width:9px;height:9px;border-radius:50%;background:#7fd39a"></span><span style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:#7fd39a">AUTOPILOT</span></span></div>
      {body}
      {cap("warm domains, ramped sends, watched complaints - handled, so you never think about it.")}</div>'''

# 8. ROAD - IVORY closing: order-of-work. copy-letter turned away at a locked mailbox on a
# dead road. (illustrative road scene = distinct closing)
def road():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {ititle("Fix the road first","ORDER OF WORK")}
      <svg width="760" height="360" viewBox="0 0 760 360" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="rd" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#c9b79a"/><stop offset="100%" stop-color="#e2d6c0"/></linearGradient>
          <linearGradient id="box" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#a06a44"/><stop offset="100%" stop-color="#7a4a2c"/></linearGradient>
        </defs>
        <polygon points="250,330 510,330 430,120 330,120" fill="url(#rd)" stroke="rgba(120,90,55,.35)" stroke-width="1.5"/>
        <line x1="380" y1="330" x2="380" y2="122" stroke="#f6efe2" stroke-width="6" stroke-dasharray="20 20"/>
        <g transform="translate(340,58)">
          <rect x="0" y="34" width="80" height="52" rx="10" fill="url(#box)" stroke="rgba(90,55,30,.4)"/>
          <path d="M0 46 a40 26 0 0 1 80 0" fill="#8a5636"/>
          <rect x="36" y="58" width="8" height="26" rx="3" fill="#5a3720"/>
          <g transform="translate(60,4)"><rect x="0" y="10" width="22" height="18" rx="4" fill="none" stroke="#96562d" stroke-width="3"/><path d="M4 10 V6 a7 7 0 0 1 14 0 v4" fill="none" stroke="#96562d" stroke-width="3"/></g>
        </g>
        <g transform="translate(150,236) rotate(-12)">
          <rect x="0" y="0" width="120" height="80" rx="8" fill="#fff" stroke="rgba(200,70,35,.5)" stroke-width="2"/>
          <path d="M6 8 L60 46 L114 8" fill="none" stroke="rgba(200,70,35,.6)" stroke-width="2.4"/>
          <text x="60" y="66" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({RED})">great copy</text>
        </g>
        <path d="M280 250 q26 -34 58 -30" fill="none" stroke="rgb({RED})" stroke-width="2.6" stroke-dasharray="5 6" stroke-linecap="round"/>
        <path d="M330 216 l10 4 l-3 -11" fill="rgb({RED})"/>
        <text x="470" y="300" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="#96562d">returned:</text>
        <text x="470" y="322" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="#96562d">box is locked</text>
      </svg>
      {cap("great copy on dead infra is a love letter in a locked mailbox.","#8a745a")}</div>'''

PANELS={"sent":sent(),"opens":opens(),"fresh":fresh(),"onedomain":onedomain(),
        "spike":spike(),"catchall":catchall(),"infra":infra(),"road":road()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/ghosted"; os.makedirs(outd,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":960,"height":900},device_scale_factor=2)
        CSS=Lm.css(ACC)
        for name,html in PANELS.items():
            full=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body style='padding:30px'>{html}</body></html>"
            pg.set_content(full); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{outd}/{name}.png",omit_background=True,full_page=True)
            print("rendered",name)
        b.close()
    print("done")
