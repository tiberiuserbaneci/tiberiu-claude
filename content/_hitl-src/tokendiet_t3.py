#!/usr/bin/env python3
# TIER 3 - THE CENTS DISCIPLINE, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO stat-chip strips, NO
# clip-path cuts, NO extruded walls. Ultron cost = CENTS; high $ only as a competitor stack.
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
def ihead(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LEAK - COST METER: two horizontal cost meters, same tool + same work, one founder pays a
# few cents, the other pays a multiple of the same cents (habit, not price).
def leak():
    rows=[("Disciplined founder","context reset, tiers matched","1.4c",0.11,f"rgb({ACC})","#FAFAF7"),
          ("Bloated founder","context dragged, deep on all","39c",0.86,f"rgb({RED})","#e8a48f")]
    grp=""
    for i,(lab,sub,val,frac,col,vcol) in enumerate(rows):
        y=44+i*170; tx=40; tw=520; th=34; ty=y+62; fill=tw*frac
        ticks="".join(f'<line x1="{tx+tw*t/10:.0f}" y1="{ty-9}" x2="{tx+tw*t/10:.0f}" y2="{ty-3}" stroke="rgba(250,250,247,.22)" stroke-width="2"/>' for t in range(11))
        grp+=(f'<text x="{tx}" y="{y+20}" font-family="DM Sans" font-weight="800" font-size="22" fill="#FAFAF7">{lab}</text>'
              f'<text x="{tx}" y="{y+44}" font-family="DM Sans" font-size="15" fill="#8f8f85">{sub}</text>'
              f'{ticks}'
              f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="{th/2}" fill="rgba(250,250,247,.06)" stroke="rgba(255,255,255,.08)"/>'
              f'<rect x="{tx}" y="{ty}" width="{fill:.0f}" height="{th}" rx="{th/2}" fill="{col}"/>'
              f'<polygon points="{tx+fill:.0f},{ty-5} {tx+fill-9:.0f},{ty-17} {tx+fill+9:.0f},{ty-17}" fill="{col}"/>'
              f'<text x="{tx+tw+26}" y="{ty+31}" font-family="DM Sans" font-weight="900" font-size="42" fill="{vcol}">{val}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The meter does not lie","SAME TOOL")}
      <svg width="760" height="392" viewBox="0 0 760 392" style="display:block">
        {grp}
        <text x="40" y="388" font-family="DM Mono" font-size="13" fill="#8f8f85">same model, same 40 tasks - the gap is 28x, and every bit of it is habit</text>
      </svg>
      {cap("one founder pays a few cents, another pays 28x the same cents for identical work.")}</div>'''

# 2. HABIT1 - SPEND CHART: cost per turn climbs when yesterday's context is dragged in; a flat
# accent line shows the same work with a per-task reset.
def habit1():
    vals=[0.3,0.5,0.8,1.2,1.6,2.1,2.7,3.4]; maxv=3.6; base=336; top=64; H=base-top
    x0=74; bw=52; gap=26; bars=""
    for i,v in enumerate(vals):
        x=x0+i*(bw+gap); h=H*v/maxv; y=base-h
        bars+=(f'<rect x="{x}" y="{y:.0f}" width="{bw}" height="{h:.0f}" rx="7" fill="url(#bar)"/>'
               f'<text x="{x+bw/2:.0f}" y="{base+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#7a746a">{i+1}</text>')
    cly=base-H*0.4/maxv
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Clear the context between tasks","PER-TASK RESET")}
      <svg width="740" height="396" viewBox="0 0 740 396">
        <defs><linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgb({RED})"/><stop offset="100%" stop-color="#6e2916"/></linearGradient></defs>
        <rect x="74" y="22" width="16" height="16" rx="4" fill="rgb({RED})"/><text x="98" y="35" font-family="DM Sans" font-size="15" fill="#c9c3b8">dragged context - 3.4c by turn 8</text>
        <rect x="430" y="22" width="16" height="16" rx="4" fill="rgb({ACC})"/><text x="454" y="35" font-family="DM Sans" font-size="15" fill="#c9c3b8">cleared each task - 0.4c flat</text>
        <line x1="64" y1="{base}" x2="712" y2="{base}" stroke="rgba(255,255,255,.12)"/>
        {bars}
        <line x1="64" y1="{cly:.0f}" x2="712" y2="{cly:.0f}" stroke="rgb({ACC})" stroke-width="3" stroke-dasharray="9 7"/>
        <text x="66" y="{base+40}" font-family="DM Mono" font-size="12" fill="#7a746a">turn</text>
      </svg>
      {cap("dragging yesterday into today makes every answer heavier, slower and pricier.")}</div>'''

# 3. HABIT2 - NODE GRAPH: three jobs on the left, each routed through the router to the cheapest
# tier that can do it (light / standard / deep), every tier a cents figure.
def habit2():
    rows=[("look up one fact","LITE","0.02c",92),
          ("draft 12 follow-ups","SMART","0.11c",232),
          ("price a hard deal","DEEP","0.40c",372)]
    hubx,hy=392,232; edges=""; jobs=""; tiers=""
    for job,tn,tc,y in rows:
        edges+=(f'<path d="M266 {y} C336 {y},336 {hy},{hubx-46} {hy}" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
                f'<path d="M{hubx+46} {hy} C500 {hy},500 {y},572 {y}" fill="none" stroke="rgb({ACC})" stroke-width="3"/>')
        jobs+=(f'<rect x="34" y="{y-30}" width="232" height="60" rx="15" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
               f'<text x="150" y="{y+6}" text-anchor="middle" font-family="DM Sans" font-size="17" fill="#c9c3b8">{job}</text>')
        tiers+=(f'<rect x="572" y="{y-38}" width="216" height="76" rx="16" fill="url(#tcard)" stroke="rgba(212,162,127,.4)"/>'
                f'<text x="592" y="{y-8}" font-family="DM Mono" font-size="14" letter-spacing=".12em" fill="#FAFAF7">{tn}</text>'
                f'<text x="770" y="{y-6}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="24" fill="rgb({ACC})">{tc}</text>'
                f'<text x="592" y="{y+22}" font-family="DM Sans" font-size="14" fill="#8f8f85">cheapest that can do it</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Right tier, right job","MODEL ROUTER")}
      <svg width="812" height="464" viewBox="0 0 812 464">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <linearGradient id="tcard" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a342d"/><stop offset="100%" stop-color="#221f1b"/></linearGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {edges}{jobs}{tiers}
        <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="46" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{hy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="14" fill="#1a0f0a">ROUTER</text>
        <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">reads the job</text>
      </svg>
      {cap("light for lookups, standard for daily work, deep only where judgement pays.")}</div>'''

# 4. HABIT3 - DOT FIELD: a field of raw log lines, most dropped (dim), a handful kept as the
# summary the model actually reads.
def habit3():
    cols,rowsn=40,18; cell=12; gap=4
    lit=set(i for i in range(cols*rowsn) if (i*7+13)%29==0)
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit: dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="rgb({ACC})" filter="url(#lg)"/>'
        else: dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:50px;color:#FAFAF7">12,400</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#a8a296;margin-left:10px">log lines in</span></div>
        <div style="text-align:right"><span style="font-family:'DM Sans';font-weight:900;font-size:32px;color:rgb({ACC})">180</span>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">kept as summary</div></div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("logs, dumps and threads get summarized first, not swallowed whole.")}</div>'''

# 5. HABIT4 - ISO STACK (ivory): isometric stack of memory files, a bloated one flagged and a
# lean one preferred - lean wins on both cost and quality.
def habit4():
    files=[("legacy-context.md","2,900 tokens - bloated",f"rgb({RED})","#f3ddd3",0,"drop"),
           ("scratch-notes.md","1,400 tokens - noisy","#a08a68","#efe6d5",128,"trim"),
           ("context.md","320 tokens - lean",f"rgb({ACC})","#fbf4ea",256,"keep")]
    cards=""
    for name,meta,tag,bg,y,mark in files:
        lean = mark=="keep"
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:{bg};'
          f'border:1.5px solid {"rgba(212,162,127,.5)" if lean else "rgba(120,95,60,.18)"};border-radius:18px;padding:20px 24px;'
          f'box-shadow:0 26px 40px rgba(120,95,60,.22), inset 0 2px 2px rgba(255,255,255,.8);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:46px;height:52px;border-radius:8px;background:linear-gradient(160deg,#fff,#e9ddc9);border:1px solid rgba(120,95,60,.2);position:relative">'
          f'<div style="position:absolute;top:8px;left:9px;right:9px;height:3px;border-radius:2px;background:{tag}"></div>'
          f'<div style="position:absolute;top:16px;left:9px;right:14px;height:3px;border-radius:2px;background:rgba(120,95,60,.3)"></div>'
          f'<div style="position:absolute;top:24px;left:9px;right:11px;height:3px;border-radius:2px;background:rgba(120,95,60,.3)"></div></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-weight:500;font-size:19px;color:#2a2016">{name}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8a745a;margin-top:2px">{meta}</div></div>'
          f'<div style="flex-shrink:0;font-family:\'DM Mono\';font-size:13px;letter-spacing:.1em;color:{tag};text-transform:uppercase">{mark}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ihead("Keep the memory files short and sharp","LEAN CONTEXT")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:420px;position:relative">{cards}</div></div>
      {cap("a lean context file beats a bloated one on both cost and quality.","#8a745a")}</div>'''

# 6. HABIT5 - TIMELINE: ten small asks strung along a timeline (each with overhead) vs one
# structured pass that covers all ten for a fraction of the cents.
def habit5():
    xs=[74+i*63 for i in range(10)]; segs=""
    for i,x in enumerate(xs):
        if i: segs+=f'<line x1="{xs[i-1]}" y1="118" x2="{x}" y2="118" stroke="rgba(200,70,35,.4)" stroke-width="2"/>'
        segs+=(f'<circle cx="{x}" cy="118" r="12" fill="#2a2724" stroke="rgb({RED})" stroke-width="2.4"/>'
               f'<text x="{x}" y="123" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#e8a48f">{i+1}</text>')
    ticks="".join(f'<rect x="{74+i*63-4}" y="296" width="8" height="18" rx="2" fill="rgba(26,15,10,.5)"/>' for i in range(10))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Batch the small stuff","ONE RUN, TEN ITEMS")}
      <svg width="812" height="400" viewBox="0 0 812 400">
        <text x="20" y="70" font-family="DM Sans" font-weight="700" font-size="18" fill="#a8a296">Ten separate asks</text>
        <line x1="74" y1="118" x2="641" y2="118" stroke="rgba(255,255,255,.08)"/>
        {segs}
        <text x="680" y="112" font-family="DM Sans" font-weight="900" font-size="30" fill="rgb({RED})">6.0c</text>
        <text x="680" y="132" font-family="DM Mono" font-size="12" fill="#8f8f85">10x overhead</text>
        <text x="20" y="256" font-family="DM Sans" font-weight="700" font-size="18" fill="#a8a296">One structured pass</text>
        <rect x="74" y="286" width="567" height="38" rx="19" fill="url(#pass)" stroke="rgba(212,162,127,.5)"/>
        {ticks}
        <text x="680" y="318" font-family="DM Sans" font-weight="900" font-size="30" fill="rgb({ACC})">0.9c</text>
        <text x="680" y="338" font-family="DM Mono" font-size="12" fill="#8f8f85">one pass</text>
        <defs><linearGradient id="pass" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#3a342d"/><stop offset="100%" stop-color="#4a4034"/></linearGradient></defs>
      </svg>
      {cap("ten tiny asks carry ten setups - one structured pass carries one.")}</div>'''

# 7. AUTOPILOT - RADIAL HUB: a central default-on core with four discipline nodes on spokes,
# each already switched on (router, reset, cap, filter).
def autopilot():
    cx,cy,R=406,232,168
    nodes=[("ROUTER","tiers every turn",-90),("RESET","context per task",0),
           ("SPEND CAP","cap on every flow",90),("FILTER","noise summarized",180)]
    spokes=""; boxes=""
    for nm,sub,a in nodes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="3"/>'
        boxes+=(f'<rect x="{x-96:.0f}" y="{y-38:.0f}" width="192" height="76" rx="16" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.5"/>'
                f'<circle cx="{x-72:.0f}" cy="{y-14:.0f}" r="6" fill="rgb({ACC})" filter="url(#on)"/>'
                f'<text x="{x-58:.0f}" y="{y-9:.0f}" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#FAFAF7">{nm}</text>'
                f'<text x="{x-72:.0f}" y="{y+20:.0f}" font-family="DM Sans" font-size="14" fill="#8f8f85">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("On the desk, the discipline is default","ON BY DEFAULT")}
      <svg width="812" height="464" viewBox="0 0 812 464" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter>
        <filter id="on" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">DEFAULT</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">no toggling</text>
        {boxes}
      </svg>
      {cap("the router tiers every turn, contexts reset per task, spend caps sit on every flow.")}</div>'''

# 8. REFRAME8 - GAUGE (ivory): a speedometer whose needle rests in the CLEAN zone, where cutting
# cost and raising quality are the same lever.
def reframe8():
    cx,cy,R=306,300,224; ticks=""
    for k in range(41):
        a=180-(k*180/40); rad=math.radians(a)
        x1=cx+R*math.cos(rad); y1=cy-R*math.sin(rad); x2=cx+(R-34)*math.cos(rad); y2=cy-(R-34)*math.sin(rad)
        col=f"rgb({RED})" if k<14 else ("#c9a06f" if k<27 else f"rgb({ACC})")
        w=6 if k%5==0 else 3
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}"/>'
    na=math.radians(34); nx=cx+(R-58)*math.cos(na); ny=cy-(R-58)*math.sin(na)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 30px">
      {ihead("Do not chase cheap, chase clean","COST = QUALITY")}
      <div style="display:flex;align-items:center;justify-content:center">
      <svg width="612" height="336" viewBox="0 0 612 336">
        {ticks}
        <text x="72" y="326" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#96562d">CHASE CHEAP</text>
        <text x="540" y="326" text-anchor="end" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#8a6a44">CHASE CLEAN</text>
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="7" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#2a2016"/>
        <text x="{cx}" y="{cy-70}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="42" fill="#2a2016">CLEAN</text>
        <text x="{cx}" y="{cy-40}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#96562d">same lever, both ways</text>
      </svg>
      </div>
      {cap("the habits that cut the cents are the same ones that raise the quality.","#8a745a")}</div>'''

PANELS={"leak":leak(),"habit1":habit1(),"habit2":habit2(),"habit3":habit3(),
        "habit4":habit4(),"habit5":habit5(),"autopilot":autopilot(),"reframe8":reframe8()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/tokendiet"; os.makedirs(outd,exist_ok=True)
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
