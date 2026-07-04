#!/usr/bin/env python3
# TIER 3 - MONETIZE WHAT EXISTS, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Reframe: you already own the inputs - Ultron turns what you have into revenue, one system.
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
def htiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. ASSETS - IVORY front-flat inventory manifest: the inputs you already own, each marked OWNED
def assets():
    G={
      "doc":'<rect x="7" y="3" width="26" height="34" rx="4" fill="none" stroke="#96562d" stroke-width="2.6"/><line x1="13" y1="13" x2="27" y2="13" stroke="#96562d" stroke-width="2.6"/><line x1="13" y1="21" x2="27" y2="21" stroke="#96562d" stroke-width="2.6"/><line x1="13" y1="29" x2="22" y2="29" stroke="#96562d" stroke-width="2.6"/>',
      "people":'<circle cx="14" cy="14" r="7" fill="none" stroke="#96562d" stroke-width="2.6"/><circle cx="28" cy="16" r="6" fill="none" stroke="#96562d" stroke-width="2.4"/><path d="M4 36 c0-9 6-13 10-13 s10 4 10 13" fill="none" stroke="#96562d" stroke-width="2.6"/><path d="M23 36 c0-7 4-11 6-11 s7 3 7 11" fill="none" stroke="#96562d" stroke-width="2.4"/>',
      "tag":'<path d="M6 6 h16 l16 16 -16 16 -16 -16 Z" fill="none" stroke="#96562d" stroke-width="2.6"/><circle cx="15" cy="15" r="4" fill="#96562d"/>'}
    items=[("EXPERTISE","what you already know","doc"),
           ("CONTACTS","the list already in your phone","people"),
           ("OFFER","the thing you already sell","tag")]
    rows=""
    for nm,sub,g in items:
        rows+=f'''<div style="display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.55);
          border:1px solid rgba(150,90,45,.18);border-radius:18px;padding:19px 24px;
          box-shadow:0 10px 22px rgba(120,95,60,.10), inset 0 2px 2px rgba(255,255,255,.8)">
          <div style="flex-shrink:0;width:60px;height:60px;border-radius:15px;background:rgba(150,90,45,.10);
            border:1px solid rgba(150,90,45,.22);display:flex;align-items:center;justify-content:center">
            <svg width="42" height="42" viewBox="0 0 42 42">{G[g]}</svg></div>
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:23px;color:#2a2016">{nm}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#8a745a;margin-top:1px">{sub}</div></div>
          <div style="flex-shrink:0;display:flex;align-items:center;gap:9px;background:rgba(150,90,45,.10);
            border:1px solid rgba(150,90,45,.30);border-radius:999px;padding:8px 16px">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>
            <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:#96562d">OWNED</span></div>
        </div>'''
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htiv("The inventory is already yours","ASSET MANIFEST")}
      <div style="display:flex;flex-direction:column;gap:15px">{rows}</div>
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-top:18px;padding-top:16px;border-top:1px solid rgba(150,90,45,.20)">
        <span style="font-family:'DM Sans';font-weight:900;font-size:32px;color:#2a2016">3 / 3 <span style="font-size:19px;color:#8a745a;font-weight:700">in stock</span></span>
        <span style="font-family:'DM Mono';font-size:14px;color:#96562d;letter-spacing:.04em">nothing left to invent</span></div>
      {cap("you are not missing an idea. you are missing the system to run what you already have.","#8a745a")}</div>'''

# 2. PATH - horizontal revenue rail: ASSET -> AGENT -> OUTBOUND -> FIRST $, dated milestones
def path():
    steps=[("ASSET","what you own","Day 0"),("AGENT","put on the job","Day 1"),
           ("OUTBOUND","in your voice","Day 2"),("FIRST $","booked","Day 5")]
    W,H=820,300; x0,x1=100,720; n=len(steps); gap=(x1-x0)/(n-1); y=158
    nodes=""
    for i,(nm,sub,day) in enumerate(steps):
        x=x0+i*gap; last=(i==n-1); r=34 if last else 22
        fill="url(#endc)" if last else "#2a2724"
        nodes+=f'<circle cx="{x:.0f}" cy="{y}" r="{r}" fill="{fill}" stroke="rgb({ACC})" stroke-width="{3 if last else 2}"/>'
        if last:
            nodes+=f'<circle cx="{x:.0f}" cy="{y}" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="3" filter="url(#eg)"/>'
            nodes+=f'<text x="{x:.0f}" y="{y+9}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#1a0f0a">$</text>'
        else:
            nodes+=f'<text x="{x:.0f}" y="{y+7}" text-anchor="middle" font-family="DM Mono" font-size="16" fill="rgb({ACC})">{i+1}</text>'
        nodes+=f'<text x="{x:.0f}" y="{y-52}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{nm}</text>'
        nodes+=f'<text x="{x:.0f}" y="{y-30}" text-anchor="middle" font-family="DM Sans" font-size="13.5" fill="#8f8f85">{sub}</text>'
        nodes+=f'<text x="{x:.0f}" y="{y+58}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})">{day}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("From what you have to paid","REVENUE PATH")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="endc" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="eg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
        <line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgba(212,162,127,.22)" stroke-width="5" stroke-linecap="round"/>
        <line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round" stroke-dasharray="1 0" opacity="0.85"/>
        {nodes}
      </svg>
      {cap("no new product, no launch. an asset you already have becomes revenue in a week.")}</div>'''

