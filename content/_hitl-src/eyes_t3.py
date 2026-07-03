#!/usr/bin/env python3
# TIER 3 model complet pe WIRE ITS EYES - forme complexe din cod (izometrie CSS 3D, graf bezier,
# radar SVG, camp de puncte), finisate. Suprascrie models_clay/eyes/*.png. Cost zero.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"

# shared dark focal card so text always sits on dark mass (reads on cream AND dark slides)
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
# SOFT card for LIGHT/cream slides (operator: contrastul dark-on-cream e prea abrupt) - warm
# espresso charcoal instead of near-black neutral + warm diffuse shadow -> the cream->card jump
# reads intentional, not jarring. Still dark enough for white text. Used on even (light) pages.
CARDL='background:linear-gradient(165deg,#463d34,#332b24);border:1px solid rgba(255,255,255,.09);border-radius:34px;box-shadow:0 40px 66px rgba(74,52,32,.34),0 14px 28px rgba(74,52,32,.26), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.34)'

# 1. JAR - isometric sealed dome over a chip (smart but sightless: closed eye slash)
def jar():
    return f'''<div style="width:900px;{CARDL};padding:44px;text-align:center">
      <div style="perspective:1400px;height:420px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg)">
          <div style="position:relative;width:340px;height:300px;margin:0 auto">
            <div style="position:absolute;left:0;bottom:0;width:340px;height:150px;border-radius:0 0 170px 170px/0 0 60px 60px;
              background:linear-gradient(180deg,#34302c,#141210);box-shadow:inset 0 -10px 24px rgba(0,0,0,.6)"></div>
            <div style="position:absolute;left:20px;top:0;width:300px;height:240px;border-radius:150px 150px 40px 40px/170px 170px 30px 30px;
              background:linear-gradient(145deg,rgba(250,250,247,.16),rgba(250,250,247,.03) 45%,rgba(0,0,0,.2));
              border:1.5px solid rgba(250,250,247,.14);box-shadow:inset 22px 14px 44px rgba(255,255,255,.10)"></div>
            <div style="position:absolute;left:110px;top:96px;width:120px;height:120px;border-radius:50%;
              background:radial-gradient(circle at 38% 32%,rgb({ACC}),#7a4326);box-shadow:0 0 44px rgba({ACC},.5)"></div>
            <div style="position:absolute;left:110px;top:96px;width:120px;height:120px">
              <svg width="120" height="120"><line x1="26" y1="26" x2="94" y2="94" stroke="#1a1210" stroke-width="9" stroke-linecap="round"/></svg></div>
          </div>
        </div>
      </div>
      <div style="font-family:'DM Sans';font-weight:900;font-size:36px;color:#FAFAF7;margin-top:6px">A BRAIN IN A JAR</div>
      <div style="font-family:'DM Mono';font-size:15px;color:#c9a583;letter-spacing:.06em;margin-top:6px">smart, sealed, sightless</div>
    </div>'''

# 2. EYES10 - isometric stack of structured result cards (agent-native search)
# FIX (operator): titlul nu mai sta in spatele stivei; scena 3D e contuinuta, fara overflow/overlap.
def eyes10():
    cards=""
    rows=[("Northwind Robotics","hiring 3 ops roles","92"),
          ("Globex Systems","raised $4M in May","88"),
          ("Initech","no AI layer yet","81")]
    for i,(a,b,c) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:25px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 17px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{c}</span>
            <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">SCORE</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:38px 44px 44px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:8px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">Structured, not blue links</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:rgb({ACC})">AGENT-NATIVE</span></div>
      <div style="perspective:2000px;height:600px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:490px;position:relative">{cards}</div></div>
    </div>'''

# 3. CRAWL - bezier flow: N site nodes converge into one brief
def crawl():
    W,H=820,440
    src=[("competitor.com",90),("pricing page",190),("job board",290),("news feed",390)]
    edges=""; nodes=""
    hubx,huby=650,240
    for nm,y in src:
        mx=(150+hubx)/2
        edges+=f'<path d="M180 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-70} {huby}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=f'''<rect x="40" y="{y-26}" width="150" height="52" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>
          <text x="115" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#c9c3b8">{nm}</text>'''
    return f'''<div style="width:900px;{CARDL};padding:40px">
      <div style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7;margin-bottom:10px">The web becomes briefs</div>
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="72" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">BRIEF</text>
        <text x="{hubx}" y="{huby+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2416">1 page</text>
      </svg></div>'''

# 4. WATCH - radar sweep (concentric rings + conic sweep + glowing blips)
def watch():
    cx,cy,R=230,230,200
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.18)"/>' for r in (66,133,200))
    cross=f'<line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.14)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.14)"/>'
    blips=[("Rival launch",300,150),("Funding news",120,90),("Mention spike",200,175)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
    return f'''<div style="width:900px;{CARD};padding:40px;display:flex;align-items:center;gap:36px">
      <svg width="460" height="460" viewBox="0 0 460 460">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>
        {rings}{cross}
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(60)):.0f} {cy-R*math.cos(math.radians(60)):.0f} Z" fill="url(#sw)"/>
        {bl}
        <circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/>
      </svg>
      <div style="text-align:left">
        <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#FAFAF7;line-height:1.05">Watched<br>on triggers</div>
        <div style="margin-top:20px">{"".join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:14px"><span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.7)"></span><span style="font-family:DM Sans;font-size:18px;color:#d9d5cc">{nm}</span></div>' for nm,_,_ in blips)}</div>
        <div style="font-family:'DM Mono';font-size:14px;color:#9a9488;margin-top:6px">reported in digests, 07:00</div>
      </div></div>'''

# 5. PROOF10 - dot field of 1,284 (a handful lit = live signals today)
def proof10():
    cols,rowsn=48,27  # 1296 ~ 1,284
    lit={137,402,631,888,1045,1190,760}
    dots=""
    cell=15; gap=3
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARDL};padding:40px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">1,284</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">companies, live</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">7 moved today</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="font-family:'DM Mono';font-size:14px;color:#8f8f85;margin-top:14px">hiring, funding, stack changes: this morning's web, not last year's training</div></div>'''

