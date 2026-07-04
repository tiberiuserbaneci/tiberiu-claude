#!/usr/bin/env python3
# TIER 3 - THE TOP FLOOR IS EMPTY (s3src23). Layered-AI-stack angle: foundation models are the
# floor, research + agents rise above, and the top operator floor is the one nobody installs -
# Ultron owns it. Each panel a UNIQUE hand-built coded scene on a clean rounded card. WIRE-ITS-EYES bar.
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

# 1. FLOOR - a front-on row of foundation-model plinths (bedrock). Swappable, rented by the token.
def floor():
    plinths=[("CLAUDE",True),("GPT-5",False),("GEMINI",False),("GROK",False)]
    w,h=158,132; dx,dy=26,26; x0=54; gap=28; base=316
    blocks=""
    for i,(nm,lit) in enumerate(plinths):
        x=x0+i*(w+gap)
        front="url(#plit)" if lit else "linear-gradient(#2f2b27,#211e1a)"
        top="#f0c49e" if lit else "#3b352f"
        side="#8a4c2c" if lit else "#191613"
        bd="rgb(212,162,127)" if lit else "rgba(255,255,255,.09)"
        tcol="#1a0f0a" if lit else "#cfc9bd"
        # top parallelogram, right side face, front rect
        blocks+=(f'<polygon points="{x},{base} {x+dx},{base-dy} {x+w+dx},{base-dy} {x+w},{base}" fill="{top}"/>'
                 f'<polygon points="{x+w},{base} {x+w+dx},{base-dy} {x+w+dx},{base-dy+h} {x+w},{base+h}" fill="{side}"/>'
                 f'<rect x="{x}" y="{base}" width="{w}" height="{h}" fill="{front}" stroke="{bd}" stroke-width="1.4"/>'
                 f'<text x="{x+w/2:.0f}" y="{base+h/2+2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="{tcol}">{nm}</text>')
        if lit:
            blocks+=f'<text x="{x+w/2:.0f}" y="{base+h/2+26:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="rgba(26,15,10,.72)">DEFAULT</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Models are the floor","THE BEDROCK")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><linearGradient id="plit" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e2a878"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        <text x="410" y="52" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".22em" fill="#7a746a">RAW INTELLIGENCE &middot; RENTED BY THE TOKEN</text>
        {blocks}
        <line x1="30" y1="466" x2="790" y2="466" stroke="rgba(212,162,127,.18)" stroke-width="2"/>
        <text x="410" y="426" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".14em" fill="#8f8f85">SWAP ANY ONE - THE STACK ABOVE DOES NOT MOVE</text>
      </svg>
      {cap("four models, one floor. everything that matters is built on top of them.")}</div>'''

# 2. INFLOW - IVORY: many sources converge via bezier into one brief that feeds up the stack
def inflow():
    src=[("the live web",96),("your docs",188),("data files",280),("call notes",372)]
    hubx,huby=612,234
    edges=""; nodes=""
    for nm,y in src:
        mx=(210+hubx)/2
        edges+=f'<path d="M228 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-72} {huby}" fill="none" stroke="#c6895f" stroke-width="2.6"/>'
        nodes+=(f'<rect x="42" y="{y-27}" width="186" height="54" rx="14" fill="#fbf6ec" stroke="rgba(120,95,60,.22)"/>'
                f'<text x="135" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#5a4634">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Knowledge flows up","THE INTAKE","#2a2016")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="brief" cx="36%" cy="30%"><stop offset="0%" stop-color="#e2a878"/><stop offset="100%" stop-color="#96562d"/></radialGradient>
        <filter id="bs" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="rgba(150,90,45,.4)"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#bs)"><circle cx="{hubx}" cy="{huby}" r="80" fill="url(#brief)"/></g>
        <ellipse cx="588" cy="210" rx="26" ry="15" fill="rgba(255,255,255,.4)" transform="rotate(-28 588 210)"/>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#fdf6ec">ONE</text>
        <text x="{hubx}" y="{huby+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#fdf6ec">BRIEF</text>
        <text x="{hubx}" y="{huby+108}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".12em" fill="#8a745a">READ ONCE, REUSED BY EVERY FLOOR</text>
      </svg>
      {cap("the web, your docs, every file - collapsed into one brief the layers above can act on.","#8a745a")}</div>'''

