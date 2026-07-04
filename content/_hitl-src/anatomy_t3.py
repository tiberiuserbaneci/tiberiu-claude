#!/usr/bin/env python3
# TIER 3 - ONE LOOP, HOUR BY HOUR, rebuilt to the WIRE-ITS-EYES / AI-BODY bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip
# strips, NO clip-path cuts, NO extruded walls. The autonomous follow-up loop, step by step.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"        # warm accent
IVA="#96562d"            # ivory-slide accent
BAD="200,70,35"          # muted red - failing / killed ONLY
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IVA}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. TRIGGER - hour-by-hour timeline: 3 leads silent to the 72h mark, the loop arms itself. Dark.
def trigger():
    lanes=[("Northwind Robotics","quote sent, Mon 11:04"),
           ("Globex Systems","asked pricing, Mon 15:20"),
           ("Initech","demo booked, Tue 09:00")]
    x0,x1=262,620; ax_y=58; y0=120; dy=74
    ticks="".join(f'<line x1="{x}" y1="{ax_y-8}" x2="{x}" y2="{ax_y}" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
        f'<text x="{x}" y="{ax_y-16}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{h}h</text>'
        for x,h in [(x0,0),((x0+x1)//2-60,24),((x0+x1)//2+60,48),(x1,72)])
    body=""
    for i,(nm,note) in enumerate(lanes):
        y=y0+i*dy
        body+=(f'<text x="30" y="{y+2}" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">{nm}</text>'
          f'<text x="30" y="{y+24}" font-family="DM Mono" font-size="11.5" fill="#8f8f85">{note}</text>'
          f'<circle cx="{x0}" cy="{y+3}" r="7" fill="rgb({ACC})"/>'
          f'<line x1="{x0+10}" y1="{y+3}" x2="{x1-14}" y2="{y+3}" stroke="rgba(250,250,247,.16)" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>'
          f'<text x="{(x0+x1)//2}" y="{y-12}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="#6f6a60">SILENT</text>'
          f'<circle cx="{x1}" cy="{y+3}" r="9" fill="rgb({ACC})" filter="url(#sp)"/>'
          f'<path d="M{x1+9} {y+3} L694 190" stroke="rgba(212,162,127,.4)" stroke-width="2" fill="none"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It wakes itself up","72H SILENT")}
      <svg width="820" height="360" viewBox="0 0 820 360">
        <defs><radialGradient id="arm" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sp" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
        <filter id="ag" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {ticks}{body}
        <g filter="url(#ag)"><circle cx="742" cy="190" r="52" fill="url(#arm)"/></g>
        <text x="742" y="184" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ARM</text>
        <text x="742" y="208" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">09:00</text>
      </svg>
      {cap("nobody typed anything. seventy-two hours of silence is the trigger.")}</div>'''

# 2. READS - iso stack of 3 context cards loaded into working memory. IVORY.
def reads():
    ctx=[("LAST REPLY","\"send me pricing, we're comparing\""),
         ("THE OBJECTION","already runs too many tools"),
         ("PRICING RULES","cents per run, no seat fees")]
    cards=""
    for i,(k,v) in enumerate(ctx):
        y=i*120
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:470px;background:linear-gradient(160deg,#ffffff,#f2eadb);'
          f'border:1px solid rgba(120,95,60,.20);border-radius:16px;padding:16px 20px;'
          f'box-shadow:0 26px 40px rgba(120,95,60,.28), inset 0 2px 2px rgba(255,255,255,.9);text-align:left">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{IVA}">{k}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#2a2016;margin-top:4px">{v}</div></div>')
    rows="".join(f'<div style="display:flex;align-items:center;gap:11px;margin-bottom:15px">'
        f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="{IVA}" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>'
        f'<span style="font-family:DM Sans;font-size:17px;color:#4a3a28">{x}</span></div>' for x in ["reply","objection","rules"])
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <div style="flex-shrink:0;perspective:1700px;width:470px;height:400px;display:flex;align-items:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-9deg);width:470px;height:360px;position:relative">{cards}</div></div>
      <div style="flex:1">
        {htitle_iv("It reads before it writes","FROM MEMORY")}
        <div style="background:rgba(255,255,255,.62);border-left:4px solid {IVA};border-radius:12px;padding:18px 20px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{IVA};margin-bottom:12px">WORKING MEMORY LOADED</div>
          {rows}
          <div style="border-top:1px solid rgba(120,95,60,.22);margin-top:6px;padding-top:12px;font-family:DM Sans;font-weight:900;font-size:26px;color:#2a2016">0 pasted by you</div></div>
        {cap("the thread, the objection, your pricing rules - pulled, never re-typed.","#8a745a")}
      </div></div>'''

# 3. DRAFT1 - semicircular gauge scoring 71, below the 90 exit line. Dark.
def draft1():
    R=130; cx=170; cy=200; L=math.pi*R; f=0.71
    tt=math.radians(180*(1-0.90)); tx=cx+R*math.cos(tt); ty=cy-R*math.sin(tt)
    nt=math.radians(180*(1-f)); nx=cx+R*math.cos(nt); ny=cy-R*math.sin(nt)
    fails=[("148 words","cap is 90"),("trigger line weak","no specific hook")]
    fc=""
    for a,b in fails:
        fc+=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(200,70,35,.09);border:1px solid rgba(200,70,35,.34);'
          f'border-radius:14px;padding:13px 18px;margin-bottom:13px">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" stroke="rgb({BAD})" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
          f'<div style="text-align:left"><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:DM Mono;font-size:13px;color:#8f8f85">{b}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <div style="flex-shrink:0">
        <svg width="360" height="250" viewBox="0 0 360 250">
          <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(250,250,247,.10)" stroke-width="22" stroke-linecap="round"/>
          <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgb({ACC})" stroke-width="22" stroke-linecap="round" stroke-dasharray="{L*f:.0f} {L:.0f}"/>
          <line x1="{tx:.0f}" y1="{ty:.0f}" x2="{cx+(R+16)*math.cos(tt):.0f}" y2="{cy-(R+16)*math.sin(tt):.0f}" stroke="#7fd39a" stroke-width="4" stroke-linecap="round"/>
          <text x="{cx+(R+30)*math.cos(tt):.0f}" y="{cy-(R+18)*math.sin(tt):.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#7fd39a">90</text>
          <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#FAFAF7" stroke-width="4" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="9" fill="#FAFAF7"/>
          <text x="{cx}" y="{cy-34}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#FAFAF7">71</text>
          <text x="{cx}" y="{cy-8}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">SELF-SCORE</text>
        </svg></div>
      <div style="flex:1">
        {htitle("Draft one fails itself","SCORE 71 / 90")}
        {fc}
        {cap("it does not ask you what is wrong. it already knows, and redoes.")}
      </div></div>'''

# 4. DRAFT3 - iteration climb 71 -> 84 -> 90 with a loop-back arrow and a green exit. IVORY.
def draft3():
    steps=[("Draft 1",71,"too long"),("Draft 2",84,"trigger fixed"),("Draft 3",90,"passes")]
    n=len(steps); cw=182; gap=22; x0=8
    cards=""
    for i,(nm,sc,note) in enumerate(steps):
        x=x0+i*(cw+gap); last=(i==n-1)
        barcol=IVA if not last else "#3f7a4e"
        bw=int((cw-40)*sc/100)
        stat=(f'<span style="font-family:DM Mono;font-size:12px;color:#3f7a4e">EXIT</span>' if last
              else f'<span style="font-family:DM Mono;font-size:12px;color:#a07a52">redo</span>')
        cards+=(f'<div style="position:absolute;left:{x}px;top:70px;width:{cw}px;background:linear-gradient(160deg,#ffffff,#f1e9da);'
          f'border:1px solid {"rgba(63,122,78,.5)" if last else "rgba(120,95,60,.2)"};border-radius:18px;padding:16px 18px;'
          f'box-shadow:0 22px 36px rgba(120,95,60,.24), inset 0 2px 2px rgba(255,255,255,.9)">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#5a4634">{nm}</span>{stat}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016;line-height:1.05;margin-top:2px">{sc}</div>'
          f'<div style="height:9px;border-radius:5px;background:rgba(120,95,60,.16);margin-top:8px"><div style="width:{bw}px;height:9px;border-radius:5px;background:{barcol}"></div></div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8a745a;margin-top:8px">{note}</div></div>')
    # loop-back arc over cards 1->2 (redo) and exit arrow after card 3
    mid1=x0+cw//2; mid2=x0+(cw+gap)+cw//2; ex=x0+2*(cw+gap)+cw+2
    arrows=(f'<path d="M{mid2} 60 C{mid2} 20,{mid1} 20,{mid1} 58" fill="none" stroke="{IVA}" stroke-width="2.5" marker-end="url(#ah)"/>'
      f'<text x="{(mid1+mid2)//2}" y="18" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="{IVA}">LOOP: REDO UNTIL PASS</text>'
      f'<path d="M{ex} 106 h38" stroke="#3f7a4e" stroke-width="4" marker-end="url(#ae)"/>'
      f'<text x="{ex+4}" y="140" text-anchor="start" font-family="DM Mono" font-size="12" fill="#3f7a4e">SENT-READY</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("It redoes until it passes","EXIT AT 90")}
      <div style="position:relative;height:280px">
        <svg width="820" height="200" viewBox="0 0 820 200" style="position:absolute;left:0;top:0;overflow:visible">
          <defs><marker id="ah" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L8 4.5 L0 9 z" fill="{IVA}"/></marker>
          <marker id="ae" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L8 4.5 L0 9 z" fill="#3f7a4e"/></marker></defs>
          {arrows}
        </svg>
        {cards}
      </div>
      {cap("exit condition met. not tired, not lazy, not hopeful. verified.","#8a745a")}</div>'''

# 5. PARKED - queue of 3 sends butting a gate + lock, autonomous inside / held outside. Dark.
def parked():
    sends=[("Northwind","follow-up ready"),("Globex","follow-up ready"),("Initech","follow-up ready")]
    chips=""
    for i,(nm,st) in enumerate(sends):
        y=70+i*104
        chips+=(f'<div style="position:absolute;left:0;top:{y}px;width:360px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:15px 18px;display:flex;align-items:center;gap:14px;'
          f'box-shadow:0 16px 28px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="1.9"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M4 7l8 6 8-6"/></svg>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:#8f8f85">{st}</div></div>'
          f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:rgb({ACC})">PARKED</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Autonomous inside, held outside","3 AT THE GATE")}
      <div style="position:relative;height:390px">
        {chips}
        <svg width="820" height="390" viewBox="0 0 820 390" style="position:absolute;left:0;top:0;pointer-events:none">
          <defs><radialGradient id="lk" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="lg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          <rect x="420" y="30" width="12" height="330" rx="6" fill="rgb({ACC})" opacity="0.5"/>
          <text x="426" y="20" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".2em" fill="#8f8f85">GATE</text>
          <line x1="360" y1="122" x2="418" y2="195" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>
          <line x1="360" y1="226" x2="418" y2="195" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>
          <line x1="360" y1="330" x2="418" y2="195" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>
          <g filter="url(#lg)"><circle cx="620" cy="195" r="96" fill="url(#lk)"/></g>
          <g transform="translate(588,158)"><rect x="0" y="34" width="64" height="48" rx="10" fill="none" stroke="#2a160c" stroke-width="6"/><path d="M12 34 V20 a20 20 0 0 1 40 0 v14" fill="none" stroke="#2a160c" stroke-width="6"/></g>
          <text x="620" y="300" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">YOUR TAP</text>
        </svg>
      </div>
      {cap("the loop runs full-speed inside. every send outside waits for one tap.")}</div>'''

# 6. TAP - 3 sends judged: two approved, one killed. Dark.
def tap():
    rows=[("Northwind Robotics","\"saw you hired 3 ops roles...\"","SENT",True),
          ("Globex Systems","\"since you asked about pricing...\"","SENT",True),
          ("Initech","\"just circling back again...\"","KILLED",False)]
    rc=""
    for nm,prev,st,ok in rows:
        col="#7fd39a" if ok else f"rgb({BAD})"
        icon=('<path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="#7fd39a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>' if ok
              else f'<path d="M7 7l10 10M17 7L7 17" stroke="rgb({BAD})" stroke-width="2.6" stroke-linecap="round"/>')
        dec="line-through;text-decoration-color:rgba(200,70,35,.7)" if not ok else "none"
        rc+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#312d29,#211e1a);'
          f'border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:16px 20px;margin-bottom:14px;'
          f'box-shadow:0 12px 24px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<div style="flex-shrink:0;width:40px;height:40px;border-radius:11px;background:rgba({ACC if ok else BAD},.14);border:1px solid rgba({ACC if ok else BAD},.34);display:flex;align-items:center;justify-content:center">'
          f'<svg width="24" height="24" viewBox="0 0 24 24">{icon}</svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85;text-decoration:{dec}">{prev}</div></div>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{col}">{st}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten seconds of judgement","2 SENT / 1 KILLED")}
      {rc}
      <div style="display:flex;align-items:center;gap:22px;margin-top:6px">
        <div style="flex:1;background:rgba(250,250,247,.03);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:14px 20px">
          <div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7">40 min <span style="color:rgb({ACC})">machine</span></div>
          <div style="font-family:DM Mono;font-size:12px;color:#8f8f85">reading, drafting, grading, scheduling</div></div>
        <div style="flex:1;background:rgba(212,162,127,.08);border:1px solid rgba(212,162,127,.3);border-radius:14px;padding:14px 20px">
          <div style="font-family:DM Sans;font-weight:900;font-size:26px;color:rgb({ACC})">10 sec you</div>
          <div style="font-family:DM Mono;font-size:12px;color:#8f8f85">two taps, one kill</div></div>
      </div>
      {cap("your judgement sits on top of the machine work, not inside it.")}</div>'''

# 7. REPLY - node flow: reply lands and the loop has already updated everything. Dark.
def reply():
    W,H=820,300
    nodes=[("Reply lands","Tue 09:41",90),("Deal moved","Call booked",290),("Next follow-up","+4 days",490),("Digest","07:00 tomorrow",690)]
    cy=150; els=""
    for i,(t,s,x) in enumerate(nodes):
        lit=(i==0)
        fill="url(#rl)" if lit else "#221f1b"
        flt='filter="url(#rg)"' if lit else ''
        els+=(f'<circle cx="{x}" cy="{cy}" r="46" fill="{fill}" stroke="rgb({ACC})" stroke-width="{2.5 if lit else 1.5}" {flt}/>'
          f'<text x="{x}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="{"#2a160c" if lit else "#e6d6c2"}">{"IN" if lit else i+1}</text>'
          f'<text x="{x}" y="{cy-70}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">{t}</text>'
          f'<text x="{x}" y="{cy+80}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">{s}</text>')
        if i<len(nodes)-1:
            nx=nodes[i+1][2]
            els+=f'<path d="M{x+48} {cy} H{nx-48}" stroke="rgba(212,162,127,.55)" stroke-width="3" marker-end="url(#rm)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The reply is already logged","AUTO-UPDATED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:10px auto 0">
        <defs><radialGradient id="rl" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter>
        <marker id="rm" markerWidth="9" markerHeight="9" refX="6" refY="4.5" orient="auto"><path d="M0 0 L8 4.5 L0 9 z" fill="rgb({ACC})"/></marker></defs>
        {els}
      </svg>
      {cap("one inbound event, and the pipeline, the schedule and the digest all move.")}</div>'''

# 8. POINT - split comparison: a prompt (one guess) vs the loop (a finished job with receipts). Dark.
def point():
    receipts=[("read the thread","3 sources"),("drafted + graded","90 / 90"),("gated for you","2 sent, 1 killed"),("logged the reply","pipeline moved")]
    rl="".join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:13px">'
        f'<svg width="20" height="20" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{a}</span>'
        f'<span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">{b}</span></div>' for a,b in receipts)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One guess versus a finished job","PROMPT / LOOP")}
      <div style="display:flex;align-items:stretch;gap:0;position:relative">
        <div style="flex:0 0 300px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);border-radius:18px;padding:24px 22px;opacity:.75">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#7a746a">A PROMPT</div>
          <div style="background:rgba(250,250,247,.05);border-radius:14px;padding:16px 18px;margin-top:18px;font-family:DM Sans;font-size:18px;color:#9a9488;line-height:1.4">"here are five sentences you could send"</div>
          <div style="font-family:DM Mono;font-size:12px;color:#7a746a;margin-top:16px">no memory &middot; no gate &middot; no log</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#8f8f85;margin-top:14px">1 guess, then it stops</div></div>
        <div style="flex-shrink:0;width:66px;display:flex;align-items:center;justify-content:center">
          <span style="font-family:DM Mono;font-weight:500;font-size:18px;letter-spacing:.1em;color:rgb({ACC})">VS</span></div>
        <div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1px solid rgba(212,162,127,.34);border-radius:18px;padding:24px 24px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({ACC})">A LOOP</div>
          <div style="margin-top:18px">{rl}</div></div>
      </div>
      {cap("a prompt gives you words. a loop gives you outcomes with receipts.")}</div>'''

PANELS={"trigger":trigger(),"reads":reads(),"draft1":draft1(),"draft3":draft3(),
        "parked":parked(),"tap":tap(),"reply":reply(),"point":point()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/anatomy"; os.makedirs(outd,exist_ok=True)
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
