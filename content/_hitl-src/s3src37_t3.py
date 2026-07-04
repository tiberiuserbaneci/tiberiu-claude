#!/usr/bin/env python3
# TIER 3 - YOU CLOSE, ULTRON DELIVERS (done-for-you reseller model), built to the WIRE-ITS-EYES bar:
# each panel a UNIQUE hand-built coded scene filling a clean rounded card, title + one-line caption,
# NO generic stat-chip strips. Helpers + __main__ copied from aibody_t3.py.
import importlib.util, os, math, random
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

# 1. MODEL - horizontal money-flow: CLIENT retainer -> YOU -> ULTRON delivers, big margin bar below
def model():
    def node(x,label,val,sub,fill,txt):
        return (f'<div style="position:absolute;left:{x}px;top:40px;width:200px;text-align:center">'
          f'<div style="background:{fill};border:1.5px solid rgba(255,255,255,.12);border-radius:20px;padding:20px 14px;box-shadow:0 24px 40px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{txt[1]}">{label}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:30px;color:{txt[0]};margin-top:6px">{val}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#9a9488;margin-top:2px">{sub}</div></div></div>')
    nodes=(node(6,'CLIENT','$4,000','pays you monthly','#241f1b',('#FAFAF7',f'rgb({ACC})'))
      +node(300,'YOU','broker','close and manage','linear-gradient(160deg,#3a352e,#241f1a)',('#FAFAF7',f'rgb({ACC})'))
      +node(594,'ULTRON','delivers','does all the work','linear-gradient(160deg,#4a3322,#2a160c)',('#FAFAF7',f'rgb({ACC})')))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You sell. Ultron ships.","THE MODEL")}
      <div style="position:relative;height:210px">
        <svg width="820" height="210" viewBox="0 0 820 210" style="position:absolute;left:0;top:0">
          <defs><marker id="ah" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6" fill="none" stroke="rgb({ACC})" stroke-width="1.6"/></marker></defs>
          <path d="M206 96 C250 96,258 96,296 96" fill="none" stroke="rgb({ACC})" stroke-width="4" marker-end="url(#ah)"/>
          <path d="M500 96 C544 96,552 96,590 96" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="4" marker-end="url(#ah)"/>
        </svg>
        {nodes}
      </div>
      <div style="margin-top:20px">
        <div style="display:flex;height:52px;border-radius:14px;overflow:hidden;border:1px solid rgba(255,255,255,.1)">
          <div style="width:3%;background:rgb(200,70,35);display:flex;align-items:center;justify-content:center"></div>
          <div style="flex:1;background:linear-gradient(90deg,#3a352e,#4a3322);display:flex;align-items:center;padding-left:22px">
            <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">your margin&nbsp;</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">$3,900+</span></div>
        </div>
        <div style="display:flex;justify-content:space-between;margin-top:8px">
          <span style="font-family:DM Mono;font-size:12px;color:rgb(200,70,35)">delivery cost: cents</span>
          <span style="font-family:DM Mono;font-size:12px;color:#8f8f85">retainer collected: $4,000</span></div>
      </div>
      {cap("you close the client; the operator does one hundred percent of the fulfillment.")}</div>'''

# 2. DEMAND - scatter dot-field of companies buying, clustered by industry, high-demand zones lit
def demand():
    random.seed(37)
    zones=[("HEALTHCARE",150,150,True),("INSURANCE",430,120,True),("LOGISTICS",640,190,False),
           ("HOME SVCS",250,330,True),("RETAIL",520,340,False),("TRAVEL",680,340,False)]
    dots=""
    for nm,zx,zy,hot in zones:
        n=26 if hot else 14
        for _ in range(n):
            a=random.uniform(0,2*math.pi); d=random.uniform(6,74)
            x=zx+d*math.cos(a); y=zy+d*math.sin(a)
            r=random.uniform(2.2,4.6)
            if hot and random.random()<0.30:
                dots+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r+1.4:.1f}" fill="rgb({ACC})" opacity="0.92"/>'
            else:
                op=0.5 if hot else 0.28
                dots+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#c9c3b8" opacity="{op}"/>'
    labels=""
    for nm,zx,zy,hot in zones:
        col=f"rgb({ACC})" if hot else "#7a746a"
        labels+=f'<text x="{zx:.0f}" y="{zy-84:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="{col}">{nm}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The market is already buying","DEMAND")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <rect x="0" y="0" width="820" height="450" fill="none"/>
        {dots}{labels}
      </svg>
      {cap("healthcare, insurance, home services - every lit dot is a company shopping now.")}</div>'''

