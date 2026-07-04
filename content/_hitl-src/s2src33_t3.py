#!/usr/bin/env python3
# TIER 3 - COLD LIST, WARM REPLY. One outbound sequence, traced end to end (SPECTER).
# Each panel a UNIQUE hand-built coded scene filling a clean rounded card, title + one-line
# caption, NO generic stat-chip strips, NO cuts/walls. Warm palette. Cents pricing.
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
def htitleiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LEADLIST - a raw cold list as dense rows, most dead weight, a few lit with a score badge
def leadlist():
    rows=[("Northwind Robotics","hiring 3 ops roles",92),
          ("Globex Systems","raised $4M in May",88),
          ("Vertex Freight","pricing page hit 4x",84),
          ("Acme Supply Co","no signal",None),
          ("Dunder Group","no signal",None),
          ("Initrode Labs","no signal",None),
          ("Soylent Foods","no signal",None),
          ("Meridian Parts","no signal",None)]
    out=""
    for a,b,c in rows:
        if c is not None:
            badge=(f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});'
                   f'padding:6px 15px;border-radius:11px;box-shadow:0 5px 13px rgba({ACC},.4)">'
                   f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:21px;color:#1a0f0a;line-height:1">{c}</span>'
                   f'<span style="font-family:\'DM Mono\';font-size:9px;letter-spacing:.1em;color:rgba(26,15,10,.7)">SCORE</span></div>')
            row=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(160deg,#38332d,#241f1a);'
                 f'border:1px solid rgba(212,162,127,.30);border-radius:13px;padding:11px 16px">'
                 f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:#FAFAF7">{a}</div>'
                 f'<div style="font-family:\'DM Sans\';font-size:13px;color:rgb({ACC})">{b}</div></div>{badge}</div>')
        else:
            row=(f'<div style="display:flex;align-items:center;gap:18px;background:rgba(250,250,247,.02);'
                 f'border:1px solid rgba(250,250,247,.06);border-radius:13px;padding:11px 16px;opacity:.5">'
                 f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#8a857b">{a}</div>'
                 f'<div style="font-family:\'DM Sans\';font-size:13px;color:#6f6a60">{b}</div></div>'
                 f'<span style="font-family:\'DM Mono\';font-size:16px;color:#5a554c">-</span></div>')
        out+=row
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("2,000 names, mostly dead","COLD LIST")}
      <div style="display:flex;flex-direction:column;gap:9px">{out}</div>
      {cap("most of a list is noise. it keeps only the few worth a first line.")}</div>'''

# 2. DOSSIER - IVORY. one prospect enriched into a ranked brief: center disc, 4 fact nodes orbit
def dossier():
    cx,cy=306,232; Rr=150
    facts=[("$4M raised","TechCrunch, May",-90),
           ("3 ops hires","LinkedIn, this wk",0),
           ("pricing page 4x","intent signal",90),
           ("no AI layer","from their stack",180)]
    ring=""
    for main,src,a in facts:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.30)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#96562d"/>')
    labels=""
    pos=[(cx,cy-Rr-14,"middle"),(cx+Rr+18,cy,"start"),(cx,cy+Rr+34,"middle"),(cx-Rr-18,cy,"end")]
    for (main,src,a),(lx,ly,anch) in zip(facts,pos):
        labels+=(f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="{anch}" font-family="DM Sans" font-weight="800" font-size="19" fill="#2a2016">{main}</text>'
          f'<text x="{lx:.0f}" y="{ly+21:.0f}" text-anchor="{anch}" font-family="DM Mono" font-size="12" fill="#8a745a">{src}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitleiv("One name, fully known","RANKED BRIEF")}
      <svg width="612" height="500" viewBox="0 0 612 500" style="display:block;margin:0 auto">
        <defs><radialGradient id="dv" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="#c07a4a"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="dvg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="rgba(150,90,45,.4)"/></filter></defs>
        {ring}
        <g filter="url(#dvg)"><circle cx="{cx}" cy="{cy}" r="64" fill="url(#dv)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#fdfbf6">Northwind</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#f3e4d4">VP Ops</text>
        {labels}
      </svg>
      {cap("raw name in, a ranked brief out - funding, hiring, stack, intent.","#8a745a")}</div>'''

