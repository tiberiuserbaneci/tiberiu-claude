#!/usr/bin/env python3
# TIER 3 - SYSTEMS NOT PROMPTS, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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

# 1. FRAME - SPLIT screen: a crossed-out prompt scrap (left) vs a packaged system (right)
def frame():
    bars="".join(f'<div style="height:9px;border-radius:5px;background:rgba(250,250,247,{op});margin-bottom:11px;width:{w}%"></div>' for op,w in [(.14,96),(.10,88),(.14,72),(.09,90),(.12,60)])
    rows="".join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">'
        f'<span style="width:26px;height:26px;border-radius:8px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.4);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:14px;color:rgb({ACC})">{i}</span>'
        f'<div style="height:8px;border-radius:4px;background:rgba(250,250,247,.18);flex:1"></div>'
        f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M6 12.5l3.5 3.5L18 7.5"/></svg></div>' for i in ["1","2","3"])
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You are still prompting","PROMPT vs SYSTEM")}
      <div style="display:flex;align-items:stretch;gap:0;height:470px">
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px">
          <div style="position:relative;width:280px;background:linear-gradient(158deg,#2c2825,#201d1a);border:1px solid rgba(200,70,35,.4);border-radius:16px;padding:24px 22px;box-shadow:0 20px 40px rgba(0,0,0,.5)">
            <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb(200,70,35);margin-bottom:14px">PROMPT.txt</div>
            {bars}
            <svg viewBox="0 0 280 210" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%"><line x1="26" y1="30" x2="254" y2="182" stroke="rgba(200,70,35,.85)" stroke-width="4" stroke-linecap="round"/></svg>
          </div>
          <div style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#8f8f85">rewritten every time</div>
        </div>
        <div style="width:1px;background:rgba(255,255,255,.1);margin:24px 0"></div>
        <div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px">
          <div style="width:280px;background:linear-gradient(160deg,#413b33,#241f1a);border:1.5px solid rgb({ACC});border-radius:16px;padding:22px 22px;box-shadow:0 26px 46px rgba(0,0,0,.55),0 0 40px rgba(212,162,127,.16)">
            <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:16px">SYSTEM</div>
            {rows}
          </div>
          <div style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:rgb({ACC})">built once, runs forever</div>
        </div>
      </div>
      {cap("a prompt is a note you retype. a system is an operator that ships.")}</div>'''

# 2. ROSTER - radial hub: 7 named agents orbit the ROUTER core
def roster():
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    roles=["research","outbound","deals","content","code","publish","legal"]
    cx,cy,R=306,238,182
    spokes=""; nodes=""; n=len(agents)
    for i,(a,r) in enumerate(zip(agents,roles)):
        ang=-90+i*360/n
        x=cx+R*math.cos(math.radians(ang)); y=cy+R*math.sin(math.radians(ang))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#241f1a" stroke="rgba(212,162,127,.45)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-3:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="13" fill="#FAFAF7">{a}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#9a9488">{r}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one roster","THE WHOLE STACK")}
      <svg width="612" height="476" viewBox="0 0 612 476" style="display:block;margin:0 auto">
        <defs><radialGradient id="rt" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#rt)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one login</text>
        {nodes}
      </svg>
      {cap("research to close. one roster replaces the ten-tab stack.")}</div>'''

