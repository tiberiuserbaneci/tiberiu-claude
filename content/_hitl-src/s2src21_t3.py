#!/usr/bin/env python3
# TIER 3 - KILL THE STACK (one Ultron system vs a duct-taped n8n+VAPI+10-API sales stack).
# Each panel a UNIQUE hand-built coded scene filling a clean rounded card, htitle + one cap,
# no chip strips / no cuts / no side-walls. Warm palette. Ultron cost = cents; high $ = competitor.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
BAD="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. STACK - the duct-taped competitor mess: a tangled bezier web of ten tool nodes into a fragile
# central junction, red dashed BREAKs on crossing wires, and a high $3,500/mo tag (competitor cost).
def stack():
    W,H=820,470
    hub=(410,235)
    tools=[("n8n",70,70),("VAPI",70,235),("OpenAI",70,400),
           ("Apollo",750,70),("Clearbit",750,175),("Hunter",750,300),
           ("HubSpot",290,430),("Cal.com",290,70),("Sheets",530,70),("Slack",510,430)]
    wires=""; nodes=""
    breaks=[0,3,6]
    for i,(nm,x,y) in enumerate(tools):
        mx=(x+hub[0])/2
        col=f"rgba({BAD},.6)" if i in breaks else "rgba(212,162,127,.35)"
        dash='stroke-dasharray="3 9"' if i in breaks else ""
        wires+=f'<path d="M{x} {y} C{mx:.0f} {y},{mx:.0f} {hub[1]},{hub[0]} {hub[1]}" fill="none" stroke="{col}" stroke-width="2.4" {dash}/>'
        if i in breaks:
            bx=(x+hub[0])/2; by=(y+hub[1])/2
            wires+=f'<g transform="translate({bx:.0f},{by:.0f}) rotate(45)"><line x1="-8" y1="0" x2="8" y2="0" stroke="rgb({BAD})" stroke-width="3"/><line x1="0" y1="-8" x2="0" y2="8" stroke="rgb({BAD})" stroke-width="3"/></g>'
        nodes+=(f'<rect x="{x-52}" y="{y-22}" width="104" height="44" rx="12" fill="#262320" stroke="rgba(255,255,255,.10)"/>'
                f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#c4beb2">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten tools, glued by hand","BRITTLE STACK")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="jnk" cx="40%" cy="32%"><stop offset="0%" stop-color="#5a4a3a"/><stop offset="100%" stop-color="#231f1b"/></radialGradient></defs>
        {wires}
        <circle cx="{hub[0]}" cy="{hub[1]}" r="66" fill="url(#jnk)" stroke="rgba({BAD},.7)" stroke-width="2.5"/>
        <text x="{hub[0]}" y="{hub[1]-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#e6ddd0">GLUE</text>
        <text x="{hub[0]}" y="{hub[1]+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({BAD})">3 broken</text>
        {nodes}
        <g transform="translate(596,392)"><rect x="0" y="0" width="196" height="60" rx="14" fill="rgba({BAD},.12)" stroke="rgba({BAD},.5)"/>
          <text x="98" y="27" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="rgb({BAD})">$3,500/mo</text>
          <text x="98" y="48" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a88f80">to keep it alive</text></g>
      </svg>
      {cap("one API change and the whole taped-together stack goes dark.")}</div>'''

# 2. ROUTER - one job token routed down 3 tier lanes, SMART lit/picked, cents pricing
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
      {htitle("A brain that budgets itself","MODEL ROUTER")}
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

# 3. CORTEX - IVORY research brief (paper): headline claim + a packed stack of sourced receipt chips
def cortex():
    receipts=[("crunchbase.com","raised $4M seed","2026-05-14"),
              ("linkedin.com","3 ops roles open","2026-05-19"),
              ("builtwith.com","no AI layer yet","2026-05-21")]
    chips=""
    for dom,note,date in receipts:
        fav=dom[0].upper()
        chips+=f'''<div style="display:flex;align-items:center;gap:15px;background:rgba(255,255,255,.55);
          border:1px solid rgba(120,95,60,.18);border-radius:15px;padding:13px 17px;box-shadow:0 8px 18px rgba(120,95,60,.12)">
          <div style="flex-shrink:0;width:38px;height:38px;border-radius:11px;background:linear-gradient(160deg,#f3e9d8,#e2d3ba);
            display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:19px;color:#96562d;border:1px solid rgba(120,95,60,.2)">{fav}</div>
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:19px;color:#2a2016">{note}</div>
          <div style="font-family:'DM Mono';font-size:13px;color:#8a745a;margin-top:1px">{dom} &middot; {date}</div></div>
          <svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(150,90,45,.12)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>'''
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">One sourced brief per lead</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">CORTEX &middot; 1 PAGE</span></div>
      <div style="background:rgba(255,255,255,.4);border-left:4px solid #96562d;border-radius:12px;padding:16px 20px;margin-bottom:18px">
        <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.16em;color:#96562d">NORTHWIND ROBOTICS</div>
        <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#2a2016;line-height:1.1;margin-top:3px">Warm. Buys now. <span style="color:#96562d">Score 92.</span></div></div>
      <div style="display:flex;flex-direction:column;gap:11px">{chips}</div>
      {cap("the ten-node enrichment chain, replaced by one page you can read.","#8a745a")}</div>'''

# 4. SPECTER - IVORY voice-match ring + a cold-email line written in your cadence
def specter():
    pct=97; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Cold email in your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">SPECTER</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:190px;height:190px">
          <svg width="190" height="190" viewBox="0 0 190 190">
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 95 95)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016">{pct}%</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">voice match</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4">
            "Saw you opened 3 ops roles. Booking those is the pain, not the posting. Worth 12 minutes?"</div>
          <div style="display:flex;gap:22px;margin-top:16px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["short lines","no hedging","one ask"])}
          </div></div>
      </div>
      {cap("sampled from your real posts - no VAPI script, no generic OpenAI draft.","#8a745a")}</div>'''

# 5. STRIKER - isometric qualify -> objection -> book pipeline ending in a held calendar slot
def striker():
    steps=[("QUALIFY","budget + timing checked",0),("OBJECTION","handled 2 of 2",1),("BOOK","calendar hold set",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Qualified, then booked","WHILE YOU SLEPT")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:110px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Thu 15:00 &#10003; held for your tap</div></div></div>
      {cap("discovery, objections and the calendar - one agent, not VAPI plus Cal.com.")}</div>'''

