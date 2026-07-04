#!/usr/bin/env python3
# TIER 3 - MARKETING AS A COMMAND PALETTE, built to the WIRE-ITS-EYES bar: each of the 8 panels a
# UNIQUE hand-coded scene filling a clean rounded card, title + one mono caption, NO stat-chip strip,
# NO clip-path cuts, NO extruded walls. Warm palette; Ultron prices in cents. Cost zero.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; BAD="200,70,35"; IVACC="#96562d"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IVACC}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:18px">{t}</div>'

# 1. PALETTE - the slash-command palette mockup: a search bar + 6 command rows, each a whole play at
# a cents price. The literal product, dense and real.
def palette():
    rows=[("/blog","SEO post drafted in your voice","0.09c"),
          ("/repurpose","one article to eight channels","0.12c"),
          ("/sequence","funnel emails, written to stage","0.08c"),
          ("/audit","competitor gaps flagged","0.14c"),
          ("/headlines","ten scored, one ships","0.05c"),
          ("/tone","clone your cadence","0.06c")]
    ri=""
    for i,(cmd,desc,cost) in enumerate(rows):
        on=(i==0)
        bg="linear-gradient(160deg,#403a33,#2b2621)" if on else "transparent"
        bd="rgba(212,162,127,.5)" if on else "rgba(255,255,255,.06)"
        ri+=(f'<div style="display:flex;align-items:center;gap:18px;background:{bg};border:1px solid {bd};'
          f'border-radius:14px;padding:15px 20px">'
          f'<div style="flex-shrink:0;width:42px;height:42px;border-radius:11px;background:rgba(212,162,127,.14);'
          f'border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">'
          f'<svg width="22" height="22" viewBox="0 0 24 24"><path d="M15 4 9 20" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round"/></svg></div>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-weight:500;font-size:19px;letter-spacing:.02em;color:#FAFAF7;width:158px">{cmd}</span>'
          f'<span style="flex:1;font-family:\'DM Sans\';font-size:18px;color:#b8b2a6">{desc}</span>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:15px;font-weight:500;color:rgb({ACC});'
          f'background:rgba(212,162,127,.10);border-radius:8px;padding:5px 11px">{cost}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Twenty plays, one line each","COMMAND PALETTE")}
      <div style="display:flex;align-items:center;gap:14px;background:#141210;border:1px solid rgba(212,162,127,.28);
        border-radius:14px;padding:16px 20px;margin-bottom:16px;box-shadow:inset 0 2px 6px rgba(0,0,0,.5)">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.5-4.5"/></svg>
        <span style="flex:1;font-family:'DM Mono';font-size:19px;color:#e2dccf">marketing<span style="color:rgb({ACC})">|</span></span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:#7a746a;border:1px solid rgba(255,255,255,.12);border-radius:7px;padding:4px 9px">CMD K</span></div>
      <div style="display:flex;flex-direction:column;gap:9px">{ri}</div>
      {cap("type a slash, get a whole workflow - not a blank campaign brief.")}</div>'''

# 2. PLAYBLOG - isometric stack of the structured draft (H1 -> intro -> sections -> CTA), the last
# card carrying a rank readout. Distinct 3D iso form.
def playblog():
    steps=[("H1","Why founders outgrow their content agency",0),
           ("INTRO","hook, in your cadence",1),
           ("H2 x4","structured, keyword-mapped",2),
           ("CTA","one comment trigger",3)]
    cards=""
    for nm,sub,i in steps:
        y=i*104
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);'
          f'border:1.5px solid rgba(255,255,255,.14);border-radius:16px;padding:16px 22px;'
          f'box-shadow:0 28px 42px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:14px;letter-spacing:.1em;color:rgb({ACC});width:74px">{nm}</span>'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#FAFAF7">{sub}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("An SEO post in one command","STRUCTURED DRAFT")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:432px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:388px;background:rgb({ACC});color:#1a0f0a;font-family:'DM Sans';font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Ranks #4 before review</div></div></div>
      {cap("keyword in, structured draft out, in your voice - you edit, never start blank.")}</div>'''

# 3. PLAYREP - bezier node graph: one article node fans into eight channel nodes.
def playrep():
    W,H=760,470
    hubx,huby=150,235
    chans=["LinkedIn","X thread","Instagram","TikTok","Newsletter","YouTube","Carousel","Reddit"]
    edges=""; nodes=""
    n=len(chans); top=48; step=(H-2*top)/(n-1)
    for i,ch in enumerate(chans):
        y=top+step*i; nx=560
        mx=(hubx+nx)/2
        edges+=f'<path d="M{hubx+64} {huby} C{mx:.0f} {huby},{mx:.0f} {y:.0f},{nx-8} {y:.0f}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.2"/>'
        nodes+=(f'<rect x="{nx}" y="{y-19:.0f}" width="168" height="38" rx="11" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="{nx+20}" cy="{y:.0f}" r="4.5" fill="rgb({ACC})"/>'
          f'<text x="{nx+36}" y="{y+5:.0f}" font-family="DM Sans" font-weight="600" font-size="16" fill="#d9d5cc">{ch}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One article becomes eight","REPURPOSE MATRIX")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {edges}
        <g filter="url(#hg)"><circle cx="{hubx}" cy="{huby}" r="64" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#1a0f0a">1</text>
        <text x="{hubx}" y="{huby+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">article</text>
        {nodes}
      </svg>
      {cap("posts, tweets, carousel scripts, newsletter - the matrix runs itself, gated.")}</div>'''

# 4. PLAYSEQ - horizontal timeline: 6 emails plotted across 3 funnel stages, all parked at the gate.
def playseq():
    W,H=820,400
    x0,x1=30,790; axy=232
    stages=[("AWARENESS",x0,282),("CONSIDERATION",282,556),("DECISION",556,x1)]
    bands=""
    for nm,a,b in stages:
        bands+=(f'<rect x="{a}" y="140" width="{b-a-8}" height="184" rx="12" fill="rgba(212,162,127,.05)" stroke="rgba(212,162,127,.14)"/>'
          f'<text x="{(a+b)/2:.0f}" y="166" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".12em" fill="#9a9488">{nm}</text>')
    mails=[("D0","Welcome"),("D2","The problem"),("D5","Proof"),("D8","Objection"),("D11","The offer"),("D14","Last call")]
    m=len(mails); first=x0+66; last=x1-66; step=(last-first)/(m-1)
    marks=""
    for i,(d,s) in enumerate(mails):
        x=first+step*i; up=(i%2==0); cy2=(axy-92) if up else (axy+92)
        cardy=(cy2-40) if up else cy2
        marks+=(f'<line x1="{x:.0f}" y1="{axy}" x2="{x:.0f}" y2="{cy2}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{axy}" r="9" fill="rgb({ACC})" filter="url(#eg)"/>'
          f'<rect x="{x-60:.0f}" y="{cardy:.0f}" width="120" height="40" rx="10" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>'
          f'<text x="{x:.0f}" y="{cardy+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">{d}</text>'
          f'<text x="{x:.0f}" y="{cardy+31:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="600" font-size="13" fill="#e2dccf">{s}</text>')
    badge=(f'<g transform="translate({W/2-107:.0f},44)">'
      f'<rect x="0" y="0" width="214" height="52" rx="16" fill="#211d19" stroke="rgba(212,162,127,.3)"/>'
      f'<g transform="translate(30,26)"><rect x="-11" y="-3" width="22" height="17" rx="4" fill="none" stroke="rgb({ACC})" stroke-width="2.6"/><path d="M-6 -3 V-8 a7 7 0 0 1 14 0 v5" fill="none" stroke="rgb({ACC})" stroke-width="2.6"/></g>'
      f'<text x="58" y="31" font-family="DM Sans" font-weight="700" font-size="16" fill="#e2dccf">held for your tap</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The funnel emails, to stage","SEQUENCE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="eg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {badge}
        {bands}
        <line x1="{x0+8}" y1="{axy}" x2="{x1-8}" y2="{axy}" stroke="rgba(212,162,127,.3)" stroke-width="2"/>
        {marks}
      </svg>
      {cap("describe the stage; five to seven emails land with CTAs, parked before send.")}</div>'''

# 5. PLAYAUDIT - dot field: a competitor's 360 published topics, six unclaimed gaps lit for you.
def playaudit():
    cols,rowsn=30,12
    lit={41,118,205,266,317,158}
    cell=17; gap=6
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<circle cx="{x+cell/2}" cy="{y+cell/2}" r="{cell/2}" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<circle cx="{x+cell/2}" cy="{y+cell/2}" r="{cell/2-1}" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">360</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">topics they cover</span></div>
        <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">GAP AUDIT</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="display:flex;align-items:center;gap:12px;margin-top:18px">
        <span style="width:13px;height:13px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba(212,162,127,.8)"></span>
        <span style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#FAFAF7">6 unclaimed gaps</span>
        <span style="font-family:'DM Mono';font-size:14px;color:#8f8f85;margin-left:6px">URLs in, angles and frequencies out</span></div></div>'''

# 6. PLAYHEAD - IVORY gauge: the winning headline score on a semicircle dial + three graded bars.
def playhead():
    score=92; a0,a1=180,360; frac=score/100; ang=a0+(a1-a0)*frac
    cx,cy,R=175,175,132
    def pt(a,rr): return (cx+rr*math.cos(math.radians(a)), cy+rr*math.sin(math.radians(a)))
    ax0,ay0=pt(a0,R); ax1,ay1=pt(a1,R)
    fx,fy=pt(ang,R)
    nx,ny=pt(ang,R-24)
    bars=[("Emotion",88),("Clarity",94),("Curiosity",90)]
    br=""
    for nm,v in bars:
        br+=(f'<div style="margin-bottom:15px"><div style="display:flex;justify-content:space-between;margin-bottom:6px">'
          f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:17px;color:#2a2016">{nm}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:15px;color:{IVACC}">{v}</span></div>'
          f'<div style="height:11px;border-radius:6px;background:rgba(150,90,45,.14)"><div style="width:{v}%;height:11px;border-radius:6px;background:{IVACC}"></div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("Ten headlines scored, one ships","HEADLINE SCORE")}
      <div style="display:flex;align-items:center;gap:40px">
        <div style="flex-shrink:0;position:relative;width:350px;height:210px">
          <svg width="350" height="210" viewBox="0 0 350 210">
            <path d="M{ax0:.1f} {ay0:.1f} A{R} {R} 0 0 1 {ax1:.1f} {ay1:.1f}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="20" stroke-linecap="round"/>
            <path d="M{ax0:.1f} {ay0:.1f} A{R} {R} 0 0 1 {fx:.1f} {fy:.1f}" fill="none" stroke="{IVACC}" stroke-width="20" stroke-linecap="round"/>
            <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#2a2016" stroke-width="6" stroke-linecap="round"/>
            <circle cx="{cx}" cy="{cy}" r="12" fill="#2a2016"/>
            <text x="{cx}" y="{cy-24}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="60" fill="#2a2016">{score}</text>
            <text x="{cx}" y="{cy+2}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="{IVACC}">TOP OF TEN</text>
          </svg></div>
        <div style="flex:1">{br}
          <div style="font-family:'DM Sans';font-size:15px;color:#5a4634;margin-top:4px">graded against the boring-headline rules</div></div>
      </div>
      {cap("emotion, clarity, curiosity - nine rejected, the strongest one goes live.","#8a745a")}</div>'''

# 7. DIFF10B - IVORY two-column comparison: dead features vs whole plays.
def diff10b():
    feats=["a chat box","30 templates","a dashboard","5 integrations"]
    plays=["/blog","/repurpose","/sequence","/audit"]
    fc=""
    for f in feats:
        fc+=(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({BAD})" stroke-width="2.6"><path d="M6 6l12 12M18 6L6 18"/></svg>'
          f'<span style="font-family:\'DM Sans\';font-size:19px;color:#6a5a48">{f}</span></div>')
    pc=""
    for p in plays:
        pc+=(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="{IVACC}" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="font-family:\'DM Mono\';font-weight:500;font-size:19px;color:#2a2016">{p}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("Features versus plays","WHY IT WINS")}
      <div style="display:flex;align-items:stretch;gap:22px">
        <div style="flex:1;background:rgba(150,90,45,.05);border:1px solid rgba(150,90,45,.16);border-radius:20px;padding:24px 26px">
          <div style="font-family:'DM Mono';font-size:14px;letter-spacing:.14em;color:#8a745a;margin-bottom:6px">TOOLS GIVE YOU</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#4a3a28;margin-bottom:18px">features</div>{fc}
          <div style="font-family:'DM Sans';font-size:15px;color:#8a745a;margin-top:8px">you still do the work</div></div>
        <div style="display:flex;align-items:center;font-family:'DM Sans';font-weight:900;font-size:22px;color:{IVACC}">vs</div>
        <div style="flex:1;background:linear-gradient(160deg,#fff8ee,#f3e6cf);border:1.5px solid {IVACC};border-radius:20px;padding:24px 26px;box-shadow:0 18px 34px rgba(150,90,45,.18)">
          <div style="font-family:'DM Mono';font-size:14px;letter-spacing:.14em;color:{IVACC};margin-bottom:6px">THE PALETTE GIVES YOU</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#2a2016;margin-bottom:18px">plays</div>{pc}
          <div style="font-family:'DM Sans';font-size:15px;color:#5a4634;margin-top:8px">voice and gate baked in</div></div>
      </div>
      {cap("each command is a whole workflow, not one more feature to operate.","#8a745a")}</div>'''

# 8. MONDAY10 - radial hub: five commands orbit the MONDAY core, one hour, all gated.
def monday10():
    W,H=820,470
    cx,cy=410,235
    cmds=[("/plan","the week mapped",-90),("/draft","3 posts written",-18),
          ("/repurpose","to 8 channels",54),("/audit","gaps flagged",126),("/queue","scheduled, gated",198)]
    spokes=""; nodes=""
    for nm,sub,a in cmds:
        x=cx+185*math.cos(math.radians(a)); y=cy+150*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        nodes+=(f'<rect x="{x-92:.0f}" y="{y-32:.0f}" width="184" height="64" rx="15" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>'
          f'<text x="{x:.0f}" y="{y-4:.0f}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="17" fill="rgb({ACC})">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+18:.0f}" text-anchor="middle" font-family="DM Sans" font-size="14" fill="#b8b2a6">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The marketing Monday, before coffee","5 COMMANDS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="mh" cx="38%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {spokes}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="72" fill="url(#mh)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#1a0f0a">MON</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">1 hour</text>
        {nodes}
      </svg>
      {cap("plan, draft, repurpose, audit, queue - five commands, one hour, run for cents.")}</div>'''

PANELS={"palette":palette(),"playblog":playblog(),"playrep":playrep(),"playseq":playseq(),
        "playaudit":playaudit(),"playhead":playhead(),"diff10b":diff10b(),"monday10":monday10()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/twentyplays"; os.makedirs(outd,exist_ok=True)
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
