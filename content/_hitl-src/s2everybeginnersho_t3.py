#!/usr/bin/env python3
# TIER 3 - THE DAY-ONE SKILL STACK, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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

# 1. SHELF - isometric stack of the day-one skill cards you install first (skill shelf / iso stack)
def shelf():
    rows=[("CORTEX","one ranked brief","research"),
          ("SPECTER","cold sequence, sent","outreach"),
          ("PULSE","a full carousel","content"),
          ("STRIKER","deal, qualified","deals"),
          ("SENTINEL","the page, shipped","code")]
    cards=""
    for i,(nm,job,role) in enumerate(rows):
        y=i*92
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;'
          f'background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:16px;padding:16px 22px;'
          f'box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);'
          f'display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:20px;color:rgb({ACC})">{nm[0]}</div>'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.12em;color:rgb({ACC})">/{nm.lower()}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:21px;color:#FAFAF7;margin-top:1px">{job}</div></div>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#8f8f85;text-transform:uppercase">{role}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Install the stack, not prompts","DAY ONE")}
      <div style="perspective:2000px;height:520px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:560px;height:460px;position:relative">{cards}</div></div>
      {cap("five skills that finish real work, live the day you sign in.")}</div>'''

# 2. BRIEF - IVORY before/after: a messy pile of tabs collapses into one ranked brief (before/after)
def brief():
    tabs=""
    for i in range(7):
        tabs+=(f'<div style="height:22px;border-radius:6px;background:rgba(150,90,45,.14);border:1px solid rgba(150,90,45,.22);'
          f'margin-bottom:9px;width:{100-i*7}%;position:relative">'
          f'<div style="position:absolute;left:9px;top:5px;width:{40-i*3}%;height:6px;border-radius:3px;background:rgba(150,90,45,.30)"></div>'
          f'<svg width="16" height="16" viewBox="0 0 24 24" style="position:absolute;right:6px;top:3px"><path d="M6 6l12 12M18 6L6 18" stroke="rgba(200,70,35,.6)" stroke-width="2.4" stroke-linecap="round"/></svg></div>')
    rank=""
    for j,(a,b) in enumerate([("Northwind","92"),("Globex","88"),("Initech","81")]):
        rank+=(f'<div style="display:flex;align-items:center;gap:12px;padding:11px 0;border-bottom:1px solid rgba(150,90,45,.14)">'
          f'<span style="font-family:\'DM Mono\';font-size:13px;color:#96562d;width:16px">{j+1}</span>'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#2a2016">{a}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:20px;color:#96562d">{b}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">40 tabs into one brief</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">/CORTEX</span></div>
      <div style="display:flex;align-items:stretch;gap:26px;height:340px">
        <div style="flex:1">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#a08a68;margin-bottom:14px">BEFORE &middot; 40 OPEN TABS</div>
          {tabs}</div>
        <div style="flex-shrink:0;display:flex;align-items:center;justify-content:center;width:60px">
          <svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
        <div style="flex:1;display:flex;flex-direction:column">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#a08a68;margin-bottom:14px">AFTER &middot; 1 RANKED PAGE</div>
          <div style="flex:1;background:rgba(255,255,255,.62);border:1px solid rgba(150,90,45,.18);border-left:4px solid #96562d;border-radius:14px;padding:6px 20px 16px;box-shadow:0 18px 30px rgba(120,95,60,.16)">{rank}
            <div style="font-family:'DM Mono';font-size:12px;color:#a08a68;margin-top:12px">scored on your ICP &middot; sources dated</div></div></div>
      </div>
      {cap("stop reading the internet. read the one page it hands back.","#8a745a")}</div>'''

