#!/usr/bin/env python3
# TIER 3 - ON-BRAND WITHOUT A DESIGNER, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one mono caption, NO generic
# stat-chip strips, NO clip-path cuts, NO extruded walls. Warm palette, Ultron price = cents.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; RED="200,70,35"; IV="#96562d"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. DRIFT - swatch/type scene: 8 mismatched brand tiles, each a drifted warm tone + a wrong font,
# every one red-flagged off-brand. The chaos of "ten shades of you" with no guardrail.
def drift():
    tiles=[("#b8674a","Inter"),("#a8724f","Arial"),("#cc8a5c","Roboto"),("#9c5f3e","Helvetica"),
           ("#d19a6f","Fraunces"),("#8f5233","Space Grotesk"),("#c07a52","Bricolage"),("#a66b45","Calibri")]
    cells=""
    for i,(hx,fn) in enumerate(tiles):
        cells+=(f'<div style="width:186px;background:#221f1b;border:1px solid rgba(255,255,255,.08);border-radius:16px;overflow:hidden;box-shadow:0 14px 26px rgba(0,0,0,.45)">'
          f'<div style="height:62px;background:{hx};position:relative"><span style="position:absolute;left:12px;bottom:8px;font-family:\'DM Mono\';font-size:12px;color:rgba(0,0,0,.55)">{hx}</span></div>'
          f'<div style="padding:12px 14px 14px;display:flex;align-items:center;justify-content:space-between">'
          f'<div><div style="font-family:\'DM Sans\';font-weight:800;font-size:17px;color:#e6e0d4">post {i+1:02d}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:12px;color:#8f8f85;margin-top:2px">{fn}</div></div>'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:rgb({RED})">&#10007;</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten shades of you","NO GUARDRAIL",tagc=f"rgb({RED})")}
      <div style="display:flex;flex-wrap:wrap;gap:16px;justify-content:center">{cells}</div>
      <div style="display:flex;align-items:center;gap:10px;margin-top:18px;justify-content:center">
        <span style="width:9px;height:9px;border-radius:50%;background:rgb({RED});box-shadow:0 0 10px rgba({RED},.7)"></span>
        <span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.1em;color:rgb({RED})">8 assets &middot; 8 fonts &middot; 8 accents &middot; 0 agreements</span></div>
      {cap("without a designer, every asset negotiates its own fonts and colors.")}</div>'''

# 2. TOKENS - IVORY brand-token board: the look written down once as law (color/type/canvas/logo).
def tokens():
    def row(label,body): return (f'<div style="display:flex;align-items:flex-start;gap:18px;padding:16px 0;border-top:1px solid rgba(120,95,60,.16)">'
        f'<div style="width:118px;flex-shrink:0;font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:{IV};padding-top:4px">{label}</div>'
        f'<div style="flex:1">{body}</div></div>')
    swatches="".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><div style="width:56px;height:56px;border-radius:12px;background:{hx};box-shadow:0 4px 10px rgba(120,95,60,.25),inset 0 1px 2px rgba(255,255,255,.35)"></div><span style="font-family:\'DM Mono\';font-size:11px;color:#6f5b40">{hx}</span></div>' for hx in ["#191919","#CC785C","#FAFAF7","#D4A27F"])
    colors=f'<div style="display:flex;gap:16px">{swatches}</div>'
    typ=('<div style="display:flex;flex-direction:column;gap:6px">'
      '<div style="font-family:\'DM Sans\';font-weight:900;font-size:26px;color:#2a2016">DM Sans <span style="font-family:\'DM Sans\';font-weight:400;font-size:16px;color:#8a745a">400 / 700 / 900</span></div>'
      '<div style="font-family:\'DM Mono\';font-size:16px;color:#5a4634">DM Mono &middot; labels, meta, tags</div></div>')
    canvas=('<div style="display:flex;gap:10px">'
      '<span style="font-family:\'DM Mono\';font-size:14px;color:#2a2016;background:rgba(150,90,45,.12);border:1px solid rgba(150,90,45,.22);border-radius:8px;padding:6px 12px">1080 &times; 1450</span>'
      '<span style="font-family:\'DM Mono\';font-size:14px;color:#2a2016;background:rgba(150,90,45,.12);border:1px solid rgba(150,90,45,.22);border-radius:8px;padding:6px 12px">44px side pad</span>'
      '<span style="font-family:\'DM Mono\';font-size:14px;color:#2a2016;background:rgba(150,90,45,.12);border:1px solid rgba(150,90,45,.22);border-radius:8px;padding:6px 12px">safe 300 / 330</span></div>')
    logo=('<div style="display:flex;align-items:center;gap:12px">'
      '<div style="width:34px;height:34px;border-radius:50%;background:radial-gradient(circle at 68% 30%,#ff9a5a,#c84623 40%,#1a2740 78%)"></div>'
      '<span style="font-family:\'DM Sans\';font-size:16px;color:#5a4634">sphere only, never the wordmark</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Your look, written as law</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:{IV}">tokens.css</span></div>
      {row("COLOR",colors)}{row("TYPE",typ)}{row("CANVAS",canvas)}{row("LOGO",logo)}
      {cap("one token file every asset obeys, so nothing negotiates its own look.","#8a745a")}</div>'''

