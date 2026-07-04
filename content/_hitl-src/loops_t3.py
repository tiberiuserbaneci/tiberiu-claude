#!/usr/bin/env python3
# TIER 3 - PROMPTS ARE DEAD, LOOPS RUN, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO generic
# stat-chip strips. Clean rounded cards only (no clip-path, no side-walls). Cost zero.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. OLDWAY - a CRON CLOCK DIAL: the human is the tick. 4 manual tasks on the face, a hand you swing.
def oldway():
    cx,cy,R=306,236,184
    ticks=""
    for a in range(0,360,30):
        rad=math.radians(a-90)
        x1=cx+(R-3)*math.cos(rad); y1=cy+(R-3)*math.sin(rad)
        x2=cx+(R-20)*math.cos(rad); y2=cy+(R-20)*math.sin(rad)
        major=(a%90==0)
        col=f"rgb({ACC})" if major else "rgba(212,162,127,.32)"
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{4 if major else 2}" stroke-linecap="round"/>'
    labels=""
    for nm,a in [("SEND",0),("REPLY",90),("POST",180),("REPORT",270)]:
        rad=math.radians(a-90); lx=cx+(R-88)*math.cos(rad); ly=cy+(R-88)*math.sin(rad)
        dy=26 if a==180 else (-16 if a==0 else 5)
        labels+=f'<text x="{lx:.0f}" y="{ly+dy:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#b7b1a4">{nm}</text>'
    hr=math.radians(52-90); hx=cx+128*math.cos(hr); hy=cy+128*math.sin(hr)
    pr=math.radians(52); px=cx+9*math.cos(pr); py=cy+9*math.sin(pr); nr=math.radians(52+180)
    nx=cx+9*math.cos(nr); ny=cy+9*math.sin(nr)
    hand=(f'<polygon points="{px:.0f},{py:.0f} {nx:.0f},{ny:.0f} {hx:.0f},{hy:.0f}" fill="rgb({ACC})"/>'
          f'<circle cx="{hx:.0f}" cy="{hy:.0f}" r="10" fill="rgb({ACC})" filter="url(#hglow)"/>'
          f'<text x="{hx+2:.0f}" y="{hy-20:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="rgb({RED})">YOU FIRE IT</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You are a human cron job","MANUAL &middot; 24/7")}
      <svg width="612" height="480" viewBox="0 0 612 480" style="display:block;margin:0 auto">
        <defs><filter id="hglow" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816" stroke="rgba(212,162,127,.22)" stroke-width="2"/>
        {ticks}{labels}{hand}
        <circle cx="{cx}" cy="{cy}" r="40" fill="#221f1b" stroke="rgba(212,162,127,.4)" stroke-width="2"/>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="rgb({ACC})">YOU</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">the tick</text>
      </svg>
      {cap("each task waits for you to fire it. one prompt, one output, all day.")}</div>'''

# 2. LOOP - a CYCLE RING: goal -> run -> check flowing clockwise, an exit branch, 212 in the core.
def loop():
    cx,cy,rr=306,238,152
    nodes=[("GOAL",0),("RUN",120),("CHECK",240)]
    pos={}
    for nm,a in nodes:
        rad=math.radians(a-90); pos[nm]=(cx+rr*math.cos(rad),cy+rr*math.sin(rad))
    arcs=""
    seq=["GOAL","RUN","CHECK","GOAL"]; ang={"GOAL":0,"RUN":120,"CHECK":240}
    for i in range(3):
        a0=ang[seq[i]]+30; a1=ang[seq[i+1]]-30
        r0=math.radians(a0-90); r1=math.radians(a1-90)
        x0=cx+rr*math.cos(r0); y0=cy+rr*math.sin(r0); x1=cx+rr*math.cos(r1); y1=cy+rr*math.sin(r1)
        arcs+=f'<path d="M{x0:.0f} {y0:.0f} A{rr} {rr} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="4" marker-end="url(#ah)"/>'
    nds=""
    for nm,a in nodes:
        x,y=pos[nm]
        nds+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="47" fill="#231f1b" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
              f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#e6dccf">{nm}</text>')
    ex,ey=pos["CHECK"]; erad=math.radians(240-90)
    ox=ex+120*math.cos(erad); oy=ey+120*math.sin(erad)
    exitb=(f'<path d="M{ex:.0f} {ey:.0f} L{ox:.0f} {oy:.0f}" stroke="rgba(212,162,127,.55)" stroke-width="3" stroke-dasharray="3 8" marker-end="url(#ah)"/>'
           f'<rect x="{ox-66:.0f}" y="{oy-24:.0f}" width="132" height="48" rx="14" fill="#201d19" stroke="rgb({ACC})" stroke-width="1.6"/>'
           f'<text x="{ox:.0f}" y="{oy+6:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".12em" fill="rgb({ACC})">EXIT &#10003;</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A flow that runs until done","GOAL &middot; CHECK &middot; EXIT")}
      <svg width="612" height="486" viewBox="0 0 612 486" style="display:block;margin:0 auto">
        <defs><marker id="ah" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="rgb({ACC})"/></marker>
        <radialGradient id="core" cx="40%" cy="34%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1a1714"/></radialGradient></defs>
        {arcs}{exitb}{nds}
        <circle cx="{cx}" cy="{cy}" r="80" fill="url(#core)" stroke="rgba(212,162,127,.3)" stroke-width="1.5"/>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="52" fill="rgb({ACC})">212</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#b7b1a4">CYCLES RAN</text>
        <text x="{cx}" y="{cy+44}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">3 sentences in</text>
      </svg>
      {cap("a goal, a checker and an exit. it cycles on its own until the job is done.")}</div>'''

# 3. DEFINE - IVORY: one typed sentence compiling into a 3-step flow blueprint.
def define():
    steps=[("01","WATCH","every new lead"),("02","WAIT","quiet 3 days"),("03","FOLLOW UP","one nudge, sent")]
    cards=""
    for i,(n,t,s) in enumerate(steps):
        arrow='<div style="display:flex;align-items:center;color:#96562d;font-size:26px;font-weight:700;padding:0 4px">&rarr;</div>' if i else ''
        cards+=(arrow+f'<div style="flex:1;background:rgba(255,255,255,.62);border:1px solid rgba(150,120,80,.24);border-radius:16px;padding:16px 16px 18px;box-shadow:0 8px 18px rgba(120,95,60,.12)">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#96562d">{n}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016;margin-top:6px">{t}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#7a674f;margin-top:2px">{s}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("One sentence, one flow","COMPILED")}
      <div style="background:#fffdf9;border:1px solid rgba(150,120,80,.28);border-left:5px solid #96562d;border-radius:14px;padding:20px 24px;display:flex;align-items:center;gap:18px;box-shadow:0 10px 24px rgba(120,95,60,.12)">
        <span style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#96562d;background:rgba(150,90,45,.1);padding:6px 12px;border-radius:999px">1 SENTENCE</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:22px;color:#2a2016;line-height:1.35">"Follow up every lead that goes quiet for 3 days."</span></div>
      <div style="text-align:center;font-size:30px;color:#96562d;line-height:1;margin:12px 0 14px">&darr;</div>
      <div style="display:flex;align-items:stretch;gap:6px">{cards}</div>
      {cap("you describe the outcome in plain English. the flow is built for you.","#8a745a")}</div>'''

# 4. TRIGGER - a bolt-rail: 3 emitters firing lightning into one FLOW that runs itself.
def trigger():
    W,H=820,432
    rows=[("DAILY 09:00","clock, every morning",84,"clock"),
          ("ON REPLY","a lead answers",216,"reply"),
          ("USAGE DROP","account goes quiet",348,"drop")]
    ICON={
      "clock":'<circle cx="0" cy="0" r="17" fill="none" stroke="rgb({A})" stroke-width="3"/><line x1="0" y1="0" x2="0" y2="-10" stroke="rgb({A})" stroke-width="3" stroke-linecap="round"/><line x1="0" y1="0" x2="8" y2="4" stroke="rgb({A})" stroke-width="3" stroke-linecap="round"/>',
      "reply":'<path d="M-16 -10 h30 a3 3 0 0 1 3 3 v14 a3 3 0 0 1 -3 3 h-20 l-10 8 v-8 a3 3 0 0 1 -3 -3 v-14 a3 3 0 0 1 3 -3Z" fill="none" stroke="rgb({A})" stroke-width="2.6"/>',
      "drop":'<path d="M-16 -12 L-6 -2 L2 -8 L16 8" fill="none" stroke="rgb({A})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M16 8 L16 -2 M16 8 L6 8" fill="none" stroke="rgb({A})" stroke-width="3" stroke-linecap="round"/>',
    }
    tiles=""; bolts=""
    hubx,huby=692,216
    for lab,sub,y,ic in rows:
        tiles+=(f'<rect x="20" y="{y-46}" width="330" height="92" rx="18" fill="url(#tile)" stroke="rgba(255,255,255,.1)"/>'
          f'<g transform="translate(64,{y})">{ICON[ic].replace("{A}",ACC)}</g>'
          f'<text x="104" y="{y-6}" font-family="DM Mono" font-size="17" letter-spacing=".08em" fill="#eae4d8">{lab}</text>'
          f'<text x="104" y="{y+18}" font-family="DM Sans" font-size="15" fill="#8f8f85">{sub}</text>')
        my=(y+huby)/2
        bolts+=(f'<polyline points="356,{y} 430,{y} 470,{my:.0f} 540,{my:.0f} 604,{huby}" fill="none" '
                f'stroke="rgb({ACC})" stroke-width="3.5" stroke-linejoin="round" filter="url(#bg)" opacity="0.9"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It fires without me","3 TRIGGERS LIVE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <radialGradient id="orb" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="bg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter>
          <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {bolts}{tiles}
        <g filter="url(#og)"><circle cx="{hubx}" cy="{huby}" r="80" fill="url(#orb)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">FLOW</text>
        <text x="{hubx}" y="{huby+22}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#3a2010">runs itself</text>
      </svg>
      {cap("daily 09:00, on every reply, on a usage drop - it fires with no reminder.")}</div>'''

# 5. VERIFY - IVORY grader: a report card that checks itself, one fail loops back to rerun.
def verify():
    rows=[("Tone matches your posts",True),("Links resolve (200 OK)",True),("No banned words",True),("Under 470 words",False)]
    lines=""
    for lab,ok in rows:
        if ok:
            mark=f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
            col="#2a2016"
        else:
            mark=f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({RED})" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
            col=f"rgb({RED})"
        lines+=(f'<div style="display:flex;align-items:center;gap:14px;padding:14px 4px;border-bottom:1px solid rgba(150,120,80,.16)">'
          f'<span style="flex-shrink:0">{mark}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:19px;color:{col}">{lab}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("It grades its own work","SELF-CHECK")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1;background:rgba(255,255,255,.58);border:1px solid rgba(150,120,80,.22);border-radius:18px;padding:8px 22px;box-shadow:0 10px 22px rgba(120,95,60,.1)">{lines}</div>
        <div style="flex-shrink:0;width:214px;display:flex;flex-direction:column;gap:16px">
          <div style="background:#fffdf9;border:1px solid rgba(150,120,80,.26);border-radius:18px;padding:20px;text-align:center;box-shadow:0 10px 22px rgba(120,95,60,.1)">
            <div style="font-family:DM Sans;font-weight:900;font-size:46px;color:#2a2016;line-height:1">47<span style="font-size:24px;color:#96562d">/50</span></div>
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#96562d;margin-top:2px">RUBRIC SCORE</div></div>
          <div style="background:rgba(150,90,45,.1);border:1px solid rgba(150,90,45,.3);border-radius:18px;padding:18px 20px;display:flex;align-items:center;gap:12px">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4v6h6M20 20v-6h-6"/><path d="M4 10a8 8 0 0 1 14-4M20 14a8 8 0 0 1-14 4"/></svg>
            <div><div style="font-family:DM Sans;font-weight:900;font-size:18px;color:#2a2016">1 fail</div>
            <div style="font-family:DM Mono;font-size:12px;color:#96562d">retries, not ships</div></div></div>
        </div>
      </div>
      {cap("every cycle grades the result before I see it. a fail reruns, it does not repeat.","#8a745a")}</div>'''

# 6. TRAP - two drain meters: an exit-less loop bleeds to empty vs an Ultron-capped loop that stops.
def trap():
    W,H=820,430
    def meter(x,title,sub,col,fill_top,capline,badge):
        bx=x; by=70; bw=150; bh=300
        body=(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="20" fill="#1a1714" stroke="rgba(255,255,255,.1)"/>'
              f'<rect x="{bx+6}" y="{fill_top}" width="{bw-12}" height="{by+bh-6-fill_top}" rx="14" fill="{col}" opacity="0.9"/>')
        if capline:
            body+=(f'<line x1="{bx-10}" y1="{capline}" x2="{bx+bw+10}" y2="{capline}" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round"/>'
                   f'<text x="{bx+bw+18}" y="{capline+5}" font-family="DM Mono" font-size="13" fill="rgb({ACC})">CAP 500</text>')
        else:
            body+=(f'<path d="M{bx+bw/2-14} {by-6} L{bx+bw/2} {by-30} L{bx+bw/2+14} {by-6}" fill="none" stroke="rgb({RED})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
                   f'<text x="{bx+bw/2:.0f}" y="{by-40}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="rgb({RED})">&infin;</text>')
        return (body+f'<text x="{bx+bw/2:.0f}" y="{by+bh+34}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="{badge}">{title}</text>'
                f'<text x="{bx+bw/2:.0f}" y="{by+bh+58}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{sub}</text>')
    left=meter(120,"NO EXIT","runs till empty",f"rgb({RED})",76,None,f"rgb({RED})")
    right=meter(540,"ULTRON CAP","stops on its own",f"rgb({ACC})",188,258,"#e6dccf")
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Loops without exits eat budgets","EXIT REQUIRED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        {left}{right}
        <text x="410" y="205" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#5a544a">VS</text>
        <circle cx="410" cy="245" r="30" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>
        <path d="M398 245 a12 12 0 1 1 4 9" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round"/>
        <rect x="404" y="238" width="12" height="12" rx="3" fill="rgb({ACC})"/>
      </svg>
      {cap("a loop with no exit spends while you sleep. Ultron caps every flow at a ceiling.")}</div>'''

# 7. GATE - a speedometer at FULL for internal work, a handbrake HOLD gate on every external move.
def gate():
    scx,scy,sR=228,300,150
    ticks=""
    for i in range(11):
        a=180-i*18; rad=math.radians(a)
        x1=scx+(sR)*math.cos(rad); y1=scy-(sR)*math.sin(rad)
        x2=scx+(sR-18)*math.cos(rad); y2=scy-(sR-18)*math.sin(rad)
        lit=i>=8
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{f"rgb({ACC})" if lit else "rgba(212,162,127,.3)"}" stroke-width="{4 if lit else 2.5}" stroke-linecap="round"/>'
    na=math.radians(16); nx=scx+(sR-30)*math.cos(na); ny=scy-(sR-30)*math.sin(na)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Full speed inside. Brakes on the door.","POWER, HELD")}
      <svg width="820" height="410" viewBox="0 0 820 410" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ng" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter>
        <marker id="ah2" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="rgb({ACC})"/></marker></defs>
        <path d="M{scx-sR} {scy} A{sR} {sR} 0 0 1 {scx+sR} {scy}" fill="none" stroke="#1a1714" stroke-width="30"/>
        {ticks}
        <line x1="{scx}" y1="{scy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{scx}" cy="{scy}" r="16" fill="url(#hub)"/>
        <text x="{scx}" y="{scy-52}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">FULL</text>
        <text x="{scx}" y="{scy+40}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">internal work</text>
        <path d="M420 210 H520" stroke="rgba(212,162,127,.5)" stroke-width="4" stroke-dasharray="3 10" stroke-linecap="round" marker-end="url(#ah2)"/>
        <text x="470" y="192" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">external move</text>
        <rect x="560" y="118" width="184" height="184" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(624,166)"><rect x="0" y="42" width="56" height="44" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 42 V29 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="652" y="284" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">HOLD</text>
        <text x="652" y="336" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">waits for your tap</text>
      </svg>
      {cap("internal cycles run flat out. every external move parks on HOLD until you tap.")}</div>'''

# 8. SCALE - diverging line chart: your hours stay flat, your systems climb to 212.
def scale():
    x0,x1,yt,yb=96,748,66,320
    xs=[x0+i*(x1-x0)/5 for i in range(6)]
    sys_y=[300,286,252,198,128,72]
    hrs_y=[314,312,315,313,314,312]
    grid="".join(f'<line x1="{x0}" y1="{yt+i*(yb-yt)/4:.0f}" x2="{x1}" y2="{yt+i*(yb-yt)/4:.0f}" stroke="rgba(255,255,255,.06)"/>' for i in range(5))
    days="".join(f'<text x="{xs[i]:.0f}" y="{yb+26:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">wk{i+1}</text>' for i in range(6))
    syspts=" ".join(f"{xs[i]:.0f},{sys_y[i]}" for i in range(6))
    hrspts=" ".join(f"{xs[i]:.0f},{hrs_y[i]}" for i in range(6))
    area=f"M{xs[0]:.0f},{yb} "+" ".join(f"L{xs[i]:.0f},{sys_y[i]}" for i in range(6))+f" L{xs[5]:.0f},{yb} Z"
    dots="".join(f'<circle cx="{xs[i]:.0f}" cy="{sys_y[i]}" r="4.5" fill="rgb({ACC})"/>' for i in range(6))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("My hours stopped scaling","LAST WEEK")}
      <svg width="820" height="392" viewBox="0 0 820 392" style="display:block;margin:0 auto">
        <defs><linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.32)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
        <filter id="eg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {grid}
        <line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="rgba(255,255,255,.14)"/>
        {days}
        <path d="{area}" fill="url(#fill)"/>
        <polyline points="{hrspts}" fill="none" stroke="#8a7a63" stroke-width="3.5" stroke-dasharray="6 6" stroke-linecap="round"/>
        <polyline points="{syspts}" fill="none" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
        {dots}
        <circle cx="{xs[5]:.0f}" cy="{sys_y[5]}" r="9" fill="rgb({ACC})" filter="url(#eg)"/>
        <text x="{xs[5]-10:.0f}" y="{sys_y[5]-16}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="24" fill="rgb({ACC})">212</text>
        <text x="{xs[5]-10:.0f}" y="{sys_y[5]+2}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#b7b1a4">cycles</text>
        <text x="{x0+8}" y="{hrs_y[0]-14}" font-family="DM Mono" font-size="13" fill="#8a7a63">your hours &middot; flat</text>
        <g transform="translate({x0+6},{yt+2})">
          <rect x="0" y="0" width="210" height="34" rx="10" fill="#201d19" stroke="rgba(212,162,127,.28)"/>
          <text x="14" y="22" font-family="DM Sans" font-weight="800" font-size="15" fill="#e6dccf">9 flows</text>
          <text x="200" y="22" text-anchor="end" font-family="DM Mono" font-size="13" fill="rgb({ACC})">3 sentences typed</text></g>
      </svg>
      {cap("nine flows ran 212 cycles last week. you typed three sentences.")}</div>'''

PANELS={"oldway":oldway(),"loop":loop(),"define":define(),"trigger":trigger(),
        "verify":verify(),"trap":trap(),"gate":gate(),"scale":scale()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/loops"; os.makedirs(outd,exist_ok=True)
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
