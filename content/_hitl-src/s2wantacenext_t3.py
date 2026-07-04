#!/usr/bin/env python3
# TIER 3 - OPERATORS NOT STUDENTS ("stop studying AI, start operating it"), built to the WIRE-ITS-EYES
# bar: each panel a UNIQUE hand-built coded scene filling a clean rounded card, title + one-line caption,
# NO generic stat-chip strips, NO cuts/walls. Warm palette. Cents pricing. Overwrites models_clay/s2wantacenext/*.png.
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

# 1. SPLIT - theory-vs-shipping split: dim crossed-out study column | lit shipped-systems column
def split():
    studied=[("AI course, 40 hrs","half-watched"),("agent tutorials","bookmarked"),("theory notebook","never opened")]
    shipped=[("200 emails sent","SPECTER"),("12 deals qualified","STRIKER"),("PR #182 merged","SENTINEL")]
    lcol=""
    for a,b in studied:
        lcol+=f'''<div style="background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);border-radius:14px;padding:16px 18px;opacity:.72">
          <div style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">{a}</div>
          <div style="font-family:'DM Mono';font-size:12px;color:#7a746a;margin-top:4px">{b}</div></div>'''
    rcol=""
    for a,b in shipped:
        rcol+=f'''<div style="background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(212,162,127,.32);border-radius:14px;padding:16px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5),inset 0 2px 2px rgba(255,255,255,.06)">
          <div style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:rgb({ACC});margin-top:4px">{b}</div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You studied. They shipped.","STUDENT / OPERATOR")}
      <div style="display:flex;gap:22px;align-items:stretch">
        <div style="flex:1">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:#7a746a;margin-bottom:14px">STUDIED</div>
          <div style="display:flex;flex-direction:column;gap:14px">{lcol}</div></div>
        <div style="width:2px;background:linear-gradient(180deg,transparent,rgba(212,162,127,.45),transparent)"></div>
        <div style="flex:1">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:rgb({ACC});margin-bottom:14px">SHIPPED</div>
          <div style="display:flex;flex-direction:column;gap:14px">{rcol}</div></div>
      </div>
      {cap("theory fills a notebook. operators fill a pipeline.")}</div>'''

# 2. CLOCK - study-hours vs ship-timeline: long dim striped bar vs short lit accent bar
def clock():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {htitle("Four hundred hours, zero shipped","TIME TO SHIP")}
      <div style="display:flex;flex-direction:column;gap:30px;margin-top:10px">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px">
            <span style="font-family:'DM Mono';font-size:14px;letter-spacing:.14em;color:#8f8f85">STUDYING AI</span>
            <span style="font-family:'DM Sans';font-weight:900;font-size:32px;color:#8f8f85">400 hrs</span></div>
          <div style="height:40px;border-radius:12px;background:repeating-linear-gradient(90deg,rgba(250,250,247,.07),rgba(250,250,247,.07) 13px,transparent 13px,transparent 26px);border:1px dashed rgba(250,250,247,.16)"></div>
          <div style="font-family:'DM Mono';font-size:12.5px;color:#7a746a;margin-top:10px">courses, papers, agent tutorials, still nothing live</div>
        </div>
        <div>
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px">
            <span style="font-family:'DM Mono';font-size:14px;letter-spacing:.14em;color:rgb({ACC})">OPERATING ULTRON</span>
            <span style="font-family:'DM Sans';font-weight:900;font-size:32px;color:#FAFAF7">1 day</span></div>
          <div style="height:40px;width:23%;border-radius:12px;background:linear-gradient(90deg,#e6b48f,rgb({ACC}));box-shadow:0 12px 26px rgba(212,162,127,.4),inset 0 2px 3px rgba(255,255,255,.4)"></div>
          <div style="font-family:'DM Mono';font-size:12.5px;color:#9a9488;margin-top:10px">first sequence live, first deals qualified, same afternoon</div>
        </div>
      </div>
      {cap("you can study the agent for a year, or run it before lunch.")}</div>'''

# 3. ROSTER - bezier flow graph: 7 named agents converge into one operator hub
def roster():
    W,H=820,470
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    hubx,huby=650,235
    edges="";nodes=""
    for i,(nm,role) in enumerate(agents):
        y=42+i*62
        mx=(184+hubx)/2
        edges+=f'<path d="M184 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-74} {huby}" stroke="rgba(212,162,127,.42)" stroke-width="2.2" fill="none"/>'
        nodes+=f'''<rect x="34" y="{y-24}" width="150" height="48" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>
          <text x="52" y="{y-3}" font-family="DM Mono" font-weight="500" font-size="15" fill="rgb({ACC})">{nm}</text>
          <text x="52" y="{y+15}" font-family="DM Sans" font-size="12" fill="#8f8f85">{role}</text>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven hires, no onboarding","AGENT ROSTER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="78" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">YOU</text>
        <text x="{hubx}" y="{huby+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one operator</text>
      </svg>
      {cap("a research, sales, content, code and legal team, live on day one.")}</div>'''

# 4. STACK - isometric stack of shipped result cards, each carrying its agent
def stack():
    rows=[("200 emails sent","34 replied, 7 booked","SPECTER"),
          ("12 deals qualified","4 moved to proposal","STRIKER"),
          ("PR #182 merged","live on main, tests green","SENTINEL")]
    cards=""
    for i,(a,b,ag) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:25px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:rgb({ACC});background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.3);padding:9px 15px;border-radius:11px">{ag}</div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Working systems, not notes","WHILE YOU STUDIED")}
      <div style="perspective:2000px;height:540px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:490px;position:relative">{cards}</div></div>
      {cap("each agent ships a real output, not a certificate.")}</div>'''

