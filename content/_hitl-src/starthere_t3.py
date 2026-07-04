#!/usr/bin/env python3
# TIER 3 - THE PLATFORM WAS NEVER IT, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips,
# NO clip-path cuts, NO extruded walls. Warm palette. Overwrites models_clay/starthere/*.png. Cost zero.
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
def ivtitle(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LISTS9 - a 45-tile grid of open (unlocked) platform doors, next to a big $0 readout.
def lists9():
    cols,rows,tw,th,gx,gy=9,5,48,38,6,8
    tiles=""
    for i in range(45):
        r,c=divmod(i,cols); x=c*(tw+gx); y=r*(th+gy); cxx=x+tw/2; cyy=y+th/2+2
        tiles+=(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="9" fill="rgba(250,250,247,.045)" stroke="rgba(255,255,255,.07)"/>'
          f'<rect x="{cxx-8:.0f}" y="{cyy-1:.0f}" width="16" height="12" rx="2.5" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2"/>'
          f'<path d="M{cxx-5:.0f} {cyy-1:.0f} v-4 a5 5 0 0 1 10 -2" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2" stroke-linecap="round"/>')
    fw=cols*(tw+gx)-gx; fh=rows*(th+gy)-gy
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The doors were never locked","45 PLATFORMS · OPEN")}
      <div style="display:flex;align-items:center;gap:36px">
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="flex-shrink:0">{tiles}</svg>
        <div style="flex:1;text-align:left">
          <div style="font-family:'DM Sans';font-weight:900;font-size:82px;color:rgb({ACC});line-height:.85">$0</div>
          <div style="font-family:'DM Mono';font-size:14px;letter-spacing:.14em;color:#8f8f85;margin-top:8px">FIRST DOLLAR</div>
          <div style="border-top:1px solid rgba(255,255,255,.09);margin-top:20px;padding-top:18px">
            <div style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#e8e2d6">45 accounts opened</div>
            <div style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#8f8f85;margin-top:4px">0 systems run</div></div>
        </div></div>
      {cap("upwork, fiverr, gumroad, etsy, substack: signing up was never the locked door.")}</div>'''

# 2. GAP9 - contribution-style heatmap: consistent daily activity is the reward, not signups.
def gap9():
    weeks,days,cell,gp=15,7,26,6; gut=44
    cells=""
    for c in range(weeks):
        for r in range(days):
            v=(c*3+r*2+(c*r)%4)%4
            a=[.07,.30,.55,.92][v]
            x=gut+c*(cell+gp); y=r*(cell+gp)
            cells+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="6" fill="rgba(212,162,127,{a})"/>'
    labs=""
    for i,d in enumerate(["M","T","W","T","F","S","S"]):
        labs+=f'<text x="26" y="{i*(cell+gp)+18}" text-anchor="end" font-family="DM Mono" font-size="13" fill="#7a746a">{d}</text>'
    fw=gut+weeks*(cell+gp)-gp; fh=days*(cell+gp)-gp
    leg="".join(f'<span style="width:15px;height:15px;border-radius:4px;background:rgba(212,162,127,{a})"></span>' for a in [.07,.30,.55,.92])
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Winners just show up","BORING · REPEATED · PAID")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block">{labs}{cells}</svg>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:18px">
        <span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#e8e2d6">97 active days, one platform</span>
        <span style="display:flex;align-items:center;gap:8px"><span style="font-family:'DM Mono';font-size:12px;color:#7a746a">less</span>{leg}<span style="font-family:'DM Mono';font-size:12px;color:#7a746a">more</span></span>
      </div>
      {cap("show up daily, respond fast, follow up. that is the entire moat, not the signup.")}</div>'''

# 3. PROFILE9 - IVORY: your profile drawn as an offer page (outcome / proof / next step) vs a resume.
def profile9():
    resume="".join(f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:11px"><span style="width:6px;height:6px;border-radius:50%;background:#b6a891"></span><span style="font-family:\'DM Sans\';font-size:16px;color:#9c8e78;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.55)">{t}</span></div>' for t in ["10 yrs experience","hard worker","team player","fast learner"])
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {ivtitle("Your profile is an offer page","OFFER, NOT RESUME")}
      <div style="display:flex;gap:24px;align-items:stretch">
        <div style="flex:1.45;border-radius:16px;overflow:hidden;border:1px solid rgba(120,95,60,.22);box-shadow:0 18px 34px rgba(120,95,60,.18)">
          <div style="display:flex;align-items:center;gap:8px;padding:12px 16px;background:#e7ddcc;border-bottom:1px solid rgba(120,95,60,.16)">
            <span style="width:11px;height:11px;border-radius:50%;background:#c9baa2"></span><span style="width:11px;height:11px;border-radius:50%;background:#c9baa2"></span><span style="width:11px;height:11px;border-radius:50%;background:#c9baa2"></span>
            <span style="margin-left:12px;font-family:'DM Mono';font-size:14px;color:#7a6a50">upwork.com/in/you</span></div>
          <div style="background:#fffdf8;padding:22px 24px 24px">
            <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#96562d">OUTCOME</div>
            <div style="font-family:'DM Sans';font-weight:800;font-size:22px;color:#2a2016;margin-top:4px;line-height:1.25">First 10 booked demos for SaaS founders, in 30 days.</div>
            <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#96562d;margin-top:20px">PROOF</div>
            <div style="font-family:'DM Sans';font-weight:700;font-size:18px;color:#4a3c2a;margin-top:4px">14 delivered · 4.9 stars · 9 rehires</div>
            <div style="display:flex;align-items:center;justify-content:space-between;margin-top:22px;background:#96562d;border-radius:12px;padding:14px 20px">
              <span style="font-family:'DM Sans';font-weight:900;font-size:18px;color:#fff8f2">Book a 15-min fit call</span>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff8f2" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
          </div></div>
        <div style="flex:1;background:rgba(255,255,255,.5);border:1px dashed rgba(150,120,80,.35);border-radius:16px;padding:20px 22px">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#b06a4a">READS LIKE A RESUME</div>
          <div style="margin-top:16px">{resume}</div>
          <div style="font-family:'DM Sans';font-size:15px;color:#a2937c;margin-top:6px">no outcome, no proof, no ask.</div></div>
      </div>
      {cap("outcome, proof, one clear next step, drafted from your real deliveries.","#8a745a")}</div>'''

# 4. RESPONSE9 - a two-lane race: your desk replies in minutes, the field replies in hours.
def response9():
    W,H=760,240
    def lane(y,label,frac,col,ftxt,dim):
        x2=90+(W-160)*frac
        track=f'<line x1="90" y1="{y}" x2="{W-70}" y2="{y}" stroke="rgba(255,255,255,.09)" stroke-width="8" stroke-linecap="round"/>'
        fill=f'<line x1="90" y1="{y}" x2="{x2:.0f}" y2="{y}" stroke="{col}" stroke-width="8" stroke-linecap="round"/>'
        dot=f'<circle cx="{x2:.0f}" cy="{y}" r="12" fill="{col}"/>'
        lab=f'<text x="90" y="{y-24}" font-family="DM Sans" font-weight="800" font-size="18" fill="{"#FAFAF7" if not dim else "#8f8f85"}">{label}</text>'
        rt=f'<text x="{x2:.0f}" y="{y+34}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="{col}">{ftxt}</text>'
        return track+fill+dot+lab+rt
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("First reply wins","SPEED IS THE ALGORITHM")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="rg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        <line x1="90" y1="20" x2="90" y2="{H-20}" stroke="rgba(255,255,255,.14)" stroke-width="2" stroke-dasharray="4 6"/>
        <text x="90" y="16" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#8f8f85">BRIEF POSTED</text>
        <g filter="url(#rg)">{lane(88,"You + the desk",0.14,f"rgb({ACC})","4 min · first in",False)}</g>
        {lane(190,"Typical freelancer",0.82,"rgba(255,255,255,.28)","6 h later · buried",True)}
      </svg>
      <div style="display:flex;align-items:center;gap:12px;margin-top:12px;background:rgba(212,162,127,.08);border:1px solid rgba(212,162,127,.28);border-radius:12px;padding:12px 18px;width:max-content">
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:#8f8f85">BRIEF READ + REPLY DRAFTED</span>
        <span style="font-family:'DM Sans';font-weight:900;font-size:22px;color:rgb({ACC})">0.4c</span></div>
      {cap("read the brief, draft the reply, park it for your tap. minutes, not hours.")}</div>'''

# 5. FOLLOW9 - a message thread where the money lands on reply number three.
def follow9():
    def bubble(txt,meta,accent=False):
        bg="linear-gradient(160deg,#e6b48f,rgb("+ACC+") 60%,#9a5a35)" if accent else "linear-gradient(160deg,#333029,#242220)"
        col="#1a0f0a" if accent else "#eae4d8"
        return (f'<div style="display:flex;flex-direction:column;align-items:flex-end;margin-bottom:14px">'
          f'<div style="max-width:560px;background:{bg};border-radius:20px 20px 6px 20px;padding:15px 20px;'
          f'box-shadow:0 12px 22px rgba(0,0,0,.4), inset 0 1.5px 2px rgba(255,255,255,.12);'
          f'font-family:\'DM Sans\';font-weight:700;font-size:19px;color:{col}">{txt}</div>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;color:#7a746a;margin-top:7px;margin-right:6px">{meta}</span></div>')
    ghost=('<div style="display:flex;align-items:center;gap:12px;margin:6px 0 16px 0">'
      '<div style="flex:1;border-top:1px dashed rgba(200,70,35,.4)"></div>'
      '<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.08em;color:#c84623">most freelancers stop here</span>'
      '<div style="flex:1;border-top:1px dashed rgba(200,70,35,.4)"></div></div>')
    won=('<div style="display:flex;align-items:center;justify-content:flex-end;gap:12px;margin-top:16px">'
      '<span style="font-family:\'DM Sans\';font-weight:900;font-size:20px;color:#FAFAF7">Project won</span>'
      f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:rgb({ACC});background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.4);border-radius:12px;padding:8px 16px">$2,400</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The money is in reply #3","NOBODY DOES THIS PART")}
      {bubble("Following up on your brief, here is how I would approach it.","reply 1 · day 0")}
      {ghost}
      {bubble("Made you a quick sample so you can see the fit.","reply 2 · day 2")}
      {bubble("Still open? I can start Monday and deliver by Friday.","reply 3 · day 5",True)}
      {won}
      {cap("quiet clients chased on triggers, delivered work re-pitched. the desk sends the third message.")}</div>'''

# 6. PORTFOLIO9 - IVORY flywheel: delivery -> post -> case note -> new brief, spinning on proof.
def portfolio9():
    cx,cy,R=250,225,150
    nodes=[("Deliver",-90),("Post it",0),("Case note",90),("New brief",180)]
    arcs=""; ns=""
    for nm,a in nodes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        a2=a+90
        x2=cx+R*math.cos(math.radians(a2)); y2=cy+R*math.sin(math.radians(a2))
        arcs+=f'<path d="M{x:.0f} {y:.0f} A{R} {R} 0 0 1 {x2:.0f} {y2:.0f}" fill="none" stroke="#96562d" stroke-width="3" marker-end="url(#ah)"/>'
        ns+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#fffdf8" stroke="rgba(150,90,45,.35)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#4a3423">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="500" height="450" viewBox="0 0 500 450" style="flex-shrink:0">
        <defs><marker id="ah" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="#96562d"/></marker>
        <radialGradient id="hub" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#96562d"/></radialGradient></defs>
        {arcs}
        <circle cx="{cx}" cy="{cy}" r="66" fill="url(#hub)"/>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">PROOF</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010" letter-spacing=".08em">compounds</text>
        {ns}</svg>
      <div style="flex:1">
        {ivtitle("Every delivery becomes proof","THE FLYWHEEL")}
        <div style="font-family:'DM Sans';font-size:19px;color:#4a3c2a;line-height:1.45">Finished work turns into posts and case notes automatically. Each one pulls the next brief in, so the account never sits cold.</div>
        {cap("do the work once, let it market you forever. the flywheel starts on delivery one.","#8a745a")}</div></div>'''

