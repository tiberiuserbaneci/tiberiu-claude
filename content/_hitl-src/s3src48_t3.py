#!/usr/bin/env python3
# TIER 3 - IDEA TO FIRST PAYING CUSTOMERS (the validate -> build -> land-3-paying loop, speed to
# first revenue). Rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded scene
# filling a clean rounded card, htitle + one-line caption, NO generic stat-chip strips.
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
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SPEED - gantt/timeline compare: the usual 6-month build (still $0) vs the 9-day loop (3 paying)
def speed():
    W,H=820,430
    x0,x1=40,780; span=x1-x0
    ticks=""
    for m in range(0,7):
        x=x0+span*m/6
        ticks+=f'<line x1="{x:.0f}" y1="70" x2="{x:.0f}" y2="360" stroke="rgba(250,250,247,.06)" stroke-width="1"/>'
        ticks+=f'<text x="{x:.0f}" y="52" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#6f6a60">m{m}</text>'
    oldy=150; newy=290; bh=58
    newlen=span*0.16
    ms=[("validate",0.0),("build",0.5),("paid",1.0)]
    mt=""
    for nm,f in ms:
        mx=x0+newlen*f
        mt+=f'<circle cx="{mx:.0f}" cy="{newy+bh/2:.0f}" r="7" fill="#1d1d1b" stroke="#FAFAF7" stroke-width="2.5"/>'
        mt+=f'<text x="{mx:.0f}" y="{newy-14:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Six months, or nine days","SPEED TO REVENUE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs>
          <linearGradient id="oldb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#5a2a1e"/><stop offset="100%" stop-color="rgb(200,70,35)"/></linearGradient>
          <linearGradient id="newb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#7a4326"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
          <filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter>
        </defs>
        {ticks}
        <text x="{x0}" y="{oldy-18}" font-family="DM Sans" font-weight="700" font-size="17" fill="#a8a296">The usual build</text>
        <rect x="{x0}" y="{oldy}" width="{span:.0f}" height="{bh}" rx="14" fill="url(#oldb)" opacity="0.9"/>
        <text x="{x1-18}" y="{oldy+bh/2+6:.0f}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="22" fill="#f3d9cf">still $0</text>
        <text x="{x0}" y="{newy-18}" font-family="DM Sans" font-weight="700" font-size="17" fill="rgb({ACC})">The Ultron loop</text>
        <g filter="url(#ng)"><rect x="{x0}" y="{newy}" width="{newlen:.0f}" height="{bh}" rx="14" fill="url(#newb)"/></g>
        {mt}
        <text x="{x0+newlen+22:.0f}" y="{newy+bh/2+6:.0f}" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">3 paying</text>
      </svg>
      {cap("most founders build for a season before a dollar. the loop gets you paid in days.")}</div>'''

# 2. VALIDATE - demand funnel: 60 talked to -> 22 feel the pain -> 3 pre-paid before any code
def validate():
    stages=[("60 founders","talked to",600,"#c9c3b8",False),
            ("22 feel it","the exact pain",380,"#e6d6c2",False),
            ("3 pre-paid","before a line of code",210,"#FAFAF7",True)]
    W,H=760,430; cx=W/2; ytop=24; sh=116; gap=14
    polys=""; labels=""; y=ytop
    for i,(big,sub,w,col,hot) in enumerate(stages):
        half=w/2; nxt=stages[i+1][2] if i+1<len(stages) else w*0.6
        tl=cx-half; tr=cx+half; bl=cx-nxt/2; br=cx+nxt/2
        fill="url(#hot)" if hot else "#2a2622"
        stroke=f"rgb({ACC})" if hot else "rgba(255,255,255,.09)"
        glow=' filter="url(#fg)"' if hot else ''
        polys+=f'<polygon points="{tl:.0f},{y} {tr:.0f},{y} {br:.0f},{y+sh} {bl:.0f},{y+sh}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"{glow}/>'
        tcol="#1a0f0a" if hot else col
        scol="rgba(26,15,10,.7)" if hot else "#8f8f85"
        labels+=f'<text x="{cx}" y="{y+sh/2-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="{tcol}">{big}</text>'
        labels+=f'<text x="{cx}" y="{y+sh/2+24:.0f}" text-anchor="middle" font-family="DM Sans" font-size="15" fill="{scol}">{sub}</text>'
        y+=sh+gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Sell it before you build it","DEMAND FIRST")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="hot" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="fg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {polys}{labels}
      </svg>
      {cap("cortex finds who hurts, specter asks. no buyers, no build.")}</div>'''

