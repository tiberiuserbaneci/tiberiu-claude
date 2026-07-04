#!/usr/bin/env python3
# TIER 3 - FIVE CLAUDES, ONE FOUNDER, rebuilt to the WIRE-ITS-EYES / AI-BODY bar: each panel a
# UNIQUE hand-built coded scene filling a clean rounded card, title + one-line caption, NO generic
# stat-chip strips, NO clip-path cuts, NO extruded walls. Warm palette. Overrides models_clay/fivetools.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"          # warm kraft accent
IVACC="#96562d"            # ivory-slide accent (darker, reads on cream)
BAD="200,70,35"            # muted red, ONLY for the wrong / broken
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'

def htitle(t,tag,ink="#FAFAF7",tagc=None):
    tagc=tagc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. door1 - GAUGE: speed dial, needle pinned near FAST, digital readout. CHAT = the fast answer.
def door1():
    cx,cy,R=306,318,238
    def P(th,r=R): return (cx+r*math.cos(math.radians(th)), cy-r*math.sin(math.radians(th)))
    # ticks across the 180..0 sweep
    ticks=""
    for i in range(0,11):
        th=180-i*18
        x1,y1=P(th,R+3); x2,y2=P(th,R-24); big=(i%5==0)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{"rgba(212,162,127,.75)" if big else "rgba(250,250,247,.22)"}" stroke-width="{3.4 if big else 2}"/>'
    val=0.86; vth=180-val*180
    lx,ly=P(180); rx,ry=P(0); vx,vy=P(vth)
    nx,ny=P(vth,R-56)
    track=f'<path d="M{lx:.0f} {ly:.0f} A{R} {R} 0 0 1 {rx:.0f} {ry:.0f}" fill="none" stroke="rgba(250,250,247,.09)" stroke-width="20" stroke-linecap="round"/>'
    valarc=f'<path d="M{lx:.0f} {ly:.0f} A{R} {R} 0 0 1 {vx:.0f} {vy:.0f}" fill="none" stroke="url(#g1)" stroke-width="20" stroke-linecap="round"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The fast answer","CHAT &middot; DOOR 1")}
      <svg width="612" height="474" viewBox="0 0 612 474" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="g1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8a4a2c"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
          <radialGradient id="hubg" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="ng" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.75"/></filter>
        </defs>
        {track}{valarc}{ticks}
        <text x="{cx-R+6:.0f}" y="{cy+30}" text-anchor="start" font-family="DM Mono" font-size="14" letter-spacing=".12em" fill="#7a746a">SLOW</text>
        <text x="{cx+R-6:.0f}" y="{cy+30}" text-anchor="end" font-family="DM Mono" font-size="14" letter-spacing=".12em" fill="rgb({ACC})">FAST</text>
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="18" fill="url(#hubg)"/>
        <text x="{cx}" y="{cy+120}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="88" fill="#FAFAF7">11s</text>
        <text x="{cx}" y="{cy+150}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".22em" fill="rgb({ACC})">FIRST DRAFT</text>
      </svg>
      {cap("quick questions and first drafts. where everyone starts, most people stop.")}</div>'''

# 2. door2 - VERTICAL TIMELINE (ivory): sessions on one spine, each remembers the last. PROJECTS = memory.
def door2():
    rows=[("MON","Kickoff","goals + ICP saved to the project"),
          ("WED","Reporting","reused last week's numbers"),
          ("FRI","Board prep","pulled the full thread"),
          ("MON","Client work","zero re-explaining")]
    items=""
    for d,t,s in rows:
        items+=f'''<div style="position:relative;margin-bottom:18px;background:rgba(255,255,255,.6);border:1px solid rgba(120,95,60,.16);border-radius:16px;padding:15px 20px 15px 22px;box-shadow:0 10px 22px rgba(150,120,80,.14), inset 0 1.5px 2px rgba(255,255,255,.9)">
          <div style="position:absolute;left:-37px;top:22px;width:18px;height:18px;border-radius:50%;background:{IVACC};box-shadow:0 0 0 5px rgba(150,86,45,.14)"></div>
          <div style="display:flex;align-items:baseline;justify-content:space-between">
            <span style="font-family:'DM Sans';font-weight:800;font-size:21px;color:#2a2016">{t}</span>
            <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.16em;color:{IVACC}">{d}</span></div>
          <div style="font-family:'DM Sans';font-size:16px;color:#6a5540;margin-top:3px">{s}</div></div>'''
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("The memory","PROJECTS &middot; DOOR 2","#17150F",IVACC)}
      <div style="position:relative;padding-left:52px">
        <div style="position:absolute;left:26px;top:16px;bottom:16px;width:2.5px;background:linear-gradient(180deg,{IVACC},rgba(150,86,45,.2))"></div>
        {items}</div>
      {cap("context that survives every session. stop re-explaining yourself.","#8a745a")}</div>'''

