#!/usr/bin/env python3
# TIER 3 - THE SIX-DOLLAR MARKET (services wedge), built to the WIRE-ITS-EYES bar: each panel a
# UNIQUE hand-built coded scene filling a clean rounded card, title + one-line caption, no generic
# stat-chip strips. Adapts the Sequoia "$1 software vs $6 services" thesis into the Ultron story:
# software is a small slice, services (the human labor) is the giant market, Ultron automates the
# services layer in cents.
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SPLIT - two proportional spend bars: $1 software (thin) vs $6 services (6x)
def split():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Six dollars to one","SPEND SPLIT")}
      <svg width="820" height="460" viewBox="0 0 820 460">
        <defs><linearGradient id="svc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#e6b48f"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#9a5a35"/></linearGradient>
        <filter id="sg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="rgba(212,162,127,.35)"/></filter></defs>
        <!-- SOFTWARE row -->
        <text x="26" y="118" font-family="DM Sans" font-weight="900" font-size="60" fill="#8f8f85">$1</text>
        <rect x="150" y="70" width="96" height="72" rx="12" fill="#3a352f" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>
        <text x="150" y="176" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="#9a9488">SOFTWARE &#183; ~$650B market</text>
        <!-- SERVICES row -->
        <text x="26" y="330" font-family="DM Sans" font-weight="900" font-size="60" fill="rgb({ACC})">$6</text>
        <rect x="150" y="270" width="640" height="108" rx="14" fill="url(#svc)" filter="url(#sg)"/>
        <text x="176" y="336" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">SERVICES</text>
        <text x="150" y="412" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="#c9a583">THE HUMAN LABOR &#183; multi-trillion market</text>
        <!-- 6x guide -->
        <line x1="246" y1="150" x2="246" y2="264" stroke="rgba(250,250,247,.18)" stroke-width="1.5" stroke-dasharray="3 7"/>
        <text x="800" y="256" text-anchor="end" font-family="DM Mono" font-size="15" fill="rgb({ACC})">6&#215; the spend</text>
      </svg>
      {cap("saas captured the small dollar. the services dollar was six times bigger.")}</div>'''

# 2. TREEMAP - one tiny software tile beside a huge field of warm services tiles
def treemap():
    tiles=[("Consulting","$",202,0,352,196,.24),("Support","$",562,0,258,196,.20),
           ("Outbound","$",0,140,182,304,.28),("Marketing","$",202,208,238,236,.22),
           ("Legal","$",452,208,168,236,.18),("Operations","$",632,208,188,236,.25)]
    rects=""
    for nm,_,x,y,w,h,op in tiles:
        rects+=(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="rgba(212,162,127,{op})" stroke="rgba(212,162,127,.42)" stroke-width="1.5"/>'
          f'<text x="{x+18}" y="{y+34}" font-family="DM Sans" font-weight="800" font-size="19" fill="#efe6d6">{nm}</text>'
          f'<text x="{x+18}" y="{y+56}" font-family="DM Mono" font-size="12" letter-spacing=".06em" fill="#b7a488">services spend</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The market is mostly services","MARKET MAP")}
      <svg width="820" height="444" viewBox="0 0 820 444">
        {rects}
        <rect x="0" y="0" width="182" height="124" rx="12" fill="rgba(250,250,247,.05)" stroke="rgba(255,255,255,.2)" stroke-width="1.5"/>
        <text x="18" y="34" font-family="DM Sans" font-weight="800" font-size="19" fill="#c9c3b8">Software</text>
        <text x="18" y="58" font-family="DM Mono" font-size="12" letter-spacing=".06em" fill="#8f8f85">$650B &#183; the tip</text>
        <text x="18" y="104" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#7a7468">SAAS ERA</text>
      </svg>
      {cap("software is a $650b corner. the services market is a multi-trillion field.")}</div>'''