# 6. DIFF10 - citation split (blind guess card vs sighted card with source+date footnotes)
def diff10():
    return f'''<div style="width:900px;display:flex;gap:22px">
      <div style="flex:1;{CARD};padding:32px">
        <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#8f8f85;margin-bottom:16px">BLIND AI</div>
        <div style="font-family:'DM Sans';font-weight:800;font-size:24px;color:#FAFAF7;line-height:1.3">"They probably raised recently."</div>
        <div style="margin-top:22px;font-family:'DM Sans';font-size:16px;color:#8f8f85">no source</div>
        <div style="font-family:'DM Sans';font-size:16px;color:#8f8f85">no date</div>
        <div style="font-family:'DM Sans';font-size:16px;color:#8f8f85">a confident guess</div>
      </div>
      <div style="flex:1;background:linear-gradient(158deg,#d98a63,#8a4630);border-radius:34px;padding:32px;border:1px solid rgba(255,255,255,.16);box-shadow:0 42px 80px rgba(0,0,0,.5)">
        <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgba(255,240,232,.85);margin-bottom:16px">SIGHTED AI</div>
        <div style="font-family:'DM Sans';font-weight:800;font-size:24px;color:#fff;line-height:1.3">"Raised $4M, May 2026."</div>
        <div style="margin-top:22px">
          <div style="background:rgba(255,255,255,.16);border-radius:10px;padding:10px 14px;margin-bottom:10px;font-family:'DM Mono';font-size:13px;color:#fff">techcrunch.com &middot; 2026-05-14</div>
          <div style="background:rgba(255,255,255,.16);border-radius:10px;padding:10px 14px;font-family:'DM Mono';font-size:13px;color:#fff">sec filing &middot; 2026-05-20</div>
        </div>
      </div></div>'''

# 7. SETUP10 - wired board (senses -> hub -> gate), bezier + lock
def setup10():
    W,H=820,420
    senses=[("SEARCH",70),("CRAWL",160),("WATCH",250),("CITE",340)]
    hubx,huby=430,205; gatex=690
    edges=""; nodes=""
    for nm,y in senses:
        edges+=f'<path d="M230 {y} C320 {y},340 {huby},{hubx-64} {huby}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=f'<rect x="60" y="{y-24}" width="170" height="48" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.09)"/><text x="145" y="{y+6}" text-anchor="middle" font-family="DM Mono" font-size="16" letter-spacing="2" fill="#c9c3b8">{nm}</text>'
    edges+=f'<path d="M{hubx+64} {huby} C{(hubx+gatex)/2:.0f} {huby},{(hubx+gatex)/2:.0f} {huby},{gatex-46} {huby}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
    return f'''<div style="width:900px;{CARDL};padding:40px">
      <div style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7;margin-bottom:8px">The senses, wired and gated</div>
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><radialGradient id="h2" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="g2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#g2)"><circle cx="{hubx}" cy="{huby}" r="64" fill="url(#h2)"/></g>
        <text x="{hubx}" y="{huby+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">CORTEX</text>
        <rect x="{gatex-46}" y="{huby-46}" width="92" height="92" rx="20" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>
        <g transform="translate({gatex-22},{huby-22})"><rect x="0" y="18" width="44" height="30" rx="6" fill="none" stroke="rgb({ACC})" stroke-width="3.5"/><path d="M8 18 V10 a14 14 0 0 1 28 0 v8" fill="none" stroke="rgb({ACC})" stroke-width="3.5"/></g>
      </svg>
      <div style="font-family:'DM Mono';font-size:14px;color:#8f8f85">every external move waits for your tap</div></div>'''

# 8. BAR10 - closing statement card with a small radar echo
def bar10():
    return f'''<div style="width:820px;{CARD};padding:44px;text-align:center">
      <svg width="120" height="120" viewBox="0 0 120 120" style="margin-bottom:8px">
        <circle cx="60" cy="60" r="52" fill="none" stroke="rgba(212,162,127,.25)"/><circle cx="60" cy="60" r="34" fill="none" stroke="rgba(212,162,127,.4)"/>
        <circle cx="60" cy="60" r="9" fill="rgb({ACC})"/></svg>
      <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#FAFAF7;line-height:1.1">Ask yours what changed<br>this week.</div>
      <div style="font-family:'DM Sans';font-size:19px;color:#c9a583;margin-top:14px">Watch it guess.</div></div>'''

PANELS={"jar":jar(),"eyes10":eyes10(),"crawl":crawl(),"watch":watch(),
        "proof10":proof10(),"diff10":diff10(),"setup10":setup10(),"bar10":bar10()}

if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/eyes"; os.makedirs(outd,exist_ok=True)
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
