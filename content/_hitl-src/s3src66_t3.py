#!/usr/bin/env python3
# TIER 3 - BLANK PAGE TO LIVE CAMPAIGN, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
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

# 1. BLANK - IVORY: the empty Ads Manager "Create Campaign" screen, blinking cursor, dead fields, 0 live
def blank():
    fields=[("Campaign name","",True),("Objective","not set",False),("Audience","not set",False),
            ("Creative","0 of 12 uploaded",False),("Daily budget","not set",False)]
    rows=""
    for lab,val,cur in fields:
        inner=(f'<span style="font-family:DM Sans;font-size:19px;color:#2a2016">|</span>' if cur
               else f'<span style="font-family:DM Sans;font-size:18px;color:#b7a98f">{val}</span>')
        rows+=(f'<div style="display:flex;align-items:center;justify-content:space-between;'
          f'background:rgba(255,255,255,.55);border:1.5px solid rgba(150,120,80,.20);border-radius:13px;padding:16px 20px">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.06em;color:#96562d">{lab}</span>{inner}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 40px 34px">
      {htitle("The empty campaign","DAY 3 / STILL BLANK",ink="#2a2016")}
      <div style="background:linear-gradient(160deg,#f6efe4,#ece0cd);border:1px solid rgba(150,120,80,.18);border-radius:20px;padding:22px;box-shadow:inset 0 2px 4px rgba(255,255,255,.7),0 18px 34px rgba(120,95,60,.14)">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px">
          <span style="width:12px;height:12px;border-radius:50%;background:#d9c9ac"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#d9c9ac"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#d9c9ac"></span>
          <span style="font-family:DM Mono;font-size:13px;color:#a08a68;margin-left:8px">ads manager &middot; new campaign</span></div>
        <div style="display:flex;flex-direction:column;gap:12px">{rows}</div>
        <div style="display:flex;align-items:center;justify-content:space-between;margin-top:20px">
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.10em;color:#c84623">DRAFT &middot; NOT PUBLISHED</span>
          <span style="font-family:DM Sans;font-weight:800;font-size:16px;color:#c9b79a;background:rgba(180,160,120,.18);padding:10px 22px;border-radius:999px">Publish</span></div>
      </div>
      {cap("cursor blinking, budget field empty, nothing live. this is where the money leaks.","#8a745a")}</div>'''

# 2. BRIEF - convergence: three input lines (offer / audience / pain) fold into one brief node
def brief():
    W,H=820,440
    src=[("OFFER","what you sell",118),("AUDIENCE","who it is for",240),("PAIN","their #1 frustration",362)]
    edges=""; chips=""; hubx,huby=628,240
    for tag,val,y in src:
        mx=(200+hubx)/2
        edges+=f'<path d="M232 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-72} {huby}" stroke="rgba(212,162,127,.55)" stroke-width="2.6" fill="none"/>'
        chips+=(f'<div style="position:absolute;left:0;top:{y-34}px;width:210px;background:linear-gradient(158deg,#33302b,#211e1a);'
          f'border:1px solid rgba(255,255,255,.10);border-radius:15px;padding:12px 16px;box-shadow:0 14px 26px rgba(0,0,0,.5),inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{tag}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#c9c3b8;margin-top:2px">{val}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Three lines, one brief","OFFER + AUDIENCE + PAIN")}
      <div style="position:relative;height:440px">
        <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
          {edges}
          <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="74" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">BRIEF</text>
          <text x="{hubx}" y="{huby+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2416">1 paste</text>
        </svg>
        {chips}
      </div>
      {cap("no creative team, no deck. paste three lines and the agent reads them like a strategist.")}</div>'''

# 3. FANOUT - dense 4x3 matrix: twelve generated ad-variant cards (4 angles x 3 hooks)
def fanout():
    angles=["PAIN","PROOF","SPEED","PRICE"]
    heads=["Stop the bleed","Booked in a day","Live before lunch"]
    grid=""
    for r,ang in enumerate(angles):
        for c in range(3):
            grid+=(f'<div style="background:linear-gradient(160deg,#33302b,#201d19);border:1px solid rgba(255,255,255,.09);'
              f'border-radius:12px;padding:11px 12px;box-shadow:0 8px 16px rgba(0,0,0,.4)">'
              f'<div style="display:flex;justify-content:space-between;align-items:center">'
              f'<span style="font-family:DM Mono;font-size:9.5px;letter-spacing:.10em;color:rgb({ACC})">{ang}</span>'
              f'<span style="font-family:DM Mono;font-size:9.5px;color:#6f6a60">v{r*3+c+1:02d}</span></div>'
              f'<div style="font-family:DM Sans;font-weight:800;font-size:13.5px;color:#FAFAF7;margin-top:6px;line-height:1.15">{heads[c]}</div>'
              f'<div style="height:4px;background:rgba(250,250,247,.14);border-radius:2px;margin-top:8px"></div>'
              f'<div style="height:4px;width:72%;background:rgba(250,250,247,.10);border-radius:2px;margin-top:5px"></div>'
              f'<div style="margin-top:9px;font-family:DM Sans;font-weight:800;font-size:10px;color:#1a0f0a;background:rgb({ACC});'
              f'display:inline-block;padding:3px 10px;border-radius:999px">Learn more</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Twelve ads, one afternoon","4 ANGLES x 3 HOOKS")}
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">{grid}</div>
      {cap("headline, primary text and CTA on every card. not three ads in two weeks, twelve today.")}</div>'''

# 4. AUDIENCE - concentric targeting rings with segment blips, each creative matched to its audience
def audience():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (64,127,190))
    segs=[("SaaS founders",300,150),("Agency owners",120,100),("E-com ops",205,172),("Consultants",40,120)]
    bl=""
    for nm,ang,dist in segs:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="10" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-17:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    pair=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      '<div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb('+ACC+')">CREATIVE 07</div>'
      '<div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7;margin-top:4px">"Stop the bleed"</div>'
      '<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:12px;display:flex;align-items:center;gap:10px">'
      '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="rgb('+ACC+')" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>'
      '<span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">matched to Agency owners</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(58)):.0f} {cy-R*math.cos(math.radians(58)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("Targeting ships with the ad","AUDIENCE, NOT A GUESS")}
        {pair}
        {cap("each creative is written for a segment, and lands with that audience attached.")}
      </div></div>'''

# 5. VOICE - IVORY gauge: style-match ring + a sample ad written in your voice
def voice():
    pct=96; r=74; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Your offer, your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">VOICE MATCH</span></div>
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
            "You do not need a creative team. You need a good brief and one afternoon."</div>
          <div style="display:flex;gap:22px;margin-top:16px">
            {"".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["your cadence","no hype","your offer"])}
          </div></div>
      </div>
      {cap("sampled from your real copy. banned words and agency fluff stripped on every draft.","#8a745a")}</div>'''

# 6. SPEND - budget ledger: agency 5K retainer crossed out, Ultron cents pacing across 12 variants
def spend():
    bars=[("v01",22),("v02",9),("v03",31),("v04",6),("v05",18),("v06",13),("v07",27),("v08",11),("v09",20),("v10",8),("v11",24),("v12",15)]
    mx=max(v for _,v in bars); cols=""
    for nm,v in bars:
        h=int(30+ (v/mx)*168)
        cols+=(f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:8px">'
          f'<div style="width:34px;height:{h}px;border-radius:8px 8px 4px 4px;background:linear-gradient(180deg,#e6b48f,rgb({ACC}) 60%,#9a5a35);box-shadow:0 8px 16px rgba(212,162,127,.28),inset 0 2px 2px rgba(255,255,255,.4)"></div>'
          f'<span style="font-family:DM Mono;font-size:10px;color:#8f8f85">{nm}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The spend runs on cents","PAY PER TOKEN")}
      <div style="display:flex;align-items:center;gap:16px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);border-radius:14px;padding:13px 18px;margin-bottom:20px;opacity:.82">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#7a7468;flex-shrink:0">AGENCY</span>
        <span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.75)">$5,000 / month retainer</span>
        <span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:#c84623;flex-shrink:0">three ads, two weeks</span></div>
      <div style="display:flex;align-items:flex-end;justify-content:space-between;height:250px;padding:0 6px">{cols}</div>
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-top:14px;border-top:1px solid rgba(255,255,255,.08);padding-top:14px">
        <span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">Twelve variants drafted and paced</span>
        <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">a few cents</span></div>
      {cap("agencies bill a retainer. this bills the tokens it used. cents, not five figures.")}</div>'''

# 7. WINNER - funnel: 12 angles narrow through a test gate into one winning line with lift
def winner():
    W,H=820,450
    top=[80+i*61 for i in range(12)]
    rays=""
    for i,x in enumerate(top):
        rays+=f'<path d="M{x} 66 C{x} 150,410 150,410 210" stroke="rgba(212,162,127,.30)" stroke-width="2" fill="none"/>'
        rays+=f'<rect x="{x-19}" y="40" width="38" height="26" rx="6" fill="#2a2724" stroke="rgba(255,255,255,.09)"/><text x="{x}" y="58" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#9a9488">v{i+1:02d}</text>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Twelve in, one winner out","SPREAD THE BET")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="win" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="wg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {rays}
        <rect x="300" y="196" width="220" height="30" rx="8" fill="#211e1a" stroke="rgba(212,162,127,.4)"/>
        <text x="410" y="216" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".10em" fill="rgb({ACC})">TEST &middot; KILL LOSERS</text>
        <path d="M410 226 L410 300" stroke="rgb({ACC})" stroke-width="4"/>
        <g filter="url(#wg)"><circle cx="410" cy="368" r="72" fill="url(#win)"/></g>
        <text x="410" y="362" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">WINNER</text>
        <text x="410" y="386" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010">v07 &middot; 3.1x</text>
      </svg>
      {cap("run all twelve, cut the flat ones fast, pour budget into the line that actually moves.")}</div>'''

# 8. LIVE - assembled: blank -> creatives + audiences + budget converge into one LIVE campaign, gated
def live():
    parts=[("12 creatives",70,96),("4 audiences",70,210),("budget set",70,324)]
    left=""
    for nm,x,y in parts:
        left+=(f'<path d="M{x+150} {y} C360 {y},400 210,520 210" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
          f'<rect x="{x}" y="{y-27}" width="176" height="54" rx="14" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x+88}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Blank to live before lunch","YOUR TAP SHIPS IT")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="lv" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="lg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#lg2)"><circle cx="590" cy="210" r="118" fill="url(#lv)"/></g>
        <circle cx="640" cy="150" r="12" fill="#7a4326"/><circle cx="640" cy="150" r="7" fill="#f0c49e"/>
        <text x="590" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#1a0f0a">LIVE</text>
        <text x="590" y="230" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010">campaign running</text>
        <text x="590" y="366" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">assembled &middot; gated &middot; yours</text>
      </svg>
      {cap("creatives, audiences and budget become one campaign that waits for your tap, then ships.")}</div>'''

PANELS={"blank":blank(),"brief":brief(),"fanout":fanout(),"audience":audience(),
        "voice":voice(),"spend":spend(),"winner":winner(),"live":live()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src66"; os.makedirs(outd,exist_ok=True)
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
