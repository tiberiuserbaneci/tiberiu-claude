#!/usr/bin/env python3
# TIER 3 - THE FIFTEEN-HOUR AUDIT, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Angle: a per-task time map. The recurring founder tasks that eat 16 hrs a week, each handed to a
# named Ultron agent, itemized and given back. Hero = the weekly time-audit breakdown.
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
def htitleiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. AUDIT (HERO) - the weekly time-audit: your 44h week, the 16 reclaimable hours split into 7
# task segments, itemized. Scene = stacked horizontal time-map + legend. No two other panels share it.
def audit():
    tasks=[("CORTEX","research",4,.96),("SPECTER","outbound",3,.84),("PULSE","content",3,.72),
           ("STRIKER","deals",2,.62),("SENTINEL","code",2,.52),("AMPLIFY","publish",1,.44),("COUNSEL","legal",1,.38)]
    barW=816
    # Row A - the whole 44h week, right 16h reclaimable
    unitA=barW/44.0; reclaim=unitA*16
    rowA=(f'<div style="position:relative;height:46px;border-radius:11px;overflow:hidden;background:rgba(250,250,247,.06);display:flex">'
          f'<div style="width:{barW-reclaim:.0f}px;height:100%;background:rgba(250,250,247,.05);display:flex;align-items:center;padding-left:18px">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#6f6a60">BUSYWORK &middot; 28 HRS</span></div>'
          f'<div style="flex:1;height:100%;background:rgba(212,162,127,.18);border-left:2px solid rgb({ACC});display:flex;align-items:center;justify-content:center">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">RECLAIMABLE &middot; 16 HRS</span></div></div>')
    # Row B - the 16h itemized into 7 task segments
    unitB=barW/16.0; segs=""
    for nm,role,h,op in tasks:
        w=unitB*h; big=w>92
        inner=""
        if big: inner+=f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:#1a0f0a">{nm}</span>'
        inner+=f'<span style="font-family:DM Sans;font-weight:900;font-size:{24 if big else 17}px;color:#1a0f0a;line-height:1">{h}h</span>'
        segs+=(f'<div style="width:{w:.0f}px;height:78px;background:rgba(212,162,127,{op});border-right:2px solid #1d1d1b;'
               f'display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px">{inner}</div>')
    rowB=f'<div style="display:flex;border-radius:11px;overflow:hidden;box-shadow:0 16px 30px rgba(0,0,0,.5)">{segs}</div>'
    # legend of the 7 tasks
    leg=""
    for nm,role,h,op in tasks:
        leg+=(f'<div style="display:flex;align-items:center;gap:9px">'
              f'<span style="width:13px;height:13px;border-radius:4px;background:rgba(212,162,127,{op});flex-shrink:0"></span>'
              f'<span style="font-family:DM Mono;font-size:13px;color:#c9c3b8">{nm}</span>'
              f'<span style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</span></div>')
    legend=f'<div style="display:flex;flex-wrap:wrap;gap:14px 26px;margin-top:20px">{leg}</div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Sixteen hours, itemized","THE AUDIT")}
      <div style="display:flex;flex-direction:column;gap:16px">{rowA}{rowB}</div>
      {legend}
      {cap("your 44-hour week, the 16 hours a system does, mapped to the task that eats them.")}</div>'''

# 2. CORTEX - research 4h: isometric stack of ranked account briefs (Monday prospecting, done)
def cortex():
    rows=[("Northwind Robotics","hiring 3 ops roles","94"),
          ("Globex Systems","raised $4M in May","89"),
          ("Initech Labs","no AI layer yet","82")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*146
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#413b35,#2b2723);'
          f'border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:20px 24px;'
          f'box-shadow:0 32px 48px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:23px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#a8a296;margin-top:2px">{b}</div></div>'
          f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:8px 15px;border-radius:12px;box-shadow:0 6px 14px rgba(212,162,127,.4)">'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:#1a0f0a;line-height:1">{c}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:9px;letter-spacing:.1em;color:rgba(26,15,10,.7)">RANK</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("Prospecting, already ranked","CORTEX &middot; 4 HRS")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:560px;height:432px;position:relative">{cards}</div></div>
      {cap("four hours of tabs and note-taking, returned as one ranked brief before coffee.")}</div>'''

