#!/usr/bin/env python3
# TIER 3 - BUILDS THAT PAY RENT, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips,
# NO clip-path cuts, NO extruded walls. Warm palette. Ultron prices = cents; revenue figures are fine.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"          # warm kraft accent
IVA="#96562d"              # ivory-card accent (warm burnt)
BAD="200,70,35"            # muted red, only for the bad/dead thing
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. TRAPD - split ledger: the attention it earns (stars/forks, warm bars, lit) vs the money it
# earns (one big struck $0). The demo-repo trap in one glance.
def trapd():
    metrics=[("Stars","2,431",1.0),("Forks","318",0.40),("Watchers","190",0.24)]
    bars=""
    for nm,val,frac in metrics:
        bars+=(f'<div style="margin-bottom:20px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:7px">'
          f'<span style="font-family:DM Mono;font-size:15px;letter-spacing:.06em;color:#c9c3b8">{nm}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:24px;color:#FAFAF7">{val}</span></div>'
          f'<div style="height:14px;border-radius:8px;background:rgba(255,255,255,.06)">'
          f'<div style="height:14px;width:{frac*100:.0f}%;border-radius:8px;background:linear-gradient(90deg,#8a4c2c,rgb({ACC}));box-shadow:0 0 16px rgba({ACC},.4)"></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Stars are not deposits","THE DEMO TRAP")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1;background:#211d19;border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:26px 26px 8px">
          <div style="display:flex;align-items:center;gap:11px;margin-bottom:22px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="rgb({ACC})"><path d="M12 2l2.9 6.3 6.9.6-5.2 4.6 1.6 6.8L12 17.3 5.8 20.9l1.6-6.8L2.2 8.9l6.9-.6z"/></svg>
            <span style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#8f8f85">founder-agent-demo</span></div>
          {bars}</div>
        <div style="flex-shrink:0;width:300px;background:linear-gradient(160deg,#2a1712,#1e1310);border:1px solid rgba({BAD},.34);border-radius:22px;padding:30px 26px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#a2887c">DEPOSITED TO DATE</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:96px;color:rgb({BAD});line-height:1;margin:10px 0">$0</span>
          <span style="font-family:DM Sans;font-size:16px;color:#a2887c">12 months live &middot; 0 invoices</span></div>
      </div>
      {cap("collects stars, forks and watchers. it has never once collected a dollar.")}</div>'''

# 2. BUILD1 - nightly pipeline timeline: a moon band on top, 3 stages left->right (source, brief,
# park), counts flowing, ending at a "waits for your tap" gate.
def build1():
    stages=[("02:00","SOURCE","341","ICP accounts pulled"),
            ("02:14","BRIEF","341","one-pagers written"),
            ("06:30","PARK","341","openers queued")]
    W,H=812,300
    cards=""; x0=8; cw=232; gap=44
    for i,(t,nm,n,sub) in enumerate(stages):
        x=x0+i*(cw+gap)
        cards+=(f'<g><rect x="{x}" y="60" width="{cw}" height="176" rx="20" fill="url(#stg)" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x+24}" y="98" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({ACC})">{t}</text>'
          f'<text x="{x+24}" y="146" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x+24}" y="184" font-family="DM Sans" font-weight="900" font-size="40" fill="#FAFAF7">{n}</text>'
          f'<text x="{x+24}" y="212" font-family="DM Sans" font-size="15" fill="#8f8f85">{sub}</text></g>')
        if i<2:
            ax=x+cw+8
            cards+=f'<path d="M{ax} 148 h{gap-16}" stroke="rgb({ACC})" stroke-width="4" marker-end="url(#ar)"/>'
    stars="".join(f'<circle cx="{40+j*47}" cy="{18+(j%3)*9}" r="1.7" fill="rgba(255,255,255,.5)"/>' for j in range(16))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The lead machine runs at night","WEEKEND BUILD")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="stg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <radialGradient id="moon" cx="38%" cy="34%"><stop offset="0%" stop-color="#f3e6d0"/><stop offset="100%" stop-color="#c8a882"/></radialGradient>
          <marker id="ar" markerWidth="10" markerHeight="10" refX="7" refY="5" orient="auto"><path d="M0 0 L8 5 L0 10 z" fill="rgb({ACC})"/></marker>
        </defs>
        <rect x="0" y="0" width="{W}" height="40" rx="12" fill="#191712"/>{stars}
        <circle cx="{W-40}" cy="20" r="13" fill="url(#moon)"/><circle cx="{W-46}" cy="16" r="11" fill="#191712"/>
        {cards}
      </svg>
      {cap("sources your ICP nightly, briefs every account, parks the openers for your tap.")}</div>'''

# 3. BUILD2 - circular follow-up loop (IVORY): 4 stations on a ring with curved arrows, a red
# "silence" branch that loops back to fire, center = zero dropped.
def build2():
    cx,cy,R=225,220,150
    stations=[("SEND","opener out",-90),("WAIT","3 days",0),("FIRE","on silence",90),("DRAFT","on reply",180)]
    ring=""; labels=""
    pts=[]
    for nm,sub,a in stations:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a)); pts.append((x,y))
    for i,(nm,sub,a) in enumerate(stations):
        x,y=pts[i]
        ring+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#fff" stroke="rgba(150,90,45,.30)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a2016">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="{IVA}">{sub}</text>')
    arcs=""
    for i in range(4):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%4]
        mx,my=(x1+x2)/2,(y1+y2)/2
        # push control point outward from centre
        dx,dy=mx-cx,my-cy; L2=math.hypot(dx,dy); ox,oy=mx+dx/L2*36,my+dy/L2*36
        arcs+=f'<path d="M{x1:.0f} {y1:.0f} Q{ox:.0f} {oy:.0f} {x2:.0f} {y2:.0f}" fill="none" stroke="{IVA}" stroke-width="3" marker-end="url(#la)" opacity="0.8"/>'
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px;display:flex;align-items:center;gap:26px">
      <svg width="450" height="450" viewBox="0 0 450 450" style="flex-shrink:0">
        <defs><marker id="la" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L7 4.5 L0 9 z" fill="{IVA}"/></marker></defs>
        {arcs}
        <circle cx="{cx}" cy="{cy}" r="66" fill="#fff" stroke="rgba(150,90,45,.22)" stroke-width="2"/>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="{IVA}">0</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#8a745a">dropped</text>
        {ring}
      </svg>
      <div style="flex:1">
        {htitle("The follow-up loop","ZERO DROPPED","#2a2016",IVA)}
        <div style="font-family:DM Sans;font-size:19px;color:#3a2c1e;line-height:1.5">A thread goes quiet, it fires. A reply lands, it drafts. Nothing waits on your memory, and nothing falls out of the pipe.</div>
        {cap("fires on silence, drafts on replies, logs every touch to the pipeline.","#8a745a")}
      </div></div>'''

# 4. BUILD3 - content desk: one line at left feeds a 2x7 grid of 14 mini-post tiles (a fortnight),
# each tile a tiny post mock (dot + text lines), all in your voice, gated.
def build3():
    days=["M","T","W","T","F","S","S"]
    tiles=""; tw=94; th=118; gx=16; gy=16; x0=200; y0=44
    n=0
    for row in range(2):
        for col in range(7):
            x=x0+col*(tw+gx); y=y0+row*(th+gy); n+=1
            fill = n<=14
            body= (f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="12" fill="url(#tile)" stroke="rgba(255,255,255,.10)"/>'
                   f'<circle cx="{x+18}" cy="{y+20}" r="8" fill="rgb({ACC})"/>'
                   f'<rect x="{x+32}" y="{y+15}" width="42" height="6" rx="3" fill="rgba(250,250,247,.34)"/>'
                   f'<rect x="{x+14}" y="{y+42}" width="{tw-28}" height="6" rx="3" fill="rgba(250,250,247,.20)"/>'
                   f'<rect x="{x+14}" y="{y+56}" width="{tw-40}" height="6" rx="3" fill="rgba(250,250,247,.20)"/>'
                   f'<rect x="{x+14}" y="{y+70}" width="{tw-24}" height="6" rx="3" fill="rgba(250,250,247,.14)"/>'
                   f'<rect x="{x+14}" y="{y+th-24}" width="30" height="12" rx="6" fill="rgba(212,162,127,.18)" stroke="rgba(212,162,127,.4)"/>'
                   f'<text x="{x+29}" y="{y+th-15}" text-anchor="middle" font-family="DM Mono" font-size="8" fill="rgb({ACC})">GATED</text>')
            tiles+=body
    daylbl="".join(f'<text x="{x0+c*(tw+gx)+tw/2:.0f}" y="30" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#7a746a">{d}</text>' for c,d in enumerate(days))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("The content desk","14 / WEEK")}
      <svg width="812" height="320" viewBox="0 0 812 320" style="display:block;margin:0 auto">
        <defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#302c28"/><stop offset="100%" stop-color="#201d1a"/></linearGradient></defs>
        {daylbl}
        <rect x="8" y="94" width="160" height="120" rx="18" fill="url(#tile)" stroke="rgba(212,162,127,.34)"/>
        <text x="88" y="140" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb({ACC})">ONE LINE</text>
        <text x="88" y="176" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">"ship it"</text>
        <path d="M172 154 h22" stroke="rgb({ACC})" stroke-width="4" marker-end="url(#a2)"/>
        <defs><marker id="a2" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L7 4.5 L0 9 z" fill="rgb({ACC})"/></marker></defs>
        {tiles}
      </svg>
      {cap("fourteen posts a week from one line, written in your voice, every draft gated.")}</div>'''

