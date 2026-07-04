#!/usr/bin/env python3
# TIER 3 - THE SMMA CONTENT AGENCY, built to the WIRE-ITS-EYES bar: each of 8 panels is a UNIQUE
# hand-built coded scene (gauge, radial roster, bezier intake, iso production stack, scheduling grid,
# ivory ledger report, split-margin, funnel+gate) filling a clean rounded card. Warm palette only.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tc=None):
    tc=tc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CEILING - a capacity gauge pinned in the red: by hand an agency caps out at ~4 clients.
def ceiling():
    cx,cy,R=306,308,222
    def pt(t,rad=R):
        a=math.radians(t); return cx-rad*math.cos(a), cy-rad*math.sin(a)
    ex,ey=pt(0); rx,ry=pt(180)
    fx,fy=pt(170)  # needle target - almost the full sweep = maxed
    ticks=""
    for t in range(0,181,30):
        x1,y1=pt(t,R+4); x2,y2=pt(t,R-30)
        col=f"rgb({RED})" if t>=120 else "rgba(250,250,247,.30)"
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="3"/>'
    nx,ny=pt(170,R-52)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Content is what caps you","CAPACITY")}
      <svg width="612" height="360" viewBox="0 0 612 360" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="fill" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#7a4326"/><stop offset="62%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="rgb({RED})"/></linearGradient>
          <filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({RED})" flood-opacity="0.55"/></filter>
        </defs>
        <path d="M{rx:.0f} {ry:.0f} A{R} {R} 0 0 1 {ex:.0f} {ey:.0f}" fill="none" stroke="#2a2724" stroke-width="34" stroke-linecap="round"/>
        <path d="M{rx:.0f} {ry:.0f} A{R} {R} 0 0 1 {fx:.0f} {fy:.0f}" fill="none" stroke="url(#fill)" stroke-width="34" stroke-linecap="round"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({RED})" stroke-width="7" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#1a1816" stroke="rgb({RED})" stroke-width="3"/>
        <text x="{cx}" y="{cy-92}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="76" fill="#FAFAF7">4</text>
        <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".14em" fill="#8f8f85">CLIENTS BY HAND</text>
        <text x="{ex-4:.0f}" y="{ey+34:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({RED})">MAXED</text>
      </svg>
      {cap("every retainer wants weekly posts. you grind them by hand and growth stops.")}</div>'''

# 2. ROSTER - radial hub-and-spokes: the agency core feeds many client workspaces, all shipping.
def roster():
    cx,cy=306,244; R=196
    clients=["Northwind","Lumen","Vertex","Cava","Rook","Bloom","Atlas","Nova"]
    spokes=""; nodes=""
    n=len(clients)
    for i,nm in enumerate(clients):
        a=math.radians(-90+ i*360/n)
        x=cx+R*math.cos(a); y=cy+R*math.sin(a)
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(212,162,127,.42)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y-14:.0f}" r="4.5" fill="rgb({ACC})" filter="url(#bg)"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#e6ded0">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+22:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#8f8f85">12 posts/mo</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One agency, eight brands","THE ROSTER")}
      <svg width="612" height="490" viewBox="0 0 612 490" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter>
        <filter id="bg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {spokes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">AGENCY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">8 workspaces</text>
        {nodes}
      </svg>
      {cap("each client is a workspace with its own brand, memory and voice inside ultron.")}</div>'''

