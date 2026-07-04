#!/usr/bin/env python3
# TIER 3 - AGENTS THAT LEARN, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. AMNESIA - timeline sawtooth: memory climbs inside a run, then crashes to zero at every boundary
def amnesia():
    W,H=760,410; runs=6; x0=64; rw=112; base=320; peak=150
    segs=""; drops=""; labels=""
    for i in range(runs):
        xa=x0+i*rw; xb=xa+rw-20
        segs+=f'<path d="M{xa} {base} L{xb} {peak}" stroke="rgb({ACC})" stroke-width="4" fill="none" stroke-linecap="round"/>'
        segs+=f'<circle cx="{xb}" cy="{peak}" r="6" fill="rgb({ACC})"/>'
        drops+=f'<line x1="{xb}" y1="{peak}" x2="{xb}" y2="{base}" stroke="rgb({BAD})" stroke-width="3" stroke-dasharray="4 6"/>'
        labels+=f'<text x="{(xa+xb)/2:.0f}" y="{base+30}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">RUN {i+1}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Memory resets every run","AMNESIA")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <line x1="{x0-14}" y1="{peak}" x2="{W-30}" y2="{peak}" stroke="rgba(212,162,127,.20)" stroke-dasharray="2 8"/>
        <text x="{W-30}" y="{peak-8}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#7a746a">learned this run</text>
        <line x1="{x0-14}" y1="{base}" x2="{W-30}" y2="{base}" stroke="rgba(255,255,255,.12)"/>
        <text x="{x0-16}" y="{base+5}" text-anchor="end" font-family="DM Mono" font-size="12" fill="rgb({BAD})">0</text>
        {segs}{drops}{labels}
        <text x="{x0-16}" y="{peak+6}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#7a746a" transform="rotate(-90 {x0-40} {(peak+base)//2})">MEMORY</text>
        <g transform="translate({W-236},{H-58})">
          <rect x="0" y="0" width="216" height="42" rx="12" fill="rgba(200,70,35,.10)" stroke="rgba(200,70,35,.4)"/>
          <text x="18" y="27" font-family="DM Mono" font-size="14" fill="rgb({BAD})">asked "refund window?" x6</text>
        </g>
      </svg>
      {cap("a task finishes, the context dies, tomorrow starts from zero. that is most agents today.")}</div>'''

# 2. TAX - isometric stack: the SAME fix filed 41 times, a payroll of repeated corrections
def tax():
    cards=""
    for i in range(5):
        n=37+i; y=i*92
        top=(i==4)
        bd="rgb("+ACC+")" if top else "rgba(255,255,255,.14)"
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid {bd};border-radius:16px;padding:16px 22px;box-shadow:0 28px 42px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(200,70,35,.14);border:1px solid rgba(200,70,35,.4);display:flex;align-items:center;justify-content:center;font-family:DM Mono;font-size:15px;color:rgb({BAD})">#{n}</div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">CORRECTION</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">remove the "10% off" line</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The correction you keep paying","REPEAT TAX")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:440px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:410px;background:rgb({BAD});color:#fff;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(200,70,35,.4)">same fix x41</div></div></div>
      {cap("every repeated correction is payroll you pay in attention.")}</div>'''

