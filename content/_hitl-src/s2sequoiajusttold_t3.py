#!/usr/bin/env python3
# TIER 3 - THE WRONG DOLLAR / THE LAYER, built to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO stat-chip strips.
# Reframe: value is the layer around the model (memory/router/agents/gate), Ultron = that layer at cents.
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
def ivtitle(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

def _arc(cx,cy,rO,rI,a0,a1):
    x0=cx+rO*math.cos(a0); y0=cy+rO*math.sin(a0)
    x1=cx+rO*math.cos(a1); y1=cy+rO*math.sin(a1)
    xi1=cx+rI*math.cos(a1); yi1=cy+rI*math.sin(a1)
    xi0=cx+rI*math.cos(a0); yi0=cy+rI*math.sin(a0)
    lg=1 if (a1-a0)>math.pi else 0
    return f'M{x0:.1f} {y0:.1f} A{rO} {rO} 0 {lg} 1 {x1:.1f} {y1:.1f} L{xi1:.1f} {yi1:.1f} A{rI} {rI} 0 {lg} 0 {xi0:.1f} {yi0:.1f} Z'

# 1. VALUESTACK - model tokens are a thin sliver, THE LAYER is a tall stacked tower beside it
def valuestack():
    layers=[("HUMAN GATE","approval, held"),("AGENT ROSTER","7 specialists"),("THE ROUTER","model per job"),("SHARED MEMORY","one core")]
    shades=["#5a4030","#4a3628","#3a2c22","#2e241c"]
    segs=""
    for (nm,sub),sh in zip(layers,shades):
        segs+=f'''<div style="width:264px;height:98px;background:linear-gradient(160deg,{sh},#241c16);border:1px solid rgba(212,162,127,.30);border-radius:15px;margin-bottom:11px;display:flex;flex-direction:column;justify-content:center;padding:0 24px;box-shadow:0 16px 28px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07)">
          <span style="font-family:'DM Sans';font-weight:800;font-size:22px;color:#FAFAF7">{nm}</span>
          <span style="font-family:'DM Mono';font-size:13px;color:#c9a583;margin-top:2px">{sub}</span></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The dollar moved up the stack","MODEL vs LAYER")}
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:74px;padding:8px 20px 4px">
        <div style="display:flex;flex-direction:column;align-items:center">
          <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:rgb({ACC});line-height:1">cents</div>
          <div style="width:172px;height:86px;margin-top:14px;border-radius:15px;background:linear-gradient(160deg,#4a423a,#2a2622);border:1px solid rgba(255,255,255,.12);box-shadow:0 16px 28px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center">
            <span style="font-family:'DM Mono';font-size:15px;letter-spacing:.06em;color:#cfc9bd">model tokens</span></div>
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#8f8f85;margin-top:16px">MODEL SPEND</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:rgb({ACC});margin-bottom:12px">THE LAYER &middot; VALUE LIVES HERE</div>
          {segs}
        </div>
      </div>
      {cap("the tokens are cents. the layer around them is the whole company.")}</div>'''

# 2. SPEND - donut allocation: model tokens a thin sliver, the layer the whole ring (IVORY)
def spend():
    data=[("Model tokens",8,"#caa079"),("Shared memory",26,"#96562d"),("The router",16,"#b56a37"),("Agent roster",30,"#7a4326"),("Human gate",20,"#c8813f")]
    cx,cy,rO,rI=205,210,152,92
    a=-math.pi/2; segs=""
    for nm,pct,col in data:
        a1=a+2*math.pi*pct/100
        segs+=f'<path d="{_arc(cx,cy,rO,rI,a,a1)}" fill="{col}" stroke="#fdfbf6" stroke-width="3"/>'
        a=a1
    legend=""
    for nm,pct,col in data:
        legend+=f'''<div style="display:flex;align-items:center;gap:13px;margin-bottom:15px">
          <span style="width:16px;height:16px;border-radius:5px;background:{col};flex-shrink:0"></span>
          <span style="flex:1;font-family:'DM Sans';font-weight:600;font-size:19px;color:#2a2016">{nm}</span>
          <span style="font-family:'DM Mono';font-weight:500;font-size:18px;color:#5a4634">{pct}%</span></div>'''
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {ivtitle("Where the money goes","SPEND MAP")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex-shrink:0;position:relative;width:410px;height:420px">
          <svg width="410" height="420" viewBox="0 0 410 420">{segs}</svg>
          <div style="position:absolute;left:0;top:0;width:410px;height:420px;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:#96562d">MODEL</span>
            <span style="font-family:'DM Sans';font-weight:900;font-size:56px;color:#2a2016;line-height:1;margin-top:2px">8%</span>
            <span style="font-family:'DM Mono';font-size:13px;color:#8a745a;margin-top:6px">the layer: 92%</span></div>
        </div>
        <div style="flex:1">{legend}</div>
      </div>
      {cap("raw model calls are the smallest line. the layer is where the value sits.","#8a745a")}</div>'''

# 3. GRAPH - one JOB routed through the ROUTER hub, wired out to the agent roster (bezier)
def graph():
    W,H=820,440
    agents=[("CORTEX","research",70),("SPECTER","outbound",180),("STRIKER","deals",290),("PULSE","content",400)]
    hubx,hy=320,235; ax=560
    edges=""; cards=""
    for nm,role,y in agents:
        mx=(hubx+ax)/2
        edges+=f'<path d="M{hubx+66} {hy} C{mx:.0f} {hy},{mx:.0f} {y},{ax-6} {y}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.6"/>'
        cards+=(f'<g><rect x="{ax}" y="{y-34}" width="238" height="68" rx="15" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="{ax+30}" cy="{y}" r="8" fill="rgb({ACC})"/>'
          f'<text x="{ax+56}" y="{y-2}" font-family="DM Sans" font-weight="800" font-size="20" fill="#FAFAF7">{nm}</text>'
          f'<text x="{ax+56}" y="{y+19}" font-family="DM Mono" font-size="13" fill="#8f8f85">{role}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One job, the right agents","ORCHESTRATION")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="ghub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        <rect x="14" y="{hy-30}" width="120" height="60" rx="14" fill="#241f1a" stroke="rgba(255,255,255,.10)"/>
        <text x="74" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#e2dccf">JOB</text>
        <text x="74" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">plain english</text>
        <path d="M134 {hy} C220 {hy},220 {hy},{hubx-66} {hy}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.6"/>
        {edges}
        <g filter="url(#gg)"><circle cx="{hubx}" cy="{hy}" r="66" fill="url(#ghub)"/></g>
        <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        {cards}
      </svg>
      {cap("the router reads the job and wires the agents that finish it, cents per turn.")}</div>'''

# 4. MEMORY - radial shared core: five source lifelines feed one memory orb, all live
def memory():
    cx,cy=210,210
    src=[("ICP",-90),("pipeline",-18),("pricing",54),("docs",126),("history",198)]
    lines=""; nodes=""
    for nm,ang in src:
        x=cx+152*math.cos(math.radians(ang)); y=cy+152*math.sin(math.radians(ang))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="32" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="mc" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="54" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">CORE</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("Memory is the layer","SHARED CORE")}
        <div style="font-family:'DM Sans';font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing, docs and history feed one memory. Every agent reads from it, so nothing repeats a question you already answered.</div>
        {cap("one core every agent reads from. cut it and the layer goes dark.")}</div></div>'''

# 5. GATE - full-capability orb held on the operator's reins, one lock (HUMAN GATE)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Full power, your reins","POWER, HELD")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="210" r="130" fill="url(#orb)"/></g>
        <text x="200" y="204" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">FULL</text>
        <text x="200" y="238" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <path d="M334 210 H610" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="140" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,178)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every external move parks for your tap. augmented, never loose.")}</div>'''

# 6. RADAR - live signal sweep + a first-to-see lead readout
def radar():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Stack",210,168),("Intent",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#rb)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">You + the layer</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">Tue 09:12</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">Your VC</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">Fri 16:40</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">3 days ahead</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="rsw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="rb" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#rsw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It saw the round first","SIGNAL LEAD")}
        {lead}
        {cap("funding, hiring, stack, intent - the layer watches while you sleep.")}
      </div></div>'''

# 7. ISO - isometric stack of scored, sourced account cards (the layer's output, not raw tokens)
def iso():
    cards=""
    rows=[("Northwind Robotics","hiring 3 ops roles","92"),
          ("Globex Systems","raised $4M in May","88"),
          ("Initech","no AI layer yet","81")]
    for i,(a,b,c) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:25px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 17px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{c}</span>
            <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">SCORE</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("Scored, sourced, ranked","THE OUTPUT")}
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:490px;position:relative">{cards}</div></div>
      {cap("model calls become scored, sourced, ready-to-act briefs.")}</div>'''

