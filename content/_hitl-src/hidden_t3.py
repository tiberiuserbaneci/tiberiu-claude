#!/usr/bin/env python3
# TIER 3 - THE HIDDEN SKILLS, built to the WIRE-ITS-EYES bar: each of 8 panels is a UNIQUE
# hand-built coded scene filling a clean rounded card (gauge / proposal / ledger / redline /
# dot-field / node-graph / iso-stack / orbital-gate). htitle + one mono cap, no chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

def garc(cx,cy,R,f0,f1,n=44):
    return " ".join(f"{cx+R*math.cos(math.radians(180+180*f)):.1f},{cy+R*math.sin(math.radians(180+180*f)):.1f}"
                    for f in (f0+(f1-f0)*i/n for i in range(n+1)))

# 1. MYTH - GAUGE scene: two dials. re-wording pinned near empty (muted red), installing capability
# swept near full (accent). ticks + needles, the real skill curve.
def myth():
    def dial(cx,val,col,lab,sub):
        R=138; track=garc(cx,300,R,0,1); fill=garc(cx,300,R,0,val)
        na=math.radians(180+180*val); nx=cx+(R-30)*math.cos(na); ny=300+(R-30)*math.sin(na)
        ticks=""
        for i in range(11):
            a=math.radians(180+180*i/10)
            x0=cx+(R+9)*math.cos(a); y0=300+(R+9)*math.sin(a); x1=cx+(R+20)*math.cos(a); y1=300+(R+20)*math.sin(a)
            ticks+=f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke="rgba(250,250,247,.22)" stroke-width="2"/>'
        return (f'{ticks}'
          f'<polyline points="{track}" fill="none" stroke="rgba(250,250,247,.10)" stroke-width="20" stroke-linecap="round"/>'
          f'<polyline points="{fill}" fill="none" stroke="{col}" stroke-width="20" stroke-linecap="round" filter="url(#gl)"/>'
          f'<line x1="{cx}" y1="300" x2="{nx:.0f}" y2="{ny:.0f}" stroke="{col}" stroke-width="6" stroke-linecap="round"/>'
          f'<circle cx="{cx}" cy="300" r="12" fill="#231f1b" stroke="{col}" stroke-width="3"/>'
          f'<text x="{cx}" y="252" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">{lab}</text>'
          f'<text x="{cx}" y="336" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="{col}">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Re-wording is not a skill","THE REAL CURVE")}
      <svg width="820" height="392" viewBox="0 0 820 392" style="display:block;margin:0 auto">
        <defs><filter id="gl" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {dial(220,0.11,"rgb(200,70,35)","RE-WORD","same 1 trick, forever")}
        {dial(600,0.93,f"rgb({ACC})","INSTALL","capabilities that stay")}
        <line x1="410" y1="120" x2="410" y2="360" stroke="rgba(255,255,255,.08)" stroke-dasharray="4 8"/>
      </svg>
      {cap("prompting was the tutorial. operators install skills, they do not re-phrase.")}</div>'''

# 2. DECKS - PROPOSAL scene (IVORY): a white sheet that wrote itself, brand tokens top-right, three
# auto-filled sections, one highlighted price band the operator added.
def decks():
    tokens="".join(f'<span style="width:16px;height:16px;border-radius:5px;background:{c};display:inline-block;margin-left:6px;box-shadow:inset 0 1px 2px rgba(255,255,255,.5)"></span>' for c in ["#2a2016","#96562d","rgb(212,162,127)"])
    secs=[("SCOPE","3 services agents, deployed and tuned"),("TIMELINE","live in 9 days, weekly reviews"),("TEAM","1 operator + Ultron, no new hires")]
    rows=""
    for lab,line in secs:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;padding:13px 0;border-bottom:1px solid rgba(120,95,60,.14)">'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:12px;letter-spacing:.12em;color:#96562d;width:96px">{lab}</span>'
          f'<span style="font-family:\'DM Sans\';font-size:18px;color:#3a2f22">{line}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The proposal built itself","DRAFT &rarr; DECK","#2a2016","#96562d")}
      <div style="background:#fffdf9;border:1px solid rgba(120,95,60,.18);border-radius:20px;padding:26px 30px 28px;box-shadow:0 22px 40px rgba(120,95,60,.16), inset 0 2px 2px rgba(255,255,255,.9);border-left:6px solid #96562d">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px">
          <span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.2em;color:#a08a68">PROPOSAL</span>
          <span style="display:flex;align-items:center"><span style="font-family:\'DM Mono\';font-size:11px;color:#a08a68">your tokens</span>{tokens}</span></div>
        <div style="font-family:\'DM Sans\';font-weight:900;font-size:28px;color:#2a2016;margin-bottom:8px">Northwind Robotics</div>
        {rows}
        <div style="display:flex;align-items:center;justify-content:space-between;margin-top:18px;background:linear-gradient(160deg,#f6e6d6,#efd8c2);border:1.5px solid #96562d;border-radius:14px;padding:16px 22px">
          <div><div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:#96562d">INVESTMENT</div>
          <div style="font-family:\'DM Sans\';font-weight:900;font-size:34px;color:#2a2016;line-height:1.05">$9,000 <span style="font-size:18px;font-weight:700;color:#6a5238">/ mo</span></div></div>
          <span style="font-family:\'DM Sans\';font-weight:900;font-size:14px;color:#fffdf9;background:#96562d;padding:9px 18px;border-radius:999px;box-shadow:0 8px 16px rgba(150,86,45,.3)">I added this</span></div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:16px">
          <span style="width:22px;height:22px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#f0c49e,#96562d);flex-shrink:0"></span>
          <span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#a08a68">DRAFTED BY PULSE &middot; NORTHWIND ROBOTICS &middot; 2026</span></div>
      </div>
      {cap("client name in, structured deck out. in your tokens, your voice, your price.","#8a745a")}</div>'''

# 3. SHEETS - LEDGER scene: a spreadsheet window, gridded rows of live figures, one cell traced by a
# dotted connector to a floating source pill (every figure carries its origin).
def sheets():
    W,Hh=740,392
    rows=[("MRR","$42.1K","stripe.com",False),("Net new","$6.4K","stripe.com",False),
          ("Pipeline","$310K","hubspot.com",True),("Runway","14 mo","ledger.csv",False)]
    top=118; rh=62; body=""
    trace_y=top+2*rh+rh/2
    for i,(k,v,src,hot) in enumerate(rows):
        y=top+i*rh; bg="rgba(250,250,247,.05)" if i%2 else "rgba(250,250,247,.02)"
        body+=(f'<rect x="40" y="{y}" width="{W-80}" height="{rh}" fill="{bg}"/>'
          f'<text x="66" y="{y+38}" font-family="DM Sans" font-weight="600" font-size="19" fill="#cfc9bd">{k}</text>'
          f'<text x="300" y="{y+38}" font-family="DM Mono" font-weight="500" font-size="22" fill="{("rgb("+ACC+")") if hot else "#f2ecdf"}">{v}</text>'
          f'<g transform="translate(468,{y+18})"><rect x="0" y="0" width="196" height="28" rx="8" fill="rgba(212,162,127,.10)" stroke="rgba(212,162,127,.32)"/>'
          f'<text x="14" y="19" font-family="DM Mono" font-size="13" fill="#d9c3ac">{src}</text>'
          f'<circle cx="178" cy="14" r="7" fill="rgba(127,211,154,.16)"/><path d="M174 14 l3 3 l6 -7" fill="none" stroke="#7fd39a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></g>'
          f'<line x1="40" y1="{y+rh}" x2="{W-40}" y2="{y+rh}" stroke="rgba(255,255,255,.06)"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every figure traces","LIVE LEDGER")}
      <svg width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" style="display:block;margin:0 auto">
        <rect x="8" y="8" width="{W-16}" height="{Hh-16}" rx="18" fill="#17150f" stroke="rgba(255,255,255,.08)"/>
        <rect x="8" y="8" width="{W-16}" height="48" rx="18" fill="#221f18"/>
        <circle cx="34" cy="32" r="6" fill="#c84623"/><circle cx="56" cy="32" r="6" fill="rgb({ACC})"/><circle cx="78" cy="32" r="6" fill="#7fd39a"/>
        <text x="{W/2:.0f}" y="37" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#8f8f85">figures.xls</text>
        <line x1="284" y1="72" x2="284" y2="{top+4*rh:.0f}" stroke="rgba(255,255,255,.06)"/><line x1="452" y1="72" x2="452" y2="{top+4*rh:.0f}" stroke="rgba(255,255,255,.06)"/>
        <text x="66" y="98" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="#8f8f85">FIGURE</text>
        <text x="300" y="98" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="#8f8f85">VALUE</text>
        <text x="478" y="98" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="#8f8f85">TRACES TO</text>
        {body}
        <path d="M470 {trace_y:.0f} C520 {trace_y:.0f},560 350,600 350" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="2" stroke-dasharray="3 5"/>
        <g transform="translate(560,332)"><rect x="0" y="0" width="152" height="42" rx="10" fill="#241f19" stroke="rgb({ACC})" stroke-width="1.5"/>
        <text x="14" y="19" font-family="DM Mono" font-size="12" fill="rgb({ACC})">GET /invoices</text>
        <text x="14" y="34" font-family="DM Mono" font-size="11" fill="#8f8f85">hubspot &middot; 200 OK</text></g>
      </svg>
      {cap("live figures with the source attached, not screenshots of a spreadsheet.")}</div>'''

# 4. CONTRACTS - REDLINE doc (IVORY): an NDA page with struck clauses in muted red, inserted accent
# text, margin change-bars and RISK / OK flags. COUNSEL read it and marked it up.
def contracts():
    def clause(sec,title,old,new,risk):
        flagc="rgb(200,70,35)" if risk else "#5a8a5f"; flag="RISK" if risk else "OK"
        edited=bool(old)
        bar=f'<span style="position:absolute;left:0;top:6px;bottom:6px;width:4px;border-radius:2px;background:{"rgb(200,70,35)" if risk else "rgba(150,90,45,.35)"}"></span>' if edited else ''
        oldln=(f'<span style="font-family:\'DM Sans\';font-size:17px;color:#a06a5a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.75)">{old}</span> '
               f'<span style="font-family:\'DM Sans\';font-size:17px;font-weight:700;color:#96562d">{new}</span>') if edited else (
               f'<span style="font-family:\'DM Sans\';font-size:17px;color:#3a2f22">{new}</span>')
        return (f'<div style="position:relative;padding:11px 0 11px 18px;border-bottom:1px solid rgba(120,95,60,.13)">{bar}'
          f'<div style="display:flex;align-items:baseline;justify-content:space-between">'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#a08a68">{sec} &middot; {title}</span>'
          f'<span style="font-family:\'DM Mono\';font-weight:500;font-size:11px;letter-spacing:.12em;color:{flagc};border:1px solid {flagc};border-radius:6px;padding:2px 8px">{flag}</span></div>'
          f'<div style="margin-top:5px">{oldln}</div></div>')
    body=(clause("&sect;4","Term","perpetual","24 months",True)
        + clause("&sect;7","Liability","unlimited","capped at fees",True)
        + clause("&sect;9","Governing law","","Romania, as drafted",False)
        + clause("&sect;2","Definitions","","clean, no changes",False))
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The NDA came back redlined","COUNSEL","#2a2016","#96562d")}
      <div style="background:#fffdf9;border:1px solid rgba(120,95,60,.18);border-radius:20px;padding:24px 28px 26px;box-shadow:0 22px 40px rgba(120,95,60,.16), inset 0 2px 2px rgba(255,255,255,.9)">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px">
          <span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:#2a2016">Mutual NDA <span style="font-family:\'DM Mono\';font-size:14px;color:#96562d">v2</span></span>
          <span style="font-family:\'DM Mono\';font-size:12px;color:#a08a68">2 risk lines flagged</span></div>
        {body}
        <div style="display:flex;align-items:center;gap:10px;margin-top:16px">
          <svg width="30" height="30" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="none" stroke="#96562d" stroke-width="1.6"/><path d="M8 12l2.6 2.6L16 8.5" fill="none" stroke="#96562d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.1em;color:#96562d">REVIEWED BY COUNSEL &middot; READY FOR YOUR SIGN-OFF</span></div>
      </div>
      {cap("reads the NDA, flags the risk lines, drafts the redlines. you approve.","#8a745a")}</div>'''

# 5. VISUALS - DOT-FIELD scene: 822 component tiles, a contiguous lit block assembles into one site,
# the rest a dim inventory. distinct tile-grid, no rows/graph.
def visuals():
    cols,rowsn=28,24
    cell=13; gap=4
    lit=set()
    for r in range(6,18):
        for c in range(8,20): lit.add(r*cols+c)
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgba(250,250,247,.10)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Design has no queue","822 PARTS")}
      <div style="display:flex;align-items:center;gap:34px">
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="flex-shrink:0">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="flex:1">
        <div style="font-family:'DM Sans';font-weight:900;font-size:66px;color:#FAFAF7;line-height:1">822</div>
        <div style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-top:2px">Crescendo components</div>
        <div style="display:flex;flex-direction:column;gap:12px;margin-top:20px">
          {"".join(f'<div style="display:flex;align-items:center;gap:11px"><span style="width:11px;height:11px;border-radius:3px;background:rgb({ACC});box-shadow:0 0 10px rgba({ACC},.7);flex-shrink:0"></span><span style="font-family:DM Sans;font-size:17px;color:#d9d5cc">{t}</span></div>' for t in ["assembled into 1 on-brand site","posts, decks, covers from one kit","0 tickets in the design queue"])}
        </div>
      </div></div>
      {cap("822 parts snap into on-brand visuals and sites. no design queue.")}</div>'''

# 6. CONNECTORS - NODE GRAPH: a central actor hub, bezier edges reaching INTO four real tool tiles
# with an action verb on each. it acts inside the tools, not beside them.
def connectors():
    W,H=816,470; hx,hy=408,235
    apps=[("Mail","sent 12",150,104,'<path d="M-16 -11 h32 a3 3 0 0 1 3 3 v16 a3 3 0 0 1 -3 3 h-32 a3 3 0 0 1 -3 -3 v-16 a3 3 0 0 1 3 -3Z M-19 -8 L0 5 L19 -8" fill="none" stroke="rgb({A})" stroke-width="2.4"/>'),
          ("CRM","updated 40",666,104,'<rect x="-15" y="-13" width="30" height="26" rx="4" fill="none" stroke="rgb({A})" stroke-width="2.4"/><circle cx="-4" cy="-4" r="4" fill="rgb({A})"/><line x1="4" y1="-6" x2="11" y2="-6" stroke="rgb({A})" stroke-width="2.4"/><line x1="-11" y1="6" x2="11" y2="6" stroke="rgb({A})" stroke-width="2.4"/>'),
          ("Calendar","booked 3",150,366,'<rect x="-15" y="-12" width="30" height="26" rx="4" fill="none" stroke="rgb({A})" stroke-width="2.4"/><line x1="-15" y1="-4" x2="15" y2="-4" stroke="rgb({A})" stroke-width="2.4"/><line x1="-8" y1="-16" x2="-8" y2="-8" stroke="rgb({A})" stroke-width="2.4"/><line x1="8" y1="-16" x2="8" y2="-8" stroke="rgb({A})" stroke-width="2.4"/><circle cx="4" cy="6" r="3" fill="rgb({A})"/>'),
          ("Payments","charged",666,366,'<rect x="-16" y="-11" width="32" height="22" rx="4" fill="none" stroke="rgb({A})" stroke-width="2.4"/><line x1="-16" y1="-3" x2="16" y2="-3" stroke="rgb({A})" stroke-width="3.5"/><line x1="-10" y1="5" x2="-2" y2="5" stroke="rgb({A})" stroke-width="2.4"/>'),]
    edges=""; cards=""
    for nm,verb,x,y,ic in apps:
        sx=hx+(70 if x>hx else -70); sy=hy+(24 if y>hy else -24)
        mx=(sx+x)/2
        edges+=f'<path d="M{sx} {sy} C{mx:.0f} {sy},{mx:.0f} {y},{x} {y}" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="3" marker-end="url(#arr)"/>'
        icon=ic.replace("{A}",ACC)
        cards+=(f'<div style="position:absolute;left:{x-84}px;top:{y-52}px;width:168px;background:linear-gradient(160deg,#35302a,#221e1a);border:1.5px solid rgba(255,255,255,.12);border-radius:18px;padding:16px 18px;box-shadow:0 22px 38px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="display:flex;align-items:center;gap:12px"><svg width="30" height="30" viewBox="-20 -18 40 36">{icon}</svg>'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{nm}</span></div>'
          f'<div style="display:flex;align-items:center;gap:7px;margin-top:10px"><span style="width:8px;height:8px;border-radius:50%;background:#7fd39a;box-shadow:0 0 8px #7fd39a"></span>'
          f'<span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">{verb}</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It acts inside your tools","LIVE CONNECTORS")}
      <div style="position:relative;width:{W}px;height:{H}px;margin:0 auto">
        <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <marker id="arr" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="rgb({ACC})"/></marker>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          {edges}
          <g filter="url(#hg)"><rect x="{hx-72}" y="{hy-48}" width="144" height="96" rx="24" fill="url(#hub)"/></g>
          <text x="{hx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">IT ACTS</text>
          <text x="{hx}" y="{hy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">inside, not beside</text>
        </svg>
        {cards}
      </div>
      {cap("mail, crm, calendar, payments. it does the move, it does not draft it for you.")}</div>'''

# 7. RESULT - ISO CARD STACK: isometric stack of finished deliverables (each with a check + meta),
# a summary chip - answers are cheap, outputs are the product.
def result():
    steps=[("LANDING PAGE","shipped to main","live"),("ONBOARDING FLOW","6 emails, scheduled","sent"),
           ("PRICING SHEET","built in your tokens","saved")]
    cards=""
    for i,(nm,sub,tag) in enumerate(steps):
        y=i*138
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;padding:20px 24px;box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:52px;height:52px;border-radius:15px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.35);display:flex;align-items:center;justify-content:center"><svg width="28" height="28" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7">{nm}</div><div style="font-family:DM Sans;font-size:16px;color:#a8a296;margin-top:1px">{sub}</div></div>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:8px;padding:5px 11px">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Execution is the product","3 SHIPPED")}
      <div style="perspective:2000px;height:474px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:580px;height:432px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:398px;display:flex;gap:0;border-radius:999px;overflow:hidden;box-shadow:0 12px 24px rgba(0,0,0,.5)">
            <span style="font-family:DM Mono;font-size:14px;color:#8f8f85;background:#221f1b;padding:9px 16px">answers 0</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:15px;color:#1a0f0a;background:rgb({ACC});padding:9px 18px">outputs 3</span></div></div></div>
      {cap("files created, work automated, tasks finished. that is the difference.")}</div>'''

# 8. GATE - ORBITAL scene: full-capability orb, a dashed orbit ring holding 4 pending external
# actions, each paused; one lock; nothing sends until your tap.
def gate():
    cx,cy=408,236; Ro=176
    acts=[("send 12 emails",210),("post the update",300),("book 3 calls",30),("collect invoice",120)]
    ring=""
    for nm,a in acts:
        x=cx+Ro*math.cos(math.radians(a)); y=cy+Ro*math.sin(math.radians(a))
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.20)" stroke-width="1.5" stroke-dasharray="3 6"/>'
          f'<g transform="translate({x:.0f},{y:.0f})"><rect x="-92" y="-24" width="184" height="48" rx="14" fill="#221f1b" stroke="rgba(212,162,127,.32)" stroke-width="1.5"/>'
          f'<g transform="translate(-70,0)"><rect x="-7" y="-8" width="5" height="16" rx="2" fill="rgb({ACC})"/><rect x="3" y="-8" width="5" height="16" rx="2" fill="rgb({ACC})"/></g>'
          f'<text x="6" y="5" text-anchor="middle" font-family="DM Sans" font-weight="600" font-size="16" fill="#e2dccf">{nm}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Executes fast, sends on your tap","HUMAN GATE")}
      <svg width="816" height="474" viewBox="0 0 816 474" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{Ro}" fill="none" stroke="rgba(212,162,127,.22)" stroke-dasharray="2 10" stroke-linecap="round"/>
        {ring}
        <g filter="url(#og)"><circle cx="{cx}" cy="{cy}" r="86" fill="url(#orb)"/></g>
        <g transform="translate({cx-26},{cy-30})"><rect x="0" y="20" width="52" height="38" rx="8" fill="none" stroke="#2a160c" stroke-width="5"/><path d="M9 20 V9 a17 17 0 0 1 34 0 v11" fill="none" stroke="#2a160c" stroke-width="5"/></g>
        <text x="{cx}" y="{cy+52}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#2a160c">FULL POWER</text>
        <text x="{cx}" y="452" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">4 actions parked &middot; waiting for your tap</text>
      </svg>
      {cap("everything external parks first. you stay the only trigger.")}</div>'''

PANELS={"myth":myth(),"decks":decks(),"sheets":sheets(),"contracts":contracts(),
        "visuals":visuals(),"connectors":connectors(),"result":result(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/hidden"; os.makedirs(outd,exist_ok=True)
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
