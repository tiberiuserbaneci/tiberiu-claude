#!/usr/bin/env python3
# TIER 3 - MINT YOUR OWN SKILLS, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
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

# 1. ADMISSION - node graph: a tangled dim MEGA-AGENT cluster (crossed out) vs one clean lit SKILL token
def admission():
    cx,cy=195,220; sats=[]
    for a in range(0,360,51):
        x=cx+118*math.cos(math.radians(a)); y=cy+108*math.sin(math.radians(a)); sats.append((x,y))
    edges=""
    for i,(x,y) in enumerate(sats):
        edges+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(250,250,247,.13)" stroke-width="1.6"/>'
        nx,ny=sats[(i+2)%len(sats)]
        edges+=f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgba(250,250,247,.08)" stroke-width="1.4"/>'
    nodes=""
    for x,y in sats:
        nodes+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="17" fill="#26231f" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You built a mega-agent","WRONG UNIT")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="skl" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-90%" y="-90%" width="280%" height="280%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        <g opacity="0.85">{edges}{nodes}
          <circle cx="{cx}" cy="{cy}" r="44" fill="#332e28" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>
          <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#a29a8c">MEGA</text>
          <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#a29a8c">AGENT</text>
          <line x1="60" y1="86" x2="330" y2="354" stroke="rgba(200,70,35,.7)" stroke-width="5" stroke-linecap="round"/>
        </g>
        <text x="{cx}" y="392" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#8f6a52">bloated · brittle · one blob</text>
        <text x="450" y="226" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#4a453d">&#8250;</text>
        <g filter="url(#sg)"><circle cx="640" cy="220" r="92" fill="url(#skl)"/></g>
        <text x="640" y="214" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">SKILL</text>
        <text x="640" y="244" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".08em">the real unit</text>
      </svg>
      {cap("even Anthropic says it now: leverage is the skill, not the mega-agent.")}</div>'''

# 2. FOLDERS - IVORY file-tree: five folders + one SKILL.md, the whole anatomy of a skill
def folders():
    FOLD='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/></svg>'
    FILE='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c84623" stroke-width="2"><path d="M6 2h8l4 4v16H6Z"/><path d="M14 2v4h4"/><path d="M9 13h6M9 17h4"/></svg>'
    rows=[(0,FOLD,"proposal-skill/","the whole thing is one directory",False),
          (1,FILE,"SKILL.md","the instructions Claude reads",True),
          (1,FOLD,"references/","docs it pulls facts from",False),
          (1,FOLD,"scripts/","the deterministic steps",False),
          (1,FOLD,"assets/","logo, templates, boilerplate",False),
          (1,FOLD,"templates/","the exact output shapes",False)]
    body=""
    for indent,icon,name,sub,hot in rows:
        ml=indent*40
        namec="#96562d" if hot else "#2a2016"
        bg='background:rgba(200,70,35,.07);border:1px solid rgba(200,70,35,.28);' if hot else 'background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.12);'
        body+=(f'<div style="margin-left:{ml}px;display:flex;align-items:center;gap:16px;{bg}border-radius:14px;padding:13px 18px">'
          f'<span style="flex-shrink:0;display:flex">{icon}</span>'
          f'<span style="flex:1;font-family:\'DM Mono\';font-weight:500;font-size:19px;color:{namec};letter-spacing:.01em">{name}</span>'
          f'<span style="font-family:\'DM Sans\';font-size:15px;color:#8a745a">{sub}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Five folders. One file.</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">FULL ANATOMY</span></div>
      <div style="display:flex;flex-direction:column;gap:11px">{body}</div>
      {cap("no graphs, no framework, no PhD. this is the entire shape of a skill.","#8a745a")}</div>'''

