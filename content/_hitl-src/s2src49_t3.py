#!/usr/bin/env python3
# TIER 3 - YOU ARE NOT AN AI ENGINEER (s2src49). Source: a "Top 60 Claude repos / frameworks"
# shopping list. Reframe: those frameworks are scaffolding for engineers - you star them and ship
# nothing; Ultron ships the 7 agents already wired, routed, gated, in your voice, priced in cents.
# Each panel a UNIQUE hand-built coded scene on a clean rounded card, title + one caption, no chip
# strips, no cuts/walls. 2 ivory panels. Warm palette only. Suprascrie models_clay/s2src49/*.png.
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

# 1. GRAVEYARD - a messy pile of overlapping, tilted, dim repo cards (real DIY frameworks) with star
# counts and a "not installed" line, a big faded UNSHIPPED stamp diagonally across. The pile IS the
# scene (no neat iso stack). Distinct form: scattered overlap.
def graveyard():
    repos=[("LangGraph","26K",-7,26,16),("AutoGPT","170K",6,338,50),("CrewAI","30K",-4,92,172),
           ("Spec Kit","50K",8,364,196),("Aider","30K",-6,58,326)]
    cards=""
    for nm,star,rot,x,y in repos:
        cards+=f'''<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);width:300px;
          background:linear-gradient(160deg,#2a2723,#1b1815);border:1px solid rgba(255,255,255,.08);border-radius:16px;
          padding:15px 18px;box-shadow:0 24px 40px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.06);opacity:.92;display:flex;align-items:center;gap:14px">
          <div style="flex-shrink:0;width:42px;height:42px;border-radius:11px;background:#141210;border:1px solid rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:20px;color:#6f6a60">{nm[0]}</div>
          <div style="flex:1"><div style="font-family:'DM Mono';font-weight:500;font-size:17px;color:#cfc9bd">{nm}</div>
            <div style="font-family:'DM Sans';font-size:13px;color:#8f8f85;margin-top:1px">{star} stars &middot; not installed</div></div>
          <span style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">&#9733;</span></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The starred-repo graveyard","0 SHIPPED")}
      <div style="position:relative;height:472px">
        {cards}
        <svg width="820" height="472" viewBox="0 0 820 472" style="position:absolute;left:0;top:0;pointer-events:none">
          <text x="452" y="256" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="76" fill="rgba(200,70,35,.20)" transform="rotate(-12 452 256)" letter-spacing="6">UNSHIPPED</text>
        </svg>
      </div>
      {cap("frameworks for engineers. you starred sixty and shipped nothing.")}</div>'''

# 2. ROSTER - radial hub-and-spokes: 7 named Ultron agents already wired around one ULTRON core,
# every node live. Distinct form: constellation of 7 (not a stack, not a radar).
def roster():
    cx,cy=306,225; Rr=168
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; n=len(agents)
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="39" fill="#221f1b" stroke="rgba(212,162,127,.34)" stroke-width="1.8"/>'
          f'<circle cx="{x+27:.0f}" cy="{y-27:.0f}" r="5.5" fill="#7fd39a" filter="url(#ld)"/>'
          f'<text x="{x:.0f}" y="{y-1:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14.5" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, already wired","THE ROSTER")}
      <svg width="612" height="500" viewBox="0 0 612 500" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="ld" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#7fd39a" flood-opacity="0.9"/></filter></defs>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ULTRON</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one login</text>
      </svg>
      {cap("no pip install, no graph to wire. the framework is the product.")}</div>'''

# 3. ROUTER - a job token enters a ROUTER diamond and two picks fall out: which agent, which tier.
# Distinct form: a small left-to-right decision flow with a diamond node.
def router():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("No orchestration to write","ROUTER")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="dia" cx="38%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="dg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="16" y="175" width="180" height="80" rx="16" fill="#221f1b" stroke="rgba(255,255,255,.1)"/>
        <text x="106" y="207" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c9c3b8">draft 12</text>
        <text x="106" y="229" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c9c3b8">follow-ups</text>
        <path d="M196 215 H288" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round"/>
        <g filter="url(#dg)"><path d="M412 125 L494 215 L412 305 L330 215 Z" fill="url(#dia)"/></g>
        <text x="412" y="209" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">ROUTER</text>
        <text x="412" y="231" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">reads job</text>
        <path d="M494 195 C560 155,592 120,624 120" stroke="rgb({ACC})" stroke-width="4" fill="none"/>
        <path d="M494 235 C560 275,592 310,624 310" stroke="rgb({ACC})" stroke-width="4" fill="none"/>
        <rect x="624" y="82" width="180" height="84" rx="16" fill="#2a2723" stroke="rgb({ACC})" stroke-width="1.5"/>
        <text x="642" y="112" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">AGENT</text>
        <text x="642" y="142" font-family="DM Sans" font-weight="800" font-size="22" fill="#FAFAF7">SPECTER</text>
        <rect x="624" y="272" width="180" height="84" rx="16" fill="#2a2723" stroke="rgb({ACC})" stroke-width="1.5"/>
        <text x="642" y="302" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">TIER &middot; SMART</text>
        <text x="642" y="334" font-family="DM Sans" font-weight="900" font-size="24" fill="#FAFAF7">0.11c</text>
      </svg>
      {cap("one job in, the right agent and the cheapest model that can do it.")}</div>'''

