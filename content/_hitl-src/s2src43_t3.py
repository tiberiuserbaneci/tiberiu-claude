#!/usr/bin/env python3
# TIER 3 - FROM PROMPT TO PRODUCT (s2src43). Reframe of the "vibe design cheatsheet" carousel
# (Claude Code + a design tool -> shipped app) into the Ultron build-to-ship recipe. Each panel a
# UNIQUE hand-built coded scene on a clean rounded card, title + one-line caption, NO stat-chip
# strips, NO cuts/walls. Warm palette, cents pricing. Mix 1-2 ivory. Overwrites models_clay/s2src43.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None):
    tagc=tagc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. BRIEF - IVORY composer: one plain-english sentence typed into the chat, with a send button
def brief():
    chips="".join(f'<span style="font-family:\'DM Mono\';font-size:14px;color:#8a745a;background:rgba(150,90,45,.09);border:1px solid rgba(150,90,45,.20);border-radius:999px;padding:8px 16px">{c}</span>' for c in ["landing page","20 cold emails","pricing page"])
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("You just say what you want","PLAIN ENGLISH",ink="#2a2016",tagc="#96562d")}
      <div style="display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.72);border:1px solid rgba(150,90,45,.20);border-radius:22px;padding:26px 26px;box-shadow:inset 0 2px 4px rgba(255,255,255,.9),0 12px 26px rgba(120,95,60,.12)">
        <div style="flex:1;font-family:'DM Sans';font-weight:500;font-size:29px;color:#2a2016;line-height:1.25">Build me a landing page and 20 cold emails for founders<span style="display:inline-block;width:4px;height:30px;background:#96562d;margin-left:5px;vertical-align:-6px"></span></div>
        <div style="flex-shrink:0;width:66px;height:66px;border-radius:50%;background:linear-gradient(160deg,#c98a5f,#96562d 60%,#7a4326);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 22px rgba(150,90,45,.4),inset 0 2px 3px rgba(255,255,255,.4)">
          <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fdfbf6" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
      </div>
      <div style="display:flex;gap:14px;margin-top:20px">{chips}</div>
      {cap("no design tool, no dev shop, no brief document. one sentence in the chat.","#8a745a")}</div>'''

# 2. ROUTER - the brief fans to 7 named agents, one lit (SENTINEL), model tier badged
def router():
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    lit=4
    hx,hcy=140,270; cx0,cw,ch=430,344,54; y0,step=42,76
    edges=""; chips=""
    for i,(nm,role) in enumerate(agents):
        cy=y0+i*step+ch/2
        on=(i==lit); col=f"rgb({ACC})" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.2
        edges+=f'<path d="M{hx+62} {hcy} C300 {hcy},310 {cy:.0f},{cx0-4} {cy:.0f}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.10)"
        fill='url(#lchip)' if on else '#221f1b'
        glow='filter="url(#cg)"' if on else ''
        nmc="#FAFAF7" if on else "#a49e92"
        tier=f'<g transform="translate({cx0+cw-118},{y0+i*step+15})"><rect x="0" y="0" width="86" height="26" rx="13" fill="rgb({ACC})"/><text x="43" y="18" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="14" fill="#1a0f0a">SMART</text></g>' if on else f'<circle cx="{cx0+cw-24}" cy="{y0+i*step+ch/2:.0f}" r="5" fill="rgba(250,250,247,.22)"/>'
        chips+=(f'<g {glow}><rect x="{cx0}" y="{y0+i*step}" width="{cw}" height="{ch}" rx="15" fill="{fill}" stroke="{bd}" stroke-width="{2 if on else 1}"/></g>'
          f'<text x="{cx0+24}" y="{y0+i*step+25}" font-family="DM Mono" font-size="17" letter-spacing=".1em" fill="{nmc}">{nm}</text>'
          f'<text x="{cx0+24}" y="{y0+i*step+44}" font-family="DM Sans" font-size="14" fill="#8f8f85">{role}</text>'
          f'{tier}')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It hires the right agent","MODEL ROUTER")}
      <svg width="820" height="612" viewBox="0 0 820 612" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <linearGradient id="lchip" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#241f1a"/></linearGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="cg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.3"/></filter></defs>
        {edges}
        <g filter="url(#hg)"><circle cx="{hx}" cy="{hcy}" r="62" fill="url(#hub)"/></g>
        <text x="{hx}" y="{hcy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
        <text x="{hx}" y="{hcy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        {chips}
      </svg>
      {cap("seven agents, one router. it picks the agent and the model tier per turn.")}</div>'''

