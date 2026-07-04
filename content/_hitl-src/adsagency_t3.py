#!/usr/bin/env python3
# TIER 3 - THE AD DESK, IN-HOUSE, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one mono caption, NO generic stat-chip strips.
# Warm palette only. Ultron actions are CENTS; high $ appears ONLY as the agency/competitor cost.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"        # warm kraft accent
IV="#96562d"             # ivory-accent (dark warm ink on cream)
RED="rgb(200,70,35)"     # muted red, BAD only
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'

def htitle(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IV}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:18px">{t}</div>'

# 1. RETAINER - agency invoice (HIGH $ = competitor cost, allowed) + billed-monthly / delivered-quarterly gap
def retainer():
    items=[("Research & strategy","$2,400"),("Copywriting, 4 concepts","$3,600"),("Creative audits","$2,000")]
    rows=""
    for a,b in items:
        rows+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
          f'<span style="font-family:DM Sans;font-size:19px;color:#cfc9bd">{a}</span>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#a8a296">{b}</span></div>')
    billed=""
    for m in ("JAN","FEB","MAR"):
        billed+=(f'<div style="display:flex;align-items:center;gap:12px;background:#211e1a;border:1px solid rgba(255,255,255,.08);border-radius:12px;padding:11px 15px">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#9a9488;width:38px">{m}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-size:15px;color:#cfc9bd">billed</span>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:16px;color:#c9c3b8">$8,000</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("What the retainer bought","AGENCY COST")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1.15;background:linear-gradient(158deg,#302c27,#201d19);border:1px solid rgba(255,255,255,.09);border-radius:20px;padding:22px 26px;box-shadow:0 20px 40px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.06)">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:rgb({ACC});margin-bottom:8px">MONTHLY RETAINER</div>
          {rows}
          <div style="display:flex;justify-content:space-between;align-items:baseline;padding-top:16px;margin-top:4px">
            <span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#e2dccf">Billed every month</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7">$8,000</span></div>
        </div>
        <div style="flex:.85;display:flex;flex-direction:column;gap:11px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#8f8f85">BILLED MONTHLY</div>
          {billed}
          <div style="height:2px;background:repeating-linear-gradient(90deg,{RED} 0 8px,transparent 8px 16px);margin:4px 2px"></div>
          <div style="display:flex;align-items:center;gap:12px;background:rgba(200,70,35,.10);border:1px solid rgba(200,70,35,.4);border-radius:12px;padding:13px 15px">
            <span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{RED};width:38px">Q2</span>
            <span style="flex:1;font-family:DM Sans;font-size:15px;color:#d9b3a3">delivered</span>
            <span style="font-family:DM Sans;font-weight:700;font-size:16px;color:{RED}">1 deck</span></div>
        </div>
      </div>
      {cap("research, copy and audits billed every month, the deck lands a quarter late.")}</div>'''

# 2. SPY - grid of rival ad thumbnails, the week's new creatives flagged (thumbnail wall, unique form)
def spy():
    ads=[("Northwind","PRICE",False),("Globex","SPEED",True),("Initech","TRUST",False),
         ("Umbrella","FEAR",True),("Hooli","PROOF",False),("Stark","BUNDLE",False)]
    tiles=""
    for brand,ang,new in ads:
        badge=(f'<span style="position:absolute;top:10px;right:10px;font-family:DM Mono;font-size:10px;letter-spacing:.1em;color:#1a0f0a;background:rgb({ACC});padding:3px 8px;border-radius:6px;font-weight:700">NEW</span>' if new else '')
        bd=f"1.5px solid rgba(212,162,127,.55)" if new else "1px solid rgba(255,255,255,.08)"
        tiles+=(f'<div style="position:relative;background:linear-gradient(160deg,#2f2b27,#211e1a);border:{bd};border-radius:16px;padding:15px 16px;box-shadow:0 12px 24px rgba(0,0,0,.4)">'
          f'{badge}'
          f'<div style="height:34px;border-radius:8px;background:linear-gradient(120deg,rgba(212,162,127,.30),rgba(212,162,127,.08));margin-bottom:12px"></div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:17px;color:#FAFAF7">{brand}</div>'
          f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#9a9488;margin-top:3px">ANGLE · {ang}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Rival ads, diffed weekly","COMPETITOR WATCH")}
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">{tiles}</div>
      <div style="display:flex;gap:26px;margin-top:18px">
        <div style="display:flex;align-items:center;gap:9px"><span style="width:12px;height:12px;border-radius:4px;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:16px;color:#d9d5cc">2 launched this week</span></div>
        <div style="display:flex;align-items:center;gap:9px"><span style="width:12px;height:12px;border-radius:4px;background:{RED}"></span><span style="font-family:DM Sans;font-size:16px;color:#d9d5cc">1 killed by Hooli</span></div>
      </div>
      {cap("every creative your competitors launched, pulled into one monday report.")}</div>'''

# 3. GAP - IVORY bar chart: hook angles ranked by how many rivals run them, the open lane is yours
def gap():
    angles=[("Discount / price",17),("Speed / time saved",13),("Social proof",11),("Fear of missing out",8),("Founder story",4),("Cost of the tool stack",1)]
    mx=17; barw=470
    bars=""
    for i,(nm,v) in enumerate(angles):
        yours=(i==len(angles)-1)
        w=max(14,int(barw*v/mx))
        col=IV if not yours else f"rgb({ACC})"
        fill=(f"linear-gradient(90deg,#b5713f,{IV})" if not yours else f"linear-gradient(90deg,rgb({ACC}),#e0b98f)")
        lbl=(f'<span style="font-family:DM Mono;font-size:13px;color:{IV};margin-left:12px">{v} ads</span>' if not yours
             else f'<span style="font-family:DM Mono;font-size:13px;font-weight:500;color:#8a4a1f;margin-left:12px">open lane</span>')
        border=(f"box-shadow:0 0 0 2px rgba(212,162,127,.55)" if yours else "")
        bars+=(f'<div style="display:flex;align-items:center;margin-bottom:15px">'
          f'<span style="width:250px;font-family:DM Sans;font-weight:{800 if yours else 500};font-size:18px;color:{"#8a4a1f" if yours else "#4a3a28"}">{nm}</span>'
          f'<div style="display:flex;align-items:center"><div style="width:{w}px;height:30px;border-radius:8px;background:{fill};{border}"></div>{lbl}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htiv("The angle nobody runs","HOOK COVERAGE")}
      <div style="margin-top:6px">{bars}</div>
      {cap("hooks ranked by how many rivals use them; the empty lane becomes yours.","#8a745a")}</div>'''

# 4. VARIATIONS - iso fanned deck: one description spawns 20 variation cards, short/medium/long
def variations():
    fan=""
    labels=[("v01","SHORT"),("v08","MEDIUM"),("v14","MEDIUM"),("v20","LONG")]
    for i,(vid,ln) in enumerate(labels):
        off=i*104
        fan+=(f'<div style="position:absolute;left:{off}px;top:{i*22}px;width:300px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:16px;padding:18px 20px;box-shadow:0 30px 46px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1)">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">{vid}</span><span style="font-family:DM Mono;font-size:11px;color:#8f8f85">{ln}</span></div>'
          f'<div style="height:9px;border-radius:5px;background:rgba(250,250,247,.14);margin-top:14px"></div>'
          f'<div style="height:9px;border-radius:5px;background:rgba(250,250,247,.10);margin-top:9px;width:78%"></div>'
          f'<div style="height:9px;border-radius:5px;background:rgba(250,250,247,.07);margin-top:9px;width:56%"></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Twenty, from one line","ONE BRIEF")}
      <div style="display:flex;align-items:center;gap:24px">
        <div style="flex-shrink:0;width:180px;background:#211e1a;border:1px dashed rgba(212,162,127,.5);border-radius:16px;padding:20px 18px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC});margin-bottom:10px">YOUR BRIEF</div>
          <div style="font-family:DM Sans;font-size:16px;color:#d9d5cc;line-height:1.4">"cold DM tool, for founders, playful"</div>
        </div>
        <svg width="46" height="30" style="flex-shrink:0"><path d="M4 15 H40 M30 6 l10 9 l-10 9" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="perspective:1800px;flex:1;height:300px;display:flex;align-items:center">
          <div style="transform-style:preserve-3d;transform:rotateX(15deg) rotateZ(-7deg);position:relative;width:610px;height:200px">{fan}
            <div style="position:absolute;right:-6px;top:150px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:22px;padding:10px 20px;border-radius:999px;box-shadow:0 12px 26px rgba(212,162,127,.45)">20 ready</div>
          </div>
        </div>
      </div>
      {cap("short, medium and long: in your voice, checked against your brand rules.")}</div>'''

# 5. AUDIT - IVORY semicircle health gauge + a fix list (186 checks) -> arc dial, unique form
def audit():
    score=74; f=score/100
    cx,cy,r=175,158,135
    def pt(A,rr):
        return (cx+rr*math.cos(math.radians(A)), cy-rr*math.sin(math.radians(A)))
    def arc(a0,a1,rr,steps=60):
        p=[]
        for k in range(steps+1):
            A=a0+(a1-a0)*k/steps; x,y=pt(A,rr); p.append(f"{x:.1f},{y:.1f}")
        return " ".join(p)
    track=arc(180,0,r); val=arc(180,180-f*180,r)
    nx,ny=pt(180-f*180,r-14)
    ticks=""
    for tk in range(0,101,20):
        A=180-tk*1.8; x0,y0=pt(A,r+6); x1,y1=pt(A,r+20)
        ticks+=f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="rgba(120,90,55,.4)" stroke-width="2"/>'
    fixes=[("Fatigue","3 ads past their peak"),("Overlap","2 sets bidding on each other"),("Anomaly","1 spend spike, 4x median")]
    fx=""
    for a,b in fixes:
        fx+=(f'<div style="display:flex;align-items:center;gap:13px;margin-bottom:13px">'
          f'<span style="flex-shrink:0;width:28px;height:28px;border-radius:8px;background:rgba(150,86,45,.14);border:1px solid rgba(150,86,45,.4);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:16px;color:{IV}">!</span>'
          f'<div><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#2a2016">{a}</span>'
          f'<span style="font-family:DM Sans;font-size:16px;color:#7a634a;margin-left:8px">{b}</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htiv("186 checks, one score","CREATIVE AUDIT")}
      <div style="display:flex;align-items:center;gap:20px">
        <div style="flex-shrink:0;position:relative;width:350px;height:250px">
          <svg width="350" height="250" viewBox="0 0 350 250">
            <polyline points="{track}" fill="none" stroke="rgba(150,120,80,.22)" stroke-width="20" stroke-linecap="round"/>
            <polyline points="{val}" fill="none" stroke="{IV}" stroke-width="20" stroke-linecap="round"/>
            {ticks}
            <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#3a2a1a" stroke-width="5" stroke-linecap="round"/>
            <circle cx="{cx}" cy="{cy}" r="9" fill="#3a2a1a"/>
          </svg>
          <div style="position:absolute;left:0;right:0;top:176px;text-align:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:50px;color:#2a2016">{score}</span>
            <span style="font-family:DM Sans;font-weight:700;font-size:22px;color:{IV}">/100</span>
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#96562d;margin-top:2px">HEALTH SCORE</div></div>
        </div>
        <div style="flex:1;background:rgba(255,255,255,.5);border-radius:16px;padding:20px 22px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{IV};margin-bottom:14px">FIX LIST ATTACHED</div>
          {fx}</div>
      </div>
      {cap("fatigue, overlap and anomalies, caught before the next budget moves.","#8a745a")}</div>'''

# 6. SCORE - hexagon radar, six dimensions, one ad plotted; weak hook flagged for rewrite
def score():
    cx,cy,R=220,225,165
    dims=[("HOOK",.5),("CLARITY",.85),("OFFER",.9),("PROOF",.7),("CTA",.8),("BRAND",.95)]
    grid=""
    for gf in (.33,.66,1.0):
        pts=[]
        for i in range(6):
            A=-90+i*60; x=cx+R*gf*math.cos(math.radians(A)); y=cy+R*gf*math.sin(math.radians(A)); pts.append(f"{x:.0f},{y:.0f}")
        grid+=f'<polygon points="{" ".join(pts)}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="1.5"/>'
    spokes=""; labels=""; vpts=[]
    for i,(nm,v) in enumerate(dims):
        A=-90+i*60; ax=cx+R*math.cos(math.radians(A)); ay=cy+R*math.sin(math.radians(A))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{ax:.0f}" y2="{ay:.0f}" stroke="rgba(212,162,127,.14)" stroke-width="1.5"/>'
        vx=cx+R*v*math.cos(math.radians(A)); vy=cy+R*v*math.sin(math.radians(A)); vpts.append(f"{vx:.0f},{vy:.0f}")
        weak=(nm=="HOOK")
        lx=cx+(R+34)*math.cos(math.radians(A)); ly=cy+(R+34)*math.sin(math.radians(A))
        col=RED if weak else "#cfc9bd"
        labels+=f'<text x="{lx:.0f}" y="{ly+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="{col}">{nm}</text>'
    dots=""
    for i,(nm,v) in enumerate(dims):
        A=-90+i*60; vx=cx+R*v*math.cos(math.radians(A)); vy=cy+R*v*math.sin(math.radians(A))
        c=RED if nm=="HOOK" else f"rgb({ACC})"
        dots+=f'<circle cx="{vx:.0f}" cy="{vy:.0f}" r="6" fill="{c}"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="470" height="470" viewBox="0 0 470 470" style="flex-shrink:0">
        {grid}{spokes}
        <polygon points="{" ".join(vpts)}" fill="rgba(212,162,127,.20)" stroke="rgb({ACC})" stroke-width="2.5"/>
        {dots}{labels}</svg>
      <div style="flex:1">
        {htitle("Scored six ways","SCORECARD")}
        <div style="display:flex;align-items:baseline;gap:12px;margin-bottom:16px">
          <span style="font-family:DM Sans;font-weight:900;font-size:52px;color:#FAFAF7">78</span>
          <span style="font-family:DM Sans;font-weight:700;font-size:20px;color:#c9a583">/ 100 overall</span></div>
        <div style="background:rgba(200,70,35,.10);border:1px solid rgba(200,70,35,.4);border-radius:14px;padding:16px 18px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{RED};margin-bottom:6px">WEAKEST: HOOK 50</div>
          <div style="font-family:DM Sans;font-size:17px;color:#d9d5cc;line-height:1.4">rewritten before launch, not sent as-is.</div></div>
        {cap("six dimensions per ad; weak hooks get rewritten, not run.")}
      </div></div>'''

# 7. CHAIN - the retainer month as one linear pipeline of 5 stages, timed under an hour
def chain():
    stages=[("SPY","rivals pulled"),("GAP","angle found"),("DRAFT","20 written"),("AUDIT","186 checks"),("SCORE","78 / 100")]
    W,H=820,300
    n=len(stages); x0=54; step=(W-2*x0)/(n-1); y=118
    edges=""; nodes=""
    for i in range(n-1):
        xa=x0+i*step; xb=x0+(i+1)*step
        edges+=f'<line x1="{xa+40:.0f}" y1="{y}" x2="{xb-40:.0f}" y2="{y}" stroke="rgb({ACC})" stroke-width="4" opacity="0.85"/>'
    for i,(nm,sub) in enumerate(stages):
        x=x0+i*step
        nodes+=(f'<circle cx="{x:.0f}" cy="{y}" r="40" fill="#221f1b" stroke="rgb({ACC})" stroke-width="2.5"/>'
          f'<circle cx="{x:.0f}" cy="{y}" r="40" fill="url(#ng)" opacity="0.5"/>'
          f'<text x="{x:.0f}" y="{y+6:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#FAFAF7">{i+1}</text>'
          f'<text x="{x:.0f}" y="{y-58:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="rgb({ACC})">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+74:.0f}" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#a8a296">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The month, done by lunch","ONE CHAIN")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="ng" cx="38%" cy="30%"><stop offset="0%" stop-color="rgba(212,162,127,.55)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient></defs>
        {edges}{nodes}
        <g transform="translate({W//2-96},232)">
          <rect x="0" y="0" width="192" height="52" rx="26" fill="#211e1a" stroke="rgb({ACC})" stroke-width="1.5"/>
          <circle cx="30" cy="26" r="13" fill="none" stroke="rgb({ACC})" stroke-width="2.5"/><line x1="30" y1="26" x2="30" y2="18" stroke="rgb({ACC})" stroke-width="2.5" stroke-linecap="round"/><line x1="30" y1="26" x2="36" y2="30" stroke="rgb({ACC})" stroke-width="2.5" stroke-linecap="round"/>
          <text x="112" y="33" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">58 min</text>
        </g>
      </svg>
      {cap("spy, gap, draft, audit, score: chained end to end, under an hour.")}</div>'''

# 8. SIGN - the human gate: a launch queued, HELD, waiting on your tap to sign (approval UI, unique)
def sign():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Every launch signs with your tap","HUMAN GATE")}
      <div style="background:linear-gradient(158deg,#2f2b27,#201d19);border:1px solid rgba(255,255,255,.09);border-radius:22px;padding:26px 28px;box-shadow:0 24px 46px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.06)">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px">
          <div><div style="font-family:DM Sans;font-weight:800;font-size:24px;color:#FAFAF7">Spring push, 6 variations</div>
          <div style="font-family:DM Sans;font-size:16px;color:#8f8f85;margin-top:2px">scored 78, audited clean, ready to run</div></div>
          <div style="display:flex;align-items:center;gap:9px;background:rgba(200,70,35,.12);border:1px solid rgba(200,70,35,.4);border-radius:999px;padding:8px 16px">
            <span style="width:9px;height:9px;border-radius:50%;background:{RED}"></span>
            <span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{RED}">HELD</span></div>
        </div>
        <div style="display:flex;align-items:stretch;gap:16px">
          <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:11px">
            {"".join(f'<div style="display:flex;align-items:center;gap:11px"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.6"><path d="M6 12.5l3.5 3.5L18 7.5" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:DM Sans;font-size:17px;color:#d9d5cc">{t}</span></div>' for t in ["nothing spends before you sign","every draft traceable to its brief","one tap launches, one tap holds"])}
          </div>
          <div style="flex-shrink:0;width:2px;background:rgba(255,255,255,.08)"></div>
          <div style="flex-shrink:0;width:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="1.6"><path d="M12 11c0-2 0-5 0-5a3 3 0 0 1 3 3v6"/><path d="M9 11V6a3 3 0 0 0-3 3v6a6 6 0 0 0 6 6 6 6 0 0 0 6-6v-3" stroke-linecap="round"/><path d="M9 11v3"/><path d="M12 11v4"/><path d="M15 12v3"/></svg>
            <div style="display:flex;align-items:center;gap:12px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 55%,#9a5a35);border-radius:999px;padding:15px 30px;box-shadow:0 14px 30px rgba(212,162,127,.4), inset 0 2px 3px rgba(255,255,255,.4)">
              <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#1a0f0a">TAP TO SIGN</span></div>
          </div>
        </div>
      </div>
      {cap("nothing spends without you. in-house means in your hands.")}</div>'''

PANELS={"retainer":retainer(),"spy":spy(),"gap":gap(),"variations":variations(),
        "audit":audit(),"score":score(),"chain":chain(),"sign":sign()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/adsagency"; os.makedirs(outd,exist_ok=True)
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
