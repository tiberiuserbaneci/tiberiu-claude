#!/usr/bin/env python3
# TIER 3 - DELETE THE PROMPT LIBRARY, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. HOARD - tile field of 120 saved prompts, only 4 ever reopened (lit); the rest dim/dead
def hoard():
    cols,rowsn=20,6  # 120
    reopened={17,44,79,101}
    cell=34; gap=8
    tiles=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in reopened:
            tiles+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="7" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            tiles+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="7" fill="rgba(250,250,247,.06)" stroke="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("120 prompts, filed and forgotten","REOPENED: 4")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:6px auto 0">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {tiles}</svg>
      <div style="display:flex;align-items:center;gap:16px;margin-top:22px;background:rgba(250,250,247,.03);border:1px solid rgba(255,255,255,.07);border-radius:16px;padding:16px 20px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:44px;color:rgb({ACC});line-height:1">3.3%</span>
        <span style="font-family:'DM Sans';font-size:18px;color:#c9c3b8;line-height:1.35">of the library you built ever gets opened twice</span></div>
      {cap("the cheat sheet felt like leverage. it is a cabinet you never visit.")}</div>'''

# 2. ROT - two decay curves: prompt effectiveness collapses at each model release, skills stay maintained
def rot():
    W,H=740,430; x0,y0=70,40; pw=W-x0-20; ph=H-y0-70
    def px(t): return x0+t*pw
    def py(v): return y0+(1-v)*ph
    # prompt decay: sawtooth dropping at 3 model releases
    ppts=[(0,.96),(.30,.80),(.30,.44),(.62,.30),(.62,.68),(.62,.24),(1,.12)]
    ppath="M"+" L".join(f"{px(t):.0f} {py(v):.0f}" for t,v in ppts)
    releases=[.30,.62]
    rel="".join(f'<line x1="{px(t):.0f}" y1="{y0}" x2="{px(t):.0f}" y2="{y0+ph}" stroke="rgba(200,70,35,.28)" stroke-width="1.5" stroke-dasharray="4 6"/>'
               f'<text x="{px(t):.0f}" y="{y0-14}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({RED})">model shift</text>' for t in releases)
    # skill line: maintained, small dips then corrected, stays high
    spts=[(0,.90),(.30,.86),(.36,.94),(.62,.88),(.68,.95),(1,.93)]
    spath="M"+" L".join(f"{px(t):.0f} {py(v):.0f}" for t,v in spts)
    grid="".join(f'<line x1="{x0}" y1="{py(v):.0f}" x2="{x0+pw}" y2="{py(v):.0f}" stroke="rgba(255,255,255,.05)"/>' for v in (0,.25,.5,.75,1))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Prompts rot the week models change","DECAY CURVE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="rg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        {grid}{rel}
        <line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+ph}" stroke="rgba(255,255,255,.16)"/>
        <line x1="{x0}" y1="{y0+ph}" x2="{x0+pw}" y2="{y0+ph}" stroke="rgba(255,255,255,.16)"/>
        <path d="{ppath}" fill="none" stroke="rgb({RED})" stroke-width="3.5" stroke-linejoin="round"/>
        <path d="{spath}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linejoin="round" filter="url(#rg)"/>
        <circle cx="{px(1):.0f}" cy="{py(.12):.0f}" r="7" fill="rgb({RED})"/>
        <circle cx="{px(1):.0f}" cy="{py(.93):.0f}" r="7" fill="rgb({ACC})" filter="url(#rg)"/>
        <text x="{x0-14}" y="{py(.98):.0f}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#8f8f85">works</text>
        <text x="{x0-14}" y="{py(.04):.0f}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#8f8f85">dead</text>
      </svg>
      <div style="display:flex;gap:30px;margin-top:6px">
        <div style="display:flex;align-items:center;gap:10px"><span style="width:22px;height:4px;border-radius:2px;background:rgb({ACC})"></span><span style="font-family:'DM Sans';font-size:16px;color:#d9d5cc">skills: versioned, corrected</span></div>
        <div style="display:flex;align-items:center;gap:10px"><span style="width:22px;height:4px;border-radius:2px;background:rgb({RED})"></span><span style="font-family:'DM Sans';font-size:16px;color:#d9d5cc">prompts: copy-paste, decaying</span></div></div>
      {cap("magic words expire on release day. skills get maintained.")}</div>'''

