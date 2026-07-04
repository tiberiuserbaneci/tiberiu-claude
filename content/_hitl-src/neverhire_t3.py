#!/usr/bin/env python3
# TIER 3 - THE HIRING FREEZE, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# 8 stems: leadgen / support / content / followups / reviews / math / line / test.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"      # warm accent
IVACC="#96562d"        # ivory-card accent
BAD="200,70,35"        # muted red, ONLY for the frozen/human/bad side
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IVACC}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LEADGEN - isometric stack of scored ICP briefs, CORTEX runs it overnight
def leadgen():
    rows=[("Northwind Robotics","hiring 3 ops roles, US","94"),
          ("Globex Systems","raised $4M Series A","89"),
          ("Initech Group","no AI layer yet","82")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*140
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;'
          f'background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;'
          f'padding:20px 24px;box-shadow:0 32px 48px rgba(0,0,0,.58), inset 0 2px 2px rgba(255,255,255,.10);'
          f'display:flex;align-items:center;gap:20px">'
          f'<div style="flex:1;text-align:left"><div style="font-family:DM Sans;font-weight:800;font-size:24px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:DM Sans;font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>'
          f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:8px 16px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{c}</span>'
          f'<span style="font-family:DM Mono;font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">FIT</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Sourced and scored overnight","LEAD GEN")}
      <div style="perspective:1950px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:580px;height:420px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:410px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">28 briefs &middot; on your desk 07:00</div></div></div>
      {cap("CORTEX runs your ICP every night - sourced, scored, briefed before you wake.")}</div>'''

# 2. SUPPORT - node flow: inbox -> triage hub -> most drafted, the rare hard case escalates to you
def support():
    W,H=810,440
    tickets=[("refund query",92),("bug report",172),("how do I...",252),("angry churn",332)]
    edges=""; nodes=""
    hubx,huby=410,212
    for nm,y in tickets:
        col=f"rgba({BAD},.55)" if nm=="angry churn" else "rgba(212,162,127,.5)"
        edges+=f'<path d="M182 {y} C300 {y},300 {huby},{hubx-72} {huby}" stroke="{col}" stroke-width="2.6" fill="none"/>'
        nodes+=(f'<rect x="40" y="{y-26}" width="142" height="52" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="111" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14.5" fill="#c9c3b8">{nm}</text>')
    # two outputs: drafted (most) and escalate (rare)
    out=(f'<path d="M{hubx+72} {huby-30} C600 {huby-30},600 130,690 130" stroke="rgba(212,162,127,.5)" stroke-width="2.6" fill="none"/>'
         f'<path d="M{hubx+72} {huby+30} C600 {huby+30},600 320,690 320" stroke="rgba({BAD},.6)" stroke-width="2.6" fill="none"/>'
         f'<rect x="628" y="98" width="150" height="64" rx="14" fill="#241f1a" stroke="rgba(212,162,127,.34)"/>'
         f'<text x="703" y="126" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">Drafted reply</text>'
         f'<text x="703" y="147" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">83% of inbox</text>'
         f'<rect x="628" y="288" width="150" height="64" rx="14" fill="#2a1a15" stroke="rgba({BAD},.5)"/>'
         f'<text x="703" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#f0d8cf">Escalated to you</text>'
         f'<text x="703" y="337" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({BAD})">with context</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Read, sorted, drafted","SUPPORT TRIAGE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{out}{nodes}
        <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="70" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">TRIAGE</text>
        <text x="{hubx}" y="{huby+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads every one</text>
      </svg>
      {cap("the inbox clears itself - only the rare hard case reaches you, context attached.")}</div>'''

# 3. CONTENT - IVORY timeline: fourteen slots across a week, all queued at 10:00 local
def content():
    W,H=760,360
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    x0,dx=48,100; baseline=250
    slots={0:2,1:2,2:2,3:2,4:2,5:1,6:1}  # 14 total
    dots=""; labels=""; guide=""
    for i,d in enumerate(days):
        x=x0+i*dx
        labels+=f'<text x="{x}" y="{baseline+44}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#8a745a">{d}</text>'
        labels+=f'<line x1="{x}" y1="70" x2="{x}" y2="{baseline}" stroke="rgba(150,90,45,.14)"/>'
        n=slots[i]
        for k in range(n):
            yy=baseline-24-k*46
            dots+=(f'<circle cx="{x}" cy="{yy}" r="15" fill="#f6ede0" stroke="{IVACC}" stroke-width="3"/>'
              f'<path d="M{x-6} {yy} l4 4 l8 -9" fill="none" stroke="{IVACC}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
    guide=f'<line x1="{x0-14}" y1="{baseline}" x2="{x0+6*dx+14}" y2="{baseline}" stroke="rgba(150,90,45,.30)" stroke-width="2"/>'
    clock=(f'<g transform="translate({x0+6*dx-4},64)"><rect x="-58" y="-20" width="116" height="34" rx="17" fill="{IVACC}"/>'
      f'<text x="0" y="3" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#fdfbf6">10:00 LOCAL</text></g>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("Fourteen slots from one line","CONTENT OPS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:6px auto 0">
        {labels}{guide}{dots}{clock}
      </svg>
      {cap("one line in, a full week of drafts in your voice, queued at 10:00 every day.","#8a745a")}</div>'''

# 4. FOLLOWUPS - radial hub: quiet threads around a core, each fires on its own trigger, sends parked
def followups():
    cx,cy=232,224; R=168
    threads=[("opened, no reply","-90"),("visited pricing","-18"),("demo, went quiet","54"),
             ("champion left","126"),("renewal in 30d","198")]
    spokes=""; nodes=""
    for nm,a in threads:
        ang=float(a)
        x=cx+R*math.cos(math.radians(ang)); y=cy+R*math.sin(math.radians(ang))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.45)" stroke-width="2.4"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#fg)"/>'
          f'<text x="{x:.0f}" y="{y-18:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#cfc9bd">{nm}</text>')
    parked=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px"><svg width="22" height="22" viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="9" rx="2" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><path d="M8 11 V8 a4 4 0 0 1 8 0 v3" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/></svg>'
      f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">Parked for your tap</span></div>'
      f'<div style="font-family:DM Sans;font-size:16px;color:#a8a296;line-height:1.4">9 drafts queued, each fired by its own trigger. Nothing sends until you approve.</div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:12px;font-family:DM Mono;font-size:14px;color:rgb({ACC})">SPECTER &middot; 0 threads dropped</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="464" height="464" viewBox="0 0 464 464">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="fg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(212,162,127,.14)"/>
        <circle cx="{cx}" cy="{cy}" r="{R-56}" fill="none" stroke="rgba(212,162,127,.10)"/>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">CHASED</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">on trigger</text>
        {nodes}
      </svg>
      <div style="flex:1">
        {htitle("Quiet threads, chased","SALES FOLLOW-UPS")}
        {parked}
        {cap("every stalled deal watched, chased when it moves - you only tap send.")}
      </div></div>'''

# 5. REVIEWS - IVORY gauge: ask-to-review conversion dial + logged rating
def reviews():
    pct=59; r=118; circ=math.pi*r; dash=circ*pct/100  # semicircle
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("Asked, chased, logged","REVIEW COLLECTION")}
      <div style="display:flex;align-items:center;gap:40px">
        <div style="flex-shrink:0;position:relative;width:300px;height:186px">
          <svg width="300" height="186" viewBox="0 0 300 186">
            <path d="M32 168 A118 118 0 0 1 268 168" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="22" stroke-linecap="round"/>
            <path d="M32 168 A118 118 0 0 1 268 168" fill="none" stroke="{IVACC}" stroke-width="22" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}"/>
          </svg>
          <div style="position:absolute;left:0;right:0;top:96px;text-align:center">
            <div style="font-family:DM Sans;font-weight:900;font-size:56px;color:#2a2016;line-height:1">{pct}%</div>
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:{IVACC}">asked &rarr; reviewed</div></div>
        </div>
        <div style="flex:1">
          <div style="display:flex;gap:5px;margin-bottom:14px">
            {"".join(f'<svg width="34" height="34" viewBox="0 0 24 24"><path d="M12 2l2.9 6.2 6.8.8-5 4.6 1.3 6.7L12 17.8 5.7 20.3 7 13.6 2 9l6.8-.8Z" fill="{IVACC}"/></svg>' for _ in range(4))}
            <svg width="34" height="34" viewBox="0 0 24 24"><path d="M12 2l2.9 6.2 6.8.8-5 4.6 1.3 6.7L12 17.8 5.7 20.3 7 13.6 2 9l6.8-.8Z" fill="none" stroke="{IVACC}" stroke-width="1.6"/></svg>
          </div>
          <div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#2a2016;line-height:1.05">4.8 avg<br><span style="font-size:20px;font-weight:700;color:#5a4634">from 126 collected</span></div>
          <div style="display:flex;gap:24px;margin-top:16px">
            {"".join(f'<div style="text-align:left"><div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#2a2016">{v}</div><div style="font-family:DM Mono;font-size:12px;color:#8a745a">{lb}</div></div>' for v,lb in [("214","asked"),("3","polite chases"),("0","you touched")])}
          </div>
        </div>
      </div>
      {cap("asked at the right moment, chased politely, logged where you already look.","#8a745a")}</div>'''

# 6. MATH - headcount-vs-agents bars: five salaries you did NOT hire vs the desk at cents
def math_panel():
    roles=[("SDR / lead gen","$54k",54),("Support rep","$44k",44),("Content marketer","$58k",58),
           ("Sales ops","$52k",52),("Community / reviews","$40k",40)]
    maxk=58; barw=430
    bars=""
    for nm,lab,k in roles:
        w=int(k/maxk*barw)
        bars+=(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:13px">'
          f'<div style="width:186px;text-align:right;font-family:DM Sans;font-size:16px;color:#c9c3b8">{nm}</div>'
          f'<div style="width:{barw}px;height:26px;background:rgba(255,255,255,.05);border-radius:7px;position:relative">'
          f'<div style="width:{w}px;height:26px;background:linear-gradient(90deg,rgba({BAD},.5),rgba({BAD},.85));border-radius:7px"></div></div>'
          f'<div style="width:56px;font-family:DM Sans;font-weight:900;font-size:18px;color:#f0d8cf">{lab}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Five salaries stayed in","THE MATH")}
      <div style="margin-bottom:14px">{bars}</div>
      <div style="height:1px;background:rgba(255,255,255,.09);margin:10px 0 16px"></div>
      <div style="display:flex;align-items:center;gap:16px">
        <div style="width:186px;text-align:right;font-family:DM Sans;font-weight:800;font-size:16px;color:rgb({ACC})">The Ultron desk</div>
        <div style="width:430px;height:26px;background:rgba(255,255,255,.05);border-radius:7px;position:relative">
          <div style="width:9px;height:26px;background:rgb({ACC});border-radius:7px;box-shadow:0 0 16px rgba(212,162,127,.7)"></div></div>
        <div style="flex:1;font-family:DM Sans;font-weight:900;font-size:18px;color:#FAFAF7">cents / run</div></div>
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:18px">
        <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#f0d8cf">$248k / yr not spent</span>
        <span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">same five jobs, done</span></div>
      {cap("fast-growing companies do not work more - they run systems around the clock.")}</div>'''

# 7. LINE - org chart: every job splits into PEOPLE (judgement) and FLOWS (repetition)
def line():
    W,H=800,440
    people=["taste","relationships","the hard calls"]
    flows=["sourcing","triage","follow-ups","reviews","content"]
    def col(items,x0,label,accent,glow):
        chips=""
        for i,it in enumerate(items):
            y=196+i*54
            chips+=(f'<rect x="{x0}" y="{y}" width="230" height="42" rx="11" fill="{glow}" stroke="{accent}" stroke-width="1.5"/>'
              f'<text x="{x0+22}" y="{y+27}" font-family="DM Sans" font-weight="700" font-size="18" fill="#e6e0d5">{it}</text>')
        return chips
    peo=col(people,60,"PEOPLE","rgba(200,70,35,.5)","rgba(200,70,35,.08)")
    flo=col(flows,510,"FLOWS",f"rgba(212,162,127,.5)","rgba(212,162,127,.08)")
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Freeze repetition. Hire judgement.","THE LINE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <rect x="308" y="40" width="184" height="60" rx="15" fill="#2a2724" stroke="rgba(255,255,255,.12)"/>
        <text x="400" y="70" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">EVERY JOB</text>
        <text x="400" y="90" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">sort before you post it</text>
        <path d="M400 100 V132 H175 V158" fill="none" stroke="rgba(200,70,35,.55)" stroke-width="2.4"/>
        <path d="M400 100 V132 H625 V158" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="2.4"/>
        <rect x="60" y="150" width="230" height="42" rx="11" fill="rgba(200,70,35,.16)" stroke="rgba(200,70,35,.5)" stroke-width="1.5"/>
        <text x="175" y="177" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".14em" fill="#f0b8a8">PEOPLE &middot; HIRE</text>
        <rect x="510" y="150" width="230" height="42" rx="11" fill="rgba(212,162,127,.16)" stroke="rgba(212,162,127,.5)" stroke-width="1.5"/>
        <text x="625" y="177" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".14em" fill="rgb({ACC})">FLOWS &middot; FREEZE</text>
        {peo}{flo}
      </svg>
      {cap("people for taste, relationships and the calls; flows for everything that repeats.")}</div>'''

# 8. TEST - dot field of job tasks run through one question: checklist -> flow, judgement -> hire
def test():
    cols,rowsn=14,7  # 98 task dots
    hire={9,23,38,55,71,84,12,63}  # the judgement handful
    cell=18; gap=12
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in hire:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="rgb({BAD})" filter="url(#hd)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="rgb({ACC})" opacity="0.9"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Would a checklist do it?","THE TEST")}
      <div style="display:flex;align-items:center;gap:40px">
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="flex-shrink:0">
          <defs><filter id="hd" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({BAD})" flood-opacity="0.9"/></filter></defs>
          {dots}</svg>
        <div style="flex:1">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">
            <span style="width:16px;height:16px;border-radius:5px;background:rgb({ACC});flex-shrink:0"></span>
            <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">90 &rarr; a flow</span></div>
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
            <span style="width:16px;height:16px;border-radius:5px;background:rgb({BAD});flex-shrink:0"></span>
            <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#f0d8cf">8 &rarr; a hire</span></div>
          <div style="font-family:DM Sans;font-size:18px;color:#c9c3b8;line-height:1.45">If a checklist answers yes, it is a flow, not a headcount. Run the test before every job posting.</div>
        </div>
      </div>
      {cap("98 recurring tasks, one question each - most were never a person's job.")}</div>'''

PANELS={"leadgen":leadgen(),"support":support(),"content":content(),"followups":followups(),
        "reviews":reviews(),"math":math_panel(),"line":line(),"test":test()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/neverhire"; os.makedirs(outd,exist_ok=True)
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
