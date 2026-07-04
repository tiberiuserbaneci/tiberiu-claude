#!/usr/bin/env python3
# TIER 3 - IT STUDIED MY BEST POSTS, built to the WIRE-ITS-EYES / AI-BODY bar: each of the 8 panels
# is a UNIQUE hand-coded scene filling a clean rounded card, htitle + one mono caption, NO stat-chip
# strips, no clip-path cuts, no extruded walls. 8 distinct scene types (iso stack, pattern extraction,
# bar autopsy, radial hub, gauge, timeline, dot field, node graph). Warm palette only. Prices in cents.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
BAD="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def ivtitle(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. ARCHIVE - isometric stack of your real winning post cards, save counts pinned
def archive():
    posts=[("Why I killed 9 sales tools","11,619 views","Mar 04","92"),
           ("I gave Claude 12,400 accounts","8,204 views","Apr 11","74"),
           ("The cold email that booked 7","6,010 views","May 02","63")]
    cards=""
    for i,(t,v,d,s) in enumerate(posts):
        y=i*146
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;'
          f'background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;padding:20px 24px;'
          f'box-shadow:0 32px 48px rgba(0,0,0,.58), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Sans\';font-weight:800;font-size:23px;color:#FAFAF7">{t}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:13.5px;color:#a8a296;margin-top:6px">{v} &middot; posted {d}</div></div>'
          f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 16px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:#1a0f0a;line-height:1">{s}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">SAVES</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 38px">
      {htitle("The goldmine behind you","YOUR ARCHIVE")}
      <div style="perspective:2000px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-9deg);width:580px;height:410px;position:relative">{cards}</div></div>
      {cap("fifty posts that already worked, sitting unused in your profile.")}</div>'''

# 2. EXTRACT - IVORY: a raw winner post on the left, its parts pulled into structured attribute chips
def extract():
    fields=[("OPENER","Most founders never","short, blunt"),
            ("NUMBER","7 booked meetings","one, exact"),
            ("CLOSE","So which are you?","a question"),
            ("LENGTH","58 words","under 62")]
    chips=""
    for lab,val,note in fields:
        chips+=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:12px 16px">'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-weight:500;font-size:11.5px;letter-spacing:.12em;color:#96562d;width:66px">{lab}</span>'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#2a2016">{val}</span>'
          f'<span style="flex-shrink:0;font-family:\'DM Sans\';font-size:14px;color:#8a745a">{note}</span></div>')
    raw=('<div style="background:rgba(255,255,255,.72);border:1px solid rgba(150,90,45,.22);border-radius:16px;padding:20px 22px;box-shadow:inset 0 2px 3px rgba(255,255,255,.9)">'
      '<div style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.14em;color:#96562d;margin-bottom:12px">WINNER &middot; 92 SAVES</div>'
      '<div style="font-family:\'DM Sans\';font-size:19px;color:#2a2016;line-height:1.5">'
      '<span style="background:rgba(150,90,45,.16);border-radius:4px;padding:1px 4px">Most founders never</span> read why the rare cold emails land. '
      'I sent 200 and <span style="background:rgba(150,90,45,.16);border-radius:4px;padding:1px 4px">7 booked meetings</span>. '
      '<span style="background:rgba(150,90,45,.16);border-radius:4px;padding:1px 4px">So which are you?</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {ivtitle("Pulled into parts","EXTRACT")}
      <div style="display:flex;align-items:stretch;gap:26px">
        <div style="flex:1;display:flex;align-items:center">{raw}</div>
        <div style="flex-shrink:0;display:flex;align-items:center;color:#96562d">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
        <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px">{chips}</div>
      </div>
      {cap("the desk collects your top posts with their numbers attached.","#8a745a")}</div>'''

