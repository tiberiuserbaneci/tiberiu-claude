#!/usr/bin/env python3
# TIER 3 - STARRED, NOT SHIPPED. Reframe of "10 GitHub repos worth starring": a star is a bookmark,
# ten repos are loose unwired parts, and the assembly gap is the real work - Ultron ships the crew
# already wired and running. Eight UNIQUE hand-built coded scenes on clean rounded cards.
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

# 1. STAR - UI mock: a just-clicked glossy star button next to a dead deploy-status panel (red LEDs)
def star():
    rows=[("DEPLOYED","no"),("WIRED","no"),("RUNNING","nothing")]
    rowhtml=""
    for i,(k,v) in enumerate(rows):
        bd="border-bottom:1px solid rgba(255,255,255,.06)" if i<len(rows)-1 else ""
        rowhtml+=(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:18px 22px;{bd}">'
          f'<div style="display:flex;align-items:center;gap:14px"><span style="width:12px;height:12px;border-radius:50%;background:rgb(200,70,35);box-shadow:0 0 12px rgba(200,70,35,.7)"></span>'
          f'<span style="font-family:\'DM Mono\';font-size:16px;letter-spacing:.1em;color:#c9c3b8">{k}</span></div>'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#8f8f85">{v}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:18px">
        <div style="display:flex;align-items:center;gap:15px;padding:22px 30px;border-radius:18px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});box-shadow:0 0 34px rgba(212,162,127,.28), inset 0 2px 3px rgba(255,255,255,.12)">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="rgb({ACC})"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <div style="text-align:left"><div style="font-family:\'DM Sans\';font-weight:900;font-size:27px;color:#FAFAF7;line-height:1">Starred</div>
          <div style="font-family:\'DM Mono\';font-size:15px;color:rgb({ACC});margin-top:3px">12,431</div></div></div>
        <div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.1em;color:#8f8f85">ONE CLICK</div>
      </div>
      <div style="flex:1">
        {htitle("A star is a bookmark","SAVED")}
        <div style="background:#191715;border:1px solid rgba(255,255,255,.08);border-radius:18px;overflow:hidden;box-shadow:inset 0 2px 4px rgba(0,0,0,.4)">{rowhtml}</div>
        {cap("the star costs one click and runs nothing. a save, not a system.")}
      </div></div>'''

# 2. PILE - scattered field of 10 repo tiles, each with a dangling unconnected wire stub
def pile():
    repos=[("research-agent",34,34),("cold-email-bot",320,20),("deal-scorer",600,66),
           ("post-writer",120,150),("code-runner",416,148),("scheduler",636,214),
           ("contract-review",24,272),("web-scraper",312,286),("vector-memory",586,318),
           ("model-router",176,398)]
    tw,th=182,52; body=""
    for nm,x,y in repos:
        sx=x+tw; sy=y+th/2
        body+=(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<path d="M{x+18} {y+26} l6 -6 m0 6 l-6 -6 M{x+34} {y+20} l6 6 l-6 6" fill="none" stroke="rgb({ACC})" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<text x="{x+52}" y="{y+32}" font-family="DM Mono" font-size="15" fill="#c9c3b8">{nm}</text>'
          f'<line x1="{sx}" y1="{sy}" x2="{sx+24}" y2="{sy-16}" stroke="rgba(200,70,35,.5)" stroke-width="2.4" stroke-dasharray="3 5"/>'
          f'<circle cx="{sx+27}" cy="{sy-18}" r="5" fill="none" stroke="rgba(200,70,35,.6)" stroke-width="2"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten repos, zero wired","UNASSEMBLED")}
      <svg width="820" height="472" viewBox="0 0 820 472" style="display:block;margin:0 auto">
        {body}
        <text x="470" y="250" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="rgba(250,250,247,.13)">10 cloned</text>
        <text x="470" y="286" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="rgba(200,70,35,.5)">0 connected</text>
      </svg>
      {cap("each repo is a loose part with a dangling wire. connecting ten is its own project.")}</div>'''

# 3. GAP - IVORY blueprint: two ledges (STARRED / RUNNING) split by a chasm, missing bridge planks
def gap():
    planks=["clone","install deps","configure","wire APIs","host","patch"]
    gx0,gx1=248,572; pl=""
    for i,p in enumerate(planks):
        y=78+i*56
        pl+=(f'<rect x="{gx0}" y="{y}" width="{gx1-gx0}" height="38" rx="9" fill="none" stroke="rgba(150,90,45,.55)" stroke-width="2" stroke-dasharray="8 6"/>'
          f'<text x="{(gx0+gx1)/2:.0f}" y="{y+25}" text-anchor="middle" font-family="DM Mono" font-size="16" letter-spacing=".04em" fill="#96562d">{p}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("The gap is the work","STARRED / RUNNING","#2a2016")}
      <svg width="820" height="446" viewBox="0 0 820 446" style="display:block;margin:0 auto">
        <defs><linearGradient id="ledge" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f3ead9"/><stop offset="100%" stop-color="#dcccb0"/></linearGradient></defs>
        <rect x="18" y="52" width="196" height="360" rx="18" fill="url(#ledge)" stroke="rgba(120,90,55,.22)"/>
        <svg x="82" y="96" width="68" height="68" viewBox="0 0 24 24" fill="#96562d"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        <text x="116" y="210" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a2016">STARRED</text>
        <text x="116" y="238" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#8a745a">one click done</text>
        <rect x="606" y="52" width="196" height="360" rx="18" fill="url(#ledge)" stroke="rgba(120,90,55,.22)" opacity=".62"/>
        <g opacity=".62"><circle cx="704" cy="132" r="34" fill="none" stroke="#96562d" stroke-width="3"/><path d="M694 116 l24 16 l-24 16 Z" fill="#96562d"/>
        <text x="704" y="210" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a2016">RUNNING</text>
        <text x="704" y="238" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#8a745a">someday</text></g>
        {pl}
      </svg>
      {cap("clone, install, wire, host, patch. weeks of assembly between a star and a system.","#8a745a")}</div>'''

# 4. ROUTER - one plain-English job routed to the right agent + the cheapest model tier that fits
def router():
    lanes=[("SPECTER","outbound",118,False),("STRIKER","deals",210,True),("PULSE","content",302,False),("COUNSEL","legal",394,False)]
    hubx,hy=196,256; lx=486; edges=""; cards=""
    for nm,role,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+66} {hy} C340 {hy},350 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:\'DM Mono\';font-size:12px;color:rgb({ACC})">DEEP</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:308px;top:{y-38}px;width:170px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:13px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#8f8f85;margin-top:2px">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One line hires the agent","THE ROUTER")}
      <div style="position:relative;height:452px">
        <svg width="820" height="452" viewBox="0 0 820 452" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="14" y="{hy-30}" width="120" height="60" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="66" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:20px;top:232px;width:108px;font-family:\'DM Mono\';font-size:12.5px;color:#c9c3b8;text-align:center">reply to<br>this objection</div>
        {cards}
      </div>
      {cap("type the job in plain english. it hires the agent and the tier that can actually do it.")}</div>'''

# 5. TEAM - radial hub-and-spokes: seven Ultron agents pre-wired to one core, all lit
def team():
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),
            ("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    cx,cy,R=410,238,178; n=len(agents); spokes=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#241f1a" stroke="rgb({ACC})" stroke-width="1.8"/>'
          f'<text x="{x:.0f}" y="{y-3:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14.5" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The crew comes wired","SEVEN AGENTS")}
      <svg width="820" height="476" viewBox="0 0 820 476" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ONE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">CREW</text>
        {nodes}
      </svg>
      {cap("research, outbound, deals, content, code, publishing, legal. talking on day one.")}</div>'''

# 6. MEMORY - IVORY isometric stack of shared-vault cards every agent reads from
def memory():
    recs=[("ICP","founder, 2-50, US and UK"),("PIPELINE","18 open, 4 late stage"),
          ("PRICING","cents per token"),("DOCS","51 pages indexed")]
    cards=""
    for i,(k,v) in enumerate(recs):
        y=i*112
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#fffdf8,#f0e7d6);border:1px solid rgba(120,95,60,.20);border-radius:18px;padding:20px 26px;box-shadow:0 26px 40px rgba(120,95,60,.20), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:22px">'
          f'<div style="flex-shrink:0;width:12px;height:52px;border-radius:6px;background:#96562d"></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.14em;color:#96562d">{k}</div><div style="font-family:\'DM Sans\';font-weight:800;font-size:22px;color:#2a2016">{v}</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 44px 34px">
      {htitle("One vault under it all","SHARED CORE","#2a2016")}
      <div style="perspective:1900px;height:460px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:414px;position:relative">{cards}</div></div>
      {cap("ten repos forget you at every restart. one core every agent reads from.","#8a745a")}</div>'''

# 7. GATE - full-capability orb held on the operator's reins, one lock/tap
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Full power. Your tap.","HUMAN GATE")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="215" r="130" fill="url(#orb)"/></g>
        <text x="200" y="209" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">FULL</text>
        <text x="200" y="243" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <path d="M334 215 H610" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="145" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,183)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="321" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every send, deal and deploy parks for your approval. augmented, never loose.")}</div>'''

# 8. RUNNING - live uptime ring gauge + running-process rows (no clone, no install)
def running():
    r=78; circ=2*math.pi*r; dash=circ*0.999
    procs=[("CORTEX","building a brief"),("SPECTER","sending 12 follow-ups"),("SENTINEL","shipped PR #182")]
    rows=""
    for nm,act in procs:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:#221f1b;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:15px 18px;margin-bottom:12px">'
          f'<span style="flex-shrink:0;width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba(212,162,127,.8)"></span>'
          f'<span style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.1em;color:rgb({ACC});width:96px">{nm}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#eae4d8">{act}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:36px">
      <div style="flex-shrink:0;position:relative;width:210px;height:210px">
        <svg width="210" height="210" viewBox="0 0 210 210">
          <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="16"/>
          <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 105 105)" filter="url(#rg)"/>
          <defs><filter id="rg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs></svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:\'DM Sans\';font-weight:900;font-size:40px;color:#FAFAF7">99.9%</span>
          <span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:rgb({ACC})">UPTIME</span></div></div>
      <div style="flex:1">
        {htitle("Running when you log in","LIVE")}
        {rows}
        {cap("no clone, no install. one login and the operator is already working.")}
      </div></div>'''

PANELS={"star":star(),"pile":pile(),"gap":gap(),"router":router(),
        "team":team(),"memory":memory(),"gate":gate(),"running":running()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src17"; os.makedirs(outd,exist_ok=True)
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
