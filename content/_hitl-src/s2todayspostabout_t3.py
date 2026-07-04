#!/usr/bin/env python3
# TIER 3 - HIDDEN POWERS YOU OWN, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Reframe: the Ultron capabilities most founders never switch on (overnight, radar, gate, memory).
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None):
    tc=tagc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SWITCHES - a capability toggle board: 6 powers you own, most switched OFF (dim, knob left),
# two lit ON (accent track, knob right, glow). The "you already own these, turn them on" scene.
def switches():
    rows=[("OVERNIGHT FLOWS","drafts, scans, briefs by 07:00",True),
          ("SIGNAL RADAR","funding, hiring, intent",False),
          ("HUMAN GATE","approval before anything sends",True),
          ("SHARED MEMORY","one core, every agent",False),
          ("AGENT ROSTER","seven, one router",False),
          ("MODEL AUTO-ROUTE","the cheapest tier that fits",False)]
    items=""
    for nm,sub,on in rows:
        if on:
            track='background:linear-gradient(160deg,#e6b48f,rgb('+ACC+') 60%,#9a5a35);box-shadow:0 0 18px rgba(212,162,127,.45), inset 0 2px 3px rgba(255,255,255,.4)'
            knob='left:40px;background:#fdfaf5'
            state=f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({ACC})">ON</span>'
            nmc="#FAFAF7"
        else:
            track='background:rgba(250,250,247,.07);box-shadow:inset 0 2px 4px rgba(0,0,0,.5)'
            knob='left:4px;background:#6a655d'
            state='<span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#6f6a60">OFF</span>'
            nmc="#b8b2a6"
        items+=(f'<div style="display:flex;align-items:center;gap:20px;background:linear-gradient(160deg,#302c28,#211e1b);'
          f'border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:15px 22px;box-shadow:0 12px 22px rgba(0,0,0,.4), inset 0 1px 2px rgba(255,255,255,.06)">'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:{nmc}">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85;margin-top:1px">{sub}</div></div>'
          f'<div style="width:34px;text-align:right">{state}</div>'
          f'<div style="position:relative;flex-shrink:0;width:74px;height:36px;border-radius:19px;{track}">'
          f'<div style="position:absolute;top:4px;{knob};width:28px;height:28px;border-radius:50%;box-shadow:0 3px 6px rgba(0,0,0,.5)"></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You own nine. You run one.","CAPABILITIES")}
      <div style="display:flex;flex-direction:column;gap:13px">{items}</div>
      {cap("bought, dormant, one tap away. most founders never flip the switch.")}</div>'''

# 2. CLOCK - overnight clock: dark face, ticks, crescent moon, hands at 02:40, 3 glowing task blips,
# a right-side timeline of what ran through the night ending "done by 07:00".
def clock():
    cx,cy,R=205,215,180
    ticks=""
    for h in range(12):
        a=math.radians(h*30-90)
        x1=cx+(R-16)*math.cos(a); y1=cy+(R-16)*math.sin(a)
        x2=cx+(R-4)*math.cos(a); y2=cy+(R-4)*math.sin(a)
        w=4 if h%3==0 else 2
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.35)" stroke-width="{w}"/>'
    blips=""
    for h in (11,2,5):
        a=math.radians(h*30-90); bx=cx+(R-40)*math.cos(a); by=cy+(R-40)*math.sin(a)
        blips+=f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="9" fill="rgb({ACC})" filter="url(#bl)"/>'
    # hour hand ~2:40, minute hand ~40
    ha=math.radians(2.66*30-90); ma=math.radians(40*6-90)
    hx=cx+96*math.cos(ha); hy=cy+96*math.sin(ha); mx=cx+140*math.cos(ma); my=cy+140*math.sin(ma)
    tl=[("23:10","Outbound drafted"),("02:40","Signals scanned"),("05:20","Brief built, 1 page")]
    rows=""
    for t,lab in tl:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:16px">'
          f'<span style="font-family:DM Mono;font-size:16px;color:rgb({ACC});width:64px;flex-shrink:0">{t}</span>'
          f'<span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.7);flex-shrink:0"></span>'
          f'<span style="font-family:DM Sans;font-size:18px;color:#d9d5cc">{lab}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="410" height="410" viewBox="0 0 410 410">
        <defs><filter id="bl" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#151311" stroke="rgba(255,255,255,.08)" stroke-width="2"/>
        {ticks}
        <g><circle cx="{cx+92}" cy="{cy-96}" r="30" fill="#d4c3a6"/><circle cx="{cx+104}" cy="{cy-104}" r="26" fill="#151311"/></g>
        <line x1="{cx}" y1="{cy}" x2="{hx:.0f}" y2="{hy:.0f}" stroke="#e2dccf" stroke-width="7" stroke-linecap="round"/>
        <line x1="{cx}" y1="{cy}" x2="{mx:.0f}" y2="{my:.0f}" stroke="rgb({ACC})" stroke-width="4.5" stroke-linecap="round"/>
        {blips}
        <circle cx="{cx}" cy="{cy}" r="8" fill="rgb({ACC})"/>
      </svg>
      <div style="flex:1">
        {htitle("It works the night shift","OVERNIGHT")}
        {rows}
        <div style="border-top:1px solid rgba(255,255,255,.08);margin-top:8px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">Done by 07:00</div>
        {cap("you never clocked it in. it ran while you slept.")}
      </div></div>'''

# 3. RADAR - signal radar sweep, 4 ranked blips, right readout: saw the round 3 days ahead.
def radar():
    cx,cy,R=205,215,185
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (62,123,185))
    blips=[("Funding",305,150),("Hiring",120,96),("Stack",210,162),("Intent",40,118)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">You + Ultron</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">Tue 09:12</span></div>'
      '<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">Your VC</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">Fri 16:40</span></div>'
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
        {htitle("It saw the round first","SIGNAL RADAR")}
        {lead}
        {cap("funding, hiring, stack, intent - a radar you never switched on.")}
      </div></div>'''

# 4. GRAPH - node graph: one router hub on the left fans bezier wires out to 5 named agents.
def graph():
    W,H=820,430
    hubx,hy=150,215
    agents=[("CORTEX","research",64),("SPECTER","outbound",150),("STRIKER","deals",236),("PULSE","content",322),("SENTINEL","code",408)]
    ny0,ny1=40,390; ncount=len(agents)
    edges=""; nodes=""
    for i,(nm,role,_) in enumerate(agents):
        y=ny0+(ny1-ny0)*i/(ncount-1)
        mx=(hubx+560)/2
        edges+=f'<path d="M{hubx+62} {hy} C{mx:.0f} {hy},{mx:.0f} {y:.0f},556 {y:.0f}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
        nodes+=(f'<rect x="558" y="{y-32:.0f}" width="228" height="64" rx="16" fill="#242019" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="580" y="{y-3:.0f}" font-family="DM Sans" font-weight="800" font-size="20" fill="#FAFAF7">{nm}</text>'
          f'<text x="580" y="{y+19:.0f}" font-family="DM Sans" font-size="14" fill="#8f8f85">{role}</text>'
          f'<circle cx="770" cy="{y:.0f}" r="5.5" fill="rgb({ACC})"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one wire","AGENT ROSTER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}
        <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="62" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        {nodes}
      </svg>
      {cap("you called one. the router hands each job to the right agent.")}</div>'''

# 5. STACK (IVORY) - isometric stack of overnight-yield cards, a delivered badge pinned at the base.
def stack():
    steps=[("12 follow-ups drafted","SPECTER, in your voice",0),("47 accounts scored","CORTEX, ranked by fit",1),("1-page brief built","overnight, sourced",2)]
    cards=""
    for main,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#463d34,#2f2820);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(74,52,32,.4), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:21px;color:#FAFAF7">{main}</div><div style="font-family:DM Sans;font-size:15px;color:#cbbfa8">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 44px 34px">
      {htitle("You wake to results","OVERNIGHT YIELD","#2a2016","#96562d")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:120px;top:396px;background:#96562d;color:#fdfaf5;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(150,86,45,.4)">Delivered &#10003; 07:00</div></div></div>
      {cap("not a blank cursor. briefs, drafts and scores stacked by morning, for cents.","#8a745a")}</div>'''

# 6. GAUGE (IVORY) - semicircular cost gauge (polyline arcs, robust), needle parked in cents zone.
def gauge():
    cx,cy,R=310,265,205
    def pt(A,rr):
        a=math.radians(A); return cx+rr*math.cos(a), cy-rr*math.sin(a)
    def poly(a0,a1):
        n=48; pts=[pt(a0+(a1-a0)*i/n,R) for i in range(n+1)]
        return "M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)
    ndeg=162; nx,ny=pt(ndeg,R-30)
    labels=""
    for A,txt,c in [(176,"cents","#96562d"),(90,"$","#8a745a"),(4,"$$$","#8a745a")]:
        lx,ly=pt(A,R+24); labels+=f'<text x="{lx:.0f}" y="{ly+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="16" fill="{c}">{txt}</text>'
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 30px">
      {htitle("A night of work, for cents","PAY PER TOKEN","#2a2016","#96562d")}
      <svg width="620" height="330" viewBox="0 0 620 330" style="display:block;margin:0 auto">
        <path d="{poly(180,0)}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="26" stroke-linecap="round"/>
        <path d="{poly(180,152)}" fill="none" stroke="#96562d" stroke-width="26" stroke-linecap="round"/>
        {labels}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="8" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#2a2016"/>
        <text x="{cx}" y="{cy-56}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="72" fill="#2a2016">0.11c</text>
        <text x="{cx}" y="{cy-22}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#96562d" letter-spacing=".08em">PER OVERNIGHT RUN</text>
      </svg>
      {cap("pay per token, not per seat. the tools it replaces bill hundreds a month.","#8a745a")}</div>'''

# 7. FIELD - dot field of 1,284 companies watched, a handful lit as this morning's movers.
def field():
    cols,rowsn=48,27
    lit={137,402,631,888,1045,1190,760}
    dots=""; cell=15; gap=3
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">1,284</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">companies, watched</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">7 moved today</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("one by hand, thousands on watch - flagged before you open the laptop.")}</div>'''

# 8. HUB - radial memory core: one lit orb feeds 5 capability spokes; off, each agent starts blind.
def hub():
    cx,cy=306,208
    nodes=[("ICP",-90),("PIPELINE",-18),("PRICING",54),("DOCS",126),("VOICE",198)]
    lines=""; blocks=""
    for nm,a in nodes:
        x=cx+156*math.cos(math.radians(a)); y=cy+156*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        blocks+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".05em" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Turn on the memory","SHARED CORE")}
      <svg width="612" height="440" viewBox="0 0 612 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">MEMORY</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one core</text>
        {blocks}
      </svg>
      {cap("icp, pipeline, pricing, docs - off, and every agent starts blind.")}</div>'''

PANELS={"switches":switches(),"clock":clock(),"radar":radar(),"graph":graph(),
        "stack":stack(),"gauge":gauge(),"field":field(),"hub":hub()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2todayspostabout"; os.makedirs(outd,exist_ok=True)
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