# 3. PACK - IVORY component-library grid: 822 pieces, grouped, every one on-brand.
def pack():
    groups=[("Cards",240),("Heroes",96),("Charts",180),("Covers",120),("Chips",186)]
    tiles=""
    icons={"Cards":'<rect x="6" y="8" width="36" height="24" rx="4" fill="none" stroke="{c}" stroke-width="2.4"/><line x1="12" y1="16" x2="34" y2="16" stroke="{c}" stroke-width="2.4"/><line x1="12" y1="24" x2="26" y2="24" stroke="{c}" stroke-width="2.4"/>',
      "Heroes":'<rect x="6" y="8" width="36" height="24" rx="4" fill="{c}" opacity="0.16"/><rect x="6" y="8" width="36" height="24" rx="4" fill="none" stroke="{c}" stroke-width="2.4"/><circle cx="16" cy="20" r="5" fill="{c}"/>',
      "Charts":'<line x1="10" y1="32" x2="10" y2="10" stroke="{c}" stroke-width="2.4"/><line x1="10" y1="32" x2="40" y2="32" stroke="{c}" stroke-width="2.4"/><rect x="16" y="20" width="6" height="12" fill="{c}"/><rect x="26" y="14" width="6" height="18" fill="{c}"/>',
      "Covers":'<rect x="12" y="6" width="26" height="28" rx="4" fill="none" stroke="{c}" stroke-width="2.4"/><rect x="6" y="10" width="26" height="24" rx="4" fill="{c}" opacity="0.16" stroke="{c}" stroke-width="2.4"/>',
      "Chips":'<rect x="6" y="14" width="36" height="16" rx="8" fill="none" stroke="{c}" stroke-width="2.4"/><circle cx="16" cy="22" r="3" fill="{c}"/><line x1="24" y1="22" x2="36" y2="22" stroke="{c}" stroke-width="2.4"/>'}
    for nm,n in groups:
        ic=icons[nm].replace("{c}",IV)
        tiles+=(f'<div style="width:150px;background:rgba(255,255,255,.55);border:1px solid rgba(150,90,45,.18);border-radius:16px;padding:16px 14px;box-shadow:0 10px 22px rgba(120,95,60,.16)">'
          f'<svg width="48" height="40" viewBox="0 0 48 40">{ic}</svg>'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:30px;color:#2a2016;margin-top:8px">{n}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#8a745a;margin-top:1px">{nm.upper()}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">822, already on-brand</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:{IV}">COMPONENT PACK</span></div>
      <div style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center">{tiles}</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-top:16px">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{IV}" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>
        <span style="font-family:'DM Mono';font-size:13px;color:{IV}">240 + 96 + 180 + 120 + 186 = 822 pieces</span></div>
      {cap("cards, heroes, charts, covers: assembled from your pack, never from scratch.","#8a745a")}</div>'''

# 4. OUTPUTS - node graph: one token source feeds proposal / landing page / carousel, one family.
def outputs():
    W,H=820,430
    outs=[("Proposal","PDF",90),("Landing page","web",215),("Carousel","reel",340)]
    hubx,hy=150,215; tx=470
    edges=""; cards=""
    for nm,kind,y in outs:
        mx=(hubx+tx)/2
        edges+=f'<path d="M{hubx+70} {hy} C{mx:.0f} {hy},{mx:.0f} {y},{tx-8} {y}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        cards+=(f'<g><rect x="{tx}" y="{y-46}" width="300" height="92" rx="16" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<rect x="{tx}" y="{y-46}" width="10" height="92" rx="5" fill="rgb({ACC})"/>'
          f'<circle cx="{tx+42}" cy="{y}" r="15" fill="none" stroke="rgb({ACC})" stroke-width="2"/><circle cx="{tx+42}" cy="{y}" r="6" fill="rgb({ACC})"/>'
          f'<text x="{tx+74}" y="{y-4}" font-family="DM Sans" font-weight="800" font-size="21" fill="#FAFAF7">{nm}</text>'
          f'<text x="{tx+74}" y="{y+20}" font-family="DM Mono" font-size="13" fill="#8f8f85">same tokens &middot; {kind}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every output, one family","ONE SOURCE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="src" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {edges}
        <g filter="url(#sg)"><circle cx="{hubx}" cy="{hy}" r="70" fill="url(#src)"/></g>
        <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">TOKENS</text>
        <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one source</text>
        {cards}
      </svg>
      {cap("the proposal matches the landing page matches the carousel.")}</div>'''

# 5. SPEED8 - timeline: the OLD slow drift-fix loop vs the NEW guardrail fast path.
def speed8():
    def lane(y,label,steps,col,total,dim):
        seg=""; n=len(steps); x0=150; x1=770; gap=(x1-x0)/(n-1)
        dsh='stroke-dasharray="3 8"' if dim else ''
        for i,st in enumerate(steps):
            x=x0+i*gap
            if i<n-1: seg+=f'<line x1="{x:.0f}" y1="{y}" x2="{x+gap:.0f}" y2="{y}" stroke="{col}" stroke-width="3" {dsh}/>'
            fill=col if not dim else "#2a2724"
            seg+=(f'<circle cx="{x:.0f}" cy="{y}" r="11" fill="{fill}" stroke="{col}" stroke-width="2.5"/>'
              f'<text x="{x:.0f}" y="{y+34}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="{"#8f8f85" if dim else "#d9d5cc"}">{st}</text>')
        return (f'<text x="30" y="{y+5}" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="{col}">{label}</text>{seg}'
          f'<text x="790" y="{y+5}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="20" fill="{col}" transform="translate(60,0)">{total}</text>')
    old=lane(96,"OLD",["draft","review","drift fix","re-review","ship"],f"rgb({RED})","3 days",True)
    new=lane(250,"NOW",["draft","ship"],f"rgb({ACC})","11 min",False)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("On-brand is the fast path","GUARDRAIL")}
      <svg width="860" height="330" viewBox="0 0 860 330" style="display:block;margin:0 auto">
        <line x1="20" y1="175" x2="840" y2="175" stroke="rgba(255,255,255,.07)"/>
        {old}{new}
        <text x="430" y="322" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">the guardrail deletes the review loop, not just the errors</text>
      </svg>
      {cap("no review cycles, no drift fixes: the quick version becomes the correct one.")}</div>'''

# 6. GATE8 - radial hub: one blessed template in the center, every instance inherits the approval.
def gate8():
    cx,cy,R=410,220,168
    kinds=["email","deck","one-pager","carousel","landing","social ad"]
    spokes=""; nodes=""
    for i,k in enumerate(kinds):
        a=-90+i*60
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2" stroke-dasharray="2 9"/>'
        nodes+=(f'<g><rect x="{x-70:.0f}" y="{y-30:.0f}" width="140" height="60" rx="14" fill="#221f1b" stroke="rgba(255,255,255,.1)"/>'
          f'<circle cx="{x-46:.0f}" cy="{y:.0f}" r="12" fill="rgba(127,211,154,.14)"/>'
          f'<path d="M{x-52:.0f} {y:.0f} l4 4 l8 -9" fill="none" stroke="#7fd39a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<text x="{x-24:.0f}" y="{y+5:.0f}" font-family="DM Sans" font-weight="700" font-size="16" fill="#d9d5cc">{k}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Bless it once, inherit forever","ONE APPROVAL")}
      <svg width="820" height="460" viewBox="0 0 820 460" style="display:block;margin:0 auto">
        <defs><radialGradient id="tmpl" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="tg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spokes}
        <g filter="url(#tg2)"><circle cx="{cx}" cy="{cy}" r="82" fill="url(#tmpl)"/></g>
        <g transform="translate({cx-24},{cy-40})"><rect x="0" y="24" width="48" height="36" rx="8" fill="none" stroke="#2a160c" stroke-width="5"/><path d="M9 24 V13 a15 15 0 0 1 30 0 v11" fill="none" stroke="#2a160c" stroke-width="5"/></g>
        <text x="{cx}" y="{cy+42}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">TEMPLATE</text>
        {nodes}
      </svg>
      {cap("you bless the template once; every instance after inherits the blessing.")}</div>'''

