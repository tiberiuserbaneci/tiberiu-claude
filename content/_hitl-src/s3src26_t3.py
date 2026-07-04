#!/usr/bin/env python3
# TIER 3 - MAX ONLY WHEN IT COUNTS. Adaptare IG "Claude Max plan" -> Ultron: seat-ul flat
# factureaza inteligenta maxima pe fiecare tura, ROUTER-ul cumpara tier-ul potrivit per tura,
# in centi. 8 scene bespoke pe bara WIRE-ITS-EYES, card rotunjit curat, titlu + un cap. Cost zero.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. FLAT SEAT - invoice/ledger, every turn billed MAX, struck 6-month total, red peak bar
def flatseat():
    rows=[("quick fact lookup","billed MAX"),("format one caption","billed MAX"),
          ("draft a follow-up","billed MAX"),("one hard deal call","billed MAX")]
    rh=""
    for a,b in rows:
        rh+=(f'<div style="display:flex;justify-content:space-between;align-items:center;'
             f'padding:15px 4px;border-bottom:1px solid rgba(255,255,255,.06)">'
             f'<span style="font-family:DM Sans;font-size:19px;color:#c9c3b8">{a}</span>'
             f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({RED})">{b}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You paid peak on every turn","FLAT MAX SEAT")}
      <div style="background:#211d19;border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:8px 24px 22px">
        <div style="display:flex;justify-content:space-between;align-items:baseline;padding:16px 4px 10px;border-bottom:1.5px solid rgba(212,162,127,.25)">
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC})">PREMIUM INVOICE</span>
          <span style="font-family:DM Mono;font-size:13px;color:#8f8f85">one flat seat</span></div>
        {rh}
        <div style="display:flex;justify-content:space-between;align-items:center;padding:22px 4px 6px">
          <span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">6-month total</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:rgb({RED});text-decoration:line-through;text-decoration-thickness:3px">$1,200</span></div>
      </div>
      <div style="margin-top:16px;height:26px;border-radius:8px;background:linear-gradient(90deg,rgba(200,70,35,.85),rgba(200,70,35,.45));display:flex;align-items:center;padding:0 16px">
        <span style="font-family:DM Mono;font-size:12.5px;letter-spacing:.12em;color:#fff">PEAK INTELLIGENCE - BILLED 24/7</span></div>
      {cap("maximum model on a lookup that needed almost none. that is the flat seat.")}</div>'''

# 2. THREE TIERS - isometric stack of Lite / Smart / Deep, cents + capability bar
def tiers():
    data=[("LITE","Haiku","quick lookups","0.02c",0.30),
          ("SMART","Sonnet","daily execution","0.11c",0.62),
          ("DEEP","Opus","hard judgement","0.40c",1.0)]
    cards=""
    for i,(nm,mdl,role,cost,fill) in enumerate(data):
        y=i*132; barw=int(180*fill)
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:22px">'
          f'<div style="flex:1"><div style="display:flex;align-items:baseline;gap:12px"><span style="font-family:DM Mono;font-size:15px;letter-spacing:.14em;color:rgb({ACC})">{nm}</span><span style="font-family:DM Sans;font-size:15px;color:#8f8f85">{mdl}</span></div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7;margin-top:3px">{role}</div>'
          f'<div style="margin-top:10px;height:9px;width:180px;border-radius:6px;background:rgba(255,255,255,.08)"><div style="height:9px;width:{barw}px;border-radius:6px;background:rgb({ACC})"></div></div></div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7">{cost}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Three tiers, the cheapest that fits","MODEL TIERS")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(19deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}</div></div>
      {cap("lite for lookups, smart for daily work, deep only for the hard calls.")}</div>'''

