#!/usr/bin/env python3
# TIER 3 - ONE COMMAND, SEVEN HIRES: each panel a UNIQUE hand-built coded scene filling a clean
# rounded card (title + one-line caption, NO generic stat-chip strips, NO cuts/walls). Warm palette.
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

# 1. COMMAND - a terminal/console window: a plain-English order typed at a prompt, then routed
def command():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You type an order","PLAIN ENGLISH")}
      <div style="background:#141210;border:1px solid rgba(255,255,255,.09);border-radius:20px;overflow:hidden;box-shadow:inset 0 2px 3px rgba(255,255,255,.05),0 24px 44px rgba(0,0,0,.5)">
        <div style="display:flex;align-items:center;gap:9px;padding:15px 20px;background:linear-gradient(180deg,#26231f,#1c1a17);border-bottom:1px solid rgba(255,255,255,.06)">
          <span style="width:12px;height:12px;border-radius:50%;background:#c84623"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:rgb({ACC})"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#4a453d"></span>
          <span style="margin-left:12px;font-family:'DM Mono';font-size:14px;letter-spacing:.14em;color:#8f8f85">ULTRON &middot; COMMAND</span>
        </div>
        <div style="padding:30px 30px 28px">
          <div style="font-family:'DM Mono';font-size:24px;color:#eae4d8;line-height:1.55">
            <span style="color:rgb({ACC})">&rsaquo; </span>draft outreach to the 20 accounts<br>
            <span style="color:rgb({ACC})">&rsaquo; </span>CORTEX just ranked<span style="display:inline-block;width:13px;height:26px;background:rgb({ACC});margin-left:6px;vertical-align:-5px"></span>
          </div>
          <div style="margin-top:28px;display:flex;align-items:center;gap:14px">
            <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#7a7468">ROUTED</span>
            <svg width="30" height="16" viewBox="0 0 30 16" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 8h24M20 3l6 5-6 5"/></svg>
            <span style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#FAFAF7">SPECTER</span>
            <span style="font-family:'DM Mono';font-size:14px;color:#8f8f85">tier SMART &middot; ~0.1c</span>
          </div>
        </div>
      </div>
      {cap("plain english in - the right agent picks it up and runs, with zero setup.")}</div>'''

# 2. ROSTER - radial org chart: ROUTER hub at the centre, 7 named agent nodes around it
def roster():
    cx,cy,R=410,232,168
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),
            ("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    n=len(agents); spokes=""; nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="41" fill="#241f1a" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+17:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven named hires, one login","THE ROSTER")}
      <svg width="820" height="474" viewBox="0 0 820 474" style="display:block;margin:0 auto">
        <defs><radialGradient id="rhub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#rhub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">you</text>
        {nodes}
      </svg>
      {cap("each agent owns one job - call it by name or let the router route.")}</div>'''

# 3. DISPATCH - one job ticket routed and STAMPED to a chosen agent with its tier + cents cost
def dispatch():
    idle=["CORTEX idle","STRIKER idle","PULSE idle","COUNSEL idle"]
    idlerow="".join(f'<div style="flex:1;text-align:center;font-family:DM Mono;font-size:12px;color:#6f6a60;background:rgba(250,250,247,.03);border:1px solid rgba(255,255,255,.06);border-radius:12px;padding:12px 8px">{t}</div>' for t in idle)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It hands the job to the right one","DISPATCH")}
      <div style="display:flex;align-items:center;gap:20px;margin-top:6px">
        <div style="flex:1;background:linear-gradient(160deg,#2f2b26,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:20px 22px;box-shadow:0 18px 30px rgba(0,0,0,.5)">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#7a7468">INCOMING JOB</div>
          <div style="font-family:'DM Sans';font-weight:800;font-size:22px;color:#FAFAF7;margin-top:8px;line-height:1.25">Draft 12 follow-ups for the May cohort</div>
          <div style="font-family:'DM Sans';font-size:15px;color:#8f8f85;margin-top:6px">plain english, no config</div>
        </div>
        <div style="flex-shrink:0;text-align:center">
          <svg width="60" height="26" viewBox="0 0 60 26" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 13h48M44 5l10 8-10 8"/></svg>
          <div style="font-family:'DM Mono';font-size:11px;letter-spacing:.12em;color:rgb({ACC});margin-top:4px">ROUTER</div>
        </div>
        <div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:16px;padding:20px 22px;box-shadow:0 0 26px rgba(212,162,127,.28)">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:rgb({ACC})">ASSIGNED</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#FAFAF7;margin-top:6px">SPECTER</div>
          <div style="display:flex;gap:10px;margin-top:14px">
            <span style="font-family:'DM Mono';font-size:13px;color:#FAFAF7;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.4);border-radius:999px;padding:5px 12px">tier SMART</span>
            <span style="font-family:'DM Mono';font-size:13px;color:#1a0f0a;background:rgb({ACC});border-radius:999px;padding:5px 12px;font-weight:600">~0.11c</span>
          </div>
        </div>
      </div>
      <div style="display:flex;gap:12px;margin-top:20px">{idlerow}</div>
      {cap("the router reads each order, picks the owner and the cheapest tier that fits.")}</div>'''

# 4. BILL - IVORY invoice: the stack it replaces (struck four-figure lines) vs the cents run
def bill():
    rows=[("Agency retainer","$4,000 / mo"),("Freelance SDR","$1,800 / mo"),("Point tools x6","$540 / mo")]
    lines=""
    for label,amt in rows:
        lines+=(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:15px 0;border-bottom:1px solid rgba(120,95,60,.18)">'
          f'<span style="font-family:DM Sans;font-size:19px;color:#5a4634">{label}</span>'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:22px;color:rgb(200,70,35);text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)">{amt}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">The stack it replaces</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">MONTHLY BILL</span></div>
      {lines}
      <div style="display:flex;justify-content:space-between;align-items:center;margin-top:22px;background:rgba(150,86,45,.10);border:1.5px solid #96562d;border-radius:18px;padding:20px 24px">
        <div><div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:#96562d">ULTRON &middot; SAME WORK</div>
        <div style="font-family:'DM Sans';font-weight:700;font-size:17px;color:#5a4634;margin-top:3px">priced per run, not per seat</div></div>
        <div style="text-align:right"><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#2a2016;line-height:1">30c</span>
        <div style="font-family:'DM Mono';font-size:13px;color:#96562d">this run</div></div>
      </div>
      {cap("the four-figure retainers are the line item you cancel - ours runs in cents.","#8a745a")}</div>'''

