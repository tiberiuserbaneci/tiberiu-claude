#!/usr/bin/env python3
# TIER 3 - THE COLD-START ROADMAP (8-step founder launch playbook, Ultron). Each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO stat-chip strips.
# Reframe of the "Complete Roadmap to Launch a Product with Claude" source into a founder pipeline
# roadmap: research -> watch -> write -> route -> qualify -> gate -> memory -> booked. Cents pricing.
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

# 1. TARGETS - ranked target board, horizontal fit-score bars (CORTEX research)
def targets():
    rows=[("Northwind Robotics","hiring 3 ops roles",94),
          ("Globex Systems","raised $4M in May",89),
          ("Initech","no operator layer yet",83),
          ("Umbrella Retail","switched CRM last week",78)]
    items=""
    for i,(a,b,p) in enumerate(rows):
        items+=f'''<div style="display:flex;align-items:center;gap:20px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:16px 20px;box-shadow:0 14px 26px rgba(0,0,0,.4), inset 0 2px 2px rgba(255,255,255,.06)">
          <div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:22px;color:rgb({ACC})">{i+1}</div>
          <div style="flex:1;min-width:0">
            <div style="font-family:'DM Sans';font-weight:800;font-size:22px;color:#FAFAF7">{a}</div>
            <div style="font-family:'DM Sans';font-size:15px;color:#8f8f85;margin-bottom:8px">{b}</div>
            <div style="height:8px;border-radius:6px;background:rgba(250,250,247,.08);overflow:hidden"><div style="height:100%;width:{p}%;border-radius:6px;background:linear-gradient(90deg,#8a4a2c,rgb({ACC}))"></div></div>
          </div>
          <div style="flex-shrink:0;text-align:right"><span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:rgb({ACC})">{p}</span><div style="font-family:'DM Mono';font-size:10px;letter-spacing:.12em;color:#8f8f85">FIT</div></div>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Who to hit, ranked","STEP 01 / 08")}
      <div style="display:flex;flex-direction:column;gap:14px">{items}</div>
      {cap("CORTEX profiles your market and scores fit - best accounts first.")}</div>'''

# 2. SIGNALS - vertical timeline feed of dated buying triggers (EYES)
def signals():
    ev=[("MON 09:04","Northwind raised $4M","FUNDING"),
        ("TUE 11:20","Globex opened 3 SDR roles","HIRING"),
        ("WED 08:15","Initech dropped its old CRM","STACK"),
        ("THU 16:38","Umbrella VP hit your pricing page","INTENT")]
    rows=""
    for i,(d,t,tag) in enumerate(ev):
        rows+=f'''<div style="display:flex;align-items:flex-start;gap:22px;position:relative;padding-bottom:{0 if i==len(ev)-1 else 26}px">
          <div style="flex-shrink:0;position:relative;z-index:2;width:20px;height:20px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 16px rgba(212,162,127,.7);border:3px solid #1d1d1b;margin-top:4px"></div>
          <div style="flex:1">
            <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:rgb({ACC})">{d}</div>
            <div style="font-family:'DM Sans';font-weight:700;font-size:21px;color:#FAFAF7;margin-top:2px">{t}</div>
          </div>
          <span style="flex-shrink:0;font-family:'DM Mono';font-size:11px;letter-spacing:.12em;color:#c9c3b8;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.3);border-radius:999px;padding:6px 13px;margin-top:4px">{tag}</span>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The buying window opens","STEP 02 / 08")}
      <div style="position:relative;padding-left:4px">
        <div style="position:absolute;left:13px;top:12px;bottom:34px;width:2px;background:linear-gradient(180deg,rgb({ACC}),rgba(212,162,127,.15))"></div>
        {rows}
      </div>
      {cap("funding, hiring, stack, intent - EYES flags the trigger the day it fires.")}</div>'''

