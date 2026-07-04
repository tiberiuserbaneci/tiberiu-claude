#!/usr/bin/env python3
# TIER 3 - BORING WINS, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded scene
# filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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

# 1. COMPOUND - dual-path line graph: clever spikes and crashes (red), boring climbs steady (accent)
def compound():
    W,H=820,430; x0,x1=44,780; base=372; top=54
    clever=[(44,300),(130,120),(210,66),(300,150),(392,244),(500,306),(610,340),(700,354),(780,360)]
    boring=[(44,346),(150,314),(268,272),(388,228),(508,186),(628,140),(720,104),(780,86)]
    grid="".join(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgba(250,250,247,.05)" stroke-width="1"/>' for y in range(top+40,base+1,72))
    cpts=" ".join(f"{x},{y}" for x,y in clever)
    bpts=" ".join(f"{x},{y}" for x,y in boring)
    barea=f"M{boring[0][0]} {base} L"+" L".join(f"{x} {y}" for x,y in boring)+f" L{boring[-1][0]} {base} Z"
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Clever spikes. Boring compounds.","30 DAYS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block">
        <defs>
          <linearGradient id="bfill" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.28)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
          <filter id="dg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
        </defs>
        <line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="rgba(250,250,247,.16)" stroke-width="1.5"/>
        {grid}
        <path d="{barea}" fill="url(#bfill)"/>
        <polyline points="{cpts}" fill="none" stroke="rgb(200,70,35)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" opacity="0.92"/>
        <polyline points="{bpts}" fill="none" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="{clever[-1][0]}" cy="{clever[-1][1]}" r="7" fill="rgb(200,70,35)"/>
        <text x="{clever[2][0]+8}" y="{clever[2][1]-14}" font-family="DM Mono" font-size="15" fill="rgb(200,70,35)">clever hack</text>
        <circle cx="{boring[-1][0]}" cy="{boring[-1][1]}" r="9" fill="rgb({ACC})" filter="url(#dg)"/>
        <text x="{boring[-1][0]-8}" y="{boring[-1][1]-20}" text-anchor="end" font-family="DM Mono" font-size="15" fill="rgb({ACC})">boring system</text>
      </svg>
      {cap("one viral trick, then silence. a boring system shows up every single day.")}</div>'''

# 2. BRAINRULE - IVORY: two choice cards, predictable (accent, picked) vs clever (red, X)
def brainrule():
    good=('<div style="flex:1;background:rgba(255,255,255,.55);border:1px solid rgba(150,90,45,.2);border-left:5px solid #96562d;border-radius:20px;padding:26px 24px 24px;text-align:center;position:relative">'
      '<div style="position:absolute;top:16px;right:18px;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#96562d">PICKED</div>'
      '<svg width="42" height="42" viewBox="0 0 24 24" style="margin-bottom:12px"><circle cx="12" cy="12" r="11" fill="rgba(150,90,45,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      '<div style="font-family:DM Sans;font-weight:900;font-size:28px;color:#96562d">Predictable</div>'
      '<div style="font-family:DM Sans;font-size:18px;color:#5a4634;margin-top:6px">Trusted in one read.</div></div>')
    bad=('<div style="flex:1;background:rgba(255,255,255,.4);border:1px solid rgba(200,70,35,.22);border-left:5px solid rgb(200,70,35);border-radius:20px;padding:26px 24px 24px;text-align:center;opacity:.9">'
      '<svg width="42" height="42" viewBox="0 0 24 24" style="margin-bottom:12px"><circle cx="12" cy="12" r="11" fill="rgba(200,70,35,.12)"/><path d="M8 8l8 8M16 8l-8 8" fill="none" stroke="rgb(200,70,35)" stroke-width="2.6" stroke-linecap="round"/></svg>'
      '<div style="font-family:DM Sans;font-weight:900;font-size:28px;color:rgb(200,70,35)">Clever</div>'
      '<div style="font-family:DM Sans;font-size:18px;color:#8a745a;margin-top:6px">Wait, what?</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">The buyer has one rule</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">SAFE = SIGNED</span></div>
      <div style="font-family:'DM Sans';font-size:20px;color:#5a4634;line-height:1.4;margin-bottom:22px">Predictable feels safe. Safe feels trustworthy. Trust gets the reply.</div>
      <div style="display:flex;gap:22px">{good}{bad}</div>
      <div style="text-align:center;font-family:'DM Sans';font-weight:800;font-size:20px;color:#2a2016;margin-top:22px">The brain picks the boring one every time.</div>
      {cap("clever gets a scroll. boring gets the meeting.","#8a745a")}</div>'''

