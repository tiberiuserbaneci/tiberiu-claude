#!/usr/bin/env python3
# TIER 3 - IT FILES A REPORT. The narrow worker-proof angle: an agent is not "does vs talks", it is a
# worker that CLOCKS IN, does a shift, and LEAVES A DELIVERABLE you can open (a timestamped daily
# briefing), reporting output not chat. 8 unique hand-built coded scenes on the WIRE-ITS-EYES bar.
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
def ivhead(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')

# 1. PROOF - split: an IDLE chatbot (blinking cursor, zero output) vs a FILED paper report on the desk
def proof():
    secs=[("Research","3 sources, ranked"),("Draft","1 post, in your voice"),("Tasks","5 queued for today")]
    rows=""
    for a,b in secs:
        rows+=(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:11px">'
          f'<span style="flex-shrink:0;width:22px;height:22px;border-radius:7px;background:rgba(150,90,45,.16);border:1px solid rgba(150,90,45,.3);display:flex;align-items:center;justify-content:center">'
          f'<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4 4L19 6"/></svg></span>'
          f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:17px;color:#2a2016">{a}</span>'
          f'<span style="font-family:\'DM Sans\';font-size:15px;color:#6a5a44">{b}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It left the work on your desk","FILED 06:00")}
      <div style="display:flex;align-items:stretch;gap:26px;height:470px">
        <div style="flex:0 0 292px;display:flex;flex-direction:column;background:#1a1815;border:1.5px dashed rgba(200,70,35,.42);border-radius:20px;padding:22px">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.18em;color:#c84623">CHATBOT</div>
          <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:13px">
            <div style="height:13px;width:72%;border-radius:6px;background:rgba(250,250,247,.06)"></div>
            <div style="height:13px;width:54%;border-radius:6px;background:rgba(250,250,247,.06)"></div>
            <div style="display:flex;align-items:center;gap:9px;margin-top:8px">
              <span style="font-family:'DM Sans';font-size:16px;color:#6f6a60">waiting for you to type</span>
              <span style="display:inline-block;width:3px;height:22px;background:rgb({ACC})"></span></div>
          </div>
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:#7a7468">IDLE &middot; 0 OUTPUT</div>
        </div>
        <div style="flex:1;display:flex;align-items:center">
          <div style="width:100%;background:linear-gradient(160deg,#fdfbf6,#efe6d5);border-radius:18px;padding:26px 28px;box-shadow:0 30px 52px rgba(0,0,0,.5);position:relative">
            <div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(120,95,60,.25);padding-bottom:12px;margin-bottom:18px">
              <span style="font-family:'DM Sans';font-weight:900;font-size:23px;color:#2a2016">DAILY BRIEFING</span>
              <span style="font-family:'DM Mono';font-size:12px;color:#96562d">06:00</span></div>
            {rows}
            <div style="position:absolute;right:-4px;bottom:16px;transform:rotate(-8deg);border:3px solid #96562d;color:#96562d;font-family:'DM Sans';font-weight:900;font-size:22px;letter-spacing:.1em;padding:5px 15px;border-radius:8px;opacity:.92">FILED</div>
          </div>
        </div>
      </div>
      {cap("a chatbot waits for a prompt. a worker files the report.")}</div>'''

# 2. BADGE - IVORY employee ID card: the worker has a job title, a hire date, a shift status
def badge():
    infos=[("EMPLOYEE ID","OP-001"),("HIRED","2026"),("REPORTS TO","You"),("SHIFT","06:00 daily")]
    rws=""
    for k,v in infos:
        rws+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:9px 0;border-bottom:1px solid rgba(120,95,60,.16)">'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.12em;color:#a08a68">{k}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:17px;color:#2a2016">{v}</span></div>')
    bars="".join(f'<rect x="{i*7}" y="0" width="{2 if i%3 else 4}" height="34" fill="#2a2016"/>' for i in range(46))
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {ivhead("It has a job title","EMPLOYEE #001")}
      <div style="display:flex;justify-content:center;align-items:center;height:462px">
        <div style="width:540px;background:linear-gradient(160deg,#ffffff,#f6efe2);border:1px solid rgba(120,95,60,.18);border-radius:22px;padding:0 0 26px;box-shadow:0 34px 58px rgba(120,95,60,.24),inset 0 2px 3px rgba(255,255,255,.9);overflow:hidden">
          <div style="height:22px;background:linear-gradient(90deg,#96562d,rgb({ACC}))"></div>
          <div style="display:flex;align-items:center;gap:22px;padding:24px 30px 18px">
            <div style="flex-shrink:0;width:96px;height:96px;position:relative">
              <svg width="96" height="96" viewBox="0 0 96 96">
                <defs><radialGradient id="av" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient></defs>
                <circle cx="48" cy="48" r="42" fill="url(#av)"/>
                <ellipse cx="38" cy="34" rx="15" ry="9" fill="rgba(255,255,255,.5)" transform="rotate(-26 38 34)"/></svg>
            </div>
            <div style="flex:1">
              <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#2a2016;line-height:1">OPERATOR</div>
              <div style="font-family:'DM Sans';font-size:17px;color:#6a5a44;margin-top:4px">Research &middot; Content &middot; Tasks</div>
              <div style="display:inline-flex;align-items:center;gap:7px;margin-top:10px;background:rgba(150,90,45,.12);border:1px solid rgba(150,90,45,.3);border-radius:999px;padding:5px 13px">
                <span style="width:9px;height:9px;border-radius:50%;background:#96562d"></span>
                <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:#96562d">ON SHIFT</span></div>
            </div>
          </div>
          <div style="padding:2px 30px 18px">{rws}</div>
          <div style="padding:0 30px"><svg width="480" height="34" viewBox="0 0 322 34" preserveAspectRatio="none" style="width:100%;height:34px">{bars}</svg></div>
        </div>
      </div>
      {cap("not an assistant tab. a role that answers to you.","#8a745a")}</div>'''

# 3. CLOCKIN - two-lane morning gantt: the worker's 06:00 shift vs you, asleep until 07:00
def clockin():
    W,H=820,430; x0,x1=64,780
    def xf(t): return x0+(t-5)*(x1-x0)/4.0
    ticks=""
    for t in (5,6,7,8,9):
        x=xf(t); ticks+=(f'<line x1="{x:.0f}" y1="70" x2="{x:.0f}" y2="360" stroke="rgba(250,250,247,.07)"/>'
          f'<text x="{x:.0f}" y="392" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{t:02d}:00</text>')
    wy=150; yy=274
    wx0,wx1=xf(6),xf(6+20/60.0)
    hatch="".join(f'<line x1="{x}" y1="{yy}" x2="{x-24}" y2="{yy+56}" stroke="rgba(250,250,247,.05)" stroke-width="7"/>' for x in range(int(x0),int(xf(7)),22))
    wake=xf(7)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It clocks in without you","MORNING SHIFT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#e6b48f"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {ticks}
        <text x="{x0}" y="132" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">WORKER</text>
        <rect x="{x0}" y="{wy}" width="{x1-x0}" height="56" rx="12" fill="rgba(250,250,247,.03)"/>
        <g filter="url(#sg)"><rect x="{wx0:.0f}" y="{wy}" width="{wx1-wx0:.0f}" height="56" rx="12" fill="url(#sh)"/></g>
        <text x="{(wx0+wx1)/2:.0f}" y="{wy+35}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">SHIFT</text>
        <text x="{wx0:.0f}" y="{wy-14}" font-family="DM Mono" font-size="12.5" fill="#d9d5cc">clock in 06:00</text>
        <text x="{wx1:.0f}" y="{wy+82}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="rgb({ACC})">briefing filed 06:20</text>
        <path d="M{wx1:.0f} {wy+56} V{yy-6}" stroke="rgba(212,162,127,.4)" stroke-width="2" stroke-dasharray="3 6"/>
        <text x="{x0}" y="{yy-16}" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#8f8f85">YOU</text>
        <rect x="{x0}" y="{yy}" width="{x1-x0}" height="56" rx="12" fill="rgba(250,250,247,.03)"/>
        {hatch}
        <text x="{(x0+wake)/2:.0f}" y="{yy+35}" text-anchor="middle" font-family="DM Sans" font-size="16" fill="#6f6a60" font-style="italic">asleep</text>
        <line x1="{wake:.0f}" y1="{yy-8}" x2="{wake:.0f}" y2="{yy+64}" stroke="rgb(200,70,35)" stroke-width="2.5"/>
        <text x="{wake+10:.0f}" y="{yy+34}" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">you wake 07:00</text>
        <text x="{wake+10:.0f}" y="{yy+52}" font-family="DM Mono" font-size="12" fill="#8f8f85">the brief is already on your desk</text>
      </svg>
      {cap("runs on a 06:00 schedule, not on the moment you type.")}</div>'''

# 4. TOOLS - radial hub-and-spokes: the worker reaches for its own 5 tools, unprompted
def tools():
    cx,cy,R=306,232,158
    kit=[("WEB",-90),("INBOX",-18),("CALENDAR",54),("DOCS",126),("CRM",198)]
    spokes=""; nodes=""
    for nm,a in kit:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgb({ACC})" stroke-width="3"/>'
          f'<circle cx="{cx+64*math.cos(math.radians(a)):.0f}" cy="{cy+64*math.sin(math.radians(a)):.0f}" r="4" fill="rgb({ACC})"/>')
        nodes+=(f'<rect x="{x-58:.0f}" y="{y-30:.0f}" width="116" height="60" rx="15" fill="linear-gradient(160deg,#332f2a,#211e1a)" style="fill:#2a2622" stroke="rgba(212,162,127,.4)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="#eae4d8">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">called</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It reaches for its own tools","5 CALLED, UNPROMPTED")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="wk" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="wg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {spokes}
        <g filter="url(#wg)"><circle cx="{cx}" cy="{cy}" r="54" fill="url(#wk)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">WORKER</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">on the job</text>
        {nodes}
      </svg>
      {cap("it calls the tool itself. you never paste a link.")}</div>'''

# 5. MEMORY - vertical shift-ledger: past shifts logged on a spine, all feeding today's brief
def memory():
    days=[("MON","learned your ICP"),("TUE","logged the $4M round"),
          ("WED","killed a dead thread"),("THU","flagged a renewal")]
    rows=""
    for d,note in days:
        rows+=(f'<div style="display:flex;align-items:center;gap:20px;position:relative;z-index:2">'
          f'<div style="flex-shrink:0;width:22px;height:22px;border-radius:50%;background:#2b2b28;border:2.5px solid rgb({ACC});box-shadow:0 0 12px rgba(212,162,127,.4)"></div>'
          f'<div style="flex-shrink:0;width:64px;font-family:\'DM Mono\';font-size:14px;letter-spacing:.1em;color:rgb({ACC})">{d}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:600;font-size:19px;color:#d9d5cc">{note}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It remembers every shift","PERSISTENT VAULT")}
      <div style="position:relative;height:470px;display:flex;flex-direction:column;justify-content:space-between;padding:8px 6px 4px">
        <div style="position:absolute;left:16px;top:22px;bottom:118px;width:2px;background:rgba(212,162,127,.35);z-index:1"></div>
        {rows}
        <div style="display:flex;align-items:center;gap:16px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:18px;padding:20px 24px;box-shadow:0 24px 40px rgba(0,0,0,.5);position:relative;z-index:2">
          <div style="flex-shrink:0;font-family:'DM Sans';font-weight:900;font-size:26px;color:rgb({ACC})">TODAY</div>
          <div style="flex:1"><div style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#FAFAF7">06:00 brief reads all four</div>
          <div style="font-family:'DM Sans';font-size:15px;color:#a8a296;margin-top:2px">no re-explaining, nothing resets</div></div>
        </div>
      </div>
      {cap("yesterday's context feeds today's brief. a chat forgets by lunch.")}</div>'''

# 6. LOOP - circular plan/act/check cycle that iterates until DONE (distinct from any linear scene)
def loop():
    cx,cy,R=306,232,150
    stg=[("PLAN",-90),("ACT",0),("CHECK",90),("LOG",180)]
    nodes=""
    pts={}
    for nm,a in stg:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a)); pts[nm]=(x,y,a)
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#241f1a" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".06em" fill="#e6d6c2">{nm}</text>')
    order=["PLAN","ACT","CHECK","LOG"]
    arcs=""
    for i in range(4):
        a0=pts[order[i]][2]; a1=pts[order[(i+1)%4]][2]
        r=R-2
        sa=math.radians(a0+16); ea=math.radians(a1-16)
        sx=cx+r*math.cos(sa); sy=cy+r*math.sin(sa); ex=cx+r*math.cos(ea); ey=cy+r*math.sin(ea)
        arcs+=f'<path d="M{sx:.0f} {sy:.0f} A{r} {r} 0 0 1 {ex:.0f} {ey:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="4" marker-end="url(#ah)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It works until the job is done","LOOP, NOT A REPLY")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><marker id="ah" markerWidth="9" markerHeight="9" refX="5" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9 Z" fill="rgb({ACC})"/></marker>
        <radialGradient id="dn" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="dg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {arcs}{nodes}
        <g filter="url(#dg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#dn)"/></g>
        <path d="M{cx-24} {cy-2} l16 17 l32 -34" fill="none" stroke="#1a0f0a" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="{cx}" y="{cy+40}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">DONE</text>
        <text x="{cx}" y="{cy+92}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">pass 3 / 3</text>
      </svg>
      {cap("one reply and a chat stops. a worker loops to done.")}</div>'''

# 7. BRIEFING - IVORY opened deliverable: the finished daily briefing, four sections you can open
def briefing():
    secs=[("RESEARCH","3 sources, ranked and read","done"),
          ("DRAFT","1 post, written in your voice","ready"),
          ("TASKS","5 queued and prioritized","sorted"),
          ("CALENDAR","2 conflicts flagged and moved","resolved")]
    rows=""
    for t,s,st in secs:
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.62);border:1px solid rgba(120,95,60,.14);border-left:4px solid #96562d;border-radius:14px;padding:16px 20px;margin-bottom:14px">'
          f'<div style="flex-shrink:0;width:40px;height:40px;border-radius:12px;background:rgba(150,90,45,.13);border:1px solid rgba(150,90,45,.28);display:flex;align-items:center;justify-content:center">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4 4L19 6"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:#96562d">{t}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#2a2016;margin-top:1px">{s}</div></div>'
          f'<div style="flex-shrink:0;font-family:\'DM Mono\';font-size:13px;color:#8a745a">{st}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {ivhead("Open it. The shift is finished.","DAILY BRIEFING")}
      <div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(120,95,60,.2);padding-bottom:12px;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:20px;color:#2a2016">Filed 06:20 &middot; one page</span>
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:#96562d">4 / 4 COMPLETE</span></div>
      {rows}
      {cap("a deliverable you open, not a thread you scroll.","#8a745a")}</div>'''

# 8. ROSTER - flat hire board: five job titles, one named worker each, cents per shift
def roster():
    hires=[("RESEARCH","CORTEX","0.02c"),("OUTBOUND","SPECTER","0.11c"),
           ("DEALS","STRIKER","0.11c"),("CONTENT","PULSE","0.11c"),("CODE","SENTINEL","0.40c")]
    rows=""
    for job,ag,cost in hires:
        rows+=(f'<div style="display:flex;align-items:center;gap:20px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:16px 22px;box-shadow:0 12px 24px rgba(0,0,0,.4)">'
          f'<div style="flex-shrink:0;width:118px"><div style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.14em;color:#8f8f85">{job}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:24px;color:rgb({ACC})">{ag}</div></div>'
          f'<svg width="30" height="14" viewBox="0 0 30 14" style="flex-shrink:0"><path d="M2 7h22M19 2l6 5-6 5" fill="none" stroke="rgba(212,162,127,.6)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<div style="flex:1;font-family:\'DM Sans\';font-size:16px;color:#a8a296">a named worker on the job</div>'
          f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:flex-end;gap:4px">'
          f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:13px;letter-spacing:.06em;color:#1a0f0a;background:rgb({ACC});padding:5px 13px;border-radius:999px">HIRED</span>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;color:rgb({ACC})">{cost}/shift</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Five roles. One hire each.","THE ROSTER")}
      <div style="display:flex;flex-direction:column;gap:14px;height:470px;justify-content:center">{rows}</div>
      {cap("same engine, a different job title. cents per shift, never a salary.")}</div>'''

PANELS={"proof":proof(),"badge":badge(),"clockin":clockin(),"tools":tools(),
        "memory":memory(),"loop":loop(),"briefing":briefing(),"roster":roster()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src43"; os.makedirs(outd,exist_ok=True)
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
