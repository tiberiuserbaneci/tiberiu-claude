#!/usr/bin/env python3
# TIER 3 - THE 60-SECOND BRIEF (CORTEX account research). Reframe of a GEO "paste-a-URL, 5 agents in
# parallel, full report in 60s" carousel into Ultron founder research: one command fans out research
# agents and returns a ranked, sourced brief for cents. Each panel is a UNIQUE hand-built coded scene
# filling a clean rounded card, title + one-line caption, NO generic stat-chip strips. Cost zero.
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

# 1. MANUAL - THE OLD WAY: isometric tilted stack of open browser tabs (one prospect, twelve tabs),
# a red competitor-cost tag ($10K/mo agency = what Ultron replaces) and a per-account clock.
def manual():
    tabs=[("crunchbase.com","funding history"),
          ("linkedin.com","team + hiring"),
          ("techcrunch.com","recent news"),
          ("g2.com","stack + reviews"),
          ("careers page","open roles")]
    cards=""
    for i,(a,b) in enumerate(tabs):
        y=i*92
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:540px;
          background:linear-gradient(160deg,#343029,#241f1a);border:1.5px solid rgba(255,255,255,.12);border-radius:14px;
          padding:15px 22px;box-shadow:0 26px 40px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.08);
          display:flex;align-items:center;gap:16px">
          <div style="display:flex;gap:6px;flex-shrink:0">
            <span style="width:11px;height:11px;border-radius:50%;background:#c84623"></span>
            <span style="width:11px;height:11px;border-radius:50%;background:rgba(212,162,127,.5)"></span>
            <span style="width:11px;height:11px;border-radius:50%;background:rgba(255,255,255,.18)"></span></div>
          <div style="flex:1;text-align:left"><div style="font-family:'DM Mono';font-size:16px;color:#eae4d8">{a}</div>
          <div style="font-family:'DM Sans';font-size:14px;color:#8f8f85">{b}</div></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("You research one account by hand","THE OLD WAY")}
      <div style="perspective:2000px;height:466px;position:relative;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(24deg) rotateZ(-10deg);width:540px;height:460px;position:relative">{cards}</div>
        <div style="position:absolute;right:4px;top:6px;background:rgba(200,70,35,.14);border:1px solid rgba(200,70,35,.5);border-radius:14px;padding:12px 18px;text-align:right">
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#e8896b;line-height:1">$10K<span style="font-size:16px">/mo</span></div>
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:#c9968a">RESEARCH AGENCY</div></div>
        <div style="position:absolute;left:6px;bottom:8px;background:#211d19;border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:10px 16px">
          <div style="font-family:'DM Mono';font-size:14px;color:rgb({ACC})">2h 15m &middot; per account</div></div>
      </div>
      {cap("twelve tabs, two hours, one prospect. multiply that by your whole list.")}</div>'''

# 2. PASTE - IVORY command bar: one slash command, a real URL, a send button. No form, no intake.
def paste():
    return f'''<div style="width:900px;{CARDIV};padding:40px 44px 40px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:28px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">You just paste a URL</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">ONE COMMAND</span></div>
      <div style="background:#fffdf9;border:1px solid rgba(120,95,60,.18);border-radius:22px;
        box-shadow:0 30px 50px rgba(120,95,60,.18), inset 0 2px 3px rgba(255,255,255,.9);padding:36px 34px 28px;margin-bottom:8px">
        <div style="font-family:'DM Mono';font-size:33px;color:#2a2016;text-align:left;line-height:1.1">
          <span style="color:#96562d;font-weight:500">/cortex</span> northwind-robotics.com<span style="display:inline-block;width:3px;height:32px;background:#96562d;margin-left:5px;vertical-align:-5px"></span></div>
        <div style="display:flex;align-items:center;justify-content:space-between;margin-top:36px">
          <div style="font-family:'DM Mono';font-size:16px;color:#96562d;letter-spacing:.04em">CORTEX &middot; 5 agents queued &middot; ~60s</div>
          <div style="width:62px;height:62px;border-radius:50%;background:linear-gradient(160deg,#c98a63,#96562d);display:flex;align-items:center;justify-content:center;box-shadow:0 12px 24px rgba(150,90,45,.42), inset 0 2px 3px rgba(255,255,255,.4)">
            <svg width="27" height="27" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg></div>
        </div>
      </div>
      {cap("no form, no research VA, no agency intake call. one line, hit send.","#8a745a")}</div>'''

# 3. FANOUT - one command splits into 5 research agents fanning out in parallel (radial spokes).
def fanout():
    hx,hy=150,232
    agents=[("profiles company",-58),("maps the buyers",-29),("reads the news",0),("scores the fit",29),("finds triggers",58)]
    spokes=""; nodes=""
    for nm,a in agents:
        x=hx+430*math.cos(math.radians(a)); y=hy+205*math.sin(math.radians(a))
        spokes+=f'<path d="M{hx+62} {hy} Q{(hx+x)/2:.0f} {hy},{x-98:.0f} {y:.0f}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<rect x="{x-98:.0f}" y="{y-27:.0f}" width="212" height="54" rx="15" fill="url(#chip)" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="{x-72:.0f}" cy="{y:.0f}" r="6" fill="rgb({ACC})" filter="url(#nd)"/>'
          f'<text x="{x-54:.0f}" y="{y+5:.0f}" font-family="DM Mono" font-size="15.5" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One command, five agents","RUNS IN PARALLEL")}
      <svg width="820" height="460" viewBox="0 0 820 460" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="chip" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
          <filter id="nd" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {spokes}
        <g filter="url(#hg)"><circle cx="{hx}" cy="{hy}" r="62" fill="url(#hub)"/></g>
        <text x="{hx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">CORTEX</text>
        <text x="{hx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">splits the job</text>
        {nodes}
        <rect x="352" y="18" width="118" height="34" rx="17" fill="rgba(212,162,127,.14)" stroke="rgba(212,162,127,.4)"/>
        <text x="411" y="40" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="rgb({ACC})">&#215;5 AT ONCE</text>
      </svg>
      {cap("the router splits the job and runs all five at once, not one after another.")}</div>'''

