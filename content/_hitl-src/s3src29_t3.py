#!/usr/bin/env python3
# TIER 3 - THE STARTER LOADOUT (adapted from IG s3src29 "24 things to install in Ultron").
# Angle: the exact day-one kit shown as THREE DISTINCT LAYERS - skills=recipes, plug-ins=crews,
# MCP=connectors. Each panel a UNIQUE hand-built coded scene filling a clean rounded card,
# title + one-line caption, NO generic stat-chip strips. Warm palette only.
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
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC});white-space:nowrap;padding-left:16px">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

def gicon(kind,col=None,sz=26):
    a=col or f"rgb({ACC})"
    if kind=="recipe":
        return f'<svg width="{sz}" height="{sz}" viewBox="0 0 24 24" fill="none" stroke="{a}" stroke-width="2.1" stroke-linecap="round"><path d="M5 6h11M5 12h11M5 18h7"/><path d="M18.5 9l3 3-3 3"/></svg>'
    if kind=="crew":
        return f'<svg width="{sz}" height="{sz}" viewBox="0 0 24 24" fill="none" stroke="{a}" stroke-width="2.1" stroke-linecap="round"><circle cx="12" cy="6.5" r="2.7"/><circle cx="5.5" cy="17" r="2.7"/><circle cx="18.5" cy="17" r="2.7"/><path d="M12 9.2v3.3M9.6 15.2l-2 1M14.4 15.2l2 1"/></svg>'
    if kind=="cable":
        return f'<svg width="{sz}" height="{sz}" viewBox="0 0 24 24" fill="none" stroke="{a}" stroke-width="2.1" stroke-linecap="round"><path d="M3 12h6"/><rect x="9" y="7.5" width="7" height="9" rx="2"/><path d="M16 10h2.5M16 14h2.5M18.5 8.5v7"/></svg>'
    return ""

# 1. LOADOUT - three shelf rows (SKILLS / PLUG-INS / MCP), each 8 slotted tiles: the day-one rack
def loadout():
    layers=[("SKILLS","recipe","8 recipes"),("PLUG-INS","crew","8 crews"),("MCP","cable","8 connectors")]
    rows=""
    for nm,kind,sub in layers:
        tiles="".join(f'<div style="width:66px;height:66px;border-radius:15px;background:linear-gradient(160deg,#332f2a,#201d1a);border:1px solid rgba(255,255,255,.09);box-shadow:inset 0 2px 2px rgba(255,255,255,.07),0 10px 18px rgba(0,0,0,.42);display:flex;align-items:center;justify-content:center">{gicon(kind)}</div>' for _ in range(8))
        rows+=f'''<div style="display:flex;align-items:center;gap:22px;margin-bottom:20px">
          <div style="width:158px;flex-shrink:0">
            <div style="font-family:'DM Sans';font-weight:900;font-size:23px;color:#FAFAF7">{nm}</div>
            <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC});margin-top:2px">{sub}</div></div>
          <div style="display:flex;gap:13px">{tiles}</div></div>'''
    return f'''<div style="width:900px;{CARD};padding:38px 40px 34px">
      {htitle("Your day-one loadout","8 + 8 + 8")}
      <div style="margin-top:6px">{rows}</div>
      {cap("twenty-four installs, three layers, nothing else on day one.")}</div>'''

# 2. LAYERS - IVORY triptych: what each layer IS (recipe / crew / cable)
def layers():
    cols=[("recipe","SKILL","a recipe","one short command runs a whole workflow"),
          ("crew","PLUG-IN","a crew","one install drops a full team of tools"),
          ("cable","MCP SERVER","a cable","a live connector into your real apps")]
    cc=""
    for i,(kind,nm,tagw,desc) in enumerate(cols):
        cc+=f'''<div style="flex:1;text-align:center;padding:0 12px">
          <div style="width:98px;height:98px;margin:0 auto 18px;border-radius:24px;background:rgba(255,255,255,.62);border:1px solid rgba(150,90,45,.20);box-shadow:0 14px 26px rgba(120,95,60,.16),inset 0 2px 3px rgba(255,255,255,.9);display:flex;align-items:center;justify-content:center">{gicon(kind,"#96562d",46)}</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#2a2016">{nm}</div>
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:#96562d;margin-top:5px">= {tagw.upper()}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#5a4634;margin-top:12px;line-height:1.42">{desc}</div></div>'''
        if i<2: cc+='<div style="width:1px;align-self:stretch;background:rgba(150,120,80,.22)"></div>'
    return f'''<div style="width:900px;{CARDIV};padding:38px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:28px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Skill, plug-in, server</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">THE THREE LAYERS</span></div>
      <div style="display:flex;align-items:flex-start;gap:10px;margin:12px 0 6px">{cc}</div>
      {cap("a recipe, a crew, a cable. know which one you are adding.","#8a745a")}</div>'''

