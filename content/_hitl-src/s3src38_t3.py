#!/usr/bin/env python3
# TIER 3 - THE TOOL HALF-LIFE. Each panel a UNIQUE hand-built coded scene filling a clean rounded
# card (WIRE-ITS-EYES bar). Angle: every AI tool you memorize is obsolete in months; skill only
# compounds when it lives in a standing operator, not in your head. NO generic stat-chip strips.
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
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. TREADMILL - decay curve: usefulness of a learned tool collapses over months, obsolete by month 6
def treadmill():
    W,H=812,412; x0,y0,x1,y1=72,34,782,344
    def X(t): return x0+(x1-x0)*t
    def Y(v): return y1-(y1-y0)*v
    n=64; pts=[(X(i/n), Y(math.exp(-3.05*(i/n)))) for i in range(n+1)]
    line="M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)
    area=f"M{x0} {y1} L"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)+f" L{x1} {y1} Z"
    grid=""
    for m in range(0,13,3):
        gx=X(m/12)
        grid+=f'<line x1="{gx:.0f}" y1="{y0}" x2="{gx:.0f}" y2="{y1}" stroke="rgba(250,250,247,.055)"/>'
        grid+=f'<text x="{gx:.0f}" y="{y1+26}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8f8f85">{m} mo</text>'
    thr=0.15; ty=Y(thr); tob=-math.log(thr)/3.05; xob=X(tob)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("The tool you master in March","HALF-LIFE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:2px auto 0">
        <defs><linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.30)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
        <filter id="dg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {grid}
        <line x1="{x0}" y1="{ty:.0f}" x2="{x1}" y2="{ty:.0f}" stroke="rgba({RED},.5)" stroke-width="1.6" stroke-dasharray="3 8"/>
        <text x="{x1-4:.0f}" y="{ty-9:.0f}" text-anchor="end" font-family="DM Mono" font-size="12" fill="rgb({RED})">usable floor</text>
        <path d="{area}" fill="url(#fade)"/>
        <path d="{line}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>
        <circle cx="{x0}" cy="{Y(1):.0f}" r="8" fill="rgb({ACC})" filter="url(#dg)"/>
        <text x="{x0+14:.0f}" y="{Y(1)-2:.0f}" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">learned</text>
        <circle cx="{xob:.0f}" cy="{ty:.0f}" r="8" fill="rgb({RED})"/>
        <text x="{xob+14:.0f}" y="{ty+6:.0f}" font-family="DM Sans" font-weight="800" font-size="17" fill="rgb({RED})">obsolete</text>
      </svg>
      {cap("you are not slow. the half-life of an ai tool is now months, not years.")}</div>'''

# 2. SHELF LIFE - horizontal lifespan bars: months-alive per tool category, then a red dead cap
def shelflife():
    rows=[("Prompt hacks",4),("That one wrapper",6),("Framework of the week",3),
          ("Model-specific tricks",3),("The hot agent lib",7),("Your no-code stack",5)]
    full=12; barw=560; x0=224
    body=""
    for nm,mo in rows:
        w=barw*mo/full
        body+=(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:15px">'
          f'<div style="width:196px;text-align:right;font-family:DM Sans;font-weight:600;font-size:18px;color:#d9d5cc">{nm}</div>'
          f'<div style="position:relative;width:{barw}px;height:34px;border-radius:9px;background:rgba(250,250,247,.05);border:1px solid rgba(255,255,255,.06);overflow:hidden">'
          f'<div style="position:absolute;left:0;top:0;height:100%;width:{w:.0f}px;background:linear-gradient(90deg,#c99a72,rgb({ACC}));border-radius:9px 0 0 9px"></div>'
          f'<div style="position:absolute;left:{w:.0f}px;top:0;height:100%;right:0;background:repeating-linear-gradient(135deg,rgba({RED},.22),rgba({RED},.22) 6px,rgba({RED},.10) 6px,rgba({RED},.10) 12px)"></div>'
          f'<span style="position:absolute;left:12px;top:50%;transform:translateY(-50%);font-family:DM Sans;font-weight:900;font-size:15px;color:#1a0f0a">{mo} mo</span>'
          f'<span style="position:absolute;right:12px;top:50%;transform:translateY(-50%);font-family:DM Mono;font-size:11px;letter-spacing:.12em;color:rgb({RED})">DEAD</span></div></div>')
    axis="".join(f'<span style="font-family:DM Mono;font-size:11px;color:#7a746a">{m}</span>' for m in [0,3,6,9,12])
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Every tool has a shelf life","TOOL DECAY")}
      <div style="margin-top:4px">{body}</div>
      <div style="display:flex;justify-content:space-between;width:{barw}px;margin-left:{x0-12}px;margin-top:-2px">{axis}</div>
      {cap("prompt hacks, wrappers, the framework of the week. all decay on a clock.")}</div>'''

