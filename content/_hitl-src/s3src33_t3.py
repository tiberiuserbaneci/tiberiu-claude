#!/usr/bin/env python3
# TIER 3 - ENGINEER THE AGENT NOT THE PROMPT. Each panel a UNIQUE hand-built coded scene on a
# clean rounded card (eyes-bar bar): title + one mono caption, no generic stat-chip strips.
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

# 1. THE SHIFT - a coiled re-type prompt loop (muted red, severed) replaced by the config card
def deadloop():
    cx,cy=190,232
    coil=""
    for i in range(5):
        r=118-i*17
        coil+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(200,70,35,{0.20+i*0.05:.2f})" stroke-width="3" stroke-dasharray="9 11"/>'
    # a cut across the coil
    cut=(f'<line x1="{cx+40}" y1="{cy-118}" x2="{cx+96}" y2="{cy-58}" stroke="#1d1d1b" stroke-width="20"/>'
         f'<line x1="{cx+44}" y1="{cy-116}" x2="{cx+92}" y2="{cy-64}" stroke="rgb(200,70,35)" stroke-width="3.5"/>'
         f'<text x="{cx+118}" y="{cy-84}" font-family="DM Mono" font-size="12.5" fill="rgb(200,70,35)">severed</text>')
    prompts=""
    for i,txt in enumerate(["\"act as a...\"","\"you are a...\"","\"rewrite this...\""]):
        prompts+=f'<text x="{cx}" y="{cy-16+i*20}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#6f6a60">{txt}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="400" height="440" viewBox="0 0 400 440">
        {coil}{cut}
        {prompts}
        <text x="{cx}" y="{cy+64}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="rgb(200,70,35)">RE-TYPING LOOP</text>
      </svg>
      <div style="flex:1">
        {htitle("The prompt loop is dead","THE SHIFT")}
        <div style="position:relative;background:linear-gradient(160deg,#3a352e,#241f1a);border:1.5px solid rgb({ACC});border-radius:18px;padding:20px 22px;box-shadow:0 24px 40px rgba(0,0,0,.5),0 0 30px rgba(212,162,127,.22)">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">ULTRON.md</span><span style="font-family:DM Mono;font-size:12px;color:#8f8f85">standing</span></div>
          {"".join(f'<div style="height:9px;border-radius:5px;background:rgba(212,162,127,{a});margin-bottom:9px;width:{w}"></div>' for a,w in [(".55","100%"),(".38","86%"),(".28","94%"),(".2","72%")])}
        </div>
        {cap("you stopped re-typing. the config remembers so you never say it twice.")}
      </div></div>'''

# 2. SKILL 01 - Context engineering: the config spine, rule rows branching into the agent
def context():
    sx=150; top=98; rows=["ICP + market","brand voice","the 7 agents","pricing = cents","human gate","the docs"]
    spine=f'<line x1="{sx}" y1="{top}" x2="{sx}" y2="{top+ (len(rows)-1)*58}" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round"/>'
    branches=""; labels=""
    for i,r in enumerate(rows):
        y=top+i*58
        branches+=(f'<circle cx="{sx}" cy="{y}" r="8" fill="rgb({ACC})"/>'
          f'<path d="M{sx+8} {y} C{sx+80} {y},{sx+120} 230,600 230" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>')
        labels+=f'<text x="{sx+26}" y="{y+5}" font-family="DM Sans" font-weight="700" font-size="18" fill="#d9d5cc">{r}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Context engineering","SKILL 01")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="ag" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="agg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        <text x="{sx}" y="{top-34}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">ULTRON.md</text>
        {spine}{branches}{labels}
        <g filter="url(#agg)"><circle cx="600" cy="230" r="92" fill="url(#ag)"/></g>
        <text x="600" y="222" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">AGENT</text>
        <text x="600" y="250" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">reads it all</text>
      </svg>
      {cap("one config file holds the rules, the voice and the docs. every agent obeys it.")}</div>'''

