#!/usr/bin/env python3
# TIER 3 - SYSTEMS NOT EMPLOYEES, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Topic: stop hiring, start wiring - the 7-agent roster replaces headcount at cents, not salaries.
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. ROLES - IVORY org chart: one FOUNDER over one ULTRON system fanning to 7 agent roles (no hires)
def roles():
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    W,H=830,432; bw=104; gap=15
    total=len(agents)*bw+(len(agents)-1)*gap; x0=(W-total)/2
    leafy=300; lh=90; fx=W/2; fy=18; hubx=W/2; huby=150
    conns=""; boxes=""
    for i,(nm,role) in enumerate(agents):
        x=x0+i*(bw+gap); cxb=x+bw/2
        conns+=f'<path d="M{hubx} {huby+30} C{hubx} {leafy-46},{cxb:.0f} {huby+70},{cxb:.0f} {leafy}" fill="none" stroke="rgba(150,90,45,.30)" stroke-width="1.8"/>'
        boxes+=(f'<rect x="{x:.0f}" y="{leafy}" width="{bw}" height="{lh}" rx="14" fill="rgba(255,255,255,.66)" stroke="rgba(150,90,45,.22)" stroke-width="1.4"/>'
          f'<text x="{cxb:.0f}" y="{leafy+37}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#2a2016">{nm}</text>'
          f'<text x="{cxb:.0f}" y="{leafy+61}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#96562d">{role}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("One login, seven roles","NO NEW HIRES")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block">
        <defs><linearGradient id="sysg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f6ead9"/><stop offset="100%" stop-color="#e7d6bf"/></linearGradient></defs>
        {conns}
        <line x1="{fx:.0f}" y1="{fy+60}" x2="{fx:.0f}" y2="{huby-30}" stroke="rgba(150,90,45,.4)" stroke-width="1.8"/>
        <rect x="{fx-90:.0f}" y="{fy}" width="180" height="60" rx="15" fill="#2a2016"/>
        <text x="{fx:.0f}" y="{fy+30}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#fdfbf6">FOUNDER</text>
        <text x="{fx:.0f}" y="{fy+50}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#d4a27f">you</text>
        <rect x="{hubx-120:.0f}" y="{huby-30}" width="240" height="60" rx="16" fill="url(#sysg)" stroke="#c8845c" stroke-width="1.5"/>
        <text x="{hubx:.0f}" y="{huby+2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a2016">ULTRON</text>
        <text x="{hubx:.0f}" y="{huby+21}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#96562d">one system, routed</text>
        {boxes}
      </svg>
      {cap("the org chart you get without posting a single job.","#8a745a")}</div>'''

# 2. PAYROLL - IVORY cost gauge: needle pinned to CENTS; salary marked red at the far end
def payroll():
    cx,cy,R=250,255,196
    t=0.12; ang=180-t*180
    nx=cx+R*0.82*math.cos(math.radians(ang)); ny=cy-R*0.82*math.sin(math.radians(ang))
    arc=f'M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}'
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("Salaries, or cents","THE MATH")}
      <div style="display:flex;align-items:center;gap:30px">
        <svg width="500" height="300" viewBox="0 0 500 312">
          <defs><linearGradient id="gg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="60%" stop-color="#d08a5c"/><stop offset="100%" stop-color="rgb(200,70,35)"/></linearGradient></defs>
          <path d="{arc}" fill="none" stroke="rgba(150,90,45,.14)" stroke-width="34" stroke-linecap="round"/>
          <path d="{arc}" fill="none" stroke="url(#gg)" stroke-width="30" stroke-linecap="round"/>
          <text x="{cx-R+8}" y="{cy+34}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#96562d">CENTS</text>
          <text x="{cx+R-8}" y="{cy+34}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb(200,70,35)">SALARY</text>
          <text x="{cx}" y="{cy-72}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a2016">cents</text>
          <text x="{cx}" y="{cy-44}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#96562d">per task</text>
          <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="7" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="16" fill="#2a2016"/>
          <circle cx="{cx}" cy="{cy}" r="7" fill="#f6ead9"/>
        </svg>
        <div style="flex:1;display:flex;flex-direction:column;gap:16px">
          <div style="background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.35);border-radius:16px;padding:18px 20px">
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb(200,70,35)">FIVE HIRES &middot; PER YEAR</div>
            <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016;line-height:1.05;margin-top:4px">$240,000</div>
            <div style="font-family:DM Sans;font-size:15px;color:#8a745a">salaries, tools, ramp time</div></div>
          <div style="background:rgba(212,162,127,.14);border:1px solid rgba(150,90,45,.4);border-radius:16px;padding:18px 20px">
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#96562d">SAME ROLES &middot; WIRED</div>
            <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016;line-height:1.05;margin-top:4px">cents<span style="font-size:20px;color:#96562d;font-weight:700"> / task</span></div>
            <div style="font-family:DM Sans;font-size:15px;color:#8a745a">pay per token, nothing idle</div></div>
        </div>
      </div>
      {cap("a headcount is a fixed cost. a roster is a few cents when it runs.","#8a745a")}</div>'''

# 3. PIPELINE - node graph: one job flows research -> outbound -> deals, two feeders join the chain
def pipeline():
    W,H=820,432
    def disc(x,y,nm,sub,r=54):
        return (f'<g filter="url(#pg)"><circle cx="{x}" cy="{y}" r="{r}" fill="url(#pn)" stroke="rgba(212,162,127,.5)" stroke-width="2"/></g>'
          f'<text x="{x}" y="{y-3}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x}" y="{y+17}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">{sub}</text>')
    def feed(x,y,nm,r=40):
        return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#221f1b" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">{nm}</text>')
    n0,n1,n2=(120,210),(360,210),(600,210); my=210
    edges=(f'<line x1="{n0[0]+54}" y1="{my}" x2="{n1[0]-54}" y2="{my}" stroke="rgb({ACC})" stroke-width="5"/>'
      f'<line x1="{n1[0]+54}" y1="{my}" x2="{n2[0]-54}" y2="{my}" stroke="rgb({ACC})" stroke-width="5"/>'
      f'<path d="M{n2[0]+54} {my} H726" fill="none" stroke="rgb({ACC})" stroke-width="5"/>'
      f'<path d="M360 112 C360 150,360 160,360 {my-54}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.6"/>'
      f'<path d="M600 316 C600 280,600 270,600 {my+54}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.6"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One job, wired end to end","THE PIPELINE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="pn" cx="38%" cy="30%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1a1815"/></radialGradient>
        <radialGradient id="out" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="pg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="rgba(0,0,0,.55)"/></filter></defs>
        {edges}
        {feed(360,72,"PULSE")}{feed(600,354,"AMPLIFY")}
        {disc(*n0,"CORTEX","ranked brief")}{disc(*n1,"SPECTER","24 emails")}{disc(*n2,"STRIKER","2 replies")}
        <g filter="url(#pg)"><rect x="726" y="176" width="82" height="68" rx="16" fill="url(#out)"/></g>
        <text x="767" y="205" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="14" fill="#1a0f0a">MEETING</text>
        <text x="767" y="224" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">booked</text>
      </svg>
      {cap("research hands to outbound, outbound to deals. no meeting, no dropped context.")}</div>'''

# 4. SHIPPED - isometric stack of real outputs left on your desk by morning
def shipped():
    rows=[("Cold sequence","24 emails, ready to send","SPECTER"),
          ("Account brief","40 accounts, ranked","CORTEX"),
          ("Pricing page","shipped to main","SENTINEL")]
    cards=""
    for i,(a,b,ag) in enumerate(rows):
        y=i*146
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">'
          f'<div style="flex:1;text-align:left"><div style="font-family:DM Sans;font-weight:800;font-size:24px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:DM Sans;font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>'
          f'<div style="flex-shrink:0;background:rgb({ACC});padding:8px 15px;border-radius:11px;box-shadow:0 6px 14px rgba({ACC},.4)"><span style="font-family:DM Mono;font-weight:500;font-size:13px;letter-spacing:.06em;color:#1a0f0a">{ag}</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("Shipped while you slept","OVERNIGHT")}
      <div style="perspective:2000px;height:490px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:470px;position:relative">{cards}</div></div>
      {cap("every role leaves real output on your desk by morning.")}</div>'''

# 5. WATCH - radar of live market signals with a first-to-see lead readout
def watch():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Stack",210,168),("Churn",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">You + Ultron</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">Tue 09:12</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">Doing it by hand</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">Fri 16:40</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">3 days ahead</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It saw the market first","SIGNAL LEAD")}
        {lead}
        {cap("funding, hiring, stack, churn - one agent watches the market every night.")}
      </div></div>'''

# 6. SCALE - dot field: 1,000 tasks a month, the handful you personally touch lit
def scale():
    cols,rowsn=50,20  # 1000
    import random; random.seed(7)
    lit=set(random.sample(range(cols*rowsn),40))
    dots=""; cell=13; gap=3
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">1,000</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">tasks a month</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">you touch 40</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("the roster runs in parallel. you review the lit ones, you do not do the work.")}</div>'''

# 7. HUB - radial memory core, 7 agent spokes, one shared brain (none severed)
def hub():
    cx,cy,R=235,225,150
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    spokes=""; nodes=""
    for i,nm in enumerate(agents):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:28px">
      <svg width="470" height="450" viewBox="0 0 470 450" style="flex-shrink:0">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {spokes}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one core</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("One memory, shared","THE CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing and docs live once. Every agent reads and writes the same core, so nothing is repeated and nothing is forgotten.</div>
        {cap("seven roles, one brain. context never resets between them.")}</div></div>'''

# 8. GATE - vertical timeline of a day's autonomous work, every external send held for your tap
def gate():
    events=[("06:40","SPECTER drafted 24 cold emails","held"),
            ("09:15","CORTEX ranked 40 target accounts","held"),
            ("11:30","PULSE wrote the launch post","held"),
            ("14:05","SENTINEL shipped the pricing fix","sent")]
    rows=""
    for i,(t,lbl,st) in enumerate(events):
        y=i*104
        if st=="held":
            chip=('<div style="display:flex;align-items:center;gap:8px;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.4);border-radius:999px;padding:7px 15px">'
              f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'
              f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.08em;color:rgb({ACC})">AWAITS YOUR TAP</span></div>')
            dotc=f"rgb({ACC})"; dotfill=f"rgba(212,162,127,.25)"
        else:
            chip=(f'<div style="display:flex;align-items:center;gap:8px;background:rgb({ACC});border-radius:999px;padding:8px 16px">'
              '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.8"><path d="M5 12.5l3.5 3.5L18 7"/></svg>'
              '<span style="font-family:DM Mono;font-weight:500;font-size:13px;letter-spacing:.08em;color:#1a0f0a">SENT &middot; YOU TAPPED</span></div>')
            dotc=f"rgb({ACC})"; dotfill=f"rgb({ACC})"
        rows+=(f'<div style="position:absolute;left:0;top:{y}px;width:100%;display:flex;align-items:center;gap:24px">'
          f'<div style="position:relative;z-index:2;flex-shrink:0;width:20px;height:20px;border-radius:50%;background:{dotfill};border:2.5px solid {dotc};box-shadow:0 0 0 5px #201d1a"></div>'
          f'<div style="flex:1;display:flex;align-items:center;justify-content:space-between;background:linear-gradient(160deg,#332f2a,#221e1a);border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:16px 20px;box-shadow:0 16px 28px rgba(0,0,0,.45)">'
          f'<div><div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">{t}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7;margin-top:2px">{lbl}</div></div>'
          f'{chip}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A day of work, all gated","HUMAN GATE")}
      <div style="position:relative;height:{len(events)*104-14}px">
        <div style="position:absolute;left:9px;top:12px;bottom:22px;width:2px;background:linear-gradient(180deg,rgba(212,162,127,.5),rgba(212,162,127,.15))"></div>
        {rows}</div>
      {cap("brain, hands and voice all run. every external send waits for your tap.")}</div>'''

PANELS={"roles":roles(),"payroll":payroll(),"pipeline":pipeline(),"shipped":shipped(),
        "watch":watch(),"scale":scale(),"hub":hub(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2mostbusinessesdo"; os.makedirs(outd,exist_ok=True)
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