# 5. DOSSIER - IVORY CORTEX brief: profile header + ranked signal bars + a grade
def dossier():
    bars=[("ICP fit",94),("Funding signal",88),("Hiring velocity",76),("Stack gap",81)]
    rows=""
    for label,pct in bars:
        rows+=(f'<div style="margin-bottom:16px">'
          f'<div style="display:flex;justify-content:space-between;margin-bottom:7px"><span style="font-family:DM Sans;font-weight:600;font-size:17px;color:#4a3f30">{label}</span>'
          f'<span style="font-family:DM Mono;font-size:15px;color:#96562d">{pct}</span></div>'
          f'<div style="height:12px;border-radius:6px;background:rgba(150,90,45,.14);overflow:hidden"><div style="width:{pct}%;height:100%;border-radius:6px;background:linear-gradient(90deg,#c98a5f,#96562d)"></div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:center;gap:18px;margin-bottom:22px">
        <div style="flex-shrink:0;width:66px;height:66px;border-radius:18px;background:linear-gradient(160deg,#c98a5f,#96562d);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:28px;color:#fdfbf6;box-shadow:0 12px 22px rgba(150,86,45,.34)">N</div>
        <div style="flex:1"><div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#2a2016">Northwind Robotics</div>
        <div style="font-family:DM Mono;font-size:14px;color:#96562d;letter-spacing:.06em">CORTEX BRIEF &middot; RANKED #3 OF 214</div></div>
        <div style="text-align:center;flex-shrink:0"><div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016;line-height:1">A</div>
        <div style="font-family:DM Mono;font-size:11px;color:#96562d">grade</div></div>
      </div>
      {rows}
      {cap("one name in, a ranked brief out - profiled before you read the first line.","#8a745a")}</div>'''

# 6. GATE - approval queue: pending agent actions, one lit and awaiting your tap
def gate():
    q=[("SPECTER","send 12 follow-up emails",True),
       ("AMPLIFY","publish the launch post",False),
       ("COUNSEL","send the NDA to Globex",False)]
    rows=""
    for agent,act,live in q:
        if live:
            btn=(f'<div style="flex-shrink:0;display:flex;align-items:center;gap:8px;background:rgb({ACC});border-radius:999px;padding:9px 18px">'
              f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
              f'<span style="font-family:DM Sans;font-weight:900;font-size:15px;color:#1a0f0a">your tap</span></div>')
            border=f'1.5px solid rgb({ACC})'; glow='box-shadow:0 0 24px rgba(212,162,127,.28)'
        else:
            btn='<span style="flex-shrink:0;font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#7a7468;border:1px solid rgba(255,255,255,.12);border-radius:999px;padding:9px 16px">HELD</span>'
            border='1px solid rgba(255,255,255,.09)'; glow=''
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(160deg,#2c2824,#201d19);border:{border};border-radius:16px;padding:18px 20px;{glow}">'
          f'<span style="flex-shrink:0;width:118px;font-family:DM Sans;font-weight:800;font-size:18px;color:rgb({ACC})">{agent}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-size:18px;color:#e2dccf">{act}</span>{btn}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","APPROVAL QUEUE")}
      <div style="display:flex;flex-direction:column;gap:16px">{rows}</div>
      <div style="display:flex;align-items:center;gap:10px;margin-top:18px;font-family:DM Mono;font-size:13px;color:#8f8f85">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>
        3 actions parked &middot; 0 sent &middot; waiting on you</div>
      {cap("every external move parks in a queue - you approve, hold or edit, then it fires.")}</div>'''

# 7. MEMORY - shared core: four labelled context shelves bracket into one, read by all seven
def memory():
    shelves=[("ICP","who you sell to"),("PIPELINE","every open deal"),
             ("PRICING","cents per action"),("DOCS","how the product works")]
    bars=""
    for k,v in shelves:
        bars+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(160deg,#322e29,#221f1b);border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:16px 20px;box-shadow:0 12px 22px rgba(0,0,0,.4)">'
          f'<span style="flex-shrink:0;width:110px;font-family:DM Mono;font-size:15px;letter-spacing:.1em;color:rgb({ACC})">{k}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-size:17px;color:#c9c3b8">{v}</span></div>')
    dots="".join('<span style="width:15px;height:15px;border-radius:50%;background:rgb('+ACC+');box-shadow:0 0 10px rgba(212,162,127,.6)"></span>' for _ in range(7))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every hire reads one memory","SHARED CORE")}
      <div style="display:flex;gap:24px;align-items:center">
        <div style="flex:1;display:flex;flex-direction:column;gap:12px">{bars}</div>
        <svg width="46" height="300" viewBox="0 0 46 300" style="flex-shrink:0"><path d="M6 12 Q40 12 40 150 Q40 288 6 288" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/><path d="M40 150 h6" stroke="rgb({ACC})" stroke-width="3"/></svg>
        <div style="flex-shrink:0;width:172px;text-align:center">
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7;line-height:1.2">Read by<br>all seven</div>
          <div style="display:flex;flex-wrap:wrap;gap:9px;justify-content:center;margin:16px auto 0;width:150px">{dots}</div>
          <div style="font-family:DM Mono;font-size:12px;color:#8f8f85;margin-top:14px">no one asks twice</div>
        </div>
      </div>
      {cap("icp, pipeline, pricing and docs in one core - nobody asks you twice.")}</div>'''

# 8. HANDOFF - horizontal relay: three agents pass a labelled payload into one booked outcome
def handoff():
    stations=[("CORTEX","ranks the account","brief"),
              ("SPECTER","writes the outreach","sequence"),
              ("STRIKER","works the reply","meeting")]
    cells=""
    for i,(nm,act,out) in enumerate(stations):
        cells+=(f'<div style="flex:1;background:linear-gradient(160deg,#322e29,#221f1b);border:1px solid rgba(255,255,255,.10);border-radius:18px;padding:20px 16px;text-align:center;box-shadow:0 16px 28px rgba(0,0,0,.45)">'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#c9c3b8;margin-top:6px;line-height:1.3">{act}</div></div>')
        if i<len(stations)-1:
            cells+=(f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:5px;padding:0 2px">'
              f'<span style="font-family:DM Mono;font-size:11px;color:rgb({ACC})">{out}</span>'
              f'<svg width="40" height="18" viewBox="0 0 40 18" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9h30M27 3l8 6-8 6"/></svg></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("They pass work to each other","THE CHAIN")}
      <div style="display:flex;align-items:center;gap:6px;margin:20px 0">{cells}</div>
      <div style="display:flex;align-items:center;gap:16px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:18px;padding:20px 24px;box-shadow:0 0 26px rgba(212,162,127,.26)">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><path d="M20 6 9 17l-5-5"/></svg>
        <div style="flex:1"><div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#FAFAF7">Meeting booked</div>
        <div style="font-family:DM Sans;font-size:15px;color:#8f8f85">one order in, a finished chain out, no handoff dropped</div></div>
        <span style="flex-shrink:0;font-family:DM Mono;font-size:13px;color:#1a0f0a;background:rgb({ACC});border-radius:999px;padding:7px 16px;font-weight:600">3 agents &middot; 1 order</span>
      </div>
      {cap("cortex briefs specter, specter feeds striker - you gave one command.")}</div>'''

PANELS={"command":command(),"roster":roster(),"dispatch":dispatch(),"bill":bill(),
        "dossier":dossier(),"gate":gate(),"memory":memory(),"handoff":handoff()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src41"; os.makedirs(outd,exist_ok=True)
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
