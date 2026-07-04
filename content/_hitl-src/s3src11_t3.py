#!/usr/bin/env python3
# TIER 3 - THREE PARTS, NO CODE (s3src11). Adapted from an IG carousel ("I built a personal AI agent
# in 20 minutes, no code"): a chat becomes an agent when you add three parts - tools it calls itself,
# memory that persists, a loop that runs until done - and Ultron ships all three pre-wired, no code.
# Each panel is a UNIQUE hand-built coded scene in a clean rounded card. WIRE-ITS-EYES bar.
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

# 1. CHAT - a chat transcript that dead-ends: you ask, it answers, then it waits. HTML bubbles + red wall.
def chat():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("A chat answers, then stops","CHAT ONLY")}
      <div style="display:flex;flex-direction:column;gap:16px;height:474px">
        <div style="align-self:flex-end;max-width:600px;background:linear-gradient(160deg,#3a352f,#26221e);border:1px solid rgba(255,255,255,.10);border-radius:20px 20px 6px 20px;padding:18px 22px;box-shadow:0 16px 30px rgba(0,0,0,.45)">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:6px">YOU</div>
          <div style="font-family:'DM Sans';font-size:20px;color:#FAFAF7;line-height:1.4">Find trending topics, pick the best one, draft a post and save it.</div></div>
        <div style="align-self:flex-start;max-width:620px;background:linear-gradient(160deg,#2a2723,#201d19);border:1px solid rgba(255,255,255,.08);border-radius:20px 20px 20px 6px;padding:18px 22px;box-shadow:0 16px 30px rgba(0,0,0,.45)">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#9a9488;margin-bottom:6px">CHATBOT</div>
          <div style="font-family:'DM Sans';font-size:20px;color:#d9d5cc;line-height:1.4">Sure. Here are five topics you could write about...</div></div>
        <div style="margin-top:auto;display:flex;align-items:center;gap:16px;background:rgba(200,70,35,.09);border:1px solid rgba(200,70,35,.36);border-radius:16px;padding:18px 22px">
          <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="rgb(200,70,35)" stroke-width="2.4" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
          <div style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#e0b6a6">Then it waits. You still do the rest.</div></div>
      </div>
      {cap("it talks, then nothing moves. the work is still sitting on your desk.")}</div>'''

# 2. PARTS - the formula, as a plate equation: CHAT + TOOLS + MEMORY + LOOP = one glowing AGENT bar.
def parts():
    def plate(lab,sub):
        return (f'<div style="flex:1;background:linear-gradient(160deg,#2f2b27,#211e1a);border:1.4px solid rgba(255,255,255,.10);border-radius:18px;padding:20px 8px;text-align:center;box-shadow:0 14px 26px rgba(0,0,0,.5)">'
                f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:21px;color:#FAFAF7">{lab}</div>'
                f'<div style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.04em;color:rgb({ACC});margin-top:6px">{sub}</div></div>')
    plus='<div style="flex-shrink:0;font-family:\'DM Sans\';font-weight:900;font-size:30px;color:#6f6a60;padding:0 2px">+</div>'
    row=plate("CHAT","the model")+plus+plate("TOOLS","it calls")+plus+plate("MEMORY","it keeps")+plus+plate("LOOP","it runs")
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("A chat plus three parts","THE FORMULA")}
      <div style="display:flex;align-items:stretch;gap:8px;height:150px">{row}</div>
      <div style="text-align:center;font-family:'DM Sans';font-weight:900;font-size:40px;color:#6f6a60;margin:14px 0 12px">=</div>
      <div style="background:linear-gradient(160deg,#453d33,#241f1a);border:1.8px solid rgb({ACC});border-radius:22px;padding:26px 30px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 26px 50px rgba(212,162,127,.26), inset 0 2px 3px rgba(255,255,255,.1)">
        <div><div style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#FAFAF7;line-height:1">AGENT</div>
          <div style="font-family:'DM Sans';font-size:17px;color:#c9a583;margin-top:4px">runs the whole job without you</div></div>
        <div style="width:80px;height:80px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#f0c49e,rgb({ACC}) 55%,#7a4326);box-shadow:0 0 30px rgba(212,162,127,.5)"></div></div>
      {cap("more of the three you add, the less of the job lands back on you.")}</div>'''

