#!/usr/bin/env python3
# TIER 3 - ONE IDEA, TWO HOURS, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. INPUT - a prompt-field mockup (one typed sentence + submit), a dashed funnel arrow into a seed core
def inp():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One sentence in","THE ONLY INPUT")}
      <div style="max-width:772px;margin:0 auto">
        <div style="background:linear-gradient(160deg,#242019,#1a1714);border:1.5px solid rgba(212,162,127,.34);border-radius:20px;padding:22px 26px;box-shadow:0 26px 46px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.06)">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:16px">
            <span style="width:10px;height:10px;border-radius:50%;background:rgb({ACC})"></span>
            <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.16em;color:#9a9488">BRIEF</span>
            <span style="margin-left:auto;font-family:'DM Mono';font-size:13px;color:rgb({ACC})">14:00</span>
          </div>
          <div style="font-family:'DM Sans';font-weight:700;font-size:30px;color:#FAFAF7;line-height:1.32">A service for founders who hate bookkeeping.<span style="display:inline-block;width:3px;height:28px;background:rgb({ACC});margin-left:5px;vertical-align:-4px"></span></div>
          <div style="display:flex;align-items:center;margin-top:22px">
            <span style="font-family:'DM Mono';font-size:13px;color:#8f8f85">9 words &middot; no template</span>
            <div style="margin-left:auto;display:flex;align-items:center;gap:10px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 55%,#9a5a35);border-radius:12px;padding:11px 22px;box-shadow:0 8px 18px rgba(212,162,127,.4)">
              <span style="font-family:'DM Sans';font-weight:900;font-size:16px;color:#1a0f0a">SUBMIT</span>
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </div>
          </div>
        </div>
        <svg width="772" height="158" viewBox="0 0 772 158" style="display:block">
          <defs><radialGradient id="seed" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="sg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
          <path d="M386 8 V72" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 11" stroke-linecap="round"/>
          <path d="M372 60 l14 16 l14 -16" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
          <g filter="url(#sg)"><circle cx="386" cy="116" r="36" fill="url(#seed)"/></g>
          <text x="386" y="122" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">BUILD</text>
        </svg>
      </div>
      {cap("no forms, no wizard, no brief doc. one line, and the afternoon starts building.")}</div>'''

# 2. OFFER - isometric stack of 3 offer cards (positioning / price / guarantee), drafted to the niche
def offer():
    rows=[("POSITIONING","The anti-spreadsheet bookkeeper"),
          ("PRICE","$149 / mo, first month free"),
          ("GUARANTEE","Refund if you touch a spreadsheet")]
    cards=""
    for i,(nm,sub) in enumerate(rows):
        y=i*132
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The offer stands up","DRAFTED TO THE NICHE")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:420px;position:relative">{cards}</div></div>
      {cap("positioning, price and guarantee written against the niche, not a template.")}</div>'''

