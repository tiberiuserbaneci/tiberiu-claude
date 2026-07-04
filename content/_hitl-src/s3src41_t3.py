#!/usr/bin/env python3
# HAND IT THE KEYS - IG Scraped s3src41 ("10 skills / tools to build a $10M business",
# a list of self-hosted open-source AI agents that "actually do things") adapted to the
# WIRE-ITS-EYES bar. The real subject: an AI that takes real actions holds the keys to your
# business. 8 unique hand-built coded scenes, one Ultron capability each, all gated by you.
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

# 1. SENDS - bezier flow: one DRAFT node fans into a 3-step sequence, converges into a lit INBOX
def sends():
    steps=[("Day 1","intro",96),("Day 3","nudge",230),("Day 6","break-up",364)]
    edges=""; nodes=""
    dx,dy=180,230; sx=350; ix=712,230
    for lab,sub,y in steps:
        # draft -> step
        mx=(dx+sx)/2
        edges+=f'<path d="M{dx} {dy} C{mx:.0f} {dy},{mx:.0f} {y},{sx} {y}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
        # step -> inbox
        mx2=(sx+180+ix[0])/2
        edges+=f'<path d="M{sx+180} {y} C{mx2:.0f} {y},{mx2:.0f} {ix[1]},{ix[0]-66} {ix[1]}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
        nodes+=(f'<rect x="{sx}" y="{y-30}" width="180" height="60" rx="14" fill="linear-gradient(160deg,#33302b,#211e1a)" fill-opacity="1" style="fill:#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{sx+20}" y="{y-4}" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">{lab.upper()}</text>'
          f'<text x="{sx+20}" y="{y+18}" font-family="DM Sans" font-weight="700" font-size="18" fill="#eae4d8">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It sends, not suggests","SPECTER · OUTBOUND")}
      <svg width="820" height="460" viewBox="0 0 820 460" style="display:block">
        <defs><radialGradient id="ib" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ig1" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}
        <rect x="30" y="{dy-34}" width="150" height="68" rx="15" fill="#221f1b" stroke="rgba(212,162,127,.34)"/>
        <text x="105" y="{dy-6}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".12em" fill="rgb({ACC})">DRAFT</text>
        <text x="105" y="{dy+16}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">one line</text>
        {nodes}
        <g filter="url(#ig1)"><circle cx="{ix[0]}" cy="{ix[1]}" r="66" fill="url(#ib)"/></g>
        <text x="{ix[0]}" y="{ix[1]-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">SENT</text>
        <text x="{ix[0]}" y="{ix[1]+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">all 3 live</text>
      </svg>
      {cap("one line becomes a five-touch sequence, written and delivered.")}</div>'''

# 2. BOOKS - IVORY week calendar grid, one slot booked with a confirm check
def books():
    days=["MON","TUE","WED","THU","FRI"]
    rowsY=[92,150,208,266]; times=["09:00","10:30","12:00","14:00"]
    colX=[60,196,332,468,604]; cw=118
    grid=""
    for ci,d in enumerate(days):
        grid+=f'<text x="{colX[ci]+cw/2}" y="66" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="{"#96562d" if d=="THU" else "#9c8a70"}">{d}</text>'
    for ri,ty in enumerate(times):
        grid+=f'<text x="30" y="{rowsY[ri]+34}" font-family="DM Mono" font-size="11.5" fill="#a89572">{ty}</text>'
        for ci in range(5):
            booked=(ci==3 and ri==1)
            if booked: continue
            grid+=f'<rect x="{colX[ci]}" y="{rowsY[ri]}" width="{cw}" height="46" rx="10" fill="rgba(150,120,80,.06)" stroke="rgba(150,120,80,.20)"/>'
    # booked event - a wider floating chip anchored on THU 10:30 so label + check breathe
    ew=196; bx=colX[3]+cw-ew+12; by=rowsY[1]-3; eh=52
    booked=(f'<rect x="{bx}" y="{by}" width="{ew}" height="{eh}" rx="12" fill="#96562d" filter="url(#bk)"/>'
      f'<text x="{bx+18}" y="{by+eh/2-4}" font-family="DM Sans" font-weight="800" font-size="15" fill="#fdfbf6">Discovery call</text>'
      f'<text x="{bx+18}" y="{by+eh/2+15}" font-family="DM Mono" font-size="11" letter-spacing=".06em" fill="rgba(253,251,246,.8)">confirmed</text>'
      f'<circle cx="{bx+ew-26}" cy="{by+eh/2}" r="14" fill="#fdfbf6"/>'
      f'<path d="M{bx+ew-33} {by+eh/2} l5 5 l9 -10" fill="none" stroke="#96562d" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The meeting, booked","LIVE CALENDAR","#2a2016")}
      <svg width="740" height="330" viewBox="0 0 740 330" style="display:block;margin:0 auto">
        <defs><filter id="bk" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="rgba(150,90,45,.5)"/></filter></defs>
        {grid}{booked}
      </svg>
      {cap("a yes turns into a held slot, no back-and-forth thread.","#8a745a")}</div>'''

# 3. CONNECTS - radial switchboard: operator hub wired to 5 real app nodes, action LEDs live
def connects():
    cx,cy=430,232; Rr=182
    apps=[("EMAIL","M2 5 L10 9 L18 5",-140),("CRM","P",-68),("DOCS","D",4),("CALENDAR","C",76),("PAYMENTS","$",148)]
    spokes=""; chips=""
    for nm,gl,a in apps:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.42)" stroke-width="2.6"/>'
          f'<circle cx="{(cx+x)/2:.0f}" cy="{(cy+y)/2:.0f}" r="4.5" fill="rgb({ACC})" filter="url(#pd)"/>')
        chips+=(f'<g><rect x="{x-70:.0f}" y="{y-27:.0f}" width="140" height="54" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.11)"/>'
          f'<circle cx="{x-46:.0f}" cy="{y:.0f}" r="7" fill="#241f1a" stroke="rgba(212,162,127,.5)" stroke-width="1.6"/>'
          f'<circle cx="{x-46:.0f}" cy="{y:.0f}" r="3" fill="rgb({ACC})"/>'
          f'<text x="{x-30:.0f}" y="{y+5:.0f}" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#d9d5cc">{nm}</text>'
          f'<circle cx="{x+58:.0f}" cy="{y-15:.0f}" r="4" fill="#c9a583"/></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Wired into your stack","TOOL USE")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="hb3" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg3" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="pd" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {spokes}
        <g filter="url(#hg3)"><circle cx="{cx}" cy="{cy}" r="70" fill="url(#hb3)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">OPERATOR</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one command</text>
        {chips}
      </svg>
      {cap("email, crm, docs, calendar and payments, driven from one sentence.")}</div>'''

# 4. BUDGET - semicircular gauge/dial: the router picks a tier, needle on SMART, cents readout
def budget():
    cx,cy,R=410,300,210
    def pt(ang,r): return (cx+r*math.cos(math.radians(ang)), cy-r*math.sin(math.radians(ang)))
    ticks=[("LITE","0.02c",150),("SMART","0.11c",90),("DEEP","0.40c",30)]
    arc=f'<path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy}" fill="none" stroke="rgba(212,162,127,.18)" stroke-width="20" stroke-linecap="round"/>'
    # lit arc up to SMART (from 180 down to 90)
    ax,ay=pt(90,R)
    arc+=f'<path d="M{cx-R} {cy} A{R} {R} 0 0 1 {ax:.0f} {ay:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="20" stroke-linecap="round" filter="url(#gg4)"/>'
    labels=""
    for nm,cost,ang in ticks:
        lx,ly=pt(ang,R+40); on=(nm=="SMART")
        labels+=(f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="{"#FAFAF7" if on else "#8f8f85"}">{nm}</text>'
          f'<text x="{lx:.0f}" y="{ly+22:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="{f"rgb({ACC})" if on else "#6f6a60"}">{cost}</text>')
        tx0,ty0=pt(ang,R-12); tx1,ty1=pt(ang,R+2)
        labels+=f'<line x1="{tx0:.0f}" y1="{ty0:.0f}" x2="{tx1:.0f}" y2="{ty1:.0f}" stroke="rgba(250,250,247,.3)" stroke-width="2"/>'
    nx,ny=pt(90,R-34)
    needle=(f'<line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>'
      f'<circle cx="{cx}" cy="{cy}" r="15" fill="#2a2724" stroke="rgb({ACC})" stroke-width="3"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("It budgets each job","MODEL ROUTER")}
      <svg width="820" height="380" viewBox="0 0 820 380" style="display:block;margin:0 auto">
        <defs><filter id="gg4" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {arc}{labels}{needle}
        <text x="{cx}" y="{cy+52}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">0.11c</text>
        <text x="{cx}" y="{cy+78}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#8f8f85">THIS JOB</text>
      </svg>
      {cap("lite for lookups, deep for judgement, you never pick a model.")}</div>'''

# 5. VAULT - IVORY private ledger: 5 packed rows of what it remembers, each behind a lock LED
def vault():
    rows=[("ICP","Founder, 2-50 staff, IT and SaaS"),
          ("PRICING","cents per token, Max at 19"),
          ("BRAND VOICE","short lines, no hedging, your cadence"),
          ("PIPELINE","34 deals, 6 in close plan"),
          ("DOCS","product specs, blueprints, techniques")]
    body=""
    for i,(k,v) in enumerate(rows):
        line="" if i==len(rows)-1 else "border-bottom:1px solid rgba(150,120,80,.20);"
        body+=(f'<div style="display:flex;align-items:center;gap:18px;padding:15px 4px;{line}">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" style="flex-shrink:0"><rect x="4" y="10.5" width="16" height="11" rx="2.5" fill="none" stroke="#96562d" stroke-width="2.2"/><path d="M7.5 10.5 V7.5 a4.5 4.5 0 0 1 9 0 v3" fill="none" stroke="#96562d" stroke-width="2.2"/></svg>'
          f'<span style="flex-shrink:0;width:150px;font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#96562d">{k}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:19px;color:#2a2016">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 32px">
      {htitle("Your business, on file","PRIVATE VAULT","#2a2016")}
      <div style="background:rgba(255,255,255,.5);border:1px solid rgba(150,120,80,.24);border-radius:20px;padding:8px 24px 12px">
        {body}
      </div>
      {cap("every agent reads one locked core before it touches a thing.","#8a745a")}</div>'''

# 6. CENTS - split compare: the self-hosted stack (tall red bill) vs the operator (a sliver of cents)
def cents():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The bill, in cents","PAY PER TOKEN")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="badbar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#d0522f"/><stop offset="100%" stop-color="#8a2f18"/></linearGradient>
          <linearGradient id="goodbar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="#a86a3f"/></linearGradient>
          <filter id="gb6" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter>
        </defs>
        <line x1="60" y1="360" x2="760" y2="360" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>
        <!-- competitor bill -->
        <rect x="120" y="70" width="180" height="290" rx="12" fill="url(#badbar)"/>
        <text x="210" y="118" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="#fff">$2,400</text>
        <text x="210" y="146" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgba(255,235,228,.9)">PER MONTH</text>
        {"".join(f'<text x="210" y="{190+i*34}" text-anchor="middle" font-family="DM Sans" font-size="15.5" fill="rgba(255,240,235,.92)">{t}</text>' for i,t in enumerate(["10 self-hosted repos","1 VPS you keep alive","updates and patches","the glue in between"]))}
        <text x="210" y="392" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".12em" fill="#e08a6a">THE STACK</text>
        <!-- operator sliver -->
        <rect x="520" y="330" width="180" height="30" rx="10" fill="url(#goodbar)" filter="url(#gb6)"/>
        <text x="610" y="300" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="#FAFAF7">cents</text>
        <text x="610" y="326" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">PER TASK</text>
        <text x="610" y="392" text-anchor="middle" font-family="DM Mono" font-size="13.5" letter-spacing=".12em" fill="rgb({ACC})">THE OPERATOR</text>
      </svg>
      {cap("a stack you host and babysit, or pennies for the work itself.")}</div>'''

# 7. WATCH - radar sweep of account signals, ranked, first-to-know readout
def watch():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("Funding",300,150),("Hiring",118,96),("Stack move",205,168),("Intent",44,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b7)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    readout=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">You knew</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">Tue 08:04</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">The press</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">Fri 11:20</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">3 days ahead</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw7" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b7" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw7)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It watches on triggers","CORTEX · SIGNALS")}
        {readout}
        {cap("funding, hiring, intent, surfaced the morning it happens.")}
      </div></div>'''

# 8. GATE - checkpoint: an action queued at a barrier, held for your approve stamp, one blocked
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing ships unasked","HUMAN GATE")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="stamp" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg8" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <!-- blocked auto-attempt (severed, subordinated top) -->
        <g opacity="0.8">
          <rect x="40" y="52" width="300" height="52" rx="13" fill="rgba(200,70,35,.08)" stroke="rgba(200,70,35,.45)"/>
          <text x="60" y="84" font-family="DM Sans" font-size="17" fill="#c98a76" text-decoration="line-through">auto-send, unsupervised</text>
          <line x1="352" y1="78" x2="392" y2="78" stroke="rgb(200,70,35)" stroke-width="3" stroke-dasharray="4 6"/>
          <line x1="372" y1="66" x2="372" y2="90" stroke="rgb(200,70,35)" stroke-width="3"/>
          <text x="420" y="84" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="#c84623">BLOCKED</text>
        </g>
        <!-- the queued action -->
        <rect x="40" y="196" width="290" height="90" rx="18" fill="linear-gradient(160deg,#33302b,#211e1a)" style="fill:#2a2724" stroke="rgba(255,255,255,.12)"/>
        <text x="62" y="234" font-family="DM Mono" font-size="12.5" letter-spacing=".12em" fill="rgb({ACC})">QUEUED</text>
        <text x="62" y="262" font-family="DM Sans" font-weight="800" font-size="22" fill="#FAFAF7">Send 240 emails</text>
        <!-- track into the barrier -->
        <path d="M330 241 H452" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <!-- barrier posts -->
        <rect x="470" y="150" width="20" height="182" rx="6" fill="#3a352f" stroke="rgba(212,162,127,.4)"/>
        <rect x="560" y="150" width="20" height="182" rx="6" fill="#3a352f" stroke="rgba(212,162,127,.4)"/>
        <rect x="470" y="150" width="110" height="26" rx="7" fill="rgb({ACC})"/>
        <text x="525" y="358" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#8f8f85">HELD</text>
        <!-- approve stamp -->
        <g filter="url(#sg8)"><circle cx="690" cy="241" r="96" fill="url(#stamp)"/></g>
        <circle cx="690" cy="241" r="96" fill="none" stroke="rgba(26,15,10,.25)" stroke-width="2"/>
        <path d="M654 244 l22 22 l46 -54" fill="none" stroke="#1a0f0a" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="690" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("full access, held on your reins, one approve away from live.")}</div>'''

PANELS={"sends":sends(),"books":books(),"connects":connects(),"budget":budget(),
        "vault":vault(),"cents":cents(),"watch":watch(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src41"; os.makedirs(outd,exist_ok=True)
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
