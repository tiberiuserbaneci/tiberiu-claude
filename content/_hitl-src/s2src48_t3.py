#!/usr/bin/env python3
# TIER 3 - NOTHING TO INSTALL, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
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

# 1. INSTALL - radial: one lit installed SKILL token, 4 real jobs as empty MANUAL sockets around it
def install():
    cx,cy=306,222; Rr=152
    sockets=[("SOURCE",-90),("WRITE",0),("QUALIFY",90),("SHIP",180)]
    ring=""
    for nm,a in sockets:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a)); ly=y+54
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(250,250,247,.10)" stroke-width="1.5" stroke-dasharray="3 7"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="rgba(250,250,247,.02)" stroke="rgba(250,250,247,.16)" stroke-width="2" stroke-dasharray="5 6"/>'
          f'<line x1="{x-13:.0f}" y1="{y-13:.0f}" x2="{x+13:.0f}" y2="{y+13:.0f}" stroke="rgba(200,70,35,.55)" stroke-width="2.4"/>'
          f'<text x="{x:.0f}" y="{ly:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="#7a746a">{nm} · STILL MANUAL</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You installed the skill","1 TRICK ADDED")}
      <svg width="612" height="476" viewBox="0 0 612 476" style="display:block;margin:0 auto">
        <defs><radialGradient id="lit" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="glow" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        {ring}
        <circle cx="{cx}" cy="{cy}" r="50" fill="url(#lit)" filter="url(#glow)"/>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">SKILL</text>
        <text x="{cx}" y="{cy+82}" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".12em" fill="rgb({ACC})">INSTALLED · DONE NOTHING</text>
      </svg>
      {cap("a skill is one trick in the chatbox. the real jobs are still on you.")}</div>'''

# 2. GLUE - the founder node tangled into a web of config chores (keys, mcp, updates)
def glue():
    fx,fy=150,232
    chores=[("API KEYS",470,68),("MCP CONFIG",520,176),("SKILL FILES",500,286),("UPDATES",450,392),("VERSION LOCK",270,430)]
    web=""; nodes=""
    for nm,x,y in chores:
        mx=(fx+x)/2+18; my=(fy+y)/2-24
        web+=f'<path d="M{fx+44} {fy} Q{mx:.0f} {my:.0f} {x-70} {y}" fill="none" stroke="rgba(200,70,35,.45)" stroke-width="2" stroke-dasharray="4 7"/>'
        nodes+=(f'<rect x="{x-70}" y="{y-24}" width="150" height="48" rx="13" fill="#241f1b" stroke="rgba(200,70,35,.34)" stroke-width="1.5"/>'
          f'<text x="{x+5}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#c7bfb3">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One command to install","THE HIDDEN JOB")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="fnd" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="fg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {web}
        <g filter="url(#fg)"><circle cx="{fx}" cy="{fy}" r="62" fill="url(#fnd)"/></g>
        <text x="{fx}" y="{fy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">YOU</text>
        <text x="{fx}" y="{fy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">now devops</text>
        {nodes}
      </svg>
      {cap("keys, configs, updates, glue - the setup quietly becomes your second job.")}</div>'''

# 3. ROUTER - plain-English in, three cent-priced tier lanes, SMART lane picked
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
    hubx,hy=170,230; lx=470
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C320 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:300px;top:{y-40}px;width:160px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You just talk, it routes","MODEL ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">plain<br>English</div>
        {cards}
      </div>
      {cap("no skill to add. the cheapest tier that can do the job, in cents.")}</div>'''

# 4. ROSTER - Ultron sphere core, seven named agent nodes on spokes (all pre-wired)
def roster():
    cx,cy,R=410,232,168
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    spokes=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/7); x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        nodes+=(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#2a2724" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="rgb({ACC})">{role}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, already wired","THE ROSTER")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#og)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#orb)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">ULTRON</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one login</text>
      </svg>
      {cap("a whole operating team, pre-built - not seven plugins you bolt on and babysit.")}</div>'''