# 3. PAGE - IVORY browser-window mockup, app.51ultron.com URL bar + hero / pricing / FAQ bands
def page():
    sections=[("HERO","Bookkeeping you never think about","Start free"),
              ("PRICING","$149/mo, first month free","3 tiers"),
              ("FAQ","Do I ever open a spreadsheet? No.","6 answers")]
    bands=""
    for nm,line,meta in sections:
        bands+=(f'<div style="background:rgba(255,255,255,.62);border:1px solid rgba(150,120,80,.2);border-radius:14px;padding:16px 18px;display:flex;align-items:center;gap:16px">'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#96562d;width:78px;flex-shrink:0">{nm}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:19px;color:#2a2016">{line}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;color:#8a745a;flex-shrink:0">{meta}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("The page goes live","IN BRAND TOKENS")}
      <div style="background:linear-gradient(160deg,#f6efe3,#ece1cf);border:1px solid rgba(150,120,80,.24);border-radius:18px;padding:16px;box-shadow:inset 0 2px 4px rgba(255,255,255,.7), 0 20px 40px rgba(120,95,60,.18)">
        <div style="display:flex;align-items:center;gap:9px;padding:8px 12px 16px">
          <span style="width:11px;height:11px;border-radius:50%;background:#d9a58a"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#e0cba0"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#c9b89a"></span>
          <div style="flex:1;margin-left:10px;background:rgba(255,255,255,.78);border:1px solid rgba(150,120,80,.2);border-radius:9px;padding:8px 14px;font-family:DM Mono;font-size:14px;color:#5a4634">app.51ultron.com</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:12px">{bands}</div>
      </div>
      {cap("hero, pricing and FAQ assembled from the pack, styled in your brand tokens.","#8a745a")}</div>'''

# 4. PLAN - a 14-slot content calendar grid (7x2), one slot lit as next-up, 3 hooks + 10:00 each
def plan():
    chips=""; hot=2
    for i in range(14):
        d=i+1; on=(i==hot)
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.08)"
        dcol="#FAFAF7" if on else "#cfc9bd"
        foot=(f'<div style="font-family:DM Mono;font-size:11px;color:rgb({ACC})">next up</div>' if on
              else '<div style="font-family:DM Mono;font-size:11px;color:#6f6a60">10:00</div>')
        chips+=(f'<div style="background:{bg};border:1.5px solid {bd};border-radius:14px;padding:14px 12px;text-align:left">'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:22px;color:{dcol}">#{d:02d}</div>'
          f'<div style="font-family:DM Sans;font-size:12px;color:#8f8f85;margin:2px 0 9px">3 hooks</div>'
          f'{foot}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The content plan lands","14 SLOTS QUEUED")}
      <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:12px">{chips}</div>
      {cap("fourteen posts, three hooks each, queued at 10:00 local and ready to schedule.")}</div>'''

# 5. OUTREACH - 4 trigger-openers (of 20) flow by bezier into a locked GATE (your tap)
def outreach():
    W,H=780,430
    rows=[("hired 3 ops roles",64),("raised $4M in May",154),("entered the US",244),("shipped v2",334)]
    edges=""; chips=""; gx=560; gcy=199
    for note,y in rows:
        edges+=f'<path d="M334 {y} C450 {y},480 {gcy},{gx-8} {gcy}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
        chips+=(f'<rect x="26" y="{y-28}" width="308" height="56" rx="14" fill="#221f1b" stroke="rgba(255,255,255,.09)"/>'
          f'<circle cx="56" cy="{y}" r="6" fill="rgb({ACC})"/>'
          f'<text x="80" y="{y-3}" font-family="DM Mono" font-size="11.5" letter-spacing=".1em" fill="rgb({ACC})">TRIGGER</text>'
          f'<text x="80" y="{y+16}" font-family="DM Sans" font-size="15" fill="#d9d5cc">{note}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Outreach waits at the gate","20 OPENERS PARKED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {edges}{chips}
        <text x="180" y="392" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">+ 16 more openers</text>
        <g filter="url(#gg)"><rect x="{gx}" y="{gcy-95}" width="190" height="190" rx="34" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <g transform="translate({gx+66},{gcy-42})"><rect x="0" y="40" width="58" height="46" rx="10" fill="none" stroke="rgb({ACC})" stroke-width="5.5"/><path d="M11 40 V26 a18 18 0 0 1 36 0 v14" fill="none" stroke="rgb({ACC})" stroke-width="5.5"/></g>
        <text x="{gx+95}" y="{gcy+128}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("twenty openers, one real trigger each, none sent until you release them.")}</div>'''

# 6. REVIEW - a 14:00 -> 16:00 timeline, four milestones checked, the SHIP node glowing at 16:00
def review():
    W,H=800,300; y=150
    stops=[("14:00","idea",80,"start"),("14:20","offer",208,"done"),("14:55","page",356,"done"),
           ("15:30","plan",504,"done"),("15:50","script",636,"done"),("16:00","SHIP",740,"ship")]
    segs=f'<line x1="80" y1="{y}" x2="740" y2="{y}" stroke="rgb({ACC})" stroke-width="4"/>'
    nodes=""
    for t,lbl,x,kind in stops:
        if kind=="ship":
            nodes+=(f'<circle cx="{x}" cy="{y}" r="30" fill="url(#shipg)" filter="url(#sh)"/>'
              f'<path d="M{x-13} {y} l9 9 l17 -20" fill="none" stroke="#2a160c" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<text x="{x}" y="{y-48}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="rgb({ACC})">{lbl}</text>'
              f'<text x="{x}" y="{y+54}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#FAFAF7">{t}</text>')
        elif kind=="done":
            nodes+=(f'<circle cx="{x}" cy="{y}" r="15" fill="#2a2622" stroke="rgb({ACC})" stroke-width="3"/>'
              f'<path d="M{x-7} {y} l5 5 l9 -11" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<text x="{x}" y="{y-30}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#d9d5cc">{lbl}</text>'
              f'<text x="{x}" y="{y+44}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{t}</text>')
        else:
            nodes+=(f'<circle cx="{x}" cy="{y}" r="13" fill="#221f1b" stroke="rgba(255,255,255,.2)" stroke-width="2.5"/>'
              f'<text x="{x}" y="{y-30}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#8f8f85">{lbl}</text>'
              f'<text x="{x}" y="{y+44}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{t}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You review. It ships.","14:00 &rarr; 16:00")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="shipg" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sh" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
        {segs}{nodes}
      </svg>
      {cap("offer, page, plan and script: two hours, one operator, zero meetings.")}</div>'''

# 7. EXCUSE - three excuses struck through in muted red, each killed by a named fact on the right
def excuse():
    rows=[("No team","one operator, seven agents"),
          ("No budget","cents per run, not a salary"),
          ("No time","two hours, start to live")]
    bars=""
    for bad,fix in rows:
        bars+=(f'<div style="display:flex;align-items:center;gap:22px;background:linear-gradient(158deg,#2a2622,#1c1916);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px 24px;box-shadow:inset 0 2px 2px rgba(255,255,255,.06)">'
          f'<span style="width:236px;flex-shrink:0;font-family:DM Sans;font-weight:800;font-size:25px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.9);text-decoration-thickness:3px">{bad}</span>'
          f'<svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(200,70,35,.16)"/><path d="M8 8l8 8M16 8l-8 8" stroke="rgb(200,70,35)" stroke-width="2.4" stroke-linecap="round"/></svg>'
          f'<div style="flex:1;text-align:right"><div style="font-family:DM Mono;font-size:11.5px;letter-spacing:.12em;color:rgb({ACC})">KILLED BY</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7;margin-top:2px">{fix}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("The excuse died here","NONE SURVIVED")}
      <div style="display:flex;flex-direction:column;gap:18px">{bars}</div>
      {cap("no team, no budget, no time: none of the three survived the afternoon.")}</div>'''

# 8. MOAT - IVORY speed gauge (plan -> live), needle near max, plus a fix-time metric and a lock badge
def moat():
    cx,cy,r=150,168,120
    def pt(ang,rr): return (cx+rr*math.cos(math.radians(ang)), cy-rr*math.sin(math.radians(ang)))
    fillend=180-0.88*180
    ex,ey=pt(fillend,r); nx,ny=pt(fillend,98)
    track=f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="20" stroke-linecap="round"/>'
    fill=f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {ex:.1f} {ey:.1f}" fill="none" stroke="#96562d" stroke-width="20" stroke-linecap="round"/>'
    needle=f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#2a2016" stroke-width="6" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="11" fill="#2a2016"/>'
    gsvg=f'''<svg width="320" height="286" viewBox="0 0 320 286" style="overflow:visible">{track}{fill}{needle}
      <text x="{cx-r+6}" y="{cy+32}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#a08a68">PLAN</text>
      <text x="{cx+r-6}" y="{cy+32}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#96562d">LIVE</text>
      <text x="{cx}" y="{cy+78}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="48" fill="#2a2016">2 hrs</text>
      <text x="{cx}" y="{cy+104}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".14em" fill="#96562d">IDEA &rarr; LIVE</text>
    </svg>'''
    m1=('<div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:16px 20px;margin-bottom:14px">'
      '<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#2a2016;line-height:1">&lt; 1 hr</div>'
      '<div style="font-family:DM Sans;font-size:16px;color:#5a4634;margin-top:3px">feedback to a live fix</div></div>')
    m2=('<div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:16px 20px;margin-bottom:14px">'
      '<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#2a2016;line-height:1">0</div>'
      '<div style="font-family:DM Sans;font-size:16px;color:#5a4634;margin-top:3px">meetings to reach launch</div></div>')
    lock=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(150,90,45,.10);border:1px solid rgba(150,90,45,.28);border-radius:12px;padding:15px 18px">'
      f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.4"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11 V8 a4 4 0 0 1 8 0 v3"/></svg>'
      f'<span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#2a2016">The gate keeps the speed safe</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("Speed is the moat","GATE KEEPS IT SAFE")}
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0">{gsvg}</div>
        <div style="flex:1">{m1}{m2}{lock}</div>
      </div>
      {cap("idea to live while rivals still plan; feedback to a fix inside the hour.","#8a745a")}</div>'''

PANELS={"input":inp(),"offer":offer(),"page":page(),"plan":plan(),
        "outreach":outreach(),"review":review(),"excuse":excuse(),"moat":moat()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/twohours"; os.makedirs(outd,exist_ok=True)
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
