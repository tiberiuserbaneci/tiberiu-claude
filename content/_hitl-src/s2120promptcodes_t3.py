#!/usr/bin/env python3
# TIER 3 - THE COMMAND PALETTE (s2120promptcodes): Ultron reframe of "120 prompt codes for Claude".
# Each panel is a UNIQUE hand-built coded scene filling a clean rounded card, title + one-line caption,
# NO generic stat-chip strips, NO clip-path cuts, NO extruded walls. Built to the WIRE-ITS-EYES bar.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None):
    tc=tagc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CODECHAOS - dot field of 120 code cells, most dim, six lit (the cheat sheet you never memorize)
def codechaos():
    cols,rowsn=15,8   # 120
    lit={7,33,51,78,96,110}
    cell=30; gap=10
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="7" fill="rgb({ACC})" filter="url(#lg)"/>'
                   f'<line x1="{x+8}" y1="{y+cell-8}" x2="{x+cell-8}" y2="{y+8}" stroke="#1a0f0a" stroke-width="2.4" stroke-linecap="round"/>')
        else:
            dots+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="7" fill="rgba(250,250,247,.055)" stroke="rgba(250,250,247,.06)"/>'
                   f'<line x1="{x+8}" y1="{y+cell-8}" x2="{x+cell-8}" y2="{y+8}" stroke="rgba(250,250,247,.12)" stroke-width="1.6" stroke-linecap="round"/>')
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A syllabus of codes","120 TO MEMORIZE")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:10px auto 4px">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("120 prompt codes on a cheat sheet you reopen every time. six stick, the rest evaporate.")}</div>'''

# 2. PALETTE - IVORY command-palette / slash menu (the shift: install commands, do not memorize codes)
def palette():
    rows=[("/outreach","write and send a full sequence",True),
          ("/brief","research any company into one page",False),
          ("/carousel","turn a note into a ready post",False),
          ("/qualify","score and route a live deal",False),
          ("/research","profile a person or a market",False)]
    items=""
    for cmd,desc,on in rows:
        bg="background:linear-gradient(160deg,rgba(150,86,45,.16),rgba(150,86,45,.07));" if on else ""
        bd="border:1px solid rgba(150,86,45,.34);" if on else "border:1px solid rgba(120,95,60,.10);"
        ret=(f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;color:#96562d;background:rgba(150,86,45,.12);'
             f'border:1px solid rgba(150,86,45,.3);border-radius:8px;padding:5px 11px">return</span>') if on else \
            '<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;color:#b6a586">enter</span>'
        items+=(f'<div style="display:flex;align-items:center;gap:18px;{bg}{bd}border-radius:14px;padding:16px 20px">'
          f'<svg width="30" height="30" viewBox="0 0 24 24" style="flex-shrink:0"><rect x="2" y="2" width="20" height="20" rx="6" fill="rgba(150,86,45,.12)" stroke="rgba(150,86,45,.36)"/><path d="M14 6 L9 18" stroke="#96562d" stroke-width="2.6" stroke-linecap="round"/></svg>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-weight:500;font-size:20px;color:#96562d;letter-spacing:.01em">{cmd}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#7a6a52;margin-top:2px">{desc}</div></div>{ret}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("Type one slash","INSTALLED COMMANDS","#2a2016","#96562d")}
      <div style="background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.16);border-radius:20px;padding:16px;box-shadow:inset 0 2px 6px rgba(120,95,60,.08)">
        <div style="display:flex;align-items:center;gap:14px;padding:14px 18px;background:rgba(255,255,255,.7);border:1px solid rgba(120,95,60,.18);border-radius:13px;margin-bottom:14px">
          <span style="font-family:DM Mono;font-weight:500;font-size:24px;color:#96562d">/</span>
          <span style="font-family:DM Sans;font-size:19px;color:#9a8a70">type a command</span>
          <span style="margin-left:auto;width:2px;height:26px;background:#96562d;opacity:.7"></span></div>
        <div style="display:flex;flex-direction:column;gap:10px">{items}</div></div>
      {cap("one command replaces a hundred memorized codes. install it once, call it by name.","#8a745a")}</div>'''

