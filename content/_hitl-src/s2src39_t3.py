#!/usr/bin/env python3
# TIER 3 - THE ASSEMBLY LINE (s2src39). Reframe of the "Claude Code + NotebookLM" pipeline cheatsheet
# into an Ultron founder-GTM production line: one plain-English ask -> router -> research -> saved
# system -> voiced draft -> shared memory -> human gate -> cents. Each panel a UNIQUE hand-built coded
# scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips. Cost zero.
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

# 1. ASK - IVORY command bar: one typed sentence + cursor, a send button, and an "expands to" strip
def ask():
    return f'''<div style="width:900px;{CARDIV};padding:44px 46px 40px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:26px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">One sentence. Not a prompt.</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PLAIN ENGLISH</span></div>
      <div style="display:flex;align-items:center;gap:18px;background:#fff;border:1.5px solid rgba(150,90,45,.2);border-radius:22px;padding:24px 22px;box-shadow:0 18px 34px rgba(120,95,60,.16), inset 0 2px 3px rgba(255,255,255,.9)">
        <div style="flex-shrink:0;width:13px;height:13px;border-radius:50%;background:#96562d;box-shadow:0 0 0 5px rgba(150,90,45,.14)"></div>
        <div style="flex:1;font-family:'DM Sans';font-weight:600;font-size:24px;color:#2a2016;line-height:1.3">Map my 20 best-fit accounts and draft the first email to each.<span style="display:inline-block;width:3px;height:26px;background:#96562d;margin-left:5px;vertical-align:-4px"></span></div>
        <div style="flex-shrink:0;width:56px;height:56px;border-radius:16px;background:linear-gradient(160deg,#e6b48f,#96562d);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 20px rgba(150,90,45,.34)">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
      </div>
      <div style="display:flex;align-items:center;gap:16px;margin-top:22px;background:rgba(150,90,45,.06);border:1px solid rgba(150,90,45,.14);border-radius:16px;padding:16px 20px">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#96562d;flex-shrink:0">EXPANDS TO</span>
        <span style="flex:1;font-family:'DM Sans';font-weight:600;font-size:18px;color:#5a4634">research &middot; rank &middot; draft &middot; gate &middot; send</span>
        <span style="font-family:'DM Mono';font-size:14px;color:#96562d;flex-shrink:0">6 steps</span></div>
      {cap("you type it once. the whole line below runs itself, no prompt engineering.","#8a745a")}</div>'''

