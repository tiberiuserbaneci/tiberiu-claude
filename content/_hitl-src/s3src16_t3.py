#!/usr/bin/env python3
# TIER 3 - THE 30-DAY LANDLORD, on the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded
# scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Reframes the "hidden Notion trial -> unlimited Opus" hack: the trial is a countdown you do not
# own; on day 31 it resets to zero. Ultron = own the meter, cents per token, agents that compound.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'
RED="200,70,35"

# 1. FUSE - IVORY: an hourglass, warm sand draining, the trial as a countdown that runs out
def fuse():
    # top chamber 66..232 apex 280,232 ; sand 45% remaining
    sand='<linearGradient id="sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e9c39c"/><stop offset="52%" stop-color="rgb('+ACC+')"/><stop offset="100%" stop-color="#b97a48"/></linearGradient>'
    wood='<linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d9b48c"/><stop offset="100%" stop-color="#a97b4e"/></linearGradient>'
    glassfill="rgba(120,95,60,.05)"; glassstroke="rgba(120,95,60,.34)"
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;text-align:center">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Free access, on a fuse</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">30-DAY TRIAL</span></div>
      <svg width="560" height="474" viewBox="0 0 560 474" style="display:block;margin:0 auto">
        <defs>{sand}{wood}
          <filter id="ss" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="rgba(120,90,55,.28)"/></filter></defs>
        <!-- side posts -->
        <rect x="112" y="60" width="9" height="348" rx="4" fill="url(#wood)"/>
        <rect x="439" y="60" width="9" height="348" rx="4" fill="url(#wood)"/>
        <!-- caps -->
        <rect x="116" y="44" width="328" height="22" rx="9" fill="url(#wood)" filter="url(#ss)"/>
        <rect x="116" y="402" width="328" height="22" rx="9" fill="url(#wood)" filter="url(#ss)"/>
        <!-- glass chambers -->
        <path d="M130 66 L430 66 L280 232 Z" fill="{glassfill}" stroke="{glassstroke}" stroke-width="2.5" stroke-linejoin="round"/>
        <path d="M280 240 L130 398 L430 398 Z" fill="{glassfill}" stroke="{glassstroke}" stroke-width="2.5" stroke-linejoin="round"/>
        <!-- top sand remaining (~45%) -->
        <path d="M180 121 L380 121 L280 232 Z" fill="url(#sand)"/>
        <path d="M180 121 L380 121 L354 138 L206 138 Z" fill="rgba(255,255,255,.30)"/>
        <!-- falling stream -->
        <rect x="275" y="230" width="10" height="100" fill="url(#sand)"/>
        <!-- bottom pile -->
        <path d="M130 398 L430 398 L430 344 Q280 300 130 344 Z" fill="url(#sand)"/>
        <path d="M280 300 Q350 314 430 344 L430 356 Q350 328 280 314 Q210 328 130 356 L130 344 Q210 314 280 300Z" fill="rgba(255,255,255,.22)"/>
        <!-- glass rim gloss -->
        <path d="M146 74 L206 140" stroke="rgba(255,255,255,.55)" stroke-width="3" stroke-linecap="round"/>
        <text x="280" y="456" text-anchor="middle" font-family="DM Mono" font-size="17" letter-spacing=".14em" fill="rgb({RED})">18 DAYS LEFT</text>
      </svg>
      {cap("unlimited today. zero on day 31.","#8a745a")}</div>'''

# 2. LANDLORD - a big frontier orb LOCKED by the platform, your access a dashed guest pass that expires
def landlord():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("You hold a guest pass","BORROWED ACCESS")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="250" cy="200" r="128" fill="url(#orb)"/></g>
        <text x="250" y="188" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">FRONTIER</text>
        <text x="250" y="216" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">MODELS</text>
        <!-- platform lock clamped over the orb -->
        <g transform="translate(214,238)"><rect x="0" y="30" width="72" height="52" rx="11" fill="#1a0f0a" stroke="#3a2010" stroke-width="2"/><path d="M13 30 V18 a23 23 0 0 1 46 0 v12" fill="none" stroke="#1a0f0a" stroke-width="7"/><circle cx="36" cy="54" r="6" fill="rgb({ACC})"/></g>
        <text x="250" y="356" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#8f8f85">OWNED BY THE PLATFORM</text>
        <!-- dashed guest pass line to the right -->
        <path d="M382 200 H560" stroke="rgb({RED})" stroke-width="4" stroke-dasharray="3 12" stroke-linecap="round"/>
        <rect x="566" y="140" width="196" height="120" rx="22" fill="#201d19" stroke="rgba(212,162,127,.35)" stroke-width="2"/>
        <g transform="translate(590,176)"><circle cx="14" cy="14" r="13" fill="none" stroke="rgb({ACC})" stroke-width="4"/><path d="M25 25 l24 24" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round"/><path d="M40 40 l8 -8 M46 46 l8 -8" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round"/></g>
        <text x="664" y="192" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">GUEST PASS</text>
        <rect x="586" y="212" width="156" height="34" rx="9" fill="rgba(200,70,35,.14)" stroke="rgba(200,70,35,.5)"/>
        <text x="664" y="234" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb({RED})">EXPIRES · DAY 31</text>
      </svg>
      {cap("the models are real. the keys are not yours to keep.")}</div>'''

