#!/usr/bin/env python3
# TIER 3 - THE STACK IS NOT A SYSTEM, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips,
# no cuts/walls. Reframe of "22 Claude skills & repos" into the Ultron one-system story.
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

# 1. STACK TAX - isometric pile of 22 dim repo/skill tiles, all yours to maintain, one red weight tag
def stack():
    rows=[("anthropics/skills","23 skills to wire"),
          ("mcp-servers/*","14 servers to host"),
          ("prompt-library","89 prompts to tune"),
          ("agent-glue.py","the code you own")]
    cards=""
    for i,(a,b) in enumerate(rows):
        y=i*118; dim=0.55+0.15*i
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;opacity:{dim:.2f};'
          f'background:linear-gradient(160deg,#33302b,#211e1a);border:1.5px solid rgba(255,255,255,.10);border-radius:18px;'
          f'padding:18px 22px;box-shadow:0 26px 40px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.07);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(250,250,247,.05);border:1px solid rgba(255,255,255,.10);'
          f'display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8f8f85" stroke-width="2"><path d="M3 7h6l2 2h10v9a2 2 0 0 1-2 2H3z"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:17px;color:#d9d5cc">{a}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#8f8f85;margin-top:2px">{b}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("You maintain all of it","22 REPOS &middot; 1 YOU")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:400px;background:rgb(200,70,35);color:#FAFAF7;font-family:DM Sans;font-weight:900;font-size:15px;padding:9px 20px;border-radius:999px;box-shadow:0 12px 24px rgba(200,70,35,.4)">every one is your problem</div></div></div>
      {cap("skills, repos, prompts, servers - you are the glue holding the pile together.")}</div>'''

# 2. ROUTER - one job token routed down 3 tier lanes, SMART lane lit/picked, cents cost
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
    hubx,hy,lx=170,230,470
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
      {htitle("You never pick a model","MODEL ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">draft 12<br>follow-ups</div>
        {cards}
      </div>
      {cap("one job in, the cheapest tier that can actually do it - cents, not dollars.")}</div>'''

# 3. THE SEVEN - radial hub-and-spokes, seven named agents around the Ultron core
def roster():
    cx,cy,Rr=306,232,182
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""
    n=len(agents)
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(212,162,127,.42)" stroke-width="1.8"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14.5" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one roster","THE SEVEN")}
      <svg width="612" height="500" viewBox="0 0 612 500" style="display:block;margin:0 auto">
        <defs><radialGradient id="core3" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg3" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#cg3)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#core3)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">ULTRON</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one login</text>
      </svg>
      {cap("not 22 skills to bolt on - seven agents already wired to each other.")}</div>'''

# 4. CENTS PRICING - IVORY: cents ring gauge next to a tall competitor $ bar vs a sliver Ultron bar
def cents():
    pct=97; r=74; circ=2*math.pi*r; dash=circ*pct/100
    bars=[("A tool stack","$90 / mo",300,"#c85a3a",True),("Ultron, this run","cents",22,"#96562d",False)]
    bh=""
    base=300
    for nm,val,h,col,comp in bars:
        top=base-h
        badge='competitor' if comp else 'you'
        bh+=(f'<div style="display:flex;flex-direction:column;align-items:center;width:150px">'
          f'<div style="height:{base-h}px"></div>'
          f'<div style="width:96px;height:{h}px;border-radius:14px 14px 4px 4px;background:linear-gradient(180deg,{col},{col}cc);box-shadow:0 12px 22px rgba(150,90,45,.22)"></div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#2a2016;margin-top:12px">{val}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:#8a745a;margin-top:2px">{nm}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Everything costs cents","PAY PER TOKEN","#2a2016")}
      <div style="display:flex;align-items:center;gap:44px">
        <div style="flex-shrink:0;position:relative;width:196px;height:196px">
          <svg width="196" height="196" viewBox="0 0 196 196">
            <circle cx="98" cy="98" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="16"/>
            <circle cx="98" cy="98" r="{r}" fill="none" stroke="#96562d" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 98 98)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016">97%</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">cheaper</span></div></div>
        <div style="flex:1;display:flex;justify-content:space-around;align-items:flex-end;height:360px">{bh}</div>
      </div>
      {cap("the stack bills a flat fee. a full run here is cents per thousand rows.","#8a745a")}</div>'''