# 7. COST8 - gauge: the retainer dial sweeps from a high-bill red zone down to cents. Ultron = cents.
def cost8():
    cx,cy,R=305,300,205
    def pt(deg,rr=R): return (cx+rr*math.cos(math.radians(deg)), cy-rr*math.sin(math.radians(deg)))
    lx,ly=pt(180); sx,sy=pt(108); rx,ry=pt(0)
    red_arc=f'M{lx:.0f} {ly:.0f} A{R} {R} 0 0 1 {sx:.0f} {sy:.0f}'
    acc_arc=f'M{sx:.0f} {sy:.0f} A{R} {R} 0 0 1 {rx:.0f} {ry:.0f}'
    nx,ny=pt(24,R-26)                      # needle points to the cents end
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("The retainer became config","PAY PER TOKEN")}
      <svg width="620" height="360" viewBox="0 0 620 360" style="display:block;margin:0 auto">
        <defs><filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        <path d="{red_arc}" fill="none" stroke="rgb({RED})" stroke-width="30" stroke-linecap="round" opacity="0.85"/>
        <path d="{acc_arc}" fill="none" stroke="rgb({ACC})" stroke-width="30" stroke-linecap="round"/>
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#2a2724" stroke="rgb({ACC})" stroke-width="3"/>
        <text x="{cx}" y="{cy-64}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="64" fill="#FAFAF7">9&#162;</text>
        <text x="{cx}" y="{cy-30}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({ACC})">PER ASSET</text>
      </svg>
      <div style="display:flex;gap:16px;margin-top:6px">
        <div style="flex:1;background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.3);border-radius:14px;padding:14px 18px">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:rgb({RED})">BEFORE</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:22px;color:#FAFAF7;margin-top:3px">$4,000/mo retainer</div></div>
        <div style="flex:1;background:rgba(212,162,127,.09);border:1px solid rgba(212,162,127,.34);border-radius:14px;padding:14px 18px">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:rgb({ACC})">NOW</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:22px;color:#FAFAF7;margin-top:3px">cents, pay per token</div></div>
      </div>
      {cap("high bills live in the old workflow. this one is configuration.")}</div>'''

# 8. TEST8 - iso stack: two finished assets side by side, same palette, the stranger test passes.
def test8():
    def asset(kind,swap):
        # a mini mockup: title bar + hero block + accent bar + logo dot - both share the SAME palette
        return (f'<div style="width:300px;background:linear-gradient(160deg,#232019,#191713);border:1px solid rgba(255,255,255,.10);border-radius:20px;padding:20px;box-shadow:0 34px 54px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">'
          f'<div style="width:24px;height:24px;border-radius:50%;background:radial-gradient(circle at 66% 30%,#ff9a5a,#c84623 42%,#1a2740 80%)"></div>'
          f'<span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.14em;color:#8f8f85">{kind}</span></div>'
          f'<div style="height:88px;border-radius:12px;background:linear-gradient(160deg,rgb({ACC}),#8a4a2c)"></div>'
          f'<div style="height:14px;width:{"70%" if not swap else "84%"};border-radius:7px;background:rgba(250,250,247,.82);margin-top:14px"></div>'
          f'<div style="height:10px;width:{"52%" if not swap else "44%"};border-radius:5px;background:rgba(250,250,247,.34);margin-top:9px"></div>'
          f'<div style="display:inline-flex;align-items:center;gap:7px;margin-top:16px;background:rgb({ACC});border-radius:999px;padding:7px 15px">'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:13px;color:#1a0f0a">51ultron.com</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Same company?","STRANGER TEST")}
      <div style="perspective:1700px;display:flex;align-items:center;justify-content:center;gap:8px;height:340px">
        <div style="transform:rotateY(20deg) rotateZ(-3deg)">{asset("carousel slide",False)}</div>
        <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:rgb({ACC});align-self:center;padding:0 6px">=</div>
        <div style="transform:rotateY(-20deg) rotateZ(3deg)">{asset("landing page",True)}</div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-top:14px">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#7fd39a" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>
        <span style="font-family:'DM Mono';font-size:14px;color:#7fd39a">no stranger can tell them apart &middot; the guardrail works</span></div>
      {cap("if a stranger cannot tell, the guardrail is holding.")}</div>'''

PANELS={"drift":drift(),"tokens":tokens(),"pack":pack(),"outputs":outputs(),
        "speed8":speed8(),"gate8":gate8(),"cost8":cost8(),"test8":test8()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/brandguard"; os.makedirs(outd,exist_ok=True)
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