# 7. ONEDOOR - a row of dim doors, one lit and enlarged, wrapped by a 30-day progress arc.
def onedoor():
    W,H=760,400
    doors=""
    xs=[70,190,310,470,590,690]; lit=3
    for i,x in enumerate(xs):
        on=(i==lit)
        if on: continue
        doors+=(f'<rect x="{x}" y="230" width="70" height="130" rx="10" fill="#221f1b" stroke="rgba(255,255,255,.08)" stroke-width="1.5"/>'
          f'<circle cx="{x+56}" cy="298" r="4" fill="rgba(250,250,247,.18)"/>')
    lx=390
    # 30-day arc over the lit door
    ticks=""
    for k in range(30):
        a=math.radians(180 - k*(180/29))
        r1,r2=150,168
        x1=lx+r1*math.cos(a); y1=120+r1*math.sin(a)*-1
        x2=lx+r2*math.cos(a); y2=120+r2*math.sin(a)*-1
        col=f"rgb({ACC})" if k<12 else "rgba(255,255,255,.12)"
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Pick one door","DEPTH BEATS DIRECTORY")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="dr" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#241f1a"/></linearGradient>
        <filter id="dg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {doors}{ticks}
        <text x="{lx}" y="40" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">DAY 12 / 30</text>
        <g filter="url(#dg)"><rect x="{lx-56}" y="150" width="112" height="210" rx="14" fill="url(#dr)" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <rect x="{lx-42}" y="166" width="84" height="178" rx="9" fill="none" stroke="rgba(255,255,255,.08)"/>
        <circle cx="{lx+30}" cy="262" r="6" fill="rgb({ACC})"/>
        <text x="{lx}" y="300" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">ONE</text>
        <text x="{lx}" y="325" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">the full loop</text>
      </svg>
      {cap("one platform, thirty days, the whole loop. then, and only then, add the second.")}</div>'''

# 8. TRUTH9 - closing: a balance tipped to the operator, the list weighs nothing.
def truth9():
    return f'''<div style="width:820px;{CARD};padding:40px 44px 40px;text-align:center;margin:0 auto">
      {htitle("The list was free","BE THE OPERATOR")}
      <svg width="560" height="300" viewBox="0 0 560 300" style="display:block;margin:8px auto 0">
        <defs><radialGradient id="op" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="272" y="70" width="16" height="180" rx="6" fill="#3a352f"/>
        <path d="M280 250 L228 285 L332 285 Z" fill="#2c2822" stroke="rgba(255,255,255,.08)"/>
        <!-- beam tipped toward operator (right down) -->
        <g transform="rotate(11 280 82)">
          <rect x="120" y="76" width="320" height="12" rx="6" fill="#4a423a"/>
          <line x1="150" y1="82" x2="150" y2="120" stroke="rgba(255,255,255,.16)" stroke-width="2"/>
          <line x1="410" y1="82" x2="410" y2="120" stroke="rgba(212,162,127,.5)" stroke-width="2"/>
          <ellipse cx="150" cy="128" rx="58" ry="14" fill="none" stroke="rgba(255,255,255,.16)" stroke-width="2"/>
          <text x="150" y="118" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">45-SITE LIST</text>
          <text x="150" y="150" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#8f8f85">$0</text>
          <g filter="url(#og)"><circle cx="410" cy="150" r="46" fill="url(#op)"/></g>
          <text x="410" y="156" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#2a160c">OPERATOR</text>
        </g>
      </svg>
      <div style="font-family:'DM Sans';font-weight:900;font-size:32px;color:#FAFAF7;margin-top:14px">The discipline was not.</div>
      {cap("45 websites, one differentiator: the operator behind the account.")}</div>'''

PANELS={"lists9":lists9(),"gap9":gap9(),"profile9":profile9(),"response9":response9(),
        "follow9":follow9(),"portfolio9":portfolio9(),"onedoor":onedoor(),"truth9":truth9()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/starthere"; os.makedirs(outd,exist_ok=True)
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
