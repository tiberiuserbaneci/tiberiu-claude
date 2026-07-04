#!/usr/bin/env python3
# TIER 3 - ONE SYSTEM NOT TEN SKILLS (s2src23), rebuilt to the WIRE-ITS-EYES bar: each panel a
# UNIQUE hand-built coded scene filling a clean rounded card, title + one-line caption, no chip strips.
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

# 1. STACK - scattered cloud of dim, disconnected tool chips + a red CONTEXT LOST break in the middle
def stack():
    tools=["CRM","Scraper","Sequencer","Chatbot","Enricher","Copy tool","Dialer","Scheduler","Docs AI","Analytics"]
    chips=""
    rots=[-6,4,-3,5,3,-5,4,-4,5,-6]
    for i,(nm,rt) in enumerate(zip(tools,rots)):
        chips+=(f'<div style="transform:rotate({rt}deg);background:linear-gradient(158deg,#262320,#1b1815);'
          f'border:1px solid rgba(255,255,255,.08);border-radius:15px;padding:14px 18px;opacity:.82;'
          f'box-shadow:0 12px 22px rgba(0,0,0,.4);display:flex;align-items:center;gap:12px">'
          f'<span style="flex-shrink:0;width:26px;height:26px;border-radius:8px;background:rgba(250,250,247,.06);'
          f'border:1px solid rgba(255,255,255,.10);display:flex;align-items:center;justify-content:center;'
          f'font-family:DM Sans;font-weight:900;font-size:14px;color:#7a746a">{nm[0]}</span>'
          f'<div><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#c9c3b8">{nm}</div>'
          f'<div style="font-family:DM Mono;font-size:11px;color:#6f6a60">own login &middot; own bill</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Ten tabs, zero memory","THE STACK")}
      <div style="position:relative;height:452px">
        <div style="display:flex;flex-wrap:wrap;gap:16px 18px;align-content:center;justify-content:center;height:100%">{chips}</div>
        <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:14px;
          background:linear-gradient(160deg,#3a1a12,#26120c);border:1.5px solid rgba(200,70,35,.55);border-radius:16px;
          padding:15px 22px;box-shadow:0 20px 40px rgba(0,0,0,.6),0 0 30px rgba(200,70,35,.18)">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="rgb(200,70,35)" stroke-width="2.6" stroke-linecap="round"><path d="M9 17H7A5 5 0 0 1 7 7h2M15 7h2a5 5 0 0 1 0 10h-2"/><line x1="8" y1="12" x2="16" y2="12" stroke-dasharray="2 3"/></svg>
          <span style="font-family:DM Mono;font-size:15px;letter-spacing:.1em;color:#e79b82">CONTEXT LOST BETWEEN TABS</span></div>
      </div>
      {cap("each tool a separate login, a separate bill, and no shared memory.")}</div>'''

# 2. ROSTER - hub-and-spokes: the router hub feeds seven named agent nodes
def roster():
    cx,cy,R=410,235,172
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/7); x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="47" fill="#221f1b" stroke="rgba(255,255,255,.13)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14.5" fill="#eae4d8">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one roster","THE TEAM")}
      <svg width="820" height="480" viewBox="0 0 820 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spokes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">plain english in</text>
        {nodes}
      </svg>
      {cap("call one by name with a slash, or type plain english and it routes for you.")}</div>'''

# 3. ROUTER - one job token routed down three tier lanes, SMART lit and picked, priced in cents
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
    hubx,hy=170,230; lx=470
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C320 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:300px;top:{y-40}px;width:170px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You never pick a model","MODEL ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub2" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg2)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub2)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">draft 12<br>follow-ups</div>
        {cards}
      </div>
      {cap("one job in, the cheapest tier that can actually do it - cents, not dollars.")}</div>'''

# 4. CENTS - IVORY bill-flip: the replaced tools stacked as red cost bars vs one warm cents callout
def cents():
    rows=[("CRM seat","$99",99),("Enrichment","$149",149),("Sequencer","$79",79),("Copy tool","$49",49)]
    mx=max(v for _,_,v in rows); bars=""
    for nm,lab,v in rows:
        w=60+ (v/mx)*300
        bars+=(f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:13px">'
          f'<span style="width:118px;flex-shrink:0;font-family:DM Sans;font-weight:600;font-size:16px;color:#5a4634">{nm}</span>'
          f'<div style="height:22px;width:{w:.0f}px;border-radius:7px;background:linear-gradient(90deg,#c8532e,#a83b20);box-shadow:inset 0 1px 2px rgba(255,255,255,.25)"></div>'
          f'<span style="font-family:DM Mono;font-size:15px;color:#a83b20">{lab}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The bill flips to cents","THE BILL","#2a2016")}
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex:1">
          {bars}
          <div style="display:flex;align-items:center;gap:14px;margin-top:18px;padding-top:16px;border-top:1px solid rgba(150,120,80,.24)">
            <span style="width:118px;flex-shrink:0;font-family:DM Sans;font-weight:800;font-size:16px;color:#2a2016">Old stack</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:24px;color:#a83b20">$376 / mo</span></div>
        </div>
        <div style="flex-shrink:0;width:230px;background:linear-gradient(160deg,#fff,#f4ead8);border:1.5px solid #96562d;border-radius:20px;padding:24px 22px;text-align:center;box-shadow:0 18px 34px rgba(150,120,80,.2)">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#96562d">ULTRON</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:52px;color:#2a2016;line-height:1.05;margin-top:6px">~11c</div>
          <div style="font-family:DM Sans;font-weight:700;font-size:16px;color:#5a4634">per job</div>
          <div style="height:12px;width:34px;margin:14px auto 0;border-radius:6px;background:linear-gradient(90deg,#e6b48f,#96562d)"></div>
        </div>
      </div>
      {cap("high dollars belong to the tools you drop. every ultron action costs cents.","#8a745a")}</div>'''

# 5. MEMORY - orbit core: one glowing memory core, data facts riding concentric rings
def memory():
    cx,cy=210,220
    facts=[("ICP",-90,150),("PIPELINE",-18,150),("PRICING",54,150),("DOCS",126,150),("VOICE",198,150)]
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.14)" stroke-dasharray="3 6"/>' for r in (78,150))
    chips=""
    for nm,a,d in facts:
        x=cx+d*math.cos(math.radians(a)); y=cy+d*math.sin(math.radians(a))
        chips+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
          f'<rect x="{x-46:.0f}" y="{y-17:.0f}" width="92" height="34" rx="11" fill="#231f1b" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".06em" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="420" height="440" viewBox="0 0 420 440">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {rings}{chips}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="56" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one core</text></svg>
      <div style="flex:1">
        {htitle("One core, never forgets","SHARED MEMORY")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing and docs live in one memory. Every agent reads the same facts, every turn, so nothing gets re-explained.</div>
        {cap("tell it once. ten tools would have forgotten by the next tab.")}</div></div>'''

# 6. GATE - full-capability orb held on the operator's tap, one lock
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It sends nothing alone","HUMAN GATE")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="210" cy="220" r="132" fill="url(#orb)"/></g>
        <text x="210" y="212" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="32" fill="#2a160c">DRAFTED</text>
        <text x="210" y="248" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">READY TO SEND</text>
        <path d="M344 220 H616" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="626" y="150" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(668,188)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="696" y="326" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every email and external move parks for your approval. still your name on it.")}</div>'''

# 7. SYSTEM - IVORY isometric chain: a repeatable four-step job, not one clever prompt
def system():
    steps=[("1","RESEARCH","the account"),("2","DRAFT","the outreach"),("3","FOLLOW UP","on a cadence"),("4","CLOSE","the deal")]
    tiles=""
    for i,(n,t,s) in enumerate(steps):
        tiles+=(f'<div style="flex:1;background:linear-gradient(160deg,#fff,#f2e7d4);border:1px solid rgba(150,120,80,.2);border-radius:18px;'
          f'padding:18px 16px;box-shadow:0 18px 30px rgba(150,120,80,.16), inset 0 2px 2px rgba(255,255,255,.9)">'
          f'<div style="width:36px;height:36px;border-radius:11px;background:#96562d;display:flex;align-items:center;justify-content:center;'
          f'font-family:DM Sans;font-weight:900;font-size:19px;color:#fff">{n}</div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#2a2016;margin-top:12px">{t}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#7a6448;margin-top:2px">{s}</div></div>')
        if i<3:
            tiles+=('<div style="flex-shrink:0;display:flex;align-items:center;padding:0 2px">'
              '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 40px 34px">
      {htitle("A system runs the job","NOT A PROMPT","#2a2016")}
      <div style="perspective:1600px;height:300px;display:flex;align-items:center">
        <div style="transform:rotateX(15deg);display:flex;align-items:stretch;gap:6px;width:100%">{tiles}</div>
      </div>
      <div style="display:flex;align-items:center;gap:12px;margin-top:6px">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round"><path d="M3 12a9 9 0 1 0 3-6.7M3 3v4h4"/></svg>
        <span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#2a2016">chained and repeatable, run it again tomorrow</span></div>
      {cap("a prompt gives one reply. a system chains research to close, on repeat.","#8a745a")}</div>'''

# 8. OPERATOR - scattered parts converge into one glowing assembled operator
def operator():
    scat=[("7 agents",70,84),("router",70,196),("memory",70,308),("gate",196,140),("cents",196,252)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+34} {y} C340 {y},360 210,520 210" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<rect x="{x-6}" y="{y-19}" width="132" height="38" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.4" opacity="0.85"/>'
          f'<text x="{x+60}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Stop stacking, start running","ONE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="590" cy="210" r="122" fill="url(#bod)"/></g>
        <text x="590" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="23" fill="#2a160c">ONE</text>
        <text x="590" y="228" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="23" fill="#2a160c">OPERATOR</text>
        <text x="590" y="368" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">plain english in, gtm out</text>
      </svg>
      {cap("seven agents, one router, one memory, one gate - one login runs it all.")}</div>'''

PANELS={"stack":stack(),"roster":roster(),"router":router(),"cents":cents(),
        "memory":memory(),"gate":gate(),"system":system(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src23"; os.makedirs(outd,exist_ok=True)
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
