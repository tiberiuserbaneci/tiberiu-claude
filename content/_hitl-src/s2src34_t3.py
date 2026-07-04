#!/usr/bin/env python3
# TIER 3 - THE DORMANT ROSTER, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded
# scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips, no cuts,
# no extruded walls. Warm palette only (accent 212,162,127; muted red 200,70,35 for a bad state).
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

# 1. ROUTER - one job token routed down 3 tier lanes, SMART lane lit/picked, cents on each lane
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

# 2. CORTEX - IVORY ranked leaderboard of scored accounts (research that already ran)
def cortex():
    rows=[("Northwind Robotics","raised $4M in May","94"),
          ("Globex Systems","hiring 3 ops roles","91"),
          ("Initech","no AI layer yet","87"),
          ("Umbra Labs","renewed two rival tools","83")]
    body=""
    for i,(a,b,c) in enumerate(rows):
        body+=(f'<div style="display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.55);'
          f'border:1px solid rgba(120,95,60,.14);border-radius:16px;padding:15px 20px;box-shadow:inset 0 2px 3px rgba(255,255,255,.85)">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#c98a55;width:32px;flex-shrink:0">{i+1}</span>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:21px;color:#2a2016">{a}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8a745a;margin-top:2px">{b}</div></div>'
          f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:#96562d;border-radius:12px;padding:8px 16px">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:24px;color:#fdfbf6;line-height:1">{c}</span>'
          f'<span style="font-family:DM Mono;font-size:9.5px;letter-spacing:.1em;color:rgba(253,251,246,.75)">FIT</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Research that already ran","CORTEX · RANKED","#2a2016","#96562d")}
      <div style="display:flex;flex-direction:column;gap:13px">{body}</div>
      {cap("profiled overnight, ranked by fit - for cents, not a research hire.","#8a745a")}</div>'''

# 3. SPECTER - vertical sequence timeline, day nodes down a spine, last one a booked reply
def specter():
    steps=[("DAY 0","Opener sent","one specific trigger",False),
           ("DAY 2","Follow-up","reframed as a question",False),
           ("DAY 5","Nudge","social proof, 41 words",False),
           ("DAY 9","Reply","booked a call",True)]
    rows=""
    n=len(steps)
    for i,(lab,t,sub,hit) in enumerate(steps):
        col=f"rgb({ACC})" if hit else "rgba(212,162,127,.42)"
        cardbd=f"rgb({ACC})" if hit else "rgba(255,255,255,.09)"
        cardbg="linear-gradient(160deg,#403a33,#241f1a)" if hit else "linear-gradient(160deg,#2b2825,#201d1a)"
        spine='<span style="flex:1;width:2px;background:rgba(212,162,127,.22)"></span>' if i<n-1 else ''
        right=(f'<span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:rgb({ACC})">replied</span>' if hit
               else f'<span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:#7a7468">{lab}</span>')
        rows+=(f'<div style="display:flex;align-items:stretch;gap:20px">'
          f'<div style="flex-shrink:0;width:20px;display:flex;flex-direction:column;align-items:center">'
          f'<span style="width:18px;height:18px;border-radius:50%;background:{col};box-shadow:0 0 12px {col}"></span>{spine}</div>'
          f'<div style="flex:1;margin-bottom:14px;background:{cardbg};border:1.5px solid {cardbd};border-radius:16px;padding:15px 18px">'
          f'<div style="display:flex;align-items:baseline"><span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{t}</span>{right}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#9a9488;margin-top:3px">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 42px 30px">
      {htitle("The outbound seat, filled","SPECTER · SEQUENCE")}
      <div style="display:flex;flex-direction:column">{rows}</div>
      {cap("opener, follow-ups and the whole chase - drafted in your voice.")}</div>'''

# 4. STRIKER - stacked stage stepper (all cleared) + a close-probability gauge ring
def striker():
    stages=[("Qualify","budget and authority confirmed"),
            ("Discovery","three pains mapped"),
            ("Objections","two handled, none open"),
            ("Close","plan sent, awaiting sign")]
    items=""
    for nm,sub in stages:
        items+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(160deg,#2f2b27,#221f1b);'
          f'border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:13px 18px;box-shadow:inset 0 1.5px 2px rgba(255,255,255,.06)">'
          f'<span style="flex-shrink:0;width:34px;height:34px;border-radius:50%;background:rgba(212,162,127,.16);'
          f'border:1px solid rgba(212,162,127,.4);display:flex;align-items:center;justify-content:center">'
          f'<svg width="18" height="18" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85">{sub}</div></div></div>')
    pct=78; r=70; circ=2*math.pi*r; dash=circ*pct/100
    gauge=(f'<div style="flex-shrink:0;position:relative;width:196px;height:196px;display:flex;align-items:center;justify-content:center">'
      f'<svg width="184" height="184" viewBox="0 0 184 184"><circle cx="92" cy="92" r="{r}" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="16"/>'
      f'<circle cx="92" cy="92" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 92 92)"/></svg>'
      f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">'
      f'<span style="font-family:DM Sans;font-weight:900;font-size:46px;color:#FAFAF7">{pct}%</span>'
      f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:rgb({ACC})">TO CLOSE</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 42px 34px">
      {htitle("Every deal knows its move","STRIKER · CLOSE PLAN")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex:1;display:flex;flex-direction:column;gap:12px">{items}</div>
        {gauge}</div>
      {cap("qualifies, handles objections and builds the close plan, per deal.")}</div>'''

# 5. MEMORY - radial shared-memory core, six agent seats drawing lifelines from one glowing heart
def memory():
    cx,cy=210,210
    seats=[("CORTEX",-90),("SPECTER",-30),("STRIKER",30),("PULSE",90),("GATE",150),("ROUTER",210)]
    lines="";nodes=""
    for nm,a in seats:
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="2.6"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="33" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="hb" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}{nodes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#2a160c">MEMORY</text></svg>
      <div style="flex:1">
        {htitle("One memory, every seat","SHARED CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing and docs live once. Every agent reads the same core, so you never retype context into a fresh chat.</div>
        {cap("stop briefing a blank box - the roster already knows you.")}</div></div>'''

# 6. PULSE - IVORY voice-match dial + a sample line written in your voice
def pulse():
    pct=98; r=74; circ=2*math.pi*r; dash=circ*pct/100
    checks=["short lines","no hedging","your cadence"]
    chk="".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in checks)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("It writes in your voice","PULSE · VOICE MATCH","#2a2016","#96562d")}
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:190px;height:190px">
          <svg width="190" height="190" viewBox="0 0 190 190">
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 95 95)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016">{pct}%</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">style match</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:DM Sans;font-size:20px;color:#2a2016;line-height:1.4">
            "I killed nine tools last month. The one I kept did not have a chat box."</div>
          <div style="display:flex;gap:22px;margin-top:16px">{chk}</div></div>
      </div>
      {cap("sampled from your real posts, banned words enforced on every draft.","#8a745a")}</div>'''

# 7. GATE - full-capability orb held on the operator's leash, one lock (power, held)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Full power. Your tap.","POWER, HELD")}
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
      {cap("every external move parks for your approval before it ever sends.")}</div>'''

