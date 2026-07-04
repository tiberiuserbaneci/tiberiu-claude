#!/usr/bin/env python3
# TIER 3 - PLAN VS SYSTEM (Claude Max 6-mo deal reframe), built to the WIRE-ITS-EYES bar: each panel
# a UNIQUE hand-built coded scene filling a clean rounded card, title + one-line caption, NO generic
# stat-chip strips, no cuts/walls. Warm palette only. Renders to models_clay/s2claudemaxcurrent/*.png
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

# 1. PLAN - split comparison: bigger plan = more chat bubbles (dim) vs system = output cards (lit)
def plan():
    chats=""
    for q in ["draft me an email","summarize this thread","what should I reply?","give me 3 ideas"]:
        chats+=(f'<div style="align-self:flex-start;max-width:88%;background:#242019;border:1px solid rgba(255,255,255,.07);'
          f'border-radius:16px 16px 16px 5px;padding:12px 16px;font-family:\'DM Sans\';font-size:16px;color:#8f8f85">{q}</div>')
    outs=[("240 emails","sent by SPECTER"),("18 briefs","built by CORTEX"),("PR #182","merged by SENTINEL"),("9 deals","scored by STRIKER")]
    cards=""
    for a,b in outs:
        cards+=(f'<div style="display:flex;align-items:center;gap:14px;background:linear-gradient(158deg,#3b352d,#251f1a);'
          f'border:1px solid rgba(212,162,127,.32);border-radius:14px;padding:12px 16px;box-shadow:0 12px 22px rgba(0,0,0,.4)">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M6 12.5l3.4 3.4L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<div style="text-align:left"><div style="font-family:\'DM Sans\';font-weight:900;font-size:20px;color:#FAFAF7;line-height:1">{a}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#c9a583">{b}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("More plan, or more done","PLAN vs SYSTEM")}
      <div style="display:flex;align-items:stretch;gap:0;height:470px">
        <div style="flex:1;display:flex;flex-direction:column;padding-right:34px">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:#7a746a;margin-bottom:16px">BIGGER PLAN</div>
          <div style="display:flex;flex-direction:column;gap:12px">{chats}</div>
          <div style="margin-top:auto;font-family:'DM Sans';font-weight:700;font-size:18px;color:#8f8f85">just more messages</div>
        </div>
        <div style="width:1px;background:linear-gradient(180deg,transparent,rgba(212,162,127,.5),transparent);position:relative">
          <div style="position:absolute;top:46%;left:50%;transform:translate(-50%,-50%);width:52px;height:52px;border-radius:50%;
            background:#201d19;border:1.5px solid rgb({ACC});display:flex;align-items:center;justify-content:center;
            font-family:'DM Sans';font-weight:900;font-size:17px;color:rgb({ACC})">VS</div></div>
        <div style="flex:1;display:flex;flex-direction:column;padding-left:34px">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:rgb({ACC});margin-bottom:16px">ULTRON SYSTEM</div>
          <div style="display:flex;flex-direction:column;gap:12px">{cards}</div>
          <div style="margin-top:auto;font-family:'DM Sans';font-weight:900;font-size:18px;color:#FAFAF7">shipped output</div>
        </div>
      </div>
      {cap("a plan gives you a bigger chat box. a system gives you finished work.")}</div>'''

# 2. METER - IVORY pay-per-token gauge: cost needle pinned near zero, cents readout, seat $ struck out
def meter():
    cx,cy,r=290,300,208
    frac=0.07
    def pt(rr,deg):
        a=math.radians(deg); return cx+rr*math.cos(a), cy-rr*math.sin(a)
    x0,y0=pt(r,180); x1,y1=pt(r,0)
    ang=180-frac*180
    vx,vy=pt(r,ang)
    nx,ny=pt(r-46,ang)
    ticks=""
    for d in range(0,181,30):
        a=math.radians(d); ix,iy=pt(r-14,d); ox,oy=pt(r,d)
        ticks+=f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="rgba(120,95,60,.4)" stroke-width="2"/>'
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      {htitle("You pay in cents, per run","PAY PER TOKEN","#2a2016")}
      <div style="display:flex;align-items:center;gap:20px">
        <svg width="580" height="330" viewBox="0 0 580 330">
          <defs><linearGradient id="mg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#96562d"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
          <path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 0 0 {x1:.1f} {y1:.1f}" fill="none" stroke="rgba(150,120,80,.22)" stroke-width="22" stroke-linecap="round"/>
          <path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 0 0 {vx:.1f} {vy:.1f}" fill="none" stroke="url(#mg)" stroke-width="22" stroke-linecap="round"/>
          {ticks}
          <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#96562d" stroke-width="7" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="16" fill="#96562d"/>
          <text x="{cx}" y="{cy-64}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="70" fill="#2a2016">0.11c</text>
          <text x="{cx}" y="{cy-30}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".14em" fill="#96562d">PER RUN</text>
        </svg>
        <div style="flex:1;text-align:left">
          <div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#2a2016;line-height:1.15">No seat.<br>No cap.</div>
          <div style="font-family:'DM Sans';font-size:17px;color:#5a4634;margin-top:10px;line-height:1.4">Only the runs you actually used.</div>
          <div style="display:inline-flex;align-items:center;gap:10px;margin-top:20px;background:rgba(200,70,35,.08);
            border:1px solid rgba(200,70,35,.28);border-radius:12px;padding:10px 14px">
            <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:rgb(200,70,35)">SEAT PLAN</span>
            <span style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#8a5a48;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.8)">$40/mo</span></div>
        </div>
      </div>
      {cap("cents per run, not a flat monthly seat you may never fill.","#8a745a")}</div>'''

# 3. OUTPUT - isometric stack of finished-work cards produced overnight
def output():
    rows=[("EMAILS","240 sent, 7 booked",0),("BRIEFS","18 accounts profiled",1),("CODE","PR #182 merged",2),("DEALS","9 scored, 3 hot",3)]
    cards=""
    for nm,sub,i in rows:
        y=i*104
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);'
          f'border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 22px;box-shadow:0 28px 42px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);'
          f'display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);'
          f'display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("It does not answer. It ships.","THE OUTPUT")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-8deg);width:560px;height:420px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:392px;background:rgb({ACC});color:#1a0f0a;font-family:'DM Sans';font-weight:900;
            font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">while you slept</div></div></div>
      {cap("a plan hands you replies. a system hands you a stack of done work.")}</div>'''

# 4. GRAPH - one chat splits into 7 named agents (bezier fan, left hub -> right nodes)
def graph():
    W,H=820,470
    agents=[("CORTEX","research",44),("SPECTER","outbound",108),("STRIKER","deals",172),
            ("PULSE","content",236),("SENTINEL","code",300),("AMPLIFY","publishing",364),("COUNSEL","legal",428)]
    hubx,huby=150,236; nx=520
    edges=""; nodes=""
    for nm,role,y in agents:
        mx=(hubx+nx)/2
        edges+=f'<path d="M{hubx+66} {huby} C{mx:.0f} {huby},{mx:.0f} {y},{nx-6} {y}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
        nodes+=(f'<rect x="{nx}" y="{y-26}" width="266" height="52" rx="13" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="{nx+28}" cy="{y}" r="7" fill="rgb({ACC})"/>'
          f'<text x="{nx+50}" y="{y-2}" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">{nm}</text>'
          f'<text x="{nx+50}" y="{y+15}" font-family="DM Mono" font-size="12" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One chat. Seven agents.","THE ROSTER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="ghub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ghg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {edges}
        <g filter="url(#ghg)"><circle cx="{hubx}" cy="{huby}" r="66" fill="url(#ghub)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
        <text x="{hubx}" y="{huby+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        {nodes}
      </svg>
      {cap("plain english in, the right specialist agent picks it up. not one bot doing everything.")}</div>'''

