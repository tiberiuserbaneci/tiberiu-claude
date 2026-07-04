#!/usr/bin/env python3
# TIER 3 - QUESTIONS VS SYSTEMS, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None):
    tc=tagc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SPLIT - dual-column comparison: a dead-end ASK (question -> one answer -> chat ends) on the left,
# a lit running SYSTEM (looped pipeline that keeps going) on the right, a glowing VS divider between.
def split():
    def chip(txt,sub,muted=False,glow=False):
        bg="rgba(250,250,247,.03)" if muted else "linear-gradient(160deg,#403a33,#241f1a)"
        bd="rgba(250,250,247,.12)" if muted else f"rgb({ACC})"
        gl="box-shadow:0 0 22px rgba(212,162,127,.28);" if glow else ""
        tc="#8f8f85" if muted else "#FAFAF7"
        s=f'<div style="font-family:DM Sans;font-size:14px;color:#9a9488;margin-top:2px">{sub}</div>' if sub else ""
        return (f'<div style="background:{bg};border:1.5px solid {bd};border-radius:14px;padding:13px 16px;{gl}">'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:18px;color:{tc}">{txt}</div>{s}</div>')
    arrow='<div style="text-align:center;color:rgba(212,162,127,.55);font-size:20px;line-height:1;margin:4px 0">&#8595;</div>'
    left=(f'<div style="flex:1;display:flex;flex-direction:column">'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.18em;color:#8f8f85;margin-bottom:14px">ASK</div>'
      + chip('"what should I email them?"','you type the prompt',muted=True) + arrow
      + chip('one answer, one thread','copy it, paste it, done',muted=True) + arrow
      + '<div style="margin-top:8px;display:flex;align-items:center;gap:10px;font-family:DM Mono;font-size:13px;color:rgb(200,70,35)">'
        '<svg width="18" height="18" viewBox="0 0 24 24" stroke="rgb(200,70,35)" stroke-width="2.6" fill="none"><path d="M6 6l12 12M18 6L6 18"/></svg>the chat ends here</div>'
      + '</div>')
    steps=[("TRIGGER","a new account lands"),("WORK","agents run the job"),("CHECK","results scored"),("REPEAT","again, no prompt")]
    right_inner=""
    for i,(nm,sub) in enumerate(steps):
        right_inner+=(f'<div style="background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.5);border-radius:13px;padding:11px 15px;box-shadow:0 0 18px rgba(212,162,127,.22)">'
          f'<div style="display:flex;align-items:baseline;justify-content:space-between"><span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">{nm}</span></div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:16px;color:#FAFAF7">{sub}</div></div>')
        if i<len(steps)-1: right_inner+=arrow
    right=(f'<div style="flex:1;display:flex;flex-direction:column">'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.18em;color:rgb({ACC});margin-bottom:14px">SYSTEM</div>'
      + right_inner
      + '<div style="margin-top:8px;display:flex;align-items:center;gap:9px;font-family:DM Mono;font-size:13px;color:rgb(212,162,127)">'
        '<svg width="18" height="18" viewBox="0 0 24 24" stroke="rgb(212,162,127)" stroke-width="2.4" fill="none"><path d="M17 2l4 4-4 4"/><path d="M3 12v-2a4 4 0 0 1 4-4h14"/><path d="M7 22l-4-4 4-4"/><path d="M21 12v2a4 4 0 0 1-4 4H3"/></svg>loops without you</div>'
      + '</div>')
    div=('<div style="width:60px;display:flex;align-items:center;justify-content:center;position:relative">'
      '<div style="position:absolute;top:0;bottom:0;width:1px;background:linear-gradient(180deg,transparent,rgba(212,162,127,.4),transparent)"></div>'
      f'<div style="width:48px;height:48px;border-radius:50%;background:#211d19;border:1.5px solid rgb({ACC});display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:15px;color:rgb({ACC});box-shadow:0 0 24px rgba(212,162,127,.35)">VS</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Asking vs operating","ONE ANSWER / A JOB")}
      <div style="display:flex;align-items:stretch">{left}{div}{right}</div>
      {cap("a prompt gives one answer and stops. a system runs the whole job on its own.")}</div>'''

# 2. LOOP - IVORY: a clockwise cycle diagram, 4 stage nodes on the ring, arrowheads along the arc,
# a nightly clock at the centre. The system runs the loop while you are asleep.
def loop():
    cx,cy,R=306,232,152
    nodes=[("TRIGGER",-90),("WORK",0),("CHECK",90),("LOG",180)]
    nd=""
    for nm,a in nodes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        nd+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#fbf7ef" stroke="#d9c4a4" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="6"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="#5a4130">{nm}</text>')
    heads=""
    for a in (-45,45,135,225):
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a)); rot=a+90
        heads+=(f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot})">'
          f'<path d="M-9 -8 L9 0 L-9 8 Z" fill="#96562d"/></g>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;text-align:center">
      {htitle("It runs on a loop","SET ONCE","#2a2016","#96562d")}
      <svg width="612" height="464" viewBox="0 0 612 464" style="display:block;margin:0 auto">
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#c8a578" stroke-width="4" stroke-dasharray="2 14" stroke-linecap="round"/>
        {heads}
        <circle cx="{cx}" cy="{cy}" r="78" fill="#fdfbf6" stroke="#e2d3ba" stroke-width="2"/>
        <circle cx="{cx}" cy="{cy}" r="78" fill="none" stroke="rgba(150,90,45,.14)" stroke-width="8"/>
        <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-38}" stroke="#96562d" stroke-width="4" stroke-linecap="round"/>
        <line x1="{cx}" y1="{cy}" x2="{cx+26}" y2="{cy+8}" stroke="#96562d" stroke-width="4" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="6" fill="#96562d"/>
        <text x="{cx}" y="{cy+62}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#a08a68">RUNS NIGHTLY</text>
        {nd}
      </svg>
      {cap("trigger, work, check, repeat. nobody sits there retyping the prompt.","#8a745a")}</div>'''

# 3. ROSTER - IVORY node graph: one ROUTER hub feeding seven named agents (a team, not one chat).
def roster():
    hubx,huby=130,215
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    y0,step,cw,ch=18,58,338,48; cx0=352
    edges=""; chips=""
    for i,(nm,role) in enumerate(agents):
        cy=y0+i*step+ch/2
        edges+=f'<path d="M{hubx+56} {huby} C250 {huby},{cx0-40} {cy:.0f},{cx0} {cy:.0f}" fill="none" stroke="#c8a578" stroke-width="2.4"/>'
        chips+=(f'<g><rect x="{cx0}" y="{y0+i*step}" width="{cw}" height="{ch}" rx="14" fill="#fdfbf6" stroke="#e0cfb2" stroke-width="1.5"/>'
          f'<circle cx="{cx0+30}" cy="{cy:.0f}" r="6" fill="#96562d"/>'
          f'<text x="{cx0+52}" y="{cy-3:.0f}" font-family="DM Sans" font-weight="800" font-size="20" fill="#2a2016">{nm}</text>'
          f'<text x="{cx0+52}" y="{cy+16:.0f}" font-family="DM Sans" font-size="14" fill="#8a745a">{role}</text></g>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("A roster, not a chatbot","7 AGENTS","#2a2016","#96562d")}
      <svg width="712" height="440" viewBox="0 0 712 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="rhub" cx="36%" cy="30%"><stop offset="0%" stop-color="#c89a6e"/><stop offset="100%" stop-color="#96562d"/></radialGradient></defs>
        {edges}
        <circle cx="{hubx}" cy="{huby}" r="56" fill="url(#rhub)"/>
        <circle cx="{hubx}" cy="{huby}" r="56" fill="none" stroke="rgba(255,255,255,.5)" stroke-width="1.5"/>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#fdfbf6">ROUTER</text>
        <text x="{hubx}" y="{huby+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#f2e3cf">routes work</text>
        {chips}
      </svg>
      {cap("one chat is one worker. this routes each job to the agent that owns it.","#8a745a")}</div>'''

# 4. RADAR - dark radar sweep of live signals, ranked, with a first-to-see readout beside it.
def radar():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Stack",210,168),("Intent",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    read="".join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:14px"><span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba(212,162,127,.7)"></span><span style="font-family:DM Sans;font-size:18px;color:#d9d5cc">{nm} moved</span></div>' for nm,_,_ in blips)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("Watched, not queried","OVERNIGHT")}
        {read}
        {cap("funding, hiring, stack, intent - tracked on triggers while you were logged off.")}
      </div></div>'''

# 5. STACK - dark isometric stack of finished outputs waiting when you wake (done overnight).
def stack():
    rows=[("Account brief","12 sources, ranked","READY"),
          ("Follow-up sequence","4 emails drafted","READY"),
          ("Landing page fix","tested, shipped","LIVE")]
    cards=""
    for i,(a,b,tag) in enumerate(rows):
        y=i*138
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;padding:20px 24px;box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:23px;color:#FAFAF7">{a}</div><div style="font-family:DM Sans;font-size:15px;color:#a8a296;margin-top:2px">{b}</div></div>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:8px;padding:5px 10px">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("You wake to results","DONE OVERNIGHT")}
      <div style="perspective:2000px;height:490px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-9deg);width:580px;height:436px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:412px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">3 jobs finished &#10003;</div></div></div>
      {cap("briefs, drafts and fixes stacked and ready - not a blank cursor.")}</div>'''

# 6. FIELD - dark dot field: one prompt = one answer, one system = thousands of runs, cents each.
def field():
    cols,rowsn=46,17
    lit={41,133,220,318,405,512,640,733,829}
    cell=13; gap=3
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgba(212,162,127,.16)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    hdr=('<div style="display:flex;align-items:stretch;gap:16px;margin-bottom:18px">'
      '<div style="flex:0 0 auto;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.16);border-radius:14px;padding:12px 20px">'
      '<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#8f8f85">1</div>'
      '<div style="font-family:DM Mono;font-size:12px;color:#7a7468">prompt = 1 answer</div></div>'
      f'<div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:14px;padding:12px 20px;box-shadow:0 0 22px rgba(212,162,127,.22)">'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7">4,000</div>'
      f'<div style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">runs = 1 system, today</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One ask, or one system","SCALE")}
      {hdr}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("a prompt scales to how fast you type. a system scales to cents per thousand runs.")}</div>'''

# 7. GATE - dark semicircular gauge: autonomy pinned full, but a lock at the hub holds every send.
def gate():
    cx,cy,R=310,300,208
    def pt(a): return (cx+R*math.cos(math.radians(a)), cy+R*math.sin(math.radians(a)))
    x0,y0=pt(180); x1,y1=pt(0)
    ticks=""
    for a in range(180,-1,-18):
        ix,iy=cx+(R-16)*math.cos(math.radians(a)),cy+(R-16)*math.sin(math.radians(a))
        ox,oy=cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))
        ticks+=f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="3"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;text-align:center">
      {htitle("Full power, on your reins","HUMAN GATE")}
      <svg width="620" height="360" viewBox="0 0 620 360" style="display:block;margin:0 auto">
        <defs><filter id="gg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="#2a2724" stroke-width="26" stroke-linecap="round"/>
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="14" stroke-linecap="round" filter="url(#gg2)"/>
        {ticks}
        <text x="{x0+8:.0f}" y="{y0+30:.0f}" text-anchor="start" font-family="DM Mono" font-size="14" fill="#8f8f85">runs</text>
        <text x="{x1-8:.0f}" y="{y1+30:.0f}" text-anchor="end" font-family="DM Mono" font-size="14" fill="#8f8f85">sends</text>
        <text x="{cx}" y="150" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">AUTONOMY 100%</text>
        <g transform="translate({cx-42},188)">
          <rect x="0" y="34" width="84" height="60" rx="13" fill="#211d19" stroke="rgb({ACC})" stroke-width="5"/>
          <path d="M16 34 V19 a26 26 0 0 1 52 0 v15" fill="none" stroke="rgb({ACC})" stroke-width="5"/>
          <circle cx="42" cy="64" r="7" fill="rgb({ACC})"/></g>
      </svg>
      <div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7;margin-top:2px">every external move waits for your tap</div>
      {cap("it runs the whole job without you, then parks the send for your one tap.")}</div>'''

# 8. OPERATOR - dark radial hub-and-spokes: functions orbit one glowing OPERATOR core (one system).
def operator():
    cx,cy=410,215; R=168
    spokes=[("research",-90),("outbound",-30),("close",30),("code",90),("content",150),("watch",210)]
    sp=""
    for nm,a in spokes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        sp+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#221f1b" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="none" stroke="rgba(212,162,127,.25)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Start running one","ONE SYSTEM")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="core8" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg8" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {sp}
        <g filter="url(#cg8)"><circle cx="{cx}" cy="{cy}" r="78" fill="url(#core8)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a160c">OPERATOR</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one login</text>
      </svg>
      {cap("research, outbound, content and code composed into one system you operate.")}</div>'''

PANELS={"split":split(),"loop":loop(),"roster":roster(),"radar":radar(),
        "stack":stack(),"field":field(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2mostpeopleare"; os.makedirs(outd,exist_ok=True)
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
