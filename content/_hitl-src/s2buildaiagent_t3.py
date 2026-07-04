#!/usr/bin/env python3
# TIER 3 - STOP BUILDING AGENTS. Ultron reframe of a LangChain/LangGraph "build an agent from
# scratch" tutorial: founders do not code agents, they operate seven pre-wired ones in plain English.
# Each panel is a UNIQUE hand-built coded scene on a clean rounded card, title + one mono caption.
# NO stat-chip strips, NO cuts / extruded walls. Warm palette. Cents pricing. Founder-facing.
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

# 1. SCRATCH - NODE GRAPH: an overloaded YOU hub, six DIY parts tangled around it, two edges severed red
def scratch():
    cx,cy=306,238
    parts=[("framework",118,86,False),("vector store",500,84,False),("evals",540,250,True),
           ("orchestration",396,412,True),("glue code",96,398,False),("prompt tuning",192,150,False)]
    edges=""; nodes=""
    for i,(nm,x,y,bad) in enumerate(parts):
        col="rgb(200,70,35)" if bad else "rgba(212,162,127,.5)"; dash='stroke-dasharray="5 9"' if bad else ""
        mx=(cx+x)//2
        edges+=f'<path d="M{cx} {cy} C{mx+50} {y-40},{mx-40} {cy+46},{x} {y}" fill="none" stroke="{col}" stroke-width="{2.4 if bad else 3}" {dash}/>'
        nodes+=(f'<circle cx="{x}" cy="{y}" r="36" fill="#221f1b" stroke="{"rgba(200,70,35,.6)" if bad else "rgba(255,255,255,.12)"}" stroke-width="2"/>'
          f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="{"#c86a4b" if bad else "#cfc9bd"}">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You wired it by hand","FROM SCRATCH")}
      <svg width="620" height="470" viewBox="0 0 620 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="you" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="yg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#yg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#you)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">YOU</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">the plumber</text>
      </svg>
      {cap("six moving parts, two already broken. months before it says hello.")}</div>'''

# 2. ROSTER - RADIAL HUB: seven named agents pre-wired around one ROUTER core
def roster():
    cx,cy,R=306,238,180
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    spokes=""; nodes=""
    for i,nm in enumerate(agents):
        a=math.radians(-90+i*(360/7))
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        w=118
        nodes+=(f'<g transform="translate({x-w/2:.0f},{y-20:.0f})"><rect width="{w}" height="40" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{w/2:.0f}" y="25" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#e2dccf">{nm}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, already wired","THE ROSTER")}
      <svg width="620" height="480" viewBox="0 0 620 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spokes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">ROUTER</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">composes them</text>
        {nodes}
      </svg>
      {cap("cortex, specter, striker, pulse, sentinel, amplify, counsel. nothing to assemble.")}</div>'''

# 3. ROUTER - ORG CHART: plain English drops into the router, which hires an agent and a model tier
def router():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Plain English hires the worker","THE ROUTER")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><linearGradient id="ib" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <radialGradient id="rt" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <!-- level 0: your sentence -->
        <rect x="230" y="24" width="360" height="58" rx="16" fill="url(#ib)" stroke="rgba(255,255,255,.10)"/>
        <text x="410" y="60" text-anchor="middle" font-family="DM Mono" font-size="17" fill="#e2dccf">"write 20 follow-ups"</text>
        <line x1="410" y1="82" x2="410" y2="128" stroke="rgba(212,162,127,.5)" stroke-width="3"/>
        <!-- level 1: router -->
        <g filter="url(#rg)"><rect x="330" y="128" width="160" height="72" rx="20" fill="url(#rt)"/></g>
        <text x="410" y="162" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">ROUTER</text>
        <text x="410" y="184" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        <!-- level 2: three candidate agents, SPECTER picked -->
        <path d="M410 200 V236 H190 V262" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2.4"/>
        <path d="M410 200 V262" fill="none" stroke="rgb({ACC})" stroke-width="4"/>
        <path d="M410 200 V236 H630 V262" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2.4"/>
        {"".join(f'<g transform="translate({x-72},262)"><rect width="144" height="56" rx="14" fill="#221f1b" stroke="{bd}" stroke-width="{bw}"/><text x="72" y="34" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".05em" fill="{tc}">{nm}</text></g>' for x,nm,bd,bw,tc in [(190,"CORTEX","rgba(255,255,255,.10)",1.5,"#9a9488"),(410,"SPECTER",f"rgb({ACC})",2.5,"#FAFAF7"),(630,"STRIKER","rgba(255,255,255,.10)",1.5,"#9a9488")])}
        <!-- level 3: model tier under the picked agent -->
        <line x1="410" y1="318" x2="410" y2="356" stroke="rgb({ACC})" stroke-width="4"/>
        <rect x="316" y="356" width="188" height="70" rx="16" fill="#2a2622" stroke="rgb({ACC})" stroke-width="1.5"/>
        <text x="410" y="388" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">SMART TIER</text>
        <text x="410" y="412" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#FAFAF7">0.11c / run</text>
      </svg>
      {cap("it hires the right agent and the cheapest model tier that can do the job. no config.")}</div>'''

# 4. COMPOSE - TIMELINE: agents hand off down one thread, ending at the human gate
def compose():
    steps=[("CORTEX","researched the account","09:00",False),
           ("SPECTER","drafted the sequence","09:02",False),
           ("STRIKER","built the close plan","09:05",False),
           ("HUMAN GATE","waits for your tap","09:06",True)]
    n=len(steps); x0,x1=90,730; y=200; dx=(x1-x0)/(n-1)
    line=f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgba(212,162,127,.4)" stroke-width="3"/>'
    marks=""
    for i,(nm,sub,t,gate) in enumerate(steps):
        x=x0+i*dx; up=(i%2==0)
        ty=y-64 if up else (y+70 if gate else y+52)
        if gate:
            marks+=(f'<rect x="{x-26}" y="{y-26}" width="52" height="52" rx="14" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>'
              f'<g transform="translate({x-15},{y-16})"><rect x="0" y="13" width="30" height="22" rx="5" fill="none" stroke="rgb({ACC})" stroke-width="3.2"/><path d="M6 13 V7 a9 9 0 0 1 18 0 v6" fill="none" stroke="rgb({ACC})" stroke-width="3.2"/></g>')
        else:
            marks+=f'<circle cx="{x}" cy="{y}" r="16" fill="rgb({ACC})"/><circle cx="{x}" cy="{y}" r="7" fill="#1a0f0a"/>'
        col=f"rgb({ACC})" if gate else "#FAFAF7"
        marks+=(f'<text x="{x}" y="{ty}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="{col}">{nm}</text>'
          f'<text x="{x}" y="{ty+(-20 if up else 22)}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{t}</text>'
          f'<text x="{x}" y="{ty+(22 if up else -18)}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#a8a296">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {htitle("They hand off to each other","ONE THREAD")}
      <svg width="820" height="400" viewBox="0 0 820 400" style="display:block;margin:0 auto">
        {line}{marks}
      </svg>
      {cap("research, write, close, then your approval. a team on one thread, not a lone bot.")}</div>'''

# 5. STACK - ISO STACK: the DIY layers you would own, collapsed under one bright Ultron block
def stack():
    layers=[("glue + retries",0.7),("evals harness",0.58),("orchestration",0.46),("vector store",0.36)]
    cards=""
    for i,(nm,op) in enumerate(layers):
        y=110+i*82
        cards+=(f'<div style="position:absolute;left:40px;top:{y}px;width:480px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1.5px solid rgba(255,255,255,.08);border-radius:16px;padding:14px 22px;box-shadow:0 22px 34px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.06);opacity:{op}">'
          f'<div style="font-family:DM Mono;font-size:15px;letter-spacing:.06em;color:#9a9488">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#6f6a60;margin-top:1px">you would own this</div></div>')
    top=(f'<div style="position:absolute;left:0px;top:0px;width:540px;background:linear-gradient(160deg,#463d34,#2b2723);border:1.5px solid rgb({ACC});border-radius:20px;padding:22px 28px;box-shadow:0 38px 56px rgba(0,0,0,.6),0 0 40px rgba(212,162,127,.22), inset 0 2px 3px rgba(255,255,255,.14);display:flex;align-items:center;gap:20px">'
      f'<div style="flex-shrink:0;width:54px;height:54px;border-radius:16px;background:radial-gradient(circle at 36% 30%,#f0c49e,rgb({ACC}) 55%,#7a4326);box-shadow:0 0 22px rgba(212,162,127,.5)"></div>'
      f'<div><div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#FAFAF7">ULTRON</div>'
      f'<div style="font-family:DM Mono;font-size:13px;color:rgb({ACC});margin-top:2px">all of it, pre-wired</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The whole stack, collapsed","YOU SKIP IT")}
      <div style="perspective:2100px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(17deg) rotateZ(-7deg);width:560px;height:430px;position:relative">{cards}{top}</div></div>
      {cap("framework, memory, evals, orchestration. one block instead of six you maintain.")}</div>'''

# 6. CENTS - GAUGE (ivory): a dial that barely moves off zero, priced in cents per run
def cents():
    a0,a1=-210,30                       # sweep in degrees
    cx,cy,r=175,180,128
    val=a0+(a1-a0)*0.14                 # needle near the low end
    def pt(ang,rr):
        rad=math.radians(ang); return cx+rr*math.cos(rad), cy+rr*math.sin(rad)
    ax0,ay0=pt(a0,r); ax1,ay1=pt(a1,r)
    arc=f'<path d="M{ax0:.1f} {ay0:.1f} A{r} {r} 0 1 1 {ax1:.1f} {ay1:.1f}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="18" stroke-linecap="round"/>'
    litend=pt(val,r); larc=f'<path d="M{ax0:.1f} {ay0:.1f} A{r} {r} 0 0 1 {litend[0]:.1f} {litend[1]:.1f}" fill="none" stroke="#96562d" stroke-width="18" stroke-linecap="round"/>'
    ticks=""
    for k in range(0,11):
        ang=a0+(a1-a0)*k/10; ix,iy=pt(ang,r-16); ox,oy=pt(ang,r+2)
        ticks+=f'<line x1="{ix:.1f}" y1="{iy:.1f}" x2="{ox:.1f}" y2="{oy:.1f}" stroke="rgba(120,80,40,.35)" stroke-width="2"/>'
    nx,ny=pt(val,r-30)
    needle=f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#96562d" stroke-width="6" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="11" fill="#96562d"/>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:10px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Priced in cents, not headcount</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PAY PER TOKEN</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <svg width="350" height="330" viewBox="0 0 350 330" style="flex-shrink:0">
          {arc}{larc}{ticks}{needle}
          <text x="{cx}" y="{cy+68}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="52" fill="#2a2016">4c</text>
          <text x="{cx}" y="{cy+96}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#96562d">PER FULL RUN</text>
        </svg>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4">
            An engineer to build and babysit your own agent costs a salary. This costs a coffee.</div>
          <div style="display:flex;gap:22px;margin-top:16px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["no seats","no retainer","cents per job"])}
          </div></div>
      </div>
      {cap("the router picks the cheapest tier that works. a full job lands in cents.","#8a745a")}</div>'''

# 7. MEMORY - DOT FIELD: one shared core of records every agent reads from
def memory():
    cols,rows=34,18; cell=13; gap=6
    lit={110,111,144,145,178,179,212,213,246,247}  # a bright cluster = the account in focus
    dots=""
    for i in range(cols*rows):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rows*(cell+gap)-gap
    chips="".join(f'<span style="font-family:DM Mono;font-size:13px;color:#c9c3b8;background:#221f1b;border:1px solid rgba(255,255,255,.1);border-radius:999px;padding:7px 15px">{x}</span>' for x in ["ICP","pipeline","pricing","docs"])
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One memory, shared by all seven","THE CORE")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="display:flex;gap:12px;justify-content:center;margin-top:20px">{chips}</div>
      {cap("every agent draws from the same core. nothing you told it once is ever forgotten.")}</div>'''

# 8. WATCH - RADAR: the eyes come pre-wired, sweeping live market signals
def watch():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Stack",210,168),("Intent",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("The eyes are already on","LIVE SIGNALS")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">CORTEX sweeps funding, hiring, stack and intent while you sleep. No scraper to build, no pipeline to babysit.</div>
        {cap("built in, not bolted on. the account moves, you hear about it first.")}</div></div>'''

PANELS={"scratch":scratch(),"roster":roster(),"router":router(),"compose":compose(),
        "stack":stack(),"cents":cents(),"memory":memory(),"watch":watch()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2buildaiagent"; os.makedirs(outd,exist_ok=True)
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
