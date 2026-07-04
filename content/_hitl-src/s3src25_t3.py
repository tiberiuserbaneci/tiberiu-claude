#!/usr/bin/env python3
# TIER 3 - NEVER RENT ONE BRAIN (s3src25). Vendor lock-in / multi-model routing angle, rebuilt to the
# WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded scene filling a clean rounded card,
# title + one-line caption, NO generic stat-chip strips.
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CAGE - wall/enclosure: your single lit model on the left, a padlocked wall down the middle,
# a greyed 3x3 grid of locked frontier models on the right (walled off).
def cage():
    grid=""
    for r in range(3):
        for c in range(3):
            x=524+c*90; y=104+r*104
            grid+=(f'<rect x="{x}" y="{y}" width="74" height="84" rx="13" fill="rgba(250,250,247,.045)" stroke="rgba(250,250,247,.12)" stroke-width="1.5"/>'
              f'<g transform="translate({x+37},{y+42})" opacity="0.5"><rect x="-11" y="-1" width="22" height="18" rx="4" fill="none" stroke="#7a746a" stroke-width="2.4"/>'
              f'<path d="M-7 -1 V-8 a7 7 0 0 1 14 0 v7" fill="none" stroke="#7a746a" stroke-width="2.4"/></g>')
    bricks="".join(f'<line x1="432" y1="{y}" x2="486" y2="{y}" stroke="rgba(250,250,247,.10)" stroke-width="1.5"/>' for y in range(96,420,34))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Free rents you one brain","WALLED IN")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="c1" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="g1" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        <g filter="url(#g1)"><circle cx="196" cy="222" r="74" fill="url(#c1)"/></g>
        <text x="196" y="216" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">1</text>
        <text x="196" y="240" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">MODEL</text>
        <text x="196" y="336" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".08em" fill="rgb({ACC})">your only one</text>
        <rect x="430" y="66" width="58" height="356" rx="14" fill="#242320" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/>
        {bricks}
        <g transform="translate(459,236)"><rect x="-20" y="-2" width="40" height="34" rx="7" fill="#201d19" stroke="rgb(200,70,35)" stroke-width="3"/>
          <path d="M-13 -2 V-14 a13 13 0 0 1 26 0 v12" fill="none" stroke="rgb(200,70,35)" stroke-width="3"/>
          <circle cx="0" cy="13" r="4" fill="rgb(200,70,35)"/></g>
        {grid}
        <text x="635" y="424" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#7a746a">the frontier, off-limits</text>
      </svg>
      {cap("one vendor hands you a single model and walls off every other one.")}</div>'''

# 2. TAX - IVORY gauge pinned at FLAGSHIP + 3 job rows all stamped the same rate, small ones overpaid
def tax():
    cx,cy,R=160,150,108
    ticks=""
    for i,lab in enumerate(["LITE","SMART","DEEP","FLAG"]):
        a=180-(i*60); x=cx+R*math.cos(math.radians(a)); y=cy-R*math.sin(math.radians(a))
        xo=cx+(R+22)*math.cos(math.radians(a)); yo=cy-(R+22)*math.sin(math.radians(a))
        ticks+=(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{cx+(R-16)*math.cos(math.radians(a)):.0f}" y2="{cy-(R-16)*math.sin(math.radians(a)):.0f}" stroke="rgba(150,90,45,.4)" stroke-width="2.5"/>'
          f'<text x="{xo:.0f}" y="{yo+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#96562d">{lab}</text>')
    na=0  # needle pinned at FLAG (rightmost, a=0)
    nx=cx+(R-26)*math.cos(math.radians(na)); ny=cy-(R-26)*math.sin(math.radians(na))
    rows=[("two-word lookup","overpaid",True),("email draft","overpaid",True),("deep analysis","fair",False)]
    rh=""
    for name,note,over in rows:
        nc="rgb(200,70,35)" if over else "#7a9a6a".replace("#7a9a6a","#96562d")
        rh+=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.16);border-left:4px solid {"rgb(200,70,35)" if over else "#96562d"};border-radius:13px;padding:13px 16px">'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:18px;color:#2a2016">{name}</span>'
          f'<span style="font-family:DM Mono;font-size:11.5px;letter-spacing:.1em;color:#96562d;background:rgba(150,90,45,.12);padding:4px 9px;border-radius:6px">FLAGSHIP</span>'
          f'<span style="font-family:DM Mono;font-size:12px;color:{nc};width:66px;text-align:right">{note}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("One tier taxes every job","FLAT RATE")}
      <div style="display:flex;align-items:center;gap:34px">
        <svg width="340" height="250" viewBox="0 0 340 250" style="flex-shrink:0">
          <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="16" stroke-linecap="round"/>
          <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgb(200,70,35)" stroke-width="16" stroke-linecap="round" stroke-dasharray="{math.pi*R*0.92:.0f} 999"/>
          {ticks}
          <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="5" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="9" fill="#2a2016"/>
          <text x="{cx}" y="{cy+40}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a2016">MAX</text>
          <text x="{cx}" y="{cy+62}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#96562d">no way to turn it down</text>
        </svg>
        <div style="flex:1;display:flex;flex-direction:column;gap:11px">{rh}</div>
      </div>
      {cap("a two-word lookup billed like a deep analysis.","#8a745a")}</div>'''

# 3. ROUTER - one job token routed down 3 provider tier lanes, SMART lane lit/picked
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily work","0.11c",230,True),("DEEP","hard calls","0.40c",364,False)]
    hubx,hy=170,230; lx=470
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C320 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:300px;top:{y-42}px;width:172px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div>'
          f'<div style="font-family:DM Mono;font-size:11px;color:#6f6a60;margin-top:5px">best provider</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It shops every model","PICKS THE TIER")}
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
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">draft 12<br>follow-ups</div>
        {cards}
      </div>
      {cap("each job goes to the cheapest brain across providers that can do it.")}</div>'''

# 4. BENCH - IVORY: isometric stack of warm model-tier cards, every frontier tier on one account
def bench():
    rows=[("LITE","quick lookups","0.02c"),("SMART","daily execution","0.11c"),("DEEP","hard judgement","0.40c")]
    cards=""
    for i,(nm,role,cost) in enumerate(rows):
        y=i*136
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;background:linear-gradient(158deg,#e0b98f,#c99a6d 52%,#a97a52);border:1px solid rgba(255,255,255,.28);border-radius:18px;padding:20px 24px;box-shadow:0 30px 46px rgba(110,70,35,.4), inset 0 2px 3px rgba(255,255,255,.45);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:rgba(42,32,22,.9);display:flex;align-items:center;justify-content:center"><span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba(212,162,127,.9)"></span></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.14em;color:#5a3a1c">{nm}</div><div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#2a1c10">{role}</div></div>'
          f'<div style="flex-shrink:0;text-align:right"><div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#2a1c10;line-height:1">{cost}</div><div style="font-family:DM Mono;font-size:10.5px;letter-spacing:.1em;color:#6e4a28">ON TAP</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 44px 34px">
      {htitle_iv("Every frontier model on tap","ONE ACCOUNT")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:600px;height:440px;position:relative">{cards}
          <div style="position:absolute;left:180px;top:406px;background:#2a1c10;color:#f0e2cf;font-family:DM Sans;font-weight:900;font-size:15px;padding:9px 20px;border-radius:999px;box-shadow:0 12px 24px rgba(110,70,35,.4)">swap any time, no landlord</div></div></div>
      {cap("lite, smart and deep across providers, none of them your landlord.","#8a745a")}</div>'''

# 5. CENTS - compare bars: a locked prepaid year (tall red) vs pay-per-token cents (short warm)
def cents():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Prepay a leash, or pay in cents","CENTS")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><linearGradient id="warm" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#8a4326"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="wg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <line x1="60" y1="360" x2="760" y2="360" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>
        <rect x="150" y="70" width="200" height="290" rx="14" fill="rgba(200,70,35,.18)" stroke="rgb(200,70,35)" stroke-width="2.5"/>
        <text x="250" y="122" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="rgb(200,70,35)">$366</text>
        <text x="250" y="150" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c0705a">per year, locked</text>
        <text x="250" y="250" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#d9cfc8">18 months free,</text>
        <text x="250" y="274" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#d9cfc8">then the meter,</text>
        <text x="250" y="298" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#d9cfc8">one vendor only</text>
        <text x="250" y="392" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="#8f8f85">THE PREPAID PLAN</text>
        <g filter="url(#wg)"><rect x="490" y="280" width="200" height="80" rx="14" fill="url(#warm)"/></g>
        <text x="590" y="322" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#1a0f0a">cents</text>
        <text x="590" y="346" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#2a160c">per job you run</text>
        <text x="590" y="250" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#d9cfc8">pay only for work,</text>
        <text x="590" y="226" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#d9cfc8">every model, no lock</text>
        <text x="590" y="392" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="rgb({ACC})">PAY-PER-TOKEN</text>
      </svg>
      {cap("$366 locked to one vendor, or cents across all of them.")}</div>'''

# 6. MEMORY - radial hub-and-spokes: your owned memory core feeds interchangeable model nodes
def memory():
    cx,cy=210,210
    nodes=[("model",-90,True),("model",-30,False),("model",30,False),("model",90,False),("model",150,False),("model",210,False)]
    lines=""; nd=""
    for i,(nm,a,inuse) in enumerate(nodes):
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        col=f"rgb({ACC})" if inuse else "rgba(212,162,127,.4)"; w=4 if inuse else 2.2
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="{w}"/>'
        rim="rgb("+ACC+")" if inuse else "rgba(255,255,255,.14)"
        tag='<tspan></tspan>' if False else ''
        lbl="in use" if inuse else "ready"
        nd+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="32" fill="#241f1a" stroke="{rim}" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="{"#e6d6c2" if inuse else "#9a9488"}">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+13:.0f}" text-anchor="middle" font-family="DM Mono" font-size="9" fill="{"rgb("+ACC+")" if inuse else "#6f6a60"}">{lbl}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">MEMORY</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">yours</text></svg>
      <div style="flex:1">
        {htitle("Your context, not their hostage","PORTABLE CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing and docs live in one core you own. Change the model, keep the memory.</div>
        {cap("swap the brain around the core. nothing you built gets stranded.")}</div></div>'''

# 7. SWAP - a socket/plug hot-swap: one operator socket, one plug in, alternates ready, swap arc
def swap():
    plugs=""
    for i,y in enumerate((250,318,386)):
        plugs+=(f'<rect x="90" y="{y-22}" width="150" height="44" rx="11" fill="#221f1b" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/>'
          f'<rect x="228" y="{y-9}" width="20" height="18" rx="3" fill="rgba(212,162,127,.4)"/>'
          f'<text x="150" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#9a9488">ready</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Best model this month, not last year","NO LOCK-IN")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="sk" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        <!-- operator socket (right hero) -->
        <rect x="520" y="90" width="230" height="230" rx="34" fill="#2a2623" stroke="rgb({ACC})" stroke-width="2.5"/>
        <text x="635" y="150" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">OPERATOR</text>
        <text x="635" y="176" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">one socket</text>
        <rect x="600" y="196" width="70" height="70" rx="12" fill="#1a1815" stroke="rgba(255,255,255,.12)"/>
        <rect x="618" y="214" width="12" height="34" rx="3" fill="rgb({ACC})"/><rect x="640" y="214" width="12" height="34" rx="3" fill="rgb({ACC})"/>
        <!-- live plug in from left -->
        <g filter="url(#sg)"><circle cx="360" cy="180" r="60" fill="url(#sk)"/></g>
        <text x="360" y="176" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">MODEL</text>
        <text x="360" y="196" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">plugged in</text>
        <path d="M420 180 H600" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>
        <rect x="594" y="171" width="18" height="18" rx="3" fill="rgb({ACC})"/>
        <!-- swap arc -->
        <path d="M360 244 C360 320,150 330,150 250" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="2.5" stroke-dasharray="6 7"/>
        <path d="M150 250 l-8 12 l16 0 Z" fill="rgba(212,162,127,.7)"/>
        {plugs}
        <text x="470" y="418" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#8f8f85">no contract   no expiry   no migration</text>
      </svg>
      {cap("hot-swap the model under one socket. the leash never comes back.")}</div>'''

# 8. OPERATOR - scattered lock-in nodes converge into one glowing owned operator orb
def operator():
    scat=[("every model",70,86),("cents / job",70,196),("no leash",70,306),("your memory",190,142),("one login",190,252)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+60} {y} C360 {y},380 210,520 210" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
          f'<rect x="{x-46}" y="{y-19}" width="132" height="38" rx="11" fill="#221f1b" stroke="rgba(255,255,255,.10)" stroke-width="1.4"/>'
          f'<text x="{x+20}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Own the router, not the rental","ONE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="op" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="opg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#opg)"><circle cx="600" cy="210" r="120" fill="url(#op)"/></g>
        <text x="600" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="600" y="230" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">OPERATOR</text>
        <text x="600" y="366" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">all models   cents   no lock-in</text>
      </svg>
      {cap("one login: every model, cents per job, your memory, no leash.")}</div>'''

PANELS={"cage":cage(),"tax":tax(),"router":router(),"bench":bench(),
        "cents":cents(),"memory":memory(),"swap":swap(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src25"; os.makedirs(outd,exist_ok=True)
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
