#!/usr/bin/env python3
# TIER 3 - ZERO SERVERS, ONE ANSWER. Reframe of a "40+ MCP servers your Claude needs" listicle to
# Ultron founder-GTM: you do not wire 40 servers, you ask for the outcome; Ultron ships already-wired.
# Each panel a UNIQUE hand-built coded scene on a clean rounded card, title + one-line caption,
# NO generic stat-chip strips, NO cuts/walls. Built to the WIRE-ITS-EYES bar.
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

# 1. PILE - the 40-server detour: a dense field of tool chips over a faint tangle of wiring,
# a handful flagged stale (muted red). Scene TYPE: tangled dense chip field.
def pile():
    names=["Tavily","Brave","Firecrawl","Fetch","Filesystem","SQLite","Postgres","Excel",
           "markdownify","cmux","gmux","claude-squad","dmux","mux","Superpowers","Taste",
           "Chrome CDP","Loop","Clawd","Codex","Playwright","Puppeteer","Slack","Notion",
           "Linear","GitHub","Sentry","Stripe","HubSpot","Gmail","Drive","Sheets","Airtable",
           "Redis","Mongo","S3","Zapier","Resend","Calendly","Perplexity"]
    stale={2,7,13,19,25,31,36}
    chips=""
    for i,n in enumerate(names):
        red=i in stale
        dot=('<span style="width:7px;height:7px;border-radius:50%;background:rgb(200,70,35);'
             'box-shadow:0 0 6px rgba(200,70,35,.8);flex-shrink:0"></span>') if red else ''
        op=".5" if red else ".92"
        chips+=(f'<div style="display:flex;align-items:center;gap:7px;background:linear-gradient(160deg,#302c27,#211e1a);'
                f'border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:8px 12px;opacity:{op}">'
                f'{dot}<span style="font-family:\'DM Mono\';font-size:14px;color:#c9c3b8;white-space:nowrap">{n}</span></div>')
    tangle=""
    for k in range(16):
        x1=40+(k*57)%740; y1=24+(k*83)%320; x2=40+(k*127)%740; y2=24+(k*151)%320
        tangle+=(f'<path d="M{x1} {y1} C{(x1+x2)//2} {y1-46},{(x1+x2)//2} {y2+46},{x2} {y2}" '
                 f'fill="none" stroke="rgba(212,162,127,.10)" stroke-width="1.5"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You would wire 40 servers","THE DETOUR")}
      <div style="position:relative;min-height:360px">
        <svg width="820" height="360" viewBox="0 0 820 360" style="position:absolute;left:0;top:0;pointer-events:none">{tangle}</svg>
        <div style="position:relative;display:flex;flex-wrap:wrap;gap:10px;justify-content:center;align-content:center;min-height:360px">{chips}</div>
      </div>
      {cap("search, crawl, db, files, sheets - forty moving parts, and every break is yours.")}</div>'''

# 2. ASK - IVORY construct: one plain-English question in a bar, one ranked answer below.
# Scene TYPE: single input -> ranked output form (light).
def ask():
    rows=[("Northwind Robotics","hiring 3 ops roles","92"),
          ("Globex Systems","raised $4M in May","88"),
          ("Initech","stack gap, no AI layer","81")]
    ans=""
    for a,b,c in rows:
        ans+=(f'<div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.6);'
              f'border:1px solid rgba(150,90,45,.16);border-radius:14px;padding:14px 18px">'
              f'<div style="flex-shrink:0;width:36px;height:36px;border-radius:10px;background:#96562d;color:#fff;'
              f'display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:16px">{c}</div>'
              f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#2a2016">{a}</div>'
              f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8a745a">{b}</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">You just ask</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">ONE LINE</span></div>
      <div style="display:flex;align-items:center;gap:14px;background:#fff;border:1px solid rgba(150,90,45,.2);border-radius:16px;padding:18px 20px;box-shadow:0 10px 24px rgba(120,95,60,.12)">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.4"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.3-4.3"/></svg>
        <span style="font-family:'DM Sans';font-size:21px;color:#2a2016">Who should I email this week?</span>
        <div style="margin-left:auto;flex-shrink:0;width:40px;height:40px;border-radius:12px;background:#96562d;display:flex;align-items:center;justify-content:center"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
      </div>
      <div style="display:flex;justify-content:center;margin:12px 0"><svg width="24" height="30" viewBox="0 0 24 30" fill="none" stroke="#c8a07a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v22M5 18l7 7 7-7"/></svg></div>
      <div style="display:flex;flex-direction:column;gap:10px">{ans}</div>
      {cap("one line of plain english. no servers, no keys, no yaml to maintain.","#8a745a")}</div>'''

# 3. WEB - bezier convergence: 4 web sources flow into one ranked BRIEF (replaces the 4 web MCPs).
# Scene TYPE: many-to-one bezier flow.
def web():
    W,H=820,420
    src=[("competitor.com",64),("pricing page",176),("hiring board",288),("news + intent",392)]
    hubx,huby=650,228
    edges="";nodes=""
    for nm,y in src:
        mx=(196+hubx)/2
        edges+=f'<path d="M196 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-74} {huby}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=(f'<rect x="40" y="{y-26}" width="156" height="52" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
                f'<text x="118" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14.5" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The web, already read","SEARCH + CRAWL")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hubw" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ghw" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#ghw)"><circle cx="{hubx}" cy="{huby}" r="78" fill="url(#hubw)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#1a0f0a">BRIEF</text>
        <text x="{hubx}" y="{huby+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2416">ranked, sourced</text>
      </svg>
      {cap("tavily, brave, firecrawl, fetch - four servers, or one agent that already reads.")}</div>'''

# 4. DATA - vertical staged pipeline: plain ask -> written query -> answer + cents cost.
# Scene TYPE: vertical stepped pipeline with a cost chip.
def data():
    def card(inner): return (f'<div style="width:600px;background:linear-gradient(160deg,#332f2a,#221f1b);'
        f'border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:18px 22px;box-shadow:0 16px 30px rgba(0,0,0,.45)">{inner}</div>')
    conn=f'<svg width="20" height="34" viewBox="0 0 20 34" style="margin:5px 0"><path d="M10 2 v20" stroke="rgba(212,162,127,.6)" stroke-width="2.5"/><path d="M3 18l7 8 7-8" fill="none" stroke="rgb({ACC})" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    askc=card(f'<div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">YOU ASK</div><div style="font-family:\'DM Sans\';font-weight:700;font-size:22px;color:#FAFAF7;margin-top:4px">Which accounts fit our ICP?</div>')
    queryc=card(f'<div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#9a9488">ULTRON WRITES</div><div style="font-family:\'DM Mono\';font-size:17px;color:#c9a583;margin-top:6px;line-height:1.4">select * from accounts<br>where fit_score &gt; 80</div>')
    ansc=(f'<div style="width:600px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:16px;padding:20px 24px;box-shadow:0 22px 40px rgba(0,0,0,.5),0 0 30px rgba(212,162,127,.18);display:flex;align-items:center;justify-content:space-between">'
        f'<div><div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">ANSWER</div><div style="font-family:\'DM Sans\';font-weight:900;font-size:38px;color:#FAFAF7;line-height:1">847 accounts</div></div>'
        f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:10px 18px;border-radius:12px"><span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:#1a0f0a;line-height:1">0.004c</span><span style="font-family:\'DM Mono\';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">PER RUN</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Your data, in plain English","QUERY, NOT SQL")}
      <div style="display:flex;flex-direction:column;align-items:center">{askc}{conn}{queryc}{conn}{ansc}</div>
      {cap("postgres, sqlite, excel - it writes the query, you read the answer, for cents.")}</div>'''

# 5. MEMORY - concentric memory-core shells feeding the seven agents. Scene TYPE: concentric shells + tag list.
def memory():
    cx,cy=225,225
    shells=[("DOCS",196),("PRICING",152),("PIPELINE",108),("ICP",64)]
    rings=""
    for nm,r in shells:
        rings+=(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.30)" stroke-width="1.8"/>'
                f'<text x="{cx}" y="{cy-r+21}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".12em" fill="#c9a583">{nm}</text>')
    agents=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    tags="".join(f'<span style="font-family:\'DM Mono\';font-size:14px;color:#d9d5cc;background:#221f1b;border:1px solid rgba(255,255,255,.09);border-radius:8px;padding:6px 11px">{a}</span>' for a in agents)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="450" height="450" viewBox="0 0 450 450" style="flex-shrink:0">
        <defs><radialGradient id="mc" cx="45%" cy="40%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {rings}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="34" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="14" fill="#2a160c">CORE</text>
      </svg>
      <div style="flex:1">
        {htitle("One memory, every agent","SHARED CORE")}
        <div style="font-family:'DM Sans';font-size:19px;color:#c9c3b8;line-height:1.45;margin-bottom:16px">ICP, pipeline, pricing and docs live once. All seven agents read the same core, so nothing forgets you.</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px">{tags}</div>
        {cap("remembered once, used by all seven - no re-briefing, ever.")}
      </div></div>'''

# 6. ROSTER - radial hub-and-spokes: ROUTER brain + 7 named agents. Scene TYPE: radial hub-spokes.
def roster():
    cx,cy,R=410,235,170
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    n=len(agents); spokes="";nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/n)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#241f1a" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
                f'<text x="{x:.0f}" y="{y-1:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="#FAFAF7">{nm}</text>'
                f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#9a9488">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, already wired","THE ROSTER")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="rh" cx="38%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#rh)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one brain</text>
        {nodes}
      </svg>
      {cap("you install nothing - the roster ships wired to one brain and one memory.")}</div>'''

