#!/usr/bin/env python3
# TIER 3 - A SALES ORG, NOT A BOT, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one mono caption, NO generic stat-chip strips.
import importlib.util, os, math, random
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; IVACC="#96562d"; BAD="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IVACC}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. EVERYTHING - one overloaded bot node collapsing under a hundred tangled, half-frayed branches
def everything():
    random.seed(11)
    cx,cy=410,248; lines=""; dots=""
    for i in range(48):
        a=random.uniform(0,2*math.pi); r=random.uniform(130,300)
        x=cx+r*math.cos(a); y=cy+r*math.sin(a)*0.6
        mx=cx+(x-cx)*0.5+random.uniform(-70,70); my=cy+(y-cy)*0.5+random.uniform(-55,55)
        bad=(i%5==0)
        col=f"rgba({BAD},.72)" if bad else "rgba(212,162,127,.26)"
        w=2.6 if bad else 1.3; dash='stroke-dasharray="3 7"' if bad else ""
        lines+=f'<path d="M{cx} {cy} Q{mx:.0f} {my:.0f} {x:.0f} {y:.0f}" fill="none" stroke="{col}" stroke-width="{w}" {dash}/>'
        dc=f"rgb({BAD})" if bad else "rgba(212,162,127,.5)"
        dots+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{4.5 if bad else 3}" fill="{dc}"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One agent doing all","DOES NOTHING WELL")}
      <svg width="820" height="500" viewBox="0 0 820 500" style="display:block;margin:0 auto">
        <defs><radialGradient id="ov" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ovg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({BAD})" flood-opacity="0.45"/></filter></defs>
        {lines}{dots}
        <circle cx="{cx}" cy="{cy}" r="70" fill="none" stroke="rgba({BAD},.5)" stroke-width="2" stroke-dasharray="6 8"/>
        <g filter="url(#ovg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#ov)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">1 BOT</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010" letter-spacing=".08em">overloaded</text>
        <text x="{cx}" y="{cy+118}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({BAD})">100+ BRANCHES &middot; 0 DONE WELL</text>
      </svg>
      {cap("one automation, a hundred branches, every task half-finished.")}</div>'''

# 2. STRUCTURE - clean org-chart: chief on top, four desks, one specialist each
def structure():
    W,H=820,470
    desks=[("RESEARCH","CORTEX",110),("OUTREACH","SPECTER",300),("ENABLE","STRIKER",500),("REVOPS","AMPLIFY",700)]
    chx=410; chy=52; busy=176; deskY=214; specY=346
    conns=f'<line x1="{chx}" y1="{chy+56}" x2="{chx}" y2="{busy}" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
    conns+=f'<line x1="{desks[0][2]+70}" y1="{busy}" x2="{desks[-1][2]+70}" y2="{busy}" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
    boxes=""
    for nm,sp,x in desks:
        conns+=f'<line x1="{x+70}" y1="{busy}" x2="{x+70}" y2="{deskY}" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
        conns+=f'<line x1="{x+70}" y1="{deskY+82}" x2="{x+70}" y2="{specY}" stroke="rgba(255,255,255,.12)" stroke-width="2" stroke-dasharray="3 6"/>'
        boxes+=(f'<rect x="{x}" y="{deskY}" width="140" height="82" rx="16" fill="url(#dbg)" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{x+70}" y="{deskY+34}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({ACC})">{nm}</text>'
          f'<text x="{x+70}" y="{deskY+60}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#c9c3b8">desk</text>'
          f'<rect x="{x+14}" y="{specY}" width="112" height="52" rx="13" fill="#221f1b" stroke="rgba(255,255,255,.08)"/>'
          f'<circle cx="{x+34}" cy="{specY+26}" r="9" fill="rgb({ACC})"/>'
          f'<text x="{x+50}" y="{specY+31}" font-family="DM Sans" font-weight="800" font-size="14" fill="#e2dccf">{sp}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Real teams have structure","CHIEF &middot; DESKS &middot; SPECIALISTS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="dbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <radialGradient id="chg" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="chf" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {conns}
        <g filter="url(#chf)"><rect x="{chx-108}" y="{chy}" width="216" height="56" rx="16" fill="url(#chg)"/></g>
        <text x="{chx}" y="{chy+36}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a160c">CHIEF &middot; you</text>
        {boxes}
      </svg>
      {cap("chief, desks, specialists. sales ran this way for a century for a reason.")}</div>'''