# 5. STACK8 - triadic cycle: 3 builds (CONTENT, LEADS, LOOPS) in a triangle, clockwise arrows,
# central Ultron-warm core = one memory, one gate.
def stack8():
    cx,cy,R=406,220,158
    builds=[("CONTENT","warms leads",-90),("LEADS","feed loops",30),("LOOPS","close deals",150)]
    verbs=["warms","feeds","closes"]
    pts=[]
    for nm,sub,a in builds:
        pts.append((cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))))
    arcs=""
    for i in range(3):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%3]
        mx,my=(x1+x2)/2,(y1+y2)/2; dx,dy=mx-cx,my-cy; Ln=math.hypot(dx,dy); ox,oy=mx+dx/Ln*56,my+dy/Ln*56
        lx,ly=mx+dx/Ln*90,my+dy/Ln*90
        arcs+=(f'<path d="M{x1:.0f} {y1:.0f} Q{ox:.0f} {oy:.0f} {x2:.0f} {y2:.0f}" fill="none" stroke="rgba(212,162,127,.6)" stroke-width="3.5" marker-end="url(#sa)"/>'
          f'<text x="{lx:.0f}" y="{ly+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">{verbs[i]}</text>')
    nodes=""
    for i,(nm,sub,a) in enumerate(builds):
        x,y=pts[i]
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="64" fill="url(#nb)" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+21:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Three builds, one system","COMPOUNDING")}
      <svg width="812" height="404" viewBox="0 0 812 404" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="core" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <radialGradient id="nb" cx="38%" cy="30%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1c1a17"/></radialGradient>
          <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
          <marker id="sa" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L7 4.5 L0 9 z" fill="rgb({ACC})"/></marker>
        </defs>
        {arcs}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="80" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#3a2010">one gate</text>
        {nodes}
      </svg>
      {cap("content warms leads, leads feed loops, loops close - all on one shared memory.")}</div>'''

# 6. RECEIPTS8 - conversion invoice (IVORY): 3 rows, each build's soft output -> its money output,
# with a stamped total. Revenue figures (rent paid) are real, not cents.
def receipts8():
    rows=[("Briefs","booked calls","31 calls","$0"),
          ("Threads","closed invoices","$18,400",""),
          ("Posts","inbound demos","22 demos","$0")]
    lines=""
    conv=[("Briefs sourced","became","31 sales calls"),
          ("Follow-up threads","became","$18,400 invoiced"),
          ("Daily posts","became","22 inbound demos")]
    for a,mid,b in conv:
        lines+=(f'<div style="display:flex;align-items:center;gap:14px;padding:18px 4px;border-bottom:1px dashed rgba(120,95,60,.28)">'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:19px;color:#3a2c1e">{a}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#a08a68">{mid}</span>'
          f'<svg width="26" height="14" viewBox="0 0 26 14" style="flex-shrink:0"><path d="M2 7 h18 M15 2 l6 5 -6 5" fill="none" stroke="{IVA}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="flex:1;text-align:right;font-family:DM Sans;font-weight:900;font-size:22px;color:{IVA}">{b}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("Every build files a receipt","IN MONEY TERMS","#2a2016",IVA)}
      <div style="background:rgba(255,255,255,.55);border:1px solid rgba(150,120,80,.22);border-radius:20px;padding:10px 24px 20px;position:relative">
        {lines}
        <div style="display:flex;align-items:baseline;justify-content:space-between;padding:20px 4px 4px">
          <span style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:#8a745a">BOOKED THIS QUARTER</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016">$41,600</span></div>
        <div style="position:absolute;bottom:30px;left:39%;transform:rotate(-9deg);border:2.5px solid rgba({BAD},.5);border-radius:10px;padding:5px 15px;font-family:DM Mono;font-weight:500;font-size:15px;letter-spacing:.2em;color:rgb({BAD})">PAID</div>
      </div>
      {cap("run cost was cents. briefs became calls, threads became invoices, posts became inbound.","#8a745a")}</div>'''

