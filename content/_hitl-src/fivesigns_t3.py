#!/usr/bin/env python3
# TIER 3 - 5 SIGNS YOU NEED AI NOW, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, htitle + mono tag + one mono caption.
# NO generic stat-chip strips. Clean rounded cards only (CARD / CARDIV), no clip-path, no side-walls.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
BAD="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc};white-space:nowrap;padding-left:20px">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'
def arc(cx,cy,r,a0,a1,large=0,sweep=1):
    x0,y0=cx+r*math.cos(math.radians(a0)),cy+r*math.sin(math.radians(a0))
    x1,y1=cx+r*math.cos(math.radians(a1)),cy+r*math.sin(math.radians(a1))
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 {large} {sweep} {x1:.1f} {y1:.1f}'

# 1. SIGN1 - tally/glyph FIELD: 40 identical support questions vs one flow that answers them
def sign1():
    cols,rn,cell,gap=8,5,54,14
    bub=""
    for i in range(40):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        bub+=(f'<g transform="translate({x},{y})">'
          f'<rect x="0" y="0" width="{cell}" height="{cell-16}" rx="9" fill="rgba(250,250,247,.055)" stroke="rgba(250,250,247,.12)"/>'
          f'<path d="M13 {cell-16} l0 10 l11 -10Z" fill="rgba(250,250,247,.055)"/>'
          f'<line x1="9" y1="12" x2="{cell-11}" y2="12" stroke="rgba(212,162,127,.42)" stroke-width="3" stroke-linecap="round"/>'
          f'<line x1="9" y1="23" x2="{cell-20}" y2="23" stroke="rgba(250,250,247,.16)" stroke-width="3" stroke-linecap="round"/></g>')
    gw=cols*(cell+gap)-gap; gh=rn*(cell+gap)-gap
    right=(f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px">'
      f'<div><span style="font-family:DM Sans;font-weight:900;font-size:56px;color:#FAFAF7;line-height:1">40</span>'
      f'<span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#c9a583;margin-left:8px">same reply / week</span></div>'
      f'<svg width="34" height="52" viewBox="0 0 34 52"><path d="M17 4 V44 M6 33 L17 46 L28 33" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      f'<div style="background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:16px;padding:16px 18px;box-shadow:0 0 26px rgba(212,162,127,.22)">'
      f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">1 ULTRON FLOW</div>'
      f'<div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7;margin-top:3px">answers in 4s</div>'
      f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-top:1px">0 of your minutes</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The same answer, 40x","SUPPORT LOOP")}
      <div style="display:flex;align-items:center;gap:34px">
        <svg width="{gw}" height="{gh}" viewBox="0 0 {gw} {gh}" style="flex-shrink:0">{bub}</svg>
        {right}
      </div>
      {cap("if support answers repeat daily, a flow should answer them in seconds.")}</div>'''

# 2. SIGN2 - NODE / bezier graph: apps wired by hand into a person, vs one clean flow
def sign2():
    W,H=820,432
    apps=[("CRM",92),("Sheets",188),("Inbox",284),("Billing",380)]
    handx,handy=470,236
    edges=""; nodes=""
    for nm,y in apps:
        mx=(200+handx)/2
        edges+=f'<path d="M200 {y} C{mx:.0f} {y},{mx:.0f} {handy},{handx-52} {handy}" fill="none" stroke="rgba(200,70,35,.42)" stroke-width="2.4" stroke-dasharray="6 6"/>'
        nodes+=(f'<rect x="40" y="{y-27}" width="160" height="54" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="66" cy="{y}" r="7" fill="rgb({ACC})"/>'
          f'<text x="86" y="{y+6}" font-family="DM Mono" font-size="15" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Payroll on glue work","MANUAL SYNC")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:2px auto 0">
        <defs><radialGradient id="s2h" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="s2g" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{nodes}
        <circle cx="{handx}" cy="{handy}" r="46" fill="#241f1a" stroke="rgba(200,70,35,.55)" stroke-width="2"/>
        <path d="M{handx-16} {handy+6} v-14 a4 4 0 0 1 8 0 v10 m0 -2 a4 4 0 0 1 8 0 v4 m0 -2 a4 4 0 0 1 8 0 v6 a14 14 0 0 1 -14 14 h-4 a12 12 0 0 1 -10 -8 l-6 -10 a4 4 0 0 1 8 -4 l2 4" fill="none" stroke="rgb({BAD})" stroke-width="2.6" stroke-linejoin="round"/>
        <text x="{handx}" y="{handy+72}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({BAD})">copy / paste, 6 hrs/wk</text>
        <path d="M{handx+46} {handy} H600" stroke="rgba(212,162,127,.3)" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>
        <g filter="url(#s2g)"><circle cx="672" cy="{handy}" r="62" fill="url(#s2h)"/></g>
        <text x="672" y="{handy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">1 FLOW</text>
        <text x="672" y="{handy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">wired once</text>
      </svg>
      {cap("hours spent moving data between apps is payroll spent on glue work.")}</div>'''

