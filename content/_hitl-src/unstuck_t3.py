#!/usr/bin/env python3
# TIER 3 - STUCK AT LEVEL ONE, built to the WIRE-ITS-EYES bar: each of the 8 panels is a UNIQUE
# hand-built coded scene filling a clean rounded card (cycle loop / radial hub / node graph / iso
# stack / clock dial / ladder / gauge / dot field). title + mono tag + one mono caption. No generic
# header+rows+chip-strip template, no repeated scene type. Cost zero.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
BAD="200,70,35"
# clean rounded cards - copied verbatim from aibody_t3.py (dark + ivory). No cuts, no side-walls.
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'

def htitle(t,tag,ink="#FAFAF7",tagcol=None):
    tc=tagcol or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
      f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
      f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

def _arrow(px,py,dirdeg,size=13,fill=None):
    f=fill or f"rgb({ACC})"
    d=math.radians(dirdeg); n=d+math.pi/2
    tx=px+size*math.cos(d); ty=py+size*math.sin(d)
    ax=px-4*math.cos(d)+9*math.cos(n); ay=py-4*math.sin(d)+9*math.sin(n)
    bx=px-4*math.cos(d)-9*math.cos(n); by=py-4*math.sin(d)-9*math.sin(n)
    return f'<polygon points="{tx:.0f},{ty:.0f} {ax:.0f},{ay:.0f} {bx:.0f},{by:.0f}" fill="{f}"/>'

