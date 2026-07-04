#!/usr/bin/env python3
# TIER 3 - THE ONE-LAPTOP COMPANY: each panel a UNIQUE hand-built coded scene filling a clean
# rounded card, title + one-line caption, NO generic stat-chip strips. Reframes the source
# "70 AI business ideas this weekend" into one Ultron operator running the whole company at cents.
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
def htitleiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SEVENTY - node graph: 70 dim idea nodes funnel through faint edges into ONE lit operator hub
def seventy():
    hubx,huby=690,232
    dots=""; edges=""
    for i in range(70):
        r,c=divmod(i,10)
        x=44+c*40+12*math.sin(i*1.7); y=34+r*62+8*math.cos(i*2.3)
        edges+=f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{hubx-72}" y2="{huby}" stroke="rgba(212,162,127,.07)" stroke-width="1"/>'
        dots+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="rgba(250,250,247,.15)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seventy ideas, one engine","THE FUNNEL")}
      <svg width="820" height="466" viewBox="0 0 820 466" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub1" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg1" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{dots}
        <g filter="url(#hg1)"><circle cx="{hubx}" cy="{huby}" r="80" fill="url(#hub1)"/></g>
        <text x="{hubx}" y="{huby-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="46" fill="#2a160c">1</text>
        <text x="{hubx}" y="{huby+26}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#3a2010">OPERATOR</text>
      </svg>
      {cap("you do not pick from a list. one operator runs the one you pick.")}</div>'''

# 2. LAPTOP - laptop-as-company: one screen, five departments fanned out and wired
def laptop():
    depts=[("RESEARCH","CORTEX"),("OUTREACH","SPECTER"),("CONTENT","PULSE"),("DEALS","STRIKER"),("DELIVERY","SENTINEL")]
    chips=""; conns=""
    sx=320; sy=222
    for i,(nm,ag) in enumerate(depts):
        cy=52+i*82
        conns+=f'<path d="M{sx} {sy} C400 {sy},430 {cy+22},468 {cy+22}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        chips+=(f'<div style="position:absolute;left:468px;top:{cy}px;width:344px;background:linear-gradient(160deg,#33302c,#211e1a);border:1px solid rgba(255,255,255,.1);border-radius:15px;padding:12px 18px;box-shadow:0 12px 22px rgba(0,0,0,.45);display:flex;align-items:center;justify-content:space-between">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7;letter-spacing:.02em">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">{ag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The whole company, one screen","FIVE DEPARTMENTS")}
      <div style="position:relative;height:466px">
        <svg width="820" height="466" viewBox="0 0 820 466" style="position:absolute;left:0;top:0">
          <defs><linearGradient id="scr" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1b1916"/></linearGradient>
          <radialGradient id="orb2" cx="38%" cy="32%"><stop offset="0%" stop-color="#8fd0ff"/><stop offset="46%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient></defs>
          {conns}
          <rect x="62" y="118" width="258" height="168" rx="14" fill="url(#scr)" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>
          <rect x="78" y="134" width="226" height="136" rx="8" fill="#141210"/>
          <circle cx="191" cy="190" r="34" fill="url(#orb2)"/>
          <text x="191" y="244" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" letter-spacing=".14em" fill="#e6d6c2">ULTRON</text>
          <path d="M44 316 L338 316 L308 286 L74 286 Z" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>
          <rect x="150" y="296" width="82" height="7" rx="3.5" fill="rgba(255,255,255,.14)"/>
        </svg>
        {chips}
      </div>
      {cap("research, outreach, content, deals, delivery. no hires, no office.")}</div>'''

