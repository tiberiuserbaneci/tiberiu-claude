#!/usr/bin/env python3
# TIER 3 - ZERO TO FIRST DOLLAR, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
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

# 1. START - ascending zero-to-first-dollar path, 6 milestones, last node = $1 (glowing goal)
def start():
    pts=[(80,392,"$0","start here"),(210,332,"1","find leads"),(342,300,"2","write outreach"),
         (474,250,"3","send + follow"),(606,190,"4","book the call"),(748,112,"$1","first client")]
    line="M "+" L ".join(f"{x} {y}" for x,y,_,_ in pts)
    nodes=""
    for i,(x,y,lab,sub) in enumerate(pts):
        last=(i==len(pts)-1); r=44 if last else 26
        fill="url(#goal)" if last else "#2a2724"
        stroke=f"rgb({ACC})" if last else "rgba(212,162,127,.4)"
        glow='filter="url(#gg)"' if last else ""
        tcol="#1a0f0a" if last else "#e6dccf"; fs=26 if last else 18
        nodes+=(f'<g {glow}><circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/></g>'
          f'<text x="{x}" y="{y+(9 if last else 6)}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="{fs}" fill="{tcol}">{lab}</text>'
          f'<text x="{x}" y="{y+r+22}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8f8f85">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Zero to first dollar","THE PATH")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="goal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        <path d="{line}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 13"/>
        {nodes}
      </svg>
      {cap("not tips and hacks - a six-step path one operator runs end to end.")}</div>'''

# 2. FUNNEL - 4 narrowing trapezoid tiers, 200 sourced down to 1 paying client (bright base)
def funnel():
    rows=[("200","cold leads sourced",False),("40","replied to outreach",False),
          ("12","booked a call",False),("1","became a paying client",True)]
    w=[680,500,320,190,96]; cx=360; top=18; th=96; gap=16; svg=""
    for i,(n,lab,hot) in enumerate(rows):
        y0=top+i*(th+gap); y1=y0+th; tw=w[i]; bw=w[i+1]
        x0=cx-tw/2; x1=cx+tw/2; x2=cx+bw/2; x3=cx-bw/2
        grad="url(#hot)" if hot else "url(#cool)"
        svg+=(f'<polygon points="{x0:.0f},{y0} {x1:.0f},{y0} {x2:.0f},{y1} {x3:.0f},{y1}" fill="{grad}" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/>'
          f'<text x="{cx}" y="{y0+th/2-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="{40 if hot else 34}" fill="{"#1a0f0a" if hot else "#FAFAF7"}">{n}</text>'
          f'<text x="{cx}" y="{y0+th/2+24:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="{"rgba(26,15,10,.7)" if hot else "#a8a296"}">{lab}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("The first-client funnel","4 STAGES")}
      <svg width="720" height="474" viewBox="0 0 720 474" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="cool" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#241f1b"/></linearGradient>
          <linearGradient id="hot" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        </defs>
        {svg}
      </svg>
      {cap("200 sourced narrows to 1 paying client - the whole path on one screen.")}</div>'''

# 3. LEADS - node graph: company nodes converge through CORTEX into a ranked top-3 shortlist
def leads():
    comp=[("Northwind",118,66),("Globex",70,168),("Initech",150,268),("Acme",92,362)]
    hubx,huby=406,214; edges=""; nodes=""
    for nm,x,y in comp:
        edges+=f'<path d="M{x+54} {y} C282 {y},300 {huby},{hubx-70} {huby}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        nodes+=(f'<rect x="{x-54}" y="{y-24}" width="108" height="48" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c9c3b8">{nm}</text>')
    top=[("Northwind","hiring 3 ops","92"),("Globex Systems","raised in May","88"),("Initech","no AI layer","81")]
    rank=""
    for i,(nm,note,sc) in enumerate(top):
        oy=huby-102+i*70; best=(i==0)
        rank+=(f'<rect x="548" y="{oy}" width="216" height="58" rx="14" fill="{"url(#best)" if best else "#241f1b"}" stroke="{f"rgb({ACC})" if best else "rgba(255,255,255,.09)"}" stroke-width="1.5"/>'
          f'<text x="566" y="{oy+26}" font-family="DM Sans" font-weight="800" font-size="17" fill="{"#1a0f0a" if best else "#e6dccf"}">{nm}</text>'
          f'<text x="566" y="{oy+46}" font-family="DM Mono" font-size="12" fill="{"rgba(26,15,10,.7)" if best else "#8f8f85"}">{note}</text>'
          f'<text x="746" y="{oy+37}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="22" fill="{"#1a0f0a" if best else f"rgb({ACC})"}">{sc}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ranked by who will buy","CORTEX")}
      <svg width="800" height="440" viewBox="0 0 800 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <linearGradient id="best" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#hg)"><circle cx="{hubx}" cy="{huby}" r="62" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">CORTEX</text>
        <text x="{hubx}" y="{huby+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">scores fit</text>
        <path d="M{hubx+64} {huby} H548" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 11" stroke-linecap="round"/>
        {rank}
      </svg>
      {cap("fit plus buying signals, ranked - you skip the tire-kickers.")}</div>'''

# 4. OUTREACH - isometric stack of personalised message drafts, each in your voice
def outreach():
    msgs=[("to: ops@northwind","Saw you are hiring 3 ops roles..."),
          ("to: cfo@globex","Congrats on the May raise..."),
          ("to: ceo@initech","No AI layer yet - a 12 min fix...")]
    cards=""
    for i,(hdr,body) in enumerate(msgs):
        y=i*138
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:580px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 32px 46px rgba(0,0,0,.58), inset 0 2px 2px rgba(255,255,255,.1)">'
          f'<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">{hdr}</span>'
          f'<span style="display:flex;align-items:center;gap:6px;font-family:DM Mono;font-size:12px;color:#8f8f85"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>your voice</span></div>'
          f'<div style="font-family:DM Sans;font-weight:600;font-size:19px;color:#FAFAF7;margin-top:8px">{body}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Every message, personalised","SPECTER")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-8deg);width:580px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:404px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">3 drafts &#8594; you approve</div></div></div>
      {cap("cold emails and follow-ups written per lead - you just tap approve.")}</div>'''

# 5. PRICE - IVORY gauge: outreach cost near-zero, an SDR seat as the expensive old way
def price():
    cx,cy,R=300,250,170
    def pt(t,rad=R):
        a=math.radians(180-180*t); return (cx+rad*math.cos(a), cy-rad*math.sin(a))
    frac=0.10
    ax0,ay0=pt(0.0); ax1,ay1=pt(1.0); fx,fy=pt(frac); nx,ny=pt(frac,R-42)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {htitle("Your outreach costs cents","PAY PER TOKEN","#2a2016")}
      <div style="display:flex;align-items:center;gap:30px">
        <svg width="600" height="300" viewBox="0 0 600 300" style="flex-shrink:0">
          <path d="M{ax0:.0f} {ay0:.0f} A{R} {R} 0 0 1 {ax1:.0f} {ay1:.0f}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="26" stroke-linecap="round"/>
          <path d="M{ax0:.0f} {ay0:.0f} A{R} {R} 0 0 1 {fx:.0f} {fy:.0f}" fill="none" stroke="#96562d" stroke-width="26" stroke-linecap="round"/>
          <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="6" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="12" fill="#2a2016"/>
          <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="62" fill="#2a2016">3&#162;</text>
          <text x="{cx}" y="{cy-24}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="#96562d">PER 100 EMAILS</text>
        </svg>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.55);border-left:4px solid #96562d;border-radius:12px;padding:16px 18px">
            <div style="font-family:DM Mono;font-size:13px;color:#8a745a;letter-spacing:.06em">THE OLD WAY</div>
            <div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#2a2016;margin-top:4px">$4,000<span style="font-size:18px;font-weight:700;color:#8a745a">/mo</span></div>
            <div style="font-family:DM Sans;font-size:15px;color:#5a4634">one junior SDR, one seat</div>
          </div>
          <div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#2a2016;margin-top:18px;line-height:1.3">Same output.<br>Cents, not a salary.</div>
        </div>
      </div>
      {cap("pay for the tokens you use - your first dollar is not gated behind a hire.","#8a745a")}</div>'''

# 6. REPLIES - dot field of 240 first touches, a handful lit = warm replies today
def replies():
    cols,rown=24,10; cell,gap=22,5
    lit={17,52,88,131,170,205,228}; dots=""
    for i in range(cols*rown):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rown*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:50px;color:#FAFAF7">240</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#c9a583;margin-left:10px">first touches, sent</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">7 warm replies</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("hundreds sent overnight, a handful reply - your first real conversations.")}</div>'''

# 7. SYSTEM - radial hub: one operator (YOU) wiring CORTEX / SPECTER / STRIKER / MEMORY / GATE
def system():
    cx,cy,R=306,222,152
    sat=[("CORTEX","finds leads",-90),("SPECTER","writes outreach",-18),("STRIKER","books calls",54),
         ("MEMORY","remembers all",126),("GATE","your tap",198)]
    lines="";nodes=""
    for nm,role,a in sat:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a)); gate=(nm=="GATE")
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<rect x="{x-64:.0f}" y="{y-30:.0f}" width="128" height="60" rx="15" fill="#241f1a" stroke="{f"rgb({ACC})" if gate else "rgba(255,255,255,.12)"}" stroke-width="{2 if gate else 1.5}"/>'
          f'<text x="{x:.0f}" y="{y-5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="{f"rgb({ACC})" if gate else "#e6dccf"}">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Sans" font-size="13" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One operator, one engine","THE SYSTEM")}
      <svg width="612" height="460" viewBox="0 0 612 460" style="display:block;margin:0 auto">
        <defs><radialGradient id="you" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="yg" x="-100%" y="-100%" width="300%" height="300%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}
        <g filter="url(#yg)"><circle cx="{cx}" cy="{cy}" r="70" fill="url(#you)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">YOU</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one login</text>
        {nodes}
      </svg>
      {cap("no team to hire - CORTEX, SPECTER and STRIKER run under your tap.")}</div>'''

# 8. FIRSTDOLLAR - IVORY timeline: two weeks of milestones ending in a $1 goal flag
def firstdollar():
    events=[("Day 1","system live",0.05),("Day 3","first reply",0.28),("Day 7","first call",0.54),
            ("Day 12","proposal sent",0.78),("Day 14","first client",1.0)]
    x0,x1,yl=76,684,168; line=f'<line x1="{x0}" y1="{yl}" x2="{x1}" y2="{yl}" stroke="#96562d" stroke-width="4" stroke-linecap="round"/>'
    marks=""
    for lab,sub,t in events:
        x=x0+(x1-x0)*t; last=(t==1.0); r=30 if last else 12
        marks+=(f'<circle cx="{x:.0f}" cy="{yl}" r="{r}" fill="{"url(#flag)" if last else "#fdfbf6"}" stroke="#96562d" stroke-width="3"/>'
          + (f'<text x="{x:.0f}" y="{yl+9}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#1a0f0a">$1</text>' if last else "")
          + f'<text x="{x:.0f}" y="{yl-r-32:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#96562d">{lab}</text>'
          + f'<text x="{x:.0f}" y="{yl-r-13:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#2a2016">{sub}</text>'
          + (f'<text x="{x:.0f}" y="{yl+r+28:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8a745a">revenue in</text>' if last else ""))
    return f'''<div style="width:900px;{CARDIV};padding:40px 42px 36px">
      {htitle("Two weeks to first dollar","THE TIMELINE","#2a2016")}
      <svg width="760" height="300" viewBox="0 0 760 300" style="display:block;margin:0 auto">
        <defs><radialGradient id="flag" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#96562d"/></radialGradient></defs>
        {line}{marks}
      </svg>
      {cap("a booked call becomes a signed client - real revenue, a team of one.","#8a745a")}</div>'''

PANELS={"start":start(),"funnel":funnel(),"leads":leads(),"outreach":outreach(),
        "price":price(),"replies":replies(),"system":system(),"firstdollar":firstdollar()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2sharethishelp"; os.makedirs(outd,exist_ok=True)
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
