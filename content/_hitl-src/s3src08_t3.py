#!/usr/bin/env python3
# TIER 3 - A REPO IS NOT AN OPERATOR. Adapts the "10 GitHub repos so good they shouldn't be free"
# carousel (AutoHedge, Vibe-Trading: free agent swarms that research/validate/decide/execute) into
# the Ultron eyes-bar bar: 8 UNIQUE hand-built coded scenes, clean rounded cards, one cap each.
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
def htiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'
RED="rgb(200,70,35)"

# 1. STARS - a 1000+ star dot field: many stars, none operated
def stars():
    cols=42; rows=25; x0=44; y0=26; dx=17.9; dy=16.4
    dots=""
    for r in range(rows):
        for c in range(cols):
            i=r*cols+c
            x=x0+c*dx; y=y0+r*dy
            if (i*7)%53<2:
                dots+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3" fill="rgb({ACC})" filter="url(#sg)"/>'
            else:
                dots+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="1.7" fill="rgba(212,162,127,.13)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Stars are not shipped","OPEN SOURCE")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><filter id="sg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="4.5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {dots}
        <rect x="262" y="178" width="296" height="98" rx="18" fill="#1b1916" stroke="rgb({ACC})" stroke-width="1.6"/>
        <text x="410" y="216" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="rgb({ACC})">9,600 STARS</text>
        <text x="410" y="252" text-anchor="middle" font-family="DM Mono" font-size="16" letter-spacing=".08em" fill="#c9c3b8">OPERATED FOR YOU: <tspan fill="{RED}" font-weight="700">0</tspan></text>
      </svg>
      {cap("a starred repo is a bookmark, not a team that runs your services.")}</div>'''

# 2. PIPELINE - horizontal bezier chain: research -> validate -> decide -> execute, all lit
def pipeline():
    nodes=[(120,"CORTEX","research"),(320,"VALIDATE","checks"),(530,"STRIKER","decides"),(730,"AMPLIFY","ships")]
    y=204; r=50
    edges=""
    for i in range(len(nodes)-1):
        x=nodes[i][0]; nx=nodes[i+1][0]
        edges+=(f'<path d="M{x+r} {y} C{x+r+46} {y-38},{nx-r-46} {y+38},{nx-r-8} {y}" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/>'
          f'<path d="M{nx-r-8} {y} l-13 -8 l0 16 Z" fill="rgb({ACC})"/>')
    ncards=""
    for x,nm,sub in nodes:
        ncards+=(f'<g><circle cx="{x}" cy="{y}" r="{r}" fill="url(#nd)" filter="url(#ng)"/>'
          f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/>'
          f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#2a160c">{nm[:2]}</text>'
          f'<text x="{x}" y="{y+r+26}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".06em" fill="#cfc9bd">{nm}</text>'
          f'<text x="{x}" y="{y+r+46}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#8f8f85">{sub}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Research. Decide. Execute.","THE PIPELINE")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="nd" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="13" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g transform="translate(70,300)"><rect x="-52" y="0" width="200" height="46" rx="12" fill="#231f1b" stroke="rgba(255,255,255,.1)"/><text x="48" y="29" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".08em" fill="#c9c3b8">one prompt in</text></g>
        <g transform="translate(600,300)"><rect x="0" y="0" width="200" height="46" rx="12" fill="rgba(212,162,127,.12)" stroke="rgb({ACC})"/><text x="100" y="29" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".08em" fill="rgb({ACC})">shipped, gated</text></g>
        {edges}{ncards}
      </svg>
      {cap("the same four-stage swarm, pointed at your services instead of a trading demo.")}</div>'''