# 3. GRAPH - contact MESH: nodes wired to each other, 3 warm leads ranked by CORTEX
def graph():
    W,H=800,470
    P={'a':(120,120),'b':(250,88),'c':(360,158),'d':(180,258),'e':(330,300),
       'f':(120,392),'g':(300,420),'h':(470,110),'i':(560,232),'j':(690,150),
       'k':(628,346),'l':(486,392),'m':(710,300)}
    E=[('a','b'),('b','c'),('a','d'),('d','e'),('c','e'),('d','f'),('e','g'),('f','g'),
       ('c','h'),('h','i'),('i','j'),('i','k'),('k','m'),('k','l'),('l','g'),('h','j'),('e','i')]
    hot={'i':('1','Old client'),'e':('2','Ex-colleague'),'h':('3','Warm intro')}
    edges=""
    for a,b in E:
        x1,y1=P[a]; x2,y2=P[b]; warm=(a in hot or b in hot)
        col=f"rgba(212,162,127,.55)" if warm else "rgba(250,250,247,.10)"; w=2.6 if warm else 1.4
        edges+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"/>'
    nodes=""
    for k,(x,y) in P.items():
        if k in hot:
            rk,nm=hot[k]
            nodes+=f'<circle cx="{x}" cy="{y}" r="22" fill="url(#warm)" filter="url(#wg)"/>'
            nodes+=f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">{rk}</text>'
            nodes+=f'<text x="{x}" y="{y+42}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">{nm}</text>'
        else:
            nodes+=f'<circle cx="{x}" cy="{y}" r="9" fill="#3a352f" stroke="rgba(255,255,255,.12)" stroke-width="1.4"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Your dead list, re-read","CONTACTS RANKED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="warm" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="wg" x="-160%" y="-160%" width="420%" height="420%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.85"/></filter></defs>
        {edges}{nodes}
      </svg>
      {cap("CORTEX reads the network already in your phone and ranks the three worth a message.")}</div>'''

# 4. STACK - isometric stack of reply cards to your existing offer (agent-worked follow-ups)
def stack():
    rows=[("Old client","re: your offer","REPLIED"),
          ("Warm intro","booked a call","MEETING"),
          ("Ex-colleague","asked for pricing","REPLIED")]
    cards=""
    for i,(a,b,tag) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16v12H4z"/><path d="M4 7l8 6 8-6"/></svg></div>
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:24px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;background:rgb({ACC});padding:8px 16px;border-radius:999px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Mono';font-weight:500;font-size:13px;letter-spacing:.08em;color:#1a0f0a">{tag}</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The offer works itself","SENT WHILE YOU SLEEP")}
      <div style="perspective:2000px;height:490px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:490px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:456px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">3 replies, 0 cold sends</div></div></div>
      {cap("SPECTER writes it in your voice and works the follow-ups you would never send.")}</div>'''

