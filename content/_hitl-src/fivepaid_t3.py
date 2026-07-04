#!/usr/bin/env python3
# TIER 3 - THE 5 SKILLS THAT PAY, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# 8 distinct scene types: radar / timeline / voice ring / iso stack / radial hub / gauge / node graph / dot field.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. RESEARCH - radar of live account signals, ranked, feeding a scored brief (CORTEX)
def research():
    cx,cy,R=205,215,185
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (62,124,185))
    blips=[("Raised $4M",120,96),("Hiring 3 ops",300,150),("New CTO",205,165),("Stack swap",35,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    brief=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px"><span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">Northwind Robotics</span>'
      f'<span style="display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:6px 13px;border-radius:11px"><span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#1a0f0a;line-height:1">94</span><span style="font-family:DM Mono;font-size:9px;letter-spacing:.08em;color:rgba(26,15,10,.7)">FIT</span></span></div>'
      '<div style="font-family:DM Sans;font-size:16px;color:#a8a296;line-height:1.4">funded · hiring · no AI layer yet</div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:24px;color:rgb({ACC})">cold call &#8594; retainer</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(62)):.0f} {cy-R*math.cos(math.radians(62)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("Research that closes","ACCOUNT BRIEF")}
        {brief}
        {cap("CORTEX scans funding, hiring, stack - one ranked brief per account, daily.")}
      </div></div>'''

# 2. OUTBOUND - horizontal timeline sequence: one trigger per email, domain stays warm, one reply
def outbound():
    W,H=820,420
    stops=[("EMAIL 1","funding note","Day 1",105,False),("EMAIL 2","new-hire angle","Day 3",300,False),
           ("EMAIL 3","launch nudge","Day 6",495,False),("REPLY","booked a call","Day 9",690,True)]
    line_y=250; cards=""; dots=""; days=""
    for nm,trig,day,x,on in stops:
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "linear-gradient(160deg,#332f2a,#211e1a)"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.10)"
        lab=f"rgb({ACC})" if on else "#9a9488"
        cards+=(f'<foreignObject x="{x-82}" y="60" width="164" height="150">'
          f'<div xmlns="http://www.w3.org/1999/xhtml" style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:16px 16px;height:118px;box-sizing:border-box;box-shadow:0 18px 30px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:{lab}">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:#FAFAF7;margin-top:8px;line-height:1.2">{trig}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:rgb({ACC});margin-top:9px">1 TRIGGER</div>'
          '</div></foreignObject>')
        col="#7fd39a" if on else f"rgb({ACC})"
        dfilt=' filter="url(#rd)"' if on else ''
        dots+=f'<circle cx="{x}" cy="{line_y}" r="11" fill="{col}"{dfilt}/>'
        days+=f'<text x="{x}" y="{line_y+42}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{day}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Outbound that lands","SEQUENCE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><filter id="rd" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#7fd39a" flood-opacity="0.9"/></filter></defs>
        <line x1="70" y1="{line_y}" x2="750" y2="{line_y}" stroke="rgba(212,162,127,.35)" stroke-width="3"/>
        {dots}{cards}{days}
        <rect x="70" y="330" width="680" height="46" rx="12" fill="rgba(127,211,154,.08)" stroke="rgba(127,211,154,.28)"/>
        <text x="94" y="359" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#7fd39a">DOMAIN HEALTH</text>
        <text x="726" y="359" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">99% warm &#183; 0 spam</text>
      </svg>
      {cap("one trigger per email, paced across 9 days - the domain never burns.")}</div>'''

# 3. CONTENT - IVORY voice ring: radial waveform recognition + a sample line in your voice
def content():
    bars=""
    N=44; r0=66;
    for i in range(N):
        a=i*(360/N)
        h=18+abs(math.sin(i*0.9))*30+ (14 if i%5==0 else 0)
        x1=95+r0*math.cos(math.radians(a)); y1=95+r0*math.sin(math.radians(a))
        x2=95+(r0+h)*math.cos(math.radians(a)); y2=95+(r0+h)*math.sin(math.radians(a))
        bars+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#96562d" stroke-width="4" stroke-linecap="round" opacity="{0.5+0.5*(i%3==0)}"/>'
    chips="".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["your cadence","short lines","no hedging"])
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Content in a voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">VOICE, NOT WORDS</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:230px;height:230px;display:flex;align-items:center;justify-content:center">
          <svg width="230" height="230" viewBox="0 0 190 190">{bars}
            <circle cx="95" cy="95" r="58" fill="rgba(150,90,45,.10)" stroke="rgba(150,90,45,.3)" stroke-width="1.5"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#2a2016;line-height:1">2 lines</span>
            <span style="font-family:DM Mono;font-size:11px;letter-spacing:.06em;color:#96562d;margin-top:4px">to recognize you</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4">
            "I killed nine tools last month. The one I kept did not have a chat box."</div>
          <div style="display:flex;gap:22px;margin-top:16px">{chips}</div>
        </div>
      </div>
      {cap("clients ID your handle from the voice - sampled from your real posts.","#8a745a")}</div>'''

# 4. BUILDS - isometric stack: prompt -> landing page -> dashboard -> live URL, same day
def builds():
    steps=[("LANDING PAGE","from one paragraph"),("DASHBOARD","live data, no code"),("SHIPPED","yourco.com is live")]
    cards=""
    for i,(nm,sub) in enumerate(steps):
        y=i*130
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Builds without builders","PLAIN ENGLISH")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:400px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Live &#10003; same day</div></div></div>
      {cap("landing pages and dashboards from a sentence - assembly, not code.")}</div>'''

# 5. SYSTEMS - radial hub: trigger nodes orbit a FLOWS core, one 07:00 digest output
def systems():
    W,H=820,440; cx,cy=330,210; orbit=155
    trig=[("new signal",-90),("form fill",-18),("reply in",54),("threshold",126),("schedule",198)]
    ring=""; nodes=""
    for nm,a in trig:
        x=cx+orbit*math.cos(math.radians(a)); y=cy+orbit*math.sin(math.radians(a))
        ring+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Systems that keep running","TRIGGERS &#8594; DIGEST")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{orbit}" fill="none" stroke="rgba(212,162,127,.14)" stroke-dasharray="3 8"/>
        {ring}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="72" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">FLOWS</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">always on</text>
        <path d="M{cx+orbit+8} {cy} H600" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>
        <rect x="600" y="150" width="196" height="120" rx="20" fill="#201d19" stroke="rgb({ACC})" stroke-width="2"/>
        <text x="698" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">07:00</text>
        <text x="698" y="228" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">DIGEST</text>
      </svg>
      {cap("set the exits once - flows fire on triggers and land a 07:00 digest.")}</div>'''

# 6. ONE - IVORY gauge: 5 ticks, needle deep into ONE, the certificate shelf struck out
def one():
    cx,cy,r=210,215,150
    segs=""
    # 5 segments across the top semicircle, boundaries every 36deg from 180..0
    for i in range(5):
        a0=180-i*36; a1=180-(i+1)*36
        x0=cx+r*math.cos(math.radians(a0)); y0=cy-r*math.sin(math.radians(a0))
        x1=cx+r*math.cos(math.radians(a1)); y1=cy-r*math.sin(math.radians(a1))
        col="#96562d" if i==0 else "rgba(150,90,45,.18)"
        segs+=f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{col}" stroke-width="20" stroke-linecap="butt"/>'
    na=180-18  # needle into segment 1 (deep)
    nx=cx+(r-34)*math.cos(math.radians(na)); ny=cy-(r-34)*math.sin(math.radians(na))
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:8px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Pick exactly one</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">GO DEEP</span></div>
      <div style="display:flex;align-items:center;gap:20px">
        <svg width="420" height="260" viewBox="0 0 420 260">
          {segs}
          <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#2a2016" stroke-width="7" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="13" fill="#2a2016"/>
          <text x="{cx}" y="{cy+42}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a2016">1 skill, daily</text>
          <text x="{cx-r+8}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#96562d">DEEP</text>
          <text x="{cx+r-8}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a08a68">shallow</text>
        </svg>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:16px 18px;margin-bottom:14px">
            <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#2a2016;line-height:1">1 run daily</div>
            <div style="font-family:DM Sans;font-size:16px;color:#5a4634;margin-top:3px">beats every alternative</div></div>
          <div style="background:rgba(200,70,35,.06);border-left:4px solid rgba(200,70,35,.6);border-radius:12px;padding:16px 18px">
            <div style="font-family:DM Sans;font-weight:800;font-size:24px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7);line-height:1">5 certificates</div>
            <div style="font-family:DM Sans;font-size:16px;color:#8a745a;margin-top:3px">on a shelf</div></div>
        </div>
      </div>
      {cap("one skill run daily inside Ultron compounds - depth is what sells.","#8a745a")}</div>'''

# 7. CLIENT - node graph: your own company at the core, its receipts converge into the pitch
def client():
    W,H=820,430
    rec=[("brief",70,74),("sequence",70,178),("page",70,282),("flow",70,356)]
    cx,cy=400,215; px=700
    edges=""; nodes=""
    for nm,x,y in rec:
        mx=(x+cx)/2
        edges+=f'<path d="M{x+58} {y} C{mx:.0f} {y},{mx:.0f} {cy},{cx-70} {cy}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.2"/>'
        nodes+=(f'<rect x="{x-20}" y="{y-24}" width="128" height="48" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x+44}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Your first client is you","RECEIPTS = PITCH")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="co" cx="38%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="78" fill="url(#co)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">YOUR</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">COMPANY</text>
        <path d="M{cx+80} {cy} H{px-72}" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>
        <circle cx="{px}" cy="{cy}" r="66" fill="#201d19" stroke="rgb({ACC})" stroke-width="2"/>
        <text x="{px}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">THE</text>
        <text x="{px}" y="{cy+22}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">PITCH</text>
      </svg>
      {cap("run the skill on your own business first - the results become the resume.")}</div>'''

# 8. METER - dot field of token cost (a few cents lit) against the invoice you send
def meter():
    cols,rowsn=34,18
    lit={41,88,142,205,266,331,410}
    dots=""; cell=13; gap=4
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="flex:1">
        {htitle("Cents to practice","THE MATH")}
        <div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:16px 20px;margin-bottom:14px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#8f8f85">METER WHILE YOU LEARN</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:rgb({ACC});line-height:1.1">3.4c</div></div>
        <div style="background:#211d19;border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:16px 20px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#8f8f85">INVOICE WHEN YOU DELIVER</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7;line-height:1.1">$2,500</div></div>
        {cap("the token meter runs in cents. the invoice does not.")}
      </div></div>'''

PANELS={"research":research(),"outbound":outbound(),"content":content(),"builds":builds(),
        "systems":systems(),"one":one(),"client":client(),"meter":meter()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/fivepaid"; os.makedirs(outd,exist_ok=True)
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
