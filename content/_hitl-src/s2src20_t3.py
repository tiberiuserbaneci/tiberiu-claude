#!/usr/bin/env python3
# TIER 3 - S2SRC20 "the content team" reframed to Ultron. Each panel a UNIQUE hand-built coded
# scene filling a clean rounded card (WIRE-ITS-EYES bar): title + one mono caption, no stat-chip
# strips, no clip-path cuts, no extruded walls. Warm palette only. Cents pricing.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. STACK - the brittle $2400 hand-glued team: scattered tool nodes, tangled criss-cross wiring,
#    one severed link in muted red, a big monthly-cost readout. (competitor cost, high $ allowed here)
def stack():
    nodes=[("n8n",150,110),("GPT-4o",360,80),("SerpAPI",600,120),("Webhook",120,300),
           ("Sheets",340,330),("Cron",560,320),("Zapier",700,230)]
    # tangled edges (deliberately crossing), plus one broken red link
    edges=[(0,1),(1,2),(0,4),(4,5),(1,5),(2,6),(3,4),(0,3),(5,6),(3,1)]
    pos={i:(x,y) for i,(_,x,y) in enumerate(nodes)}
    ep=""
    for k,(a,b) in enumerate(edges):
        ax,ay=pos[a]; bx,by=pos[b]; mx=(ax+bx)/2+((k%3)-1)*46; my=(ay+by)/2-((k%2)*40)
        ep+=f'<path d="M{ax} {ay} Q{mx:.0f} {my:.0f} {bx} {by}" fill="none" stroke="rgba(212,162,127,.22)" stroke-width="2"/>'
    # one severed link (Zapier -> Cron) in red
    zx,zy=pos[6]; cxx,cyy=pos[5]
    ep+=(f'<path d="M{zx} {zy} Q{(zx+cxx)/2:.0f} {(zy+cyy)/2-30:.0f} {cxx} {cyy}" fill="none" stroke="rgb({RED})" stroke-width="2.4" stroke-dasharray="5 7"/>'
         f'<line x1="{(zx+cxx)/2-11:.0f}" y1="{(zy+cyy)/2-24:.0f}" x2="{(zx+cxx)/2+11:.0f}" y2="{(zy+cyy)/2-2:.0f}" stroke="rgb({RED})" stroke-width="3"/>'
         f'<text x="{(zx+cxx)/2:.0f}" y="{(zy+cyy)/2-34:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({RED})">broken</text>')
    nd=""
    for nm,x,y in nodes:
        nd+=(f'<rect x="{x-52}" y="{y-22}" width="104" height="44" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.11)"/>'
             f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nine tools, taped together","GLUE STACK",tagc=f"rgb({RED})")}
      <div style="position:relative;height:436px">
        <svg width="820" height="410" viewBox="0 0 820 410" style="position:absolute;left:0;top:0">{ep}{nd}</svg>
        <div style="position:absolute;right:6px;bottom:2px;background:linear-gradient(158deg,#332320,#241715);border:1px solid rgba(200,70,35,.4);border-radius:18px;padding:16px 22px;box-shadow:0 20px 40px rgba(0,0,0,.5)">
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#f0c1b4;line-height:1">$2,400</div>
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({RED});margin-top:2px">PER MONTH TO MAINTAIN</div></div>
      </div>
      {cap("brittle wiring you rent by the month. one node dies and the whole team goes dark.")}</div>'''

# 2. TEAM - radial hub-and-spokes: ROUTER core, 7 named agents on a ring, the 3 content agents lit
def team():
    cx,cy,R=410,225,168
    agents=[("CORTEX",True),("PULSE",True),("AMPLIFY",True),("SPECTER",False),
            ("STRIKER",False),("SENTINEL",False),("COUNSEL",False)]
    spokes=""; nodes=""
    n=len(agents)
    for i,(nm,lit) in enumerate(agents):
        a=-90+i*(360/n); x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        col=f"rgb({ACC})" if lit else "rgba(212,162,127,.22)"; w=4 if lit else 2
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="{w}"/>'
        fill="#241f1a"; bd=f"rgb({ACC})" if lit else "rgba(255,255,255,.12)"
        tc="#FAFAF7" if lit else "#7a746a"
        glow=' filter="url(#ng)"' if lit else ''
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="{fill}" stroke="{bd}" stroke-width="2"{glow}/>'
                f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="{tc}">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one team","SHIPS WIRED")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="ng" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">the composer</text>
      </svg>
      {cap("cortex, pulse and amplify already know each other. no workflow to wire, none to maintain.")}</div>'''

# 3. ROUTER - one content job routed down 3 tier lanes, SMART lane lit/picked, cents on every lane
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","draft the piece","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
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
      {htitle("It picks the tier per turn","MODEL ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hb2" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <g filter="url(#hg2)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hb2)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:8px;top:298px;width:132px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">one content<br>job in</div>
        {cards}
      </div>
      {cap("cheapest tier that can actually do it - the whole team runs in cents, not a subscription.")}</div>'''

# 4. BRIEF - IVORY: 4 socratic question chips on the left funnel into ONE clean brief page (right)
def brief():
    qs=["who is it for?","the one insight?","the proof points?","the ask?"]
    W,H=760,430; bx,by=560,215
    edges=""; chips=""
    for i,q in enumerate(qs):
        y=70+i*100
        edges+=f'<path d="M310 {y} C430 {y},430 {by},{bx-14} {by}" fill="none" stroke="rgba(150,90,45,.42)" stroke-width="2.4"/>'
        chips+=(f'<g><rect x="20" y="{y-30}" width="290" height="60" rx="15" fill="rgba(255,255,255,.62)" stroke="rgba(150,110,70,.28)"/>'
                f'<circle cx="52" cy="{y}" r="8" fill="#96562d"/>'
                f'<text x="78" y="{y+6}" font-family="DM Sans" font-size="18" fill="#4a3a28">{q}</text></g>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("One idea becomes a brief","SOCRATIC",ink="#2a2016",tagc="#96562d")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="bs" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="rgba(120,90,55,.28)"/></filter></defs>
        {edges}{chips}
        <g filter="url(#bs)"><rect x="{bx}" y="{by-142}" width="176" height="284" rx="14" fill="#fffdf9" stroke="rgba(150,110,70,.3)"/></g>
        <rect x="{bx+22}" y="{by-116}" width="90" height="14" rx="7" fill="#96562d"/>
        {"".join(f'<rect x="{bx+22}" y="{by-84+i*26}" width="{132-(i%3)*22}" height="9" rx="4.5" fill="rgba(80,60,40,.28)"/>' for i in range(7))}
        <text x="{bx+88}" y="{by+126}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#96562d">BRIEF - 1 PAGE</text>
      </svg>
      {cap("it asks the sharp questions, then folds your answers into one brief ready to be written.","#8a745a")}</div>'''

# 5. RESEARCH - radar sweep of live web signals + a stack of dated, sourced receipt lines
def research():
    cx,cy,R=200,210,180
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (60,120,180))
    blips=[("funding",300,150),("hiring",120,92),("stack",205,160),("intent",44,116)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
             f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    recs=[("techcrunch.com","2026-06-30","funding"),("sec.gov","2026-06-28","filing"),("g2.com","2026-07-01","reviews")]
    rc=""
    for dom,date,note in recs:
        rc+=(f'<div style="display:flex;align-items:center;gap:14px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:14px;padding:12px 16px">'
             f'<div style="flex-shrink:0;width:34px;height:34px;border-radius:10px;background:linear-gradient(160deg,#4a423a,#2a2622);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:17px;color:rgb({ACC});border:1px solid rgba(255,255,255,.1)">{dom[0].upper()}</div>'
             f'<div style="flex:1;text-align:left"><div style="font-family:DM Mono;font-size:15px;color:#eae4d8">{dom}</div>'
             f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{note} &middot; {date}</div></div>'
             f'<svg width="22" height="22" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.16)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="400" height="400" viewBox="0 0 400 400">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(62)):.0f} {cy-R*math.cos(math.radians(62)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("Live web, every claim sourced","THIS MORNING")}
        <div style="display:flex;flex-direction:column;gap:10px">{rc}</div>
        {cap("real numbers pulled today - each one carries its own dated receipt before a word is drafted.")}
      </div></div>'''

# 6. VOICE - IVORY: style-match gauge ring + a sample line written in your voice
def voice():
    pct=98; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("It writes in your voice","VOICE MATCH",ink="#2a2016",tagc="#96562d")}
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:190px;height:190px">
          <svg width="190" height="190" viewBox="0 0 190 190">
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 95 95)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016">{pct}%</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">style match</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4">
            "I killed the $2400 stack last month. The team I kept did not have nine dashboards."</div>
          <div style="display:flex;gap:22px;margin-top:16px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["short lines","no hedging","your cadence"])}
          </div></div>
      </div>
      {cap("sampled from your real posts, banned words enforced on every draft.","#8a745a")}</div>'''

# 7. CHANNELS - isometric stack of channel-native output cards from one master piece
def channels():
    rows=[("LINKEDIN","dark infographic post","1080x1350"),
          ("X THREAD","7 posts, hook first","280 chars"),
          ("SHORT","30s script + captions","9:16"),
          ("NEWSLETTER","long-form, sectioned","1 issue")]
    cards=""
    for i,(nm,sub,fmt) in enumerate(rows):
        y=i*108
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;padding:18px 24px;box-shadow:0 30px 46px rgba(0,0,0,.58), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><span style="font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC})">{nm[0]}</span></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{sub}</div></div>'
          f'<div style="flex-shrink:0;font-family:DM Mono;font-size:12px;color:#c9c3b8;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.28);border-radius:9px;padding:6px 12px">{fmt}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("One piece, cut for each channel","NATIVE")}
      <div style="perspective:2200px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(15deg) rotateZ(-5deg);width:580px;height:432px;position:relative">{cards}</div></div>
      {cap("the same master idea reshaped for every feed - written once, formatted many ways.")}</div>'''

# 8. GATE - the ready-to-post queue held on the operator's reins, one lock = your tap
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing posts without you","HUMAN GATE")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="210" r="130" fill="url(#orb)"/></g>
        <text x="200" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="46" fill="#2a160c">12</text>
        <text x="200" y="232" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#2a160c">assets queued</text>
        <text x="200" y="262" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".1em">drafted &middot; scheduled</text>
        <path d="M334 210 H610" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="140" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,178)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("the team drafts and schedules everything, then parks every send for one human approval.")}</div>'''

PANELS={"stack":stack(),"team":team(),"router":router(),"brief":brief(),
        "research":research(),"voice":voice(),"channels":channels(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src20"; os.makedirs(outd,exist_ok=True)
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
