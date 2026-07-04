#!/usr/bin/env python3
# TIER 3 - THE MISSING FIFTH. Angle: Claude Code got you 80%. The last fifth (memory, roster,
# router, gate) is what turns a raw model into an operator. 8 unique hand-built coded scenes on
# clean rounded CARD/CARDIV, htitle + one cap each, warm palette. No generic stat-chip strips.
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

# 1. GAP - donut gauge: 80% built (ivory), the last 20% wedge glows accent = the operator layer
def gap():
    r=150; circ=2*math.pi*r; done=circ*0.80; miss=circ*0.20; cx,cy=306,225
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You did the hard part","80 / 20")}
      <svg width="612" height="460" viewBox="0 0 612 460" style="display:block;margin:0 auto">
        <defs><filter id="gg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="13" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,.05)" stroke-width="42"/>
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(250,250,247,.28)" stroke-width="42" stroke-dasharray="{done:.1f} {circ:.1f}" transform="rotate(-90 {cx} {cy})"/>
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="42" stroke-dasharray="{miss:.1f} {circ:.1f}" stroke-dashoffset="{-done:.1f}" transform="rotate(-90 {cx} {cy})" filter="url(#gg)"/>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="72" fill="#FAFAF7">80%</text>
        <text x="{cx}" y="{cy+28}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".14em" fill="#8f8f85">ALREADY BUILT</text>
        <line x1="200" y1="70" x2="248" y2="120" stroke="rgb({ACC})" stroke-width="2" stroke-dasharray="3 5"/>
        <text x="196" y="58" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})">+20% THE LAST FIFTH</text>
      </svg>
      <div style="display:flex;gap:14px;margin-top:6px">
        <div style="flex:1;display:flex;align-items:center;gap:10px"><span style="width:15px;height:15px;border-radius:4px;background:rgba(250,250,247,.28);flex-shrink:0"></span><span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">model, scraper, workflow</span></div>
        <div style="flex:1;display:flex;align-items:center;gap:10px"><span style="width:15px;height:15px;border-radius:4px;background:rgb({ACC});flex-shrink:0"></span><span style="font-family:DM Sans;font-size:16px;color:#FAFAF7">memory, roster, router, gate</span></div>
      </div>
      {cap("the model is the hard 80. the operator layer is the last fifth.")}</div>'''

# 2. RAW MODEL - a terminal window (pure capability) with 4 empty, unwired dock sockets
def haveit():
    ports=[("MEMORY","forgets"),("ROSTER","one worker"),("ROUTER","you pick"),("GATE","no brake")]
    socks=""
    for i,(nm,st) in enumerate(ports):
        x=i*208
        socks+=(f'<div style="position:absolute;left:{x}px;top:0;width:184px">'
          f'<div style="height:20px;border-left:1.5px dashed rgba(200,70,35,.5);margin:0 auto 0;width:0"></div>'
          f'<div style="border:1.5px dashed rgba(200,70,35,.45);border-radius:16px;padding:16px 14px;background:rgba(200,70,35,.05);text-align:center">'
          f'<div style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#b9b3a8">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:rgb(200,70,35);margin-top:5px">{st}</div>'
          f'<div style="margin-top:8px;font-family:DM Mono;font-size:12px;color:rgb(200,70,35)">not wired</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Raw power, nothing wired","THE MODEL")}
      <div style="margin:6px auto 26px;width:560px;background:#141311;border:1px solid rgba(255,255,255,.1);border-radius:16px;box-shadow:0 30px 54px rgba(0,0,0,.6), inset 0 1px 2px rgba(255,255,255,.08);overflow:hidden">
        <div style="display:flex;align-items:center;gap:8px;padding:12px 16px;background:#201d1a;border-bottom:1px solid rgba(255,255,255,.07)">
          <span style="width:11px;height:11px;border-radius:50%;background:#3a352f"></span><span style="width:11px;height:11px;border-radius:50%;background:#3a352f"></span><span style="width:11px;height:11px;border-radius:50%;background:#3a352f"></span>
          <span style="margin-left:10px;font-family:DM Mono;font-size:13px;color:#8f8f85">claude-code &#183; raw model</span>
          <span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:6px;padding:3px 8px">80% DONE</span></div>
        <div style="padding:20px 22px;font-family:DM Mono;font-size:16px;line-height:1.85;color:#d9d5cc">
          <div><span style="color:rgb({ACC})">&gt;_</span> you have the model</div>
          <div><span style="color:rgb({ACC})">&gt;_</span> it can code, scrape, reason</div>
          <div><span style="color:rgb({ACC})">&gt;_</span> pure capability<span style="display:inline-block;width:11px;height:20px;background:rgb({ACC});margin-left:4px;vertical-align:-3px"></span></div></div></div>
      <div style="position:relative;height:118px">{socks}</div>
      {cap("a terminal is one worker with no memory, no team, no router, no brake.")}</div>'''

