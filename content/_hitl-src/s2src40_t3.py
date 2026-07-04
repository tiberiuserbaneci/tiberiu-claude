#!/usr/bin/env python3
# TIER 3 - THE OVERNIGHT PIPELINE. Each panel a UNIQUE hand-built coded scene on a clean rounded
# card, title + one-line caption, NO stat-chip strips / cuts / walls. Warm palette, cents only.
# An overnight-timeline deck (an OUTCOME, not an org chart): 18:00 lights out -> 09:00 full pipeline.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return ('<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return ('<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LIGHTSOUT - 18:00: one instruction handed off, an analog clock, an empty pipeline strip
def lightsout():
    cx,cy,R=150,150,120
    ticks=""
    for k in range(12):
        a=math.radians(k*30-90); x1=cx+(R-4)*math.cos(a); y1=cy+(R-4)*math.sin(a)
        x2=cx+(R-18)*math.cos(a); y2=cy+(R-18)*math.sin(a)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="{3 if k%3==0 else 1.5}"/>'
    clock=f'''<svg width="300" height="300" viewBox="0 0 300 300" style="flex-shrink:0">
      <defs><radialGradient id="dial" cx="38%" cy="32%"><stop offset="0%" stop-color="#26231f"/><stop offset="100%" stop-color="#151311"/></radialGradient>
      <filter id="cg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.28"/></filter></defs>
      <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#dial)" stroke="rgba(212,162,127,.32)" stroke-width="2"/></g>
      {ticks}
      <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-64}" stroke="#FAFAF7" stroke-width="6" stroke-linecap="round"/>
      <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+82}" stroke="rgb({ACC})" stroke-width="4.5" stroke-linecap="round"/>
      <circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/>
      <text x="{cx}" y="{cy+108}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".2em" fill="rgb({ACC})">18:00</text>
    </svg>'''
    brief=f'''<div style="flex:1;display:flex;flex-direction:column;gap:16px">
      <div style="background:#141210;border:1px solid rgba(255,255,255,.09);border-radius:16px;overflow:hidden;box-shadow:0 20px 40px rgba(0,0,0,.5)">
        <div style="display:flex;align-items:center;gap:7px;padding:11px 16px;background:#211d19">
          <span style="width:10px;height:10px;border-radius:50%;background:#c8503c"></span>
          <span style="width:10px;height:10px;border-radius:50%;background:#c8a04b"></span>
          <span style="width:10px;height:10px;border-radius:50%;background:#7fa86a"></span>
          <span style="margin-left:auto;font-family:'DM Mono';font-size:12px;color:#6f6a60">night shift</span></div>
        <div style="padding:20px 20px 22px;font-family:'DM Mono';font-size:19px;color:#e8e2d6;line-height:1.5">
          <span style="color:rgb({ACC})">$</span> book me 30 calls<br>&nbsp;&nbsp;by friday, 9am</div>
      </div>
      <div style="background:rgba(200,70,35,.07);border:1px dashed rgba(200,70,35,.3);border-radius:14px;padding:13px 18px;display:flex;align-items:center;gap:12px">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#c86a4b;flex-shrink:0">OLD STACK</span>
        <span style="font-family:'DM Sans';font-size:16px;color:#a8988a">$1,400/mo</span>
        <span style="margin-left:auto;font-family:'DM Mono';font-size:12px;color:#8f8f85">still empty by morning</span></div>
    </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You logged off. It clocked in.","ONE LINE, LIGHTS OUT")}
      <div style="display:flex;align-items:center;gap:34px">{clock}{brief}</div>
      {cap("one line of plain English, then the operator worked the whole night shift.")}</div>'''

