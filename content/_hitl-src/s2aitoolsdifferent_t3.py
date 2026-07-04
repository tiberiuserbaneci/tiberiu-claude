#!/usr/bin/env python3
# TIER 3 - ONE OPERATOR OVER A TOOL ZOO, built to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO stat-chip strips.
# Reframe: stop juggling ten AI tools; one Ultron operator, the ROUTER picks model/agent per job.
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

# 1. TOOLZOO (IVORY) - a fan of dim, struck-through competitor tabs collapsing into one lit Ultron window
def toolzoo():
    tools=["ChatGPT","Gemini","Perplexity","Copilot","Jasper","Grok","Notion AI","Poe","Midjourney"]
    chips=""
    for t in tools:
        chips+=(f'<div style="display:flex;align-items:center;gap:9px;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.20);border-radius:11px;padding:9px 15px">'
          f'<span style="width:8px;height:8px;border-radius:50%;background:rgba(150,90,45,.30)"></span>'
          f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:16px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.75)">{t}</span></div>')
    win=('<div style="max-width:560px;margin:0 auto;background:linear-gradient(160deg,#ffffff,#f3ead9);border:1px solid rgba(120,95,60,.22);border-radius:18px;box-shadow:0 34px 56px rgba(120,95,60,.26);overflow:hidden">'
      '<div style="display:flex;align-items:center;gap:10px;padding:14px 18px;border-bottom:1px solid rgba(120,95,60,.14)">'
      '<span style="width:11px;height:11px;border-radius:50%;background:#d9b7a0"></span><span style="width:11px;height:11px;border-radius:50%;background:#e6d3b8"></span><span style="width:11px;height:11px;border-radius:50%;background:#cdd8c9"></span>'
      '<div style="flex:1;margin-left:8px;background:rgba(255,255,255,.85);border:1px solid rgba(120,95,60,.18);border-radius:9px;padding:7px 14px;font-family:\'DM Mono\';font-size:14px;color:#5a4634">app.51ultron.com</div></div>'
      '<div style="display:flex;align-items:center;gap:20px;padding:26px 30px">'
      '<svg width="76" height="76" viewBox="0 0 76 76"><defs><radialGradient id="orbz" cx="38%" cy="32%"><stop offset="0%" stop-color="#f6d7bd"/><stop offset="55%" stop-color="rgb(212,162,127)"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient></defs>'
      '<circle cx="38" cy="38" r="32" fill="url(#orbz)"/><ellipse cx="30" cy="28" rx="11" ry="6" fill="rgba(255,255,255,.55)" transform="rotate(-28 30 28)"/></svg>'
      '<div style="text-align:left"><div style="font-family:\'DM Sans\';font-weight:900;font-size:28px;color:#2a2016;line-height:1.05">One operator</div>'
      '<div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#96562d">every job, one login</div></div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("Ten tabs, one window","THE TOOL ZOO")}
      <div style="display:flex;flex-wrap:wrap;gap:11px;justify-content:center;margin-bottom:14px">{chips}</div>
      <div style="text-align:center;margin-bottom:14px"><svg width="42" height="34" viewBox="0 0 42 34"><path d="M8 8 L21 24 L34 8" fill="none" stroke="#96562d" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      {win}
      {cap("nine logins struck through, one operator kept - the ROUTER runs the rest.","#8a745a")}</div>'''

# 2. ROUTER (DARK) - node graph: 4 jobs -> ROUTER hub -> the right agent + model tier, one lit
def router():
    hubx,hy=150,236
    jobs=[("research a company",96),("write cold emails",190),("qualify a deal",282),("draft a post",374)]
    lanes=[("CORTEX","DEEP · 0.40c","research",96,False),
           ("SPECTER","SMART · 0.11c","outbound",190,True),
           ("STRIKER","SMART · 0.11c","deals",282,False),
           ("PULSE","LITE · 0.02c","content",374,False)]
    edges=""
    for nm,y in jobs:
        edges+=f'<path d="M232 {y} C300 {y},300 {hy},{hubx-56} {hy}" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
    # left job chips as HTML, right agent cards as HTML, hub in svg
    jobchips=""
    for nm,y in jobs:
        jobchips+=(f'<div style="position:absolute;left:0;top:{y-24}px;width:236px;background:#221f1b;border:1px solid rgba(255,255,255,.09);border-radius:13px;padding:11px 14px">'
          f'<div style="font-family:\'DM Sans\';font-size:16px;color:#d9d5cc">{nm}</div></div>')
    cards=""
    for nm,tier,role,y,on in lanes:
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:\'DM Mono\';font-size:11px;color:rgb({ACC})">routed</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:590px;top:{y-32}px;width:230px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:14px;padding:12px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.1em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:18px;color:#FAFAF7;margin-top:3px">{tier}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:13px;color:#8f8f85">{role}</div></div></div>')
    lanedges=""
    for nm,tier,role,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.22)"; w=5 if on else 2
        lanedges+=f'<path d="M{hubx+56} {hy} C440 {hy},470 {y},584 {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One router, every job","MODEL ROUTER")}
      <div style="position:relative;height:470px">
        <svg width="820" height="470" viewBox="0 0 820 470" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}{lanedges}
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="56" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">reads the job</text>
        </svg>
        {jobchips}{cards}
      </div>
      {cap("one prompt in - it hires the agent and the cheapest tier that can do it.")}</div>'''

# 3. RADAR (DARK) - one operator watching every job type at once
def radar():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Research",300,150),("Outreach",120,96),("Deals",210,168),("Content",40,120),("Legal",250,60)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8.5" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    readout=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      '<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:#FAFAF7">Ten AI tabs</span><span style="font-family:\'DM Mono\';font-size:14px;color:#8f8f85">10 logins</span></div>'
      '<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:\'DM Sans\';font-size:17px;color:#8f8f85">One Ultron</span><span style="font-family:\'DM Mono\';font-size:14px;color:#8f8f85">1 login</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:\'DM Sans\';font-weight:900;font-size:30px;color:rgb({ACC})">all at once</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It runs every job","ONE OPERATOR")}
        {readout}
        {cap("research, outreach, deals, content, legal - one thread, not ten tabs.")}
      </div></div>'''

# 4. STACK (DARK) - isometric stack: the agent roster under one roof
def stack():
    rows=[("CORTEX","research profiles","DEEP"),
          ("SPECTER","outbound sequences","SMART"),
          ("STRIKER","deal qualification","SMART"),
          ("PULSE","content in your voice","LITE")]
    cards=""
    for i,(a,b,tier) in enumerate(rows):
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:20px;color:rgb({ACC})">{a[0]}</div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{a}</div><div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#FAFAF7">{b}</div></div>'
          f'<div style="flex-shrink:0;font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#8f8f85;background:rgba(250,250,247,.05);border:1px solid rgba(255,255,255,.09);border-radius:10px;padding:6px 12px">{tier}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("One roster, not ten logins","SEVEN AGENTS")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:440px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:404px;background:rgb({ACC});color:#1a0f0a;font-family:\'DM Sans\';font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">+3 more, one bill</div></div></div>
      {cap("CORTEX, SPECTER, STRIKER, PULSE and the rest - one roof, one subscription.")}</div>'''

# 5. GAUGE (IVORY) - the whole zoo for cents vs the expensive stack it replaces
def gauge():
    pct=94; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("The whole zoo, for cents","PRICING")}
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:190px;height:190px">
          <svg width="190" height="190" viewBox="0 0 190 190">
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 95 95)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:\'DM Sans\';font-weight:900;font-size:40px;color:#2a2016">cents</span>
            <span style="font-family:\'DM Mono\';font-size:12px;color:#96562d">per job</span></div></div>
        <div style="flex:1">
          <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.5);border-radius:12px;padding:16px 20px;margin-bottom:12px">
            <span style="flex:1;font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">Ten separate subscriptions</span>
            <span style="font-family:\'DM Sans\';font-weight:900;font-size:24px;color:rgb(200,70,35)">$300+/mo</span></div>
          <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.7);border-left:4px solid #96562d;border-radius:12px;padding:16px 20px">
            <span style="flex:1;font-family:\'DM Sans\';font-weight:800;font-size:19px;color:#2a2016">One operator, pay per token</span>
            <span style="font-family:\'DM Sans\';font-weight:900;font-size:24px;color:#96562d">0.11c</span></div>
        </div>
      </div>
      {cap("no ten flat fees - cents per job, you only pay for the work you run.","#8a745a")}</div>'''

# 6. FIELD (DARK) - dot field: every job this month, each routed from one login
def field():
    cols,rowsn=48,27
    lit={137,402,631,888,1045,1190,760,55,970}
    dots=""; cell=15; gap=3
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:40px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:\'DM Sans\';font-weight:900;font-size:52px;color:#FAFAF7">1,296</span>
        <span style="font-family:\'DM Sans\';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">jobs this month</span></div>
        <div style="font-family:\'DM Mono\';font-size:13px;color:rgb({ACC})">1 login, 0 tabs</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("every job routed to the right agent and tier - not ten tools you switch between.")}</div>'''