# 3. ROUTER - node graph: one plain line routed to the cheapest model tier that fits
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",236,True),("DEEP","hard judgement","0.40c",376,False)]
    hubx,hy=180,236; edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+60} {hy} C330 {hy},345 {y},470 {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="box-shadow:0 0 26px rgba(212,162,127,.28)" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        costcol=f"rgb({ACC})" if on else "#c9a583"
        cards+=(f'<div style="position:absolute;left:472px;top:{y-42}px;width:300px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:15px 18px;display:flex;align-items:center;gap:16px">'
          f'<div style="flex:1"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85;margin-top:2px">{role}</div></div>'
          f'<div style="flex-shrink:0"><span style="font-family:DM Sans;font-weight:900;font-size:26px;color:{costcol}">{cost}</span></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One line picks the tier","MODEL ROUTER")}
      <div style="position:relative;height:472px">
        <svg width="820" height="472" viewBox="0 0 820 472" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="14" y="{hy-34}" width="106" height="68" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <text x="67" y="{hy-4}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">draft 12</text>
          <text x="67" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">emails</text>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="56" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">reads the job</text>
        </svg>
        {cards}
      </div>
      {cap("the cheapest tier that can actually do the job. cents, never a flat seat.")}</div>'''

# 4. SIGNALS - radar of live market moves, ranked, with a first-to-see lead readout
def signals():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Stack",210,168),("Intent",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">You + Ultron</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">Tue 09:12</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">Your VC</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">Fri 16:40</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">3 days ahead</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It saw the round first","SIGNAL LEAD")}
        {lead}
        {cap("funding, hiring, stack, intent. this morning's web, watched for you.")}
      </div></div>'''

# 5. SEQUENCE - IVORY: a gated outbound timeline, every step locked behind your tap
def sequence():
    stations=[("DAY 0","First touch","APPROVED",False),
              ("DAY 3","Follow-up","APPROVED",False),
              ("DAY 7","Break-up","YOUR TAP",True)]
    cells=""
    for d,t,s,held in stations:
        lockcol="#96562d" if held else "rgba(150,90,45,.5)"
        boxsh="box-shadow:0 0 30px rgba(150,86,45,.35),0 14px 26px rgba(120,95,60,.2)" if held else "box-shadow:0 14px 26px rgba(120,95,60,.18)"
        pillbg="#96562d" if held else "rgba(150,90,45,.12)"
        pillcol="#fdfbf6" if held else "#8a745a"
        cells+=f'''<div style="flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:1">
          <div style="width:80px;height:80px;border-radius:22px;background:rgba(255,255,255,.62);border:2px solid {lockcol};display:flex;align-items:center;justify-content:center;{boxsh}">
            <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="{lockcol}" stroke-width="2.2"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div>
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#96562d;margin-top:16px">{d}</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016;margin-top:4px">{t}</div>
          <div style="margin-top:12px;font-family:DM Mono;font-size:12px;letter-spacing:.1em;background:{pillbg};color:{pillcol};padding:6px 15px;border-radius:999px">{s}</div>
        </div>'''
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Every send waits for you</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">HUMAN GATE</span></div>
      <div style="position:relative;height:300px;display:flex;align-items:flex-start;padding:34px 20px 0">
        <div style="position:absolute;left:14%;right:14%;top:74px;height:3px;background:rgba(150,90,45,.28)"></div>
        {cells}
      </div>
      {cap("SPECTER drafts the whole sequence. nothing leaves without your tap.","#8a745a")}</div>'''

# 6. PROOF - dot field: the whole market scanned each morning, only movers lit
def proof():
    cols,rowsn=48,26
    lit={137,402,631,777,1010,1150,470}
    cell=14; gap=3; dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:50px;color:#FAFAF7">1,248</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">accounts, watched</span></div>
        <span style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">7 moved today</span></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("it scans the whole market each morning and lights only what moved.")}</div>'''

# 7. CENTS - IVORY gauge: the needle parks in cents; the old stack sits in the dollar zone
def cents():
    cx,cy,R=306,300,215
    def pt(a,rr): return (cx+rr*math.cos(math.radians(a)), cy-rr*math.sin(math.radians(a)))
    lx,ly=pt(180,R); tx,ty=pt(90,R); rx,ry=pt(0,R)
    ticks=""
    for a in range(0,181,30):
        x1,y1=pt(a,R-6); x2,y2=pt(a,R-26)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(120,95,60,.4)" stroke-width="2"/>'
    nx,ny=pt(152,R-42)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 30px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">The old stack cost thousands</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PAY PER TOKEN</span></div>
      <svg width="612" height="360" viewBox="0 0 612 360" style="display:block;margin:0 auto">
        <path d="M{lx:.0f} {ly:.0f} A{R} {R} 0 0 1 {tx:.0f} {ty:.0f}" fill="none" stroke="#96562d" stroke-width="26" stroke-linecap="round"/>
        <path d="M{tx:.0f} {ty:.0f} A{R} {R} 0 0 1 {rx:.0f} {ry:.0f}" fill="none" stroke="rgba(200,70,35,.5)" stroke-width="26" stroke-linecap="round"/>
        {ticks}
        <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="60" fill="#2a2016">0.11c</text>
        <text x="{cx}" y="{cy-26}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".12em" fill="#96562d">PER RESEARCH BRIEF</text>
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="7" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#2a2016"/>
        <text x="{cx-150}" y="{cy+42}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#96562d">CENTS</text>
        <text x="{cx+150}" y="{cy+42}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb(200,70,35)">$1,000s</text>
      </svg>
      {cap("a full brief lands for cents. the seat license was the expensive part.","#8a745a")}</div>'''

# 8. OPERATOR - isometric stack of composed agent outputs assembled under one login
def operator():
    rows=[("CORTEX","brief ready"),("SPECTER","sequence drafted"),("STRIKER","deal scored"),("PULSE","post written")]
    cards=""
    for i,(a,b) in enumerate(rows):
        y=i*100
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:17px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{a}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{b}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Assemble the operator","ONE LOGIN")}
      <div style="perspective:1900px;height:480px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:440px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:404px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">One operator, one login</div></div></div>
      {cap("every agent, one shared memory, one gate. the whole system in one chat.")}</div>'''

PANELS={"frame":frame(),"roster":roster(),"router":router(),"signals":signals(),
        "sequence":sequence(),"proof":proof(),"cents":cents(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src02"; os.makedirs(outd,exist_ok=True)
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
