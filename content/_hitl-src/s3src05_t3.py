#!/usr/bin/env python3
# TIER 3 - OUTCOMES, NOT INSTRUCTIONS. Adapted from IG s3src05 (a "vibe-coding SOP: it is not a
# chatbot, it is an operator you give outcomes to, not instructions"). Re-told Ultron, founder-facing.
# Each panel is a UNIQUE hand-built coded scene in a clean rounded card. htitle + one cap. No stat-chip strips.
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

# 1. SHIFT - split compare: a chatbot bubble loop that dead-ends vs an operator that ships the outcome
def shift():
    left=('<div style="flex:1">'
      '<div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.12em;color:#8f8f85;margin-bottom:14px">CHATBOT</div>'
      + "".join(f'<div style="background:#241f1b;border:1px solid rgba(200,70,35,.28);border-radius:14px;padding:14px 16px;margin-bottom:12px;font-family:DM Sans;font-size:16px;color:#c9c3b8">{t}</div>' for t in ["how do I book demos?","try changing the copy","still nothing booked"])
      + f'<div style="display:flex;align-items:center;gap:8px;font-family:DM Mono;font-size:13px;color:rgb({RED})"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({RED})" stroke-width="2.6"><path d="M18 6 6 18M6 6l12 12"/></svg>you are still typing</div></div>')
    right=('<div style="flex:1">'
      f'<div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:14px">OPERATOR</div>'
      f'<div style="background:linear-gradient(160deg,#3a332b,#241f1a);border:1.5px solid rgb({ACC});border-radius:16px;padding:20px 22px;box-shadow:0 20px 40px rgba(0,0,0,.5),0 0 30px rgba(212,162,127,.22)">'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7;line-height:1">20</div>'
      f'<div style="font-family:DM Sans;font-size:17px;color:#d9d5cc;margin-top:2px">demos booked</div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.1);margin-top:16px;padding-top:14px;display:flex;align-items:center;gap:9px">'
      f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>'
      f'<span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">delivered, not discussed</span></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A chatbot answers. This acts.","CHAT VS OPERATOR")}
      <div style="display:flex;align-items:stretch;gap:26px;min-height:400px">
        {left}
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#6f6a60">VS</div></div>
        {right}
      </div>
      {cap("a chatbot hands you more to do. an operator finishes the job for you.")}</div>'''

# 2. BRIEF - a wax-sealed work order: one outcome line, the step list struck out
def brief():
    steps="".join(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:9px"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb({RED})" stroke-width="2.4"><path d="M18 6 6 18M6 6l12 12"/></svg><span style="font-family:DM Sans;font-size:15px;color:#7a746a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">{t}</span></div>' for t in ["find the leads","write each email","chase follow-ups","chase again"])
    seal=(f'<svg width="128" height="128" viewBox="0 0 128 128"><defs><radialGradient id="wax" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>'
      f'<filter id="ws" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="6" stdDeviation="9" flood-color="rgba(0,0,0,.5)"/></filter></defs>'
      f'<g filter="url(#ws)"><path d="M64 8 L78 22 L98 20 L100 40 L118 52 L108 70 L116 90 L96 96 L90 116 L70 110 L64 124 L58 110 L38 116 L32 96 L12 90 L20 70 L10 52 L28 40 L30 20 L50 22 Z" fill="url(#wax)"/></g>'
      f'<circle cx="64" cy="64" r="34" fill="none" stroke="rgba(42,22,12,.5)" stroke-width="2"/>'
      f'<text x="64" y="60" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="#2a160c">OPS</text>'
      f'<text x="64" y="76" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">BRIEF</text></svg>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You write the outcome","THE BRIEF")}
      <div style="display:flex;align-items:center;gap:30px;min-height:400px">
        <div style="flex:1">
          <div style="background:linear-gradient(160deg,#302a24,#211d18);border:1.5px solid rgba(212,162,127,.4);border-radius:18px;padding:26px 26px 24px;box-shadow:0 24px 44px rgba(0,0,0,.5)">
            <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:12px">WORK ORDER</div>
            <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;line-height:1.15">Book 20 qualified demos this week.</div>
            <div style="border-top:1px dashed rgba(255,255,255,.14);margin-top:20px;padding-top:16px">
              <div style="font-family:DM Mono;font-size:12px;color:#7a746a;margin-bottom:12px">STEPS YOU NO LONGER WRITE</div>
              {steps}
            </div>
          </div>
        </div>
        <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:10px">{seal}<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">SEALED</span></div>
      </div>
      {cap("one line of intent in. the system works out every step for itself.")}</div>'''

# 3. CREW - radial hub-and-spokes: ROUTER center assigns the 7 named agents
def crew():
    cx,cy,R=410,225,168
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes=""; nodes=""
    n=len(agents)
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        on=(i==1)
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.32)"; w=4.5 if on else 2
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="{w}" stroke-dasharray="{"none" if on else "3 7"}"/>'
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.13)"; fill="#332c25" if on else "#221f1b"
        glow=f' filter="url(#ng)"' if on else ""
        nodes+=(f'<g{glow}><circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="{fill}" stroke="{bd}" stroke-width="2"/></g>'
          f'<text x="{x:.0f}" y="{y-3:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="{"#FAFAF7" if on else "#c9c3b8"}">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="{"rgb("+ACC+")" if on else "#7a746a"}">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It hires its own crew","ROUTER + 7 AGENTS")}
      <svg width="820" height="454" viewBox="0 0 820 454" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter>
        <filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {spokes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+15}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">reads the job</text>
        {nodes}
      </svg>
      {cap("the router reads the brief and assigns the agent that owns the job.")}</div>'''

# 4. LOOP - self-correcting iteration ring: run, check, catch (red), retry, keep going
def loop():
    cx,cy,R=280,225,150
    stations=[("RUN","-90",False),("CHECK","0",False),("CATCH","90",True),("RETRY","180",False)]
    arc=""; nodes=""
    for i,(nm,a,bad) in enumerate(stations):
        ang=float(a); x=cx+R*math.cos(math.radians(ang)); y=cy+R*math.sin(math.radians(ang))
        col=f"rgb({RED})" if bad else f"rgb({ACC})"
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="{"#2a1c17" if bad else "#2b2620"}" stroke="{col}" stroke-width="2.4"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="{col if bad else "#FAFAF7"}">{nm}</text>')
    # curved arrows between stations along the ring
    pts=[]
    for _,a,_ in stations:
        ang=float(a); pts.append((cx+R*math.cos(math.radians(ang)),cy+R*math.sin(math.radians(ang))))
    ring=(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="3" stroke-dasharray="6 10"/>'
      f'<path d="M {cx+R} {cy-8} a10 10 0 0 1 0 0 l-14 -12 m14 12 l-14 12" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round"/>')
    center=(f'<circle cx="{cx}" cy="{cy}" r="60" fill="#211d18" stroke="rgba(212,162,127,.3)" stroke-width="1.5"/>'
      f'<text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="rgb({ACC})">14</text>'
      f'<text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">retries, 0 asks</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="450" height="420" viewBox="0 0 560 454" style="flex-shrink:0">
        {ring}{center}{nodes}
        <text x="{cx+R+2:.0f}" y="{cy-58:.0f}" font-family="DM Mono" font-size="12" fill="rgb({RED})">error found</text>
      </svg>
      <div style="flex:1;min-width:0">
        {htitle("Fixes its own mistakes","THE LOOP")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">It runs the work, catches its own error, and retries. No stall, no ping asking you what to do next.</div>
        {cap("it keeps iterating for hours until the outcome is actually done.")}
      </div></div>'''

# 5. MEMORY - IVORY ledger: it reads your whole business, one indexed core
def memory():
    rows=[("ICP","2-50 emp, founder-led","842 accounts"),("PIPELINE","open + stage + owner","31 deals"),
          ("PRICING","tiers, terms, floors","live"),("DOCS","product, specs, faqs","118 files"),
          ("PAST DEALS","won, lost, why","5 quarters")]
    rr=""
    for nm,desc,val in rows:
        rr+=(f'<div style="display:flex;align-items:center;gap:16px;padding:15px 18px;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.14);border-radius:14px;margin-bottom:11px;box-shadow:0 6px 14px rgba(150,120,80,.1)">'
          f'<div style="flex-shrink:0;width:120px;font-family:DM Mono;font-size:13px;letter-spacing:.08em;color:#96562d">{nm}</div>'
          f'<div style="flex:1;font-family:DM Sans;font-size:16px;color:#3a2f22">{desc}</div>'
          f'<div style="flex-shrink:0;font-family:DM Sans;font-weight:800;font-size:16px;color:#2a2016">{val}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("It knows your whole business","SHARED MEMORY","#2a2016")}
      <div style="display:flex;align-items:center;gap:24px">
        <div style="flex:1">{rr}</div>
        <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:8px;width:130px">
          <svg width="110" height="110" viewBox="0 0 110 110"><defs><radialGradient id="mc" cx="40%" cy="34%"><stop offset="0%" stop-color="#c99a6d"/><stop offset="100%" stop-color="#96562d"/></radialGradient></defs>
          <circle cx="55" cy="55" r="40" fill="url(#mc)"/>
          {"".join(f'<line x1="55" y1="55" x2="{55+52*math.cos(math.radians(a)):.0f}" y2="{55+52*math.cos(math.radians(a))*0+52*math.sin(math.radians(a)):.0f}" stroke="rgba(150,90,45,.4)" stroke-width="2"/>' for a in range(-90,270,72))}
          <circle cx="55" cy="55" r="40" fill="none" stroke="rgba(255,255,255,.5)" stroke-width="1.5"/>
          <text x="55" y="52" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="13" fill="#fff">ONE</text>
          <text x="55" y="68" text-anchor="middle" font-family="DM Mono" font-size="9" fill="#f3e6d5">CORE</text></svg>
          <span style="font-family:DM Mono;font-size:11px;color:#96562d;text-align:center">every agent<br>reads it</span>
        </div>
      </div>
      {cap("icp, pipeline, pricing, docs. one memory, nothing forgets you.","#8a745a")}</div>'''

# 6. GATE - approval queue: pending outbound actions each parked for your one tap, a lock on the gate
def gate():
    items=[("SPECTER","12 cold emails","ready to send"),("STRIKER","Q3 proposal","ready to send"),("PULSE","launch post","ready to send")]
    q=""
    for nm,what,st in items:
        q+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(160deg,#2e2823,#211d18);border:1px solid rgba(212,162,127,.22);border-radius:15px;padding:16px 18px;margin-bottom:13px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><span style="font-family:DM Mono;font-size:11px;color:rgb({ACC})">{nm[:3]}</span></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{what}</div><div style="font-family:DM Mono;font-size:12px;color:#8f8f85">{st}</div></div>'
          f'<div style="flex-shrink:0;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:14px;padding:9px 18px;border-radius:999px;box-shadow:0 6px 14px rgba(212,162,127,.35)">TAP</div></div>')
    lock=(f'<svg width="120" height="120" viewBox="0 0 120 120"><rect x="18" y="14" width="84" height="92" rx="20" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>'
      f'<g transform="translate(38,40)"><rect x="0" y="26" width="44" height="34" rx="8" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/><path d="M8 26 V16 a14 14 0 0 1 28 0 v10" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/></g></svg>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:28px;min-height:400px">
        <div style="flex:1">{q}</div>
        <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:12px">{lock}<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC});text-align:center">held at<br>the gate</span></div>
      </div>
      {cap("it does the work. every outbound move parks for your one tap.")}</div>'''

# 7. COST - IVORY receipt compare: competitor seat licences (high $) vs Ultron cents per job
def cost():
    def bar(label,val,frac,red,note):
        col="rgb(200,70,35)" if red else "#96562d"
        w=int(frac*380)
        return (f'<div style="margin-bottom:26px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:9px">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.06em;color:#5a4634">{label}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:30px;color:{col}">{val}</span></div>'
          f'<div style="height:26px;background:rgba(150,120,80,.14);border-radius:8px;overflow:hidden"><div style="height:100%;width:{w}px;background:linear-gradient(90deg,{col},{col});border-radius:8px"></div></div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:#8a745a;margin-top:7px">{note}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("They bill seats. You pay cents.","PAY PER TOKEN","#2a2016")}
      <div style="padding:8px 4px 0">
        {bar("THE OLD STACK - 4 SEATS","$1,200 / mo",1.0,True,"per-seat licences you pay whether you use them or not")}
        {bar("ULTRON - THE SAME WEEK OF WORK","cents",0.06,False,"pay per token, only for work actually finished")}
      </div>
      <div style="margin-top:6px;padding:16px 18px;background:rgba(255,255,255,.5);border-left:4px solid #96562d;border-radius:12px;font-family:DM Sans;font-size:17px;color:#3a2f22">No seats to fill. No idle licences. A booked-demo brief costs cents.</div>
      {cap("the expensive stack is theirs. every finished job here is cents.","#8a745a")}</div>'''

# 8. OPERATOR - one login: a control board, whole crew reporting, the outcome DELIVERED
def operator():
    crew=[("CORTEX","842 accounts ranked"),("SPECTER","12 emails queued"),("STRIKER","proposal drafted"),("AMPLIFY","scheduled 9:00")]
    rows=""
    for nm,st in crew:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;padding:13px 16px;background:rgba(255,255,255,.03);border-bottom:1px solid rgba(255,255,255,.06)">'
          f'<div style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 10px rgba(212,162,127,.6)"></div>'
          f'<span style="flex-shrink:0;width:104px;font-family:DM Mono;font-size:12.5px;letter-spacing:.06em;color:rgb({ACC})">{nm}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-size:16px;color:#d9d5cc">{st}</span>'
          f'<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg></div>')
    win=(f'<div style="border-radius:20px;overflow:hidden;border:1px solid rgba(255,255,255,.09);box-shadow:0 30px 56px rgba(0,0,0,.5)">'
      f'<div style="display:flex;align-items:center;gap:8px;padding:14px 18px;background:#1a1815;border-bottom:1px solid rgba(255,255,255,.07)">'
      f'<span style="width:11px;height:11px;border-radius:50%;background:#3a352e"></span><span style="width:11px;height:11px;border-radius:50%;background:#3a352e"></span><span style="width:11px;height:11px;border-radius:50%;background:#3a352e"></span>'
      f'<span style="margin-left:10px;font-family:DM Mono;font-size:12px;color:#8f8f85">app.51ultron.com  ·  one brief</span></div>'
      f'<div style="background:linear-gradient(160deg,#252420,#1b1a17)">'
      f'<div style="display:flex;align-items:center;justify-content:space-between;padding:18px 20px;background:linear-gradient(160deg,#3a332b,#241f1a)">'
      f'<div><div style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:rgb({ACC})">OUTCOME</div><div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">20 demos booked</div></div>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:15px;color:#1a0f0a;background:rgb({ACC});padding:9px 18px;border-radius:999px">DELIVERED</div></div>'
      f'{rows}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One login runs the whole crew","ONE OPERATOR")}
      {win}
      {cap("brief it once. brain, crew, memory and gate report back in one place.")}</div>'''

PANELS={"shift":shift(),"brief":brief(),"crew":crew(),"loop":loop(),
        "memory":memory(),"gate":gate(),"cost":cost(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src05"; os.makedirs(outd,exist_ok=True)
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