# 5. CENTS - IVORY: the subscription stack (high $) vs one Ultron run (cents)
def cents():
    tools=[("Sourcing tool","$99"),("Sequencer","$149"),("Enrichment","$120"),("Copy tool","$79"),("Scheduler","$59")]
    rows=""
    for nm,pr in tools:
        rows+=(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:11px 16px;background:rgba(150,90,45,.06);border:1px solid rgba(150,90,45,.14);border-radius:11px;margin-bottom:8px">'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:17px;color:#4a3a28">{nm}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:19px;color:#96562d">{pr}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The skill was free, the stack was not","MONTHLY","#2a2016")}
      <div style="display:flex;gap:30px;align-items:stretch">
        <div style="flex:1">{rows}
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:6px;padding:0 4px">
            <span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#8a745a">FIVE SEATS / MONTH</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#96562d">$506</span></div></div>
        <div style="flex-shrink:0;width:246px;background:linear-gradient(160deg,#2b2b28,#1d1d1b);border-radius:22px;padding:26px 24px;display:flex;flex-direction:column;justify-content:center;box-shadow:0 26px 44px rgba(120,95,60,.28)">
          <div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.14em;color:rgb({ACC})">ULTRON · SAME JOB</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:64px;color:#FAFAF7;line-height:1;margin:10px 0 2px">7c</div>
          <div style="font-family:DM Sans;font-size:16px;color:#c9c3b8">per run, pay per token</div>
          <div style="margin-top:16px;font-family:DM Mono;font-size:12px;color:#8f8f85">no seats · no lock-in</div></div>
      </div>
      {cap("a wall of subscriptions to run one funnel. ultron runs it for cents.","#8a745a")}</div>'''

# 6. MEMORY - radial shared core, agent lifelines, four memory tokens feeding in
def memory():
    cx,cy=210,214
    agents=[("outbound",-90),("deals",-18),("content",54),("code",126),("research",198)]
    lines=""; nodes=""
    for nm,a in agents:
        x=cx+150*math.cos(math.radians(a)); y=cy+150*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="31" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="420" height="428" viewBox="0 0 420 428">
        <defs><radialGradient id="hb" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#2a160c">CORE</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">your memory</text>{nodes}</svg>
      <div style="flex:1">
        {htitle("One core, every agent","SHARED MEMORY")}
        <div style="display:flex;flex-wrap:wrap;gap:9px;margin-bottom:6px">
          {"".join(f'<span style="font-family:DM Mono;font-size:14px;color:#d9d5cc;background:rgba(212,162,127,.1);border:1px solid rgba(212,162,127,.3);border-radius:9px;padding:8px 14px">{t}</span>' for t in ["ICP","pipeline","pricing","docs"])}
        </div>
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45;margin-top:8px">A bolt-on skill starts cold every time. Ultron reads the same core on every job.</div>
        {cap("no memory, no operator. one core feeds them all.")}</div></div>'''

# 7. GATE - IVORY: a queued external action parked at a lock, waiting for your tap
def gate():
    queue=[("Send 40 emails","SPECTER"),("Publish the post","AMPLIFY"),("Sign the NDA","COUNSEL")]
    rows=""
    for i,(act,ag) in enumerate(queue):
        held = i==0
        bd="#96562d" if held else "rgba(150,90,45,.16)"
        state=('<span style="font-family:DM Mono;font-size:12px;color:#96562d;display:flex;align-items:center;gap:6px">'
               '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.6"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>held for tap</span>') if held else '<span style="font-family:DM Mono;font-size:12px;color:#a89372">queued</span>'
        rows+=(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:15px 18px;background:rgba(255,255,255,.55);border:1.5px solid {bd};border-radius:14px;margin-bottom:10px">'
          f'<div><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#2a2016">{act}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:#8a745a;margin-top:2px">{ag}</div></div>{state}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("It can send. It waits for you.","HUMAN GATE","#2a2016")}
      {rows}
      <div style="display:flex;gap:12px;margin-top:6px">
        <div style="flex:1;background:#96562d;color:#fdfbf6;font-family:DM Sans;font-weight:900;font-size:18px;text-align:center;padding:15px;border-radius:14px;box-shadow:0 14px 24px rgba(150,90,45,.34)">Approve &#10003;</div>
        <div style="flex:1;background:rgba(150,90,45,.1);color:#96562d;font-family:DM Sans;font-weight:800;font-size:18px;text-align:center;padding:15px;border-radius:14px;border:1.5px solid rgba(150,90,45,.24)">Hold</div>
      </div>
      {cap("every external move parks at the gate. powerful, never unsupervised.","#8a745a")}</div>'''

# 8. OPERATOR - scattered skill chips converge into one glowing Ultron operator
def operator():
    scat=[("skill",70,96),("skill",70,206),("skill",70,316),("plugin",192,150),("plugin",192,262)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+34} {y} C360 {y},380 214,520 214" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<rect x="{x-34}" y="{y-20}" width="68" height="40" rx="11" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.75"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Stop collecting skills","ONE OPERATOR")}
      <svg width="820" height="446" viewBox="0 0 820 446" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="590" cy="214" r="122" fill="url(#bod)"/></g>
        <text x="590" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="590" y="230" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">LOGIN</text>
        <text x="590" y="372" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">wired · gated · yours</text>
      </svg>
      {cap("one login runs research, outbound, deals and content - the whole company.")}</div>'''

PANELS={"install":install(),"glue":glue(),"router":router(),"roster":roster(),
        "cents":cents(),"memory":memory(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src48"; os.makedirs(outd,exist_ok=True)
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
