#!/usr/bin/env python3
# TIER 3 - THE TRIAL RUNS OUT, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Adapts an IG growth-hack carousel ("use Claude Opus free via a 30-day trial") into the Ultron
# counter-story: a borrowed trial is a countdown, an operator is permanent - every model routed,
# agents that run the work, cents per token, human-gated, no expiry.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",acc=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{acc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. EXPIRE - a drained countdown gauge: the 30-day trial ring emptied to zero + a spent 30-tick meter
def expire():
    r=150; cx=cy=190; circ=2*math.pi*r
    spent=circ*0.94; rem=circ*0.06
    ticks=""
    tw,tg=14,8; n=30; totalw=n*(tw+tg)-tg; x0=(760-totalw)//2
    for i in range(n):
        x=x0+i*(tw+tg)
        if i>=28:
            ticks+=f'<rect x="{x}" y="0" width="{tw}" height="46" rx="4" fill="rgb({RED})" filter="url(#tk)"/>'
        else:
            ticks+=f'<rect x="{x}" y="12" width="{tw}" height="30" rx="4" fill="rgba(250,250,247,.08)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A free trial is a timer","30-DAY TRIAL")}
      <div style="display:flex;align-items:center;gap:34px">
        <svg width="380" height="380" viewBox="0 0 380 380" style="flex-shrink:0">
          <defs><filter id="rg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({RED})" flood-opacity="0.6"/></filter></defs>
          <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(250,250,247,.07)" stroke-width="26"/>
          <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgb({RED})" stroke-width="26" stroke-linecap="round" stroke-dasharray="{rem:.0f} {circ:.0f}" transform="rotate(-90 {cx} {cy})" filter="url(#rg)"/>
          <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="76" fill="#FAFAF7">0</text>
          <text x="{cx}" y="{cy+34}" text-anchor="middle" font-family="DM Mono" font-size="16" letter-spacing=".18em" fill="rgb({RED})">DAYS LEFT</text>
        </svg>
        <div style="flex:1">
          <div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7;line-height:1.08">Day 31,<br>locked out again.</div>
          <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.42;margin-top:16px">Borrowed frontier access is a loophole with a countdown. The models were never yours.</div>
          <svg width="440" height="58" viewBox="0 0 460 58" style="margin-top:22px">
            <defs><filter id="tk" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({RED})" flood-opacity="0.9"/></filter></defs>
            {ticks}
          </svg>
        </div>
      </div>
      {cap("30 days of somebody else's plan, then back to zero.")}</div>'''

# 2. MODELS - IVORY radial fan: one ROUTER hub, three Claude tiers, the middle picked for the job
def models():
    hubx,huby=160,250
    nodes=[("LITE","Haiku","quick lookups","0.02c",-40,False),
           ("SMART","Sonnet","daily execution","0.11c",0,True),
           ("DEEP","Opus","hard judgement","0.40c",40,False)]
    spokes=""; cards=""; Rr=290
    for nm,mdl,role,cost,ang,on in nodes:
        x=hubx+Rr*math.cos(math.radians(ang)); y=huby+Rr*math.sin(math.radians(ang))
        col="#96562d" if on else "rgba(150,90,45,.32)"; w=5 if on else 2.5
        spokes+=f'<line x1="{hubx+58}" y1="{huby}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="{w}"/>'
        if on:
            bg="linear-gradient(158deg,#e6b48f,#cf8d63)"; bd="#96562d"; ink="#2a1a10"; sub="#4a2f1c"; badge=f'<span style="font-family:DM Mono;font-size:11px;color:#2a1a10;background:rgba(255,255,255,.5);padding:2px 9px;border-radius:20px">picked</span>'
            glow="box-shadow:0 18px 34px rgba(150,90,45,.34)"
        else:
            bg="rgba(255,255,255,.66)"; bd="rgba(150,90,45,.22)"; ink="#4a3f30"; sub="#9a8468"; badge=""; glow="box-shadow:0 10px 22px rgba(120,95,60,.12)"
        cards+=(f'<div style="position:absolute;left:{x-10:.0f}px;top:{y-48:.0f}px;width:220px;background:{bg};border:1.5px solid {bd};border-radius:18px;padding:14px 18px;{glow}">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:{ink}">{nm}</span>{badge}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:23px;color:{ink};margin-top:3px">{mdl} <span style="font-size:16px;font-weight:800;color:{sub}">{cost}</span></div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:{sub}">{role}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("You never pick the model","MODEL ROUTER","#2a2016","#96562d")}
      <div style="position:relative;height:500px">
        <svg width="820" height="500" viewBox="0 0 820 500" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub2" cx="36%" cy="30%"><stop offset="0%" stop-color="#e6b48f"/><stop offset="100%" stop-color="#96562d"/></radialGradient>
          <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgba(150,90,45,.4)"/></filter></defs>
          {spokes}
          <rect x="8" y="{huby-26}" width="70" height="52" rx="12" fill="rgba(150,90,45,.10)" stroke="rgba(150,90,45,.24)"/>
          <text x="43" y="{huby-2}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#7a5836">plain</text>
          <text x="43" y="{huby+14}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#7a5836">english</text>
          <g filter="url(#hg2)"><circle cx="{hubx}" cy="{huby}" r="58" fill="url(#hub2)"/></g>
          <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#fff">ROUTER</text>
          <text x="{hubx}" y="{huby+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        {cards}
      </div>
      {cap("one login, every tier. the cheapest that can actually do the job.","#8a745a")}</div>'''

# 3. NOLIMITS - a dense field of runs, all lit; a tiny dashed corner = where most plans stop
def nolimits():
    cols,rows=42,24; cell,gap=14,4; pitch=cell+gap
    capc,capr=8,5
    dots=""
    for i in range(cols*rows):
        r,c=divmod(i,cols); x=c*pitch; y=r*pitch
        if c<capc and r<capr:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.07)"/>'
        else:
            a=0.5+0.4*((i*37)%5)/4
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(212,162,127,{a:.2f})"/>'
    fw=cols*pitch-gap; fh=rows*pitch-gap
    capw=capc*pitch-gap; caph=capr*pitch-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:50px;color:#FAFAF7">No ceiling</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:12px">on messages</span></div>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">PAY PER TOKEN</span></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        {dots}
        <rect x="-3" y="-3" width="{capw+6}" height="{caph+6}" rx="7" fill="none" stroke="rgb({RED})" stroke-width="2" stroke-dasharray="6 5"/>
        <text x="{capw+16}" y="{caph//2+2}" font-family="DM Mono" font-size="14" fill="rgb({RED})">most plans stop here</text>
      </svg>
      {cap("not throttled by a plan. billed only for the tokens you actually spend.")}</div>'''

# 4. AGENTS - isometric stack of finished agent outputs, delivered overnight, 24/7 chip
def agents():
    rows=[("CORTEX","12 accounts ranked","brief ready"),
          ("SPECTER","9 follow-ups queued","sequence live"),
          ("PULSE","3 posts drafted","in your voice")]
    cards=""
    for i,(ag,work,tag) in enumerate(rows):
        y=i*138
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;padding:20px 24px;box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:54px;height:54px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{ag}</div><div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7">{work}</div></div>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;color:#a8a296;background:rgba(250,250,247,.06);padding:6px 12px;border-radius:20px">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("They run while you sleep","24 / 7")}
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:580px;height:470px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:434px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Delivered by 07:00</div></div></div>
      {cap("seven specialists ship finished work to your vault by morning.")}</div>'''