# 3. DAY31 - a 30-cell timeline that lights up warm then a severed red day 31; assets wiped above
def day31():
    assets=["Custom agents","Research runs","Meeting notes","Your prompts"]
    chips=""
    for a in assets:
        chips+=(f'<div style="display:flex;align-items:center;gap:10px;background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.28);border-radius:12px;padding:11px 15px">'
          f'<svg width="17" height="17" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M6 6 L18 18 M18 6 L6 18" stroke="rgb({RED})" stroke-width="3" stroke-linecap="round"/></svg>'
          f'<span style="font-family:DM Sans;font-size:16px;color:#c9c3b8;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">{a}</span></div>')
    cells=""
    x=0; cw=22; gap=3.4
    for d in range(30):
        op=0.30+0.70*(d/29)
        cells+=f'<rect x="{x:.1f}" y="0" width="{cw}" height="52" rx="5" fill="rgb({ACC})" opacity="{op:.2f}"/>'
        x+=cw+gap
    # gap then day 31 severed
    x31=x+18
    day31cell=(f'<rect x="{x31:.1f}" y="-6" width="30" height="64" rx="6" fill="rgba(200,70,35,.14)" stroke="rgb({RED})" stroke-width="2.5"/>'
      f'<path d="M{x31+6:.1f} 4 L{x31+24:.1f} 44 M{x31+24:.1f} 4 L{x31+6:.1f} 44" stroke="rgb({RED})" stroke-width="3" stroke-linecap="round"/>')
    fw=x31+30
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Day 31 resets you","THE CLIFF")}
      <div style="display:flex;flex-wrap:wrap;gap:12px;margin-bottom:26px">{chips}</div>
      <svg width="{fw:.0f}" height="80" viewBox="0 -12 {fw:.0f} 80" style="display:block;width:100%">
        {cells}{day31cell}
      </svg>
      <div style="display:flex;justify-content:space-between;margin-top:8px;font-family:'DM Mono';font-size:12.5px;color:#8f8f85">
        <span>DAY 1</span><span>DAY 15</span><span style="color:rgb({RED})">DAY 31 · WIPED</span></div>
      {cap("everything you built lived inside someone else's trial.")}</div>'''

# 4. METER - IVORY ledger: task / tier / cost in cents, a running total, no card no clock no reset
def meter():
    rows=[("Rank 400 accounts","LITE","0.02c"),
          ("Draft 12 follow-ups","SMART","0.11c"),
          ("Enrich 50 new leads","SMART","0.11c"),
          ("Close-plan review","DEEP","0.40c"),
          ("Weekly signal digest","LITE","0.02c")]
    body=""
    for task,tier,cost in rows:
        body+=(f'<div style="display:flex;align-items:center;gap:16px;padding:15px 4px;border-bottom:1px solid rgba(120,95,60,.18)">'
          f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:19px;color:#2a2016">{task}</span>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#96562d;background:rgba(150,90,45,.10);border:1px solid rgba(150,90,45,.25);border-radius:7px;padding:4px 11px">{tier}</span>'
          f'<span style="flex-shrink:0;width:78px;text-align:right;font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016">{cost}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Own the meter</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PAY PER TOKEN</span></div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#a08a68">SPENT TODAY</span>
        <span style="font-family:DM Mono;font-weight:500;font-size:24px;letter-spacing:.30em;color:#2a2016;background:linear-gradient(#efe6d5,#e2d6c0);border:1px solid rgba(120,95,60,.28);border-radius:9px;padding:4px 14px;box-shadow:inset 0 2px 4px rgba(120,95,60,.22)">0.66c</span></div>
      <div style="display:flex;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#a08a68;padding:0 4px 6px;border-bottom:2px solid rgba(120,95,60,.30)">
        <span style="flex:1">TASK</span><span style="width:96px">TIER</span><span style="width:78px;text-align:right">COST</span></div>
      {body}
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:16px">
        <span style="font-family:DM Mono;font-size:13px;color:#8a745a">no card &middot; no clock &middot; no reset</span>
        <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#96562d">= 0.66c</span></div>
      {cap("pay per token. cents per task. it never resets.","#8a745a")}</div>'''

