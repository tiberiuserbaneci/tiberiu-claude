#!/usr/bin/env python3
# TIER 3 - DAY ONE: THE FIVE PLAYS, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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

# 1. TEACH - the /init interview captured as filled form fields, terminal header + a 10:00 timer
def teach():
    fields=[("ICP","Founders, 2-50 people, IT services"),
            ("OFFER","AI operator for founders"),
            ("PRICING","Max $19/mo, then cents per run"),
            ("NO-LIST","no cold spam, no fake urgency")]
    rows=""
    for lab,val in fields:
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(158deg,#332f2a,#221e1a);'
          f'border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:16px 20px;'
          f'box-shadow:0 14px 26px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<span style="flex-shrink:0;width:96px;font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{lab}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:19px;color:#eae4d8">{val}</span>'
          f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(127,211,154,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#7fd39a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One interview, then it knows","/INIT")}
      <div style="display:flex;align-items:center;gap:12px;background:#141210;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:14px 20px;margin-bottom:18px">
        <span style="width:12px;height:12px;border-radius:50%;background:#e0564a"></span>
        <span style="width:12px;height:12px;border-radius:50%;background:#e6b24a"></span>
        <span style="width:12px;height:12px;border-radius:50%;background:#7fd39a"></span>
        <span style="flex:1;font-family:DM Mono;font-size:16px;color:#c9c3b8;margin-left:8px">&gt; claude /init</span>
        <span style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:rgb({ACC})">10:00</span></div>
      <div style="display:flex;flex-direction:column;gap:12px">{rows}</div>
      {cap("four answers captured once, and every reply after is about your business.")}</div>'''

# 2. READ - a ranked leaderboard: 20 accounts scored vs YOUR ICP, top five as heavy score bars
def read():
    accts=[("Northwind Robotics","hiring 3 ops roles",94),
           ("Globex Systems","raised $4M in May",89),
           ("Initech","no AI layer yet",83),
           ("Hooli Labs","switched CRM",76),
           ("Umbrella Co","flat, no signal",61)]
    mx=94; rows=""
    for i,(nm,note,sc) in enumerate(accts):
        w=int(560*sc/mx); low=sc<70
        barcol=f"rgba(200,70,35,.85)" if low else f"rgb({ACC})"
        rows+=(f'<div style="display:flex;align-items:center;gap:16px">'
          f'<span style="flex-shrink:0;width:26px;font-family:DM Mono;font-size:15px;color:#7a746a;text-align:right">{i+1}</span>'
          f'<div style="flex:1">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:14px;color:#8f8f85">{note}</span></div>'
          f'<div style="height:22px;border-radius:7px;background:rgba(250,250,247,.06);overflow:hidden">'
          f'<div style="width:{w}px;height:100%;border-radius:7px;background:linear-gradient(90deg,{barcol},rgba({ACC},.6));box-shadow:inset 0 2px 2px rgba(255,255,255,.25)"></div></div></div>'
          f'<span style="flex-shrink:0;width:44px;font-family:DM Sans;font-weight:900;font-size:26px;color:{"#c86b46" if low else "#FAFAF7"};text-align:right">{sc}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Twenty accounts, ranked for you","FIRST RESEARCH RUN")}
      <div style="display:flex;flex-direction:column;gap:16px">{rows}</div>
      <div style="display:flex;align-items:center;gap:10px;margin-top:16px;font-family:DM Mono;font-size:13px;color:#8f8f85">
        <span style="flex:1;border-top:1px dashed rgba(255,255,255,.12)"></span>+15 more, scored against YOUR customer, not averages<span style="flex:1;border-top:1px dashed rgba(255,255,255,.12)"></span></div>
      {cap("profiled and ranked in one run, so you read the room before you speak.")}</div>'''

# 3. VOICE - IVORY construct: style-match gauge ring + a sample written in your voice
def voice():
    pct=98; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Your voice, not your instructions</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">5 POSTS PASTED</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:190px;height:190px">
          <svg width="190" height="190" viewBox="0 0 190 190">
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 95 95)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:44px;color:#2a2016">{pct}%</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">style match</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4">
            "I killed nine tools last month. The one I kept did not have a chat box."</div>
          <div style="display:flex;gap:22px;margin-top:16px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["short lines","no hedging","your cadence"])}
          </div></div>
      </div>
      {cap("sampled from your five best posts, so every draft sounds like you on a good day.","#8a745a")}</div>'''

# 4. CHORE - a trigger automation: typed once feeds a daily LOOP, exits set, sends parked for approval
def chore():
    W,H=760,430
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One chore, put on a trigger","TYPED ONCE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="nd" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <radialGradient id="loop" cx="42%" cy="34%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="lg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter>
          <marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="rgb({ACC})"/></marker>
        </defs>
        <!-- trigger -->
        <rect x="20" y="176" width="180" height="78" rx="16" fill="url(#nd)" stroke="rgba(255,255,255,.10)"/>
        <text x="110" y="208" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">TRIGGER</text>
        <text x="110" y="232" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#e2dccf">lead goes quiet</text>
        <path d="M200 215 H300" stroke="rgb({ACC})" stroke-width="3.5" fill="none" marker-end="url(#ar)"/>
        <!-- daily loop core -->
        <g filter="url(#lg)"><circle cx="400" cy="215" r="92" fill="url(#loop)"/></g>
        <path d="M400 138 A78 78 0 1 1 335 175" fill="none" stroke="#2a160c" stroke-width="7" stroke-linecap="round" marker-end="url(#ar)" opacity="0.7"/>
        <text x="400" y="206" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">DAILY</text>
        <text x="400" y="234" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010">runs 09:00</text>
        <path d="M492 215 H600" stroke="rgb({ACC})" stroke-width="3.5" fill="none" marker-end="url(#ar)"/>
        <!-- two outputs: exits + parked send -->
        <rect x="602" y="120" width="150" height="80" rx="15" fill="url(#nd)" stroke="rgba(255,255,255,.10)"/>
        <text x="677" y="150" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#8f8f85">EXITS SET</text>
        <text x="677" y="176" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#e2dccf">3 replies stop it</text>
        <rect x="602" y="230" width="150" height="80" rx="15" fill="url(#nd)" stroke="rgba(212,162,127,.4)"/>
        <text x="677" y="260" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">PARKED</text>
        <text x="677" y="286" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#e2dccf">sends await tap</text>
        <path d="M540 190 C575 160,585 160,602 160" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>
        <path d="M540 240 C575 268,585 270,602 270" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>
      </svg>
      {cap("typed once, it follows up every quiet lead daily and parks the sends for you.")}</div>'''

# 5. DIGEST - IVORY one-page morning report: what it did, what needs approval, what is queued
def digest():
    def line(txt,kind):
        if kind=="done":
            ic='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f8f66" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>'
            col="#3a3026"
        elif kind=="wait":
            ic='<span style="width:15px;height:15px;border-radius:50%;border:2.5px solid #96562d;display:inline-block"></span>'
            col="#3a3026"
        else:
            ic='<span style="width:14px;height:14px;border-radius:3px;background:rgba(120,95,60,.3);display:inline-block"></span>'
            col="#6a5a48"
        return (f'<div style="display:flex;align-items:center;gap:12px;padding:7px 0">'
          f'<span style="flex-shrink:0;width:18px;display:flex;justify-content:center">{ic}</span>'
          f'<span style="font-family:DM Sans;font-size:18px;color:{col}">{txt}</span></div>')
    def sect(label,color,body):
        return (f'<div style="margin-bottom:14px"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{color};margin-bottom:2px">{label}</div>{body}</div>')
    done=sect("DONE",'#4f8f66',line("Profiled 12 new accounts",'done')+line("Drafted 8 follow-ups",'done'))
    wait=sect("NEEDS YOUR TAP",'#96562d',line("2 replies to warm leads",'wait')+line("1 proposal to Globex",'wait'))
    queue=sect("QUEUED TOMORROW",'#8a745a',line("Refresh ICP scores",'queue')+line("Watch 4 rival triggers",'queue'))
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">The day on one page</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">DIGEST &middot; 07:00</span></div>
      <div style="background:rgba(255,255,255,.62);border:1px solid rgba(120,95,60,.16);border-radius:20px;padding:26px 30px;box-shadow:inset 0 2px 4px rgba(255,255,255,.9),0 10px 24px rgba(120,95,60,.12)">
        <div style="display:flex;gap:36px">
          <div style="flex:1;border-right:1px solid rgba(120,95,60,.16);padding-right:28px">{done}{wait}</div>
          <div style="flex:1">{queue}
            <div style="margin-top:6px;background:#2a160c;border-radius:14px;padding:16px 18px">
              <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#f0c49e;line-height:1">1 page</div>
              <div style="font-family:DM Mono;font-size:13px;color:rgba(212,162,127,.8);margin-top:3px">read it with coffee</div></div></div>
        </div>
      </div>
      {cap("everything it did, everything it wants approved, tomorrow queued, one glance.","#8a745a")}</div>'''

# 6. HOUR - a horizontal 60-minute timeline: the five plays laid end to end, ticks and minute marks
def hour():
    plays=[("TEACH",12,ACC),("READ",14,ACC),("VOICE",10,ACC),("CHORE",14,ACC),("DIGEST",10,ACC)]
    total=60; W=740; x=0; segs=""; ticks=""; labels=""; acc=0
    for i,(nm,mins,_) in enumerate(plays):
        w=W*mins/total
        shade=0.9-i*0.11
        segs+=(f'<rect x="{x:.0f}" y="40" width="{w-6:.0f}" height="70" rx="12" fill="rgb({ACC})" opacity="{shade:.2f}" '
          f'style="filter:drop-shadow(0 10px 18px rgba(0,0,0,.4))"/>'
          f'<text x="{x+(w-6)/2:.0f}" y="82" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">{nm}</text>'
          f'<text x="{x+(w-6)/2:.0f}" y="102" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgba(26,15,10,.65)">{mins} min</text>')
        acc+=mins
        ticks+=f'<line x1="{x:.0f}" y1="118" x2="{x:.0f}" y2="132" stroke="rgba(250,250,247,.35)" stroke-width="1.5"/>'
        x+=w
    ticks+=f'<line x1="{W:.0f}" y1="118" x2="{W:.0f}" y2="132" stroke="rgba(250,250,247,.35)" stroke-width="1.5"/>'
    marks=""
    for m in (0,15,30,45,60):
        px=W*m/total
        anch="start" if m==0 else ("end" if m==60 else "middle")
        marks+=f'<text x="{px:.0f}" y="152" text-anchor="{anch}" font-family="DM Mono" font-size="13" fill="#8f8f85">{m:02d}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Five plays, sixty minutes","ONE SITTING")}
      <div style="display:flex;align-items:baseline;gap:16px;margin-bottom:20px">
        <span style="font-family:DM Sans;font-weight:900;font-size:64px;color:#FAFAF7;line-height:.9">60</span>
        <span style="font-family:DM Sans;font-weight:700;font-size:22px;color:#c9a583">minutes total, on the Ultron desk</span></div>
      <svg width="{W}" height="170" viewBox="0 0 {W} 170" style="display:block;margin:0 auto">{segs}{ticks}{marks}</svg>
      {cap("not a course, not a certification, one hour of setup and the desk is live.")}</div>'''

# 7. TRAP - dependency graph: play one is the root; skip it and the four downstream plays go generic/severed
def trap():
    W,H=820,460
    kids=[("READ",600,44),("VOICE",600,156),("CHORE",600,268),("DIGEST",600,380)]
    rcx,rcy=185,230
    edges=""; nodes=""
    for nm,x,y in kids:
        cy=y+22
        edges+=f'<path d="M320 {rcy} C440 {rcy},450 {cy},{x-8} {cy}" fill="none" stroke="rgba(200,70,35,.55)" stroke-width="2.6" stroke-dasharray="5 8"/>'
        mx=(410+x-8)/2; my=(rcy+cy)/2
        edges+=f'<line x1="{mx-15:.0f}" y1="{my-15:.0f}" x2="{mx+15:.0f}" y2="{my+15:.0f}" stroke="rgb(200,70,35)" stroke-width="3.4" stroke-linecap="round"/>'
        nodes+=(f'<rect x="{x}" y="{y}" width="185" height="44" rx="12" fill="#211e1a" stroke="rgba(200,70,35,.4)" opacity="0.75"/>'
          f'<text x="{x+22}" y="{y+28}" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#8f8f85">{nm}</text>'
          f'<text x="{x+163}" y="{y+28}" text-anchor="end" font-family="DM Sans" font-size="13" fill="#c86b46">generic</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Skip play one, lose the four","THE ONE TRAP")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb(200,70,35)" flood-opacity="0.4"/></filter></defs>
        {edges}
        <g filter="url(#rg)"><rect x="60" y="{rcy-70}" width="260" height="140" rx="22" fill="#241713" stroke="rgb(200,70,35)" stroke-width="2.5" stroke-dasharray="7 7"/></g>
        <text x="190" y="{rcy-24}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#c86b46">PLAY 1 SKIPPED</text>
        <text x="190" y="{rcy+10}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#FAFAF7">TEACH</text>
        <text x="190" y="{rcy+40}" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#8f8f85">generic context in</text>
        {nodes}
      </svg>
      {cap("generic context makes generic outputs, every disappointment traces back here.")}</div>'''

# 8. CURVE - a compounding growth curve over weeks: corrections become rules become skills, sharper weekly
def curve():
    W,H=740,360
    pts=[(0,300),(120,262),(250,220),(380,168),(510,104),(660,34)]
    d="M"+" L".join(f"{x} {y}" for x,y in pts)
    area=f"M{pts[0][0]} 320 L"+" L".join(f"{x} {y}" for x,y in pts)+f" L{pts[-1][0]} 320 Z"
    stages=[("W1","corrections",300),("W3","rules",220),("W5","skills",104)]
    stg=""
    for lab,txt,y in stages:
        x={300:0,220:250,104:510}[y]
        stg+=(f'<circle cx="{x}" cy="{y}" r="8" fill="rgb({ACC})" filter="url(#cg)"/>'
          f'<text x="{x+14}" y="{y-14}" font-family="DM Mono" font-size="13" fill="rgb({ACC})">{lab}</text>'
          f'<text x="{x+14}" y="{y+6}" font-family="DM Sans" font-weight="700" font-size="16" fill="#e2dccf">{txt}</text>')
    grid="".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="rgba(250,250,247,.05)"/>' for y in (80,160,240,320))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Day one is the floor","IT COMPOUNDS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="af" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.35)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
          <filter id="cg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {grid}
        <line x1="0" y1="320" x2="{W}" y2="320" stroke="rgba(250,250,247,.2)" stroke-width="1.5"/>
        <path d="{area}" fill="url(#af)"/>
        <path d="{d}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        {stg}
        <text x="660" y="24" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="18" fill="#FAFAF7">sharper weekly</text>
      </svg>
      {cap("corrections become rules, rules become skills, the desk only gets sharper.")}</div>'''

PANELS={"teach":teach(),"read":read(),"voice":voice(),"chore":chore(),
        "digest":digest(),"hour":hour(),"trap":trap(),"curve":curve()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/dayone"; os.makedirs(outd,exist_ok=True)
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