# 3. LOOPLEARN - IVORY feedback loop: Evaluate -> Reflect -> Store -> Apply, ringed with arrows
def looplearn():
    cx,cy,R=310,250,142; nr=48
    steps=[("1","EVALUATE","grades output",-90,"below"),
           ("2","REFLECT","finds the miss",0,"right"),
           ("3","STORE","writes the lesson",90,"below"),
           ("4","APPLY","uses next run",180,"left")]
    nodes=""
    for num,name,sub,a,side in steps:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{nr}" fill="#fbf7ef" stroke="#96562d" stroke-width="3"/>'
          f'<text x="{x:.0f}" y="{y+9:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#96562d">{num}</text>')
        if side=="right":
            lx=x+nr+16; anc="start"; ly=y-4
        elif side=="left":
            lx=x-nr-16; anc="end"; ly=y-4
        elif a==-90:
            lx=x; anc="middle"; ly=y-nr-30
        else:
            lx=x; anc="middle"; ly=y+nr+34
        nodes+=(f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="{anc}" font-family="DM Sans" font-weight="800" font-size="19" fill="#2a2016">{name}</text>'
          f'<text x="{lx:.0f}" y="{ly+21:.0f}" text-anchor="{anc}" font-family="DM Mono" font-size="13" fill="#8a745a">{sub}</text>')
    arcs=""
    for a1,a2 in ((-90,0),(0,90),(90,180),(180,270)):
        s=a1+24; e=a2-24
        sx=cx+R*math.cos(math.radians(s)); sy=cy+R*math.sin(math.radians(s))
        ex=cx+R*math.cos(math.radians(e)); ey=cy+R*math.sin(math.radians(e))
        arcs+=f'<path d="M{sx:.0f} {sy:.0f} A {R} {R} 0 0 1 {ex:.0f} {ey:.0f}" fill="none" stroke="#96562d" stroke-width="3.5"/>'
        tdir=math.atan2(math.cos(math.radians(e)),-math.sin(math.radians(e)))
        b1=tdir+math.radians(150); b2=tdir-math.radians(150); Lh=15
        p1=(ex+Lh*math.cos(b1),ey+Lh*math.sin(b1)); p2=(ex+Lh*math.cos(b2),ey+Lh*math.sin(b2))
        arcs+=f'<path d="M{p1[0]:.0f} {p1[1]:.0f} L{ex:.0f} {ey:.0f} L{p2[0]:.0f} {p2[1]:.0f}" fill="none" stroke="#96562d" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("The self-improving loop","EVAL TO APPLY")}
      <svg width="620" height="500" viewBox="0 0 620 500" style="display:block;margin:0 auto">
        {arcs}{nodes}
        <circle cx="{cx}" cy="{cy}" r="52" fill="#96562d"/>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#fbf7ef">LESSON</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgba(251,247,239,.75)">filed</text>
      </svg>
      {cap("the agent grades its output, writes the lesson, uses it next run.","#8a745a")}</div>'''

# 4. FILE - node graph: a raw correction is promoted to a rule, rules compose into a durable skill
def filegraph():
    W,H=780,430
    corr=[("no discounts",70),("subject under 6 words",190),("drop 'circle back'",310)]
    rules=[("pricing: hold firm",120),("copy: tighten",260)]
    cx1,cx2,cx3=40,300,560
    edges=""
    epairs=[(70,120),(190,260),(310,260)]
    for cy,ry in epairs:
        mx=(cx1+150+cx2)/2
        edges+=f'<path d="M{cx1+186} {cy} C{mx:.0f} {cy},{mx:.0f} {ry},{cx2} {ry}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
    for ry in (120,260):
        mx=(cx2+160+cx3)/2
        edges+=f'<path d="M{cx2+160} {ry} C{mx:.0f} {ry},{mx:.0f} 190,{cx3} 190" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="3"/>'
    cnodes=""
    for nm,y in corr:
        cnodes+=(f'<rect x="{cx1}" y="{y-28}" width="186" height="56" rx="14" fill="#221f1b" stroke="rgba(200,70,35,.35)"/>'
          f'<line x1="{cx1+18}" y1="{y-9}" x2="{cx1+30}" y2="{y+3}" stroke="rgb({BAD})" stroke-width="2.4"/><line x1="{cx1+30}" y1="{y-9}" x2="{cx1+18}" y2="{y+3}" stroke="rgb({BAD})" stroke-width="2.4"/>'
          f'<text x="{cx1+44}" y="{y+5}" font-family="DM Sans" font-size="15" fill="#d3cdc1">{nm}</text>')
    rnodes=""
    for nm,y in rules:
        rnodes+=(f'<rect x="{cx2}" y="{y-30}" width="160" height="60" rx="15" fill="#2f2a24" stroke="rgba(212,162,127,.5)" stroke-width="1.5"/>'
          f'<text x="{cx2+80}" y="{y-4}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="rgb({ACC})">RULE</text>'
          f'<text x="{cx2+80}" y="{y+16}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#FAFAF7">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One fix, then it generalizes","PROMOTED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="skill" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <text x="{cx1+93}" y="26" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="#7a746a">CORRECTIONS</text>
        <text x="{cx2+80}" y="26" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="#7a746a">RULES</text>
        <text x="{cx3+66}" y="26" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="#7a746a">SKILL</text>
        {edges}{cnodes}{rnodes}
        <g filter="url(#sg)"><circle cx="{cx3+66}" cy="190" r="82" fill="url(#skill)"/></g>
        <text x="{cx3+66}" y="184" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">SPECTER</text>
        <text x="{cx3+66}" y="208" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">your outbound</text>
      </svg>
      {cap("say no discounts once: blocked forever. fix a draft once: the fix generalizes.")}</div>'''

