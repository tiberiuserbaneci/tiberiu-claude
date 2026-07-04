#!/usr/bin/env python3
# TIER 3 - FIVE ENGINEERS, ONE TERMINAL. Angle: SENTINEL is a whole engineering ORG of ROLES
# (architect / builder / tester / reviewer / docs) staffed by one terminal command - founder-facing
# (shipped product + PR, no raw code). Each panel a UNIQUE hand-built coded scene on a clean rounded
# card, title + one-line caption. Helpers + __main__ copied verbatim from aibody_t3.py.
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

# 1. ORG - radial hub-and-spokes: one terminal command staffs 5 role nodes
def org():
    cx,cy,R=410,232,172
    roles=[("ARCHITECT","plans it",-90),("BUILDER","writes it",-18),("TESTER","checks it",54),
           ("REVIEWER","reviews it",126),("DOCS","documents it",198)]
    ring=""
    for nm,duty,a in roles:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2.4"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="55" fill="#241f1a" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="55" fill="none" stroke="rgba(255,255,255,.07)" stroke-width="1"/>'
          f'<text x="{x:.0f}" y="{y-4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="rgb({ACC})">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Sans" font-size="13" fill="#a8a296">{duty}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One line staffs the team","SENTINEL ORG")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {ring}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="74" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">SENTINEL</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one command</text>
      </svg>
      {cap("type one line and a whole engineering team reports in.")}</div>'''

# 2. ARCHITECT - IVORY blueprint: a goal branches into an ordered plan before any code
def architect():
    steps=[("1","Data model",55),("2","API route",145),("3","Billing UI",235),("4","Test plan",325)]
    gx,gy=250,205
    edges=""; chips=""
    for n,label,y in steps:
        cy=y+34; mx=(gx+470)/2
        edges+=f'<path d="M{gx} {gy} C{mx:.0f} {gy},{mx:.0f} {cy},470 {cy}" fill="none" stroke="#96562d" stroke-width="2.4" opacity="0.7"/>'
        chips+=(f'<div style="position:absolute;left:470px;top:{y}px;width:300px;display:flex;align-items:center;gap:16px;'
          f'background:linear-gradient(160deg,#fbf6ee,#efe4d2);border:1px solid rgba(120,95,60,.2);border-radius:16px;padding:14px 18px;box-shadow:0 12px 22px rgba(120,95,60,.14)">'
          f'<span style="flex-shrink:0;width:34px;height:34px;border-radius:10px;background:#96562d;color:#fdfbf6;font-family:DM Sans;font-weight:900;font-size:18px;display:flex;align-items:center;justify-content:center">{n}</span>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:20px;color:#2a2016">{label}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("It plans before it builds","ARCHITECT",ink="#2a2016")}
      <div style="position:relative;height:410px">
        <svg width="800" height="410" viewBox="0 0 800 410" style="position:absolute;left:0;top:0">
          {edges}
          <rect x="30" y="{gy-58}" width="220" height="116" rx="20" fill="#2a2016"/>
          <text x="140" y="{gy-14}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">GOAL</text>
          <text x="140" y="{gy+16}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="21" fill="#fdfbf6">Billing page</text>
          <text x="140" y="{gy+42}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#c9b79a">plain English</text>
        </svg>
        {chips}
      </div>
      {cap("brainstorm, plan, then build. the fix for rushed AI slop.","#8a745a")}</div>'''

