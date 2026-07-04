#!/usr/bin/env python3
# TIER 3 - THE 3-HOUR COURSE, INSTALLED. Rebuilt to the WIRE-ITS-EYES bar: each of the 8 panels a
# UNIQUE hand-built coded scene on a clean rounded card, htitle + one mono caption, NO stat-chip
# strips, NO clip-path cuts, NO extruded walls. Warm palette, Ultron cost = cents. Overwrites
# models_clay/syllabus/*.png. Cost zero.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"          # warm accent
IVA="#96562d"              # ivory-slide accent ink
BAD="200,70,35"            # muted red - ONLY for the bad/open/unsafe
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'

def htitle(t,tag):  # dark-card header
    return ('<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
        f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
        f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def hti(t,tag):     # ivory-card header
    return ('<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">'
        f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
        f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IVA}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:18px">{t}</div>'

# 1. mod1 - SYLLABUS / MODULE MAP (ivory). The 5-module course as a map, module 1 lit, an arrow to
# a self-written CLAUDE.md config file. Illustrates: the desk interviews you once and writes memory.
def mod1():
    mods=[("1","MEMORY","system prompts, files",True),
          ("2","AGENTS","teams and harnesses",False),
          ("3","SKILLS","subagents, leverage",False),
          ("4","BROWSER","computer use",False),
          ("5","SECURITY","permissions, gate",False)]
    rows=""
    for n,nm,sub,on in mods:
        chipbg=f"linear-gradient(160deg,{IVA},#7a4322)" if on else "rgba(150,120,80,.16)"
        chipc="#fdfbf6" if on else "#8a745a"
        bd=f"1.5px solid {IVA}" if on else "1px solid rgba(120,95,60,.16)"
        bg="rgba(150,90,45,.10)" if on else "rgba(255,255,255,.45)"
        nmc="#2a2016"; subc="#8a745a"
        tick=(f'<svg width="20" height="20" viewBox="0 0 24 24" style="margin-left:auto;flex-shrink:0"><path d="M6 12.5l3.5 3.5L18 7" fill="none" stroke="{IVA}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>' if on else '')
        rows+=(f'<div style="display:flex;align-items:center;gap:15px;background:{bg};border:{bd};border-radius:15px;padding:13px 16px">'
          f'<div style="flex-shrink:0;width:38px;height:38px;border-radius:11px;background:{chipbg};display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:19px;color:{chipc}">{n}</div>'
          f'<div><div style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:{nmc};letter-spacing:.02em">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:13.5px;color:{subc}">{sub}</div></div>{tick}</div>')
    doc=('<div style="background:rgba(255,255,255,.72);border:1px solid rgba(120,95,60,.2);border-radius:16px;padding:18px 18px 20px;box-shadow:0 18px 34px rgba(120,95,60,.16)">'
      f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:14px"><span style="width:11px;height:11px;border-radius:50%;background:{IVA}"></span>'
      '<span style="font-family:\'DM Mono\';font-weight:500;font-size:14px;color:#2a2016;letter-spacing:.04em">CLAUDE.md</span>'
      f'<span style="margin-left:auto;font-family:\'DM Mono\';font-size:10.5px;letter-spacing:.12em;color:{IVA}">AUTO</span></div>'
      + "".join(f'<div style="height:9px;border-radius:5px;background:rgba(150,120,80,.{o});width:{w}%;margin-bottom:9px"></div>' for o,w in [("30",96),("22",84),("30",92),("18",70),("26",88),("18",60)])
      + '<div style="font-family:\'DM Sans\';font-size:13px;color:#8a745a;margin-top:6px">written from one interview</div></div>')
    arrow=('<svg width="42" height="40" viewBox="0 0 42 40"><path d="M4 20h30M26 10l10 10-10 10" fill="none" '
      f'stroke="{IVA}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {hti("You never hand-write the config","MODULE 1 &middot; MEMORY")}
      <div style="display:flex;align-items:center;gap:26px">
        <div style="flex:1;display:flex;flex-direction:column;gap:11px">{rows}</div>
        <div style="flex-shrink:0">{arrow}</div>
        <div style="width:290px;flex-shrink:0">{doc}</div>
      </div>
      {cap("the course teaches you to write memory files by hand. the desk interviews you once and writes its own.","#8a745a")}</div>'''

# 2. mod2 - NODE GRAPH (dark). Seven named agents ringed around a ROUTER hub, bezier hand-off edges.
def mod2():
    W,H=820,500; cx,cy=410,248; R=196
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    edges=""; nodes=""
    pts=[]
    for i,nm in enumerate(agents):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a)); pts.append((x,y))
        edges+=f'<path d="M{cx} {cy} Q{(cx+x)/2+ (y-cy)*0.14:.0f} {(cy+y)/2 - (x-cx)*0.14:.0f} {x:.0f} {y:.0f}" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
    # a couple of peer hand-off arcs between adjacent agents
    for i in (0,2,4):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%7]
        edges+=f'<path d="M{x1:.0f} {y1:.0f} Q{cx} {cy} {x2:.0f} {y2:.0f}" fill="none" stroke="rgba(212,162,127,.14)" stroke-width="1.6" stroke-dasharray="3 7"/>'
    for (x,y),nm in zip(pts,agents):
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#221f1b" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="none" stroke="rgba(212,162,127,.35)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".04em" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, already wired","MODULE 2 &middot; TEAMS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub2" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#hg2)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#hub2)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">composes</text>
      </svg>
      {cap("three hours on orchestration. here the seven agents compose and hand off out of the box.")}</div>'''

# 3. mod3 - ISOMETRIC STACK (dark). A stocked shelf of 71 working skills, real names on the tiles.
def mod3():
    tiles=[("deep-research","fan-out + verify"),("dataviz","charts that read"),
           ("code-review","diff, ranked"),("verify","drive it end-to-end")]
    cards=""
    for i,(nm,sub) in enumerate(tiles):
        y=i*118
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 22px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h10" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:16px;color:#eae4d8;letter-spacing:.02em">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85;margin-top:1px">{sub}</div></div>'
          f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    badge=(f'<div style="position:absolute;left:392px;top:404px;display:flex;align-items:baseline;gap:9px;background:rgb({ACC});color:#1a0f0a;padding:11px 22px;border-radius:999px;box-shadow:0 12px 26px rgba(212,162,127,.4)">'
      '<span style="font-family:DM Sans;font-weight:900;font-size:30px;line-height:1">71</span>'
      '<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em">SKILLS LIVE</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Seventy-one skills, shipped","MODULE 3 &middot; LEVERAGE")}
      <div style="perspective:1900px;height:500px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:470px;position:relative">{cards}{badge}</div></div>
      {cap("the syllabus explains the concept. the desk ships 71 working skills, and each run costs cents.")}</div>'''

# 4. mod4 - TIMELINE (dark). A four-step action chain book -> fill -> check -> file, ending at a gate.
def mod4():
    W,H=820,430
    steps=[("BOOK","the meeting"),("FILL","the form"),("CHECK","the data"),("FILE","the record")]
    n=len(steps); x0,x1=90,730; gap=(x1-x0)/(n-1); y=176
    seg=""; nodes=""
    for i in range(n-1):
        seg+=f'<line x1="{x0+i*gap+46:.0f}" y1="{y}" x2="{x0+(i+1)*gap-46:.0f}" y2="{y}" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>'
    for i,(nm,sub) in enumerate(steps):
        x=x0+i*gap
        nodes+=(f'<circle cx="{x:.0f}" cy="{y}" r="46" fill="#221f1b" stroke="rgb({ACC})" stroke-width="2.5"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#FAFAF7">{i+1}</text>'
          f'<text x="{x:.0f}" y="{y+20:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="rgb({ACC})">STEP</text>'
          f'<text x="{x:.0f}" y="{y-78:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+94:.0f}" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#9a9488">{sub}</text>')
    gx=596; gy=y+128
    gate=(f'<line x1="{x1:.0f}" y1="{y+46}" x2="{gx+58}" y2="{gy}" stroke="rgba(212,162,127,.4)" stroke-width="2" stroke-dasharray="3 6"/>'
      f'<g transform="translate({gx},{gy})"><rect x="0" y="0" width="168" height="70" rx="16" fill="#201d19" stroke="rgb({ACC})" stroke-width="2"/>'
      f'<g transform="translate(24,19)"><rect x="0" y="16" width="30" height="22" rx="6" fill="none" stroke="rgb({ACC})" stroke-width="3.5"/><path d="M6 16 V9 a9 9 0 0 1 18 0 v7" fill="none" stroke="rgb({ACC})" stroke-width="3.5"/></g>'
      '<text x="112" y="32" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">gated</text>'
      '<text x="112" y="53" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#9a9488">your tap</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It books, fills, checks, files","MODULE 4 &middot; BROWSER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">{seg}{nodes}{gate}</svg>
      {cap("the lecture shows demos. the desk runs the real browser, and every external move waits for your tap.")}</div>'''

# 5. mod5 - GAUGE (dark). A posture dial: a thin red OPEN zone, a wide accent GATED zone, needle at
# GATED, a lock at the hub. Distinct speedometer-tick form.
def mod5():
    W,H=820,440; cx,cy=410,340; R=250
    ticks=""
    a0,a1=200,-20    # sweep left(200) over top to right(-20)
    steps=26
    for i in range(steps+1):
        a=a0+(a1-a0)*i/steps
        open_zone = i < 5     # first slice = OPEN / unsafe
        col=f"rgb({BAD})" if open_zone else (f"rgb({ACC})" if i>7 else "rgba(212,162,127,.4)")
        rin=R-26 if i%2 else R-34
        x1=cx+ (R)*math.cos(math.radians(a)); y1=cy - (R)*math.sin(math.radians(a))
        x2=cx+ rin*math.cos(math.radians(a)); y2=cy - rin*math.sin(math.radians(a))
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{5 if not open_zone else 5}" stroke-linecap="round"/>'
    na=-2   # needle near GATED (right)
    nx=cx+(R-58)*math.cos(math.radians(na)); ny=cy-(R-58)*math.sin(math.radians(na))
    needle=f'<line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#FAFAF7" stroke-width="5" stroke-linecap="round"/>'
    lbl=(f'<text x="{cx-R+34:.0f}" y="{cy+8}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({BAD})">OPEN</text>'
      f'<text x="{cx+R-30:.0f}" y="{cy+8}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">GATED</text>')
    lock=(f'<g transform="translate({cx-27},{cy-96})"><rect x="0" y="30" width="54" height="42" rx="10" fill="#201d19" stroke="rgb({ACC})" stroke-width="4"/>'
      f'<path d="M10 30 V19 a17 17 0 0 1 34 0 v11" fill="none" stroke="rgb({ACC})" stroke-width="4"/>'
      f'<circle cx="27" cy="50" r="6" fill="rgb({ACC})"/></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Defaults closed, not open","MODULE 5 &middot; SECURITY")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="ndg" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {ticks}{lbl}
        <g filter="url(#ndg)"><circle cx="{cx}" cy="{cy}" r="16" fill="rgb({ACC})"/></g>
        {needle}{lock}
        <text x="{cx}" y="{cy-118}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".14em" fill="#9a9488">POSTURE</text>
      </svg>
      {cap("the course warns you. the desk defaults to the gate: nothing external ships without a tap.")}</div>'''

# 6. gap10 - DOT FIELD (dark). One founder-week of 40 hours: the block spent configuring bleeds red,
# the rest is selling time. Illustrates: every setup hour is a lost sell.
def gap10():
    cols,rows_n=10,4   # 40 hours
    conf=14            # hours a founder loses to setup elsewhere
    cell=42; gp=13; dots=""
    for i in range(cols*rows_n):
        r,c=divmod(i,cols); x=c*(cell+gp); y=r*(cell+gp)
        if i<conf:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="10" fill="rgba({BAD},.9)" stroke="rgba({BAD},.5)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="10" fill="rgb({ACC})" opacity="0.92"/>'
    fw=cols*(cell+gp)-gp; fh=rows_n*(cell+gp)-gp
    legend=('<div style="display:flex;gap:26px;margin-top:20px">'
      f'<div style="display:flex;align-items:center;gap:10px"><span style="width:18px;height:18px;border-radius:5px;background:rgb({BAD})"></span><span style="font-family:DM Sans;font-size:16px;color:#d9d5cc">14h configuring</span></div>'
      f'<div style="display:flex;align-items:center;gap:10px"><span style="width:18px;height:18px;border-radius:5px;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:16px;color:#d9d5cc">26h selling</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">Setup hours are lost sells</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">ONE WEEK &middot; 40H</span></div>
      <div style="display:flex;align-items:center;gap:40px">
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="flex-shrink:0">{dots}</svg>
        <div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:58px;color:#FAFAF7;line-height:1">14h</div>
          <div style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#c9a583;margin-top:2px">gone before you sell</div>
          {legend}
        </div>
      </div>
      {cap("founders need outcomes, not configuration. here the config already IS the product.")}</div>'''

# 7. hour10 - INSTALL SCENE (ivory). A three-step onboarding: connect, interview, first run, filled
# progress bar, done by lunch. Illustrates: the 3 hours became one onboarding.
def hour10():
    steps=[("CONNECT","app + your inbox","09:04"),("INTERVIEW","one pass, your voice","09:31"),("FIRST RUN","a real brief shipped","11:52")]
    rows=""
    for i,(nm,sub,ts) in enumerate(steps):
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.6);border:1px solid rgba(120,95,60,.16);border-radius:15px;padding:15px 18px">'
          f'<div style="flex-shrink:0;width:40px;height:40px;border-radius:50%;background:linear-gradient(160deg,{IVA},#7a4322);display:flex;align-items:center;justify-content:center"><svg width="20" height="20" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7" fill="none" stroke="#fdfbf6" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:#2a2016;letter-spacing:.02em">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#8a745a">{sub}</div></div>'
          f'<span style="font-family:\'DM Mono\';font-size:15px;color:{IVA}">{ts}</span></div>')
    bar=(f'<div style="margin-top:22px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:9px">'
      '<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.1em;color:#8a745a">INSTALLED</span>'
      f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:20px;color:{IVA}">100%</span></div>'
      f'<div style="height:16px;border-radius:9px;background:rgba(150,120,80,.2);overflow:hidden"><div style="height:100%;width:100%;background:linear-gradient(90deg,{IVA},#c17a42)"></div></div>'
      '<div style="font-family:\'DM Sans\';font-size:14px;color:#8a745a;margin-top:9px">the whole syllabus, lived before lunch</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {hti("Three hours became one onboarding","ONE INSTALL")}
      <div style="display:flex;flex-direction:column;gap:12px">{rows}</div>
      {bar}
      {cap("connect, interview, first run. the first run costs cents, and it ships by lunch.","#8a745a")}</div>'''

# 8. point10 - RADIAL HUB (dark). A loop: install -> run -> correct -> repeat cycling an OPERATOR hub.
def point10():
    W,H=820,470; cx,cy=410,235; R=168
    loop=[("INSTALL",-90),("RUN",0),("CORRECT",90),("REPEAT",180)]
    nodes=""; arcs=""
    for nm,a in loop:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="52" fill="#221f1b" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".04em" fill="#e2dccf">{nm}</text>')
    # clockwise arcs between consecutive loop nodes, with arrowheads
    ang=[a for _,a in loop]
    for i in range(4):
        a=ang[i]; b=ang[(i+1)%4]
        ar=R  # arc radius for the connecting path
        # midpoint bulge outward
        ma=(a + (45 if True else 0))
        sx=cx+R*math.cos(math.radians(a+22)); sy=cy+R*math.sin(math.radians(a+22))
        ex=cx+R*math.cos(math.radians(b-22)); ey=cy+R*math.sin(math.radians(b-22))
        arcs+=f'<path d="M{sx:.0f} {sy:.0f} A{R} {R} 0 0 1 {ex:.0f} {ey:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="3" marker-end="url(#ah)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Knowledge was never the moat","THE POINT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="oph" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ohg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter>
        <marker id="ah" markerWidth="9" markerHeight="9" refX="5" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="rgb({ACC})"/></marker></defs>
        {arcs}{nodes}
        <g filter="url(#ohg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#oph)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">OPERATOR</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">ships daily</text>
      </svg>
      {cap("the people shipping are not the ones studying. install, run, correct, repeat.")}</div>'''

PANELS={"mod1":mod1(),"mod2":mod2(),"mod3":mod3(),"mod4":mod4(),
        "mod5":mod5(),"gap10":gap10(),"hour10":hour10(),"point10":point10()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/syllabus"; os.makedirs(outd,exist_ok=True)
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
