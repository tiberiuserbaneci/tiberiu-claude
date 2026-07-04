#!/usr/bin/env python3
# TIER 3 - DROP THE REQUEST, GET THE FILE. Ultron adaptation of the "Obsidian vault as business OS"
# scraped carousel: a plain-text vault is the shared, writable company memory; you drop a request as a
# file into Queue, the agents read the vault, the system files the output into Generated. Each panel is
# a UNIQUE hand-built coded scene on a clean rounded card, title + one caption, no generic stat strips.
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

# 1. THE GAP - a field of notes dissolving left to right into a dead session; nothing was filed
def gap():
    cols,rows=17,8; x0,y0,dx,dy=32,26,46,44
    dots=""
    for r in range(rows):
        for c in range(cols):
            x=x0+c*dx; y=y0+r*dy; frac=c/(cols-1)
            op=max(0.0,1-frac*1.28)
            if frac>0.80:
                a=max(0.10,0.55-(frac-0.80)*2.2)
                dots+=(f'<line x1="{x-5}" y1="{y-5}" x2="{x+5}" y2="{y+5}" stroke="rgba(200,70,35,{a:.2f})" stroke-width="2.2"/>'
                       f'<line x1="{x+5}" y1="{y-5}" x2="{x-5}" y2="{y+5}" stroke="rgba(200,70,35,{a:.2f})" stroke-width="2.2"/>')
            elif op>0.02:
                dots+=f'<circle cx="{x}" cy="{y}" r="6" fill="rgba(212,162,127,{op:.2f})"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A chat keeps nothing","NO VAULT")}
      <svg width="820" height="374" viewBox="0 0 820 374" style="display:block;margin:6px auto 0">
        {dots}
        <line x1="606" y1="8" x2="606" y2="360" stroke="rgba(200,70,35,.42)" stroke-width="1.6" stroke-dasharray="5 8"/>
        <text x="150" y="358" font-family="DM Mono" font-size="13" fill="#9a9488">what you told it</text>
        <text x="700" y="358" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb(200,70,35)">session ends</text>
      </svg>
      {cap("close the tab and the context is gone. nothing was ever written down.")}</div>'''

# 2. THE VAULT - IVORY isometric stack of plain-text file cards = the whole company in files
def vault():
    files=[("ICP.md","who we sell to"),("pricing.md","tiers and cents"),("pipeline.md","every open deal"),
           ("voice.md","how we write"),("offers.md","what we sell")]
    cards=""
    for i,(fn,sub) in enumerate(files):
        y=i*74
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#fffdf8,#f0e7d7);'
          f'border:1.5px solid rgba(120,95,60,.22);border-radius:16px;padding:15px 22px;'
          f'box-shadow:0 24px 34px rgba(120,95,60,.22), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:18px">'
          f'<svg width="26" height="30" viewBox="0 0 24 28" fill="none"><path d="M4 2h11l5 5v19a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1z" fill="#fff" stroke="#96562d" stroke-width="1.8"/><path d="M15 2v5h5" fill="none" stroke="#96562d" stroke-width="1.8"/><path d="M7 14h9M7 18h9M7 22h6" stroke="rgba(150,90,45,.6)" stroke-width="1.6" stroke-linecap="round"/></svg>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:16px;color:#2a2016">{fn}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8a745a">{sub}</div></div>'
          f'<span style="font-family:DM Mono;font-size:12px;color:#96562d">plain text</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Your whole company, in files","ONE VAULT","#2a2016")}
      <div style="perspective:2000px;height:452px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-9deg);width:560px;height:370px;position:relative">{cards}</div></div>
      {cap("every fact the business knows, in files any agent can read.","#8a745a")}</div>'''