# 3. WEEKEND - IVORY timeline: friday night to a running company, milestone cards on one track
def weekend():
    steps=[("FRI 8PM","Wire up Ultron",False),("SAT AM","Research + list built",False),
           ("SAT PM","Outreach sent",False),("SUN","First replies land",False),("MON","Company running",True)]
    n=len(steps); cw=148; x0=48; x1=772; y=214; step=(x1-x0-cw)//(n-1)
    line=f'<line x1="{x0+cw//2}" y1="{y}" x2="{x0+cw//2+step*(n-1)}" y2="{y}" stroke="rgba(150,90,45,.25)" stroke-width="3"/>'
    line+=f'<line x1="{x0+cw//2}" y1="{y}" x2="{x0+cw//2+step*(n-1)}" y2="{y}" stroke="#96562d" stroke-width="3"/>'
    marks=""
    for i,(t,d,fin) in enumerate(steps):
        cx=x0+i*step+cw//2; above=(i%2==0); cardy=(y-116) if above else (y+40)
        col="#96562d" if fin else "#b9793f"
        stem_y1=cardy+76 if above else cardy; stem_y2=y-13 if above else y+13
        marks+=f'<line x1="{cx}" y1="{stem_y1}" x2="{cx}" y2="{stem_y2}" stroke="rgba(150,90,45,.4)" stroke-width="1.5"/>'
        bd="#96562d" if fin else "rgba(150,90,45,.28)"
        marks+=(f'<rect x="{cx-cw//2}" y="{cardy}" width="{cw}" height="76" rx="14" fill="rgba(255,255,255,.55)" stroke="{bd}" stroke-width="{2 if fin else 1.3}"/>'
          f'<text x="{cx}" y="{cardy+30}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="#96562d">{t}</text>'
          f'<text x="{cx}" y="{cardy+56}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#2a2016">{d}</text>')
        if fin: marks+=f'<circle cx="{cx}" cy="{y}" r="24" fill="none" stroke="rgba(150,86,45,.4)" stroke-width="2"/>'
        marks+=f'<circle cx="{cx}" cy="{y}" r="{13 if fin else 10}" fill="{col}" stroke="#fdfbf6" stroke-width="3"/>'
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitleiv("Friday night to a company","48 HOURS")}
      <svg width="820" height="416" viewBox="0 0 820 416" style="display:block;margin:10px auto 0">
        {line}{marks}
      </svg>
      {cap("set it up over a weekend. by sunday it is already working the pipeline.","#8a745a")}</div>'''

# 4. ROSTER - org chart: the operator on top, the agent team wired below
def roster():
    agents=[("CORTEX","research"),("SPECTER","outreach"),("PULSE","content"),("STRIKER","deals"),("AMPLIFY","publish")]
    n=len(agents); bw=138; gap=(820-n*bw)//(n-1); topcx=410
    boxes=""; edges=""
    for i,(nm,role) in enumerate(agents):
        x=i*(bw+gap); cx=x+bw//2; by=250
        edges+=f'<path d="M{topcx} 118 C{topcx} 190,{cx} 176,{cx} {by-6}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        boxes+=(f'<g><rect x="{x}" y="{by}" width="{bw}" height="118" rx="16" fill="#241f1b" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<circle cx="{cx}" cy="{by+38}" r="15" fill="rgba(212,162,127,.14)" stroke="rgba(212,162,127,.4)"/>'
          f'<circle cx="{cx}" cy="{by+38}" r="5" fill="rgb({ACC})"/>'
          f'<text x="{cx}" y="{by+78}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#FAFAF7">{nm}</text>'
          f'<text x="{cx}" y="{by+100}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#8f8f85">{role}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Your team, already named","THE ROSTER")}
      <svg width="820" height="410" viewBox="0 0 820 410" style="display:block;margin:0 auto">
        <defs><radialGradient id="op4" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og4" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {edges}
        <g filter="url(#og4)"><rect x="{topcx-96}" y="26" width="192" height="92" rx="20" fill="#211e1a" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <text x="{topcx}" y="66" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">YOU</text>
        <text x="{topcx}" y="92" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="rgb({ACC})">THE OPERATOR</text>
        {boxes}
      </svg>
      {cap("cortex researches, specter writes, striker closes, pulse posts.")}</div>'''

# 5. CENTS - isometric stack of salary cards (the headcount a founder would hire) vs a cents chip
def cents():
    hires=[("Researcher","$4,200"),("SDR / outbound","$3,800"),("Content writer","$3,500"),("Closer","$5,000")]
    cards=""
    for i,(nm,cost) in enumerate(hires):
        y=i*90
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:430px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.13);border-radius:16px;padding:14px 22px;box-shadow:0 24px 36px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;justify-content:space-between">'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#e6e0d5">{nm}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb(200,70,35)">{cost}<span style="font-size:13px;color:#9a9488">/mo</span></span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <div style="flex:1">
        {htitle("A team is salaries.","THE COST")}
        <div style="perspective:1700px;height:430px;display:flex;align-items:center;justify-content:center">
          <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-9deg);width:430px;height:400px;position:relative">{cards}
            <div style="position:absolute;left:118px;top:378px;background:rgb(200,70,35);color:#fff;font-family:DM Sans;font-weight:900;font-size:17px;padding:9px 22px;border-radius:999px;box-shadow:0 12px 24px rgba(200,70,35,.45)">$16,500 / mo total</div></div></div>
      </div>
      <div style="flex-shrink:0;width:250px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;
        background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:24px;padding:34px 20px;box-shadow:0 30px 50px rgba(0,0,0,.5), 0 0 40px rgba(212,162,127,.18)">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:rgb({ACC})">ULTRON</span>
        <span style="font-family:DM Sans;font-weight:900;font-size:60px;color:#FAFAF7;line-height:1">11c</span>
        <span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#c9a583">per run</span>
        <div style="font-family:DM Mono;font-size:12px;color:#8f8f85;margin-top:8px;text-align:center;line-height:1.5">pay per token,<br>not per hire</div>
      </div>
    </div>'''

# 6. REVENUE - IVORY climbing revenue curve: first reply, first call, first deal, MRR
def revenue():
    pts=[(120,282,"1st reply","SAT"),(288,214,"1st call","SUN"),(452,142,"1st deal","WK 1"),(628,72,"MRR","WK 2")]
    ax_x0,ax_x1,ax_y=90,690,300
    poly=" ".join(f"{x},{y}" for x,y,_,_ in pts)
    area=f'M {pts[0][0]},{ax_y} L '+" L ".join(f"{x},{y}" for x,y,_,_ in pts)+f' L {pts[-1][0]},{ax_y} Z'
    grid="".join(f'<line x1="{ax_x0}" y1="{gy}" x2="{ax_x1}" y2="{gy}" stroke="rgba(150,90,45,.14)" stroke-width="1"/>' for gy in (90,160,230,300))
    nodes=""
    for x,y,lab,wk in pts:
        nodes+=(f'<circle cx="{x}" cy="{y}" r="8" fill="#96562d" stroke="#fdfbf6" stroke-width="3"/>'
          f'<text x="{x}" y="{y-18}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#2a2016">{lab}</text>'
          f'<text x="{x}" y="{ax_y+26}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#96562d">{wk}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitleiv("Real money, not a demo","WEEK ONE")}
      <svg width="760" height="360" viewBox="0 0 760 360" style="display:block;margin:6px auto 0">
        <defs><linearGradient id="rev" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(150,86,45,.34)"/><stop offset="100%" stop-color="rgba(150,86,45,0)"/></linearGradient></defs>
        {grid}
        <line x1="{ax_x0}" y1="{ax_y}" x2="{ax_x1}" y2="{ax_y}" stroke="rgba(120,80,40,.4)" stroke-width="2"/>
        <path d="{area}" fill="url(#rev)"/>
        <polyline points="{poly}" fill="none" stroke="#96562d" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        {nodes}
      </svg>
      {cap("first outreach saturday, first reply sunday, first deal the week after.","#8a745a")}</div>'''

