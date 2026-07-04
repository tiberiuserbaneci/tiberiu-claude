#!/usr/bin/env python3
# TIER 3 - THE JOB PICKS THE AGENT (adaptation of the "hype vs value, best tool per job" IG carousel).
# Reframed to Ultron's ROUTER: you never pick the tool/model, the job routes to the agent that owns it.
# Each panel is a UNIQUE hand-built coded scene filling a clean rounded card, title + one caption.
# Built to the WIRE-ITS-EYES bar (eyes_t3.py / aibody_t3.py). Warm palette only, no stat-chip template.
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

# 1. MATRIX - radial hub-and-spokes: ROUTER centre, 7 job->agent pills around it (the reference map)
def matrix():
    jobs=[("CODE","SENTINEL"),("RESEARCH","CORTEX"),("WRITING","PULSE"),("OUTBOUND","SPECTER"),
          ("DEALS","STRIKER"),("PUBLISH","AMPLIFY"),("LEGAL","COUNSEL")]
    cx,cy,R=410,250,196; n=len(jobs)
    spokes=""; pills=""
    for i,(job,agent) in enumerate(jobs):
        a=-90+i*(360/n); x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2.5"/>'
                 f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="rgb({ACC})" filter="url(#nd)"/>')
        pills+=(f'<div style="position:absolute;left:{x-73:.0f}px;top:{y-33:.0f}px;width:146px;'
                f'background:linear-gradient(160deg,#3a352f,#221f1b);border:1.5px solid rgba(212,162,127,.30);border-radius:15px;'
                f'padding:9px 12px;box-shadow:0 16px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07)">'
                f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:#8f8f85">{job}</div>'
                f'<div style="font-family:DM Sans;font-weight:900;font-size:20px;color:#FAFAF7;line-height:1.05">{agent}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven jobs, seven agents","ROUTER MAP")}
      <div style="position:relative;height:500px">
        <svg width="820" height="500" viewBox="0 0 820 500" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
          <filter id="nd" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
          {spokes}
          <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#hub)"/></g>
          <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">ROUTER</text>
          <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        {pills}
      </div>
      {cap("one prompt in, the router reads the work and hands it to the agent that owns it.")}</div>'''

# 2. SENTINEL - horizontal ship timeline: request -> build -> test -> merged PR (coding job)
def sentinel():
    files=["dashboard.tsx","api/route.ts","schema.sql"]
    fchips="".join(f'<div style="background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:11px;padding:8px 14px;font-family:DM Mono;font-size:13px;color:#c9c3b8">{f}</div>' for f in files)
    stations=[("REQUEST","plain English",120),("BUILD","wrote the code",320),("TEST","42 passed, 0 failed",520)]
    st=""
    for nm,sub,x in stations:
        st+=(f'<circle cx="{x}" cy="150" r="17" fill="#2a2724" stroke="rgb({ACC})" stroke-width="3"/>'
             f'<circle cx="{x}" cy="150" r="6" fill="rgb({ACC})"/>'
             f'<text x="{x}" y="112" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".12em" fill="rgb({ACC})">{nm}</text>'
             f'<text x="{x}" y="200" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#d9d5cc">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Coding ships as a PR","CODE -&gt; SENTINEL")}
      <div style="display:flex;gap:14px;margin-bottom:14px">{fchips}</div>
      <svg width="820" height="260" viewBox="0 0 820 260" style="display:block">
        <defs><radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <line x1="120" y1="150" x2="700" y2="150" stroke="rgba(212,162,127,.35)" stroke-width="3"/>
        {st}
        <g filter="url(#mg)"><circle cx="700" cy="150" r="58" fill="url(#seal)"/></g>
        <path d="M676 150 l16 16 l30 -36" fill="none" stroke="#1a0f0a" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="700" y="238" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#FAFAF7">SHIP</text>
        <text x="700" y="90" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">PR #182 merged</text>
      </svg>
      {cap("describe the fix, it builds and tests before you ever open the code.")}</div>'''

# 3. CORTEX - isometric stack of ranked research cards (one brief, not ten tabs)
def cortex():
    rows=[("Northwind Robotics","raised $4M, hiring 3 ops","94"),
          ("Globex Systems","new AI budget line, Q2","88"),
          ("Initech","no AI layer yet, 40 staff","81")]
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
      {htitle("Research comes back ranked","RESEARCH -&gt; CORTEX")}
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:460px;position:relative">{cards}</div></div>
      {cap("people, companies and markets scored into one page, best fit on top.")}</div>'''

# 4. PULSE - IVORY draft document written in your voice, with a corner voice-match badge
def pulse():
    r=34; circ=2*math.pi*r; dash=circ*0.98
    lines="".join(f'<div style="height:11px;border-radius:6px;background:rgba(120,95,60,.16);width:{w}%;margin-bottom:13px"></div>' for w in (96,88,72))
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It drafts in your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">WRITING -&gt; PULSE</span></div>
      <div style="position:relative;background:rgba(255,255,255,.62);border:1px solid rgba(120,95,60,.18);border-radius:20px;padding:30px 34px;box-shadow:0 20px 40px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.9)">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px">
          <div style="width:40px;height:40px;border-radius:50%;background:linear-gradient(160deg,#d9a37c,#96562d)"></div>
          <div><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">Your LinkedIn post</div>
          <div style="font-family:DM Mono;font-size:12px;color:#96562d">draft 1 &middot; ready to approve</div></div></div>
        <div style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016;line-height:1.32;border-left:4px solid #96562d;padding-left:18px;padding-right:132px;margin-bottom:22px">
          "I killed nine tools last month. The one I kept did not have a chat box."</div>
        {lines}
        <div style="position:absolute;top:26px;right:28px;width:96px;height:96px">
          <svg width="96" height="96" viewBox="0 0 96 96">
            <circle cx="48" cy="48" r="{r}" fill="rgba(150,90,45,.16)" stroke="rgba(150,90,45,.18)" stroke-width="9"/>
            <circle cx="48" cy="48" r="{r}" fill="none" stroke="#96562d" stroke-width="9" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 48 48)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016">98%</span>
            <span style="font-family:DM Mono;font-size:9px;letter-spacing:.1em;color:#96562d">VOICE</span></div></div>
      </div>
      {cap("sampled from your real posts, banned words enforced on every draft.","#8a745a")}</div>'''

# 5. SPECTER - bezier fan: one persona -> a timed multi-step sequence -> reply
def specter():
    W,H=820,470
    steps=[("Cold email","day 0",95),("Follow-up","day 3",210),("Value nudge","day 7",325),("Break-up","day 12",440)]
    px,py=150,235; rx=560
    edges=""; cards=""
    for nm,day,y in steps:
        mx=(px+rx)/2
        edges+=f'<path d="M210 {py} C{mx:.0f} {py},{mx:.0f} {y},{rx-8} {y}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
        cards+=(f'<div style="position:absolute;left:378px;top:{y-30}px;width:250px;'
                f'background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:14px;padding:12px 16px;'
                f'box-shadow:0 16px 26px rgba(0,0,0,.5);display:flex;align-items:center;justify-content:space-between">'
                f'<span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#eae4d8">{nm}</span>'
                f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">{day}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Outbound runs as a sequence","OUTBOUND -&gt; SPECTER")}
      <div style="position:relative;height:{H}px">
        <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="pn" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="pg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <g filter="url(#pg)"><circle cx="{px}" cy="{py}" r="64" fill="url(#pn)"/></g>
          <text x="{px}" y="{py-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">1 ICP</text>
          <text x="{px}" y="{py+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">founder, US</text>
        </svg>
        {cards}
      </div>
      {cap("one persona in, a personalized multi-step sequence out, timed for you.")}</div>'''

# 6. STRIKER - funnel: deal stages narrowing to won (deals job)
def striker():
    stages=[("QUALIFY","28 leads",100,760),("DISCOVERY","19 in play",180,600),("OBJECTIONS","11 alive",260,450),
            ("PROPOSAL","6 sent",340,310)]
    bars=""
    for nm,val,y,w in stages:
        x=(760-w)/2+30
        bars+=(f'<rect x="{x:.0f}" y="{y}" width="{w}" height="58" rx="10" fill="url(#fn)" stroke="rgba(255,255,255,.10)"/>'
               f'<text x="{x+22:.0f}" y="{y+37}" font-family="DM Mono" font-size="15" letter-spacing=".1em" fill="#e2dccf">{nm}</text>'
               f'<text x="{x+w-22:.0f}" y="{y+37}" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{val}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Deals move to a close plan","DEALS -&gt; STRIKER")}
      <svg width="820" height="480" viewBox="0 0 820 480" style="display:block">
        <defs><linearGradient id="fn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#211e1a"/></linearGradient>
        <radialGradient id="won" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="wg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {bars}
        <g filter="url(#wg)"><rect x="300" y="418" width="220" height="58" rx="12" fill="url(#won)"/></g>
        <text x="352" y="455" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">WON</text>
        <text x="498" y="455" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">3</text>
      </svg>
      {cap("qualifies, handles objections, drafts the proposal, plans the close.")}</div>'''

# 7. AMPLIFY - weekly schedule grid across channels and local times (publishing job)
def amplify():
    days=["MON","TUE","WED","THU","FRI"]; chans=["LINKEDIN","TIKTOK","INSTAGRAM"]
    lit={(0,0),(0,2),(0,4),(1,1),(1,3),(2,0),(2,2),(2,4)}
    cell=118; ch=64; x0=140; y0=52; gap=12
    head="".join(f'<text x="{x0+j*(cell+gap)+cell/2:.0f}" y="36" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#8f8f85">{d}</text>' for j,d in enumerate(days))
    rows=""
    for i,c in enumerate(chans):
        y=y0+i*(ch+gap)
        rows+=f'<text x="0" y="{y+ch/2+5:.0f}" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="rgb({ACC})">{c}</text>'
        for j in range(len(days)):
            x=x0+j*(cell+gap)
            if (i,j) in lit:
                rows+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{ch}" rx="12" fill="url(#hot)" filter="url(#hg2)"/>'
                       f'<text x="{x+cell/2:.0f}" y="{y+ch/2+5:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#1a0f0a">10:30</text>')
            else:
                rows+=f'<rect x="{x}" y="{y}" width="{cell}" height="{ch}" rx="12" fill="rgba(250,250,247,.045)" stroke="rgba(255,255,255,.07)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One asset, every channel, on time","PUBLISH -&gt; AMPLIFY")}
      <svg width="820" height="290" viewBox="0 0 820 290" style="display:block;margin:6px auto 0">
        <defs><linearGradient id="hot" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="hg2" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {head}{rows}
      </svg>
      {cap("each asset reformatted per channel and fired at its best local hour.")}</div>'''

# 8. COUNSEL - IVORY wax seal + clause receipt chips, one risk flagged in muted red (legal job)
def counsel():
    docs=[("Mutual NDA","clean, standard terms",False),
          ("MSA v3","liability cap missing",True),
          ("Term sheet","2x pref, flagged",True)]
    chips=""
    for nm,note,risk in docs:
        col="#c84623" if risk else "#4a7a4a" if False else "#8a745a"
        icon=(f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M12 3 L21 7 V12 C21 17 17 20 12 21 C7 20 3 17 3 12 V7 Z" fill="none" stroke="#c84623" stroke-width="2"/><line x1="12" y1="9" x2="12" y2="14" stroke="#c84623" stroke-width="2.4" stroke-linecap="round"/><circle cx="12" cy="17" r="1.3" fill="#c84623"/></svg>' if risk else
              f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="10" fill="none" stroke="#96562d" stroke-width="2"/><path d="M7 12.5 l3 3 l7 -7.5" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
        chips+=(f'<div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.6);border:1px solid rgba(120,95,60,.18);'
                f'border-left:4px solid {"#c84623" if risk else "#96562d"};border-radius:14px;padding:14px 18px;box-shadow:0 12px 22px rgba(120,95,60,.12)">'
                f'{icon}<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">{nm}</div>'
                f'<div style="font-family:DM Sans;font-size:15px;color:{col};margin-top:1px">{note}</div></div>'
                f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:{"#c84623" if risk else "#96562d"}">{"RISK" if risk else "OK"}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;align-items:center;gap:32px">
      <div style="flex-shrink:0">
        <svg width="250" height="250" viewBox="0 0 250 250">
          <defs><radialGradient id="wax" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
          <radialGradient id="wb" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.4)"/><stop offset="62%" stop-color="rgba(204,120,92,.08)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
          <filter id="ws" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="rgba(120,90,55,.4)"/></filter>
          <filter id="wsp" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="7"/></filter></defs>
          <circle cx="125" cy="125" r="120" fill="url(#wb)"/>
          <g filter="url(#ws)">
            {"".join(f'<line x1="125" y1="125" x2="{125+108*math.cos(math.radians(a)):.0f}" y2="{125+108*math.sin(math.radians(a)):.0f}" stroke="#8a4c2c" stroke-width="9"/>' for a in range(0,360,15))}
            <circle cx="125" cy="125" r="100" fill="url(#wax)"/></g>
          <circle cx="125" cy="125" r="100" fill="none" stroke="rgba(255,255,255,.16)" stroke-width="2"/>
          <circle cx="125" cy="125" r="80" fill="none" stroke="rgba(26,15,10,.24)" stroke-width="2"/>
          <path d="M92 128 l22 22 l44 -52" fill="none" stroke="#1a0f0a" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
          <ellipse cx="96" cy="86" rx="38" ry="20" fill="rgba(255,255,255,.28)" filter="url(#wsp)" transform="rotate(-32 96 86)"/>
          <text x="125" y="185" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="17" letter-spacing="4" fill="#1a0f0a">REVIEWED</text>
        </svg></div>
      <div style="flex:1">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
          <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It reads the fine print</span>
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">LEGAL -&gt; COUNSEL</span></div>
        <div style="display:flex;flex-direction:column;gap:12px">{chips}</div>
        {cap("drafts and reviews NDAs, MSAs and term sheets, marks the danger.","#8a745a")}
      </div></div>'''

PANELS={"matrix":matrix(),"sentinel":sentinel(),"cortex":cortex(),"pulse":pulse(),
        "specter":specter(),"striker":striker(),"amplify":amplify(),"counsel":counsel()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src22"; os.makedirs(outd,exist_ok=True)
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