# 3. AUTOPSY - horizontal bars: what the data says vs where my taste guessed (dashed marker)
def autopsy():
    rows=[("Short openers",89,40),("One number per post",76,55),("Questions that end",71,34),("Long context blocks",18,66)]
    TR=720
    bars=""
    for nm,data,taste in rows:
        wrong=abs(data-taste)>30
        col=f"rgb({BAD})" if wrong else f"rgb({ACC})"
        note="my taste was off" if wrong else "confirmed"
        dfill=data/100*TR; mx=taste/100*TR
        bars+=(f'<div style="margin-bottom:20px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px">'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#FAFAF7">{nm}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:13px;color:{col}">{note}</span></div>'
          f'<div style="position:relative;width:{TR}px;height:26px;background:rgba(250,250,247,.06);border-radius:8px">'
          f'<div style="position:absolute;left:0;top:0;height:26px;width:{dfill:.0f}px;background:linear-gradient(90deg,rgba({ACC},.55),rgb({ACC}));border-radius:8px"></div>'
          f'<div style="position:absolute;left:{dfill-44:.0f}px;top:2px;font-family:\'DM Sans\';font-weight:900;font-size:15px;color:#1a0f0a">{data}%</div>'
          f'<div style="position:absolute;left:{mx:.0f}px;top:-6px;width:0;height:38px;border-left:2px dashed {col}"></div>'
          f'<div style="position:absolute;left:{mx-14:.0f}px;top:-24px;font-family:\'DM Mono\';font-size:11px;color:{col}">taste</div>'
          f'</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Data vs my taste","AUTOPSY")}
      {bars}
      {cap("short openers, one number, questions that end. the data disagreed with my taste.")}</div>'''

# 4. DISTILL - radial hub: 5 findings converge into one installed SKILL core
def distill():
    cx,cy=215,215
    finds=[("hook",-90),("1 number",-18),("question",54),("no hedge",126),("short",198)]
    lines=""; nodes=""
    for nm,a in finds:
        x=cx+158*math.cos(math.radians(a)); y=cy+158*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#d9d3c6">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="440" height="440" viewBox="0 0 440 440">
        <defs><radialGradient id="sk" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="skg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}{nodes}<g filter="url(#skg)"><circle cx="{cx}" cy="{cy}" r="64" fill="url(#sk)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">SKILL</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">installed</text></svg>
      <div style="flex:1">
        {htitle("Findings become a play","DISTILLED")}
        <div style="font-family:'DM Sans';font-size:19px;color:#c9c3b8;line-height:1.45">Five patterns, one file. Not notes in a doc, a play the desk runs on every future draft, automatically.</div>
        {cap("insight made executable: the winning rules, installed once.")}</div></div>'''

# 5. FIFTY1 - IVORY gauge: the 51st draft scored against your winners + a ranked candidate list
def fifty1():
    pct=94; r=74; circ=2*math.pi*r; dash=circ*pct/100
    cands=[("Draft A",94,True),("Draft C",88,False),("Draft B",81,False),("Draft D",73,False)]
    rows=""
    for nm,sc,top in cands:
        bg="rgba(150,90,45,.14)" if top else "rgba(255,255,255,.5)"
        bd="#96562d" if top else "rgba(150,90,45,.14)"
        tag='<span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:#96562d;margin-left:8px">PICKED</span>' if top else ''
        rows+=(f'<div style="display:flex;align-items:center;gap:12px;background:{bg};border:1px solid {bd};border-radius:12px;padding:11px 16px;margin-bottom:9px">'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:700;font-size:17px;color:#2a2016">{nm}{tag}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:#96562d">{sc}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {ivtitle("Ranked before I saw it","51ST DRAFT")}
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:200px;height:200px">
          <svg width="200" height="200" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 100 100)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:46px;color:#2a2016">{pct}</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">match to winners</span></div></div>
        <div style="flex:1">{rows}</div>
      </div>
      {cap("drafted against my own winning patterns, ranked before I saw it.","#8a745a")}</div>'''

# 6. REFRESH - monthly timeline: corpus grows, skill version bumps each run
def refresh():
    steps=[("APR","50",110,"v1"),("MAY","54",148,"v2"),("JUN","61",206,"v3"),("JUL","68",260,"v4")]
    W,H=760,340; base=290; x0=90; gap=(W-2*x0)/(len(steps)-1)
    line=f'<line x1="{x0}" y1="{base}" x2="{W-x0}" y2="{base}" stroke="rgba(212,162,127,.3)" stroke-width="2.5"/>'
    body=""
    for i,(m,n,bh,v) in enumerate(steps):
        x=x0+i*gap; on=(i==len(steps)-1)
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.55)"
        body+=(f'<rect x="{x-32:.0f}" y="{base-bh}" width="64" height="{bh}" rx="10" fill="{col}" opacity="{0.95 if on else 0.5}"/>'
          f'<text x="{x:.0f}" y="{base-bh+30}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#1a0f0a">{n}</text>'
          f'<text x="{x:.0f}" y="{base-bh-14}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">skill {v}</text>'
          f'<circle cx="{x:.0f}" cy="{base}" r="7" fill="{col}"/>'
          f'<text x="{x:.0f}" y="{base+34}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".14em" fill="#a8a296">{m}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The study reruns","REFRESH · MONTHLY")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">{line}{body}
        <text x="{x0}" y="40" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#8f8f85">POSTS IN CORPUS</text></svg>
      {cap("new winners join the corpus; the skill updates itself with fresh patterns.")}</div>'''

# 7. MOAT8 - dot field: your 50-post archive, the winners lit; generic AI has none of it
def moat8():
    cols,rows=10,5; lit={2,7,11,14,19,23,28,31,36,40,44,47}
    cell,gap=60,15; dots=""
    for i in range(cols*rows):
        rr,cc=divmod(i,cols); x=cc*(cell+gap); y=rr*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="12" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="12" fill="rgba(250,250,247,.07)" stroke="rgba(250,250,247,.06)"/>'
    fw=cols*(cell+gap)-gap; fh=rows*(cell+gap)-gap
    legend=('<div style="display:flex;gap:28px;margin-top:20px">'
      f'<div style="display:flex;align-items:center;gap:10px"><span style="width:16px;height:16px;border-radius:5px;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.6)"></span><span style="font-family:DM Sans;font-size:16px;color:#d9d5cc">12 winners you own</span></div>'
      '<div style="display:flex;align-items:center;gap:10px"><span style="width:16px;height:16px;border-radius:5px;background:rgba(250,250,247,.09)"></span><span style="font-family:DM Sans;font-size:16px;color:#8f8f85">the rest of your history</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nobody owns your field","THE MOAT")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {dots}</svg>
      {legend}
      {cap("generic AI writes averages. this writes from evidence only you own.")}</div>'''

# 8. ORDER8 - node graph: corpus -> [1 STUDY] -> [2 GENERATE] -> post, the reversed order struck out
def order8():
    W,H=820,430
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Study, then generate","THE ORDER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="n1" cx="38%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <radialGradient id="n2" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <!-- reversed order, subordinated + struck -->
        <text x="410" y="46" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#7a7468">MOST PEOPLE: GENERATE, THEN HOPE</text>
        <line x1="248" y1="40" x2="572" y2="40" stroke="rgb({BAD})" stroke-width="2"/>
        <!-- corpus -->
        <rect x="34" y="176" width="130" height="78" rx="16" fill="#221f1b" stroke="rgba(255,255,255,.1)"/>
        <text x="99" y="210" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#e2dccf">archive</text>
        <text x="99" y="234" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">50 posts</text>
        <path d="M164 215 C210 215,220 195,244 195" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3"/>
        <!-- 1 STUDY -->
        <g filter="url(#ng)"><circle cx="330" cy="195" r="86" fill="url(#n1)"/></g>
        <text x="330" y="176" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#2a160c">STEP 1</text>
        <text x="330" y="208" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">STUDY</text>
        <text x="330" y="230" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">learn the winners</text>
        <path d="M416 195 H500" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round"/>
        <polygon points="500,187 516,195 500,203" fill="rgb({ACC})"/>
        <!-- 2 GENERATE -->
        <g filter="url(#ng)"><circle cx="602" cy="195" r="86" fill="url(#n2)"/></g>
        <text x="602" y="176" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#2a160c">STEP 2</text>
        <text x="602" y="208" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">GENERATE</text>
        <text x="602" y="230" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">write from evidence</text>
        <path d="M688 215 C724 215,732 300,764 300" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3"/>
        <rect x="690" y="272" width="118" height="70" rx="16" fill="#221f1b" stroke="rgba(212,162,127,.3)"/>
        <text x="749" y="304" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">the 51st</text>
        <text x="749" y="326" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">your best</text>
      </svg>
      {cap("most people ask AI to write. operators make it learn, then write.")}</div>'''

PANELS={"archive":archive(),"extract":extract(),"autopsy":autopsy(),"distill":distill(),
        "fifty1":fifty1(),"refresh":refresh(),"moat8":moat8(),"order8":order8()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/studyyou"; os.makedirs(outd,exist_ok=True)
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