# 3. INTAKE - bezier flow: brand inputs converge into one saved client profile (CORTEX).
def intake():
    W,H=820,440
    src=[("brand voice",92),("past posts",192),("offer + ICP",292),("visual style",392)]
    edges=""; nodes=""
    hubx,huby=628,242
    for nm,y in src:
        mx=(190+hubx)/2
        edges+=f'<path d="M200 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-72} {huby}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=(f'<rect x="40" y="{y-27}" width="160" height="54" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="120" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:40px 40px 34px">
      {htitle("New client, profiled in one pass","CORTEX INTAKE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="ph" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="pg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#pg)"><circle cx="{hubx}" cy="{huby}" r="74" fill="url(#ph)"/></g>
        <text x="{hubx}" y="{huby-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">PROFILE</text>
        <text x="{hubx}" y="{huby+16}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#3a2010">saved to vault</text>
        <g transform="translate({hubx-16},{huby+92})"><rect x="0" y="8" width="32" height="24" rx="4" fill="none" stroke="rgb({ACC})" stroke-width="2.6"/><path d="M6 8 V3 a10 10 0 0 1 20 0 v5" fill="none" stroke="rgb({ACC})" stroke-width="2.6"/></g>
      </svg>
      {cap("cortex reads their brand, posts, offer and icp into one profile - once.")}</div>'''

# 4. PRODUCTION - isometric stack of finished post cards, each in a different client's voice (PULSE).
def production():
    rows=[("Lumen Skincare","5-slide carousel","in their voice"),
          ("Vertex Gym","hook + caption set","in their voice"),
          ("Rook Legal","3 short posts","in their voice")]
    cards=""
    for i,(a,b,tag) in enumerate(rows):
        y=i*146
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:20px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">
          <div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.36);
            display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:24px;color:rgb({ACC})">{a[0]}</div>
          <div style="flex:1"><div style="font-family:'DM Sans';font-weight:800;font-size:23px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;font-family:'DM Mono';font-size:11px;letter-spacing:.06em;color:rgb({ACC});background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.3);padding:6px 12px;border-radius:999px">{tag}</div></div>'''
    return f'''<div style="width:900px;{CARD};padding:38px 44px 44px">
      {htitle("Posts written in each brand voice","PULSE")}
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:466px;position:relative">{cards}</div></div>
      {cap("pulse drafts carousels and captions per client, matched to their real voice.")}</div>'''

# 5. CALENDAR - dense weekly scheduling grid across channels (AMPLIFY).
def calendar():
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    chans=["LINKEDIN","TIKTOK","INSTAGR"]
    # per channel, per day: list of (client-initial, time)
    sched=[
      [[("N","9a")],[("L","1p")],[("V","9a"),("C","6p")],[("R","1p")],[("B","9a")],[("A","6p")],[("N","1p")]],
      [[("C","6p"),("A","1p")],[("N","7p")],[("L","6p")],[("V","7p"),("R","1p")],[("B","6p")],[("X","9a")],[("A","6p")]],
      [[("B","12p")],[("V","6p"),("N","9a")],[("R","1p")],[("L","6p")],[("A","12p")],[("C","6p")],[("N","9a"),("B","6p")]],
    ]
    def chip(ini,tm):
        return (f'<div style="display:flex;align-items:center;gap:5px;background:rgba(212,162,127,.13);border:1px solid rgba(212,162,127,.3);border-radius:7px;padding:3px 7px">'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:12px;color:rgb({ACC})">{ini}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:10px;color:#b6afa2">{tm}</span></div>')
    head='<div></div>'+''.join(f'<div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.08em;color:#8f8f85;text-align:center;padding-bottom:6px">{d}</div>' for d in days)
    rows=""
    for ci,ch in enumerate(chans):
        rows+=f'<div style="display:flex;align-items:center;font-family:\'DM Mono\';font-size:12px;letter-spacing:.08em;color:rgb({ACC})">{ch}</div>'
        for di in range(7):
            cell="".join(chip(i,t) for i,t in sched[ci][di])
            rows+=(f'<div style="background:#221f1b;border:1px solid rgba(255,255,255,.06);border-radius:11px;min-height:62px;'
              f'padding:8px;display:flex;flex-direction:column;gap:5px;align-items:flex-start;justify-content:center">{cell}</div>')
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("Scheduled across every channel","AMPLIFY")}
      <div style="display:grid;grid-template-columns:82px repeat(7,1fr);gap:8px;align-items:stretch">
        {head}{rows}
      </div>
      {cap("amplify queues each post per channel and time zone - a full week, per client.")}</div>'''

# 6. REPORT - IVORY monthly client report that writes and sends itself.
def report():
    metrics=[("Reach","128,400","+22%"),("Saves","1,940","+41%"),("Posts shipped","12","on time"),("Engagement","4.8%","+0.9")]
    rows=""
    for lab,val,dl in metrics:
        up = dl.startswith("+")
        arrow=(f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>' if up else '')
        rows+=(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:15px 4px;border-bottom:1px solid rgba(150,120,80,.18)">'
          f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:20px;color:#4a3f30">{lab}</span>'
          f'<div style="display:flex;align-items:baseline;gap:14px">'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:28px;color:#2a2016">{val}</span>'
          f'<span style="display:flex;align-items:center;gap:4px;font-family:\'DM Mono\';font-size:14px;color:#96562d;min-width:64px;justify-content:flex-end">{arrow}{dl}</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The monthly report writes itself","AUTO-SENT",ink="#2a2016",tc="#96562d")}
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px">
        <div style="display:flex;align-items:center;gap:14px">
          <div style="width:46px;height:46px;border-radius:12px;background:linear-gradient(160deg,#f6ecdc,#e2d2b8);border:1px solid rgba(150,120,80,.3);display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:22px;color:#96562d">L</div>
          <div><div style="font-family:'DM Sans';font-weight:800;font-size:22px;color:#2a2016">Lumen Skincare</div>
          <div style="font-family:'DM Mono';font-size:13px;color:#a08a68">June report</div></div></div>
        <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.06em;color:#96562d;background:rgba(150,90,45,.1);border:1px solid rgba(150,90,45,.28);padding:7px 13px;border-radius:999px">SENT JUL 1</div>
      </div>
      <div style="background:rgba(255,255,255,.5);border-radius:16px;padding:6px 20px 8px">{rows}</div>
      {cap("reach, saves and engagement per client, packaged and sent without you.","#8a745a")}</div>'''

# 7. MARGIN - split compare: the old stack cost (dollars) vs Ultron (cents), the kept margin.
def margin():
    def line(lab,val,c):
        return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
          f'<span style="font-family:\'DM Sans\';font-size:17px;color:#c9c3b8">{lab}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:{c}">{val}</span></div>')
    old=line("Graphic designer",f'<span style="color:rgb({RED})">$5,000/mo</span>',"#fff")+line("Scheduling tools","$200/mo","#e6ded0")+line("Your hours","40/week","#e6ded0")
    new=line("Content by PULSE","cents/post",f"rgb({ACC})")+line("Publishing by AMPLIFY","included",f"rgb({ACC})")+line("Your hours","minutes/day",f"rgb({ACC})")
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You bill thousands, it costs cents","THE MARGIN")}
      <div style="display:flex;gap:18px;align-items:stretch">
        <div style="flex:1;background:rgba(200,70,35,.06);border:1px solid rgba(200,70,35,.28);border-radius:18px;padding:18px 22px">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:rgb({RED});margin-bottom:6px">OLD STACK</div>
          {old}
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:rgb({RED});margin-top:14px">$5,200 + your time</div></div>
        <div style="display:flex;align-items:center;font-family:'DM Mono';font-size:15px;color:#8f8f85">vs</div>
        <div style="flex:1;background:rgba(212,162,127,.08);border:1px solid rgba(212,162,127,.34);border-radius:18px;padding:18px 22px;box-shadow:0 0 30px rgba(212,162,127,.12) inset">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:6px">ON ULTRON</div>
          {new}
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:rgb({ACC});margin-top:14px">~$30/mo in tokens</div></div>
      </div>
      <div style="margin-top:16px;background:linear-gradient(90deg,rgba(212,162,127,.18),rgba(212,162,127,.05));border:1px solid rgba(212,162,127,.34);border-radius:14px;padding:16px 22px;display:flex;align-items:baseline;justify-content:space-between">
        <span style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#FAFAF7">Kept on a $15k month</span>
        <span style="font-family:'DM Sans';font-weight:900;font-size:34px;color:rgb({ACC})">$14,970</span></div>
      {cap("a designer and a tool stack become cents per post - the margin is the moat.")}</div>'''

# 8. OPERATOR - client nodes funnel into one operator, then park at the HUMAN GATE before publish.
def operator():
    W,H=820,440
    nodes=[("Northwind",70),("Lumen",150),("Vertex",230),("Rook",310),("Bloom",390)]
    ox,oy=470,230
    left=""
    for nm,y in nodes:
        left+=(f'<path d="M148 {y} C300 {y},330 {oy},{ox-72} {oy}" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<rect x="34" y="{y-20}" width="114" height="40" rx="11" fill="#221f1b" stroke="rgba(255,255,255,.1)"/>'
          f'<text x="91" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten clients ship on your one tap","HUMAN GATE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="op" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="54%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {left}
        <g filter="url(#og)"><circle cx="{ox}" cy="{oy}" r="72" fill="url(#op)"/></g>
        <text x="{ox}" y="{oy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">OPERATOR</text>
        <text x="{ox}" y="{oy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">you</text>
        <path d="M{ox+74} {oy} H612" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="{oy-70}" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate({620+42},{oy-32})"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="{oy+96}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every post parks at the gate. you approve, ultron publishes across the roster.")}</div>'''

PANELS={"ceiling":ceiling(),"roster":roster(),"intake":intake(),"production":production(),
        "calendar":calendar(),"report":report(),"margin":margin(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src51"; os.makedirs(outd,exist_ok=True)
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
