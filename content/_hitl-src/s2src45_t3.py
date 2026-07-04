#!/usr/bin/env python3
# TIER 3 - THE HOURS LEDGER, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded
# scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Angle: founder-GTM time collapse - recurring jobs, hours before vs minutes/cents after.
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

# 1. LEDGER - the signature: a DENSE before/after ledger of recurring founder jobs. Heavy, packed,
# every row filled edge to edge (hours on the left, minutes/cents on the right), one lit total row.
def ledger():
    rows=[("Account research","2h","2m"),("Company brief","1h","90s"),
          ("Signal scan","3h","live"),("Sequence draft","90m","4m"),
          ("Objection prep","1h","30s"),("Proposal draft","2h","6m"),
          ("Content repurpose","2h","5m"),("Code review","1h","8m"),
          ("Pipeline review","1h","3m"),("Weekly digest","45m","20s")]
    body=""
    for i,(job,bef,aft) in enumerate(rows):
        bg="rgba(250,250,247,.035)" if i%2 else "rgba(250,250,247,.0)"
        body+=(f'<div style="display:flex;align-items:center;gap:18px;padding:11px 20px;background:{bg};border-radius:9px">'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:600;font-size:19px;color:#e6e1d7">{job}</span>'
          f'<span style="width:78px;text-align:right;font-family:\'DM Mono\';font-size:17px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.55)">{bef}</span>'
          f'<span style="width:26px;text-align:center;font-family:\'DM Mono\';font-size:15px;color:rgb({ACC})">&#8594;</span>'
          f'<span style="width:78px;text-align:right;font-family:\'DM Mono\';font-weight:500;font-size:19px;color:rgb({ACC})">{aft}</span></div>')
    total=('<div style="display:flex;align-items:center;gap:18px;padding:15px 20px;margin-top:8px;'
      'background:linear-gradient(160deg,#403a33,#241f1a);border:1px solid rgba(212,162,127,.34);border-radius:13px">'
      '<span style="flex:1;font-family:\'DM Sans\';font-weight:900;font-size:22px;color:#FAFAF7">The full week</span>'
      '<span style="width:78px;text-align:right;font-family:\'DM Mono\';font-size:18px;color:#c9a583">15h+</span>'
      f'<span style="width:26px;text-align:center;font-family:\'DM Mono\';font-size:15px;color:rgb({ACC})">&#8594;</span>'
      f'<span style="width:78px;text-align:right;font-family:\'DM Sans\';font-weight:900;font-size:22px;color:rgb({ACC})">cents</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A week, priced in hours","BEFORE &#8594; AFTER")}
      <div style="display:flex;flex-direction:column;gap:2px">{body}{total}</div>
      {cap("the same recurring jobs - hours on the left, minutes and cents on the right.")}</div>'''

# 2. ROUTER - one job token routed into 3 tier lanes, SMART lit/picked, priced in cents
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
        cards+=(f'<div style="position:absolute;left:300px;top:{y-40}px;width:170px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A brain that budgets itself","MODEL ROUTER")}
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
      {cap("one job in, the cheapest tier that can actually do it - cents, not dollars.")}</div>'''

# 3. RESEARCH - many open tabs on the left collapse via bezier into one ranked BRIEF disc
def research():
    W,H=790,470
    tabs=[("company site",70),("pricing page",158),("job board",246),("news feed",334),("+ 11 more",422)]
    hubx,huby=630,246
    edges=""; nodes=""
    for nm,y in tabs:
        mx=(190+hubx)/2
        edges+=f'<path d="M196 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-72} {huby}" stroke="rgba(212,162,127,.42)" stroke-width="2.4" fill="none"/>'
        ghost=nm=="+ 11 more"
        fill="#232019" if ghost else "#2a2724"; tc="#7a746a" if ghost else "#c9c3b8"
        nodes+=(f'<rect x="42" y="{y-27}" width="154" height="54" rx="12" fill="{fill}" stroke="rgba(255,255,255,.09)"/>'
          f'<circle cx="66" cy="{y}" r="6" fill="rgb({ACC})" opacity="{0.4 if ghost else 0.9}"/>'
          f'<text x="86" y="{y+5}" font-family="DM Mono" font-size="15" fill="{tc}">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Fifteen tabs become one brief","CORTEX")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="82" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#1a0f0a">BRIEF</text>
        <text x="{hubx}" y="{huby+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">1 page, ranked</text>
        <rect x="536" y="352" width="188" height="54" rx="14" fill="#211d19" stroke="rgba(212,162,127,.3)"/>
        <text x="630" y="378" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">2h &#8594; 2m</text>
        <text x="630" y="396" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">read time</text>
      </svg>
      {cap("company, market and person read into one ranked page - the job that started it.")}</div>'''

# 4. CONTENT - IVORY: one source asset fans OUT into a week of channel outputs, in your voice
def repurpose():
    chans=[("LinkedIn",90),("X thread",172),("Newsletter",254),("TikTok",336),("Instagram",90),("Blog",254)]
    # right column arranged in two sub-columns for density
    right=""
    layout=[("LinkedIn",70),("X thread",158),("Newsletter",246),("TikTok",334),("Instagram",422)]
    W,H=790,470
    srcx,srcy=140,246; colx=470
    for nm,y in layout:
        right+=(f'<path d="M{srcx+92} {srcy} C{(srcx+colx)/2:.0f} {srcy},{(srcx+colx)/2:.0f} {y},{colx-8} {y}" stroke="rgba(150,90,45,.4)" stroke-width="2.2" fill="none"/>'
          f'<rect x="{colx}" y="{y-26}" width="250" height="52" rx="14" fill="rgba(255,255,255,.62)" stroke="rgba(150,90,45,.22)"/>'
          f'<circle cx="{colx+28}" cy="{y}" r="7" fill="#96562d"/>'
          f'<text x="{colx+52}" y="{y+6}" font-family="DM Sans" font-weight="700" font-size="18" fill="#2a2016">{nm}</text>'
          f'<text x="{colx+238}" y="{y+6}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#96562d">in voice</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("One asset, a week of channels","PULSE","#2a2016")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="src" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#96562d"/><stop offset="100%" stop-color="#6f3d1c"/></linearGradient>
        <filter id="ss" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="rgba(150,90,45,.4)"/></filter></defs>
        {right}
        <g filter="url(#ss)"><rect x="{srcx-92}" y="{srcy-96}" width="184" height="192" rx="20" fill="url(#src)"/></g>
        <text x="{srcx}" y="{srcy-8}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#fdfbf6">ONE</text>
        <text x="{srcx}" y="{srcy+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#fdfbf6">POST</text>
        <text x="{srcx}" y="{srcy+58}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgba(253,251,246,.8)">2h &#8594; 5m</text>
      </svg>
      {cap("sampled from your real posts, banned words enforced on every draft.","#8a745a")}</div>'''

# 5. CODE - isometric BUILD -> TEST -> SHIP pipeline ending in a merged PR
def ship():
    steps=[("BUILD","wrote the page",0),("TEST","38 passed, 0 failed",1),("SHIP","live on main",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Built, tested, shipped","SENTINEL")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:120px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Merged &#10003; PR #182</div></div></div>
      {cap("plain English becomes a page, tested before it ships - an afternoon to minutes.")}</div>'''

# 6. DEALS - IVORY: an objection struck through, reframed into a response + a small close-plan check
def deals():
    checks=["Budget confirmed","Decision maker named","Close date set"]
    checklist=""
    for c in checks:
        checklist+=(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><circle cx="12" cy="12" r="10" stroke="rgba(150,90,45,.3)"/><path d="M7 12.5l3.2 3.2L17 8.5"/></svg>'
          f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:18px;color:#2a2016">{c}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("It answers the objection","STRIKER","#2a2016")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1;display:flex;flex-direction:column;gap:16px">
          <div style="background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.28);border-radius:16px;padding:16px 20px">
            <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#b1502f;margin-bottom:6px">PROSPECT</div>
            <div style="font-family:'DM Sans';font-size:20px;color:#7a5b48;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)">"Too expensive right now."</div></div>
          <div style="display:flex;justify-content:center"><svg width="34" height="24" viewBox="0 0 34 24" fill="none" stroke="#96562d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h26M20 4l9 8-9 8"/></svg></div>
          <div style="background:rgba(255,255,255,.66);border-left:4px solid #96562d;border-radius:14px;padding:16px 20px">
            <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#96562d;margin-bottom:6px">DRAFTED REPLY</div>
            <div style="font-family:'DM Sans';font-size:19px;color:#2a2016;line-height:1.4">"At cents per run, it pays back in the first week. Let me show the math."</div></div>
        </div>
        <div style="width:300px;flex-shrink:0;background:rgba(255,255,255,.5);border:1px solid rgba(150,90,45,.2);border-radius:18px;padding:22px 22px">
          <div style="font-family:'DM Sans';font-weight:800;font-size:19px;color:#2a2016;margin-bottom:16px">Close plan</div>
          {checklist}
          <div style="border-top:1px solid rgba(150,90,45,.2);margin-top:8px;padding-top:14px;font-family:'DM Mono';font-size:13px;color:#96562d">drafted in 30s</div>
        </div>
      </div>
      {cap("qualifies, handles the pushback and drafts the close plan - every deal, same rigor.","#8a745a")}</div>'''

# 7. MEMORY - radial shared core; five workflow lifelines draw from one memory (why jobs repeat)
def memory():
    cx,cy=210,210
    org=[("ICP",-90),("PIPELINE",-18),("PRICING",54),("DOCS",126),("VOICE",198)]
    lines=""; nodes=""
    for nm,a in org:
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="37" fill="#38342e" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".03em" fill="#eae4d8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="mc" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="56" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">CORE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">shared</text></svg>
      <div style="flex:1">
        {htitle("Memory is why it repeats","ONE CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing and docs live in one core every agent reads. That is why each job reruns in a single tap, not from scratch.</div>
        {cap("nothing starts cold - one memory feeds all seven agents.")}</div></div>'''

# 8. GATE - full-capability orb held on the operator's reins, one lock (hours refunded, control kept)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Hours refunded, control kept","HUMAN GATE")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="210" r="130" fill="url(#orb)"/></g>
        <text x="200" y="204" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a160c">FULL</text>
        <text x="200" y="238" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <path d="M334 210 H610" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="140" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,178)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every external move parks for your tap before anything sends. still your company.")}</div>'''

PANELS={"ledger":ledger(),"router":router(),"research":research(),"repurpose":repurpose(),
        "ship":ship(),"deals":deals(),"memory":memory(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src45"; os.makedirs(outd,exist_ok=True)
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
