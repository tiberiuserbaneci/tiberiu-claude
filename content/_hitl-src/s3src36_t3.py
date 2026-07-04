#!/usr/bin/env python3
# TIER 3 - THE AGENT THAT CALLS (voice sales agent). Rebuilt to the WIRE-ITS-EYES bar: each panel a
# UNIQUE hand-built coded scene filling a clean rounded card, title + one-line caption, no generic
# stat-chip strips. Angle: the agent RESEARCHES, then places a REAL CALL, qualifies, books. Voice is
# the hero (waveform/call UI), not email. Warm palette only. 6 dark CARD + 2 ivory CARDIV.
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

# 1. RING - HERO: a live call screen with a real waveform, lead identity, timer, connected dot
def ring():
    heights=[26,44,70,96,122,150,128,98,150,112,74,138,150,92,150,124,68,150,104,142,150,84,150,118,62,132,150,96,150,122,72,142,150,90,124,150,102,64,132,150]
    bw=10; gap=8; bars=""
    for i,h in enumerate(heights):
        x=i*(bw+gap); op="1" if 7<=i<=32 else "0.45"
        bars+=f'<rect x="{x}" y="{(150-h)/2:.0f}" width="{bw}" height="{h}" rx="5" fill="rgb({ACC})" opacity="{op}" filter="url(#wg)"/>'
    fw=len(heights)*(bw+gap)-gap
    screen=(f'<div style="background:linear-gradient(160deg,#211d19,#161311);border:1px solid rgba(212,162,127,.28);'
      f'border-radius:24px;padding:26px 30px 28px;box-shadow:0 30px 54px rgba(0,0,0,.55), inset 0 2px 3px rgba(255,255,255,.06)">'
      f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:22px">'
      f'<div style="flex-shrink:0;width:56px;height:56px;border-radius:16px;background:linear-gradient(160deg,#3a332c,#241f1a);border:1px solid rgba(255,255,255,.10);display:flex;align-items:center;justify-content:center">'
      f'<svg width="27" height="27" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5 2 4.2c0 8.6 9.2 17.8 17.8 17.8l.7-4.5-5-2-2 2c-2.6-1.3-5.4-4.1-6.7-6.7l2-2z"/><path d="M15.5 3.2c1.9.3 3.6 1.3 4.8 2.9m-4.5-6.4"/></svg></div>'
      f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:23px;color:#FAFAF7">Marisa Cole</div>'
      f'<div style="font-family:DM Sans;font-size:15px;color:#9a9488">VP Operations &middot; Northwind</div></div>'
      f'<div style="text-align:right"><div style="display:flex;align-items:center;gap:8px;justify-content:flex-end"><span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.9)"></span>'
      f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC})">CONNECTED</span></div>'
      f'<div style="font-family:DM Mono;font-size:20px;color:#e6d6c2;margin-top:5px">02:14</div></div></div>'
      f'<svg width="{fw}" height="150" viewBox="0 0 {fw} 150" style="display:block;width:100%;height:118px">'
      f'<defs><filter id="wg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>{bars}</svg>'
      f'<div style="display:flex;align-items:center;justify-content:space-between;margin-top:22px;border-top:1px solid rgba(255,255,255,.08);padding-top:16px">'
      f'<span style="font-family:DM Mono;font-size:14px;color:#8f8f85">SPECTER &middot; on the line</span>'
      f'<span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">qualifying live</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It called the lead itself","LIVE CALL")}
      {screen}
      {cap("not another email in a dead inbox. a real voice, dialing a real number.")}</div>'''

# 2. DOSSIER - IVORY: the pre-call brief CORTEX pulls before the phone rings
def dossier():
    rows=[("FUNDING","Raised $4M seed &middot; May 2026"),
          ("ROLE","VP Operations, 40 reports, owns tooling"),
          ("STACK","5 point tools, no automation layer yet"),
          ("HOOK","Scaling ops fast, drowning in manual work")]
    body=""
    for k,v in rows:
        body+=(f'<div style="display:flex;align-items:flex-start;gap:16px;padding:15px 0;border-bottom:1px solid rgba(150,120,80,.18)">'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#96562d;width:88px;flex-shrink:0;padding-top:3px">{k}</span>'
          f'<span style="font-family:DM Sans;font-weight:500;font-size:20px;color:#2a2016;line-height:1.3">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("It knows them before it dials","CORTEX BRIEF")}
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:8px">
        <div style="width:58px;height:58px;border-radius:16px;background:linear-gradient(160deg,#f3e7d4,#e2d3ba);border:1px solid rgba(150,120,80,.28);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:26px;color:#96562d">N</div>
        <div><div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#2a2016">Northwind Robotics</div>
        <div style="font-family:DM Mono;font-size:13px;color:#a08a68">brief built in 9s &middot; live web</div></div></div>
      <div style="margin-top:6px">{body}</div>
      {cap("one page pulled from the live web, in its ear before hello.","#8a745a")}</div>'''