# 3. LEDGER (ivory) - a company budget book: one software line, six services lines
def ledger():
    rows=[("Software / SaaS",0.16,"$1",False),
          ("Research",0.62,"","svc"),("Outbound",0.78,"","svc"),("Deals",0.7,"","svc"),
          ("Content",0.84,"","svc"),("Code",0.66,"","svc"),("Legal",0.58,"","svc")]
    body=""
    for nm,frac,amt,svc in rows:
        barcol="#96562d" if svc else "rgba(120,95,60,.34)"
        lblink="#2a2016" if svc else "#7a6a52"
        w=int(360*frac)
        tag=amt if amt else "services"
        tagcol="#7a6a52" if not svc else "#96562d"
        body+=(f'<div style="display:flex;align-items:center;gap:18px;padding:11px 0;border-bottom:1px solid rgba(120,95,60,.16)">'
          f'<span style="width:150px;font-family:DM Sans;font-weight:{700 if svc else 500};font-size:19px;color:{lblink}">{nm}</span>'
          f'<span style="flex:1;position:relative;height:20px"><span style="position:absolute;left:0;top:0;height:20px;width:{w}px;border-radius:6px;background:{barcol}"></span></span>'
          f'<span style="width:82px;text-align:right;font-family:DM Mono;font-size:14px;color:{tagcol}">{tag}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("One software line. Six services lines.","THE BUDGET")}
      <div>{body}</div>
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:16px">
        <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016">Services total</span>
        <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#96562d">$6</span></div>
      {cap("every services line is human labor. that is where the money actually sits.","#8a745a")}</div>'''

# 4. OUTCOMES - tool (struck, red) -> finished outcome (lit, accent) swap rows
def outcomes():
    pairs=[("a legal app","the reviewed contract"),("a mail tool","the booked meeting"),
           ("a support desk","the resolved tickets"),("a marketing suite","the launched campaign")]
    rows=""
    for tool,out in pairs:
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;margin-bottom:16px">'
          f'<div style="width:300px;background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.32);border-radius:14px;padding:15px 18px">'
          f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:rgb({RED});margin-bottom:3px">THE TOOL</div>'
          f'<div style="font-family:DM Sans;font-weight:600;font-size:20px;color:#c9948a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">{tool}</div></div>'
          f'<svg width="34" height="20" viewBox="0 0 34 20" style="flex-shrink:0"><path d="M2 10 H28 M22 4 l6 6 -6 6" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:14px;padding:15px 18px;box-shadow:0 0 22px rgba(212,162,127,.16)">'
          f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:3px">THE WORK</div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{out}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nobody buys the tool","TOOL &#8594; WORK")}
      <div>{rows}</div>
      {cap("the next company sells the finished work, not a blank app to do it in.")}</div>'''

# 5. ROSTER - Ultron sphere hub, six agents each owning one services line (hub-and-spokes)
def roster():
    cx,cy,R=410,232,168
    agents=[("CORTEX","research",-90),("SPECTER","outbound",-30),("STRIKER","deals",30),
            ("PULSE","content",90),("SENTINEL","code",150),("COUNSEL","legal",210)]
    spokes=""; nodes=""
    for nm,svc,a in agents:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        nodes+=(f'<g><rect x="{x-92:.0f}" y="{y-30:.0f}" width="184" height="60" rx="14" '
          f'fill="#221f1b" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="rgb({ACC})">{svc}</text></g>')
    orb=f'<image href="data:image/png;base64,{Lm.ORB}" x="{cx-66}" y="{cy-66}" width="132" height="132"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Six services, one operator","THE ROSTER")}
      <svg width="820" height="464" viewBox="0 0 820 464">
        <defs><filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#og)"><circle cx="{cx}" cy="{cy}" r="72" fill="#0c0e14"/></g>{orb}
        <text x="{cx}" y="{cy+112}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#8f8f85">ULTRON &#183; runs the labor</text>
      </svg>
      {cap("each services line has an owner. one operator runs the whole desk.")}</div>'''

# 6. CENTS (ivory) - a gauge from dollars down to cents, needle pinned at cents
def cents():
    cx,cy,R=280,270,210
    a=math.radians(168)  # needle near the low (cents) end of a 180..0 sweep
    nx=cx+(R-40)*math.cos(a); ny=cy-(R-40)*math.sin(a)
    ticks=""
    for i,lab in enumerate(["$$$$","$$$","$$","$","c"]):
        ta=math.radians(180-i*45)
        lx=cx+(R+18)*math.cos(ta); ly=cy-(R+18)*math.sin(ta)
        col="#96562d" if lab=="c" else "#8a745a"
        ticks+=f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="{col}">{lab}</text>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;align-items:center;gap:20px">
      <svg width="440" height="320" viewBox="0 0 440 320">
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="26" stroke-linecap="round"/>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R*math.cos(math.radians(45)):.0f} {cy-R*math.sin(math.radians(45)):.0f}" fill="none" stroke="#e7cbb0" stroke-width="26" stroke-linecap="round"/>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R*math.cos(math.radians(150)):.0f} {cy-R*math.sin(math.radians(150)):.0f}" fill="none" stroke="#96562d" stroke-width="26" stroke-linecap="round"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="7" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="13" fill="#2a2016"/>
        <text x="{cx}" y="{cy-56}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="44" fill="#2a2016">cents</text>
        <text x="{cx}" y="{cy-30}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#96562d">per task</text>
      </svg>
      <div style="flex:1">
        {htitle_iv("The six dollars, for cents","THE PRICE")}
        <div style="background:rgba(200,70,35,.07);border:1px solid rgba(200,70,35,.28);border-radius:14px;padding:15px 18px;margin-bottom:12px">
          <div style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:rgb({RED});margin-bottom:3px">HUMAN SERVICES LINE</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:24px;color:#a85a45;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.65)">$4,000 / month retainer</div></div>
        <div style="background:rgba(150,90,45,.1);border-left:4px solid #96562d;border-radius:12px;padding:15px 18px">
          <div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#2a2016">Ultron bills by the token.</div></div>
        {cap("a retainer bills by the hour. this bills in cents, per task.","#8a745a")}
      </div></div>'''

# 7. PIPELINE - linear flow: request enters, runs the stages, finished work ships out
def pipeline():
    stages=[("REQUEST","plain English"),("SOURCED","CORTEX"),("DRAFTED","PULSE"),("REVIEWED","COUNSEL"),("GATE","your tap")]
    n=len(stages); W=760; x0=30; step=(W-x0)/n
    segs=""
    for i,(nm,sub) in enumerate(stages):
        x=x0+step*i+step/2
        gate=(nm=="GATE")
        bd=f"rgb({ACC})" if gate else "rgba(255,255,255,.12)"
        bg="linear-gradient(160deg,#403a33,#241f1a)" if gate else "linear-gradient(160deg,#302c27,#201d1a)"
        segs+=(f'<div style="position:absolute;left:{x-64:.0f}px;top:110px;width:128px;background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 12px;text-align:center;{"box-shadow:0 0 22px rgba(212,162,127,.18)" if gate else ""}">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:15px;color:#d9d5cc;margin-top:3px">{sub}</div></div>')
        if i<n-1:
            segs+=f'<svg width="{step:.0f}" height="20" viewBox="0 0 {step:.0f} 20" style="position:absolute;left:{x+64:.0f}px;top:145px"><path d="M2 10 H{step-24:.0f} M{step-30:.0f} 4 l6 6 -6 6" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    pkg=('<div style="position:absolute;left:300px;top:300px;display:flex;align-items:center;gap:14px;background:rgb('+ACC+');border-radius:16px;padding:14px 26px;box-shadow:0 14px 30px rgba(212,162,127,.4)">'
      '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8l-9-5-9 5 9 5 9-5zM3 8v8l9 5 9-5V8M12 13v8"/></svg>'
      '<span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#1a0f0a">Finished work, delivered</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {htitle("Request in, work out","END TO END")}
      <div style="position:relative;height:420px">{segs}
        <svg width="70" height="60" viewBox="0 0 70 60" style="position:absolute;left:360px;top:214px"><path d="M35 4 V50 M22 38 l13 13 13 -13" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        {pkg}</div>
      {cap("sourced, drafted, reviewed, gated. the service runs itself, not a blank tool.")}</div>'''

# 8. WEDGE - services-spend streams bezier-converge into one operator orb ("own the six")
def wedge():
    spend=[("Agency retainer","$3k",96),("Contractor hours","$1.4k",176),("Support team","$900",256),("Legal counsel","$700",336)]
    hubx,huby=650,232
    edges=""; chips=""
    for nm,amt,y in spend:
        edges+=f'<path d="M300 {y} C440 {y},480 {huby},{hubx-92} {huby}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.5"/>'
        chips+=(f'<g><rect x="20" y="{y-30}" width="280" height="60" rx="14" fill="#221f1b" stroke="rgba(200,70,35,.28)" stroke-width="1.5"/>'
          f'<text x="42" y="{y-4}" font-family="DM Sans" font-weight="700" font-size="18" fill="#d9d5cc">{nm}</text>'
          f'<text x="42" y="{y+16}" font-family="DM Mono" font-size="12" fill="#8f8f85">a services line you pay for</text>'
          f'<text x="284" y="{y+2}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="20" fill="rgb({RED})">{amt}</text></g>')
    orb=f'<image href="data:image/png;base64,{Lm.ORB}" x="{hubx-66}" y="{huby-66}" width="132" height="132"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The six-dollar layer, owned","THE WEDGE")}
      <svg width="820" height="464" viewBox="0 0 820 464">
        <defs><filter id="wg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {edges}{chips}
        <g filter="url(#wg)"><circle cx="{hubx}" cy="{huby}" r="74" fill="#0c0e14"/></g>{orb}
        <text x="{hubx}" y="{huby+118}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">one operator</text>
        <text x="{hubx}" y="{huby+144}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">automates the $6</text>
      </svg>
      {cap("automate the services spend. that is where the next company is built.")}</div>'''

PANELS={"split":split(),"treemap":treemap(),"ledger":ledger(),"outcomes":outcomes(),
        "roster":roster(),"cents":cents(),"pipeline":pipeline(),"wedge":wedge()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src44"; os.makedirs(outd,exist_ok=True)
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