# 3. SKILLS - row of 8 command chips, /brief lit and expanding into a 4-step recipe pipeline
def skills():
    cmds=["/brief","/sequence","/discovery","/post","/ship","/schedule","/nda","/digest"]
    chips=""
    for c in cmds:
        on=c=="/brief"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.10)"
        bg="rgba(212,162,127,.14)" if on else "rgba(255,255,255,.03)"
        col="#FAFAF7" if on else "#b0aa9e"
        glow="box-shadow:0 0 20px rgba(212,162,127,.35);" if on else ""
        chips+=f'''<div style="{glow}background:{bg};border:1.5px solid {bd};border-radius:11px;padding:11px 15px;font-family:'DM Mono';font-size:16px;color:{col}">{c}</div>'''
    steps=[("find",190),("enrich",352),("rank",514)]
    stepsvg=""
    for nm,x in steps:
        stepsvg+=(f'<rect x="{x}" y="90" width="140" height="56" rx="14" fill="linear-gradient(160deg,#3a352f,#241f1a)"/>'
          f'<rect x="{x}" y="90" width="140" height="56" rx="14" fill="#2b2723" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x+70}" y="124" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="19" fill="#e6e0d4">{nm}</text>')
    arrows=""
    for ax in (166,328,490,652):
        arrows+=f'<path d="M{ax} 118 h20" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round"/><path d="M{ax+15} 111 l7 7 -7 7" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("One word runs the recipe","8 SKILLS")}
      <div style="display:flex;flex-wrap:wrap;gap:11px;margin-bottom:26px">{chips}</div>
      <svg width="820" height="236" viewBox="0 0 820 236">
        <defs><radialGradient id="out3" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og3" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="10" y="88" width="146" height="60" rx="15" fill="rgba(212,162,127,.14)" stroke="rgb({ACC})" stroke-width="1.8"/>
        <text x="83" y="115" text-anchor="middle" font-family="DM Mono" font-size="18" fill="#FAFAF7">/brief</text>
        <text x="83" y="136" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="rgb({ACC})">1 command</text>
        {stepsvg}{arrows}
        <g filter="url(#og3)"><circle cx="734" cy="118" r="58" fill="url(#out3)"/></g>
        <text x="734" y="113" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">brief</text>
        <text x="734" y="134" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">1 page</text>
      </svg>
      {cap("/brief becomes find, enrich, rank, write. a workflow behind each shortcut.")}</div>'''

# 4. PLUGINS - radial burst: one install (gstack) explodes into a whole crew of member tools
def plugins():
    cx,cy=306,236; rx,ry=196,158
    members=["deploy","test","review","migrate","lint","docs","api","ui","auth","db"]
    spokes=""; nodes=""
    n=len(members)
    for i,m in enumerate(members):
        a=math.radians(i*(360/n)-90)
        x=cx+rx*math.cos(a); y=cy+ry*math.sin(a)
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#cfc9bd">{m}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:8px">
      <svg width="612" height="472" viewBox="0 0 612 472">
        <defs><radialGradient id="hubp" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hgp" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#hgp)"><circle cx="{cx}" cy="{cy}" r="70" fill="url(#hubp)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">gstack</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">1 install</text>
        {nodes}</svg>
      <div style="flex:1;padding-right:6px">
        {htitle("One install, a crew","8 PLUG-INS")}
        <div style="font-family:'DM Sans';font-size:19px;color:#c9c3b8;line-height:1.45">A plug-in is a bundle. gstack drops 20+ specialist tools. marketingskills drops 44. One command, a whole team.</div>
        {cap("install the team, not the tool.")}</div></div>'''

