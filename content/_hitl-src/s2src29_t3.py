#!/usr/bin/env python3
# TIER 3 - SIXTEEN TABS OR ONE SYSTEM, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagcol=None):
    tc=tagcol or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. STACK - the 16-tool pile (grey chips, 4 broken red) collapsing into one lit ULTRON orb
def stack():
    pool=["MCP","REPO","TOOL","API","PLUGIN","WRAPPER","SCRIPT","BOT","MCP","REPO","TOOL","API","PLUGIN","WRAPPER","SCRIPT","BOT"]
    broken={2,6,9,13}
    chips=""
    for i,tag in enumerate(pool):
        bad=i in broken
        bd="rgba(200,70,35,.55)" if bad else "rgba(255,255,255,.09)"
        col="rgb(200,70,35)" if bad else "#8f8f85"
        dash="border-style:dashed;" if bad else ""
        dot="rgba(200,70,35,.5)" if bad else "rgba(250,250,247,.12)"
        chips+=(f'<div style="width:66px;height:54px;border:1.5px solid {bd};{dash}border-radius:12px;'
          f'background:#221f1b;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px">'
          f'<div style="width:15px;height:15px;border-radius:5px;background:{dot}"></div>'
          f'<span style="font-family:\'DM Mono\';font-size:9px;letter-spacing:.05em;color:{col}">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Sixteen tabs, still no system","STACK VS SYSTEM")}
      <div style="display:flex;align-items:center;gap:22px;margin-top:8px">
        <div style="flex-shrink:0;width:314px">
          <div style="display:flex;flex-wrap:wrap;gap:9px;width:314px">{chips}</div>
          <div style="font-family:'DM Mono';font-size:12px;color:rgb(200,70,35);margin-top:15px;letter-spacing:.05em">4 broken &middot; 0 talk to each other</div>
        </div>
        <svg width="72" height="60" viewBox="0 0 72 60"><path d="M6 30 H56 M44 16 L60 30 L44 44" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex:1;text-align:center">
          <svg width="240" height="240" viewBox="0 0 240 240" style="display:block;margin:0 auto">
            <defs><radialGradient id="s_orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
            <filter id="s_g" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
            <g filter="url(#s_g)"><circle cx="120" cy="120" r="86" fill="url(#s_orb)"/></g>
            <text x="120" y="114" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">ONE</text>
            <text x="120" y="150" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">SYSTEM</text>
          </svg>
          <div style="font-family:'DM Mono';font-size:12.5px;color:rgb({ACC});margin-top:6px;letter-spacing:.08em">wired, not bolted on</div>
        </div>
      </div>
      {cap("mcp servers, repos, wrappers - sixteen logins that never talk.")}</div>'''

# 2. AGENTS - radial hub-and-spokes: ROUTER core, 7 named agent chips around it
def agents():
    ag=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    cx,cy,R=410,232,196; n=len(ag); spokes="";nodes=""
    for i,(nm,role) in enumerate(ag):
        a=math.radians(-90+i*360/n)
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
        w,h=130,56
        nodes+=(f'<rect x="{x-w/2:.0f}" y="{y-h/2:.0f}" width="{w}" height="{h}" rx="15" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x:.0f}" y="{y-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven specialists, one roster","THE AGENTS")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="a_hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="a_g" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spokes}
        <g filter="url(#a_g)"><circle cx="{cx}" cy="{cy}" r="64" fill="url(#a_hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one roster</text>
        {nodes}
      </svg>
      {cap("research, outbound, deals, content, code, publishing, legal - each owns its job.")}</div>'''

# 3. ROUTER - one job token routed to 3 tier lanes (cents), SMART lit/picked
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",232,True),("DEEP","hard judgement","0.40c",368,False)]
    hy=232; edges="";cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.5
        edges+=f'<path d="M290 {hy} C370 {hy},390 {y},452 {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 20px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else '<span style="font-family:DM Mono;font-size:12px;color:#6f6a60">idle</span>'
        cards+=(f'<div style="position:absolute;left:452px;top:{y-42}px;width:196px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:15px 18px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One brain picks the tier","MODEL ROUTER")}
      <div style="position:relative;height:464px">
        <svg width="820" height="464" viewBox="0 0 820 464" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="r_hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="r_g" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
          {edges}
          <rect x="8" y="{hy-30}" width="150" height="60" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <text x="83" y="{hy-4}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">draft 12</text>
          <text x="83" y="{hy+14}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">follow-ups</text>
          <line x1="158" y1="{hy}" x2="172" y2="{hy}" stroke="rgba(212,162,127,.4)" stroke-width="3"/>
          <g filter="url(#r_g)"><circle cx="230" cy="{hy}" r="60" fill="url(#r_hub)"/></g>
          <text x="230" y="{hy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="230" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        {cards}
      </div>
      {cap("one job in, the cheapest tier that can do it - cents, not dollars.")}</div>'''

# 4. CENTS - IVORY bill: the 16-tool stack in dollars (red bar) vs Ultron in cents (tiny bar)
def cents():
    def bar(label,sub,val,valcol,pct,barcol,track):
        return (f'<div style="margin-bottom:26px">'
          f'<div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:10px">'
          f'<div><div style="font-family:\'DM Sans\';font-weight:800;font-size:21px;color:#2a2016">{label}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#8a745a;margin-top:2px">{sub}</div></div>'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:40px;color:{valcol};line-height:1">{val}</div></div>'
          f'<div style="height:28px;border-radius:9px;background:{track};overflow:hidden">'
          f'<div style="width:{pct}%;height:100%;background:{barcol};border-radius:9px"></div></div></div>')
    comp=bar("The 16-tool stack","seats and subscriptions, every month","$400+/mo","rgb(200,70,35)",100,"linear-gradient(90deg,#c84623,#a83a1e)","rgba(200,70,35,.13)")
    ult=bar("Ultron","cents per task, per token","cents","#96562d",5,"#96562d","rgba(150,90,45,.13)")
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Their dollars, our cents","THE BILL","#2a2016","#96562d")}
      <div style="margin-top:14px">{comp}{ult}</div>
      {cap("the pile runs a monthly invoice. ultron charges cents for the work done.","#8a745a")}</div>'''

# 5. GATE - a queue of held actions butting into a lock, released only by your tap
def gate():
    acts=[("SEND","cold email &middot; 40 leads"),("MOVE","advance &middot; 3 deals"),("SHIP","deploy &middot; pricing page")]
    chips=""
    for nm,sub in acts:
        chips+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:15px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07);margin-bottom:14px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(212,162,127,.13);border:1px solid rgba(212,162,127,.32);display:flex;align-items:center;justify-content:center;font-family:\'DM Mono\';font-size:12px;letter-spacing:.04em;color:rgb({ACC})">{nm[:2]}</div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.1em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:600;font-size:17px;color:#eae4d8;margin-top:1px">{sub}</div></div>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:#d6a06a;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.3);border-radius:999px;padding:5px 12px">HELD</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:26px;margin-top:6px">
        <div style="flex:1">{chips}
          <div style="font-family:'DM Mono';font-size:12.5px;color:#8f8f85;margin-top:2px;letter-spacing:.04em">3 actions waiting, none sent</div></div>
        <svg width="58" height="58" viewBox="0 0 58 58" style="flex-shrink:0"><path d="M8 29 H46 M35 17 L50 29 L35 41" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex-shrink:0;width:206px;text-align:center">
          <div style="width:150px;height:150px;margin:0 auto;border-radius:34px;background:linear-gradient(160deg,#2b2824,#1c1a17);border:2px solid rgb({ACC});display:flex;align-items:center;justify-content:center;box-shadow:0 0 30px rgba(212,162,127,.25)">
            <svg width="72" height="72" viewBox="0 0 72 72"><rect x="16" y="32" width="40" height="30" rx="7" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M24 32 V22 a12 12 0 0 1 24 0 v10" fill="none" stroke="rgb({ACC})" stroke-width="5"/></svg>
          </div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:22px;color:#FAFAF7;margin-top:16px">Your tap</div>
          <div style="font-family:'DM Mono';font-size:12px;color:rgb({ACC});margin-top:4px;letter-spacing:.08em">approve to send</div>
        </div>
      </div>
      {cap("every email, deal move and deploy parks until you approve it.")}</div>'''

# 6. MEMORY - IVORY shared-core vault: one memory cylinder every agent reads from
def memory():
    data=["ICP","PIPELINE","PRICING","DOCS"]
    rows=""
    for i,d in enumerate(data):
        yy=152+i*50
        rows+=(f'<rect x="70" y="{yy}" width="220" height="38" rx="9" fill="rgba(255,255,255,.6)" stroke="rgba(150,90,45,.22)"/>'
          f'<circle cx="92" cy="{yy+19}" r="5" fill="#96562d"/>'
          f'<text x="110" y="{yy+25}" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="#4a3f30">{d}</text>')
    ag=[("CORTEX",120),("SPECTER",210),("PULSE",300),("SENTINEL",390)]
    conns="";nodes=""
    for nm,yy in ag:
        conns+=f'<path d="M300 232 C400 232,430 {yy},560 {yy}" fill="none" stroke="rgba(150,90,45,.4)" stroke-width="2"/>'
        nodes+=(f'<rect x="560" y="{yy-22}" width="150" height="44" rx="13" fill="rgba(255,255,255,.62)" stroke="rgba(150,90,45,.2)"/>'
          f'<text x="635" y="{yy+5}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#2a2016">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("One core every agent reads","SHARED MEMORY","#2a2016","#96562d")}
      <svg width="740" height="440" viewBox="0 0 740 440" style="display:block;margin:0 auto">
        <defs><linearGradient id="m_cyl" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#f3ead9"/><stop offset="50%" stop-color="#fdfbf6"/><stop offset="100%" stop-color="#e6dac4"/></linearGradient></defs>
        {conns}
        <rect x="50" y="108" width="260" height="248" fill="url(#m_cyl)"/>
        <line x1="50" y1="108" x2="50" y2="356" stroke="rgba(150,90,45,.25)"/><line x1="310" y1="108" x2="310" y2="356" stroke="rgba(150,90,45,.25)"/>
        <ellipse cx="180" cy="356" rx="130" ry="30" fill="#e6dac4" stroke="rgba(150,90,45,.25)"/>
        {rows}
        <ellipse cx="180" cy="108" rx="130" ry="30" fill="url(#m_cyl)" stroke="rgba(150,90,45,.3)"/>
        <text x="180" y="114" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".2em" fill="#96562d">MEMORY</text>
        {nodes}
      </svg>
      {cap("icp, pipeline, pricing, docs - every agent draws from the same memory.","#8a745a")}</div>'''

# 7. SYSTEMS - isometric saved-system pipeline: chained steps that rerun forever
def systems():
    steps=[("TRIGGER","a new lead lands"),("CORTEX","profiles the account"),("SPECTER","drafts the sequence"),("GATE","waits for your tap")]
    cards=""
    for i,(nm,sub) in enumerate(steps):
        y=i*104
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);'
          f'border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 22px;'
          f'box-shadow:0 28px 42px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:34px;height:34px;border-radius:10px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);'
          f'display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:16px;color:rgb({ACC})">{i+1}</div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Save the system, not the prompt","RUN ONCE, RERUN")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(19deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:398px;display:flex;align-items:center;gap:9px;background:rgb({ACC});color:#1a0f0a;font-family:'DM Sans';font-weight:900;font-size:15px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>SAVED &middot; RERUNS FOREVER</div></div></div>
      {cap("a sequence you run once and rerun forever - steps chained, not pasted.")}</div>'''

# 8. OPERATOR - scattered tool nodes converge into one login orb
def operator():
    scat=[("tool",70,86),("mcp",70,196),("repo",70,306),("api",188,140),("script",188,252)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+30} {y} C360 {y},400 214,548 214" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.7"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Close the tabs, open one","ONE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="o_bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="o_g" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#o_g)"><circle cx="600" cy="214" r="122" fill="url(#o_bod)"/></g>
        <text x="600" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">ONE</text>
        <text x="600" y="236" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">LOGIN</text>
        <text x="600" y="372" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">routed &middot; gated &middot; remembered</text>
      </svg>
      {cap("one chat routes to every agent, holds the memory, waits at the gate.")}</div>'''

PANELS={"stack":stack(),"agents":agents(),"router":router(),"cents":cents(),
        "gate":gate(),"memory":memory(),"systems":systems(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src29"; os.makedirs(outd,exist_ok=True)
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