# 3. RESEARCH - IVORY dossier: a scored prospect brief with intel rows + a fit gauge
def research():
    pct=92; r=70; circ=2*math.pi*r; dash=circ*pct/100
    rows=[("Hiring","3 ops roles this week"),("Funding","raised $4M in May"),("Stack","no AI layer yet"),("Fit","US, 2-50 staff, IT")]
    rowh=""
    for k,v in rows:
        rowh+=(f'<div style="display:flex;align-items:baseline;gap:14px;padding:11px 0;border-bottom:1px solid rgba(150,120,80,.18)">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.06em;color:{IVACC};width:78px;flex-shrink:0">{k}</span>'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:18px;color:#2a2016">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("Research: prospect intel","CORTEX")}
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:184px;height:184px">
          <svg width="184" height="184" viewBox="0 0 184 184">
            <circle cx="92" cy="92" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="92" cy="92" r="{r}" fill="none" stroke="{IVACC}" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 92 92)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016">{pct}</span>
            <span style="font-family:DM Mono;font-size:12px;color:{IVACC}">FIT SCORE</span></div></div>
        <div style="flex:1">
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016;margin-bottom:4px">Northwind Robotics</div>
          {rowh}</div>
      </div>
      {cap("profiled, scored and briefed before anyone writes a word.","#8a745a")}</div>'''

# 4. OUTREACH - three channel drafts stacked, each parked behind an amber tap-gate
def outreach():
    chans=[("EMAIL","Re: your 3 new ops hires -"),("LINKEDIN","Saw the $4M round. One line -"),("FOLLOW-UP","Circling back on the ops build -")]
    ICON={"EMAIL":'<rect x="2" y="5" width="26" height="18" rx="3" fill="none" stroke="rgb({A})" stroke-width="2.2"/><path d="M3 7l12 9 12-9" fill="none" stroke="rgb({A})" stroke-width="2.2"/>',
          "LINKEDIN":'<rect x="3" y="3" width="24" height="24" rx="4" fill="none" stroke="rgb({A})" stroke-width="2.2"/><rect x="8" y="12" width="3.4" height="9" fill="rgb({A})"/><circle cx="9.7" cy="8" r="2" fill="rgb({A})"/><path d="M15 21v-5a3 3 0 0 1 6 0v5" fill="none" stroke="rgb({A})" stroke-width="2.2"/>',
          "FOLLOW-UP":'<path d="M5 9h14a4 4 0 0 1 4 4 4 4 0 0 1-4 4H9l-5 4V9z" fill="none" stroke="rgb({A})" stroke-width="2.2"/>'}
    rows=""
    for nm,draft in chans:
        ic=ICON[nm].replace("{A}",ACC)
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(255,255,255,.09);border-radius:18px;padding:18px 20px;box-shadow:0 16px 30px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:13px;background:rgba(212,162,127,.13);border:1px solid rgba(212,162,127,.32);display:flex;align-items:center;justify-content:center"><svg width="28" height="28" viewBox="0 0 30 30">{ic}</svg></div>'
          f'<div style="flex:1;text-align:left"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:600;font-size:18px;color:#e6e1d6;margin-top:2px">{draft}</div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center;gap:8px;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.4);border-radius:999px;padding:8px 16px">'
          f'<svg width="16" height="16" viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="9" rx="2" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><path d="M8 11V8a4 4 0 0 1 8 0v3" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/></svg>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:rgb({ACC})">your tap</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Outreach: gated sends","SPECTER")}
      <div style="display:flex;flex-direction:column;gap:16px">{rows}</div>
      {cap("drafted per channel, in your voice, every send parked for your tap.")}</div>'''

