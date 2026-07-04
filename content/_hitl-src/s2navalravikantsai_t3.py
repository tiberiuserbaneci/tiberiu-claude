#!/usr/bin/env python3
# TIER 3 - THE NEW LEVERAGE, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Frame: Naval's four leverages (labor/capital/code/media); reframe: agents are the new, permissionless
# leverage - one operator gets code+media+labor at cents, no team. Operator IS the leverage.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None):
    tc=tagc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. FOURWAYS - leverage-type comparison: 4 stacked rows, each classic leverage with the gate it
# used to demand (payroll / a check / a dev team / a following), a red LOCKED marker on every one.
def fourways():
    rows=[("01","LABOR","hire and manage a team","a payroll"),
          ("02","CAPITAL","raise it from investors","a check"),
          ("03","CODE","recruit engineers to build","a dev team"),
          ("04","MEDIA","grow an audience for years","a following")]
    items=""
    for idx,nm,desc,need in rows:
        items+=(f'<div style="display:flex;align-items:center;gap:20px;background:linear-gradient(160deg,#302c28,#211e1a);'
          f'border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:16px 22px;'
          f'box-shadow:0 14px 26px rgba(0,0,0,.4), inset 0 2px 2px rgba(255,255,255,.06)">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(212,162,127,.12);'
          f'border:1px solid rgba(212,162,127,.32);display:flex;align-items:center;justify-content:center;'
          f'font-family:DM Mono;font-weight:500;font-size:16px;color:rgb({ACC})">{idx}</div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:23px;letter-spacing:.02em;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#9a9488;margin-top:1px">{desc}</div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center;gap:9px;background:rgba(200,70,35,.10);'
          f'border:1px solid rgba(200,70,35,.4);border-radius:10px;padding:8px 13px">'
          f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb(200,70,35)" stroke-width="2.4">'
          f'<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'
          f'<span style="font-family:DM Mono;font-size:13px;color:#c85a3a">needs {need}</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The old four were gatekept","4 LEVERAGES")}
      <div style="display:flex;flex-direction:column;gap:14px">{items}</div>
      {cap("labor, capital, code, media - each one needed something a solo founder did not have.")}</div>'''

# 2. AGENTS - bezier flow: one prompt -> a router hub -> three leverage outputs (code, media, labor).
# The agents ARE the new leverage; permissionless, no team behind them.
def agents():
    W,H=820,440
    inx,iny=70,220; hubx,huby=360,220
    outs=[("CODE","Sentinel ships",96),("MEDIA","Pulse writes",220),("LABOR","Specter sends",344)]
    ox=590
    edges=f'<path d="M{inx+150} {iny} C260 {iny},280 {huby},{hubx-66} {huby}" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="3"/>'
    cards=""
    for nm,who,y in outs:
        edges+=f'<path d="M{hubx+66} {huby} C480 {huby},{ox-40} {y},{ox} {y}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.6"/>'
        cards+=(f'<g><rect x="{ox}" y="{y-38}" width="200" height="76" rx="16" fill="url(#och)" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>'
          f'<text x="{ox+22}" y="{y-6}" font-family="DM Sans" font-weight="900" font-size="21" fill="#FAFAF7">{nm}</text>'
          f'<text x="{ox+22}" y="{y+18}" font-family="DM Mono" font-size="13" fill="rgb({ACC})">{who}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Agents are the leverage","THE FIFTH")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <linearGradient id="och" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {edges}
        <rect x="{inx}" y="{iny-38}" width="150" height="76" rx="16" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>
        <text x="{inx+75}" y="{iny-4}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#e6dccf">one prompt</text>
        <text x="{inx+75}" y="{iny+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">you type</text>
        <g filter="url(#hg)"><circle cx="{hubx}" cy="{huby}" r="66" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROSTER</text>
        <text x="{hubx}" y="{huby+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">7 agents</text>
        {cards}
      </svg>
      {cap("one operator routes to a roster - code, media and labor leverage, no headcount.")}</div>'''

# 3. MULTIPLIER - IVORY semicircular MULTIPLIER gauge, needle pinned near 9x. One operator = a
# nine-person output. Distinct from the dark gate gauge: ivory, a real needle, a 1x..10x scale.
def multiplier():
    cx,cy,R=310,300,206
    def pt(a,r=R): return (cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))
    x0,y0=pt(180); x1,y1=pt(0)
    v=9; ang=180-(v-1)/9*180; fx,fy=pt(ang)
    ticks=""
    for a in range(180,-1,-18):
        ix,iy=pt(a,R-18); ox,oy=pt(a,R)
        ticks+=f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="rgba(150,90,45,.4)" stroke-width="3"/>'
    lab=""
    for t,a in [("1x",180),("5x",90),("10x",0)]:
        lx,ly=pt(a,R-46)
        lab+=f'<text x="{lx:.0f}" y="{ly+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#a08a68">{t}</text>'
    nx,ny=pt(ang,R-34)
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 30px;text-align:center">
      {htitle("One operator, a team's output","MULTIPLIER","#2a2016","#96562d")}
      <svg width="620" height="356" viewBox="0 0 620 356" style="display:block;margin:0 auto">
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="#e2d3ba" stroke-width="24" stroke-linecap="round"/>
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {fx:.0f} {fy:.0f}" fill="none" stroke="#96562d" stroke-width="24" stroke-linecap="round"/>
        {ticks}{lab}
        <text x="{cx}" y="182" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="76" fill="#2a2016">9x</text>
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#5a4130" stroke-width="6" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#fdfbf6" stroke="#96562d" stroke-width="4"/>
      </svg>
      <div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016;margin-top:2px">one login covers a nine-person team</div>
      {cap("the operator is the leverage - one seat produces what a whole team used to.","#8a745a")}</div>'''

# 4. STACK - dark isometric stack: the three permissionless leverages stacked under you, each owned
# by a named agent. Code / media / labor, no team to hire.
def stack():
    rows=[("CODE","Sentinel ships the product","SHIPS"),
          ("MEDIA","Pulse writes the content","POSTS"),
          ("LABOR","Specter runs the outreach","SENDS")]
    cards=""
    for i,(a,b,tag) in enumerate(rows):
        y=i*138
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.15);border-radius:18px;padding:20px 24px;box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:900;font-size:24px;letter-spacing:.02em;color:#FAFAF7">{a}</div><div style="font-family:DM Sans;font-size:15px;color:#a8a296;margin-top:2px">{b}</div></div>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:8px;padding:5px 10px">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Three leverages, one stack","UNDER YOU")}
      <div style="perspective:2000px;height:490px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-9deg);width:580px;height:436px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:412px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">No team hired &#10003;</div></div></div>
      {cap("code, media and labor, each owned by an agent - stacked, not staffed.")}</div>'''

