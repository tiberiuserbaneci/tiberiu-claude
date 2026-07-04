#!/usr/bin/env python3
# TIER 3 - S2SRC47 "PROMPTS DON'T REMEMBER". Each panel a UNIQUE hand-built coded scene on a clean
# rounded CARD/CARDIV, htitle + one caption, warm palette, cents. No stat-chip strips, no cuts, no
# walls. Source = a 200-prompt copy-paste library; reframe = Ultron is the layer above prompts.
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
def htitleiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. PASTE - IVORY: a saved-prompt mock with bracket placeholders + a 0% context meter (stateless)
def paste():
    ph=lambda t:f'<span style="display:inline-block;font-family:\'DM Mono\';font-size:16px;color:#96562d;background:rgba(190,70,40,.10);border:1px solid rgba(190,70,40,.30);border-radius:7px;padding:2px 9px;margin:0 2px">{t}</span>'
    body=(f'<div style="font-family:\'DM Sans\';font-size:21px;line-height:1.85;color:#3a2f22">'
      f'Write a cold email to a founder at {ph("[YOUR ICP]")} about {ph("[PASTE PRODUCT]")}, '
      f'in the tone of {ph("[PASTE 3 POSTS]")}, using {ph("[PASTE PIPELINE]")}.</div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitleiv("Every prompt starts blank","STATELESS")}
      <div style="background:rgba(255,255,255,.62);border:1px solid rgba(120,95,60,.18);border-radius:20px;padding:26px 28px;box-shadow:inset 0 2px 4px rgba(255,255,255,.9),0 12px 24px rgba(120,95,60,.10)">
        <div style="display:flex;gap:8px;margin-bottom:18px">
          <span style="width:12px;height:12px;border-radius:50%;background:#d9cbb6"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#d9cbb6"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#d9cbb6"></span>
          <span style="margin-left:auto;font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#a08a68">SAVED PROMPT #17</span></div>
        {body}
      </div>
      <div style="margin-top:24px;display:flex;align-items:center;gap:20px">
        <div style="flex:1">
          <div style="display:flex;justify-content:space-between;font-family:'DM Mono';font-size:14px;color:#8a745a;margin-bottom:8px"><span>CONTEXT LOADED</span><span style="color:#be4628;font-weight:500">0%</span></div>
          <div style="height:14px;border-radius:999px;background:rgba(150,120,80,.18);overflow:hidden"><div style="width:2%;height:100%;background:#be4628;border-radius:999px"></div></div></div>
        <div style="flex-shrink:0;text-align:center;background:rgba(190,70,40,.08);border:1px solid rgba(190,70,40,.24);border-radius:14px;padding:12px 20px">
          <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#be4628;line-height:1">41x</div>
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.06em;color:#a08a68">re-pasted this week</div></div>
      </div>
      {cap("the words are saved. the business is not. you feed it in again, every run.","#8a745a")}</div>'''

# 2. ROUTER - one job token routed down 3 tier lanes, SMART lit/picked, cents per tier
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",228,True),("DEEP","hard judgement","0.40c",360,False)]
    hubx,hy=168,228; lx=474
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C322 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:302px;top:{y-40}px;width:168px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The router picks the tier","MODEL ROUTER")}
      <div style="position:relative;height:456px">
        <svg width="820" height="456" viewBox="0 0 820 456" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:12px;top:204px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">draft 12<br>follow-ups</div>
        {cards}
      </div>
      {cap("one job in, the cheapest tier that can actually do it - cents, never dollars.")}</div>'''

# 3. AGENTS - radial hub-and-spokes: ROUTER core, 7 named agents on the ring
def agents():
    cx,cy,R=306,236,182
    ag=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
        ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; nodes=""
    for i,(nm,role) in enumerate(ag):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#241f1a" stroke="rgba(212,162,127,.42)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one roster","SEVEN AGENTS")}
      <svg width="612" height="480" viewBox="0 0 612 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">routes work</text>
        {nodes}
      </svg>
      {cap("type plain english; it hands the job to the agent that owns it.")}</div>'''

# 4. MEMORY - glowing core (left) feeding 4 data-lifelines to labelled record chips (right)
def memory():
    cx,cy=180,214
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (60,96,132))
    data=[("ICP","founder, 2-50, US/UK"),("PIPELINE","41 open, 6 hot"),("PRICING","cents per token"),("DOCS","every technique")]
    chips=""
    for nm,sub in data:
        chips+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:15px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.8);flex-shrink:0"></span>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:600;font-size:17px;color:#e6e1d6">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="360" height="440" viewBox="0 0 360 440" style="flex-shrink:0">
        <defs><radialGradient id="mc" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {"".join(f'<line x1="{cx+54}" y1="{cy}" x2="352" y2="{68+i*104}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>' for i in range(4))}
        {rings}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="50" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">MEMORY</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">one core</text>
      </svg>
      <div style="flex:1;display:flex;flex-direction:column;gap:13px">
        {htitle("One memory, every agent","SHARED CORE")}
        {chips}
        {cap("prompts forget on close. the core remembers your whole business.")}
      </div></div>'''

# 5. GATE - a parked outbound queue (3 actions held) + one big approve control
def gate():
    q=[("SPECTER","email to 24 leads","drafted"),("PULSE","publish launch post","staged"),("COUNSEL","send NDA to Globex","ready")]
    rows=""
    for who,what,st in q:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:15px;padding:15px 18px;box-shadow:0 12px 22px rgba(0,0,0,.45)">'
          f'<svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0"><rect x="7" y="6" width="3.4" height="12" rx="1.4" fill="rgb({ACC})"/><rect x="13.6" y="6" width="3.4" height="12" rx="1.4" fill="rgb({ACC})"/></svg>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{what}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:#9a9488">{who} &middot; {st}</div></div>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:999px;padding:5px 13px;flex-shrink:0">PARKED</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without you","HUMAN GATE")}
      <div style="display:flex;flex-direction:column;gap:14px">{rows}</div>
      <div style="margin-top:22px;display:flex;align-items:stretch;border-radius:16px;overflow:hidden;box-shadow:0 18px 34px rgba(212,162,127,.28)">
        <div style="flex:1;background:rgba(212,162,127,.08);border:1px solid rgba(212,162,127,.34);border-right:none;border-radius:16px 0 0 16px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center">
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#9a9488">3 actions waiting</span>
          <span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">Review before any leave</span></div>
        <div style="flex-shrink:0;display:flex;align-items:center;gap:12px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 55%,#9a5a35);padding:0 30px">
          <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#1a0f0a">YOUR TAP</span>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
      </div>
      {cap("every external move parks here for approval - augmented, never unsupervised.")}</div>'''

# 6. COST - IVORY: competitor seat-stack (tall $ bar) vs Ultron cents (sliver). High $ = competitor only.
def cost():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitleiv("Seats vs tokens","THE MATH")}
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:70px;height:400px;padding:0 20px">
        <div style="display:flex;flex-direction:column;align-items:center">
          <div style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#be4628;line-height:1">$1,200</div>
          <div style="font-family:'DM Mono';font-size:13px;color:#a08a68;margin-bottom:14px">per month</div>
          <div style="width:150px;height:300px;border-radius:16px 16px 0 0;background:linear-gradient(180deg,#c96a4a,#be4628);box-shadow:inset 0 3px 4px rgba(255,255,255,.3),0 20px 34px rgba(190,70,40,.28);display:flex;flex-direction:column;justify-content:flex-end;padding:16px;gap:7px">
            {"".join('<div style="height:1px;background:rgba(255,255,255,.22)"></div>' for _ in range(6))}
            <div style="font-family:'DM Sans';font-weight:800;font-size:16px;color:#fff;text-align:center">6 seat tools</div></div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center">
          <div style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#2a2016;line-height:1">7c</div>
          <div style="font-family:'DM Mono';font-size:13px;color:#a08a68;margin-bottom:14px">per job run</div>
          <div style="width:150px;height:26px;border-radius:12px 12px 0 0;background:linear-gradient(180deg,#e6b48f,#c98a5f);box-shadow:inset 0 2px 3px rgba(255,255,255,.5),0 12px 22px rgba(150,120,80,.2)"></div>
          <div style="font-family:'DM Sans';font-weight:800;font-size:16px;color:#5a4634;margin-top:10px">Ultron, per token</div>
        </div>
      </div>
      {cap("you pay for the work a job burns, not for a shelf of empty seats.","#8a745a")}</div>'''

# 7. COVERAGE - vertical handoff spine: 7 stages, each an agent, wired end to end (no copy-paste)
def coverage():
    stages=[("Research","CORTEX","targets ranked"),("Outbound","SPECTER","sequences sent"),
            ("Deals","STRIKER","objections handled"),("Content","PULSE","posts in your voice"),
            ("Code","SENTINEL","shipped and tested"),("Publish","AMPLIFY","scheduled per channel"),
            ("Legal","COUNSEL","NDAs reviewed")]
    rows=""
    n=len(stages)
    for i,(stg,ag,out) in enumerate(stages):
        last=i==n-1
        arrow="" if last else f'<div style="position:absolute;left:19px;top:52px;bottom:-14px;width:2px;background:linear-gradient(180deg,rgba(212,162,127,.5),rgba(212,162,127,.5))"></div>'
        rows+=(f'<div style="position:relative;display:flex;align-items:center;gap:18px;padding-bottom:14px">'
          f'{arrow}'
          f'<div style="flex-shrink:0;width:40px;height:40px;border-radius:12px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.42);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:15px;color:rgb({ACC});z-index:1">{i+1}</div>'
          f'<div style="flex:1;display:flex;align-items:baseline;gap:12px"><span style="font-family:DM Sans;font-weight:800;font-size:21px;color:#FAFAF7">{stg}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">{ag}</span></div>'
          f'<span style="font-family:DM Sans;font-size:16px;color:#9a9488;flex-shrink:0">{out}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 42px 30px">
      {htitle("One pipeline, seven handoffs","ONE PIPELINE")}
      <div style="margin-top:4px">{rows}</div>
      {cap("the job flows stage to stage on its own - four prompt folders, retired.")}</div>'''

# 8. OPERATOR - scattered prompt-snippets converge into one glowing Ultron operator orb
def operator():
    scat=[("[PASTE CODE]",70,86),("[YOUR ICP]",70,196),("[PASTE POST]",70,306),("[PASTE DEAL]",190,142),("[PASTE DOC]",190,252)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+58} {y} C360 {y},380 208,528 208" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<rect x="{x-52}" y="{y-19}" width="112" height="38" rx="10" fill="#221f1b" stroke="rgba(255,255,255,.1)" opacity="0.8"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Close the folder, open the operator","ONE LOGIN")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="596" cy="208" r="122" fill="url(#bod)"/></g>
        <text x="596" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">ONE</text>
        <text x="596" y="228" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">OPERATOR</text>
        <text x="596" y="370" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">routes &middot; remembers &middot; gates</text>
      </svg>
      {cap("two hundred snippets become one system you run from a single chat.")}</div>'''

PANELS={"paste":paste(),"router":router(),"agents":agents(),"memory":memory(),
        "gate":gate(),"cost":cost(),"coverage":coverage(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src47"; os.makedirs(outd,exist_ok=True)
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