# 5. ENABLE - IVORY: the paperwork nobody loves, checked off on time
def enable():
    tasks=[("Proposal drafted + sent","09:14 Tue"),("Discovery call booked","Thu 15:00"),
           ("Follow-up sequence queued","3 steps"),("NDA prefilled for review","ready")]
    items=""
    for t,when in tasks:
        items+=(f'<div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.55);border:1px solid rgba(150,120,80,.16);'
          f'border-radius:16px;padding:15px 18px;box-shadow:0 8px 16px rgba(120,95,60,.10)">'
          f'<div style="flex-shrink:0;width:34px;height:34px;border-radius:10px;background:{IVACC};display:flex;align-items:center;justify-content:center">'
          f'<svg width="20" height="20" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="#fdfbf6" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:19px;color:#2a2016">{t}</span>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:13px;color:{IVACC}">{when}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("Enablement: paperwork, done","ON TIME")}
      <div style="display:flex;flex-direction:column;gap:13px">{items}</div>
      {cap("proposals, scheduling, follow-ups: the work nobody loves, on time.","#8a745a")}</div>'''

# 6. REVOPS - horizontal funnel, stages narrowing, live counts + a clean-data readout
def revops():
    stages=[("New",240,660),("Replied",62,470),("Booked",18,300),("Won",5,150)]
    W,H=760,420; y=40; bars=""
    for nm,n,w in stages:
        x=(W-w)/2
        bars+=(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="66" rx="12" fill="url(#fb)" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x+22:.0f}" y="{y+42}" font-family="DM Mono" font-size="15" letter-spacing=".1em" fill="#e2dccf">{nm}</text>'
          f'<text x="{W-x-22:.0f}" y="{y+44}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="30" fill="rgb({ACC})">{n}</text>')
        y+=92
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("RevOps: the pipe stays true","PIPELINE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="fb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#211e1a"/></linearGradient></defs>
        {bars}
      </svg>
      <div style="display:flex;gap:12px;margin-top:6px">
        {"".join(f'<div style="flex:1;background:rgba(212,162,127,.08);border:1px solid rgba(212,162,127,.24);border-radius:12px;padding:11px 14px;text-align:center;font-family:DM Mono;font-size:13px;color:rgb({ACC})">{c}</div>' for c in ["stages move on replies","data stays clean","digests land daily"])}
      </div>
      {cap("the pipeline moves itself and the numbers you read are real.")}</div>'''

# 7. ONEJOB - the workforce grid: six specialists, one job each, mastered
def onejob():
    agents=[("CORTEX","research"),("SPECTER","outreach"),("STRIKER","deals"),
            ("AMPLIFY","publishing"),("COUNSEL","legal"),("SENTINEL","code")]
    tiles=""
    for nm,job in agents:
        tiles+=(f'<div style="background:linear-gradient(160deg,#312d28,#211e1a);border:1px solid rgba(255,255,255,.09);border-radius:18px;'
          f'padding:20px 20px 18px;box-shadow:0 14px 26px rgba(0,0,0,.42), inset 0 2px 2px rgba(255,255,255,.06)">'
          f'<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#FAFAF7">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.06em;color:#1a0f0a;background:rgb({ACC});border-radius:999px;padding:3px 9px">1 JOB</span></div>'
          f'<div style="font-family:DM Sans;font-weight:600;font-size:16px;color:#c9c3b8;margin-bottom:12px">{job}</div>'
          f'<div style="height:7px;border-radius:4px;background:rgba(255,255,255,.08);overflow:hidden"><div style="height:100%;width:100%;background:rgb({ACC})"></div></div>'
          f'<div style="font-family:DM Mono;font-size:11px;color:#8f8f85;margin-top:6px">mastered</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One job per agent","A WORKFORCE")}
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">{tiles}</div>
      {cap("six specialists, one job each, done extremely well - not a chatbot with a hundred to-dos.")}</div>'''

# 8. CHIEF - the pyramid: you at the apex, one tap, the org running underneath
def chief():
    W,H=760,440
    tiers=[("apex",290,66,"YOU","1 tap a day",True),
           ("desks",470,60,"4 DESK LEADS","research &middot; outreach &middot; enable &middot; revops",False),
           ("base",650,60,"THE SPECIALISTS","seven agents, always on",False)]
    y=30; shapes=""
    prev=None
    for name,w,h,lab,sub,apex in tiers:
        x=(W-w)/2; cxm=W/2
        if apex:
            shapes+=(f'<path d="M{cxm} {y} L{x+w} {y+h} L{x} {y+h} Z" fill="url(#ap)" filter="url(#apf)"/>'
              f'<text x="{cxm:.0f}" y="{y+h-16}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">{lab}</text>')
            # tap icon above apex
            shapes+=(f'<circle cx="{cxm:.0f}" cy="{y-2}" r="4" fill="rgb({ACC})"/>')
            subcol=f"rgb({ACC})"
        else:
            shapes+=(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="{h}" rx="14" fill="url(#tb)" stroke="rgba(255,255,255,.10)"/>'
              f'<text x="{cxm:.0f}" y="{y+30}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({ACC})">{lab}</text>')
            subcol="#8f8f85"
        shapes+=f'<text x="{cxm:.0f}" y="{y+h+ (0 if apex else -12) + (24 if apex else 0)}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".05em" fill="{subcol}">{sub}</text>'
        y+=h+58
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You sit on top","ONE TAP A DAY")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="ap" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></linearGradient>
        <linearGradient id="tb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <filter id="apf" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {shapes}
      </svg>
      {cap("the org runs, you approve. hierarchy with a human at the head.")}</div>'''

PANELS={"everything":everything(),"structure":structure(),"research":research(),"outreach":outreach(),
        "enable":enable(),"revops":revops(),"onejob":onejob(),"chief":chief()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/salesorg"; os.makedirs(outd,exist_ok=True)
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
