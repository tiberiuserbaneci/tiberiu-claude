#!/usr/bin/env python3
# TIER 3 - SIX MONTHS BUILDING, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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

# 1. TIMELINE - a build log: six month markers down a lit spine, each a lesson, the last one glowing
def timeline():
    rows=[("MONTH 1","Clever prompts. So clever.",False),
          ("MONTH 2","They broke on turn two.",False),
          ("MONTH 3","Wrapped them in loops.",False),
          ("MONTH 4","Gave the loop a memory.",False),
          ("MONTH 5","Put a gate in front.",False),
          ("MONTH 6","Routed the model per turn.",True)]
    items=""
    for m,l,on in rows:
        dot=f"rgb({ACC})" if on else "rgba(212,162,127,.32)"
        glow="box-shadow:0 0 18px rgba(212,162,127,.85)" if on else ""
        ring="border:3px solid rgba(212,162,127,.9)" if on else "border:3px solid rgba(212,162,127,.28)"
        lcol="#FAFAF7" if on else "#c4bfb4"
        wt=900 if on else 700
        items+=(f'<div style="display:flex;align-items:center;gap:26px;height:66px">'
          f'<div style="flex-shrink:0;width:22px;height:22px;border-radius:50%;background:{dot};{ring};{glow};position:relative;z-index:2"></div>'
          f'<div style="width:118px;flex-shrink:0;font-family:\'DM Mono\';font-size:14px;letter-spacing:.14em;color:rgb({ACC})">{m}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:{wt};font-size:25px;color:{lcol}">{l}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Six months, six rewrites","BUILD LOG")}
      <div style="position:relative;padding:6px 0">
        <div style="position:absolute;left:10px;top:34px;bottom:34px;width:3px;background:linear-gradient(180deg,rgba(212,162,127,.18),rgb({ACC}));z-index:1"></div>
        {items}
      </div>
      {cap("everything i shipped in month one was outdated by month three.")}</div>'''

# 2. LOOPS - a running loop cycle (plan/act/check/repeat) vs a dead single prompt
def loops():
    cx,cy,R=210,210,142
    steps=[("PLAN",-90),("ACT",0),("CHECK",90),("ADAPT",180)]
    nodes=""
    for nm,a in steps:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgb({ACC})" stroke-width="2.5"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#e6dccb">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:28px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs>
          <marker id="ah" markerWidth="12" markerHeight="12" refX="6" refY="6" orient="auto"><path d="M1 1 L10 6 L1 11" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></marker>
          <filter id="lgw" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter>
        </defs>
        <g filter="url(#lgw)"><circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="6" stroke-dasharray="{2*math.pi*R*0.72:.0f} {2*math.pi*R:.0f}" transform="rotate(-64 {cx} {cy})" marker-end="url(#ah)"/></g>
        {nodes}
        <circle cx="{cx}" cy="{cy}" r="52" fill="#1c1917" stroke="rgba(212,162,127,.35)" stroke-width="1.5"/>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="rgb({ACC})">LOOP</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">runs again</text>
      </svg>
      <div style="flex:1">
        {htitle("A prompt fires once","LOOP &gt; PROMPT")}
        <div style="font-family:DM Sans;font-size:20px;color:#c9c3b8;line-height:1.45">A prompt answers and forgets. A loop plans, acts, checks its own work, and goes again until the job is actually done.</div>
        <div style="display:flex;align-items:center;gap:14px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);border-radius:14px;padding:13px 18px;margin-top:18px;opacity:.8">
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#7a7468;flex-shrink:0">ONE PROMPT</span>
          <span style="font-family:DM Sans;font-size:17px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">answers, then dies on turn two</span></div>
        {cap("the loop is the one thing from month one that survived.")}
      </div></div>'''

# 3. MEMORY - IVORY radial core: one memory feeding every agent through lit lifelines
def memory():
    cx,cy=210,210
    agents=[("CORTEX",-90),("SPECTER",-18),("STRIKER",54),("PULSE",126),("SENTINEL",198)]
    lines=""; nodes=""
    for nm,a in agents:
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="31" fill="#fbf6ec" stroke="rgba(150,90,45,.4)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" letter-spacing=".04em" fill="#7a5230">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#c98a56"/><stop offset="60%" stop-color="#96562d"/><stop offset="100%" stop-color="#6d3c1e"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="6" stdDeviation="16" flood-color="rgba(150,90,45,.45)"/></filter></defs>
        {lines}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#fdf6ec">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#f0d9c2">one core</text>
      </svg>
      <div style="flex:1">
        {htitle("Context forgets. Memory holds.","MEMORY &gt; CONTEXT","#2a2016")}
        <div style="font-family:DM Sans;font-size:19px;color:#4a3c2c;line-height:1.45">ICP, pipeline, pricing, docs. Every agent reads the same core, so nothing has to be re-explained. Cut the memory and every window starts blank.</div>
        {cap("a window forgets in an hour. the core remembers you for good.","#8a745a")}</div></div>'''

# 4. GATE - full-capability orb held on the operator's reins, one lock (HUMAN GATE)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Autonomy, on a leash","GATE &gt; AUTOPILOT")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="210" r="132" fill="url(#orb)"/></g>
        <text x="200" y="202" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">FULL</text>
        <text x="200" y="238" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <path d="M334 210 H612" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="622" y="140" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(664,178)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="692" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">HUMAN GATE</text>
      </svg>
      {cap("i gave it every tool, then kept the reins. it parks for my tap, always.")}</div>'''

# 5. ROUTER - one job routed down 3 tier lanes, SMART lane lit/picked, cents on each
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
      {htitle("One model cannot pay the bill","ROUTING &gt; ONE MODEL")}
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
      {cap("the cheapest tier that can actually do the job - cents, never dollars.")}</div>'''

# 6. RADAR - the field keeps moving: live blips, and a Jan-vs-Jun relearn readout
def radar():
    cx,cy,R=205,215,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("new pattern",300,150),("new tool",120,96),("new limit",210,168),("new lever",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    readout=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      '<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">January playbook</span><span style="font-family:DM Mono;font-size:13px;color:rgb(200,70,35)">stale</span></div>'
      '<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">June playbook</span>'
      f'<span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">live</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">relearned 4x</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="410" height="410" viewBox="0 0 410 410">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("Last year's map is stale","THE FIELD MOVES")}
        {readout}
        {cap("what worked in january was gone by june. the field moves weekly.")}
      </div></div>'''

# 7. STACK - IVORY isometric stack of the four rules that survived every rewrite
def stack():
    rows=[("Loops","beat prompts","runs until done"),
          ("Memory","beats context","never re-explains"),
          ("Gate","beats autopilot","parks for your tap"),
          ("Routing","beats one model","cents per job")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*110
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;'
          f'background:linear-gradient(160deg,#fdfbf6,#ece1cf);border:1.5px solid rgba(150,90,45,.28);border-radius:18px;padding:18px 24px;'
          f'box-shadow:0 30px 44px rgba(120,95,60,.28), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:22px">'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Sans\';font-weight:900;font-size:26px;color:#2a2016">{a} <span style="font-weight:500;font-size:20px;color:#8a5a30">{b}</span></div>'
          f'<div style="font-family:\'DM Mono\';font-size:14px;color:#9a7a52;margin-top:2px">{c}</div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:12px;background:#96562d;box-shadow:0 6px 14px rgba(150,90,45,.4)">'
          f'<svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="#fdf6ec" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 44px 34px">
      {htitle("Four rules survived every rewrite","THE KEEPERS","#2a2016")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:600px;height:410px;position:relative">{cards}</div></div>
      {cap("six months of building distilled to four lines that stopped breaking.","#8a745a")}</div>'''

# 8. HUB - radial hub: seven agents on one memory, one gate, one router (the Ultron way)
def hub():
    cx,cy=410,215
    agents=[("CORTEX",-90),("SPECTER",-38),("STRIKER",14),("PULSE",66),("SENTINEL",118),("AMPLIFY",170),("COUNSEL",222)]
    spokes=""; nodes=""
    for nm,a in agents:
        x=cx+168*math.cos(math.radians(a)); y=cy+168*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.5"/>'
        nodes+=(f'<rect x="{x-52:.0f}" y="{y-19:.0f}" width="104" height="38" rx="12" fill="#241f1a" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="#e6dccb">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ship a system, not a prompt","ONE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="98" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">SYSTEM</text>
        {nodes}
      </svg>
      {cap("seven agents, one memory, one gate, one router. that is the whole lesson.")}</div>'''

PANELS={"timeline":timeline(),"loops":loops(),"memory":memory(),"gate":gate(),
        "router":router(),"radar":radar(),"stack":stack(),"hub":hub()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s26monthsbuilding"; os.makedirs(outd,exist_ok=True)
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
