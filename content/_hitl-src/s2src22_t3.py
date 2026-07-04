#!/usr/bin/env python3
# TIER 3 - THE ONE-PERSON COMPANY (s2src22), built to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO generic stat strips.
# Reframe of an "AI automation agency" source (laptop + ChatGPT + VAPI) into the Ultron system.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. STACK - the taped-together tool stack Ultron replaces: scattered tool chips knotted by red
# dashed connectors, a red "breaks weekly" cost badge in the middle (competitor cost only).
def stack():
    tools=[("scraper",118,96,-7),("chat box",430,84,6),("dialer",512,214,-5),
           ("CRM",356,356,7),("sheet",150,352,-6),("zapier",76,224,5)]
    edges=""; n=len(tools)
    for i in range(n):
        x1,y1=tools[i][1],tools[i][2]; x2,y2=tools[(i+2)%n][1],tools[(i+2)%n][2]
        mx=(x1+x2)/2+30; my=(y1+y2)/2-24
        edges+=f'<path d="M{x1} {y1} Q{mx:.0f} {my:.0f} {x2} {y2}" fill="none" stroke="rgba(200,70,35,.42)" stroke-width="2.4" stroke-dasharray="7 7"/>'
    nodes=""
    for nm,x,y,rot in tools:
        nodes+=(f'<g transform="rotate({rot} {x} {y})"><rect x="{x-60}" y="{y-25}" width="120" height="50" rx="13" fill="#2a2622" stroke="rgba(200,70,35,.4)" stroke-width="1.5"/>'
          f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="DM Mono" font-size="16" fill="#c9c3b8">{nm}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten tools, taped together","THE OLD WAY")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgba(200,70,35,.5)"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#rg)"><rect x="196" y="196" width="220" height="78" rx="16" fill="#241715" stroke="rgb(200,70,35)" stroke-width="2.5"/></g>
        <text x="306" y="230" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#e8b6a5">$1,200/mo</text>
        <text x="306" y="256" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb(200,70,35)" letter-spacing=".1em">BREAKS WEEKLY</text>
      </svg>
      {cap("a scraper, a chat box, a dialer, a CRM. stitched by hand, breaking weekly.")}</div>'''

# 2. ROUTER - one job token routed down 3 tier lanes, SMART lane lit/picked, cents on each
def router():
    lanes=[("LITE","quick lookups","0.02c",92,False),("SMART","daily execution","0.11c",228,True),("DEEP","hard judgement","0.40c",364,False)]
    hubx,hy=150,228; lx=452
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+60} {hy} C300 {hy},310 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.32))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:302px;top:{y-42}px;width:300px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:16px 18px;display:flex;align-items:center;justify-content:space-between">'
          f'<div><div style="display:flex;align-items:baseline;gap:10px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85;margin-top:2px">{role}</div></div>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7">{cost}</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A brain that budgets itself","MODEL ROUTER")}
      <div style="position:relative;height:456px">
        <svg width="820" height="456" viewBox="0 0 820 456" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="60" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        {cards}
      </div>
      {cap("one job in, the cheapest tier that can do it. cents, never dollars.")}</div>'''

# 3. AGENTS - constellation: central orb, 7 named agent nodes ringed on glowing spokes
def agents():
    cx,cy=306,228; R=176
    names=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    spokes=""; nodes=""
    for i,nm in enumerate(names):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.8"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" letter-spacing=".04em" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven specialists, one login","THE TEAM")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ONE</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">CHAT</text>
      </svg>
      {cap("research, outreach, deals, content, code, publishing, legal. each callable by name.")}</div>'''

# 4. RESEARCH - IVORY: sources bezier-converge into one ranked brief document (replaces copy-paste)
def research():
    src=[("the person",112),("the company",184),("the market",256),("the news",328)]
    docx=468; docmid=220
    edges=""; nodes=""
    for nm,y in src:
        mx=(190+docx)/2
        edges+=f'<path d="M192 {y} C{mx:.0f} {y},{mx:.0f} {docmid},{docx-4} {docmid}" stroke="rgba(150,90,45,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=(f'<rect x="40" y="{y-24}" width="152" height="48" rx="12" fill="rgba(255,255,255,.55)" stroke="rgba(150,90,45,.28)"/>'
          f'<text x="116" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#5a4634">{nm}</text>')
    rows=""
    for i,(lab,sc) in enumerate([("Northwind Robotics","92"),("Globex Systems","88"),("Initech","81")]):
        yy=176+i*52
        rows+=(f'<rect x="490" y="{yy}" width="286" height="40" rx="9" fill="rgba(255,255,255,.72)" stroke="rgba(150,90,45,.18)"/>'
          f'<text x="506" y="{yy+26}" font-family="DM Sans" font-weight="700" font-size="16" fill="#2a2016">{lab}</text>'
          f'<circle cx="742" cy="{yy+20}" r="15" fill="#96562d"/>'
          f'<text x="742" y="{yy+25}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="13" fill="#fff">{sc}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("One brief, not ten tabs","CORTEX","#2a2016","#96562d")}
      <svg width="812" height="440" viewBox="0 0 812 440" style="display:block;margin:0 auto">
        <rect x="466" y="120" width="330" height="228" rx="20" fill="rgba(255,255,255,.9)" stroke="rgba(150,90,45,.28)" stroke-width="1.5"/>
        <text x="490" y="152" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#96562d">RANKED BRIEF</text>
        {edges}{nodes}{rows}
      </svg>
      {cap("cortex profiles the person, company and market into one ranked brief.","#8a745a")}</div>'''

# 5. SYSTEMS - iso stack of SAVED, reused workflow cards; a crossed-out "pasted prompt" ghost on top
def systems():
    steps=[("Cold sequence","reused 34x",0),("ICP scoring","reused 21x",1),("Deal review","reused 12x",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M4 12h16M4 17h10"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{nm}</div><div style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">{sub}</div></div>'
          f'<svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    ghost=('<div style="display:flex;align-items:center;gap:14px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);border-radius:14px;padding:12px 18px;margin-bottom:20px;opacity:.72">'
      '<span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#7a7468;flex-shrink:0">PASTED PROMPT</span>'
      '<span style="font-family:DM Sans;font-size:17px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">copied into a strange app, then lost</span>'
      '<span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:#c84623;flex-shrink:0">gone</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 30px">
      {htitle("Systems, not prompts","SAVED &middot; REUSED")}
      {ghost}
      <div style="perspective:1900px;height:400px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:376px;position:relative">{cards}</div></div>
      {cap("every workflow saved, reused and improved. nothing pasted and lost.")}</div>'''

# 6. GATE - full batch held on the operator's reins, one lock (human gate)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="210" r="128" fill="url(#orb)"/></g>
        <text x="200" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">240</text>
        <text x="200" y="234" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">EMAILS READY</text>
        <path d="M332 210 H612" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="140" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,178)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="318" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every outbound move parks for your tap. augmented, never unsupervised.")}</div>'''

# 7. MEMORY - radial shared core, 5 lifelines, one severed (cut = blind)
def memory():
    cx,cy=210,210
    organs=[("ICP",-90),("pipeline",-18),("pricing",54),("docs",126),("voice",198)]
    lines=""; nodes=""
    for i,(nm,a) in enumerate(organs):
        x=cx+150*math.cos(math.radians(a)); y=cy+150*math.sin(math.radians(a)); cut=(i==2)
        col="rgb(200,70,35)" if cut else "rgba(212,162,127,.5)"; dash='stroke-dasharray="4 8"' if cut else ""
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="3" {dash}/>'
        if cut: lines+=f'<text x="{(cx+x)/2:.0f}" y="{(cy+y)/2-10:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb(200,70,35)">cut = blind</text>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="32" fill="#241f1a" stroke="{"rgba(200,70,35,.6)" if cut else "rgba(255,255,255,.14)"}" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="{"#6f6a60" if cut else "#cfc9bd"}">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="hb" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#hg2)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">CORE</text></svg>
      <div style="flex:1">
        {htitle("Cut the memory, it goes blind","SHARED CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing, docs and your voice. Every agent draws from one shared core.</div>
        {cap("one memory feeds all seven. no core, no company.")}</div></div>'''

# 8. PRICE - IVORY: competitor tall red bar vs Ultron tiny cents bar
def price():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Hundreds a month, or cents a run","THE PRICE","#2a2016","#96562d")}
      <svg width="812" height="430" viewBox="0 0 812 430" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="redbar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(200,70,35,.5)"/><stop offset="100%" stop-color="rgba(200,70,35,.18)"/></linearGradient>
          <linearGradient id="goldbar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c79a72"/><stop offset="100%" stop-color="#96562d"/></linearGradient>
        </defs>
        <rect x="120" y="70" width="180" height="300" rx="14" fill="url(#redbar)" stroke="rgba(200,70,35,.4)" stroke-width="1.5"/>
        <text x="210" y="46" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#c84623">$1,200</text>
        <text x="210" y="400" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#8a745a">the taped stack / mo</text>
        <rect x="512" y="336" width="180" height="34" rx="10" fill="url(#goldbar)"/>
        <text x="602" y="316" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#96562d">cents</text>
        <text x="602" y="400" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#8a745a">ultron / run</text>
      </svg>
      {cap("pay per token through one router. cents per thousand rows, not a monthly tax.","#8a745a")}</div>'''

PANELS={"stack":stack(),"router":router(),"agents":agents(),"research":research(),
        "systems":systems(),"gate":gate(),"memory":memory(),"price":price()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src22"; os.makedirs(outd,exist_ok=True)
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
