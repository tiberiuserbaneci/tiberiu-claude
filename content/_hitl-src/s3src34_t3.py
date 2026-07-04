#!/usr/bin/env python3
# TIER 3 - FOUR PARTS, ONE AGENT. The four primitives that turn a chatbot into a working agent:
# Files (context) + Commands (skills) + Memory (vault) + Tools (actions), each a UNIQUE hand-built
# coded scene on a clean rounded card, title + one-line caption. Built to the WIRE-ITS-EYES bar.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tc=None):
    tc=tc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. ANATOMY - AGENT hub over 4 lit primitive nodes; a chatbot is only one box
def anatomy():
    prim=[("Files","context",110),("Commands","skills",300),("Memory","vault",490),("Tools","actions",680)]
    icon={
      "Files":'<path d="M6 3h8l6 6v12H6z" fill="none" stroke="ICO" stroke-width="1.9"/><path d="M14 3v6h6" fill="none" stroke="ICO" stroke-width="1.9"/>',
      "Commands":'<path d="M5 7l5 5-5 5M12 17h7" fill="none" stroke="ICO" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
      "Memory":'<rect x="4" y="5" width="16" height="14" rx="2" fill="none" stroke="ICO" stroke-width="1.9"/><path d="M9 5v6M13 5v6M17 5v6" stroke="ICO" stroke-width="1.9"/>',
      "Tools":'<path d="M14 6a4 4 0 0 0-5 5l-5 5 3 3 5-5a4 4 0 0 0 5-5l-3 3-2-2 2-2z" fill="none" stroke="ICO" stroke-width="1.9" stroke-linejoin="round"/>'}
    ox,oy=395,110; ny=300; nodes=""; edges=""
    for nm,role,x in prim:
        edges+=(f'<path d="M{ox} {oy+66} C{ox} 220,{x+75} 210,{x+75} {ny}" fill="none" stroke="rgb({ACC})" stroke-width="3" opacity=".7"/>')
        ico=icon[nm].replace("ICO",f"rgb({ACC})")
        nodes+=(f'<g transform="translate({x},{ny})">'
          f'<rect x="0" y="0" width="150" height="150" rx="22" fill="#242019" stroke="rgba(212,162,127,.32)" stroke-width="1.6"/>'
          f'<g transform="translate(55,26) scale(1.7)">{ico}</g>'
          f'<text x="75" y="110" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="21" fill="#FAFAF7">{nm}</text>'
          f'<text x="75" y="132" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".06em" fill="rgb({ACC})">{role}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Four parts, not one box","CHATBOT vs AGENT")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="ah" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ag" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}
        <g filter="url(#ag)"><circle cx="{ox}" cy="{oy}" r="66" fill="url(#ah)"/></g>
        <text x="{ox}" y="{oy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">AGENT</text>
        <text x="{ox}" y="{oy+18}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#3a2010">wires all four</text>
        <rect x="612" y="42" width="176" height="40" rx="12" fill="#221f1b" stroke="rgba(200,70,35,.4)"/>
        <line x1="628" y1="62" x2="644" y2="62" stroke="rgb(200,70,35)" stroke-width="2.4"/>
        <text x="700" y="67" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">chatbot = 1 of 4</text>
        {nodes}
      </svg>
      {cap("a chatbot answers. an agent has files, commands, memory and tools.")}</div>'''

# 2. FILES (IVORY) - a project directory tree read whole into one brief
def files():
    tree=[("workspace/",0,"fold"),("docs/",1,"fold"),("architecture.md",2,"f"),("pricing.md",2,"f"),
          ("icp.md",1,"f"),("pipeline.csv",1,"f"),("contracts/",1,"fold"),("msa-draft.pdf",2,"f")]
    rows=""
    for nm,depth,kind in tree:
        pad=depth*26
        glyph=('<svg width="17" height="17" viewBox="0 0 24 24" style="vertical-align:-3px"><path d="M3 6h6l2 2h10v11H3z" fill="rgba(150,90,45,.16)" stroke="#96562d" stroke-width="1.7"/></svg>'
               if kind=="fold" else
               '<svg width="15" height="17" viewBox="0 0 24 24" style="vertical-align:-3px"><path d="M6 3h8l5 5v13H6z" fill="#fff" stroke="#b5a488" stroke-width="1.6"/><path d="M14 3v5h5" fill="none" stroke="#b5a488" stroke-width="1.6"/></svg>')
        wt="700" if kind=="fold" else "500"
        col="#2a2016" if kind=="fold" else "#5a4634"
        rows+=(f'<div style="display:flex;align-items:center;gap:9px;padding:6px 0 6px {pad}px;font-family:\'DM Mono\';font-size:16px;font-weight:{wt};color:{col}">'
          f'{glyph}<span>{nm}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;gap:30px;align-items:center">
      <div style="flex:1">
        {htitle("Your files are the workspace","CONTEXT","#2a2016","#96562d")}
        <div style="background:rgba(255,255,255,.55);border:1px solid rgba(150,120,80,.2);border-radius:16px;padding:12px 20px">{rows}</div>
      </div>
      <div style="flex-shrink:0;width:250px">
        <div style="background:#fff;border-left:5px solid #96562d;border-radius:14px;padding:22px 20px;box-shadow:0 18px 30px rgba(120,95,60,.18)">
          <div style="font-family:DM Sans;font-weight:900;font-size:58px;color:#2a2016;line-height:1">50</div>
          <div style="font-family:DM Sans;font-weight:700;font-size:17px;color:#5a4634;margin-top:-2px">docs read</div>
          <div style="height:1px;background:rgba(150,120,80,.25);margin:16px 0"></div>
          <div style="display:flex;align-items:center;gap:9px">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>
            <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">1 brief</span></div>
          <div style="font-family:DM Mono;font-size:13px;color:#8a745a;margin-top:6px">zero uploads</div>
        </div>
      </div>
      {cap("no uploads. it reads every file already in your project.","#8a745a")}</div>'''

# 3. COMMANDS - a terminal command palette; seven slash commands, one specialist each
def commands():
    cmds=[("/cortex","research the account",False),("/specter","write the outbound",True),
          ("/striker","qualify the deal",False),("/pulse","draft the content",False),
          ("/sentinel","ship the code",False),("/amplify","schedule the post",False),
          ("/counsel","review the NDA",False)]
    rows=""
    for c,d,on in cmds:
        cc=f"rgb({ACC})" if on else "#e4ac82"
        bg="background:rgba(212,162,127,.12);border-radius:9px;" if on else ""
        cur='<span style="color:rgb('+ACC+')">|</span>' if on else ''
        rows+=(f'<div style="display:flex;align-items:baseline;gap:14px;padding:8px 12px;{bg}font-family:\'DM Mono\';font-size:17px">'
          f'<span style="color:#5f5a52;width:14px">$</span>'
          f'<span style="color:{cc};font-weight:500;width:112px">{c}</span>'
          f'<span style="color:#c9c3b8">{d}</span>{cur}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One slash, the right specialist","SKILLS")}
      <div style="background:#161513;border:1px solid rgba(255,255,255,.1);border-radius:20px;overflow:hidden;box-shadow:inset 0 2px 3px rgba(255,255,255,.05),0 24px 44px rgba(0,0,0,.4)">
        <div style="display:flex;align-items:center;gap:8px;padding:13px 18px;border-bottom:1px solid rgba(255,255,255,.08);background:#1e1c19">
          <span style="width:12px;height:12px;border-radius:50%;background:#c84623;display:inline-block"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#d4a27f;display:inline-block"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#5f5a52;display:inline-block"></span>
          <span style="font-family:DM Mono;font-size:13px;color:#8f8f85;margin-left:10px">ultron - commands</span></div>
        <div style="padding:14px 14px">{rows}</div>
      </div>
      {cap("seven callable specialists. name the job, skip the busywork.")}</div>'''

# 4. MEMORY - persistence timeline: facts carried across 3 sessions vs a prompt that resets
def memory():
    sx=[150,410,670]; labels=["Mon","Wed","today"]; session=""
    for i,(x,lb) in enumerate(zip(sx,labels)):
        session+=(f'<circle cx="{x}" cy="70" r="11" fill="rgb({ACC})"/>'
          f'<text x="{x}" y="42" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">S{i+1}</text>'
          f'<text x="{x}" y="100" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8f8f85">{lb}</text>')
    chips=["ICP","pricing","pipeline","docs"]
    chipbar=""
    for j,c in enumerate(chips):
        cx=118+j*168
        chipbar+=(f'<rect x="{cx}" y="150" width="146" height="52" rx="14" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>'
          f'<text x="{cx+73}" y="182" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="rgb({ACC})">{c}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It remembers across sessions","VAULT")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <line x1="150" y1="70" x2="670" y2="70" stroke="rgba(212,162,127,.35)" stroke-width="3"/>
        {session}
        <text x="35" y="182" font-family="DM Mono" font-size="12.5" fill="#8f8f85">VAULT</text>
        <rect x="108" y="132" width="620" height="92" rx="20" fill="rgba(212,162,127,.06)" stroke="rgba(212,162,127,.22)"/>
        {chipbar}
        <path d="M150 108 V128 M410 108 V128 M670 108 V128" stroke="rgba(212,162,127,.5)" stroke-width="2" stroke-dasharray="3 5"/>
        <text x="35" y="330" font-family="DM Mono" font-size="12.5" fill="rgb(200,70,35)">PROMPT</text>
        <path d="M108 322 H728" stroke="rgb(200,70,35)" stroke-width="2.5" stroke-dasharray="4 10"/>
        <g font-family="DM Mono" font-size="13" fill="#a06a54">
          <text x="150" y="360" text-anchor="middle">blank</text><text x="410" y="360" text-anchor="middle">blank</text><text x="670" y="360" text-anchor="middle">blank</text></g>
        <circle cx="150" cy="322" r="7" fill="none" stroke="rgb(200,70,35)" stroke-width="2"/>
        <circle cx="410" cy="322" r="7" fill="none" stroke="rgb(200,70,35)" stroke-width="2"/>
        <circle cx="670" cy="322" r="7" fill="none" stroke="rgb(200,70,35)" stroke-width="2"/>
      </svg>
      {cap("icp, pricing, pipeline, docs - carried forward, never re-explained.")}</div>'''

# 5. TOOLS - one request fans out to four real actions, each executed
def tools():
    acts=[("Email sent","SPECTER",64),("PR merged","SENTINEL",192),("Meeting booked","STRIKER",320),("NDA drafted","COUNSEL",448)]
    hubx,hy=150,256; lx=430; edges=""; cards=""
    for nm,ag,y in acts:
        edges+=f'<path d="M{hubx+58} {hy} C300 {hy},310 {y},{lx-6} {y}" fill="none" stroke="rgb({ACC})" stroke-width="3.2" opacity=".8"/>'
        cards+=(f'<div style="position:absolute;left:280px;top:{y-38}px;width:440px;background:linear-gradient(160deg,#3a352e,#241f1a);border:1.5px solid rgba(212,162,127,.3);border-radius:16px;padding:15px 20px;display:flex;align-items:center;gap:16px;box-shadow:0 20px 34px rgba(0,0,0,.45)">'
          f'<div style="flex-shrink:0;width:42px;height:42px;border-radius:12px;background:rgba(212,162,127,.16);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{nm}</div></div>'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">{ag}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It does not answer, it acts","ACTIONS")}
      <div style="position:relative;height:470px">
        <svg width="820" height="470" viewBox="0 0 820 470" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="th" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="tg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
          {edges}
          <g filter="url(#tg)"><circle cx="{hubx}" cy="{hy}" r="58" fill="url(#th)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">DO</text>
          <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one request</text>
        </svg>
        {cards}
      </div>
      {cap("cold emails, pull requests, proposals, contracts - done, not described.")}</div>'''

# 6. STACK (IVORY) - the four primitives as an isometric layered build under one AGENT
def stack():
    layers=[("Tools","actions",0),("Memory","vault",1),("Commands","skills",2),("Files","context",3)]
    cards=""
    for nm,role,i in layers:
        y=i*96
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:520px;background:linear-gradient(160deg,#fffdf9,#efe6d5);border:1.5px solid rgba(150,120,80,.28);border-radius:16px;padding:18px 26px;box-shadow:0 22px 34px rgba(120,95,60,.22), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(150,90,45,.12);border:1px solid rgba(150,90,45,.3);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:20px;color:#96562d">{4-i}</div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#2a2016">{nm}</div></div>'
          f'<div style="font-family:DM Mono;font-size:14px;letter-spacing:.08em;color:#96562d">{role}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The four-layer build","ARCHITECTURE","#2a2016","#96562d")}
      <div style="display:flex;align-items:center;gap:20px">
        <div style="perspective:1800px;flex:1;height:440px;display:flex;align-items:center;justify-content:center">
          <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:520px;height:380px;position:relative">{cards}</div>
        </div>
        <div style="flex-shrink:0;width:170px;text-align:center">
          <div style="width:150px;height:150px;border-radius:50%;margin:0 auto;background:radial-gradient(circle at 38% 32%,#f0c49e,#96562d 70%);box-shadow:0 22px 40px rgba(150,90,45,.4);display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#fff">AGENT</span>
            <span style="font-family:DM Mono;font-size:11px;color:#ffe8d6">= 4 layers</span></div>
          <div style="font-family:DM Mono;font-size:13px;color:#8a745a;margin-top:14px">stack, not chat</div>
        </div>
      </div>
      {cap("stack the four and a chatbot becomes an operator.","#8a745a")}</div>'''

# 7. GATE - external actions queue at a HOLD bar, released one at a time on your tap
def gate():
    q=[("send 12 emails","hold",70),("open PR #182","hold",158),("book 3 calls","sent",246)]
    rows=""
    for txt,st,y in q:
        sent=(st=="sent")
        bd=f"rgb({ACC})" if sent else "rgba(255,255,255,.12)"
        chip=(f'<div style="display:flex;align-items:center;gap:8px;color:rgb({ACC})"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Mono;font-size:13px">sent</span></div>'
          if sent else '<span style="font-family:DM Mono;font-size:13px;color:#a89c88;border:1px solid rgba(255,255,255,.18);border-radius:8px;padding:4px 12px">hold</span>')
        rows+=(f'<div style="position:absolute;left:0;top:{y}px;width:300px;background:linear-gradient(160deg,#37322c,#231f1a);border:1.5px solid {bd};border-radius:14px;padding:15px 18px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 16px 28px rgba(0,0,0,.4)">'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{txt}</span>{chip}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing fires without your tap","HUMAN GATE")}
      <div style="position:relative;height:420px">
        <svg width="820" height="420" viewBox="0 0 820 420" style="position:absolute;left:0;top:0">
          <rect x="352" y="20" width="14" height="380" rx="7" fill="rgb({ACC})" opacity=".85"/>
          <text x="359" y="14" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">GATE</text>
          <path d="M300 88 H352 M300 176 H352" stroke="rgba(255,255,255,.14)" stroke-width="2" stroke-dasharray="4 6"/>
          <path d="M366 264 H470" stroke="rgb({ACC})" stroke-width="3"/>
          <g filter="url(#tap)"><rect x="472" y="230" width="150" height="70" rx="18" fill="rgba(212,162,127,.14)" stroke="rgb({ACC})" stroke-width="2"/></g>
          <text x="547" y="262" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
          <text x="547" y="284" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">approve</text>
          <defs><filter id="tap" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        </svg>
        {rows}
      </div>
      {cap("every external action queues at the gate. you approve, it ships.")}</div>'''

# 8. OPERATOR - the four primitives converge into one AGENT you run, priced in cents
def operator():
    prim=[("files",70,120),("commands",70,215),("memory",70,310),("tools",70,405)]
    left=""
    for nm,x,y in prim:
        left+=(f'<path d="M{x+62} {y} C320 {y},360 262,540 262" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
          f'<rect x="{x-8}" y="{y-24}" width="150" height="48" rx="13" fill="#221f1b" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{x+67}" y="{y+6}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Four parts, one operator","ASSEMBLED")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="ob" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="obg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#obg)"><circle cx="620" cy="262" r="118" fill="url(#ob)"/></g>
        <text x="620" y="250" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">ONE</text>
        <text x="620" y="282" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">AGENT</text>
        <rect x="524" y="404" width="192" height="42" rx="21" fill="rgba(212,162,127,.12)" stroke="rgba(212,162,127,.4)"/>
        <text x="620" y="431" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="rgb({ACC})">cents per task</text>
      </svg>
      {cap("files, commands, memory, tools - wired into one agent you run.")}</div>'''

PANELS={"anatomy":anatomy(),"files":files(),"commands":commands(),"memory":memory(),
        "tools":tools(),"stack":stack(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src34"; os.makedirs(outd,exist_ok=True)
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
