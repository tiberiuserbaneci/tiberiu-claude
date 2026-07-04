#!/usr/bin/env python3
# TIER 3 - "FREE IS NOT A MOAT" (Google Gemini Pro free 18mo reframe). Each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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

# 1. TRAP - IVORY: an expiring FREE coupon (countdown draining to red) vs the persistent system
def trap():
    ticket=('<div style="position:relative;width:300px;flex-shrink:0">'
      '<div style="background:linear-gradient(160deg,#fffdf8,#f4ead8);border:1px solid rgba(150,120,80,.28);border-radius:22px;padding:24px 26px;box-shadow:0 26px 44px rgba(120,90,55,.22), inset 0 2px 3px rgba(255,255,255,.9)">'
      '<div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.2em;color:#96562d">GOOGLE GEMINI PRO</div>'
      '<div style="font-family:\'DM Sans\';font-weight:900;font-size:78px;color:#2a2016;line-height:.9;margin-top:8px">FREE</div>'
      '<div style="font-family:\'DM Sans\';font-weight:800;font-size:22px;color:#8a745a;margin-top:2px">for 18 months</div>'
      '<div style="border-top:2px dashed rgba(150,120,80,.42);margin:20px -26px 18px"></div>'
      '<div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:#8a745a;margin-bottom:9px">TIME LEFT ON THE DEAL</div>'
      '<div style="height:14px;border-radius:8px;background:rgba(150,120,80,.16);overflow:hidden;box-shadow:inset 0 1px 2px rgba(120,90,55,.2)">'
      '<div style="width:34%;height:100%;background:linear-gradient(90deg,rgb('+ACC+'),rgb(200,70,35))"></div></div>'
      '<div style="display:flex;justify-content:space-between;margin-top:11px">'
      '<span style="font-family:\'DM Mono\';font-size:12px;color:#8a745a">then full price</span>'
      '<span style="font-family:\'DM Mono\';font-size:12px;font-weight:500;color:rgb(200,70,35)">EXPIRES</span></div>'
      '</div></div>')
    right=('<div style="flex:1">'
      '<div style="font-family:\'DM Sans\';font-weight:900;font-size:33px;color:#2a2016;line-height:1.08">Free for everyone is an edge for no one.</div>'
      '<div style="font-family:\'DM Sans\';font-size:19px;color:#5a4634;line-height:1.46;margin-top:16px">A free model is a rented mouth on a countdown. What compounds is the system wrapped around it.</div>'
      '<div style="display:inline-flex;align-items:center;gap:10px;margin-top:22px;background:rgba(150,90,45,.10);border:1px solid rgba(150,90,45,.30);border-radius:999px;padding:11px 18px">'
      '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>'
      '<span style="font-family:\'DM Sans\';font-weight:700;font-size:16px;color:#96562d">your system: still here in month 19</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:38px 42px 34px">
      {htitle("A free tool is not a moat","THE TRAP","#2a2016")}
      <div style="display:flex;align-items:center;gap:34px">{ticket}{right}</div>
      {cap("the model is free for everyone. free is a floor, not an edge.","#8a745a")}</div>'''

# 2. ROUTER - one job routed across every model, cheapest that works is picked (cents)
def router():
    models=[("GEMINI","free, for now","free",78,False),
            ("CLAUDE","hard judgement","0.11c",188,True),
            ("GPT-4o","broad tasks","0.14c",298,False),
            ("LLAMA","bulk, cheapest","0.02c",408,False)]
    hubx,hy=160,240; lx=470
    edges=""; cards=""
    for nm,role,cost,y,on in models:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C320 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:300px;top:{y-40}px;width:172px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:13px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:25px;color:#FAFAF7;margin-top:3px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every model, one router","RENTED AT CENTS")}
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
        <div style="position:absolute;left:12px;top:214px;width:92px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">score 200<br>accounts</div>
        {cards}
      </div>
      {cap("you never marry one model. the router rents whichever is cheapest for the job.")}</div>'''

# 3. COMPOUND - line chart: free model plateaus flat, the system compounds past the free window
def compound():
    W,H=770,430
    base=352; x0=64; x1=712
    ticks=""
    for i,m in enumerate([0,6,12,18]):
        x=x0+(x1-x0)*i/3
        ticks+=(f'<line x1="{x:.0f}" y1="{base}" x2="{x:.0f}" y2="{base+8}" stroke="rgba(250,250,247,.25)"/>'
                f'<text x="{x:.0f}" y="{base+28}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">mo {m}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Free plateaus. Systems compound.","MOAT CURVE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="sysf" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.34)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
          <filter id="cg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter>
        </defs>
        <line x1="{x0}" y1="60" x2="{x0}" y2="{base}" stroke="rgba(250,250,247,.14)"/>
        <line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="rgba(250,250,247,.22)"/>
        {ticks}
        <!-- free deal window ends marker -->
        <line x1="{x1}" y1="60" x2="{x1}" y2="{base}" stroke="rgba(200,70,35,.6)" stroke-width="2" stroke-dasharray="5 7"/>
        <text x="{x1-6}" y="80" text-anchor="end" font-family="DM Mono" font-size="12.5" fill="rgb(200,70,35)">free window ends</text>
        <!-- system compounding area + curve -->
        <path d="M{x0} 330 C240 322,360 286,486 214 S650 96,{x1} 74 L{x1} {base} L{x0} {base} Z" fill="url(#sysf)"/>
        <path d="M{x0} 330 C240 322,360 286,486 214 S650 96,{x1} 74" fill="none" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round" filter="url(#cg)"/>
        <circle cx="{x1}" cy="74" r="8" fill="rgb({ACC})" filter="url(#cg)"/>
        <text x="{x1-14}" y="60" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="17" fill="rgb({ACC})">your system</text>
        <!-- flat free-model line -->
        <path d="M{x0} 322 C220 314,360 310,500 309 S650 310,{x1} 310" fill="none" stroke="rgba(250,250,247,.34)" stroke-width="3.5" stroke-dasharray="9 8" stroke-linecap="round"/>
        <text x="{x0+150}" y="298" font-family="DM Sans" font-weight="700" font-size="16" fill="#9a9488">free model, flat</text>
      </svg>
      {cap("memory, agents and data compound every day the free window ticks down.")}</div>'''

# 4. RADAR - the system watches signals; a free chat model just waits to be asked
def radar():
    cx,cy,R=230,230,200
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.18)"/>' for r in (66,133,200))
    cross=f'<line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.14)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.14)"/>'
    blips=[("Funding round",300,150),("Hiring spike",120,92),("Stack change",205,176),("Buy intent",44,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
    return f'''<div style="width:900px;{CARD};padding:40px;display:flex;align-items:center;gap:34px">
      <svg width="460" height="460" viewBox="0 0 460 460">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}{cross}
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(60)):.0f} {cy-R*math.cos(math.radians(60)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("A free model waits. Yours watches.","SIGNAL RADAR")}
        <div style="margin-top:2px">{"".join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:14px"><span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.7)"></span><span style="font-family:DM Sans;font-size:18px;color:#d9d5cc">{nm}</span></div>' for nm,_,_ in blips)}</div>
        {cap("funding, hiring, stack, intent: the market, watched for you overnight.")}
      </div></div>'''

# 5. STACK - isometric layers: the model is the swappable bottom commodity, the system stacks above
def stack():
    layers=[("HUMAN GATE","your tap on every send",False),
            ("7 AGENTS","research to close",False),
            ("MEMORY","ICP, pipeline, docs",False),
            ("ANY MODEL","commodity, swappable",True)]
    cards=""
    for i,(nm,sub,commodity) in enumerate(layers):
        y=i*118
        if commodity:
            bg="linear-gradient(160deg,#2a2723,#1c1a17)"; bd="1.5px dashed rgba(212,162,127,.4)"; nc="#9a9488"; sc="#7a7468"
            tag='<span style="font-family:DM Mono;font-size:12px;color:rgb(200,70,35)">swap freely</span>'
        else:
            bg="linear-gradient(160deg,#403a35,#2b2723)"; bd="1.5px solid rgba(255,255,255,.14)"; nc=f"rgb({ACC})"; sc="#FAFAF7"
            tag=f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="22" height="22" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:{bg};border:{bd};border-radius:18px;padding:18px 24px;box-shadow:0 30px 44px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08);display:flex;align-items:center;gap:20px">'
          f'{tag if not commodity else ""}'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:{nc}">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:{sc}">{sub}</div></div>'
          f'{tag if commodity else ""}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The model is the bottom layer","THE STACK")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-8deg);width:580px;height:436px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:-52px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">= your company</div></div></div>
      {cap("swap the model like a battery. the stack above it is the company.")}</div>'''

# 6. GAUGE - IVORY: cost dial parked in cents; a costly seat plan is the crossed-out competitor
def gauge():
    cx,cy,R=230,250,180
    def pt(deg,rr):
        a=math.radians(180-deg); return (cx+rr*math.cos(a), cy-rr*math.sin(a))
    track=""
    for d in range(0,181,5):
        x1,y1=pt(d,R); x2,y2=pt(d,R-22)
        col="rgba(200,70,35,.8)" if d>132 else ("rgba(150,90,45,.9)" if d>96 else "rgba(150,120,80,.35)")
        track+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="4"/>'
    nx,ny=pt(20,R-40)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;align-items:center;gap:30px">
      <svg width="470" height="300" viewBox="0 0 470 300">
        {track}
        <text x="{cx-R+8:.0f}" y="{cy+26}" font-family="DM Mono" font-size="12" fill="#8a745a">cents</text>
        <text x="{cx+R-40:.0f}" y="{cy+26}" font-family="DM Mono" font-size="12" fill="rgb(200,70,35)">$$$</text>
        <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#2a2016" stroke-width="7" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="15" fill="#2a2016"/>
        <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#2a2016">0.11c</text>
        <text x="{cx}" y="{cy-30}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#96562d">PER ACTION</text>
      </svg>
      <div style="flex:1">
        {htitle("Priced in cents","COST GAUGE","#2a2016")}
        <div style="font-family:'DM Sans';font-size:19px;color:#5a4634;line-height:1.45">Pay per token. A thousand rows scored costs cents, not a subscription you forget to cancel.</div>
        <div style="display:inline-flex;align-items:center;gap:10px;margin-top:18px;background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.28);border-radius:12px;padding:11px 16px">
          <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:rgb(200,70,35)">TYPICAL AI SEAT</span>
          <span style="font-family:'DM Sans';font-weight:800;font-size:18px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">$99 / month</span></div>
        {cap("pay per token. cents per thousand rows, never a seat you forgot to cancel.","#8a745a")}
      </div></div>'''

# 7. FIELD - dot field: free-model waves come and go (dim/red), your system is the constant column
def field():
    cols,rowsn=40,22
    persist=20
    expired={53,88,131,167,214,266,309,355,401,448,492,537,601,668,712,760,803}
    dots=""; cell=15; gap=4
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if c==persist:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        elif i in expired:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(200,70,35,.55)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("Models come and go","YOU COMPOUND")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="display:flex;gap:26px;margin-top:16px">
        <div style="display:flex;align-items:center;gap:9px"><span style="width:12px;height:12px;border-radius:3px;background:rgb({ACC});box-shadow:0 0 10px rgba({ACC},.8)"></span><span style="font-family:DM Sans;font-size:15px;color:#c9c3b8">your operating system</span></div>
        <div style="display:flex;align-items:center;gap:9px"><span style="width:12px;height:12px;border-radius:3px;background:rgba(200,70,35,.55)"></span><span style="font-family:DM Sans;font-size:15px;color:#9a9488">a free-model deal that expired</span></div></div>
      {cap("a dozen free-model waves in two years. the operating system outlives them all.")}</div>'''

# 8. HUB - radial hub-and-spokes: the moat is the whole roster, memory, router and gate around one core
def hub():
    cx,cy,R=380,250,196
    nodes=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL","MEMORY","ROUTER","GATE"]
    spokes=""; ncircles=""
    n=len(nodes)
    for i,nm in enumerate(nodes):
        a=math.radians(-90+i*(360/n))
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        ncircles+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="32" fill="#221f1b" stroke="rgba(255,255,255,.14)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".04em" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The moat is the whole system","ONE CORE")}
      <svg width="760" height="500" viewBox="0 0 760 500" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}{ncircles}
        <g filter="url(#cg2)"><circle cx="{cx}" cy="{cy}" r="70" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">ULTRON</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">your system</text>
      </svg>
      {cap("seven agents, memory, the router and the gate. a free model has none of it.")}</div>'''

PANELS={"trap":trap(),"router":router(),"compound":compound(),"radar":radar(),
        "stack":stack(),"gauge":gauge(),"field":field(),"hub":hub()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2googlegeminipro"; os.makedirs(outd,exist_ok=True)
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