# 3. WRITE - IVORY cold-email mockup written in your voice (SPECTER)
def write():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Written in your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">STEP 03 / 08</span></div>
      <div style="background:rgba(255,255,255,.66);border:1px solid rgba(120,95,60,.18);border-radius:18px;padding:24px 26px;box-shadow:0 18px 34px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.9)">
        <div style="display:flex;justify-content:space-between;border-bottom:1px solid rgba(120,95,60,.16);padding-bottom:12px;margin-bottom:14px">
          <span style="font-family:'DM Mono';font-size:14px;color:#8a745a">To: ops@northwind.co</span>
          <span style="font-family:'DM Mono';font-size:14px;color:#96562d">SPECTER · draft 1</span></div>
        <div style="font-family:'DM Sans';font-weight:800;font-size:21px;color:#2a2016;margin-bottom:12px">Saw the 3 ops roles.</div>
        <div style="font-family:'DM Sans';font-size:18px;color:#4a3a28;line-height:1.5">You are staffing ops fast. We cut that load to one operator for founders your size. Worth 10 minutes?</div>
      </div>
      <div style="display:flex;gap:20px;margin-top:18px;flex-wrap:wrap">
        {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["your cadence","no hedging","62 words","trigger-led"])}
      </div>
      {cap("sampled from your real posts. banned words enforced on every draft.","#8a745a")}</div>'''

# 4. ROUTE - tier lanes, SMART lit, cents per turn, old-way high $ crossed (ROUTER)
def route():
    lanes=[("LITE","quick lookups","0.02c",False),
           ("SMART","daily outreach","0.11c",True),
           ("DEEP","hard judgement","0.40c",False)]
    rows=""
    for nm,role,cost,on in lanes:
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="box-shadow:0 0 26px rgba(212,162,127,.28), inset 0 2px 2px rgba(255,255,255,.08);" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">ROUTER PICKED</span>' if on else '<span style="font-family:DM Mono;font-size:12px;color:#6f6a60">idle</span>'
        rows+=f'''<div style="display:flex;align-items:center;gap:22px;background:{bg};border:1.5px solid {bd};border-radius:16px;padding:18px 22px;{glow}">
          <div style="flex-shrink:0;width:150px"><div style="font-family:'DM Mono';font-size:14px;letter-spacing:.14em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</div><div style="font-family:'DM Sans';font-size:14px;color:#8f8f85">{role}</div></div>
          <div style="flex:1">{pick}</div>
          <div style="flex-shrink:0;text-align:right"><span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:{f'rgb({ACC})' if on else '#9a9488'}">{cost}</span><div style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:#8f8f85">PER TURN</div></div>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The cheapest brain per job","STEP 04 / 08")}
      <div style="display:flex;flex-direction:column;gap:14px">{rows}</div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:16px;background:rgba(200,70,35,.07);border:1px dashed rgba(200,70,35,.35);border-radius:14px;padding:13px 18px">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#c84623;flex-shrink:0">THE OLD WAY</span>
        <span style="font-family:'DM Sans';font-size:17px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">$2,000 / mo SDR seat plus a tool stack</span></div>
      {cap("the router reads each turn and bills cents - not a retainer.")}</div>'''

# 5. QUALIFY - inbound reply + BANT checklist + booked verdict (STRIKER)
def qualify():
    checks=[("BUDGET","approved this quarter"),("AUTHORITY","VP of Ops, decision maker"),
            ("NEED","ops team underwater"),("TIMING","wants a call this week")]
    rows=""
    for k,v in checks:
        rows+=f'''<div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)">
          <svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.16)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span style="flex-shrink:0;width:118px;font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:rgb({ACC})">{k}</span>
          <span style="flex:1;font-family:'DM Sans';font-size:17px;color:#d9d5cc">{v}</span></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;gap:30px;align-items:stretch">
      <div style="flex-shrink:0;width:300px;display:flex;flex-direction:column;gap:16px">
        <div style="background:#211d19;border:1px solid rgba(212,162,127,.28);border-left:4px solid rgb({ACC});border-radius:16px;padding:18px 20px">
          <div style="font-family:'DM Mono';font-size:12px;color:#8f8f85;margin-bottom:8px">REPLY · 09:41</div>
          <div style="font-family:'DM Sans';font-size:19px;color:#FAFAF7;line-height:1.4">"Interesting. What would this look like for a team our size?"</div></div>
        <div style="margin-top:auto;background:rgb({ACC});border-radius:16px;padding:18px 20px;box-shadow:0 14px 28px rgba(212,162,127,.35)">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:rgba(26,15,10,.7)">STRIKER VERDICT</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#1a0f0a;margin-top:2px">Qualified. Booked.</div></div>
      </div>
      <div style="flex:1">
        {htitle("It qualifies the reply","STEP 05 / 08")}
        {rows}
        {cap("budget, authority, need, timing - scored before it reaches you.")}
      </div></div>'''

# 6. GATE - full ready-to-send batch held on the operator's tap (HUMAN GATE)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing sends without you","STEP 06 / 08")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="205" cy="210" r="128" fill="url(#orb)"/></g>
        <text x="205" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="42" fill="#2a160c">240</text>
        <text x="205" y="234" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".12em">EMAILS READY</text>
        <path d="M340 210 H600" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="612" y="140" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(654,178)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="682" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every send parks at the human gate. augmented outbound, never unsupervised.")}</div>'''