# 3. SIGN3 - FUNNEL: a wide queue narrows through your thumb-gate, only a trickle clears
def sign3():
    W,H=430,452
    cx=W/2
    top=80; ny=250; bot=376; halfT=195; halfN=46
    funnel=(f'<path d="M{cx-halfT} {top} L{cx+halfT} {top} L{cx+halfN} {ny} L{cx-halfN} {ny} Z" '
            f'fill="rgba(212,162,127,.10)" stroke="rgba(212,162,127,.34)" stroke-width="2"/>')
    chips=""
    pos=[(-140,112),(-60,112),(20,112),(100,112),(-118,140),(-38,140),(42,140),(115,140),(-88,170),(-8,170),(70,170),(-30,196)]
    for dx,y in pos:
        chips+=f'<rect x="{cx+dx-22:.0f}" y="{y}" width="44" height="18" rx="6" fill="rgba(250,250,247,.10)" stroke="rgba(250,250,247,.16)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="flex-shrink:0">
        <defs><filter id="s3g" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        <text x="{cx}" y="60" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">47 tasks queued</text>
        {funnel}{chips}
        <g transform="translate({cx-26},{ny-4})">
          <path d="M8 46 v-22 a5 5 0 0 1 10 0 v14 l14 -18 a6 6 0 0 1 10 6 l-8 14 h10 a6 6 0 0 1 0 12 l-2 12 a8 8 0 0 1 -8 6 H16 a8 8 0 0 1 -8 -8 Z" fill="rgba(212,162,127,.16)" stroke="rgb({ACC})" stroke-width="2.4" stroke-linejoin="round"/>
        </g>
        <text x="{cx+64}" y="{ny+22}" font-family="DM Mono" font-size="13" fill="rgb({ACC})">your thumb</text>
        <line x1="{cx}" y1="{ny+52}" x2="{cx}" y2="{bot-30}" stroke="rgba(212,162,127,.3)" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>
        <rect x="{cx-70}" y="{bot-24}" width="140" height="48" rx="12" fill="#241f1a" stroke="rgba(212,162,127,.4)"/>
        <circle cx="{cx-46}" cy="{bot}" r="6" fill="rgb({ACC})" filter="url(#s3g)"/>
        <text x="{cx-30}" y="{bot+5}" font-family="DM Sans" font-weight="700" font-size="16" fill="#e6d6c2">3 / hour</text>
      </svg>
      <div style="flex:1">
        {htitle("You are the bottleneck","WORK QUEUE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Everything that ships routes through your two thumbs. The queue grows faster than you can tap.</div>
        <div style="font-family:DM Sans;font-weight:900;font-size:34px;color:rgb({ACC});margin-top:16px">23 waiting on you</div>
        {cap("Ultron preps everything, you just tap the ones that matter.")}
      </div></div>'''

# 4. SIGN4 - GAUGE / dial: speed-to-lead, needle deep in the cold zone
def sign4():
    cx,cy,R=250,300,196
    zones=[(180,240,f"rgb({ACC})"),(240,300,"#c9a583"),(300,360,f"rgb({BAD})")]
    zsvg=""
    for a0,a1,col in zones:
        zsvg+=f'<path d="{arc(cx,cy,R,a0,a1)}" fill="none" stroke="{col}" stroke-width="26" stroke-linecap="butt"/>'
    ticks=""
    for a in range(180,361,30):
        x0,y0=cx+(R-24)*math.cos(math.radians(a)),cy+(R-24)*math.sin(math.radians(a))
        x1,y1=cx+(R-6)*math.cos(math.radians(a)),cy+(R-6)*math.sin(math.radians(a))
        ticks+=f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke="rgba(255,255,255,.28)" stroke-width="2"/>'
    na=326
    nx,ny=cx+(R-40)*math.cos(math.radians(na)),cy+(R-40)*math.sin(math.radians(na))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="500" height="360" viewBox="0 0 500 360" style="flex-shrink:0">
        {zsvg}{ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#FAFAF7" stroke-width="5" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="12" fill="#FAFAF7"/>
        <text x="{cx-R+8}" y="{cy+26}" font-family="DM Mono" font-size="12" fill="rgb({ACC})">4 min</text>
        <text x="{cx+R-38}" y="{cy+26}" font-family="DM Mono" font-size="12" fill="rgb({BAD})">hours</text>
        <text x="{cx}" y="{cy-42}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">5 hrs</text>
        <text x="{cx}" y="{cy-18}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({BAD})">COLD · LOST</text>
      </svg>
      <div style="flex:1">
        {htitle("Leads cool in the inbox","SPEED TO LEAD")}
        <div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
          <div style="background:rgba(200,70,35,.10);border:1px solid rgba(200,70,35,.4);border-radius:14px;padding:14px 18px">
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({BAD})">YOUR INBOX</div>
            <div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7">replies in 5 hours</div></div>
          <div style="background:rgba(212,162,127,.10);border:1px solid rgb({ACC});border-radius:14px;padding:14px 18px">
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">ULTRON FLOW</div>
            <div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7">replies in 4 minutes, gated</div></div>
        </div>
        {cap("speed to lead decides the meeting. the flow answers in seconds.")}
      </div></div>'''

# 5. SIGN5 - IVORY iso card stack: month-end reports assemble into one sourced page
def sign5():
    rows=[("P&L","revenue, cost, margin"),("Cash","runway, burn, in/out"),("Metrics","MRR, churn, CAC")]
    cards=""
    for i,(a,b) in enumerate(rows):
        y=i*118
        bars="".join(f'<span style="width:{w}px;height:8px;border-radius:4px;background:{"#96562d" if k==2 else "rgba(150,90,45,.32)"};display:inline-block;margin-right:6px"></span>' for k,w in enumerate([46,30,64]))
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:520px;background:linear-gradient(160deg,#fffdf9,#f1e8d8);'
          f'border:1px solid rgba(150,120,80,.28);border-radius:16px;padding:18px 22px;box-shadow:0 26px 40px rgba(120,95,60,.28), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:20px">'
          f'<div style="flex:1;text-align:left"><div style="font-family:DM Sans;font-weight:800;font-size:23px;color:#2a2016">{a}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8a745a;margin-top:1px">{b}</div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center">{bars}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Month-end steals 3 days","MONTH CLOSE","#2a2016","#96562d")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="perspective:1700px;flex-shrink:0;width:520px;height:470px;display:flex;align-items:center">
          <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:520px;height:354px;position:relative">{cards}</div>
        </div>
        <div style="flex:1">
          <div style="background:linear-gradient(160deg,#96562d,#7a4326);border-radius:16px;padding:20px 22px;box-shadow:0 22px 40px rgba(150,90,45,.4)">
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#f0d9c4">ULTRON · ON DEMAND</div>
            <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#fffdf9;margin-top:6px">1 page</div>
            <div style="font-family:DM Sans;font-size:16px;color:#f3e4d4;margin-top:2px">assembled in minutes, every figure sourced</div></div>
          <div style="display:flex;align-items:center;gap:9px;margin-top:16px">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>
            <span style="font-family:DM Sans;font-size:16px;color:#5a4634">no more 3-day close</span></div>
        </div>
      </div>
      {cap("the numbers already exist. Ultron assembles them on demand, with sources.","#8a745a")}</div>'''

# 6. TEST - IVORY segmented score ring: 3 of 5 signs lit -> you are the system
def test():
    cx,cy,r=150,168,110
    n=5; gap=8; seg=(360/n)-gap
    segs=""
    for i in range(n):
        a0=-90+i*(360/n)+gap/2; a1=a0+seg
        lit=i<3
        col="#96562d" if lit else "rgba(150,90,45,.20)"
        segs+=f'<path d="{arc(cx,cy,r,a0,a1)}" fill="none" stroke="{col}" stroke-width="20" stroke-linecap="round"/>'
    qs=[("Q1","support loop",True),("Q2","manual sync",True),("Q3","work queue",True),("Q4","lead lag",False),("Q5","month close",False)]
    rows=""
    for q,lab,yes in qs:
        c="#96562d" if yes else "rgba(120,95,60,.35)"
        mark=("<path d='M6 10.5 9 13.5 15 6' fill='none' stroke='#fffdf9' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'/>" if yes else "<line x1='6' y1='6' x2='15' y2='15' stroke='#8a745a' stroke-width='2.4' stroke-linecap='round'/><line x1='15' y1='6' x2='6' y2='15' stroke='#8a745a' stroke-width='2.4' stroke-linecap='round'/>")
        rows+=(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:11px">'
          f'<svg width="21" height="21" viewBox="0 0 21 21" style="flex-shrink:0"><circle cx="10.5" cy="10.5" r="10" fill="{c}"/>{mark}</svg>'
          f'<span style="font-family:DM Mono;font-size:14px;letter-spacing:.06em;color:#96562d">{q}</span>'
          f'<span style="font-family:DM Sans;font-size:17px;color:#4a3f30">{lab}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Three yes or more","THE TEST","#2a2016","#96562d")}
      <div style="display:flex;align-items:center;gap:40px">
        <div style="flex-shrink:0;position:relative;width:300px;height:336px">
          <svg width="300" height="336" viewBox="0 0 300 336">{segs}</svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:66px;color:#2a2016;line-height:1">3<span style="font-size:34px;color:#96562d">/5</span></span>
            <span style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#96562d;margin-top:4px">YES</span></div>
        </div>
        <div style="flex:1">
          {rows}
          <div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#2a2016;margin-top:8px">You are the system.</div>
        </div>
      </div>
      {cap("five yes answers is not a staffing problem. it is missing systems.","#8a745a")}</div>'''

# 7. FIX - horizontal ranked leak meter: worst leak highlighted, one plug on it
def fix():
    leaks=[("Support loop","6 hrs/wk",6,True),("Manual sync","4 hrs/wk",4,False),
           ("Lead lag","3 hrs/wk",3,False),("Month close","3 hrs/wk",3,False),("Task queue","2 hrs/wk",2,False)]
    mx=6; maxw=520
    bars=""
    for nm,val,h,worst in leaks:
        w=int(maxw*h/mx)
        if worst:
            fill=f"linear-gradient(90deg,#7a4326,rgb({ACC}))"; bd=f"rgb({ACC})"; glow="box-shadow:0 0 24px rgba(212,162,127,.34)"; txt="#1a0f0a"
        else:
            fill="linear-gradient(90deg,#332f2a,#3d3831)"; bd="rgba(255,255,255,.10)"; glow=""; txt="#c9c3b8"
        plug=(f'<div style="position:absolute;right:12px;top:50%;transform:translateY(-50%);display:flex;align-items:center;gap:6px">'
              f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.4" stroke-linecap="round"><path d="M14 4l6 6-4 4-6-6z"/><path d="M10 8l-6 6v4h4l6-6"/></svg>'
              f'<span style="font-family:DM Mono;font-size:12px;color:#1a0f0a">FIX FIRST</span></div>') if worst else ''
        bars+=(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:14px">'
          f'<span style="width:132px;flex-shrink:0;font-family:DM Sans;font-weight:700;font-size:18px;color:{"#FAFAF7" if worst else "#c9c3b8"}">{nm}</span>'
          f'<div style="position:relative;width:{w}px;height:44px;border-radius:12px;background:{fill};border:1.5px solid {bd};{glow};display:flex;align-items:center;padding-left:16px">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:17px;color:{txt}">{val}</span>{plug}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Plug the worst leak","FIX FIRST")}
      <div style="margin-top:6px">{bars}</div>
      {cap("automate the worst leak first. Ultron sets it up from one sentence.")}</div>'''

# 8. GATE - flow orb held on your veto: dashed reins to a lock/tap panel
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Automate. Keep the veto.","HUMAN GATE")}
      <svg width="820" height="424" viewBox="0 0 820 424" style="display:block;margin:0 auto">
        <defs><radialGradient id="g8" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="g8g" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#g8g)"><circle cx="205" cy="212" r="132" fill="url(#g8)"/></g>
        <text x="205" y="206" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">AUTO</text>
        <text x="205" y="240" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".1em">EVERY FLOW</text>
        <path d="M340 212 H612" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <text x="476" y="192" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">parks here</text>
        <rect x="622" y="140" width="144" height="144" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(664,178)"><rect x="0" y="36" width="60" height="44" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M11 36 V22 a19 19 0 0 1 38 0 v14" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="694" y="322" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every flow that touches a customer parks for your tap first.")}</div>'''

PANELS={"sign1":sign1(),"sign2":sign2(),"sign3":sign3(),"sign4":sign4(),
        "sign5":sign5(),"test":test(),"fix":fix(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/fivesigns"; os.makedirs(outd,exist_ok=True)
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
