#!/usr/bin/env python3
# TIER 3 - YOU ARE THE BOARD NOW. Org-chart-of-agents reframe (Paperclip source). Each panel a UNIQUE
# hand-built coded scene on a clean rounded card, title + one-line caption, NO generic stat-chip strips,
# NO cuts/walls. Warm palette only + one muted red for the bad/competitor state. Cents pricing.
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
def ihead(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CHAOS - scattered disconnected tool windows tangled by broken (red) traces, none reporting up
def chaos():
    DOTS='<span style="width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.18);display:inline-block;margin-right:5px"></span>'*3
    BAR1='<div style="height:5px;background:rgba(255,255,255,.09);border-radius:3px;margin-top:9px"></div>'
    BAR2='<div style="height:5px;width:66%;background:rgba(255,255,255,.06);border-radius:3px;margin-top:5px"></div>'
    wins=[("outreach.ai",40,26,False),("coder tab 3",300,12,True),("research chat",560,40,False),
          ("deal notes",84,236,True),("scratch prompt",360,214,False),("PR by hand",604,250,True)]
    cxy=[(x+75,y+40) for (_,x,y,_) in wins]
    pairs=[(0,1),(1,2),(0,3),(3,4),(4,5),(2,5),(1,4),(0,4)]; redset={(3,4),(1,4)}
    lines=""
    for a,b in pairs:
        x1,y1=cxy[a]; x2,y2=cxy[b]; red=(a,b) in redset
        col="rgba(200,70,35,.65)" if red else "rgba(250,250,247,.12)"; dash="4 8" if red else "2 9"
        lines+=f'<path d="M{x1} {y1} C{(x1+x2)/2:.0f} {y1-46},{(x1+x2)/2:.0f} {y2+46},{x2} {y2}" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="{dash}"/>'
    windows=""
    for label,x,y,broken in wins:
        bd="rgba(200,70,35,.42)" if broken else "rgba(255,255,255,.09)"
        tag='<div style="font-family:\'DM Mono\';font-size:10px;letter-spacing:.06em;color:rgb(200,70,35);margin-top:9px">CONTEXT LOST</div>' if broken else ''
        windows+=(f'<div style="position:absolute;left:{x}px;top:{y}px;width:150px;background:linear-gradient(160deg,#2a2724,#201d1a);border:1px solid {bd};border-radius:12px;padding:11px 13px;box-shadow:0 16px 30px rgba(0,0,0,.5)">'
          f'<div style="line-height:0">{DOTS}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:12.5px;color:#c9c3b8;margin-top:9px">{label}</div>'
          f'{BAR1}{BAR2}{tag}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Twenty tabs, no boss","SOLO CHAOS")}
      <div style="position:relative;height:470px">
        <svg width="820" height="470" viewBox="0 0 820 470" style="position:absolute;left:0;top:0">{lines}</svg>
        {windows}
      </div>
      {cap("a dozen ai tabs, none reporting to anyone - context lost between every one.")}</div>'''

# 2. ORGCHART - top-down hierarchy: YOU (the board) over a bus, seven named agents drop below
def orgchart():
    agents=[("CORTEX","research"),("SPECTER","outreach"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    centers=[76,192,308,424,540,656,772]
    lines=f'<line x1="424" y1="104" x2="424" y2="168" stroke="rgba(212,162,127,.55)" stroke-width="3.5"/>'
    lines+=f'<line x1="{centers[0]}" y1="168" x2="{centers[-1]}" y2="168" stroke="rgba(212,162,127,.34)" stroke-width="3"/>'
    for c in centers: lines+=f'<line x1="{c}" y1="168" x2="{c}" y2="226" stroke="rgba(212,162,127,.34)" stroke-width="2.5"/>'
    chips=""
    for (nm,role),c in zip(agents,centers):
        chips+=(f'<div style="position:absolute;left:{c-53}px;top:226px;width:106px;background:linear-gradient(160deg,#2f2b26,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:15px;padding:15px 6px;text-align:center;box-shadow:0 16px 28px rgba(0,0,0,.45)">'
          f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:15px;color:#FAFAF7;letter-spacing:.01em">{nm}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:11px;color:rgb({ACC});margin-top:5px">{role}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven report to you","THE ROSTER")}
      <div style="position:relative;height:340px">
        <svg width="820" height="340" viewBox="0 0 820 340" style="position:absolute;left:0;top:0">
          <defs><linearGradient id="you2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
          <filter id="yg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          {lines}
          <g filter="url(#yg2)"><rect x="336" y="34" width="176" height="70" rx="20" fill="url(#you2)"/></g>
          <text x="424" y="70" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a160c">YOU</text>
          <text x="424" y="91" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">the board</text>
        </svg>
        {chips}
      </div>
      {cap("cortex, specter, striker, pulse, sentinel, amplify, counsel - a named team, not a chat box.")}</div>'''

# 3. ROUTER - the chair reads one job and assigns it to an agent + the cheapest model tier (cents)
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","runs on STRIKER","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
    hubx,hy=170,230; lx=470
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C320 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">assigned</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:300px;top:{y-42}px;width:174px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The chair assigns the work","THE ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hubR" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hgR" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hgR)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hubR)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">qualify 12<br>deals</div>
        {cards}
      </div>
      {cap("one job in, the right agent and the cheapest tier that can run it - cents, not dollars.")}</div>'''

# 4. LEDGER - IVORY spend book in cents beside the struck-through competitor dollar (cents value-prop)
def ledger():
    rows=[("Score 200 accounts","3c"),("Draft 40 cold emails","2c"),("Qualify 12 deals","4c"),("Write 5 posts","2c")]
    rowhtml=""
    for job,c in rows:
        rowhtml+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:14px 4px;border-bottom:1px solid rgba(120,95,60,.18)">'
          f'<span style="font-family:\'DM Sans\';font-size:19px;color:#3a2f22">{job}</span>'
          f'<span style="font-family:\'DM Mono\';font-weight:500;font-size:19px;color:#5a4634">{c}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ihead("The books close in cents","TO THE TOKEN")}
      <div style="display:flex;gap:28px;align-items:stretch">
        <div style="flex:1">
          {rowhtml}
          <div style="display:flex;justify-content:space-between;align-items:baseline;padding:18px 4px 0">
            <span style="font-family:'DM Sans';font-weight:900;font-size:23px;color:#2a2016">Month to date</span>
            <span style="font-family:'DM Sans';font-weight:900;font-size:44px;color:#96562d">11c</span></div>
        </div>
        <div style="flex-shrink:0;width:236px;background:rgba(150,90,45,.06);border:1px dashed rgba(150,90,45,.38);border-radius:20px;padding:24px 20px;display:flex;flex-direction:column;justify-content:center;text-align:center">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#a08a68">THE OLD STACK</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:46px;color:#8a7256;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.75);margin-top:10px">$900</div>
          <div style="font-family:'DM Sans';font-size:15px;color:#8a7256;margin-top:6px">per month, same work</div>
        </div>
      </div>
      {cap("spend tracked down to the token. the stack it replaced billed $900 a month.","#8a745a")}</div>'''

# 5. MEMORY - concentric shared core, seven intact agent lifelines all drawing from one record
def memory():
    cx,cy=205,212
    agents=["cortex","specter","striker","pulse","sentinel","amplify","counsel"]
    lines=""; nodes=""
    for i,nm in enumerate(agents):
        a=-90+i*(360/7)
        x=cx+150*math.cos(math.radians(a)); y=cy+150*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="memC" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="memG" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="88" fill="none" stroke="rgba(212,162,127,.14)"/>
        {lines}<g filter="url(#memG)"><circle cx="{cx}" cy="{cy}" r="54" fill="url(#memC)"/></g>
        <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#2a160c">MEMORY</text></svg>
      <div style="flex:1">
        {htitle("One memory, seven readers","SHARED CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing and docs live in one core. Every agent reads it before it acts, so nobody forgets you.</div>
        {cap("no memory, no company - one record feeds all seven.")}</div></div>'''

# 6. GATE - a queue of parked external moves butting into the HUMAN GATE lock, held for your tap
def gate():
    items=[("Send 40 cold emails","SPECTER",30,90),("Proposal to Globex","STRIKER",175,235),("Deploy PR #182","SENTINEL",320,380)]
    conns=""; cards=""
    for label,who,top,mid in items:
        conns+=f'<rect x="410" y="{mid-5}" width="86" height="10" rx="5" fill="rgb({ACC})" opacity="0.85" filter="url(#tgt)"/>'
        cards+=(f'<div style="position:absolute;left:0;top:{top}px;width:400px;height:120px;box-sizing:border-box;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:18px;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px;box-shadow:0 20px 34px rgba(0,0,0,.5)">'
          f'<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:\'DM Sans\';font-weight:700;font-size:20px;color:#FAFAF7">{label}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:#8f8f85;background:rgba(250,250,247,.06);border:1px solid rgba(250,250,247,.12);border-radius:999px;padding:5px 12px">HELD</span></div>'
          f'<div style="font-family:\'DM Mono\';font-size:13px;color:rgb({ACC})">from {who}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><filter id="tgt" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>{conns}</svg>
        {cards}
        <div style="position:absolute;left:500px;top:40px;width:280px;height:380px;box-sizing:border-box;background:linear-gradient(160deg,#403a33,#211e1a);border:2px solid rgb({ACC});border-radius:26px;box-shadow:0 30px 60px rgba(0,0,0,.5),0 0 40px rgba(212,162,127,.16);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px">
          <svg width="96" height="96" viewBox="0 0 96 96"><rect x="20" y="42" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5.5"/><path d="M30 42 V29 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5.5"/><circle cx="48" cy="61" r="6" fill="rgb({ACC})"/></svg>
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#FAFAF7;letter-spacing:.02em">GATE</div>
          <div style="font-family:'DM Mono';font-size:14px;color:rgb({ACC})">waits for your tap</div>
        </div>
      </div>
      {cap("every external move parks here and waits for one tap. augmented, still your company.")}</div>'''

# 7. SYSTEMS - IVORY: a saved reusable workflow (numbered, reruns) beside a throwaway prompt that dies
def systems():
    steps=[("1","Find accounts"),("2","Score fit"),("3","Draft outreach"),("4","Wait for gate")]
    stepshtml=""
    for i,(n,lbl) in enumerate(steps):
        stepshtml+=(f'<div style="display:flex;align-items:center;gap:16px">'
          f'<div style="flex-shrink:0;width:42px;height:42px;border-radius:50%;background:#96562d;display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:19px;color:#fdfbf6">{n}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:21px;color:#2a2016">{lbl}</div></div>')
        if i<len(steps)-1: stepshtml+='<div style="width:2px;height:20px;background:rgba(150,90,45,.4);margin-left:20px"></div>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ihead("A saved system, not a prompt","RERUNS")}
      <div style="display:flex;gap:34px;align-items:center">
        <div style="flex:1">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.16em;color:#96562d;margin-bottom:16px">SAVED SEQUENCE &middot; RUNS ON EVERY ACCOUNT</div>
          {stepshtml}
        </div>
        <div style="flex-shrink:0;width:250px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#a08a68">A LOOSE PROMPT</div>
          <div style="width:100%;background:rgba(150,90,45,.05);border:1px dashed rgba(150,90,45,.4);border-radius:18px 18px 18px 4px;padding:18px 20px;font-family:'DM Sans';font-size:17px;color:#9a8266;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7);line-height:1.35">"write me a cold email for this account..."</div>
          <div style="font-family:'DM Mono';font-size:12px;color:#c84623">retyped every time &middot; dies at the tab</div>
        </div>
      </div>
      {cap("wire the sequence once, it reruns on every account. a loose prompt dies at the tab.","#8a745a")}</div>'''

# 8. BOARD - closing: seven agent nodes converge into one company orb, one login, you at the head
def board():
    agents=["cortex","specter","striker","pulse","sentinel","amplify","counsel"]
    ys=[46,102,158,214,270,326,382]; ocx,ocy=590,214
    left=""
    for nm,y in zip(agents,ys):
        left+=(f'<path d="M172 {y} C360 {y},420 {ocy},{ocx-116} {ocy}" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<rect x="34" y="{y-17}" width="140" height="34" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.1)"/>'
          f'<text x="104" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("You sit at the head","ONE LOGIN")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="boB" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="boG" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#boG)"><circle cx="{ocx}" cy="{ocy}" r="118" fill="url(#boB)"/></g>
        <text x="{ocx}" y="{ocy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="{ocx}" y="{ocy+24}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">COMPANY</text>
        <text x="{ocx}" y="{ocy+150}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">goals set &middot; work approved &middot; yours</text>
      </svg>
      {cap("you set the goals and approve. seven agents research, write, close and ship.")}</div>'''

PANELS={"chaos":chaos(),"orgchart":orgchart(),"router":router(),"ledger":ledger(),
        "memory":memory(),"gate":gate(),"systems":systems(),"board":board()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src46"; os.makedirs(outd,exist_ok=True)
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
