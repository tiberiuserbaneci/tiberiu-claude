#!/usr/bin/env python3
# TIER 3 - THE 5AM SHIFT, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded
# scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CLOCKIN - analog night clock (left) + a scheduled wake-list (right). The shift starts overnight,
# nobody set an alarm - each agent wakes on its own scheduled tick.
def clockin():
    cx,cy,r=175,205,132
    ticks=""
    for h in range(12):
        a=math.radians(h*30-90); x1=cx+(r-4)*math.cos(a); y1=cy+(r-4)*math.sin(a)
        x2=cx+(r-18)*math.cos(a); y2=cy+(r-18)*math.sin(a)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="{3 if h%3==0 else 1.6}"/>'
    # hands at ~03:00 (deep night)
    ha=math.radians(3*30-90); ma=math.radians(-90)
    hx=cx+66*math.cos(ha); hy=cy+66*math.sin(ha); mx=cx+96*math.cos(ma); my=cy+96*math.sin(ma)
    rows=[("02:00","CORTEX","scans overnight signals"),
          ("03:15","CORTEX","triages inbox + movers"),
          ("04:30","PULSE","drafts today's content"),
          ("05:45","AMPLIFY","stages the digest")]
    rh=""
    for t,ag,job in rows:
        rh+=(f'<div style="display:flex;align-items:center;gap:16px;border-left:3px solid rgb({ACC});padding:11px 0 11px 18px;margin-bottom:12px">'
             f'<span style="font-family:DM Mono;font-weight:500;font-size:20px;color:rgb({ACC});width:66px;flex-shrink:0">{t}</span>'
             f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{ag}</div>'
             f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85">{job}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <svg width="360" height="420" viewBox="0 0 360 420">
        <defs><radialGradient id="face" cx="40%" cy="34%"><stop offset="0%" stop-color="#26221e"/><stop offset="100%" stop-color="#151311"/></radialGradient>
        <filter id="cg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.28"/></filter></defs>
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#face)" stroke="rgba(212,162,127,.35)" stroke-width="2"/></g>
        {ticks}
        <path d="M{cx-20} {cy-88} a30 30 0 1 0 26 44 a24 24 0 1 1 -26 -44Z" fill="rgba(212,162,127,.5)"/>
        <line x1="{cx}" y1="{cy}" x2="{mx:.0f}" y2="{my:.0f}" stroke="#e6d6c2" stroke-width="4" stroke-linecap="round"/>
        <line x1="{cx}" y1="{cy}" x2="{hx:.0f}" y2="{hy:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/>
        <text x="{cx}" y="{cy+118}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".18em" fill="#8f8f85">NIGHT SHIFT</text>
      </svg>
      <div style="flex:1">
        {htitle("Wakes on schedule","03:00 LOCAL")}
        {rh}
        {cap("research, triage and drafting wake on the clock, not on willpower.")}
      </div></div>'''

# 2. TRENDS - ranked overnight movers with score bars, sorted, weighed against your ICP
def trends():
    rows=[("Northwind Robotics","hiring 3 AE roles",94),
          ("Globex Systems","raised $4M seed",89),
          ("Initech","new VP of Sales",83),
          ("Hooli","pricing page relaunch",77),
          ("Vandelay Inc","posted an RFP",71)]
    body=""
    for i,(nm,sig,sc) in enumerate(rows):
        w=int(300*sc/100)
        body+=(f'<div style="display:flex;align-items:center;gap:18px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
               f'<span style="font-family:DM Mono;font-size:15px;color:#6f6a60;width:24px;flex-shrink:0">{i+1:02d}</span>'
               f'<div style="width:250px;flex-shrink:0"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div>'
               f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85">{sig}</div></div>'
               f'<div style="flex:1;height:14px;background:rgba(255,255,255,.06);border-radius:7px;overflow:hidden">'
               f'<div style="width:{w}px;height:100%;background:linear-gradient(90deg,#8a4c2c,rgb({ACC}));border-radius:7px;box-shadow:0 0 14px rgba({ACC},.4)"></div></div>'
               f'<span style="font-family:DM Sans;font-weight:900;font-size:26px;color:rgb({ACC});width:52px;text-align:right;flex-shrink:0">{sc}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Overnight movers, scored","23 SCANNED")}
      <div style="font-family:DM Mono;font-size:13px;color:#8f8f85;margin-bottom:6px">TOP 5, RANKED AGAINST YOUR ICP &middot; FIT SCORE / 100</div>
      {body}
      {cap("every signal in your niche, weighed against your ICP before sunrise.")}</div>'''

# 3. DRAFTED - IVORY day-calendar: today's slots pre-filled in your voice, parked for your tap
def drafted():
    slots=[("09:00","LinkedIn post","Why I killed nine tools","parked",True),
           ("11:30","Newsletter","The 5am shift","parked",True),
           ("14:00","X thread","Cents, not seats","draft",False),
           ("16:00","Reply pack","12 warm comments","parked",True)]
    rows=""
    for t,kind,title,status,ok in slots:
        pill=(f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:{"#96562d" if ok else "#a08a68"};'
              f'background:{"rgba(150,86,45,.12)" if ok else "rgba(160,138,104,.14)"};padding:5px 12px;border-radius:999px">{status}</span>')
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;margin-bottom:14px">'
               f'<span style="font-family:DM Mono;font-weight:500;font-size:18px;color:#8a745a;width:56px;flex-shrink:0">{t}</span>'
               f'<div style="flex:1;background:rgba(255,255,255,.55);border-left:4px solid #96562d;border-radius:12px;padding:14px 18px;display:flex;align-items:center;gap:16px">'
               f'<div style="flex:1"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#a08a68">{kind.upper()}</div>'
               f'<div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#2a2016">{title}</div></div>{pill}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      {htitle_iv("Today's slots, filled","CONTENT CALENDAR")}
      {rows}
      <div style="display:inline-flex;align-items:center;gap:8px;margin-top:2px;background:rgba(150,86,45,.10);padding:8px 16px;border-radius:999px">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>
        <span style="font-family:DM Sans;font-weight:700;font-size:15px;color:#96562d">98% voice match, banned words enforced</span></div>
      {cap("your calendar, filled in your voice, ranked by your bar, parked for your tap.","#8a745a")}</div>'''

# 4. BUILTFLOW - horizontal pipeline graph: yesterday's cursed manual job wired into one flow
def builtflow():
    W,H=820,300
    steps=[("pull 40 leads",70),("enrich",250),("score vs ICP",430),("draft outreach",610),("queued",760)]
    nodes=""; edges=""; cy=150
    for i,(nm,x) in enumerate(steps):
        w=150 if i<4 else 96
        if i>0:
            px=steps[i-1][1]+ (150 if i-1<4 else 96)/2
            edges+=f'<path d="M{px:.0f} {cy} C{(px+x)/2:.0f} {cy},{(px+x)/2:.0f} {cy},{x-w/2:.0f} {cy}" fill="none" stroke="rgb({ACC})" stroke-width="4" filter="url(#eg)"/>'
        fill="url(#last)" if i==4 else "url(#nd)"
        nodes+=(f'<rect x="{x-w/2:.0f}" y="{cy-38}" width="{w}" height="76" rx="16" fill="{fill}" stroke="rgba(212,162,127,{0.9 if i==4 else 0.28})" stroke-width="{2.5 if i==4 else 1.5}"/>'
                f'<text x="{x:.0f}" y="{cy+6}" text-anchor="middle" font-family="DM Sans" font-weight="{900 if i==4 else 700}" font-size="16" fill="{"#1a0f0a" if i==4 else "#e6e0d4"}">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 32px">
      {htitle("Friction became a flow","BUILT 04:30")}
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:6px">
        <span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba({RED},.7)">yesterday, by hand &middot; 40 min every morning</span></div>
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><linearGradient id="nd" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <radialGradient id="last" cx="40%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4c2c"/></radialGradient>
        <filter id="eg" x="-20%" y="-60%" width="140%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}</svg>
      <div style="display:inline-flex;align-items:center;gap:10px;background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.3);border-radius:999px;padding:9px 18px;margin-top:4px">
        <span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.8)"></span>
        <span style="font-family:DM Sans;font-weight:800;font-size:16px;color:#FAFAF7">now one flow &middot; runs in 20 seconds</span></div>
      {cap("the repeated job you cursed at 16:00 became a flow by 06:00.")}</div>'''

# 5. DIGEST10 - dashboard grid: the whole company on one page (done / parked / waiting / suggested)
def digest10():
    cells=""
    data=[("DONE","14",["12 follow-ups sent","2 flows run"]),
          ("PARKED","6",["await your tap","3 posts, 3 emails"]),
          ("WAITING","3",["external replies due","2 nudges queued"]),
          ("SUGGESTED","4",["next moves ranked","1 flagged urgent"])]
    for lbl,n,items in data:
        li="".join(f'<div style="display:flex;align-items:center;gap:9px;margin-top:7px"><span style="width:5px;height:5px;border-radius:50%;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:15px;color:#c4beb2">{x}</span></div>' for x in items)
        cells+=(f'<div style="background:linear-gradient(158deg,#302c28,#211e1b);border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:20px 22px;box-shadow:inset 0 2px 2px rgba(255,255,255,.06)">'
                f'<div style="display:flex;align-items:baseline;justify-content:space-between"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{lbl}</span>'
                f'<span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7;line-height:1">{n}</span></div>{li}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 32px">
      {htitle("Your company on one page","06:55 DIGEST")}
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">{cells}</div>
      {cap("done, parked, waiting, suggested - your whole company on one screen.")}</div>'''

# 6. WALKIN - isometric stack of staged work, ready the moment you walk in
def walkin():
    steps=[("APPROVE","3 SPECTER sequences, ready to send",0),
           ("BRIEF","2 call briefs, prospects researched",1),
           ("DECIDE","Vandelay RFP: pricing to sign off",2)]
    cards=""
    for lbl,sub,i in steps:
        y=i*130
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">{i+1}</div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{lbl}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The work is staged","READY AT 07:00")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:130px;top:398px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">the day is already moving</div></div></div>
      {cap("two calls, three approvals, one judgement call - staged before you sat down.")}</div>'''

# 7. COST10 - IVORY gauge: the night bills in cents, next to the expensive human alternative
def cost10():
    r=78; circ=2*math.pi*r; pct=6; dash=circ*pct/100
    comp=[("A human ops hire","$6,200 / mo",RED,True),
          ("An overnight freelancer","$40 / task","150,90,45",False),
          ("Ultron night shift","31c / night","150,86,45",False)]
    rc=""
    for nm,val,col,bad in comp:
        strike="text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6);" if bad else ""
        big=(nm=="Ultron night shift")
        rc+=(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(150,120,80,.18)">'
             f'<span style="font-family:DM Sans;font-weight:{800 if big else 500};font-size:{19 if big else 17}px;color:{"#96562d" if big else "#5a4634"}">{nm}</span>'
             f'<span style="font-family:DM Sans;font-weight:900;font-size:{26 if big else 20}px;color:rgb({col});{strike}">{val}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      {htitle_iv("The night bills in cents","PER NIGHT")}
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0;position:relative;width:200px;height:200px">
          <svg width="200" height="200" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="16"/>
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="#96562d" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 100 100)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:46px;color:#2a2016;line-height:1">31c</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d;margin-top:2px">for the whole night</span></div></div>
        <div style="flex:1">{rc}</div>
      </div>
      {cap("no overtime, no burnout, no monday mood - pay-per-token, cents a night.","#8a745a")}</div>'''

# 8. FLIP10 - radial hub: the 5am team, every role already staffed by an agent
def flip10():
    cx,cy=410,230
    roles=[("CORTEX","research",-90),("PULSE","content",-18),("AMPLIFY","publishing",54),("SPECTER","outbound",126),("SENTINEL","code",198)]
    lines=""; nodes=""
    for nm,role,a in roles:
        x=cx+168*math.cos(math.radians(a)); y=cy+168*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(212,162,127,.5)" stroke-width="1.5"/>'
                f'<circle cx="{x:.0f}" cy="{y-14:.0f}" r="5" fill="rgb({ACC})" filter="url(#nb)"/>'
                f'<text x="{x:.0f}" y="{y+2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#e6e0d4">{nm}</text>'
                f'<text x="{x:.0f}" y="{y+20:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 32px">
      {htitle("The 5am team exists","5 / 5 STAFFED")}
      <svg width="820" height="460" viewBox="0 0 820 460" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter>
        <filter id="nb" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {lines}
        <g filter="url(#cg2)"><circle cx="{cx}" cy="{cy}" r="86" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">5AM</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">TEAM</text>
        {nodes}</svg>
      {cap("the 5am team exists. yours is just not hired yet.")}</div>'''

PANELS={"clockin":clockin(),"trends":trends(),"drafted":drafted(),"builtflow":builtflow(),
        "digest10":digest10(),"walkin":walkin(),"cost10":cost10(),"flip10":flip10()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/fiveam"; os.makedirs(outd,exist_ok=True)
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