# 2. ROUTER - a job routed from one ask to 3 named agents, first lit/running, cents per agent
def route():
    agents=[("CORTEX","maps the accounts","0.11c",96,True),
            ("SPECTER","writes the emails","0.09c",210,False),
            ("PULSE","packages the brief","0.04c",324,False)]
    hubx,hy=176,210
    edges=""; cards=""
    for nm,role,cost,y,on in agents:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+60} {hy} C330 {hy},350 {y},466 {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        tag=(f'<span style="font-family:DM Mono;font-size:11px;color:rgb({ACC})">running</span>' if on
             else '<span style="font-family:DM Mono;font-size:11px;color:#8f8f85">queued</span>')
        cards+=(f'<div style="position:absolute;left:466px;top:{y-42}px;width:332px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:16px 18px;display:flex;align-items:center;gap:16px">'
          f'<div style="flex:1"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#FAFAF7">{nm}</span>{tag}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85;margin-top:2px">{role}</div></div>'
          f'<div style="flex-shrink:0;text-align:right"><div style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">{cost}</div><div style="font-family:DM Mono;font-size:10px;color:#8f8f85">this run</div></div>'
          f'</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The router hires the crew","ONE ASK, 3 AGENTS")}
      <div style="position:relative;height:428px">
        <svg width="820" height="428" viewBox="0 0 820 428" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          <rect x="8" y="{hy-30}" width="104" height="60" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>
          <text x="60" y="{hy-2}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="14" fill="#d9d5cc">your ask</text>
          <text x="60" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">1 line</text>
          <path d="M112 {hy} H{hubx-60}" stroke="rgb({ACC})" stroke-width="3"/>
          {edges}
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="60" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">reads the job</text>
        </svg>
        {cards}
      </div>
      {cap("you never pick an agent or a model. the router does, and bills cents.")}</div>'''

# 3. RESEARCH - CORTEX: 4 web sources converge (bezier) into one ranked brief card
def research():
    src=[("competitor.com",70),("funding news",158),("job boards",246),("SEC filings",334)]
    edges=""; nodes=""
    for nm,y in src:
        edges+=f'<path d="M200 {y} C360 {y},404 202,470 202" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
        nodes+=(f'<rect x="22" y="{y-27}" width="178" height="54" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="111" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#c9c3b8">{nm}</text>')
    rows=[("1","Northwind Robotics","92"),("2","Globex Systems","88"),("3","Initech","81")]
    rowhtml="".join(f'<div style="display:flex;align-items:center;gap:14px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.07)"><span style="font-family:DM Mono;font-size:15px;color:rgb({ACC})">{n}</span><span style="flex:1;font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{a}</span><span style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">{s}</span></div>' for n,a,s in rows)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The web, ranked into a brief","CORTEX")}
      <div style="position:relative;height:410px">
        <svg width="820" height="410" viewBox="0 0 820 410" style="position:absolute;left:0;top:0">{edges}{nodes}</svg>
        <div style="position:absolute;left:466px;top:56px;width:334px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1.5px solid rgba(212,162,127,.34);border-radius:20px;padding:20px 22px;box-shadow:0 30px 50px rgba(0,0,0,.5)">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px"><span style="font-family:DM Sans;font-weight:900;font-size:19px;color:#FAFAF7">Ranked brief</span><span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">1 page</span></div>
          {rowhtml}
          <div style="font-family:DM Mono;font-size:12px;color:#8f8f85;margin-top:12px">sourced &middot; dated &middot; deduped</div>
        </div>
      </div>
      {cap("live signals in, one ranked one-pager out. no tabs, no manual reading.")}</div>'''

# 4. SYSTEM - isometric stack of numbered pipeline-step cards (a saved, reusable system, not a prompt)
def workflow():
    steps=[("01","Find best-fit accounts"),("02","Score and rank"),("03","Draft the first email"),
           ("04","Wait for your tap"),("05","Send and log the reply")]
    cards=""
    for i,(n,t) in enumerate(steps):
        y=i*92
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:16px;padding:16px 22px;box-shadow:0 26px 40px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<span style="font-family:DM Mono;font-weight:500;font-size:18px;color:rgb({ACC})">{n}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:20px;color:#FAFAF7">{t}</span>'
          f'<span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 10px rgba(212,162,127,.6)"></span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("A saved system, not a prompt","RUN IT AGAIN")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:452px;position:relative">{cards}</div></div>
      {cap("the whole pipeline is stored. next week the same ask reruns itself in one click.")}</div>'''

# 5. DRAFT - IVORY email-draft mockup with a voice-match badge + your-voice trait checklist
def draft():
    lines=["Saw Northwind is hiring three ops roles this month.",
           "Most teams bolt on a tool per role. It never sticks.",
           "Worth 15 minutes on what we did instead?"]
    body="".join(f'<div style="font-family:DM Sans;font-size:19px;color:#2a2016;line-height:1.5;margin-bottom:9px">{l}</div>' for l in lines)
    traits="".join(f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:13px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:16px;color:#5a4634">{t}</span></div>' for t in ["your short lines","no hedging words","your sign-off"])
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:22px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It drafts in your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PULSE &middot; 96% MATCH</span></div>
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1;background:#fff;border:1px solid rgba(150,90,45,.16);border-radius:18px;padding:24px 26px;box-shadow:0 20px 38px rgba(120,95,60,.16)">
          <div style="display:flex;justify-content:space-between;border-bottom:1px solid rgba(150,90,45,.14);padding-bottom:12px;margin-bottom:16px"><span style="font-family:DM Mono;font-size:13px;color:#96562d">TO: NORTHWIND &middot; OPS LEAD</span><span style="font-family:DM Mono;font-size:13px;color:#a08a68">draft 1 of 20</span></div>
          {body}
        </div>
        <div style="flex-shrink:0;width:238px;display:flex;flex-direction:column;justify-content:center;background:rgba(150,90,45,.06);border-radius:16px;padding:24px 22px">
          <div style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016;line-height:1">96%</div>
          <div style="font-family:DM Mono;font-size:12px;color:#96562d;margin-bottom:20px">sounds like you</div>
          {traits}
        </div>
      </div>
      {cap("sampled from your real posts. banned words enforced on every draft.","#8a745a")}</div>'''

# 6. MEMORY - a glowing database cylinder feeding the line, 4 labelled memory rows beside it
def memory():
    rows=[("ICP","founders &middot; 2-50 &middot; US/UK"),("PIPELINE","41 open &middot; 6 late-stage"),
          ("PRICING","cents per run"),("DOCS","product &middot; tone &middot; cases")]
    rowhtml="".join(f'<div style="display:flex;align-items:baseline;gap:14px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.07)"><span style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:rgb({ACC});width:100px;flex-shrink:0">{k}</span><span style="font-family:DM Sans;font-size:18px;color:#d9d5cc">{v}</span></div>' for k,v in rows)
    cyl=f'''<defs>
        <linearGradient id="cyl" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#7a4326"/><stop offset="46%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#6a3a20"/></linearGradient>
        <radialGradient id="disc" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
      <ellipse cx="150" cy="352" rx="98" ry="24" fill="rgba(0,0,0,.42)"/>
      <g filter="url(#cg)">
        <path d="M54 112 V300 A96 30 0 0 0 246 300 V112" fill="url(#cyl)"/>
        <ellipse cx="150" cy="200" rx="96" ry="30" fill="none" stroke="rgba(0,0,0,.18)" stroke-width="2"/>
        <ellipse cx="150" cy="252" rx="96" ry="30" fill="none" stroke="rgba(0,0,0,.18)" stroke-width="2"/>
        <ellipse cx="150" cy="112" rx="96" ry="30" fill="url(#disc)"/>
        <ellipse cx="150" cy="112" rx="96" ry="30" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="1.5"/></g>
      <ellipse cx="128" cy="102" rx="30" ry="10" fill="rgba(255,255,255,.35)"/>
      <text x="150" y="120" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="15" letter-spacing="2" fill="#2a160c">CORE</text>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <svg width="300" height="400" viewBox="0 0 300 400" style="flex-shrink:0">{cyl}</svg>
      <div style="flex:1">
        {htitle("One memory feeds it all","SHARED CORE")}
        {rowhtml}
        {cap("every stage reads the same core. it never re-asks who you sell to.")}
      </div></div>'''

# 7. GATE - the finished deliverable parked behind a lock, waiting for the operator's tap
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Finished, then it stops","HUMAN GATE")}
      <svg width="820" height="410" viewBox="0 0 820 410" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="dc" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#221e1a"/></linearGradient>
          <filter id="gg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.28"/></filter></defs>
        <rect x="72" y="120" width="292" height="178" rx="20" fill="#241f1a" opacity="0.55"/>
        <rect x="64" y="112" width="292" height="178" rx="20" fill="#2b2723" opacity="0.8"/>
        <rect x="56" y="104" width="292" height="178" rx="20" fill="url(#dc)" stroke="rgba(255,255,255,.12)"/>
        <text x="82" y="150" font-family="DM Mono" font-size="14" letter-spacing="2" fill="rgb({ACC})">READY TO SEND</text>
        <text x="82" y="192" font-family="DM Sans" font-weight="900" font-size="27" fill="#FAFAF7">20 emails &middot; 1 brief</text>
        <text x="82" y="228" font-family="DM Sans" font-size="17" fill="#8f8f85">sourced, dated, in your voice</text>
        <text x="82" y="262" font-family="DM Mono" font-size="14" fill="#c9a583">status: parked</text>
        <circle cx="330" cy="132" r="19" fill="rgb({ACC})"/>
        <path d="M321 132 l6 6 l12 -13" fill="none" stroke="#1a0f0a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M356 193 H600" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>
        <g filter="url(#gg2)"><rect x="610" y="123" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <g transform="translate(652,161)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="680" y="300" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("nothing leaves your company until you tap send. augmented, never loose.")}</div>'''

# 8. PRICE - the expensive stack it replaces (struck), against one cents figure for the whole run
def cost():
    comp=[("Clay + Apollo + Instantly","$1,240"),("An SDR agency retainer","$3,500"),("A RevOps hire","$8,000")]
    rows="".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:15px 18px;background:rgba(200,70,35,.07);border:1px solid rgba(200,70,35,.22);border-radius:14px;margin-bottom:13px"><span style="font-family:DM Sans;font-size:18px;color:#c9c3b8">{n}</span><span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#c86a4a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.75)">{p}<span style="font-family:DM Mono;font-size:12px;color:#9a9488;text-decoration:none"> /mo</span></span></div>' for n,p in comp)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The stack it replaces","PRICED IN CENTS")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1;display:flex;flex-direction:column;justify-content:center">{rows}</div>
        <div style="flex-shrink:0;width:302px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:20px;padding:30px 24px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;box-shadow:0 30px 50px rgba(0,0,0,.5), 0 0 44px rgba(212,162,127,.16)">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:rgb({ACC})">THIS WHOLE RUN</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:82px;color:#FAFAF7;line-height:1;margin:8px 0">24c</div>
          <div style="font-family:DM Sans;font-size:16px;color:#c9a583">pay per token, per run</div>
        </div>
      </div>
      {cap("20 accounts mapped, 20 emails drafted. twenty-four cents, not a retainer.")}</div>'''

PANELS={"ask":ask(),"route":route(),"research":research(),"workflow":workflow(),
        "draft":draft(),"memory":memory(),"gate":gate(),"cost":cost()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src39"; os.makedirs(outd,exist_ok=True)
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
