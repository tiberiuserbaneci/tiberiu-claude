#!/usr/bin/env python3
# TIER 3 - THE HOUSE RECIPE (s3src10). Adapts the NotebookLM -> Claude "Skills Factory" carousel into
# the Ultron eyes-bar standard: 8 UNIQUE hand-built coded scenes on clean rounded CARD/CARDIV cards,
# htitle + one cap each, warm palette only. Narrow reframe: distill your best sources ONCE into a
# grounded recipe every agent reuses forever (NOT the prompts-dont-remember angle).
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SOURCES - IVORY: an intake tray holding four fanned source sheets (pdf, article, transcript, doc)
def sources():
    sheets=[("PDF","product deck",-7,0,26),("ARTICLE","best posts",-2,150,14),
            ("TRANSCRIPT","sales calls",3,300,2),("DOC","the real playbook",8,450,-10)]
    body=""
    for tag,name,rot,dx,dy in sheets:
        body+=(f'<div style="position:absolute;left:{dx}px;top:{100+dy}px;transform:rotate({rot}deg);'
          f'width:250px;height:300px;background:linear-gradient(160deg,#ffffff,#f2ead9);border:1px solid rgba(120,95,60,.22);'
          f'border-radius:14px;box-shadow:0 22px 40px rgba(120,95,60,.24), inset 0 2px 2px rgba(255,255,255,.9);padding:20px 22px">'
          f'<div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.18em;color:#96562d">{tag}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#2a2016;margin-top:8px;line-height:1.15">{name}</div>'
          + "".join(f'<div style="height:7px;border-radius:4px;background:rgba(120,95,60,.16);margin-top:{10 if i==0 else 9}px;width:{[86,74,90,60][i]}%"></div>' for i in range(4))
          + '</div>')
    # gathering bracket + label on the right
    bracket=('<svg width="70" height="360" viewBox="0 0 70 360" style="position:absolute;right:16px;top:70px">'
      f'<path d="M8 8 C46 8,46 172,62 180 C46 188,46 352,8 352" fill="none" stroke="#96562d" stroke-width="4" stroke-linecap="round"/></svg>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("Feed it your best sources","INTAKE","#2a2016")}
      <div style="position:relative;height:470px">{body}{bracket}
        <div style="position:absolute;right:2px;top:224px;font-family:\'DM Mono\';font-size:13px;letter-spacing:.06em;color:#96562d;transform:rotate(0deg)">curated</div></div>
      {cap("pdfs, articles, call transcripts, your real playbooks - the good stuff, in one place.","#8a745a")}</div>'''

# 2. DISTILL - DARK: five source nodes converge through bezier edges into one glowing recipe file
def distill():
    W,H=820,460
    src=[("product deck",70),("pricing doc",165),("sales calls",260),("best posts",355),("brand voice",430)]
    hubx,huby=650,240
    edges=""; nodes=""
    for nm,y in src:
        mx=(200+hubx)/2
        edges+=f'<path d="M198 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-64} {huby}" stroke="rgba(212,162,127,.5)" stroke-width="2.4" fill="none"/>'
        nodes+=(f'<rect x="40" y="{y-24}" width="158" height="48" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="119" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14.5" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Distilled into one recipe","5 SOURCES 1 FILE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#gh)"><rect x="{hubx-92}" y="{huby-108}" width="184" height="216" rx="20" fill="url(#hub)"/></g>
        <rect x="{hubx-70}" y="{huby-78}" width="140" height="8" rx="4" fill="rgba(26,15,10,.5)"/>
        {"".join(f'<rect x="{hubx-70}" y="{huby-52+i*22}" width="{[126,140,108,132][i]}" height="7" rx="3.5" fill="rgba(26,15,10,.35)"/>' for i in range(4))}
        <text x="{hubx}" y="{huby+92}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">skill.md</text>
      </svg>
      {cap("hours of scattered sources become one page an agent can actually follow.")}</div>'''

# 3. GROUNDED - DARK: a recipe document where every step carries a source receipt (one guessed line
#    struck out in muted red). No green - the checks are warm accent.
def grounded():
    steps=[("Open with their funding trigger","techcrunch.com"),
           ("Reference their exact tech stack","builtwith.com"),
           ("Match our pricing to their size","internal doc"),
           ("Close on their hiring signal","linkedin.com")]
    rows=""
    for txt,srcn in steps:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(255,255,255,.10);border-radius:15px;padding:15px 18px;box-shadow:0 12px 22px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.16)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:600;font-size:18px;color:#eae4d8">{txt}</span>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:12px;color:rgb({ACC});background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.28);border-radius:999px;padding:5px 12px">{srcn}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every step cites a source","GROUNDED")}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);border-radius:14px;padding:12px 18px;margin-bottom:16px;opacity:.72">
        <span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:#7a7468;flex-shrink:0">GUESSED</span>
        <span style="font-family:\'DM Sans\';font-size:17px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba({RED},.75)">"they seem like they would buy"</span>
        <span style="margin-left:auto;font-family:\'DM Mono\';font-size:12px;color:rgb({RED});flex-shrink:0">no source</span></div>
      <div style="display:flex;flex-direction:column;gap:12px">{rows}</div>
      {cap("written only from what you fed it - no invented steps, no drift over time.")}</div>'''

# 4. SHELF - DARK: an isometric rack of labeled job-recipe cards (one skill per job type)
def shelf():
    jobs=[("COLD EMAIL","SPECTER"),("PROPOSAL","STRIKER"),("LANDING PAGE","SENTINEL"),
          ("FAQ REPLY","PULSE"),("CONTRACT CLAUSE","COUNSEL")]
    cards=""
    for i,(name,agent) in enumerate(jobs):
        y=i*96
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;background:linear-gradient(160deg,#403a35,#2b2723);'
          f'border:1.5px solid rgba(255,255,255,.14);border-radius:16px;padding:16px 22px;'
          f'box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:11px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">'
          f'<svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 3h9l4 4v14a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z" fill="none" stroke="rgb({ACC})" stroke-width="1.8"/><path d="M14 3v5h5" fill="none" stroke="rgb({ACC})" stroke-width="1.8"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:22px;color:#FAFAF7">{name}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:13px;color:#a8a296;margin-top:1px">grounded recipe</div></div>'
          f'<div style="flex-shrink:0;font-family:\'DM Mono\';font-size:13px;letter-spacing:.08em;color:rgb({ACC});background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.26);border-radius:999px;padding:6px 13px">{agent}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("One recipe per job","THE SHELF")}
      <div style="perspective:2000px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:600px;height:460px;position:relative">{cards}</div></div>
      {cap("cold email, proposal, faq, contract - a shelf of recipes, not one giant prompt.")}</div>'''