# 3. THE STRUCTURE - dense ledger of the 8 folders; queue + generated lit as the loop
def folders():
    rows=[("01","CLIENTS","one folder per client",0),("02","PROJECTS","one folder per project",0),
          ("03","OPERATIONS","how the business runs",0),("04","CONTENT","drafts, calendars, posts",0),
          ("05","FINANCES","income, expenses, invoices",0),("06","RESEARCH","notes, briefs, intel",0),
          ("07","QUEUE","you drop requests here",1),("08","GENERATED","the system drops outputs",1)]
    out=""
    for num,nm,desc,lit in rows:
        bg="rgba(212,162,127,.11)" if lit else "linear-gradient(160deg,#2e2e2b,#242422)"
        bd="rgba(212,162,127,.36)" if lit else "rgba(255,255,255,.05)"
        icol=f"rgb({ACC})" if lit else "rgba(212,162,127,.7)"
        nmcol=f"rgb({ACC})" if lit else "#FAFAF7"
        out+=(f'<div style="display:flex;align-items:center;gap:15px;padding:10px 18px;border-radius:12px;'
          f'background:{bg};border:1px solid {bd};margin-bottom:7px">'
          f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{icol}" stroke-width="2"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>'
          f'<span style="font-family:DM Mono;font-size:15px;color:{icol};width:26px">{num}</span>'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;letter-spacing:.02em;color:{nmcol}">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-left:auto">{desc}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 32px">
      {htitle("Eight folders run the company","THE STRUCTURE")}
      <div>{out}</div>
      {cap("build the vault like a business, not like a brain.")}</div>'''

# 4. THE QUEUE - a request file drops down a chute into folder 07
def queue():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("You drop a request as a file","THE INPUT")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <defs><filter id="qg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="238" y="14" width="344" height="126" rx="16" fill="#242220" stroke="rgba(255,255,255,.12)"/>
        <text x="264" y="52" font-family="DM Mono" font-size="15" fill="rgb({ACC})">request.md</text>
        <text x="264" y="86" font-family="DM Sans" font-weight="700" font-size="20" fill="#FAFAF7">draft 12 follow-ups</text>
        <text x="264" y="116" font-family="DM Sans" font-size="16" fill="#8f8f85">for the Q3 no-reply list</text>
        <path d="M410 148 L410 250" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>
        <path d="M388 232 L410 262 L432 232" fill="none" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M300 300 h60 l14 -16 h146 v150 a10 10 0 0 1 -10 10 H310 a10 10 0 0 1 -10 -10 Z" fill="rgba(212,162,127,.12)" stroke="rgb({ACC})" stroke-width="2.5" filter="url(#qg)"/>
        <text x="410" y="368" text-anchor="middle" font-family="DM Mono" font-size="15" fill="rgb({ACC})">07</text>
        <text x="410" y="402" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="24" fill="#FAFAF7">QUEUE</text>
      </svg>
      {cap("write what you need into queue. that plain-text note is the whole interface.")}</div>'''

# 5. THE AGENTS - radial hub-and-spokes: one vault, seven named specialists reading it
def agents():
    cx,cy,R=410,222,168
    ag=["CORTEX","SPECTER","STRIKER","PULSE","SENTINEL","AMPLIFY","COUNSEL"]
    spokes=""; nodes=""
    for i,nm in enumerate(ag):
        a=-90+i*(360/len(ag))
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(255,255,255,.13)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".04em" fill="#d9d5cc">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven specialists, one vault","THE READERS")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {spokes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">VAULT</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">shared memory</text>
      </svg>
      {cap("cortex, specter, striker, pulse, sentinel, amplify, counsel draw from the same files.")}</div>'''

# 6. THE ROUTER - a tier gauge picking the cheapest model that fits, priced in cents
def tier():
    cx,cy,R=410,296,178
    def pt(deg):
        return cx+R*math.cos(math.radians(deg)), cy-R*math.sin(math.radians(deg))
    lx,ly=pt(150); dx,dy=pt(30); sx,sy=pt(90)
    ticks=""
    labs=[("LITE","0.02c","lookups",150),("SMART","0.11c","daily work",90),("DEEP","0.40c","hard calls",30)]
    for nm,cost,role,deg in labs:
        tx,ty=pt(deg); ix,iy=cx+(R-22)*math.cos(math.radians(deg)),cy-(R-22)*math.sin(math.radians(deg))
        on=(deg==90)
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.45)"
        ticks+=f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{tx:.0f}" y2="{ty:.0f}" stroke="{col}" stroke-width="4"/>'
        lyoff = -26 if deg==90 else 30
        anch = "middle" if deg==90 else ("start" if deg<90 else "end")
        px = tx + (0 if deg==90 else (14 if deg<90 else -14))
        ticks+=(f'<text x="{px:.0f}" y="{ty+lyoff:.0f}" text-anchor="{anch}" font-family="DM Sans" font-weight="800" font-size="18" fill="{"#FAFAF7" if on else "#9a9488"}">{nm}</text>'
          f'<text x="{px:.0f}" y="{ty+lyoff+22:.0f}" text-anchor="{anch}" font-family="DM Mono" font-size="13" fill="{col}">{cost} · {role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The router prices the job","MODEL TIER")}
      <svg width="820" height="392" viewBox="0 0 820 392" style="display:block;margin:0 auto">
        <defs><linearGradient id="arc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(212,162,127,.3)"/><stop offset="50%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="rgba(212,162,127,.3)"/></linearGradient>
        <filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
        <path d="M{lx:.0f} {ly:.0f} A{R} {R} 0 0 1 {dx:.0f} {dy:.0f}" fill="none" stroke="url(#arc)" stroke-width="16" stroke-linecap="round"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{sx:.0f}" y2="{sy:.0f}" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="13" fill="rgb({ACC})"/>
        <rect x="{cx-92}" y="{cy+34}" width="184" height="52" rx="14" fill="rgba(212,162,127,.12)" stroke="rgb({ACC})" stroke-width="1.6"/>
        <text x="{cx}" y="{cy+66}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">SMART · picked</text>
      </svg>
      {cap("lite for lookups, smart for daily work, deep for hard calls. cents per run.")}</div>'''

# 7. THE OUTPUT - IVORY receipt: the finished asset filed back into folder 08
def generated():
    items=[("12 follow-ups drafted","specter"),("ICP brief refreshed","cortex"),("invoice logged","counsel"),("post scheduled","amplify")]
    lines=""
    for txt,who in items:
        lines+=(f'<div style="display:flex;align-items:center;gap:14px;padding:12px 4px;border-bottom:1px solid rgba(150,120,80,.18)">'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:19px;color:#2a2016">{txt}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:#96562d">{who}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The finished file lands here","GENERATED","#2a2016")}
      <div style="background:rgba(255,255,255,.55);border:1.5px solid rgba(150,120,80,.22);border-radius:20px;padding:22px 26px">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:8px">
          <span style="font-family:DM Mono;font-size:15px;letter-spacing:.06em;color:#2a2016">08 / GENERATED</span>
          <span style="font-family:DM Mono;font-size:14px;color:#96562d">Tue 09:14</span></div>
        {lines}
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-top:16px">
          <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#2a2016">4 files</span>
          <span style="font-family:DM Mono;font-size:14px;color:#8a745a">filed to the vault</span></div>
      </div>
      {cap("drafts, briefs, invoices, sequences. the result is filed back as a new note.","#8a745a")}</div>'''

# 8. THE GATE - request meets the human seal, approved output loops back into the vault
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("You seal it, it compounds","HUMAN GATE")}
      <svg width="820" height="446" viewBox="0 0 820 446" style="display:block;margin:0 auto">
        <defs><radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <rect x="34" y="118" width="176" height="120" rx="16" fill="#242220" stroke="rgba(255,255,255,.12)"/>
        <text x="58" y="158" font-family="DM Mono" font-size="14" fill="rgb({ACC})">output.md</text>
        <text x="58" y="192" font-family="DM Sans" font-weight="700" font-size="19" fill="#FAFAF7">ready to</text>
        <text x="58" y="216" font-family="DM Sans" font-weight="700" font-size="19" fill="#FAFAF7">ship</text>
        <path d="M214 178 H286" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 11" stroke-linecap="round"/>
        <g filter="url(#sg)"><circle cx="410" cy="178" r="96" fill="url(#seal)"/></g>
        <circle cx="410" cy="178" r="74" fill="none" stroke="rgba(42,22,12,.4)" stroke-width="2" stroke-dasharray="4 6"/>
        <text x="410" y="172" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">YOUR</text>
        <text x="410" y="204" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">TAP</text>
        <path d="M506 178 H628 a14 14 0 0 1 14 14 v96 a14 14 0 0 1 -14 14 H150 a14 14 0 0 1 -14 -14 v-14" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="3" stroke-dasharray="7 7"/>
        <path d="M124 296 l12 -20 l12 20" fill="none" stroke="rgba(212,162,127,.55)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        <rect x="500" y="330" width="240" height="86" rx="16" fill="rgba(212,162,127,.10)" stroke="rgb({ACC})" stroke-width="2"/>
        <text x="620" y="366" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})">approved</text>
        <text x="620" y="396" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="21" fill="#FAFAF7">back to the vault</text>
      </svg>
      {cap("nothing ships without your tap, then each output becomes tomorrow's memory.")}</div>'''

PANELS={"gap":gap(),"vault":vault(),"folders":folders(),"queue":queue(),
        "agents":agents(),"tier":tier(),"generated":generated(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src09"; os.makedirs(outd,exist_ok=True)
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
