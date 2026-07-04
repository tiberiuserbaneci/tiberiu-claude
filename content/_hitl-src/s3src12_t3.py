#!/usr/bin/env python3
# TIER 3 - THE LAST RUNG IS A TEAM (adaptare IG "7 Levels of Claude Code" -> Ultron capability climb).
# WIRE-ITS-EYES bar: 8 unique hand-built coded scenes, clean rounded cards, title + one caption, no
# generic stat-chip strips. 6 dark + 2 ivory (mcp, skills). Warm palette only; red = the wall/stop state.
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
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LADDER - ascending bar climb, 7 rungs; rung 3 (Tools) is a red stop, rung 7 (Team) glows accent.
def ladder():
    rungs=[("Prompt",92),("Context",132),("Tools",174),("MCP",216),("Skills",258),("Subagents",300),("Team",352)]
    bw=90; gap=18; x0=34; base=402; W=x0*2+len(rungs)*bw+(len(rungs)-1)*gap
    bars=""
    for i,(nm,h) in enumerate(rungs):
        x=x0+i*(bw+gap); top=base-h; cx=x+bw/2
        if i==6:
            fill="url(#topb)"; filt=' filter="url(#tg)"'; ncol=f"rgb({ACC})"; lvlc=f"rgb({ACC})"
        elif i==2:
            fill="url(#redb)"; filt=""; ncol=f"rgb({RED})"; lvlc=f"rgb({RED})"
        else:
            fill="url(#neub)"; filt=""; ncol="#9a948a"; lvlc="#6f6a60"
        bars+=(f'<rect x="{x}" y="{top}" width="{bw}" height="{h}" rx="12"{filt} fill="{fill}" stroke="rgba(255,255,255,.09)"/>'
               f'<text x="{cx:.0f}" y="{top-14}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="{lvlc}">Lvl {i+1}</text>'
               f'<text x="{cx:.0f}" y="{base+30}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="{ncol}">{nm}</text>')
        if i==2:
            bars+=(f'<g transform="translate({cx:.0f},{top-42})"><rect x="-58" y="-20" width="116" height="30" rx="8" fill="rgba(200,70,35,.16)" stroke="rgb({RED})"/>'
                   f'<text x="0" y="1" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="rgb({RED})">MOST STOP</text></g>')
        if i==6:
            bars+=(f'<circle cx="{cx:.0f}" cy="{top+34}" r="19" fill="url(#orb)"/>'
                   f'<text x="{cx:.0f}" y="{top+70}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="rgb({ACC})">ULTRON</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven rungs, one ceiling","THE CLIMB")}
      <svg width="{W}" height="470" viewBox="0 0 {W} 470" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="neub" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#242019"/></linearGradient>
          <linearGradient id="redb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#5a2a1c"/><stop offset="100%" stop-color="#341510"/></linearGradient>
          <linearGradient id="topb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e6b48f"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4c2c"/></linearGradient>
          <radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#fbe4d2"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="tg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="13" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <line x1="{x0-6}" y1="{base}" x2="{W-x0+6}" y2="{base}" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/>
        {bars}
      </svg>
      {cap("prompt to team. the top rung is not a bigger prompt, it is a company.")}</div>'''

# 2. PROMPT - a single terminal line: one question, one answer. Where everyone meets Claude.
def prompt():
    lines=[('<span style="color:rgb('+ACC+')">&gt;</span> how is this codebase structured?','#eae4d8'),
           ('claude &middot; reading files','#7a746a'),
           ("It is a Node / Express API.",'#d9d5cc'),
           ('entry: <span style="color:rgb('+ACC+')">src/index.js</span>','#d9d5cc'),
           ('routes: <span style="color:rgb('+ACC+')">src/routes/</span>','#d9d5cc')]
    body="".join(f'<div style="font-family:\'DM Mono\';font-size:19px;line-height:2.0;color:{c}">{t}</div>' for t,c in lines)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("You type. It answers.","LEVEL 1")}
      <div style="background:linear-gradient(160deg,#141210,#0d0c0b);border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:26px 30px 30px;box-shadow:inset 0 2px 3px rgba(255,255,255,.06),0 24px 44px rgba(0,0,0,.5)">
        <div style="display:flex;gap:11px;margin-bottom:22px">
          <span style="width:14px;height:14px;border-radius:50%;background:rgb({ACC})"></span>
          <span style="width:14px;height:14px;border-radius:50%;background:#3a352f"></span>
          <span style="width:14px;height:14px;border-radius:50%;background:#3a352f"></span></div>
        {body}
        <div style="display:inline-block;width:13px;height:24px;background:rgb({ACC});margin-top:8px;vertical-align:middle;box-shadow:0 0 14px rgba({ACC},.6)"></div>
      </div>
      {cap("one question at a time. how everyone meets claude, and where most quietly stall.")}</div>'''

# 3. CONTEXT - a coded CLAUDE.md file tree; the active project leaf lit in accent.
def context():
    def row(indent,glyph,gcol,name,note,ncol="#d9d5cc",bold=False):
        fw="800" if bold else "500"
        rt=f'<span style="margin-left:auto;font-family:\'DM Mono\';font-size:15px;color:#7a746a">{note}</span>' if note else ""
        return (f'<div style="display:flex;align-items:center;gap:14px;padding:9px 0 9px {indent}px">'
                f'<span style="width:22px;height:18px;border-radius:5px;background:{gcol};flex-shrink:0"></span>'
                f'<span style="font-family:\'DM Mono\';font-weight:{fw};font-size:19px;color:{ncol}">{name}</span>{rt}</div>')
    rows=(row(0,"","#b8c6da","~/","project root",ncol="#9a948a")
        + row(30,"","#e6e0d4","CLAUDE.md","who you are, style")
        + row(30,"","#c8b79a","Acme/","company + role",ncol="#c9c3b8")
        + row(66,"","#e6e0d4","CLAUDE.md","role, voice, rules")
        + row(66,"","#8f8a80","Marketing/","")
        + row(66,"","#8f8a80","Finance/","")
        + row(30,"","#c8b79a","Product/","active project",ncol="#c9c3b8")
        + row(66,"",f"rgb({ACC})","CLAUDE.md","this build",ncol=f"rgb({ACC})",bold=True))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Hand it a CLAUDE.md","LEVEL 2")}
      <div style="background:linear-gradient(160deg,#211e1b,#171512);border:1px solid rgba(255,255,255,.07);border-radius:20px;padding:20px 30px 22px;border-left:3px solid rgba(212,162,127,.4)">
        {rows}
      </div>
      {cap("your code, docs and rules nested by scope. it works off your world, not a guess.")}</div>'''

# 4. TOOLWALL - lit tool rail, then a red barrier "MOST STOP HERE", then the higher rungs ghosted.
def toolwall():
    def chip(nm,lit=True):
        if lit:
            return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px">'
                    f'<div style="width:96px;height:96px;border-radius:20px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.42);box-shadow:0 16px 28px rgba(0,0,0,.5),inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center">'
                    f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:30px;color:rgb({ACC})">{nm[0]}</span></div>'
                    f'<span style="font-family:\'DM Mono\';font-size:13px;color:#c9c3b8">{nm}</span></div>')
        return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;opacity:.34">'
                f'<div style="width:78px;height:78px;border-radius:18px;background:#242019;border:1.5px dashed rgba(255,255,255,.14);display:flex;align-items:center;justify-content:center">'
                f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:22px;color:#7a746a">{nm[0]}</span></div>'
                f'<span style="font-family:\'DM Mono\';font-size:12px;color:#7a746a">{nm}</span></div>')
    lit="".join(chip(n) for n in ["Read","Grep","Edit","Bash"])
    ghost="".join(chip(n,False) for n in ["MCP","Skills","Team"])
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Tools are the wall","LEVEL 3")}
      <div style="display:flex;align-items:center;gap:24px;height:400px">
        <div style="display:flex;gap:18px;align-items:center">{lit}</div>
        <div style="display:flex;flex-direction:column;align-items:center;align-self:stretch;justify-content:center;gap:14px;padding:0 6px">
          <div style="width:0;flex:1;border-left:4px dashed rgb({RED})"></div>
          <div style="writing-mode:vertical-rl;transform:rotate(180deg);font-family:\'DM Mono\';font-size:15px;letter-spacing:.2em;color:rgb({RED})">MOST STOP HERE</div>
          <div style="width:0;flex:1;border-left:4px dashed rgb({RED})"></div>
        </div>
        <div style="display:flex;gap:16px;align-items:center">{ghost}</div>
      </div>
      {cap("read, edit, run, search. real actions, but still one worker doing one thing.")}</div>'''

# 5. MCP - IVORY patchbay: a Claude core cabled into your real systems (crm, db, inbox, calendar).
def mcp():
    sysu=[("CRM","deals + contacts",92),("Database","your product data",176),("Inbox","send + read mail",260),("Calendar","book the meeting",344)]
    corex,corey=120,218; sockx=560
    cables=""; sock=""
    for nm,note,y in sysu:
        mx=(corex+sockx)/2
        cables+=f'<path d="M{corex+72} {corey} C{mx:.0f} {corey},{mx:.0f} {y},{sockx-4} {y}" fill="none" stroke="#96562d" stroke-width="3" opacity="0.75"/>'
        cables+=f'<circle cx="{sockx-4}" cy="{y}" r="7" fill="#96562d"/>'
        sock+=(f'<div style="position:absolute;left:{sockx}px;top:{y-34}px;width:250px;display:flex;align-items:center;gap:14px;'
               f'background:rgba(255,255,255,.66);border:1px solid rgba(120,95,60,.24);border-radius:16px;padding:14px 18px;box-shadow:0 12px 22px rgba(120,95,60,.16)">'
               f'<span style="width:14px;height:14px;border-radius:4px;background:#96562d;flex-shrink:0"></span>'
               f'<div><div style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#2a2016">{nm}</div>'
               f'<div style="font-family:\'DM Sans\';font-size:14px;color:#8a745a">{note}</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("MCP plugs it in","LEVEL 4","#2a2016")}
      <div style="position:relative;height:440px">
        <svg width="820" height="440" viewBox="0 0 820 440" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="mcore" cx="36%" cy="30%"><stop offset="0%" stop-color="#e6b48f"/><stop offset="60%" stop-color="#b8703f"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgba(150,90,45,.4)"/></filter></defs>
          {cables}
          <g filter="url(#mg)"><circle cx="{corex}" cy="{corey}" r="72" fill="url(#mcore)"/></g>
          <text x="{corex}" y="{corey-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#fdfbf6">CLAUDE</text>
          <text x="{corex}" y="{corey+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#fbe4d2">via MCP</text>
        </svg>
        {sock}
      </div>
      {cap("your crm, database, inbox and calendar become tools it can actually use.","#8a745a")}</div>'''

# 6. SKILLS - IVORY isometric stack of reusable skill cards, each with a run count.
def skills():
    rows=[("cold-email-audit","scores every send",  "x214"),
          ("icp-score","ranks each account",         "x1.2k"),
          ("pr-review","reads the diff, flags risk", "x96"),
          ("brief-builder","one page from the web",  "x340")]
    cards=""
    for i,(nm,sub,n) in enumerate(rows):
        y=i*120
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;display:flex;align-items:center;gap:20px;'
                f'background:linear-gradient(160deg,#fffdf9,#f1e7d6);border:1px solid rgba(120,95,60,.20);border-radius:18px;padding:20px 24px;'
                f'box-shadow:0 26px 40px rgba(120,95,60,.22), inset 0 2px 2px rgba(255,255,255,.9)">'
                f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(150,90,45,.12);border:1px solid rgba(150,90,45,.3);display:flex;align-items:center;justify-content:center">'
                f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:24px;color:#96562d">/</span></div>'
                f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-weight:500;font-size:20px;color:#2a2016">/{nm}</div>'
                f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8a745a;margin-top:1px">{sub}</div></div>'
                f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:#96562d;padding:9px 15px;border-radius:12px">'
                f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:20px;color:#fdfbf6;line-height:1">{n}</span>'
                f'<span style="font-family:\'DM Mono\';font-size:10px;letter-spacing:.1em;color:rgba(253,251,246,.72)">RUNS</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 44px 40px">
      {htitle("Skills it can reuse","LEVEL 5","#2a2016")}
      <div style="perspective:2000px;height:520px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:600px;height:420px;position:relative">{cards}</div></div>
      {cap("package a workflow once. it runs the same audit, the same score, every time.","#8a745a")}</div>'''

# 7. SUBAGENTS - one task fans into parallel lanes, each a worker on a slice, folded into one result.
def subagents():
    W,H=820,450
    lanes=[("scan competitors",70),("pull the pricing",172),("read the reviews",274),("draft the brief",376)]
    startx,mergex=250,600; sy=225
    fan=""; merge=""; lanehtml=""
    for nm,y in lanes:
        m1=(120+startx)/2
        fan+=f'<path d="M120 {sy} C{m1:.0f} {sy},{m1:.0f} {y},{startx-6} {y}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
        m2=(startx+230+mergex)/2
        merge+=f'<path d="M{startx+232} {y} C{m2:.0f} {y},{m2:.0f} {sy},{mergex-6} {sy}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
        lanehtml+=(f'<div style="position:absolute;left:{startx}px;top:{y-30}px;width:230px;display:flex;align-items:center;gap:14px;'
                   f'background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:14px;padding:14px 16px;box-shadow:0 14px 24px rgba(0,0,0,.5)">'
                   f'<div style="flex-shrink:0;width:34px;height:34px;border-radius:10px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">'
                   f'<svg width="18" height="18" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><path d="M5 20c0-4 3.5-6 7-6s7 2 7 6" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/></svg></div>'
                   f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:16px;color:#e2dccf">{nm}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One task, many workers","LEVEL 6")}
      <div style="position:relative;height:450px">
        <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="tk" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {fan}{merge}
          <rect x="26" y="{sy-40}" width="94" height="80" rx="16" fill="#2a2724" stroke="rgba(255,255,255,.12)"/>
          <text x="73" y="{sy-2}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">one</text>
          <text x="73" y="{sy+18}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">task</text>
          <g filter="url(#sg)"><circle cx="{mergex+70}" cy="{sy}" r="66" fill="url(#tk)"/></g>
          <text x="{mergex+70}" y="{sy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ONE</text>
          <text x="{mergex+70}" y="{sy+18}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">RESULT</text>
        </svg>
        {lanehtml}
      </div>
      {cap("subagents run in parallel, each on a slice, then fold the work back into one.")}</div>'''

# 8. TEAM - radial org: ROUTER orb at the core, 7 named agents on the ring, HUMAN GATE on the send.
def team():
    cx,cy,R=300,232,180
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; nodes=""
    n=len(agents)
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#221f1b" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
                f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="#eae4d8">{nm}</text>'
                f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#9a948a">{role}</text>')
    gate=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.34);border-radius:18px;padding:20px 22px">'
      f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px"><svg width="24" height="24" viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2.5" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/></svg>'
      f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#FAFAF7">HUMAN GATE</span></div>'
      f'<div style="font-family:\'DM Sans\';font-size:16px;color:#c9c3b8;line-height:1.45">Every send waits for your tap. The team drafts, you approve, it ships.</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="600" height="470" viewBox="0 0 600 470">
        <defs><radialGradient id="rt" cx="36%" cy="30%"><stop offset="0%" stop-color="#fbe4d2"/><stop offset="58%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#rt)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ROUTER</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">picks the agent</text>
        {nodes}
      </svg>
      <div style="flex:1">
        {htitle("The last rung is a team","LEVEL 7")}
        {gate}
        {cap("seven agents, one router, your gate. that team is ultron.")}
      </div></div>'''

PANELS={"ladder":ladder(),"prompt":prompt(),"context":context(),"toolwall":toolwall(),
        "mcp":mcp(),"skills":skills(),"subagents":subagents(),"team":team()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src12"; os.makedirs(outd,exist_ok=True)
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