# 5. CONNECTORS - Ultron core cabled out to 8 real app tiles (MCP servers)
def connectors():
    core=(410,235)
    apps=[("Notion","No",24,46),("GitHub","Gh",24,158),("Gmail","Gm",24,270),("Drive","Dr",24,382),
          ("Slack","Sl",626,46),("Linear","Li",626,158),("HubSpot","Hs",626,270),("Stripe","St",626,382)]
    tiles=""; cables=""; plugs=""
    for nm,mk,x,y in apps:
        left=x<400
        tiles+=(f'<rect x="{x}" y="{y}" width="170" height="56" rx="15" fill="linear-gradient(160deg,#332f2a,#201d1a)"/>'
          f'<rect x="{x}" y="{y}" width="170" height="56" rx="15" fill="#2b2723" stroke="rgba(255,255,255,.10)"/>'
          f'<rect x="{x+13}" y="{y+13}" width="30" height="30" rx="8" fill="rgba(212,162,127,.16)" stroke="rgba(212,162,127,.34)"/>'
          f'<text x="{x+28}" y="{y+34}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="14" fill="rgb({ACC})">{mk}</text>'
          f'<text x="{x+56}" y="{y+34}" font-family="DM Mono" font-size="16" fill="#e2dccf">{nm}</text>')
        ex=(x+170) if left else x
        cx1=(ex+core[0])/2
        cy=y+28
        cables+=f'<path d="M{ex} {cy} C{cx1:.0f} {cy},{cx1:.0f} {core[1]},{core[0]+(-72 if left else 72)} {core[1]}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.2"/>'
        px=core[0]+(-72 if left else 72)
        plugs+=f'<circle cx="{ex}" cy="{cy}" r="4.5" fill="rgb({ACC})"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Wired into your real tools","8 MCP")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="corem" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cgm" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {cables}{tiles}{plugs}
        <g filter="url(#cgm)"><circle cx="{core[0]}" cy="{core[1]}" r="72" fill="url(#corem)"/></g>
        <text x="{core[0]}" y="{core[1]-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">ULTRON</text>
        <text x="{core[0]}" y="{core[1]+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads + acts</text>
      </svg>
      {cap("notion, slack, github, stripe. it works where you already work.")}</div>'''

# 6. INSTALL - isometric stack of install cards ticking to done, 24/24
def install():
    rows=[("SKILLS","8 recipes ready"),("PLUG-INS","8 crews added"),("MCP","8 apps connected"),("MEMORY","vault wired")]
    cards=""
    for i,(nm,sub) in enumerate(rows):
        y=i*106
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The whole kit, one pass","24 / 24")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:414px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">24 of 24 installed &#10003;</div></div></div>
      {cap("one loadout file, one install. the whole kit lands together.")}</div>'''

# 7. UNLOCK - three layer streams converge into one capability orb
def unlock():
    groups=[("SKILLS","recipe",90),("PLUG-INS","crew",235),("MCP","cable",380)]
    left=""
    for nm,kind,y in groups:
        left+=(f'<path d="M232 {y} C400 {y},430 235,470 235" fill="none" stroke="rgba(212,162,127,.34)" stroke-width="2.4"/>'
          f'<rect x="40" y="{y-38}" width="196" height="76" rx="18" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
          f'<g transform="translate(74,{y-13})">{gicon(kind,None,26)}</g>'
          f'<text x="112" y="{y-2}" font-family="DM Sans" font-weight="800" font-size="19" fill="#e6e0d4">{nm}</text>'
          f'<text x="112" y="{y+20}" font-family="DM Mono" font-size="12" fill="#8f8f85">8 installed</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("What the loadout unlocks","COMPOUND")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <defs><radialGradient id="opb" cx="42%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ogb" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#ogb)"><circle cx="600" cy="235" r="126" fill="url(#opb)"/></g>
        <text x="600" y="222" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="600" y="252" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">OPERATOR</text>
        <text x="600" y="392" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">researches, ships, connects</text>
      </svg>
      {cap("recipes plus crews plus cables become one operator that ships.")}</div>'''

# 8. LEDGER - IVORY day-one manifest sheet: the three layers listed, checked, save-ready
def ledger():
    blocks=[("SKILLS","recipe",["/brief","/post","/ship","/nda"],"8"),
            ("PLUG-INS","crew",["gstack","marketingskills","codex"],"8"),
            ("MCP","cable",["Notion","Slack","GitHub","Stripe"],"8")]
    rows=""
    for nm,kind,items,ct in blocks:
        chips="".join(f'<span style="font-family:\'DM Mono\';font-size:14px;color:#5a4634;background:rgba(255,255,255,.6);border:1px solid rgba(150,90,45,.18);border-radius:8px;padding:5px 11px">{it}</span>' for it in items)
        extra=int(ct)-len(items)
        rows+=f'''<div style="display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.5);border:1px solid rgba(150,90,45,.16);border-radius:18px;padding:16px 20px;box-shadow:inset 0 2px 3px rgba(255,255,255,.8)">
          <div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:rgba(150,90,45,.10);border:1px solid rgba(150,90,45,.22);display:flex;align-items:center;justify-content:center">{gicon(kind,"#96562d",28)}</div>
          <div style="flex-shrink:0;width:118px">
            <div style="font-family:'DM Sans';font-weight:900;font-size:20px;color:#2a2016">{nm}</div>
            <div style="font-family:'DM Mono';font-size:12px;color:#96562d">{ct} installed</div></div>
          <div style="flex:1;display:flex;flex-wrap:wrap;gap:8px;align-items:center">{chips}<span style="font-family:'DM Mono';font-size:13px;color:#a08a68">+{extra} more</span></div>
          <svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(150,90,45,.12)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'''
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:22px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">The exact day-one kit</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">SAVE THIS</span></div>
      <div style="display:flex;flex-direction:column;gap:16px">{rows}</div>
      {cap("screenshot the sheet. install these twenty-four first, ignore the rest.","#8a745a")}</div>'''

PANELS={"loadout":loadout(),"layers":layers(),"skills":skills(),"plugins":plugins(),
        "connectors":connectors(),"install":install(),"unlock":unlock(),"ledger":ledger()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src29"; os.makedirs(outd,exist_ok=True)
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
