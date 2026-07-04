#!/usr/bin/env python3
# TIER 3 - THE CLOSING HALF (deal-stage machine: STRIKER runs qualify -> discovery -> objections ->
# proposal -> close plan, human gate at every send). WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. PIPELINE - kanban deal board: 5 stage columns, deal cards with $ value, close column lit
def pipeline():
    stages=[("QUALIFY",[("Northwind","$12K"),("Globex","$6K")]),
            ("DISCOVER",[("Initech","$24K"),("Vandelay","$8K")]),
            ("OBJECTION",[("Acme","$9K"),("Hooli","$22K")]),
            ("PROPOSE",[("Umbrella","$31K"),("Wonka","$15K")]),
            ("CLOSE",[("Stark","$48K"),("Pied Piper","$14K")])]
    cols=""
    for i,(nm,deals) in enumerate(stages):
        lit=(i==len(stages)-1)
        cards=""; tot=0
        for co_,val in deals:
            tot+=int(val.replace("$","").replace("K",""))
            cards+=(f'<div style="background:linear-gradient(160deg,#33302b,#211e1a);border:1px solid rgba(255,255,255,.10);'
                    f'border-radius:12px;padding:12px 13px;box-shadow:0 10px 20px rgba(0,0,0,.45),inset 0 1.5px 2px rgba(255,255,255,.08)">'
                    f'<div style="font-family:DM Sans;font-weight:800;font-size:15px;color:#FAFAF7;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{co_}</div>'
                    f'<div style="font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC});margin-top:3px">{val}</div></div>')
        hc=f"rgb({ACC})" if lit else "#9a9488"
        bd="rgba(212,162,127,.4)" if lit else "rgba(255,255,255,.09)"
        cols+=(f'<div style="flex:1;display:flex;flex-direction:column;gap:11px">'
               f'<div style="text-align:center;font-family:DM Mono;font-size:11px;letter-spacing:.06em;color:{hc};padding-bottom:9px;border-bottom:1.5px solid {bd}">{nm}</div>'
               f'{cards}'
               f'<div style="margin-top:auto;padding-top:6px;text-align:center;font-family:DM Mono;font-size:12px;color:#6f6a60">${tot}K open</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 36px 34px">
      {htitle("Five stages, one desk","DEAL DESK")}
      <div style="display:flex;gap:12px;align-items:stretch">{cols}</div>
      {cap("every open deal walks qualify to close on one board STRIKER keeps live.")}</div>'''

# 2. QUALIFY - fit-score ring gauge + 4 criteria bars (budget, authority, need, timeline)
def qualify():
    pct=84; r=78; circ=2*math.pi*r; dash=circ*pct/100
    crit=[("Budget",90),("Authority",72),("Need",95),("Timeline",68)]
    bars=""
    for nm,v in crit:
        bars+=(f'<div style="margin-bottom:19px">'
          f'<div style="display:flex;justify-content:space-between;margin-bottom:7px">'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#d9d5cc">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">{v}</span></div>'
          f'<div style="height:13px;border-radius:7px;background:rgba(250,250,247,.08);overflow:hidden">'
          f'<div style="width:{v}%;height:100%;border-radius:7px;background:linear-gradient(90deg,#8a4a2c,rgb({ACC}));box-shadow:0 0 14px rgba(212,162,127,.4)"></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:44px">
      <div style="flex-shrink:0;position:relative;width:236px;height:236px">
        <svg width="236" height="236" viewBox="0 0 236 236">
          <defs><filter id="qg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          <circle cx="118" cy="118" r="{r}" fill="none" stroke="rgba(212,162,127,.14)" stroke-width="18"/>
          <circle cx="118" cy="118" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="18" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 118 118)" filter="url(#qg)"/></svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:60px;color:#FAFAF7;line-height:1">{pct}</span>
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:rgb({ACC});margin-top:4px">FIT SCORE</span></div></div>
      <div style="flex:1">
        {htitle("Scored before you spend a minute","QUALIFY")}
        {bars}
        {cap("budget, authority, need, timeline, ranked so you work the live ones.")}</div></div>'''

# 3. DISCOVERY - IVORY notes page: the call becomes ranked pains + an owner each + next step
def discovery():
    pains=[("Reps lose 6h a week to manual research","Ops"),
           ("No single view of the open pipeline","RevOps"),
           ("A proposal takes three days to draft","Sales"),
           ("Deals go quiet right after the demo","Founder")]
    rows=""
    for txt,owner in pains:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;padding:14px 0;border-bottom:1px solid rgba(150,120,80,.18)">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(150,90,45,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:18px;color:#2a2016">{txt}</span>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.05em;color:#96562d;background:rgba(150,90,45,.1);padding:6px 12px;border-radius:8px">{owner}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("It listens, then structures","DISCOVERY")}
      <div style="background:rgba(255,255,255,.55);border-left:4px solid #96562d;border-radius:12px;padding:16px 20px;margin-bottom:18px;font-family:DM Sans;font-size:19px;color:#4a3a28;line-height:1.4">
        "We are not slow at selling. We are slow at everything around the sell."</div>
      {rows}
      {cap("the call becomes ranked pains, an owner each, and the next step. no lost notes.","#8a745a")}</div>'''

# 4. OBJECTION - routing/matching graph: objection nodes -> STRIKER hub -> proven rebuttal nodes
def objection():
    W,H=820,462
    pairs=[("Too expensive","Cents per run"),
           ("No time to switch","Live in a day"),
           ("Already using a tool","Runs beside it"),
           ("Need team buy-in","One-page brief")]
    ys=[74,182,290,398]; hubx,huby=410,236; lx=28; rx=560
    ledges=""; redges=""; ln=""; rn=""
    for (obj,reb),y in zip(pairs,ys):
        m1=(lx+250+hubx)/2; m2=(hubx+rx)/2
        ledges+=f'<path d="M{lx+250} {y} C{m1:.0f} {y},{m1:.0f} {huby},{hubx-52} {huby}" fill="none" stroke="rgba(200,70,35,.42)" stroke-width="2.4"/>'
        redges+=f'<path d="M{hubx+52} {huby} C{m2:.0f} {huby},{m2:.0f} {y},{rx} {y}" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="2.4"/>'
        ln+=(f'<rect x="{lx}" y="{y-27}" width="250" height="54" rx="13" fill="#2a2320" stroke="rgba(200,70,35,.3)"/>'
             f'<circle cx="{lx+24}" cy="{y}" r="5" fill="rgb(200,70,35)"/>'
             f'<text x="{lx+42}" y="{y+6}" font-family="DM Sans" font-weight="600" font-size="17" fill="#d8c8c1">{obj}</text>')
        rn+=(f'<rect x="{rx}" y="{y-27}" width="232" height="54" rx="13" fill="url(#rg)" stroke="rgba(212,162,127,.4)"/>'
             f'<text x="{rx+20}" y="{y+6}" font-family="DM Sans" font-weight="700" font-size="17" fill="#FAFAF7">{reb}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every no already has a yes","OBJECTIONS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="rg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352d"/><stop offset="100%" stop-color="#221f1a"/></linearGradient>
        <radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {ledges}{redges}{ln}{rn}
        <g filter="url(#hg)"><circle cx="{hubx}" cy="{huby}" r="52" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-3}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#1a0f0a">STRIKER</text>
        <text x="{hubx}" y="{huby+17}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">rebuts</text>
      </svg>
      {cap("the objection each deal will raise, matched to your best proven answer.")}</div>'''

# 5. PROPOSAL - IVORY paper document: scope / metric / timeline / terms drafted from discovery
def proposal():
    lines=[("Scope","Outbound plus deal desk for 4 reps"),
           ("Success metric","2x meetings, 30 percent faster close"),
           ("Timeline","Live in 5 business days"),
           ("Terms","Monthly, cancel anytime")]
    rows=""
    for k,v in lines:
        rows+=(f'<div style="display:flex;gap:18px;padding:13px 0;border-bottom:1px solid rgba(150,120,80,.18)">'
          f'<span style="flex-shrink:0;width:150px;font-family:DM Mono;font-size:13px;letter-spacing:.05em;color:#96562d">{k}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:18px;color:#2a2016">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("The proposal builds itself","PROPOSAL")}
      <div style="background:rgba(255,255,255,.55);border:1px solid rgba(150,120,80,.2);border-radius:16px;padding:6px 24px 14px;box-shadow:inset 0 2px 5px rgba(255,255,255,.7)">
        <div style="display:flex;justify-content:space-between;align-items:baseline;padding:16px 0 12px;border-bottom:2px solid rgba(150,90,45,.3)">
          <span style="font-family:DM Sans;font-weight:900;font-size:23px;color:#2a2016">Proposal, Northwind Robotics</span>
          <span style="font-family:DM Mono;font-size:13px;color:#96562d">DRAFT v1</span></div>
        {rows}
        <div style="display:flex;justify-content:space-between;align-items:center;padding-top:16px">
          <span style="font-family:DM Sans;font-weight:700;font-size:16px;color:#5a4634">Pulled from the discovery call</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#96562d">8 min, cents to run</span></div></div>
      {cap("scope, metrics, timeline and terms, drafted from discovery, ready for your edit.","#8a745a")}</div>'''

# 6. CLOSE PLAN - horizontal timeline with dated milestones, first two done, a NOW marker
def closeplan():
    W,H=820,400
    steps=[("Discovery","May 14",True),("Proposal sent","May 16",True),
           ("Legal review","May 21",False),("Signature","May 24",False)]
    n=len(steps); pad=104; span=(W-2*pad)/(n-1); baseY=210
    line=f'<line x1="{pad}" y1="{baseY}" x2="{W-pad}" y2="{baseY}" stroke="rgba(255,255,255,.12)" stroke-width="3"/>'
    prog=f'<line x1="{pad}" y1="{baseY}" x2="{pad+span:.0f}" y2="{baseY}" stroke="rgb({ACC})" stroke-width="4"/>'
    nowx=pad+span*1.5
    nowm=(f'<line x1="{nowx:.0f}" y1="{baseY-30}" x2="{nowx:.0f}" y2="{baseY+30}" stroke="rgba(212,162,127,.5)" stroke-width="2" stroke-dasharray="4 5"/>'
          f'<rect x="{nowx-34:.0f}" y="{baseY-64}" width="68" height="30" rx="8" fill="rgb({ACC})"/>'
          f'<text x="{nowx:.0f}" y="{baseY-44}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#1a0f0a">NOW</text>')
    nodes=""
    for i,(nm,date,done) in enumerate(steps):
        x=pad+i*span
        fill=f"rgb({ACC})" if done else "#2a2724"
        stroke=f"rgb({ACC})" if done else "rgba(255,255,255,.2)"
        glow='filter="url(#ng)"' if done else ""
        datecol=f"rgb({ACC})" if done else "#8f8f85"
        nodes+=f'<circle cx="{x:.0f}" cy="{baseY}" r="16" fill="{fill}" stroke="{stroke}" stroke-width="3" {glow}/>'
        if done: nodes+=f'<path d="M{x-7:.0f} {baseY} l5 5 l9 -11" fill="none" stroke="#1a0f0a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        nodes+=(f'<text x="{x:.0f}" y="{baseY-44}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="{"#FAFAF7" if done else "#9a9488"}">{nm}</text>'
                f'<text x="{x:.0f}" y="{baseY+50}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="{datecol}">{date}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {htitle("A dated path to signed","CLOSE PLAN")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="ng" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        {line}{prog}{nowm}{nodes}</svg>
      {cap("a mutual action plan with dates, so the deal never stalls in the dark.")}</div>'''

# 7. HUMAN GATE - send queue held behind a lock, one operator approve-to-send tap
def gate():
    items=[("Proposal","Northwind Robotics","$12K"),
           ("Quote","Globex Systems","$6K"),
           ("Contract","Initech","$24K")]
    rows=""
    for kind,who,val in items:
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(212,162,127,.22);border-radius:16px;padding:16px 20px;box-shadow:0 14px 26px rgba(0,0,0,.5),inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">'
          f'<svg width="22" height="22" viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2.5" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><path d="M8 10 V7 a4 4 0 0 1 8 0 v3" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{kind} <span style="color:#8f8f85;font-weight:500;font-size:16px">to {who}</span></div>'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb(200,70,35);margin-top:3px">HELD, WAITING FOR YOU</div></div>'
          f'<div style="flex-shrink:0;font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC})">{val}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without you","HUMAN GATE")}
      <div style="display:flex;flex-direction:column;gap:15px">{rows}</div>
      <div style="display:flex;align-items:center;gap:16px;margin-top:22px">
        <div style="flex:1;height:1px;background:rgba(255,255,255,.1)"></div>
        <div style="display:flex;align-items:center;gap:12px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 55%,#9a5a35);border-radius:999px;padding:14px 32px;box-shadow:0 14px 30px rgba(212,162,127,.4),inset 0 2px 3px rgba(255,255,255,.4)">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4 4L19 6"/></svg>
          <span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#1a0f0a">Approve to send</span></div>
        <div style="flex:1;height:1px;background:rgba(255,255,255,.1)"></div></div>
      {cap("proposal, quote, contract: each one parks for your tap before it leaves.")}</div>'''

# 8. CLOSE - dimensional wax SEAL (SIGNED) + a packed stack of close-out receipt chips
def close():
    chips=[("Contract","signed by both sides"),
           ("Terms","locked to the proposal"),
           ("Deal","moved to WON, $48K"),
           ("Memory","written back for the next deal")]
    rows=""
    for k,v in chips:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.1);'
          f'border-radius:14px;padding:13px 17px;box-shadow:0 12px 22px rgba(0,0,0,.45),inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:13px;letter-spacing:.05em;color:rgb({ACC});width:78px">{k}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:17px;color:#d9d5cc">{v}</span></div>')
    spokes="".join(f'<line x1="145" y1="145" x2="{145+128*math.cos(math.radians(a)):.0f}" y2="{145+128*math.sin(math.radians(a)):.0f}" stroke="#8a4c2c" stroke-width="10"/>' for a in range(0,360,15))
    seal=f'''<svg width="278" height="278" viewBox="0 0 290 290">
        <defs>
          <radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <radialGradient id="sbloom" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.5)"/><stop offset="62%" stop-color="rgba(204,120,92,.10)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
          <filter id="ssh" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="rgba(0,0,0,.6)"/></filter>
          <filter id="spec" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="8"/></filter></defs>
        <circle cx="145" cy="145" r="140" fill="url(#sbloom)"/>
        <g filter="url(#ssh)">{spokes}<circle cx="145" cy="145" r="118" fill="url(#seal)"/></g>
        <circle cx="145" cy="145" r="118" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
        <circle cx="145" cy="145" r="96" fill="none" stroke="rgba(26,15,10,.28)" stroke-width="2"/>
        <path d="M96 150 q22 -30 40 -6 q10 14 24 -2 q14 -18 34 4" fill="none" stroke="#1a0f0a" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
        <ellipse cx="110" cy="98" rx="44" ry="24" fill="rgba(255,255,255,.28)" filter="url(#spec)" transform="rotate(-32 110 98)"/>
        <text x="145" y="214" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="20" letter-spacing="5" fill="#1a0f0a">SIGNED</text>
      </svg>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:32px">
      <div style="flex-shrink:0;display:flex;align-items:center;justify-content:center">{seal}</div>
      <div style="flex:1">
        {htitle("Closed, and logged","THE CLOSE")}
        <div style="display:flex;flex-direction:column;gap:12px">{rows}</div>
        {cap("signature, terms and the win written back to memory for the next deal.")}</div></div>'''

PANELS={"pipeline":pipeline(),"qualify":qualify(),"discovery":discovery(),"objection":objection(),
        "proposal":proposal(),"closeplan":closeplan(),"gate":gate(),"close":close()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src50"; os.makedirs(outd,exist_ok=True)
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
