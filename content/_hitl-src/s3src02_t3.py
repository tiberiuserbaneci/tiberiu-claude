#!/usr/bin/env python3
# TIER 3 - BRAND DEALS WITHOUT THE FOLLOWING. Adapted from IG scraped s3src02
# ("3 Websites to Earn tech $$$ from LinkedIn, even under 1,000 followers": Limelight,
# Passionfruit - creator/brand-deal marketplaces). Re-told as Ultron: one operator that
# lands and runs paid B2B brand deals for a small-following founder. Each panel a UNIQUE
# hand-built coded scene in a clean rounded card. NO generic stat-chip strips.
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
RED="rgb(200,70,35)"

# 1. REACH-LIE - split compare: a big empty account (0 deals) vs a small niche account (paid)
def reach():
    def col(foll,label,deals,dealtxt,accent):
        col_c=f"rgb({ACC})" if accent else RED
        ring=f"box-shadow:0 0 34px rgba(212,162,127,.28)" if accent else ""
        badge=("linear-gradient(160deg,#403a33,#241f1a)" if accent else "#241d1b")
        bd=f"rgb({ACC})" if accent else "rgba(200,70,35,.5)"
        return (f'<div style="flex:1;background:{badge};border:1.5px solid {bd};border-radius:22px;padding:26px 24px;{ring}">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{col_c}">{label}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:52px;color:#FAFAF7;line-height:1.05;margin-top:6px">{foll}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-top:2px">followers</div>'
          f'<div style="height:1px;background:rgba(255,255,255,.09);margin:20px 0"></div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:40px;color:{col_c}">{deals}</div>'
          f'<div style="font-family:DM Sans;font-size:16px;color:#c9c3b8;margin-top:2px">{dealtxt}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Reach is not the product","WHO GETS PAID")}
      <div style="display:flex;align-items:stretch;gap:20px;height:400px">
        {col("12,400","THE BIG ACCOUNT","0","brand deals this year",False)}
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px">
          <div style="font-family:DM Mono;font-size:15px;letter-spacing:.2em;color:#6f6a60">VS</div>
        </div>
        {col("900","THE NICHE ACCOUNT","4","live paid deals",True)}
      </div>
      {cap("brands buy a niche audience that trusts you, not a follower count.")}</div>'''

# 2. MATCH-FLOW - bezier routing: three brands -> a FIT gate -> one small creator
def match():
    brands=[("B2B SaaS",96),("Dev tools",210),("Sales AI",324)]
    fx,fy=430,210; cx,cy=740,210
    edges=""; nodes=""
    for nm,y in brands:
        edges+=f'<path d="M196 {y} C320 {y},330 {fy},{fx-46} {fy}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.4"/>'
        nodes+=(f'<rect x="40" y="{y-30}" width="156" height="60" rx="15" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5"/>'
          f'<text x="118" y="{y-4}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#e6e1d6">{nm}</text>'
          f'<text x="118" y="{y+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">wants creators</text>')
    edges+=f'<path d="M{fx+46} {fy} C610 {fy},640 {cy},{cx-64} {cy}" fill="none" stroke="rgb({ACC})" stroke-width="5.5"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Matched on fit, not size","CORTEX MATCH")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="fit" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="fg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#fg)"><rect x="{fx-46}" y="{fy-46}" width="92" height="92" rx="20" fill="url(#fit)" transform="rotate(45 {fx} {fy})"/></g>
        <text x="{fx}" y="{fy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">FIT</text>
        <text x="{fx}" y="{fy+18}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">niche match</text>
        <circle cx="{cx}" cy="{cy}" r="60" fill="#241f1a" stroke="rgb({ACC})" stroke-width="2.5"/>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">You</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="rgb({ACC})">AI niche</text>
      </svg>
      {cap("cortex reads each brief and pitches you only where you actually fit.")}</div>'''

# 3. CAMPAIGN-BOARD - IVORY app board: dense grid of live brand campaigns, follower size open
def board():
    camps=[("Craft.io","Product tooling","LinkedIn","#c8734a"),
           ("ZoomInfo","Sales intel","LinkedIn, News","#c84623"),
           ("HubSpot","Marketing apps","LinkedIn, X","#b8863f"),
           ("LlamaIndex","AI dev tools","Podcasts, Posts","#96562d"),
           ("SurveyMonkey","RevShare","Posts, Video","#a86a3c"),
           ("Thor AI","Creator program","LinkedIn","#c8955a")]
    tiles=""
    for nm,role,ch,c in camps:
        tiles+=(f'<div style="background:rgba(255,255,255,.6);border:1px solid rgba(120,95,60,.18);border-radius:16px;padding:15px 16px">'
          f'<div style="display:flex;align-items:center;gap:10px">'
          f'<div style="width:26px;height:26px;border-radius:8px;background:{c};flex-shrink:0"></div>'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:16px;color:#2a2016">{nm}</span></div>'
          f'<div style="font-family:DM Sans;font-size:13.5px;color:#6a5540;margin-top:9px">{role}</div>'
          f'<div style="display:flex;align-items:center;justify-content:space-between;margin-top:9px">'
          f'<span style="font-family:DM Mono;font-size:11px;color:#8a745a">{ch}</span>'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:12px;color:#fdfbf6;background:#96562d;padding:4px 12px;border-radius:999px">Apply</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Live brand campaigns</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">THE MARKETPLACE</span></div>
      <div style="font-family:DM Sans;font-size:15px;color:#6a5540;margin-bottom:14px">Explore brands actively looking for creators &nbsp;&middot;&nbsp; <span style="color:#96562d;font-weight:700">All follower sizes</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:13px">{tiles}</div>
      {cap("dozens of B2B brands paying creators right now, follower size open.","#8a745a")}</div>'''

# 4. AGENT-LOOP - radial hub-and-spokes: seven agents ringed around one live DEAL
def loop():
    cx,cy,R=410,222,168
    ag=[("CORTEX","find"),("SPECTER","pitch"),("STRIKER","terms"),("PULSE","write"),
        ("AMPLIFY","publish"),("COUNSEL","paper"),("SENTINEL","page")]
    spokes=""; chips=""
    for i,(nm,vb) in enumerate(ag):
        a=-90+i*(360/len(ag))
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2" stroke-dasharray="3 6"/>'
        chips+=(f'<div style="position:absolute;left:{x-64:.0f}px;top:{y-27:.0f}px;width:128px;background:linear-gradient(160deg,#332e28,#221e1a);border:1.5px solid rgba(212,162,127,.3);border-radius:14px;padding:9px 0;text-align:center">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:15px;color:#e6e1d6">{vb}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one deal","THE ROSTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="dl" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="dg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {spokes}
          <g filter="url(#dg)"><circle cx="{cx}" cy="{cy}" r="72" fill="url(#dl)"/></g>
          <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">DEAL</text>
          <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">landed + run</text>
        </svg>
        {chips}
      </div>
      {cap("find, pitch, negotiate, write, publish, paper, page - one operator, seven agents.")}</div>'''

# 5. VOICE-POST - IVORY manuscript: the sponsored post drafted in your voice, brand woven in
def post():
    checks="".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:14px;color:#5a4634">{x}</span></div>' for x in ["your cadence","brand woven in","no ad voice"])
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">The sponsored post, your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PULSE DRAFT</span></div>
      <div style="background:rgba(255,255,255,.7);border:1px solid rgba(120,95,60,.2);border-radius:18px;padding:22px 24px;box-shadow:0 20px 34px rgba(120,95,60,.14)">
        <div style="display:flex;align-items:center;gap:12px">
          <div style="width:44px;height:44px;border-radius:50%;background:linear-gradient(160deg,#c8955a,#96562d)"></div>
          <div><div style="font-family:DM Sans;font-weight:800;font-size:17px;color:#2a2016">You &middot; Founder</div>
          <div style="font-family:DM Mono;font-size:11.5px;color:#8a745a">Promoted &middot; partner post</div></div></div>
        <div style="font-family:DM Sans;font-size:20px;color:#2a2016;line-height:1.5;margin-top:16px">I killed nine tools last month. The one I kept scores every lead before I wake up. That is the whole pitch for <span style="color:#96562d;font-weight:800">their platform</span>, and it is the only ad I would run.</div>
        <div style="display:flex;gap:24px;margin-top:16px;font-family:DM Mono;font-size:12.5px;color:#8a745a"><span>1,204 impressions</span><span>38 saves</span><span>12 comments</span></div>
      </div>
      <div style="display:flex;gap:24px;margin-top:16px">{checks}</div>
      {cap("reads like you, not an ad - banned words enforced on every draft.","#8a745a")}</div>'''

# 6. VERIFIED-GAUGE - ring gauge of verified impressions pulled straight from your profile
def proof():
    pct=82; r=88; circ=2*math.pi*r; dash=circ*pct/100
    chips=[("impressions","41,208"),("saves","372"),("reach","9,140")]
    rows=""
    for lab,val in chips:
        rows+=(f'<div style="display:flex;align-items:center;justify-content:space-between;background:#221f1b;border:1px solid rgba(212,162,127,.22);border-radius:14px;padding:14px 18px">'
          f'<span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">{lab}</span>'
          f'<span style="display:flex;align-items:center;gap:8px"><span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">{val}</span>'
          f'<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg></span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;position:relative;width:236px;height:236px">
        <svg width="236" height="236" viewBox="0 0 236 236">
          <defs><filter id="rg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
          <circle cx="118" cy="118" r="{r}" fill="none" stroke="rgba(212,162,127,.15)" stroke-width="17"/>
          <circle cx="118" cy="118" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="17" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 118 118)" filter="url(#rg)"/></svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;line-height:1">41,208</span>
          <span style="font-family:DM Mono;font-size:11px;color:rgb({ACC});margin-top:4px">verified 30d</span></div></div>
      <div style="flex:1">
        {htitle("Verified stats, auto-pulled","PROOF ENGINE")}
        <div style="display:flex;flex-direction:column;gap:11px">{rows}</div>
        {cap("pulled straight from your profile - verified numbers land bigger deals.")}</div>
      </div>'''

# 7. CONTRACT-SEAL - wax seal + a column of signed term chips (COUNSEL)
def seal():
    terms=[("Scope","1 post + 1 newsletter"),("Usage rights","90 days, paid media"),
           ("Payment","net-15, on publish"),("Kill clause","no exclusivity trap")]
    chips=""
    for lab,val in terms:
        chips+=(f'<div style="background:#221f1b;border:1px solid rgba(212,162,127,.22);border-radius:14px;padding:13px 18px;display:flex;align-items:center;gap:14px">'
          f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<div><div style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:rgb({ACC})">{lab.upper()}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:17px;color:#e6e1d6">{val}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <svg width="230" height="330" viewBox="0 0 230 330" style="flex-shrink:0">
        <defs><radialGradient id="wax" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="wg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="46" y="24" width="150" height="188" rx="12" fill="#242019" stroke="rgba(255,255,255,.1)"/>
        {"".join(f'<rect x="66" y="{48+i*22}" width="{110-i*14}" height="7" rx="3.5" fill="rgba(212,162,127,.28)"/>' for i in range(6))}
        <g filter="url(#wg)"><circle cx="121" cy="236" r="58" fill="url(#wax)"/></g>
        <circle cx="121" cy="236" r="44" fill="none" stroke="#2a160c" stroke-width="2" stroke-dasharray="4 5" opacity=".5"/>
        <text x="121" y="230" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">TERMS</text>
        <text x="121" y="252" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">SEALED</text>
      </svg>
      <div style="flex:1">
        {htitle("The paper, drafted for you","COUNSEL")}
        <div style="display:flex;flex-direction:column;gap:11px">{chips}</div>
        {cap("scope, usage rights, net-15 - reviewed before you ever sign.")}</div>
      </div>'''

# 8. PAYOUT-LEDGER - a ledger of brand payouts (dollars in) against Ultron's cost (cents)
def ledger():
    deals=[("Craft.io","sponsored post","$1,200",0.86),("ZoomInfo","newsletter ad","$800",0.57),
           ("HubSpot","2-post series","$1,500",1.0),("Thor AI","consulting call","$650",0.46)]
    rows=""
    for nm,role,amt,w in deals:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
          f'<div style="width:150px;flex-shrink:0"><div style="font-family:DM Sans;font-weight:800;font-size:17px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:DM Mono;font-size:11.5px;color:#8f8f85">{role}</div></div>'
          f'<div style="flex:1;height:16px;background:rgba(255,255,255,.05);border-radius:8px;overflow:hidden">'
          f'<div style="width:{w*100:.0f}%;height:100%;background:linear-gradient(90deg,#7a4326,rgb({ACC}));border-radius:8px"></div></div>'
          f'<div style="width:92px;text-align:right;font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">{amt}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You earn dollars, it costs cents","THE LEDGER")}
      <div style="margin-top:4px">{rows}</div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:20px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 22px">
        <div><div style="font-family:DM Mono;font-size:11px;letter-spacing:.12em;color:rgb({ACC})">EARNED THIS MONTH</div>
        <div style="font-family:DM Sans;font-weight:900;font-size:38px;color:#FAFAF7">$4,150</div></div>
        <div style="text-align:right"><div style="font-family:DM Mono;font-size:11px;letter-spacing:.12em;color:#8f8f85">ULTRON RAN IT FOR</div>
        <div style="font-family:DM Sans;font-weight:900;font-size:38px;color:rgb({ACC})">31 cents</div></div>
      </div>
      {cap("brands pay you in thousands; ultron runs the whole loop for cents.")}</div>'''

PANELS={"reach":reach(),"match":match(),"board":board(),"loop":loop(),
        "post":post(),"proof":proof(),"seal":seal(),"ledger":ledger()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src02"; os.makedirs(outd,exist_ok=True)
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
