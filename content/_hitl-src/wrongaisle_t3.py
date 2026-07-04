#!/usr/bin/env python3
# TIER 3 - THE WRONG PLUGIN AISLE, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# 8 distinct scene types: shelf aisle / gauge / comparison / node graph / iso stack / timeline /
# dot field / radial hub. Warm palette only. Ultron prices are cents.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; IVA="#96562d"; RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagcol=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagcol}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. AISLE - a literal store shelf of dev-tool product boxes, each stamped "irrelevant to Q3"
def aisle():
    items=[("repo-mapper","maps your codebase",'<path d="M9 8l-5 6 5 6M23 8l5 6-5 6" fill="none" stroke="rgb('+ACC+')" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'),
           ("knowledge-graph","links every file",'<circle cx="16" cy="9" r="4" fill="none" stroke="rgb('+ACC+')" stroke-width="2.6"/><circle cx="8" cy="22" r="4" fill="none" stroke="rgb('+ACC+')" stroke-width="2.6"/><circle cx="24" cy="22" r="4" fill="none" stroke="rgb('+ACC+')" stroke-width="2.6"/><path d="M14 12l-4 7M18 12l4 7M12 22h8" stroke="rgb('+ACC+')" stroke-width="2.6"/>'),
           ("code-navigator","jumps to defs",'<circle cx="14" cy="14" r="8" fill="none" stroke="rgb('+ACC+')" stroke-width="2.8"/><line x1="20" y1="20" x2="27" y2="27" stroke="rgb('+ACC+')" stroke-width="2.8" stroke-linecap="round"/>')]
    boxes=""
    for nm,sub,icon in items:
        boxes+=(f'<div style="width:226px;background:linear-gradient(162deg,#34302b,#201d1a);border:1px solid rgba(255,255,255,.10);'
          f'border-radius:16px;overflow:hidden;box-shadow:0 26px 42px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.08);position:relative">'
          f'<div style="height:118px;background:linear-gradient(160deg,rgba(212,162,127,.16),rgba(212,162,127,.04));display:flex;align-items:center;justify-content:center;border-bottom:1px solid rgba(255,255,255,.07)">'
          f'<svg width="56" height="56" viewBox="0 0 32 32">{icon}</svg></div>'
          f'<div style="padding:16px 18px 18px"><div style="font-family:\'DM Mono\';font-weight:500;font-size:18px;color:#eae4d8">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#8f8f85;margin-top:3px">{sub}</div>'
          f'<div style="display:inline-flex;align-items:center;gap:7px;margin-top:14px;background:rgba({RED},.14);border:1px solid rgba({RED},.4);'
          f'border-radius:8px;padding:6px 11px"><span style="width:8px;height:8px;border-radius:50%;background:rgb({RED})"></span>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.06em;color:#e0a08c">PIPELINE: none</span></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Written for engineers","AISLE 7 &middot; DEV TOOLS")}
      <div style="position:relative;padding:8px 20px 40px">
        <div style="display:flex;justify-content:space-between;gap:18px;position:relative;z-index:2">{boxes}</div>
        <!-- shelf plank the boxes stand on -->
        <div style="position:absolute;left:0;right:0;bottom:6px;height:22px;border-radius:5px;
          background:linear-gradient(180deg,#5a4a3a,#3a2e22);box-shadow:0 16px 26px rgba(0,0,0,.5), inset 0 2px 1px rgba(255,255,255,.14)"></div>
        <div style="position:absolute;left:0;right:0;bottom:0;height:8px;border-radius:0 0 5px 5px;background:#241c14"></div>
      </div>
      {cap("repo mappers, knowledge graphs, code navigators. impressive, irrelevant to your quarter.")}</div>'''

# 2. TELL - a gauge pinned at zero: polished demo, no revenue path
def tell():
    cx,cy,R=210,225,168
    def pt(deg,r):
        a=math.radians(deg); return (cx+r*math.cos(a), cy-r*math.sin(a))
    ticks=""
    for d in range(0,181,30):
        x1,y1=pt(d,R); x2,y2=pt(d,R-18)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(150,90,45,.4)" stroke-width="3"/>'
    ax0,ay0=pt(180,R); ax1,ay1=pt(0,R)
    # red danger band near the left (0) end
    dx0,dy0=pt(180,R); dx1,dy1=pt(150,R)
    nx,ny=pt(171,R-34)  # needle pinned near 0
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {htitle("Cool demo, zero revenue","DIAL READS 0",ink="#2a2016",tagcol=IVA)}
      <div style="display:flex;align-items:center;gap:26px">
        <svg width="420" height="270" viewBox="0 0 420 270" style="flex-shrink:0">
          <path d="M{ax0:.0f} {ay0:.0f} A{R} {R} 0 0 1 {ax1:.0f} {ay1:.0f}" fill="none" stroke="rgba(150,90,45,.22)" stroke-width="16" stroke-linecap="round"/>
          <path d="M{dx0:.0f} {dy0:.0f} A{R} {R} 0 0 1 {dx1:.0f} {dy1:.0f}" fill="none" stroke="rgb({RED})" stroke-width="16" stroke-linecap="round"/>
          {ticks}
          <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="7" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="13" fill="#2a2016"/>
          <text x="{cx}" y="{cy-44}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#2a2016">0</text>
          <text x="{cx}" y="{cy-14}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".14em" fill="{IVA}">REVENUE PATH</text>
        </svg>
        <div style="flex:1;display:flex;flex-direction:column;gap:20px">
          <div><div style="display:flex;justify-content:space-between;font-family:'DM Sans';font-size:17px;color:#5a4634;margin-bottom:7px"><span style="font-weight:700;color:#2a2016">Demo polish</span><span>100%</span></div>
            <div style="height:14px;border-radius:8px;background:rgba(150,90,45,.16)"><div style="height:100%;width:100%;border-radius:8px;background:{IVA}"></div></div></div>
          <div><div style="display:flex;justify-content:space-between;font-family:'DM Sans';font-size:17px;color:#5a4634;margin-bottom:7px"><span style="font-weight:700;color:#2a2016">Deal it moves</span><span style="color:#b3502f">0</span></div>
            <div style="height:14px;border-radius:8px;background:rgba(150,90,45,.16)"><div style="height:100%;width:3%;border-radius:8px;background:rgb({RED})"></div></div></div>
          <div><div style="display:flex;justify-content:space-between;font-family:'DM Sans';font-size:17px;color:#5a4634;margin-bottom:7px"><span style="font-weight:700;color:#2a2016">Hours it saves</span><span style="color:#b3502f">0</span></div>
            <div style="height:14px;border-radius:8px;background:rgba(150,90,45,.16)"><div style="height:100%;width:3%;border-radius:8px;background:rgb({RED})"></div></div></div>
        </div>
      </div>
      {cap("if you cannot name the deal it moves or the hour it saves, it is a toy.","#8a745a")}</div>'''

# 3. FLIP - split comparison: a TOOL (one trick, dim) vs a DESK (owns an outcome, lit)
def flip():
    def panel(kind,head,sub,lines,lit):
        bd=f"rgb({ACC})" if lit else "rgba(255,255,255,.09)"
        bg="linear-gradient(162deg,#403a33,#241f1a)" if lit else "linear-gradient(162deg,#2a2723,#1c1a17)"
        glow="box-shadow:0 26px 46px rgba(0,0,0,.5),0 0 40px rgba(212,162,127,.18), inset 0 2px 2px rgba(255,255,255,.08);" if lit else "box-shadow:0 22px 40px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.05);"
        kc=f"rgb({ACC})" if lit else "#8f8f85"
        rows=""
        for t in lines:
            dot=f'<span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});flex-shrink:0"></span>' if lit else f'<span style="width:9px;height:2px;background:#6f6a60;flex-shrink:0;margin-top:9px"></span>'
            rows+=(f'<div style="display:flex;align-items:flex-start;gap:11px;margin-top:12px"><div style="margin-top:6px">{dot}</div>'
              f'<span style="font-family:\'DM Sans\';font-size:17px;color:{"#e2dccf" if lit else "#8f8f85"};line-height:1.35">{t}</span></div>')
        return (f'<div style="flex:1;background:{bg};border:1.5px solid {bd};border-radius:22px;padding:24px 24px 26px;{glow}">'
          f'<div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.16em;color:{kc}">{kind}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:30px;color:#FAFAF7;margin-top:8px">{head}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8f8f85;margin-top:3px">{sub}</div>{rows}</div>')
    left=panel("A TOOL","Does one trick","then waits for you",["autocomplete a line","lint a file","map a repo"],False)
    right=panel("A DESK","Owns an outcome","and reports it back",["SPECTER books the meeting","STRIKER closes the deal","PULSE ships the post"],True)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Desks, not tools","FOUNDER PLUGINS")}
      <div style="display:flex;align-items:stretch;gap:20px;position:relative">
        {left}
        <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:3;width:58px;height:58px;border-radius:50%;
          background:linear-gradient(160deg,#3a352f,#1c1a17);border:1.5px solid rgba(212,162,127,.5);display:flex;align-items:center;justify-content:center;
          font-family:'DM Sans';font-weight:900;font-size:18px;color:rgb({ACC});box-shadow:0 12px 24px rgba(0,0,0,.5)">vs</div>
        {right}
      </div>
      {cap("research, outbound, deals, content, legal: each install owns an outcome.")}</div>'''

# 4. DESKCHECK - node graph: one question fans into three desk outputs
def deskcheck():
    W,H=820,430
    qx,qy=140,215
    outs=[("CORTEX","ranked briefs",84),("SPECTER","booked replies",215),("STRIKER","closed deals",346)]
    edges=""; nodes=""
    tx=560
    for nm,out,y in outs:
        mx=(qx+tx)/2
        edges+=f'<path d="M{qx+96} {qy} C{mx:.0f} {qy},{mx:.0f} {y},{tx-6} {y}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
        nodes+=(f'<g><rect x="{tx}" y="{y-46}" width="238" height="92" rx="16" fill="url(#nc)" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{tx+22}" y="{y-14}" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({ACC})">{nm}</text>'
          f'<text x="{tx+22}" y="{y+22}" font-family="DM Sans" font-weight="800" font-size="24" fill="#FAFAF7">{out}</text>'
          f'<circle cx="{tx+214}" cy="{y}" r="6" fill="#7fd39a" filter="url(#ld)"/></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every plugin answers one thing","WHAT LANDS?")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="nc" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <linearGradient id="qg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#221e1a"/></linearGradient>
          <filter id="ld" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#7fd39a" flood-opacity="0.9"/></filter>
        </defs>
        {edges}
        <rect x="{qx-96}" y="{qy-72}" width="192" height="144" rx="24" fill="url(#qg)" stroke="rgb({ACC})" stroke-width="2"/>
        <text x="{qx}" y="{qy-18}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">What</text>
        <text x="{qx}" y="{qy+14}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">lands?</text>
        <text x="{qx}" y="{qy+50}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">in the pipeline</text>
        {nodes}
      </svg>
      {cap("what enters the pipeline because this exists. cortex briefs, specter replies, striker closes.")}</div>'''

# 5. STACKP - isometric stack of the five founder desks, you pinned on the gate above
def stackp():
    rows=[("CORTEX","intel &middot; ranked briefs","brief"),
          ("SPECTER","outreach &middot; sent replies","reply"),
          ("STRIKER","deals &middot; close plans","close"),
          ("PULSE","content &middot; posts live","post"),
          ("COUNSEL","paperwork &middot; NDAs, MSAs","doc")]
    cards=""
    for i,(nm,sub,out) in enumerate(rows):
        y=i*94
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);'
          f'border:1.5px solid rgba(255,255,255,.14);border-radius:16px;padding:16px 22px;'
          f'box-shadow:0 28px 42px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#FAFAF7;margin-top:2px">{sub}</div></div>'
          f'<div style="flex-shrink:0;font-family:\'DM Mono\';font-size:13px;color:#c9a583;background:rgba(212,162,127,.12);'
          f'border:1px solid rgba(212,162,127,.3);border-radius:9px;padding:7px 13px">{out}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Five desks, one company","THE STACK")}
      <div style="perspective:2000px;height:520px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-9deg);width:560px;height:470px;position:relative">
          <div style="position:absolute;left:150px;top:-6px;background:rgb({ACC});color:#1a0f0a;font-family:'DM Sans';font-weight:900;font-size:15px;
            padding:9px 20px;border-radius:999px;box-shadow:0 12px 24px rgba(212,162,127,.4);z-index:9">YOU &middot; on the gate</div>
          {cards}
        </div>
      </div>
      {cap("intel, outreach, deals, content, paperwork. the sixth desk is you, on the gate.")}</div>'''

# 6. TESTRUN - a 48-hour timeline of receipts, uninstall verdict at the end (ivory)
def testrun():
    W,H=830,300; y0=150; x0=70; x1=760
    stops=[("0h","install",""),("16h","20 briefs","CORTEX"),("32h","10 drafts","SPECTER"),("48h","1 proposal out","STRIKER")]
    n=len(stops); dots=""
    for i,(hr,ev,ag) in enumerate(stops):
        x=x0+(x1-x0)*i/(n-1); last=(i==n-1)
        col=IVA if last else "#a86a44"
        r=17 if last else 12
        dots+=(f'<line x1="{x:.0f}" y1="{y0-r-6}" x2="{x:.0f}" y2="{y0-58}" stroke="rgba(150,90,45,.35)" stroke-width="1.5"/>'
          f'<circle cx="{x:.0f}" cy="{y0}" r="{r}" fill="{col}"/>')
        if last:
            dots+=f'<path d="M{x-7:.0f} {y0} l4 4 l8 -9" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
        dots+=(f'<text x="{x:.0f}" y="{y0-66}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#2a2016">{ev}</text>'
          f'<text x="{x:.0f}" y="{y0+40}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="{IVA}">{hr}</text>')
        if ag: dots+=f'<text x="{x:.0f}" y="{y0+62}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a08a68">{ag}</text>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 30px">
      {htitle("Demand a receipt in 48h","INSTALL TEST",ink="#2a2016",tagcol=IVA)}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="rgba(150,90,45,.3)" stroke-width="4" stroke-linecap="round"/>
        <line x1="{x0}" y1="{y0}" x2="{x0+(x1-x0)*(n-1)/(n-1)}" y2="{y0}" stroke="{IVA}" stroke-width="4" stroke-linecap="round" opacity="0.5"/>
        {dots}
      </svg>
      <div style="display:flex;justify-content:center;margin-top:2px">
        <div style="display:inline-flex;align-items:center;gap:10px;background:rgba({RED},.12);border:1px solid rgba({RED},.4);border-radius:999px;padding:8px 18px">
          <span style="width:9px;height:9px;border-radius:50%;background:rgb({RED})"></span>
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.06em;color:#a8402a">no receipt by 48h &rarr; uninstall</span></div>
      </div>
      {cap("twenty briefs, ten drafts, one proposal out. no receipt, uninstall.","#8a745a")}</div>'''

# 7. TRAPB - dot field of installs that produce nothing: 10 plugins lit, output stays at zero
def trapb():
    dots=""
    cell=44; gap=18
    for i in range(10):
        r,c=divmod(i,5); x=c*(cell+gap); y=r*(cell+gap)
        dots+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="11" fill="url(#lit)" filter="url(#lg)" stroke="rgba(255,255,255,.14)"/>'
          f'<path d="M{x+11} {y+22} l6 6 l14 -16" fill="none" stroke="#1a0f0a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    fw=5*(cell+gap)-gap; fh=2*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten deep, still drafting alone","INSTALLED vs SHIPPED")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex-shrink:0">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:14px">10 DEV PLUGINS RUNNING</div>
          <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
            <defs><radialGradient id="lit" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
            <filter id="lg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
            {dots}
          </svg>
        </div>
        <svg width="52" height="40" viewBox="0 0 52 40" style="flex-shrink:0"><path d="M4 20h40M32 8l14 12-14 12" fill="none" stroke="#6f6a60" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex:1;background:linear-gradient(162deg,#2a2723,#1a1815);border:1.5px dashed rgba(200,70,35,.4);border-radius:20px;padding:26px 28px;text-align:center">
          <div style="font-family:'DM Sans';font-weight:900;font-size:76px;color:#8f8f85;line-height:1">0</div>
          <div style="font-family:'DM Mono';font-size:14px;letter-spacing:.1em;color:#a8402a;margin-top:2px">FOLLOW-UPS SENT</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#8f8f85;margin-top:14px">the graph mapper cannot write it. a desk can.</div>
        </div>
      </div>
      {cap("ten dev plugins deep and the outbox is still empty. the desk drafts, the tool waits.")}</div>'''

# 8. RULE7 - radial decision hub: what the plugin page shows routes you to keep or leave
def rule7():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Shop by outcome, not demo","THE RULE")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="hub" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter>
        </defs>
        <!-- spokes -->
        <path d="M262 215 C380 130,430 92,520 92" fill="none" stroke="rgba(200,70,35,.5)" stroke-width="4"/>
        <path d="M262 215 C380 300,430 338,520 338" fill="none" stroke="rgba(212,162,127,.6)" stroke-width="4"/>
        <!-- hub -->
        <g filter="url(#hg)"><circle cx="180" cy="215" r="102" fill="url(#hub)"/></g>
        <text x="180" y="204" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">THE</text>
        <text x="180" y="240" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">RULE</text>
        <!-- BAD verdict: shows code -->
        <rect x="520" y="42" width="278" height="100" rx="20" fill="#221d1a" stroke="rgba(200,70,35,.5)" stroke-width="1.5"/>
        <g transform="translate(548,72)"><circle cx="20" cy="20" r="20" fill="rgba(200,70,35,.16)"/><path d="M12 12l16 16M28 12l-16 16" stroke="rgb({RED})" stroke-width="3" stroke-linecap="round"/></g>
        <text x="606" y="86" font-family="DM Sans" font-weight="800" font-size="22" fill="#e2dccf">Page shows code</text>
        <text x="606" y="116" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="#c86a52">wrong aisle &middot; walk on</text>
        <!-- GOOD verdict: shows pipeline -->
        <rect x="520" y="288" width="278" height="100" rx="20" fill="linear-gradient(160deg,#403a33,#241f1a)" stroke="rgb({ACC})" stroke-width="2"/>
        <rect x="520" y="288" width="278" height="100" rx="20" fill="#2a2620" stroke="rgb({ACC})" stroke-width="2"/>
        <g transform="translate(548,318)"><circle cx="20" cy="20" r="20" fill="rgba(212,162,127,.18)"/><path d="M11 21l6 6 12 -14" fill="none" stroke="rgb({ACC})" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></g>
        <text x="606" y="332" font-family="DM Sans" font-weight="800" font-size="22" fill="#FAFAF7">Page shows pipeline</text>
        <text x="606" y="362" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="rgb({ACC})">right desk &middot; install</text>
      </svg>
      {cap("if the plugin page shows code, you are in the wrong aisle. if it shows pipeline, install.")}</div>'''

PANELS={"aisle":aisle(),"tell":tell(),"flip":flip(),"deskcheck":deskcheck(),
        "stackp":stackp(),"testrun":testrun(),"trapb":trapb(),"rule7":rule7()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/wrongaisle"; os.makedirs(outd,exist_ok=True)
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