# 3. BRANCH - a bezier conversation tree: every answer has a path, none freezes the call
def branch():
    W,H=820,468
    root=(112,234,"Opener")
    mids=[(112,"Interested",True),(234,"Busy right now",True),(378,"Not a fit",False)]
    leaves=[(84,"Book a demo",True),(234,"Set a callback",True),(400,"Nurture, exit",False)]
    mx,lx=430,690
    edges=""; nodes=""
    def node(x,y,txt,w,lit,leaf=False):
        col=f"rgb({ACC})" if lit else "rgba(200,70,35,.6)"
        fill="linear-gradient(160deg,#403a33,#241f1a)" if lit else "#211d1a"
        tc="#FAFAF7" if lit else "#b58a7c"
        return (f'<div style="position:absolute;left:{x}px;top:{y-27}px;width:{w}px;height:54px;background:{fill};'
          f'border:1.6px solid {col};border-radius:15px;display:flex;align-items:center;justify-content:center;'
          f'font-family:DM Sans;font-weight:700;font-size:16px;color:{tc};box-shadow:0 12px 24px rgba(0,0,0,.4)">{txt}</div>')
    # svg edges
    for (my,mtxt,mlit),(ly,ltxt,llit) in zip(mids,leaves):
        c1=f"rgb({ACC})" if mlit else "rgba(200,70,35,.5)"
        c2=f"rgb({ACC})" if llit else "rgba(200,70,35,.5)"
        edges+=f'<path d="M{root[0]+150} {root[1]} C310 {root[1]},310 {my},{mx} {my}" fill="none" stroke="{c1}" stroke-width="{3 if mlit else 2}"/>'
        edges+=f'<path d="M{mx+178} {my} C610 {my},610 {ly},{lx} {ly}" fill="none" stroke="{c2}" stroke-width="{3 if llit else 2}"/>'
    svg=f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">{edges}</svg>'
    html=node(root[0],root[1],root[2],150,True)
    for my,mtxt,mlit in mids: html+=node(mx,my,mtxt,178,mlit)
    for ly,ltxt,llit in leaves: html+=node(lx,ly,ltxt,150,llit)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A branch for every answer","CALL SCRIPT")}
      <div style="position:relative;height:{H}px">{svg}{html}</div>
      {cap("objections mapped in advance. it never goes silent on the line.")}</div>'''

# 4. GAUGE - live qualification score forming while the agent talks
def gauge():
    pct=84; r=80; circ=2*math.pi*r; dash=circ*pct/100
    chips=[("BUDGET","approved","yes"),("AUTHORITY","VP, owns it","yes"),("NEED","ops overload","high"),("TIMING","this quarter","Q3")]
    cc=""
    for k,v,tag in chips:
        cc+=(f'<div style="background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:15px 18px;box-shadow:0 12px 22px rgba(0,0,0,.45)">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">{k}</span>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:15px;color:#FAFAF7;text-transform:uppercase">{tag}</span></div>'
          f'<div style="font-family:DM Sans;font-size:16px;color:#a8a296;margin-top:3px">{v}</div></div>')
    ringsvg=(f'<svg width="196" height="196" viewBox="0 0 196 196">'
      f'<circle cx="98" cy="98" r="{r}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="16"/>'
      f'<circle cx="98" cy="98" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 98 98)" filter="url(#gg2)"/>'
      f'<defs><filter id="gg2" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs></svg>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;position:relative;width:196px;height:196px">{ringsvg}
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:52px;color:#FAFAF7;line-height:1">{pct}</span>
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">QUALIFIED</span></div></div>
      <div style="flex:1">
        {htitle("It qualifies while it talks","STRIKER SCORE")}
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">{cc}</div>
        {cap("budget, authority, need, timing scored live, not after the call.")}</div></div>'''

