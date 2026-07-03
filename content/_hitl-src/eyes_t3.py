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

# 1. JAR - LIGHT construction, built FROM the cream slide bg (operator: "pleaca de la culoarea
# backgroundului in constructia elementului"). Ivory clay card that emerges from the cream page
# with gentle tonal steps + warm soft shadow; dark ink text; the warm brain-chip is the one focal
# accent. No abrupt dark block. (slide 2 only, pending validation)
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def jar():
    # ABSTRACT: luminous atom-core (contained intelligence) inside an ABSTRACT translucent SEAL
    # bubble (no literal jar/knob/base). Object scaled to ~OBJ_FILL of the card width (visual rule:
    # the built element fills the card, not floats small). Mono specimen-label type. cx=310.
    return f'''<div style="width:900px;{CARDIV};padding:38px 40px 34px;text-align:center">
      <div style="display:flex;align-items:center;justify-content:center">
      <svg width="612" height="560" viewBox="0 0 612 560">
        <defs>
          <radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
          <radialGradient id="bloom" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.45)"/><stop offset="58%" stop-color="rgba(204,120,92,.12)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
          <radialGradient id="seal" cx="38%" cy="30%"><stop offset="0%" stop-color="rgba(255,255,255,.20)"/><stop offset="62%" stop-color="rgba(214,222,228,.05)"/><stop offset="100%" stop-color="rgba(200,208,214,.14)"/></radialGradient>
          <filter id="node" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
          <filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="9"/></filter>
        </defs>
        <ellipse cx="306" cy="518" rx="196" ry="26" fill="rgba(120,90,55,.16)" filter="url(#soft)"/>
        <g>
          <circle cx="306" cy="268" r="184" fill="url(#bloom)"/>
          <ellipse cx="306" cy="268" rx="176" ry="66" fill="none" stroke="rgba(204,120,92,.34)" stroke-width="3" transform="rotate(24 306 268)"/>
          <ellipse cx="306" cy="268" rx="176" ry="66" fill="none" stroke="rgba(204,120,92,.28)" stroke-width="3" transform="rotate(-32 306 268)"/>
          <ellipse cx="306" cy="268" rx="176" ry="66" fill="none" stroke="rgba(204,120,92,.22)" stroke-width="3" transform="rotate(84 306 268)"/>
          <circle cx="466" cy="238" r="12" fill="rgb({ACC})" filter="url(#node)"/>
          <circle cx="150" cy="300" r="11" fill="rgb({ACC})" filter="url(#node)"/>
          <circle cx="338" cy="118" r="10" fill="rgb({ACC})" filter="url(#node)"/>
          <circle cx="262" cy="418" r="9" fill="rgb({ACC})" filter="url(#node)"/>
          <circle cx="306" cy="268" r="84" fill="url(#core)"/>
          <ellipse cx="280" cy="238" rx="30" ry="18" fill="rgba(255,255,255,.5)" transform="rotate(-28 280 238)"/>
        </g>
        <circle cx="306" cy="268" r="252" fill="url(#seal)"/>
        <circle cx="306" cy="268" r="252" fill="none" stroke="rgba(255,255,255,.42)" stroke-width="1.5"/>
        <path d="M128 160 A252 252 0 0 1 306 55" fill="none" stroke="rgba(255,255,255,.75)" stroke-width="5" stroke-linecap="round" opacity="0.7"/>
        <path d="M96 250 A252 252 0 0 1 132 156" fill="none" stroke="rgba(255,255,255,.5)" stroke-width="3.5" stroke-linecap="round" opacity="0.55"/>
      </svg>
      </div>
      <div style="font-family:'DM Mono';font-weight:500;font-size:19px;letter-spacing:.34em;color:#4a3f30;margin-top:8px">A BRAIN IN A JAR</div>
      <div style="font-family:'DM Mono';font-weight:400;font-size:12px;letter-spacing:.24em;color:#a08a68;margin-top:9px;text-transform:uppercase">smart &nbsp;&middot;&nbsp; sealed &nbsp;&middot;&nbsp; sightless</div>
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
    return f'''<div style="width:900px;{CARD};padding:40px">
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
    return f'''<div style="width:900px;{CARD};padding:40px">
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

# 7. SETUP10 - premium MOTHERBOARD: chunky 3D sense modules w/ icons + status LEDs, thick glowing
# orthogonal traces + solder joints, a prominent 3D GATE module, CORTEX output. Dense, dimensional
# (operator: circuitul plat era slab). Distinct topology from crawl's radial curves. Black CARD.
def setup10():
    W,H=830,470
    ICON={
      "SEARCH":'<circle cx="0" cy="0" r="9" fill="none" stroke="rgb({A})" stroke-width="3"/><line x1="7" y1="7" x2="15" y2="15" stroke="rgb({A})" stroke-width="3" stroke-linecap="round"/>',
      "CRAWL":'<line x1="-13" y1="0" x2="13" y2="0" stroke="rgb({A})" stroke-width="3"/><line x1="0" y1="-13" x2="0" y2="13" stroke="rgb({A})" stroke-width="3"/><circle cx="0" cy="0" r="4" fill="rgb({A})"/><circle cx="10" cy="-10" r="3" fill="rgb({A})"/><circle cx="-10" cy="10" r="3" fill="rgb({A})"/>',
      "WATCH":'<path d="M-14 0 Q0 -11 14 0 Q0 11 -14 0Z" fill="none" stroke="rgb({A})" stroke-width="3"/><circle cx="0" cy="0" r="4.5" fill="rgb({A})"/>',
      "CITE":'<path d="M-12 -10 h20 a3 3 0 0 1 3 3 v18 a3 3 0 0 1 -3 3 h-20 a3 3 0 0 1 -3 -3 v-18 a3 3 0 0 1 3 -3Z" fill="none" stroke="rgb({A})" stroke-width="2.6"/><line x1="-7" y1="-2" x2="7" y2="-2" stroke="rgb({A})" stroke-width="2.6"/><line x1="-7" y1="5" x2="3" y2="5" stroke="rgb({A})" stroke-width="2.6"/>',
    }
    senses=[("SEARCH",78),("CRAWL",166),("WATCH",254),("CITE",342)]
    busx=452; gatex0=548; gatecy=210; outx=770
    traces=""; joints=""; chips=""
    for nm,y in senses:
        traces+=f'<path d="M300 {y} H{busx} V{gatecy}" fill="none" stroke="rgb({ACC})" stroke-width="3.5" opacity="0.55" filter="url(#tg)"/>'
        joints+=f'<circle cx="{busx}" cy="{y}" r="6" fill="rgb({ACC})" filter="url(#nd)"/>'
        ic=ICON[nm].replace("{A}",ACC)
        chips+=(f'<g><rect x="44" y="{y-33}" width="256" height="66" rx="15" fill="url(#chip)" stroke="rgba(255,255,255,.10)"/>'
                f'<rect x="44" y="{y-33}" width="256" height="66" rx="15" fill="none" stroke="rgba(0,0,0,.4)" stroke-width="1"/>'
                f'<g transform="translate(80,{y})">{ic}</g>'
                f'<text x="116" y="{y+6}" font-family="DM Mono" font-size="17" letter-spacing="2.5" fill="#e2dccf">{nm}</text>'
                f'<circle cx="272" cy="{y}" r="6" fill="#7fd39a" filter="url(#ld)"/></g>')
    return f'''<div style="width:900px;{CARD};padding:38px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">The senses, wired and gated</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">4 / 4 LIVE</span></div>
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs>
          <linearGradient id="chip" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
          <linearGradient id="gate" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#221f1b"/></linearGradient>
          <radialGradient id="outc" cx="36%" cy="30%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1c1a17"/></radialGradient>
          <filter id="tg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter>
          <filter id="nd" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
          <filter id="ld" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#7fd39a" flood-opacity="0.9"/></filter>
          <filter id="gg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter>
        </defs>
        <line x1="{busx}" y1="78" x2="{busx}" y2="342" stroke="rgb({ACC})" stroke-width="3.5" opacity="0.55" filter="url(#tg)"/>
        {traces}
        <path d="M{busx} {gatecy} H{gatex0}" fill="none" stroke="rgb({ACC})" stroke-width="3.5" opacity="0.55" filter="url(#tg)"/>
        {chips}{joints}
        <g filter="url(#gg)"><rect x="{gatex0}" y="{gatecy-62}" width="140" height="124" rx="22" fill="url(#gate)" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <rect x="{gatex0+16}" y="{gatecy-46}" width="108" height="92" rx="14" fill="none" stroke="rgba(255,255,255,.06)"/>
        <g transform="translate({gatex0+45},{gatecy-30})"><rect x="0" y="22" width="50" height="34" rx="7" fill="none" stroke="rgb({ACC})" stroke-width="4"/><path d="M9 22 V13 a16 16 0 0 1 32 0 v9" fill="none" stroke="rgb({ACC})" stroke-width="4"/></g>
        <text x="{gatex0+70}" y="{gatecy+78}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="rgb({ACC})">GATE</text>
        <path d="M{gatex0+140} {gatecy} H{outx-48}" fill="none" stroke="rgb({ACC})" stroke-width="3.5" opacity="0.55" filter="url(#tg)"/>
        <circle cx="{outx}" cy="{gatecy}" r="48" fill="url(#outc)" stroke="rgba(255,255,255,.12)"/>
        <text x="{outx}" y="{gatecy+5}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#e6d6c2">CORTEX</text>
      </svg>
      <div style="font-family:'DM Mono';font-size:14px;color:#8f8f85;margin-top:2px">every external move waits for your tap</div></div>'''

# CTA pill "comment BUILDER" - coded to match the Tier-3 construct (glossy accent pill w/ send)
def cta_pill():
    return f'''<div style="width:760px;height:200px;display:flex;align-items:center;justify-content:center">
      <div style="display:flex;align-items:center;gap:0;border-radius:999px;overflow:hidden;
        box-shadow:0 24px 46px rgba(0,0,0,.45)">
        <div style="display:flex;flex-direction:column;justify-content:center;padding:26px 34px 26px 40px;
          background:linear-gradient(160deg,#2b2824,#1c1a17);border:1px solid rgba(255,255,255,.08);border-right:none">
          <span style="font-family:'DM Mono';font-weight:500;font-size:25px;letter-spacing:.14em;color:rgb({ACC})">COMMENT</span>
          <span style="font-family:'DM Sans';font-weight:900;font-size:46px;color:#FAFAF7;line-height:1;margin-top:4px">BUILDER</span>
        </div>
        <div style="align-self:stretch;display:flex;align-items:center;padding:0 40px;
          background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 55%,#9a5a35);box-shadow:inset 0 2px 3px rgba(255,255,255,.4)">
          <svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </div>
      </div>
    </div>'''

# 8. BAR10 - closing statement card, minimal pulse spark (distinct from watch's radar rings)
def bar10():
    return f'''<div style="width:820px;{CARD};padding:44px;text-align:center">
      <svg width="240" height="70" viewBox="0 0 240 70" style="margin-bottom:14px">
        <path d="M8 46 H70 L86 46 L100 20 L116 60 L132 46 H172" fill="none" stroke="rgb({ACC})" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="200" cy="46" r="9" fill="rgb({ACC})" filter="url(#pl)"/>
        <defs><filter id="pl" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
      </svg>
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