# 6. MEMORY - radial shared core, 7 agent spokes drawing from one memory, one severed = dead
def memory():
    cx,cy=210,210
    agents=[("CORTEX",-90),("SPECTER",-38),("STRIKER",14),("PULSE",66),("SENTINEL",130),("AMPLIFY",180),("COUNSEL",232)]
    lines=""; nodes=""
    for i,(nm,a) in enumerate(agents):
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a)); cut=(i==5)
        col=f"rgb({BAD})" if cut else "rgba(212,162,127,.5)"; dash='stroke-dasharray="4 8"' if cut else ""
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="3" {dash}/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="{f"rgba({BAD},.6)" if cut else "rgba(255,255,255,.14)"}" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="{"#6f6a60" if cut else "#cfc9bd"}">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="hb" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="54" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#2a160c">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">one core</text></svg>
      <div style="flex:1">
        {htitle("Ten tools forget you","SHARED CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing, docs - every agent draws from one memory. A glued stack of tools has none.</div>
        {cap("cut the core and the body goes dark. keep it and nothing forgets.")}</div></div>'''

# 7. GATE - full-capability orb held on the operator's reins, one lock (HUMAN GATE)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Full power. My reins.","HUMAN GATE")}
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
      {cap("every send and every call parks for your tap. augmented, never unsupervised.")}</div>'''

# 8. OPERATOR - scattered agent nodes converge into one glowing assembled system (one login)
def operator():
    scat=[("CORTEX",70,80),("SPECTER",70,180),("STRIKER",70,280),("PULSE",70,380),("SENTINEL",190,130),("COUNSEL",190,330)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+34} {y} C340 {y},360 210,520 210" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.75"/>'
          f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#9a9488">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one login","ONE SYSTEM")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="590" cy="210" r="120" fill="url(#bod)"/></g>
        <text x="590" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="590" y="230" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">SYSTEM</text>
        <text x="590" y="366" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">composed &middot; gated &middot; cents</text>
      </svg>
      {cap("no n8n, no VAPI, no ten dashboards - one system, cents to run.")}</div>'''

PANELS={"stack":stack(),"router":router(),"cortex":cortex(),"specter":specter(),
        "striker":striker(),"memory":memory(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src21"; os.makedirs(outd,exist_ok=True)
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
