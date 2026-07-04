#!/usr/bin/env python3
# TIER 3 - PROMOTE YOUR CODER (SENTINEL seniority ladder), built to the WIRE-ITS-EYES bar:
# 8 UNIQUE hand-built coded scenes, clean rounded CARD/CARDIV, warm palette, htitle + one cap each.
# Angle: junior-vague -> senior spec/plan/test/review/ship. NOT the handoff-pipeline / direction angle.
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LADDER - vertical seniority ladder: one rail through 4 level nodes, junior dim at the
# bottom -> senior lit/glowing at the top. Summarises the whole deck.
def ladder():
    rows=[("SHIPS","Specs, tests, reviews, then opens the PR.","SENTINEL",True),
          ("REVIEWS","Catches its own bugs before you see them.","",False),
          ("PLANS","Maps the codebase, proposes a plan first.","",False),
          ("GUESSES","Fires off code from a one-line prompt.","DEFAULT",None)]
    railx=72; ys=[70,190,310,430]
    rail=f'<line x1="{railx}" y1="{ys[0]}" x2="{railx}" y2="{ys[-1]}" stroke="rgba(212,162,127,.30)" stroke-width="3"/>'
    nodes=""
    for (lv,desc,tag,top),y in zip(rows,ys):
        if top:
            fill=f"rgb({ACC})"; stroke=f"rgb({ACC})"; glow=' filter="url(#lg)"'
        elif top is None:
            fill="#241f1a"; stroke=f"rgba({RED},.55)"; glow=""
        else:
            fill="#2a2622"; stroke="rgba(212,162,127,.5)"; glow=""
        nodes+=f'<circle cx="{railx}" cy="{y}" r="15" fill="{fill}" stroke="{stroke}" stroke-width="3"{glow}/>'
    rowdivs=""
    for (lv,desc,tag,top),y in zip(rows,ys):
        if top:
            lvc=f"rgb({ACC})"; dc="#e6d6c2"
        elif top is None:
            lvc=f"rgb({RED})"; dc="#7a746a"
        else:
            lvc="#FAFAF7"; dc="#a8a296"
        badge=f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});margin-left:14px">{tag}</span>' if tag else ''
        rowdivs+=(f'<div style="position:absolute;left:118px;top:{y-34}px;right:8px">'
          f'<div style="display:flex;align-items:baseline"><span style="font-family:DM Sans;font-weight:900;font-size:30px;color:{lvc}">{lv}</span>{badge}</div>'
          f'<div style="font-family:DM Sans;font-size:17px;color:{dc};margin-top:2px">{desc}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Same agent, four levels","SENIORITY")}
      <div style="position:relative;height:474px">
        <svg width="150" height="474" viewBox="0 0 150 474" style="position:absolute;left:0;top:0">
          <defs><filter id="lg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
          {rail}{nodes}
          <path d="M{railx} {ys[-1]-4} L{railx} {ys[0]+4}" stroke="none"/>
          <path d="M{railx-8} {ys[0]+20} L{railx} {ys[0]+4} L{railx+8} {ys[0]+20}" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        {rowdivs}
      </div>
      {cap("the same agent runs at four levels. you choose which one shows up.")}</div>'''

# 2. SPEC - IVORY paper ticket: a struck-out vague ask on top, then an acceptance-criteria
# checklist it writes for itself. Document form.
def spec():
    crit=["CSV and PDF export both supported","Empty state renders, no crash",
          "Amounts in cents, never rounded","Owner-only, auth enforced",
          "Errors surfaced, not swallowed","A test on every path",
          "Matches the project conventions"]
    rows=""
    for c in crit:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;padding:11px 0;border-bottom:1px solid rgba(120,95,60,.14)">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" style="flex-shrink:0"><rect x="2" y="2" width="20" height="20" rx="6" fill="rgba(150,90,45,.10)" stroke="#96562d" stroke-width="1.6"/><path d="M7 12.4l3.2 3.2L17 8.4" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="font-family:DM Sans;font-size:18px;color:#2a2016">{c}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("It writes the spec first","ACCEPTANCE")}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(200,70,35,.06);border:1px dashed rgba(200,70,35,.4);border-radius:14px;padding:12px 18px;margin-bottom:20px">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#a05030;flex-shrink:0">VAGUE ASK</span>
        <span style="font-family:DM Sans;font-size:18px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">"just make invoice export work"</span></div>
      <div style="background:rgba(255,255,255,.55);border-left:4px solid #96562d;border-radius:12px;padding:8px 22px 10px">
        <div style="display:flex;align-items:baseline;justify-content:space-between;padding:12px 0 6px;border-bottom:1.5px solid rgba(120,95,60,.22)">
          <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">Add invoice export</span>
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#96562d">DEFINITION OF DONE</span></div>
        {rows}
      </div>
      {cap("a vague ask becomes acceptance criteria it can check off itself.","#8a745a")}</div>'''

# 3. PLAN - top-down plan tree (DAG): one root branches into 4 ordered steps, ending on a
# "no code yet" gate. Distinct branching form.
def plan():
    steps=[("1","READ CODE"),("2","MAP DEPS"),("3","PROPOSE"),("4","YOUR TAP")]
    rx,rytop,rw,rh=310,40,200,72; rcx=rx+rw//2; rby=rytop+rh
    cy=250; cw=160; xs=[40,240,440,640]
    edges=""; cards=""
    for (n,lab),x in zip(steps,xs):
        ccx=x+cw//2
        edges+=f'<path d="M{rcx} {rby} C{rcx} {(rby+cy)//2},{ccx} {(rby+cy)//2-20},{ccx} {cy}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
        cards+=(f'<g><rect x="{x}" y="{cy}" width="{cw}" height="96" rx="16" fill="url(#stp)" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="{x+30}" cy="{cy+30}" r="17" fill="rgba(212,162,127,.16)" stroke="rgb({ACC})" stroke-width="1.5"/>'
          f'<text x="{x+30}" y="{cy+36}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="rgb({ACC})">{n}</text>'
          f'<text x="{ccx}" y="{cy+74}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing="1.5" fill="#e2dccf">{lab}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It plans before it codes","PLAN MODE")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="rt" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#211e1a"/></linearGradient>
          <linearGradient id="stp" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.30"/></filter>
        </defs>
        {edges}
        <g filter="url(#rg)"><rect x="{rx}" y="{rytop}" width="{rw}" height="{rh}" rx="20" fill="url(#rt)" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <text x="{rcx}" y="{rytop+30}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#FAFAF7">PLAN MODE</text>
        <text x="{rcx}" y="{rytop+54}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">the whole change, first</text>
        {cards}
        <g transform="translate(310,376)">
          <rect x="0" y="0" width="200" height="46" rx="14" fill="rgba(212,162,127,.10)" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>
          <g transform="translate(20,11)"><rect x="0" y="10" width="22" height="16" rx="4" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/><path d="M4 10 V6 a7 7 0 0 1 14 0 v4" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/></g>
          <text x="120" y="29" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({ACC})">NO CODE YET</text>
        </g>
      </svg>
      {cap("reads deps, maps the change, proposes the plan. not one line yet.")}</div>'''

# 4. MEMORY - radial hub-and-spokes: one rules core feeding every session on the ring.
def memory():
    cx,cy=410,232; R=178
    days=["Mon","Tue","Wed","Thu","Fri","Sat"]
    spokes=""; sats=""
    for i,d in enumerate(days):
        a=-90+i*(360/len(days))
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        sats+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="14" fill="#cfc9bd">{d}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="9.5" letter-spacing=".08em" fill="#8f8f85">SESSION</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One memory, every session","PROJECT RULES")}
      <svg width="820" height="464" viewBox="0 0 820 464" style="display:block;margin:0 auto">
        <defs><radialGradient id="mc" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {spokes}{sats}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="82" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-8}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">MEMORY</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010" letter-spacing=".06em">stack · rules</text>
        <text x="{cx}" y="{cy+34}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010" letter-spacing=".06em">guardrails</text>
      </svg>
      {cap("one rules file, read at the start of every session. never re-explained.")}</div>'''

# 5. TESTS - ring gauge (all green-free: accent) + a compact pass LED strip, "0 failing".
def tests():
    pct=100; r=76; circ=2*math.pi*r; dash=circ*pct/100
    cases=["auth guard","empty state","cents rounding","csv export","error path","refund path"]
    leds=""
    for c in cases:
        leds+=(f'<div style="display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
          f'<span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 10px rgba({ACC},.8);flex-shrink:0"></span>'
          f'<span style="font-family:DM Sans;font-size:17px;color:#d9d5cc;flex:1">{c}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">pass</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;position:relative;width:210px;height:210px">
        <svg width="210" height="210" viewBox="0 0 210 210">
          <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="16"/>
          <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 105 105)" filter="url(#tgl)"/>
          <defs><filter id="tgl" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        </svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:42px;color:#FAFAF7">42/42</span>
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.06em;color:rgb({ACC})">passing</span></div>
      </div>
      <div style="flex:1">
        {htitle("Tests are the contract","0 FAILING")}
        {leds}
        {cap("it writes them, runs them, fixes red. you see it only green.")}
      </div></div>'''

# 6. REVIEW - IVORY: a dimensional REVIEWED stamp + 3 raised finding chips (caught -> fixed).
def review():
    finds=[("Edge case missed","handled"),("Silent failure","surfaced"),("Untested path","covered")]
    chips=""
    for bad,good in finds:
        chips+=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.6);border:1px solid rgba(120,95,60,.18);border-radius:15px;padding:14px 18px;box-shadow:0 12px 22px rgba(120,95,60,.12)">'
          f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(150,90,45,.12)"/><path d="M7 12.4l3.2 3.2L17 8.4" fill="none" stroke="#96562d" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="font-family:DM Sans;font-size:18px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)">{bad}</span>'
          f'<span style="font-family:DM Mono;font-size:15px;color:#a05030">-&gt;</span>'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#2a2016">{good}</span></div>')
    seal="".join(f'<line x1="145" y1="145" x2="{145+128*math.cos(math.radians(a)):.0f}" y2="{145+128*math.sin(math.radians(a)):.0f}" stroke="#8a4c2c" stroke-width="10"/>' for a in range(0,360,15))
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("It reviews its own work","SELF-CAUGHT")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex:1;display:flex;flex-direction:column;gap:14px">{chips}</div>
        <div style="flex-shrink:0">
          <svg width="290" height="290" viewBox="0 0 290 290">
            <defs>
              <radialGradient id="sl" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
              <radialGradient id="slb" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.4)"/><stop offset="62%" stop-color="rgba(204,120,92,.10)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
              <filter id="slsh" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="rgba(120,80,40,.4)"/></filter>
              <filter id="slsp" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="8"/></filter>
            </defs>
            <circle cx="145" cy="145" r="140" fill="url(#slb)"/>
            <g filter="url(#slsh)">{seal}<circle cx="145" cy="145" r="118" fill="url(#sl)"/></g>
            <circle cx="145" cy="145" r="118" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
            <circle cx="145" cy="145" r="96" fill="none" stroke="rgba(26,15,10,.28)" stroke-width="2"/>
            <path d="M108 148 l24 24 l50 -58" fill="none" stroke="#1a0f0a" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
            <ellipse cx="110" cy="98" rx="44" ry="24" fill="rgba(255,255,255,.28)" filter="url(#slsp)" transform="rotate(-32 110 98)"/>
            <text x="145" y="214" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="19" letter-spacing="4" fill="#1a0f0a">REVIEWED</text>
          </svg>
        </div>
      </div>
      {cap("three issues caught and fixed before a human opened the pull request.","#8a745a")}</div>'''

# 7. SHIP - isometric stack of commit/test/PR cards ending in a merged pill.
def ship():
    steps=[("BRANCH","feat/invoice-export"),("TESTS","42 passed, 0 failed"),("PULL REQUEST","opened, described, ready")]
    cards=""
    for i,(nm,sub) in enumerate(steps):
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("It opens the pull request","BRANCH · PR · MERGE")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:120px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Merged &#10003; PR #182</div></div></div>
      {cap("branch, tests, description, PR. a senior loop from one plain-English line.")}</div>'''

# 8. VERSUS - split compare: vague junior column vs spec'd senior column, verdict below.
def versus():
    jr=["Guesses your intent","Skips the tests","You find the bugs","You review every line"]
    sr=["Specs it first","Ships it green","Reviews itself","Opens a clean PR"]
    def col(items,accent,head,tagcol):
        rows=""
        for it in items:
            mark=(f'<svg width="20" height="20" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
                  if accent else f'<svg width="20" height="20" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M7 7l10 10M17 7l-10 10" stroke="rgb({RED})" stroke-width="2.6" stroke-linecap="round"/></svg>')
            tc="#FAFAF7" if accent else "#8f8f85"
            rows+=f'<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span>{mark}</span><span style="font-family:DM Sans;font-size:18px;color:{tc}">{it}</span></div>'
        bd=f"rgb({ACC})" if accent else "rgba(255,255,255,.10)"
        glow="box-shadow:0 0 32px rgba(212,162,127,.18);" if accent else ""
        bg="linear-gradient(160deg,#3a342d,#221f1b)" if accent else "#211e1a"
        return (f'<div style="flex:1;background:{bg};border:1.5px solid {bd};border-radius:20px;padding:20px 24px 8px;{glow}">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:{tagcol};margin-bottom:6px">{head}</div>{rows}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Junior prompt vs senior system","SENTINEL")}
      <div style="position:relative;display:flex;align-items:stretch;gap:56px">
        {col(jr,False,"VAGUE PROMPT","#a05030")}
        {col(sr,True,"SPEC'D SYSTEM",f"rgb({ACC})")}
        <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:56px;height:56px;border-radius:50%;background:#1a1816;border:1.5px solid rgba(212,162,127,.5);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:17px;color:rgb({ACC})">VS</div>
      </div>
      <div style="margin-top:18px;background:rgba(212,162,127,.08);border:1px solid rgba(212,162,127,.3);border-radius:14px;padding:14px 20px;text-align:center;font-family:DM Sans;font-weight:700;font-size:19px;color:#e6d6c2">SENTINEL is the code agent inside Ultron. Senior by default, gated by you.</div>
      {cap("one is a chatbot you keep correcting. the other you just approve.")}</div>'''

PANELS={"ladder":ladder(),"spec":spec(),"plan":plan(),"memory":memory(),
        "tests":tests(),"review":review(),"ship":ship(),"versus":versus()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src21"; os.makedirs(outd,exist_ok=True)
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
