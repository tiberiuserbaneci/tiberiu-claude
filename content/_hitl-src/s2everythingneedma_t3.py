#!/usr/bin/env python3
# TIER 3 - THE $10M OPERATOR STACK, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Reframe: you don't master 20 skills for a $10M business, you install one operator.
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

# 1. STACK - isometric layered platform: the operator stack you install instead of 20 skills
def stack():
    layers=[("YOU","the operator",4,True),
            ("GATE","your tap on every move",3,False),
            ("LOOPS","the same day, every day",2,False),
            ("AGENTS","seven roles, one login",1,False),
            ("MEMORY","one shared core",0,False)]
    cards=""
    for nm,sub,i,top in layers:
        y=(4-i)*100
        if top:
            bg=f"linear-gradient(160deg,#f0c49e,rgb({ACC}) 55%,#9a5a35)"; bd=f"rgb({ACC})"; ink="#1a0f0a"; sink="rgba(26,15,10,.7)"; glow="filter:drop-shadow(0 0 26px rgba(212,162,127,.4))"
        else:
            bg="linear-gradient(160deg,#403a35,#2b2723)"; bd="rgba(255,255,255,.14)"; ink="#FAFAF7"; sink="#a8a296"; glow=""
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;{glow};'
          f'background:{bg};border:1.5px solid {bd};border-radius:18px;padding:20px 26px;'
          f'box-shadow:0 30px 46px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.12);display:flex;align-items:center;gap:22px">'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Sans\';font-weight:900;font-size:26px;color:{ink};line-height:1">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:16px;color:{sink};margin-top:3px">{sub}</div></div>'
          f'<div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.12em;color:{ink};opacity:.75">L{i}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("You install a stack, not skills","5 LAYERS")}
      <div style="perspective:2100px;height:600px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(24deg) rotateZ(-9deg);width:600px;height:500px;position:relative">{cards}</div></div>
      {cap("agents, loops, memory and a gate - one operator holds all twenty skills for you.")}</div>'''

# 2. ROADMAP - IVORY: the whole path to $10M on one horizontal timeline of milestones
def roadmap():
    stops=[("$0","Signal","find the accounts",70),
           ("$100K","Outreach","book the meetings",236),
           ("$1M","Close","run the deals",402),
           ("$4M","Ship","build the product",568),
           ("$10M","Publish","own the market",734)]
    Y=176; nodes=""; path=f'<path d="M70 {Y} H734" stroke="rgba(150,90,45,.28)" stroke-width="5" stroke-linecap="round"/>'
    fill=f'<path d="M70 {Y} H{70+(734-70)*0.62:.0f}" stroke="#96562d" stroke-width="5" stroke-linecap="round"/>'
    for i,(amt,ph,sub,x) in enumerate(stops):
        big=i==4; done=i<=2; r=26 if big else 20
        fillc="#96562d" if (done or big) else "#fdfbf6"; stroke="#96562d" if (done or big) else "rgba(150,90,45,.4)"
        nodes+=(f'<circle cx="{x}" cy="{Y}" r="{r}" fill="{fillc}" stroke="{stroke}" stroke-width="{3 if not done else 0}"/>'
          + (f'<path d="M{x-9} {Y} l6 6 l12 -14" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>' if done and not big else '')
          + (f'<text x="{x}" y="{Y+8}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#fff">10M</text>' if big else '')
          + f'<text x="{x}" y="{Y-42}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="{27 if big else 23}" fill="{"#96562d" if big else "#2a2016"}">{amt}</text>'
          + f'<text x="{x}" y="{Y+58}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#5a4634">{ph.upper()}</text>'
          + f'<text x="{x}" y="{Y+80}" text-anchor="middle" font-family="DM Sans" font-size="13.5" fill="#8a745a">{sub}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("The whole path, one screen","0 TO $10M")}
      <svg width="800" height="300" viewBox="0 0 800 300" style="display:block;margin:8px auto 0">
        {path}{fill}{nodes}</svg>
      {cap("the same five moves, run every day - the operator walks the whole road for you.","#8a745a")}</div>'''