# 3. TOOLS - radial call-out: a central agent core reaches out to five tools it fires itself.
def tools():
    cx,cy,R=306,232,168
    ic={
      "Search web":'<circle cx="0" cy="-1" r="8" fill="none" stroke="rgb({A})" stroke-width="2.4"/><line x1="6" y1="5" x2="13" y2="12" stroke="rgb({A})" stroke-width="2.6" stroke-linecap="round"/>',
      "Send email":'<rect x="-12" y="-8" width="24" height="17" rx="2.5" fill="none" stroke="rgb({A})" stroke-width="2.2"/><path d="M-12 -6 L0 3 L12 -6" fill="none" stroke="rgb({A})" stroke-width="2.2"/>',
      "Draft post":'<path d="M-10 10 L-10 3 L6 -13 L13 -6 L-3 10 Z" fill="none" stroke="rgb({A})" stroke-width="2.2" stroke-linejoin="round"/><line x1="2" y1="-9" x2="9" y2="-2" stroke="rgb({A})" stroke-width="2.2"/>',
      "Run code":'<path d="M-4 -9 L-13 0 L-4 9" fill="none" stroke="rgb({A})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 -9 L13 0 L4 9" fill="none" stroke="rgb({A})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
      "Book time":'<rect x="-12" y="-10" width="24" height="21" rx="3" fill="none" stroke="rgb({A})" stroke-width="2.2"/><line x1="-12" y1="-4" x2="12" y2="-4" stroke="rgb({A})" stroke-width="2.2"/><line x1="-6" y1="-14" x2="-6" y2="-8" stroke="rgb({A})" stroke-width="2.2" stroke-linecap="round"/><line x1="6" y1="-14" x2="6" y2="-8" stroke="rgb({A})" stroke-width="2.2" stroke-linecap="round"/>',
    }
    order=[("Search web",-90),("Send email",-25),("Draft post",41),("Run code",139),("Book time",205)]
    edges="";nodes=""
    for nm,a in order:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        ly=y+56 if math.sin(math.radians(a))>0.2 else y-46
        edges+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
          f'<g transform="translate({x:.0f},{y:.0f})">{ic[nm].replace("{A}",ACC)}</g>'
          f'<text x="{x:.0f}" y="{ly:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It reaches for its own tools","PART 1 · TOOLS")}
      <svg width="612" height="486" viewBox="0 0 612 486" style="display:block;margin:0 auto">
        <defs><radialGradient id="tc" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="tg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#tg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#tc)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">AGENT</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">calls itself</text></svg>
      {cap("no copy-paste between tabs. it picks up the tool the job needs.")}</div>'''

# 4. MEMORY - persistence: five day-sessions across the top, all drawing from one shared store below.
def memory():
    sess=[("MON",110),("TUE",258),("WED",406),("THU",554),("FRI",702)]
    tops="";lines=""
    for nm,x in sess:
        lines+=f'<line x1="{x}" y1="122" x2="{x}" y2="300" stroke="rgba(212,162,127,.34)" stroke-width="2.2" stroke-dasharray="4 6"/>'
        tops+=(f'<circle cx="{x}" cy="92" r="30" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="1.6"/>'
          f'<text x="{x}" y="97" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#d9d5cc">{nm}</text>')
    facts=["ICP","PRICING","PIPELINE","YOUR VOICE"];chips=""
    fx=88
    for f in facts:
        w=len(f)*13+52
        chips+=(f'<g><rect x="{fx}" y="352" width="{w}" height="46" rx="12" fill="rgba(212,162,127,.12)" stroke="rgba(212,162,127,.4)"/>'
          f'<text x="{fx+w/2:.0f}" y="381" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".05em" fill="rgb({ACC})">{f}</text></g>')
        fx+=w+22
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It remembers every session","PART 2 · MEMORY")}
      <svg width="820" height="472" viewBox="0 0 820 472" style="display:block;margin:0 auto">
        {lines}{tops}
        <rect x="40" y="300" width="740" height="150" rx="22" fill="#211d19" stroke="rgba(212,162,127,.34)" stroke-width="1.6"/>
        <text x="66" y="332" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#8f8f85">PERSISTENT STORE</text>
        {chips}
        <text x="66" y="430" font-family="DM Sans" font-size="15" fill="#a8a296">written once, carried into every run</text></svg>
      {cap("ICP, pricing, your voice: told once, never re-explained.")}</div>'''

