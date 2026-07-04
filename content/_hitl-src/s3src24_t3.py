#!/usr/bin/env python3
# TIER 3 - THE ZERO-CODE LAUNCH SEQUENCE, on the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Reframes the scraped "70 AI business ideas / zero coding / low startup cost" carousel into Ultron:
# launch and run a real services business with no engineers, for cents, replacing an agency retainer.
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

# 1. FLOOR - two bars on a ground line: agency retainer (red, tall) vs Ultron cents (warm, tiny)
def floor():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("An agency bills 5K. You pay cents.","COST FLOOR")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="red" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e0714b"/><stop offset="100%" stop-color="#a5371c"/></linearGradient>
          <linearGradient id="warmb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="#b17a4f"/></linearGradient>
        </defs>
        <line x1="70" y1="392" x2="750" y2="392" stroke="rgba(255,255,255,.16)" stroke-width="2"/>
        <rect x="150" y="88" width="210" height="304" rx="14" fill="url(#red)"/>
        <rect x="150" y="88" width="210" height="24" rx="14" fill="rgba(255,255,255,.14)"/>
        <text x="255" y="68" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#FAFAF7">$2K to $10K</text>
        <text x="255" y="422" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#c8bfae">AGENCY RETAINER</text>
        <text x="255" y="440" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#8f8f85">per client, every month</text>
        <rect x="470" y="356" width="210" height="36" rx="12" fill="url(#warmb)"/>
        <text x="575" y="338" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="rgb({ACC})">cents</text>
        <text x="575" y="422" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#c8bfae">ULTRON, ALL IN</text>
        <text x="575" y="440" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#8f8f85">per run, pay per token</text>
        <path d="M255 148 C300 116,530 116,575 300" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2" stroke-dasharray="3 7"/>
        <text x="415" y="112" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".05em" fill="rgb({ACC})">same output</text>
      </svg>
      {cap("an agency staffs a team and bills a retainer. you pay per token, in cents.")}</div>'''

# 2. SEQUENCE - IVORY vertical numbered timeline: the four zero-code steps to a live business
def sequence():
    steps=[("01","Describe the business","plain English, no code needed"),
           ("02","The ROUTER wires the agents","the right hire for each job"),
           ("03","You tap to approve","the gate holds every send"),
           ("04","It runs, for cents","live by the weekend")]
    rows=""
    for n,t,s in steps:
        rows+=(f'<div style="display:flex;align-items:center;gap:22px;position:relative;z-index:1">'
          f'<div style="flex-shrink:0;width:64px;height:64px;border-radius:20px;background:linear-gradient(160deg,#ffffff,#efe2cc);border:1.5px solid rgba(150,90,45,.35);box-shadow:0 12px 22px rgba(150,90,45,.20), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:24px;color:#96562d">{n}</div>'
          f'<div style="flex:1;background:rgba(255,255,255,.55);border-left:4px solid #96562d;border-radius:14px;padding:15px 20px">'
          f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:22px;color:#2a2016">{t}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:14px;color:#8a745a;margin-top:3px">{s}</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Four steps to live</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">LAUNCH SEQUENCE</span></div>
      <div style="position:relative;display:flex;flex-direction:column;gap:16px">
        <div style="position:absolute;left:31px;top:24px;bottom:24px;width:2px;background:rgba(150,90,45,.25);z-index:0"></div>
        {rows}
      </div>
      {cap("no engineers, no infra, no code. describe it and approve it.","#8a745a")}</div>'''