# 8. HUB - radial hub-and-spokes: the operating layer, one login (IVORY)
def hub():
    cx,cy=306,236
    spokes=[("THE ROUTER",-90),("SHARED MEMORY",-30),("AGENT ROSTER",30),("HUMAN GATE",90),("THE EYES",150),("YOUR VOICE",210)]
    lines=""; nodes=""
    for nm,ang in spokes:
        x=cx+184*math.cos(math.radians(ang)); y=cy+184*math.sin(math.radians(ang))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,86,45,.42)" stroke-width="2.6"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#fdfbf6" stroke="rgba(150,90,45,.30)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="none" stroke="rgba(255,255,255,.7)" stroke-width="1"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="12" fill="#5a4634">{nm.split(" ")[0]}</text>'
          f'<text x="{x:.0f}" y="{y+20:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8a745a">{nm.split(" ",1)[1] if " " in nm else ""}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 30px">
      {ivtitle("Own the operating layer","ONE SYSTEM")}
      <svg width="612" height="472" viewBox="0 0 612 472" style="display:block;margin:0 auto">
        <defs><radialGradient id="hb2" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hbg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}
        <g filter="url(#hbg)"><circle cx="{cx}" cy="{cy}" r="72" fill="url(#hb2)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ULTRON</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010" letter-spacing=".08em">the layer</text>
        {nodes}
      </svg>
      {cap("router, memory, agents and gate - one operating layer at cents.","#8a745a")}</div>'''

PANELS={"valuestack":valuestack(),"spend":spend(),"graph":graph(),"memory":memory(),
        "gate":gate(),"radar":radar(),"iso":iso(),"hub":hub()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2sequoiajusttold"; os.makedirs(outd,exist_ok=True)
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