# 3. RETYPE - closed loop: paste -> tweak -> hope -> repeat, YOU trapped in the centre
def retype():
    cx,cy,R=210,210,150
    steps=[("PASTE",-90),("TWEAK",30),("HOPE",150)]
    arc=""; nodes=""
    for i,(nm,a) in enumerate(steps):
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        a2=steps[(i+1)%3][1]
        # arrow arc from this node toward next along the ring
        ax=cx+R*math.cos(math.radians(a+18)); ay=cy+R*math.sin(math.radians(a+18))
        bx=cx+R*math.cos(math.radians(a2-18)); by=cy+R*math.sin(math.radians(a2-18))
        arc+=f'<path d="M{ax:.0f} {ay:.0f} A{R} {R} 0 0 1 {bx:.0f} {by:.0f}" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="3" marker-end="url(#ar)"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
                f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><marker id="ar" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 z" fill="rgb({ACC})"/></marker>
        <filter id="yg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {arc}
        <g filter="url(#yg)"><circle cx="{cx}" cy="{cy}" r="58" fill="#2a160c" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="rgb({ACC})">YOU</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9a583">every run</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("Each use costs a re-wording","MANUAL LOOP")}
        <div style="font-family:'DM Sans';font-size:20px;color:#c9c3b8;line-height:1.45">Paste the block. Tweak the wording. Hope it lands. The 120 do not run themselves - they wait for your hands, every single time.</div>
        {cap("paste, tweak, hope. the loop never closes without you.")}</div></div>'''

# 4. TWELVE - a 3x4 command palette: the 120 collapse into 12 named skills, one slash-command each
def twelve():
    skills=[("/brief","research a target"),("/draft","write in your voice"),("/audit","score the funnel"),
            ("/price","build the quote"),("/followup","chase the thread"),("/report","weekly digest"),
            ("/qualify","rank the lead"),("/sequence","5-step outbound"),("/objection","handle the no"),
            ("/nda","draft + redline"),("/enrich","fill the record"),("/schedule","post per channel")]
    cells=""
    for cmd,desc in skills:
        cells+=(f'<div style="background:linear-gradient(158deg,#332f2a,#221e1a);border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:14px 16px;box-shadow:0 12px 22px rgba(0,0,0,.4), inset 0 1.5px 2px rgba(255,255,255,.07)">'
                f'<div style="font-family:\'DM Mono\';font-weight:500;font-size:18px;color:rgb({ACC})">{cmd}</div>'
                f'<div style="font-family:\'DM Sans\';font-size:13px;color:#9a9488;margin-top:3px">{desc}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">Twelve skills cover the 120</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">120 &rarr; 12</span></div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px">{cells}</div>
      {cap("brief, draft, audit, price, follow up, report: one command each, same play every run.")}</div>'''