# 3. ROUTER - job chip -> ROUTER hub -> 3 tier nodes, SMART lit/picked (bezier flow)
def router():
    hx,hy=250,235; nx=530
    tiers_=[("LITE","lookups","0.02c",118,False),("SMART","daily","0.11c",235,True),("DEEP","hard call","0.40c",352,False)]
    edges="";nodes=""
    for nm,role,cost,y,on in tiers_:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.26)"; w=6 if on else 2.5
        edges+=f'<path d="M{hx+72} {hy} C400 {hy},430 {y},{nx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        fill="#3a332c" if on else "#221f1b"; bd=f"rgb({ACC})" if on else "rgba(255,255,255,.10)"
        tick=f'<text x="{nx+188}" y="{y+30}" text-anchor="end" font-family="DM Mono" font-size="12" fill="rgb({ACC})">picked</text>' if on else ''
        nodes+=(f'<rect x="{nx}" y="{y-38}" width="210" height="76" rx="16" fill="{fill}" stroke="{bd}" stroke-width="{2.4 if on else 1.4}"/>'
          f'<text x="{nx+20}" y="{y-8}" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="{"#FAFAF7" if on else "#9a9488"}">{nm}</text>'
          f'<text x="{nx+20}" y="{y+16}" font-family="DM Sans" font-size="15" fill="#8f8f85">{role}</text>'
          f'<text x="{nx+190}" y="{y-2}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">{cost}</text>{tick}')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The router picks the tier","PER TURN")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <rect x="20" y="{hy-34}" width="150" height="68" rx="15" fill="#211d19" stroke="rgba(255,255,255,.10)"/>
        <text x="95" y="{hy-6}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">draft 12</text>
        <text x="95" y="{hy+14}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">follow-ups</text>
        <path d="M170 {hy} H{hx-72}" stroke="rgba(212,162,127,.4)" stroke-width="3"/>
        {edges}
        <g filter="url(#hg)"><rect x="{hx-72}" y="{hy-58}" width="144" height="116" rx="26" fill="url(#hub)"/></g>
        <text x="{hx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ROUTER</text>
        <text x="{hx}" y="{hy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        {nodes}</svg>
      {cap("plain english in, the cheapest tier that can actually do it - never you.")}</div>'''

# 4. TOKEN METER - IVORY ring gauge, cents this turn + recent turns priced in cents
def meter():
    r=80; circ=2*math.pi*r; dash=circ*0.16
    chips=[("lite lookup","0.02c"),("caption draft","0.09c"),("deep deal call","0.40c")]
    ch="".join(f'<div style="display:flex;justify-content:space-between;background:rgba(255,255,255,.55);border-radius:12px;padding:12px 16px"><span style="font-family:DM Sans;font-size:17px;color:#5a4634">{a}</span><span style="font-family:DM Mono;font-size:16px;color:#96562d">{b}</span></div>' for a,b in chips)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">You pay per turn, in cents</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">TOKEN METER</span></div>
      <div style="display:flex;align-items:center;gap:36px">
        <div style="flex-shrink:0;position:relative;width:210px;height:210px">
          <svg width="210" height="210" viewBox="0 0 210 210">
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="16"/>
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="#96562d" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 105 105)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016">0.11c</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d">this turn</span></div></div>
        <div style="flex:1;display:flex;flex-direction:column;gap:12px">{ch}</div>
      </div>
      {cap("no flat seat. a deep turn is cents, a lite lookup a fraction of one.","#8a745a")}</div>'''

# 5. ESCALATE - balance scale: routine turn on SMART (up), hard call tips to DEEP (down, glow)
def deep():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Max fires only when it counts","ESCALATE")}
      <svg width="700" height="450" viewBox="0 0 700 450" style="display:block;margin:0 auto">
        <defs><radialGradient id="dg" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="dgl" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <rect x="344" y="150" width="12" height="222" rx="6" fill="#3a352e"/>
        <rect x="298" y="366" width="104" height="16" rx="8" fill="#2b2723"/>
        <line x1="168" y1="126" x2="532" y2="176" stroke="url(#dg)" stroke-width="15" stroke-linecap="round"/>
        <circle cx="350" cy="151" r="15" fill="#241f1a" stroke="rgb({ACC})" stroke-width="3"/>
        <line x1="168" y1="128" x2="168" y2="238" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>
        <line x1="532" y1="178" x2="532" y2="292" stroke="rgb({ACC})" stroke-width="3"/>
        <rect x="78" y="238" width="180" height="74" rx="16" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>
        <text x="168" y="270" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#8f8f85">ROUTINE TURN</text>
        <text x="168" y="296" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#c9c3b8">SMART</text>
        <g filter="url(#dgl)"><rect x="442" y="292" width="180" height="82" rx="16" fill="#3a332c" stroke="rgb({ACC})" stroke-width="2.4"/></g>
        <text x="532" y="326" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">HARD JUDGEMENT</text>
        <text x="532" y="354" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#FAFAF7">DEEP</text>
      </svg>
      {cap("routine stays on smart. a hard call tips the beam and escalates to opus.")}</div>'''

# 6. ROSTER - radial hub-and-spokes, ROUTER core + 7 named agent nodes
def roster():
    cx,cy,R=306,225,168
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    spokes="";nodes=""
    for i,(nm,role) in enumerate(agents):
        a=-90+i*(360/7)
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" letter-spacing=".03em" fill="#e7e2d8">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Sans" font-size="12.5" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one router","THE ROSTER")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="rh" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#rg)"><circle cx="{cx}" cy="{cy}" r="52" fill="url(#rh)"/></g>
        <text x="{cx}" y="{cy-3}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">picks + tiers</text>
        {nodes}</svg>
      {cap("cortex, specter, striker, pulse, sentinel, amplify, counsel - each owns a job.")}</div>'''