# 3. GRAVEYARD - chip field of tools, most crossed-out dead (muted red), a few still alive (accent)
def graveyard():
    cols,rowsn=9,6; total=cols*rowsn
    alive={7,19,26,33,41,48}
    cw,ch,gx,gy=82,50,10,12
    cells=""
    for i in range(total):
        r,c=divmod(i,cols); x=c*(cw+gx); y=r*(ch+gy)
        if i in alive:
            cells+=(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="11" fill="rgba(212,162,127,.14)" stroke="rgb({ACC})" stroke-width="1.6" filter="url(#al)"/>'
              f'<circle cx="{x+16}" cy="{y+ch/2:.0f}" r="4.5" fill="rgb({ACC})"/>')
        else:
            cells+=(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="11" fill="rgba(250,250,247,.035)" stroke="rgba(255,255,255,.07)" stroke-width="1"/>'
              f'<line x1="{x+15}" y1="{y+14}" x2="{x+cw-15}" y2="{y+ch-14}" stroke="rgba({RED},.5)" stroke-width="2.2"/>')
    fw=cols*(cw+gx)-gx; fh=rowsn*(ch+gy)-gy
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">Count the tools you forgot</span>
        <span style="font-family:'DM Mono';font-size:14px;letter-spacing:.05em;color:rgb({ACC})"><span style="color:rgb({RED})">48 dead</span> &middot; 6 alive</span></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="al" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.75"/></filter></defs>
        {cells}</svg>
      {cap("you did not fall behind. the ground moved under everything you memorized.")}</div>'''

# 4. LEAK - IVORY: knowledge poured into your head drains out through holes, retention stays tiny
def leak():
    drops=[("prompt syntax",150,300),("that shortcut",232,332),("the workflow",320,306),("model quirks",404,338)]
    dd=""
    for nm,x,y in drops:
        dd+=(f'<circle cx="{x}" cy="{y}" r="7" fill="#c07a4a" opacity="0.9"/>'
          f'<text x="{x}" y="{y+24}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a07048">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 30px">
      {htitle("Your head is a leaky bucket","RETENTION","#2a2016")}
      <div style="display:flex;align-items:center;gap:30px">
        <svg width="470" height="410" viewBox="0 0 470 410">
          <defs><linearGradient id="pour" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(150,86,45,.0)"/><stop offset="100%" stop-color="rgba(150,86,45,.7)"/></linearGradient>
          <linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d8a877"/><stop offset="100%" stop-color="#b06a3a"/></linearGradient></defs>
          <text x="235" y="30" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#8a6a44">EVERY NEW TOOL</text>
          <path d="M228 42 h14 v120 h-14 Z" fill="url(#pour)"/>
          <path d="M120 168 L350 168 L318 366 a14 14 0 0 1 -14 10 H166 a14 14 0 0 1 -14 -10 Z" fill="none" stroke="#96562d" stroke-width="4"/>
          <path d="M150 300 L340 300 L318 366 a14 14 0 0 1 -14 10 H166 a14 14 0 0 1 -14 -10 Z" fill="url(#fill)" opacity="0.85"/>
          <ellipse cx="235" cy="168" rx="115" ry="15" fill="none" stroke="#96562d" stroke-width="4"/>
          <circle cx="150" cy="272" r="7" fill="#efe6d5" stroke="#96562d" stroke-width="2"/>
          <circle cx="322" cy="278" r="7" fill="#efe6d5" stroke="#96562d" stroke-width="2"/>
          <circle cx="236" cy="360" r="7" fill="#efe6d5" stroke="#96562d" stroke-width="2"/>
          {dd}
          <text x="235" y="250" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#3a2a18">held: 9%</text>
        </svg>
        <div style="flex:1">
          <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#2a2016;line-height:1.08">Memory does not compound.</div>
          <div style="font-family:'DM Sans';font-size:19px;color:#5a4634;line-height:1.42;margin-top:14px">What you hold in your head leaks out between projects. You relearn the same tool twice a year and call it staying current.</div>
        </div>
      </div>
      {cap("knowledge that sits in you drains. knowledge in a system stays.","#8a745a")}</div>'''