# 5. ONELINE - IVORY terminal: a wall of prompt instructions collapses into one slash command
def oneline():
    lines=["You are an expert B2B growth analyst. Given a","funnel, first restate the stages, then for each","compute conversion, flag the weakest, propose 3","fixes ranked by effort. Use a formal tone, avoid","hedging, cite the metric behind every claim, and","return a table plus a short summary. Do not..."]
    strut="".join(f'<div style="height:11px;background:rgba(150,90,45,.16);border-radius:3px;margin-bottom:9px;width:{w}%"></div>' for w in (100,92,96,88,94,60))
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">A page became five words</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">COLLAPSED</span></div>
      <div style="display:flex;align-items:stretch;gap:26px">
        <div style="flex:1;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.18);border-radius:16px;padding:20px 22px;position:relative;opacity:.85">
          <div style="font-family:'DM Mono';font-size:11px;letter-spacing:.14em;color:#a08a68;margin-bottom:14px">THE OLD PROMPT &middot; 214 WORDS</div>
          {strut}
          <div style="position:absolute;inset:0;border-radius:16px;background:linear-gradient(180deg,rgba(245,236,227,0) 40%,rgba(245,236,227,.85))"></div>
        </div>
        <div style="flex-shrink:0;display:flex;flex-direction:column;justify-content:center;align-items:center;width:70px">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          <div style="font-family:'DM Mono';font-size:11px;color:#96562d;margin-top:8px;text-align:center">skill</div>
        </div>
        <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
          <div style="background:#241f1a;border-radius:14px;padding:22px 22px;box-shadow:0 20px 40px rgba(74,52,32,.34)">
            <div style="display:flex;gap:7px;margin-bottom:16px"><span style="width:11px;height:11px;border-radius:50%;background:#d96b4a"></span><span style="width:11px;height:11px;border-radius:50%;background:rgba(212,162,127,.7)"></span><span style="width:11px;height:11px;border-radius:50%;background:rgba(255,255,255,.3)"></span></div>
            <div style="font-family:'DM Mono';font-size:22px;color:#FAFAF7"><span style="color:rgb({ACC})">/audit</span> my funnel</div>
          </div>
          <div style="font-family:'DM Sans';font-size:15px;color:#8a745a;margin-top:14px;text-align:center">five words, same output</div>
        </div>
      </div>
      {cap("a page of instructions lives inside the skill now. you type five words.","#8a745a")}</div>'''

# 6. RUNS - a schedule timeline: a skill self-fires overnight on a trigger, a prompt just sits idle
def runs():
    W,H=760,300; x0=70; xr=W-40; y_skill=90; y_prompt=210
    ticks=[("00:00",0),("03:00",.25),("06:00",.5),("09:00",.75),("12:00",1)]
    def tx(f): return x0+f*(xr-x0)
    axis=""
    for lbl,f in ticks:
        axis+=(f'<line x1="{tx(f):.0f}" y1="60" x2="{tx(f):.0f}" y2="250" stroke="rgba(255,255,255,.05)"/>'
               f'<text x="{tx(f):.0f}" y="278" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#7a746a">{lbl}</text>')
    # skill lane: idle bar then a FIRE burst at a trigger
    firex=tx(.42)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Skills fire. Prompts wait.","AUTONOMY")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="fl" cx="50%" cy="50%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="fg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        {axis}
        <text x="{x0}" y="{y_skill-30}" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">SKILL</text>
        <rect x="{x0}" y="{y_skill-8}" width="{xr-x0}" height="16" rx="8" fill="rgba(212,162,127,.14)"/>
        <line x1="{firex:.0f}" y1="{y_skill-46}" x2="{firex:.0f}" y2="{y_skill}" stroke="rgba(212,162,127,.5)" stroke-width="1.5" stroke-dasharray="3 5"/>
        <text x="{firex:.0f}" y="{y_skill-52}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9a583">trigger: new signal</text>
        <g filter="url(#fg)"><circle cx="{firex:.0f}" cy="{y_skill}" r="26" fill="url(#fl)"/></g>
        <text x="{firex:.0f}" y="{y_skill+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="13" fill="#2a160c">FIRE</text>
        <rect x="{firex+34:.0f}" y="{y_skill-6}" width="{xr-firex-34:.0f}" height="12" rx="6" fill="rgb({ACC})"/>
        <text x="{y_prompt}" y="{y_prompt-30}" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#8f8f85" transform="translate({x0-70},60)"></text>
        <text x="{x0}" y="{y_prompt-30}" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#8f8f85">PROMPT</text>
        <rect x="{x0}" y="{y_prompt-8}" width="{xr-x0}" height="16" rx="8" fill="rgba(250,250,247,.05)" stroke="rgba(250,250,247,.08)" stroke-dasharray="6 6"/>
        <text x="{(x0+xr)/2:.0f}" y="{y_prompt+5}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#6f6a60">idle until you paste it</text>
      </svg>
      {cap("on triggers, on schedules, overnight: a skill fires itself. a prompt never will.")}</div>'''