# 5. GAUGE - IVORY cost dial: needle parked at cents, expensive stack crossed out
def gauge():
    cx,cy,R=280,262,182
    def pt(a,r): return (cx+r*math.cos(math.radians(a)), cy-r*math.sin(math.radians(a)))
    tx0,ty0=pt(180,R); tx1,ty1=pt(0,R)
    # warm cheap arc segment (right third, 0..60deg)
    ax0,ay0=pt(60,R); ax1,ay1=pt(0,R)
    needa=15; nx,ny=pt(needa,R-30)
    ticks=""
    for a in range(0,181,30):
        p1=pt(a,R); p2=pt(a,R-16)
        ticks+=f'<line x1="{p1[0]:.0f}" y1="{p1[1]:.0f}" x2="{p2[0]:.0f}" y2="{p2[1]:.0f}" stroke="rgba(150,90,45,.35)" stroke-width="2.4"/>'
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 30px">
      {htiv("Priced in cents, not salaries","COST GAUGE")}
      <div style="display:block;margin:0 auto;width:560px;position:relative">
        <svg width="560" height="216" viewBox="0 64 560 216" style="display:block;margin:0 auto">
          <path d="M{tx0:.0f} {ty0:.0f} A{R} {R} 0 0 1 {tx1:.0f} {ty1:.0f}" fill="none" stroke="rgba(150,90,45,.20)" stroke-width="18" stroke-linecap="round"/>
          <path d="M{ax0:.0f} {ay0:.0f} A{R} {R} 0 0 1 {ax1:.0f} {ay1:.0f}" fill="none" stroke="#96562d" stroke-width="18" stroke-linecap="round"/>
          {ticks}
          <text x="{pt(180,R+2)[0]+8:.0f}" y="{cy+16:.0f}" text-anchor="start" font-family="DM Mono" font-size="14" fill="rgb(200,70,35)">$$$</text>
          <text x="{pt(0,R+2)[0]-8:.0f}" y="{cy+16:.0f}" text-anchor="end" font-family="DM Mono" font-size="14" fill="#96562d">cents</text>
          <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="6" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="13" fill="#2a2016"/>
        </svg>
      </div>
      <div style="text-align:center;margin-top:6px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#2a2016">0.4c</span>
        <span style="font-family:'DM Mono';font-size:15px;color:#96562d;margin-left:12px">per outbound action</span></div>
      <div style="display:flex;align-items:center;justify-content:center;gap:14px;margin-top:12px">
        <span style="font-family:'DM Sans';font-size:18px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">an SDR + tools: $4,000 / mo</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.06em;color:rgb(200,70,35)">replaced</span></div>
      {cap("pay per token. a full outbound week costs less than one coffee.","#8a745a")}</div>'''

# 6. FIELD - dot field of 900 contacts, seven warm today (distinct from the mesh graph)
def field():
    cols,rowsn=45,20  # 900
    lit={83,177,264,401,558,672,790}
    cell=15; gap=4; dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<circle cx="{x+cell/2:.0f}" cy="{y+cell/2:.0f}" r="{cell/2+1:.0f}" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<circle cx="{x+cell/2:.0f}" cy="{y+cell/2:.0f}" r="{cell/2-1:.0f}" fill="rgba(250,250,247,.10)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:38px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">900</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">contacts you already have</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">7 warm today</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("it watches the list you forgot and flags the few worth a message this morning.")}</div>'''

# 7. HUB - radial hub-and-spokes: your assets at the core, seven agents wired around, one system
def hub():
    W,H=800,470; cx,cy=400,238; R=168
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    spokes=""; nodes=""
    n=len(agents)
    for i,nm in enumerate(agents):
        a=-90+i*360/n
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.35)" stroke-width="2.2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgba(212,162,127,.45)" stroke-width="1.8"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".02em" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One system around your inputs","SEVEN AGENTS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="78" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">WHAT</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">YOU OWN</text>
        {nodes}
      </svg>
      {cap("research, outbound, deals and content, wired around what you already have. one login.")}</div>'''

# 8. FLIP - before/after: hunting a new idea (dim, crossed) vs monetize what exists (lit, warm)
def flip():
    old=["a brand new idea","a new audience","months of building","$0 for a long time"]
    new=["the offer you have","the list you own","turned on this week","first dollar in days"]
    def rows(items,good):
        out=""
        for t in items:
            if good:
                ic='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb('+ACC+')" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
                col="#e9e3d7"
            else:
                ic='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb(200,70,35)" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
                col="#8f8880"
            deco='text-decoration:line-through;text-decoration-color:rgba(200,70,35,.55)' if not good else ''
            out+=f'<div style="display:flex;align-items:center;gap:13px;margin-bottom:15px"><span style="flex-shrink:0">{ic}</span><span style="font-family:\'DM Sans\';font-size:19px;color:{col};{deco}">{t}</span></div>'
        return out
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Two ways to make money","BEFORE / AFTER")}
      <div style="display:flex;align-items:stretch;gap:20px">
        <div style="flex:1;background:rgba(250,250,247,.03);border:1px solid rgba(200,70,35,.24);border-radius:22px;padding:24px 24px 20px">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb(200,70,35);margin-bottom:16px">MOST PEOPLE</div>
          {rows(old,False)}</div>
        <div style="flex-shrink:0;display:flex;align-items:center;justify-content:center;width:70px">
          <div style="width:52px;height:52px;border-radius:50%;background:rgb({ACC});display:flex;align-items:center;justify-content:center;box-shadow:0 10px 22px rgba(212,162,127,.4)">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div></div>
        <div style="flex:1;background:linear-gradient(160deg,rgba(212,162,127,.14),rgba(212,162,127,.04));border:1px solid rgba(212,162,127,.4);border-radius:22px;padding:24px 24px 20px">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:16px">OPERATORS</div>
          {rows(new,True)}</div>
      </div>
      {cap("the revenue was never in a new idea. it was in the assets you already had.")}</div>'''

PANELS={"assets":assets(),"path":path(),"graph":graph(),"stack":stack(),
        "gauge":gauge(),"field":field(),"hub":hub(),"flip":flip()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2mostpeoplethink"; os.makedirs(outd,exist_ok=True)
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
