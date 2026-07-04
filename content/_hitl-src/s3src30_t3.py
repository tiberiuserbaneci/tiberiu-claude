#!/usr/bin/env python3
# TIER 3 - INBOXES THAT LAND (cold-email sending infrastructure / deliverability layer).
# Adapted from IG scraped s3src30 to the WIRE-ITS-EYES bar: 8 unique hand-built coded scenes,
# clean CARD/CARDIV rounded cards, warm palette, htitle + one cap each. NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tc=None):
    tc=tc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SPAM - IVORY email-client mockup: cold-from-root lands in the SPAM folder, poisoning real mail
def spam():
    inbox=""
    for t,s in [("Northwind - deal reply","re: your proposal"),("Stripe - invoice","payment received")]:
        inbox+=(f'<div style="display:flex;align-items:center;gap:13px;background:rgba(255,255,255,.66);border:1px solid rgba(120,95,60,.14);border-radius:12px;padding:12px 15px;margin-bottom:9px">'
          f'<span style="width:9px;height:9px;border-radius:50%;background:#96562d;flex-shrink:0"></span>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:17px;color:#2a2016">{t}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8a745a">{s}</div></div></div>')
    spam=""
    for t,s in [("you@yourcompany.com","cold blast - 240 recipients"),("you@yourcompany.com","follow-up 2 - 240 recipients"),("you@yourcompany.com","follow-up 3 - 240 recipients")]:
        spam+=(f'<div style="display:flex;align-items:center;gap:13px;background:rgba(200,70,35,.07);border:1px solid rgba(200,70,35,.28);border-radius:12px;padding:12px 15px;margin-bottom:9px">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M12 2 22 20 2 20Z" fill="none" stroke="#c84623" stroke-width="2.2" stroke-linejoin="round"/><line x1="12" y1="9" x2="12" y2="14" stroke="#c84623" stroke-width="2.2" stroke-linecap="round"/><circle cx="12" cy="17" r="1.2" fill="#c84623"/></svg>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-weight:500;font-size:16px;color:#7a3320">{t}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#a06248">{s}</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 40px 34px">
      {htitle("Cold-from-root lands in spam","YOUR MAIN DOMAIN","#2a2016","#96562d")}
      <div style="display:flex;gap:20px">
        <div style="flex:0 0 300px">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#96562d;margin-bottom:11px">INBOX - 2</div>
          {inbox}
          <div style="font-family:DM Sans;font-size:13.5px;color:#8a745a;margin-top:6px;line-height:1.4">The deals and invoices you actually need to receive.</div>
        </div>
        <div style="flex:1;background:rgba(200,70,35,.05);border:1px solid rgba(200,70,35,.22);border-radius:18px;padding:16px 18px">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:11px">
            <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#c84623">SPAM - 720</span>
            <span style="font-family:DM Mono;font-size:13px;color:#c84623">reputation shot</span></div>
          {spam}
        </div>
      </div>
      {cap("one cold blast from your root taints every email that domain will ever send.","#8a745a")}</div>'''

# 2. BURNERS - a protected root domain up top, disposable burner domains fanned below via bezier DNA
def burners():
    root=(410,112); burn=[("get-yourco.com",78),("try-yourco.io",254),("yourco-team.com",430),("hey-yourco.com",606)]
    by=336
    edges=""; pills=""
    for dom,x in burn:
        mx=(root[0]+x+72)/2
        edges+=f'<path d="M{root[0]} {root[1]+58} C{mx:.0f} {root[1]+58},{x+72} {by-70},{x+72} {by-38}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Burn the throwaways, not the brand","STEP 01 - DOMAINS")}
      <div style="position:relative;height:456px">
        <svg width="820" height="456" viewBox="0 0 820 456" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="rt" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
          {edges}
          <g filter="url(#rg)"><circle cx="{root[0]}" cy="{root[1]}" r="58" fill="url(#rt)"/></g>
          <g transform="translate({root[0]-16},{root[1]-20})"><rect x="0" y="12" width="32" height="26" rx="5" fill="none" stroke="#1a0f0a" stroke-width="3.4"/><path d="M6 12 V4 a10 10 0 0 1 20 0 v8" fill="none" stroke="#1a0f0a" stroke-width="3.4"/></g>
          <text x="{root[0]}" y="{root[1]+92}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">yourcompany.com</text>
          <text x="{root[0]}" y="{root[1]+114}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">0 cold sends - protected</text>
        </svg>
        {"".join(f'<div style="position:absolute;left:{x}px;top:{by-38}px;width:144px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1.5px solid rgba(255,255,255,.10);border-radius:16px;padding:14px 14px;box-shadow:0 20px 34px rgba(0,0,0,.5)"><div style="font-family:DM Mono;font-weight:500;font-size:14.5px;color:#eae4d8;word-break:break-all">{dom}</div><div style="display:flex;align-items:center;gap:7px;margin-top:9px"><span style="width:8px;height:8px;border-radius:50%;background:#c84623"></span><span style="font-family:DM Sans;font-size:13px;color:#a8a296">disposable</span></div></div>' for dom,x in burn)}
      </div>
      {cap("separate sending domains absorb every filter hit - your root stays clean.")}</div>'''

# 3. FLEET - isometric 3x3 grid of mailbox tiles, each carrying a light per-day send load
def fleet():
    names=["ana@","ben@","cara@","dan@","eve@","finn@","gia@","hugo@","ivy@"]
    tiles=""
    for i,nm in enumerate(names):
        r,c=divmod(i,3); x=c*192; y=r*140
        tiles+=(f'<div style="position:absolute;left:{x}px;top:{y}px;width:172px;height:120px;'
          f'background:linear-gradient(158deg,#3d372f,#26221d);border:1.5px solid rgba(255,255,255,.13);border-radius:16px;'
          f'padding:14px 15px;box-shadow:0 24px 34px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" style="display:block"><rect x="2.5" y="5" width="19" height="14" rx="2.5" fill="none" stroke="rgb({ACC})" stroke-width="2"/><path d="M3 6.5 12 13 21 6.5" fill="none" stroke="rgb({ACC})" stroke-width="2"/></svg>'
          f'<div style="font-family:DM Mono;font-size:14px;color:#eae4d8;margin-top:9px">{nm}</div>'
          f'<div style="display:flex;align-items:center;gap:6px;margin-top:11px">'
          f'<div style="flex:1;height:6px;border-radius:3px;background:rgba(255,255,255,.09);overflow:hidden"><div style="width:26%;height:100%;background:rgb({ACC})"></div></div>'
          f'<span style="font-family:DM Mono;font-size:11.5px;color:rgb({ACC})">4/day</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:38px 44px 40px">
      {htitle("A fleet of inboxes, light on each","STEP 02 - MAILBOXES")}
      <div style="perspective:2100px;height:520px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(24deg) rotateZ(-10deg);width:536px;height:400px;position:relative">{tiles}</div></div>
      {cap("a few sends per inbox per day keeps every mailbox under the filter radar.")}</div>'''

# 4. WARMUP - IVORY area/line chart: sending volume ramps over 30 days as reputation is earned
def warmup():
    days=[(0,5),(1,8),(2,12),(3,17),(4,23),(5,30),(6,38),(7,45)]
    W,H=700,300; x0,y0=54,246; xw,yh=600,208
    mx=45.0
    pts=[(x0+d/7*xw, y0-v/mx*yh) for d,v in days]
    poly=" ".join(f"{x:.0f},{y:.0f}" for x,y in pts)
    area=f"M{x0},{y0} " + " ".join(f"L{x:.0f},{y:.0f}" for x,y in pts) + f" L{x0+xw},{y0} Z"
    dots="".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5.5" fill="#96562d" stroke="#fff" stroke-width="2"/>' for x,y in pts)
    grid="".join(f'<line x1="{x0}" y1="{y0-yh*g/4:.0f}" x2="{x0+xw}" y2="{y0-yh*g/4:.0f}" stroke="rgba(120,95,60,.16)"/>' for g in range(5))
    ticks="".join(f'<text x="{x0+i/3*xw:.0f}" y="{y0+24}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a08a68">D{[1,10,20,30][i]}</text>' for i in range(4))
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Reputation is earned, day by day","STEP 03 - WARMUP","#2a2016","#96562d")}
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:6px">
        <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#2a2016">5</span>
        <svg width="26" height="16" viewBox="0 0 26 16"><path d="M2 8 H22 M16 3 L22 8 L16 13" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#96562d">45</span>
        <span style="font-family:DM Sans;font-size:16px;color:#8a745a">sends / mailbox / day</span></div>
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block">
        <defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(150,86,45,.34)"/><stop offset="100%" stop-color="rgba(150,86,45,0)"/></linearGradient></defs>
        {grid}
        <path d="{area}" fill="url(#ar)"/>
        <polyline points="{poly}" fill="none" stroke="#96562d" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
        {dots}
        <line x1="{x0}" y1="{y0}" x2="{x0+xw}" y2="{y0}" stroke="rgba(120,95,60,.4)" stroke-width="1.5"/>
        {ticks}</svg>
      {cap("volume climbs slowly for weeks while inbox providers learn to trust each mailbox.","#8a745a")}</div>'''

# 5. ROTATION - radial round-robin dial: sends cycle mailbox to mailbox, one lit as "now"
def rotation():
    cx,cy,R=250,232,168; n=6; active=2
    nodes="";
    for i in range(n):
        a=math.radians(-90+i*360/n); x=cx+R*math.cos(a); y=cy+R*math.sin(a); on=(i==active)
        col=f"rgb({ACC})" if on else "rgba(255,255,255,.14)"; fill="#2a2622" if not on else "#3a2c1e"
        glow='filter="url(#ng)"' if on else ""
        nodes+=(f'<g {glow}><circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="{fill}" stroke="{col}" stroke-width="{3 if on else 1.6}"/>'
          f'<svg x="{x-11:.0f}" y="{y-9:.0f}" width="22" height="18" viewBox="0 0 24 20"><rect x="1" y="1" width="22" height="18" rx="2.5" fill="none" stroke="{f"rgb({ACC})" if on else "#8f8f85"}" stroke-width="1.8"/><path d="M1.5 2 12 10 22.5 2" fill="none" stroke="{f"rgb({ACC})" if on else "#8f8f85"}" stroke-width="1.8"/></svg></g>'
          + (f'<text x="{x:.0f}" y="{y+50:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">now</text>' if on else ''))
    # rotation arc arrow
    a0=math.radians(-90+active*360/n-38); a1=math.radians(-90+(active+1)*360/n-14)
    ar=R
    ax0,ay0=cx+ar*math.cos(a0),cy+ar*math.sin(a0); ax1,ay1=cx+ar*math.cos(a1),cy+ar*math.sin(a1)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="500" height="464" viewBox="0 0 500 464">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
        <filter id="ng" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.75"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(212,162,127,.16)" stroke-dasharray="3 8"/>
        <path d="M{ax0:.0f} {ay0:.0f} A{ar} {ar} 0 0 1 {ax1:.0f} {ay1:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>
        <path d="M{ax1:.0f} {ay1:.0f} l-13 -3 l6 12 Z" fill="rgb({ACC})"/>
        {nodes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="56" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-3}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">SEND</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">round-robin</text>
      </svg>
      <div style="flex:1">
        {htitle("No single mailbox ever spikes","STEP 04 - ROTATION")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Every message picks the next inbox in line. Six mailboxes at four sends each is twenty-four a day, and not one of them looks like a blaster.</div>
        {cap("rotate the fleet, never spike a single box.")}</div></div>'''

# 6. AUTH - three DNS records stamped VERIFIED (embossed seal badge each), a red unsigned ghost on top
def auth():
    recs=[("SPF","v=spf1 include:_spf ~all","sender allowed"),
          ("DKIM","v=DKIM1; k=rsa; p=MIGf...","signature valid"),
          ("DMARC","v=DMARC1; p=quarantine","policy enforced")]
    rows=""
    for tag,val,note in recs:
        rays="".join(f'<line x1="20" y1="20" x2="{20+15*math.cos(math.radians(k)):.1f}" y2="{20+15*math.sin(math.radians(k)):.1f}" stroke="rgba(212,162,127,.22)" stroke-width="3"/>' for k in range(0,360,30))
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:15px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="flex-shrink:0;width:74px;font-family:DM Mono;font-weight:500;font-size:15px;letter-spacing:.06em;color:rgb({ACC})">{tag}</div>'
          f'<div style="flex:1;text-align:left"><div style="font-family:DM Mono;font-size:15px;color:#eae4d8;word-break:break-all">{val}</div>'
          f'<div style="font-family:DM Sans;font-size:13.5px;color:#8f8f85;margin-top:2px">{note}</div></div>'
          f'<svg width="40" height="40" viewBox="0 0 40 40" style="flex-shrink:0"><circle cx="20" cy="20" r="17" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
          f'{rays}'
          f'<path d="M13 20.5 l4.5 4.5 L28 14.5" fill="none" stroke="rgb({ACC})" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Signed so the inbox trusts you","STEP 05 - AUTH")}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(250,250,247,.03);border:1px dashed rgba(200,70,35,.30);border-radius:14px;padding:12px 18px;margin-bottom:20px;opacity:.85">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#c84623;flex-shrink:0">UNSIGNED</span>
        <span style="font-family:DM Sans;font-size:17px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">looks spoofed - routed straight to spam</span>
        <span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:#c84623;flex-shrink:0">rejected</span></div>
      <div style="display:flex;flex-direction:column;gap:14px">{rows}</div>
      {cap("the three records that prove you are real, set once and checked on every domain.")}</div>'''

# 7. PLACEMENT - dot field of 1,000 sends, most lit = inbox, a red handful = spam
def placement():
    cols,rowsn=40,25   # 1000
    spam={73,188,241,377,432,559,613,700,744,812,861,903,957,410,520}
    dots=""; cell=15; gap=3
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in spam:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(200,70,35,.85)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" opacity="0.9" filter="url(#lg)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:40px 40px 36px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">98.5%</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:12px">reached the inbox</span></div>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">1,000 SENDS</span></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        {dots}</svg>
      <div style="display:flex;gap:26px;margin-top:16px">
        <div style="display:flex;align-items:center;gap:9px"><span style="width:13px;height:13px;border-radius:4px;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:15px;color:#c9c3b8">inbox</span></div>
        <div style="display:flex;align-items:center;gap:9px"><span style="width:13px;height:13px;border-radius:4px;background:rgba(200,70,35,.85)"></span><span style="font-family:DM Sans;font-size:15px;color:#c9c3b8">spam - 15</span></div>
        {cap("warmed, rotated and signed: the gap between a read and a bounce.")}</div></div>'''

# 8. OPERATOR - the five infra parts converge into one agent orb, held on the operator's tap
def operator():
    parts=[("domains",70,84),("mailboxes",70,192),("warmup",70,300),("rotation",190,138),("auth",190,246)]
    left=""
    for nm,x,y in parts:
        left+=(f'<path d="M{x+30} {y} C340 {y},370 210,520 210" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.75"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One agent runs the sending layer","THE OPERATOR")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="590" cy="210" r="120" fill="url(#bod)"/></g>
        <text x="590" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">SPECTER</text>
        <text x="590" y="230" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".06em">outbound agent</text>
        <path d="M590 330 V372" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>
        <g transform="translate(568,372)"><rect x="0" y="16" width="44" height="34" rx="8" fill="none" stroke="rgb({ACC})" stroke-width="4"/><path d="M8 16 V7 a14 14 0 0 1 28 0 v9" fill="none" stroke="rgb({ACC})" stroke-width="4"/></g>
        <text x="672" y="410" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("Ultron spins the domains, warms the mailboxes and rotates every send - gated by you.")}</div>'''

PANELS={"spam":spam(),"burners":burners(),"fleet":fleet(),"warmup":warmup(),
        "rotation":rotation(),"auth":auth(),"placement":placement(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src30"; os.makedirs(outd,exist_ok=True)
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