# 5. GAUGE - IVORY: cents ring gauge, competitor course cost vs pay-per-token
def gauge():
    pct=6; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">A course costs $600. This costs cents.</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PAY PER TOKEN</span></div>
      <div style="display:flex;align-items:center;gap:36px">
        <div style="flex-shrink:0;position:relative;width:200px;height:200px">
          <svg width="200" height="200" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="16"/>
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="#96562d" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 100 100)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:42px;color:#2a2016">0.11c</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">per job</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:20px 22px">
            <div style="font-family:'DM Sans';font-weight:900;font-size:32px;color:#2a2016;line-height:1.08">240 emails drafted</div>
            <div style="font-family:'DM Sans';font-size:20px;color:#5a4634;margin-top:5px">for the price of a coffee</div></div>
          <div style="display:flex;gap:22px;margin-top:18px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["no seat fee","no course","cents per run"])}
          </div></div>
      </div>
      {cap("everything at ultron costs cents. pay per token, nothing wasted.","#8a745a")}</div>'''

# 6. RADAR - radar sweep of live market signals, first-to-see lead readout
def radar():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Rival",210,168),("Intent",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">You + Ultron</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">Tue 09:12</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">Still on the tutorial</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">Fri 16:40</span></div>'
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
        {htitle("It watches while you sleep","OVERNIGHT")}
        {lead}
        {cap("funding, hiring, rivals, intent - signals no syllabus will teach you.")}
      </div></div>'''

# 7. FIELD - dot field: thousands of tutorials read, a handful of systems actually shipped
def field():
    cols,rowsn=44,24  # 1056 dots
    lit={73,208,341,486,612,760,905,1002}
    dots=""
    cell=15; gap=3
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:40px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">10,000</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">tutorials read</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">8 systems live</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="font-family:'DM Mono';font-size:14px;color:#8f8f85;margin-top:14px">reading is not shipping. only the lit ones ever sent an email.</div></div>'''

# 8. HUB - radial hub-and-spokes: 6 agent spokes on the operator, one HUMAN GATE lock
def hub():
    cx,cy,Rr=306,230,168
    spokes=[("outbound",-90),("research",-30),("deals",30),("content",90),("code",150),("legal",210)]
    ring=""
    for nm,a in spokes:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="32" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents. Your reins.","HUMAN GATE")}
      <svg width="612" height="480" viewBox="0 0 612 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {ring}
        <g filter="url(#og)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#orb)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">YOU</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one operator</text>
        <!-- human gate lock badge, subordinated, pinned bottom -->
        <g transform="translate({cx-40},430)">
          <rect x="0" y="0" width="80" height="42" rx="11" fill="#201d19" stroke="rgb({ACC})" stroke-width="2"/>
          <g transform="translate(28,9)"><rect x="0" y="10" width="24" height="18" rx="4" fill="none" stroke="rgb({ACC})" stroke-width="3"/><path d="M4 10 V6 a8 8 0 0 1 16 0 v4" fill="none" stroke="rgb({ACC})" stroke-width="3"/></g>
        </g>
        <text x="{cx}" y="418" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="rgb({ACC})">every external move waits for your tap</text>
      </svg>
      {cap("the agents run the work. you still hold the gate. augmented, never unsupervised.")}</div>'''

PANELS={"split":split(),"clock":clock(),"roster":roster(),"stack":stack(),
        "gauge":gauge(),"radar":radar(),"field":field(),"hub":hub()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2wantacenext"; os.makedirs(outd,exist_ok=True)
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
