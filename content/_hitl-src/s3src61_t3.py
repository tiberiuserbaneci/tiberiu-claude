#!/usr/bin/env python3
# TIER 3 - HANDSHAKE OR PAPER (the founding legal-doc stack, COUNSEL angle), built to the
# WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded scene filling a clean rounded card,
# title + one-line caption, NO generic stat-chip strips.
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
def hivory(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

SHIELD="M560 60 L730 118 L730 280 Q730 374 560 454 Q390 374 390 280 L390 118 Z"

# 1. GAP - split/compare: a struck-out verbal handshake ghost vs a solid shield of doc plates
def gap():
    plates=""
    ys=[92,148,204,260,316,372]
    for i,y in enumerate(ys):
        op=.9-i*0.06
        plates+=f'<rect x="392" y="{y}" width="336" height="42" rx="7" fill="url(#pl)" opacity="{op:.2f}"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A shield, not a handshake","18 DOCS")}
      <svg width="760" height="470" viewBox="0 0 760 470" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="pl" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4c2c"/></linearGradient>
          <clipPath id="sh"><path d="{SHIELD}"/></clipPath>
          <filter id="shg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="10" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter>
        </defs>
        <!-- verbal handshake ghost, void -->
        <rect x="44" y="150" width="272" height="170" rx="20" fill="rgba(250,250,247,.03)" stroke="rgba(200,70,35,.5)" stroke-width="2" stroke-dasharray="8 8"/>
        <g transform="translate(180,210)" stroke="rgba(200,70,35,.72)" stroke-width="7" stroke-linecap="round" fill="none">
          <path d="M-46 8 L-18 -14 L2 4 L-14 22"/><path d="M46 8 L18 -14 L-2 4 L14 22"/>
        </g>
        <line x1="90" y1="168" x2="270" y2="302" stroke="rgba(200,70,35,.8)" stroke-width="4"/>
        <text x="180" y="288" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".18em" fill="#c05a35">HANDSHAKE</text>
        <text x="180" y="345" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#7a746a">verbal &middot; protects nothing</text>
        <!-- shield of stacked document plates -->
        <g filter="url(#shg)"><path d="{SHIELD}" fill="#241f1a"/></g>
        <g clip-path="url(#sh)">{plates}</g>
        <path d="{SHIELD}" fill="none" stroke="rgb({ACC})" stroke-width="3"/>
        <path d="M520 250 l26 26 l58 -66" fill="none" stroke="#FAFAF7" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="560" y="430" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">18 SIGNED &middot; SEALED</text>
      </svg>
      {cap("a verbal deal holds until it does not. the founding stack is the only thing that does.")}</div>'''

# 2. STACK - isometric tower of the founding documents
def stack():
    docs=[("Certificate of Incorporation","state filing"),
          ("Founder Agreement","equity + vesting"),
          ("Mutual NDA","before any pitch"),
          ("Master Services Agreement","how you sell"),
          ("IP Assignment","code owned by the company"),
          ("Cap Table","who owns what"),
          ("Term Sheet","when you raise")]
    cards=""
    for i,(nm,sub) in enumerate(docs):
        y=i*62
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;background:linear-gradient(160deg,#413b35,#2b2723);'
          f'border:1.5px solid rgba(255,255,255,.15);border-radius:15px;padding:13px 22px;box-shadow:0 26px 40px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.10);'
          f'display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:34px;height:34px;border-radius:9px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);'
          f'display:flex;align-items:center;justify-content:center"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.2"><path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/></svg></div>'
          f'<div style="flex:1;min-width:0"><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#a8a296">{sub}</div></div>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:13px;color:rgb({ACC})">{i+1:02d}</span></div>')
    cards+=(f'<div style="position:absolute;left:0;top:{7*62}px;width:600px;background:rgb({ACC});border-radius:15px;padding:12px 22px;'
      f'box-shadow:0 26px 40px rgba(0,0,0,.5);display:flex;align-items:center;justify-content:space-between">'
      f'<span style="font-family:DM Sans;font-weight:900;font-size:19px;color:#1a0f0a">+ 11 more, all drafted</span>'
      f'<span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#1a0f0a">18</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("The founding stack","18 &middot; SEALED")}
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(23deg) rotateZ(-9deg);width:600px;height:520px;position:relative">{cards}</div></div>
      {cap("incorporation to term sheet, one sealed folder, not scattered emails.")}</div>'''

# 3. INCORPORATION - IVORY certificate object with an embossed foil seal
def incorporation():
    fields=[("CIN","DL2024PTC123456"),("JURISDICTION","Delaware, USA"),("AUTHORIZED SHARES","10,000,000")]
    rows=""
    for k,v in fields:
        rows+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:11px 0;border-bottom:1px solid rgba(120,95,60,.18)">'
          f'<span style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:#96562d">{k}</span>'
          f'<span style="font-family:DM Mono;font-size:16px;color:#2a2016">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {hivory("Proof it legally exists","INCORPORATION")}
      <div style="background:linear-gradient(160deg,#fffdf9,#f6efe2);border:1.5px solid rgba(120,95,60,.24);border-radius:20px;padding:30px 34px 26px;position:relative;box-shadow:inset 0 0 0 3px rgba(150,120,80,.10)">
        <div style="font-family:DM Sans;font-weight:900;font-size:27px;letter-spacing:.01em;color:#2a2016;line-height:1.08">CERTIFICATE OF<br>INCORPORATION</div>
        <div style="width:96px;height:4px;background:#96562d;border-radius:3px;margin:12px 0 20px"></div>
        <div style="font-family:DM Sans;font-size:17px;color:#5a4a36;line-height:1.4;max-width:520px">This certifies that the company named below is duly incorporated and authorized to issue shares of stock.</div>
        <div style="margin-top:20px;max-width:560px">{rows}</div>
        <!-- embossed foil seal -->
        <svg width="140" height="140" viewBox="0 0 140 140" style="position:absolute;right:30px;bottom:26px">
          <defs><radialGradient id="foil" cx="38%" cy="32%"><stop offset="0%" stop-color="#f4d8a8"/><stop offset="55%" stop-color="#c79a5e"/><stop offset="100%" stop-color="#8a6432"/></radialGradient>
          <filter id="fs" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="rgba(120,90,50,.45)"/></filter></defs>
          {"".join(f'<line x1="70" y1="70" x2="{70+62*math.cos(math.radians(a)):.0f}" y2="{70+62*math.sin(math.radians(a)):.0f}" stroke="#b89257" stroke-width="6"/>' for a in range(0,360,18))}
          <g filter="url(#fs)"><circle cx="70" cy="70" r="52" fill="url(#foil)"/></g>
          <circle cx="70" cy="70" r="52" fill="none" stroke="rgba(255,255,255,.5)" stroke-width="1.5"/>
          <circle cx="70" cy="70" r="40" fill="none" stroke="rgba(90,60,30,.35)" stroke-width="1.5"/>
          <text x="70" y="66" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#4a3420">FILED</text>
          <text x="70" y="84" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#4a3420">2024</text>
        </svg>
      </div>
      {cap("registered, on record with the state. the day your company becomes real.","#8a745a")}</div>'''

# 4. FOUNDERS - vesting timeline (4-year vest, 1-year cliff) with the pre-cliff zone void
def founders():
    x0,x1=70,748; y=228; span=x1-x0; cliff=x0+span*0.25
    ticks=""
    for i in range(5):
        tx=x0+span*i/4
        pct=[0,25,50,75,100][i]
        ticks+=(f'<line x1="{tx:.0f}" y1="{y-13}" x2="{tx:.0f}" y2="{y+13}" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
          f'<text x="{tx:.0f}" y="{y+42}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c9c3b8">Y{i}</text>'
          f'<text x="{tx:.0f}" y="{y-26}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="{"#6f6a60" if i==0 else "rgb("+ACC+")"}">{pct}%</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Vesting before trust","FOUNDER AGREEMENT")}
      <svg width="800" height="300" viewBox="0 0 800 300" style="display:block;margin:6px auto 0">
        <defs><linearGradient id="vg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8a4c2c"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        <!-- pre-cliff void zone -->
        <rect x="{x0}" y="{y-9}" width="{cliff-x0:.0f}" height="18" rx="9" fill="rgba(200,70,35,.14)" stroke="rgba(200,70,35,.5)" stroke-width="1.5" stroke-dasharray="6 6"/>
        <text x="{(x0+cliff)/2:.0f}" y="{y+70}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c05a35">nothing vests before the cliff</text>
        <!-- vested track -->
        <rect x="{cliff:.0f}" y="{y-9}" width="{x1-cliff:.0f}" height="18" rx="9" fill="url(#vg)"/>
        {ticks}
        <!-- cliff gate -->
        <line x1="{cliff:.0f}" y1="{y-64}" x2="{cliff:.0f}" y2="{y+16}" stroke="rgb({RED})" stroke-width="3" stroke-dasharray="4 5"/>
        <rect x="{cliff-52:.0f}" y="{y-96}" width="104" height="30" rx="8" fill="rgba(200,70,35,.16)" stroke="rgb({RED})" stroke-width="1.5"/>
        <text x="{cliff:.0f}" y="{y-76}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#e08a63">1-YEAR CLIFF</text>
        <circle cx="{x1:.0f}" cy="{y}" r="11" fill="rgb({ACC})" filter="url(#fg)"/>
        <defs><filter id="fg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <text x="{x1:.0f}" y="{y+90}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="rgb({ACC})">fully vested</text>
      </svg>
      <div style="display:flex;gap:14px;margin-top:8px">
        {"".join(f'<div style="flex:1;background:#221f1b;border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:14px 18px"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">{k}</div><div style="font-family:DM Sans;font-weight:700;font-size:17px;color:#FAFAF7;margin-top:3px">{v}</div></div>' for k,v in [("ROLES","who owns what day to day"),("DECISIONS","majority or CEO call"),("EXIT","unvested equity returns")])}
      </div>
      {cap("split equity, roles and the exit clause the day you incorporate, not the day you fight.")}</div>'''

# 5. COUNSEL - radial hub, the COUNSEL agent core drafting every contract type, one flagged
def counsel():
    cx,cy,Rr=250,220,160
    nodes=[("NDA",-90,False),("MSA",-25,False),("Term Sheet",40,False),("IP Assign",105,False),("Employment",170,True),("Privacy",235,False)]
    ring=""
    for nm,a,flag in nodes:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        col=f"rgb({RED})" if flag else "rgba(212,162,127,.55)"
        ndbd=f"rgba(200,70,35,.65)" if flag else "rgba(255,255,255,.14)"
        das='stroke-dasharray="4 6"' if flag else ""
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="{3 if flag else 2}" {das}/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="{ndbd}" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="{"#e08a63" if flag else "#d9d5cc"}">{nm}</text>')
        if flag:
            ring+=f'<text x="{x:.0f}" y="{y+52:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({RED})">risk flagged</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="500" height="440" viewBox="0 0 500 440">
        <defs><radialGradient id="cx" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {ring}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="64" fill="url(#cx)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">COUNSEL</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">drafts &middot; reviews</text>
      </svg>
      <div style="flex:1">
        {htitle("One agent, every contract","COUNSEL")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">NDAs, MSAs, term sheets, IP assignment. Drafted, reviewed, and the risky clauses flagged before you sign.</div>
        {cap("a lawyer bills $4,500 a doc. counsel drafts and reviews it for cents.")}</div></div>'''

# 6. RISK - semicircular risk gauge, needle high, N clauses flagged
def risk():
    cx,cy,R=280,300,190
    def pt(deg,rad):
        return (cx+rad*math.cos(math.radians(deg)), cy+rad*math.sin(math.radians(deg)))
    # arc from 180 (left) to 360 (right), value at ~ -40deg i.e. 140deg into the sweep (high)
    ax0,ay0=pt(180,R); ax1,ay1=pt(360,R)
    val=180+180*0.72  # needle angle
    nx,ny=pt(val,R-34)
    ticks=""
    for t in range(0,181,30):
        a=180+t
        ix,iy=pt(a,R); ox,oy=pt(a,R-20)
        ticks+=f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="rgba(250,250,247,.35)" stroke-width="2"/>'
    chips=[("Auto-renew","locks you in 3 years"),("Unlimited indemnity","uncapped liability"),("IP license grant","they keep your work")]
    ch=""
    for nm,note in chips:
        ch+=(f'<div style="display:flex;align-items:center;gap:12px;background:rgba(200,70,35,.10);border:1px solid rgba(200,70,35,.42);border-radius:13px;padding:11px 16px">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({RED})" stroke-width="2.4"><path d="M12 2 L22 20 H2 Z"/><line x1="12" y1="9" x2="12" y2="14"/><circle cx="12" cy="17.5" r="0.6" fill="rgb({RED})" stroke="none"/></svg>'
          f'<div style="flex:1"><span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#f0d8cc">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:#b58a78;margin-left:8px">{note}</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="380" height="380" viewBox="0 0 560 380">
        <defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="70%" stop-color="#c07a45"/><stop offset="100%" stop-color="rgb({RED})"/></linearGradient>
        <filter id="ng" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({RED})" flood-opacity="0.8"/></filter></defs>
        <path d="M{ax0:.0f} {ay0:.0f} A{R} {R} 0 0 1 {ax1:.0f} {ay1:.0f}" fill="none" stroke="rgba(250,250,247,.10)" stroke-width="30" stroke-linecap="round"/>
        <path d="M{ax0:.0f} {ay0:.0f} A{R} {R} 0 0 1 {ax1:.0f} {ay1:.0f}" fill="none" stroke="url(#ga)" stroke-width="30" stroke-linecap="round" stroke-dasharray="{math.pi*R*0.72:.0f} 2000"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({RED})" stroke-width="6" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="13" fill="#241f1a" stroke="rgb({RED})" stroke-width="3"/>
        <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="64" fill="#FAFAF7">3</text>
        <text x="{cx}" y="{cy-24}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({RED})">CLAUSES FLAGGED</text>
        <text x="{ax0:.0f}" y="{ay0+34:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">safe</text>
        <text x="{ax1:.0f}" y="{ay1+34:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c05a35">costly</text>
      </svg>
      <div style="flex:1">
        {htitle("Reads what you would sign blind","RISK SCAN")}
        <div style="display:flex;flex-direction:column;gap:11px;margin-top:2px">{ch}</div>
        {cap("every clause parsed, the ones that can cost you the company pulled to the top.")}</div></div>'''

# 7. CAPTABLE - IVORY donut of ownership, warm wedges, legend
def captable():
    segs=[("Founders",64,"rgb(212,162,127)"),("Option pool",16,"#c99a5e"),("Investors",14,"#96562d"),("Advisors",6,"#e0c39a")]
    cx,cy,r,sw=145,145,104,42
    circ=2*math.pi*r; off=0.0; arcs=""; a0=-90
    for nm,pc,col in segs:
        dash=circ*pc/100
        arcs+=(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}" '
          f'stroke-dasharray="{dash:.1f} {circ:.1f}" stroke-dashoffset="{-off:.1f}" transform="rotate(-90 {cx} {cy})"/>')
        off+=dash
    legend=""
    for nm,pc,col in segs:
        legend+=(f'<div style="display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid rgba(120,95,60,.16)">'
          f'<span style="width:14px;height:14px;border-radius:4px;background:{col};flex-shrink:0"></span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:19px;color:#2a2016">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:18px;color:#5a4a36">{pc}%</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;align-items:center;gap:36px">
      <svg width="290" height="290" viewBox="0 0 290 290" style="flex-shrink:0">
        {arcs}
        <circle cx="{cx}" cy="{cy}" r="60" fill="#fdfbf6" stroke="rgba(120,95,60,.18)"/>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a2016">100%</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#96562d">on record</text>
      </svg>
      <div style="flex:1">
        {hivory("The cap table, to the decimal","OWNERSHIP")}
        {legend}
        {cap("ip assigned to the company, not to a founder's old laptop.","#8a745a")}</div></div>'''

# 8. SEALED - convergence: scattered docs pull into one gated, signed vault
def sealed():
    scat=[("incorporation",70,80),("founder agreement",70,180),("nda / msa",70,280),("ip + cap table",190,130),("term sheet",190,230)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+58} {y} C360 {y},400 200,520 200" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
          f'<rect x="{x-4}" y="{y-20}" width="150" height="40" rx="11" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x+71}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a8a296">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Drafted in cents, gated by you","HUMAN GATE")}
      <svg width="800" height="420" viewBox="0 0 800 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="vt" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="vg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#vg2)"><circle cx="560" cy="200" r="118" fill="url(#vt)"/></g>
        <g transform="translate(526,150)"><rect x="0" y="34" width="68" height="50" rx="11" fill="none" stroke="#2a160c" stroke-width="6"/><path d="M12 34 V21 a22 22 0 0 1 44 0 v13" fill="none" stroke="#2a160c" stroke-width="6"/></g>
        <text x="560" y="250" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">SIGNED</text>
        <text x="560" y="352" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#8f8f85">drafted &middot; reviewed &middot; your tap</text>
      </svg>
      {cap("counsel drafts all 18 for cents. you approve every signature. still your company.")}</div>'''

PANELS={"gap":gap(),"stack":stack(),"incorporation":incorporation(),"founders":founders(),
        "counsel":counsel(),"risk":risk(),"captable":captable(),"sealed":sealed()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src61"; os.makedirs(outd,exist_ok=True)
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
