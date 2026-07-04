#!/usr/bin/env python3
# TIER 3 - THE POWER USER SETUP, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# 8 distinct scenes: gauge / radial-hub / timeline / node-graph / iso-stack / dot-field / hero-lock / bars.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
BAD="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagcol=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagcol}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. STOCK - GAUGE: a capability dial pinned to "answers only", the operate zone dark and unused
def stock():
    cx,cy,R=306,258,210
    # ticks across the top semicircle (180deg left -> 0deg right)
    ticks=""
    for i in range(11):
        a=math.radians(180-i*18)
        x1=cx+R*math.cos(a); y1=cy-R*math.sin(a)
        x2=cx+(R-18)*math.cos(a); y2=cy-(R-18)*math.sin(a)
        maj=(i%5==0)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(250,250,247,{.32 if maj else .14})" stroke-width="{3 if maj else 1.6}"/>'
    # lit arc only over the ASK zone (first ~22%)
    a0=math.radians(180); a1=math.radians(180-0.22*180)
    lx0,ly0=cx+R*math.cos(a0),cy-R*math.sin(a0); lx1,ly1=cx+R*math.cos(a1),cy-R*math.sin(a1)
    na=math.radians(180-0.18*180)  # needle at ~18%
    nx=cx+(R-30)*math.cos(na); ny=cy-(R-30)*math.sin(na)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Out of the box, it only answers","STOCK MODE")}
      <svg width="612" height="430" viewBox="0 0 612 430" style="display:block;margin:0 auto">
        <defs><filter id="ng" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.85"/></filter></defs>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(250,250,247,.10)" stroke-width="18" stroke-linecap="round"/>
        <path d="M{lx0:.0f} {ly0:.0f} A{R} {R} 0 0 1 {lx1:.0f} {ly1:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="18" stroke-linecap="round"/>
        {ticks}
        <text x="{cx-R+4:.0f}" y="{cy+34}" text-anchor="start" font-family="DM Mono" font-size="15" letter-spacing=".1em" fill="rgb({ACC})">ASKS</text>
        <text x="{cx}" y="{cy-R-14}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".1em" fill="#6f6a60">DRAFTS</text>
        <text x="{cx+R-4:.0f}" y="{cy+34}" text-anchor="end" font-family="DM Mono" font-size="15" letter-spacing=".1em" fill="#6f6a60">OPERATES</text>
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="15" fill="#1a1816" stroke="rgb({ACC})" stroke-width="3"/>
        <text x="{cx}" y="{cy+96}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#FAFAF7">ANSWERS ONLY</text>
        <text x="{cx}" y="{cy+126}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".12em" fill="rgb({ACC})">the needle never moves</text>
      </svg>
      {cap("stock settings are training wheels. installed right, it operates.")}</div>'''

# 2. PLUGINS - RADIAL HUB: one INSTALL core, four desk plugins on spokes
def plugins():
    cx,cy=306,235; Rr=176
    desks=[("RESEARCH","CORTEX",-90),("CONTENT","PULSE",0),("DEALS","STRIKER",90),("CODE","SENTINEL",180)]
    spokes=""; nodes=""
    for title,agent,a in desks:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="3"/>'
        nodes+=(f'<g><rect x="{x-92:.0f}" y="{y-40:.0f}" width="184" height="80" rx="16" fill="url(#dk)" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{x:.0f}" y="{y-6:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="21" fill="#FAFAF7">{title}</text>'
          f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">{agent}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("A whole team in one install","4 DESKS")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><linearGradient id="dk" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#221f1b"/></linearGradient>
        <radialGradient id="core" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-90%" y="-90%" width="280%" height="280%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">INSTALL</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one command</text>
        {nodes}
      </svg>
      {cap("each plugin is a desk. research, content, deals, code, installed once.")}</div>'''

