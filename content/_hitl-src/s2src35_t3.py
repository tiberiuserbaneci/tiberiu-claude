#!/usr/bin/env python3
# TIER 3 - THE COMPOUND MEMORY, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Theme: Ultron's memory core that captures everything and compounds week over week. Cents pricing.
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

# 1. AMNESIA - a chat window mockup with the memory meter pinned at 0% (generic AI has no recall)
def amnesia():
    bubbles=('<div style="display:flex;justify-content:flex-end;margin-bottom:12px">'
      f'<div style="max-width:64%;background:rgb({ACC});color:#1a0f0a;font-family:\'DM Sans\';font-weight:600;font-size:18px;padding:12px 16px;border-radius:16px 16px 4px 16px">Where does the Acme deal stand?</div></div>'
      '<div style="display:flex;justify-content:flex-start">'
      '<div style="max-width:76%;background:#2b2723;color:#c9c3b8;font-family:\'DM Sans\';font-size:18px;padding:12px 16px;border-radius:16px 16px 16px 4px;border:1px solid rgba(255,255,255,.07)">I have no record of Acme, or of any earlier conversation.</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every session starts blank","NO MEMORY")}
      <div style="background:linear-gradient(160deg,#211e1a,#181613);border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:24px 26px;box-shadow:inset 0 2px 3px rgba(255,255,255,.06)">
        <div style="display:flex;align-items:center;gap:9px;border-bottom:1px solid rgba(255,255,255,.07);padding-bottom:15px;margin-bottom:20px">
          <span style="width:11px;height:11px;border-radius:50%;background:#c84623"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#3a352f"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#3a352f"></span>
          <span style="font-family:'DM Mono';font-size:14px;color:#8f8f85;margin-left:8px">session #4198 &middot; new</span>
          <span style="margin-left:auto;font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#c84623">CONTEXT CLEARED</span></div>
        {bubbles}
        <div style="margin-top:26px;display:flex;align-items:center;gap:16px">
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#8f8f85">MEMORY</span>
          <div style="flex:1;height:15px;border-radius:8px;background:rgba(250,250,247,.06);border:1px solid rgba(255,255,255,.08);overflow:hidden"><div style="width:2%;height:100%;background:#c84623"></div></div>
          <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#c84623">0%</span></div>
      </div>
      {cap("no history, no context. you re-brief it from scratch, every single time.")}</div>'''

# 2. LOOP - bezier convergence: four capture sources flow into one glowing memory core
def capture():
    W,H=820,450
    src=[("Sales calls",90),("Inbox threads",190),("Deal notes",290),("Docs & specs",390)]
    hubx,huby=650,240; edges=""; nodes=""
    for nm,y in src:
        mx=(212+hubx)/2
        edges+=f'<path d="M212 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-78} {huby}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=(f'<rect x="40" y="{y-27}" width="174" height="54" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="127" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="16" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Everything lands in one core","CAPTURE LOOP")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="88" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#1a0f0a">MEMORY</text>
        <text x="{hubx}" y="{huby+18}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010">one core</text>
      </svg>
      {cap("calls, inboxes, deals and docs - captured once, remembered for good.")}</div>'''

# 3. WEEK 1 - IVORY seed: three basics chips butting into a small warm seed core
def week1():
    facts=[("WHO YOU ARE","seed-stage SaaS, 6 people"),("WHAT YOU SELL","RevOps automation"),("WHO YOU SELL TO","US and UK founders")]
    chips=""
    for k,v in facts:
        chips+=(f'<div style="background:rgba(255,255,255,.62);border-left:4px solid #96562d;border-radius:12px;padding:14px 18px;margin-bottom:14px">'
          f'<div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:#96562d">{k}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:20px;color:#2a2016;margin-top:2px">{v}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Week one: the basics</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">DAY 1-7</span></div>
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex:1">{chips}</div>
        <div style="flex-shrink:0;width:230px;display:flex;align-items:center;justify-content:center">
          <svg width="230" height="230" viewBox="0 0 230 230">
            <defs><radialGradient id="seed" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="#c8895f"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
            <radialGradient id="sbloom" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(150,90,45,.30)"/><stop offset="100%" stop-color="rgba(150,90,45,0)"/></radialGradient></defs>
            <circle cx="115" cy="108" r="105" fill="url(#sbloom)"/>
            <circle cx="115" cy="108" r="54" fill="url(#seed)"/>
            <ellipse cx="99" cy="90" rx="18" ry="11" fill="rgba(255,255,255,.5)" transform="rotate(-28 99 90)"/>
            <text x="115" y="204" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".14em" fill="#96562d">SEED CORE</text>
          </svg>
        </div>
      </div>
      {cap("who you are, what you sell, how you win - locked in from day one.","#8a745a")}</div>'''

# 4. WEEK 4 - orbital constellation of client-account nodes ringed around the grown core
def week4():
    cx,cy,R=300,225,168
    clients=["Acme","Globex","Northwind","Initech","Umbrella","Stark","Wayne","Hooli"]
    n=len(clients); orbit=""
    for i,nm in enumerate(clients):
        a=-90+i*(360/n)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        orbit+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.22)" stroke-width="1.5"/>'
          f'<rect x="{x-52:.0f}" y="{y-19:.0f}" width="104" height="38" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It knows your whole book","WEEK 4")}
      <svg width="600" height="470" viewBox="0 0 600 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="cr" cx="38%" cy="32%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(212,162,127,.14)" stroke-dasharray="3 8"/>
        {orbit}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#cr)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="32" fill="#1a0f0a">42</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">accounts</text>
      </svg>
      {cap("every account, thread and promise made on a call - recalled on demand.")}</div>'''

# 5. WEEK 8 - a caught-items agenda: overdue commitments flagged red, an upcoming one surfaced early
def week8():
    rows=[("Follow up with Globex","promised Tuesday, now 4 days late",True),
          ("Send Acme the revised terms","you committed on the May 14 call",True),
          ("Northwind renewal","auto-surfaced, 30 days out",False)]
    items=""
    for t,s,caught in rows:
        if caught:
            badge=f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:11px;letter-spacing:.12em;color:#1a0f0a;background:rgb({ACC});padding:6px 12px;border-radius:999px">CAUGHT</span>'
            bar="rgb(200,70,35)"
        else:
            badge=f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:11px;letter-spacing:.12em;color:rgb({ACC});border:1px solid rgba(212,162,127,.45);padding:5px 11px;border-radius:999px">AHEAD</span>'
            bar=f"rgb({ACC})"
        items+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(158deg,#312d28,#211e1a);border:1px solid rgba(255,255,255,.09);border-left:4px solid {bar};border-radius:16px;padding:16px 20px;margin-bottom:14px;box-shadow:0 12px 24px rgba(0,0,0,.4)">'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#FAFAF7">{t}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8f8f85;margin-top:2px">{s}</div></div>{badge}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It catches what you missed","WEEK 8")}
      {items}
      {cap("overdue follow-ups, forgotten commitments, dots joined across your pipeline.")}</div>'''

# 6. CURVE - IVORY compound-growth chart: memory depth rising over weeks vs a flat generic tool
def curve():
    W,H=760,340
    x0,y0,x1,y1=72,30,720,300
    weeks=[1,2,4,6,8,10,12]; pts=[]
    for w in weeks:
        px=x0+(w-1)/11*(x1-x0); depth=(w/12)**1.7
        pts.append((px, y1-depth*(y1-y0)))
    path=f"M{pts[0][0]:.0f} {pts[0][1]:.0f}"
    for i in range(1,len(pts)):
        (px0,py0),(px1,py1)=pts[i-1],pts[i]; mx=(px0+px1)/2
        path+=f" C{mx:.0f} {py0:.0f},{mx:.0f} {py1:.0f},{px1:.0f} {py1:.0f}"
    dots="".join(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="6" fill="#96562d"/>' for px,py in pts)
    grid="".join(f'<line x1="{x0}" y1="{y0+(y1-y0)*g/4:.0f}" x2="{x1}" y2="{y0+(y1-y0)*g/4:.0f}" stroke="rgba(150,120,80,.14)"/>' for g in range(5))
    wl="".join(f'<text x="{x0+(w-1)/11*(x1-x0):.0f}" y="{y1+30}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8a745a">W{w}</text>' for w in weeks)
    flat=f'<path d="M{x0} {y1-14} L{x1} {y1-24}" stroke="#b7a88f" stroke-width="2.5" stroke-dasharray="6 6" fill="none"/>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:8px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Memory that compounds</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">DEPTH / WEEK</span></div>
      <svg width="{W}" height="{H+44}" viewBox="0 0 {W} {H+44}" style="display:block;margin:0 auto">
        <defs><linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(150,90,45,.28)"/><stop offset="100%" stop-color="rgba(150,90,45,0)"/></linearGradient></defs>
        {grid}
        <path d="{path} L{x1} {y1} L{x0} {y1} Z" fill="url(#area)"/>
        {flat}
        <text x="{x1-6}" y="{y1-30}" text-anchor="end" font-family="DM Mono" font-size="13" fill="#a8977c">generic tool: resets</text>
        <path d="{path}" fill="none" stroke="#96562d" stroke-width="4" stroke-linecap="round"/>
        {dots}
        <text x="{pts[-1][0]-2:.0f}" y="{pts[-1][1]-16:.0f}" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="16" fill="#2a2016">knows you cold</text>
        {wl}
      </svg>
      {cap("every interaction deepens the core. tools reset; your operator gets sharper.","#8a745a")}</div>'''

# 7. AGENTS - shared core on the left, seven named agent chips on the right, glowing lifelines
def agents():
    ags=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
         ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    W,H=820,500; cx,cy=168,250; n=len(ags); top=32; gap=(H-2*top)/(n-1)
    lines=""; chips=""
    for i,(nm,role) in enumerate(ags):
        y=top+i*gap
        lines+=f'<path d="M{cx+68} {cy} C330 {cy},372 {y:.0f},470 {y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2" fill="none"/>'
        chips+=(f'<rect x="470" y="{y-26:.0f}" width="330" height="52" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>'
          f'<text x="492" y="{y+5:.0f}" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{nm}</text>'
          f'<text x="786" y="{y+5:.0f}" text-anchor="end" font-family="DM Mono" font-size="14" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one memory","SHARED CORE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="ac" cx="38%" cy="32%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ag" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}
        <g filter="url(#ag)"><circle cx="{cx}" cy="{cy}" r="82" fill="url(#ac)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">shared core</text>
      </svg>
      {cap("CORTEX, SPECTER, STRIKER and the rest all draw from the same brain.")}</div>'''

# 8. CENTS - the stitched competitor stack (high $, crossed out) vs Ultron memory at cents/update
def cents():
    stack=[("CRM seat","$99/mo"),("AI notetaker","$30/mo"),("Data enrichment","$200/mo")]
    rows=""
    for nm,c in stack:
        rows+=(f'<div style="display:flex;justify-content:space-between;align-items:center;background:rgba(250,250,247,.03);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:14px 18px;margin-bottom:12px">'
          f'<span style="font-family:\'DM Sans\';font-size:18px;color:#a8a296">{nm}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:17px;color:#c84623;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.8)">{c}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("One core replaces the stack","THE MATH")}
      <div style="display:flex;align-items:stretch;gap:26px">
        <div style="flex:1">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#8f8f85;margin-bottom:12px">THE STITCHED STACK</div>
          {rows}
          <div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid rgba(255,255,255,.1);padding-top:14px;margin-top:4px">
            <span style="font-family:'DM Sans';font-weight:700;font-size:18px;color:#c9c3b8">every month</span>
            <span style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#c84623;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.75)">$329</span></div>
        </div>
        <div style="flex-shrink:0;width:300px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:22px;padding:30px 24px;box-shadow:0 24px 44px rgba(0,0,0,.5), inset 0 2px 3px rgba(255,255,255,.1)">
          <div style="font-family:'DM Sans';font-weight:900;font-size:28px;color:#FAFAF7;line-height:1.1">Ultron memory</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:60px;color:rgb({ACC});line-height:1;margin-top:14px">cents</div>
          <div style="font-family:'DM Mono';font-size:15px;color:#c9a583;margin-top:8px">per update</div>
          <div style="font-family:'DM Sans';font-size:15px;color:#8f8f85;margin-top:16px">pay per token, nothing idle</div>
        </div>
      </div>
      {cap("stop paying three subscriptions to half-remember your own business.")}</div>'''

PANELS={"amnesia":amnesia(),"capture":capture(),"week1":week1(),"week4":week4(),
        "week8":week8(),"curve":curve(),"agents":agents(),"cents":cents()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src35"; os.makedirs(outd,exist_ok=True)
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