# 3. CURVE - revenue vs cost: headcount cost climbs, operator cost stays flat in cents
def curve():
    W,H=760,430; x0,y0,x1,y1=70,40,720,360
    def px(t): return x0+(x1-x0)*t
    def py(v): return y1-(y1-y0)*v
    grid=""
    for i in range(5):
        gy=y0+(y1-y0)*i/4
        grid+=f'<line x1="{x0}" y1="{gy:.0f}" x2="{x1}" y2="{gy:.0f}" stroke="rgba(250,250,247,.06)" stroke-width="1"/>'
    # headcount cost - steep rising curve
    hc="".join(f'{px(t):.0f},{py(t*t*0.94):.0f} ' for t in [i/12 for i in range(13)])
    # operator cost - near flat low line
    op="".join(f'{px(t):.0f},{py(0.03+0.02*t):.0f} ' for t in [i/12 for i in range(13)])
    area=f'M{x0},{y1} L' + op.replace(' ',' L') + f'{x1},{y1} Z'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Headcount curves up. You stay flat.","COST TO SCALE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="af" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.34)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
        <filter id="cg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
        {grid}
        <line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="rgba(250,250,247,.2)"/><line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="rgba(250,250,247,.2)"/>
        <polyline points="{hc}" fill="none" stroke="rgb(200,70,35)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="{area}" fill="url(#af)"/>
        <polyline points="{op}" fill="none" stroke="rgb({ACC})" stroke-width="4.5" stroke-linecap="round" filter="url(#cg)"/>
        <text x="{x1-6}" y="{py(0.9)-6:.0f}" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="18" fill="rgb(200,70,35)">a hire per skill</text>
        <text x="{x1-6}" y="{py(0.05)-14:.0f}" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="18" fill="rgb({ACC})">one operator, cents</text>
        <text x="{x0-8}" y="{y0+6}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#8f8f85">$/mo</text>
        <text x="{x1}" y="{y1+24}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#8f8f85">revenue &#8594; $10M</text>
      </svg>
      {cap("every new skill is a salary. the operator runs pay-per-token - cents, not payroll.")}</div>'''

# 4. ORG - org chart: YOU on top, the seven-agent roster reporting up, zero payroll
def org():
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    W,H=800,440; topx,topy=400,54; rowy=250; n=len(agents); gap=(W-80)/n
    conns=""; boxes=""
    for i,(nm,role) in enumerate(agents):
        x=40+gap*i+gap/2
        conns+=f'<path d="M{topx} {topy+58} C{topx} 170,{x:.0f} 150,{x:.0f} {rowy-6}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        boxes+=(f'<g><rect x="{x-48:.0f}" y="{rowy}" width="96" height="112" rx="15" fill="#241f1a" stroke="rgba(255,255,255,.12)" stroke-width="1.4"/>'
          f'<circle cx="{x:.0f}" cy="{rowy+34}" r="16" fill="rgba(212,162,127,.14)" stroke="rgba(212,162,127,.4)"/>'
          f'<circle cx="{x:.0f}" cy="{rowy+34}" r="5.5" fill="rgb({ACC})"/>'
          f'<text x="{x:.0f}" y="{rowy+74}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{rowy+96}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#8f8f85">{role}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Your whole org, zero payroll","1 FOUNDER · 7 AGENTS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="you" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="yg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {conns}
        <g filter="url(#yg)"><rect x="{topx-92}" y="{topy-6}" width="184" height="70" rx="18" fill="url(#you)"/></g>
        <text x="{topx}" y="{topy+26}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#1a0f0a">YOU</text>
        <text x="{topx}" y="{topy+48}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgba(26,15,10,.7)">the operator</text>
        {boxes}
      </svg>
      {cap("research, outbound, deals, content, code, publish, legal - all report to one login.")}</div>'''

# 5. GRAPH - node graph of handoffs: agents compose, the work moves itself down the chain
def graph():
    W,H=800,440
    nodes=[("CORTEX",120,110),("SPECTER",380,90),("STRIKER",650,150),
           ("PULSE",250,300),("AMPLIFY",540,330),("SENTINEL",130,360)]
    edges=[(0,1),(1,2),(0,3),(3,4),(2,4),(0,5),(3,1)]
    ed=""
    for a,b in edges:
        x1,y1=nodes[a][1],nodes[a][2]; x2,y2=nodes[b][1],nodes[b][2]
        mx=(x1+x2)/2
        ed+=f'<path d="M{x1} {y1} C{mx:.0f} {y1},{mx:.0f} {y2},{x2} {y2}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
    nd=""
    for nm,x,y in nodes:
        nd+=(f'<circle cx="{x}" cy="{y}" r="46" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.6"/>'
          f'<circle cx="{x}" cy="{y}" r="46" fill="rgba(212,162,127,.05)"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#e6d6c2">{nm}</text>')
    dots=""
    for a,b in edges[:4]:
        x1,y1=nodes[a][1],nodes[a][2]; x2,y2=nodes[b][1],nodes[b][2]
        dots+=f'<circle cx="{(x1+x2)/2:.0f}" cy="{(y1+y2)/2:.0f}" r="5" fill="rgb({ACC})" filter="url(#gd)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Each agent hands off to the next","IT COMPOSES")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="gd" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {ed}{dots}{nd}
      </svg>
      {cap("research feeds outreach, outreach feeds deals, deals feed content - one flow.")}</div>'''

# 6. GAUGE - IVORY: output gauge, one founder reading a full team's throughput
def gauge():
    cx,cy,R=250,270,190; a0,a1=180,360   # semicircle sweep
    frac=0.86; needle=a0+(a1-a0)*frac
    def pt(ang,rr): return (cx+rr*math.cos(math.radians(ang)), cy+rr*math.sin(math.radians(ang)))
    ticks=""
    for i in range(0,13):
        ang=a0+(a1-a0)*i/12; ox,oy=pt(ang,R); ix,iy=pt(ang,R-(24 if i%3==0 else 14))
        ticks+=f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="rgba(150,90,45,.45)" stroke-width="{3 if i%3==0 else 1.6}"/>'
    ax0,ay0=pt(a0,R); axe,aye=pt(needle,R)
    arc=f'M{ax0:.0f} {ay0:.0f} A{R} {R} 0 0 1 {axe:.0f} {aye:.0f}'
    nx,ny=pt(needle,R-40)
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px;display:flex;align-items:center;gap:30px">
      <svg width="440" height="320" viewBox="0 0 500 320">
        <path d="M{pt(a0,R)[0]:.0f} {pt(a0,R)[1]:.0f} A{R} {R} 0 0 1 {pt(a1,R)[0]:.0f} {pt(a1,R)[1]:.0f}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="24" stroke-linecap="round"/>
        <path d="{arc}" fill="none" stroke="#96562d" stroke-width="24" stroke-linecap="round"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="6" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="15" fill="#2a2016"/>
        <text x="{cx}" y="{cy-70}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="72" fill="#2a2016">12x</text>
        <text x="{cx}" y="{cy-36}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".14em" fill="#96562d">TEAM OUTPUT</text>
      </svg>
      <div style="flex:1">
        {htitle_iv("One founder, a team's output","THROUGHPUT")}
        <div style="font-family:'DM Sans';font-size:19px;color:#2a2016;line-height:1.45">The work of a headcount of twelve, running for the cost of your morning coffee.</div>
        {cap("output scales, cost does not - cents per run, no salaries attached.","#8a745a")}
      </div></div>'''

# 7. FIELD - dot field of thousands of moves overnight, a handful lit for your review today
def field():
    cols,rowsn=46,26
    lit={83,214,377,540,690,905,1051,1180}
    dots=""; cell=15; gap=3
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit: dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else: dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:40px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">1,196</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">moves overnight</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">8 need your eyes</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("accounts scored, emails drafted, PRs opened while you slept - you just review.")}</div>'''

# 8. HUB - radial hub-and-spokes: OPERATOR core, the four parts you install orbiting it
def hub():
    cx,cy=306,240; Rr=168
    spokes=[("AGENTS","seven roles",-90),("LOOPS","run daily",0),("MEMORY","one core",90),("GATE","your tap",180)]
    ring=""
    for nm,sub,a in spokes:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.6"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="52" fill="#241f1a" stroke="rgba(212,162,127,.38)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Four parts, one operator","THE INSTALL")}
      <svg width="612" height="480" viewBox="0 0 612 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {ring}
        <g filter="url(#cg2)"><circle cx="{cx}" cy="{cy}" r="76" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">OPERATOR</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgba(26,15,10,.7)">one login</text>
      </svg>
      {cap("agents, loops, memory and a gate wire into one system that reports to you.")}</div>'''

PANELS={"stack":stack(),"roadmap":roadmap(),"curve":curve(),"org":org(),
        "graph":graph(),"gauge":gauge(),"field":field(),"hub":hub()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2everythingneedma"; os.makedirs(outd,exist_ok=True)
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
