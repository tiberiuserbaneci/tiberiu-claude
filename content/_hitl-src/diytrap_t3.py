#!/usr/bin/env python3
# TIER 3 - THE BUILD-IT-YOURSELF TRAP, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO generic
# stat-chip strips, NO clip-path cuts, NO extruded walls. Cost zero (all coded SVG/CSS).
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagcol=None):
    tagcol=tagcol or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagcol}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. RECIPE - isometric stack of engineering-syllabus cards a founder never signed up to maintain
def recipe():
    topics=[("STATE MACHINES","transitions, guards, deadlocks","+6 hrs/wk"),
            ("AGENT GRAPHS","nodes, edges, cycle detection","+4 hrs/wk"),
            ("CONTROL FLOW","retry, backoff, timeouts","+3 hrs/wk"),
            ("TOOL SCHEMAS","validation, parsing, errors","+5 hrs/wk")]
    cards=""
    for i,(nm,sub,hrs) in enumerate(topics):
        y=i*112
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);'
          f'border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 22px;'
          f'box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:13px;background:rgba(212,162,127,.13);border:1px solid rgba(212,162,127,.32);'
          f'display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC})">{i+1}</div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:600;font-size:18px;color:#e2dccf;margin-top:2px">{sub}</div></div>'
          f'<div style="flex-shrink:0;font-family:DM Mono;font-size:14px;letter-spacing:.04em;color:#c89a86;background:rgba(200,70,35,.12);'
          f'border:1px solid rgba(200,70,35,.3);border-radius:9px;padding:7px 13px">{hrs}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The tutorial's syllabus","10 SLIDES IN")}
      <div style="perspective:1900px;height:440px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(19deg) rotateZ(-8deg);width:560px;height:420px;position:relative">{cards}</div></div>
      <div style="display:flex;justify-content:center;margin-top:2px">
        <span style="background:rgba(200,70,35,.14);border:1px solid rgba(200,70,35,.5);color:#e8a892;
          font-family:DM Mono;font-size:14px;letter-spacing:.08em;padding:9px 22px;border-radius:999px">you now maintain all four, forever</span></div>
      {cap("frameworks, graphs, state machines. the tutorial forgot you run a company.")}</div>'''

# 2. WIRING - IVORY tangled hand-wired Plan/Act/Observe loop: clean loop under a mess of red edges
def wiring():
    P=(150,250); A=(470,130); O=(470,370)
    def node(x,y,lab):
        return (f'<circle cx="{x}" cy="{y}" r="40" fill="#fdfbf6" stroke="#96562d" stroke-width="2.5"/>'
                f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".06em" fill="#3a2a1c">{lab}</text>')
    clean=(  # the loop the tutorials teach - clean, ivory-accent
      f'<path d="M186 227 Q330 150 428 145" fill="none" stroke="#96562d" stroke-width="4" marker-end="url(#ah)"/>'
      f'<path d="M486 168 Q524 250 486 332" fill="none" stroke="#96562d" stroke-width="4" marker-end="url(#ah)"/>'
      f'<path d="M430 355 Q300 330 182 278" fill="none" stroke="#96562d" stroke-width="4" marker-end="url(#ah)"/>')
    tangle="".join(  # everything YOU have to wire by hand
      [f'<path d="{d}" fill="none" stroke="rgb({RED})" stroke-width="2" stroke-dasharray="4 7" opacity="0.6" marker-end="url(#ar)"/>'
       for d in ["M500 108 C600 60 610 200 512 122","M452 402 C360 470 250 380 168 292",
                 "M508 356 C620 300 590 168 512 156","M196 288 C300 440 430 420 452 398",
                 "M120 232 C40 150 130 70 148 208"]])
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("You wire every arrow","PLAN / ACT / OBSERVE","#2a2016","#96562d")}
      <svg width="640" height="480" viewBox="0 0 640 480" style="display:block;margin:0 auto">
        <defs>
          <marker id="ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6Z" fill="#96562d"/></marker>
          <marker id="ar" markerWidth="8" markerHeight="8" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6Z" fill="rgb({RED})"/></marker>
        </defs>
        {tangle}{clean}
        {node(*P,"PLAN")}{node(*A,"ACT")}{node(*O,"OBSERVE")}
        <text x="316" y="256" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#96562d">3 weekends</text>
        <text x="316" y="278" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#a06a45">of your wiring</text>
      </svg>
      {cap("the loop the tutorials teach is real. wiring it yourself is three weekends.","#8a745a")}</div>'''