# 3. DRAFT - an email composer window, one personalized opening line lit
def draft():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Written for one human","SPECTER DRAFT")}
      <div style="background:linear-gradient(160deg,#242019,#1a1713);border:1px solid rgba(255,255,255,.10);border-radius:20px;overflow:hidden;box-shadow:0 30px 54px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.06)">
        <div style="display:flex;align-items:center;gap:9px;padding:15px 20px;background:rgba(255,255,255,.03);border-bottom:1px solid rgba(255,255,255,.07)">
          <span style="width:12px;height:12px;border-radius:50%;background:#3a352f"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#3a352f"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#3a352f"></span>
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:#8f8f85;margin-left:12px">NEW MESSAGE</span></div>
        <div style="padding:22px 26px">
          <div style="display:flex;gap:14px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,.06)"><span style="font-family:'DM Mono';font-size:14px;color:#7a746a;width:64px">To</span><span style="font-family:'DM Sans';font-size:17px;color:#d9d5cc">ops lead, Northwind Robotics</span></div>
          <div style="display:flex;gap:14px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span style="font-family:'DM Mono';font-size:14px;color:#7a746a;width:64px">Subject</span><span style="font-family:'DM Sans';font-weight:700;font-size:17px;color:#FAFAF7">3 ops roles is a lot at once</span></div>
          <div style="margin-top:18px;background:rgba(212,162,127,.12);border-left:3px solid rgb({ACC});border-radius:8px;padding:14px 16px;font-family:'DM Sans';font-size:19px;color:#f2ede2;line-height:1.4">Saw you opened 3 ops roles this week. Usually that means the manual work is winning.</div>
          <div style="margin-top:14px;font-family:'DM Sans';font-size:18px;color:#a8a296;line-height:1.5">We put one operator agent on that load for founders your size. Worth 10 minutes?</div>
        </div></div>
      {cap("each email opens on a real trigger, never a template blast.")}</div>'''

# 4. CADENCE - vertical timeline of the 4-touch sequence
def cadence():
    steps=[("DAY 1","First email","the trigger open",True),
           ("DAY 3","Follow-up","one line, one nudge",True),
           ("DAY 7","Value add","a number they care about",True),
           ("DAY 12","Breakup","last call, no pressure",False)]
    spine_top,gap=44,116
    nodes=""
    for i,(day,title,sub,strong) in enumerate(steps):
        y=spine_top+i*gap
        dotcol=f"rgb({ACC})" if strong else "rgba(212,162,127,.4)"
        nodes+=(f'<div style="position:absolute;left:0;top:{y-30}px;display:flex;align-items:center;gap:24px;width:720px">'
          f'<div style="position:relative;flex-shrink:0;width:64px;display:flex;justify-content:center">'
          f'<span style="width:22px;height:22px;border-radius:50%;background:{dotcol};box-shadow:0 0 16px rgba({ACC},.5);border:3px solid #1d1d1b"></span></div>'
          f'<div style="flex:1;display:flex;align-items:center;gap:20px;background:linear-gradient(160deg,#332e28,#221e1a);border:1px solid rgba(255,255,255,.09);border-radius:15px;padding:15px 20px">'
          f'<span style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.1em;color:rgb({ACC});width:70px;flex-shrink:0">{day}</span>'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#FAFAF7">{title}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#8f8f85">{sub}</div></div></div></div>')
    total=spine_top+(len(steps)-1)*gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("A sequence, not a send","4 TOUCHES")}
      <div style="position:relative;height:{total+40}px">
        <div style="position:absolute;left:31px;top:{spine_top}px;width:2px;height:{total-spine_top}px;background:rgba(212,162,127,.3)"></div>
        {nodes}</div>
      {cap("one send is a coin flip. the replies live inside the sequence.")}</div>'''

# 5. CENTS - IVORY. old sending stack billed a salary; Ultron bills in cents
def cents():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitleiv("The old stack cost a salary","NOW: CENTS")}
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:60px;height:420px;padding:0 20px">
        <div style="display:flex;flex-direction:column;align-items:center">
          <span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#9a7a55;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7);margin-bottom:12px">$1,200/mo</span>
          <div style="width:150px;height:280px;border-radius:16px 16px 6px 6px;background:linear-gradient(180deg,#c9b79b,#a5906f);border:1px solid rgba(120,95,60,.25);box-shadow:inset 0 3px 4px rgba(255,255,255,.5), 0 18px 30px rgba(120,95,60,.2)"></div>
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.08em;color:#8a745a;margin-top:16px">THE SENDING STACK</span></div>
        <div style="display:flex;flex-direction:column;align-items:center">
          <span style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#96562d;margin-bottom:12px">3c</span>
          <div style="width:150px;height:70px;border-radius:16px 16px 6px 6px;background:linear-gradient(180deg,#e0a878,#96562d);border:1px solid rgba(150,90,45,.4);box-shadow:inset 0 3px 4px rgba(255,255,255,.35), 0 14px 26px rgba(150,90,45,.3)"></div>
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.08em;color:#8a745a;margin-top:16px">ULTRON, PER LEAD</span></div>
      </div>
      {cap("the sending tools billed monthly. this bills in cents, per lead, per token.","#8a745a")}</div>'''

# 6. GATE - HUMAN GATE: a batch of drafts parked behind a lock, one tap to send
def gate():
    pend=[("Northwind Robotics","3 ops roles open"),
          ("Globex Systems","raised $4M in May"),
          ("Vertex Freight","pricing page 4x")]
    cards=""
    for a,b in pend:
        cards+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#221e1a);'
          f'border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:13px 18px">'
          f'<div style="flex-shrink:0;width:36px;height:36px;border-radius:10px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.3);'
          f'display:flex;align-items:center;justify-content:center"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.2"><path d="M4 6h16M4 12h16M4 18h10"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:13px;color:#8f8f85">{b}</div></div>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#c9a583;flex-shrink:0">PENDING</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without you","HUMAN GATE")}
      <div style="display:flex;align-items:center;justify-content:space-between;background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:16px 22px;margin-bottom:18px">
        <div style="display:flex;align-items:center;gap:16px">
          <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.2"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>
          <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#FAFAF7">42 ready, parked</span></div>
        <div style="display:flex;align-items:center;gap:9px;background:rgb({ACC});padding:11px 22px;border-radius:999px;box-shadow:0 10px 22px rgba({ACC},.4)">
          <span style="font-family:'DM Sans';font-weight:900;font-size:16px;color:#1a0f0a">Approve and send</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div></div>
      <div style="display:flex;flex-direction:column;gap:11px">{cards}</div>
      {cap("the batch waits at the gate. one tap and it goes.")}</div>'''