# 3. ORE - isometric stack: repeated jobs are the raw material, one refined skill seam glows through
def ore():
    layers=[("the proposal you rewrite","x14 this quarter",0),
            ("the monthly stack audit","x9 so far",1),
            ("the pricing follow-up","x22 threads",2)]
    cards=""
    for label,n,i in layers:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#413a33,#2b2723);border:1.5px solid rgba(255,255,255,.13);border-radius:16px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:14px;height:52px;border-radius:5px;background:linear-gradient(180deg,#f0c49e,rgb({ACC}) 55%,#7a4326);box-shadow:0 0 16px rgba(212,162,127,.6)"></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#FAFAF7">{label}</div>'
          f'<div style="font-family:DM Mono;font-size:14px;color:#9a9488;margin-top:2px">{n}</div></div>'
          f'<div style="flex-shrink:0;font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">ORE</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Your workflow is the ore","RAW MATERIAL")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:130px;top:398px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">refine &#8594; 1 skill</div></div></div>
      {cap("the job you already repeat by hand is the seam worth mining.")}</div>'''

# 4. MINT - four-pass press: Discover / Scaffold / Distill / Audit stamp out one command coin
def mint():
    steps=[("DISCOVER","find the repeated job"),("SCAFFOLD","five folders, one file"),
           ("DISTILL","cut to the real steps"),("AUDIT","run it, watch it break")]
    W,H=820,430; x0=40; sw=150; gap=28; sy=70
    stations=""; conns=""
    for i,(nm,sub) in enumerate(steps):
        x=x0+i*(sw+gap)
        stations+=(f'<g><rect x="{x}" y="{sy}" width="{sw}" height="150" rx="20" fill="url(#stn)" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="{x+sw/2:.0f}" cy="{sy+42}" r="22" fill="none" stroke="rgb({ACC})" stroke-width="3"/>'
          f'<text x="{x+sw/2:.0f}" y="{sy+50}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="rgb({ACC})">{i+1}</text>'
          f'<text x="{x+sw/2:.0f}" y="{sy+96}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#e2dccf">{nm}</text>'
          f'<text x="{x+sw/2:.0f}" y="{sy+124}" text-anchor="middle" font-family="DM Sans" font-size="13" fill="#8f8f85">{sub}</text></g>')
        if i<3:
            cxm=x+sw+gap/2
            conns+=f'<path d="M{x+sw} {sy+75} h{gap}" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" filter="url(#tg)"/><path d="M{x+sw+gap-9:.0f} {sy+69} l9 6 l-9 6" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linejoin="round"/>'
    coy=320
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Four passes to a command","THE MINT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="stn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <radialGradient id="coin" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="tg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter>
        <filter id="cg" x="-90%" y="-90%" width="280%" height="280%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {conns}{stations}
        <line x1="410" y1="220" x2="410" y2="{coy-58}" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>
        <g filter="url(#cg)"><ellipse cx="410" cy="{coy}" rx="150" ry="60" fill="url(#coin)"/></g>
        <ellipse cx="410" cy="{coy}" rx="150" ry="60" fill="none" stroke="rgba(26,15,10,.25)" stroke-width="2"/>
        <text x="410" y="{coy+8}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="26" letter-spacing=".06em" fill="#1a0f0a">/proposal</text>
      </svg>
      {cap("four passes and the workflow becomes a command anyone on your desk can run.")}</div>'''

# 5. VOICE - IVORY compare: a downloaded skill writes generic, a minted one carries your rules
def voice():
    chips=["your rules","your no-list","your phrasing"]
    ch="".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in chips)
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Same job, two voices</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">YOURS, ENFORCED</span></div>
      <div style="background:rgba(120,95,60,.06);border:1px dashed rgba(120,95,60,.32);border-radius:16px;padding:18px 20px;margin-bottom:16px;opacity:.82">
        <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px"><span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#a08a68">DOWNLOADED</span><span style="font-family:DM Mono;font-size:12px;color:#c84623">writes like everyone</span></div>
        <div style="font-family:'DM Sans';font-size:19px;color:#7a6a54;line-height:1.4">"We are excited to leverage our synergies to unlock value for your business."</div></div>
      <div style="background:rgba(255,255,255,.62);border-left:4px solid #96562d;border-radius:14px;padding:20px 22px">
        <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px"><span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#96562d">MINTED FROM YOUR DESK</span><span style="font-family:DM Mono;font-size:12px;color:#96562d">unfair by design</span></div>
        <div style="font-family:'DM Sans';font-size:21px;color:#2a2016;line-height:1.4">"I killed nine tools last month. The one I kept did not have a chat box."</div>
        <div style="display:flex;gap:24px;margin-top:16px">{ch}</div></div>
      {cap("a minted skill carries your rules and your no-list on every single draft.","#8a745a")}</div>'''

# 6. SHELF - 2x3 grid: six skills minted from real repeated jobs on my own desk
def shelf():
    tiles=[("Proposal","from: rewritten x14","P"),("Audit","from: monthly stack review","A"),
           ("Brief","from: research recap","B"),("Pricing","from: quote threads","$"),
           ("Follow-up","from: nudge sequence","F"),("Report","from: weekly rollup","R")]
    cells=""
    for name,src,g in tiles:
        cells+=(f'<div style="background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.09);border-radius:18px;padding:20px 20px;box-shadow:0 16px 30px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07);display:flex;flex-direction:column;gap:12px">'
          f'<div style="display:flex;align-items:center;gap:13px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:linear-gradient(160deg,#4a423a,#2a2622);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:21px;color:rgb({ACC});border:1px solid rgba(255,255,255,.10)">{g}</div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7">{name}</div></div>'
          f'<div style="display:flex;align-items:center;justify-content:space-between">'
          f'<span style="font-family:DM Sans;font-size:14px;color:#8f8f85">{src}</span>'
          f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:rgb({ACC})">MINTED</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Six, from my own desk","THE SHELF")}
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">{cells}</div>
      {cap("each one born from a job I already repeated, now a command I never retype.")}</div>'''