# 3. ROSTER - radial hub-and-spokes: ROUTER hub + the seven named agents as the agency team
def roster():
    cx,cy,R=410,234,180
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    n=len(agents); spokes=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*360/n
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="45" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y-3:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".04em" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven specialists, one login","THE ROSTER")}
      <svg width="820" height="474" viewBox="0 0 820 474" style="display:block;margin:0 auto">
        <defs><radialGradient id="rhub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#rhub)"/></g>
        <text x="{cx}" y="{cy-3}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">routes each job</text>
        {nodes}
      </svg>
      {cap("the agency roster without the agency. it hires the right one per job.")}</div>'''

# 4. CORTEX - radar sweep of live signals + a ranked brief readout
def cortex():
    cx,cy,R=196,214,178
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (60,119,178))
    blips=[("Funding",305,150),("Hiring",128,100),("Intent",205,165),("Stack",55,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="rgb({ACC})" filter="url(#cb)"/>'
          f'<text x="{x:.0f}" y="{y-15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    ranked=[("Acme Robotics",94),("Nimbus Data",91),("Orbit Health",88)]
    rows=""
    for nm,sc in ranked:
        rows+=(f'<div style="display:flex;align-items:center;justify-content:space-between;gap:14px;padding:11px 0;border-top:1px solid rgba(255,255,255,.08)">'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#e7e2d8">{nm}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:15px;color:rgb({ACC})">{sc}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="392" height="392" viewBox="0 0 392 392" style="flex-shrink:0">
        <defs><radialGradient id="csw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="cb" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(62)):.0f} {cy-R*math.cos(math.radians(62)):.0f} Z" fill="url(#csw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="6" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It ranks the market","CORTEX")}
        <div style="display:flex;align-items:baseline;gap:12px;margin:2px 0 8px">
          <span style="font-family:'DM Sans';font-weight:900;font-size:46px;color:rgb({ACC})">847</span>
          <span style="font-family:'DM Sans';font-size:17px;color:#8f8f85">fit, from 12,400 scanned</span></div>
        {rows}
        {cap("funding, hiring, intent and stack, ranked into one brief.")}
      </div></div>'''

# 5. SPECTER - bezier flow graph: one lead flows through opener, nudge, break-up, into a booked node
def specter():
    pts=[(96,296,"Trigger"),(250,150,"Opener"),(404,300,"Nudge"),(558,150,"Break-up"),(712,286,"Booked")]
    path="M96 296 C168 224,188 150,250 150 C318 150,340 300,404 300 C468 300,500 150,558 150 C620 150,652 286,712 286"
    nodes=""
    for i,(x,y,lb) in enumerate(pts):
        on=(i==len(pts)-1)
        filt=' filter="url(#sg)"' if on else ''
        fill='url(#sgrad)' if on else '#241f1a'
        stroke=f'rgb({ACC})' if on else 'rgba(212,162,127,.34)'
        tcol='#1a0f0a' if on else '#e0dbd0'
        r=36 if on else 30
        nodes+=(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"{filt}/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="{tcol}">{lb}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A sequence per lead","SPECTER")}
      <svg width="820" height="400" viewBox="0 0 820 400" style="display:block;margin:0 auto">
        <defs><radialGradient id="sgrad" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
        <path d="{path}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>
        {nodes}
        <text x="712" y="340" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">handed to STRIKER</text>
      </svg>
      {cap("opener, nudge, break-up, sent on cadence and handed off on reply.")}</div>'''

# 6. STRIKER - deal funnel: leads narrow through qualified and meetings into closed
def striker():
    bands=[("Leads",240,640),("Qualified",62,470),("Meetings",18,300),("Closed",6,150)]
    cx=410; y0=54; h=82; gap=16; polys=""
    for i,(nm,val,w) in enumerate(bands):
        nw=bands[i+1][2] if i<len(bands)-1 else 92
        top=y0+i*(h+gap)
        x1=cx-w/2; x2=cx+w/2; x3=cx+nw/2; x4=cx-nw/2
        last=(i==len(bands)-1)
        grad='url(#fbot)' if last else 'url(#ftop)'
        tname='#1a0f0a' if last else '#f2ece0'; tval='#1a0f0a' if last else '#FAFAF7'
        polys+=(f'<polygon points="{x1:.0f},{top} {x2:.0f},{top} {x3:.0f},{top+h} {x4:.0f},{top+h}" fill="{grad}" stroke="rgba(255,255,255,.08)"/>'
          f'<text x="{x1+28:.0f}" y="{top+h/2+3:.0f}" font-family="DM Sans" font-weight="700" font-size="18" fill="{tname}">{nm}</text>'
          f'<text x="{x2-28:.0f}" y="{top+h/2+10:.0f}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="30" fill="{tval}">{val}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Leads in, closed deals out","STRIKER")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="ftop" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#4a4038"/><stop offset="100%" stop-color="#322b25"/></linearGradient>
          <linearGradient id="fbot" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        </defs>
        {polys}
      </svg>
      {cap("qualification, discovery, objections and the close plan, run for you.")}</div>'''

