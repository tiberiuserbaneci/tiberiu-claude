#!/usr/bin/env python3
# TIER 3 - RESELL THE VOICE AGENT, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Angle: the BUSINESS of reselling voice-AI agents to local shops (Ultron builds+runs them in cents).
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
def htiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. GAP - a missed-call LEDGER: rows of inbound calls, most rung out to voicemail (bookings lost)
def gap():
    rows=[("08:52","New patient booking","MISSED",True),
          ("09:15","Reschedule request","MISSED",True),
          ("09:40","Quote question","answered",False),
          ("10:07","New booking","MISSED",True),
          ("11:22","Appointment change","MISSED",True),
          ("13:04","Walk-in inquiry","answered",False),
          ("14:31","New patient booking","MISSED",True)]
    r=""
    for t,who,st,miss in rows:
        col=f"rgb({RED})" if miss else f"rgb({ACC})"
        r+=(f'<div style="display:flex;align-items:center;gap:16px;padding:12px 18px;border-left:3px solid {col};background:rgba(255,255,255,.02);border-radius:10px;margin-bottom:8px">'
          f'<span style="font-family:DM Mono;font-size:14px;color:#8f8f85;width:50px">{t}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:18px;color:#e6e0d6">{who}</span>'
          f'<span style="font-family:DM Mono;font-size:12.5px;letter-spacing:.08em;color:{col}">{st}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every missed call is money gone","THE GAP")}
      <div style="margin:4px 0 4px">{r}</div>
      <div style="display:flex;align-items:baseline;justify-content:space-between;background:rgba(200,70,35,.10);border:1px solid rgba(200,70,35,.32);border-radius:14px;padding:15px 22px;margin-top:6px">
        <span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">5 of 7 calls hit voicemail</span>
        <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({RED})">$1,900/wk lost</span></div>
      {cap("local shops still book by phone, and the phone keeps ringing out.")}</div>'''

# 2. PROSPECTS - a MAP PIN FIELD: street grid with scattered business pins, the phone-bound ones lit
def market():
    W,H=812,452
    vl="".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="rgba(212,162,127,.06)"/>' for x in range(66,W,84))
    hl="".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="rgba(212,162,127,.06)"/>' for y in range(56,H,78))
    diag=('<path d="M0 360 C240 300,360 200,812 120" fill="none" stroke="rgba(212,162,127,.10)" stroke-width="10"/>'
          '<path d="M150 0 C210 180,300 300,470 452" fill="none" stroke="rgba(212,162,127,.08)" stroke-width="9"/>')
    pins=[(118,96,0),(250,150,1),(176,300,1),(96,392,0),(330,86,1),(300,262,1),(414,186,1),
          (498,120,0),(560,300,1),(474,372,1),(648,96,1),(704,244,0),(626,404,1),(742,346,1),(392,414,1)]
    def pin(x,y,hot):
        if hot:
            return (f'<g filter="url(#pg)"><path d="M{x} {y+8} C{x-19} {y-16},{x-21} {y-40},{x} {y-40} C{x+21} {y-40},{x+19} {y-16},{x} {y+8}Z" fill="rgb({ACC})"/></g>'
              f'<circle cx="{x}" cy="{y-24}" r="7" fill="#241f1a"/>')
        return (f'<path d="M{x} {y+6} C{x-15} {y-14},{x-17} {y-34},{x} {y-34} C{x+17} {y-34},{x+15} {y-14},{x} {y+6}Z" fill="rgba(212,162,127,.20)" stroke="rgba(255,255,255,.10)"/>'
              f'<circle cx="{x}" cy="{y-21}" r="5.5" fill="#241f1a"/>')
    pf="".join(pin(*p) for p in pins)
    tags=('<g><rect x="270" y="150" width="176" height="30" rx="8" fill="#211d19" stroke="rgba(212,162,127,.34)"/>'
          '<text x="286" y="170" font-family="DM Mono" font-size="12.5" fill="#d9d5cc">Dental · books by phone</text></g>'
          '<g><rect x="580" y="300" width="150" height="30" rx="8" fill="#211d19" stroke="rgba(212,162,127,.34)"/>'
          '<text x="596" y="320" font-family="DM Mono" font-size="12.5" fill="#d9d5cc">Salon · no online</text></g>')
    badge=('<g><rect x="536" y="20" width="256" height="42" rx="12" fill="#211d19" stroke="rgba(212,162,127,.3)"/>'
           f'<circle cx="562" cy="41" r="6" fill="rgb({ACC})"/>'
           '<text x="580" y="46" font-family="DM Mono" font-size="14" fill="#FAFAF7" letter-spacing=".04em">31 near you · still on the phone</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Find the shops stuck on the phone","THE PROSPECTS")}
      <svg width="812" height="452" viewBox="0 0 812 452" style="display:block;margin:0 auto">
        <defs><filter id="pg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {vl}{hl}{diag}{pf}{tags}{badge}
      </svg>
      {cap("google maps is a list of clinics, salons and garages drowning in calls.")}</div>'''

# 3. BUILD - IVORY flow: shop brief -> ULTRON core -> a ready voice agent (bezier connectors)
def build():
    con=('<path d="M262 210 C316 210,318 210,372 210" fill="none" stroke="#96562d" stroke-width="4" stroke-dasharray="2 11" stroke-linecap="round"/>'
         '<path d="M486 210 C540 210,542 210,596 210" fill="none" stroke="#96562d" stroke-width="4" stroke-dasharray="2 11" stroke-linecap="round"/>')
    brief=('<g><rect x="40" y="120" width="200" height="182" rx="18" fill="#fbf7ee" stroke="rgba(120,95,60,.28)"/>'
           '<rect x="62" y="146" width="120" height="13" rx="6" fill="#c9b79a"/>'
           +"".join(f'<rect x="62" y="{176+i*26}" width="{w}" height="10" rx="5" fill="rgba(120,95,60,.30)"/>' for i,w in enumerate([156,138,150,118]))+
           '<text x="140" y="292" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#96562d">shop services</text></g>')
    agent=('<g><rect x="600" y="128" width="176" height="164" rx="22" fill="#2a2420" stroke="rgba(212,162,127,.4)"/>'
           '<g transform="translate(662,168)" fill="none" stroke="rgb(212,162,127)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
           '<path d="M6 4 C6 30,26 50,52 50 l0 -14 -14 -6 -8 8 C22 44,12 34,12 26 l8 -8 -6 -14 Z"/>'
           '<rect x="26" y="0" width="34" height="26" rx="7"/><circle cx="36" cy="13" r="2.6" fill="rgb(212,162,127)" stroke="none"/><circle cx="50" cy="13" r="2.6" fill="rgb(212,162,127)" stroke="none"/></g>'
           '<text x="688" y="276" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="rgb(212,162,127)">voice agent · ready</text></g>')
    core=(f'<g filter="url(#ug)"><circle cx="306" cy="210" r="60" fill="url(#uorb)"/></g>'
          '<text x="306" y="205" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">ULTRON</text>'
          '<text x="306" y="226" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">builds it</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htiv("One brief in, a voice agent out","THE BUILD")}
      <svg width="816" height="420" viewBox="0 0 816 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="uorb" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ug" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {con}{brief}{core}{agent}
      </svg>
      {cap("paste their services into ultron, get the agent that answers and books.","#8a745a")}</div>'''

# 4. MARGIN - the reseller economics: tiny cents cost vs a flat monthly retainer, then the margin bar
def margin():
    cost=('<div style="flex:1;background:#221f1b;border:1.5px solid rgba(255,255,255,.09);border-radius:18px;padding:20px 22px">'
          '<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#9a9488">YOU PAY ULTRON</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:46px;color:rgb({ACC});margin-top:6px;line-height:1">6c<span style="font-size:22px;color:#8f8f85"> / call</span></div>'
          '<div style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-top:6px">pay-per-token · about $9/mo of runtime</div></div>')
    rev=('<div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.5);border-radius:18px;padding:20px 22px;box-shadow:0 0 26px rgba(212,162,127,.16)">'
         '<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb(212,162,127)">CLIENT PAYS YOU</div>'
         '<div style="font-family:DM Sans;font-weight:900;font-size:46px;color:#FAFAF7;margin-top:6px;line-height:1">$350<span style="font-size:22px;color:#8f8f85"> / mo</span></div>'
         '<div style="font-family:DM Sans;font-size:15px;color:#c9c3b8;margin-top:6px">flat retainer · billed every month</div></div>')
    bar=('<div style="display:flex;height:52px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.08)">'
         f'<div style="width:4%;background:rgb({RED});display:flex;align-items:center;justify-content:center"></div>'
         f'<div style="flex:1;background:linear-gradient(90deg,#7a4326,rgb({ACC}));display:flex;align-items:center;padding-left:20px;font-family:DM Sans;font-weight:900;font-size:19px;color:#1a0f0a">your margin · about $340 every month, per client</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It runs for cents. You bill monthly.","THE MARGIN")}
      <div style="display:flex;gap:20px;margin-bottom:20px">{cost}{rev}</div>
      <div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.1em;color:#8f8f85;margin-bottom:9px">COST &#183; MARGIN</div>
      {bar}
      {cap("ultron answers each call for cents, the shop pays you a flat retainer.")}</div>'''

# 5. OFFER - IVORY proposal sheet with priced line items + a wax-seal stamp
def offer():
    items=[("Setup and launch","one-time","$500"),
           ("Voice agent, managed","monthly","$350/mo"),
           ("Ultron runtime","your cost","cents"),
           ("You keep","every month","the margin")]
    rows=""
    for i,(a,b,c) in enumerate(items):
        cc="#96562d" if c in ("cents","the margin") else "#2a2016"
        rows+=(f'<div style="display:flex;align-items:baseline;padding:15px 4px;{"border-top:1px solid rgba(120,95,60,.18)" if i else ""}">'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:20px;color:#2a2016">{a}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:#8a745a;margin-right:20px">{b}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:22px;color:{cc};width:120px;text-align:right">{c}</span></div>')
    seal=('<div style="position:absolute;right:34px;bottom:24px;width:104px;height:104px">'
          '<svg width="104" height="104" viewBox="0 0 104 104">'
          '<defs><radialGradient id="wax" cx="38%" cy="32%"><stop offset="0%" stop-color="#d98a5e"/><stop offset="60%" stop-color="#b5522f"/><stop offset="100%" stop-color="#7a3418"/></radialGradient></defs>'
          +"".join(f'<circle cx="52" cy="52" r="46" fill="none" stroke="#a9502c" stroke-width="3" transform="rotate({a} 52 52)" stroke-dasharray="3 5"/>' for a in [0])+
          '<path d="M52 6 '+"".join(f'L{52+46*math.cos(math.radians(k*30)):.0f} {52+46*math.sin(math.radians(k*30)):.0f} L{52+40*math.cos(math.radians(k*30+15)):.0f} {52+40*math.sin(math.radians(k*30+15)):.0f} ' for k in range(12))+'Z" fill="url(#wax)"/>'
          '<circle cx="52" cy="52" r="34" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="1.5"/>'
          '<text x="52" y="49" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#fdeee2">DEAL</text>'
          '<text x="52" y="66" text-anchor="middle" font-family="DM Mono" font-size="9" fill="#f3d8c4" letter-spacing=".1em">SIGNED</text></svg></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;position:relative">
      {htiv("Setup fee, then a monthly retainer","THE OFFER")}
      <div style="background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.18);border-radius:16px;padding:10px 24px;margin-right:120px">{rows}</div>
      {seal}
      {cap("price it like a service, bill every month it answers their phone.","#8a745a")}</div>'''

# 6. ALWAYS ON - a 24-hour radial dial, answered-call ticks all the way around, zero missed
def alwayson():
    cx,cy,R=210,210,168
    ticks=""
    for h in range(24):
        a=math.radians(h*15-90)
        x1=cx+R*math.cos(a); y1=cy+R*math.sin(a)
        x2=cx+(R-22)*math.cos(a); y2=cy+(R-22)*math.sin(a)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.35)" stroke-width="{4 if h%6==0 else 2}"/>'
    blips=""
    for h in range(24):
        a=math.radians(h*15-90); rr=R-42
        x=cx+rr*math.cos(a); y=cy+rr*math.sin(a)
        blips+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="rgb({ACC})" filter="url(#ab)"/>'
    labels="".join(f'<text x="{cx+(R+18)*math.cos(math.radians(h*15-90)):.0f}" y="{cy+(R+18)*math.sin(math.radians(h*15-90))+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{h if h else 24}</text>' for h in (0,6,12,18))
    stat=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px;margin-bottom:14px">'
          '<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7;line-height:1">100%</div>'
          '<div style="font-family:DM Sans;font-size:16px;color:#8f8f85">of calls answered on ring one</div></div>'
          '<div style="display:flex;gap:14px">'
          f'<div style="flex:1;background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.28);border-radius:12px;padding:12px 14px"><div style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">0</div><div style="font-family:DM Mono;font-size:12px;color:#8f8f85">missed</div></div>'
          '<div style="flex:1;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:12px;padding:12px 14px"><div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">24/7</div><div style="font-family:DM Mono;font-size:12px;color:#8f8f85">no breaks</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:28px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><filter id="ab" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.85"/></filter>
        <radialGradient id="ac" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816" stroke="rgba(212,162,127,.1)"/>
        {ticks}{blips}{labels}
        <circle cx="{cx}" cy="{cy}" r="52" fill="url(#ac)"/>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#1a0f0a">24/7</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">always on</text></svg>
      <div style="flex:1">
        {htitle("It answers every hour","ALWAYS ON")}
        {stat}
        {cap("no lunch break, no voicemail, it picks up while the shop sleeps.")}
      </div></div>'''

# 7. STACK - climbing MRR bars, one recurring retainer added each month, up to the headline number
def mrr():
    bars=[("M1",350,"+1"),("M2",900,"+2"),("M3",1600,"+2"),("M4",2500,"+3"),("M5",3400,"+3"),("M6",4500,"+4")]
    maxv=4500.0; bw=104; gap=24; base=372; H=300
    svg=""
    x=44
    for nm,v,add in bars:
        h=H*v/maxv; y=base-h; lit=(nm=="M6")
        fill=f"url(#litbar)" if lit else "url(#bar)"
        svg+=(f'<rect x="{x}" y="{y:.0f}" width="{bw}" height="{h:.0f}" rx="12" fill="{fill}" stroke="{"rgb("+ACC+")" if lit else "rgba(212,162,127,.22)"}" stroke-width="{2 if lit else 1}"/>'
          +("" if lit else f'<text x="{x+bw/2}" y="{y-14:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#d9d5cc">${v:,}</text>')
          f'<text x="{x+bw/2}" y="{base+26}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{nm}</text>'
          f'<text x="{x+bw/2}" y="{base+46}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">{add} client</text>')
        x+=bw+gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Every client is a recurring line","THE STACK")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,.14)"/></linearGradient>
        <linearGradient id="litbar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        <line x1="30" y1="372" x2="800" y2="372" stroke="rgba(255,255,255,.12)"/>
        {svg}
        <text x="770" y="70" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">$4,500/mo</text>
        <text x="770" y="94" text-anchor="end" font-family="DM Mono" font-size="13" fill="#8f8f85">six shops, recurring</text></svg>
      {cap("stack a handful of local shops and the monthly retainers add up fast.")}</div>'''

# 8. PORTFOLIO - hub-and-spokes: you + Ultron at the core, each spoke a live client agent
def portfolio():
    cx,cy=410,222; R=168
    clients=["Dental","Salon","Clinic","Garage","Spa","Vet","Gym","Barber"]
    spokes=""; nodes=""
    n=len(clients)
    for i,name in enumerate(clients):
        a=math.radians(i*(360/n)-90)
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="14" fill="#e6e0d6">{name}</text>'
          f'<g transform="translate({x-16:.0f},{y+8:.0f})"><circle cx="4" cy="4" r="4" fill="rgb({ACC})"/><text x="14" y="8" font-family="DM Mono" font-size="11" fill="#8f8f85">live</text></g>')
    core=(f'<g filter="url(#pog)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#porb)"/></g>'
          f'<text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">YOU +</text>'
          f'<text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ULTRON</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten clients, one dashboard","THE PORTFOLIO")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="porb" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="pog" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}{core}{nodes}
      </svg>
      {cap("ultron runs every agent, you watch the pipeline and collect the retainers.")}</div>'''

PANELS={"gap":gap(),"market":market(),"build":build(),"margin":margin(),
        "offer":offer(),"alwayson":alwayson(),"mrr":mrr(),"portfolio":portfolio()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src47"; os.makedirs(outd,exist_ok=True)
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