# 5. LOOP - a circular arrow cycle (plan/act/check/learn) that runs until it exits to DONE.
def loop():
    cx,cy,R=232,214,150
    nodes=[("PLAN",-90),("ACT",0),("CHECK",90),("LEARN",180)]
    ring="";nd=""
    for nm,a in nodes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        lx=x; ly=y
        off={"PLAN":(0,-46),"ACT":(0,-44),"CHECK":(0,60),"LEARN":(0,-44)}[nm]
        nd+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="12" fill="rgb({ACC})" stroke="#1a1613" stroke-width="3"/>'
          f'<text x="{x+off[0]:.0f}" y="{y+off[1]:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#d9d5cc">{nm}</text>')
    # clockwise arc top -> left (270 deg), arrowhead at the left node pointing up
    ax=cx-R; ay=cy
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It runs until the job is done","PART 3 · LOOP")}
      <svg width="600" height="452" viewBox="0 0 600 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="lc" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="lg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="6"/>
        <path d="M{cx} {cy-R} A{R} {R} 0 1 1 {ax} {ay}" fill="none" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>
        <path d="M{ax-11} {ay+4} L{ax} {ay-16} L{ax+11} {ay+4} Z" fill="rgb({ACC})"/>
        {nd}
        <g filter="url(#lg)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#lc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">RUNS</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">on its own</text>
        <line x1="{cx+R}" y1="{cy}" x2="452" y2="{cy}" stroke="rgb({ACC})" stroke-width="3" stroke-dasharray="3 7"/>
        <rect x="452" y="{cy-34}" width="120" height="68" rx="16" fill="#211d19" stroke="rgb({ACC})" stroke-width="2"/>
        <path d="M470 {cy} l12 12 l22 -26" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="512" y="{cy+30}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">DONE</text></svg>
      {cap("plan, act, check, repeat. it stops when the work is finished, not you.")}</div>'''

# 6. NOCODE - IVORY: a plain-English instruction note becomes a live agent. No repo, no deploy.
def nocode():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">You describe it in plain English</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">ZERO CODE</span></div>
      <div style="background:rgba(255,255,255,.66);border-left:4px solid #96562d;border-radius:14px;padding:24px 26px;box-shadow:0 12px 26px rgba(120,95,60,.14)">
        <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#96562d;margin-bottom:12px">SYSTEM PROMPT</div>
        <div style="font-family:'DM Sans';font-size:22px;color:#2a2016;line-height:1.5">You are my research agent. Every morning scan my market, rank what changed, and send me a one-page brief.<span style="display:inline-block;width:3px;height:22px;background:#96562d;margin-left:4px;transform:translateY(4px)"></span></div>
      </div>
      <div style="display:flex;align-items:center;gap:16px;margin-top:20px">
        <div style="display:flex;align-items:center;gap:12px;background:#96562d;border-radius:999px;padding:12px 22px">
          <span style="width:16px;height:16px;border-radius:50%;background:#fdfbf6;box-shadow:0 0 12px rgba(253,251,246,.7)"></span>
          <span style="font-family:'DM Sans';font-weight:900;font-size:17px;letter-spacing:.06em;color:#fdfbf6">LIVE</span></div>
        <div style="font-family:'DM Sans';font-weight:700;font-size:18px;color:#5a4634">0 lines of code &middot; 0 servers</div></div>
      {cap("one paragraph of instruction is the whole build.","#8a745a")}</div>'''