# 5. STANDING OPERATOR - radial hub: one persistent core, the 7 named agents ringed around it
def standing():
    cx,cy,R=410,214,168
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=math.radians(-90+i*(360/7))
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        nodes+=(f'<g transform="translate({x-62:.0f},{y-24:.0f})">'
          f'<rect x="0" y="0" width="124" height="48" rx="14" fill="#241f1a" stroke="rgba(255,255,255,.12)" stroke-width="1.4"/>'
          f'<text x="62" y="21" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{nm}</text>'
          f'<text x="62" y="38" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{role}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Put the skill in a standing operator","THE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="op" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spokes}
        <g filter="url(#og)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#op)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">OPERATOR</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">always on</text>
        {nodes}
      </svg>
      {cap("the workflow lives in the system, not your memory. it is there when you wake up.")}</div>'''

# 6. HOT-SWAP - fixed workflow rail on top, tool sockets below: one ejected dead, one live, one inserting
def hotswap():
    W,H=816,412
    sock=[(150,"gpt-4o","deprecated","out",RED,False),(408,"claude","live now","hold",ACC,True),(666,"next model","incoming","in",ACC,True)]
    body=""
    for sx,nm,st,mode,col,on in sock:
        # empty socket housing
        body+=f'<rect x="{sx-90}" y="228" width="180" height="152" rx="20" fill="rgba(250,250,247,.03)" stroke="rgba(255,255,255,.08)" stroke-dasharray="6 7"/>'
        # connector bar up to the rail
        cc=f"rgb({col})" if on else f"rgba({col},.35)"
        body+=f'<rect x="{sx-6}" y="100" width="12" height="132" fill="{cc}"/>'
        cy0=284
        glow='filter="url(#sg)"' if on else ""
        body+=f'<g {glow}><rect x="{sx-72}" y="{cy0-42}" width="144" height="84" rx="16" fill="rgba({col},.13)" stroke="rgb({col})" stroke-width="2.2"/></g>'
        body+=f'<text x="{sx}" y="{cy0-2}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="{"#FAFAF7" if on else "#9a9488"}">{nm}</text>'
        body+=f'<text x="{sx}" y="{cy0+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({col})">{st}</text>'
        if mode=="out":
            body+=f'<path d="M{sx} 210 l-12 18 h24 Z" fill="rgb({col})"/>'
        elif mode=="in":
            body+=f'<path d="M{sx} 214 l-12 -18 h24 Z" fill="rgb({col})"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Tools swap. The system stays.","HOT-SWAP")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="railg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#211e1a"/></linearGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="46" y="30" width="724" height="70" rx="18" fill="url(#railg)" stroke="rgb({ACC})" stroke-width="2"/>
        <text x="408" y="60" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">YOUR WORKFLOW</text>
        <text x="408" y="84" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">services engine &middot; unchanged</text>
        {body}
      </svg>
      {cap("the router picks the best model per job and swaps it underneath. you relearn nothing.")}</div>'''

# 7. COMPOUND - IVORY ledger: each week adds to memory, running balance climbs, never resets
def compound():
    rows=[("Week 1","+ 40 briefs",40),("Week 2","+ 70 briefs",110),("Week 3","+ 100 briefs",210),
          ("Week 4","+ 150 briefs",360),("Week 5","+ 230 briefs",590),("Week 6","+ 320 briefs",910)]
    mx=910
    body=""
    for i,(wk,add,tot) in enumerate(rows):
        bw=300*tot/mx
        body+=(f'<div style="display:flex;align-items:center;gap:16px;padding:11px 0;border-bottom:1px solid rgba(120,95,60,.18)">'
          f'<span style="width:82px;font-family:DM Mono;font-size:15px;color:#7a5a38">{wk}</span>'
          f'<span style="width:120px;font-family:DM Sans;font-weight:600;font-size:16px;color:#5a4634">{add}</span>'
          f'<div style="flex:1;height:16px;border-radius:6px;background:rgba(150,120,80,.14);position:relative">'
          f'<div style="position:absolute;left:0;top:0;height:100%;width:{bw:.0f}px;border-radius:6px;background:linear-gradient(90deg,#c99a72,#96562d)"></div></div>'
          f'<span style="width:78px;text-align:right;font-family:DM Sans;font-weight:900;font-size:20px;color:#2a2016">{tot}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 30px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:10px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Sitting in a system, it compounds</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">MEMORY LEDGER</span></div>
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;opacity:.7">
        <span style="width:82px;font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#8a6a44">PERIOD</span>
        <span style="width:120px;font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#8a6a44">ADDED</span>
        <span style="flex:1"></span>
        <span style="width:78px;text-align:right;font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#8a6a44">RUNNING</span></div>
      {body}
      {cap("every brief you approve feeds the next. it never starts from zero.","#8a745a")}</div>'''

# 8. LEARN ONCE - split: left the relearn treadmill loop, right one operator that upgrades itself
def learnonce():
    # left loop with tool dots cycling
    lcx,lcy,lr=220,220,120
    loopdots=""
    for i,nm in enumerate(["tool","tool","tool","tool","tool","tool"]):
        a=math.radians(i*60)
        x=lcx+lr*math.cos(a); y=lcy+lr*math.sin(a)
        loopdots+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgba({RED},.55)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Stop relearning every quarter","LEARN ONCE")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="opb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="obg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        <line x1="410" y1="40" x2="410" y2="380" stroke="rgba(255,255,255,.09)" stroke-width="1.5" stroke-dasharray="4 8"/>
        <!-- LEFT: relearn loop -->
        <text x="220" y="54" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({RED})">YOU, TODAY</text>
        <path d="M{lcx+lr} {lcy} A{lr} {lr} 0 1 1 {lcx+lr-0.1} {lcy-0.1}" fill="none" stroke="rgba({RED},.45)" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>
        <path d="M{lcx+lr-2} {lcy-14} l16 12 l-18 8 Z" fill="rgb({RED})"/>
        {loopdots}
        <text x="{lcx}" y="{lcy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#d9d5cc">RELEARN</text>
        <text x="{lcx}" y="{lcy+22}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">every 90 days</text>
        <!-- RIGHT: one operator, self-updating -->
        <text x="600" y="54" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">ONE OPERATOR</text>
        <g filter="url(#obg)"><circle cx="600" cy="216" r="112" fill="url(#opb)"/></g>
        <text x="600" y="206" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#1a0f0a">LEARN</text>
        <text x="600" y="238" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#1a0f0a">ONCE</text>
        <g transform="translate(600,318)"><path d="M-26 4 a20 20 0 1 1 6 15" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/><path d="M-26 -12 v16 h16 Z" fill="rgb({ACC})"/></g>
        <text x="600" y="384" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">upgrades itself</text>
      </svg>
      {cap("own one operator that learns once and updates itself. the tools are its problem.")}</div>'''

PANELS={"treadmill":treadmill(),"shelflife":shelflife(),"graveyard":graveyard(),"leak":leak(),
        "standing":standing(),"hotswap":hotswap(),"compound":compound(),"learnonce":learnonce()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src38"; os.makedirs(outd,exist_ok=True)
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
