#!/usr/bin/env python3
# TIER 3 - STARTING FROM ZERO, 2026, rebuilt to the WIRE-ITS-EYES bar: each of the 8 panels is a
# UNIQUE hand-built coded scene (pillars / iso-stack / pipeline / dot-field / timeline / gauge /
# ring / control-panel) filling a clean rounded card, title + one mono caption. NO stat-chip strips,
# NO clip-path cuts, NO extruded walls. Warm palette. Ultron cost = cents; high $ only as competitor.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; BAD="200,70,35"; IVA="#96562d"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None):
    tagc=tagc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
      f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink};letter-spacing:-.2px">{t}</span>'
      f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:18px">{t}</div>'

# 1. BARRIER - three standing pillars (the only problems left) + a toppled TECHNICAL slab crossed out
def barrier():
    pills=[("01","NICHE","who exactly you serve, in one line","not a stack"),
           ("02","DISTRIBUTION","how the right people find you","not a language"),
           ("03","CONSISTENCY","showing up every single day","not a framework")]
    cards=""
    for n,nm,desc,foot in pills:
        cards+=(f'<div style="flex:1;background:linear-gradient(165deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.30);'
          f'border-radius:20px;padding:26px 22px 22px;box-shadow:0 30px 48px rgba(0,0,0,.52), inset 0 2px 2px rgba(255,255,255,.09), inset 0 -12px 24px rgba(0,0,0,.4);'
          f'display:flex;flex-direction:column;text-align:left;min-height:318px">'
          f'<div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.18em;color:rgb({ACC})">{n}</div>'
          f'<div style="width:52px;height:52px;border-radius:15px;margin-top:16px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);'
          f'display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M5 21h14"/></svg></div>'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:29px;color:#FAFAF7;margin-top:18px">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:17px;color:#a8a296;line-height:1.42;margin-top:8px">{desc}</div>'
          f'<div style="margin-top:auto;padding-top:16px;font-family:\'DM Mono\';font-size:12.5px;letter-spacing:.06em;color:#7f7a6e">{foot}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("The barrier moved","NOT TECHNICAL")}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);
        border-radius:14px;padding:12px 18px;margin-bottom:20px;opacity:.8">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.16em;color:#7a7468;flex-shrink:0">OLD WALL</span>
        <span style="font-family:'DM Sans';font-size:18px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba({BAD},.75)">"you have to learn to code first"</span>
        <span style="margin-left:auto;font-family:'DM Mono';font-size:12px;color:rgb({BAD});flex-shrink:0">removed</span></div>
      <div style="display:flex;gap:18px">{cards}</div>
      {cap("the only three problems left. none of them are code.")}</div>'''

# 2. BUILD - IVORY iso-stack: one sentence assembles a live landing page from 822 parts
def build():
    layers=[("FOOTER","links, legal",4),("LEAD FORM","name + email",3),("FAQ","6 questions",2),("PRICING","3 tiers",1),("HERO","offer + CTA",0)]
    cards=""
    for nm,sub,i in layers:
        y=i*96
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:520px;background:linear-gradient(160deg,#fffdf8,#efe7d8);'
          f'border:1.5px solid rgba(120,95,60,.22);border-radius:16px;padding:18px 22px;'
          f'box-shadow:0 26px 40px rgba(120,95,60,.24), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(150,86,45,.12);border:1px solid rgba(150,86,45,.28);'
          f'display:flex;align-items:center;justify-content:center;font-family:\'DM Mono\';font-weight:500;font-size:13px;color:{IVA}">{5-i}</div>'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.12em;color:{IVA}">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#2a2016">{sub}</div></div>'
          f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{IVA}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 12.5l3.5 3.5L18 7.5"/></svg></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 36px">
      {htitle("The build is a sentence now","822 PARTS",ink="#17150F",tagc=IVA)}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.2);border-radius:14px;padding:15px 20px;margin-bottom:22px">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:{IVA};flex-shrink:0">YOU TYPE</span>
        <span style="font-family:'DM Sans';font-size:19px;color:#2a2016">"A booking page for a boring niche service."</span></div>
      <div style="perspective:1900px;height:490px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:520px;height:470px;position:relative">{cards}
          <div style="position:absolute;left:96px;top:452px;background:{IVA};color:#fff;font-family:'DM Sans';font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 12px 24px rgba(150,86,45,.4)">Live &#10003; app.51ultron.com</div></div></div>
      {cap("Crescendo assembles the page from 822 parts. You wrote one line.","#8a745a")}</div>'''

# 3. WORKFLOW - trigger orb + a dashed connector into a stack of 3 auto-running actions
def workflow():
    acts=[("FOLLOW-UP","3 emails, spaced by intent","sent"),
          ("DELIVERY","asset dropped to the buyer","shipped"),
          ("REPORTING","opens, replies, revenue logged","logged")]
    rows=""
    for nm,sub,st in acts:
        rows+=(f'<div style="background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:18px;'
          f'padding:20px 22px;margin-bottom:16px;display:flex;align-items:center;gap:18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.32);'
          f'display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center;gap:8px"><span style="width:10px;height:10px;border-radius:50%;background:#7fd39a;box-shadow:0 0 12px rgba(127,211,154,.8)"></span>'
          f'<span style="font-family:\'DM Mono\';font-size:12.5px;color:#8f8f85">{st}</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It runs without you","FLOWS ON TRIGGERS")}
      <div style="display:flex;align-items:center;gap:26px">
        <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center">
          <div style="width:172px;height:172px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#f0c49e,rgb({ACC}) 52%,#7a4326);
            box-shadow:0 0 40px rgba(212,162,127,.35),0 20px 40px rgba(0,0,0,.5), inset 0 3px 6px rgba(255,255,255,.4);
            display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:'DM Sans';font-weight:900;font-size:22px;color:#2a160c;line-height:1">NEW LEAD</span>
            <span style="font-family:'DM Mono';font-size:13px;color:#3a2010;margin-top:4px">02:14 AM</span></div>
          <svg width="30" height="86" viewBox="0 0 30 86"><line x1="15" y1="4" x2="15" y2="66" stroke="rgb({ACC})" stroke-width="3.5" stroke-dasharray="3 9" stroke-linecap="round"/><path d="M6 60l9 12 9-12" fill="none" stroke="rgb({ACC})" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:#8f8f85">no human touched it</span>
        </div>
        <div style="flex:1">{rows}</div>
      </div>
      {cap("a lead lands at 2am; the follow-up, delivery and report happen while you sleep.")}</div>'''

# 4. PROOF/PROBLEM - dot-field of niches (few glamorous lit) + real boring-niche invoice chips
def problem():
    cols,rowsn=26,15
    lit={31,58,97,142,190,233,271,318,355,299}
    dots=""; cell=13; gap=6
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<circle cx="{x+cell/2:.0f}" cy="{y+cell/2:.0f}" r="{cell/2:.0f}" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<circle cx="{x+cell/2:.0f}" cy="{y+cell/2:.0f}" r="{cell/2-2:.0f}" fill="rgba(250,250,247,.10)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    inv=[("Pool-route scheduling","$2,400 / mo"),("HVAC dispatch software","$1,900 / mo"),("Dental billing cleanup","$3,200 / mo")]
    chips=""
    for nm,amt in inv:
        chips+=(f'<div style="display:flex;align-items:center;gap:14px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);'
          f'border-radius:15px;padding:15px 18px;margin-bottom:13px;box-shadow:0 12px 22px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><path d="M4 5h16v14H4z"/><path d="M4 9h16"/></svg>'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#eae4d8">{nm}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:12.5px;color:#8f8f85;margin-top:1px">real invoice, real buyer</div></div>'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:rgb({ACC});flex-shrink:0">{amt}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px;display:flex;gap:32px;align-items:center">
      <div style="flex-shrink:0">
        <div style="font-family:'DM Mono';font-size:12.5px;letter-spacing:.14em;color:#8f8f85;margin-bottom:14px">390 NICHES &middot; <span style="color:rgb({ACC})">10 GLAMOROUS</span></div>
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
          <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>{dots}</svg>
        <div style="font-family:'DM Mono';font-size:12.5px;color:#7f7a6e;margin-top:14px;max-width:{fw}px;line-height:1.5">the lit ten are the crowded, glamorous ones. the other 380 quietly print money.</div>
      </div>
      <div style="flex:1">
        {htitle("Boring niches pay","REAL INVOICES")}
        {chips}
        {cap("pick a problem people already pay for. the unglamorous ones win.")}</div>
    </div>'''

# 5. DAILY - IVORY week timeline: 14 posts planned from one line across 7 days
def daily():
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    kinds=[["hook","proof"],["story","tip"],["hook","hot take"],["proof","story"],["tip","hook"],["recap","story"],["proof","hook"]]
    colw=""
    for d,ks in zip(days,kinds):
        chips=""
        for k in ks:
            chips+=(f'<div style="background:linear-gradient(160deg,#fffdf8,#eee6d6);border:1px solid rgba(120,95,60,.22);border-radius:12px;'
              f'padding:12px 10px;text-align:center;box-shadow:0 10px 18px rgba(120,95,60,.16), inset 0 1.5px 2px rgba(255,255,255,.85)">'
              f'<div style="width:26px;height:26px;border-radius:8px;margin:0 auto 7px;background:rgba(150,86,45,.12);border:1px solid rgba(150,86,45,.28);'
              f'display:flex;align-items:center;justify-content:center"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="{IVA}" stroke-width="2.6" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h10"/></svg></div>'
              f'<div style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.04em;color:#2a2016">{k}</div></div>')
        colw+=(f'<div style="flex:1;display:flex;flex-direction:column;gap:12px">'
          f'<div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IVA};text-align:center">{d}</div>{chips}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 36px">
      {htitle("Show up daily","14 POSTS PLANNED",ink="#17150F",tagc=IVA)}
      <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.2);border-radius:14px;padding:15px 20px;margin-bottom:22px">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:{IVA};flex-shrink:0">ONE LINE IN</span>
        <span style="font-family:'DM Sans';font-size:19px;color:#2a2016">"Plan my week around one boring-niche offer."</span>
        <span style="margin-left:auto;font-family:'DM Sans';font-weight:900;font-size:20px;color:{IVA};flex-shrink:0">14 out</span></div>
      <div style="display:flex;gap:12px;align-items:stretch">{colw}</div>
      {cap("14 posts scheduled from a single line. your only job is to be real on camera.","#8a745a")}</div>'''

# 6. PROFIT - speedometer gauge to year one + a cents-vs-competitor cost readout
def profit():
    cx,cy=250,270; rO=190; rI=150; ticks=""
    for i in range(25):
        a=180-i*7.5; rad=math.radians(a)
        lit=a>=133
        x1=cx+rO*math.cos(rad); y1=cy-rO*math.sin(rad); x2=cx+rI*math.cos(rad); y2=cy-rI*math.sin(rad)
        col=f"rgb({ACC})" if lit else "rgba(212,162,127,.18)"; w=7 if lit else 4
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
    na=math.radians(133); nx=cx+(rI-14)*math.cos(na); ny=cy-(rI-14)*math.sin(na)
    labs=""
    for a,t in [(176,"start"),(133,"YR 1"),(4,"YR 3")]:
        rad=math.radians(a); lx=cx+(rO+22)*math.cos(rad); ly=cy-(rO+22)*math.sin(rad)
        anc="start" if a>90 else ("middle" if a==90 else "end"); anc="middle" if abs(a-90)<50 else anc
        labs+=f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="{anc}" font-family="DM Mono" font-size="14" fill="{"rgb("+ACC+")" if t=="YR 1" else "#8f8f85"}">{t}</text>'
    stats=[("Your cost base","8c","per run",f"rgb({ACC})",False),
           ("Old agency stack","$4,000","per month",f"rgb({BAD})",True),
           ("Your output","1 team","of agents","#FAFAF7",False)]
    scards=""
    for lab,big,sub,col,strike in stats:
        deco="text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)" if strike else ""
        scards+=(f'<div style="background:linear-gradient(160deg,#302c27,#201d1a);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:16px 18px;flex:1;text-align:left">'
          f'<div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#8f8f85">{lab}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:30px;color:{col};margin-top:6px;{deco}">{big}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:14px;color:#8f8f85">{sub}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Profit inside year one","COST = CENTS")}
      <div style="display:flex;align-items:center;gap:26px">
        <svg width="500" height="320" viewBox="0 0 500 320" style="flex-shrink:0">
          {ticks}
          <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>
          <circle cx="{cx}" cy="{cy}" r="14" fill="rgb({ACC})"/>
          <circle cx="{cx}" cy="{cy}" r="14" fill="none" stroke="#1a0f0a" stroke-width="3"/>
          {labs}
          <text x="{cx+52}" y="{cy-30}" text-anchor="start" font-family="DM Sans" font-weight="900" font-size="40" fill="#FAFAF7">Year 1</text>
          <text x="{cx+54}" y="{cy}" text-anchor="start" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb({ACC})">MOST HIT PROFIT HERE</text>
        </svg>
        <div style="flex:1;display:flex;flex-direction:column;gap:14px">{scards}</div>
      </div>
      {cap("cost base in cents, output of a whole team. the maths turns positive fast.")}</div>'''

# 7. TEN - ring of 10 customer nodes sourced by the machine, closed by you at the hub
def ten():
    cx,cy,R=225,225,168
    closed={0,2,5,7}
    nodes=""; spokes=""
    for i in range(10):
        a=math.radians(-90+i*36); x=cx+R*math.cos(a); y=cy+R*math.sin(a); cl=i in closed
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{"rgba(127,211,154,.5)" if cl else "rgba(212,162,127,.4)"}" stroke-width="{3 if cl else 2}"/>'
        fill=f"url(#cl)" if cl else "#241f1a"
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="26" fill="{fill}" stroke="{"rgba(127,211,154,.7)" if cl else "rgba(212,162,127,.5)"}" stroke-width="2" filter="url(#nd)"/>')
        if cl:
            nodes+=f'<path d="M{x-9:.0f} {y+1:.0f}l6 6 12 -13" fill="none" stroke="#0f1a12" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        else:
            nodes+=f'<circle cx="{x:.0f}" cy="{y-3:.0f}" r="6" fill="rgb({ACC})"/><path d="M{x-9:.0f} {y+13:.0f} a9 9 0 0 1 18 0" fill="rgb({ACC})"/>'
    steps=[("Sourced","40 accounts scored"),("Drafted","10 intros written"),("Closed by you","10 handshakes")]
    lst=""
    for a,b in steps:
        lst+=(f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#e6e0d4">{a}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:14px;color:rgb({ACC})">{b}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:28px">
      <svg width="450" height="450" viewBox="0 0 450 450" style="flex-shrink:0">
        <defs>
          <radialGradient id="hub" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <radialGradient id="cl" cx="40%" cy="34%"><stop offset="0%" stop-color="#2b3a2e"/><stop offset="100%" stop-color="#1a241c"/></radialGradient>
          <filter id="nd" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="6" stdDeviation="7" flood-color="rgba(0,0,0,.5)"/></filter>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">10</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">you close</text>
      </svg>
      <div style="flex:1">
        {htitle("Ten customers, ten handshakes","SOURCED &middot; YOU CLOSE")}
        <div>{lst}</div>
        {cap("the machine sources and drafts all ten. you close like a human.")}
      </div></div>'''

# 8. YOURS - control panel: 3 capability toggles (build/run/approve) feeding one gate lock
def yours():
    caps=[("BUILD","pages from a sentence"),("RUN","flows on your triggers"),("APPROVE","every send waits for you")]
    rows=""
    for nm,sub in caps:
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);'
          f'border-radius:16px;padding:18px 20px;margin-bottom:14px;box-shadow:0 12px 24px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.14em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:19px;color:#FAFAF7;margin-top:2px">{sub}</div></div>'
          f'<div style="flex-shrink:0;width:64px;height:34px;border-radius:999px;background:rgba(212,162,127,.2);border:1px solid rgba(212,162,127,.4);'
          f'display:flex;align-items:center;padding:0 4px;justify-content:flex-end">'
          f'<div style="width:26px;height:26px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#f0c49e,rgb({ACC}));box-shadow:0 0 12px rgba(212,162,127,.7)"></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <div style="flex:1">
        {htitle("Build. Run. Approve.","ONE GATE, YOURS")}
        {rows}
      </div>
      <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:16px;
        background:linear-gradient(160deg,#403a33,#211e1a);border:2px solid rgb({ACC});border-radius:26px;padding:34px 30px;
        box-shadow:0 0 40px rgba(212,162,127,.22),0 24px 44px rgba(0,0,0,.5)">
        <svg width="72" height="82" viewBox="0 0 72 82"><rect x="10" y="34" width="52" height="42" rx="10" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M20 34 V22 a16 16 0 0 1 32 0 v12" fill="none" stroke="rgb({ACC})" stroke-width="5"/><circle cx="36" cy="52" r="6" fill="rgb({ACC})"/><line x1="36" y1="58" x2="36" y2="66" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round"/></svg>
        <div style="font-family:'DM Sans';font-weight:900;font-size:22px;color:#FAFAF7;text-align:center;line-height:1.1">Your<br>tap</div>
        <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:rgb({ACC});text-align:center">nothing sends<br>without it</div>
      </div>
    </div>'''

PANELS={"barrier":barrier(),"build":build(),"workflow":workflow(),"problem":problem(),
        "daily":daily(),"profit":profit(),"ten":ten(),"yours":yours()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/zerostart"; os.makedirs(outd,exist_ok=True)
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