# 3. SKILL 02 - Agent skills: an isometric skill capsule stamped once, fanning to many agents
def skills():
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL"]
    fan=""
    for i,a in enumerate(agents):
        y=70+i*78
        fan+=(f'<path d="M400 220 C520 220,540 {y+22},640 {y+22}" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<rect x="640" y="{y}" width="150" height="46" rx="12" fill="#241f1a" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="656" y="{y+29}" font-family="DM Mono" font-size="13.5" letter-spacing=".08em" fill="#cfc9bd">{a}</text>'
          f'<path d="M770 {y+16} l7 7 12 -13" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
    caps=""
    for i in range(3):
        off=i*13
        caps+=(f'<g transform="translate({120-off},{170+off})">'
          f'<rect x="0" y="0" width="200" height="120" rx="20" fill="linear" style="fill:#332e28" stroke="rgba(255,255,255,.10)"/>'
          f'</g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Package it once","SKILL 02")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><linearGradient id="cap" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#403a33"/><stop offset="1" stop-color="#241f1a"/></linearGradient>
        <filter id="cs" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="#000" flood-opacity="0.5"/></filter></defs>
        <g transform="translate(96,150)">
          <rect x="26" y="26" width="210" height="128" rx="22" fill="#241f1a" opacity="0.5"/>
          <rect x="13" y="13" width="210" height="128" rx="22" fill="#2b2723" opacity="0.7"/>
          <g filter="url(#cs)"><rect x="0" y="0" width="210" height="128" rx="22" fill="url(#cap)" stroke="rgb({ACC})" stroke-width="1.5"/></g>
          <circle cx="44" cy="44" r="16" fill="rgba(212,162,127,.16)" stroke="rgb({ACC})" stroke-width="1.5"/>
          <path d="M37 44 l5 5 9 -10" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="72" y="50" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">SKILL</text>
          <text x="24" y="92" font-family="DM Mono" font-size="12.5" fill="#a49c8e">outreach.sequence</text>
          <text x="24" y="114" font-family="DM Mono" font-size="12.5" fill="#a49c8e">wrapped &#183; reusable</text>
        </g>
        {fan}
      </svg>
      {cap("wrap any repeatable job into one skill. every agent can call it on demand.")}</div>'''

# 4. SKILL 03 - MCP: one central plug hub, radial spokes to a ring of server nodes
def mcp():
    cx,cy,R=410,206,150
    N=14; nodes=""
    for i in range(N):
        a=math.radians(i*(360/N)-90)
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        nodes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.22)" stroke-width="1.6"/>'
          f'<rect x="{x-19:.0f}" y="{y-15:.0f}" width="38" height="30" rx="8" fill="#241f1a" stroke="rgba(255,255,255,.13)"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="rgb({ACC})"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One plug, every tool","SKILL 03")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub2" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {nodes}
        <g filter="url(#hg2)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#hub2)"/></g>
        <g transform="translate({cx-16},{cy-22})"><rect x="0" y="16" width="32" height="26" rx="6" fill="none" stroke="#2a160c" stroke-width="4"/><path d="M8 16 V6 M24 16 V6" stroke="#2a160c" stroke-width="4" stroke-linecap="round"/></g>
        <text x="{cx}" y="{cy+42}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#2a160c">MCP</text>
        <text x="{cx}" y="436" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="rgb({ACC})">10,000+ servers</text>
      </svg>
      {cap("mcp is the one connector. wire your agent to any tool you already run.")}</div>'''

# 5. SKILL 04 - Plugins and markets (IVORY): a marketplace grid of installable plugin tiles
def market():
    tiles=[("Outreach","installed",True),("Research","install",False),("Deals","install",False),
           ("Content","installed",True),("Legal","install",False),("Publish","install",False)]
    grid=""
    for i,(nm,st,on) in enumerate(tiles):
        r,c=divmod(i,3); x=40+c*230; y=40+r*168
        bd="#96562d" if on else "rgba(120,95,60,.28)"
        chipbg="#96562d" if on else "rgba(150,120,80,.14)"; chipfg="#fdfbf6" if on else "#96562d"
        grid+=(f'<div style="position:absolute;left:{x}px;top:{y}px;width:206px;height:142px;background:rgba(255,255,255,.62);border:1.5px solid {bd};border-radius:20px;box-shadow:0 16px 30px rgba(120,95,60,.16);padding:18px 20px;display:flex;flex-direction:column">'
          f'<div style="width:42px;height:42px;border-radius:13px;background:linear-gradient(160deg,#f3ead9,#e3d3ba);border:1px solid rgba(150,90,45,.22);display:flex;align-items:center;justify-content:center"><div style="width:16px;height:16px;border:2.4px solid #96562d;border-radius:4px"></div></div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016;margin-top:12px">{nm}</div>'
          f'<div style="margin-top:auto"><span style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:{chipfg};background:{chipbg};border-radius:999px;padding:5px 13px">{st}</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("Bundle and ship it","SKILL 04","#2a2016")}
      <div style="position:relative;height:390px;margin:6px auto 0;width:718px">{grid}</div>
      {cap("bundle a whole operator and ship it, or install one in a single command.","#8a745a")}</div>'''

# 6. SKILL 05 - Hooks: a quality gate pipeline, checkpoint ticks, one red block held back
def gate():
    steps=[("draft","hook: banned words",True),("build","hook: tests run",True),("send","gate: your tap",False)]
    lane=""
    for i,(nm,sub,passed) in enumerate(steps):
        x=54+i*248
        col=f"rgb({ACC})" if passed else "rgb(200,70,35)"
        icon=(f'<path d="M{x+30} 118 l14 14 24 -26" fill="none" stroke="rgb({ACC})" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>' if passed
              else f'<g transform="translate({x+28},104)"><rect x="0" y="16" width="46" height="34" rx="7" fill="none" stroke="rgb(200,70,35)" stroke-width="4"/><path d="M8 16 V8 a15 15 0 0 1 30 0 v8" fill="none" stroke="rgb(200,70,35)" stroke-width="4"/></g>')
        lane+=(f'<rect x="{x}" y="70" width="204" height="118" rx="18" fill="#241f1a" stroke="{col}" stroke-width="1.8"/>'
          f'<text x="{x+22}" y="106" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="{col}">{nm.upper()}</text>'
          f'{icon}'
          f'<text x="{x+22}" y="176" font-family="DM Sans" font-size="15.5" fill="#c9c3b8">{sub}</text>')
        if i<2:
            lane+=f'<path d="M{x+204} 129 H{x+248}" stroke="rgba(212,162,127,.5)" stroke-width="3" marker-end="url(#ar)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It polices itself","SKILL 05")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><marker id="ar" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 z" fill="rgb({ACC})"/></marker></defs>
        <g transform="translate(0,90)">{lane}</g>
        <rect x="54" y="316" width="452" height="66" rx="16" fill="rgba(212,162,127,.08)" stroke="rgba(212,162,127,.28)"/>
        <text x="80" y="356" font-family="DM Sans" font-weight="700" font-size="18" fill="#d9d5cc">2 checks passed, 1 held for you</text>
        <rect x="558" y="316" width="204" height="66" rx="16" fill="rgba(200,70,35,.1)" stroke="rgba(200,70,35,.4)"/>
        <text x="660" y="356" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb(200,70,35)">AWAITING TAP</text>
      </svg>
      {cap("hooks and slash commands check every step, so you stop babysitting the output.")}</div>'''

# 7. SKILL 06 - Subagents: a router fanning into seven parallel specialist lanes
def teams():
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    hy=226; rows=""
    for i,(nm,role) in enumerate(agents):
        y=48+i*57
        rows+=(f'<path d="M170 {hy} C300 {hy},340 {y+18},430 {y+18}" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
          f'<rect x="430" y="{y}" width="336" height="40" rx="11" fill="#241f1a" stroke="rgba(255,255,255,.1)"/>'
          f'<circle cx="454" cy="{y+20}" r="5" fill="rgb({ACC})"/>'
          f'<text x="474" y="{y+26}" font-family="DM Mono" font-size="13.5" letter-spacing=".08em" fill="#e4dfd4">{nm}</text>'
          f'<text x="756" y="{y+26}" text-anchor="end" font-family="DM Sans" font-size="14.5" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Run a fleet","SKILL 06")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="rt" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {rows}
        <g filter="url(#rg)"><circle cx="90" cy="{hy}" r="58" fill="url(#rt)"/></g>
        <text x="90" y="{hy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">ROUTER</text>
        <text x="90" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">splits it</text>
      </svg>
      {cap("one brief splits across seven specialists working in parallel, not one at a time.")}</div>'''

# 8. SKILL 07 - Dynamic workflows: a bezier flow graph self-generating hundreds of parallel runs
def flows():
    ax,ay=118,226
    ends=[(720,70),(760,150),(772,226),(760,302),(720,382)]
    mid=[(400,120),(430,180),(440,226),(430,272),(400,332)]
    graph=""
    for (mx,my),(ex,ey) in zip(mid,ends):
        graph+=(f'<path d="M{ax+42} {ay} C{ax+150} {ay},{mx-80} {my},{mx} {my}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
          f'<path d="M{mx} {my} C{mx+90} {my},{ex-70} {ey},{ex-46} {ey}" fill="none" stroke="rgba(212,162,127,.22)" stroke-width="1.8"/>'
          f'<circle cx="{mx}" cy="{my}" r="14" fill="#2b2723" stroke="rgb({ACC})" stroke-width="1.6"/>'
          f'<path d="M{mx-5} {my} l4 4 7 -8" fill="none" stroke="rgb({ACC})" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    runs=""
    for ex,ey in ends:
        runs+=f'<rect x="{ex-46}" y="{ey-15}" width="92" height="30" rx="8" fill="#241f1a" stroke="rgba(255,255,255,.12)"/><circle cx="{ex-30}" cy="{ey}" r="4" fill="rgb({ACC})"/><text x="{ex-16}" y="{ey+4}" font-family="DM Mono" font-size="11" fill="#a49c8e">run</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It writes its own runs","SKILL 07")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="br" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="brg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {graph}{runs}
        <g filter="url(#brg)"><circle cx="{ax}" cy="{ay}" r="52" fill="url(#br)"/></g>
        <text x="{ax}" y="{ay-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">1 BRIEF</text>
        <text x="{ax}" y="{ay+18}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">plain english</text>
        <text x="700" y="432" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="rgb({ACC})">300+ runs, one brief</text>
      </svg>
      {cap("dynamic workflows spawn hundreds of parallel runs from a single plain-english brief.")}</div>'''

PANELS={"deadloop":deadloop(),"context":context(),"skills":skills(),"mcp":mcp(),
        "market":market(),"gate":gate(),"teams":teams(),"flows":flows()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src33"; os.makedirs(outd,exist_ok=True)
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
