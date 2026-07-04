#!/usr/bin/env python3
# TIER 3 - THE CAROUSEL CODE, rebuilt to the WIRE-ITS-EYES bar: each of the 8 panels is a UNIQUE
# hand-built coded scene (filmstrip / grid / iso stack / timeline / dot field / gauge / node graph /
# radial hub) filling a clean rounded card, htitle + one mono caption. NO generic stat-chip strips,
# NO clip-path cuts, NO extruded walls. Warm palette, 2 ivory panels. Founder-facing.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; IVA="#96562d"; BAD="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagcol=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagcol}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:18px">{t}</div>'

# 1. myth7 - GRID: a 2x2 gallery of ever-more-polished templates, every one with a dead-flat metric
def myth7():
    cells=[("Gradient hero",'<div style="height:32px;background:linear-gradient(90deg,rgba(212,162,127,.55),rgba(212,162,127,.12))"></div>'),
           ("Icon set",''.join(f'<div style="width:16px;height:16px;border-radius:5px;background:rgba(212,162,127,.30)"></div>' for _ in range(6))),
           ("Serif display",'<span style="font-family:\'DM Sans\';font-weight:900;font-size:30px;color:rgba(212,162,127,.55)">Aa</span>'),
           ("3D mockups",'<div style="width:70px;height:44px;border-radius:6px;border:2px solid rgba(212,162,127,.4);box-shadow:0 8px 14px rgba(0,0,0,.5)"></div>')]
    def cell(name,inner,i):
        head=(f'<div style="height:60px;border-radius:11px;overflow:hidden;background:#17150f;border:1px solid rgba(255,255,255,.06);display:flex;align-items:center;justify-content:center;gap:6px;flex-wrap:wrap;padding:8px">{inner}</div>') if i in (1,2,3) else (f'<div style="height:60px;border-radius:11px;overflow:hidden;background:#17150f;border:1px solid rgba(255,255,255,.06)">{inner}<div style="padding:9px"><div style="height:6px;width:70%;background:rgba(255,255,255,.14);border-radius:3px;margin-bottom:6px"></div><div style="height:6px;width:45%;background:rgba(255,255,255,.09);border-radius:3px"></div></div></div>')
        return (f'<div style="background:linear-gradient(160deg,#2b2723,#211e1a);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:16px 18px;box-shadow:inset 0 2px 2px rgba(255,255,255,.05)">'
          f'{head}'
          f'<div style="display:flex;align-items:center;justify-content:space-between;margin-top:14px">'
          f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.06em;color:#cfc9bd">{name}</span>'
          f'<div style="display:flex;align-items:center;gap:9px">'
          f'<svg width="52" height="16" viewBox="0 0 52 16"><line x1="2" y1="9" x2="50" y2="9" stroke="rgba({BAD},.85)" stroke-width="2.4" stroke-dasharray="1 5" stroke-linecap="round"/></svg>'
          f'<span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:rgb({BAD})">FLAT</span></div></div></div>')
    grid=''.join(cell(n,inr,i) for i,(n,inr) in enumerate(cells))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It was never the pretty template","8 MONTHS")}
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">{grid}</div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:20px;background:rgba(212,162,127,.06);border:1px solid rgba(212,162,127,.18);border-radius:14px;padding:14px 20px">
        <span style="font-family:'DM Sans';font-weight:700;font-size:17px;color:#e2dccf">60+ posts, polish climbing every week</span>
        <span style="font-family:'DM Sans';font-weight:900;font-size:22px;color:rgb({BAD})">0 lift</span></div>
      {cap("sophistication and polish did not move a single metric.")}</div>'''

# 2. pat1 - FILMSTRIP: cover frame lit, one arrow to the next slide, the rest dim
def pat1():
    W,H=780,360
    strip=f'<rect x="0" y="46" width="{W}" height="268" rx="20" fill="#1b1815" stroke="rgba(255,255,255,.06)"/>'
    holes=""
    x=22
    while x<W-14:
        holes+=f'<rect x="{x}" y="58" width="20" height="14" rx="3" fill="rgba(250,250,247,.12)"/><rect x="{x}" y="288" width="20" height="14" rx="3" fill="rgba(250,250,247,.12)"/>'
        x+=46
    fx=[22,232,430,600]; fy=94; fw=[168,150,150,150]; fh=172
    frames=""
    # cover (lit)
    frames+=(f'<rect x="{fx[0]}" y="{fy}" width="{fw[0]}" height="{fh}" rx="14" fill="#241f1a" stroke="rgb({ACC})" stroke-width="2.5" filter="url(#glowc)"/>'
      f'<rect x="{fx[0]+14}" y="{fy+16}" width="{fw[0]-28}" height="46" rx="8" fill="url(#covg)"/>'
      f'<rect x="{fx[0]+14}" y="{fy+74}" width="{fw[0]-52}" height="9" rx="4" fill="rgba(255,255,255,.20)"/>'
      f'<rect x="{fx[0]+14}" y="{fy+92}" width="{fw[0]-72}" height="9" rx="4" fill="rgba(255,255,255,.12)"/>'
      f'<text x="{fx[0]+fw[0]//2}" y="{fy+fh-16}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">COVER</text>')
    labs=["SLIDE 2","SLIDE 3","SLIDE 4"]
    for i in range(1,4):
        op=0.55 if i==1 else (0.34 if i==2 else 0.2)
        frames+=(f'<g opacity="{op}"><rect x="{fx[i]}" y="{fy}" width="{fw[i]}" height="{fh}" rx="14" fill="#242019" stroke="rgba(255,255,255,.10)"/>'
          f'<rect x="{fx[i]+14}" y="{fy+18}" width="{fw[i]-28}" height="9" rx="4" fill="rgba(255,255,255,.16)"/>'
          f'<rect x="{fx[i]+14}" y="{fy+36}" width="{fw[i]-50}" height="9" rx="4" fill="rgba(255,255,255,.10)"/>'
          f'<rect x="{fx[i]+14}" y="{fy+54}" width="{fw[i]-38}" height="9" rx="4" fill="rgba(255,255,255,.08)"/>'
          f'<text x="{fx[i]+fw[i]//2}" y="{fy+fh-16}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".12em" fill="#8f8f85">{labs[i-1]}</text></g>')
    arrow=f'<g filter="url(#glowc)"><path d="M198 {fy+fh//2} h26" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/><path d="M218 {fy+fh//2-9} l10 9 l-10 9" fill="none" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></g>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The cover sells the swipe","SLIDE 1 &rarr; 2")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="covg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4a2c"/></linearGradient>
        <filter id="glowc" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {strip}{holes}{frames}{arrow}
      </svg>
      {cap("one promise, one visual, zero cleverness. its only job is the next slide.")}</div>'''