# 7. GATE - full-capability orb held on the operator's reins, one lock (autonomous inside, tap outside)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Autonomous inside, your tap out","POWER, HELD")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="205" cy="210" r="132" fill="url(#orb)"/></g>
        <text x="205" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">SKILLS</text>
        <text x="205" y="234" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".1em">EXECUTE &middot; COMPOSE</text>
        <path d="M342 210 H600" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <text x="470" y="192" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">external send</text>
        <rect x="612" y="138" width="150" height="150" rx="32" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(658,178)"><rect x="0" y="36" width="60" height="44" rx="10" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M11 36 V22 a19 19 0 0 1 38 0 v14" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="687" y="322" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("skills execute and compose, and every external send still parks for you.")}</div>'''

# 8. PURGE - IVORY before/after split: the struck-out prompt notebook empties, 12 skill chips fill the desk
def purge():
    struck=["cold email v3 FINAL","cold email v3 FINAL(2)","icp research mega-prompt","funnel audit long","objection handler","weekly report prompt","enrichment prompt","...113 more"]
    old=""
    for i,s in enumerate(struck):
        old+=(f'<div style="display:flex;align-items:center;gap:10px;padding:7px 0;{"border-top:1px solid rgba(120,95,60,.14)" if i else ""}">'
              f'<span style="width:14px;height:14px;border-radius:4px;border:1.5px solid rgba(200,70,35,.5);flex-shrink:0"></span>'
              f'<span style="font-family:\'DM Mono\';font-size:14px;color:#a08a68;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">{s}</span></div>')
    chips=""
    for c in ["/brief","/draft","/audit","/price","/followup","/report","/qualify","/nda","/sequence","/enrich","/objection","/schedule"]:
        chips+=f'<span style="font-family:\'DM Mono\';font-size:15px;color:#96562d;background:rgba(150,90,45,.10);border:1px solid rgba(150,90,45,.24);border-radius:9px;padding:8px 12px">{c}</span>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Deleted mine in one afternoon</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">KEPT: 0</span></div>
      <div style="display:flex;gap:24px;align-items:stretch">
        <div style="flex:1;background:rgba(255,255,255,.5);border:1px solid rgba(120,95,60,.16);border-radius:16px;padding:18px 22px">
          <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px"><span style="font-family:'DM Mono';font-size:11px;letter-spacing:.14em;color:#a08a68">THE NOTEBOOK</span><span style="font-family:'DM Sans';font-weight:900;font-size:20px;color:rgb({RED})">120 &rarr; 0</span></div>
          {old}
        </div>
        <div style="flex:1;background:linear-gradient(160deg,#463d34,#332b24);border-radius:16px;padding:18px 22px;box-shadow:0 20px 40px rgba(74,52,32,.3)">
          <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px"><span style="font-family:'DM Mono';font-size:11px;letter-spacing:.14em;color:rgb({ACC})">THE DESK</span><span style="font-family:'DM Sans';font-weight:900;font-size:20px;color:#FAFAF7">12 skills</span></div>
          <div style="display:flex;flex-wrap:wrap;gap:9px">{chips.replace("#96562d","rgb("+ACC+")").replace("rgba(150,90,45,.10)","rgba(212,162,127,.12)").replace("rgba(150,90,45,.24)","rgba(212,162,127,.3)")}</div>
        </div>
      </div>
      {cap("kept zero prompts, minted twelve skills. the notebook is empty, the desk is full.","#8a745a")}</div>'''

PANELS={"hoard":hoard(),"rot":rot(),"retype":retype(),"twelve":twelve(),
        "oneline":oneline(),"runs":runs(),"gate":gate(),"purge":purge()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/no120"; os.makedirs(outd,exist_ok=True)
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
