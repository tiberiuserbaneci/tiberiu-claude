#!/usr/bin/env python3
# TIER 3 - THE REGISTRY AUDIT, on the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded scene
# filling a clean rounded card, htitle + one caption, NO generic stat-chip strips.
# Story: CORTEX reads the ENTIRE public skill registry and returns a ranked, cited, grouped shortlist.
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

# 1. PILE - dot field of 812 registry entries, a handful lit (the winners)
def pile():
    cols,rowsn=48,17   # 816 ~ 812
    lit={55,71,158,203,299,344,410,466,517,588,640,701,733,769,790}
    cell=15; gap=3.5
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:36px 40px 36px">
      {htitle("A registry too big to read","812 SKILLS")}
      <svg width="{fw:.0f}" height="{fh:.0f}" viewBox="0 0 {fw:.0f} {fh:.0f}" style="display:block;margin:6px auto 4px">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:10px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#FAFAF7">812<span style="font-size:19px;font-weight:700;color:#8f8f85;margin-left:10px">candidates</span></span>
        <span style="font-family:'DM Mono';font-size:14px;color:rgb({ACC})">15 lit = survivors</span></div>
      {cap("hundreds of public skills, most of them noise. no founder opens all 812.")}</div>'''

# 2. LEDGER - IVORY registry page: every row actually read, kept in accent, junk cut in muted red
def ledger():
    rows=[("humanizer","voice match, no robotic tells","kept"),
          ("beautiful-prose","strong verbs, zero filler","kept"),
          ("hook-generator","real copy frameworks","kept"),
          ("ai-detector-x2","dead link, no maintainer","cut"),
          ("promptpack-99","thin wrapper, no logic","cut"),
          ("frontend-design","bold UI, not generic AI","kept")]
    lines=""
    for i,(nm,note,st) in enumerate(rows):
        kept=(st=="kept")
        mark=(f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
              if kept else
              f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb(200,70,35)" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>')
        nmc="#2a2016" if kept else "#9a8a76"
        deco="text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)" if not kept else ""
        stcol="#96562d" if kept else "rgb(200,70,35)"
        top="border-top:1px solid rgba(120,95,60,.16);" if i>0 else ""
        lines+=(f'<div style="display:flex;align-items:center;gap:18px;padding:15px 4px;{top}">'
          f'<div style="flex-shrink:0;width:30px;text-align:center;font-family:DM Mono;font-size:15px;color:#a08a68">{i+1:02d}</div>'
          f'<div style="flex:1;min-width:0"><div style="font-family:DM Mono;font-weight:500;font-size:19px;color:{nmc};{deco}">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#7a6a54;margin-top:2px">{note}</div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center;gap:9px">{mark}'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{stcol};text-transform:uppercase">{st}</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      {htitle("Every row, actually read","READ &middot; SCORED","#2a2016")}
      <div style="background:rgba(255,255,255,.5);border:1px solid rgba(120,95,60,.14);border-radius:20px;padding:6px 22px">{lines}</div>
      {cap("cortex opens each entry, tests the claim, keeps only what holds up.","#8a745a")}</div>'''