# 1. FLOOR - CYCLE LOOP: ask/copy/close on a closed ring with clockwise arrows (the treadmill)
def floor():
    cx,cy,R=306,236,152
    nodes=[("ASK",-90),("COPY",30),("CLOSE",150)]
    mids=[-30,90,210]
    ring=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(212,162,127,.22)" stroke-width="2" stroke-dasharray="2 10"/>'
    arrows=""
    for a in mids:
        px=cx+R*math.cos(math.radians(a)); py=cy+R*math.sin(math.radians(a))
        arrows+=_arrow(px,py,a+90,15,f"rgba(212,162,127,.7)")
    ns=""
    for nm,a in nodes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        ns+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="47" fill="#221f1b" stroke="rgba(212,162,127,.35)" stroke-width="2"/>'
             f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="#d3cdc1">{nm}</text>')
    bar=(f'<rect x="{cx-84}" y="{cy-24}" width="168" height="48" rx="12" fill="#17150f" stroke="rgba(255,255,255,.10)"/>'
         f'<circle cx="{cx-58}" cy="{cy}" r="9" fill="none" stroke="#7a7468" stroke-width="2.4"/><line x1="{cx-51}" y1="{cy+7}" x2="{cx-44}" y2="{cy+14}" stroke="#7a7468" stroke-width="2.4"/>'
         f'<text x="{cx-32}" y="{cy+5}" font-family="DM Mono" font-size="13" fill="#6f6a60">write a prompt...</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A smarter search bar","LEVEL 1")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        {ring}{arrows}
        {bar}
        {ns}
        <text x="{cx}" y="{cy+204}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".14em" fill="rgb({BAD})">SAME LOOP, EVERY DAY</text>
      </svg>
      {cap("ask, copy, close the tab. a smarter search bar, nothing more.")}</div>'''

# 2. MEMORY - IVORY RADIAL HUB: one memory core, 3 saved-fact nodes docked on lifelines
def memory():
    cx,cy=306,244
    facts=[("ICP","2-50 employees",-90),("VOICE","your cadence",30),("PRICING","cents, not seats",150)]
    lines=""; ns=""
    for nm,sub,a in facts:
        x=cx+172*math.cos(math.radians(a)); y=cy+172*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.32)" stroke-width="3"/>'
        ns+=(f'<rect x="{x-84:.0f}" y="{y-34:.0f}" width="168" height="68" rx="16" fill="#fffaf1" stroke="rgba(150,90,45,.30)" stroke-width="1.5"/>'
             f'<text x="{x:.0f}" y="{y-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#2a2016">{nm}</text>'
             f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8a745a">{sub}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("It remembers what you hate","LEVEL 2 · PERSISTS","#2a2016","#96562d")}
      <svg width="612" height="490" viewBox="0 0 612 490" style="display:block;margin:0 auto">
        <defs><radialGradient id="mcore" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="#c07a4c"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgba(200,120,70,.5)"/></filter></defs>
        {lines}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#mcore)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#fff5ec">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#fce4d2">kept for you</text>
        {ns}</svg>
      {cap("your ICP, voice and pricing persist. no reintroductions every morning.","#8a745a")}</div>'''

# 3. JOBS - NODE/BEZIER GRAPH: you-node fans to 3 agents working in parallel while you watch
def jobs():
    agents=[("SOURCE","847 accounts ranked",125,.92),("BRIEF","12 one-pagers built",230,.66),("DRAFT","9 emails, your voice",335,1.0)]
    hubx,huby=150,230
    edges=""
    for nm,out,y,f in agents:
        edges+=f'<path d="M{hubx+72} {huby} C320 {huby},330 {y},468 {y}" fill="none" stroke="rgb({ACC})" stroke-width="3" opacity="0.5"/>'
    cards=""
    for nm,out,y,f in agents:
        done=f>=1.0
        cards+=(f'<div style="position:absolute;left:472px;top:{y-52}px;width:320px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.3);border-radius:16px;padding:15px 18px;box-shadow:0 22px 36px rgba(0,0,0,.5)">'
          f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:11px;color:{"#7fd39a" if done else "#c9a583"}">{"done" if done else "working"}</span></div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7;margin-bottom:10px">{out}</div>'
          f'<div style="height:8px;border-radius:5px;background:rgba(255,255,255,.08)"><div style="height:8px;border-radius:5px;width:{int(f*100)}%;background:rgb({ACC})"></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It works while you watch","LEVEL 3 · PARALLEL")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><filter id="jg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter></defs>
          {edges}
          <g filter="url(#jg)"><rect x="{hubx-72}" y="{huby-52}" width="144" height="104" rx="22" fill="#2a2724" stroke="rgb({ACC})" stroke-width="2"/></g>
          <text x="{hubx}" y="{huby-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#FAFAF7">YOU</text>
          <text x="{hubx}" y="{huby+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">watching</text>
          <text x="{hubx}" y="{huby+38}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">the one thing</text>
        </svg>
        {cards}
      </div>
      {cap("agents source, brief and draft while you do the one thing only you can.")}</div>'''

# 4. SHIP - ISO CARD STACK: build -> test -> ship pipeline ending in a merged PR
def ship():
    steps=[("BUILD","wrote the pricing page",0),("TEST","38 passed, 0 failed",1),("SHIP","live on main",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("It ships while you sell","LEVEL 4 · SHIPPED")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:120px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Merged &#10003; PR #204</div></div></div>
      {cap("pages and fixes from plain english, tested before you ever see them.")}</div>'''

# 5. ROUTINES - CLOCK DIAL: 07:00 trigger clock + the digest waiting on the right
def routines():
    cx,cy,R=210,210,168
    ticks=""
    for h in range(12):
        a=math.radians(h*30-90); r1=R-4 if h%3 else R-2; r0=R-22 if h%3 else R-30
        w=2 if h%3 else 4
        ticks+=f'<line x1="{cx+r0*math.cos(a):.0f}" y1="{cy+r0*math.sin(a):.0f}" x2="{cx+r1*math.cos(a):.0f}" y2="{cy+r1*math.sin(a):.0f}" stroke="rgba(212,162,127,.5)" stroke-width="{w}"/>'
    ha=math.radians(7*30-90); ma=math.radians(-90)  # 07:00
    blips=""
    for a in (-52,138,246):
        x=cx+(R-16)*math.cos(math.radians(a)); y=cy+(R-16)*math.sin(math.radians(a))
        blips+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="rgb({ACC})" filter="url(#rb)"/>'
    rows=[("5 leads sourced","overnight"),("3 replies handled","06:20"),("1 page shipped","04:11")]
    digest=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px"><span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">07:00 DIGEST</span><span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">ready</span></div>'
      +"".join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:8px 0;border-top:1px solid rgba(255,255,255,.07)"><span style="font-family:DM Sans;font-size:18px;color:#d9d5cc">{a}</span><span style="font-family:DM Mono;font-size:13px;color:#8f8f85">{b}</span></div>' for a,b in rows)
      +'</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><filter id="rb" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816" stroke="rgba(212,162,127,.2)" stroke-width="2"/>
        <circle cx="{cx}" cy="{cy}" r="{R-40}" fill="none" stroke="rgba(255,255,255,.05)"/>
        {ticks}{blips}
        <line x1="{cx}" y1="{cy}" x2="{cx+94*math.cos(ma):.0f}" y2="{cy+94*math.sin(ma):.0f}" stroke="#FAFAF7" stroke-width="5" stroke-linecap="round"/>
        <line x1="{cx}" y1="{cy}" x2="{cx+64*math.cos(ha):.0f}" y2="{cy+64*math.sin(ha):.0f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="9" fill="rgb({ACC})"/>
        <text x="{cx}" y="{cy+118}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#8f8f85">TRIGGERS, NOT TYPING</text></svg>
      <div style="flex:1">
        {htitle("It runs while you sleep","LEVEL 5 · AUTO")}
        {digest}
        {cap("triggers replace typing. the digest waits for you at 07:00.")}
      </div></div>'''

# 6. GAP - LADDER/LEVELS: 5 rungs, most founders stuck at L2, level 3 glowing just above
def gap():
    W,H=760,470
    x1,x2=150,250
    levels=[("L5","runs itself",92,"future"),("L4","ships for you",170,"future"),
            ("L3","works for you",248,"here"),("L2","remembers you",326,"norm"),("L1","smarter search",404,"norm")]
    rails=(f'<line x1="{x1}" y1="70" x2="{x1}" y2="426" stroke="rgba(212,162,127,.4)" stroke-width="6" stroke-linecap="round"/>'
           f'<line x1="{x2}" y1="70" x2="{x2}" y2="426" stroke="rgba(212,162,127,.4)" stroke-width="6" stroke-linecap="round"/>')
    body=""
    for lvl,desc,y,state in levels:
        if state=="future":
            col="rgba(212,162,127,.22)"; ink="#6f6a60"; sub="#5a554c"
        elif state=="here":
            col=f"rgb({ACC})"; ink="#FAFAF7"; sub=f"rgb({ACC})"
        else:
            col="rgba(212,162,127,.6)"; ink="#d9d5cc"; sub="#8f8f85"
        glow=' filter="url(#lg)"' if state=="here" else ""
        body+=f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-width="11" stroke-linecap="round"{glow}/>'
        body+=f'<text x="285" y="{y-4}" font-family="DM Sans" font-weight="900" font-size="24" fill="{ink}">{lvl}</text>'
        body+=f'<text x="330" y="{y-4}" font-family="DM Sans" font-weight="600" font-size="21" fill="{sub}">{desc}</text>'
    body+=f'<circle cx="200" cy="326" r="13" fill="#FAFAF7" stroke="rgb({ACC})" stroke-width="3"/>'
    body+=('<rect x="16" y="306" width="118" height="40" rx="10" fill="rgba(200,70,35,.14)" stroke="rgba(200,70,35,.5)"/>'
           f'<text x="75" y="331" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".06em" fill="rgb({BAD})">MOST STOP</text>')
    body+=(f'{_arrow(600,248,180,15)}'
           f'<rect x="606" y="228" width="140" height="40" rx="10" fill="rgba(212,162,127,.14)" stroke="rgb({ACC})"/>'
           f'<text x="676" y="253" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".06em" fill="rgb({ACC})">LEVEL 3 EXISTS</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nobody told you level 3 exists","THE GAP")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-120%" y="-400%" width="340%" height="900%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        {rails}{body}</svg>
      {cap("most founders never hear the next level exists. now you have.")}</div>'''

# 7. GATE - GAUGE: autonomy needle swept high, control held by a lock at the hub (your tap)
def gate():
    cx,cy,R=350,330,240
    f=0.84
    def pt(frac,rad):
        th=math.radians(180-frac*180); return (cx+rad*math.cos(th), cy-rad*math.sin(th))
    lx,ly=pt(0,R); tx,ty=pt(1,R); vx,vy=pt(f,R)
    bg=f'<path d="M{lx:.0f} {ly:.0f} A{R} {R} 0 0 1 {tx:.0f} {ty:.0f}" fill="none" stroke="rgba(255,255,255,.09)" stroke-width="22" stroke-linecap="round"/>'
    val=f'<path d="M{lx:.0f} {ly:.0f} A{R} {R} 0 0 1 {vx:.0f} {vy:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="22" stroke-linecap="round" filter="url(#gag)"/>'
    ticks=""
    for frac,lab in [(0,"LOW"),(0.5,"MID"),(1,"FULL")]:
        ox,oy=pt(frac,R+26)
        ticks+=f'<text x="{ox:.0f}" y="{oy:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{lab}</text>'
    nx,ny=pt(f,R-30)
    needle=f'<line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#FAFAF7" stroke-width="6" stroke-linecap="round"/>'
    lock=(f'<circle cx="{cx}" cy="{cy}" r="52" fill="#221f1b" stroke="rgb({ACC})" stroke-width="2.5"/>'
          f'<g transform="translate({cx-24},{cy-26})"><rect x="0" y="22" width="48" height="34" rx="8" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M9 22 V12 a15 15 0 0 1 30 0 v10" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Climb fast, keep the handbrake","AUTONOMY · HELD")}
      <svg width="700" height="400" viewBox="0 0 700 400" style="display:block;margin:0 auto">
        <defs><filter id="gag" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {bg}{val}{ticks}{needle}{lock}
        <text x="{cx}" y="112" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="52" fill="#FAFAF7">84%</text>
        <text x="{cx}" y="140" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".16em" fill="rgb({ACC})">AUTONOMY</text>
        <text x="{cx}" y="{cy+94}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">every external move parks for your tap</text>
      </svg>
      {cap("autonomy grows, control does not shrink. external moves park for you.")}</div>'''

# 8. CEILING - IVORY DOT FIELD: a quiet field, steady operations running, one founder at the core
def ceiling():
    cols,rows=38,15; cell,gap=15,5
    lit={112,203,264,331,405,470,88,516}; core=286
    dots=""
    for i in range(cols*rows):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i==core:
            dots+=f'<rect x="{x-3}" y="{y-3}" width="{cell+6}" height="{cell+6}" rx="6" fill="#96562d" filter="url(#cg)"/>'
        elif i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(150,90,45,.55)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(120,95,60,.14)"/>'
    fw=cols*(cell+gap)-gap; fh=rows*(cell+gap)-gap
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#2a2016">1</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#96562d;margin-left:10px">founder, one subscription</span></div>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">JUST RUNNING</span></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="cg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#96562d" flood-opacity="0.9"/></filter></defs>
        {dots}</svg>
      {cap("a company that moves overnight. the ceiling is quiet, just running.","#8a745a")}</div>'''

PANELS={"floor":floor(),"memory":memory(),"jobs":jobs(),"ship":ship(),
        "routines":routines(),"gap":gap(),"gate":gate(),"ceiling":ceiling()}

if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/unstuck"; os.makedirs(outd,exist_ok=True)
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