# 2. RESEARCH - isometric stack of ranked target dossiers (CORTEX)
def research():
    cards=""
    rows=[("Northwind Robotics","hiring 3 ops roles · Series A","94"),
          ("Globex Systems","raised $4M in May","89"),
          ("Initech","no AI layer yet · 40 staff","83")]
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
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("847 read. 40 worth your time.","RANKED BY DAWN")}
      <div style="font-family:'DM Sans';font-size:16px;color:#9a9488;margin:-4px 0 4px">CORTEX scanned the web overnight and scored every account by fit.</div>
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:460px;position:relative">{cards}</div></div>
      {cap("no scraping tool, no VA - one ranked shortlist waiting in the morning.")}</div>'''

# 3. ROUTER - job token fanned to 3 cost tiers, SMART picked, cents total (MODEL ROUTER)
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
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
      {htitle("A brain that budgets itself","MODEL ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">draft 40<br>sequences</div>
        {cards}
        <div style="position:absolute;left:492px;top:404px;display:flex;align-items:baseline;gap:10px">
          <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:rgb({ACC})">$0.60</span>
          <span style="font-family:DM Sans;font-size:16px;color:#8f8f85">for the whole night</span></div>
      </div>
      {cap("each job takes the cheapest tier that can do it - a night of thinking, sixty cents.")}</div>'''

