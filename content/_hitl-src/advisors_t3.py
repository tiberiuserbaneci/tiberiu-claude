#!/usr/bin/env python3
# TIER 3 - THE BOARD OF ADVISORS, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CONTEXT - a balance scale: light "generic advice" pan (struck) rises, heavy "your context" pan sinks
def context():
    apex=(410,158); L_end=(168,124); R_end=(652,192)
    ghost=('<g opacity="0.72">'
      '<line x1="168" y1="124" x2="150" y2="248" stroke="rgba(255,255,255,.22)" stroke-width="1.6"/>'
      '<line x1="168" y1="124" x2="186" y2="248" stroke="rgba(255,255,255,.22)" stroke-width="1.6"/>'
      '<path d="M110 248 Q168 292 226 248" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="2"/>'
      '<rect x="74" y="286" width="188" height="74" rx="14" fill="rgba(250,250,247,.03)" stroke="rgba(250,250,247,.16)" stroke-width="1.5" stroke-dasharray="6 6"/>'
      '<text x="168" y="320" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#8f8f85">generic advice</text>'
      f'<line x1="92" y1="356" x2="244" y2="290" stroke="rgb({RED})" stroke-width="2.6" stroke-linecap="round"/>'
      f'<text x="168" y="382" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({RED})">cheap · ignored</text></g>')
    chips=""
    for i,(nm,val) in enumerate([("DEALS","47 open"),("CLIENTS","112 named"),("CASH","runway 9mo")]):
        y=306+i*44
        chips+=(f'<g><rect x="556" y="{y}" width="192" height="36" rx="9" fill="url(#hv)" stroke="rgba(212,162,127,.4)"/>'
          f'<text x="572" y="{y+24}" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">{nm}</text>'
          f'<text x="732" y="{y+24}" text-anchor="end" font-family="DM Sans" font-weight="700" font-size="15" fill="#eae4d8">{val}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Advice is cheap. Context is not.","WHY IT FAILS")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="hv" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352e"/><stop offset="100%" stop-color="#241f1a"/></linearGradient>
          <filter id="pv" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter>
        </defs>
        <rect x="396" y="158" width="28" height="252" rx="6" fill="url(#hv)"/>
        <path d="M356 410 H464 L438 372 H382 Z" fill="#211e1a" stroke="rgba(255,255,255,.08)"/>
        {ghost}
        <g filter="url(#pv)">
          <line x1="{R_end[0]}" y1="{R_end[1]}" x2="626" y2="300" stroke="rgba(212,162,127,.55)" stroke-width="1.8"/>
          <line x1="{R_end[0]}" y1="{R_end[1]}" x2="678" y2="300" stroke="rgba(212,162,127,.55)" stroke-width="1.8"/>
          <path d="M556 300 Q652 348 748 300" fill="none" stroke="rgb({ACC})" stroke-width="2.5"/>
        </g>
        <line x1="{L_end[0]}" y1="{L_end[1]}" x2="{R_end[0]}" y2="{R_end[1]}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round"/>
        <circle cx="{apex[0]}" cy="{apex[1]}" r="12" fill="rgb({ACC})"/>
        <circle cx="{apex[0]}" cy="{apex[1]}" r="4" fill="#1a0f0a"/>
        {chips}
      </svg>
      {cap("generic advice ignores your deals, your clients, your cash. yours weighs it.")}</div>'''

# 2. THREE - triangular constellation: 3 advisor lenses around a YOU core (IVORY)
def three():
    cx,cy,R=306,232,158
    who=[("PRICER","margins",-90),("EDITOR","clarity",150),("STRATEGIST","doors",30)]
    lines=""; nodes=""
    pts=[]
    for nm,lens,a in who:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a)); pts.append((x,y))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.34)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="52" fill="#fbf7f0" stroke="#96562d" stroke-width="2.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="52" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="8"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#2a2016">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#96562d">{lens}</text>')
    arcs=""
    for i in range(3):
        (x1,y1),(x2,y2)=pts[i],pts[(i+1)%3]
        mx,my=(x1+x2)/2,(y1+y2)/2; bx,by=mx+(mx-cx)*0.16,my+(my-cy)*0.16
        arcs+=f'<path d="M{x1:.0f} {y1:.0f} Q{bx:.0f} {by:.0f} {x2:.0f} {y2:.0f}" fill="none" stroke="rgba(150,90,45,.22)" stroke-width="1.6" stroke-dasharray="2 8"/>'
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("Three advisors, three lenses.","THE BOARD","#2a2016","#96562d")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        {arcs}{lines}
        <circle cx="{cx}" cy="{cy}" r="44" fill="#96562d"/>
        <circle cx="{cx}" cy="{cy}" r="44" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="1.5"/>
        <text x="{cx}" y="{cy+7}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#fbf7f0">YOU</text>
        {nodes}
      </svg>
      {cap("the pricer, the editor, the strategist - each a skill, each on call.","#8a745a")}</div>'''

# 3. BOOKS - isometric stack of your ledgers, all reading from one memory
def books():
    ledgers=[("DEALS","47 open · $612k pipe",0),("CLIENTS","112 named accounts",1),("NUMBERS","MRR $84k · CAC $310",2)]
    def rows(): return "".join(f'<div style="width:{w}px;height:4px;border-radius:2px;background:rgba(250,250,247,.20)"></div>' for w in (120,96,132))
    cards=""
    for nm,sub,i in ledgers:
        y=i*132
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:16px;padding:20px 24px 20px 30px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:22px">'
          f'<div style="position:absolute;left:0;top:0;bottom:0;width:12px;border-radius:16px 0 0 16px;background:linear-gradient(180deg,rgb({ACC}),#7a4326)"></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.14em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#FAFAF7;margin-top:2px">{sub}</div></div>'
          f'<div style="display:flex;flex-direction:column;gap:5px">{rows()}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("They read your books.","ONE MEMORY")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:560px;height:436px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:404px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:15px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">wired to one memory core</div></div></div>
      {cap("deals, clients, numbers - they advise on your data, not a generic playbook.")}</div>'''

# 4. PRICER - semicircular margin gauge + verdict + a floor-vs-recommended bar pair
def pricer():
    cx,cy,R=210,262,168
    def pt(frac,rad):
        a=math.radians(180-frac*180); return (cx+rad*math.cos(a),cy-rad*math.sin(a))
    need=pt(0.74,R-18); tickstr=""
    for f in (0,.25,.5,.75,1):
        a,b=pt(f,R),pt(f,R-16); tickstr+=f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="rgba(255,255,255,.22)" stroke-width="2"/>'
    aL=pt(0,R); aM=pt(0.5,R); aR=pt(1,R)
    bars=""
    for nm,val,w,warm in [("Your floor","$6.5k",188,False),("Repriced","$9.0k",286,True)]:
        col=f"rgb({ACC})" if warm else "rgba(250,250,247,.16)"
        tc="#FAFAF7" if warm else "#9a9488"
        bars+=(f'<div style="margin-bottom:16px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:7px">'
          f'<span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">{nm}</span><span style="font-family:DM Sans;font-weight:900;font-size:22px;color:{tc}">{val}</span></div>'
          f'<div style="height:16px;border-radius:8px;background:rgba(255,255,255,.05);overflow:hidden"><div style="width:{w}px;height:100%;border-radius:8px;background:{col}"></div></div></div>')
    gauge=f'''<svg width="430" height="330" viewBox="0 0 430 330" style="flex-shrink:0">
        <defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#4a4038"/><stop offset="60%" stop-color="#9a7a4a"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="ng" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <path d="M{aL[0]:.0f} {aL[1]:.0f} A{R} {R} 0 0 1 {aR[0]:.0f} {aR[1]:.0f}" fill="none" stroke="url(#ga)" stroke-width="22" stroke-linecap="round"/>
        {tickstr}
        <line x1="{cx}" y1="{cy}" x2="{need[0]:.0f}" y2="{need[1]:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="13" fill="rgb({ACC})"/><circle cx="{cx}" cy="{cy}" r="5" fill="#1a0f0a"/>
        <text x="{cx-R+6:.0f}" y="{cy+26:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">LOW</text>
        <text x="{cx+R-6:.0f}" y="{cy+26:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">FAIR</text>
        <text x="{cx:.0f}" y="{cy-14:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">RAISE</text>
      </svg>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It ran the numbers: raise.","UNIT ECONOMICS")}
      <div style="display:flex;align-items:center;gap:24px">
        {gauge}
        <div style="flex:1">{bars}</div>
      </div>
      {cap("unit economics on a real proposal. the floor was too low and it proved why.")}</div>'''

# 5. EDITOR - split document: overwritten draft (half struck) vs cut-to-spine (IVORY)
def editor():
    def lines(struck_from):
        s=""
        widths=[300,264,300,240,288,300,216,276,300,252]
        for i,w in enumerate(widths):
            y=i*26
            if struck_from is not None and i>=struck_from:
                s+=(f'<rect x="0" y="{y}" width="{w}" height="9" rx="4" fill="rgba(200,70,35,.20)"/>'
                    f'<line x1="0" y1="{y+4.5}" x2="{w}" y2="{y+4.5}" stroke="rgb({RED})" stroke-width="2"/>')
            else:
                s+=f'<rect x="0" y="{y}" width="{w}" height="9" rx="4" fill="rgba(120,95,60,.32)"/>'
        return s
    def kept():
        s=""
        for i,w in enumerate([300,252,288,232,300]):
            s+=f'<rect x="0" y="{i*30}" width="{w}" height="10" rx="5" fill="#96562d"/>'
        return s
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("It read the draft: cut half.","STRIP TO THE SPINE","#2a2016","#96562d")}
      <div style="display:flex;align-items:stretch;gap:26px">
        <div style="flex:1;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.2);border-radius:18px;padding:22px 24px">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:#8a745a">DRAFT</span><span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#8a745a">840 w</span></div>
          <svg width="320" height="270" viewBox="0 0 320 270">{lines(4)}</svg>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px">
          <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.2"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.5 7.5 20 18M8.5 16.5 20 6"/></svg>
          <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.6"><path d="M5 12h12M13 7l6 5-6 5"/></svg>
        </div>
        <div style="flex:1;background:rgba(150,86,45,.08);border:1px solid rgba(150,90,45,.28);border-radius:18px;padding:22px 24px">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:#96562d">SHIPPED</span><span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016">410 w</span></div>
          <svg width="320" height="150" viewBox="0 0 320 150">{kept()}</svg>
          <div style="margin-top:18px;font-family:DM Sans;font-weight:700;font-size:16px;color:#2a2016;line-height:1.4">the offer, up top. no burial.</div>
        </div>
      </div>
      {cap("overwritten proposals bury the offer. it stripped it to the spine.","#8a745a")}</div>'''

# 6. STRATEGIST - one-question doorway filter: deals in -> "opens doors?" -> opened vs dead-end
def strategist():
    deals=""
    for i,(nm,y) in enumerate([("Deal A",112),("Deal B",212),("Deal C",312)]):
        deals+=(f'<rect x="34" y="{y-26}" width="150" height="52" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>'
          f'<text x="109" y="{y+6}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#c9c3b8">{nm}</text>'
          f'<path d="M184 {y} H300" stroke="rgba(212,162,127,.4)" stroke-width="2.5" stroke-dasharray="2 9"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It asked one question.","BETTER FILTER")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><linearGradient id="dr" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <filter id="drg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.3"/></filter></defs>
        {deals}
        <g filter="url(#drg)"><path d="M320 372 V132 a90 90 0 0 1 180 0 V372 Z" fill="url(#dr)" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <path d="M348 372 V138 a62 62 0 0 1 124 0 V372" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="2"/>
        <circle cx="452" cy="250" r="7" fill="rgb({ACC})"/>
        <text x="410" y="212" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#FAFAF7">OPENS</text>
        <text x="410" y="240" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#FAFAF7">DOORS?</text>
        <text x="410" y="308" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">the one filter</text>
        <path d="M500 168 H636" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round"/>
        <path d="M500 332 H636" stroke="rgb({RED})" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 8"/>
        <rect x="636" y="132" width="150" height="76" rx="16" fill="rgba(212,162,127,.1)" stroke="rgb({ACC})" stroke-width="1.5"/>
        <text x="711" y="164" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">compounds</text>
        <text x="711" y="188" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">two more doors</text>
        <rect x="636" y="296" width="150" height="76" rx="16" fill="rgba(200,70,35,.06)" stroke="rgba(200,70,35,.5)" stroke-width="1.5"/>
        <text x="711" y="328" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#c9c3b8">dead end</text>
        <text x="711" y="352" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({RED})">one-off cash</text>
      </svg>
      {cap("not is the deal good. is the deal a doorway. better filter, better clients.")}</div>'''

# 7. CLOSED - horizontal step timeline ending in a clean signature
def closed():
    steps=[("REPRICED","floor +38%",120),("REWRITTEN","half the words",320),("REQUALIFIED","opens doors",520)]
    nodes=""; y=150
    for nm,sub,x in steps:
        nodes+=(f'<circle cx="{x}" cy="{y}" r="38" fill="#211e1a" stroke="rgb({ACC})" stroke-width="2.5"/>'
          f'<path d="M{x-15} {y}l10 11 20 -22" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<text x="{x}" y="{y+70}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x}" y="{y+92}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{sub}</text>')
    sx=712
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The deal signed clean.","ONE CLEAN CLOSE")}
      <svg width="820" height="320" viewBox="0 0 820 320" style="display:block;margin:0 auto">
        <defs><radialGradient id="sg" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sgg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <line x1="120" y1="150" x2="{sx}" y2="150" stroke="rgba(212,162,127,.35)" stroke-width="3"/>
        {nodes}
        <g filter="url(#sgg)"><circle cx="{sx}" cy="150" r="58" fill="url(#sg)"/></g>
        <path d="M{sx-30} 156 q10 -22 20 0 q6 14 16 -6 q8 -14 18 2" fill="none" stroke="#1a0f0a" stroke-width="4" stroke-linecap="round"/>
        <text x="{sx}" y="240" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#FAFAF7">SIGNED</text>
        <text x="{sx}" y="262" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">cleanest this year</text>
      </svg>
      {cap("repriced, rewritten, requalified - one of the cleanest signatures this year.")}</div>'''

# 8. BOARD - your three advisors answering in one chat window, 02:14, costing cents
def board():
    msgs=[("P","PRICER","Floor is too low. Raise it 12 percent."),
          ("E","EDITOR","Cut the intro. Lead with the number."),
          ("S","STRATEGIST","Take it. This one opens two doors.")]
    rows=""
    for av,nm,txt in msgs:
        rows+=(f'<div style="display:flex;align-items:flex-start;gap:16px;margin-bottom:16px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:14px;background:linear-gradient(160deg,rgb({ACC}),#7a4326);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:20px;color:#1a0f0a">{av}</div>'
          f'<div style="flex:1;background:linear-gradient(160deg,#332f2a,#221f1b);border:1px solid rgba(255,255,255,.09);border-radius:4px 16px 16px 16px;padding:13px 18px">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:4px">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:600;font-size:19px;color:#eae4d8">{txt}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Your board sits in one chat.","ON CALL 02:14")}
      <div style="background:#161412;border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:22px 24px;box-shadow:inset 0 2px 4px rgba(0,0,0,.5)">
        <div style="display:flex;align-items:center;justify-content:space-between;padding-bottom:16px;margin-bottom:18px;border-bottom:1px solid rgba(255,255,255,.07)">
          <div style="display:flex;align-items:center;gap:10px">
            <span style="width:11px;height:11px;border-radius:50%;background:#7fd39a;box-shadow:0 0 10px rgba(127,211,154,.7)"></span>
            <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">The board</span>
            <span style="font-family:DM Mono;font-size:13px;color:#8f8f85">3 advisors · online</span></div>
          <span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">02:14</span></div>
        {rows}
        <div style="display:flex;align-items:center;gap:14px;margin-top:20px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:999px;padding:13px 22px">
          <span style="flex:1;font-family:DM Sans;font-size:17px;color:#6f6a60">Ask your board anything...</span>
          <span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">costs cents</span></div>
      </div>
      {cap("on call at 2am, briefed on everything you sell, costing cents.")}</div>'''

PANELS={"context":context(),"three":three(),"books":books(),"pricer":pricer(),
        "editor":editor(),"strategist":strategist(),"closed":closed(),"board":board()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/advisors"; os.makedirs(outd,exist_ok=True)
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
