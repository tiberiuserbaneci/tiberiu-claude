#!/usr/bin/env python3
# TIER 3 - AN ORG CHART WITH NO GAPS. Coverage-completeness angle: a real company org, every box
# filled by a named Ultron agent. 8 UNIQUE hand-built coded scenes (org tree, coverage grid, iso
# brief stack, sequence timeline, deal funnel, hub-and-spokes distribution, ivory contract sheet,
# ivory coverage gauge). Clean CARD/CARDIV, warm palette, htitle + one cap each.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. ORG TREE - the complete company org, CEO on top, every department box filled by a named agent
def orgtree():
    cols=[("CORTEX","research","SPECTER","outbound"),
          ("STRIKER","deals","PULSE","content"),
          ("SENTINEL","product","AMPLIFY","distribution"),
          ("COUNSEL","legal","ROUTER","operations")]
    cx=[112,308,504,700]
    busY=120; r1y=146; r2y=250; bh=76
    def box(x,y,agent,fn):
        lx=x-88
        return (f'<rect x="{lx}" y="{y}" width="176" height="{bh}" rx="15" fill="url(#bx)" stroke="rgba(212,162,127,.42)" stroke-width="1.5"/>'
          f'<circle cx="{lx+176-22}" cy="{y+22}" r="8" fill="rgb({ACC})"/>'
          f'<path d="M{lx+176-27} {y+22} l3.4 3.4 l6.4 -7.6" fill="none" stroke="#1a0f0a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<text x="{lx+20}" y="{y+36}" font-family="DM Sans" font-weight="800" font-size="21" fill="#FAFAF7">{agent}</text>'
          f'<text x="{lx+20}" y="{y+59}" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="rgb({ACC})">{fn}</text>')
    boxes=""; conns=""
    for i,(a1,f1,a2,f2) in enumerate(cols):
        x=cx[i]
        conns+=f'<line x1="{x}" y1="{busY}" x2="{x}" y2="{r1y}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        conns+=f'<line x1="{x}" y1="{r1y+bh}" x2="{x}" y2="{r2y}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        boxes+=box(x,r1y,a1,f1)+box(x,r2y,a2,f2)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every seat has a name","FULL ORG")}
      <svg width="820" height="356" viewBox="0 0 820 356" style="display:block;margin:0 auto">
        <defs><linearGradient id="bx" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38322b"/><stop offset="100%" stop-color="#231f1b"/></linearGradient>
        <radialGradient id="ceo" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <line x1="410" y1="70" x2="410" y2="94" stroke="rgba(212,162,127,.5)" stroke-width="2.4"/>
        <line x1="112" y1="94" x2="700" y2="94" stroke="rgba(212,162,127,.5)" stroke-width="2.4"/>
        <line x1="112" y1="94" x2="112" y2="{busY}" stroke="rgba(212,162,127,.5)" stroke-width="2.4"/>
        <line x1="700" y1="94" x2="700" y2="{busY}" stroke="rgba(212,162,127,.5)" stroke-width="2.4"/>
        {conns}
        <g filter="url(#cg)"><rect x="316" y="16" width="188" height="58" rx="16" fill="url(#ceo)"/></g>
        <text x="410" y="42" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">YOU</text>
        <text x="410" y="62" text-anchor="middle" font-family="DM Mono" font-size="11.5" letter-spacing=".1em" fill="#3a2010">HUMAN GATE</text>
        {boxes}
      </svg>
      {cap("one founder at the top, an Ultron agent in every box below. zero empty seats.")}</div>'''

# 2. COVERAGE GRID - the chart most solo founders actually run: 7 open red sockets, you in one box
def gaps():
    fns=["Research","Outbound","Deals","Content","Product","Distribution","Legal","Operations"]
    covered={3}  # only Content, done by you part-time
    tiles=""
    for i,fn in enumerate(fns):
        if i in covered:
            tiles+=(f'<div style="background:linear-gradient(160deg,#38322b,#231f1b);border:1.5px solid rgba(212,162,127,.5);border-radius:16px;padding:16px 16px 14px;box-shadow:inset 0 2px 2px rgba(255,255,255,.06)">'
              f'<div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">{fn}</div>'
              f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:rgb({ACC});margin-top:8px">YOU &middot; PART-TIME</div></div>')
        else:
            tiles+=(f'<div style="background:rgba(200,70,35,.05);border:1.5px dashed rgba(200,70,35,.5);border-radius:16px;padding:16px 16px 14px">'
              f'<div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#a8a296">{fn}</div>'
              f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:rgb({RED});margin-top:8px">SEAT OPEN</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:20px">
        <div><span style="font-family:DM Sans;font-weight:900;font-size:52px;color:rgb({RED});line-height:1">1</span>
          <span style="font-family:DM Sans;font-weight:700;font-size:22px;color:#a8a296;margin-left:6px">/ 8 covered</span></div>
        <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({RED})">7 SEATS OPEN</span></div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">{tiles}</div>
      {cap("you in one box, seven functions unmanned. that gap is your ceiling.")}</div>'''

