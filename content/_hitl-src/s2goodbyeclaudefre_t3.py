#!/usr/bin/env python3
# TIER 3 - GOODBYE CLAUDE? / OWN THE SYSTEM. Reframe of the "free model of the week" trap: Ultron
# routes every job across Lite/Smart/Deep automatically, you own the OS on top. Each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO stat-chip strips.
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

# 1. TRAP - IVORY timeline of the model-of-the-week churn: 4 dated migrations, each ported model
# struck out in muted red, the last still in-flight. Distinct scene: horizontal timeline.
def trap():
    events=[("JAN","GPT wave","2 days porting",False),
            ("MAR","Llama tune","4 days porting",False),
            ("MAY","frontier X","3 days porting",False),
            ("JUL","free GLM","porting now",True)]
    cols=""
    for mo,md,note,live in events:
        dotc="#96562d" if live else "rgba(200,70,35,.9)"
        glow="box-shadow:0 0 16px rgba(150,90,45,.55)" if live else ""
        strike="" if live else "text-decoration:line-through;text-decoration-color:rgba(200,70,35,.85);text-decoration-thickness:2px;"
        namec="#2a2016" if live else "#7a6a55"
        bd="1.5px solid #96562d" if live else "1px solid rgba(120,95,60,.20)"
        tag=("still chasing" if live else "abandoned")
        tagc="#96562d" if live else "#b06a4a"
        cols+=(f'<div style="width:180px;text-align:center;position:relative">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:#a08a68;margin-bottom:10px">{mo}</div>'
          f'<div style="width:18px;height:18px;border-radius:50%;background:{dotc};margin:0 auto;position:relative;z-index:2;{glow}"></div>'
          f'<div style="margin-top:26px;background:rgba(255,255,255,.62);border:{bd};border-radius:14px;padding:16px 12px 14px">'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:19px;color:{namec};{strike}">{md}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8a745a;margin-top:5px">{note}</div>'
          f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:{tagc};margin-top:8px">{tag}</div>'
          f'</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 38px 34px">
      {htitle("You migrated four times this quarter","THE TRAP","#2a2016","#96562d")}
      <div style="position:relative;padding-top:22px">
        <div style="position:absolute;left:12%;right:12%;top:38px;height:3px;background:linear-gradient(90deg,rgba(200,70,35,.35),rgba(150,90,45,.55))"></div>
        <div style="display:flex;justify-content:space-between;position:relative">{cols}</div>
      </div>
      {cap("every hyped model costs days of porting and breaks what already worked.","#8a745a")}</div>'''

# 2. ROUTER - one job token routed down 3 tier lanes, SMART lane lit/picked (model-router node graph)
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
    hubx,hy=170,230; lx=470
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C320 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:300px;top:{y-40}px;width:160px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One job in. The right tier out.","THE ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">draft 12<br>follow-ups</div>
        {cards}
      </div>
      {cap("you never pick a model. the cheapest tier that can do the job wins.")}</div>'''

# 3. TIERS - IVORY: three dial gauges, cents cost per tier, SMART lit as the default (tier gauge)
def tiers():
    gauges=[("LITE","Haiku","quick lookups","0.02c",22,False),
            ("SMART","Sonnet","daily execution","0.11c",60,True),
            ("DEEP","Opus","hard judgement","0.40c",96,True)]
    r=66; circ=2*math.pi*r
    cells=""
    for nm,md,role,cost,pct,dark in gauges:
        dash=circ*pct/100
        lit=(nm=="SMART")
        track="rgba(150,90,45,.16)"
        arc="#96562d"
        ring=(f'<svg width="170" height="170" viewBox="0 0 170 170">'
          f'<circle cx="85" cy="85" r="{r}" fill="none" stroke="{track}" stroke-width="14"/>'
          f'<circle cx="85" cy="85" r="{r}" fill="none" stroke="{arc}" stroke-width="14" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 85 85)"/></svg>')
        halo="box-shadow:0 0 0 2px #96562d, 0 18px 34px rgba(150,90,45,.20);" if lit else "box-shadow:0 12px 24px rgba(120,95,60,.12);"
        badge=(f'<div style="font-family:DM Mono;font-size:10px;letter-spacing:.12em;color:#96562d;margin-top:2px">DEFAULT</div>' if lit else f'<div style="font-family:DM Mono;font-size:10px;letter-spacing:.12em;color:#b7a488;margin-top:2px">&nbsp;</div>')
        cells+=(f'<div style="flex:1;text-align:center;background:rgba(255,255,255,.58);border:1px solid rgba(120,95,60,.16);border-radius:20px;padding:20px 14px 22px;{halo}">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:#2a2016">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8a745a;margin-bottom:8px">{md}</div>'
          f'<div style="position:relative;width:170px;height:170px;margin:0 auto">{ring}'
          f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#2a2016;line-height:1">{cost}</span>'
          f'<span style="font-family:DM Mono;font-size:11px;color:#96562d">per job</span></div></div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#5a4634;margin-top:10px">{role}</div>{badge}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 34px 32px">
      {htitle("Three tiers. Priced in cents.","THE TIERS","#2a2016","#96562d")}
      <div style="display:flex;gap:16px">{cells}</div>
      {cap("lookups on lite, daily work on smart, hard calls on deep. always cents.","#8a745a")}</div>'''

# 4. STACK - model constellation: a central ROUTER hub wired to a scatter of model sockets (star field)
def constellation():
    cx,cy=410,235
    stars=[("frontier",120,80),("coding",690,110),("open-weight",150,300),("cheap",700,320),
           ("fast",300,60),("reasoning",560,60),("vision",250,410),("long-context",600,410)]
    lines=""; nodes=""
    for nm,x,y in stars:
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="rgba(212,162,127,.22)" stroke-width="1.6"/>'
    for nm,x,y in stars:
        nodes+=(f'<g><circle cx="{x}" cy="{y}" r="8" fill="rgb({ACC})" filter="url(#st)"/>'
          f'<rect x="{x-58}" y="{y+14}" width="116" height="30" rx="9" fill="#221f1b" stroke="rgba(255,255,255,.08)"/>'
          f'<text x="{x}" y="{y+34}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">{nm}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every model is just a socket","THE STACK")}
      <svg width="820" height="480" viewBox="0 0 820 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="cw" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="st" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {lines}{nodes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="74" fill="url(#cw)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">owns the wall</text>
      </svg>
      {cap("the router wires to all of them. you own the wall, not any one plug.")}</div>'''

# 5. AUTO-ADOPT - radar sweep: new models detected as blips, adopted with zero migration (radar)
def radar():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("free GLM 5.2",300,150),("cheaper tier",120,96),("new frontier",210,168),("faster mini",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">Detected</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">02:14</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">Routed live</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">02:19</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">0 migrations</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("A better model ships. Adopted.","AUTO-ADOPT")}
        {lead}
        {cap("the router watches the field and routes to it. no weekend rewrites.")}
      </div></div>'''

# 6. ROSTER - radial hub: 7 named agents as spokes around one Ultron core (radial hub)
def roster():
    cx,cy=410,230; Rr=178
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    spokes=""; nodes=""
    n=len(agents)
    for i,nm in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".04em" fill="#d9d5cc">{nm}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents. One operator.","THE ROSTER")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="70" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">ULTRON</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one memory</text>
        {nodes}
      </svg>
      {cap("research, outbound, deals, content, code, publishing, legal - one core.")}</div>'''

# 7. REAL NUMBERS - dot field of ~968 (a handful lit = one job's true cost in cents) (dot field)
def cents():
    cols,rowsn=44,22
    lit={57,241,410,588,760,933,150}
    dots=""
    cell=15; gap=3
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 32px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">3c</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">per thousand rows</span></div>
        <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">REAL NUMBERS</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="font-family:'DM Mono';font-size:14px;color:#8f8f85;margin-top:16px">you pay per token, not per hype cycle. the scary invoice was the tool you replaced.</div></div>'''

# 8. GATE - isometric stack of pending outbound actions, each parked for the human tap (iso stack)
def gate():
    steps=[("SEND","240 cold emails","waiting"),("PUBLISH","6 posts queued","waiting"),("EXECUTE","3 proposals out","tap to send")]
    cards=""
    for i,(nm,sub,st) in enumerate(steps):
        y=i*128; live=(i==len(steps)-1)
        lock=(f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgb({ACC});display:flex;align-items:center;justify-content:center">'
              f'<svg width="24" height="24" viewBox="0 0 24 24"><path d="M5 11h14v9H5z" fill="none" stroke="#1a0f0a" stroke-width="2.2"/><path d="M8 11V8a4 4 0 0 1 8 0v3" fill="none" stroke="#1a0f0a" stroke-width="2.2"/></svg></div>'
          if live else
              f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">'
              f'<svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 11h12v8H6z" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><path d="M9 11V8a3 3 0 0 1 6 0v3" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/></svg></div>')
        stc=f"rgb({ACC})" if live else "#8f8f85"
        bd="rgba(212,162,127,.55)" if live else "rgba(255,255,255,.14)"
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid {bd};border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'{lock}'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div>'
          f'<div style="flex-shrink:0;font-family:DM Mono;font-size:13px;color:{stc}">{st}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Nothing sends without your tap","THE GATE")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">HUMAN GATE</div></div></div>
      {cap("every external move parks at the gate. augmented, never unsupervised.")}</div>'''

PANELS={"trap":trap(),"router":router(),"tiers":tiers(),"constellation":constellation(),
        "radar":radar(),"roster":roster(),"cents":cents(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2goodbyeclaudefre"; os.makedirs(outd,exist_ok=True)
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
