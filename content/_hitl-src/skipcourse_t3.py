#!/usr/bin/env python3
# TIER 3 - SKIP THE COURSE, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded
# scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips, no
# clip-path cuts, no extruded walls. 8 distinct scenes. Warm palette. Ultron cost = cents; a course
# price only ever appears as a COMPETITOR cost.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. PATH9 - NODE GRAPH: the feed's mastery ladder forks into 3 paid curriculums, each a dead-end
def path9():
    courses=[("PROMPTING","$499","14 lessons",92),
             ("AUTOMATION","$899","22 lessons",230),
             ("CODING","$1,499","31 lessons",368)]
    hubx,hy=150,230
    edges=""; cards=""
    for nm,price,les,y in courses:
        edges+=f'<path d="M{hubx+62} {hy} C296 {hy},312 {y},468 {y}" fill="none" stroke="rgba(212,162,127,.30)" stroke-width="2.5"/>'
        edges+=f'<circle cx="486" cy="{y}" r="5" fill="rgba(200,70,35,.85)"/>'
        cards+=(f'<div style="position:absolute;left:300px;top:{y-42}px;width:210px;background:#221f1b;border:1.5px solid rgba(255,255,255,.09);border-radius:16px;padding:15px 18px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#c9c3b8">{nm}</span><span style="font-family:DM Sans;font-weight:900;font-size:21px;color:rgb({RED})">{price}</span></div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85;margin-top:4px">{les} &middot; 0 runs on your work</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The ladder they sell","3 CURRICULUMS DEEP")}
      <div style="position:relative;height:462px">
        <svg width="820" height="462" viewBox="0 0 820 462" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="feed" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="fg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          {edges}
          <g filter="url(#fg)"><circle cx="{hubx}" cy="{hy}" r="66" fill="url(#feed)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">THE FEED</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">sells the climb</text>
          <text x="536" y="{hy+5}" font-family="DM Mono" font-size="13" fill="rgba(200,70,35,.9)">dead end</text>
        </svg>
        <div style="position:absolute;left:14px;top:300px;width:120px;font-family:DM Mono;font-size:12px;color:#8f8f85;text-align:center">$2,897 in courses<br>before run one</div>
        {cards}
      </div>
      {cap("three curriculums, one certificate, zero runs on your real pipeline.")}</div>'''

# 2. FLIP9 - COURSE-VS-DOING split (IVORY): toy example on the left, your real run on the right
def flip9():
    def col(head,tag,tagc,items,mark,markc):
        rows=""
        for it in items:
            rows+=(f'<div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px">'
              f'<span style="flex-shrink:0;margin-top:2px">{mark}</span>'
              f'<span style="font-family:DM Sans;font-size:17px;color:#3a2c1e;line-height:1.35">{it}</span></div>')
        return (f'<div style="flex:1;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.16);border-radius:18px;padding:20px 22px">'
          f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">{head}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{tagc}">{tag}</span></div>{rows}</div>')
    x=f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({RED})" stroke-width="2.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
    ck=f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
    toy=col("Course sandbox","TOY",f"rgb({RED})",["Summarize this Wikipedia page","Write a haiku about coffee","Classify 10 fake reviews"],x,RED)
    real=col("Your pipeline","REAL","#96562d",["Brief 20 target accounts","Draft outreach in your voice","Score last week's replies"],ck,"96562d")
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Learn on your pipeline</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">NOT TOY EXAMPLES</span></div>
      <div style="display:flex;align-items:stretch;gap:20px;position:relative">
        {toy}
        <div style="align-self:center;flex-shrink:0;width:44px;height:44px;border-radius:50%;background:#96562d;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 18px rgba(150,90,45,.4)"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fdfbf6" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
        {real}
      </div>
      {cap("a haiku teaches you nothing. one real run on real work teaches the rules.","#8a745a")}</div>'''

# 3. RUN1 - ISO STACK: one research job ships, 20 accounts briefed as a raised card stack
def run1():
    rows=[("Northwind Robotics","hiring 3 ops roles"),
          ("Globex Systems","raised $4M in May"),
          ("Initech","no AI layer yet"),
          ("Umbrella Labs","new VP Sales")]
    cards=""
    for i,(a,b) in enumerate(rows):
        y=i*104
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:540px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;padding:18px 22px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#a8a296;margin-top:1px">{b}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Ship one job, end to end","RUN 1")}
      <div style="perspective:1900px;height:456px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:540px;height:414px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:384px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:10px 22px;border-radius:999px;box-shadow:0 12px 24px rgba(212,162,127,.4)">20 accounts briefed &#10003;</div></div></div>
      {cap("twenty accounts briefed teaches more than any prompt-anatomy lecture.")}</div>'''

# 4. RUN10 - TIMELINE: ten correction ticks, a no-list accreting rule by rule until drafts land
def run10():
    W,H=760,150
    y=64; x0,x1=110,650; step=(x1-x0)/9
    axis=f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgba(212,162,127,.35)" stroke-width="3"/>'
    ticks=""; labels=[(1,"first draft"),(4,"+ no-list"),(7,"tone locked"),(10,"drafts land")]
    lab={k:v for k,v in labels}
    for i in range(10):
        x=x0+i*step; on=(i+1) in lab; r=11 if on else 6
        fill=f"rgb({ACC})" if on else "rgba(212,162,127,.4)"
        gl='filter="url(#tg)"' if on else ""
        ticks+=f'<circle cx="{x:.0f}" cy="{y}" r="{r}" fill="{fill}" {gl}/>'
        ticks+=f'<text x="{x:.0f}" y="{y+32}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{i+1}</text>'
        if on:
            ticks+=f'<text x="{x:.0f}" y="{y-24}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="14" fill="#e2dccf">{lab[i+1]}</text>'
    nolist=["no em dashes","no 'circle back'","lead with the number","max 62 words","one ask per email","never 'synergy'","cut the greeting"]
    chips="".join(f'<div style="background:#221f1b;border:1px solid rgba(212,162,127,.30);border-radius:12px;padding:11px 16px;display:flex;align-items:center;gap:10px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:16px;color:#d9d5cc">{r}</span></div>' for r in nolist)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Correct it ten times","RULES STICK")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto 6px">
        <defs><filter id="tg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {axis}{ticks}</svg>
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin:8px 2px 14px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#FAFAF7">Your no-list, by run ten</span>
        <span style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">7 rules, enforced</span></div>
      <div style="display:flex;flex-wrap:wrap;gap:12px">{chips}</div>
      {cap("by run ten your no-list exists and the drafts stop disappointing.")}</div>'''

# 5. RUN50 - RADIAL HUB: a trigger core fires jobs on its own, an approve tap on each outbound
def run50():
    cx,cy=240,235; R=168
    spokes=[("new funding","brief + outreach",-90),("champion hired","warm intro",-18),
            ("pricing page hit","send deck",54),("competitor churn","take the meeting",126),
            ("renewal in 30d","expansion play",198)]
    arms=""; nodes=""
    for nm,job,a in spokes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        arms+=f'<line x1="{cx+52*math.cos(math.radians(a)):.0f}" y1="{cy+52*math.sin(math.radians(a)):.0f}" x2="{x-30*math.cos(math.radians(a)):.0f}" y2="{y-30*math.sin(math.radians(a)):.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="rgb({ACC})" filter="url(#nb)"/>'
          f'<text x="{x:.0f}" y="{y-40:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#d9d5cc">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+50:.0f}" text-anchor="middle" font-family="DM Sans" font-size="13" fill="#8f8f85">{job}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="480" height="480" viewBox="0 0 480 480">
        <defs><radialGradient id="core" cx="38%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="nb" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {arms}{nodes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">AUTO</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">50 runs in</text>
      </svg>
      <div style="flex:1">
        {htitle("Wire the triggers","STOP INITIATING")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Five signals now fire their own jobs. You do not start the work, you tap approve on what it drafted.</div>
        <div style="display:inline-flex;align-items:center;gap:10px;margin-top:18px;background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:12px;padding:12px 18px">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>
          <span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#FAFAF7">you approve, it sends</span></div>
        {cap("the jobs fire themselves; you approve. the automation course, lived.")}
      </div></div>'''

# 6. RUN100 - GAUGE (IVORY): a dial swept to 100, the workflow minted into one owned command
def run100():
    pct=100; r=120; circ=math.pi*r  # half-circle gauge (180deg)
    dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Mint your workflow</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">RUN 100</span></div>
      <div style="display:flex;align-items:center;gap:36px">
        <div style="flex-shrink:0;position:relative;width:320px;height:214px">
          <svg width="320" height="214" viewBox="0 0 320 214">
            <path d="M40 190 A120 120 0 0 1 280 190" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="22" stroke-linecap="round"/>
            <path d="M40 190 A120 120 0 0 1 280 190" fill="none" stroke="#96562d" stroke-width="22" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}"/>
          </svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding-bottom:8px">
            <span style="font-family:DM Sans;font-weight:900;font-size:66px;color:#2a2016;line-height:.9">100</span>
            <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#96562d;margin-top:4px">RUNS LOGGED</span></div>
        </div>
        <div style="flex:1">
          <div style="font-family:DM Sans;font-size:19px;color:#3a2c1e;line-height:1.42;margin-bottom:18px">The pattern you repeated a hundred times becomes one command you own. No coding course required.</div>
          <div style="display:inline-flex;align-items:center;gap:12px;background:#2a2016;border-radius:14px;padding:15px 22px;box-shadow:0 12px 24px rgba(80,55,30,.28)">
            <span style="font-family:DM Mono;font-size:22px;color:rgb({ACC})">/</span>
            <span style="font-family:DM Mono;font-weight:500;font-size:22px;letter-spacing:.04em;color:#fdfbf6">my-outreach-desk</span></div>
          <div style="font-family:DM Sans;font-size:15px;color:#8a745a;margin-top:14px">runs for cents, reusable forever</div>
        </div>
      </div>
      {cap("the coding course you skipped becomes one command you own.","#8a745a")}</div>'''

# 7. GATE9 - DOT FIELD: a hundred runs, all inside the internal boundary, one parked for your tap
def gate9():
    cols,rowsn=20,5; cell=17; gap=13
    tap={47}
    dots=""
    for i in range(cols*rowsn):
        rr,c=divmod(i,cols); x=c*(cell+gap); y=rr*(cell+gap)
        if i in tap:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="rgb({ACC})" filter="url(#tg2)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="rgba(212,162,127,.34)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every run is safe","INTERNAL BY DEFAULT")}
      <div style="border:1.5px dashed rgba(212,162,127,.32);border-radius:20px;padding:30px 34px 26px;position:relative">
        <div style="position:absolute;top:-11px;left:28px;background:#232120;padding:0 12px;font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({ACC})">INTERNAL SANDBOX</div>
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
          <defs><filter id="tg2" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
          {dots}</svg>
        <div style="display:flex;align-items:center;justify-content:space-between;margin-top:24px;border-top:1px solid rgba(255,255,255,.08);padding-top:20px">
          <div><span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7">100</span><span style="font-family:DM Sans;font-size:16px;color:#a8a296;margin-left:10px">runs, none shipped</span></div>
          <div style="display:flex;align-items:center;gap:11px;background:#211d19;border:1px solid rgba(212,162,127,.34);border-radius:12px;padding:11px 17px">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>
            <span style="font-family:DM Sans;font-weight:700;font-size:16px;color:#FAFAF7">1 parked for your tap</span></div>
        </div>
      </div>
      {cap("nothing external ships without your tap, so mistakes stay internal.")}</div>'''

# 8. DIPLOMA - LADDER: rungs climb run 1 -> 100 to a desk that runs like you, no certificate
def diploma():
    W,H=440,470
    rungs=[(1,"first job shipped",410),(10,"no-list locked",330),(50,"triggers wired",250),(100,"skill minted",170)]
    lx,rx=64,196
    rail=f'<line x1="{lx}" y1="130" x2="{lx}" y2="440" stroke="rgba(212,162,127,.32)" stroke-width="5" stroke-linecap="round"/><line x1="{rx}" y1="130" x2="{rx}" y2="440" stroke="rgba(212,162,127,.32)" stroke-width="5" stroke-linecap="round"/>'
    steps=""
    for n,lab,y in rungs:
        steps+=f'<line x1="{lx}" y1="{y}" x2="{rx}" y2="{y}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>'
        steps+=f'<circle cx="{lx}" cy="{y}" r="9" fill="rgb({ACC})"/>'
        steps+=f'<text x="{rx+20}" y="{y+5}" font-family="DM Mono" font-size="15" fill="#d9d5cc">{n} &middot; {lab}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:18px">
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="flex-shrink:0">
        <defs><radialGradient id="desk" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="dg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {rail}{steps}
        <g filter="url(#dg)"><circle cx="{(lx+rx)//2}" cy="96" r="44" fill="url(#desk)"/></g>
        <text x="{(lx+rx)//2}" y="102" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">YOUR DESK</text>
      </svg>
      <div style="flex:1;min-width:0">
        {htitle("A hundred runs","NO CERTIFICATE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">There is no diploma at the top of this ladder. Just a pipeline that moves and a system that remembers how you work.</div>
        {cap("the desk works like you, and it costs cents a run to keep it there.")}</div></div>'''

PANELS={"path9":path9(),"flip9":flip9(),"run1":run1(),"run10":run10(),
        "run50":run50(),"run100":run100(),"gate9":gate9(),"diploma":diploma()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/skipcourse"; os.makedirs(outd,exist_ok=True)
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