# 3. SPECTER - outbound 3h: a sequence timeline, contact node -> 4 scheduled sends -> a reply badge
def specter():
    W,H=820,430
    stops=[("Day 1","intro",150),("Day 3","nudge",320),("Day 6","value",490),("Day 10","break-up",660)]
    y=150; edges=""; nodes=""
    prevx=70
    for lab,kind,x in stops:
        edges+=f'<path d="M{prevx} {y} C{(prevx+x)/2:.0f} {y},{(prevx+x)/2:.0f} {y},{x-30} {y}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=(f'<g><rect x="{x-30}" y="{y-30}" width="60" height="60" rx="14" fill="#2a2724" stroke="rgba(212,162,127,.4)"/>'
          f'<path d="M{x-16} {y-8} h32 v18 h-32Z M{x-16} {y-8} l16 12 l16 -12" fill="none" stroke="rgb({ACC})" stroke-width="2.2" stroke-linejoin="round"/>'
          f'<text x="{x}" y="{y-46}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#d9d5cc">{lab}</text>'
          f'<text x="{x}" y="{y+58}" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#8f8f85">{kind}</text></g>')
        prevx=x
    # reply badge dropping from the Day 6 stop
    reply=(f'<path d="M490 180 C490 250,610 250,610 316" stroke="rgba(212,162,127,.4)" stroke-width="2.5" stroke-dasharray="5 7" fill="none"/>'
      f'<g filter="url(#rg)"><rect x="510" y="316" width="200" height="72" rx="16" fill="linear"/></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The follow-ups run themselves","SPECTER &middot; 3 HRS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><filter id="rg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="rgba(0,0,0,.5)"/></filter></defs>
        {edges}{nodes}
        <path d="M490 180 C490 250,610 250,610 312" stroke="rgba(212,162,127,.45)" stroke-width="2.5" stroke-dasharray="5 7" fill="none"/>
        <rect x="486" y="312" width="248" height="84" rx="18" fill="url(#replyg)" stroke="rgb({ACC})" stroke-width="2"/>
        <defs><linearGradient id="replyg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#241f1a"/></linearGradient></defs>
        <text x="610" y="348" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="rgb({ACC})">Replied</text>
        <text x="610" y="374" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#a8a296">meeting booked</text>
      </svg>
      {cap("four-step sequences, written and timed for every prospect, three hours a week gone.")}</div>'''

# 4. PULSE - content 3h (IVORY): one idea fanning out into every channel (atomizer fan)
def pulse():
    cx,cy=150,236
    chans=[("LinkedIn",-40),("TikTok",-13),("Instagram",14),("Newsletter",41)]
    fan=""; chips=""
    for i,(nm,ang) in enumerate(chans):
        ex=cx+300*math.cos(math.radians(ang)); ey=cy+300*math.sin(math.radians(ang))
        fan+=f'<path d="M{cx+42} {cy} C{cx+180} {cy},{ex-150:.0f} {ey:.0f},{ex-14:.0f} {ey:.0f}" stroke="rgba(150,86,45,.42)" stroke-width="2.4" fill="none"/>'
        chips+=(f'<div style="position:absolute;left:{ex-6:.0f}px;top:{ey-24:.0f}px;background:rgba(255,255,255,.72);border:1px solid rgba(150,90,45,.28);'
          f'border-radius:12px;padding:10px 18px;box-shadow:0 10px 20px rgba(120,90,55,.16);font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#2a2016;white-space:nowrap">{nm}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitleiv("One idea, every channel","PULSE &middot; 3 HRS")}
      <div style="position:relative;height:472px">
        <svg width="560" height="472" viewBox="0 0 560 472" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="idea" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="#c8794f"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
          <filter id="ig2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="rgba(150,90,45,.4)"/></filter></defs>
          {fan}
          <g filter="url(#ig2)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#idea)"/></g>
          <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#fdfbf6">1</text>
          <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#fdf3e8">idea</text>
        </svg>
        {chips}
      </div>
      {cap("one operator note, reshaped in your voice for four feeds, three hours reclaimed.","#8a745a")}</div>'''

# 5. STRIKER - deals 2h: a downward funnel of deal stages narrowing to a close
def striker():
    stages=[("DISCOVERY","questions drafted",760,150),("QUALIFY","budget + timeline",600,220),
            ("PROPOSAL","priced + sent",440,290),("CLOSE","signed",280,360)]
    W,H=820,430; cx=410; segs=""
    for nm,sub,w,y in stages:
        segs+=(f'<g><rect x="{cx-w/2:.0f}" y="{y-28}" width="{w}" height="56" rx="12" fill="url(#fn)" stroke="rgba(212,162,127,.35)"/>'
          f'<text x="{cx-w/2+22:.0f}" y="{y-2}" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="rgb({ACC})">{nm}</text>'
          f'<text x="{cx-w/2+22:.0f}" y="{y+18}" font-family="DM Sans" font-size="15" fill="#a8a296">{sub}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Discovery prep, handled","STRIKER &middot; 2 HRS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><linearGradient id="fn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a342d"/><stop offset="100%" stop-color="#241f1a"/></linearGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {segs}
        <g filter="url(#cg)"><circle cx="{cx}" cy="360" r="30" fill="none"/></g>
      </svg>
      {cap("qualification, objections and the proposal drafted for you, two hours off every deal.")}</div>'''

# 6. SENTINEL - code 2h: a week of shipped fixes as an area line-chart ending in a merged badge
def sentinel():
    W,H=760,360
    pts=[(40,300),(150,250),(260,270),(370,180),(480,200),(590,120),(700,90)]
    line=" ".join(f"{x},{y}" for x,y in pts)
    area=f"40,320 "+line+f" 700,320"
    dots="".join(f'<circle cx="{x}" cy="{y}" r="6" fill="rgb({ACC})" filter="url(#dg)"/>' for x,y in pts)
    grid="".join(f'<line x1="40" y1="{y}" x2="700" y2="{y}" stroke="rgba(255,255,255,.05)"/>' for y in (110,180,250,320))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Fixes shipped from a sentence","SENTINEL &middot; 2 HRS")}
      <div style="position:relative">
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.32)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
        <filter id="dg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {grid}
        <polygon points="{area}" fill="url(#ar)"/>
        <polyline points="{line}" fill="none" stroke="rgb({ACC})" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
        {dots}
        <text x="40" y="350" font-family="DM Mono" font-size="13" fill="#7a746a">MON</text>
        <text x="672" y="350" font-family="DM Mono" font-size="13" fill="#7a746a">SUN</text>
      </svg>
      <div style="position:absolute;right:34px;top:6px;background:rgb({ACC});color:#1a0f0a;font-family:\'DM Sans\';font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">14 merged &#10003;</div>
      </div>
      {cap("dashboards, fixes and automations described in plain english, tested before they land.")}</div>'''

# 7. AMPLIFY + COUNSEL - the last 2h: twin meters, one scheduled, one reviewed
def routine():
    def meter(tag,agent,big,sub,icon):
        return (f'<div style="flex:1;background:linear-gradient(160deg,#332f2a,#211e1a);border:1.5px solid rgba(255,255,255,.10);'
          f'border-radius:22px;padding:26px 28px;box-shadow:0 26px 44px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">'
          f'<div style="width:46px;height:46px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">{icon}</div>'
          f'<div><div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{agent}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:16px;color:#a8a296">{tag}</div></div></div>'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:52px;color:#FAFAF7;line-height:1">{big}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:16px;color:#8f8f85;margin-top:6px">{sub}</div></div>')
    cal=f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><rect x="3" y="4.5" width="18" height="16" rx="2.5"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="8" y1="2.5" x2="8" y2="6.5"/><line x1="16" y1="2.5" x2="16" y2="6.5"/></svg>'
    doc=f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><path d="M7 3h7l4 4v14H7Z"/><line x1="10" y1="12" x2="16" y2="12"/><line x1="10" y1="16" x2="16" y2="16"/></svg>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {htitle("The last two hours","AMPLIFY + COUNSEL")}
      <div style="display:flex;gap:22px;margin-top:6px">
        {meter("PUBLISHING","AMPLIFY","12","posts formatted and scheduled per channel",cal)}
        {meter("LEGAL REVIEW","COUNSEL","3","NDAs and an MSA flagged, clause by clause",doc)}
      </div>
      {cap("formatting, scheduling and contract review, the quiet two hours nobody sees.")}</div>'''

# 8. GIVE-BACK (IVORY) - where the 16 hours go: a donut split into three destinations
def giveback():
    cx,cy,r=175,215,120; sw=52; circ=2*math.pi*r
    parts=[("Selling",8,"#c8794f"),("Building",5,"#d4a27f"),("Off the clock",3,"#e6c9ac")]
    total=16; off=0; arcs=""; leg=""
    for nm,h,col in parts:
        frac=h/total; dash=circ*frac
        arcs+=(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}" '
          f'stroke-dasharray="{dash:.1f} {circ-dash:.1f}" stroke-dashoffset="{-off:.1f}" transform="rotate(-90 {cx} {cy})"/>')
        off+=dash
        leg+=(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">'
          f'<span style="width:16px;height:16px;border-radius:5px;background:{col};flex-shrink:0"></span>'
          f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#2a2016;flex:1">{nm}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:#96562d">{h}h</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;align-items:center;gap:30px">
      <svg width="350" height="430" viewBox="0 0 350 430">
        {arcs}
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="46" fill="#2a2016">16h</text>
        <text x="{cx}" y="{cy+24}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#96562d">GIVEN BACK</text>
      </svg>
      <div style="flex:1">
        {htitleiv("Where the hours went","GIVEN BACK")}
        {leg}
        {cap("the 16 hours do not vanish, they move to the work only you can do.","#8a745a")}
      </div></div>'''

PANELS={"audit":audit(),"cortex":cortex(),"specter":specter(),"pulse":pulse(),
        "striker":striker(),"sentinel":sentinel(),"routine":routine(),"giveback":giveback()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src54"; os.makedirs(outd,exist_ok=True)
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
