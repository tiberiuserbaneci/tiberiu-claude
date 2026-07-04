#!/usr/bin/env python3
# TIER 3 - HOW REAL AGENTS ARE BUILT, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO generic
# stat-chip strips. Clean rounded cards only (CARD / CARDIV) - no clip-path, no side-walls.
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

# 1. REACT - the reasoning loop drawn as a true circular flow: THINK -> ACT -> OBSERVE -> back
def react():
    cx,cy,R=310,235,150
    nodes=[("THINK","reasons about the goal",-90),("ACT","calls one tool",30),("OBSERVE","reads what came back",150)]
    nb=""
    for nm,sub,a in nodes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        on=(nm=="THINK")
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.12)"
        nb+=(f'<g><rect x="{x-84:.0f}" y="{y-38:.0f}" width="168" height="76" rx="18" fill="#2a2622" stroke="{bd}" stroke-width="{2.4 if on else 1.4}"/>'
             f'<rect x="{x-84:.0f}" y="{y-38:.0f}" width="168" height="76" rx="18" fill="url(#nf)" opacity="{0.9 if on else 0.55}"/>'
             f'<text x="{x:.0f}" y="{y-6:.0f}" text-anchor="middle" font-family="DM Mono" font-size="16" letter-spacing=".14em" fill="{"#FAFAF7" if on else "#e2dccf"}">{nm}</text>'
             f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Sans" font-size="13.5" fill="#9a9488">{sub}</text></g>')
    arcs=""
    for a1,a2 in ((-90,30),(30,150),(150,270)):
        sa=math.radians(a1+26); ea=math.radians(a2-26)
        x1=cx+R*math.cos(sa); y1=cy+R*math.sin(sa); x2=cx+R*math.cos(ea); y2=cy+R*math.sin(ea)
        arcs+=f'<path d="M{x1:.0f} {y1:.0f} A{R} {R} 0 0 1 {x2:.0f} {y2:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="3.5" marker-end="url(#ah)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Think, act, look. Then think again","REACT LOOP")}
      <svg width="620" height="470" viewBox="0 0 620 470" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="nf" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(255,255,255,.06)"/><stop offset="100%" stop-color="rgba(0,0,0,.2)"/></linearGradient>
          <marker id="ah" markerWidth="11" markerHeight="11" refX="7" refY="5.5" orient="auto"><path d="M1 1 L9 5.5 L1 10 Z" fill="rgb({ACC})"/></marker>
        </defs>
        {arcs}{nb}
        <circle cx="{cx}" cy="{cy}" r="46" fill="#211d19" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="rgb({ACC})">x4</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".08em" fill="#8f8f85">till done</text>
      </svg>
      {cap("real agents reason before every tool call and check what came back.")}</div>'''

# 2. CODEACT - a git-merge graph: SENTINEL writes on a branch, tests pass, merged to main
def codeact():
    W,H=820,430
    yb,ym=300,150   # base(main) lane, merge(branch) lane
    commits=[("write the fix",180),("run the tests",370),("build passes",560)]
    dots=""
    for nm,x in commits:
        dots+=(f'<circle cx="{x}" cy="{ym}" r="15" fill="#2a2622" stroke="rgb({ACC})" stroke-width="3"/>'
               f'<circle cx="{x}" cy="{ym}" r="6" fill="rgb({ACC})"/>'
               f'<text x="{x}" y="{ym-34}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It does not describe fixes. It merges them","SENTINEL")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="mg" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mgw" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        <line x1="40" y1="{yb}" x2="700" y2="{yb}" stroke="rgba(255,255,255,.18)" stroke-width="5"/>
        <circle cx="40" cy="{yb}" r="12" fill="#2a2622" stroke="rgba(255,255,255,.3)" stroke-width="2.5"/>
        <text x="40" y="{yb+38}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#8f8f85">main</text>
        <path d="M40 {yb} C120 {yb},120 {ym},200 {ym}" fill="none" stroke="rgb({ACC})" stroke-width="4"/>
        <line x1="200" y1="{ym}" x2="560" y2="{ym}" stroke="rgb({ACC})" stroke-width="4"/>
        <path d="M560 {ym} C660 {ym},640 {yb},700 {yb}" fill="none" stroke="rgb({ACC})" stroke-width="4"/>
        {dots}
        <g filter="url(#mgw)"><circle cx="700" cy="{yb}" r="42" fill="url(#mg)"/></g>
        <path d="M684 {yb} l11 11 l22 -26" fill="none" stroke="#1a0f0a" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="700" y="{yb+72}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">Merged</text>
        <text x="700" y="{yb+94}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">PR #182</text>
        <g transform="translate(300,{ym+58})"><rect x="0" y="0" width="230" height="52" rx="14" fill="#211d19" stroke="rgba(212,162,127,.3)"/>
          <circle cx="30" cy="26" r="13" fill="rgba(212,162,127,.16)"/><path d="M23 26.5 l5 5 l10 -12" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="56" y="32" font-family="DM Sans" font-weight="700" font-size="17" fill="#e6d6c2">42 passed &middot; 0 failed</text></g>
      </svg>
      {cap("plain english in, a tested pull request out - it writes it, not describes it.")}</div>'''

# 3. PLAN - IVORY: deep tier drafts the plan once, the light tier runs each step (cents)
def plan():
    steps=["profile the account","find the trigger","draft the opener","queue the follow-ups"]
    plancard=""
    for i,s in enumerate(steps):
        plancard+=(f'<div style="display:flex;align-items:center;gap:12px;padding:11px 0;border-bottom:{"1px solid rgba(120,95,60,.16)" if i<3 else "none"}">'
          f'<span style="flex-shrink:0;width:26px;height:26px;border-radius:8px;background:#96562d;color:#fff;font-family:DM Sans;font-weight:900;font-size:14px;display:flex;align-items:center;justify-content:center">{i+1}</span>'
          f'<span style="font-family:DM Sans;font-size:17px;color:#2a2016">{s}</span></div>')
    runcard=""
    for i,s in enumerate(steps):
        runcard+=(f'<div style="display:flex;align-items:center;gap:12px;padding:11px 0;border-bottom:{"1px solid rgba(120,95,60,.16)" if i<3 else "none"}">'
          f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(150,86,45,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="font-family:DM Sans;font-size:17px;color:#5a4634">{s}</span>'
          f'<span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:#a08a68">0.02c</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("Plan with the big brain. Run with the cheap one","PLAN / RUN","#2a2016")}
      <div style="display:flex;align-items:stretch;gap:20px">
        <div style="flex:1;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.16);border-radius:18px;padding:16px 20px">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#96562d">DEEP</span><span style="font-family:DM Sans;font-size:14px;color:#8a745a">plans once</span></div>
          {plancard}</div>
        <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13M12 6l6 6-6 6"/></svg>
          <span style="font-family:DM Mono;font-size:11px;color:#a08a68;margin-top:6px">hands off</span></div>
        <div style="flex:1;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.16);border-radius:18px;padding:16px 20px">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#96562d">LITE</span><span style="font-family:DM Sans;font-size:14px;color:#8a745a">runs each</span></div>
          {runcard}</div>
      </div>
      <div style="display:flex;align-items:center;gap:10px;margin-top:16px;background:rgba(150,86,45,.1);border-radius:12px;padding:12px 18px">
        <span style="font-family:DM Sans;font-weight:900;font-size:24px;color:#96562d">0.08c</span>
        <span style="font-family:DM Sans;font-size:16px;color:#5a4634">total for the whole run. cents, not seats.</span></div>
      {cap("one deep plan, four cheap steps - judgement where it counts, thrift everywhere else.","#8a745a")}</div>'''

# 4. REFLECT - IVORY: version stack scored against your bar, only v3 clears
def reflect():
    vers=[("v1",58,"first pass",False),("v2",71,"tightened",False),("v3",94,"cleared",True)]
    rows=""
    for nm,sc,note,ok in vers:
        w=int(sc/100*340)
        fill="#96562d" if ok else "rgba(200,70,35,.75)"
        mark=('<svg width="26" height="26" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="rgba(150,86,45,.16)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>' if ok
              else '<svg width="26" height="26" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="rgba(200,70,35,.12)"/><path d="M8 8l8 8M16 8l-8 8" fill="none" stroke="rgba(200,70,35,.85)" stroke-width="2.6" stroke-linecap="round"/></svg>')
        op="1" if ok else ".62"
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;opacity:{op}">'
          f'<span style="flex-shrink:0;width:44px;font-family:DM Mono;font-weight:500;font-size:18px;color:#2a2016">{nm}</span>'
          f'<div style="flex:1"><div style="height:16px;border-radius:8px;background:rgba(120,95,60,.14);overflow:hidden"><div style="width:{w}px;height:100%;border-radius:8px;background:{fill}"></div></div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8a745a;margin-top:4px">{note}</div></div>'
          f'<span style="flex-shrink:0;font-family:DM Sans;font-weight:900;font-size:26px;color:{"#2a2016" if ok else "#a08a68"}">{sc}</span>'
          f'<span style="flex-shrink:0">{mark}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("v1 never reaches you. v3 does","SELF-CRITIQUE","#2a2016")}
      <div style="background:rgba(255,255,255,.5);border:1px solid rgba(120,95,60,.16);border-radius:18px;padding:24px 28px;display:flex;flex-direction:column;gap:22px">
        <div style="display:flex;justify-content:flex-end"><span style="font-family:DM Mono;font-size:12px;color:#96562d;letter-spacing:.06em;border:1px dashed #96562d;border-radius:8px;padding:5px 12px">your bar &middot; 90</span></div>
        {rows}
      </div>
      {cap("it drafts, scores itself against your bar, and only ships the one that clears it.","#8a745a")}</div>'''

# 5. MULTI - a constellation of 7 named specialists around one chat hub
def multi():
    cx,cy,R=310,238,178
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    spokes=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="38" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven specialists beat one giant","SPECIALISTS")}
      <svg width="620" height="476" viewBox="0 0 620 476" style="display:block;margin:0 auto">
        <defs><radialGradient id="hubc" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hgw" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#hgw)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#hubc)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ONE CHAT</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">routes the job</text>
        {nodes}
      </svg>
      {cap("research, outbound, deals, content - one job each, done extremely well.")}</div>'''

# 6. STACK - the five patterns stacked into one isometric system
def stack():
    layers=[("REACT LOOP","reason then act",0),("CODEACT","writes and merges",1),
            ("PLAN / RUN","big brain, cheap hands",2),("SELF-CRITIQUE","only v3 ships",3),
            ("SPECIALISTS","seven agents, one job",4)]
    slabs=""
    for nm,sub,i in layers:
        y=(4-i)*96; top=(i==4)
        bg="linear-gradient(160deg,#4a4038,#2b2420)" if top else "linear-gradient(160deg,#3a352f,#26221e)"
        bd=f"rgb({ACC})" if top else "rgba(255,255,255,.12)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.32))" if top else ""
        slabs+=(f'<div style="position:absolute;left:0;top:{y}px;width:520px;{glow};'
          f'background:{bg};border:1.5px solid {bd};border-radius:16px;padding:16px 22px;'
          f'box-shadow:0 26px 40px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:18px">'
          f'<span style="flex-shrink:0;font-family:DM Sans;font-weight:900;font-size:30px;color:{"rgb("+ACC+")" if top else "rgba(212,162,127,.5)"}">{i+1}</span>'
          f'<div><div style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:{"#FAFAF7" if top else "#cfc9bd"}">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Real systems stack all five","COMPOSED")}
      <div style="perspective:2000px;height:494px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(24deg) rotateZ(-10deg);width:520px;height:460px;position:relative">{slabs}</div></div>
      {cap("ultron composes all five per job. you just type the goal.")}</div>'''

# 7. GATE - the sixth pattern: a human tap held between the agent and the one external action
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Pattern six: a human on the trigger","HUMAN GATE")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="ag" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="agw" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#agw)"><circle cx="150" cy="215" r="104" fill="url(#ag)"/></g>
        <text x="150" y="208" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">AGENT</text>
        <text x="150" y="238" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".1em">ready to send</text>
        <path d="M258 215 H366" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="372" y="145" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(414,183)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="442" y="320" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
        <path d="M518 215 H610" stroke="rgba(212,162,127,.35)" stroke-width="4" stroke-dasharray="6 8" stroke-linecap="round"/>
        <rect x="614" y="160" width="176" height="110" rx="20" fill="#211d19" stroke="rgba(255,255,255,.1)"/>
        <text x="702" y="196" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#e6d6c2">Send 240</text>
        <text x="702" y="220" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#e6d6c2">emails</text>
        <text x="702" y="250" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#c84623">HELD</text>
      </svg>
      {cap("the most reliable design keeps one human on the only external trigger.")}</div>'''

# 8. OPERATOR - outcome split: one model core, structured into different company workforces
def operator():
    def col(roles):
        cards=""
        for r in roles:
            cards+=(f'<div style="background:linear-gradient(160deg,#332f2a,#221e1a);border:1px solid rgba(255,255,255,.1);border-radius:13px;'
              f'padding:11px 16px;margin-bottom:10px;display:flex;align-items:center;gap:11px">'
              f'<span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});flex-shrink:0"></span>'
              f'<span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#e6e0d6">{r}</span></div>')
        return cards
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Same models. Different companies","WORKFORCE")}
      <div style="display:flex;align-items:center;gap:24px">
        <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:12px">
          <div style="width:150px;height:150px;border-radius:26px;background:radial-gradient(circle at 36% 30%,#f0c49e,rgb({ACC}) 55%,#7a4326);
            display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(212,162,127,.4)">
            <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a160c">SAME</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a160c">MODELS</span></div>
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13M12 6l6 6-6 6"/></svg>
          <span style="font-family:DM Mono;font-size:11px;color:#8f8f85">structured</span>
        </div>
        <div style="flex:1;display:flex;gap:18px">
          <div style="flex:1;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:18px;padding:16px 14px">
            <div style="font-family:DM Sans;font-weight:900;font-size:16px;color:#FAFAF7;text-align:center;margin-bottom:6px">SaaS startup</div>
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});text-align:center;margin-bottom:12px">OUTBOUND</div>
            {col(["SDR","Researcher","Closer"])}</div>
          <div style="flex:1;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);border-radius:18px;padding:16px 14px">
            <div style="font-family:DM Sans;font-weight:900;font-size:16px;color:#FAFAF7;text-align:center;margin-bottom:6px">Agency</div>
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});text-align:center;margin-bottom:12px">DELIVERY</div>
            {col(["Writer","Analyst","Account PM"])}</div>
        </div>
      </div>
      {cap("the same models, structured right, become a workforce.")}</div>'''

PANELS={"react":react(),"codeact":codeact(),"plan":plan(),"reflect":reflect(),
        "multi":multi(),"stack":stack(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/patterns"; os.makedirs(outd,exist_ok=True)
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
