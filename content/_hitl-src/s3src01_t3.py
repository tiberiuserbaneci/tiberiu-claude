#!/usr/bin/env python3
# TIER 3 - THE FIVE SURFACES OF CLAUDE, built to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, htitle + one-line cap, NO generic stat-chip
# strips. Source: "5 Claude tools to learn in 2026" (Chat / Projects / Cowork / Skills / Code) -
# re-told as Ultron: most people stop at the chat box, operators climb all five surfaces.
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

LOCK='<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#6f6a60" stroke-width="2"><rect x="4.5" y="11" width="15" height="9.5" rx="2.2"/><path d="M8 11V7.6a4 4 0 0 1 8 0V11"/></svg>'
def burst(col,s=34):
    sp=""
    for k in range(12):
        a=math.radians(k*30); x1=12+3.2*math.cos(a); y1=12+3.2*math.sin(a); x2=12+9.2*math.cos(a); y2=12+9.2*math.sin(a)
        sp+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="2.1" stroke-linecap="round"/>'
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24">{sp}</svg>'

# 1. FLOOR - a shelf of 5 surface tiles, only CHAT lit, the other four dark and locked
def floor():
    tiles=[("CHAT",True),("PROJECTS",False),("COWORK",False),("SKILLS",False),("CODE",False)]
    cells=""
    for nm,on in tiles:
        if on:
            face=('background:linear-gradient(158deg,#e0955f,#b8521f);border:1px solid rgba(255,255,255,.28);'
                  'box-shadow:0 22px 40px rgba(184,82,31,.42), inset 0 2px 3px rgba(255,255,255,.34)')
            icon=burst("#fff")
            here=f'<div style="font-family:DM Mono;font-size:10.5px;letter-spacing:.1em;color:rgb({ACC});margin-top:9px">YOU ARE HERE</div>'
            lab='#FAFAF7'
        else:
            face='background:#242018;border:1px solid rgba(255,255,255,.06);box-shadow:inset 0 -8px 18px rgba(0,0,0,.4)'
            icon=LOCK
            here='<div style="height:22px"></div>'
            lab='#6f6a60'
        cells+=(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center">'
          f'<div style="width:100%;height:150px;border-radius:22px;{face};display:flex;align-items:center;justify-content:center">{icon}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:16px;color:{lab};margin-top:13px">{nm}</div>{here}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Everyone lives in one box","1 OF 5 SURFACES")}
      <div style="display:flex;gap:16px;align-items:flex-start;height:250px;padding-top:34px">{cells}</div>
      {cap("chat is the ground floor. four whole surfaces sit locked above it.")}</div>'''

# 2. CHAT (surface 01) - IVORY plain chat window: one question, one answer, then it forgets
def chat():
    win=('<div style="width:560px;margin:0 auto;background:#fff;border:1px solid rgba(120,95,60,.18);border-radius:20px;'
      'box-shadow:0 26px 46px rgba(120,95,60,.20);overflow:hidden">'
      '<div style="display:flex;align-items:center;gap:9px;padding:16px 20px;border-bottom:1px solid rgba(120,95,60,.12)">'
      '<span style="width:11px;height:11px;border-radius:50%;background:#e0955f"></span>'
      '<span style="font-family:DM Mono;font-size:13px;color:#96562d">new chat</span>'
      '<span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:#b7a690">stateless</span></div>'
      '<div style="padding:24px 22px 26px;display:flex;flex-direction:column;gap:16px">'
      '<div style="align-self:flex-end;max-width:74%;background:#f0e6d6;border-radius:16px 16px 4px 16px;padding:13px 17px;font-family:DM Sans;font-size:17px;color:#2a2016">Rewrite this email shorter.</div>'
      '<div style="display:flex;gap:12px;align-items:flex-start;max-width:82%">'
      f'<div style="flex-shrink:0;width:38px;height:38px;border-radius:11px;background:linear-gradient(158deg,#e0955f,#b8521f);display:flex;align-items:center;justify-content:center">{burst("#fff",22)}</div>'
      '<div style="background:#faf4ea;border:1px solid rgba(120,95,60,.14);border-radius:16px 16px 16px 4px;padding:13px 17px;font-family:DM Sans;font-size:17px;color:#2a2016;line-height:1.4">Here is a tighter version, three lines and a clear ask.</div></div>'
      '<div style="display:flex;align-items:center;gap:8px;margin-top:4px;padding-top:14px;border-top:1px dashed rgba(120,95,60,.22)">'
      '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#c84623" stroke-width="2.2"><path d="M3 6h18M8 6V4h8v2M6 6l1 15h10l1-15"/></svg>'
      '<span style="font-family:DM Mono;font-size:12.5px;color:#a88a72">closes the tab, remembers nothing</span></div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("Type a question, get an answer","SURFACE 01",ink="#2a2016")}
      <div style="padding-top:6px">{win}</div>
      {cap("fast and stateless. a brilliant answer machine with no memory of you.","#8a745a")}</div>'''

# 3. PROJECTS (surface 02) - a project header with pinned context chips feeding a memory ring
def projects():
    chips=["ICP profile","Pricing sheet","Brand voice","Pipeline","Positioning docs"]
    chipbar="".join(f'<div style="background:#221f1b;border:1px solid rgba(212,162,127,.30);border-radius:999px;padding:9px 16px;font-family:DM Sans;font-size:15px;color:#d9d5cc;display:flex;align-items:center;gap:8px"><span style="width:7px;height:7px;border-radius:50%;background:rgb({ACC})"></span>{c}</div>' for c in chips)
    r=70; circ=2*math.pi*r; dash=circ
    ring=(f'<svg width="180" height="180" viewBox="0 0 180 180">'
      f'<circle cx="90" cy="90" r="{r}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="14"/>'
      f'<circle cx="90" cy="90" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="14" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 90 90)"/></svg>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A chat box that remembers you","SURFACE 02")}
      <div style="display:flex;gap:30px;align-items:center;height:400px">
        <div style="flex:1">
          <div style="display:flex;align-items:center;gap:12px;background:linear-gradient(160deg,#332c25,#241f1a);border:1px solid rgba(255,255,255,.09);border-radius:18px;padding:16px 20px;margin-bottom:18px">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><path d="M3 7a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
            <span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">Q2 Launch</span>
            <span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:rgb({ACC})">pinned once</span></div>
          <div style="display:flex;flex-wrap:wrap;gap:12px">{chipbar}</div>
        </div>
        <div style="flex-shrink:0;position:relative;width:180px;height:180px">
          {ring}
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7">100%</span>
            <span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">context held</span></div></div>
      </div>
      {cap("your docs, icp and voice pinned once. every reply starts already briefed.")}</div>'''

# 4. COWORK (surface 03) - radial hub of 7 Ultron agents reaching into a stack of real files
def cowork():
    cx,cy=210,215; R=155
    agents=[("CORTEX",-90),("SPECTER",-38),("STRIKER",14),("PULSE",66),("SENTINEL",118),("AMPLIFY",170),("COUNSEL",222)]
    spokes=""; nodes=""
    for nm,a in agents:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="26" fill="#221f1b" stroke="rgba(212,162,127,.4)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#d9d5cc">{nm}</text>')
    files=""
    for i,fn in enumerate(["deals.csv","brief.md","site.tsx"]):
        yy=150+i*70
        files+=(f'<div style="position:absolute;left:0;top:{yy}px;width:290px;background:linear-gradient(160deg,#3a332c,#2a241f);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:14px 18px;box-shadow:0 18px 30px rgba(0,0,0,.5);display:flex;align-items:center;gap:12px">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><path d="M6 2h9l5 5v15H6z"/><path d="M15 2v5h5"/></svg>'
          f'<span style="font-family:DM Mono;font-size:15px;color:#e4e0d6">{fn}</span>'
          f'<span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:rgb({ACC})">edited</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="430" height="430" viewBox="0 0 430 430">
        <defs><radialGradient id="hb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}<g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#hb)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">COWORK</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">7 agents</text>
        {nodes}</svg>
      <div style="flex:1;position:relative;height:400px">
        {htitle("An agent that works your files","SURFACE 03")}
        <div style="position:relative;height:330px">{files}</div>
        {cap("seven named agents, each owning a job, editing your real workspace.")}
      </div></div>'''

# 5. SKILLS (surface 04) - IVORY: a skill capsule slotting into a socket, reused forever
def skills():
    steps=["how you qualify a lead","your objection library","your close-plan template"]
    taught="".join(f'<div style="display:flex;align-items:center;gap:11px"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:17px;color:#5a4634">{s}</span></div>' for s in steps)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Teach your process once","SURFACE 04",ink="#2a2016")}
      <div style="display:flex;gap:34px;align-items:center;height:390px">
        <div style="flex-shrink:0;width:280px;height:340px;position:relative">
          <svg width="280" height="340" viewBox="0 0 280 340">
            <defs><linearGradient id="cap" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e0955f"/><stop offset="100%" stop-color="#b8521f"/></linearGradient>
            <filter id="cg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgba(184,82,31,.4)"/></filter></defs>
            <rect x="52" y="196" width="176" height="118" rx="20" fill="none" stroke="rgba(150,90,45,.32)" stroke-width="3" stroke-dasharray="7 8"/>
            <text x="140" y="336" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#96562d">SKILL SOCKET</text>
            <g filter="url(#cg)"><rect x="78" y="60" width="124" height="150" rx="30" fill="url(#cap)"/></g>
            <rect x="78" y="60" width="124" height="150" rx="30" fill="none" stroke="rgba(255,255,255,.3)" stroke-width="1.5"/>
            <g transform="translate(140,120)"><g transform="translate(-13,-13)">{ "".join(f'<line x1="13" y1="13" x2="{13+9*math.cos(math.radians(k*30)):.1f}" y2="{13+9*math.sin(math.radians(k*30)):.1f}" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' for k in range(12)) }</g></g>
            <text x="140" y="176" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#fff2e6">taught once</text>
            <path d="M140 214 v18" stroke="#96562d" stroke-width="3" stroke-dasharray="3 6" stroke-linecap="round"/></svg>
        </div>
        <div style="flex:1">
          <div style="display:flex;flex-direction:column;gap:15px;margin-bottom:22px">{taught}</div>
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:16px 20px">
            <div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#2a2016">reused 340x</div>
            <div style="font-family:DM Mono;font-size:13px;color:#96562d">never re-explained</div></div>
        </div>
      </div>
      {cap("onboard claude to how you work once, then it runs your way on every task.","#8a745a")}</div>'''

# 6. CODE (surface 05) - isometric plain-English -> build -> ship ending in a live app window
def code():
    steps=[("PROMPT",'"build a pricing page"',0),("BUILD","SENTINEL writes it",1),("SHIP","live on your domain",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*126
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:540px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:19px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><span style="font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC})">{i+1}</span></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Describe software, it builds it","SURFACE 05")}
      <div style="perspective:1900px;height:460px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:540px;height:420px;position:relative">{cards}
          <div style="position:absolute;left:96px;top:392px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Deployed &#10003; no engineer</div></div></div>
      {cap("plain english in, a shipped product out. tested before it goes live.")}</div>'''

# 7. ROUTER - one job walks in, the router sends it to the right surface (5 lanes, one lit)
def router():
    lanes=[("CHAT","quick answer",90,False),("PROJECTS","needs context",170,False),("COWORK","touch my files",250,True),("SKILLS","my process",330,False),("CODE","build it",410,False)]
    hubx,hy=150,250
    edges=""; cards=""
    for nm,role,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.4
        edges+=f'<path d="M{hubx+58} {hy} C300 {hy},320 {y},470 {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 20px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:11.5px;color:rgb({ACC})">routed</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:300px;top:{y-32}px;width:150px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:14px;padding:12px 15px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:12.5px;letter-spacing:.1em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85;margin-top:3px">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("The right surface, chosen for you","WHEN TO USE EACH")}
      <div style="position:relative;height:480px">
        <svg width="820" height="480" viewBox="0 0 820 480" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="8" y="{hy-26}" width="86" height="52" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>
          <g filter="url(#hg2)"><circle cx="{hubx}" cy="{hy}" r="58" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+15}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">reads the job</text></svg>
        <div style="position:absolute;left:10px;top:228px;width:82px;font-family:DM Mono;font-size:11.5px;color:#c9c3b8;text-align:center">one job</div>
        {cards}
      </div>
      {cap("you never pick the surface. the router reads the job and opens the right one.")}</div>'''

# 8. CLIMB - ascending staircase of the 5 surfaces to a lit summit, all rungs on
def climb():
    names=["CHAT","PROJECTS","COWORK","SKILLS","CODE"]
    x0=40; bw=138; gap=14; baseY=418
    blocks=""; tops=[]
    for i,nm in enumerate(names):
        h=110+i*66; x=x0+i*(bw+gap); y=baseY-h; lit=i==4
        top=f"rgb({ACC})" if lit else f"rgba(212,162,127,{0.4+i*0.13:.2f})"
        blocks+=(f'<rect x="{x}" y="{y}" width="{bw}" height="{h}" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.08)"/>'
          f'<rect x="{x}" y="{y}" width="{bw}" height="12" rx="6" fill="{top}"/>'
          f'<text x="{x+bw/2:.0f}" y="{baseY-16}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".06em" fill="#cfc9bd" transform="rotate(-90 {x+bw/2:.0f} {baseY-16})">{nm}</text>'
          f'<text x="{x+bw/2:.0f}" y="{y-14}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#8f8f85">0{i+1}</text>')
        tops.append((x+bw/2,y))
    path="M"+" L".join(f"{px:.0f} {py-2:.0f}" for px,py in tops)
    lx,ly=tops[-1]
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Operators climb all five","THE FULL LADDER")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="sum" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        <path d="{path}" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="2.5" stroke-dasharray="4 7"/>
        {blocks}
        <g filter="url(#sg)"><circle cx="{lx:.0f}" cy="{ly-46:.0f}" r="30" fill="url(#sum)"/></g>
        <text x="{lx:.0f}" y="{ly-41:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#1a0f0a">YOU</text></svg>
      {cap("chat, projects, cowork, skills, code. each rung compounds the one below it.")}</div>'''

PANELS={"floor":floor(),"chat":chat(),"projects":projects(),"cowork":cowork(),
        "skills":skills(),"code":code(),"router":router(),"climb":climb()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src01"; os.makedirs(outd,exist_ok=True)
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