# 3. BUILDER - isometric assembly, the top layer is the shipped product SCREEN (not code)
def builder():
    tile=lambda lbl,val:(f'<div style="flex:1;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.3);border-radius:12px;padding:12px 14px">'
        f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:rgb({ACC})">{lbl}</div>'
        f'<div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#FAFAF7;margin-top:3px">{val}</div></div>')
    screen=(f'<div style="width:560px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.1)">'
        f'<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">'
        f'<span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">Billing</span>'
        f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:999px;padding:4px 12px">LIVE</span></div>'
        f'<div style="display:flex;gap:14px;margin-bottom:16px">{tile("PLAN","Active")}{tile("SEATS","5")}{tile("RENEWS","Jul 30")}</div>'
        f'<svg width="512" height="70" viewBox="0 0 512 70"><polyline points="0,54 70,44 140,48 210,30 280,36 350,18 420,24 500,8" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<circle cx="500" cy="8" r="6" fill="rgb({ACC})"/></svg></div>')
    back=lambda lbl,y:(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1.5px solid rgba(255,255,255,.1);border-radius:18px;padding:16px 22px;box-shadow:0 24px 40px rgba(0,0,0,.5);display:flex;align-items:center;gap:14px">'
        f'<span style="width:10px;height:10px;border-radius:50%;background:rgb({ACC})"></span>'
        f'<span style="font-family:DM Mono;font-size:15px;color:#a8a296">{lbl}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("It ships a screen, not a snippet","BUILDER")}
      <div style="perspective:2000px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">
          {back("data_model.ts",0)}{back("api/billing",96)}
          <div style="position:absolute;left:0;top:192px">{screen}</div>
        </div></div>
      {cap("plain English in, a working product page out.")}</div>'''

# 4. TESTER - a packed grid of passing checks, one regression caught in red
def tester():
    cols,rows=8,5; caught=27
    cell,gap=42,12
    marks=""
    for i in range(cols*rows):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i==caught:
            marks+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="11" fill="rgba(200,70,35,.16)" stroke="rgb(200,70,35)" stroke-width="2"/>'
              f'<path d="M{x+13} {y+13} l16 16 M{x+29} {y+13} l-16 16" stroke="rgb(200,70,35)" stroke-width="3" stroke-linecap="round"/>')
        else:
            marks+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="11" fill="rgba(212,162,127,.16)" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>'
              f'<path d="M{x+12} {y+22} l7 7 l11 -14" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    fw=cols*(cell+gap)-gap; fh=rows*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">40</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">checks, every change</span></div>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb(200,70,35)">1 CAUGHT</span></div>
      <div style="display:flex;align-items:center;gap:36px">
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="flex-shrink:0">{marks}</svg>
        <div style="flex:1">
          <div style="background:rgba(200,70,35,.1);border-left:4px solid rgb(200,70,35);border-radius:12px;padding:16px 18px">
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb(200,70,35)">REGRESSION CAUGHT</div>
            <div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7;margin-top:5px">Discount stacked twice on renewal</div>
            <div style="font-family:DM Sans;font-size:15px;color:#a8a296;margin-top:6px">fixed before it ever reached a customer</div></div></div>
      </div>
      {cap("it writes the tests too, and catches the one that would break.")}</div>'''

# 5. REVIEWER - annotated review threads on a diff, one blocker flagged then cleared
def reviewer():
    rows=[("billing.ts:42","missing null check on trial users","block"),
          ("form.tsx:16","rename amt to amountDue","nit"),
          ("api/route.ts:88","add rate limit to webhook","nit")]
    chips=""
    for loc,note,sev in rows:
        red=(sev=="block")
        dot="rgb(200,70,35)" if red else f"rgb({ACC})"
        tag=("BLOCKS MERGE" if red else "nit")
        tagc="rgb(200,70,35)" if red else "#8f8f85"
        bd="rgba(200,70,35,.4)" if red else "rgba(255,255,255,.1)"
        chips+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid {bd};border-radius:16px;padding:15px 18px;box-shadow:0 14px 26px rgba(0,0,0,.45)">'
          f'<span style="flex-shrink:0;width:11px;height:11px;border-radius:50%;background:{dot};box-shadow:0 0 10px {dot}"></span>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:15px;color:#eae4d8;width:158px">{loc}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-size:17px;color:#c9c3b8">{note}</span>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:{tagc}">{tag}</span></div>')
    verdict=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(212,162,127,.1);border:1px solid rgba(212,162,127,.34);border-radius:16px;padding:16px 20px;margin-top:16px">'
      f'<svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.18)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">1 blocker fixed</span>'
      f'<span style="font-family:DM Sans;font-size:17px;color:#a8a296">then approved for merge</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A second set of eyes on every diff","REVIEWER")}
      <div style="display:flex;flex-direction:column;gap:12px">{chips}</div>
      {verdict}
      {cap("it catches the bug in review, before your users ever do.")}</div>'''

# 6. DOCS - IVORY changelog document written on merge
def docs():
    entries=[("Added","one-click billing page for founder plans"),
             ("Added","renewal reminders 3 days before charge"),
             ("Fixed","double discount on annual renewals"),
             ("Changed","trial length from 7 to 14 days")]
    rowsh=""
    for kind,text in entries:
        rowsh+=(f'<div style="display:flex;align-items:baseline;gap:14px;padding:11px 0;border-bottom:1px solid rgba(120,95,60,.16)">'
          f'<span style="flex-shrink:0;width:74px;font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:#96562d">{kind}</span>'
          f'<span style="font-family:DM Sans;font-size:19px;color:#2a2016">{text}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("It writes the docs you skip","DOCS",ink="#2a2016")}
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px">
        <span style="font-family:DM Mono;font-size:15px;letter-spacing:.16em;color:#96562d">CHANGELOG</span>
        <div style="display:flex;align-items:center;gap:12px">
          <span style="font-family:DM Sans;font-weight:900;font-size:18px;color:#2a2016;background:rgba(150,90,45,.12);border-radius:999px;padding:5px 14px">v1.4.0</span>
          <span style="font-family:DM Mono;font-size:14px;color:#8a745a">2026-07-04</span></div></div>
      <div>{rowsh}</div>
      {cap("every change logged on merge, so future you is never lost.","#8a745a")}</div>'''