# 7. PICK - a selector grid of job tiles; you switch on the one you need, one lit as picked.
def pick():
    ag=[("CORTEX","research",True),("PULSE","content",False),("SENTINEL","code",False),
        ("SPECTER","outbound",False),("STRIKER","deals",False),("COUNSEL","legal",False)]
    tiles=""
    for nm,role,on in ag:
        bg="linear-gradient(160deg,#453d33,#241f1a)" if on else "linear-gradient(160deg,#2b2824,#201d19)"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        gl="box-shadow:0 20px 40px rgba(212,162,127,.26);" if on else "box-shadow:0 12px 24px rgba(0,0,0,.45);"
        tick=(f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgb({ACC})"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>') if on else (f'<span style="width:22px;height:22px;border-radius:50%;border:1.6px solid rgba(255,255,255,.18);flex-shrink:0"></span>')
        tiles+=(f'<div style="width:344px;display:flex;align-items:center;gap:16px;background:{bg};border:1.5px solid {bd};border-radius:18px;padding:18px 20px;{gl}">'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:{"#FAFAF7" if on else "#d9d5cc"}">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8f8f85;margin-top:1px">{role}</div></div>{tick}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Same build. Pick the job.","ONE OF SEVEN")}
      <div style="display:flex;flex-wrap:wrap;gap:18px;justify-content:space-between">{tiles}</div>
      {cap("one prompt swaps the job: research today, outbound tomorrow.")}</div>'''

# 8. LIVE - a speedometer arc gauge reading 20 min to LIVE, with the human gate lock beside it.
def live():
    cx,cy,R=250,300,180
    a0,a1=180,360  # semicircle left->right
    # needle near the end (~92%)
    na=a0+(a1-a0)*0.92; nx=cx+(R-30)*math.cos(math.radians(na)); ny=cy+(R-30)*math.sin(math.radians(na))
    ticks=""
    for i in range(0,7):
        a=a0+(a1-a0)*i/6; x1=cx+(R-4)*math.cos(math.radians(a)); y1=cy+(R-4)*math.sin(math.radians(a))
        x2=cx+(R-22)*math.cos(math.radians(a)); y2=cy+(R-22)*math.sin(math.radians(a))
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px;display:flex;align-items:center;gap:24px">
      <svg width="500" height="360" viewBox="0 0 500 360">
        <defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#7a4326"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="gg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="20"/>
        <path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R*math.cos(math.radians(na)):.0f} {cy+R*math.sin(math.radians(na)):.0f}" fill="none" stroke="url(#ga)" stroke-width="20" stroke-linecap="round" filter="url(#gg)"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#FAFAF7" stroke-width="5" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="12" fill="#FAFAF7"/>
        <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#FAFAF7">20</text>
        <text x="{cx}" y="{cy-26}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".16em" fill="rgb({ACC})">MINUTES TO LIVE</text></svg>
      <div style="flex:1">
        {htitle("Live, on your reins","BUILT · GATED")}
        <div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:20px 22px">
          <div style="display:flex;align-items:center;gap:16px">
            <svg width="40" height="40" viewBox="0 0 24 24"><rect x="4" y="10.5" width="16" height="11" rx="2.4" fill="none" stroke="rgb({ACC})" stroke-width="2"/><path d="M7.5 10.5 V7 a4.5 4.5 0 0 1 9 0 v3.5" fill="none" stroke="rgb({ACC})" stroke-width="2"/></svg>
            <div><div style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#FAFAF7">Human gate</div>
              <div style="font-family:'DM Sans';font-size:15px;color:#a8a296">every external move waits for your tap</div></div></div></div>
        {cap("assembled, running, and never off the leash.")}
      </div></div>'''

PANELS={"chat":chat(),"parts":parts(),"tools":tools(),"memory":memory(),
        "loop":loop(),"nocode":nocode(),"pick":pick(),"live":live()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src11"; os.makedirs(outd,exist_ok=True)
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