# 3. pat2 - ISO STACK (IVORY): a stack of pages each carrying ONE beat, a rejected two-beat ghost behind
def pat2():
    beats=[("The hook","slide 1"),("The proof","slide 2"),("The turn","slide 3"),("The ask","slide 4")]
    cards=""
    for i,(lab,role) in enumerate(beats):
        y=i*112
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:520px;background:#ffffff;border:1px solid rgba(120,95,60,.16);border-radius:16px;padding:20px 24px;box-shadow:0 26px 40px rgba(120,95,60,.22), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:22px">'
          f'<div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:linear-gradient(160deg,#f0d9c2,#d8a37c);border:1px solid rgba(150,90,45,.3);display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:20px;color:#5a3418">{i+1}</div>'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Sans\';font-weight:800;font-size:22px;color:#2a2016">{lab}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8a745a">{role}</div></div>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:{IVA}">1 IDEA</span></div>')
    ghost=(f'<div style="position:absolute;left:64px;top:-70px;width:520px;background:rgba(200,70,35,.06);border:1px dashed rgba({BAD},.5);border-radius:16px;padding:14px 24px;display:flex;align-items:center;gap:16px;opacity:.9">'
      f'<span style="font-family:\'DM Sans\';font-size:17px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba({BAD},.8)">two ideas on one page</span>'
      f'<span style="margin-left:auto;font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:rgb({BAD})">CUT</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("One beat per page","ONE BEAT",ink="#2a2016",tagcol=IVA)}
      <div style="perspective:1900px;height:520px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(19deg) rotateZ(-8deg);width:584px;height:480px;position:relative">{ghost}{cards}</div></div>
      {cap("two ideas on a slide is one idea too many. the swipe rhythm is the retention.","#8a745a")}</div>'''

# 4. pat3 - TIMELINE: 7 slide nodes, slide 2 opens a loop that slide 7 closes (an arc over the line)
def pat3():
    W,H=760,340
    bx0,bx1,by=54,706,232
    n=7; step=(bx1-bx0)/(n-1)
    xs=[bx0+i*step for i in range(n)]
    base=f'<line x1="{bx0}" y1="{by}" x2="{bx1}" y2="{by}" stroke="rgba(212,162,127,.28)" stroke-width="3"/>'
    nodes=""
    for i,x in enumerate(xs):
        big=(i==1 or i==6)
        r=17 if big else 9
        fill=f"rgb({ACC})" if big else "rgba(212,162,127,.35)"
        flt='filter="url(#gb)"' if big else ""
        nodes+=f'<circle cx="{x:.0f}" cy="{by}" r="{r}" fill="{fill}" {flt}/>'
        nodes+=f'<text x="{x:.0f}" y="{by+ (46 if not big else 52)}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="{"#e2dccf" if big else "#8f8f85"}">{i+1}</text>'
    # loop arc from slide2 to slide7
    x2,x7=xs[1],xs[6]; topy=88
    arc=(f'<path d="M{x2:.0f} {by-18} C{x2:.0f} {topy},{x7:.0f} {topy},{x7:.0f} {by-18}" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>'
      f'<text x="{(x2+x7)/2:.0f}" y="{topy-8}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb({ACC})">tension held across the swipe</text>')
    tags=(f'<text x="{x2:.0f}" y="{by+72}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">opens loop</text>'
      f'<text x="{x7:.0f}" y="{by+72}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">closes loop</text>'
      f'<text x="{xs[0]:.0f}" y="{by+72}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">cover</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Slide two decides if they finish","OPEN LOOP")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="gb" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {base}{arc}{nodes}{tags}
      </svg>
      {cap("the swipe-off page carries the tension: open a loop the last page closes.")}</div>'''

# 5. pat4 - DOT FIELD: a lit contiguous block (the reference page saves) inside a field of dim impressions
def pat4():
    cols,rows=40,17
    cell,gap=15,3
    # contiguous lit block = the one reference page that gets saved
    lit=set()
    for r in range(5,10):
        for c in range(24,32):
            lit.add(r*cols+c)
    dots=""
    for i in range(cols*rows):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rows*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:50px;color:#FAFAF7;line-height:1">0.90%</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:18px;color:#c9a583;margin-left:12px">saved, the reference page</span></div>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:rgb({ACC})">vs 0.02% elsewhere</span></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="display:flex;gap:26px;margin-top:16px">
        {"".join(f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.06em;color:#c9c3b8">&middot; {x}</span>' for x in ["the list","the test","the map"])}</div>
      {cap("one page they will need again. saves are the algorithm.")}</div>'''

# 6. grade7 - GAUGE (IVORY): a 5/5 ring + 30s dial, five review boxes all checked
def grade7():
    r=74; circ=2*math.pi*r
    checks=["Cover sells the swipe","One beat per page","Slide two opens a loop","A save-worthy reference page","One clear CTA"]
    rows="".join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:13px"><svg width="22" height="22" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(150,86,45,.12)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="{IVA}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:DM Sans;font-size:18px;color:#2a2016">{c}</span></div>' for c in checks)
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("I review posts against the code","30 SECONDS",ink="#2a2016",tagcol=IVA)}
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0;position:relative;width:196px;height:196px">
          <svg width="196" height="196" viewBox="0 0 196 196">
            <circle cx="98" cy="98" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="15"/>
            <circle cx="98" cy="98" r="{r}" fill="none" stroke="{IVA}" stroke-width="15" stroke-linecap="round" stroke-dasharray="{circ:.0f} {circ:.0f}" transform="rotate(-90 98 98)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016">5/5</span>
            <span style="font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:{IVA}">30s pass</span></div></div>
        <div style="flex:1">{rows}</div>
      </div>
      {cap("cover promise, beat rhythm, loop tension, save page, one cta.","#8a745a")}</div>'''

# 7. desk7 - NODE GRAPH: PULSE hub fans out into the five patterns, stamped on every draft
def desk7():
    W,H=780,440
    hubx,hy=150,220
    pats=[("COVER",60),("BEAT",150),("LOOP",240),("SAVE",330),("CTA",420)]
    nx=520
    edges=""; nodes=""
    for nm,y in pats:
        edges+=f'<path d="M{hubx+66} {hy} C330 {hy},{nx-120} {y},{nx-34} {y}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{nx}" cy="{y}" r="30" fill="#241f1a" stroke="rgb({ACC})" stroke-width="2"/>'
          f'<text x="{nx}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".06em" fill="rgb({ACC})">{nm}</text>'
          f'<circle cx="{nx+50}" cy="{y}" r="6" fill="#c9a583"/>'
          f'<text x="{nx+66}" y="{y+5}" font-family="DM Sans" font-size="15" fill="#c9c3b8">stamped</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("PULSE builds to the code","AUTO-DRAFT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="ph" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="phg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}
        <g filter="url(#phg)"><circle cx="{hubx}" cy="{hy}" r="66" fill="url(#ph)"/></g>
        <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">PULSE</text>
        <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">content agent</text>
        {nodes}
      </svg>
      {cap("every deck it drafts carries the five patterns before i ever see it.")}</div>'''

# 8. payoff7 - RADIAL HUB: three inputs converge into one GROWTH core, the metrics follow
def payoff7():
    W,H=760,440
    cx,cy=430,225; R=112
    inputs=[("Same niche",210),("Same effort",150),("Patterned delivery",270)]
    spokes=""; labels=""
    for nm,a in inputs:
        x=cx+205*math.cos(math.radians(a)); y=cy+205*math.sin(math.radians(a))
        spokes+=f'<path d="M{x:.0f} {y:.0f} L{cx+ (R+8)*math.cos(math.radians(a)):.0f} {cy+(R+8)*math.sin(math.radians(a)):.0f}" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
        spokes+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})"/>'
        ty=y-18 if a==150 else y+30
        labels+=f'<text x="{x:.0f}" y="{ty:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#d9d5cc">{nm}</text>'
    # rising mini sparkline inside the orb
    spark='<polyline points="-46,26 -22,14 2,18 26,-8 48,-26" fill="none" stroke="#2a160c" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    upar=f'<path d="M{cx+150} {cy-40} l0 -70 M{cx+150-14} {cy-96} l14 -14 l14 14" fill="none" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><text x="{cx+150}" y="{cy-6}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">metrics</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Growth stopped being luck","CONSEQUENCE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="gro" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="54%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="grg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spokes}
        <g filter="url(#grg)"><circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#gro)"/></g>
        <g transform="translate({cx},{cy-6})">{spark}</g>
        <text x="{cx}" y="{cy+58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">GROWTH</text>
        {labels}{upar}
      </svg>
      {cap("same niche, same effort, patterned delivery. the metrics followed.")}</div>'''

PANELS={"myth7":myth7(),"pat1":pat1(),"pat2":pat2(),"pat3":pat3(),
        "pat4":pat4(),"grade7":grade7(),"desk7":desk7(),"payoff7":payoff7()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/carouselcode"; os.makedirs(outd,exist_ok=True)
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