# 5. CURVE - IVORY compounding curve: match-to-you climbs from run 1 (average) to run 100 (yours)
def curve():
    W,H=760,410; x0=74; x1=706; yb=330; yt=96
    def val(t): return 0.61+0.37*(1-math.exp(-3.4*t))
    def X(t): return x0+(x1-x0)*t
    def Y(t): return yb-(yb-yt)*((val(t)-0.61)/0.37)
    pts=[(X(k/100),Y(k/100)) for k in range(0,101,4)]
    line="M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)
    area=f"M{x0} {yb} L"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)+f" L{x1} {yb} Z"
    grid=""
    for k,lab in ((25,"25"),(50,"50"),(75,"75")):
        gx=X(k/100)
        grid+=f'<line x1="{gx:.0f}" y1="{yt}" x2="{gx:.0f}" y2="{yb}" stroke="rgba(150,90,45,.14)"/><text x="{gx:.0f}" y="{yb+26}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a08a68">{lab}</text>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("It compounds into you","RUN 1 TO 100")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(150,86,45,.28)"/><stop offset="100%" stop-color="rgba(150,86,45,0)"/></linearGradient></defs>
        <line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="rgba(120,80,40,.35)"/>
        <line x1="{x0}" y1="{yt}" x2="{x0}" y2="{yb}" stroke="rgba(120,80,40,.35)"/>
        {grid}
        <path d="{area}" fill="url(#ar)"/>
        <path d="{line}" fill="none" stroke="#96562d" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="{X(0):.0f}" cy="{Y(0):.0f}" r="8" fill="#b08a5a"/>
        <text x="{X(0)+14:.0f}" y="{Y(0)+2:.0f}" font-family="DM Sans" font-weight="700" font-size="15" fill="#5a4634">run 1 . average 61%</text>
        <circle cx="{X(1):.0f}" cy="{Y(1):.0f}" r="10" fill="#96562d"/>
        <text x="{X(1)-8:.0f}" y="{Y(1)-18:.0f}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a2016">run 100 . you 97%</text>
        <text x="{x1}" y="{yb+26}" text-anchor="end" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#a08a68">RUNS</text>
      </svg>
      {cap("the same flow, months later, writes like you, prices like you, filters like you.","#8a745a")}</div>'''

# 6. PROOF - dot field: a 34-rule no-list, each rule written exactly once
def proof():
    real=["no discounts, ever","subject 6 words max","kill 'just checking in'","name the trigger","cents, not dollars","cite the source"]
    chips=""
    for r in real:
        chips+=(f'<div style="display:flex;align-items:center;gap:9px;background:rgba(212,162,127,.13);border:1px solid rgba(212,162,127,.4);border-radius:12px;padding:11px 15px">'
          f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:16px;color:#eae4d8">{r}</span></div>')
    for i in range(28):
        chips+=(f'<div style="width:46px;height:46px;border-radius:11px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.3);display:flex;align-items:center;justify-content:center;font-family:DM Mono;font-size:12px;color:rgba(212,162,127,.75)">{i+7:02d}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:56px;color:#FAFAF7">34</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:12px">rules on the no-list</span></div>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">0 REPEATS</span></div>
      <div style="display:flex;flex-wrap:wrap;gap:12px;align-content:flex-start;min-height:300px">{chips}</div>
      {cap("each one came from a single correction that never needed repeating.")}</div>'''