# 5. ROSTER - org tree: one ROUTER root branching to seven named specialist leaves
def roster():
    leaves=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),
            ("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    xs=[70,185,300,415,530,645,760]
    conns=f'<line x1="415" y1="120" x2="415" y2="182" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/><line x1="{xs[0]}" y1="182" x2="{xs[-1]}" y2="182" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
    chips=""
    for x,(ag,job) in zip(xs,leaves):
        conns+=f'<line x1="{x}" y1="182" x2="{x}" y2="248" stroke="rgba(212,162,127,.35)" stroke-width="2"/>'
        chips+=(f'<rect x="{x-52}" y="248" width="104" height="96" rx="15" fill="#241f1a" stroke="rgba(255,255,255,.11)"/>'
          f'<text x="{x}" y="290" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{ag}</text>'
          f'<text x="{x}" y="316" text-anchor="middle" font-family="DM Mono" font-size="11.5" letter-spacing=".04em" fill="rgb({ACC})">{job}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Type plain English","ONE ROSTER, SEVEN JOBS")}
      <svg width="820" height="380" viewBox="0 0 820 380" style="display:block;margin:0 auto">
        <defs><radialGradient id="rt" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rtg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {conns}
        <g filter="url(#rtg)"><circle cx="415" cy="66" r="52" fill="url(#rt)"/></g>
        <text x="415" y="62" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
        <text x="415" y="82" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">picks one</text>
        {chips}
      </svg>
      {cap("you describe the job. the router hands it to the right specialist.")}</div>'''

# 6. CENTS - IVORY ledger: the stack you cancel billed by the month vs Ultron billed by the token
def cents():
    items=[("Research subscription","$99"),("Outbound tool","$89"),
           ("AI seats, three","$120"),("Content suite","$49")]
    rowsh=""
    for nm,pr in items:
        rowsh+=(f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:13px 4px;border-bottom:1px dotted rgba(150,90,45,.30)">'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:19px;color:#4a3f30">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:18px;color:#7a5836">{pr}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Their stack bills monthly","YOU PAY IN CENTS","#2a2016","#96562d")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1.25">
          {rowsh}
          <div style="display:flex;align-items:baseline;justify-content:space-between;padding:15px 4px 0">
            <span style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({RED})">MONTHLY TOTAL</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:rgb({RED})">$357</span></div>
        </div>
        <div style="flex:1;background:linear-gradient(158deg,#e6b48f,#cf8d63);border-radius:20px;padding:26px 24px;display:flex;flex-direction:column;justify-content:center;box-shadow:0 20px 40px rgba(150,90,45,.30)">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:#2a1a10">ULTRON</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:48px;color:#2a1a10;line-height:1;margin-top:8px">cents</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#3a2416;margin-top:2px">per run</div>
          <div style="font-family:DM Sans;font-size:16px;color:#4a2f1c;margin-top:14px;line-height:1.4">Pay for the tokens you spend. No seats. No month.</div>
        </div>
      </div>
      {cap("cancel four subscriptions. one bill, measured in cents, not seats.","#8a745a")}</div>'''

# 7. GATE - a hold queue: three external actions parked, each awaiting one tap, top one live
def gate():
    q=[("SPECTER","Send 12 cold emails",True),
       ("PULSE","Publish the launch post",False),
       ("COUNSEL","Sign the NDA",False)]
    cards=""
    for ag,act,live in q:
        if live:
            bg="linear-gradient(160deg,#403a33,#241f1a)"; bd=f"rgb({ACC})"; glow="box-shadow:0 0 26px rgba(212,162,127,.28)"
            pill=f'<div style="flex-shrink:0;display:flex;align-items:center;gap:9px;background:rgb({ACC});padding:10px 18px;border-radius:999px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg><span style="font-family:DM Sans;font-weight:900;font-size:15px;color:#1a0f0a">your tap</span></div>'
        else:
            bg="#211e1a"; bd="rgba(255,255,255,.09)"; glow=""
            pill='<span style="flex-shrink:0;font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#8f8f85;background:rgba(250,250,247,.05);padding:9px 16px;border-radius:999px">on hold</span>'
        cards+=(f'<div style="display:flex;align-items:center;gap:20px;background:{bg};border:1.5px solid {bd};border-radius:18px;padding:20px 24px;{glow}">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:13px;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.30);display:flex;align-items:center;justify-content:center"><svg width="22" height="22" viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="9" rx="2" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><path d="M8 11V8a4 4 0 0 1 8 0v3" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({ACC})">{ag}</div><div style="font-family:DM Sans;font-weight:800;font-size:21px;color:#FAFAF7">{act}</div></div>'
          f'{pill}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:18px">
        <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#9a9488">OUTBOUND QUEUE</span>
        <span style="flex:1;height:1px;background:rgba(255,255,255,.10)"></span>
        <span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">3 parked</span></div>
      <div style="display:flex;flex-direction:column;gap:16px">{cards}</div>
      {cap("every external move parks in a queue. you approve, then it moves.")}</div>'''

# 8. HORIZON - line-compare: the trial falls off a cliff at day 30, the operator keeps rising
def horizon():
    x0,x30,x60=90,425,760; ytop,ybase=70,330
    ytrial=140
    grid="".join(f'<line x1="90" y1="{y}" x2="760" y2="{y}" stroke="rgba(250,250,247,.05)"/>' for y in (110,180,250,320))
    xt=f'<line x1="90" y1="{ybase}" x2="760" y2="{ybase}" stroke="rgba(250,250,247,.16)"/>'
    ticks=""
    for x,lb in ((x0,"Day 0"),(x30,"Day 30"),(x60,"Day 60")):
        ticks+=(f'<line x1="{x}" y1="{ybase}" x2="{x}" y2="{ybase+8}" stroke="rgba(250,250,247,.3)"/>'
          f'<text x="{x}" y="{ybase+30}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#8f8f85">{lb}</text>')
    trial=(f'<path d="M{x0} {ytrial} L{x30} {ytrial} L{x30+14} {ybase}" fill="none" stroke="rgb({RED})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
      f'<line x1="{x30+14}" y1="{ybase}" x2="{x60}" y2="{ybase}" stroke="rgb({RED})" stroke-width="3" stroke-dasharray="3 8"/>'
      f'<line x1="{x30}" y1="{ytop}" x2="{x30}" y2="{ybase}" stroke="rgba(200,70,35,.4)" stroke-width="1.5" stroke-dasharray="5 6"/>'
      f'<circle cx="{x30+14}" cy="{ybase}" r="8" fill="rgb({RED})" filter="url(#hf)"/>'
      f'<text x="{x30+26}" y="{ybase-14}" font-family="DM Mono" font-size="13" fill="rgb({RED})">locked out</text>')
    ult=(f'<path d="M{x0} 300 C260 270,420 190,{x60} {ytop+6}" fill="none" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round" filter="url(#hf2)"/>'
      f'<circle cx="{x60}" cy="{ytop+6}" r="8" fill="rgb({ACC})" filter="url(#hf2)"/>'
      f'<text x="{x60-6}" y="{ytop-2}" text-anchor="end" font-family="DM Mono" font-size="13" fill="rgb({ACC})">still compounding</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One expires, one compounds","NO EXPIRY")}
      <svg width="820" height="400" viewBox="0 0 820 400" style="display:block;margin:0 auto">
        <defs><filter id="hf" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({RED})" flood-opacity="0.8"/></filter>
        <filter id="hf2" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        {grid}{xt}{ticks}{trial}{ult}
      </svg>
      <div style="display:flex;gap:28px;margin-top:6px">
        <div style="display:flex;align-items:center;gap:10px"><span style="width:22px;height:4px;border-radius:3px;background:rgb({RED})"></span><span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">Free trial</span></div>
        <div style="display:flex;align-items:center;gap:10px"><span style="width:22px;height:4px;border-radius:3px;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">Ultron operator</span></div>
      </div>
      {cap("a 30-day borrow resets to zero. an operator keeps the memory and the models.")}</div>'''

PANELS={"expire":expire(),"models":models(),"nolimits":nolimits(),"agents":agents(),
        "roster":roster(),"cents":cents(),"gate":gate(),"horizon":horizon()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src07"; os.makedirs(outd,exist_ok=True)
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
