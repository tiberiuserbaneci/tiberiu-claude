#!/usr/bin/env python3
# TIER 3 - YOU ARE THE BILL (adaptare IG "67 best open-source AI repos" in context Ultron).
# Fiecare panel e o scena UNICA construita din cod intr-un card rotunjit curat, title + un cap.
# NO generic stat-chip strips. Overwrites models_clay/s3src03/*.png. Cost zero.
import importlib.util, os, math, random
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SHOPPING LIST - a dense star-field: hundreds of faint GitHub stars, 67 lit "repo" stars in 4 clusters
def shoppinglist():
    random.seed(11)
    bg=""
    for _ in range(560):
        x=random.uniform(24,796); y=random.uniform(26,432)
        r=random.uniform(.6,1.7); o=random.uniform(.05,.17)
        bg+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="rgba({ACC},{o:.2f})"/>'
    clusters=[("INFERENCE",190,150,20),("RAG",610,150,17),("AGENTS",190,330,16),("VECTOR DB",610,330,14)]
    fg=""
    for nm,cx,cy,n in clusters:
        for _ in range(n):
            a=random.uniform(0,6.283); d=random.uniform(6,92)
            x=cx+d*math.cos(a); y=cy+d*math.sin(a)*0.72
            r=random.uniform(2.4,4.6)
            fg+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r+2.2:.1f}" fill="rgba({ACC},.16)"/>'
                 f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="rgb({ACC})" opacity="{random.uniform(.6,1):.2f}"/>')
        fg+=(f'<text x="{cx}" y="{cy-104}" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".12em" fill="#d9d5cc">{nm}</text>'
             f'<text x="{cx}" y="{cy-84}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">{n} repos</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Sixty-seven repos to clone","THE LIST")}
      <svg width="820" height="464" viewBox="0 0 820 464" style="display:block;margin:0 auto">
        {bg}{fg}
        <text x="410" y="452" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#7c766b">four layers &#183; sixty-seven repos &#183; zero of them running yet</text>
      </svg>
      {cap("the list looks free. cloning it is the only part that is.")}</div>'''

# 2. STAR TRAP - big ring gauge: 98K stars filled, a thin red sliver = 0 running
def startrap():
    r=118; circ=2*math.pi*r
    stars=circ*0.985; run=circ*0.0
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="360" height="360" viewBox="0 0 360 360">
        <defs><filter id="rg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <circle cx="180" cy="180" r="{r}" fill="none" stroke="rgba(212,162,127,.12)" stroke-width="26"/>
        <g filter="url(#rg)"><circle cx="180" cy="180" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="26" stroke-linecap="round" stroke-dasharray="{stars:.0f} {circ:.0f}" transform="rotate(-90 180 180)"/></g>
        <circle cx="180" cy="180" r="82" fill="none" stroke="rgba(200,70,35,.5)" stroke-width="6" stroke-dasharray="2 {2*math.pi*82:.0f}" transform="rotate(-90 180 180)"/>
        <text x="180" y="168" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="52" fill="#FAFAF7">98K</text>
        <text x="180" y="196" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({ACC})">GITHUB STARS</text>
        <text x="180" y="224" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="rgb({RED})">running: 0</text>
      </svg>
      <div style="flex:1">
        {htitle("A star is a bookmark","VANITY METRIC")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.5">98,000 people starred it. None of those stars host the model, write the glue, or answer your pager at 2am.</div>
        <div style="margin-top:16px;background:#211d19;border:1px solid rgba(200,70,35,.32);border-radius:14px;padding:14px 18px;display:flex;justify-content:space-between;align-items:baseline">
          <span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#FAFAF7">stars to production</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:rgb({RED})">0%</span></div>
        {cap("the star count is the easy number. the deploy count is the honest one.")}
      </div></div>'''

# 3. THE GLUE - bezier flow graph: three repos converge through a hand-written glue layer into your app
def theglue():
    left=[("ollama","inference",110),("chroma","vectors",235),("docling","ingest",360)]
    nodes=""; edges=""
    mx,my=392,235; ax,ay=700,235
    for nm,sub,y in left:
        broken=(nm=="docling")
        col=f"rgb({RED})" if broken else f"rgba({ACC},.6)"
        dash='stroke-dasharray="5 9"' if broken else ""
        edges+=f'<path d="M188 {y} C300 {y},300 {my},{mx-6} {my}" fill="none" stroke="{col}" stroke-width="3.2" {dash}/>'
        lbl="version clash" if broken else "glue.py"
        lc=f"rgb({RED})" if broken else "#8f8f85"
        edges+=f'<text x="272" y="{(y+my)//2-8}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="{lc}">{lbl}</text>'
        bd=f"rgba(200,70,35,.55)" if broken else "rgba(255,255,255,.14)"
        nodes+=(f'<rect x="70" y="{y-30}" width="118" height="60" rx="15" fill="#242019" stroke="{bd}" stroke-width="1.6"/>'
                f'<text x="129" y="{y-4}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">{nm}</text>'
                f'<text x="129" y="{y+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{sub}</text>')
    edges+=f'<path d="M{mx+120} {my} C620 {my},600 {ay},{ax-58} {ay}" fill="none" stroke="rgba({ACC},.6)" stroke-width="3.2"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Now wire them together","THE GLUE")}
      <svg width="820" height="464" viewBox="0 0 820 464" style="display:block;margin:0 auto">
        {edges}
        <rect x="{mx}" y="{my-52}" width="120" height="104" rx="18" fill="#2a2622" stroke="rgba(212,162,127,.4)" stroke-width="2"/>
        <text x="{mx+60}" y="{my-8}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="rgb({ACC})">langchain</text>
        <text x="{mx+60}" y="{my+14}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">the harness</text>
        <text x="{mx+60}" y="{my+34}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">you maintain</text>
        {nodes}
        <circle cx="{ax}" cy="{ay}" r="52" fill="#221f1b" stroke="rgba(255,255,255,.14)" stroke-width="1.6"/>
        <text x="{ax}" y="{ay-2}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">your</text>
        <text x="{ax}" y="{ay+18}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">app</text>
      </svg>
      {cap("seven repos, six integrations, every one of them yours to keep alive.")}</div>'''

# 4. DEPENDENCY ROT - a version tree with two branches severed in muted red
def rot():
    root=(410,58)
    mids=[("inference",150,178),("retrieval",410,178),("serving",670,178)]
    leaves={"inference":[("torch 2.4","x",70,320,True),("cuda 12.6","ok",236,320,False)],
            "retrieval":[("pydantic 2","x",340,320,True),("numpy 2.1","ok",478,320,False)],
            "serving":[("fastapi","ok",596,320,False),("uvicorn","ok",744,320,False)]}
    svg=""
    for nm,x,y in mids:
        svg+=f'<path d="M{root[0]} {root[1]+26} C{root[0]} 120,{x} 110,{x} {y-26}" fill="none" stroke="rgba({ACC},.4)" stroke-width="2.6"/>'
        svg+=(f'<rect x="{x-70}" y="{y-26}" width="140" height="52" rx="14" fill="#242019" stroke="rgba(255,255,255,.12)"/>'
              f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#d9d5cc">{nm}</text>')
        for lnm,st,lx,ly,broke in leaves[nm]:
            col=f"rgb({RED})" if broke else f"rgba({ACC},.42)"
            dash='stroke-dasharray="5 8"' if broke else ""
            svg+=f'<path d="M{x} {y+26} C{x} 264,{lx} 250,{lx} {ly-24}" fill="none" stroke="{col}" stroke-width="2.6" {dash}/>'
            bd=f"rgba(200,70,35,.55)" if broke else "rgba(255,255,255,.1)"
            tc="#7a746a" if broke else "#cfc9bd"
            svg+=(f'<rect x="{lx-64}" y="{ly-24}" width="128" height="48" rx="12" fill="#201d18" stroke="{bd}"/>'
                  f'<text x="{lx}" y="{ly-2}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="{tc}">{lnm}</text>')
            tag="breaking" if broke else "pinned"
            tgc=f"rgb({RED})" if broke else "#6f6a60"
            svg+=f'<text x="{lx}" y="{ly+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="{tgc}">{tag}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Monday it breaks again","DEPENDENCY ROT")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <circle cx="{root[0]}" cy="{root[1]}" r="30" fill="#2a2622" stroke="rgba(212,162,127,.4)" stroke-width="2"/>
        <text x="{root[0]}" y="{root[1]+5}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">stack</text>
        {svg}
      </svg>
      {cap("every repo ships on its own clock. you are the on-call for all of them.")}</div>'''

# 5. TRUE COST - IVORY ledger: the self-host invoice nobody shows, then Ultron in cents
def truecost():
    rows=[("GPU rent, one A100","$2,400 / mo"),("Vector DB hosting","$380 / mo"),
          ("DevOps + on-call","$3,000 / mo"),("Downtime + patches","your nights")]
    body=""
    for i,(k,v) in enumerate(rows):
        body+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:13px 0;'
               f'border-bottom:1px solid rgba(120,95,60,.16)">'
               f'<span style="font-family:DM Sans;font-size:19px;color:#3a2d1e">{k}</span>'
               f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#7a3d22">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The invoice nobody shows you","TRUE COST","#2a2016","#96562d")}
      <div style="background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.2);border-radius:18px;padding:6px 24px 8px">
        {body}
        <div style="display:flex;justify-content:space-between;align-items:baseline;padding:16px 0 10px">
          <span style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#7a3d22">SELF-HOST TOTAL</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#7a3d22">$5,780+ / mo</span></div>
      </div>
      <div style="margin-top:16px;display:flex;justify-content:space-between;align-items:center;
        background:linear-gradient(150deg,#96562d,#7a3d22);border-radius:16px;padding:16px 22px;box-shadow:0 14px 26px rgba(150,90,45,.28)">
        <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#fdf7ee">Ultron, same jobs done</span>
        <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#fdf7ee">cents per run</span></div>
      {cap("the repo is free. the GPUs, the ops and your nights are the price.","#8a745a")}</div>'''

# 6. THE OPERATOR - radial hub-and-spokes: the ROUTER already wired to seven agents
def operator():
    cx,cy=225,215; R=168
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba({ACC},.34)" stroke-width="2"/>'
                 f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(212,162,127,.32)" stroke-width="1.6"/>'
                 f'<text x="{x:.0f}" y="{y-1:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".04em" fill="#e6ddcf">{nm}</text>'
                 f'<text x="{x:.0f}" y="{y+14:.0f}" text-anchor="middle" font-family="DM Mono" font-size="9.5" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="450" height="450" viewBox="0 0 450 450">
        <defs><radialGradient id="hub6" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg6" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#hg6)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#hub6)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">picks the agent</text>
      </svg>
      <div style="flex:1">
        {htitle("Seven agents, pre-wired","THE OPERATOR")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.5">The stack you would spend a quarter cloning and gluing is running on login one, on Claude, with nothing to host.</div>
        {cap("research, outbound, deals, content, code, publishing, legal. already assembled.")}
      </div></div>'''

# 7. MODEL SHELF - a segmented selector, SMART lit; the router chooses the tier, you choose nothing
def modelshelf():
    segs=[("LITE","quick lookups","0.02c",False),("SMART","daily execution","0.11c",True),("DEEP","hard judgement","0.40c",False)]
    seg=""
    for i,(nm,role,cost,on) in enumerate(segs):
        bg="linear-gradient(160deg,#463d33,#2a241d)" if on else "#211e1a"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="box-shadow:0 0 30px rgba(212,162,127,.28), inset 0 2px 2px rgba(255,255,255,.1);" if on else ""
        nc="#FAFAF7" if on else "#9a9488"; costc="#FAFAF7" if on else "#8f8f85"
        pick=f'<div style="font-family:DM Mono;font-size:11px;color:rgb({ACC});margin-top:8px">&#9679; picked</div>' if on else '<div style="height:19px"></div>'
        seg+=(f'<div style="flex:1;background:{bg};border:1.6px solid {bd};border-radius:18px;padding:20px 18px;{glow}text-align:center">'
              f'<div style="font-family:DM Mono;font-size:14px;letter-spacing:.14em;color:{nc}">{nm}</div>'
              f'<div style="font-family:DM Sans;font-weight:900;font-size:30px;color:{costc};margin-top:8px">{cost}</div>'
              f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85;margin-top:2px">{role}</div>{pick}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("No model to choose","MODEL ROUTER")}
      <div style="display:flex;align-items:center;gap:10px;margin:10px 0 4px;justify-content:center">
        <div style="font-family:DM Mono;font-size:13px;color:#8f8f85">job in</div>
        <svg width="52" height="16"><path d="M2 8 H44 M38 3 L46 8 L38 13" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">router reads it</div>
      </div>
      <div style="display:flex;gap:16px;margin-top:16px">{seg}</div>
      <div style="margin-top:20px;text-align:center;font-family:DM Sans;font-weight:700;font-size:18px;color:#c9c3b8">You never pick ollama vs vllm vs a model. It picks the cheapest tier that can do the job.</div>
      {cap("one selector, priced in cents. no inference server to babysit.")}</div>'''

# 8. HUMAN GATE - IVORY: a wax-seal APPROVED over a receipt strip of shipped work, priced in cents
def gate():
    chips=[("draft 12 follow-ups","0.11c"),("score 340 accounts","0.24c"),("ship pricing page","0.09c")]
    strip=""
    for k,v in chips:
        strip+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:12px 0;border-bottom:1px dashed rgba(120,95,60,.3)">'
                f'<span style="font-family:DM Sans;font-size:18px;color:#3a2d1e">{k}</span>'
                f'<span style="font-family:DM Mono;font-size:15px;color:#7a3d22">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;align-items:center;gap:30px">
      <svg width="230" height="290" viewBox="0 0 230 290" style="flex-shrink:0">
        <defs><radialGradient id="wax" cx="38%" cy="32%"><stop offset="0%" stop-color="#c9754d"/><stop offset="60%" stop-color="#96562d"/><stop offset="100%" stop-color="#5f3218"/></radialGradient>
        <filter id="ws" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="rgba(95,50,24,.45)"/></filter></defs>
        <g filter="url(#ws)"><path d="M115 24 {"".join(f"L{115+96*math.cos(math.radians(a)):.0f} {150+96*math.sin(math.radians(a)):.0f} L{115+108*math.cos(math.radians(a+15)):.0f} {150+108*math.sin(math.radians(a+15)):.0f}" for a in range(-90,270,30))} Z" fill="url(#wax)"/></g>
        <circle cx="115" cy="150" r="76" fill="none" stroke="rgba(255,240,225,.32)" stroke-width="2.5"/>
        <text x="115" y="142" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#fdf1e6">YOUR</text>
        <text x="115" y="172" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".16em" fill="#fdf1e6">TAP</text>
        <text x="115" y="270" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#96562d">HUMAN GATE</text>
      </svg>
      <div style="flex:1">
        {htitle("You approve. It ships.","HUMAN GATE","#2a2016","#96562d")}
        <div style="background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.2);border-radius:16px;padding:6px 20px 8px">
          {strip}
          <div style="display:flex;justify-content:space-between;align-items:baseline;padding:14px 0 8px">
            <span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#7a3d22">RUN TOTAL</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:24px;color:#7a3d22">0.44c</span></div>
        </div>
        {cap("no cloning, no hosting, no pager. one login, cents per run.","#8a745a")}
      </div></div>'''

PANELS={"shoppinglist":shoppinglist(),"startrap":startrap(),"theglue":theglue(),"rot":rot(),
        "truecost":truecost(),"operator":operator(),"modelshelf":modelshelf(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src03"; os.makedirs(outd,exist_ok=True)
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