# 3. AGENTS - radial crew: 7 named agents ringed around one core (the agent layer)
def agents():
    crew=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
          ("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    cx,cy,R=410,238,182
    spokes=""; nodes=""
    for i,(nm,role) in enumerate(crew):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.26)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="44" fill="#241f1a" stroke="rgba(212,162,127,.42)" stroke-width="1.8"/>'
                f'<text x="{x:.0f}" y="{y-3:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14.5" fill="#FAFAF7">{nm}</text>'
                f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven hands, one crew","THE AGENT LAYER")}
      <svg width="820" height="480" viewBox="0 0 820 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#1a0f0a">7</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="#3a2010">AGENTS</text>
        {nodes}
      </svg>
      {cap("named specialists, not one blurry assistant. each owns a single job on the floor.")}</div>'''

# 4. GAP - building elevation: three floors filled, the top OPERATOR floor sits vacant
def gap():
    floors=[("OPERATOR","the layer nobody installs",False),
            ("AGENTS","seven hands",True),
            ("RESEARCH","one brief",True),
            ("FOUNDATION","the models",True)]
    fx0,fw=280,300; fh=88; g=8; y=44
    body=""
    for nm,sub,filled in floors:
        if filled:
            body+=(f'<rect x="{fx0}" y="{y}" width="{fw}" height="{fh}" rx="10" fill="url(#fl)" stroke="rgba(255,255,255,.10)"/>'
                   f'<rect x="{fx0}" y="{y}" width="8" height="{fh}" rx="4" fill="rgb({ACC})"/>'
                   f'<text x="{fx0+30}" y="{y+38}" font-family="DM Sans" font-weight="800" font-size="21" fill="#FAFAF7">{nm}</text>'
                   f'<text x="{fx0+30}" y="{y+64}" font-family="DM Mono" font-size="13" fill="#9a9488">{sub}</text>')
        else:
            body+=(f'<rect x="{fx0}" y="{y}" width="{fw}" height="{fh}" rx="10" fill="rgba(200,70,35,.05)" stroke="rgb(200,70,35)" stroke-width="2" stroke-dasharray="8 8"/>'
                   f'<text x="{fx0+30}" y="{y+38}" font-family="DM Sans" font-weight="800" font-size="21" fill="#c98a6c">{nm}</text>'
                   f'<text x="{fx0+30}" y="{y+64}" font-family="DM Mono" font-size="13" fill="#a86a52">{sub}</text>'
                   f'<text x="{fx0+fw-18}" y="{y+52}" text-anchor="end" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb(200,70,35)">VACANT</text>')
        y+=fh+g
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The top floor sits empty","THE GAP")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><linearGradient id="fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302b"/><stop offset="100%" stop-color="#211e1a"/></linearGradient></defs>
        <ellipse cx="430" cy="422" rx="188" ry="16" fill="rgba(0,0,0,.4)"/>
        {body}
        <text x="150" y="90" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#7a746a">you</text>
        <text x="150" y="112" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#7a746a">wired</text>
        <text x="150" y="134" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#7a746a">these -&gt;</text>
      </svg>
      {cap("models, search, agents - all installed. the floor that runs them, missing.")}</div>'''

# 5. ROUTER - the dispatcher over every model: one job in, cheapest tier that can do it, in cents
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.09c",232,True),("DEEP","hard judgement","0.38c",368,False)]
    hubx,hy,lx=168,232,470
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; wd=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C320 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{wd}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:302px;top:{y-42}px;width:168px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One dispatcher over every model","THE ROUTER")}
      <div style="position:relative;height:464px">
        <svg width="820" height="464" viewBox="0 0 820 464" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="8" y="{hy-30}" width="96" height="60" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:12px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">score<br>240 leads</div>
        {cards}
      </div>
      {cap("you never pick a model. it hires the tier the job needs - cents, not dollars.")}</div>'''

# 6. SPINE - one memory backbone running through every floor, feeding the same core to all
def spine():
    layers=[("OPERATOR",100),("AGENTS",188),("RESEARCH",276),("FOUNDATION",364)]
    mem=[("ICP","who you sell to",100),("PIPELINE","every open deal",188),("PRICING","your real numbers",276),("DOCS","how it all works",364)]
    colx=250; ticks=""; rungs=""; cards=""
    for nm,y in layers:
        ticks+=(f'<circle cx="{colx}" cy="{y}" r="7" fill="rgb({ACC})"/>'
                f'<text x="{colx-24}" y="{y+5}" text-anchor="end" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#8f8f85">{nm}</text>')
    for nm,sub,y in mem:
        rungs+=f'<line x1="{colx}" y1="{y}" x2="330" y2="{y}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        cards+=(f'<div style="position:absolute;left:330px;top:{y-33}px;width:398px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-left:3px solid rgb({ACC});border-radius:14px;padding:12px 18px">'
                f'<div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div>'
                f'<div style="font-family:DM Mono;font-size:12.5px;color:#9a9488;margin-top:1px">{sub}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One memory under the stack","THE SPINE")}
      <div style="position:relative;height:452px">
        <svg width="820" height="452" viewBox="0 0 820 452" style="position:absolute;left:0;top:0">
          <defs><linearGradient id="col" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#211e1a"/></linearGradient>
          <filter id="mg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          <rect x="{colx-18}" y="60" width="36" height="356" rx="18" fill="url(#col)" stroke="rgba(212,162,127,.32)"/>
          {rungs}{ticks}
          <g filter="url(#mg)"><circle cx="{colx}" cy="418" r="30" fill="rgb({ACC})"/></g>
          <text x="{colx}" y="452" text-anchor="middle" font-family="DM Mono" font-size="11.5" letter-spacing=".1em" fill="#8f8f85">MEMORY CORE</text>
        </svg>
        {cards}
      </div>
      {cap("icp, pipeline, pricing, docs - every floor draws the same core. nothing forgets you.")}</div>'''

