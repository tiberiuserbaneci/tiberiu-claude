#!/usr/bin/env python3
# TIER 3 - ONE SKILL, FIVE INCOMES, built to the WIRE-ITS-EYES / AI-BODY bar: each panel a UNIQUE
# hand-coded scene filling a clean rounded card, htitle + one mono caption, NO stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
IVACC="#96562d"
BAD="rgb(200,70,35)"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IVACC}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. MYTHOS - one-to-many FAN-OUT: one skill orb on the left rays out into 5 named shape chips
def mythos():
    hx,hy=158,238
    shapes=[("SERVICE","done for them",55),("PRODUCT","packaged once",150),
            ("CONTENT","proof in public",245),("TEACHING","the method priced",340),
            ("TOOL","method executable",435)]
    edges=""; chips=""
    for i,(nm,sub,y) in enumerate(shapes):
        edges+=f'<path d="M{hx+68} {hy} C320 {hy},350 {y},452 {y}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="3"/>'
        chips+=(f'<rect x="452" y="{y-37}" width="352" height="74" rx="17" fill="url(#chip)" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="494" cy="{y}" r="19" fill="none" stroke="rgb({ACC})" stroke-width="2"/>'
          f'<text x="494" y="{y+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="rgb({ACC})">{i+1}</text>'
          f'<text x="530" y="{y-4}" font-family="DM Sans" font-weight="800" font-size="22" fill="#FAFAF7" letter-spacing=".04em">{nm}</text>'
          f'<text x="530" y="{y+22}" font-family="DM Sans" font-size="15" fill="#8f8f85">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Everyone hunts a new skill","ONE BECOMES FIVE")}
      <svg width="820" height="490" viewBox="0 0 820 490" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="core" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <linearGradient id="chip" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{chips}
        <g filter="url(#cg)"><circle cx="{hx}" cy="{hy}" r="74" fill="url(#core)"/></g>
        <text x="{hx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">ONE</text>
        <text x="{hx}" y="{hy+18}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">SKILL</text>
      </svg>
      {cap("the money was in the skill you already have, reshaped five ways.")}</div>'''

# 2. SERVICE - ISO STACK: intake -> delivery -> follow-up pipeline the desk runs, ending in a live badge
def service():
    steps=[("INTAKE","brief scoped, priced"),("DELIVERY","work shipped in your voice"),("FOLLOW-UP","invoice and chase, automatic")]
    cards=""
    for i,(nm,sub) in enumerate(steps):
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">{i+1}</div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Done for them","SHAPE 1 &middot; SERVICE")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:120px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Retainer live &#10003; $8,000/mo</div></div></div>
      {cap("your skill applied to their business - the desk runs the whole engagement.")}</div>'''

# 3. PRODUCT - NODE GRAPH (ivory): component nodes converge into one package, delivered automatically
def product():
    W,H=760,430
    comps=[("Templates",70),("Audits",170),("Playbooks",270),("Checklists",370)]
    edges=""; nodes=""
    px,py=560,220
    for nm,y in comps:
        edges+=f'<path d="M232 {y} C400 {y},420 {py},{px-92} {py}" fill="none" stroke="rgba(150,90,45,.42)" stroke-width="2.5"/>'
        nodes+=(f'<rect x="34" y="{y-27}" width="198" height="54" rx="14" fill="#fff" stroke="rgba(120,95,60,.20)"/>'
          f'<circle cx="66" cy="{y}" r="7" fill="{IVACC}"/>'
          f'<text x="88" y="{y+6}" font-family="DM Sans" font-weight="700" font-size="18" fill="#3a2b1c">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("Packaged once","SHAPE 2 &middot; PRODUCT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="pk" cx="36%" cy="30%"><stop offset="0%" stop-color="#c98a5c"/><stop offset="100%" stop-color="{IVACC}"/></radialGradient>
        <filter id="pg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="rgba(150,90,45,.4)"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#pg)"><circle cx="{px}" cy="{py}" r="90" fill="url(#pk)"/></g>
        <text x="{px}" y="{py-8}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#fff">PACKAGE</text>
        <text x="{px}" y="{py+20}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#ffe6d2">built once</text>
        <path d="M{px+92} {py} h64" stroke="{IVACC}" stroke-width="4" stroke-linecap="round"/>
        <path d="M{px+150} {py-8} l12 8 l-12 8" fill="none" stroke="{IVACC}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="{px+110}" y="{py-24}" font-family="DM Mono" font-size="13" fill="#8a6a44">sold 5x</text>
      </svg>
      {cap("templates, audits and systems from your own workflow, delivered automatically.","#8a745a")}</div>'''

# 4. CONTENTS - TIMELINE: a 7-day posting week, one post per day, bars = reach, one lit
def contents():
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    heights=[120,150,96,180,210,70,110]  # relative reach
    lit=4
    W,H=760,420; base=330; x0=60; step=100
    bars=""; axis=""
    for i,(d,h) in enumerate(zip(days,heights)):
        x=x0+i*step; on=(i==lit)
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.34)"
        glow='filter="url(#bg)"' if on else ""
        bars+=(f'<rect x="{x-24}" y="{base-h}" width="48" height="{h}" rx="9" fill="{col}" {glow}/>'
          f'<circle cx="{x}" cy="{base-h-16}" r="8" fill="{col}"/>'
          f'<text x="{x}" y="{base+26}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="{"rgb("+ACC+")" if on else "#8f8f85"}">{d}</text>')
        if on:
            bars+=f'<text x="{x}" y="{base-h-30}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="rgb({ACC})">9,400</text>'
    axis=f'<line x1="{x0-40}" y1="{base}" x2="{x0+6*step+40}" y2="{base}" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Proof in public","SHAPE 3 &middot; CONTENT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="bg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        {axis}{bars}
        <text x="{x0-40}" y="80" font-family="DM Mono" font-size="13" fill="#8f8f85">reach / post</text>
      </svg>
      {cap("the desk turns client work into a daily post in your voice - content sells shapes 1 and 2.")}</div>'''

# 5. TEACHING - GAUGE (ivory): cohort fill dial + a compact cohort readout
def teaching():
    pct=90; seats=18; total=20; r=76; circ=2*math.pi*r; dash=circ*pct/100
    rows=[("Cohort","03 &middot; live"),("Price","$1,200 / seat"),("Length","6 weeks, 8 modules")]
    rl=""
    for k,v in rows:
        rl+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:12px 0;border-bottom:1px solid rgba(150,120,80,.16)">'
          f'<span style="font-family:DM Mono;font-size:14px;letter-spacing:.06em;color:#8a745a">{k}</span>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#2a2016">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("The method, priced","SHAPE 4 &middot; TEACHING")}
      <div style="display:flex;align-items:center;gap:40px">
        <div style="flex-shrink:0;position:relative;width:200px;height:200px">
          <svg width="200" height="200" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="16"/>
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="{IVACC}" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 100 100)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016">{seats}/{total}</span>
            <span style="font-family:DM Mono;font-size:12px;color:{IVACC}">seats filled</span></div></div>
        <div style="flex:1">{rl}</div>
      </div>
      {cap("your process, structured into a course by the same desk that runs it.","#8a745a")}</div>'''

# 6. TOOL - DOT FIELD: a field of runs, a handful lit = live runs of the skill others use
def tool5():
    cols,rowsn=54,39   # 2106 ~ 2,100
    lit={128,540,977,1203,1560,1788,1990,66,850}
    dots=""; cell=12; gap=3
    for i in range(cols*rowsn):
        rr,cc=divmod(i,cols); x=cc*(cell+gap); y=rr*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">2,106</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">runs this month</span></div>
        <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">SHAPE 5 &middot; TOOL</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("mint the workflow as a skill others run - cents a run, you keep the credit and the judgement.")}</div>'''

# 7. ENGINE5 - RADIAL HUB: one desk hub, 5 orbital shape nodes on the same memory / voice / gate
def engine5():
    cx,cy=410,228
    shapes=[("SERVICE",-90),("PRODUCT",-18),("CONTENT",54),("TEACHING",126),("TOOL",198)]
    Rr=176; lines=""; nodes=""
    for nm,a in shapes:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="none" stroke="rgba(212,162,127,.35)" stroke-width="1"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One desk runs all five","SAME ENGINE")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="dk" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="dg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {lines}
        <g filter="url(#dg)"><circle cx="{cx}" cy="{cy}" r="82" fill="url(#dk)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">DESK</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one operator</text>
        {nodes}
      </svg>
      {cap("same memory, same voice, same gate feeding service, product, content, teaching and tool.")}</div>'''

# 8. ORDER5 - INCOME STREAMS: 5 ordered revenue bars, service first funds the rest, tool last
def order5():
    W,H=760,420; base=316; x0=86; step=132; maxH=250; maxv=8000
    streams=[("SERVICE",8000,"1"),("PRODUCT",2400,"2"),("CONTENT",3000,"3"),("TEACHING",4500,"4"),("TOOL",1200,"5")]
    bars=""; flow=""
    for i,(nm,v,n) in enumerate(streams):
        x=x0+i*step; h=v/maxv*maxH; on=(i==0)
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.5)"
        bars+=(f'<rect x="{x-42}" y="{base-h:.0f}" width="84" height="{h:.0f}" rx="12" fill="{col}"/>'
          f'<rect x="{x-42}" y="{base-h:.0f}" width="84" height="10" rx="5" fill="rgba(255,255,255,.28)"/>'
          f'<text x="{x}" y="{base-h-14:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#FAFAF7">${v:,}</text>'
          f'<text x="{x}" y="{base+26}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".06em" fill="{"rgb("+ACC+")" if on else "#9a9488"}">{nm}</text>'
          f'<circle cx="{x}" cy="{base+52}" r="13" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="1.5"/>'
          f'<text x="{x}" y="{base+57}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="#c9a583">{n}</text>')
        if i<4:
            fx=x+13; fx2=x0+(i+1)*step-13
            flow+=f'<path d="M{fx} {base+52} H{fx2-6}" stroke="rgba(212,162,127,.4)" stroke-width="2"/><path d="M{fx2-12} {base+46} l8 6 l-8 6" fill="none" stroke="rgba(212,162,127,.6)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Service first, tool last","THE ORDER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <line x1="{x0-46}" y1="{base}" x2="{x0+4*step+46}" y2="{base}" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/>
        {bars}{flow}
        <text x="{x0+4*step+46}" y="96" text-anchor="end" font-family="DM Mono" font-size="14" fill="#c9a583">$19,100 / mo total</text>
      </svg>
      {cap("cash from shape one funds the rest - each shape feeds the next.")}</div>'''

PANELS={"mythos":mythos(),"service":service(),"product":product(),"contents":contents(),
        "teaching":teaching(),"tool5":tool5(),"engine5":engine5(),"order5":order5()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/oneskill"; os.makedirs(outd,exist_ok=True)
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