# 7. GATE - memory core (self-loops internally) held behind a lock: it sends only on your tap
def gate():
    cx,cy=210,220
    ring="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,{o})" stroke-width="2"/>' for r,o in ((118,.18),(94,.26),(68,.4)))
    # internal self-loop arrow around the core
    lr=136
    def P(a): return (cx+lr*math.cos(math.radians(a)),cy+lr*math.sin(math.radians(a)))
    sx,sy=P(-40); ex,ey=P(240)
    tdir=math.atan2(math.cos(math.radians(240)),-math.sin(math.radians(240)))
    b1=tdir+math.radians(150); b2=tdir-math.radians(150)
    ap1=(ex+16*math.cos(b1),ey+16*math.sin(b1)); ap2=(ex+16*math.cos(b2),ey+16*math.sin(b2))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Learns alone, sends with you","GATED")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-90%" y="-90%" width="280%" height="280%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <path d="M{sx:.0f} {sy:.0f} A {lr} {lr} 0 1 1 {ex:.0f} {ey:.0f}" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="3" stroke-dasharray="6 7"/>
        <path d="M{ap1[0]:.0f} {ap1[1]:.0f} L{ex:.0f} {ey:.0f} L{ap2[0]:.0f} {ap2[1]:.0f}" fill="none" stroke="rgba(212,162,127,.7)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        {ring}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">LEARNS</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">internal</text>
        <text x="{cx}" y="{cy+lr+52}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#8f8f85">MEMORY CORE</text>
        <path d="M400 220 H556" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="410" y="196" width="120" height="48" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.12)"/>
        <text x="470" y="225" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#d3cdc1">SEND</text>
        <rect x="600" y="146" width="150" height="150" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(647,186)"><rect x="0" y="36" width="58" height="44" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M11 36 V22 a18 18 0 0 1 36 0 v14" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="675" y="330" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("self-improvement stays internal; every external move parks for your tap.")}</div>'''

# 8. QUESTION - twin gauges: training pinned at full, memory pinned at zero
def question():
    def gauge(gcx,gcy,rr,v,fill,valtxt,valcol,lab):
        track=f'<path d="M{gcx-rr} {gcy} A {rr} {rr} 0 0 1 {gcx+rr} {gcy}" fill="none" stroke="rgba(255,255,255,.10)" stroke-width="20" stroke-linecap="round"/>'
        te=180-v*180
        ex=gcx+rr*math.cos(math.radians(te)); ey=gcy-rr*math.sin(math.radians(te))
        filled=""
        if v>0.01:
            large=0
            filled=f'<path d="M{gcx-rr} {gcy} A {rr} {rr} 0 {large} 1 {ex:.1f} {ey:.1f}" fill="none" stroke="{fill}" stroke-width="20" stroke-linecap="round"/>'
        nx=gcx+(rr-26)*math.cos(math.radians(te)); ny=gcy-(rr-26)*math.sin(math.radians(te))
        needle=f'<line x1="{gcx}" y1="{gcy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{fill}" stroke-width="6" stroke-linecap="round"/><circle cx="{gcx}" cy="{gcy}" r="12" fill="{fill}"/>'
        return (track+filled+needle+
          f'<text x="{gcx}" y="{gcy-30}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="46" fill="{valcol}">{valtxt}</text>'
          f'<text x="{gcx}" y="{gcy+40}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".12em" fill="#9a9488">{lab}</text>')
    g1=gauge(220,300,150,1.0,f"rgb({ACC})","100%",f"rgb({ACC})","TRAINED DAILY")
    g2=gauge(600,300,150,0.0,f"rgb({BAD})","0%",f"rgb({BAD})","REMEMBERED")
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Trained daily, remembers nothing","THE ASK")}
      <svg width="820" height="380" viewBox="0 0 820 380" style="display:block;margin:0 auto">
        {g1}{g2}
        <text x="410" y="300" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="rgba(255,255,255,.18)">vs</text>
      </svg>
      {cap("demand memory before you demand intelligence.")}</div>'''

PANELS={"amnesia7":amnesia(),"tax":tax(),"looplearn":looplearn(),"file7":filegraph(),
        "curve7":curve(),"proof7":proof(),"gate7":gate(),"question7":question()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/selflearn"; os.makedirs(outd,exist_ok=True)
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