# 3. ROSTER - radial hub: one slash routes to seven named agents
def roster():
    cx,cy,R=380,258,196
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),
            ("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    n=len(agents); lines=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="48" fill="#221f1b" stroke="rgba(212,162,127,.34)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y-3:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15.5" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+17:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#a89a86">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, each named","CALL BY NAME")}
      <svg width="760" height="516" viewBox="0 0 760 516" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#2a160c">/</text>
        {nodes}
      </svg>
      {cap("one slash routes to the agent that owns the job. you never memorize a code again.")}</div>'''

# 4. ONEFLOW - node graph: one command fires a whole system (research to write to qualify)
def oneflow():
    W,H=880,420
    cmd=(70,210)
    chain=[("CORTEX",270,120),("SPECTER",440,300),("STRIKER",610,150)]
    out=(760,240)
    pts=[cmd]+[(x,y) for _,x,y in chain]+[out]
    edges=""
    for i in range(len(pts)-1):
        x0,y0=pts[i]; x1,y1=pts[i+1]; mx=(x0+x1)/2
        edges+=f'<path d="M{x0+40} {y0} C{mx} {y0},{mx} {y1},{x1-40} {y1}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
    discs=""
    for nm,x,y in chain:
        discs+=(f'<circle cx="{x}" cy="{y}" r="52" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.8"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#e6d6c2">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One command, a whole system","SLASH ONCE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="og" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gg" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}
        <rect x="{cmd[0]-46}" y="{cmd[1]-30}" width="132" height="60" rx="15" fill="#2a2724" stroke="rgba(255,255,255,.12)"/>
        <text x="{cmd[0]+20}" y="{cmd[1]+7}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="19" fill="rgb({ACC})">/outreach</text>
        {discs}
        <g filter="url(#gg)"><circle cx="{out[0]}" cy="{out[1]}" r="60" fill="url(#og)"/></g>
        <text x="{out[0]}" y="{out[1]-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">BOOKED</text>
        <text x="{out[0]}" y="{out[1]+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">1 pass</text>
      </svg>
      {cap("slash outreach and three agents research, write and qualify in a single pass.")}</div>'''

# 5. INSTALL - isometric stack of installed command cards (learn once, wired for good)
def install():
    steps=[("/outreach","sequences on demand"),("/brief","one-page research"),("/carousel","posts from a note")]
    cards=""
    for i,(cmd,sub) in enumerate(steps):
        y=i*132
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-weight:500;font-size:20px;color:rgb({ACC})">{cmd}</div><div style="font-family:DM Sans;font-size:15px;color:#a8a296">{sub}</div></div>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#cfc9bd;border:1px solid rgba(255,255,255,.16);border-radius:8px;padding:6px 12px">INSTALLED</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Learn it once","IT NEVER FORGETS")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:432px;position:relative">{cards}</div></div>
      {cap("each command installs into your workspace and stays wired, no cheat sheet to reopen.")}</div>'''

# 6. GATE - full-system orb held on the operator's reins, one lock (HUMAN GATE)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It runs. You tap send.","HUMAN GATE")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og2)"><circle cx="200" cy="210" r="130" fill="url(#orb)"/></g>
        <text x="200" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">FULL</text>
        <text x="200" y="236" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">SYSTEM</text>
        <path d="M334 210 H610" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="140" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,178)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("the command fires the system, but every external move parks at the gate for you.")}</div>'''

# 7. CENTS - speedometer gauge, needle parked at the cheap end (pay per token, cents a run)
def cents():
    cx,cy,R=300,290,208
    def pt(deg,rad):
        return (cx+rad*math.cos(math.radians(deg)), cy-rad*math.sin(math.radians(deg)))
    # ticks across the top semicircle 180 (left/cheap) -> 0 (right/expensive)
    ticks=""
    for k in range(0,11):
        a=180-k*18
        x0,y0=pt(a,R); x1,y1=pt(a,R-(26 if k%5==0 else 15))
        col=f"rgb({ACC})" if k<=3 else ("rgb(200,70,35)" if k>=9 else "rgba(250,250,247,.28)")
        ticks+=f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke="{col}" stroke-width="{3 if k%5==0 else 2}"/>'
    arcL0=pt(180,R); arcL1=pt(126,R)
    arcH0=pt(54,R); arcH1=pt(0,R)
    na=158  # needle parked near the cheap end
    nx,ny=pt(na,R-52)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A hundred codes, a few cents","PAY PER TOKEN")}
      <svg width="620" height="352" viewBox="0 0 620 352" style="display:block;margin:2px auto 0">
        <defs><filter id="ng" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.85"/></filter></defs>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(250,250,247,.08)" stroke-width="20" stroke-linecap="round"/>
        <path d="M{arcL0[0]:.0f} {arcL0[1]:.0f} A{R} {R} 0 0 1 {arcL1[0]:.0f} {arcL1[1]:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="20" stroke-linecap="round"/>
        <path d="M{arcH0[0]:.0f} {arcH0[1]:.0f} A{R} {R} 0 0 1 {arcH1[0]:.0f} {arcH1[1]:.0f}" fill="none" stroke="rgb(200,70,35)" stroke-width="20" stroke-linecap="round" opacity="0.75"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#2a2724" stroke="rgb({ACC})" stroke-width="3"/>
        <text x="{cx-R+8}" y="{cy+34}" text-anchor="start" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="rgb({ACC})">CENTS</text>
        <text x="{cx+R-8}" y="{cy+34}" text-anchor="end" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="rgb(200,70,35)">SEAT LICENSE</text>
        <text x="{cx}" y="{cy-72}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="56" fill="#FAFAF7">0.1c</text>
        <text x="{cx}" y="{cy-40}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".14em" fill="#a89a86">A COMMAND RUN</text>
      </svg>
      {cap("no per-seat license. a full command run costs cents because you pay only per token.")}</div>'''

# 8. SHIP - IVORY timeline: install once, then it fires every day after
def ship():
    W,H=760,320
    y0=176
    stops=[(70,"DAY 0","install /carousel",True),
           (215,"MON","runs",False),(355,"TUE","runs",False),
           (495,"WED","runs",False),(635,"THU","runs",False)]
    track=(f'<line x1="60" y1="{y0}" x2="700" y2="{y0}" stroke="#c9b89a" stroke-width="4" stroke-linecap="round"/>'
           f'<path d="M700 {y0} l-16 -9 v18 z" fill="#96562d"/>'
           f'<text x="716" y="{y0+6}" font-family="DM Mono" font-size="14" fill="#96562d">on</text>')
    marks=""
    for x,lab,sub,big in stops:
        r=22 if big else 13
        fill="#96562d" if big else "rgb(212,162,127)"
        marks+=(f'<circle cx="{x}" cy="{y0}" r="{r}" fill="{fill}" stroke="rgba(150,90,45,.3)" stroke-width="2"/>')
        if big:
            marks+='<path d="M%d %d l6 6 l12 -13" fill="none" stroke="#fdfbf6" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'%(x-9,y0)
        else:
            marks+=f'<line x1="{x}" y1="{y0-r-6}" x2="{x}" y2="{y0-r-30}" stroke="rgba(150,90,45,.4)" stroke-width="2"/>'
        marks+=(f'<text x="{x}" y="{y0+r+30}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="15" fill="#96562d" letter-spacing=".06em">{lab}</text>'
                f'<text x="{x}" y="{y0+r+52}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#7a6a52">{sub}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("Install today","RUNS FOREVER","#2a2016","#96562d")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:6px auto 0">
        {track}{marks}
      </svg>
      {cap("set the command up once and it fires on demand, every day after, no re-learning.","#8a745a")}</div>'''

PANELS={"codechaos":codechaos(),"palette":palette(),"roster":roster(),"oneflow":oneflow(),
        "install":install(),"gate":gate(),"cents":cents(),"ship":ship()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2120promptcodes"; os.makedirs(outd,exist_ok=True)
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