# 3. door3 - ISOMETRIC FILE STACK: folder -> sheet -> report, saved in place. COWORK = hands on files.
def door3():
    steps=[("FOLDER","reads /Q3-close"),("SHEET","1,240 rows reconciled"),("REPORT","drafted where it lives")]
    icon={"FOLDER":'<path d="M4 8 h7 l3 3 h8 a2 2 0 0 1 2 2 v9 a2 2 0 0 1 -2 2 H4 a2 2 0 0 1 -2 -2 V10 a2 2 0 0 1 2 -2Z" fill="none" stroke="rgb('+ACC+')" stroke-width="2.2"/>',
          "SHEET":'<rect x="4" y="4" width="20" height="20" rx="3" fill="none" stroke="rgb('+ACC+')" stroke-width="2.2"/><line x1="4" y1="11" x2="24" y2="11" stroke="rgb('+ACC+')" stroke-width="2"/><line x1="11" y1="4" x2="11" y2="24" stroke="rgb('+ACC+')" stroke-width="2"/>',
          "REPORT":'<path d="M7 3 h9 l6 6 v16 a1 1 0 0 1 -1 1 H7 a1 1 0 0 1 -1 -1 V4 a1 1 0 0 1 1 -1Z" fill="none" stroke="rgb('+ACC+')" stroke-width="2.2"/><line x1="10" y1="14" x2="19" y2="14" stroke="rgb('+ACC+')" stroke-width="2"/><line x1="10" y1="19" x2="16" y2="19" stroke="rgb('+ACC+')" stroke-width="2"/>'}
    cards=""
    for i,(nm,sub) in enumerate(steps):
        y=i*130
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="28" height="28" viewBox="0 0 28 28">{icon[nm]}</svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Hands on your files","COWORK &middot; DOOR 3")}
      <div style="perspective:1900px;height:474px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:432px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:400px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Saved in place &#10003;</div></div></div>
      {cap("reads your folders, works your sheets, drafts reports where they live.")}</div>'''

# 4. door4 - NODE GRAPH: a workflow chain, one command, looped back "every run". SKILLS = repeatable plays.
def door4():
    W,H=820,470
    nodes=[("/weekly-report","command",120,110),("pull metrics","step",560,110),
           ("format deck","step",560,320),("post + notify","output",120,320)]
    boxw,boxh=270,92
    def cxy(x,y): return (x+boxw/2,y+boxh/2)
    edges=""
    seq=[0,1,2,3]
    for a,b in zip(seq,seq[1:]):
        (x0,y0),(x1,y1)=cxy(*nodes[a][2:]),cxy(*nodes[b][2:])
        if nodes[a][3]==nodes[b][3]:      # horizontal
            edges+=f'<path d="M{x0+boxw/2 if x1>x0 else x0-boxw/2:.0f} {y0:.0f} H{x1-boxw/2 if x1>x0 else x1+boxw/2:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="4" marker-end="url(#ar)"/>'
        else:                             # vertical
            edges+=f'<path d="M{x0:.0f} {y0+boxh/2:.0f} V{y1-boxh/2:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="4" marker-end="url(#ar)"/>'
    # loop back output(3) -> command(0), curved on the left, labelled every run
    (ox,oy)=cxy(*nodes[3][2:]); (sx,sy)=cxy(*nodes[0][2:])
    loop=f'<path d="M{ox-boxw/2:.0f} {oy:.0f} C-24 {oy:.0f},-24 {sy:.0f},{sx-boxw/2:.0f} {sy:.0f}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3" stroke-dasharray="7 8" marker-end="url(#ar2)"/>'
    boxes=""
    for nm,role,x,y in nodes:
        cmd=(role=="command"); out=(role=="output")
        bg="linear-gradient(160deg,#403a33,#241f1a)" if (cmd or out) else "#221f1b"
        bd=f"rgb({ACC})" if (cmd or out) else "rgba(255,255,255,.1)"
        boxes+=(f'<g><rect x="{x}" y="{y}" width="{boxw}" height="{boxh}" rx="18" fill="{bg}" stroke="{bd}" stroke-width="{2.4 if (cmd or out) else 1.4}"/>'
          f'<text x="{x+22}" y="{y+38}" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="rgb({ACC})">{role.upper()}</text>'
          f'<text x="{x+22}" y="{y+68}" font-family="DM Sans" font-weight="800" font-size="23" fill="#FAFAF7">{nm}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The repeatable play","SKILLS &middot; DOOR 4")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <marker id="ar" markerWidth="10" markerHeight="10" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="rgb({ACC})"/></marker>
          <marker id="ar2" markerWidth="10" markerHeight="10" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="rgba(212,162,127,.6)"/></marker>
        </defs>
        {edges}{loop}{boxes}
        <text x="30" y="{(oy+sy)/2:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})" transform="rotate(-90 30 {(oy+sy)/2:.0f})">every run</text>
      </svg>
      {cap("your workflow installed as one command. same play, no re-prompting.")}</div>'''