# 3. BUILD - a real browser window shipping the actual page, LIVE badge
def build():
    feats="".join(f'<div style="flex:1;background:#26231f;border:1px solid rgba(255,255,255,.06);border-radius:10px;padding:14px 14px"><div style="width:26px;height:26px;border-radius:7px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.3)"></div><div style="height:7px;width:70%;background:rgba(250,250,247,.22);border-radius:4px;margin-top:12px"></div><div style="height:7px;width:48%;background:rgba(250,250,247,.12);border-radius:4px;margin-top:8px"></div></div>' for _ in range(3))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It ships the real page","SENTINEL")}
      <div style="background:linear-gradient(160deg,#2a2723,#201d19);border:1px solid rgba(255,255,255,.10);border-radius:18px;overflow:hidden;box-shadow:0 30px 54px rgba(0,0,0,.5)">
        <div style="display:flex;align-items:center;gap:14px;padding:15px 20px;background:#17150f;border-bottom:1px solid rgba(255,255,255,.06)">
          <span style="width:12px;height:12px;border-radius:50%;background:#4a453d"></span><span style="width:12px;height:12px;border-radius:50%;background:#4a453d"></span><span style="width:12px;height:12px;border-radius:50%;background:#4a453d"></span>
          <div style="flex:1;background:#0f0e0b;border:1px solid rgba(255,255,255,.07);border-radius:9px;padding:8px 16px;font-family:'DM Mono';font-size:15px;color:#c9c3b8;margin-left:8px">app.51ultron.com/site</div>
          <span style="display:flex;align-items:center;gap:8px;font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:#7fd39a;background:rgba(127,211,154,.10);border:1px solid rgba(127,211,154,.3);border-radius:999px;padding:6px 14px"><span style="width:9px;height:9px;border-radius:50%;background:#7fd39a;box-shadow:0 0 10px #7fd39a"></span>LIVE</span>
        </div>
        <div style="padding:34px 40px 38px">
          <div style="font-family:'DM Sans';font-weight:900;font-size:44px;color:#FAFAF7;line-height:1.05">The operator for<br><span style="color:rgb({ACC})">founders who ship.</span></div>
          <div style="font-family:'DM Sans';font-size:19px;color:#a8a296;margin-top:14px;max-width:560px">One chat runs research, outbound, deals and content. Built, tested and live on your domain.</div>
          <div style="display:inline-flex;align-items:center;gap:10px;background:rgb({ACC});color:#1a0f0a;font-family:'DM Sans';font-weight:900;font-size:17px;padding:14px 26px;border-radius:12px;margin-top:22px;box-shadow:0 12px 26px rgba(212,162,127,.35)">Start free
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
          <div style="display:flex;gap:16px;margin-top:30px">{feats}</div>
        </div>
      </div>
      {cap("it writes, tests and ships the actual page. live, not a mockup.")}</div>'''

# 4. LIBRARY - dashboard grid of shipped assets (dashboard + library)
def library():
    items=[("Landing page","Shipped",True),("Cold emails","Shipped",True),("LinkedIn post","Shipped",True),
           ("Sales deck","Draft",False),("Newsletter","Shipped",True),("Pricing page","Draft",False)]
    def glyph(): return '<div style="display:flex;flex-direction:column;gap:4px;margin-top:12px"><div style="height:8px;width:80%;background:rgba(250,250,247,.20);border-radius:4px"></div><div style="height:8px;width:55%;background:rgba(250,250,247,.10);border-radius:4px"></div></div>'
    cards=""
    for nm,st,ok in items:
        dot="#7fd39a" if ok else "#c9a583"
        cards+=(f'<div style="width:246px;background:linear-gradient(160deg,#2c2824,#211e1a);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:18px 18px;box-shadow:0 16px 30px rgba(0,0,0,.4)">'
          f'<div style="display:flex;align-items:center;justify-content:space-between">'
          f'<div style="width:34px;height:34px;border-radius:9px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.32);display:flex;align-items:center;justify-content:center"><div style="width:14px;height:14px;border:2px solid rgb({ACC});border-radius:3px"></div></div>'
          f'<span style="display:flex;align-items:center;gap:6px;font-family:\'DM Mono\';font-size:12px;color:#8f8f85"><span style="width:7px;height:7px;border-radius:50%;background:{dot}"></span>{st}</span></div>'
          f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:#FAFAF7;margin-top:14px">{nm}</div>'
          f'{glyph()}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every asset on one shelf","DASHBOARD + LIBRARY")}
      <div style="display:flex;flex-wrap:wrap;gap:16px;justify-content:center">{cards}</div>
      {cap("pages, emails, posts and decks. a dashboard and a library, one place.")}</div>'''

