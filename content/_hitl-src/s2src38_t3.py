#!/usr/bin/env python3
# TIER 3 - THE COLD-START PLAYBOOK. Source: "Ultimate Claude Starter Pack Playbook" resource-list
# carousel, reframed to Ultron as ONE outbound campaign a solo founder runs end-to-end (source ->
# time -> write -> approve -> send -> follow up -> book -> the cents bill). Each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO stat-chip strips,
# NO cuts/walls. Warm palette, mix of dark + ivory. Cents value prop; high $ only as the old stack.
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
def htiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SOURCED - isometric stack of ranked account cards (CORTEX builds the first list)
def sourced():
    rows=[("Northwind Robotics","3 ops roles open","94"),
          ("Globex Systems","raised $4M in May","89"),
          ("Initech","no AI layer yet","83")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:25px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 17px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{c}</span>
            <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">FIT</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 44px 44px">
      {htitle("847 accounts, ranked by fit","CORTEX · SOURCE")}
      <div style="perspective:2000px;height:600px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:490px;position:relative">{cards}</div></div>
      {cap("one brief in, every ICP-fit account scored overnight — fractions of a cent each.")}</div>'''

# 2. SIGNAL - radar sweep, live triggers timed for outreach
def signal():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",120,96),("New tool",210,168),("Exec hire",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    rows=[("Funding round","fire now"),("2 ops hires","fire now"),("Renewal in 30d","queued")]
    lead=""
    for a,b in rows:
        on=(b=="fire now"); col=f"rgb({ACC})" if on else "#8f8f85"
        lead+=(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
          f'<span style="font-family:DM Sans;font-size:18px;color:#d9d5cc">{a}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:{col}">{b}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It waits for the trigger","LIVE SIGNALS")}
        <div style="margin-top:2px">{lead}</div>
        {cap("funding, hiring, new tools, intent — it reaches out the day the signal fires.")}
      </div></div>'''

# 3. WRITTEN - IVORY email draft mockup, one trigger + one question, under 62 words
def written():
    body=('<div style="font-family:\'DM Sans\';font-size:19px;line-height:1.5;color:#3a3024">'
      'Saw Northwind just opened three ops roles.'
      '<div style="background:rgba(150,90,45,.12);border-left:3px solid #96562d;border-radius:8px;padding:8px 12px;margin:12px 0;color:#2a2016">'
      'Are you handling the ramp with headcount, or looking to automate the first slice?</div>'
      'If the second, I have a two-line setup worth 15 minutes.</div>')
    chip=lambda t:(f'<span style="display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.6);'
      f'border:1px solid rgba(150,90,45,.2);border-radius:999px;padding:7px 15px;font-family:\'DM Mono\';font-size:13px;color:#7a5a38">'
      f'<span style="width:8px;height:8px;border-radius:50%;background:#96562d"></span>{t}</span>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htiv("58 words, your cadence","SPECTER · DRAFT")}
      <div style="background:rgba(255,255,255,.62);border:1px solid rgba(150,90,45,.16);border-radius:20px;overflow:hidden;box-shadow:0 18px 34px rgba(120,95,60,.14)">
        <div style="display:flex;align-items:center;gap:10px;padding:15px 22px;border-bottom:1px solid rgba(150,90,45,.14);background:rgba(255,255,255,.4)">
          <span style="width:12px;height:12px;border-radius:50%;background:#d99d78"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#e6c39e"></span>
          <span style="font-family:'DM Mono';font-size:14px;color:#7a5a38;margin-left:8px">To: ops lead · Northwind Robotics</span></div>
        <div style="padding:24px 26px 26px">{body}</div>
      </div>
      <div style="display:flex;gap:14px;margin-top:20px">{chip("58 words")}{chip("1 specific trigger")}{chip("a question, not a pitch")}</div>
      {cap("written in your real voice — banned words enforced, never a template.","#8a745a")}</div>'''

# 4. GATE - queued messages held behind one lock, waiting for the operator's tap
def gate():
    queued=""
    labels=["Northwind Robotics","Globex Systems","Initech","Umbrella Co","Hooli Inc","Stark Labs"]
    for i,nm in enumerate(labels):
        queued+=(f'<div style="display:flex;align-items:center;gap:12px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(255,255,255,.09);border-radius:13px;padding:11px 15px;box-shadow:0 10px 20px rgba(0,0,0,.4)">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 8l9 6 9-6"/></svg>'
          f'<span style="flex:1;font-family:DM Sans;font-size:16px;color:#d9d5cc">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#8f8f85">HELD</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex:1;display:flex;flex-direction:column;gap:10px">
        {htitle("6 sends, waiting on you","HUMAN GATE")}
        {queued}
      </div>
      <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:22px">
        <svg width="200" height="230" viewBox="0 0 200 230">
          <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          <g filter="url(#og)"><circle cx="100" cy="112" r="92" fill="url(#orb)"/></g>
          <g transform="translate(62,74)"><rect x="0" y="40" width="76" height="56" rx="12" fill="none" stroke="#2a160c" stroke-width="8"/><path d="M14 40 V25 a24 24 0 0 1 48 0 v15" fill="none" stroke="#2a160c" stroke-width="8"/></g>
        </svg>
        <div style="background:rgb({ACC});color:#1a0f0a;font-family:'DM Sans';font-weight:900;font-size:20px;padding:14px 32px;border-radius:999px;box-shadow:0 12px 24px rgba(212,162,127,.4)">APPROVE →</div>
        <div style="font-family:'DM Mono';font-size:13px;color:#8f8f85">your tap releases them</div>
      </div></div>'''

# 5. SENT - timezone dial, each region's outreach fired at local 9am
def sent():
    cx,cy,R=210,215,175
    ticks=""
    for i in range(12):
        a=math.radians(i*30-90); x1=cx+(R-14)*math.cos(a); y1=cy+(R-14)*math.sin(a); x2=cx+R*math.cos(a); y2=cy+R*math.sin(a)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
    marks=[("UK",-125,"09:00"),("US-E",-90,"09:00"),("US-W",-55,"09:00")]
    spokes=""
    for nm,deg,t in marks:
        a=math.radians(deg); x=cx+(R-22)*math.cos(a); y=cy+(R-22)*math.sin(a)
        lx=cx+(R+30)*math.cos(a); ly=cy+(R+30)*math.sin(a)
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgb({ACC})" stroke-width="4" filter="url(#gl)"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="10" fill="rgb({ACC})" filter="url(#gl)"/>'
          f'<text x="{lx:.0f}" y="{ly-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">{nm}</text>')
    rowsl=""
    for nm,_,t in marks:
        rowsl+=(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
          f'<span style="font-family:DM Sans;font-size:19px;color:#d9d5cc">{nm} morning</span>'
          f'<span style="font-family:DM Mono;font-weight:500;font-size:17px;color:rgb({ACC})">{t}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:32px">
      <svg width="420" height="430" viewBox="0 0 420 430">
        <defs><filter id="gl" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816" stroke="rgba(212,162,127,.2)" stroke-width="2"/>
        <circle cx="{cx}" cy="{cy}" r="{R-40}" fill="none" stroke="rgba(212,162,127,.1)"/>
        {ticks}{spokes}
        <circle cx="{cx}" cy="{cy}" r="9" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("Sent at each local 9am","AMPLIFY")}
        <div style="margin-top:4px">{rowsl}</div>
        {cap("staggered by timezone — every prospect gets it at their own morning.")}
      </div></div>'''

# 6. FOLLOWUP - 3-step cadence timeline, chasing the no-replies across the week
def followup():
    W,H=820,300
    nodes=[("Day 1","first touch",140,True),("Day 3","nudge",410,True),("Day 7","last ask",680,True)]
    base=200; seg=""; circ=""
    seg+=f'<line x1="140" y1="{base}" x2="680" y2="{base}" stroke="rgba(212,162,127,.35)" stroke-width="3"/>'
    for nm,sub,x,on in nodes:
        circ+=(f'<circle cx="{x}" cy="{base}" r="40" fill="#241f1a" stroke="rgb({ACC})" stroke-width="3" filter="url(#ng)"/>'
          f'<text x="{x}" y="{base-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#FAFAF7">{nm.split()[1]}</text>'
          f'<text x="{x}" y="{base+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">{nm.split()[0]}</text>'
          f'<text x="{x}" y="{base+70}" text-anchor="middle" font-family="DM Sans" font-size="16" fill="#a8a296">{sub}</text>')
    tags=""
    for x0 in (275,545):
        tags+=(f'<rect x="{x0-58}" y="{base-96}" width="116" height="30" rx="15" fill="rgba(200,70,35,.12)" stroke="rgba(200,70,35,.4)"/>'
          f'<text x="{x0}" y="{base-76}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c86a4a">no reply</text>'
          f'<path d="M{x0} {base-66} v22" stroke="rgba(200,70,35,.4)" stroke-width="2" stroke-dasharray="3 4"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("It chases the silent ones","3-STEP CADENCE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:6px auto 0">
        <defs><filter id="ng" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter></defs>
        {seg}{tags}{circ}</svg>
      {cap("a spaced three-step cadence on every no-reply — you forget, it never does.")}</div>'''

# 7. BOOKED - IVORY week calendar, three slots filled with booked calls
def booked():
    days=["MON","TUE","WED","THU","FRI"]
    booked_cells={(1,0),(0,2),(3,3)}  # (row,col)
    grid=""
    for c,d in enumerate(days):
        grid+=f'<div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.1em;color:#7a5a38;text-align:center;padding-bottom:8px">{d}</div>'
    for r in range(4):
        for c in range(5):
            if (r,c) in booked_cells:
                grid+=('<div style="background:#96562d;border-radius:10px;height:58px;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 8px 16px rgba(150,90,45,.35)">'
                  '<span style="font-family:\'DM Sans\';font-weight:800;font-size:14px;color:#fff;line-height:1">Call</span>'
                  '<span style="font-family:\'DM Mono\';font-size:11px;color:rgba(255,255,255,.85)">booked</span></div>')
            else:
                grid+='<div style="background:rgba(255,255,255,.5);border:1px solid rgba(150,90,45,.14);border-radius:10px;height:58px"></div>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htiv("7 replies. 3 calls booked.","STRIKER · BOOK")}
      <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px">{grid}</div>
      <div style="display:flex;align-items:center;gap:12px;margin-top:20px">
        <div style="flex:1;height:1px;background:rgba(150,90,45,.18)"></div>
        <span style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#2a2016">3 on your calendar</span>
        <div style="flex:1;height:1px;background:rgba(150,90,45,.18)"></div></div>
      {cap("replies qualified and slotted straight onto your week — you just show up.","#8a745a")}</div>'''

# 8. CENTS - the bill: the old stack in dollars vs this week on Ultron in cents
def cents():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("The whole week cost cents","THE BILL")}
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:70px;height:430px;padding:20px 30px 0">
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%">
          <div style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#8f8f85">$420</div>
          <div style="width:150px;height:300px;margin-top:14px;border-radius:16px 16px 0 0;background:linear-gradient(180deg,#4a423a,#2a2622);border:1px solid rgba(255,255,255,.08);box-shadow:inset 0 3px 3px rgba(255,255,255,.08)"></div>
          <div style="font-family:'DM Mono';font-size:14px;letter-spacing:.1em;color:#8f8f85;margin-top:14px">OLD STACK / MO</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%">
          <div style="font-family:'DM Sans';font-weight:900;font-size:64px;color:rgb({ACC});filter:drop-shadow(0 0 22px rgba(212,162,127,.45))">$0.37</div>
          <div style="width:150px;height:14px;margin-top:14px;border-radius:8px 8px 0 0;background:linear-gradient(180deg,#f0c49e,rgb({ACC}));box-shadow:0 0 26px rgba(212,162,127,.5)"></div>
          <div style="font-family:'DM Mono';font-size:14px;letter-spacing:.1em;color:rgb({ACC});margin-top:14px">THIS WEEK / ULTRON</div>
        </div>
      </div>
      {cap("the old stack billed hundreds a month — this ran on pay-per-token cents.")}</div>'''

PANELS={"sourced":sourced(),"signal":signal(),"written":written(),"gate":gate(),
        "sent":sent(),"followup":followup(),"booked":booked(),"cents":cents()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src38"; os.makedirs(outd,exist_ok=True)
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