# 7. REPLIES - inbox of overnight replies, a couple booked
def replies():
    inbox=[("Northwind Robotics","Re: 3 ops roles is a lot","Sure, send a time","BOOKED"),
           ("Globex Systems","Re: saw the round","What does it cost?","REPLIED"),
           ("Vertex Freight","Re: your pricing page","Book me Thursday","BOOKED"),
           ("Meridian Parts","Re: quick question","Not right now","PASSED")]
    rows=""
    for a,sub,snip,st in inbox:
        booked=(st=="BOOKED")
        stcol=f"rgb({ACC})" if booked else ("#c9a583" if st=="REPLIED" else "#6f6a60")
        stbg=f"rgba(212,162,127,.16)" if booked else "rgba(250,250,247,.05)"
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(160deg,#332e28,#221e1a);'
          f'border:1px solid {("rgba(212,162,127,.32)" if booked else "rgba(255,255,255,.08)")};border-radius:14px;padding:14px 18px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:linear-gradient(160deg,#4a423a,#2a2622);'
          f'display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:19px;color:rgb({ACC})">{a[0]}</div>'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#a8a296">{snip}</div></div>'
          f'<span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:{stcol};background:{stbg};padding:6px 12px;border-radius:8px;flex-shrink:0">{st}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You wake to replies","OVERNIGHT")}
      <div style="display:flex;flex-direction:column;gap:11px">{rows}</div>
      {cap("sent while you slept, answered before your coffee.")}</div>'''

# 8. CALENDAR - a work week with booked meeting slots lit
def calendar():
    days=["MON","TUE","WED","THU","FRI"]
    slots=["09","11","14","16"]
    booked={(0,1),(1,0),(1,3),(2,2),(3,0),(3,3),(4,1)}
    cols=""
    for di,d in enumerate(days):
        cells=""
        for si,s in enumerate(slots):
            if (di,si) in booked:
                cells+=(f'<div style="height:58px;border-radius:10px;background:linear-gradient(160deg,#e0a878,rgb({ACC}) 60%,#9a5a35);'
                  f'display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 8px 16px rgba({ACC},.35), inset 0 2px 2px rgba(255,255,255,.3)">'
                  f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:13px;color:#1a0f0a;line-height:1">CALL</span>'
                  f'<span style="font-family:\'DM Mono\';font-size:10px;color:rgba(26,15,10,.7)">{s}:00</span></div>')
            else:
                cells+=('<div style="height:58px;border-radius:10px;background:rgba(250,250,247,.03);'
                  'border:1px solid rgba(250,250,247,.05)"></div>')
        cols+=(f'<div style="flex:1;display:flex;flex-direction:column;gap:9px">'
          f'<div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.12em;color:#8f8f85;text-align:center;margin-bottom:3px">{d}</div>{cells}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Cold Monday, full Friday","7 BOOKED")}
      <div style="display:flex;gap:12px">{cols}</div>
      {cap("cold list to a calendar of calls, run overnight, priced in cents.")}</div>'''

PANELS={"leadlist":leadlist(),"dossier":dossier(),"draft":draft(),"cadence":cadence(),
        "cents":cents(),"gate":gate(),"replies":replies(),"calendar":calendar()}

if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src33"; os.makedirs(outd,exist_ok=True)
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