# 3. RESEARCH - CORTEX: isometric stack of ranked target briefs
def research():
    rows=[("Northwind Robotics","hiring 3 ops roles","94"),
          ("Globex Systems","raised a round in May","89"),
          ("Initech","no AI layer yet","82")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:25px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 17px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{c}</span>
            <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">FIT</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:38px 44px 44px">
      {htitle("The research seat, ranked","CORTEX")}
      <div style="perspective:2000px;height:520px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:460px;position:relative">{cards}</div></div>
    </div>'''

# 4. OUTBOUND - SPECTER: linear multi-touch sequence timeline, last node booked and lit
def outbound():
    steps=[("Touch 1","intro",False),("Touch 2","nudge",False),("Touch 3","case study",False),
           ("Reply","warm",False),("Booked","call held",True)]
    n=len(steps); x0=70; x1=750; y=150
    dx=(x1-x0)/(n-1)
    line=f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgba(212,162,127,.3)" stroke-width="3"/>'
    nodes=""
    for i,(nm,sub,on) in enumerate(steps):
        x=x0+i*dx
        if on:
            nodes+=(f'<circle cx="{x:.0f}" cy="{y}" r="26" fill="rgb({ACC})" filter="url(#og)"/>'
              f'<path d="M{x-11:.0f} {y} l7 7 l14 -16" fill="none" stroke="#1a0f0a" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            nodes+=(f'<circle cx="{x:.0f}" cy="{y}" r="19" fill="#2a2622" stroke="rgba(212,162,127,.55)" stroke-width="2.5"/>'
              f'<circle cx="{x:.0f}" cy="{y}" r="6" fill="rgb({ACC})"/>')
        nodes+=(f'<text x="{x:.0f}" y="{y-42}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+52}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8f8f85">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Outbound that follows up itself","SPECTER")}
      <svg width="820" height="300" viewBox="0 0 820 300" style="display:block;margin:8px auto 0">
        <defs><filter id="og" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.75"/></filter></defs>
        {line}{nodes}
        <text x="410" y="252" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#FAFAF7">50 leads in <tspan fill="rgb({ACC})">&#8594;</tspan> 7 calls booked</text>
      </svg>
      {cap("finds the lead, writes the email, works the follow-up. you just close.")}</div>'''

# 5. DEALS - STRIKER: proportional deal funnel, closed band brightest
def deals():
    stages=[("Leads","200",560),("Qualified","90",470),("Discovery","40",380),("Proposal","18",290),("Closed","7",200)]
    cxr=410; y0=24; bh=64; gap=12
    bands=""
    for i,(nm,num,w) in enumerate(stages):
        y=y0+i*(bh+gap); x=cxr-w/2; last=(i==len(stages)-1)
        fill="url(#fend)" if last else "url(#fband)"
        bands+=(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="{bh}" rx="12" fill="{fill}" stroke="rgba(212,162,127,{0.6 if last else 0.28})" stroke-width="{2 if last else 1.2}"/>'
          f'<text x="{cxr-w/2+22:.0f}" y="{y+40}" font-family="DM Sans" font-weight="800" font-size="20" fill="{"#1a0f0a" if last else "#FAFAF7"}">{nm}</text>'
          f'<text x="{cxr+w/2-22:.0f}" y="{y+41}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="24" fill="{"#1a0f0a" if last else "rgb("+ACC+")"}">{num}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Deals worked to the close","STRIKER")}
      <svg width="820" height="404" viewBox="0 0 820 404" style="display:block;margin:0 auto">
        <defs><linearGradient id="fband" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#38322b"/><stop offset="100%" stop-color="#241f1a"/></linearGradient>
        <linearGradient id="fend" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#9a5a35"/></linearGradient></defs>
        {bands}
      </svg>
      {cap("qualify, discovery, objections, proposal, close. one seat runs the whole board.")}</div>'''

# 6. MARKETING - PULSE + AMPLIFY: hub-and-spokes, one brief reshaped to every channel
def marketing():
    cx,cy=205,215; R=170
    chans=[("LinkedIn",-90),("TikTok",-26),("Instagram",38),("Newsletter",102),("X",166)]
    spokes=""; chips=""
    for nm,a in chans:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
        chips+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="420" height="430" viewBox="0 0 420 430">
        <defs><radialGradient id="hb" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}{chips}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">1</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#3a2010">brief</text>
      </svg>
      <div style="flex:1">
        {htitle("One brief, every channel","PULSE + AMPLIFY")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Written once in your voice, reshaped and scheduled per channel and time zone. Two seats, no calendar.</div>
        {cap("content and distribution, filled and firing while you sleep.")}
      </div></div>'''

# 7. LEGAL - COUNSEL (IVORY): a contract sheet, clauses checked or flagged
def legal():
    clauses=[("Payment terms","net 30 accepted",False),
             ("Liability cap","1x fees, standard",False),
             ("Auto-renewal","evergreen, 90d notice",True),
             ("IP assignment","work-for-hire clear",False),
             ("Governing law","venue skewed to them",True)]
    rows=""
    for nm,note,flag in clauses:
        if flag:
            icon=(f'<span style="flex-shrink:0;width:26px;height:26px;border-radius:50%;background:rgba(200,70,35,.14);display:flex;align-items:center;justify-content:center">'
              f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb({RED})" stroke-width="2.6" stroke-linecap="round"><path d="M12 8v5"/><circle cx="12" cy="17" r="0.6" fill="rgb({RED})" stroke="none"/><path d="M12 3 2 20h20Z"/></svg></span>')
            tag=f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({RED})">FLAGGED</span>'
            nc="#7a2f1c"
        else:
            icon=(f'<span style="flex-shrink:0;width:26px;height:26px;border-radius:50%;background:rgba(150,86,45,.16);display:flex;align-items:center;justify-content:center">'
              f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span>')
            tag='<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#96562d">CLEAR</span>'
            nc="#5a4634"
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.14);border-radius:14px;padding:15px 18px">'
          f'{icon}<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14.5px;color:{nc}">{note}</div></div>{tag}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("Contracts, read and flagged","COUNSEL","#2a2016")}
      <div style="background:rgba(120,95,60,.06);border:1px solid rgba(120,95,60,.14);border-radius:18px;padding:14px 14px;display:flex;flex-direction:column;gap:11px">
        <div style="display:flex;align-items:baseline;justify-content:space-between;padding:0 4px 4px">
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:#96562d">MASTER SERVICES AGREEMENT</span>
          <span style="font-family:DM Mono;font-size:13px;color:#7a2f1c">2 to fix</span></div>
        {rows}
      </div>
      {cap("NDAs, MSAs and term sheets drafted and risk-flagged before you sign.","#8a745a")}</div>'''

# 8. COVERAGE - ROUTER + GATE (IVORY): full ring gauge, every function ticked, zero headcount
def coverage():
    r=86; circ=2*math.pi*r
    fns=["research","outbound","deals","content","product","distro","legal","ops"]
    ticks=""
    for i,fn in enumerate(fns):
        ticks+=(f'<div style="display:flex;align-items:center;gap:8px">'
          f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="font-family:DM Mono;font-size:13px;color:#5a4634">{fn}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Every function covered","8 / 8","#2a2016")}
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0;position:relative;width:210px;height:210px">
          <svg width="210" height="210" viewBox="0 0 210 210">
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="17"/>
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="#96562d" stroke-width="17" stroke-linecap="round" stroke-dasharray="{circ:.0f} {circ:.0f}" transform="rotate(-90 105 105)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:52px;color:#2a2016;line-height:1">8/8</span>
            <span style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:#96562d;margin-top:2px">seats filled</span></div></div>
        <div style="flex:1">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:13px 18px;margin-bottom:16px">{ticks}</div>
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:14px 18px;font-family:DM Sans;font-size:18px;color:#2a2016;line-height:1.4">
            A full team is 8 hires and a payroll. This is <span style="font-weight:800">one login</span>, billed in cents.</div>
        </div>
      </div>
      {cap("no empty box, no headcount. the ROUTER hires the agent, you hold the gate.","#8a745a")}</div>'''

PANELS={"orgtree":orgtree(),"gaps":gaps(),"research":research(),"outbound":outbound(),
        "deals":deals(),"marketing":marketing(),"legal":legal(),"coverage":coverage()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src39"; os.makedirs(outd,exist_ok=True)
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