# 8. OPERATOR - the full roster board: 9 seats (7 agents + router + gate) all woken by one login
def operator():
    seats=[("ROUTER","picks the tier"),("CORTEX","research"),("SPECTER","outbound"),
           ("STRIKER","deals"),("PULSE","content"),("SENTINEL","code"),
           ("AMPLIFY","publishing"),("COUNSEL","legal"),("GATE","your tap")]
    tiles=""
    for nm,role in seats:
        tiles+=(f'<div style="background:linear-gradient(160deg,#3a342d,#241f1a);border:1px solid rgba(212,162,127,.3);'
          f'border-radius:16px;padding:16px 16px;box-shadow:0 10px 22px rgba(0,0,0,.4), inset 0 2px 2px rgba(255,255,255,.08), 0 0 26px rgba(212,162,127,.08)">'
          f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:6px">'
          f'<span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 10px rgb({ACC})"></span>'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:17px;color:#FAFAF7">{nm}</span></div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#9a9488">{role}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 42px 34px">
      {htitle("Fill the whole roster","9 / 9 ACTIVE")}
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{tiles}</div>
      {cap("one login wakes seven agents, the router and the gate, all at once.")}</div>'''

PANELS={"router":router(),"cortex":cortex(),"specter":specter(),"striker":striker(),
        "memory":memory(),"pulse":pulse(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src34"; os.makedirs(outd,exist_ok=True)
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