# 3. RANK - isometric stack of ranked score cards (best fit floats to the top)
def rank():
    rows=[("frontend-design","design and UI","94"),
          ("humanizer","writing and content","91"),
          ("cortex-research","market research","88")]
    cards=""
    for i,(nm,job,sc) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex-shrink:0;font-family:'DM Sans';font-weight:900;font-size:30px;color:rgba(212,162,127,.55);width:44px">#{i+1}</div>
          <div style="flex:1;text-align:left"><div style="font-family:'DM Mono';font-weight:500;font-size:22px;color:#FAFAF7">{nm}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{job}</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 17px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{sc}</span>
            <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">FIT</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:38px 44px 44px">
      {htitle("Ranked, not just listed","BEST FIT FIRST")}
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:600px;height:450px;position:relative">{cards}</div></div>
      {cap("scored on fit, evidence and freshness. the shortlist sorts itself.")}</div>'''

# 4. CITE - dimensional wax-seal + packed source-receipt chips (every pick shows its evidence)
def cite():
    receipts=[("changelog.dev","2026-06-02","shipped in prod"),
              ("benchmarks.ai","2026-05-28","top-decile score"),
              ("github.com","2026-06-10","1.2k real installs")]
    chips=""
    for dom,date,note in receipts:
        fav=dom[0].upper()
        chips+=f'''<div style="display:flex;align-items:center;gap:16px;
          background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);
          border-radius:16px;padding:14px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">
          <div style="flex-shrink:0;width:40px;height:40px;border-radius:11px;background:linear-gradient(160deg,#4a423a,#2a2622);
            display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:20px;color:rgb({ACC});border:1px solid rgba(255,255,255,.10)">{fav}</div>
          <div style="flex:1;text-align:left">
            <div style="font-family:'DM Mono';font-weight:500;font-size:17px;color:#eae4d8;letter-spacing:.02em">{dom}</div>
            <div style="font-family:'DM Sans';font-size:14px;color:#8f8f85;margin-top:1px">{note} &middot; {date}</div></div>
          <svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.16)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Every pick shows its receipt","SOURCED &middot; DATED")}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);
        border-radius:14px;padding:12px 18px;margin-bottom:22px;opacity:.72">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#7a7468;flex-shrink:0">HYPE</span>
        <span style="font-family:'DM Sans';font-size:18px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">"everyone says this one is a must-have"</span>
        <span style="margin-left:auto;font-family:'DM Mono';font-size:12px;color:#c84623;flex-shrink:0">no source</span></div>
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex:1">
          <div style="font-family:'DM Sans';font-weight:900;font-size:32px;color:#FAFAF7;line-height:1.05;margin-bottom:18px">Ranked <span style="color:rgb({ACC})">#1</span>, and here is why.</div>
          <div style="display:flex;flex-direction:column;gap:12px">{chips}</div>
        </div>
        <div style="flex-shrink:0;display:flex;align-items:center;justify-content:center">
          <svg width="280" height="280" viewBox="0 0 280 280">
            <defs>
              <radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
              <radialGradient id="sealbloom" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.5)"/><stop offset="62%" stop-color="rgba(204,120,92,.10)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
              <filter id="sealsh" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="rgba(0,0,0,.6)"/></filter>
              <filter id="spec" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="8"/></filter>
            </defs>
            <circle cx="140" cy="140" r="136" fill="url(#sealbloom)"/>
            <g filter="url(#sealsh)">
              {"".join(f'<line x1="140" y1="140" x2="{140+124*math.cos(math.radians(a)):.0f}" y2="{140+124*math.sin(math.radians(a)):.0f}" stroke="#8a4c2c" stroke-width="10"/>' for a in range(0,360,15))}
              <circle cx="140" cy="140" r="114" fill="url(#seal)"/>
            </g>
            <circle cx="140" cy="140" r="114" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
            <circle cx="140" cy="140" r="93" fill="none" stroke="rgba(26,15,10,.28)" stroke-width="2"/>
            <path d="M104 143 l24 24 l50 -58" fill="none" stroke="#1a0f0a" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
            <ellipse cx="106" cy="95" rx="42" ry="23" fill="rgba(255,255,255,.28)" filter="url(#spec)" transform="rotate(-32 106 95)"/>
            <text x="140" y="206" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="18" letter-spacing="4" fill="#1a0f0a">VERIFIED</text>
          </svg>
        </div>
      </div>
      {cap("no blind recommendation. each entry carries the source that earned its rank.")}</div>'''

# 5. GROUP - radial hub-and-spokes: CORTEX at the core, one cluster per job-to-be-done
def group():
    cx,cy=260,235; R=178
    jobs=[("WRITING","4 skills",-90),("DESIGN","3 skills",-30),("RESEARCH","3 skills",30),
          ("OUTREACH","2 skills",90),("DEALS","2 skills",150),("CONTENT","1 skill",210)]
    spokes=""; nodes=""
    for nm,cnt,a in jobs:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2.4"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".06em" fill="#e6dccb">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="13" fill="rgb({ACC})">{cnt}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="500" height="470" viewBox="0 0 500 470">
        <defs><radialGradient id="hb" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">CORTEX</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">by the job</text>
      </svg>
      <div style="flex:1">
        {htitle("Grouped by the job","BY THE TASK")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Writing, design, research, outreach, deals. The shortlist maps to what you need done, not to who sells it.</div>
        {cap("you find the skill by the task, not by scrolling a vendor list.")}</div></div>'''