# 3. MEMORY (ivory) - a ledger of remembered facts every session reads from
def memory():
    rows=[("ICP","Founders, 2-50, IT / software, US + UK"),("PIPELINE","18 open, 4 in proposal"),
          ("PRICING","Max 19, Enterprise 297 per seat"),("DOCS","architecture, bcp, techniques"),
          ("HISTORY","last 40 chats, indexed")]
    rr=""
    for nm,v in rows:
        rr+=(f'<div style="display:flex;align-items:center;gap:16px;padding:14px 0;border-bottom:1px solid rgba(150,120,80,.16)">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3" style="flex-shrink:0"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="font-family:DM Mono;font-size:15px;letter-spacing:.08em;color:#96562d;width:118px;flex-shrink:0">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:18px;color:#2a2016">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("It never forgets your company","THE VAULT","#2a2016")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1">{rr}</div>
        <div style="flex-shrink:0;width:150px;border-left:3px solid #96562d;padding-left:18px;display:flex;flex-direction:column;justify-content:center;gap:12px">
          {"".join(f'<div style="font-family:DM Mono;font-size:14px;color:#5a4634">session {s}</div><div style="font-family:DM Mono;font-size:12px;color:#96562d">reads here</div>' for s in ("1","2","3"))}
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016;margin-top:4px">all one core</div></div>
      </div>
      {cap("raw chats start from zero. the vault carries you into every new session.","#8a745a")}</div>'''

# 4. ROSTER - the 7 named agents; the one you already run lit, six specialists added
def roster():
    ag=[("CORTEX","research","the ranked brief",0),("SPECTER","outbound","cold email + sequences",0),
        ("STRIKER","deals","objections, close plans",0),("PULSE","content","posts in your voice",0),
        ("SENTINEL","code","reads, ships the PR",1),("AMPLIFY","publishing","per channel + time zone",0),
        ("COUNSEL","legal","NDAs, MSAs, term sheets",0)]
    rr=""
    for nm,role,desc,have in ag:
        bd="rgb(212,162,127)" if have else "rgba(255,255,255,.09)"
        bg="linear-gradient(120deg,#3a332c,#241f1a)" if have else "#201d19"
        mono=nm[0]
        tag=(f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">you run this</span>' if have
             else '<span style="font-family:DM Mono;font-size:12px;color:#7a746a">+ added</span>')
        rr+=(f'<div style="display:flex;align-items:center;gap:16px;background:{bg};border:1.5px solid {bd};border-radius:14px;padding:11px 16px">'
          f'<div style="flex-shrink:0;width:38px;height:38px;border-radius:10px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:18px;color:rgb({ACC})">{mono}</div>'
          f'<span style="font-family:DM Mono;font-size:15px;letter-spacing:.1em;color:#FAFAF7;width:112px;flex-shrink:0">{nm}</span>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:16px;color:#c9c3b8;width:104px;flex-shrink:0">{role}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:#8f8f85;flex:1">{desc}</span>{tag}</div>')
    return f'''<div style="width:900px;{CARD};padding:32px 40px 32px">
      {htitle("One worker becomes seven","THE ROSTER")}
      <div style="display:flex;flex-direction:column;gap:9px">{rr}</div>
      {cap("you already have the coder. the last fifth hands you six more specialists.")}</div>'''

# 5. ROUTER - one job forks into the picked agent AND the priced model tier
def router():
    agents=[("CORTEX",90),("SPECTER",150),("STRIKER",210)]; pick_a="SPECTER"
    tiers=[("LITE","0.02c",300),("SMART","0.11c",360),("DEEP","0.40c",420)]; pick_t="SMART"
    hx,hy=300,255
    ag=""
    for nm,y in agents:
        on=nm==pick_a; col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=4.5 if on else 2
        ag+=f'<path d="M{hx} {hy} C{hx+70} {hy},520 {y},560 {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.1)"; tc="#FAFAF7" if on else "#8f8f85"
        gl="filter:drop-shadow(0 0 16px rgba(212,162,127,.35))" if on else ""
        ag+=(f'<g transform="translate(560,{y-22})" style="{gl}"><rect width="180" height="44" rx="12" fill="{"#3a332c" if on else "#201d19"}" stroke="{bd}" stroke-width="1.5"/>'
          f'<text x="16" y="28" font-family="DM Mono" font-size="15" letter-spacing=".1em" fill="{tc}">{nm}</text>'
          + (f'<text x="164" y="28" text-anchor="end" font-family="DM Mono" font-size="12" fill="rgb({ACC})">pick</text>' if on else '') + '</g>')
    tr=""
    for nm,cost,y in tiers:
        on=nm==pick_t; col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=4.5 if on else 2
        tr+=f'<path d="M{hx} {hy} C{hx+70} {hy},520 {y},560 {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.1)"; tc="#FAFAF7" if on else "#8f8f85"
        gl="filter:drop-shadow(0 0 16px rgba(212,162,127,.35))" if on else ""
        tr+=(f'<g transform="translate(560,{y-22})" style="{gl}"><rect width="180" height="44" rx="12" fill="{"#3a332c" if on else "#201d19"}" stroke="{bd}" stroke-width="1.5"/>'
          f'<text x="16" y="28" font-family="DM Mono" font-size="15" letter-spacing=".1em" fill="{tc}">{nm}</text>'
          f'<text x="164" y="28" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="16" fill="{tc}">{cost}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It hires the agent and prices it","THE ROUTER")}
      <svg width="760" height="480" viewBox="0 0 760 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="rh" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <rect x="8" y="{hy-30}" width="150" height="60" rx="13" fill="#221f1b" stroke="rgba(255,255,255,.1)"/>
        <text x="83" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#d9d5cc">draft 40</text>
        <text x="83" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">cold emails</text>
        <path d="M158 {hy} H236" stroke="rgba(212,162,127,.5)" stroke-width="3"/>
        {ag}{tr}
        <g filter="url(#rg)"><circle cx="{hx}" cy="{hy}" r="60" fill="url(#rh)"/></g>
        <text x="{hx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
        <text x="{hx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">reads the job</text>
        <text x="650" y="70" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#8f8f85">WHICH AGENT</text>
        <text x="650" y="288" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#8f8f85">WHICH TIER</text>
      </svg>
      {cap("one job in, the right specialist and the cheapest tier that can do it.")}</div>'''

# 6. GATE - outbound queued at a checkpoint bar; nothing passes without your tap
def gate():
    items=[("40 cold emails",130),("LinkedIn post",210),("PR #182",290)]
    q=""
    for nm,y in items:
        q+=(f'<g transform="translate(70,{y-26})"><rect width="230" height="52" rx="12" fill="#201d19" stroke="rgba(200,70,35,.4)" stroke-width="1.5"/>'
          f'<circle cx="26" cy="26" r="8" fill="none" stroke="rgb(200,70,35)" stroke-width="2.4"/><path d="M26 21 v6 M26 31 v.5" stroke="rgb(200,70,35)" stroke-width="2.4" stroke-linecap="round"/>'
          f'<text x="50" y="31" font-family="DM Sans" font-weight="700" font-size="16" fill="#c9c3b8">{nm}</text>'
          f'<text x="214" y="31" text-anchor="end" font-family="DM Mono" font-size="11" fill="rgb(200,70,35)">held</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <svg width="760" height="430" viewBox="0 0 760 430" style="display:block;margin:0 auto">
        <defs><filter id="tg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        <text x="185" y="72" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#8f8f85">QUEUED &#183; PENDING</text>
        {q}
        <line x1="410" y1="70" x2="410" y2="360" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round"/>
        <rect x="386" y="176" width="48" height="78" rx="12" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(396,192)"><rect x="0" y="20" width="28" height="22" rx="5" fill="none" stroke="rgb({ACC})" stroke-width="3.4"/><path d="M5 20 v-6 a9 9 0 0 1 18 0 v6" fill="none" stroke="rgb({ACC})" stroke-width="3.4"/></g>
        <path d="M470 215 H610" stroke="rgba(212,162,127,.35)" stroke-width="3" stroke-dasharray="2 11" stroke-linecap="round"/>
        <g filter="url(#tg)"><rect x="500" y="182" width="210" height="66" rx="16" fill="rgb({ACC})"/></g>
        <text x="605" y="214" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">APPROVE</text>
        <text x="605" y="238" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">your tap sends it</text>
        <text x="605" y="120" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">YOU DECIDE</text>
      </svg>
      {cap("every external move parks at the gate. powerful, never unsupervised.")}</div>'''

# 7. COMPARE (ivory) - raw = one layer; operator = five stacked layers
def compare():
    layers=[("HUMAN GATE","approval brake"),("MODEL ROUTER","agent + tier"),("AGENT ROSTER","seven specialists"),("MEMORY VAULT","never forgets"),("THE MODEL","raw capability")]
    st=""
    for i,(nm,sub) in enumerate(layers):
        base=i==len(layers)-1
        bg="linear-gradient(150deg,#fff,#f3ebdc)" if not base else "linear-gradient(150deg,#4a4038,#332b24)"
        bd="rgba(150,120,80,.28)" if not base else "rgba(255,255,255,.12)"
        tc="#2a2016" if not base else "#FAFAF7"; sc="#8a745a" if not base else "#c9c3b8"
        st+=(f'<div style="background:{bg};border:1.5px solid {bd};border-radius:14px;padding:14px 18px;box-shadow:0 12px 22px rgba(120,95,60,.14);display:flex;align-items:baseline;justify-content:space-between">'
          f'<span style="font-family:DM Mono;font-size:15px;letter-spacing:.08em;color:{tc}">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:{sc}">{sub}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      {htitle("One layer, or five that ship","RAW  VS  OPERATOR","#2a2016")}
      <div style="display:flex;gap:30px;align-items:stretch">
        <div style="width:250px;flex-shrink:0;display:flex;flex-direction:column">
          <div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:#96562d;margin-bottom:14px">RAW MODEL</div>
          <div style="flex:1;display:flex;align-items:center">
            <div style="width:100%;background:linear-gradient(150deg,#4a4038,#332b24);border:1.5px solid rgba(255,255,255,.12);border-radius:16px;padding:30px 22px;text-align:center;box-shadow:0 18px 30px rgba(120,95,60,.2)">
              <div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#FAFAF7">THE MODEL</div>
              <div style="font-family:DM Mono;font-size:13px;color:#c9c3b8;margin-top:6px">raw capability</div>
              <div style="font-family:DM Mono;font-size:12px;color:rgb(200,70,35);margin-top:14px">4 layers missing</div></div></div></div>
        <div style="flex:1">
          <div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:#96562d;margin-bottom:14px">OPERATOR &#183; THE LAST FIFTH ADDED</div>
          <div style="display:flex;flex-direction:column;gap:9px">{st}</div></div>
      </div>
      {cap("the raw model is layer one. memory, roster, router and gate stack on top.","#8a745a")}</div>'''

# 8. OPERATOR - raw model + four modules snap into one glowing operator
def operator():
    mods=[("MEMORY",96),("ROSTER",180),("ROUTER",264),("GATE",348)]
    ml=""
    for nm,y in mods:
        ml+=(f'<path d="M300 {y} C420 {y},470 222,548 222" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
          f'<rect x="110" y="{y-26}" width="190" height="52" rx="13" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.5"/>'
          f'<text x="205" y="{y+6}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".12em" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Snap on the last fifth","ONE OPERATOR")}
      <svg width="760" height="440" viewBox="0 0 760 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="ob" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="obg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        <rect x="14" y="196" width="86" height="52" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.12)"/>
        <text x="57" y="220" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">raw</text>
        <text x="57" y="236" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">model</text>
        {ml}
        <g filter="url(#obg)"><circle cx="600" cy="222" r="118" fill="url(#ob)"/></g>
        <text x="600" y="210" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">OPERATOR</text>
        <text x="600" y="244" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".06em">one login</text>
        <text x="600" y="380" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">memory &#183; roster &#183; router &#183; gate</text>
      </svg>
      {cap("snap the four onto claude code and the raw model becomes an operator.")}</div>'''

PANELS={"gap":gap(),"haveit":haveit(),"memory":memory(),"roster":roster(),
        "router":router(),"gate":gate(),"compare":compare(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src57"; os.makedirs(outd,exist_ok=True)
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