# 3. NICHE - IVORY bullseye: industries orbit faint on outer rings, one locked in the centre
def niche():
    cx,cy=306,232
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(150,90,45,.20)" stroke-width="1.5"/>' for r in (70,140,205))
    orbit=[("Insurance",205,-40),("Logistics",205,40),("Retail",205,150),("Travel",205,215),
           ("Debt",140,-140),("Fin. Svcs",140,110)]
    tags=""
    for nm,rr,ang in orbit:
        x=cx+rr*math.cos(math.radians(ang)); y=cy+rr*math.sin(math.radians(ang))
        tags+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="rgba(150,90,45,.35)"/>'
          f'<text x="{x:.0f}" y="{y-14:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#a08560">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Pick one. Go deep.","LOCK IT","#2a2016")}
      <svg width="612" height="464" viewBox="0 0 612 464" style="display:block;margin:0 auto">
        <defs><radialGradient id="bull" cx="40%" cy="34%"><stop offset="0%" stop-color="#d98a52"/><stop offset="60%" stop-color="#96562d"/><stop offset="100%" stop-color="#6e3d1c"/></radialGradient></defs>
        {rings}{tags}
        <circle cx="{cx}" cy="{cy}" r="58" fill="url(#bull)"/>
        <g transform="translate({cx-19},{cy-26})"><rect x="0" y="17" width="38" height="28" rx="6" fill="none" stroke="#fdfbf6" stroke-width="4"/><path d="M7 17 V9 a12 12 0 0 1 24 0 v8" fill="none" stroke="#fdfbf6" stroke-width="4"/></g>
        <text x="{cx}" y="{cy+46}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#fdfbf6">HEALTHCARE</text>
      </svg>
      {cap("one niche with real pain and real budget beats ten you only dabble in.","#8a745a")}</div>'''

# 4. INSTALL - horizontal deploy timeline PICK -> INSTALL -> LIVE, closing on a 100% progress ring
def install():
    steps=[("PICK","the niche",70),("INSTALL","the operator",270),("LIVE","for the client",470)]
    line=f'<line x1="86" y1="120" x2="486" y2="120" stroke="rgba(212,162,127,.4)" stroke-width="3"/>'
    marks=""
    for nm,sub,x in steps:
        marks+=(f'<circle cx="{x}" cy="120" r="15" fill="rgb({ACC})" stroke="#1d1d1b" stroke-width="4"/>'
          f'<text x="{x}" y="80" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x}" y="164" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{sub}</text>')
    r=78; circ=2*math.pi*r
    ring=(f'<circle cx="670" cy="120" r="{r}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="14"/>'
      f'<circle cx="670" cy="120" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="14" stroke-linecap="round" stroke-dasharray="{circ:.0f} {circ:.0f}" transform="rotate(-90 670 120)"/>'
      f'<text x="670" y="114" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">100%</text>'
      f'<text x="670" y="140" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">live · 12 min</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {htitle("Installed, not built","DEPLOY")}
      <svg width="820" height="280" viewBox="0 0 820 280" style="display:block;margin:26px auto 0">
        {line}{marks}{ring}
      </svg>
      {cap("no code, no integrations - the niche operator boots in minutes, not months.")}</div>'''