# 3. BREAKS - a 7-day uptime strip that goes dark the day you stop watching (HTML cells + fault pins)
def breaks():
    days=[("MON","watched",True),("TUE","watched",True),("WED","watched",True),
          ("THU","you left",None),("FRI","silent fail",False),("SAT","bad send",False),("SUN","dead",False)]
    cells=""
    for d,st,ok in days:
        if ok is True:
            bg="linear-gradient(160deg,#33302c,#221f1b)";bd="rgba(212,162,127,.34)";lab=f"rgb({ACC})"
            mark=f'<svg width="22" height="22" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        elif ok is None:
            bg="linear-gradient(160deg,#2a2723,#1c1a17)";bd="rgba(250,250,247,.16)";lab="#9a9488"
            mark=f'<svg width="22" height="22" viewBox="0 0 24 24"><path d="M8 4 L16 20" stroke="#9a9488" stroke-width="2.4" stroke-linecap="round"/><path d="M8 12 H16" stroke="#9a9488" stroke-width="2.4" stroke-dasharray="2 3"/></svg>'
        else:
            bg="linear-gradient(160deg,#3a201a,#241310)";bd="rgba(200,70,35,.6)";lab="#e8a892"
            mark=f'<svg width="22" height="22" viewBox="0 0 24 24"><path d="M7 7l10 10M17 7L7 17" stroke="rgb({RED})" stroke-width="2.6" stroke-linecap="round"/></svg>'
        cells+=(f'<div style="flex:1;background:{bg};border:1.5px solid {bd};border-radius:16px;padding:20px 8px 18px;'
          f'display:flex;flex-direction:column;align-items:center;gap:14px">'
          f'<div style="font-family:DM Mono;font-size:14px;letter-spacing:.14em;color:#d9d5cc">{d}</div>'
          f'<div style="height:60px;display:flex;align-items:center">{mark}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:14px;color:{lab};text-align:center">{st}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It runs until it doesn't","NO GATE ON SENDS","#FAFAF7",f"rgb({RED})")}
      <div style="display:flex;gap:12px;align-items:stretch">{cells}</div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:20px;background:rgba(200,70,35,.08);
        border:1px solid rgba(200,70,35,.32);border-radius:14px;padding:14px 20px">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({RED});flex-shrink:0">FAILS IN PRIVATE</span>
        <span style="font-family:DM Sans;font-size:17px;color:#c9c3b8">edge case at 02:00, no alert, no human tap. you find out from the customer.</span></div>
      {cap("edge cases, silent failures, no gate on sends. diy agents fail where nobody looks.")}</div>'''

# 4. BILL - maintenance-cost curve: hours-in climbs, leads-out stays on the floor
def bill():
    W,H=720,380; x0,y0,x1,y1=90,40,690,320  # plot box
    weeks=6
    hrs=[.10,.26,.44,.60,.80,.96]
    lds=[.02,.03,.03,.05,.03,.04]
    def px(i): return x0+(x1-x0)*i/(weeks-1)
    def py(v): return y1-(y1-y0)*v
    grid="".join(f'<line x1="{x0}" y1="{py(g)}" x2="{x1}" y2="{py(g)}" stroke="rgba(250,250,247,.06)"/>' for g in (0,.25,.5,.75,1))
    xlab="".join(f'<text x="{px(i)}" y="{y1+26}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">wk {i+1}</text>' for i in range(weeks))
    hpts=" ".join(f"{px(i):.0f},{py(v):.0f}" for i,v in enumerate(hrs))
    lpts=" ".join(f"{px(i):.0f},{py(v):.0f}" for i,v in enumerate(lds))
    area=f"M{x0},{y1} " + " ".join(f"L{px(i):.0f},{py(v):.0f}" for i,v in enumerate(hrs)) + f" L{x1},{y1} Z"
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Hours in, leads flat","THE REAL INVOICE")}
      <div style="display:flex;gap:24px;margin-bottom:6px">
        <div style="display:flex;align-items:center;gap:9px"><span style="width:26px;height:4px;border-radius:3px;background:rgb({ACC})"></span>
          <span style="font-family:DM Sans;font-size:15px;color:#d9d5cc">weekends on plumbing</span></div>
        <div style="display:flex;align-items:center;gap:9px"><span style="width:26px;height:4px;border-radius:3px;background:rgb({RED})"></span>
          <span style="font-family:DM Sans;font-size:15px;color:#d9d5cc">leads booked</span></div></div>
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block">
        <defs><linearGradient id="af" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.30)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient></defs>
        {grid}
        <line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="rgba(250,250,247,.16)"/>
        <line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="rgba(250,250,247,.16)"/>
        <path d="{area}" fill="url(#af)"/>
        <polyline points="{hpts}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <polyline points="{lpts}" fill="none" stroke="rgb({RED})" stroke-width="3.5" stroke-dasharray="7 6" stroke-linecap="round"/>
        <circle cx="{px(5):.0f}" cy="{py(hrs[5]):.0f}" r="7" fill="rgb({ACC})"/>
        <text x="{px(5)-12:.0f}" y="{py(hrs[5])-14:.0f}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">62 hrs</text>
        <text x="{px(5)-8:.0f}" y="{py(lds[5])-16:.0f}" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="17" fill="#e8a892">0 booked</text>
        {xlab}
      </svg>
      {cap("every weekend on plumbing is a weekend not selling. that is the invoice.")}</div>'''

# 5. INSTALL - clean constellation: the Ultron sphere hub, 7 named agents already wired, all checked
def install():
    cx,cy,R=350,250,205
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    edges=""; nodes=""
    n=len(agents)
    for i,nm in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        edges+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
        nodes+=(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#2a2724" stroke="rgba(212,162,127,.5)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="#e6d6c2">{nm}</text>'
          f'<circle cx="{x+30:.0f}" cy="{y-30:.0f}" r="11" fill="#141210"/>'
          f'<circle cx="{x+30:.0f}" cy="{y-30:.0f}" r="9" fill="rgba(127,211,154,.16)" stroke="#7fd39a" stroke-width="1"/>'
          f'<path d="M{x+25:.0f} {y-30:.0f} l3.5 3.5 l6 -7" fill="none" stroke="#7fd39a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, already wired","7 / 7 COMPOSING")}
      <svg width="700" height="500" viewBox="0 0 700 500" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="38%" cy="30%"><stop offset="0%" stop-color="#6db4ff"/><stop offset="34%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {edges}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="74" fill="url(#hub)"/></g>
        <ellipse cx="{cx-22}" cy="{cy-26}" rx="22" ry="13" fill="rgba(255,255,255,.4)" transform="rotate(-28 {cx-22} {cy-26})"/>
        <text x="{cx}" y="{cy+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">ULTRON</text>
        {nodes}
      </svg>
      {cap("cortex, specter, striker and the rest: built, tested, composing with each other.")}</div>'''

# 6. AUDITED - a gauge: every cycle audits its own work, and a lock chip parks each external send
def audited():
    cx,cy,r=300,270,175; a0,a1=180,360  # bottom-open semicircle track (drawn as top arc 180->360)
    def pt(ang): return (cx+r*math.cos(math.radians(ang)), cy+r*math.sin(math.radians(ang)))
    x0,y0=pt(a0); x1,y1=pt(a1)
    val=1.0; av=a0+(a1-a0)*val  # needle at full coverage
    nx,ny=cx+(r-30)*math.cos(math.radians(av)), cy+(r-30)*math.sin(math.radians(av))
    ticks=""
    for k in range(0,6):
        ta=a0+(a1-a0)*k/5; ix,iy=pt(ta); ox,oy=cx+(r+14)*math.cos(math.radians(ta)),cy+(r+14)*math.sin(math.radians(ta))
        ticks+=f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="rgba(250,250,247,.22)" stroke-width="2"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="440" height="330" viewBox="0 0 440 330">
        <defs><linearGradient id="gv" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#7a4326"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="ng" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        <path d="M{x0:.0f} {y0:.0f} A{r} {r} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="rgba(250,250,247,.10)" stroke-width="22" stroke-linecap="round"/>
        <path d="M{x0:.0f} {y0:.0f} A{r} {r} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="url(#gv)" stroke-width="22" stroke-linecap="round"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="13" fill="rgb({ACC})"/>
        <text x="{cx}" y="{cy-34}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#FAFAF7">100%</text>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">CYCLES AUDITED</text>
      </svg>
      <div style="flex:1">
        {htitle("Audited, not just running","SELF-CHECK")}
        <div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">
          <div style="display:flex;align-items:center;gap:14px">
            <div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(212,162,127,.13);border:1px solid rgba(212,162,127,.4);display:flex;align-items:center;justify-content:center">
              <svg width="24" height="24" viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2.5" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/><path d="M7.5 10 V7 a4.5 4.5 0 0 1 9 0 v3" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/></svg></div>
            <div><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">Every external send</div>
            <div style="font-family:DM Sans;font-size:16px;color:#8f8f85">parks for your tap</div></div></div>
        </div>
        {cap("their loop is a demo. this one checks its own work every cycle.")}
      </div></div>'''

# 7. FIRSTRUN - IVORY chat mockup: one sentence typed at 09:14, twenty briefs back by 09:23
def firstrun():
    briefs=[("Northwind Robotics","hiring 3 ops roles","92"),
            ("Globex Systems","raised $4M in May","88"),
            ("Initech","no AI layer yet","81")]
    rows=""
    for a,b,c in briefs:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.62);border:1px solid rgba(120,95,60,.14);'
          f'border-radius:14px;padding:14px 18px">'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">{a}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#7a6650;margin-top:1px">{b}</div></div>'
          f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:#96562d;padding:8px 15px;border-radius:11px">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:21px;color:#fdfbf6;line-height:1">{c}</span>'
          f'<span style="font-family:DM Mono;font-size:9px;letter-spacing:.1em;color:rgba(253,251,246,.72)">FIT</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("One sentence in, twenty out","FIRST RUN","#2a2016","#96562d")}
      <div style="background:rgba(255,255,255,.5);border:1px solid rgba(120,95,60,.16);border-radius:16px;padding:18px 20px;
        display:flex;align-items:center;gap:14px;margin-bottom:16px">
        <span style="font-family:DM Mono;font-weight:500;font-size:20px;color:#96562d">&gt;</span>
        <span style="flex:1;font-family:DM Sans;font-weight:600;font-size:20px;color:#2a2016">Source my next twenty accounts</span>
        <span style="font-family:DM Mono;font-size:14px;color:#a08a68">09:14</span></div>
      <div style="display:flex;flex-direction:column;gap:11px">{rows}
        <div style="text-align:center;font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#a08a68;padding-top:4px">+ 17 more briefs</div></div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:16px;background:#96562d;border-radius:14px;padding:14px 22px">
        <span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#fdfbf6">20 briefs, ranked</span>
        <span style="font-family:DM Mono;font-size:14px;color:rgba(253,251,246,.82)">ready 09:23 &middot; 9 min</span></div>
      {cap("typed at 09:14, twenty ranked briefs on your screen by 09:23.","#8a745a")}</div>'''

# 8. VERDICT - closing split: build the product (lit), not the plumbing (dim, struck out)
def verdict():
    build=["your offer","your distribution","your customers"]
    plumb=["agent graphs","retry logic","state machines"]
    def li(t,good):
        if good:
            ic=f'<svg width="20" height="20" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            col="#e6d6c2";deco=""
        else:
            ic=f'<svg width="20" height="20" viewBox="0 0 24 24"><path d="M7 7l10 10M17 7L7 17" stroke="rgb({RED})" stroke-width="2.4" stroke-linecap="round"/></svg>'
            col="#8f8f85";deco="text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)"
        return f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:13px"><span style="flex-shrink:0">{ic}</span><span style="font-family:DM Sans;font-size:19px;color:{col};{deco}">{t}</span></div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Build your product","NOT YOUR PLUMBING")}
      <div style="display:flex;gap:20px;align-items:stretch">
        <div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:22px;padding:26px 26px 22px;
          box-shadow:0 0 40px rgba(212,162,127,.16), inset 0 2px 3px rgba(255,255,255,.1)">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:rgb({ACC});margin-bottom:16px">BUILD THIS</div>
          {"".join(li(x,True) for x in build)}</div>
        <div style="flex-shrink:0;display:flex;align-items:center;font-family:DM Sans;font-weight:900;font-size:22px;color:#6f6a60">not</div>
        <div style="flex:1;background:#211e1a;border:1.5px solid rgba(255,255,255,.08);border-radius:22px;padding:26px 26px 22px;opacity:.9">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:#7a7468;margin-bottom:16px">NOT THIS</div>
          {"".join(li(x,False) for x in plumb)}</div>
      </div>
      {cap("the company wins on offers and distribution, not on hand-wired graphs.")}</div>'''

PANELS={"recipe":recipe(),"wiring":wiring(),"breaks":breaks(),"bill":bill(),
        "install":install(),"audited":audited(),"firstrun":firstrun(),"verdict":verdict()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/diytrap"; os.makedirs(outd,exist_ok=True)
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
