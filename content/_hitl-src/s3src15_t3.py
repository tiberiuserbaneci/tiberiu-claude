#!/usr/bin/env python3
# TIER 3 - THE VAULT THAT READS ITSELF (adapt of IG "Obsidian second brain"), on the WIRE-ITS-EYES
# bar: each of 8 panels a UNIQUE hand-built coded scene filling a clean rounded card, title + one-line
# caption, NO generic stat-chip strips. Reframe: a note app that only STORES is a graveyard; Ultron's
# vault is a shared memory every agent READS on the job. Overwrites models_clay/s3src15/*.png.
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

# 1. GRAVEYARD - dense packed field of dim note-tiles (folded corner), all dormant, one red 0% seal
def graveyard():
    cols,rows=12,7; tw,th=48,60; gx,gy=14,16
    W=cols*(tw+gx)-gx; H=rows*(th+gy)-gy
    tiles=""
    for r in range(rows):
        for c in range(cols):
            x=c*(tw+gx); y=r*(th+gy)
            shade=0.05+((r*7+c*3)%4)*0.012
            tiles+=(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="7" fill="rgba(250,250,247,{shade:.3f})" stroke="rgba(250,250,247,.05)"/>'
                f'<path d="M{x+tw-15} {y} h15 v15 Z" fill="rgba(250,250,247,.03)"/>'
                f'<line x1="{x+10}" y1="{y+22}" x2="{x+tw-10}" y2="{y+22}" stroke="rgba(250,250,247,.06)" stroke-width="2"/>'
                f'<line x1="{x+10}" y1="{y+34}" x2="{x+tw-16}" y2="{y+34}" stroke="rgba(250,250,247,.05)" stroke-width="2"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A vault nobody reads","0% REOPENED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:8px auto 0">
        <defs><filter id="dust" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="5"/></filter></defs>
        <ellipse cx="{W//2}" cy="{H-6}" rx="{W//2-30}" ry="18" fill="rgba(0,0,0,.35)" filter="url(#dust)"/>
        {tiles}</svg>
      {cap("2,700 notes saved, none reopened. a second brain that only stores is a graveyard.")}</div>'''

# 2. WEB - knowledge-graph constellation: notes linked into a web nobody ever walks (faint bezier net)
def web():
    nodes=[(120,90),(250,60),(390,110),(520,70),(650,130),(140,220),(300,200),(470,230),(620,250),
           (200,340),(360,320),(530,350),(680,330),(410,410)]
    edges=[(0,1),(1,2),(2,3),(3,4),(0,5),(1,6),(2,6),(3,7),(4,8),(5,6),(6,7),(7,8),
           (5,9),(6,10),(7,11),(8,12),(9,10),(10,11),(11,12),(10,13),(11,13),(6,2),(7,3)]
    lines=""
    for a,b in edges:
        x1,y1=nodes[a]; x2,y2=nodes[b]; mx=(x1+x2)/2; my=(y1+y2)/2-24
        lines+=f'<path d="M{x1} {y1} Q{mx:.0f} {my:.0f} {x2} {y2}" fill="none" stroke="rgba(212,162,127,.20)" stroke-width="1.6"/>'
    dots=""
    for i,(x,y) in enumerate(nodes):
        rr=8 if i in (6,7,10) else 6
        dots+=f'<circle cx="{x}" cy="{y}" r="{rr}" fill="rgba(230,220,205,.42)" stroke="rgba(212,162,127,.3)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Linked, never walked","THE WEB")}
      <svg width="800" height="460" viewBox="0 0 800 460" style="display:block;margin:0 auto">
        {lines}{dots}
        <g transform="translate(360,320)"><circle r="26" fill="rgba(200,70,35,.12)" stroke="rgba(200,70,35,.5)" stroke-width="1.5"/>
          <path d="M-9 0 h18 M0 -9 v18" stroke="rgba(200,70,35,.7)" stroke-width="2.4"/></g>
        <text x="360" y="392" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8f8f85">no path is ever traced</text>
      </svg>
      {cap("every note links to every other. pretty web, and nobody ever walks it.")}</div>'''

# 3. THIRTY - split/compare: BOLT ON 30 loose plugin chips (red, messy) vs COMES WIRED (one unit)
def thirty():
    plug=["daily notes","kanban","calendar","tasks","dataview","templater","excalidraw","git sync",
          "readwise","canvas","tag wrangler","outliner","sliding panes","spaced rep"]
    chips=""
    for i,p in enumerate(plug):
        r,c=divmod(i,2); x=c*168; y=r*44
        chips+=(f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({(-4 if i%2 else 5)}deg);'
            f'background:#2a2724;border:1px solid rgba(200,70,35,.28);border-radius:9px;padding:6px 11px;'
            f'font-family:DM Mono;font-size:12px;color:#9a9488;white-space:nowrap">{p}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("30 plug-ins, or 0","ASSEMBLED")}
      <div style="display:flex;align-items:stretch;gap:26px;height:430px">
        <div style="flex:1;background:rgba(200,70,35,.05);border:1px dashed rgba(200,70,35,.3);border-radius:20px;padding:22px 24px;position:relative">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#c84623">BOLT ON</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7;margin:2px 0 18px">30 plug-ins</div>
          <div style="position:relative;height:300px">{chips}</div>
        </div>
        <div style="display:flex;align-items:center;font-family:DM Sans;font-weight:900;font-size:22px;color:#6f6a60">vs</div>
        <div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:20px;padding:22px 24px;display:flex;flex-direction:column;box-shadow:inset 0 0 40px rgba(212,162,127,.12)">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC})">COMES WIRED</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7;margin:2px 0 20px">1 system</div>
          <div style="flex:1;display:flex;align-items:center;justify-content:center">
            <svg width="220" height="220" viewBox="0 0 220 220">
              <defs><radialGradient id="u3" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
              <filter id="ug3" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
              <g filter="url(#ug3)"><circle cx="110" cy="100" r="80" fill="url(#u3)"/></g>
              <text x="110" y="94" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ULTRON</text>
              <text x="110" y="118" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">vault built in</text>
            </svg>
          </div>
        </div>
      </div>
      {cap("you do not assemble a brain from 30 add-ons. the vault ships wired.")}</div>'''

# 4. SHAREDCORE - radial hub: one vault core, 7 agents read it on lifelines (none severed)
def sharedcore():
    cx,cy=210,215; R=168
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    lines=""; nodes=""
    for i,nm in enumerate(agents):
        a=-90+i*(360/7); x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.6"/>'
            f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" letter-spacing=".04em" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="430" height="430" viewBox="0 0 430 430">
        <defs><radialGradient id="core4" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg4" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}
        <g filter="url(#cg4)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#core4)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">VAULT</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one memory</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("One core, seven readers","SHARED MEMORY")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing, docs and every closed deal live in one core. Cortex, Specter, Striker and the rest all read the same memory.</div>
        {cap("no agent works from a blank page. they all pull from your vault.")}</div></div>'''

# 5. READJOB - left-to-right lane: a job passes through the VAULT which injects 3 context chips into it
def readjob():
    ctx=[("ICP","seed IT founders, US/UK"),("PRICING","cents per token"),("WON","Initech, closed Mar")]
    chips=""
    for i,(k,v) in enumerate(ctx):
        y=96+i*92
        chips+=(f'<g><rect x="298" y="{y-30}" width="230" height="60" rx="13" fill="#211e1a" stroke="rgba(212,162,127,.32)"/>'
            f'<rect x="298" y="{y-30}" width="8" height="60" rx="4" fill="rgb({ACC})"/>'
            f'<text x="322" y="{y-6}" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="rgb({ACC})">{k}</text>'
            f'<text x="322" y="{y+16}" font-family="DM Sans" font-size="15" fill="#d9d5cc">{v}</text>'
            f'<path d="M414 {y+30} V{y+60 if i<2 else y+58}" stroke="rgba(212,162,127,.4)" stroke-width="2" stroke-dasharray="3 5"/></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Read before it acts","AUTO-CONTEXT")}
      <svg width="810" height="440" viewBox="0 0 810 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="v5" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="vg5" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="24" y="196" width="150" height="72" rx="15" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
        <text x="99" y="228" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#9a9488">JOB</text>
        <text x="99" y="250" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#FAFAF7">outbound</text>
        <path d="M174 232 H236" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>
        <g filter="url(#vg5)"><circle cx="300" cy="232" r="58" fill="url(#v5)"/></g>
        <text x="300" y="228" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">VAULT</text>
        <text x="300" y="248" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">loads context</text>
        {chips}
        <path d="M528 232 H600" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>
        <rect x="600" y="176" width="186" height="112" rx="16" fill="#211e1a" stroke="rgba(212,162,127,.34)"/>
        <text x="693" y="206" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">SPECTER</text>
        <line x1="622" y1="230" x2="764" y2="230" stroke="rgba(250,250,247,.22)" stroke-width="2"/>
        <line x1="622" y1="248" x2="764" y2="248" stroke="rgba(250,250,247,.16)" stroke-width="2"/>
        <line x1="622" y1="266" x2="730" y2="266" stroke="rgba(250,250,247,.16)" stroke-width="2"/>
      </svg>
      {cap("every job pulls your icp, pricing and past wins before a word is written.")}</div>'''

# 6. VAULT - IVORY isometric stack of labeled memory cards (what the vault actually holds)
def vault():
    rows=[("ICP","seed IT founders, US/UK","live"),
          ("PIPELINE","18 deals, staged","live"),
          ("PRICING","cents per token","set"),
          ("DOCS","product + techniques","synced"),
          ("WINS","41 closed, tagged","kept")]
    cards=""
    for i,(k,v,tag) in enumerate(rows):
        y=i*94
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;background:linear-gradient(160deg,#fffdf8,#efe6d4);'
            f'border:1px solid rgba(120,95,60,.2);border-radius:16px;padding:16px 22px;box-shadow:0 22px 34px rgba(120,95,60,.20), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:20px">'
            f'<div style="flex-shrink:0;width:74px;font-family:DM Mono;font-size:13px;letter-spacing:.08em;color:#96562d">{k}</div>'
            f'<div style="flex:1;font-family:DM Sans;font-weight:700;font-size:20px;color:#2a2016">{v}</div>'
            f'<div style="flex-shrink:0;font-family:DM Mono;font-size:12px;color:#8a745a;background:rgba(150,90,45,.1);padding:4px 12px;border-radius:999px">{tag}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 40px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">What the vault holds</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">WORKING MEMORY</span></div>
      <div style="perspective:2000px;height:530px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:600px;height:470px;position:relative">{cards}</div></div>
      {cap("not a pile of notes. icp, pipeline, pricing, docs and wins, kept current.","#8a745a")}</div>'''

# 7. TAX - gauge/dial: the re-brief time per task, needle swung from a red 20-min zone down to 0
def tax():
    cx,cy,R=290,250,200
    def P(theta,rad): return cx+rad*math.cos(math.radians(theta)), cy-rad*math.sin(math.radians(theta))
    ticks=""
    for t in range(0,181,30):
        x1,y1=P(t,R); x2,y2=P(t,R-22)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(250,250,247,.26)" stroke-width="3"/>'
    lx,ly=P(180,R); mx,my=P(120,R); rx,ry=P(0,R)   # left=20min(red 180..120), right=0min(accent)
    nx,ny=P(10,R-42)                                # needle -> near 0 (right)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="580" height="320" viewBox="0 0 580 320">
        <defs><filter id="ng7" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        <path d="M{lx:.0f} {ly:.0f} A{R} {R} 0 0 1 {mx:.0f} {my:.0f}" fill="none" stroke="rgba(200,70,35,.6)" stroke-width="16" stroke-linecap="round"/>
        <path d="M{mx:.0f} {my:.0f} A{R} {R} 0 0 1 {rx:.0f} {ry:.0f}" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="16" stroke-linecap="round"/>
        {ticks}
        <text x="{lx:.0f}" y="{ly+30:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c84623">20 min</text>
        <text x="{rx:.0f}" y="{ry+30:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">0 min</text>
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" filter="url(#ng7)"/>
        <circle cx="{cx}" cy="{cy}" r="14" fill="rgb({ACC})"/>
        <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="60" fill="#FAFAF7">0</text>
        <text x="{cx}" y="{cy-28}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#9a9488">min re-briefing</text>
      </svg>
      <div style="flex:1">
        {htitle("The re-brief tax, gone","CONTEXT TAX")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Most tools start from zero on every task, so you paste your business back in each time. The vault already knows it.</div>
        {cap("no re-pasting your icp and pricing into a blank box, ever again.")}</div></div>'''

# 8. YOURS - a warm vault door (combination dial around the Ultron orb) held by the operator's key
def yours():
    cx,cy=250,220
    dial="".join(f'<line x1="{cx+118*math.cos(math.radians(a)):.0f}" y1="{cy+118*math.sin(math.radians(a)):.0f}" x2="{cx+134*math.cos(math.radians(a)):.0f}" y2="{cy+134*math.sin(math.radians(a)):.0f}" stroke="rgba(212,162,127,.5)" stroke-width="{4 if a%30==0 else 2}"/>' for a in range(0,360,10))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("One vault. Your key.","YOURS")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb8" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og8" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="70" y="40" width="360" height="360" rx="40" fill="#201d19" stroke="rgba(255,255,255,.08)"/>
        <rect x="94" y="64" width="312" height="312" rx="30" fill="none" stroke="rgba(212,162,127,.16)"/>
        {dial}
        <circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="rgba(212,162,127,.22)" stroke-width="2"/>
        <g filter="url(#og8)"><circle cx="{cx}" cy="{cy}" r="86" fill="url(#orb8)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ULTRON</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">your vault</text>
        <path d="M436 220 H560" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <g transform="translate(586,150)">
          <circle cx="46" cy="46" r="42" fill="#211e1a" stroke="rgb({ACC})" stroke-width="2.5"/>
          <circle cx="46" cy="46" r="16" fill="none" stroke="rgb({ACC})" stroke-width="6"/>
          <rect x="42" y="58" width="8" height="60" fill="rgb({ACC})"/>
          <rect x="42" y="96" width="26" height="8" fill="rgb({ACC})"/>
          <rect x="42" y="112" width="20" height="8" fill="rgb({ACC})"/>
          <text x="46" y="150" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">one login</text>
        </g>
      </svg>
      {cap("your data, one login, gated by you. every draw waits for your tap.")}</div>'''

PANELS={"graveyard":graveyard(),"web":web(),"thirty":thirty(),"sharedcore":sharedcore(),
        "readjob":readjob(),"vault":vault(),"tax":tax(),"yours":yours()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src15"; os.makedirs(outd,exist_ok=True)
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