# 3. DEBATE - triangle of agents arguing, edges converge to one verdict node
def debate():
    P={"CORTEX":(410,86),"STRIKER":(214,300),"PULSE":(606,300)}
    verdict=(410,210)
    order=[("CORTEX","STRIKER"),("STRIKER","PULSE"),("PULSE","CORTEX")]
    edges=""
    for a,b in order:
        ax,ay=P[a]; bx,by=P[b]
        mx,my=(ax+bx)/2,(ay+by)/2
        edges+=f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="rgba(212,162,127,.5)" stroke-width="2.4" stroke-dasharray="7 6"/>'
        edges+=f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="14" fill="#231f1b" stroke="rgba(212,162,127,.4)"/><text x="{mx:.0f}" y="{my+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">vs</text>'
    conv=""
    for nm,(x,y) in P.items():
        conv+=f'<line x1="{x}" y1="{y}" x2="{verdict[0]}" y2="{verdict[1]}" stroke="rgba(250,250,247,.10)" stroke-width="1.4"/>'
    nodes=""
    for nm,(x,y) in P.items():
        nodes+=(f'<circle cx="{x}" cy="{y}" r="46" fill="#26221d" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#e7e1d6">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("They argue, then act","AGENT DEBATE")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="vg" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="vf" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {conv}{edges}{nodes}
        <g filter="url(#vf)"><circle cx="{verdict[0]}" cy="{verdict[1]}" r="52" fill="url(#vg)"/></g>
        <text x="{verdict[0]}" y="{verdict[1]-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">VERDICT</text>
        <text x="{verdict[0]}" y="{verdict[1]+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one move</text>
        <text x="410" y="404" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#8f8f85">then parked at the human gate</text>
      </svg>
      {cap("three agents challenge the call, so you get a reasoned move, not a coin flip.")}</div>'''

# 4. ROSTER - radial router hub, seven named agent spokes
def roster():
    cx,cy=410,222; R=168
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; nodes=""
    n=len(agents)
    for i,(nm,role) in enumerate(agents):
        a=math.radians(-90+i*360/n)
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.3)" stroke-width="2" stroke-dasharray="3 7"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="36" fill="#26221d" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-1:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="13" fill="#e7e1d6">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven named owners","THE ROSTER")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="hb" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-90%" y="-90%" width="280%" height="280%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">picks the agent</text>
      </svg>
      {cap("not 64 loose skills. one router hands each job to the agent that owns it.")}</div>'''

# 5. AUTONOMY - a gauge dialled back from full-auto to the human gate, with a lock
def autonomy():
    cx,cy=410,332; R=176; R0=150
    track=" ".join(f"{cx+R*math.cos(math.radians(a)):.0f},{cy-R*math.sin(math.radians(a)):.0f}" for a in range(180,-1,-3))
    red=" ".join(f"{cx+R*math.cos(math.radians(a)):.0f},{cy-R*math.sin(math.radians(a)):.0f}" for a in range(32,-1,-3))
    ticks=""
    for a in range(0,181,30):
        x1=cx+(R-16)*math.cos(math.radians(a)); y1=cy-(R-16)*math.sin(math.radians(a))
        x2=cx+R*math.cos(math.radians(a)); y2=cy-R*math.sin(math.radians(a))
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(250,250,247,.25)" stroke-width="2"/>'
    na=math.radians(122); tipx=cx+R0*math.cos(na); tipy=cy-R0*math.sin(na)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It runs, until your tap","THE GATE")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="pv" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient></defs>
        <polyline points="{track}" fill="none" stroke="rgba(212,162,127,.34)" stroke-width="12" stroke-linecap="round"/>
        <polyline points="{red}" fill="none" stroke="{RED}" stroke-width="12" stroke-linecap="round"/>
        {ticks}
        <text x="{cx-R+6:.0f}" y="{cy+30}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".06em" fill="#9a9488">MANUAL</text>
        <text x="{cx+R-6:.0f}" y="{cy+30}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".06em" fill="{RED}">FULL AUTO</text>
        <line x1="{cx}" y1="{cy}" x2="{tipx:.0f}" y2="{tipy:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="url(#pv)"/>
        <g transform="translate({tipx-24:.0f},{tipy-58:.0f})"><rect x="0" y="20" width="48" height="36" rx="8" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/><path d="M8 20 V10 a16 16 0 0 1 32 0 v10" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/></g>
        <text x="{cx}" y="{cy+70}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">HUMAN GATE</text>
      </svg>
      {cap("the free repo trades unsupervised. every external move here waits for your tap.")}</div>'''

# 6. PRICE - IVORY ledger: the stack it replaces vs cents per run
def price():
    items=[("Quant + analyst tools","$900"),("Data + infra","$1,400"),("Trader / SDR seats","$1,900")]
    rows=""
    for nm,amt in items:
        rows+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:12px 0;border-bottom:1px dashed rgba(120,95,60,.28)">'
          f'<span style="font-family:DM Sans;font-size:19px;color:#5a4634">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:19px;color:#7a5a3a">{amt}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htiv("Cents, not a quant team","THE PRICE")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1;background:rgba(255,255,255,.5);border:1px solid rgba(120,95,60,.2);border-radius:16px;padding:14px 22px 8px">
          <div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.12em;color:#96562d;margin-bottom:4px">THE STACK IT REPLACES</div>
          {rows}
          <div style="display:flex;justify-content:space-between;align-items:baseline;padding-top:14px">
            <span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#2a2016">Monthly</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:{RED};text-decoration:line-through">$4,200</span></div>
        </div>
        <div style="width:280px;flex-shrink:0;background:linear-gradient(160deg,#fff,#f3ead9);border:2px solid #96562d;border-radius:16px;padding:22px 24px;display:flex;flex-direction:column;justify-content:center">
          <div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.12em;color:#96562d">ULTRON · THIS RUN</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:64px;color:#2a2016;line-height:1;margin:8px 0 2px">$2.40</div>
          <div style="font-family:DM Sans;font-size:16px;color:#5a4634">pay per token, cents per job</div>
        </div>
      </div>
      {cap("open source is free to clone and thousands a month to staff. this runs in cents.","#8a745a")}</div>'''

# 7. MEMORY - IVORY split timeline: the repo forgets each run, the operator remembers
def memory():
    runs=[130,340,550,752]
    repo=""; prev=None
    for i,x in enumerate(runs):
        if prev is not None:
            repo+=f'<line x1="{prev+18}" y1="150" x2="{x-18}" y2="150" stroke="{RED}" stroke-width="2.4" stroke-dasharray="4 9"/>'
            repo+=f'<text x="{(prev+x)/2:.0f}" y="128" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="{RED}">forgets</text>'
        repo+=f'<rect x="{x-16}" y="134" width="32" height="32" rx="7" fill="#efe3cf" stroke="rgba(120,95,60,.4)" stroke-width="1.8"/><text x="{x}" y="192" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#8a745a">cold start</text>'
        prev=x
    ult=f'<line x1="{runs[0]}" y1="330" x2="{runs[-1]}" y2="330" stroke="#96562d" stroke-width="4"/>'
    for i,x in enumerate(runs):
        ult+=f'<circle cx="{x}" cy="330" r="14" fill="#96562d"/><text x="{x}" y="372" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#7a5a3a">remembers</text>'
    feeders=""
    for lbl,x in [("ICP",210),("pricing",430),("docs",650)]:
        feeders+=f'<line x1="{x}" y1="284" x2="{x}" y2="316" stroke="rgba(150,90,45,.45)" stroke-width="1.8" stroke-dasharray="3 5"/><text x="{x}" y="278" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#96562d">{lbl}</text>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htiv("Nothing resets on you","THE MEMORY")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <text x="30" y="90" font-family="DM Sans" font-weight="800" font-size="18" fill="#2a2016">The repo</text>
        <text x="30" y="112" font-family="DM Mono" font-size="12.5" fill="{RED}">every clone from zero</text>
        {repo}
        <line x1="30" y1="240" x2="790" y2="240" stroke="rgba(120,95,60,.2)" stroke-width="1"/>
        {feeders}
        <text x="30" y="418" font-family="DM Sans" font-weight="800" font-size="18" fill="#2a2016">Ultron</text>
        {ult}
      </svg>
      {cap("the swarm boots blank each run. the operator keeps your ICP, pipeline and pricing.","#8a745a")}</div>'''

# 8. OPERATOR - scattered repos converge into one operated Ultron system
def operator():
    repos=[("AutoHedge",70,96),("Vibe-Trading",70,206),("research repo",70,316),("risk repo",196,150),("exec repo",196,262)]
    left=""
    for nm,x,y in repos:
        left+=(f'<path d="M{x+64} {y} C360 {y},380 214,520 214" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<rect x="{x-6}" y="{y-19}" width="140" height="38" rx="10" fill="#221f1b" stroke="rgba(255,255,255,.1)" opacity="0.85"/>'
          f'<text x="{x+64}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#9a9488">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Stop cloning tools","ONE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="600" cy="214" r="122" fill="url(#bod)"/></g>
        <text x="600" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="23" fill="#2a160c">ULTRON</text>
        <text x="600" y="234" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a160c">OPERATOR</text>
        <text x="600" y="372" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#8f8f85">composed · gated · yours</text>
      </svg>
      {cap("ten free repos you would stitch and staff, collapsed into one operated system.")}</div>'''

PANELS={"stars":stars(),"pipeline":pipeline(),"debate":debate(),"roster":roster(),
        "autonomy":autonomy(),"price":price(),"memory":memory(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src08"; os.makedirs(outd,exist_ok=True)
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