# 4. OUTBOUND - horizontal 3-touch sequence timeline with wait pills and cents (SPECTER)
def outbound():
    def email(day,label,subj):
        return (f'<div style="width:196px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.1);border-radius:16px;'
          f'box-shadow:0 20px 34px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07);overflow:hidden">'
          f'<div style="padding:11px 15px;background:#26221e;display:flex;align-items:center;justify-content:space-between">'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">{day}</span>'
          f'<span style="font-family:DM Mono;font-size:11px;color:#8f8f85">0.3c</span></div>'
          f'<div style="padding:16px 16px 18px">'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:17px;color:#FAFAF7">{label}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#9a9488;margin-top:5px;line-height:1.35">{subj}</div></div></div>')
    def wait(t):
        return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px;flex-shrink:0">'
          f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
          f'<span style="font-family:DM Mono;font-size:11px;color:#8f8f85">{t}</span></div>')
    row=(f'<div style="display:flex;align-items:center;gap:14px;justify-content:center">'
        f'{email("DAY 1","Opener","one specific trigger, a question not a pitch")}{wait("wait 2d")}'
        f'{email("DAY 3","Nudge","reply to your own thread, 40 words")}{wait("wait 3d")}'
        f'{email("DAY 6","Break-up","one last line, permission to close")}</div>')
    branch=(f'<div style="margin-top:26px;display:flex;align-items:center;justify-content:center;gap:14px">'
        f'<span style="font-family:DM Mono;font-size:13px;color:#9a9488">reply detected</span>'
        f'<svg width="30" height="18" viewBox="0 0 30 18" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round"><path d="M2 9h24M20 3l6 6-6 6"/></svg>'
        f'<span style="font-family:DM Sans;font-weight:800;font-size:17px;color:#FAFAF7;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.34);border-radius:12px;padding:8px 16px">STRIKER takes the call</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("A sequence, queued by midnight","3 TOUCHES · CENTS")}
      <div style="padding:22px 0 6px">{row}{branch}</div>
      {cap("40 prospects, a full three-touch sequence drafted for twelve cents total.")}</div>'''

# 5. VOICE - IVORY ring gauge + a sample cold-email line written in your voice (PULSE)
def voice():
    pct=98; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("It writes like you do","VOICE MATCH")}
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
            "Saw you opened three ops roles this week. Who is handling outbound while you hire?"</div>
          <div style="display:flex;gap:22px;margin-top:16px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["short lines","no hedging","your cadence"])}
          </div></div>
      </div>
      {cap("sampled from your real posts, banned words enforced on every draft.","#8a745a")}</div>'''

# 6. MEMORY - radial core, 5 agent lifelines drawing from one memory (SHARED CORE)
def memory():
    cx,cy=210,210
    agents=[("CORTEX",-90),("SPECTER",-18),("STRIKER",54),("PULSE",126),("AMPLIFY",198)]
    lines=""; nodes=""
    for nm,a in agents:
        x=cx+150*math.cos(math.radians(a)); y=cy+150*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="32" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="54" fill="url(#mc)"/></g>
        <ellipse cx="{cx}" cy="{cy-16}" rx="30" ry="9" fill="none" stroke="#2a160c" stroke-width="3"/>
        <path d="M{cx-30} {cy-16} V{cy+16}" stroke="#2a160c" stroke-width="3"/><path d="M{cx+30} {cy-16} V{cy+16}" stroke="#2a160c" stroke-width="3"/>
        <ellipse cx="{cx}" cy="{cy}" rx="30" ry="9" fill="none" stroke="#2a160c" stroke-width="3"/>
        <ellipse cx="{cx}" cy="{cy+16}" rx="30" ry="9" fill="none" stroke="#2a160c" stroke-width="3"/>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("It remembered every no","SHARED CORE")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">ICP, pipeline, pricing, past replies - every agent draws from one memory. Nothing you said in week one is lost by week ten.</div>
        {cap("one core feeds them all. nothing forgets you.")}</div></div>'''

# 7. GATE - a queue of parked sends held at one lock, 0 delivered (HUMAN GATE)
def gate():
    queue=[("40","emails ready to fire"),("12","follow-ups queued"),("3","proposals drafted")]
    items=""
    for n,label in queue:
        items+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(255,255,255,.1);border-radius:16px;padding:15px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC});line-height:1;min-width:56px">{n}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-size:17px;color:#d9d5cc">{label}</span>'
          f'<svg width="22" height="22" viewBox="0 0 24 24" fill="rgb({ACC})"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#8f8f85">HELD</span></div>')
    lock=f'''<svg width="230" height="300" viewBox="0 0 230 300" style="flex-shrink:0">
      <defs><radialGradient id="gl" cx="38%" cy="30%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1a1815"/></radialGradient>
      <filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter></defs>
      <g filter="url(#gg)"><rect x="35" y="60" width="160" height="160" rx="34" fill="url(#gl)" stroke="rgb({ACC})" stroke-width="2.5"/></g>
      <g transform="translate(83,108)"><rect x="0" y="40" width="64" height="50" rx="11" fill="none" stroke="rgb({ACC})" stroke-width="6"/><path d="M12 40 V25 a20 20 0 0 1 40 0 v15" fill="none" stroke="rgb({ACC})" stroke-width="6"/></g>
      <text x="115" y="258" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">0 SENT</text>
      <text x="115" y="284" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb({ACC})">awaits your tap</text>
    </svg>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sent. All parked.","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex:1;display:flex;flex-direction:column;gap:13px">{items}</div>
        {lock}
      </div>
      {cap("the whole night's work sits behind one lock until you tap approve at 09:00.")}</div>'''

# 8. MORNING - IVORY filled pipeline kanban board, the payoff (PIPELINE, FULL)
def morning():
    cols=[("NEW",["Northwind","Globex","Initech","Acme","Hooli"]),
          ("BOOKED",["Wed 10:00","Thu 14:30","Fri 09:15"]),
          ("WARM",["Umbrella","Stark","Wayne","Vandelay"])]
    board=""
    for head,items in cols:
        cells=""
        for it in items:
            cells+=(f'<div style="background:rgba(255,255,255,.66);border:1px solid rgba(120,95,60,.14);border-radius:11px;'
              f'padding:11px 14px;font-family:DM Sans;font-weight:700;font-size:16px;color:#2a2016;box-shadow:0 4px 10px rgba(120,95,60,.1)">{it}</div>')
        board+=(f'<div style="flex:1;background:rgba(150,120,80,.08);border-radius:16px;padding:14px 13px">'
          f'<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#96562d">{head}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:16px;color:#2a2016">{len(items)}</span></div>'
          f'<div style="display:flex;flex-direction:column;gap:10px">{cells}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 36px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">09:00 - you tap approve</span>
        <span style="font-family:'DM Sans';font-weight:900;font-size:22px;color:#96562d">30 booked</span></div>
      <div style="display:flex;gap:14px;align-items:flex-start">{board}</div>
      {cap("you went to bed with an empty board. one tap ships the night. zero to pipeline.","#8a745a")}</div>'''

PANELS={"lightsout":lightsout(),"research":research(),"router":router(),"outbound":outbound(),
        "voice":voice(),"memory":memory(),"gate":gate(),"morning":morning()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src40"; os.makedirs(outd,exist_ok=True)
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