# 7. COMPOUND - bar chart: each kept correction hardens the skill, month 3 runs sharper than month 1
def compound():
    W,H=760,400
    months=[("M1","first run",120,3),("M2","corrections kept",210,7),("M3","hardened",320,12)]
    bx=90; bw=150; gap=90; base=330
    bars=""; ticks=""
    for i,(m,sub,h,fixes) in enumerate(months):
        x=bx+i*(bw+gap)
        bars+=(f'<rect x="{x}" y="{base-h}" width="{bw}" height="{h}" rx="12" fill="url(#bar)"/>'
          f'<rect x="{x}" y="{base-h}" width="{bw}" height="14" rx="7" fill="rgba(255,255,255,.22)"/>'
          f'<text x="{x+bw/2:.0f}" y="{base+30}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">{m}</text>'
          f'<text x="{x+bw/2:.0f}" y="{base+52}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#8f8f85">{sub}</text>'
          f'<text x="{x+bw/2:.0f}" y="{base-h-16}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})">{fixes} fixes kept</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It only sharpens","COMPOUNDING")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4c2c"/></linearGradient></defs>
        <line x1="60" y1="{base}" x2="{W-30}" y2="{base}" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>
        {bars}
        <path d="M165 210 C300 130, 400 90, 555 34" fill="none" stroke="rgba(250,250,247,.28)" stroke-width="2.5" stroke-dasharray="3 8"/>
      </svg>
      {cap("fix it once, the skill remembers forever. every correction is banked.")}</div>'''

# 8. SHIFT - closing statement: a flat collected pile (dim) vs a compounding built stack (lit)
def shift():
    dim=""; lit=""
    for i in range(5):
        dim+=f'<rect x="0" y="{i*20}" width="150" height="14" rx="5" fill="rgba(250,250,247,.09)"/>'
    for i in range(6):
        w=52+i*20
        lit+=f'<rect x="0" y="{i*17}" width="{w}" height="14" rx="5" fill="url(#gl)" opacity="{0.5+i*0.09:.2f}"/>'
    return f'''<div style="width:820px;{CARD};padding:44px 46px 42px;text-align:center">
      <svg width="470" height="150" viewBox="0 0 470 150" style="display:block;margin:0 auto 30px">
        <defs><linearGradient id="gl" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8a4c2c"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        <g transform="translate(40,14)">{dim}<text x="75" y="140" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#7a746a">COLLECT</text></g>
        <text x="235" y="70" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#4a453d">&#8250;</text>
        <g transform="translate(268,4)">{lit}<text x="85" y="140" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">COMPOUND</text></g>
      </svg>
      <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#FAFAF7;line-height:1.14">The library you make beats<br>the library you save.</div>
      <div style="font-family:'DM Sans';font-size:19px;color:#c9a583;margin-top:14px">Stop downloading. Start minting.</div></div>'''

PANELS={"admission":admission(),"folders":folders(),"ore":ore(),"mint":mint(),
        "voice":voice(),"shelf":shelf(),"compound":compound(),"shift":shift()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/mintskills"; os.makedirs(outd,exist_ok=True)
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