# 5. ROSTER - DARK: radial hub, one recipe at the centre, seven agents reading it on spokes
def roster():
    cx,cy,R=306,232,178
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    spokes=""; nodes=""
    for i,nm in enumerate(agents):
        a=-90+i*(360/len(agents))
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.8"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".02em" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The whole roster cooks from it","7 AGENTS")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="rc" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#rg)"><rect x="{cx-58}" y="{cy-64}" width="116" height="128" rx="16" fill="url(#rc)"/></g>
        <rect x="{cx-40}" y="{cy-40}" width="80" height="7" rx="3.5" fill="rgba(26,15,10,.5)"/>
        {"".join(f'<rect x="{cx-40}" y="{cy-22+i*16}" width="{[72,80,60][i]}" height="6" rx="3" fill="rgba(26,15,10,.35)"/>' for i in range(3))}
        <text x="{cx}" y="{cy+56}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">skill.md</text>
      </svg>
      {cap("one recipe, seven agents - the same standard whoever runs the job.")}</div>'''

# 6. CONSISTENT - DARK: small-multiples grid of eight run tickets, all producing an identical output
def consistent():
    cells=""
    for i in range(8):
        r,c=divmod(i,4)
        cells+=(f'<div style="background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);'
          f'border-radius:14px;padding:14px 14px 12px;box-shadow:0 12px 22px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:11px">'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#9a9488">RUN {i+1:02d}</span>'
          f'<svg width="16" height="16" viewBox="0 0 24 24"><path d="M6 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          # identical mini-bar glyph in every ticket
          f'<svg width="100%" height="46" viewBox="0 0 150 46" preserveAspectRatio="none">'
          + "".join(f'<rect x="{4+j*20}" y="{46-h}" width="13" height="{h}" rx="2.5" fill="rgb({ACC})" opacity="{0.55+0.06*j:.2f}"/>' for j,h in enumerate([18,30,24,40,34,44,28]))
          + '</svg></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Monday or Friday, same output","CONSISTENT")}
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{cells}</div>
      <div style="display:flex;align-items:baseline;gap:12px;margin-top:20px">
        <span style="font-family:\'DM Sans\';font-weight:900;font-size:40px;color:#FAFAF7">8 / 8</span>
        <span style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#c9a583">identical to spec</span></div>
      {cap("no more lottery - the recipe holds whoever runs it, whenever they run it.")}</div>'''