# 5. CALENDAR - IVORY: the meeting dropped straight onto your week
def calendar():
    days=["MON","TUE","WED","THU","FRI"]; times=["09","10","11","12"]
    cells=""
    booked=(3,1)  # THU, 10:00 row
    for ri,t in enumerate(times):
        for ci,d in enumerate(days):
            if (ci,ri)==booked:
                cells+=('<div style="grid-column:%d;grid-row:%d;border-radius:12px;background:linear-gradient(160deg,#d98a5e,#c06a3d);'
                  'box-shadow:0 12px 24px rgba(192,106,61,.4), inset 0 2px 2px rgba(255,255,255,.3);display:flex;flex-direction:column;'
                  'align-items:center;justify-content:center;padding:6px">'
                  '<span style="font-family:DM Sans;font-weight:900;font-size:16px;color:#fff;line-height:1">Marisa</span>'
                  '<span style="font-family:DM Mono;font-size:11px;color:rgba(255,255,255,.85)">10:30 demo</span></div>')%(ci+2,ri+2)
            else:
                cells+=('<div style="grid-column:%d;grid-row:%d;border-radius:12px;background:rgba(150,120,80,.07);'
                  'border:1px solid rgba(150,120,80,.12)"></div>')%(ci+2,ri+2)
    heads="".join(f'<div style="grid-column:{ci+2};grid-row:1;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#a08a68;text-align:center;padding-bottom:6px">{d}</div>' for ci,d in enumerate(days))
    tlabs="".join(f'<div style="grid-column:1;grid-row:{ri+2};font-family:DM Mono;font-size:12px;color:#a08a68;display:flex;align-items:center;padding-right:8px">{t}</div>' for ri,t in enumerate(times))
    grid=(f'<div style="display:grid;grid-template-columns:34px repeat(5,1fr);grid-template-rows:auto repeat(4,74px);gap:9px">{heads}{tlabs}{cells}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("Booked on your calendar","MEETING SET")}
      {grid}
      {cap("it reads your live availability and drops the invite before it hangs up.","#8a745a")}</div>'''

# 6. MEMORY - transcript lines flow into a memory core so the next call already knows
def memory():
    W,H=820,452
    lines=[("0:12","opened on the funding round",96),
           ("1:04","handled 'we already use email'",196),
           ("1:58","agreed to a Thursday demo",296),
           ("2:11","flagged: wants pricing first",396)]
    hubx,huby=648,246
    edges=""; nodes=""
    for t,txt,y in lines:
        mxp=(210+hubx)/2
        edges+=f'<path d="M212 {y} C{mxp:.0f} {y},{mxp:.0f} {huby},{hubx-70} {huby}" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.4"/>'
        nodes+=(f'<rect x="34" y="{y-28}" width="178" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="52" y="{y-4}" font-family="DM Mono" font-size="13" fill="rgb({ACC})">{t}</text>'
          f'<text x="52" y="{y+16}" font-family="DM Sans" font-size="14" font-weight="500" fill="#cfc9bd">{txt}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every word, remembered","INTO THE VAULT")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><radialGradient id="core" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#cg)"><circle cx="{hubx}" cy="{huby}" r="76" fill="url(#core)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">VAULT</text>
        <text x="{hubx}" y="{huby+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">1 memory</text>
      </svg>
      {cap("transcript, summary and next step logged. the next call opens where this closed.")}</div>'''

# 7. FUNNEL - one night of dialing, narrowing to booked meetings
def funnel():
    stages=[("240","dials placed",680),("88","picked up",510),("31","qualified",340),("12","meetings booked",190)]
    bars=""
    for i,(n,lbl,w) in enumerate(stages):
        lit=(i==len(stages)-1)
        bg=(f"linear-gradient(160deg,#e6b48f,rgb({ACC}) 60%,#9a5a35)" if lit else "linear-gradient(160deg,#3a332c,#241f1a)")
        bd=(f"rgb({ACC})" if lit else "rgba(212,162,127,.28)")
        nc="#1a0f0a" if lit else "#FAFAF7"; lc="rgba(26,15,10,.72)" if lit else "#9a9488"
        glow="box-shadow:0 16px 30px rgba(212,162,127,.4)" if lit else "box-shadow:0 12px 22px rgba(0,0,0,.4)"
        bars+=(f'<div style="width:{w}px;height:78px;margin:0 auto;background:{bg};border:1.5px solid {bd};border-radius:16px;{glow};'
          f'display:flex;align-items:center;justify-content:center;gap:16px">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:40px;color:{nc};line-height:1">{n}</span>'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:18px;color:{lc}">{lbl}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("240 dials, 12 booked","ONE NIGHT")}
      <div style="display:flex;flex-direction:column;gap:14px;padding:8px 0">{bars}</div>
      {cap("it worked the whole list overnight. you woke up to a full calendar.")}</div>'''

# 8. GATE - the calling power, held on the operator's tap (HUMAN GATE)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It calls. You approve.","HUMAN GATE")}
      <svg width="820" height="424" viewBox="0 0 820 424" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="205" cy="212" r="132" fill="url(#orb)"/></g>
        <g transform="translate(205,196)"><path d="M-30 -22 -50 -18c0 40 42 82 82 82l4-20-24-9-9 9c-12-6-25-19-31-31l9-9z" fill="#2a160c"/></g>
        <text x="205" y="262" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".12em">LIVE CALLS</text>
        <path d="M341 212 H612" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="622" y="142" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(664,180)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="692" y="318" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every number it dials is on a list you signed off. augmented, never rogue.")}</div>'''

PANELS={"ring":ring(),"dossier":dossier(),"branch":branch(),"gauge":gauge(),
        "calendar":calendar(),"memory":memory(),"funnel":funnel(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src36"; os.makedirs(outd,exist_ok=True)
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
