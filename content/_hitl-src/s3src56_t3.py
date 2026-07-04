#!/usr/bin/env python3
# TIER 3 - "THE FIVE YOU SKIP" (adaptare IG s3src56: 5 Claude Code features nobody uses).
# Fiecare panel e o scena unica hand-built pe card curat CARD/CARDIV, title + o singura caption.
# Hero = cele 5 feature-uri concrete (Skills / Subagents / Hooks / Slash commands / Connectors),
# apoi 3 panouri de payoff Ultron (model tier / memory / operator). Zero cod brut. Cost zero.
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
def ivtitle(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')

# 1. SKILLS - IVORY recipe-rack: a trigger phrase drops in, the matching playbook card lights up
def skills():
    plays=[("CORTEX brief","profile any company or person",False),
           ("SPECTER play","the 3-step cold sequence",True),
           ("STRIKER close","objection to signed proposal",False),
           ("PULSE post","a draft in your own voice",False)]
    rows=""
    for nm,desc,lit in plays:
        if lit:
            rows+=(f'<div style="display:flex;align-items:center;gap:16px;transform:translateX(30px);'
              f'background:linear-gradient(160deg,#ffffff,#f4ead9);border:1px solid rgba(150,86,45,.4);border-left:5px solid #96562d;'
              f'border-radius:16px;padding:16px 20px;box-shadow:0 18px 34px rgba(150,110,60,.24),inset 0 2px 3px rgba(255,255,255,.9)">'
              f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:21px;color:#2a2016">{nm}</div>'
              f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8a745a;margin-top:1px">{desc}</div></div>'
              f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:#96562d">LOADED</span></div>')
        else:
            rows+=(f'<div style="display:flex;align-items:center;gap:16px;'
              f'background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.18);border-radius:16px;padding:16px 20px">'
              f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:700;font-size:20px;color:#4a3f30">{nm}</div>'
              f'<div style="font-family:\'DM Sans\';font-size:14px;color:#a08a68;margin-top:1px">{desc}</div></div>'
              f'<span style="width:10px;height:10px;border-radius:50%;background:rgba(150,120,80,.3)"></span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ivtitle("One recipe, loaded on cue","SKILLS")}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(150,86,45,.08);border:1px dashed rgba(150,86,45,.4);border-radius:14px;padding:13px 18px">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#96562d;flex-shrink:0">TRIGGER</span>
        <span style="font-family:'DM Sans';font-size:18px;color:#4a3f30">"draft the cold outreach"</span>
        <svg width="26" height="26" viewBox="0 0 24 24" style="margin-left:auto" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg></div>
      <div style="display:flex;flex-direction:column;gap:12px;margin-top:14px">{rows}</div>
      <div style="font-family:'DM Mono';font-size:14px;color:#8a745a;margin-top:20px">your playbooks load themselves the moment the job appears.</div></div>'''

# 2. SUBAGENTS - one ask fans out into 3 scoped agents running in parallel, each reports back
def subagents():
    lanes=[("CORTEX","profiled 38 accounts",92),("SPECTER","drafted 12 emails",222),("COUNSEL","flagged 1 clause",352)]
    edges=""; cards=""; sx,sy=150,222
    for nm,res,y in lanes:
        edges+=f'<path d="M{sx+8} {sy} C300 {sy},300 {y},430 {y}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        cards+=(f'<div style="position:absolute;left:300px;top:{y-38}px;width:250px;'
          f'background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.28);border-radius:16px;padding:14px 18px;box-shadow:0 22px 38px rgba(0,0,0,.5),inset 0 2px 2px rgba(255,255,255,.08);display:flex;align-items:center;gap:14px">'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7;margin-top:2px">{res}</div></div>'
          f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M6 12.5l3.4 3.4L18 8" fill="none" stroke="rgb({ACC})" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Three jobs, three fresh minds","SUBAGENTS")}
      <div style="position:relative;height:470px">
        <svg width="820" height="470" viewBox="0 0 820 470" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="sh" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="shg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <g filter="url(#shg)"><circle cx="{sx}" cy="{sy}" r="60" fill="url(#sh)"/></g>
          <text x="{sx}" y="{sy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">1 ASK</text>
          <text x="{sx}" y="{sy+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">review launch</text>
        </svg>
        {cards}
        <div style="position:absolute;left:576px;top:196px;width:150px;font-family:DM Mono;font-size:12.5px;color:#c9c3b8;line-height:1.5;border-left:2px solid rgba(212,162,127,.4);padding-left:14px">all three ran<br>in parallel,<br>your thread<br>stays clean</div>
      </div>
      {cap("hand off scoped work, it runs in its own context and reports back.")}</div>'''

# 3. HOOKS - a linear send pipeline; a tripwire fires the gate and HOLDS the send for your tap
def hooks():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It stops itself before it sends","HOOKS")}
      <svg width="820" height="356" viewBox="0 0 820 356" style="display:block;margin:8px auto 0">
        <defs>
          <radialGradient id="lk" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="lg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter>
        </defs>
        <line x1="90" y1="168" x2="560" y2="168" stroke="rgba(212,162,127,.55)" stroke-width="10" stroke-linecap="round"/>
        <line x1="620" y1="168" x2="762" y2="168" stroke="rgba(200,70,35,.4)" stroke-width="10" stroke-linecap="round" stroke-dasharray="3 15"/>
        <circle cx="90" cy="168" r="16" fill="#2a2724" stroke="rgba(255,255,255,.14)"/><text x="90" y="210" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">draft</text>
        <circle cx="300" cy="168" r="16" fill="#2a2724" stroke="rgba(255,255,255,.14)"/><text x="300" y="210" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">queue</text>
        <line x1="440" y1="112" x2="440" y2="224" stroke="rgb({ACC})" stroke-width="2.5" stroke-dasharray="4 6"/>
        <polygon points="440,102 449,120 431,120" fill="rgb({ACC})"/>
        <text x="440" y="94" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="rgb({ACC})">HOOK FIRES</text>
        <g filter="url(#lg2)"><circle cx="560" cy="168" r="60" fill="url(#lk)"/></g>
        <g transform="translate(538,146)"><rect x="0" y="20" width="44" height="34" rx="8" fill="none" stroke="#1a0f0a" stroke-width="5"/><path d="M8 20 V11 a14 14 0 0 1 28 0 v9" fill="none" stroke="#1a0f0a" stroke-width="5"/></g>
        <text x="560" y="264" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#FAFAF7">HELD</text>
        <text x="560" y="288" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">waits for your tap</text>
        <rect x="700" y="138" width="60" height="60" rx="14" fill="#201d19" stroke="rgba(200,70,35,.55)" stroke-width="2"/>
        <text x="730" y="173" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="#c84623">SEND</text>
        <text x="730" y="220" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#a86a55">blocked</text>
      </svg>
      <div style="display:flex;align-items:center;gap:14px;background:rgba(212,162,127,.08);border:1px solid rgba(212,162,127,.28);border-radius:14px;padding:13px 18px;margin-top:6px">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:rgb({ACC});flex-shrink:0">RULE</span>
        <span style="font-family:'DM Sans';font-size:18px;color:#d9d5cc">before any external send, wait for approval</span></div>
      {cap("a hook fires the gate on its own, nothing leaves unwatched.")}</div>'''

# 4. SLASH COMMANDS - IVORY command palette; each agent is one keystroke, the picked row lit
def commands():
    cmds=[("/cortex","research a company or a person",False),
          ("/specter","write the cold sequence",True),
          ("/striker","handle the objection, draft the proposal",False),
          ("/pulse","draft the post in your voice",False),
          ("/counsel","review the contract",False)]
    rows=""
    for cmd,desc,sel in cmds:
        if sel:
            rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(160deg,#96562d,#7a4326);border-radius:12px;padding:14px 18px;box-shadow:0 10px 22px rgba(150,86,45,.3)">'
              f'<span style="font-family:\'DM Mono\';font-weight:500;font-size:19px;color:#fdf6ec;min-width:118px">{cmd}</span>'
              f'<span style="font-family:\'DM Sans\';font-size:17px;color:#f4e6d6;flex:1">{desc}</span>'
              f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fdf6ec" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 10V6a3 3 0 0 1 6 0v9M15 15l-3 3-3-3"/></svg></div>')
        else:
            rows+=(f'<div style="display:flex;align-items:center;gap:18px;padding:13px 18px;border-bottom:1px solid rgba(120,95,60,.14)">'
              f'<span style="font-family:\'DM Mono\';font-weight:500;font-size:19px;color:#96562d;min-width:118px">{cmd}</span>'
              f'<span style="font-family:\'DM Sans\';font-size:17px;color:#5a4634;flex:1">{desc}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ivtitle("Call an operator by name","SLASH COMMANDS")}
      <div style="background:rgba(255,255,255,.66);border:1px solid rgba(120,95,60,.18);border-radius:18px;padding:12px;box-shadow:inset 0 2px 4px rgba(150,120,80,.1)">
        <div style="display:flex;align-items:center;gap:14px;padding:12px 18px 16px;border-bottom:1px solid rgba(120,95,60,.16)">
          <span style="font-family:'DM Mono';font-weight:500;font-size:22px;color:#96562d">/</span>
          <span style="font-family:'DM Sans';font-size:18px;color:#a08a68">type a command</span></div>
        <div style="display:flex;flex-direction:column;padding-top:8px;gap:2px">{rows}</div>
      </div>
      <div style="font-family:'DM Mono';font-size:14px;color:#8a745a;margin-top:20px">one keystroke and the right agent is already working.</div></div>'''

# 5. CONNECTORS - central core, 6 tool ports plugged in around it (inbox, deals, docs...)
def connect():
    cx,cy,R=300,225,150
    ports=[("Inbox",-90),("Deals",-30),("Calendar",30),("Docs",90),("Web",150),("Vault",210)]
    spokes=""; nodes=""
    for nm,a in ports:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        nodes+=(f'<rect x="{x-56:.0f}" y="{y-25:.0f}" width="112" height="50" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="{x-38:.0f}" cy="{y:.0f}" r="5" fill="rgb({ACC})" filter="url(#pd)"/>'
          f'<text x="{x+12:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Plug in your whole stack","CONNECTORS")}
      <svg width="640" height="470" viewBox="0 0 640 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="cr" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="crg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="pd" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {spokes}
        <g filter="url(#crg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#cr)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">CORE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">6 tools live</text>
        {nodes}
      </svg>
      {cap("claude works your real inbox, deals and docs, not a screenshot.")}</div>'''

# 6. MODEL TIER - a 3-zone gauge; the job needle lands on SMART, priced in cents
def router():
    cx,cy,R=410,320,196
    def pt(t):
        r=math.radians(t); return (cx+R*math.cos(r), cy-R*math.sin(r))
    def arc(t1,t2,col,w,glow=""):
        x1,y1=pt(t1); x2,y2=pt(t2)
        return f'<path d="M{x1:.1f} {y1:.1f} A{R} {R} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="{w}" {glow}/>'
    segs=arc(180,121,"rgba(232,196,160,.85)",30)+arc(119,61,f"rgb({ACC})",42,'filter="url(#gG)"')+arc(59,0,"#9a5a35",30)
    needle=f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-R+34}" stroke="#FAFAF7" stroke-width="5" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="14" fill="#FAFAF7"/>'
    labels=(f'<text x="{cx-150}" y="{cy+34}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#a8a296">LITE</text>'
            f'<text x="{cx}" y="{cy-R-16}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="rgb({ACC})">SMART</text>'
            f'<text x="{cx+150}" y="{cy+34}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#a8a296">DEEP</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The cheap model, unless it cannot","MODEL TIER")}
      <svg width="820" height="360" viewBox="0 0 820 360" style="display:block;margin:0 auto">
        <defs><filter id="gG" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {segs}{labels}{needle}
      </svg>
      <div style="display:flex;align-items:center;justify-content:center;gap:16px;margin-top:2px">
        <span style="font-family:'DM Sans';font-size:18px;color:#c9c3b8">draft 12 follow-ups</span>
        <svg width="30" height="16" viewBox="0 0 30 16" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><path d="M2 8h22M19 3l6 5-6 5"/></svg>
        <span style="font-family:'DM Sans';font-weight:800;font-size:18px;color:#FAFAF7">SMART</span>
        <span style="font-family:'DM Mono';font-size:12px;color:#1a0f0a;background:rgb({ACC});padding:5px 12px;border-radius:999px;font-weight:600">0.11c</span></div>
      {cap("each job routed to the smallest tier that can do it, priced in cents.")}</div>'''

# 7. MEMORY - a vault spine feeding stacked strata (ICP, pricing, pipeline...), persists across runs
def memory():
    layers=[("ICP","founders, 2-50, US and UK"),
            ("PRICING","cents per token"),
            ("PIPELINE","37 live deals"),
            ("DOCS","product, specs, blueprints"),
            ("VOICE","sampled from your posts")]
    rows=""
    for nm,val in layers:
        rows+=(f'<div style="display:flex;align-items:center;gap:20px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:15px 20px;box-shadow:inset 0 2px 2px rgba(255,255,255,.06)">'
          f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.12em;color:rgb({ACC});min-width:96px">{nm}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:19px;color:#eae4d8;flex:1">{val}</span>'
          f'<span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 10px rgba(212,162,127,.8)"></span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It never forgets your company","MEMORY")}
      <div style="display:flex;gap:18px">
        <div style="position:relative;width:52px;flex-shrink:0;display:flex;flex-direction:column;align-items:center">
          <div style="position:absolute;top:8px;bottom:40px;width:6px;border-radius:3px;background:linear-gradient(#f0c49e,rgb({ACC}),#7a4326);box-shadow:0 0 18px rgba(212,162,127,.5)"></div>
          <div style="margin-top:auto;font-family:'DM Mono';font-size:11px;letter-spacing:.1em;color:#8f8f85;writing-mode:vertical-rl;transform:rotate(180deg)">ONE VAULT</div>
        </div>
        <div style="flex:1;display:flex;flex-direction:column;gap:12px">{rows}</div>
      </div>
      <div style="display:flex;align-items:center;gap:12px;margin-top:16px">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><path d="M3 12a9 9 0 1 0 9-9 9 9 0 0 0-7 3M3 3v4h4"/></svg>
        <span style="font-family:'DM Sans';font-size:17px;color:#c9c3b8">every session reads the same core, nothing resets</span></div>
      {cap("set your company once, every agent draws from it.")}</div>'''

# 8. THE STACK - the 5 feature nodes converge into one glowing operator orb
def operator():
    feats=[("SKILLS",70),("SUBAGENTS",155),("HOOKS",240),("COMMANDS",325),("CONNECT",410)]
    ox,oy=600,240
    left=""
    for nm,y in feats:
        left+=(f'<path d="M150 {y} C360 {y},430 {oy},{ox-110} {oy}" fill="none" stroke="rgba(212,162,127,.35)" stroke-width="2.5"/>'
          f'<rect x="20" y="{y-24}" width="130" height="48" rx="13" fill="#221f1b" stroke="rgba(255,255,255,.1)"/>'
          f'<text x="85" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Five switches on is an operator","THE STACK")}
      <svg width="820" height="480" viewBox="0 0 820 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="op" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="opg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {left}
        <g filter="url(#opg)"><circle cx="{ox}" cy="{oy}" r="118" fill="url(#op)"/></g>
        <text x="{ox}" y="{oy-8}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">ONE</text>
        <text x="{ox}" y="{oy+26}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">OPERATOR</text>
        <text x="{ox}" y="{oy+150}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#8f8f85">skills to shipped, one login</text>
      </svg>
      {cap("flip all five and you stop chatting with a tool, you run a company.")}</div>'''

PANELS={"skills":skills(),"subagents":subagents(),"hooks":hooks(),"commands":commands(),
        "connect":connect(),"router":router(),"memory":memory(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src56"; os.makedirs(outd,exist_ok=True)
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
