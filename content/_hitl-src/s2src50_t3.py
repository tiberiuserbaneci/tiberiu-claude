#!/usr/bin/env python3
# TIER 3 - THE ASSEMBLY LINE (reframe of "Claude Code into a content machine" -> Ultron founder floor).
# Each panel a UNIQUE hand-built coded scene on a clean rounded card, title + one-line cap, no chip strips.
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

# 1. INTAKE - raw inputs drop through a hopper, one glowing ORDER token exits onto the belt
def intake():
    fx=390
    inputs=[("A LEAD",150),("A MARKET",310),("A BRIEF",470),("A SIGNAL",630)]
    chips=""
    for nm,x in inputs:
        chips+=(f'<rect x="{x-72}" y="24" width="144" height="52" rx="13" fill="#221f1b" stroke="rgba(212,162,127,.32)"/>'
          f'<text x="{x}" y="57" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#d9d5cc">{nm}</text>'
          f'<path d="M{x} 78 C{x} 132,{fx} 138,{fx} 176" fill="none" stroke="rgba(212,162,127,.35)" stroke-width="2.4" stroke-dasharray="4 6"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You brief it once","LINE INTAKE")}
      <svg width="780" height="470" viewBox="0 0 780 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="fnl" cx="50%" cy="18%"><stop offset="0%" stop-color="rgba(212,162,127,.30)"/><stop offset="100%" stop-color="rgba(212,162,127,.05)"/></radialGradient>
        <radialGradient id="ord" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        {chips}
        <path d="M250 186 L530 186 L432 300 L348 300 Z" fill="url(#fnl)" stroke="rgba(212,162,127,.5)" stroke-width="2.2"/>
        <text x="390" y="242" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">HOPPER</text>
        <line x1="390" y1="300" x2="390" y2="360" stroke="rgba(212,162,127,.5)" stroke-width="2.4"/>
        <rect x="120" y="392" width="540" height="56" rx="12" fill="#1a1816" stroke="rgba(255,255,255,.08)"/>
        {"".join(f'<circle cx="{c}" cy="420" r="6" fill="rgba(255,255,255,.09)"/>' for c in range(150,640,58))}
        <g filter="url(#og)"><circle cx="390" cy="388" r="35" fill="url(#ord)"/></g>
        <text x="390" y="393" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">ORDER</text>
      </svg>
      {cap("hand-crafting each asset does not scale. one order feeds the whole line.")}</div>'''

# 2. ROUTER - the line reads the order and drops it on the cheapest tier track that can run it
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
        cards+=(f'<div style="position:absolute;left:300px;top:{y-40}px;width:160px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The line picks its tools","MODEL ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the order</text>
        </svg>
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">1 order<br>on the belt</div>
        {cards}
      </div>
      {cap("one order in, the cheapest tier that can actually run it - cents, not dollars.")}</div>'''

# 3. STATIONS - seven single-purpose workstations along one conveyor, one running
def stations():
    fns=[("RESEARCH",1),("OUTBOUND",2),("DEALS",3),("CONTENT",4),("CODE",5),("PUBLISH",6),("LEGAL",7)]
    lit=3
    pods=""
    for i,(nm,n) in enumerate(fns):
        on=(i==lit)
        bg="linear-gradient(160deg,#413a32,#241f1a)" if on else "linear-gradient(160deg,#2a2724,#1e1b18)"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.08)"
        glow="box-shadow:0 0 24px rgba(212,162,127,.35)" if on else ""
        badge=f"rgb({ACC})" if on else "rgba(212,162,127,.22)"
        badgeink="#2a160c" if on else "#d9d5cc"
        stat="running" if on else "ready"
        statc=f"rgb({ACC})" if on else "#6f6a60"
        pods+=(f'<div style="flex:1;background:{bg};border:1.5px solid {bd};border-radius:15px;padding:16px 6px 14px;text-align:center;{glow}">'
          f'<div style="width:30px;height:30px;margin:0 auto 10px;border-radius:9px;background:{badge};display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:15px;color:{badgeink}">{n}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:#e6e1d6">{nm}</div>'
          f'<div style="font-family:DM Mono;font-size:10.5px;color:{statc};margin-top:6px">{stat}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Seven workers, one belt","THE STATIONS")}
      <div style="height:22px"></div>
      <div style="display:flex;gap:9px;align-items:stretch">{pods}</div>
      <div style="height:20px;margin-top:20px;border-radius:8px;background:repeating-linear-gradient(90deg,#26231f,#26231f 16px,#191714 16px,#191714 32px);box-shadow:inset 0 2px 5px rgba(0,0,0,.6)"></div>
      <div style="display:flex;justify-content:space-between;margin-top:8px;font-family:DM Mono;font-size:11px;color:#6f6a60"><span>order enters</span><span>finished asset</span></div>
      {cap("research, outbound, deals, content, code, publish, legal - each does one thing.")}</div>'''

# 4. OUTPUT - IVORY: finished founder assets ride off the belt in every format
def output():
    IK="#2a2016"
    env='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/></svg>'
    doc='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2"><path d="M6 3h9l4 4v14H6z"/><path d="M9 12h7M9 16h7"/></svg>'
    chat='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2"><path d="M4 5h16v11H9l-4 4z"/><path d="M8 9h8M8 12h5"/></svg>'
    bar='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2"><path d="M4 20V4"/><rect x="7" y="12" width="3" height="6"/><rect x="12" y="8" width="3" height="10"/><rect x="17" y="5" width="3" height="13"/></svg>'
    flow='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2"><circle cx="6" cy="6" r="2.4"/><circle cx="18" cy="12" r="2.4"/><circle cx="6" cy="18" r="2.4"/><path d="M8 7l8 4M8 17l8-4"/></svg>'
    items=[("COLD EMAIL",env,-4),("PROPOSAL",doc,3),("POST",chat,-3),("DEAL BRIEF",bar,4),("SEQUENCE",flow,-2)]
    row=""
    for lbl,gl,tl in items:
        row+=(f'<div style="flex:1;transform:rotate({tl}deg);background:#fffdf9;border:1px solid rgba(120,95,60,.22);border-radius:14px;padding:16px 10px 15px;box-shadow:0 16px 26px rgba(120,95,60,.22)">'
          f'{gl}<div style="font-family:DM Sans;font-weight:800;font-size:14px;color:{IK};margin-top:9px;line-height:1.15">{lbl}</div>'
          f'<div style="height:5px;background:rgba(150,120,80,.28);border-radius:3px;margin-top:9px"></div>'
          f'<div style="height:5px;width:68%;background:rgba(150,120,80,.28);border-radius:3px;margin-top:5px"></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 32px">
      {htitle("One input, every format",'OFF THE BELT',IK)}
      <div style="display:flex;gap:14px;align-items:flex-end;padding:14px 0 6px">{row}</div>
      <div style="height:20px;margin-top:16px;border-radius:8px;background:repeating-linear-gradient(90deg,#e6dac4,#e6dac4 15px,#d6c6a8 15px,#d6c6a8 30px);box-shadow:inset 0 2px 4px rgba(120,95,60,.32)"></div>
      {cap("finished work, not chat replies - emails, proposals, posts, briefs, sequences.","#8a745a")}</div>'''

# 5. THROUGHPUT - IVORY: cost per finished unit, cents vs the old stack's dollars
def throughput():
    IK="#2a2016"; maxw=470
    rows=[("THE OLD STACK","$140 / asset","seats + tools + hours",maxw,"#c84623",False),
          ("THE ULTRON LINE","0.4c / asset","pay per token",26,"#96562d",True)]
    bars=""
    for nm,val,sub,w,col,ours in rows:
        strike="text-decoration:line-through;text-decoration-color:#c84623" if not ours else ""
        bars+=(f'<div style="margin-bottom:22px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#7a6a52">{nm}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:20px;color:{col};{strike}">{val}</span></div>'
          f'<div style="height:26px;width:{w}px;border-radius:7px;background:{col};box-shadow:0 8px 16px rgba(150,120,80,.22)"></div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8a745a;margin-top:6px">{sub}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {htitle("A finished asset costs cents",'COST PER UNIT',IK)}
      <div style="display:flex;align-items:center;gap:36px">
        <div style="flex-shrink:0;text-align:center">
          <div style="font-family:DM Sans;font-weight:900;font-size:88px;line-height:.9;color:#96562d">0.4c</div>
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.08em;color:#8a745a;margin-top:6px">per asset off<br>the line</div></div>
        <div style="flex:1">{bars}</div>
      </div>
      {cap("high prices only ever belong to the stack ultron replaces.","#8a745a")}</div>'''

# 6. WAREHOUSE - one memory core supplies every station from a shared rack
def warehouse():
    shelves=[("ICP","who to chase"),("PIPELINE","every open deal"),("PRICING","the cents story"),("DOCS","the whole product")]
    rack=""
    for i,(nm,sub) in enumerate(shelves):
        y=44+i*88
        rack+=(f'<div style="position:absolute;left:0;top:{y}px;width:236px;background:linear-gradient(160deg,#332e28,#221f1b);border:1px solid rgba(212,162,127,.28);border-left:4px solid rgb({ACC});border-radius:12px;padding:12px 16px">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#c9c3b8;margin-top:2px">{sub}</div></div>')
    nodes=[("stations",70),("outbound",170),("content",270),("deals",370)]
    lines=""; dots=""
    for nm,y in nodes:
        lines+=f'<path d="M470 210 C560 210,600 {y},700 {y}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.2"/>'
        dots+=(f'<circle cx="704" cy="{y}" r="19" fill="#221f1b" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="704" y="{y+34}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;position:relative">
      {htitle("Every station pulls one core","THE WAREHOUSE")}
      <div style="position:relative;height:420px">
        <div style="position:absolute;left:0;top:0;width:236px">{rack}</div>
        <svg width="780" height="420" viewBox="0 0 780 420" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="wc" cx="40%" cy="34%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
          <filter id="wg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
          {lines}
          <g filter="url(#wg)"><circle cx="410" cy="210" r="60" fill="url(#wc)"/></g>
          <text x="410" y="204" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#2a160c">MEMORY</text>
          <text x="410" y="226" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">shared core</text>
          {dots}
        </svg>
      </div>
      {cap("icp, pipeline, pricing, docs - one warehouse feeds them all. cut it, the floor goes dark.")}</div>'''

# 7. QC - the shipping bay: every finished asset parks at the gate for the operator's stamp
def qc():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing ships without you","SHIPPING BAY")}
      <svg width="800" height="420" viewBox="0 0 800 420" style="display:block;margin:0 auto">
        <defs><linearGradient id="crate" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a332c"/><stop offset="100%" stop-color="#241f1a"/></linearGradient>
        <radialGradient id="stmp" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <rect x="40" y="140" width="230" height="170" rx="14" fill="url(#crate)" stroke="rgba(212,162,127,.3)" stroke-width="2"/>
        <line x1="40" y1="200" x2="270" y2="200" stroke="rgba(212,162,127,.28)" stroke-width="2"/>
        <line x1="155" y1="140" x2="155" y2="310" stroke="rgba(212,162,127,.28)" stroke-width="2"/>
        <text x="155" y="130" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#c9c3b8">FINISHED ASSET</text>
        <path d="M270 225 H470" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="486" y="150" width="150" height="150" rx="18" fill="none" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g filter="url(#sg)"><circle cx="561" cy="205" r="58" fill="url(#stmp)"/></g>
        <path d="M537 205 l16 16 30 -34" fill="none" stroke="#2a160c" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="561" y="332" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
        <text x="690" y="205" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">HELD FOR</text>
        <text x="690" y="226" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">APPROVAL</text>
      </svg>
      {cap("every external move parks at the bay. augmented, never running loose.")}</div>'''

# 8. FACTORY - the whole floor as one connected line, run from a single login
def factory():
    stages=[("INTAKE","brief in",70),("ROUTER","tier picked",258),("STATIONS","work done",446),("BAY","you ship",634)]
    boxes=""; conns=""
    for i,(nm,sub,x) in enumerate(stages):
        boxes+=(f'<div style="position:absolute;left:{x}px;top:150px;width:150px;background:linear-gradient(160deg,#332e28,#211e1a);border:1.5px solid rgba(212,162,127,.32);border-radius:16px;padding:16px 12px;text-align:center;box-shadow:0 20px 34px rgba(0,0,0,.5)">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:15px;color:#e6e1d6;margin-top:5px">{sub}</div></div>')
        if i<len(stages)-1:
            conns+=f'<path d="M{x+150} 188 H{stages[i+1][2]}" fill="none" stroke="rgb({ACC})" stroke-width="3" marker-end="url(#ar)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("One floor, one login","THE FULL LINE")}
      <div style="position:relative;height:400px">
        <svg width="810" height="400" viewBox="0 0 810 400" style="position:absolute;left:0;top:0">
          <defs><marker id="ar" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0 0l6 3-6 3z" fill="rgb({ACC})"/></marker>
          <radialGradient id="ctrl" cx="40%" cy="34%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          {conns}
          <g filter="url(#cg)"><rect x="330" y="320" width="150" height="56" rx="16" fill="url(#ctrl)"/></g>
          <text x="405" y="355" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">ONE LOGIN</text>
          <path d="M405 260 V320" stroke="rgba(212,162,127,.4)" stroke-width="2" stroke-dasharray="4 6"/>
          <path d="M405 260 H405" stroke="none"/>
          {"".join(f'<path d="M{x+75} 236 V262 H405 V320" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="1.5"/>' for _,_,x in stages)}
        </svg>
        {boxes}
      </div>
      {cap("intake, routing, stations and the bay - one chat runs the whole plant.")}</div>'''

PANELS={"intake":intake(),"router":router(),"stations":stations(),"output":output(),
        "throughput":throughput(),"warehouse":warehouse(),"qc":qc(),"factory":factory()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src50"; os.makedirs(outd,exist_ok=True)
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
