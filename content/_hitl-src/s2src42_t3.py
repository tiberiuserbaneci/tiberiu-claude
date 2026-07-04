#!/usr/bin/env python3
# TIER 3 - s2src42 "CENTS PER BRIEF": the $80K SDR reframed as one Cortex command that turns any
# company URL into a qualified, cited, cents-priced, gated prospect dossier. Each panel a UNIQUE
# hand-built coded scene on a clean rounded card (per CLAUDE.md 31.0). No stat-chip strips, no cuts.
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

# 1. COMMAND - a coded terminal / command-palette window: one slash command drives the whole rep
def command():
    items=[("research","company url  ->  ranked brief",True),
           ("compare","two rivals, side by side",False),
           ("qualify","score against your ICP",False)]
    sug=""
    for nm,desc,on in items:
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "rgba(255,255,255,.02)"
        bd=f"1px solid rgba(212,162,127,.42)" if on else "1px solid rgba(255,255,255,.06)"
        col="#FAFAF7" if on else "#cfc9bd"
        tag=f'<span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">enter</span>' if on else ''
        sug+=(f'<div style="display:flex;align-items:center;gap:14px;background:{bg};border:{bd};border-radius:12px;padding:13px 16px">'
              f'<span style="font-family:DM Mono;font-size:16px;color:rgb({ACC})">/cortex</span>'
              f'<span style="font-family:DM Sans;font-weight:800;font-size:18px;color:{col}">{nm}</span>'
              f'<span style="font-family:DM Sans;font-size:15px;color:#8f8f85">{desc}</span>'
              f'<span style="margin-left:auto">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Not a hire. A keystroke.","COMMAND")}
      <div style="background:#141210;border:1px solid rgba(255,255,255,.09);border-radius:20px;overflow:hidden;box-shadow:inset 0 2px 3px rgba(255,255,255,.05),0 20px 40px rgba(0,0,0,.5)">
        <div style="display:flex;align-items:center;gap:9px;padding:14px 18px;background:linear-gradient(180deg,#2a2724,#211e1b);border-bottom:1px solid rgba(255,255,255,.06)">
          <span style="width:12px;height:12px;border-radius:50%;background:rgb(200,70,35)"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:rgb({ACC})"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:rgba(255,255,255,.28)"></span>
          <span style="margin-left:12px;font-family:DM Mono;font-size:13px;color:#8f8f85">ultron / cortex</span></div>
        <div style="padding:26px 26px 12px">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
            <span style="font-family:DM Mono;font-size:23px;color:rgb({ACC})">&gt;</span>
            <span style="font-family:DM Mono;font-size:23px;color:#FAFAF7">/cortex&nbsp;research&nbsp;</span>
            <span style="font-family:DM Mono;font-size:23px;color:#cfc9bd">competitor.com</span>
            <span style="width:12px;height:27px;background:rgb({ACC});display:inline-block;border-radius:2px"></span></div>
          <div style="display:flex;flex-direction:column;gap:11px">{sug}</div></div></div>
      {cap("type the command, drop a url. the rep is a keystroke, not a salary.")}</div>'''

# 2. INTAKE - one url pill fans DOWN into 5 extracted attribute tiles (link -> parsed fields)
def intake():
    W,H=820,440
    attrs=[("ICP FIT","92%"),("SIZE","2-50"),("FUNDING","$4M"),("STACK","no AI"),("TRIGGER","hiring x3")]
    ux,uy=410,52; n=len(attrs); slot=W/n; cy=300
    edges=""; tiles=""
    for i,(k,v) in enumerate(attrs):
        cx=slot*(i+0.5)
        edges+=f'<path d="M{ux} {uy+34} C{ux} 180,{cx:.0f} 190,{cx:.0f} {cy-34}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/><circle cx="{cx:.0f}" cy="{cy-34}" r="4" fill="rgb({ACC})"/>'
        tiles+=(f'<g><rect x="{cx-72:.0f}" y="{cy-32}" width="144" height="102" rx="17" fill="url(#tile)" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{cx:.0f}" y="{cy:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="rgb({ACC})">{k}</text>'
          f'<text x="{cx:.0f}" y="{cy+42:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#FAFAF7">{v}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One link in, a full dossier out","EXTRACT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <filter id="ug" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {edges}
        <g filter="url(#ug)"><rect x="{ux-170}" y="{uy-32}" width="340" height="64" rx="32" fill="linear" style="fill:#2a2724" stroke="rgb({ACC})" stroke-width="2"/></g>
        <circle cx="{ux-118}" cy="{uy}" r="15" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/><line x1="{ux-133}" y1="{uy}" x2="{ux-103}" y2="{uy}" stroke="rgb({ACC})" stroke-width="2"/><ellipse cx="{ux-118}" cy="{uy}" rx="7" ry="15" fill="none" stroke="rgb({ACC})" stroke-width="2"/>
        <text x="{ux-88}" y="{uy+7}" font-family="DM Mono" font-size="20" fill="#FAFAF7">competitor.com</text>
      </svg>
      {cap("it reads the site, news, hiring and stack, then pulls the fields that matter.")}</div>'''

# 3. DOSSIER - IVORY one-page brief mockup: company header, fit badge, 3 cited sections
def dossier():
    bullets=[("SIGNAL","Raised $4M in May, hiring 3 ops roles"),
             ("FIT","2-50 team, IT services - center of your ICP"),
             ("ANGLE","No AI layer yet - lead with the Cortex demo")]
    rows=""
    for k,v in bullets:
        rows+=(f'<div style="display:flex;gap:16px;align-items:flex-start;padding:15px 0;border-top:1px solid rgba(120,95,60,.18)">'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#96562d;width:70px;padding-top:4px">{k}</span>'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:20px;color:#2a2016;line-height:1.35">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">A ranked brief, cited and dated</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">ONE PAGE</span></div>
      <div style="background:rgba(255,255,255,.62);border:1px solid rgba(120,95,60,.16);border-radius:18px;padding:22px 26px 8px">
        <div style="display:flex;align-items:center;justify-content:space-between;padding-bottom:14px">
          <div><div style="font-family:DM Sans;font-weight:900;font-size:28px;color:#2a2016">Northwind Robotics</div>
          <div style="font-family:DM Mono;font-size:14px;color:#8a745a;margin-top:2px">northwindrobotics.com</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:#96562d;border-radius:16px;padding:11px 20px;box-shadow:0 10px 20px rgba(150,90,45,.3)">
            <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#fdfbf6;line-height:1">92</span>
            <span style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:rgba(253,251,246,.85)">FIT SCORE</span></div></div>
        {rows}</div>
      {cap("every claim carries its source. one page to act on, not ten open tabs.","#8a745a")}</div>'''

# 4. PRICE - CENTS: an $80K human desk (struck) vs a few-cents Cortex brief. big before/after
def price():
    return f'''<div style="width:900px;{CARD};padding:38px 44px 38px">
      {htitle("An $80K desk, down to cents","THE MATH")}
      <div style="display:flex;align-items:stretch;gap:22px;margin-top:6px">
        <div style="flex:1;background:linear-gradient(160deg,#2a211d,#1d1815);border:1px solid rgba(200,70,35,.32);border-radius:20px;padding:28px 24px;text-align:center;display:flex;flex-direction:column;justify-content:center">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb(200,105,80);margin-bottom:12px">ONE HUMAN SDR</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:54px;color:#c9c3b8;line-height:1;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.85);text-decoration-thickness:5px">$80,000</div>
          <div style="font-family:DM Sans;font-size:17px;color:#8f8f85;margin-top:12px">per year, before ramp</div></div>
        <div style="flex-shrink:0;display:flex;align-items:center">
          <svg width="66" height="40" viewBox="0 0 66 40" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 20h48M40 8l16 12-16 12"/></svg></div>
        <div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:20px;padding:28px 24px;text-align:center;box-shadow:0 0 46px rgba(212,162,127,.22);display:flex;flex-direction:column;justify-content:center">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:8px">ONE CORTEX BRIEF</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:78px;color:#FAFAF7;line-height:1">4<span style="font-size:46px">&cent;</span></div>
          <div style="font-family:DM Sans;font-size:17px;color:#c9a583;margin-top:10px">per qualified prospect</div></div>
      </div>
      {cap("pay per brief, in cents. the desk is gone, the briefs are not.")}</div>'''

# 5. SCORE - IVORY: big fit number + 4 weighted criteria bars (shows its work)
def score():
    crit=[("ICP match",94),("Timing",90),("Budget signal",88),("Reachability",96)]
    bars=""
    for k,v in crit:
        bars+=(f'<div style="margin-bottom:17px"><div style="display:flex;justify-content:space-between;margin-bottom:6px">'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:18px;color:#2a2016">{k}</span>'
          f'<span style="font-family:DM Mono;font-size:16px;color:#96562d">{v}</span></div>'
          f'<div style="height:14px;border-radius:8px;background:rgba(150,90,45,.14);overflow:hidden">'
          f'<div style="height:100%;width:{v}%;border-radius:8px;background:linear-gradient(90deg,#c88a5a,#96562d)"></div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:22px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It scores the fit and shows why</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">FIT 92 / 100</span></div>
      <div style="display:flex;gap:40px;align-items:center">
        <div style="flex-shrink:0;text-align:center">
          <div style="font-family:DM Sans;font-weight:900;font-size:124px;color:#2a2016;line-height:.86">92</div>
          <div style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#96562d;margin-top:6px">QUALIFIED</div></div>
        <div style="flex:1">{bars}</div>
      </div>
      {cap("a number you can defend, with the four reasons standing behind it.","#8a745a")}</div>'''

# 6. GATE - HUMAN GATE: brief ready -> lock -> outbox waiting for your tap
def gate():
    lock=f'''<svg width="150" height="188" viewBox="0 0 150 188">
        <defs><filter id="lg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <g filter="url(#lg)"><rect x="20" y="34" width="110" height="110" rx="26" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <g transform="translate(47,60)"><rect x="0" y="34" width="56" height="42" rx="10" fill="none" stroke="rgb({ACC})" stroke-width="5.5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5.5"/></g>
        <text x="75" y="178" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text></svg>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It drafts everything, then stops","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:18px;margin-top:8px">
        <div style="flex:1;background:linear-gradient(160deg,#33302c,#211e1a);border:1px solid rgba(255,255,255,.1);border-radius:18px;padding:22px 22px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC});margin-bottom:10px">BRIEF READY</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7">Northwind Robotics</div>
          <div style="font-family:DM Sans;font-size:16px;color:#8f8f85;margin-top:5px">draft email + 2 follow-ups</div></div>
        <div style="flex-shrink:0">{lock}</div>
        <div style="flex:1;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.18);border-radius:18px;padding:22px 22px;opacity:.62">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#8f8f85;margin-bottom:10px">OUTBOX</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#9a9488">holding</div>
          <div style="font-family:DM Sans;font-size:16px;color:#6f6a60;margin-top:5px">nothing ships until you approve</div></div>
      </div>
      {cap("it writes the brief and the outreach, then parks. one tap from you before a word sends.")}</div>'''

# 7. MEMORY - central ICP core, 5 past runs orbiting, all drawing from the one core
def memory():
    cx,cy=410,232
    runs=[("Northwind",-90),("Globex",-18),("Initech",54),("Acme Data",126),("Vertex Co",198)]
    lines=""; nodes=""
    for nm,a in runs:
        x=cx+168*math.cos(math.radians(a)); y=cy+168*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#cfc9bd">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+22:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">scored</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("It never asks who you sell to","SHARED CORE")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="54%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="82" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">YOUR</text>
        <text x="{cx}" y="{cy+24}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ICP</text>
        {nodes}
      </svg>
      {cap("your ideal customer lives in one core. every run scores against the same memory.")}</div>'''

# 8. QUEUE - many company urls converge into one RANKED shortlist (who to call first, and why)
def queue():
    urls=[("competitor.com",60),("rival.io",145),("target.co",225),("prospect.com",305),("lead.ai",390)]
    jx=430
    edges=""; pills=""
    for nm,y in urls:
        edges+=f'<path d="M182 {y} C300 {y},320 225,{jx} 225" stroke="rgba(212,162,127,.38)" stroke-width="2" fill="none"/>'
        pills+=(f'<rect x="30" y="{y-22}" width="152" height="44" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="106" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c9c3b8">{nm}</text>')
    ranked=[("1","Northwind","92"),("2","Globex","88"),("3","Initech","81")]
    cards=""
    for i,(rk,nm,sc) in enumerate(ranked):
        y=i*102; on=(i==0)
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "linear-gradient(160deg,#302c28,#201d1a)"
        bd=f"1.5px solid rgb({ACC})" if on else "1px solid rgba(255,255,255,.1)"
        cards+=(f'<div style="position:absolute;left:470px;top:{60+y}px;width:352px;{("box-shadow:0 0 34px rgba(212,162,127,.25);" if on else "")}background:{bg};border:{bd};border-radius:16px;padding:16px 18px;display:flex;align-items:center;gap:16px">'
          f'<span style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.4);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">{rk}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7">{nm}</span>'
          f'<span style="flex-shrink:0;font-family:DM Sans;font-weight:900;font-size:26px;color:{"#FAFAF7" if on else "#9a9488"}">{sc}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Fifty urls in, a ranked shortlist out","QUEUE")}
      <div style="position:relative;height:452px">
        <svg width="450" height="452" viewBox="0 0 450 452" style="position:absolute;left:0;top:0">
          {edges}{pills}
          <circle cx="{jx}" cy="225" r="7" fill="rgb({ACC})"/>
        </svg>
        {cards}
      </div>
      {cap("feed it a list, get a ranked queue - who to call first and exactly why.")}</div>'''

PANELS={"command":command(),"intake":intake(),"dossier":dossier(),"price":price(),
        "score":score(),"gate":gate(),"memory":memory(),"queue":queue()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src42"; os.makedirs(outd,exist_ok=True)
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