# 5. door5 - DOT FIELD: a test grid, all green-free accent, 42/42 passed then shipped. CODE = the builder.
def door5():
    cols,rowsn=7,6           # 42
    cell,gap=52,14
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="13" fill="url(#pg)" filter="url(#pgl)"/><path d="M{x+16} {y+27} l7 7 l13 -16" fill="none" stroke="#1a0f0a" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Plain English to shipped","CODE &middot; DOOR 5")}
      <div style="display:flex;align-items:center;gap:36px">
        <div style="flex-shrink:0;width:250px">
          <div style="font-family:'DM Sans';font-weight:900;font-size:74px;color:#FAFAF7;line-height:.95">42<span style="color:rgb({ACC})">/42</span></div>
          <div style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-top:2px">tests passing</div>
          <div style="font-family:'DM Mono';font-size:14px;color:#8f8f85;margin-top:10px">0 failed &middot; 0 flaky</div>
          <div style="display:inline-flex;align-items:center;gap:9px;margin-top:22px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:11px 20px;border-radius:999px;box-shadow:0 12px 24px rgba(212,162,127,.4)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>SHIPPED &middot; main</div>
        </div>
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
          <defs><radialGradient id="pg" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#9a5a35"/></radialGradient>
          <filter id="pgl" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="rgba(0,0,0,.45)"/></filter></defs>
          {dots}</svg>
      </div>
      {cap("pages, dashboards and tools from plain English, tested before they ship.")}</div>'''

# 6. mistake9 - ORG-CHART mapping: jobs -> right door (accent), the one wrong edge crossed in muted red.
def mistake9():
    W,H=820,464
    jobs=[("weekly report","every week",84),("one-off question","just ask",214),("build a tool","from English",344)]
    doors=[("Skills","door 4",84),("Chat","door 1",214),("Code","door 5",344)]
    jx,jw=40,300; dx,dw=480,300
    correct={0:0,1:1,2:2}       # job idx -> door idx (right)
    edges=""
    for ji,di in correct.items():
        y0=jobs[ji][2]; y1=doors[di][2]
        edges+=f'<path d="M{jx+jw} {y0} C{(jx+jw+dx)/2:.0f} {y0},{(jx+jw+dx)/2:.0f} {y1},{dx} {y1}" fill="none" stroke="rgb({ACC})" stroke-width="3.4"/>'
    # THE MISTAKE: weekly report (job0) -> Chat (door1), red dashed, X on it
    y0=jobs[0][2]; y1=doors[1][2]; mx=(jx+jw+dx)/2
    edges+=f'<path d="M{jx+jw} {y0} C{mx:.0f} {y0},{mx:.0f} {y1},{dx} {y1}" fill="none" stroke="rgb({BAD})" stroke-width="3" stroke-dasharray="8 7"/>'
    cxm=mx; cym=(y0+y1)/2
    edges+=f'<circle cx="{cxm:.0f}" cy="{cym:.0f}" r="17" fill="#241713" stroke="rgb({BAD})" stroke-width="2"/><line x1="{cxm-7:.0f}" y1="{cym-7:.0f}" x2="{cxm+7:.0f}" y2="{cym+7:.0f}" stroke="rgb({BAD})" stroke-width="2.6"/><line x1="{cxm+7:.0f}" y1="{cym-7:.0f}" x2="{cxm-7:.0f}" y2="{cym+7:.0f}" stroke="rgb({BAD})" stroke-width="2.6"/>'
    def col(items,x,w,right):
        g=""
        for i,(t,s,y) in enumerate(items):
            hot=right and i==0
            bd=f"rgb({ACC})" if hot else "rgba(255,255,255,.1)"
            g+=(f'<g><rect x="{x}" y="{y-42}" width="{w}" height="84" rx="18" fill="url(#jc)" stroke="{bd}" stroke-width="{2.4 if hot else 1.4}"/>'
              f'<text x="{x+24}" y="{y-4}" font-family="DM Sans" font-weight="800" font-size="24" fill="#FAFAF7">{t}</text>'
              f'<text x="{x+24}" y="{y+22}" font-family="DM Mono" font-size="13" fill="{"rgb("+ACC+")" if right else "#8f8f85"}">{s}</text></g>')
        return g
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Match the door to the job","THE MISTAKE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="jc" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#302c28"/><stop offset="100%" stop-color="#201d1a"/></linearGradient></defs>
        <text x="{jx+16}" y="26" font-family="DM Mono" font-size="12" letter-spacing=".16em" fill="#7a746a">THE JOB</text>
        <text x="{dx+16}" y="26" font-family="DM Mono" font-size="12" letter-spacing=".16em" fill="rgb({ACC})">THE RIGHT DOOR</text>
        {edges}{col(jobs,jx,jw,False)}{col(doors,dx,dw,True)}
        <text x="{cxm:.0f}" y="{cym+40:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({BAD})">the mistake</text>
      </svg>
      {cap("re-typing a workflow into Chat every week is a Skills job done badly.")}</div>'''