# 7. VERSIONS - DARK: a horizontal version timeline, current version glowing, held in your vault
def versions():
    W,H=820,430
    pts=[("v1","first draft",90),("v2","tighter close",300),("v3","added proof",510),("v4","live",720)]
    line=f'<line x1="90" y1="150" x2="720" y2="150" stroke="rgba(212,162,127,.3)" stroke-width="3"/>'
    dots=""; labels=""
    for i,(v,note,x) in enumerate(pts):
        cur=(i==len(pts)-1)
        if cur:
            dots+=(f'<circle cx="{x}" cy="150" r="26" fill="url(#cv)" filter="url(#vg)"/>'
              f'<text x="{x}" y="157" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">{v}</text>')
        else:
            dots+=(f'<circle cx="{x}" cy="150" r="18" fill="#2a2724" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
              f'<text x="{x}" y="156" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">{v}</text>')
        labels+=(f'<text x="{x}" y="212" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="{"#FAFAF7" if cur else "#a8a296"}">{note}</text>')
    # vault base holding the timeline
    vault=(f'<rect x="40" y="250" width="740" height="128" rx="20" fill="rgba(212,162,127,.05)" stroke="rgba(212,162,127,.2)"/>'
      f'<g transform="translate(360,286)"><rect x="0" y="22" width="100" height="66" rx="12" fill="none" stroke="rgb({ACC})" stroke-width="5"/>'
      f'<path d="M18 22 V12 a32 32 0 0 1 64 0 v10" fill="none" stroke="rgb({ACC})" stroke-width="5"/>'
      f'<circle cx="50" cy="52" r="8" fill="rgb({ACC})"/></g>'
      f'<text x="410" y="368" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">YOUR VAULT</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Fix it once, everyone upgrades","VERSIONED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="cv" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="vg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {line}{dots}{labels}{vault}
      </svg>
      {cap("improve the recipe and every agent inherits the new version instantly - it is yours.")}</div>'''

# 8. LOOP - IVORY: a loop arrow feeding a rising library of recipe spines (the shelf compounds)
def loop():
    spines=[("cold email",118),("proposal",150),("faq",182),("landing",214),("support",246),("contract",278)]
    bars=""
    n=len(spines)
    for i,(nm,h) in enumerate(spines):
        x=40+i*82
        bars+=(f'<g><rect x="{x}" y="{330-h}" width="58" height="{h}" rx="9" fill="url(#spn)" stroke="rgba(150,90,45,.25)"/>'
          f'<rect x="{x+8}" y="{342-h}" width="42" height="9" rx="4" fill="#96562d" opacity="0.85"/>'
          f'<text x="{x+29}" y="352" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8a745a">{nm}</text></g>')
    loop_arrow=(f'<path d="M556 300 a150 150 0 1 0 -150 -150" fill="none" stroke="#96562d" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 12"/>'
      f'<path d="M406 150 l-16 -22 m16 22 l-22 8" fill="none" stroke="#96562d" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
      f'<text x="500" y="60" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#96562d">+1 EACH JOB</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("The library compounds","THE LOOP","#2a2016")}
      <svg width="612" height="380" viewBox="0 0 612 380" style="display:block;margin:0 auto">
        <defs><linearGradient id="spn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fbf5ea"/><stop offset="100%" stop-color="#e7dac4"/></linearGradient></defs>
        <line x1="30" y1="331" x2="582" y2="331" stroke="rgba(150,90,45,.3)" stroke-width="2"/>
        {bars}{loop_arrow}
      </svg>
      {cap("add one recipe per job and your operator only gets sharper - it never resets.","#8a745a")}</div>'''

PANELS={"sources":sources(),"distill":distill(),"grounded":grounded(),"shelf":shelf(),
        "roster":roster(),"consistent":consistent(),"versions":versions(),"loop":loop()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src10"; os.makedirs(outd,exist_ok=True)
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