# 3. OUTREACH - bezier node graph: one ICP fans into a full multi-step sequence (node graph)
def outreach():
    W,H=820,430
    steps=[("Email 1","hook + trigger",70),("Wait 2d","",150),("Follow-up","one question",230),("Break-up","last touch",330)]
    srcx,srcy=140,215; sx=470
    edges=""; nodes=""
    for nm,sub,y in steps:
        mx=(srcx+sx)/2
        edges+=f'<path d="M{srcx+70} {srcy} C{mx:.0f} {srcy},{mx:.0f} {y},{sx-8} {y}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
        nodes+=(f'<rect x="{sx}" y="{y-30}" width="300" height="60" rx="14" fill="linear-gradient(160deg,#33302c,#211e1a)"/>'
          f'<rect x="{sx}" y="{y-30}" width="300" height="60" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{sx+22}" y="{y-2}" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{nm}</text>'
          + (f'<text x="{sx+22}" y="{y+20}" font-family="DM Sans" font-size="14" fill="#8f8f85">{sub}</text>' if sub else '')
          + f'<circle cx="{sx+276}" cy="{y}" r="6" fill="#7fd39a" filter="url(#ld)"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One ICP, a full sequence","/SPECTER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="src" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="ld" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#7fd39a" flood-opacity="0.9"/></filter></defs>
        {edges}
        <g filter="url(#sg)"><circle cx="{srcx}" cy="{srcy}" r="68" fill="url(#src)"/></g>
        <text x="{srcx}" y="{srcy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">ICP</text>
        <text x="{srcx}" y="{srcy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">1 founder</text>
        {nodes}
      </svg>
      {cap("you name one prospect, it writes and paces the whole thread - cents a send.")}</div>'''

# 4. CAROUSEL - IVORY radial hub: one topic radiates into six ready assets (radial hub)
def carousel():
    cx,cy=250,238; R=150
    assets=[("post",-90),("carousel",-30),("hook",30),("ALT text",90),("comment",150),("DM",210)]
    spokes=""
    for nm,a in assets:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.30)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="rgba(255,255,255,.66)" stroke="rgba(150,90,45,.24)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#96562d">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="500" height="476" viewBox="0 0 500 476">
        <defs><radialGradient id="hubc" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="#c07a4c"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgba(150,90,45,.4)"/></filter></defs>
        {spokes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#hubc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#fdfbf6">1 TOPIC</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#fbe9d8">you drop it</text>
      </svg>
      <div style="flex:1">
        <div style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016;line-height:1.1;margin-bottom:8px">One topic,<br>six assets</div>
        <div style="font-family:'DM Sans';font-size:19px;color:#5a4634;line-height:1.45">One line in. Post, carousel, hook, ALT, first comment and the DM reply, all in your voice.</div>
        {cap("the whole content kit, ready to schedule.","#8a745a")}</div>
    </div>'''

# 5. AUDIT - arc gauge: the classic stack dial pinned high vs the Ultron cents reading (gauge)
def audit():
    cx,cy,R=280,300,210
    def pt(a,rr): return (cx+rr*math.cos(math.radians(a)), cy+rr*math.sin(math.radians(a)))
    ticks=""
    for a in range(180,361,15):
        x1,y1=pt(a,R); x2,y2=pt(a,R-18)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
    na=340  # needle points near the low/cents end (right)
    nx,ny=pt(na,R-40)
    lx1,ly1=pt(184,R+6); lx2,ly2=pt(356,R+6)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Audit the stack you pay for","/TOOL AUDIT")}
      <div style="display:flex;align-items:center;gap:26px">
        <svg width="560" height="330" viewBox="0 0 560 330">
          <defs><linearGradient id="arc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#c84623"/><stop offset="55%" stop-color="#c9a583"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
          <filter id="ng" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
          <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(250,250,247,.08)" stroke-width="26"/>
          <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="url(#arc)" stroke-width="26" stroke-linecap="round"/>
          {ticks}
          <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round" filter="url(#ng)"/>
          <circle cx="{cx}" cy="{cy}" r="16" fill="#211e1a" stroke="rgb({ACC})" stroke-width="3"/>
          <text x="{lx1:.0f}" y="{ly1+22:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c84623">$900/mo</text>
          <text x="{lx2:.0f}" y="{ly2+22:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})">cents/run</text>
        </svg>
        <div style="flex:1">
          <div style="font-family:'DM Sans';font-weight:900;font-size:62px;color:#FAFAF7;line-height:1">cents</div>
          <div style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-top:2px">per run, not per seat</div>
          <div style="margin-top:20px;padding:16px 18px;background:#211d19;border:1px solid rgba(255,255,255,.09);border-radius:14px">
            <div style="display:flex;justify-content:space-between;font-family:'DM Sans';font-size:17px;color:#8f8f85;padding-bottom:9px;border-bottom:1px solid rgba(255,255,255,.08)"><span>9 SaaS seats</span><span style="color:#c84623;text-decoration:line-through">$900</span></div>
            <div style="display:flex;justify-content:space-between;font-family:'DM Sans';font-weight:800;font-size:17px;color:#FAFAF7;padding-top:9px"><span>Ultron, pay per token</span><span style="color:rgb({ACC})">cents</span></div></div>
        </div>
      </div>
      {cap("list what you pay monthly. it prices the same work in cents.")}</div>'''

# 6. SIGNALS - radar sweep of live market signals, first-to-see (radar)
def signals():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Stack move",205,168),("Intent",44,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    feed=""
    for nm,when in [("Rival raised $4M","Tue 09:12"),("Target hiring 3 ops","Wed 07:40"),("Account swapped CRM","Thu 08:03")]:
        feed+=(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:13px">'
          f'<span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.7);flex-shrink:0"></span>'
          f'<span style="flex:1;font-family:DM Sans;font-size:18px;color:#d9d5cc">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:#8f8f85">{when}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("See the market move first","/RADAR")}
        {feed}
        {cap("funding, hiring, stack and intent - this morning's web, watched for you.")}</div>
    </div>'''

# 7. GATE - dot field of drafts, all parked, awaiting one tap (dot field)
def gate():
    cols,rowsn=24,10  # 240 drafts
    approved={57,58,59}
    dots=""; cell=15; gap=6
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in approved:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.10)" stroke="rgba(250,250,247,.06)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">Nothing sends without you</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">HUMAN GATE</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
          <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
          {dots}</svg>
        <div style="flex-shrink:0;text-align:center">
          <svg width="120" height="120" viewBox="0 0 120 120">
            <defs><filter id="kg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
            <g filter="url(#kg)"><rect x="24" y="52" width="72" height="56" rx="14" fill="none" stroke="rgb({ACC})" stroke-width="6"/></g>
            <path d="M38 52 V38 a22 22 0 0 1 44 0 v14" fill="none" stroke="rgb({ACC})" stroke-width="6"/>
            <circle cx="60" cy="78" r="7" fill="rgb({ACC})"/></svg>
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#FAFAF7;margin-top:8px">240 drafts</div>
          <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC});margin-top:4px">3 approved by you</div></div>
      </div>
      {cap("it drafts everything and stops. one tap per send, always yours.")}</div>'''

# 8. WEEK1 - install timeline, day one to first shipped output this week (install timeline)
def week1():
    steps=[("DAY 1","Install the stack","sign in, agents live"),
           ("DAY 2","First ranked brief","CORTEX on 40 accounts"),
           ("DAY 3","Sequence out","SPECTER, cents a send"),
           ("DAY 5","Carousel shipped","PULSE, your voice")]
    W=800; y=140; seg=(W-120)/(len(steps)-1)
    line=f'<line x1="60" y1="{y}" x2="{W-60}" y2="{y}" stroke="rgba(212,162,127,.3)" stroke-width="3"/>'
    line+=f'<line x1="60" y1="{y}" x2="{60+seg*3:.0f}" y2="{y}" stroke="rgb({ACC})" stroke-width="3"/>'
    nodes=""; labels=""
    for i,(day,t,sub) in enumerate(steps):
        x=60+seg*i
        nodes+=(f'<circle cx="{x:.0f}" cy="{y}" r="16" fill="#211e1a" stroke="rgb({ACC})" stroke-width="3"/>'
          f'<circle cx="{x:.0f}" cy="{y}" r="7" fill="rgb({ACC})"/>'
          f'<text x="{x:.0f}" y="{y-38}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">{day}</text>')
        labels+=(f'<div style="position:absolute;left:{x-95:.0f}px;top:{y+34}px;width:190px;text-align:center">'
          f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#FAFAF7;line-height:1.15">{t}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8f8f85;margin-top:4px">{sub}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {htitle("Ship something this week","START HERE")}
      <div style="position:relative;height:340px">
        <svg width="{W}" height="200" viewBox="0 0 {W} 200" style="position:absolute;left:0;top:0">{line}{nodes}</svg>
        {labels}
        <div style="position:absolute;left:{60+seg*3-70:.0f}px;top:{y-96}px;background:rgb({ACC});color:#1a0f0a;font-family:'DM Sans';font-weight:900;font-size:15px;padding:8px 16px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">SHIPPED &#10003;</div>
      </div>
      {cap("day one you install, this week you ship - not another course to finish.")}</div>'''

PANELS={"shelf":shelf(),"brief":brief(),"outreach":outreach(),"carousel":carousel(),
        "audit":audit(),"signals":signals(),"gate":gate(),"week1":week1()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2everybeginnersho"; os.makedirs(outd,exist_ok=True)
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