# 7. desk9 - RADIAL HUB: one composer, five doors wired around it, memory carried. THE DESK.
def desk9():
    W,H=820,472
    cx,cy=410,236; R=182
    doors=[("Chat",-90),("Projects",-18),("Cowork",54),("Skills",126),("Code",198)]
    spokes=""; nodes=""
    for nm,a in doors:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.8"/>'
          f'<text x="{x:.0f}" y="{y+6:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#e6dccb">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One composer, five doors","THE DESK")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hb" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R+46}" fill="none" stroke="rgba(212,162,127,.14)" stroke-dasharray="3 9"/>
        {spokes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="86" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">COMPOSER</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#3a2010">one prompt</text>
        {nodes}
      </svg>
      {cap("type the goal. the router opens the right door and carries your memory.")}</div>'''

# 8. unlock9 - CONSTELLATION (ivory): the five doors as stars, faint links, 80% = knowing they exist.
def unlock9():
    W,H=820,462
    stars=[("Chat",150,120),("Projects",360,86),("Cowork",610,150),("Skills",470,300),("Code",180,330)]
    links=[(0,1),(1,2),(2,3),(3,4),(4,0),(1,4)]
    ln=""
    for a,b in links:
        ln+=f'<line x1="{stars[a][1]}" y1="{stars[a][2]}" x2="{stars[b][1]}" y2="{stars[b][2]}" stroke="rgba(150,86,45,.32)" stroke-width="1.6"/>'
    st=""
    for nm,x,y in stars:
        st+=(f'<circle cx="{x}" cy="{y}" r="30" fill="rgba(150,86,45,.10)"/>'
          f'<circle cx="{x}" cy="{y}" r="13" fill="{IVACC}" filter="url(#sg)"/>'
          f'<text x="{x}" y="{y+50}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#3a2c1c">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("Knowing beats coding","THE UNLOCK","#17150F",IVACC)}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="sg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgba(150,86,45,.7)"/></filter></defs>
        {ln}{st}
        <g transform="translate(628,300)">
          <text x="0" y="0" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="90" fill="{IVACC}">80%</text>
          <text x="0" y="34" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#8a745a">IS KNOWING</text>
          <text x="0" y="56" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#8a745a">THEY EXIST</text>
        </g>
      </svg>
      {cap("non-technical was never the barrier. open door two tonight.","#8a745a")}</div>'''

PANELS={"door1":door1(),"door2":door2(),"door3":door3(),"door4":door4(),
        "door5":door5(),"mistake9":mistake9(),"desk9":desk9(),"unlock9":unlock9()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/fivetools"; os.makedirs(outd,exist_ok=True)
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