# 7. TIME8 - build-time comparison on a labelled week axis: a tiny lit evening bar (ships 3 builds)
# against a long muted semester bar that ships nothing. Ticks + labels fill the band, no collisions.
def time8():
    W,H=812,336
    x0=48; x1=764; span=x1-x0
    weeks=[0,4,8,12,16]
    ticks=""
    for w in weeks:
        gx=x0+span*w/16
        ticks+=(f'<line x1="{gx:.0f}" y1="70" x2="{gx:.0f}" y2="286" stroke="rgba(255,255,255,.07)"/>'
          f'<text x="{gx:.0f}" y="312" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#7a746a">{("start" if w==0 else str(w)+"w")}</text>')
    ev_w=span*0.6/16  # ~half a week visual
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("An evening, not a semester","BUILD TIME")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="ev" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8a4c2c"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        {ticks}
        <text x="{x0}" y="118" font-family="DM Sans" font-weight="700" font-size="19" fill="#c9c3b8">The desk build</text>
        <rect x="{x0}" y="132" width="{ev_w:.0f}" height="56" rx="14" fill="url(#ev)" style="filter:drop-shadow(0 0 22px rgba(212,162,127,.4))"/>
        <text x="{x0+ev_w+22:.0f}" y="168" font-family="DM Sans" font-weight="900" font-size="27" fill="#FAFAF7">~4 hrs</text>
        <g transform="translate({x0+ev_w+180:.0f},150)">
          <rect x="0" y="0" width="196" height="38" rx="19" fill="rgba(127,211,154,.12)" stroke="rgba(212,162,127,.4)"/>
          <path d="M18 19 l7 7 l13 -16" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="50" y="25" font-family="DM Sans" font-weight="700" font-size="16" fill="#e6d6c2">3 builds live</text></g>
        <text x="{x0}" y="230" font-family="DM Sans" font-weight="700" font-size="19" fill="#8f8f85">A semester course</text>
        <rect x="{x0}" y="244" width="{span:.0f}" height="46" rx="14" fill="rgba(200,70,35,.13)" stroke="rgba({BAD},.4)"/>
        <line x1="{x0+14}" y1="267" x2="{x1-120}" y2="267" stroke="rgba({BAD},.7)" stroke-width="2.5"/>
        <text x="{x1-16:.0f}" y="273" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="19" fill="rgb({BAD})">16 weeks</text></svg>
      {cap("described in plain English, assembled by the desk, tested on your real pipeline.")}</div>'''

# 8. FILTER8 - decision fork: one question splits into a paying YES lane (accent) and an honest
# hobby NO lane (neutral, labelled).
def filter8():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One question decides","THE PAY TEST")}
      <svg width="812" height="440" viewBox="0 0 812 440" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="qd" cx="40%" cy="32%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1c1a17"/></radialGradient>
          <marker id="fa" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L7 4.5 L0 9 z" fill="rgb({ACC})"/></marker>
          <filter id="qg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter>
        </defs>
        <g filter="url(#qg)"><rect x="256" y="24" width="300" height="96" rx="22" fill="url(#qd)" stroke="rgb({ACC})" stroke-width="2"/></g>
        <text x="406" y="66" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#FAFAF7">Would a client</text>
        <text x="406" y="98" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="rgb({ACC})">pay for this?</text>
        <path d="M330 120 C300 180,220 190,190 232" fill="none" stroke="rgb({ACC})" stroke-width="3.5" marker-end="url(#fa)"/>
        <path d="M482 120 C512 180,592 190,622 232" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="3.5" stroke-dasharray="4 8" marker-end="url(#fa)"/>
        <text x="250" y="196" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="16" letter-spacing=".1em" fill="rgb({ACC})">YES</text>
        <text x="566" y="196" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="16" letter-spacing=".1em" fill="#8f8f85">NO</text>
        <rect x="40" y="248" width="300" height="150" rx="20" fill="url(#qd)" stroke="rgb({ACC})" stroke-width="2"/>
        <text x="190" y="300" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="27" fill="#FAFAF7">Ship it.</text>
        <text x="190" y="338" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#c9a583">It invoices.</text>
        <text x="190" y="372" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="rgb({ACC})">rent paid</text>
        <rect x="472" y="248" width="300" height="150" rx="20" fill="#211d19" stroke="rgba(255,255,255,.10)"/>
        <text x="622" y="300" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="27" fill="#c9c3b8">It's a hobby.</text>
        <text x="622" y="338" text-anchor="middle" font-family="DM Sans" font-size="18" fill="#8f8f85">Fine. Label it.</text>
        <text x="622" y="372" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#8f8f85">no rent</text>
      </svg>
      {cap("if a client would not pay for it, it is a hobby. hobbies are fine, labelled honestly.")}</div>'''

PANELS={"trapd":trapd(),"build1":build1(),"build2":build2(),"build3":build3(),
        "stack8":stack8(),"receipts8":receipts8(),"time8":time8(),"filter8":filter8()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/proofstack"; os.makedirs(outd,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":960,"height":900},device_scale_factor=2)
        for name,html in PANELS.items():
            full=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{Lm.css(ACC)}</style></head><body style='padding:30px'>{html}</body></html>"
            pg.set_content(full); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{outd}/{name}.png",omit_background=True,full_page=True)
            print("rendered",name)
        b.close()
    print("done")