# 5. RADAR - live signal sweep, you first to see the round
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
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:#FAFAF7">You + Ultron</span><span style="font-family:\'DM Mono\';font-size:14px;color:rgb({ACC})">Tue 09:12</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:\'DM Sans\';font-size:17px;color:#8f8f85">Your VC</span><span style="font-family:\'DM Mono\';font-size:14px;color:#8f8f85">Fri 16:40</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:\'DM Sans\';font-weight:900;font-size:30px;color:rgb({ACC})">3 days ahead</div></div>')
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
        {cap("funding, hiring, stack, intent - watched overnight so you move first.")}
      </div></div>'''

# 6. GAUGE - IVORY dual dials: plan pinned at CAP (red maxed), system open with no redline
def gauge():
    def dial(label,val,maxed):
        r=78; circ=2*math.pi*r; span=0.75; dash=circ*span*val
        col="rgb(200,70,35)" if maxed else "#96562d"
        track=f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(150,120,80,.20)" stroke-width="16" stroke-linecap="round" stroke-dasharray="{circ*span:.0f} {circ:.0f}" transform="rotate(135 100 100)"/>'
        arc=f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="{col}" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(135 100 100)"/>'
        big='CAP' if maxed else '&#8734;'
        sub='maxed out' if maxed else 'no ceiling'
        bcol="rgb(200,70,35)" if maxed else "#2a2016"
        return (f'<div style="text-align:center"><div style="position:relative;width:200px;height:200px">'
          f'<svg width="200" height="200" viewBox="0 0 200 200">{track}{arc}</svg>'
          f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:{"38" if maxed else "52"}px;color:{bcol};line-height:1">{big}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#96562d;margin-top:2px">{sub}</span></div></div>'
          f'<div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.16em;color:#5a4634;margin-top:8px">{label}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      {htitle("A plan runs out. A system scales.","NO CEILING","#2a2016")}
      <div style="display:flex;align-items:center;justify-content:center;gap:70px;height:300px">
        {dial("SEAT PLAN",1.0,True)}
        <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#c9a583">&#8594;</div>
        {dial("PAY PER TOKEN",0.34,False)}
      </div>
      {cap("the seat caps your month. pay-per-token scales run by run, same cents each.","#8a745a")}</div>'''

