#!/usr/bin/env python3
# TIER 3 - THE COMPLETE AI BODY, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
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

# 1. DIFFERENCE - clean radial: one lit MOUTH bay in the centre, 4 empty organ sockets around it
def difference():
    cx,cy=306,215; Rr=150
    sockets=[("BRAIN",-90),("EYES",0),("HEART",90),("HANDS",180)]
    ring=""
    for nm,a in sockets:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        ly=y+52 if a!=90 else y+52
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(250,250,247,.10)" stroke-width="1.5" stroke-dasharray="3 7"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="rgba(250,250,247,.02)" stroke="rgba(250,250,247,.16)" stroke-width="2" stroke-dasharray="5 6"/>'
          f'<line x1="{x-13:.0f}" y1="{y-13:.0f}" x2="{x+13:.0f}" y2="{y+13:.0f}" stroke="rgba(200,70,35,.55)" stroke-width="2.4"/>'
          f'<text x="{x:.0f}" y="{ly:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="#7a746a">{nm} · MISSING</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You rented a mouth","1 OF 5 ORGANS")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="lit" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="glow" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        {ring}
        <circle cx="{cx}" cy="{cy}" r="48" fill="url(#lit)" filter="url(#glow)"/>
        <text x="{cx}" y="{cy+80}" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".12em" fill="rgb({ACC})">MOUTH · RENTED</text>
      </svg>
      {cap("a chatbot is one organ. the body has five, and yours are empty sockets.")}</div>'''

# 2. ROUTER - one job token routed down 3 tier lanes, SMART lane lit/picked
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

# 3. EYES - radar of live signals, ranked, with a first-to-see lead readout
def eyes():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Stack",210,168),("Intent",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">You + Ultron</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">Tue 09:12</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">Your VC</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">Fri 16:40</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">3 days ahead</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It saw the round first","SIGNAL LEAD")}
        {lead}
        {cap("funding, hiring, stack, intent - this morning's web, watched for you.")}
      </div></div>'''

# 4. VOICE - IVORY construct: style-match ring + a sample written in your voice
def voice():
    pct=98; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It writes in your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">VOICE MATCH</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:190px;height:190px">
          <svg width="190" height="190" viewBox="0 0 190 190">
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 95 95)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016">{pct}%</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">style match</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4">
            "I killed nine tools last month. The one I kept did not have a chat box."</div>
          <div style="display:flex;gap:22px;margin-top:16px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["short lines","no hedging","your cadence"])}
          </div></div>
      </div>
      {cap("sampled from your real posts, banned words enforced on every draft.","#8a745a")}</div>'''

# 5. HANDS - isometric build -> test -> ship pipeline ending in a merged PR
def hands():
    steps=[("BUILD","wrote the feature",0),("TEST","42 passed, 0 failed",1),("SHIP","live on main",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Built, tested, shipped","WHILE YOU WERE OUT")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:120px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Merged &#10003; PR #182</div></div></div>
      {cap("pages, dashboards and fixes from plain English - tested before it ships.")}</div>'''

# 6. HEART - radial memory-core, 5 organ lifelines, one severed
def heart():
    cx,cy=210,210
    organs=[("brain",-90),("eyes",-18),("hands",54),("mouth",126),("voice",198)]
    lines=""; nodes=""
    for i,(nm,a) in enumerate(organs):
        x=cx+150*math.cos(math.radians(a)); y=cy+150*math.sin(math.radians(a)); cut=(i==2)
        col="rgb(200,70,35)" if cut else "rgba(212,162,127,.5)"; dash='stroke-dasharray="4 8"' if cut else ""
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="3" {dash}/>'
        if cut: lines+=f'<text x="{(cx+x)/2:.0f}" y="{(cy+y)/2-10:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb(200,70,35)">severed</text>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="{"rgba(200,70,35,.6)" if cut else "rgba(255,255,255,.14)"}" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="{"#6f6a60" if cut else "#cfc9bd"}">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="hb" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="50" fill="url(#hb)"/></g>
        <path d="M{cx} {cy+22} C{cx-30} {cy-2},{cx-30} {cy-24},{cx-12} {cy-24} C{cx-4} {cy-24},{cx} {cy-16},{cx} {cy-16} C{cx} {cy-16},{cx+4} {cy-24},{cx+12} {cy-24} C{cx+30} {cy-24},{cx+30} {cy-2},{cx} {cy+22}Z" fill="#2a160c"/></svg>
      <div style="flex:1">
        {htitle("Memory is the heart","SHARED CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing, docs - every organ draws from one memory. Cut it and the body goes dark.</div>
        {cap("one core feeds them all. no memory, no body.")}</div></div>'''

# 7. GATE - full-capability orb held on the operator's reins, one lock
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Strong body. My reins.","POWER, HELD")}
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
      {cap("every external move parks for your tap. augmented, never unsupervised.")}</div>'''

# 8. OPERATOR - scattered organ nodes converge into one glowing assembled body
def operator():
    scat=[("brain",70,90),("eyes",70,200),("voice",70,310),("hands",190,150),("heart",190,260)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+30} {y} C340 {y},360 210,520 210" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.7"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Assemble the body","ONE SYSTEM")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="590" cy="210" r="120" fill="url(#bod)"/></g>
        <text x="590" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="590" y="230" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">BODY</text>
        <text x="590" y="366" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">composed · gated · yours</text>
      </svg>
      {cap("one chat wires brain, eyes, voice, hands and heart into one operator.")}</div>'''

PANELS={"difference":difference(),"router":router(),"eyes":eyes(),"voice":voice(),
        "hands":hands(),"heart":heart(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/aibody"; os.makedirs(outd,exist_ok=True)
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
