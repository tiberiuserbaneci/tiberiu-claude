#!/usr/bin/env python3
# TIER 3 - YOU ARE THE INTEGRATION LAYER (s3src14). Adapts the scraped "Build a B2B lead machine
# with Claude" carousel into the WIRE-ITS-EYES bar: 8 UNIQUE hand-built coded scenes, clean rounded
# CARD/CARDIV cards, title + one-line caption, warm palette, NO generic stat-chip strips.
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

# 1. BROKEN - disconnected mesh: 6 tool tiles ringed, no links between them, YOU wired to every one
def broken():
    cx,cy,R=410,232,184
    tools=["APOLLO","LINKEDIN","GMAIL","OUTREACH","SHEETS","CALENDLY"]
    angs=[-90,-30,30,90,150,210]
    spokes=""; tiles=""; gaps=""
    for nm,a in zip(tools,angs):
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.38)" stroke-width="2.2" stroke-dasharray="4 7"/>'
        w=152 if len(nm)>7 else 132
        tiles+=(f'<rect x="{x-w/2:.0f}" y="{y-26:.0f}" width="{w}" height="52" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
                f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14.5" letter-spacing=".06em" fill="#cfc9bd">{nm}</text>')
        ga=a+30; gx=cx+R*math.cos(math.radians(ga)); gy=cy+R*math.sin(math.radians(ga))
        gaps+=(f'<line x1="{gx-9:.0f}" y1="{gy-9:.0f}" x2="{gx+9:.0f}" y2="{gy+9:.0f}" stroke="rgb(200,70,35)" stroke-width="2.6"/>'
               f'<line x1="{gx-9:.0f}" y1="{gy+9:.0f}" x2="{gx+9:.0f}" y2="{gy-9:.0f}" stroke="rgb(200,70,35)" stroke-width="2.6"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You are the integration layer","THE PROBLEM")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="you" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="yg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}{gaps}{tiles}
        <g filter="url(#yg)"><circle cx="{cx}" cy="{cy}" r="56" fill="url(#you)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">YOU</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">the glue</text>
      </svg>
      {cap("six tools, none wired to each other. every hand-off runs through you.")}</div>'''

# 2. SOCKET - IVORY: two connectors (Apollo, Gmail) seat into one central PROJECT core, OAuth, no keys
def socket():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Plugged in, not glued</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">CONNECTORS &middot; 2/2</span></div>
      <svg width="740" height="430" viewBox="0 0 740 430" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="core" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f7f0e2"/><stop offset="100%" stop-color="#e3d3bb"/></linearGradient>
          <filter id="cs" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="rgba(150,120,80,.30)"/></filter>
        </defs>
        <g filter="url(#cs)"><rect x="270" y="112" width="200" height="200" rx="30" fill="url(#core)" stroke="rgba(150,110,70,.38)" stroke-width="2"/></g>
        <text x="370" y="202" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a2016">ONE</text>
        <text x="370" y="235" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a2016">PROJECT</text>
        <rect x="256" y="182" width="18" height="60" rx="5" fill="#c8b48f"/>
        <rect x="466" y="182" width="18" height="60" rx="5" fill="#c8b48f"/>
        <g>
          <rect x="38" y="147" width="152" height="130" rx="18" fill="#fbf6ec" stroke="rgba(150,110,70,.32)" stroke-width="1.5"/>
          <text x="114" y="202" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="22" fill="#2a2016">APOLLO</text>
          <text x="114" y="228" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8a745a">270M contacts</text>
          <path d="M190 212 H262" stroke="#96562d" stroke-width="9" stroke-linecap="round"/>
          <circle cx="196" cy="212" r="7" fill="#96562d"/>
        </g>
        <g>
          <rect x="550" y="147" width="152" height="130" rx="18" fill="#fbf6ec" stroke="rgba(150,110,70,.32)" stroke-width="1.5"/>
          <text x="626" y="202" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="22" fill="#2a2016">GMAIL</text>
          <text x="626" y="228" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8a745a">send + reply</text>
          <path d="M550 212 H478" stroke="#96562d" stroke-width="9" stroke-linecap="round"/>
          <circle cx="544" cy="212" r="7" fill="#96562d"/>
        </g>
        <g transform="translate(356,338)">
          <rect x="0" y="11" width="28" height="21" rx="4" fill="none" stroke="#96562d" stroke-width="3"/>
          <path d="M6 11 V5 a8 8 0 0 1 16 0 v6" fill="none" stroke="#96562d" stroke-width="3"/>
        </g>
        <text x="370" y="398" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#6f5c44">OAUTH 2.0 &middot; NO API KEYS</text>
      </svg>
      {cap("connect once in settings. the project holds the wires, you never touch them.","#8a745a")}</div>'''

# 3. FLOW - bezier spine: 5 pipeline stages, each handed to the agent that owns it
def flow():
    stages=[("RESEARCH","CORTEX"),("WRITE","SPECTER"),("SEND","AMPLIFY"),("REPLY","SPECTER"),("BOOK","STRIKER")]
    n=len(stages); W,H=820,440
    xs=[95+i*(630/(n-1)) for i in range(n)]
    ys=[262,192,300,196,266]
    spine=""
    for i in range(n-1):
        x1,y1=xs[i],ys[i]; x2,y2=xs[i+1],ys[i+1]; mx=(x1+x2)/2
        spine+=f'<path d="M{x1:.0f} {y1:.0f} C{mx:.0f} {y1:.0f},{mx:.0f} {y2:.0f},{x2:.0f} {y2:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="5" filter="url(#fg)"/>'
    nodes=""
    for (st,ag),x,y in zip(stages,xs,ys):
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="36" fill="#2b2622" stroke="rgb({ACC})" stroke-width="2.5"/>'
                f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".05em" fill="#f0e8db">{st}</text>'
                f'<rect x="{x-46:.0f}" y="{y+48:.0f}" width="92" height="30" rx="8" fill="rgba(212,162,127,.14)" stroke="rgba(212,162,127,.34)"/>'
                f'<text x="{x:.0f}" y="{y+68:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="rgb({ACC})">{ag}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One project runs the line","PIPELINE WIRED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="fg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spine}{nodes}
      </svg>
      {cap("each stage handed to the agent that owns it. no tabs, no copy-paste.")}</div>'''

# 4. FUNNEL - conversion bands narrowing, per-stage percent + counts
def funnel():
    bands=[("Leads","1,248","100%"),("Contacted","892","71.5%"),("Replied","478","38.3%"),
           ("Meeting","47","13.7%"),("Opportunity","16","34.0%")]
    fills=["#e3c4a0","#d4a27f","#c88a5f","#b56a3f","#9a4e28"]
    topw,botw,bh,gap,cx=610,215,74,8,340
    n=len(bands); poly=""; labels=""
    for i,(nm,cnt,pct) in enumerate(bands):
        wt=topw-(topw-botw)*i/n; wb=topw-(topw-botw)*(i+1)/n
        y0=38+i*(bh+gap); yc=y0+bh/2
        poly+=(f'<polygon points="{cx-wt/2:.0f},{y0} {cx+wt/2:.0f},{y0} {cx+wb/2:.0f},{y0+bh} {cx-wb/2:.0f},{y0+bh}" fill="{fills[i]}"/>')
        labels+=(f'<text x="{cx}" y="{yc-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#2a160c">{nm}</text>'
                 f'<text x="{cx}" y="{yc+19:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">{cnt}</text>'
                 f'<text x="700" y="{yc-2:.0f}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">{pct}</text>'
                 f'<text x="700" y="{yc+18:.0f}" text-anchor="end" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="#8f8f85">conv</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 32px">
      {htitle("1,248 in, 16 deals out","THE FUNNEL")}
      <svg width="740" height="454" viewBox="0 0 740 454" style="display:block;margin:0 auto">
        {poly}{labels}
      </svg>
      {cap("every stage measured. the line reports its own math.")}</div>'''

# 5. FIELD - 1,248 dot field, 47 lit (meetings booked)
def field():
    cols,rows=48,26; total=cols*rows
    lit={(i*263+31)%total for i in range(47)}
    cell,gap=13,3; dots=""
    for i in range(total):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rows*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:36px 40px 36px">
      {htitle("1,248 leads worked, hands off","47 BOOKED")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:6px auto 0">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("each lit cell booked a meeting. every send logged while you slept.")}</div>'''

# 6. GAUGE - IVORY semicircular gauge, 8.9 percent reply rate + supporting counts
def gauge():
    pct=8.9; maxv=20.0; frac=pct/maxv
    cx,cy,R=230,252,178
    def pt(a): return (cx+R*math.cos(math.radians(a)), cy-R*math.sin(math.radians(a)))
    def arc(a0,a1,steps=48):
        seg=[]
        for k in range(steps+1):
            a=a0+(a1-a0)*k/steps; x,y=pt(a); seg.append(f'{x:.1f} {y:.1f}')
        return 'M'+' L'.join(seg)
    bg=arc(180,0); val=arc(180,180-180*frac)
    nx,ny=pt(180-180*frac)
    ticks=""
    for a,lab in [(180,'0'),(135,'5'),(90,'10'),(45,'15'),(0,'20')]:
        ox,oy=cx+(R+22)*math.cos(math.radians(a)),cy-(R+22)*math.sin(math.radians(a))
        ix,iy=cx+(R-13)*math.cos(math.radians(a)),cy-(R-13)*math.sin(math.radians(a))
        tx,ty=cx+(R+2)*math.cos(math.radians(a)),cy-(R+2)*math.sin(math.radians(a))
        ticks+=(f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{tx:.0f}" y2="{ty:.0f}" stroke="rgba(150,110,70,.45)" stroke-width="2.5"/>'
                f'<text x="{ox:.0f}" y="{oy+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a08a68">{lab}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It held the reply rate</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">342 / 3,842</span></div>
      <svg width="470" height="300" viewBox="0 0 470 300" style="display:block;margin:0 auto">
        <path d="{bg}" fill="none" stroke="rgba(150,110,70,.20)" stroke-width="20" stroke-linecap="round"/>
        <path d="{val}" fill="none" stroke="#96562d" stroke-width="20" stroke-linecap="round"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="5" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="12" fill="#2a2016"/>
        <text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#2a2016">{pct}%</text>
        <text x="{cx}" y="{cy-30}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#96562d">REPLY RATE</text>
      </svg>
      <div style="display:flex;gap:16px;margin-top:6px">
        <div style="flex:1;background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:14px 18px">
          <div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#2a2016">3,842</div>
          <div style="font-family:'DM Mono';font-size:12px;color:#8a745a">emails sent</div></div>
        <div style="flex:1;background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:14px 18px">
          <div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#2a2016">342</div>
          <div style="font-family:'DM Mono';font-size:12px;color:#8a745a">replies back</div></div>
      </div>
      {cap("8.9 percent, steady for seven days it ran unattended.","#8a745a")}</div>'''

# 7. GATE - drafts queue into a gate pillar with a lock; nothing sends without the operator's tap
def gate():
    drafts=[("Priya &middot; VP Sales","re: your Q3 hiring push"),
            ("Marco &middot; Founder","idea for Northwind"),
            ("Dana &middot; Head of Ops","saw the raise, congrats")]
    ys=[86,225,364]; cards=""; feeds=""; gx=470
    for (a,b),y in zip(drafts,ys):
        cards+=(f'<rect x="30" y="{y-42}" width="358" height="84" rx="16" fill="url(#chip)" stroke="rgba(255,255,255,.10)"/>'
                f'<text x="52" y="{y-8}" font-family="DM Sans" font-weight="800" font-size="18" fill="#f0e8db">{a}</text>'
                f'<text x="52" y="{y+18}" font-family="DM Sans" font-size="15" fill="#9a9488">{b}</text>'
                f'<text x="366" y="{y-24}" text-anchor="end" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="rgb({ACC})">DRAFT</text>')
        feeds+=f'<rect x="388" y="{y-5}" width="{gx-388}" height="10" rx="5" fill="rgb({ACC})" opacity="0.7"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <svg width="820" height="460" viewBox="0 0 820 460" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="chip" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <linearGradient id="gt" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#211e1a"/></linearGradient>
          <filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.30"/></filter>
        </defs>
        {feeds}{cards}
        <g filter="url(#gg)"><rect x="{gx}" y="46" width="128" height="368" rx="28" fill="url(#gt)" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <g transform="translate({gx+38},188)"><rect x="0" y="30" width="52" height="40" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="6"/><path d="M9 30 V17 a17 17 0 0 1 34 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="6"/></g>
        <text x="{gx+64}" y="298" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#FAFAF7">GATE</text>
        <text x="{gx+64}" y="326" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">your tap</text>
        <rect x="{gx+130}" y="225" width="42" height="10" rx="5" fill="rgb({ACC})" opacity="0.9"/>
        <rect x="{gx+180}" y="150" width="180" height="150" rx="20" fill="#201d19" stroke="rgba(212,162,127,.34)" stroke-width="1.5"/>
        <text x="{gx+270}" y="212" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#FAFAF7">SENT</text>
        <text x="{gx+270}" y="240" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">after you approve</text>
        <g>{"".join(f'<circle cx="{gx+230+i*40}" cy="270" r="8" fill="rgb({ACC})"/>' for i in range(3))}</g>
      </svg>
      {cap("every draft parks at the gate. approve the batch, then it flies.")}</div>'''

# 8. SPLIT - before/after: 7 red-tinged tabs (you, the wire) vs one glowing operator core
def split():
    tabs=""
    for i in range(7):
        y=74+i*44
        tabs+=(f'<rect x="40" y="{y}" width="288" height="30" rx="8" fill="#2a2422" stroke="rgba(200,70,35,.35)"/>'
               f'<circle cx="60" cy="{y+15}" r="5" fill="rgb(200,70,35)"/>'
               f'<rect x="76" y="{y+10}" width="{130+(i*17)%120}" height="10" rx="5" fill="rgba(250,250,247,.15)"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven tabs, or one operator","BEFORE / AFTER")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <defs><radialGradient id="op" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <text x="184" y="52" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb(200,70,35)">WITHOUT</text>
        {tabs}
        <text x="184" y="424" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#9a7a70">7 tabs &middot; manual glue</text>
        <circle cx="415" cy="238" r="30" fill="#141210" stroke="rgba(255,255,255,.14)"/>
        <text x="415" y="244" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#cfc9bd">VS</text>
        <text x="640" y="52" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">WITH ULTRON</text>
        <g filter="url(#og)"><circle cx="640" cy="238" r="120" fill="url(#op)"/></g>
        <text x="640" y="228" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="640" y="258" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">OPERATOR</text>
        <text x="640" y="424" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#c9a583">one login &middot; it runs itself</text>
      </svg>
      {cap("stop being the integration layer. install the one that is.")}</div>'''

PANELS={"broken":broken(),"socket":socket(),"flow":flow(),"funnel":funnel(),
        "field":field(),"gauge":gauge(),"gate":gate(),"split":split()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src14"; os.makedirs(outd,exist_ok=True)
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