# 3. ROUTER - one job routed down 3 tier lanes, SMART lane lit/picked (cents pricing)
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
      {htitle("The same right tier, every time","MODEL ROUTER")}
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
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">draft 12<br>follow-ups</div>
        {cards}
      </div>
      {cap("boring means no roulette - the cheapest tier that can do the job, in cents.")}</div>'''

# 4. CENTS - IVORY receipt/ledger: competitor stack struck out, Ultron per-job cents
def cents():
    rows=[("Draft 12 follow-ups","0.11c"),("Rank 800 accounts","0.30c"),("Research one company","0.04c"),("Watch the market, daily","0.06c")]
    lines=""
    for lbl,amt in rows:
        lines+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:11px 0;border-bottom:1px dashed rgba(150,120,80,.28)">'
          f'<span style="font-family:DM Sans;font-size:19px;color:#3a2f22">{lbl}</span>'
          f'<span style="font-family:DM Mono;font-weight:500;font-size:19px;color:#96562d">{amt}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Boring costs cents</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PER JOB</span></div>
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:20px">
        <span style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#8a745a;flex-shrink:0">REPLACES</span>
        <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.8)">a $1,200/mo clever stack</span></div>
      <div style="background:rgba(255,255,255,.5);border:1px solid rgba(150,120,80,.22);border-radius:20px;padding:8px 26px 14px;box-shadow:inset 0 2px 4px rgba(255,255,255,.7)">
        {lines}
        <div style="display:flex;justify-content:space-between;align-items:baseline;padding-top:16px">
          <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016">You pay</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#96562d">pennies</span></div>
      </div>
      {cap("pay per token, per job. no seat, no salary, no scary invoice.","#8a745a")}</div>'''

# 5. SYSTEM - isometric stack of 4 system layers vs a lone crossed-out prompt sticky
def system():
    layers=[("MEMORY","never forgets you",0),("AGENTS","seven specialists",1),("ROUTER","picks the tier",2),("GATE","waits for your tap",3)]
    slabs=""
    for nm,sub,i in layers:
        y=i*110
        slabs+=(f'<div style="position:absolute;left:0;top:{y}px;width:520px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:16px;padding:18px 24px;box-shadow:0 28px 40px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC})">{i+1}</div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{sub}</div></div></div>')
    sticky=('<div style="position:absolute;right:26px;top:40px;transform:rotate(7deg);width:200px;background:linear-gradient(160deg,#e9c063,#d8a63f);border-radius:6px;padding:20px 18px;box-shadow:0 22px 34px rgba(0,0,0,.5)">'
      '<div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#6a4a12">CLEVER PROMPT</div>'
      '<div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a1c05;margin-top:6px;line-height:1.25">"act as a world-class..."</div>'
      '<div style="margin-top:14px;font-family:DM Mono;font-size:12px;color:rgb(200,70,35);border-top:1px solid rgba(120,80,20,.3);padding-top:10px">forgets it all next chat</div>'
      '<svg style="position:absolute;inset:0" width="200" height="150" viewBox="0 0 200 150" preserveAspectRatio="none"><path d="M14 132 L186 20" stroke="rgba(200,70,35,.8)" stroke-width="4" stroke-linecap="round"/></svg></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Not a prompt. A system.","STACK &gt; TRICK")}
      <div style="position:relative;height:480px">
        {sticky}
        <div style="perspective:1900px;position:absolute;left:26px;top:24px">
          <div style="transform-style:preserve-3d;transform:rotateX(18deg) rotateZ(-9deg);width:520px;height:430px;position:relative">{slabs}</div></div>
      </div>
      {cap("a prompt is a trick you retype. a system runs the whole workflow, on its own.")}</div>'''

# 6. MEMORY - radial core with lifelines feeding every agent from one memory
def memory():
    cx,cy=210,215
    feeds=[("ICP",-90),("pipeline",-18),("pricing",54),("docs",126),("voice",198)]
    lines=""; nodes=""
    for nm,a in feeds:
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="32" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="424" height="424" viewBox="0 0 424 424">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="54" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">ONE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010" letter-spacing=".08em">CORE</text></svg>
      <div style="flex:1">
        {htitle("It never forgets you","SHARED CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing, docs, your voice - every agent draws from one memory. Tell it once, it holds forever.</div>
        {cap("boring is reliable because nothing ever forgets what you told it.")}</div></div>'''

# 7. GATE - full-capability orb held on a rein, one lock (HUMAN GATE)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing moves until you tap","HUMAN GATE")}
      <svg width="820" height="410" viewBox="0 0 820 410" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="205" r="128" fill="url(#orb)"/></g>
        <text x="200" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">FULL</text>
        <text x="200" y="234" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <path d="M332 205 H610" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="135" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,173)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="312" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("nothing sends and nothing spends until you approve it. powerful, never loose.")}</div>'''

# 8. ROSTER - ring of seven named agents around the router hub (hub-and-spokes)
def roster():
    cx,cy,R=306,262,196
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; chips=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        chips+=(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+17:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#9a9488">{role}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven boring specialists","ONE ROSTER")}
      <svg width="612" height="524" viewBox="0 0 612 524" style="display:block;margin:0 auto">
        <defs><radialGradient id="rh" cx="38%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#rh)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">ROUTER</text>
        <text x="{cx}" y="{cy+17}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">routes to one</text>
        {chips}
      </svg>
      {cap("no clever generalist. seven predictable agents, each owns exactly one job.")}</div>'''

PANELS={"compound":compound(),"brainrule":brainrule(),"router":router(),"cents":cents(),
        "system":system(),"memory":memory(),"gate":gate(),"roster":roster()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src07"; os.makedirs(outd,exist_ok=True)
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