# 4. SOURCES - bezier convergence: 5 web sources pulled and reconciled into one brief page.
def sources():
    src=[("Crunchbase","funding"),("LinkedIn","hiring"),("TechCrunch","news"),("careers","open roles"),("G2","reviews")]
    ys=[60,145,230,315,400]
    hubx,huby=660,230
    edges=""; nodes=""
    for (nm,sub),y in zip(src,ys):
        mx=(196+hubx)/2
        edges+=f'<path d="M196 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-72} {huby}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=(f'<rect x="36" y="{y-30}" width="160" height="60" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="116" y="{y-4}" text-anchor="middle" font-family="DM Mono" font-size="16" fill="#e2dccf">{nm}</text>'
          f'<text x="116" y="{y+18}" text-anchor="middle" font-family="DM Sans" font-size="13" fill="#8f8f85">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The whole web, read for you","CROSS-CHECKED")}
      <svg width="820" height="460" viewBox="0 0 820 460" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub2" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="76" fill="url(#hub2)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="23" fill="#1a0f0a">BRIEF</text>
        <text x="{hubx}" y="{huby+22}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2416">1 page</text>
      </svg>
      {cap("funding, hiring, stack, reviews, intent - pulled and reconciled into one page.")}</div>'''

# 5. BRIEF - isometric stack of ranked account cards, each with a fit score and the one reason.
def brief():
    rows=[("Northwind Robotics","hiring 3 ops roles","94"),
          ("Globex Systems","raised $4M in May","89"),
          ("Initech","no AI layer yet","82")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:25px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 17px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{c}</span>
            <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">FIT</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:38px 44px 44px">
      {htitle("A ranked brief, not a link dump","RANKED BY FIT")}
      <div style="perspective:2000px;height:600px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:490px;position:relative">{cards}</div></div>
      {cap("top accounts first, each with the one reason they are ready to buy now.")}</div>'''

# 6. RECEIPTS - dimensional VERIFIED wax-seal + a packed stack of source-receipt chips, the blind
# guess subordinated to a small crossed-out ghost strip. Every claim is sourced and dated.
def receipts():
    recs=[("techcrunch.com","2026-05-14","funding round"),
          ("sec.gov","2026-05-20","S-1 filing"),
          ("linkedin.com","2026-05-22","3 ops hires")]
    chips=""
    for dom,date,note in recs:
        fav=dom[0].upper()
        chips+=f'''<div style="display:flex;align-items:center;gap:16px;
          background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);
          border-radius:16px;padding:14px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">
          <div style="flex-shrink:0;width:40px;height:40px;border-radius:11px;background:linear-gradient(160deg,#4a423a,#2a2622);
            display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:20px;color:rgb({ACC});border:1px solid rgba(255,255,255,.10)">{fav}</div>
          <div style="flex:1;text-align:left">
            <div style="font-family:'DM Mono';font-weight:500;font-size:17px;color:#eae4d8;letter-spacing:.02em">{dom}</div>
            <div style="font-family:'DM Sans';font-size:14px;color:#8f8f85;margin-top:1px">{note} &middot; {date}</div></div>
          <svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.16)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Every line carries its source","SOURCED &middot; DATED")}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);
        border-radius:14px;padding:12px 18px;margin-bottom:22px;opacity:.72">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:#7a7468;flex-shrink:0">BLIND</span>
        <span style="font-family:'DM Sans';font-size:18px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">"they probably raised recently"</span>
        <span style="margin-left:auto;font-family:'DM Mono';font-size:12px;color:#c84623;flex-shrink:0">no source</span></div>
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex:1">
          <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#FAFAF7;line-height:1.05;margin-bottom:18px">Raised <span style="color:rgb({ACC})">$4M</span>, May 2026.</div>
          <div style="display:flex;flex-direction:column;gap:12px">{chips}</div>
        </div>
        <div style="flex-shrink:0;display:flex;align-items:center;justify-content:center">
          <svg width="290" height="290" viewBox="0 0 290 290">
            <defs>
              <radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
              <radialGradient id="sealbloom" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.5)"/><stop offset="62%" stop-color="rgba(204,120,92,.10)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
              <filter id="sealsh" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="rgba(0,0,0,.6)"/></filter>
              <filter id="spec" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="8"/></filter>
            </defs>
            <circle cx="145" cy="145" r="140" fill="url(#sealbloom)"/>
            <g filter="url(#sealsh)">
              {"".join(f'<line x1="145" y1="145" x2="{145+128*math.cos(math.radians(a)):.0f}" y2="{145+128*math.sin(math.radians(a)):.0f}" stroke="#8a4c2c" stroke-width="10"/>' for a in range(0,360,15))}
              <circle cx="145" cy="145" r="118" fill="url(#seal)"/>
            </g>
            <circle cx="145" cy="145" r="118" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
            <circle cx="145" cy="145" r="96" fill="none" stroke="rgba(26,15,10,.28)" stroke-width="2"/>
            <path d="M108 148 l24 24 l50 -58" fill="none" stroke="#1a0f0a" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
            <ellipse cx="110" cy="98" rx="44" ry="24" fill="rgba(255,255,255,.28)" filter="url(#spec)" transform="rotate(-32 110 98)"/>
            <text x="145" y="212" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="19" letter-spacing="4" fill="#1a0f0a">VERIFIED</text>
          </svg>
        </div>
      </div>
      {cap("cited and dated - your rep never quotes a hallucination.")}</div>'''

# 7. CENTS - IVORY: a tiny-arc gauge (a full brief at $0.04) beside a struck five-figure agency bar.
def cents():
    r=76; circ=2*math.pi*r; dash=circ*0.06
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">A full brief costs cents</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PAY PER TOKEN</span></div>
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0;position:relative;width:200px;height:200px">
          <svg width="200" height="200" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="16"/>
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="#96562d" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 100 100)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016">$0.04</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">per brief</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.28);border-radius:14px;padding:16px 20px;margin-bottom:14px">
            <div style="display:flex;justify-content:space-between;align-items:baseline">
              <span style="font-family:'DM Sans';font-size:17px;color:#7a5a4a">research agency</span>
              <span style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#b64a2c;text-decoration:line-through;text-decoration-color:rgba(182,74,44,.55)">$10,000<span style="font-size:15px">/mo</span></span></div>
            <div style="height:9px;border-radius:5px;background:linear-gradient(90deg,#c26a4a,#b64a2c);margin-top:12px"></div></div>
          <div style="background:rgba(150,90,45,.10);border:1px solid rgba(150,90,45,.3);border-radius:14px;padding:16px 20px">
            <div style="display:flex;justify-content:space-between;align-items:baseline">
              <span style="font-family:'DM Sans';font-size:17px;color:#5a4634">one CORTEX brief</span>
              <span style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#96562d">$0.04</span></div>
            <div style="height:9px;width:6px;border-radius:5px;background:#96562d;margin-top:12px"></div></div>
        </div>
      </div>
      {cap("cents per prospect, not a five-figure retainer. it is just tokens.","#8a745a")}</div>'''

# 8. GATE - HUMAN GATE: the finished brief orb held behind a lock; nothing hands off to SPECTER
# without the operator's tap.
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing sends without you","HUMAN GATE")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter>
        <radialGradient id="spo" cx="36%" cy="30%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1c1a17"/></radialGradient></defs>
        <g filter="url(#og)"><circle cx="168" cy="210" r="120" fill="url(#orb)"/></g>
        <text x="168" y="204" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">BRIEF</text>
        <text x="168" y="238" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">READY</text>
        <path d="M292 210 H432" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="440" y="140" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(482,178)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="510" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
        <path d="M588 210 H636" stroke="rgba(212,162,127,.4)" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <circle cx="712" cy="210" r="66" fill="#141210"/>
        <circle cx="712" cy="210" r="58" fill="url(#spo)" stroke="rgba(212,162,127,.45)" stroke-width="1.5"/>
        <text x="712" y="206" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#e6d6c2">SPECTER</text>
        <text x="712" y="228" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">writes it</text>
      </svg>
      {cap("read the brief, tap approve, then SPECTER writes the opener. your call, always.")}</div>'''

PANELS={"manual":manual(),"paste":paste(),"fanout":fanout(),"sources":sources(),
        "brief":brief(),"receipts":receipts(),"cents":cents(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src44"; os.makedirs(outd,exist_ok=True)
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