# 3. SKILLS - TIMELINE (ivory): one slash command expands into the whole play
def skills():
    steps=[("DRAFT","the angle"),("DESIGN","the poster"),("SCHEDULE","the slot"),("POST","+ first comment")]
    n=len(steps); x0=70; x1=760; span=x1-x0; gap=span/(n-1); y=250
    line=f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgba(150,90,45,.35)" stroke-width="3"/>'
    dots=""
    for i,(s,sub) in enumerate(steps):
        x=x0+i*gap
        dots+=(f'<circle cx="{x:.0f}" cy="{y}" r="15" fill="#96562d"/><circle cx="{x:.0f}" cy="{y}" r="15" fill="none" stroke="rgba(255,255,255,.7)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-40}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#2a2016">{s}</text>'
          f'<text x="{x:.0f}" y="{y+44}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8a745a">{sub}</text>'
          f'<text x="{x:.0f}" y="{y+7}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#fdfbf6">{i+1}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {htitle("One line runs the whole play","SLASH COMMAND",ink="#2a2016",tagcol="#96562d")}
      <div style="display:flex;align-items:center;gap:16px;margin:6px auto 26px;width:max-content">
        <div style="font-family:'DM Mono';font-weight:500;font-size:30px;color:#fdfbf6;background:linear-gradient(160deg,#a8642f,#7a4326);border:1px solid rgba(255,255,255,.2);border-radius:14px;padding:14px 26px;box-shadow:0 14px 28px rgba(120,70,30,.4)">/launch-week</div>
        <svg width="46" height="30" viewBox="0 0 46 30" fill="none" stroke="#96562d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15h34M30 6l10 9-10 9"/></svg>
        <span style="font-family:'DM Sans';font-weight:700;font-size:17px;color:#5a4634">replaces a page of prompting</span>
      </div>
      <svg width="830" height="330" viewBox="0 0 830 330" style="display:block;margin:0 auto">{line}{dots}</svg>
      {cap("a slash command replaces a page of prompting. repeatable, every time.","#8a745a")}</div>'''

# 4. CONNECTORS - NODE GRAPH: agent core wired by bezier into four real apps, each acknowledged
def connectors():
    W,H=820,470; hubx,huby=180,235
    apps=[("Mail","inbox + sends",70),("Docs","specs + notes",190),("CRM","pipeline",300),("Payments","invoices",410)]
    edges=""; nodes=""; nx=560
    for nm,sub,y in apps:
        mx=(hubx+nx)/2
        edges+=f'<path d="M{hubx+70} {huby} C{mx:.0f} {huby},{mx:.0f} {y},{nx-8} {y}" stroke="rgba(212,162,127,.5)" stroke-width="2.6" fill="none"/>'
        nodes+=(f'<rect x="{nx}" y="{y-38}" width="230" height="76" rx="16" fill="url(#ap)" stroke="rgba(255,255,255,.11)"/>'
          f'<text x="{nx+22}" y="{y-4}" font-family="DM Sans" font-weight="800" font-size="21" fill="#FAFAF7">{nm}</text>'
          f'<text x="{nx+22}" y="{y+20}" font-family="DM Sans" font-size="14" fill="#8f8f85">{sub}</text>'
          f'<circle cx="{nx+206}" cy="{y}" r="8" fill="#7fd39a" filter="url(#ld)"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("It acts inside your real apps","WIRED IN")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="ap" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-90%" y="-90%" width="280%" height="280%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter>
        <filter id="ld" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#7fd39a" flood-opacity="0.9"/></filter></defs>
        {edges}
        <g filter="url(#hg)"><circle cx="{hubx}" cy="{huby}" r="70" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">AGENT</text>
        <text x="{hubx}" y="{huby+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">acts, not asks</text>
        {nodes}
      </svg>
      {cap("mail, docs, crm, payments. no copy-paste bridge, no tab zoo.")}</div>'''

# 5. THREE - ISO STACK: the starter trio installed tonight, each with a green check
def three():
    trio=[("MARKETING","content + campaigns"),("DESIGN","brand + posters"),("DOCS","specs + guides")]
    cards=""
    for i,(nm,sub) in enumerate(trio):
        y=i*140
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;padding:22px 26px;box-shadow:0 32px 46px rgba(0,0,0,.58), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:22px">'
          f'<div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:24px;color:rgb({ACC})">{i+1}</div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:25px;color:#FAFAF7">{nm}</div><div style="font-family:DM Sans;font-size:16px;color:#a8a296;margin-top:1px">{sub}</div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center;gap:8px;background:rgba(127,211,154,.12);border:1px solid rgba(127,211,154,.4);border-radius:12px;padding:8px 14px">'
          f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#7fd39a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#7fd39a">INSTALLED</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 30px">
      {htitle("Install three tonight","STARTER TRIO")}
      <div style="perspective:2000px;height:460px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:580px;height:420px;position:relative">{cards}</div></div>
      {cap("marketing, design, docs: the trio that covers the loudest jobs first.")}</div>'''

# 6. PREINSTALLED - DOT FIELD: 71 skills lit, and the 7 agents already wired beside them
def preinstalled():
    cols,rows=13,6  # 78 cells, 71 lit
    cell=26; gap=8; lit=71
    dots=""
    for i in range(cols*rows):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i<lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="7" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="7" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rows*(cell+gap)-gap
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    arows="".join(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:9px"><span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 10px rgba({ACC},.7)"></span><span style="font-family:DM Mono;font-size:14px;letter-spacing:.06em;color:#d9d5cc">{a}</span></div>' for a in agents)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("It comes installed","DAY ONE = DAY 100")}
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0">
          <div style="display:flex;align-items:baseline;gap:10px;margin-bottom:14px"><span style="font-family:DM Sans;font-weight:900;font-size:52px;color:#FAFAF7">71</span><span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#c9a583">skills, ready</span></div>
          <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
            <defs><filter id="lg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
            {dots}</svg></div>
        <div style="flex:1;border-left:1px solid rgba(255,255,255,.1);padding-left:30px">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:14px">7 AGENTS WIRED</div>
          {arows}
        </div>
      </div>
      {cap("71 skills, 7 agents, connectors wired. day one behaves like day one hundred.")}</div>'''

# 7. GATE - HERO LOCK: full capability held on reins, one tap before anything external
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 32px">
      {htitle("The brake comes installed too","POWER, HELD")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="205" cy="210" r="132" fill="url(#orb)"/></g>
        <text x="205" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">FULL</text>
        <text x="205" y="238" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <path d="M340 210 H600" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 13" stroke-linecap="round"/>
        <rect x="612" y="138" width="150" height="150" rx="32" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(658,178)"><rect x="0" y="36" width="58" height="44" rx="10" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M11 36 V22 a18 18 0 0 1 36 0 v14" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="687" y="326" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("everything external waits for your tap. power without accidents.")}</div>'''

# 8. COMPOUND - BARS (ivory): corrections stack into rules, the setup pays rent every month
def compound():
    months=[("M1",3),("M2",8),("M3",14),("M4",21),("M5",29),("M6",38)]
    x0=70; bw=78; gp=42; base=340; maxv=38; hmax=250
    bars=""
    for i,(m,v) in enumerate(months):
        x=x0+i*(bw+gp); h=hmax*v/maxv; y=base-h
        bars+=(f'<rect x="{x}" y="{y:.0f}" width="{bw}" height="{h:.0f}" rx="10" fill="url(#bar)"/>'
          f'<text x="{x+bw/2:.0f}" y="{y-12:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a2016">{v}</text>'
          f'<text x="{x+bw/2:.0f}" y="{base+28}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#8a745a">{m}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {htitle("Set once. Collect monthly","RULES COMPOUND",ink="#2a2016",tagcol="#96562d")}
      <svg width="800" height="400" viewBox="0 0 800 400" style="display:block;margin:0 auto">
        <defs><linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#a8642f"/><stop offset="100%" stop-color="#7a4326"/></linearGradient></defs>
        <line x1="{x0-14}" y1="{base}" x2="746" y2="{base}" stroke="rgba(150,90,45,.4)" stroke-width="2"/>
        {bars}
        <text x="{x0-14}" y="60" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#96562d">RULES LEARNED, RUNNING TOTAL</text>
      </svg>
      {cap("corrections become rules. the setup pays rent every month after.","#8a745a")}</div>'''

PANELS={"stock":stock(),"plugins":plugins(),"skills":skills(),"connectors":connectors(),
        "three":three(),"preinstalled":preinstalled(),"gate":gate(),"compound":compound()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/installs24"; os.makedirs(outd,exist_ok=True)
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