# 7. MEMORY - IVORY radial core, company facts orbiting, feeds every agent (shared memory)
def memory():
    cx,cy=210,215; R=150
    facts=[("ICP",-90),("PIPELINE",-18),("PRICING",54),("DOCS",126),("HISTORY",198)]
    parts=""
    for nm,a in facts:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        parts+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.35)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="36" fill="#fbf6ee" stroke="rgba(150,90,45,.3)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".04em" fill="#96562d">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px;display:flex;align-items:center;gap:20px">
      <svg width="420" height="430" viewBox="0 0 420 430" style="flex-shrink:0">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="#c07a4e"/><stop offset="100%" stop-color="#96562d"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgba(150,90,45,.4)"/></filter></defs>
        {parts}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#fffdf9">MEMORY</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#ffeede">one core</text>
      </svg>
      <div style="flex:1">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
          <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">One memory, seven agents</span>
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">STEP 07 / 08</span></div>
        <div style="font-family:'DM Sans';font-size:19px;color:#4a3a28;line-height:1.45">Your ICP, pipeline, pricing and docs live in one core. Every agent draws from it, so nothing is explained twice and nothing is forgotten.</div>
        {cap("no memory, no compounding. this is the part that gets smarter.","#8a745a")}
      </div></div>'''

# 8. BOOKED - week calendar with booked slots + cents cost readout (the outcome)
def booked():
    days=["MON","TUE","WED","THU","FRI"]
    bset={(0,1),(1,0),(1,2),(2,2),(3,1),(3,3),(4,0)}
    cols=""
    for d in range(5):
        cells=""
        for s in range(4):
            if (d,s) in bset:
                cells+=f'<div style="height:46px;border-radius:9px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 60%,#9a5a35);box-shadow:0 6px 14px rgba(212,162,127,.35), inset 0 2px 2px rgba(255,255,255,.4);display:flex;align-items:center;justify-content:center;font-family:DM Mono;font-size:11px;color:#1a0f0a;font-weight:500">MEET</div>'
            else:
                cells+='<div style="height:46px;border-radius:9px;background:rgba(250,250,247,.05);border:1px solid rgba(255,255,255,.05)"></div>'
        cols+=f'''<div style="flex:1;display:flex;flex-direction:column;gap:10px">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:#8f8f85;text-align:center">{days[d]}</div>{cells}</div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The week fills up","STEP 08 / 08")}
      <div style="display:flex;gap:12px;margin-bottom:20px">{cols}</div>
      <div style="display:flex;gap:16px">
        <div style="flex:1;background:#211d19;border:1px solid rgba(212,162,127,.28);border-radius:16px;padding:18px 22px">
          <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:rgb({ACC})">7 meetings</div>
          <div style="font-family:'DM Sans';font-size:15px;color:#8f8f85">booked this week</div></div>
        <div style="flex:1;background:#211d19;border:1px solid rgba(212,162,127,.28);border-radius:16px;padding:18px 22px">
          <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#FAFAF7">cents</div>
          <div style="font-family:'DM Sans';font-size:15px;color:#8f8f85">not an SDR salary</div></div>
      </div>
      {cap("zero to pipeline while you build the product.")}</div>'''

PANELS={"targets":targets(),"signals":signals(),"write":write(),"route":route(),
        "qualify":qualify(),"gate":gate(),"memory":memory(),"booked":booked()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src36"; os.makedirs(outd,exist_ok=True)
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