# 7. FIELD - dot field of 10,000 runs, a handful lit (each dot = one run, cents each)
def field():
    cols,rowsn=50,20
    lit={137,402,631,888,712,455,60,999,540,321}
    dots=""; cell=13; gap=4
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="rgb({ACC})" filter="url(#flg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:38px 40px 36px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">10,000</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">runs this month</span></div>
        <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">CENTS EACH</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
        <defs><filter id="flg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("you pay for the runs that fired, nothing for a seat you half use.")}</div>'''

# 8. HUB - radial core: one memory feeding agents/eyes/voice/hands, gated by your tap
def hub():
    cx,cy=210,215
    spokes=[("AGENTS",-90),("EYES",-30),("VOICE",30),("HANDS",90),("MEMORY",150),("GATE",210)]
    lines=""; nodes=""
    for nm,a in spokes:
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        gate=(nm=="GATE")
        col="rgb(200,70,35)" if False else "rgba(212,162,127,.5)"
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="3"/>'
        ic=''
        if gate:
            ic=f'<g transform="translate({x-13:.0f},{y-14:.0f})"><rect x="0" y="10" width="26" height="19" rx="4" fill="none" stroke="rgb({ACC})" stroke-width="3"/><path d="M5 10 V6 a8 8 0 0 1 16 0 v4" fill="none" stroke="rgb({ACC})" stroke-width="3"/></g>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'{ic if gate else ""}'
          f'<text x="{x:.0f}" y="{y+(30 if gate else 5):.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="430" viewBox="0 0 420 430">
        <defs><radialGradient id="hcore" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hgl" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#hgl)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#hcore)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ONE</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">CORE</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("Not a plan. A system.","ONE CORE")}
        <div style="font-family:'DM Sans';font-size:19px;color:#c9c3b8;line-height:1.45">One memory feeds every agent. Eyes, voice and hands draw from it, and the gate holds every external move for your tap.</div>
        {cap("memory, agents and the gate, wired into one operator you own.")}</div></div>'''

PANELS={"plan":plan(),"meter":meter(),"output":output(),"graph":graph(),
        "radar":radar(),"gauge":gauge(),"field":field(),"hub":hub()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2claudemaxcurrent"; os.makedirs(outd,exist_ok=True)
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