# 5. CREW - one root fans into the 7 named agents, each doing the client's work
def crew():
    rootx,rooty=120,235
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    ny0=40; step=64; cx=520
    edges=""; cards=""
    for i,(nm,role) in enumerate(agents):
        y=ny0+i*step+22
        edges+=f'<path d="M{rootx+52} {rooty} C300 {rooty},320 {y},{cx-8} {y}" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
        cards+=(f'<div style="position:absolute;left:200px;top:{y-22}px;width:290px;background:linear-gradient(160deg,#332e28,#221f1b);border:1.5px solid rgba(255,255,255,.09);border-radius:13px;padding:9px 16px;display:flex;justify-content:space-between;align-items:baseline">'
          f'<span style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:rgb({ACC})">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:#c9c3b8">{role}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven specialists deliver","THE CREW")}
      <div style="position:relative;height:480px">
        <svg width="820" height="480" viewBox="0 0 820 480" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="rt" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          {edges}
          <g filter="url(#rg)"><circle cx="{rootx}" cy="{rooty}" r="52" fill="url(#rt)"/></g>
          <text x="{rootx}" y="{rooty-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">YOUR</text>
          <text x="{rootx}" y="{rooty+15}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">OPERATOR</text>
        </svg>
        {cards}
      </div>
      {cap("research, outbound, deals, content, code, publishing, legal - one team on the client.")}</div>'''

# 6. MARGIN - IVORY ledger: a month of fulfillment tasks, each a few cents, tiny total vs the retainer
def margin():
    rows=[("1,240 research briefs","CORTEX","19c"),("6,800 outbound emails","SPECTER","34c"),
          ("410 deal replies","STRIKER","12c"),("90 content pieces","PULSE","11c"),
          ("code + publishing runs","SENTINEL","08c")]
    body=""
    for task,who,cost in rows:
        body+=(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-bottom:1px solid rgba(150,120,80,.18)">'
          f'<div><span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#2a2016">{task}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;color:#a08560;margin-left:10px">{who}</span></div>'
          f'<span style="font-family:DM Mono;font-size:17px;color:#96562d">{cost}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("They pay a retainer. You pay cents.","THE MARGIN","#2a2016")}
      <div style="background:rgba(255,255,255,.55);border-radius:18px;padding:6px 24px 8px;box-shadow:inset 0 1px 2px rgba(255,255,255,.8)">
        {body}
        <div style="display:flex;align-items:center;justify-content:space-between;padding:16px 0 8px">
          <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016">full month of delivery</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#96562d">under $1 / day</span></div>
      </div>
      {cap("the client pays thousands; a full month of fulfillment costs you cents.","#8a745a")}</div>'''

# 7. OUTCOMES - isometric stack of result cards the client sees (not the machinery)
def outcomes():
    res=[("34","meetings booked","this month",0),("1,240","replies handled","by SPECTER",1),
         ("212","tickets closed","zero waiting",2),("90 hrs","given back","to the client",3)]
    cards=""
    for big,lab,sub,i in res:
        y=i*104
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.13);border-radius:18px;padding:16px 24px;box-shadow:0 28px 40px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.09);display:flex;align-items:center;gap:22px">'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:38px;color:rgb({ACC});min-width:150px">{big}</div>'
          f'<div><div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#FAFAF7">{lab}</div>'
          f'<div style="font-family:DM Mono;font-size:13px;color:#8f8f85">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The client sees results","OUTCOMES")}
      <div style="perspective:2000px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:560px;height:420px;position:relative">{cards}</div>
      </div>
      {cap("meetings, replies, tickets closed - outcomes on a dashboard, never the machinery.")}</div>'''

# 8. WHITE-LABEL - your brand seal on front, Ultron sphere as the hidden engine, human gate lock
def whitelabel():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Your brand up front","WHITE-LABEL")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="eng" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="eg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.34"/></filter>
        <radialGradient id="seal" cx="40%" cy="34%"><stop offset="0%" stop-color="#39332c"/><stop offset="100%" stop-color="#201d19"/></radialGradient></defs>
        <g filter="url(#eg)" opacity="0.9"><circle cx="560" cy="200" r="120" fill="url(#eng)"/></g>
        <text x="560" y="194" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ULTRON</text>
        <text x="560" y="222" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010" letter-spacing=".1em">the engine</text>
        <circle cx="250" cy="200" r="128" fill="url(#seal)" stroke="rgb({ACC})" stroke-width="2.5"/>
        <circle cx="250" cy="200" r="110" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="1.5" stroke-dasharray="3 8"/>
        <text x="250" y="186" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="rgb({ACC})">YOUR AGENCY</text>
        <text x="250" y="222" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">ON THE</text>
        <text x="250" y="252" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">FRONT</text>
        <g transform="translate(388,168)"><rect x="0" y="26" width="44" height="34" rx="7" fill="#201d19" stroke="rgb({ACC})" stroke-width="4"/><path d="M8 26 V16 a14 14 0 0 1 28 0 v10" fill="none" stroke="rgb({ACC})" stroke-width="4"/></g>
        <text x="410" y="252" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">your gate</text>
      </svg>
      {cap("clients hire you; the operator runs quietly underneath, gated by your approval.")}</div>'''

PANELS={"model":model(),"demand":demand(),"niche":niche(),"install":install(),
        "crew":crew(),"margin":margin(),"outcomes":outcomes(),"whitelabel":whitelabel()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src37"; os.makedirs(outd,exist_ok=True)
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