# 5. SYSTEMS NOT PROMPTS - IVORY bezier flow: one plain-English line composes an agent pipeline
def system():
    W,H=760,430
    stages=[("CORTEX","find 30 fits",110),("SPECTER","draft outreach",210),("STRIKER","qualify replies",310)]
    edges=""; nodes=""
    inx,iny=70,210; outx=680
    prev=(inx+40,iny)
    for nm,role,y in stages:
        nx=390
        edges+=f'<path d="M{prev[0]} {prev[1]} C{(prev[0]+nx)/2:.0f} {prev[1]},{(prev[0]+nx)/2:.0f} {y},{nx-118} {y}" fill="none" stroke="#c69a6e" stroke-width="2.6"/>'
        edges+=f'<path d="M{nx+118} {y} C{(nx+outx)/2:.0f} {y},{(nx+outx)/2:.0f} 210,{outx-30} 210" fill="none" stroke="#c69a6e" stroke-width="2.6"/>'
        nodes+=(f'<rect x="{nx-118}" y="{y-30}" width="236" height="60" rx="15" fill="#fbf5ea" stroke="rgba(150,90,45,.28)"/>'
          f'<text x="{nx-96}" y="{y-4}" font-family="DM Sans" font-weight="800" font-size="17" fill="#2a2016">{nm}</text>'
          f'<text x="{nx-96}" y="{y+17}" font-family="DM Sans" font-size="14" fill="#8a745a">{role}</text>'
          f'<circle cx="{nx+96}" cy="{y}" r="5" fill="#96562d"/>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("One line, a whole pipeline","COMPOSED","#2a2016")}
      <div style="background:rgba(255,255,255,.55);border-left:4px solid #96562d;border-radius:12px;padding:15px 20px;margin-bottom:18px;font-family:'DM Sans';font-size:19px;color:#2a2016">
        "Fill my pipeline with UK founders and warm them up."</div>
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="io" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="#c07a4a"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient></defs>
        {edges}
        <circle cx="{inx}" cy="{iny}" r="40" fill="url(#io)"/><text x="{inx}" y="{iny+5}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#2a160c">you</text>
        {nodes}
        <circle cx="{outx}" cy="210" r="46" fill="url(#io)"/><text x="{outx}" y="205" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#2a160c">DONE</text>
        <text x="{outx}" y="226" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">gated</text>
      </svg>
      {cap("plain english in, a composed pipeline of agents out - not one lonely prompt.","#8a745a")}</div>'''

# 6. HUMAN GATE - full-capability orb held on the operator's reins, a single lock
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Full power. Your one tap.","HUMAN GATE")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb6" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og6" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og6)"><circle cx="210" cy="220" r="132" fill="url(#orb6)"/></g>
        <text x="210" y="214" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">FULL</text>
        <text x="210" y="248" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <path d="M344 220 H612" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <text x="478" y="200" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">every external send</text>
        <rect x="624" y="150" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(666,188)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="694" y="326" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("nothing sends, ships or spends until you approve it. augmented, never unsupervised.")}</div>'''

# 7. SHARED MEMORY - one warm core, four data facets fed in from the left; distinct horizontal form
def memory():
    facets=[("ICP","who you sell to",110),("PIPELINE","every open deal",180),("PRICING","cents per run",250),("DOCS","product truth",320)]
    cx,cy=610,220
    edges=""; chips=""
    for nm,sub,y in facets:
        edges+=f'<path d="M330 {y} C450 {y},470 {cy},{cx-96} {cy}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.6"/>'
        chips+=(f'<g><rect x="34" y="{y-32}" width="296" height="64" rx="16" fill="linear-gradient(160deg,#33302c,#201d1a)" stroke="rgba(255,255,255,.10)"/>'
          f'<rect x="34" y="{y-32}" width="296" height="64" rx="16" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="58" y="{y-4}" font-family="DM Mono" font-size="15" letter-spacing=".12em" fill="rgb({ACC})">{nm}</text>'
          f'<text x="58" y="{y+18}" font-family="DM Sans" font-size="15" fill="#c9c3b8">{sub}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One core they all read","SHARED MEMORY")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="mc" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{chips}
        <circle cx="{cx}" cy="{cy}" r="112" fill="none" stroke="rgba(212,162,127,.18)"/>
        <circle cx="{cx}" cy="{cy}" r="86" fill="none" stroke="rgba(212,162,127,.24)"/>
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one core</text>
      </svg>
      {cap("22 tools each forget you. here one memory feeds every agent, every time.")}</div>'''

# 8. THE OPERATOR - scattered agent nodes on the left converge into one glowing assembled system
def assemble():
    scat=[("router",70,86),("cortex",70,210),("gate",70,334),("memory",192,148),("specter",192,272)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+30} {y} C340 {y},360 210,520 210" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.72"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Assemble the system","ONE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod8" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg8" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg8)"><circle cx="590" cy="210" r="120" fill="url(#bod8)"/></g>
        <text x="590" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="590" y="230" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">SYSTEM</text>
        <text x="590" y="366" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">composed &middot; gated &middot; yours</text>
      </svg>
      {cap("one chat wires seven agents, router, memory and gate into a single operator.")}</div>'''

PANELS={"stack":stack(),"router":router(),"roster":roster(),"cents":cents(),
        "system":system(),"gate":gate(),"memory":memory(),"assemble":assemble()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src28"; os.makedirs(outd,exist_ok=True)
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
