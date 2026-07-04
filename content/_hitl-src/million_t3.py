#!/usr/bin/env python3
# TIER 3 - THE ONE-LAPTOP COMPANY, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagcol=None):
    tc=tagcol or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
      f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
      f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. NOTTEAM - side-by-side comparison: a dim team-of-20 headcount grid (high payroll $, the old way)
# VS one glowing laptop (cents), a vertical divider between them.
def notteam():
    people=""
    for i in range(20):
        r,c=divmod(i,5); x=c*44; y=r*46
        people+=(f'<g transform="translate({x},{y})" opacity="0.5"><circle cx="14" cy="11" r="9" fill="none" stroke="#6f6a60" stroke-width="2"/>'
          f'<path d="M1 34 a13 13 0 0 1 26 0Z" fill="none" stroke="#6f6a60" stroke-width="2"/>'
          f'<line x1="2" y1="2" x2="26" y2="36" stroke="rgba(200,70,35,.5)" stroke-width="1.6"/></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Twenty seats, or none","THE OLD MATH")}
      <div style="display:flex;align-items:stretch;gap:0;height:400px">
        <div style="flex:1;padding:14px 30px 14px 6px;display:flex;flex-direction:column;justify-content:center">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#8f8f85;margin-bottom:16px">TEAM OF 20</div>
          <svg width="234" height="228" viewBox="0 0 234 228">{people}</svg>
          <div style="margin-top:18px"><span style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#c9c3b8">$1.4M</span>
          <span style="font-family:'DM Sans';font-size:17px;color:#8f8f85;margin-left:8px">/ yr payroll</span></div>
        </div>
        <div style="width:1px;background:linear-gradient(180deg,transparent,rgba(255,255,255,.16),transparent);margin:20px 0"></div>
        <div style="flex:1;padding:14px 6px 14px 34px;display:flex;flex-direction:column;justify-content:center">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:20px">ONE LAPTOP</div>
          <svg width="250" height="200" viewBox="0 0 250 200">
            <defs><radialGradient id="scr" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
            <filter id="lg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
            <g filter="url(#lg)"><rect x="45" y="26" width="160" height="106" rx="12" fill="#201d19" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
            <rect x="58" y="40" width="134" height="78" rx="6" fill="url(#scr)"/></g>
            <text x="125" y="88" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">1</text>
            <path d="M22 168 L228 168 L212 138 L38 138 Z" fill="#2a2622" stroke="rgba(255,255,255,.12)" stroke-width="2"/>
            <rect x="104" y="150" width="42" height="7" rx="3.5" fill="rgba(255,255,255,.16)"/>
          </svg>
          <div style="margin-top:18px"><span style="font-family:'DM Sans';font-weight:900;font-size:40px;color:rgb({ACC})">cents</span>
          <span style="font-family:'DM Sans';font-size:17px;color:#c9a583;margin-left:8px">/ task, metered</span></div>
        </div>
      </div>
      {cap("not a funded startup, not twenty hires - one laptop and a bill measured in cents.")}</div>'''

# 2. AGENTS - node graph: one job splits into 4 parallel agent nodes, all reconverge on the founder GATE
def agents():
    W,H=820,430
    hx,hy=110,215          # source
    gx,gy=690,215          # founder gate
    nodes=[("RESEARCH",380,66),("OUTREACH",380,158),("CONTENT",380,272),("BUILDS",380,364)]
    edges=""; cards=""
    for nm,x,y in nodes:
        m1=(hx+x)/2; m2=(x+gx)/2
        edges+=f'<path d="M{hx+52} {hy} C{m1:.0f} {hy},{m1:.0f} {y},{x-2} {y}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
        edges+=f'<path d="M{x+150} {y} C{m2:.0f} {y},{m2:.0f} {gy},{gx-54} {gy}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
        cards+=(f'<rect x="{x}" y="{y-26}" width="150" height="52" rx="14" fill="url(#nd)" stroke="rgba(255,255,255,.12)"/>'
          f'<circle cx="{x+22}" cy="{y}" r="6" fill="rgb({ACC})" filter="url(#nb)"/>'
          f'<text x="{x+40}" y="{y+5}" font-family="DM Mono" font-size="15" letter-spacing="1.5" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Four agents, one tap","PARALLEL · GATED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="src" cx="36%" cy="30%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1c1a17"/></radialGradient>
        <linearGradient id="nd" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <radialGradient id="gt" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="nb" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
        <filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {edges}
        <circle cx="{hx}" cy="{hy}" r="52" fill="url(#src)" stroke="rgba(255,255,255,.10)"/>
        <text x="{hx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#e6d6c2">ONE</text>
        <text x="{hx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#9a9488">brief</text>
        {cards}
        <g filter="url(#gg)"><circle cx="{gx}" cy="{gy}" r="70" fill="url(#gt)"/></g>
        <g transform="translate({gx-24},{gy-34})"><rect x="0" y="20" width="48" height="34" rx="8" fill="none" stroke="#2a160c" stroke-width="5"/><path d="M9 20 V9 a15 15 0 0 1 30 0 v11" fill="none" stroke="#2a160c" stroke-width="5"/></g>
        <text x="{gx}" y="{gy+52}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">YOUR TAP</text>
      </svg>
      {cap("research, outreach, content, builds - run in parallel, released only on your tap.")}</div>'''

# 3. REVENUE (ivory) - dual chart: revenue bars climbing +32% while a flat headcount line stays at 1
def revenue():
    months=["Jan","Feb","Mar","Apr","May","Jun"]
    vals=[38,44,49,58,66,87]  # index, ends +32% on last step feel
    W,H=680,360; bw=64; gap=40; base=300; x0=64
    bars=""; hx=[]
    for i,v in enumerate(vals):
        x=x0+i*(bw+gap); h=v*2.6; y=base-h
        bars+=(f'<rect x="{x}" y="{y:.0f}" width="{bw}" height="{h:.0f}" rx="8" fill="url(#bar)"/>'
          f'<text x="{x+bw/2:.0f}" y="{base+26}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#8a745a">{months[i]}</text>')
        hx.append((x+bw/2,base-40))
    flat=" ".join(f"{px:.0f},{py:.0f}" for px,py in hx)
    dots="".join(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="6" fill="#463d34"/>' for px,py in hx)
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("Revenue up, roster flat","+32% THIS MONTH","#2a2016","#96562d")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c2733f"/><stop offset="100%" stop-color="#96562d"/></linearGradient></defs>
        <line x1="{x0-14}" y1="{base}" x2="{W-20}" y2="{base}" stroke="rgba(120,95,60,.35)" stroke-width="2"/>
        {bars}
        <polyline points="{flat}" fill="none" stroke="#463d34" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>
        {dots}
        <rect x="{W-140}" y="30" width="120" height="34" rx="8" fill="rgba(70,61,52,.10)" stroke="rgba(120,95,60,.3)"/>
        <text x="{W-80}" y="52" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#5a4634">headcount 1</text>
      </svg>
      {cap("bars compound month over month; the headcount line never leaves 1 - payroll flat since day zero.","#8a745a")}</div>'''

# 4. SPEED - two horizontal timeline lanes: idea->live offer (an afternoon), feedback->fix (an hour)
def speed():
    def lane(y,label,steps,total):
        seg=""; n=len(steps); span=680; x0=70
        for i,(t,) in enumerate(steps):
            x=x0+i*(span/(n-1))
            seg+=f'<circle cx="{x:.0f}" cy="{y}" r="11" fill="url(#dot)" stroke="rgb({ACC})" stroke-width="2"/>'
            seg+=f'<text x="{x:.0f}" y="{y+34}" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#d9d5cc">{t}</text>'
        return (f'<line x1="70" y1="{y}" x2="750" y2="{y}" stroke="rgba(212,162,127,.35)" stroke-width="3"/>'
          f'<text x="70" y="{y-26}" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">{label}</text>'
          f'<rect x="600" y="{y-40}" width="150" height="28" rx="8" fill="rgba(212,162,127,.12)" stroke="rgba(212,162,127,.3)"/>'
          f'<text x="675" y="{y-21}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">{total}</text>'+seg)
    l1=lane(120,"IDEA TO LIVE OFFER",[("idea",),("draft",),("build",),("live",)],"one afternoon")
    l2=lane(300,"FEEDBACK TO FIX",[("signal",),("diagnose",),("patch",),("shipped",)],"under an hour")
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Ship in an afternoon","SPEED > SIZE")}
      <svg width="810" height="380" viewBox="0 0 810 380" style="display:block;margin:0 auto">
        <defs><radialGradient id="dot" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient></defs>
        {l1}{l2}
      </svg>
      {cap("idea to live offer in an afternoon, feedback to fix in an hour - size cannot keep pace.")}</div>'''

# 5. COSTS - a gauge dial (cost needle parked at cents) + a spread bar: cents in, full market out
def costs():
    cx,cy,R=210,250,168
    # needle near the low (cents) end of a 180deg sweep
    ang=math.radians(180-18)  # near left/low
    nx=cx+ (R-38)*math.cos(ang); ny=cy- (R-38)*math.sin(ang)
    ticks=""
    for i in range(0,181,30):
        a=math.radians(180-i)
        x1=cx+R*math.cos(a); y1=cy-R*math.sin(a); x2=cx+(R-18)*math.cos(a); y2=cy-(R-18)*math.sin(a)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="3"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="420" height="300" viewBox="0 0 420 300">
        <defs><linearGradient id="arc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#c84623"/></linearGradient>
        <filter id="ng" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(255,255,255,.06)" stroke-width="20"/>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx-R*math.cos(math.radians(54)):.0f} {cy-R*math.sin(math.radians(54)):.0f}" fill="none" stroke="url(#arc)" stroke-width="20" stroke-linecap="round"/>
        {ticks}
        <text x="{cx-R+6}" y="{cy+34}" font-family="DM Mono" font-size="14" fill="#9a9488">cents</text>
        <text x="{cx+R-56}" y="{cy+34}" font-family="DM Mono" font-size="14" fill="#c84623">$$$</text>
        <g filter="url(#ng)"><line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/></g>
        <circle cx="{cx}" cy="{cy}" r="14" fill="#2a2622" stroke="rgb({ACC})" stroke-width="3"/>
        <text x="{cx}" y="{cy-56}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">$0.09</text>
        <text x="{cx}" y="{cy-34}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">cost / run</text>
      </svg>
      <div style="flex:1">
        {htitle("Cost is a rounding error","THE SPREAD")}
        <div style="display:flex;flex-direction:column;gap:14px;margin-top:2px">
          <div><div style="display:flex;justify-content:space-between;font-family:DM Sans;font-size:16px;color:#c9c3b8;margin-bottom:6px"><span>What it costs you</span><span style="color:rgb({ACC})">cents</span></div>
          <div style="height:16px;border-radius:8px;background:rgba(255,255,255,.06)"><div style="width:8%;height:100%;border-radius:8px;background:rgb({ACC})"></div></div></div>
          <div><div style="display:flex;justify-content:space-between;font-family:DM Sans;font-size:16px;color:#c9c3b8;margin-bottom:6px"><span>What the market pays</span><span style="color:#FAFAF7">full price</span></div>
          <div style="height:16px;border-radius:8px;background:rgba(255,255,255,.06)"><div style="width:100%;height:100%;border-radius:8px;background:linear-gradient(90deg,rgb({ACC}),#e6b48f)"></div></div></div>
        </div>
        {cap("the meter runs in cents, the invoice is full market. that gap is the business.")}
      </div></div>'''

# 6. CALENDAR (ivory) - split: an EMPTY week grid (no standups/syncs) beside a FULL pipeline funnel
def calendar():
    days=["MON","TUE","WED","THU","FRI"]
    grid=""
    for c,d in enumerate(days):
        grid+=f'<text x="{30+c*88}" y="20" font-family="DM Mono" font-size="13" fill="#8a745a">{d}</text>'
        for r in range(4):
            grid+=f'<rect x="{6+c*88}" y="{34+r*70}" width="76" height="60" rx="10" fill="rgba(255,255,255,.5)" stroke="rgba(120,95,60,.18)"/>'
    funnel=""
    stages=[("Signals in",300,"860"),("Qualified",232,"214"),("In outreach",164,"96"),("Closing",96,"31")]
    fy=30
    for nm,w,n in stages:
        fx=(300-w)/2+40
        funnel+=(f'<path d="M{fx} {fy} h{w} l-26 56 h{w-52} Z" fill="url(#fn)" stroke="rgba(120,95,60,.2)"/>'
          f'<text x="{40+150}" y="{fy+34}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#fdfbf6">{nm}</text>'
          f'<text x="{40+150}" y="{fy+52}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgba(253,251,246,.75)">{n}</text>')
        fy+=68
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("Empty calendar, full pipe","07:00 DIGEST","#2a2016","#96562d")}
      <div style="display:flex;gap:30px;align-items:stretch">
        <div style="flex:1">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:#96562d;margin-bottom:10px">NO STANDUPS · NO SYNCS</div>
          <svg width="450" height="316" viewBox="0 0 450 316">{grid}
            <text x="225" y="176" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="22" fill="rgba(120,95,60,.35)" letter-spacing=".12em">CLEAR</text>
          </svg>
        </div>
        <div style="width:1px;background:linear-gradient(180deg,transparent,rgba(120,95,60,.28),transparent)"></div>
        <div style="flex-shrink:0;width:340px">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:#96562d;margin-bottom:10px">PIPELINE, WORKING</div>
          <svg width="340" height="316" viewBox="0 0 340 316">
            <defs><linearGradient id="fn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c2733f"/><stop offset="100%" stop-color="#96562d"/></linearGradient></defs>
            {funnel}</svg>
        </div>
      </div>
      {cap("no standups, no syncs - decisions when you choose, a 07:00 digest does the reporting.","#8a745a")}</div>'''

# 7. GATED - isometric stack of 3 outbound-send cards, each holding a lock LED, one tap releases all
def gated():
    sends=[("SPECTER","240 emails staged","HELD"),("STRIKER","proposal to Globex","HELD"),("AMPLIFY","6 posts queued","HELD")]
    cards=""
    for i,(ag,what,st) in enumerate(sends):
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">'
          f'<svg width="26" height="26" viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="9" rx="2" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/><path d="M8 11 V8 a4 4 0 0 1 8 0 v3" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{ag}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{what}</div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center;gap:8px"><span style="width:9px;height:9px;border-radius:50%;background:#c84623;box-shadow:0 0 10px rgba(200,70,35,.8)"></span>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#c99">{st}</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Nothing sends without you","AUTONOMY, HELD")}
      <div style="perspective:1900px;height:440px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:580px;height:400px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:392px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">One tap releases all &#8594;</div></div></div>
      {cap("the agents scale the work, but every external move parks on a red hold for your tap.")}</div>'''

# 8. YOU - closing: a spotlit laptop on an isometric pedestal, one spark, the open question
def you():
    return f'''<div style="width:820px;{CARD};padding:44px 44px 40px;text-align:center;margin:0 auto">
      <svg width="440" height="330" viewBox="0 0 440 330" style="display:block;margin:0 auto 6px">
        <defs><radialGradient id="spot" cx="50%" cy="30%"><stop offset="0%" stop-color="rgba(212,162,127,.28)"/><stop offset="70%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <radialGradient id="scr2" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <linearGradient id="ped" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#332f2a"/><stop offset="100%" stop-color="#1c1a17"/></linearGradient>
        <filter id="lg2" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        <path d="M220 6 L400 300 L40 300 Z" fill="url(#spot)"/>
        <path d="M120 300 L320 300 L360 250 L80 250 Z" fill="url(#ped)" stroke="rgba(255,255,255,.08)"/>
        <path d="M80 250 L80 268 L120 300 L120 300 Z" fill="rgba(0,0,0,.4)"/>
        <g filter="url(#lg2)"><rect x="146" y="120" width="148" height="98" rx="12" fill="#201d19" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
        <rect x="158" y="132" width="124" height="74" rx="6" fill="url(#scr2)"/></g>
        <text x="220" y="180" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">YOU</text>
        <path d="M118 240 L322 240 L340 226 L100 226 Z" fill="#2a2622" stroke="rgba(255,255,255,.1)"/>
      </svg>
      <div style="font-family:'DM Sans';font-weight:900;font-size:36px;color:#FAFAF7;line-height:1.1">Someone builds this<br>this year.</div>
      <div style="font-family:'DM Sans';font-size:20px;color:#c9a583;margin-top:14px">The only question is whether it is you.</div>
    </div>'''

PANELS={"notteam":notteam(),"agents":agents(),"revenue":revenue(),"speed":speed(),
        "costs":costs(),"calendar":calendar(),"gated":gated(),"you":you()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/million"; os.makedirs(outd,exist_ok=True)
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