# 5. TIERS - one router, three model tiers, a job routed to the cheapest that can do it
def tiers():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
    hubx,hy=180,230; lx=470
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C330 {hy},340 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:308px;top:{y-40}px;width:180px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One router, three tiers","PAY PER JOB")}
      <div style="position:relative;height:460px">
        <svg width="828" height="460" viewBox="0 0 828 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="14" y="{hy-30}" width="96" height="60" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:16px;top:206px;width:92px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">rank 400<br>accounts</div>
        {cards}
      </div>
      {cap("same frontier models. the cheapest tier that can do the job, in cents.")}</div>'''

# 6. ROSTER - radial hub, seven named agents around the router, kept for good
def roster():
    cx,cy,R=410,222,178
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),
            ("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="44" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-1:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, kept for good","YOUR ROSTER")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="rc" cx="38%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#rc)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">picks + gates</text>
        {nodes}
      </svg>
      {cap("hired once. they do not expire on day 31.")}</div>'''

# 7. COMPOUND - area curve: the borrowed trial peaks then cliffs to zero; the operator compounds
def compound():
    W,H=738,378; x0,x1,y0,yb=70,760,60,330
    def X(d): return x0+(d/300)*(x1-x0)
    def Y(v): return yb-v*(yb-y0)
    opts=[(0,0.05),(30,0.12),(90,0.30),(180,0.60),(300,0.95)]
    d=f'M{X(opts[0][0]):.0f} {Y(opts[0][1]):.0f} '
    for i in range(1,len(opts)):
        px,pv=opts[i-1]; cx,cv=opts[i]; mx=(px+cx)/2
        d+=f'C{X(mx):.0f} {Y(pv):.0f},{X(mx):.0f} {Y(cv):.0f},{X(cx):.0f} {Y(cv):.0f} '
    area=d+f'L{x1} {yb} L{x0} {yb} Z'
    tx=X(30); ty=Y(0.55)
    trial=f'M{x0} {ty:.0f} L{tx:.0f} {ty:.0f} L{tx:.0f} {yb}'
    grid="".join(f'<line x1="{x0}" y1="{Y(v):.0f}" x2="{x1}" y2="{Y(v):.0f}" stroke="rgba(250,250,247,.05)"/>' for v in (0.25,0.5,0.75,1.0))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A hack peaks, an operator compounds","30 vs 300 DAYS")}
      <div style="display:flex;gap:22px;margin-bottom:10px">
        <div style="display:flex;align-items:center;gap:8px"><span style="width:12px;height:12px;border-radius:3px;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:15px;color:#d9d5cc">your operator</span></div>
        <div style="display:flex;align-items:center;gap:8px"><span style="width:12px;height:12px;border-radius:3px;background:rgb({RED})"></span><span style="font-family:DM Sans;font-size:15px;color:#d9d5cc">borrowed trial</span></div></div>
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block">
        <defs><linearGradient id="af" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.42)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
        <filter id="cg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {grid}
        <line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="rgba(250,250,247,.22)"/>
        <path d="{area}" fill="url(#af)"/>
        <path d="{d}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" filter="url(#cg)"/>
        <path d="{trial}" fill="none" stroke="rgb({RED})" stroke-width="4" stroke-linecap="round"/>
        <path d="M{tx:.0f} {yb} L{x1} {yb}" fill="none" stroke="rgb({RED})" stroke-width="2.5" stroke-dasharray="3 9"/>
        <circle cx="{tx:.0f}" cy="{yb}" r="6" fill="rgb({RED})"/>
        <text x="{tx+10:.0f}" y="{yb-12:.0f}" font-family="DM Mono" font-size="12.5" fill="rgb({RED})">reset to zero</text>
        <circle cx="{X(300):.0f}" cy="{Y(0.95):.0f}" r="7" fill="rgb({ACC})" filter="url(#cg)"/>
        <text x="{tx:.0f}" y="{yb+22:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">DAY 30</text>
        <text x="{x1:.0f}" y="{yb+22:.0f}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#8f8f85">DAY 300</text>
      </svg>
      {cap("every brief feeds one memory that keeps growing.")}</div>'''

# 8. OWN - convergence: rented pieces assemble into one operator you own outright
def own():
    scat=[("frontier models",70,86),("seven agents",70,196),("one memory",70,306),("cents meter",190,141),("no clock",190,251)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+30} {y} C350 {y},370 210,520 210" fill="none" stroke="rgba(212,162,127,.34)" stroke-width="2.2"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="#221f1b" stroke="rgba(212,162,127,.28)" stroke-width="1.5"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Own it, do not rent it","ONE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="592" cy="210" r="122" fill="url(#bod)"/></g>
        <text x="592" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">OWNED</text>
        <text x="592" y="228" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".08em">your operator</text>
        <text x="592" y="366" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">no trial &middot; no countdown</text>
      </svg>
      {cap("one system you own, not a trial you borrow.")}</div>'''

PANELS={"fuse":fuse(),"landlord":landlord(),"day31":day31(),"meter":meter(),
        "tiers":tiers(),"roster":roster(),"compound":compound(),"own":own()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src16"; os.makedirs(outd,exist_ok=True)
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