# 4. CENTS - IVORY: two comparison bars. The DIY stack + an engineer (big red, high $) vs Ultron
# (tiny accent, cents). High price only ever a competitor. Distinct form: bar comparison.
def cents():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:24px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Free to star. Brutal to run.</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">THE PRICE</span></div>
      <div style="margin-bottom:28px">
        <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:9px">
          <span style="font-family:'DM Sans';font-weight:700;font-size:18px;color:#5a4634">The DIY stack + an engineer</span>
          <span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#c84623">$2,400<span style="font-size:16px;font-weight:700"> /mo</span></span></div>
        <div style="height:46px;width:100%;border-radius:12px;background:linear-gradient(160deg,#d06a4e,#be4628);box-shadow:inset 0 2px 3px rgba(255,255,255,.25), 0 12px 24px rgba(190,70,40,.28)"></div></div>
      <div>
        <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:9px">
          <span style="font-family:'DM Sans';font-weight:700;font-size:18px;color:#5a4634">Ultron</span>
          <span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#96562d">cents<span style="font-size:16px;font-weight:700"> /run</span></span></div>
        <div style="height:46px;width:9%;border-radius:12px;background:linear-gradient(160deg,#e6b48f,#96562d);box-shadow:inset 0 2px 3px rgba(255,255,255,.4), 0 12px 24px rgba(150,90,45,.3)"></div></div>
      {cap("pay per token. no infra bill, no salary, no framework to maintain.","#8a745a")}</div>'''

# 5. GATE - full-capability orb on a dashed rein to a lock. Human gate. Distinct form: mechanism
# (orb -> tether -> lock), warm accent lock, "your tap".
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Strong body. Your reins.","HUMAN GATE")}
      <svg width="820" height="410" viewBox="0 0 820 410" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="205" r="128" fill="url(#orb)"/></g>
        <text x="200" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="32" fill="#2a160c">FULL</text>
        <text x="200" y="234" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <path d="M330 205 H598" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="612" y="132" width="150" height="150" rx="32" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(657,172)"><rect x="0" y="36" width="60" height="46" rx="10" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M11 36 V22 a19 19 0 0 1 38 0 v14" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="687" y="322" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("it sends nothing until you approve. augmented, never unsupervised.")}</div>'''

# 6. MEMORY - concentric labeled strata core: ICP / PIPELINE / PRICING / DOCS / VOICE ringing one
# glowing memory core. Distinct form: strata rings (no spokes, no radar sweep).
def memory():
    cx,cy=306,250
    bands=[("VOICE",250),("DOCS",205),("PRICING",160),("PIPELINE",115),("ICP",70)]
    rings=""
    for i,(nm,r) in enumerate(bands):
        op=0.30-0.04*i
        rings+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,{op:.2f})" stroke-width="2"/>'
        rings+=f'<text x="{cx}" y="{cy-r+20}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#b9b3a7">{nm}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One core every agent reads","SHARED MEMORY")}
      <svg width="612" height="520" viewBox="0 0 612 520" style="display:block;margin:0 auto">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {rings}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="40" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">MEMORY</text>
      </svg>
      {cap("persistent state you never configure. nothing forgets you.")}</div>'''

# 7. VOICE - IVORY: style-match gauge + a sample written in your voice + 3 checks. Distinct form:
# gauge ring + quote (light card).
def voice():
    pct=97; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It writes in your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">VOICE MATCH</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:190px;height:190px">
          <svg width="190" height="190" viewBox="0 0 190 190">
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 95 95)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:'DM Sans';font-weight:900;font-size:44px;color:#2a2016">{pct}%</span>
            <span style="font-family:'DM Mono';font-size:12px;color:#96562d">style match</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4">
            "I starred sixty repos and shipped none. The tool I kept had no framework to learn."</div>
          <div style="display:flex;gap:22px;margin-top:16px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["short lines","no hedging","your cadence"])}
          </div></div>
      </div>
      {cap("sampled from your real posts, banned words enforced on every draft.","#8a745a")}</div>'''

# 8. OPERATOR - scattered agent nodes converge into one app-window login (app.51ultron.com, one
# prompt, RUN). Distinct form: convergence into a framed product window.
def operator():
    scat=[("CORTEX",68,78),("SPECTER",68,190),("PULSE",68,302),("SENTINEL",188,134),("AMPLIFY",188,246)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+30} {y} C330 {y},360 190,470 190" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="28" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.72"/>'
          f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#9a9488">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Close the tabs. Open one login.","ONE OPERATOR")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        {left}
        <rect x="470" y="66" width="332" height="252" rx="18" fill="#1b1815" stroke="rgba(212,162,127,.4)" stroke-width="2"/>
        <rect x="470" y="66" width="332" height="42" rx="18" fill="#2a2723"/>
        <rect x="470" y="88" width="332" height="20" fill="#2a2723"/>
        <circle cx="492" cy="87" r="5" fill="#c84623"/><circle cx="510" cy="87" r="5" fill="rgb({ACC})"/><circle cx="528" cy="87" r="5" fill="#7fd39a"/>
        <text x="636" y="92" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">app.51ultron.com</text>
        <rect x="494" y="150" width="284" height="54" rx="12" fill="#241f1a" stroke="rgba(212,162,127,.3)"/>
        <text x="512" y="183" font-family="DM Sans" font-size="16" fill="#8f8f85">Ask Ultron anything...</text>
        <rect x="494" y="228" width="150" height="42" rx="10" fill="rgb({ACC})"/>
        <text x="569" y="255" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#1a0f0a">RUN</text>
        <text x="636" y="300" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85" letter-spacing=".07em">seven agents &middot; one gate &middot; one memory</text>
      </svg>
      {cap("one chat routes every agent. no tabs, no installs, no framework.")}</div>'''

PANELS={"graveyard":graveyard(),"roster":roster(),"router":router(),"cents":cents(),
        "gate":gate(),"memory":memory(),"voice":voice(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src49"; os.makedirs(outd,exist_ok=True)
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