# 6. SIEVE - coded funnel: 812 candidates narrow through three cut gates down to 15 survivors
def sieve():
    W,H=560,470
    gates=[("812","every public entry",0),("dedupe","drop copies",1),("dead links","drop the broken",2),("thin wrappers","drop the empty",3)]
    bands=""
    topw,botw=520,150; steps=len(gates)
    for nm,note,i in gates:
        t=i/steps; b=(i+1)/steps
        wt=topw+(botw-topw)*t; wb=topw+(botw-topw)*b
        y=40+i*96; hh=88
        x0t=(W-wt)/2; x0b=(W-wb)/2
        op=0.16+i*0.14
        bands+=(f'<path d="M{x0t:.0f} {y} H{x0t+wt:.0f} L{x0b+wb:.0f} {y+hh} H{x0b:.0f} Z" fill="rgba(212,162,127,{op:.2f})" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>'
          f'<text x="{W/2:.0f}" y="{y+38:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="{26 if i==0 else 19}" fill="#FAFAF7">{nm}</text>'
          f'<text x="{W/2:.0f}" y="{y+60:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#e9dcc9">{note}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><radialGradient id="win" cx="50%" cy="40%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="wg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {bands}
        <g filter="url(#wg)"><circle cx="{W/2:.0f}" cy="432" r="42" fill="url(#win)"/></g>
        <text x="{W/2:.0f}" y="440" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#1a0f0a">15</text>
      </svg>
      <div style="flex:1">
        {htitle("812 in. Fifteen out.","THE CUT")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Copies, dead links and empty wrappers fall at the first gates. Only skills that survive every cut reach your brief.</div>
        {cap("volume is easy. the shortlist is the whole job.")}</div></div>'''

# 7. FRESH - radar sweep watching the registry: new / updated blips, one deprecated in muted red
def fresh():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("new: agent-sdk",305,150,False),("updated: humanizer",120,96,False),
           ("dropped: old-wrap",210,168,True),("new: canvas-design",42,120,False)]
    bl=""
    for nm,ang,dist,dead in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        col="rgb(200,70,35)" if dead else f"rgb({ACC})"
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{col}" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="{"#c86a52" if dead else "#d9d5cc"}">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("The registry keeps moving","STILL LIVE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">New skills land every week, old ones die. CORTEX rechecks and re-ranks so the brief never goes stale.</div>
        {cap("a shortlist saved once rots. this one re-scores itself.")}</div></div>'''

# 8. BRIEF - IVORY one-page deliverable: ranked, cited list + a human approve tap
def brief():
    picks=[("frontend-design","design and UI","94"),
           ("humanizer","writing","91"),
           ("cortex-research","research","88"),
           ("hook-generator","content","85"),
           ("beautiful-prose","writing","83")]
    rowsh=""
    for i,(nm,job,sc) in enumerate(picks):
        top="border-top:1px solid rgba(120,95,60,.16);" if i>0 else ""
        rowsh+=(f'<div style="display:flex;align-items:center;gap:16px;padding:13px 2px;{top}">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#96562d;width:34px">#{i+1}</span>'
          f'<span style="flex:1;font-family:DM Mono;font-weight:500;font-size:19px;color:#2a2016">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:#7a6a54;margin-right:14px">{job}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:19px;color:#2a2016;background:rgba(150,90,45,.14);padding:4px 12px;border-radius:9px">{sc}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      {htitle("One page. Ranked. Cited.","THE BRIEF","#2a2016")}
      <div style="background:rgba(255,255,255,.58);border:1px solid rgba(120,95,60,.16);border-radius:20px;padding:8px 24px 12px">
        <div style="display:flex;justify-content:space-between;align-items:baseline;padding:8px 2px 10px;border-bottom:2px solid rgba(150,90,45,.28)">
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#96562d">TOP 5 OF 812</span>
          <span style="font-family:DM Mono;font-size:13px;color:#a08a68">grouped &middot; sourced</span></div>
        {rowsh}</div>
      <div style="display:flex;align-items:center;gap:16px;margin-top:20px">
        <div style="flex:1;font-family:DM Sans;font-size:16px;color:#5a4634;line-height:1.4">The whole registry, compressed to the handful worth your time. Nothing installs until you tap.</div>
        <div style="flex-shrink:0;display:flex;align-items:center;gap:11px;background:#96562d;padding:14px 26px;border-radius:999px;box-shadow:0 12px 24px rgba(150,90,45,.3)">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fdfbf6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>
          <span style="font-family:DM Sans;font-weight:900;font-size:18px;color:#fdfbf6">APPROVE</span></div>
      </div>
      {cap("the exhaustive read done for you. your tap ships it.","#8a745a")}</div>'''

PANELS={"pile":pile(),"ledger":ledger(),"rank":rank(),"cite":cite(),
        "group":group(),"sieve":sieve(),"fresh":fresh(),"brief":brief()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src27"; os.makedirs(outd,exist_ok=True)
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