# 5. MARKET - dark radar sweep of live market signals, ranked, with a first-to-move readout.
def market():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("Stack",210,168),("Intent",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    read="".join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:14px"><span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba(212,162,127,.7)"></span><span style="font-family:DM Sans;font-size:18px;color:#d9d5cc">{nm} moved</span></div>' for nm,_,_ in blips)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It moved first","THE EDGE")}
        {read}
        {cap("funding, hiring, stack, intent - a one-person company that moves before the crowd.")}
      </div></div>'''

# 6. OUTPUT - dark dot field: by hand a solo founder manages a few touches; with agents, hundreds
# the same afternoon, at cents each.
def output():
    cols,rowsn=46,17
    lit={38,127,209,301,388,470,555,640,733,812,690,150,420}
    cell=13; gap=3
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgba(212,162,127,.16)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    hdr=('<div style="display:flex;align-items:stretch;gap:16px;margin-bottom:18px">'
      '<div style="flex:0 0 auto;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.16);border-radius:14px;padding:12px 20px">'
      '<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#8f8f85">6</div>'
      '<div style="font-family:DM Mono;font-size:12px;color:#7a7468">a day, by hand</div></div>'
      f'<div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:14px;padding:12px 20px;box-shadow:0 0 22px rgba(212,162,127,.22)">'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7">240</div>'
      f'<div style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">this afternoon, solo</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Volume one person could not hit","THE VOLUME")}
      {hdr}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("outreach, follow-ups and posts by hand cap out fast. agents run them at cents each.")}</div>'''

# 7. ROSTER - dark radial hub-and-spokes: seven named agents orbit one glowing OPERATOR core that
# holds the shared memory. Every send waits for the human tap (the gate is woven in).
def roster():
    cx,cy=410,215; R=170
    spokes=[("CORTEX",-90),("SPECTER",-38),("STRIKER",14),("PULSE",66),("SENTINEL",128),("AMPLIFY",190),("COUNSEL",244)]
    sp=""
    for nm,a in spokes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        sp+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#221f1b" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="none" stroke="rgba(212,162,127,.25)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".02em" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one memory","THE ROSTER")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="core7" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg7" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {sp}
        <g filter="url(#cg7)"><circle cx="{cx}" cy="{cy}" r="80" fill="url(#core7)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">OPERATOR</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one memory</text>
      </svg>
      {cap("all seven draw from one core, and every external move waits for your tap.")}</div>'''

# 8. SHIFT - IVORY horizontal timeline: THEN (recruit, onboard, payroll, thousands/mo) collapses into
# NOW (one deploy, cents per run). The leverage that needed a team now runs on a card.
def shift():
    then=[("Recruit",96),("Onboard",236),("Payroll",376)]
    railY=214
    nodes=""
    for nm,x in then:
        nodes+=(f'<circle cx="{x}" cy="{railY}" r="15" fill="#f3ead9" stroke="#c9a578" stroke-width="3"/>'
          f'<circle cx="{x}" cy="{railY}" r="5" fill="#a08a68"/>'
          f'<text x="{x}" y="{railY-30}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#8a745a">{nm}</text>')
    nowx=620
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 30px">
      {htitle("From payroll to per-token","THE SHIFT","#2a2016","#96562d")}
      <svg width="740" height="330" viewBox="0 0 740 330" style="display:block;margin:0 auto">
        <text x="60" y="80" font-family="DM Mono" font-size="14" letter-spacing=".16em" fill="#a08a68">THEN</text>
        <text x="{nowx-16}" y="80" font-family="DM Mono" font-size="14" letter-spacing=".16em" fill="#96562d">NOW</text>
        <line x1="60" y1="{railY}" x2="470" y2="{railY}" stroke="#d9c4a4" stroke-width="4" stroke-dasharray="3 10" stroke-linecap="round"/>
        {nodes}
        <text x="266" y="270" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#8a745a">thousands / month</text>
        <path d="M486 {railY} h56" stroke="#96562d" stroke-width="4" stroke-linecap="round"/>
        <path d="M536 {railY-9} l12 9 l-12 9" fill="none" stroke="#96562d" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="{nowx}" cy="{railY}" r="52" fill="none" stroke="#96562d" stroke-width="3"/>
        <circle cx="{nowx}" cy="{railY}" r="42" fill="#96562d"/>
        <text x="{nowx}" y="{railY-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#fdfbf6">Deploy</text>
        <text x="{nowx}" y="{railY+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#f2e3cf">one login</text>
        <text x="{nowx}" y="270" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a2016">cents / run</text>
      </svg>
      {cap("the leverage that used to need payroll now runs per token - you pay the work, not seats.","#8a745a")}</div>'''

PANELS={"fourways":fourways(),"agents":agents(),"multiplier":multiplier(),"stack":stack(),
        "market":market(),"output":output(),"roster":roster(),"shift":shift()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2navalravikantsai"; os.makedirs(outd,exist_ok=True)
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