# 3. OFFER - IVORY offer card: one outcome, one price, a pre-pay link (a landing page suits light)
def offer():
    checks=["One outcome, delivered","Live in days, not months","Money back if it misses"]
    ci=""
    for c in checks:
        ci+=f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:19px;color:#3a2f22">{c}</span></div>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">A paid promise, not a demo</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">THE OFFER</span></div>
      <div style="background:rgba(255,255,255,.66);border:1px solid rgba(120,95,60,.2);border-radius:22px;padding:28px 32px;box-shadow:0 20px 40px rgba(120,95,60,.16), inset 0 2px 3px rgba(255,255,255,.9)">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px">
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#a0562d">YOUR OFFER</span>
          <span style="font-family:'DM Mono';font-size:13px;color:#b0492a;background:rgba(200,70,35,.1);border:1px solid rgba(200,70,35,.3);border-radius:999px;padding:5px 12px">3 seats left</span></div>
        <div style="font-family:'DM Sans';font-weight:900;font-size:33px;color:#2a2016;line-height:1.1;margin-bottom:18px">Ship your ops in a week, done for you.</div>
        {ci}
        <div style="display:flex;align-items:center;justify-content:space-between;margin-top:20px;padding-top:20px;border-top:1px solid rgba(120,95,60,.2)">
          <div><span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#2a2016">$500</span><span style="font-family:'DM Sans';font-size:16px;color:#8a745a"> to start</span></div>
          <div style="background:linear-gradient(160deg,#c98a5f,#96562d);color:#fff;font-family:'DM Sans';font-weight:900;font-size:18px;padding:14px 30px;border-radius:14px;box-shadow:0 12px 24px rgba(150,86,45,.4)">Pre-pay</div>
        </div>
      </div>
      {cap("one outcome, one price, a pre-pay link. striker shapes what closes.","#8a745a")}</div>'''

# 4. BUILD - isometric MVP stack: scope -> build -> live, ending in a shipped v0.1 pill
def build():
    steps=[("SCOPE","one job the 3 buyers asked for",0),("BUILD","shipped in 2 days",1),("LIVE","on your own domain",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The smallest thing that delivers","MVP · SENTINEL")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:120px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Live &#10003; v0.1</div></div></div>
      {cap("sentinel builds only what the three buyers asked for, nothing else.")}</div>'''