# 7. CENTS - IVORY: the competitor's stacked monthly bill (tall, muted red) vs Ultron's cents coin.
# Scene TYPE: comparison stack vs coin.
def cents():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Forty subscriptions, or cents</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">THE BILL</span></div>
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:90px;height:340px">
        <div style="display:flex;flex-direction:column;align-items:center">
          <div style="font-family:'DM Sans';font-weight:900;font-size:32px;color:rgb(200,70,35);line-height:1">$1,200</div>
          <div style="font-family:'DM Mono';font-size:13px;color:#a0604a;margin-bottom:10px">/ month, always on</div>
          <div style="width:158px;height:238px;border-radius:16px 16px 0 0;background:repeating-linear-gradient(180deg,rgb(200,70,35) 0px,rgb(200,70,35) 9px,rgba(150,50,25,.9) 9px,rgba(150,50,25,.9) 11px);box-shadow:0 18px 34px rgba(200,70,35,.28),inset 0 2px 3px rgba(255,255,255,.25)"></div>
          <div style="font-family:'DM Sans';font-weight:700;font-size:16px;color:#5a4634;margin-top:12px">40 servers you maintain</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;padding-bottom:6px">
          <div style="font-family:'DM Sans';font-weight:900;font-size:32px;color:#96562d;line-height:1">cents</div>
          <div style="font-family:'DM Mono';font-size:13px;color:#a08a68;margin-bottom:14px">/ job, only when used</div>
          <div style="width:120px;height:120px;border-radius:50%;background:radial-gradient(circle at 38% 32%,#f0c49e,rgb({ACC}) 55%,#8a4a2c);box-shadow:0 16px 30px rgba(150,90,45,.3),inset 0 3px 4px rgba(255,255,255,.55);display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:52px;color:#3a2010">&#162;</div>
          <div style="font-family:'DM Sans';font-weight:700;font-size:16px;color:#5a4634;margin-top:12px">one bill, per token</div>
        </div>
      </div>
      {cap("the stack bills monthly whether you use it or not. ultron bills the job.","#8a745a")}</div>'''

# 8. GATE - HUMAN GATE: a queue of pending outbound actions holding for the operator tap.
# Scene TYPE: approval queue list + tap bar.
def gate():
    items=[("SPECTER","send 12 follow-ups"),("PULSE","publish today's post"),("STRIKER","book the Globex call")]
    rows=""
    for ag,act in items:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:16px 20px;box-shadow:0 14px 26px rgba(0,0,0,.45)">'
               f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:\'DM Mono\';font-size:12px;letter-spacing:.06em;color:rgb({ACC})">{ag[:3]}</div>'
               f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Sans\';font-weight:700;font-size:20px;color:#FAFAF7">{act}</div>'
               f'<div style="font-family:\'DM Mono\';font-size:13px;color:#9a9488;margin-top:1px">{ag}</div></div>'
               f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:12px;letter-spacing:.12em;color:rgb({ACC});background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.32);border-radius:999px;padding:6px 14px">HOLD</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing sends without you","HUMAN GATE")}
      <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:22px">{rows}</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:16px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:18px;padding:20px;box-shadow:0 0 30px rgba(212,162,127,.2)">
        <svg width="30" height="30" viewBox="0 0 24 24"><rect x="4" y="11" width="16" height="10" rx="3" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/><path d="M8 11 V8 a4 4 0 0 1 8 0 v3" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/></svg>
        <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#FAFAF7">Waiting for your tap</span>
      </div>
      {cap("every external move parks in one queue and holds until you approve it.")}</div>'''

PANELS={"pile":pile(),"ask":ask(),"web":web(),"data":data(),
        "memory":memory(),"roster":roster(),"cents":cents(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src32"; os.makedirs(outd,exist_ok=True)
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