# 7. GATE - IVORY wax-seal + pending receipt chips: every external move parked for a tap
def gate():
    pend=[("SPECTER","send 42 cold emails"),("STRIKER","email a proposal"),("AMPLIFY","publish 3 posts")]
    chips=""
    for ag,act in pend:
        chips+=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.6);border:1px solid rgba(150,90,45,.18);border-radius:16px;padding:14px 18px">'
          f'<div style="flex-shrink:0;width:34px;height:34px;border-radius:10px;background:rgba(150,90,45,.12);display:flex;align-items:center;justify-content:center"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.6"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#96562d">{ag}</div><div style="font-family:\'DM Sans\';font-weight:700;font-size:17px;color:#2a2016">wants to {act}</div></div>'
          f'<div style="flex-shrink:0;font-family:\'DM Sans\';font-weight:800;font-size:13px;letter-spacing:.06em;color:#8a745a">HELD</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Everything parks for your tap</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">HUMAN GATE</span></div>
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:15px">
          <svg width="200" height="200" viewBox="0 0 200 200">
            <defs><radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#e6c69f"/><stop offset="58%" stop-color="#c78a5c"/><stop offset="100%" stop-color="#89522a"/></radialGradient>
            <filter id="slg" x="-50%" y="-50%" width="200%" height="200%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="rgba(120,80,40,.4)"/></filter></defs>
            <circle cx="100" cy="100" r="86" fill="url(#seal)" filter="url(#slg)"/>
            <circle cx="100" cy="100" r="74" fill="none" stroke="rgba(255,255,255,.45)" stroke-width="2" stroke-dasharray="3 8"/>
            <path d="M74 100 l17 17 l34 -40" fill="none" stroke="#ffffff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#96562d">YOUR APPROVAL</div>
        </div>
        <div style="flex:1;display:flex;flex-direction:column;gap:13px">{chips}</div>
      </div>
      {cap("every external move waits. you approve, then it sends. still your company.","#8a745a")}</div>'''

# 8. METER - ring gauge cost meter + the cents-vs-agency comparison
def meter():
    r=96; circ=2*math.pi*r; dash=circ*0.06
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;position:relative;width:300px;height:300px">
        <svg width="300" height="300" viewBox="0 0 300 300">
          <defs><filter id="mg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
          <circle cx="150" cy="150" r="{r}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="20"/>
          <circle cx="150" cy="150" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="20" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 150 150)" filter="url(#mg)"/>
        </svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:'DM Sans';font-weight:900;font-size:60px;color:#FAFAF7;line-height:1">30c</span>
          <span style="font-family:'DM Mono';font-size:13px;color:rgb({ACC});margin-top:5px">this launch run</span></div>
      </div>
      <div style="flex:1">
        {htitle("You pay in cents","PAY PER TOKEN")}
        <div style="border-left:4px solid rgb({ACC});padding:6px 0 6px 18px;margin-bottom:16px">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.06em;color:#8f8f85">ULTRON, PER RUN</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:40px;color:rgb({ACC})">30c</div></div>
        <div style="border-left:4px solid rgb(200,70,35);padding:6px 0 6px 18px">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.06em;color:#8f8f85">AGENCY, PER MONTH</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:40px;color:rgb(200,70,35)">$5,000</div></div>
        {cap("tokens the work burns, nothing sitting on a retainer.")}
      </div></div>'''

PANELS={"floor":floor(),"sequence":sequence(),"roster":roster(),"cortex":cortex(),
        "specter":specter(),"striker":striker(),"gate":gate(),"meter":meter()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src24"; os.makedirs(outd,exist_ok=True)
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