# 5. REACH - left-to-right flow: SPECTER hub -> 3 warm buyer nodes with live status
def reach():
    W,H=820,440
    hubx,huby=150,220
    tg=[("Founder A","replied in 20 min",96),("Founder B","booked a call",220),("Founder C","asked for the link",344)]
    edges=""; nodes=""
    for nm,st,y in tg:
        mx=(hubx+620)/2
        edges+=f'<path d="M{hubx+64} {huby} C{mx:.0f} {huby},{mx:.0f} {y},620 {y}" stroke="rgb({ACC})" stroke-width="2.6" fill="none" opacity="0.7"/>'
        nodes+=(f'<rect x="620" y="{y-38}" width="182" height="76" rx="16" fill="#2a2724" stroke="rgba(212,162,127,.32)"/>'
          f'<text x="642" y="{y-6}" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{nm}</text>'
          f'<text x="642" y="{y+18}" font-family="DM Sans" font-size="14" fill="#9a9488">{st}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Straight to the warm buyers","OUTREACH · SPECTER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><radialGradient id="sp" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}
        <g filter="url(#sg)"><circle cx="{hubx}" cy="{huby}" r="64" fill="url(#sp)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">SPECTER</text>
        <text x="{hubx}" y="{huby+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">warm 22</text>
        {nodes}
      </svg>
      {cap("no cold list. the people who already said they feel the pain.")}</div>'''

# 6. CLOSE - receipt ledger: 3 paid cards + a first-revenue total banner
def close():
    rows=[("Northwind Co.","annual plan","$490"),("Bright Labs","annual plan","$490"),("Pilate Studio","quarterly plan","$180")]
    chips=""
    for nm,plan,amt in rows:
        chips+=f'''<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:16px 20px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">
          <div style="flex-shrink:0;width:42px;height:42px;border-radius:11px;background:linear-gradient(160deg,#4a423a,#2a2622);display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:20px;color:rgb({ACC});border:1px solid rgba(255,255,255,.10)">{nm[0]}</div>
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#eae4d8">{nm}</div><div style="font-family:'DM Sans';font-size:14px;color:#8f8f85">{plan}</div></div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#FAFAF7;margin-right:6px">{amt}</div>
          <div style="flex-shrink:0;background:rgb({ACC});color:#1a0f0a;font-family:'DM Mono';font-size:12px;letter-spacing:.1em;padding:6px 12px;border-radius:999px">PAID</div>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The first three said yes","CLOSED · STRIKER")}
      <div style="display:flex;flex-direction:column;gap:14px">{chips}</div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:18px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:16px;padding:18px 24px;box-shadow:0 0 26px rgba(212,162,127,.2)">
        <span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#c9c3b8">First revenue, day nine</span>
        <span style="font-family:'DM Sans';font-weight:900;font-size:34px;color:rgb({ACC})">$1,160</span></div>
      {cap("objections handled, links sent, three cards charged.")}</div>'''

# 7. ORCHESTRATE - radial hub-and-spokes: ROUTER at center, the loop's agents around it
def orchestrate():
    cx,cy,R=300,232,168
    agents=[("CORTEX","validate",-90),("SPECTER","reach",-30),("STRIKER","close",30),
            ("SENTINEL","build",90),("PULSE","announce",150),("AMPLIFY","publish",210)]
    spokes=""; nodes=""
    for nm,role,a in agents:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.8"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#eadfce">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="540" height="470" viewBox="0 0 600 470" style="flex-shrink:0">
        <defs><radialGradient id="ro" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="70" fill="url(#ro)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">picks per step</text>
      </svg>
      <div style="flex:1">
        {htitle("One operator runs it","ROUTER")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Validate, offer, build, reach, close. The ROUTER hires the right agent and the cheapest model that can do each step.</div>
        {cap("cortex to close, one chat, cents per step.")}</div></div>'''

# 8. REVENUE - convergence: the five steps flow into one glowing first-revenue node (day 9)
def revenue():
    scat=[("idea",70,80),("validate",70,190),("offer",70,300),("build",200,135),("reach",200,245),("close",200,355)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+30} {y} C360 {y},400 215,500 215" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.75"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A sentence in, revenue out","DAY 9")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <defs><radialGradient id="rev" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rvg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {left}
        <g filter="url(#rvg)"><circle cx="620" cy="215" r="120" fill="url(#rev)"/></g>
        <text x="620" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">3 PAYING</text>
        <text x="620" y="230" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">DAY 9</text>
        <text x="620" y="372" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">validated · built · closed</text>
      </svg>
      {cap("from one sentence to three charged cards, one system, in days.")}</div>'''

PANELS={"speed":speed(),"validate":validate(),"offer":offer(),"build":build(),
        "reach":reach(),"close":close(),"orchestrate":orchestrate(),"revenue":revenue()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src48"; os.makedirs(outd,exist_ok=True)
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