# 7. GATE - HUMAN GATE gauge: the needle held on YOUR TAP, actions queued left, sent right
def gate():
    cx,cy,R=410,320,196
    ticks=""
    for a in range(0,181,15):
        rad=math.radians(180-a)
        x1=cx+(R-4)*math.cos(rad); y1=cy-(R-4)*math.sin(rad)
        x2=cx+(R-26)*math.cos(rad); y2=cy-(R-26)*math.sin(rad)
        maj=(a%45==0)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,{0.7 if maj else 0.3})" stroke-width="{3 if maj else 1.5}"/>'
    needrad=math.radians(90); nx=cx+(R-40)*math.cos(needrad); ny=cy-(R-40)*math.sin(needrad)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("It moves only on your tap","HUMAN GATE")}
      <svg width="820" height="392" viewBox="0 0 820 392" style="display:block;margin:0 auto">
        <defs><linearGradient id="arc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8f8f85"/><stop offset="50%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#c9a583"/></linearGradient>
        <filter id="ng" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(255,255,255,.06)" stroke-width="30"/>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="url(#arc)" stroke-width="12" stroke-linecap="round" opacity="0.85"/>
        {ticks}
        <text x="{cx-R+8}" y="{cy+34}" text-anchor="start" font-family="DM Mono" font-size="14" fill="#9a9488">queued</text>
        <text x="{cx+R-8}" y="{cy+34}" text-anchor="end" font-family="DM Mono" font-size="14" fill="#c9a583">sent</text>
        <g filter="url(#ng)"><line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round"/></g>
        <circle cx="{cx}" cy="{cy}" r="20" fill="#211e1a" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate({cx-26},{cy-176})"><rect x="0" y="30" width="52" height="40" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M9 30 V18 a17 17 0 0 1 34 0 v12" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="{cx}" y="{cy-64}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#FAFAF7">YOUR TAP</text>
        <text x="{cx}" y="{cy-36}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">every action, held</text>
      </svg>
      {cap("every send, deal and publish parks for you. nothing goes rogue.")}</div>'''

# 8. MEMORY - radial hub-and-spokes: one shared core, every stored fact orbiting on a lifeline
def memory():
    cx,cy=410,214
    facts=[("ICP",-90),("PIPELINE",-18),("PRICING",54),("DOCS",126),("VOICE",198)]
    spokes=""; chips=""
    for nm,a in facts:
        x=cx+168*math.cos(math.radians(a)); y=cy+168*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        chips+=(f'<rect x="{x-58:.0f}" y="{y-24:.0f}" width="116" height="48" rx="14" fill="#241f1a" stroke="rgba(255,255,255,.13)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#e6e0d5">{nm}</text>')
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.12)"/>' for r in (96,132,168))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One memory, every agent","SHARED CORE")}
      <svg width="820" height="446" viewBox="0 0 820 446" style="display:block;margin:0 auto">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {rings}{spokes}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">MEMORY</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11.5" letter-spacing=".08em" fill="#3a2010">the core</text>
        {chips}
      </svg>
      {cap("icp, pipeline, pricing, docs. one core every agent draws from.")}</div>'''

PANELS={"seventy":seventy(),"laptop":laptop(),"weekend":weekend(),"roster":roster(),
        "cents":cents(),"revenue":revenue(),"gate":gate(),"memory":memory()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s270aibusiness"; os.makedirs(outd,exist_ok=True)
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
