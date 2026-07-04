#!/usr/bin/env python3
# TIER 3 - THE DUCT TAPE, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded
# scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Angle: every rented tool is 80% right; you are the human glue in the 20% gaps. Ultron is one
# operator cut to your actual shape. (NOT a tool-count / one-vs-many comparison.)
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. MISFIT - bar-meter chart: each tool ~80% filled warm, top ~20% a hatched red GAP
def misfit():
    tools=[("Scheduling",82),("Invoices",78),("CRM",74),("Intake",80),("Email",76),("Tasks",71)]
    bars=""
    for nm,pct in tools:
        gap=100-pct
        bars+=(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:12px">'
          f'<div style="position:relative;width:78px;height:322px;border-radius:15px;overflow:hidden;background:#211e1a;border:1px solid rgba(255,255,255,.08)">'
          f'<div style="position:absolute;top:0;left:0;right:0;height:{gap}%;background:repeating-linear-gradient(135deg,rgba({RED},.92),rgba({RED},.92) 6px,rgba({RED},.5) 6px,rgba({RED},.5) 12px)"></div>'
          f'<div style="position:absolute;bottom:0;left:0;right:0;height:{pct}%;background:linear-gradient(180deg,#e6b48f,rgb({ACC}) 58%,#9a5a35)"></div>'
          f'<div style="position:absolute;bottom:12px;left:0;right:0;text-align:center;font-family:DM Sans;font-weight:900;font-size:23px;color:#1a0f0a">{pct}</div></div>'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.05em;color:#a8a296;text-align:center">{nm}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every tool is 80% right","THE MISFIT")}
      <div style="display:flex;gap:16px;align-items:flex-end;padding:8px 4px 0">{bars}</div>
      <div style="display:flex;align-items:center;gap:11px;margin-top:18px">
        <span style="width:17px;height:17px;border-radius:4px;background:repeating-linear-gradient(135deg,rgba({RED},.92),rgba({RED},.92) 4px,rgba({RED},.5) 4px,rgba({RED},.5) 8px);flex-shrink:0"></span>
        <span style="font-family:DM Mono;font-size:13px;color:#c8805f">the misfit gap you patch by hand</span></div>
      {cap("the last fifth never fits your workflow. that gap is where you live.")}</div>'''

# 2. GLUE - hub graph: 6 tool nodes, dashed red manual edges all routed THROUGH one YOU node
def glue():
    cx,cy,R=430,232,168
    tools=[("Scheduling",-90),("Invoices",-30),("CRM",30),("Tasks",90),("Email",150),("Intake",210)]
    edges=""; nodes=""
    for nm,a in tools:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        edges+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba({RED},.6)" stroke-width="2.4" stroke-dasharray="5 7"/>'
        nodes+=(f'<rect x="{x-66:.0f}" y="{y-24:.0f}" width="132" height="48" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">{nm}</text>')
    labels=[("csv export",300,116),("copy / paste",120,116),("re-type",210,110)]
    tape=""
    for t,a,d in labels:
        x=cx+d*math.cos(math.radians(a)); y=cy+d*math.sin(math.radians(a))
        tape+=f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#c8805f">{t}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You are the glue","MANUAL GLUE")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><filter id="yg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({RED})" flood-opacity="0.4"/></filter></defs>
        {edges}{tape}{nodes}
        <g filter="url(#yg)"><circle cx="{cx}" cy="{cy}" r="58" fill="#241f1a" stroke="rgb({RED})" stroke-width="2.5"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">YOU</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#c8805f">the API</text>
      </svg>
      {cap("exports, copy-paste, re-typing. you are the integration between them.")}</div>'''

# 3. SWIVEL - swimlane timeline: one task hops across six app lanes, 40 minutes bleed out
def swivel():
    lanes=["Scheduling","Invoices","CRM","Intake","Email","Tasks"]
    x0,x1=196,724; top=26; laneH=54
    rows=""
    for i,nm in enumerate(lanes):
        y=top+i*laneH
        rows+=(f'<text x="176" y="{y+laneH/2+5:.0f}" text-anchor="end" font-family="DM Mono" font-size="13" fill="#9a9488">{nm}</text>'
          f'<line x1="{x0}" y1="{y+laneH/2:.0f}" x2="{x1}" y2="{y+laneH/2:.0f}" stroke="rgba(255,255,255,.06)" stroke-dasharray="2 8"/>')
    hops=[0,2,4,1,5,3,4,2]
    pts=[(x0+(x1-x0)*i/(len(hops)-1), top+lane*laneH+laneH/2) for i,lane in enumerate(hops)]
    poly=" ".join(f"{x:.0f},{y:.0f}" for x,y in pts)
    dots="".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="rgb({ACC})" filter="url(#sg)"/>' for x,y in pts)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One task, six tabs","SWIVEL TAX")}
      <svg width="820" height="378" viewBox="0 0 820 378" style="display:block;margin:0 auto">
        <defs><filter id="sg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {rows}
        <polyline points="{poly}" fill="none" stroke="rgb({ACC})" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
        {dots}
        <g transform="translate(600,352)">
          <circle cx="0" cy="0" r="17" fill="none" stroke="rgb({RED})" stroke-width="2.6"/>
          <line x1="0" y1="0" x2="0" y2="-9" stroke="rgb({RED})" stroke-width="2.6" stroke-linecap="round"/>
          <line x1="0" y1="0" x2="7" y2="3" stroke="rgb({RED})" stroke-width="2.6" stroke-linecap="round"/>
          <text x="28" y="6" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">40 min lost</text>
        </g>
      </svg>
      {cap("forty minutes of tab-switching for a job worth four.")}</div>'''

# 4. BILL - IVORY ledger: the rented stack invoiced, seats you barely touch (competitor cost)
def bill():
    rows=[("CRM seats","$450",18),("Email marketing","$299",22),("Scheduling","$180",30),
          ("Intake forms","$99",12),("Task manager","$240",25),("Chat and misc","$740",15)]
    body=""
    for nm,cost,used in rows:
        body+=(f'<div style="display:flex;align-items:center;gap:18px;padding:13px 0;border-bottom:1px solid rgba(120,95,60,.16)">'
          f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:19px;color:#2a2016">{nm}</span>'
          f'<div style="width:120px;height:9px;border-radius:5px;background:rgba(120,95,60,.16);position:relative">'
          f'<div style="position:absolute;left:0;top:0;bottom:0;width:{used}%;background:#96562d;border-radius:5px"></div></div>'
          f'<span style="width:52px;text-align:right;font-family:DM Mono;font-size:13px;color:#8a745a">{used}%</span>'
          f'<span style="width:78px;text-align:right;font-family:DM Sans;font-weight:800;font-size:20px;color:#2a2016">{cost}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("Renting all of it","THE BILL")}
      <div style="display:flex;align-items:center;gap:18px;padding:0 0 8px">
        <span style="flex:1"></span>
        <span style="width:120px;font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#a08a68;text-align:center">SEAT USED</span>
        <span style="width:52px"></span>
        <span style="width:78px;text-align:right;font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#a08a68">PER MO</span></div>
      {body}
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-top:20px">
        <span style="font-family:DM Sans;font-weight:800;font-size:22px;color:#2a2016">Every month, again</span>
        <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#96562d">$2,008</span></div>
      {cap("two grand a month for seats. you touch a fifth of them.","#8a745a")}</div>'''

# 5. SHAPED - IVORY blueprint: your irregular workflow outline filled exactly by one warm operator;
# generic rented rectangles overhang the edges (they never fit)
def shaped():
    # your-workflow blob path (dashed ivory-accent), warm operator fills it, gray rented rects overhang
    blob="M170 150 C250 96,470 96,556 150 C640 200,646 300,586 356 C520 418,360 430,270 400 C176 368,120 300,132 236 C138 196,150 168,170 150 Z"
    rects=[(96,120,120,74,"rented"),(560,300,132,70,"rented"),(300,392,118,64,"rented")]
    ghost=""
    for x,y,w,h,t in rects:
        ghost+=(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="rgba(120,95,60,.10)" stroke="rgba({RED},.75)" stroke-width="2" stroke-dasharray="6 6"/>'
          f'<text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#b0562f">{t}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("One operator, your shape","SHAPED TO YOU")}
      <svg width="760" height="470" viewBox="0 0 760 470" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="op" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
          <filter id="og5" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="rgba(150,90,45,.35)"/></filter>
        </defs>
        {ghost}
        <g filter="url(#og5)"><path d="{blob}" fill="url(#op)"/></g>
        <path d="{blob}" fill="none" stroke="#96562d" stroke-width="2.4" stroke-dasharray="8 7"/>
        <text x="358" y="262" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">FITS</text>
        <text x="358" y="296" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#3a2010">your workflow</text>
        <text x="600" y="130" font-family="DM Mono" font-size="12" fill="#a08a68">your outline</text>
      </svg>
      {cap("not a tool you bend into. a system cut to your shape.","#8a745a")}</div>'''

# 6. ROUTER - clean fan: one request routes to the right agent + model tier (7 Ultron agents)
def router():
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    lit=1
    hubx,huby=214,232; ax=470
    y0,dy=54,58
    edges=""; chips=""
    for i,(nm,role) in enumerate(agents):
        y=y0+i*dy; on=(i==lit)
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.2
        edges+=f'<path d="M{hubx+62} {huby} C340 {huby},350 {y},{ax-8} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        glow="filter:drop-shadow(0 0 20px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:11px;color:rgb({ACC})">picked</span>' if on else ''
        chips+=(f'<div style="position:absolute;left:256px;top:{y-24}px;width:246px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:13px;padding:9px 15px;display:flex;align-items:baseline;justify-content:space-between">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:17px;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:13px;color:#8f8f85;margin-left:10px;flex:1">{role}</span>{pick}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One request, right hands","THE ROUTER")}
      <div style="position:relative;height:470px">
        <svg width="510" height="470" viewBox="0 0 510 470" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="rh" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="8" y="{huby-30}" width="96" height="60" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <text x="56" y="{huby-4}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#c9c3b8">draft the</text>
          <text x="56" y="{huby+14}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#c9c3b8">follow-up</text>
          <g filter="url(#rg)"><circle cx="{hubx}" cy="{huby}" r="60" fill="url(#rh)"/></g>
          <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{huby+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">reads the job</text>
        </svg>
        {chips}
      </div>
      {cap("you ask once. it picks the agent and the model tier for you.")}</div>'''

# 7. MEMORY - split/compare: siloed locked tool-boxes (left) vs one shared core feeding agents (right)
def memory():
    silos=[("Scheduling",0),("CRM",1),("Email",2),("Tasks",3)]
    left=""
    for nm,i in silos:
        y=52+i*98
        left+=(f'<div style="position:absolute;left:0;top:{y}px;width:250px;background:#221f1b;border:1.5px solid rgba({RED},.4);border-radius:14px;padding:14px 16px;display:flex;align-items:center;gap:12px">'
          f'<svg width="20" height="20" viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2.5" fill="none" stroke="rgb({RED})" stroke-width="2.2"/><path d="M8 10 V7 a4 4 0 0 1 8 0 v3" fill="none" stroke="rgb({RED})" stroke-width="2.2"/></svg>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:16px;color:#c9c3b8">{nm}</div>'
          f'<div style="font-family:DM Mono;font-size:11px;color:#b0562f">data locked in</div></div></div>')
    agents=["CORTEX","SPECTER","STRIKER","PULSE"]
    lines=""; nodes=""
    ccx,ccy=250,215
    for i,nm in enumerate(agents):
        a=-60+i*40; x=ccx+150*math.cos(math.radians(a)); y=ccy+150*math.sin(math.radians(a))
        lines+=f'<line x1="{ccx}" y1="{ccy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="2.4"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One memory, not twelve silos","SHARED CORE")}
      <div style="display:flex;align-items:stretch;gap:20px">
        <div style="position:relative;width:250px;height:434px">{left}</div>
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:#8f8f85;transform:rotate(-90deg);white-space:nowrap">SILOED &nbsp; VS &nbsp; SHARED</div>
          <div style="width:1px;height:120px;background:rgba(255,255,255,.12);margin:14px 0"></div>
        </div>
        <div style="flex:1;position:relative">
          <svg width="500" height="434" viewBox="0 0 500 434">
            <defs><radialGradient id="mc" cx="46%" cy="40%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
            <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
            {lines}<g filter="url(#mg)"><circle cx="{ccx}" cy="{ccy}" r="54" fill="url(#mc)"/></g>
            <text x="{ccx}" y="{ccy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">CORE</text>
            <text x="{ccx}" y="{ccy+16}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">icp · pricing</text>
            {nodes}
          </svg>
        </div>
      </div>
      {cap("icp, pricing, pipeline in one core. nothing asks you twice.")}</div>'''

# 8. GATE - approval queue butts a lock-orb hero: it does the glue work, you tap to send
def gate():
    q=[("Send 12 follow-ups","SPECTER"),("Post today's update","PULSE"),("Ship the pricing fix","SENTINEL")]
    cards=""
    for i,(t,ag) in enumerate(q):
        y=i*100
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:398px;background:linear-gradient(160deg,#33302b,#211e1a);border:1.5px solid rgba(255,255,255,.12);border-radius:16px;padding:15px 18px;display:flex;align-items:center;gap:14px;box-shadow:0 20px 34px rgba(0,0,0,.45)">'
          f'<span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.7);flex-shrink:0"></span>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{t}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:#8f8f85">{ag} · ready</div></div>'
          f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:rgb({ACC})">HELD</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Your workflow. Your tap.","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:36px">
        <div style="position:relative;width:398px;height:300px">{cards}</div>
        <svg width="340" height="360" viewBox="0 0 340 360">
          <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="ogx" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          <path d="M6 180 H78" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 11" stroke-linecap="round"/>
          <g filter="url(#ogx)"><circle cx="180" cy="180" r="118" fill="url(#orb)"/></g>
          <g transform="translate(146,138)"><rect x="0" y="34" width="68" height="50" rx="11" fill="none" stroke="#2a160c" stroke-width="6"/><path d="M13 34 V21 a21 21 0 0 1 42 0 v13" fill="none" stroke="#2a160c" stroke-width="6"/></g>
          <text x="180" y="256" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">YOUR TAP</text>
        </svg>
      </div>
      {cap("it does the glue work. you still approve every send.")}</div>'''

PANELS={"misfit":misfit(),"glue":glue(),"swivel":swivel(),"bill":bill(),
        "shaped":shaped(),"router":router(),"memory":memory(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src64"; os.makedirs(outd,exist_ok=True)
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