# 7. SHIP - the run timeline on the left lands as a wax-sealed MERGED pull request on the right
def ship():
    stages=[("Plan","Architect","09:02"),("Build","Builder","09:14"),("Test","Tester","09:20"),
            ("Review","Reviewer","09:24"),("Merge","all clear","09:26")]
    tl=""; n=len(stages); step=88; y0=24
    for i,(st,who,t) in enumerate(stages):
        y=y0+i*step; last=(i==n-1)
        col=f"rgb({ACC})" if last else "rgba(212,162,127,.55)"
        if i<n-1: tl+=f'<line x1="26" y1="{y}" x2="26" y2="{y+step}" stroke="rgba(212,162,127,.34)" stroke-width="2.4"/>'
        tl+=(f'<circle cx="26" cy="{y}" r="10" fill="{col}"/>'
          f'<text x="52" y="{y-4}" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{st}</text>'
          f'<text x="52" y="{y+18}" font-family="DM Sans" font-size="14" fill="#8f8f85">{who}</text>'
          f'<text x="300" y="{y+4}" text-anchor="end" font-family="DM Mono" font-size="14" fill="rgb({ACC})">{t}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <div style="flex:1">
        {htitle("The whole team, one PR","SHIPPED")}
        <svg width="320" height="460" viewBox="0 0 320 460">{tl}</svg>
      </div>
      <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center">
        <svg width="290" height="290" viewBox="0 0 290 290">
          <defs><radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <radialGradient id="sb" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.5)"/><stop offset="62%" stop-color="rgba(204,120,92,.1)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
          <filter id="ss" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="rgba(0,0,0,.6)"/></filter>
          <filter id="sp" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="8"/></filter></defs>
          <circle cx="145" cy="145" r="140" fill="url(#sb)"/>
          <g filter="url(#ss)">{"".join(f'<line x1="145" y1="145" x2="{145+128*math.cos(math.radians(a)):.0f}" y2="{145+128*math.sin(math.radians(a)):.0f}" stroke="#8a4c2c" stroke-width="10"/>' for a in range(0,360,15))}
          <circle cx="145" cy="145" r="118" fill="url(#seal)"/></g>
          <circle cx="145" cy="145" r="118" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
          <circle cx="145" cy="145" r="96" fill="none" stroke="rgba(26,15,10,.28)" stroke-width="2"/>
          <text x="145" y="138" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" letter-spacing="1" fill="#1a0f0a">MERGED</text>
          <text x="145" y="172" text-anchor="middle" font-family="DM Mono" font-size="16" letter-spacing="2" fill="#2a160c">PR #182</text>
          <ellipse cx="110" cy="96" rx="44" ry="24" fill="rgba(255,255,255,.28)" filter="url(#sp)" transform="rotate(-32 110 96)"/></svg>
        <div style="font-family:DM Mono;font-size:14px;color:#8f8f85;margin-top:8px">live on main</div>
      </div>
      {cap("plan, build, test, review, docs: one clean PR you approve.")}</div>'''

# 8. OPERATOR - 5 role nodes converge through the HUMAN GATE into one shipped release
def operator():
    scat=[("architect",70,80),("builder",70,175),("tester",70,270),("reviewer",70,350),("docs",190,215)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+30} {y} C320 {y},350 220,430 220" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.82"/>'
          f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Five roles, one terminal","HUMAN GATE")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="rel" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <rect x="430" y="150" width="90" height="140" rx="20" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(451,196)"><rect x="0" y="30" width="48" height="38" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/><path d="M9 30 V19 a15 15 0 0 1 30 0 v11" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/></g>
        <text x="475" y="316" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">your tap</text>
        <path d="M520 220 H588" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>
        <g filter="url(#rg)"><circle cx="680" cy="220" r="112" fill="url(#rel)"/></g>
        <text x="680" y="208" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">SHIPPED</text>
        <text x="680" y="240" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010">v1.4 on main</text>
      </svg>
      {cap("you run the team from one line, and you still hold the merge.")}</div>'''

PANELS={"org":org(),"architect":architect(),"builder":builder(),"tester":tester(),
        "reviewer":reviewer(),"docs":docs(),"ship":ship(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src31"; os.makedirs(outd,exist_ok=True)
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