# 7. GATE - full-capability queued behind the operator's tap: pending actions, one lock
def gate():
    acts=[("24 cold emails","SPECTER"),("1 LinkedIn post","PULSE"),("1 proposal","STRIKER")]
    chips=""
    for i,(nm,who) in enumerate(acts):
        y=70+i*118
        chips+=(f'<div style="position:absolute;left:0;top:{y}px;width:400px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:16px 20px;box-shadow:0 14px 26px rgba(0,0,0,.5);display:flex;align-items:center;gap:16px">'
                f'<span style="width:12px;height:12px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba(212,162,127,.8);flex-shrink:0"></span>'
                f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{nm}</div>'
                f'<div style="font-family:DM Mono;font-size:12px;color:#9a9488;margin-top:1px">drafted by {who}</div></div>'
                f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">PENDING</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing leaves without your tap","THE GATE")}
      <div style="position:relative;height:424px">
        {chips}
        <svg width="820" height="424" viewBox="0 0 820 424" style="position:absolute;left:0;top:0;pointer-events:none">
          <line x1="446" y1="40" x2="446" y2="392" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="3 12" stroke-linecap="round"/>
          <defs><filter id="lk" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter></defs>
          <g filter="url(#lk)"><rect x="560" y="126" width="180" height="170" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/></g>
          <g transform="translate(624,168)"><rect x="0" y="42" width="72" height="54" rx="11" fill="none" stroke="rgb({ACC})" stroke-width="6"/><path d="M13 42 V26 a23 23 0 0 1 46 0 v16" fill="none" stroke="rgb({ACC})" stroke-width="6"/></g>
          <text x="650" y="330" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">YOUR TAP</text>
          <text x="650" y="356" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="rgb({ACC})">3 waiting</text>
        </svg>
      </div>
      {cap("every external move parks at the top floor. augmented, never unsupervised.")}</div>'''

# 8. TOPTIER - IVORY: isometric exploded platform stack, the operator orb seated on the top floor
def toptier():
    tiles=[("FOUNDATION",400),("RESEARCH",322),("AGENTS",244),("MEMORY + GATE",166)]
    cx=410; hw=152; hh=44; th=22
    body=""
    for nm,y in tiles:
        body+=(f'<polygon points="{cx-hw},{y} {cx},{y+hh} {cx},{y+hh+th} {cx-hw},{y+th}" fill="#7a4a2c"/>'
               f'<polygon points="{cx},{y+hh} {cx+hw},{y} {cx+hw},{y+th} {cx},{y+hh+th}" fill="#5f3820"/>'
               f'<polygon points="{cx-hw},{y} {cx},{y-hh} {cx+hw},{y} {cx},{y+hh}" fill="url(#tile)" stroke="rgba(255,255,255,.18)" stroke-width="1"/>'
               f'<text x="{cx}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".08em" fill="#fdf1e2">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Own the top floor","THE OPERATOR LAYER","#2a2016")}
      <svg width="820" height="512" viewBox="0 0 820 512" style="display:block;margin:0 auto">
        <defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c07a44"/><stop offset="100%" stop-color="#8a4c2c"/></linearGradient>
        <radialGradient id="op" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="6" stdDeviation="20" flood-color="rgba(150,90,45,.5)"/></filter></defs>
        {body}
        <line x1="{cx}" y1="122" x2="{cx}" y2="72" stroke="rgba(150,90,45,.45)" stroke-width="2.5" stroke-dasharray="3 7"/>
        <g filter="url(#og)"><circle cx="{cx}" cy="70" r="50" fill="url(#op)"/></g>
        <ellipse cx="394" cy="54" rx="17" ry="10" fill="rgba(255,255,255,.5)" transform="rotate(-28 394 54)"/>
        <text x="{cx}" y="66" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">THE</text>
        <text x="{cx}" y="84" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">OPERATOR</text>
      </svg>
      {cap("foundation, research, agents, memory, gate - one layer seated on top of it all.","#8a745a")}</div>'''

PANELS={"floor":floor(),"inflow":inflow(),"agents":agents(),"gap":gap(),
        "router":router(),"spine":spine(),"gate":gate(),"toptier":toptier()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src23"; os.makedirs(outd,exist_ok=True)
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