# 5. SPEC - your brand memory written once, applied to everything (reframe DESIGN.md)
def memory():
    rows=[("ICP","founders &middot; 2 to 50 &middot; US / UK"),("VOICE","blunt, no hedging"),
          ("PRICING","cents per run"),("PALETTE","slate + book cloth"),("BANNED","no fluff, no filler")]
    rr=""
    for k,v in rows:
        rr+=(f'<div style="display:flex;align-items:center;gap:18px;padding:15px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
          f'<span style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.12em;color:rgb({ACC});width:96px;flex-shrink:0">{k}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:20px;color:#e4ded2">{v}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;position:relative;width:230px;height:300px">
        <svg width="230" height="300" viewBox="0 0 230 300">
          <defs><radialGradient id="core" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="cg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          <rect x="34" y="26" width="162" height="248" rx="18" fill="#211e1a" stroke="rgba(255,255,255,.10)"/>
          <path d="M150 26 h46 v46 Z" fill="#2c2824" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#cg2)"><circle cx="115" cy="150" r="52" fill="url(#core)"/></g>
          <text x="115" y="146" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">brand</text>
          <text x="115" y="168" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">.spec</text>
          <text x="115" y="238" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="#8f8f85">WRITTEN ONCE</text>
        </svg></div>
      <div style="flex:1">
        {htitle("It remembers your brand","SHARED SPEC")}
        <div>{rr}</div>
        {cap("one spec feeds every asset it builds. nothing goes off brand.")}</div></div>'''

# 6. GATE - deploy console: ship switch held, queued actions paused for your tap
def gate():
    q=[("Publish landing page"),("Send 20 cold emails"),("Push pricing update")]
    rows=""
    for t in q:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:#211e1a;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:14px 18px">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round"><line x1="8" y1="6" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="18"/></svg>'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:600;font-size:19px;color:#e4ded2">{t}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:rgb({ACC});background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.3);border-radius:999px;padding:6px 14px">HELD</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing goes live without you","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:24px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(212,162,127,.3);border-radius:20px;padding:26px 30px;box-shadow:0 22px 40px rgba(0,0,0,.5)">
        <div style="flex:1">
          <div style="font-family:'DM Sans';font-weight:900;font-size:28px;color:#FAFAF7">Ship to production</div>
          <div style="font-family:'DM Mono';font-size:14px;color:#8f8f85;margin-top:4px">4 changes waiting for your tap</div></div>
        <div style="width:130px;height:64px;border-radius:999px;background:#1a1714;border:1px solid rgba(255,255,255,.10);display:flex;align-items:center;padding:0 8px;box-shadow:inset 0 2px 5px rgba(0,0,0,.5)">
          <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(160deg,#4a423a,#2a2622);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 10px rgba(0,0,0,.5)">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11 V8 a4 4 0 0 1 8 0 v3"/></svg></div></div>
      </div>
      <div style="display:flex;flex-direction:column;gap:12px;margin-top:20px">{rows}</div>
      {cap("every deploy parks at the gate. you approve, then it ships.")}</div>'''

# 7. MATH - IVORY receipt: the old stack in dollars vs Ultron in cents
def cost():
    stack=[("Design tool","$30 / mo"),("Dev / agency","$2,400"),("Copy tool","$49 / mo"),("Scheduler","$19 / mo")]
    rr=""
    for nm,pr in stack:
        rr+=(f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:12px 0;border-bottom:1px dashed rgba(150,90,45,.28)">'
          f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:21px;color:#5a4634">{nm}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:20px;color:rgba(200,70,35,.85);text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)">{pr}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The old stack, in dollars","TOOL AUDIT",ink="#2a2016",tagc="#96562d")}
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:4px">
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:#96562d">THE STACK</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:#a08a68">PER MONTH</span></div>
      <div>{rr}</div>
      <div style="display:flex;align-items:center;justify-content:space-between;background:linear-gradient(160deg,#f7efe2,#efe4d1);border:1px solid rgba(150,90,45,.28);border-radius:18px;padding:22px 26px;margin-top:22px;box-shadow:inset 0 2px 3px rgba(255,255,255,.9)">
        <div><div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#2a2016">Ultron does the lot</div>
        <div style="font-family:'DM Mono';font-size:14px;color:#8a745a;margin-top:2px">one operator, pay per token</div></div>
        <div style="text-align:right"><span style="font-family:'DM Sans';font-weight:900;font-size:46px;color:#96562d;line-height:1">cents</span>
        <div style="font-family:'DM Mono';font-size:13px;color:#8a745a">/ run</div></div></div>
      {cap("design tool, dev, copy tool, agency. ours is cents per run.","#8a745a")}</div>'''

# 8. SYSTEM - it is a running system, not a one-off prompt (recurring loop)
def system():
    cx,cy,R=300,258,168
    nodes=[("BRIEF",-90),("BUILD",0),("SHIP",90),("WATCH",180)]
    nd=""
    for nm,a in nodes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        nd+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="44" fill="#2a2723" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".08em" fill="#e4ded2">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="516" height="516" viewBox="0 0 516 516">
        <defs><radialGradient id="cc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <marker id="ah" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto"><path d="M1 1 L8 5 L1 9" fill="none" stroke="rgb({ACC})" stroke-width="2" stroke-linecap="round"/></marker>
        <filter id="cg3" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <path d="M{cx} {cy-R} A {R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" marker-end="url(#ah)" opacity="0.85"/>
        <path d="M{cx+R} {cy} A {R} {R} 0 0 1 {cx} {cy+R}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" marker-end="url(#ah)" opacity="0.85"/>
        <path d="M{cx} {cy+R} A {R} {R} 0 0 1 {cx-R} {cy}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" marker-end="url(#ah)" opacity="0.85"/>
        <path d="M{cx-R} {cy} A {R} {R} 0 0 1 {cx} {cy-R}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" marker-end="url(#ah)" opacity="0.85"/>
        {nd}
        <g filter="url(#cg3)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#cc)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">LIVE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">every day</text>
      </svg>
      <div style="flex:1">
        {htitle("A system, not a prompt","IT KEEPS RUNNING")}
        <div style="font-family:'DM Sans';font-size:20px;color:#c9c3b8;line-height:1.45">A prompt answers once and forgets. This keeps working after you close the tab: briefs in, assets out, on a loop you set.</div>
        {cap("close the tab. it is still shipping.")}</div></div>'''

PANELS={"brief":brief(),"router":router(),"build":build(),"library":library(),
        "memory":memory(),"gate":gate(),"cost":cost(),"system":system()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src43"; os.makedirs(outd,exist_ok=True)
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