# 7. HUB (DARK) - radial hub-and-spokes: one operator core, seven agents + the human gate
def hub():
    cx,cy=210,210
    spokes=[("CORTEX",-90),("SPECTER",-38),("STRIKER",14),("PULSE",66),("SENTINEL",118),("AMPLIFY",170),("COUNSEL",222)]
    lines=""; nodes=""
    for nm,a in spokes:
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#cfc9bd">{nm}</text>')
    # human gate node at the bottom, muted-red-free warm, holding the reins
    gx,gy=cx,cy+152
    lines+=f'<line x1="{cx}" y1="{cy}" x2="{gx}" y2="{gy}" stroke="rgba(212,162,127,.45)" stroke-width="2.5" stroke-dasharray="4 6"/>'
    nodes+=(f'<circle cx="{gx}" cy="{gy}" r="30" fill="#241f1a" stroke="rgb({ACC})" stroke-width="2"/>'
      f'<text x="{gx}" y="{gy+4}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="rgb({ACC})">GATE</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="core" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">ONE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">OPERATOR</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("One core, seven agents","SHARED MEMORY")}
        <div style="font-family:\'DM Sans\';font-size:19px;color:#c9c3b8;line-height:1.45">Shared memory feeds all seven agents from one core, and every external move waits for your tap at the gate.</div>
        {cap("one memory, seven agents, one human gate - not ten tools that forget you.")}</div></div>'''

# 8. TIMELINE (DARK) - a workday collapsed onto one thread instead of ten tab-switches
def timeline():
    stops=[("09:00","CORTEX","research"),("10:30","SPECTER","outreach"),("12:00","STRIKER","qualify"),
           ("14:00","PULSE","content"),("16:00","COUNSEL","review"),("18:00","SENTINEL","ship")]
    n=len(stops); x0,x1,yl=70,750,150
    step=(x1-x0)/(n-1)
    line=f'<line x1="{x0}" y1="{yl}" x2="{x1}" y2="{yl}" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>'
    marks=""
    for i,(t,ag,job) in enumerate(stops):
        x=x0+i*step; up=(i%2==0)
        marks+=f'<circle cx="{x:.0f}" cy="{yl}" r="9" fill="rgb({ACC})" filter="url(#tp)"/>'
        if up:
            marks+=(f'<rect x="{x-64:.0f}" y="{yl-88}" width="128" height="58" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
              f'<text x="{x:.0f}" y="{yl-60}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="rgb({ACC})">{ag}</text>'
              f'<text x="{x:.0f}" y="{yl-40}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#c9c3b8">{job}</text>'
              f'<line x1="{x:.0f}" y1="{yl-30}" x2="{x:.0f}" y2="{yl-9}" stroke="rgba(212,162,127,.5)" stroke-width="2"/>')
        else:
            marks+=(f'<rect x="{x-64:.0f}" y="{yl+30}" width="128" height="58" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
              f'<text x="{x:.0f}" y="{yl+58}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="rgb({ACC})">{ag}</text>'
              f'<text x="{x:.0f}" y="{yl+78}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#c9c3b8">{job}</text>'
              f'<line x1="{x:.0f}" y1="{yl+9}" x2="{x:.0f}" y2="{yl+30}" stroke="rgba(212,162,127,.5)" stroke-width="2"/>')
        marks+=f'<text x="{x:.0f}" y="{yl+ (128 if up else -100)}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{t}</text>'
    dim=["ChatGPT","Gemini","Perplexity","Copilot","Jasper"]
    dchips=""
    for d in dim:
        dchips+=(f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:15px;color:#6f6a60;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6);background:rgba(250,250,247,.03);border:1px solid rgba(255,255,255,.07);border-radius:9px;padding:6px 12px">{d}</span>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Your whole day, one thread","ONE LOGIN")}
      <div style="display:flex;flex-wrap:wrap;gap:9px;justify-content:center;margin-bottom:18px;opacity:.72">{dchips}
        <span style="font-family:\'DM Mono\';font-size:13px;color:#7a746a;align-self:center;margin-left:6px">yesterday: 10 tabs</span></div>
      <svg width="820" height="290" viewBox="0 0 820 290" style="display:block;margin:0 auto">
        <defs><filter id="tp" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        {line}{marks}</svg>
      {cap("six jobs, six agents, one continuous thread - no tab you forgot to check.")}</div>'''

PANELS={"toolzoo":toolzoo(),"router":router(),"radar":radar(),"stack":stack(),
        "gauge":gauge(),"field":field(),"hub":hub(),"timeline":timeline()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2aitoolsdifferent"; os.makedirs(outd,exist_ok=True)
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