# 7. HUMAN GATE - IVORY parchment, wax seal + held-item receipt chips
def gate():
    items=[("Cold email","SPECTER"),("Proposal","STRIKER"),("Pull request","SENTINEL"),("NDA","COUNSEL")]
    ch="".join(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.55);border-radius:14px;padding:12px 16px">'
       f'<div style="width:34px;height:34px;border-radius:9px;background:rgba(150,90,45,.14);border:1px solid rgba(150,90,45,.3);display:flex;align-items:center;justify-content:center">'
       f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.6"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div>'
       f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#2a2016">{a}</div><div style="font-family:DM Mono;font-size:12px;color:#8a745a">{b} - waiting</div></div>'
       f'<span style="font-family:DM Mono;font-size:12px;color:#96562d">tap</span></div>' for a,b in items)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Nothing sends without your tap</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">HUMAN GATE</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:210px;height:210px">
          <svg width="210" height="210" viewBox="0 0 210 210">
            <defs><radialGradient id="wax" cx="40%" cy="34%"><stop offset="0%" stop-color="#c98a5f"/><stop offset="60%" stop-color="#96562d"/><stop offset="100%" stop-color="#6d3c1c"/></radialGradient></defs>
            <circle cx="105" cy="105" r="82" fill="url(#wax)"/>
            <circle cx="105" cy="105" r="68" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="2" stroke-dasharray="3 6"/>
            <path d="M76 104 l19 19 l40 -44" fill="none" stroke="#fbeadd" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
            <text x="105" y="152" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".18em" fill="#fbeadd">APPROVED</text></svg></div>
        <div style="flex:1;display:flex;flex-direction:column;gap:11px">{ch}</div>
      </div>
      {cap("cold emails, deals, code and contracts all park for one human tap.","#8a745a")}</div>'''

# 8. CONTEXT - horizontal compare: flat model window (red, truncated) vs Ultron vault (long, loaded)
def memory():
    recs=["ICP","pipeline","pricing","docs","past turns","objections"]
    rc="".join(f'<span style="font-family:DM Mono;font-size:13px;color:#2a160c;background:rgb({ACC});border-radius:8px;padding:6px 12px">{r}</span>' for r in recs)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("A short window forgets, the vault does not","CONTEXT")}
      <div style="display:flex;flex-direction:column;gap:26px;margin-top:8px">
        <div>
          <div style="display:flex;justify-content:space-between;margin-bottom:10px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({RED})">FLAT MODEL WINDOW</span><span style="font-family:DM Mono;font-size:12px;color:#8f8f85">clears each session</span></div>
          <div style="display:flex;align-items:center;gap:12px">
            <div style="height:46px;width:230px;border-radius:12px;background:linear-gradient(90deg,rgba(200,70,35,.5),rgba(200,70,35,.14));border:1px solid rgba(200,70,35,.4)"></div>
            <span style="font-family:DM Mono;font-size:13px;color:rgb({RED})">truncated</span></div>
        </div>
        <div>
          <div style="display:flex;justify-content:space-between;margin-bottom:10px"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">ULTRON VAULT</span><span style="font-family:DM Mono;font-size:12px;color:#8f8f85">always loaded</span></div>
          <div style="height:120px;border-radius:16px;background:#211d19;border:1px solid rgba(212,162,127,.32);padding:18px 20px;display:flex;flex-wrap:wrap;gap:10px;align-content:center">{rc}</div>
        </div>
      </div>
      {cap("icp, pipeline, pricing and docs stay loaded, so every turn starts warm.")}</div>'''

PANELS={"flatseat":flatseat(),"tiers":tiers(),"router":router(),"meter":meter(),
        "deep":deep(),"roster":roster(),"gate":gate(),"memory":memory()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src26"; os.makedirs(outd,exist_ok=True)
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
