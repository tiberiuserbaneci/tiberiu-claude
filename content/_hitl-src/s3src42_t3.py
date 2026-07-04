#!/usr/bin/env python3
# TIER 3 - THE PERMISSIONLESS TWO (Naval's four leverages, re-told as Ultron). Each panel a UNIQUE
# hand-built coded scene on a clean rounded card (WIRE-ITS-EYES bar). Helpers + __main__ copied from
# aibody_t3.py. Renders 8 PNGs to models_clay/s3src42/. Cost zero.
import importlib.util, os, math, base64
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

# real Ultron SPHERE logo (operator rule: sphere, never a generic mark) - base64 inlined
with open(f"{ROOT}/content/ultron-logo.png","rb") as _f:
    LOGO="data:image/png;base64,"+base64.b64encode(_f.read()).decode()

# 1. QUADMAP - the 2x2 leverage map. top row (labor, capital) NEEDS PERMISSION (muted + red lock),
# bottom row (code, media) PERMISSIONLESS (accent + glow), Ultron sphere sitting in both bottom cells.
def quadmap():
    def cell(label,glyph,perm,ultron=False):
        if perm:
            bg="#221f1b"; bd="rgba(255,255,255,.08)"; ink="#9a9488"; sub="rgba(200,70,35,.9)"; st="needs a yes"; glow=""
        else:
            bg="linear-gradient(160deg,#403a33,#241f1a)"; bd=f"rgb({ACC})"; ink="#FAFAF7"; sub=f"rgb({ACC})"; st="no permission"; glow="box-shadow:0 0 30px rgba(212,162,127,.28), inset 0 2px 2px rgba(255,255,255,.08);"
        badge=f'<img src="{LOGO}" style="position:absolute;top:16px;right:16px;width:34px;height:34px;border-radius:50%">' if ultron else ''
        lock=('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb(200,70,35)" stroke-width="2.4"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>') if perm else ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb('+ACC+')" stroke-width="2.4"><path d="M4 11h16v10H4z"/><path d="M8 11V8a4 4 0 0 1 7.7-1.5"/></svg>')
        return (f'<div style="position:relative;background:{bg};border:1.5px solid {bd};border-radius:20px;padding:22px 22px;{glow}min-height:150px;display:flex;flex-direction:column;justify-content:space-between">'
          f'{badge}'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:30px;color:{ink}">{glyph}</div>'
          f'<div><div style="font-family:DM Sans;font-weight:800;font-size:22px;color:{ink}">{label}</div>'
          f'<div style="display:flex;align-items:center;gap:8px;margin-top:6px">{lock}<span style="font-family:DM Mono;font-size:13px;color:{sub}">{st}</span></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The four-way map","LEVERAGE MAP")}
      <div style="display:flex;gap:14px;align-items:stretch">
        <div style="display:flex;flex-direction:column;justify-content:space-between;padding:8px 0;text-align:center">
          <div style="writing-mode:vertical-rl;transform:rotate(180deg);font-family:DM Mono;font-size:12px;letter-spacing:.18em;color:#c84623;flex:1;display:flex;align-items:center;justify-content:center">NEEDS PERMISSION</div>
          <div style="writing-mode:vertical-rl;transform:rotate(180deg);font-family:DM Mono;font-size:12px;letter-spacing:.18em;color:rgb({ACC});flex:1;display:flex;align-items:center;justify-content:center">PERMISSIONLESS</div>
        </div>
        <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px">
          {cell("Labor","01",True)}{cell("Capital","02",True)}
          {cell("Code","03",False,True)}{cell("Media","04",False,True)}
        </div>
      </div>
      {cap("labor and capital ask permission. code and media never do.")}</div>'''

# 2. LABOR - hierarchy: founder on top, a red permission lock on the wire, a row of worker nodes below.
def labor():
    workers=[("hire",110),("manage",250),("pay",390),("retain",530),("replace",670)]
    nodes=""; wires=""
    fx,fy=390,72
    for nm,x in workers:
        wires+=f'<path d="M{fx} {fy+34} C{fx} 150,{x} 150,{x} 214" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<rect x="{x-56}" y="214" width="112" height="74" rx="16" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5"/>'
          f'<circle cx="{x}" cy="242" r="12" fill="none" stroke="#8f8f85" stroke-width="2"/><path d="M{x-16} 272 a16 16 0 0 1 32 0" fill="none" stroke="#8f8f85" stroke-width="2"/>'
          f'<text x="{x}" y="308" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Labor asks first","NEEDS PERMISSION")}
      <svg width="820" height="380" viewBox="0 0 820 380" style="display:block;margin:0 auto">
        <defs><radialGradient id="fnd" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient></defs>
        {wires}
        <circle cx="{fx}" cy="{fy}" r="34" fill="url(#fnd)"/>
        <text x="{fx}" y="{fy+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">YOU</text>
        <g transform="translate(556,120)"><rect x="0" y="0" width="184" height="60" rx="14" fill="rgba(200,70,35,.10)" stroke="rgb(200,70,35)" stroke-width="1.6"/>
          <g transform="translate(18,16)"><rect x="0" y="12" width="26" height="18" rx="3" fill="none" stroke="rgb(200,70,35)" stroke-width="2.4"/><path d="M5 12V8a8 8 0 0 1 16 0v4" fill="none" stroke="rgb(200,70,35)" stroke-width="2.4"/></g>
          <text x="112" y="26" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb(200,70,35)">permission</text>
          <text x="112" y="46" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb(200,70,35)">required</text></g>
        {nodes}
      </svg>
      {cap("hire, manage, pay, retain. leverage that can quit on you.")}</div>'''

# 3. CAPITAL - dilution ledger: founder share shrinks across rounds, muted investor mass grows.
def capital():
    rows=[("Day one",100,"0.02c raised"),("Seed",78,"first yes"),("Series A",56,"more yes"),("Series B",41,"most control gone")]
    bars=""
    y=0
    for nm,own,note in rows:
        fillw=int(560*own/100)
        bars+=(f'<div style="margin-bottom:20px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px">'
          f'<span style="font-family:DM Mono;font-size:14px;letter-spacing:.08em;color:#c9c3b8">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:#8f8f85">{note}</span></div>'
          f'<div style="height:34px;border-radius:9px;overflow:hidden;display:flex;background:#211d19;border:1px solid rgba(255,255,255,.06)">'
          f'<div style="width:{own}%;background:linear-gradient(90deg,rgb({ACC}),#b07a4f);display:flex;align-items:center;padding-left:14px"><span style="font-family:DM Sans;font-weight:900;font-size:16px;color:#241206">you {own}%</span></div>'
          f'<div style="flex:1;background:repeating-linear-gradient(45deg,rgba(200,70,35,.22),rgba(200,70,35,.22) 8px,rgba(200,70,35,.10) 8px,rgba(200,70,35,.10) 16px);display:flex;align-items:center;justify-content:flex-end;padding-right:12px"><span style="font-family:DM Mono;font-size:12px;color:rgba(200,70,35,.95)">investors {100-own}%</span></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Capital asks too","NEEDS PERMISSION")}
      <div style="margin-top:6px">{bars}</div>
      {cap("raise, dilute, report. leverage you have to be granted.")}</div>'''

# 4. CODE - one source build spawns a dense field of running instances, at zero marginal cost.
def code():
    cols,rowsN=44,22; dots=""
    for r in range(rowsN):
        for c in range(cols):
            x=8+c*15.4; yy=8+r*15.4
            src=(c<6 and r<6)
            if src:
                dots+=f'<circle cx="{x:.0f}" cy="{yy:.0f}" r="3.4" fill="rgb({ACC})" opacity="0.95"/>'
            else:
                op=0.16+0.5*((c+r)%5)/5
                dots+=f'<circle cx="{x:.0f}" cy="{yy:.0f}" r="2.6" fill="rgba(212,162,127,{op:.2f})"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Code never sleeps","PERMISSIONLESS")}
      <div style="display:flex;align-items:center;gap:26px">
        <svg width="700" height="352" viewBox="0 0 700 352" style="flex:1">
          <rect x="0" y="0" width="700" height="352" rx="16" fill="#191715"/>
          {dots}
          <rect x="2" y="2" width="94" height="94" rx="10" fill="none" stroke="rgb({ACC})" stroke-width="1.6" stroke-dasharray="5 5"/>
          <text x="49" y="118" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">source</text>
        </svg>
        <div style="width:150px;flex-shrink:0">
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:rgb({ACC});line-height:1">968</div>
          <div style="font-family:DM Mono;font-size:13px;color:#8f8f85;margin-top:4px">copies running</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7;line-height:1;margin-top:22px">0c</div>
          <div style="font-family:DM Mono;font-size:13px;color:#8f8f85;margin-top:4px">to make each one</div>
        </div>
      </div>
      {cap("build once, it runs everywhere for free. no one to manage.")}</div>'''

# 5. MEDIA (IVORY) - one post broadcasts outward, audience dots on concentric rings, reach readout.
def media():
    cx,cy=250,205
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(150,90,45,.20)" stroke-width="1.6"/>' for r in (66,120,178))
    aud=[(20,178),(70,120),(120,178),(165,120),(215,178),(300,120),(340,178),(255,66),(110,66),(200,66)]
    bl=""
    for ang,dist in aud:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#96562d" opacity="0.85"/>'
    header=('<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
      '<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">Media never stops</span>'
      '<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">PERMISSIONLESS</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px;display:flex;flex-direction:column">
      {header}
      <div style="display:flex;align-items:center;gap:30px">
        <svg width="440" height="410" viewBox="0 0 440 410">
          <defs><radialGradient id="bcast" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.30)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
          <radialGradient id="src2" cx="38%" cy="30%"><stop offset="0%" stop-color="#e79b6a"/><stop offset="100%" stop-color="#96562d"/></radialGradient></defs>
          <circle cx="{cx}" cy="{cy}" r="178" fill="url(#bcast)"/>{rings}
          {bl}
          <circle cx="{cx}" cy="{cy}" r="30" fill="url(#src2)"/>
          <path d="M{cx-9} {cy-9} h18 v18 h-18 z" fill="none" stroke="#fff" stroke-width="2.4"/>
          <text x="{cx}" y="{cy+56}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#96562d">1 post</text>
        </svg>
        <div style="flex:1">
          <div style="font-family:DM Sans;font-weight:900;font-size:56px;color:#2a2016;line-height:1">12,400</div>
          <div style="font-family:DM Mono;font-size:14px;color:#8a745a;margin-top:4px">reached from one post</div>
          <div style="height:1px;background:rgba(150,120,80,.24);margin:20px 0"></div>
          <div style="font-family:DM Sans;font-size:19px;color:#5a4634;line-height:1.4">Publish once. It keeps working while you sleep, at zero marginal cost.</div>
        </div>
      </div>
      {cap("publish once, it reaches thousands while you do something else.","#8a745a")}</div>'''

# 6. BOTH - two input tiles (CODE, MEDIA) beam into one Ultron sphere: both leverages, one login.
def both():
    def tile(lbl,sub,y):
        return (f'<div style="position:absolute;left:0;top:{y}px;width:250px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:20px;padding:18px 22px;box-shadow:0 20px 34px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#FAFAF7">{lbl}</div>'
          f'<div style="font-family:DM Mono;font-size:13px;color:rgb({ACC});margin-top:4px">{sub}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Both, one login","THE UNLOCK")}
      <div style="position:relative;height:392px">
        <svg width="820" height="392" viewBox="0 0 820 392" style="position:absolute;left:0;top:0">
          <path d="M258 76 C440 76,470 196,586 196" fill="none" stroke="rgb({ACC})" stroke-width="4"/>
          <path d="M258 300 C440 300,470 196,586 196" fill="none" stroke="rgb({ACC})" stroke-width="4"/>
          <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter>
          <g filter="url(#og)"><circle cx="660" cy="196" r="6" fill="rgba(212,162,127,.5)"/></g>
        </svg>
        <img src="{LOGO}" style="position:absolute;left:566px;top:104px;width:184px;height:184px;border-radius:50%;box-shadow:0 0 46px rgba(212,162,127,.5)">
        {tile("CODE","ships product",40)}
        {tile("MEDIA","ships reach",264)}
        <div style="position:absolute;left:606px;top:298px;width:104px;text-align:center;font-family:DM Mono;font-size:13px;color:#8f8f85">one operator</div>
      </div>
      {cap("one login runs the code and the media at the same time.")}</div>'''

# 7. ROUTE - a job token routed by the ROUTER into two lanes: code (SENTINEL) and media (PULSE, AMPLIFY).
def route():
    hubx,hy=168,196
    def lane(y,tag,agents,desc):
        chips="".join(f'<span style="font-family:DM Mono;font-size:13px;color:rgb({ACC});background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.3);border-radius:8px;padding:4px 10px;margin-right:8px">{a}</span>' for a in agents)
        return (f'<div style="position:absolute;left:326px;top:{y-46}px;width:434px;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:18px;padding:16px 20px;box-shadow:0 18px 30px rgba(0,0,0,.5)">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#FAFAF7">{tag}</span></div>'
          f'<div style="margin:10px 0 8px">{chips}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85">{desc}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One job, two lanes","ROUTED")}
      <div style="position:relative;height:388px">
        <svg width="820" height="388" viewBox="0 0 820 388" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub2" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          <path d="M{hubx+60} {hy} C300 {hy},310 108,320 108" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/>
          <path d="M{hubx+60} {hy} C300 {hy},310 284,320 284" fill="none" stroke="rgb({ACC})" stroke-width="4.5"/>
          <rect x="10" y="{hy-26}" width="92" height="52" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>
          <text x="56" y="{hy-2}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#c9c3b8">launch a</text>
          <text x="56" y="{hy+14}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#c9c3b8">feature</text>
          <g filter="url(#hg2)"><circle cx="{hubx}" cy="{hy}" r="58" fill="url(#hub2)"/></g>
          <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">splits the job</text>
        </svg>
        {lane(108,"CODE",["SENTINEL"],"builds and ships the product")}
        {lane(284,"MEDIA",["PULSE","AMPLIFY"],"writes and publishes the reach")}
      </div>
      {cap("sentinel builds. pulse and amplify publish. the router splits the job.")}</div>'''

# 8. OPERATOR - one founder holds two lit leverage orbs (CODE, MEDIA); HIRE and RAISE crossed out.
def operator():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One founder, two levers","THE OPERATOR")}
      <svg width="820" height="392" viewBox="0 0 820 392" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="op" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="opg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter>
        </defs>
        <path d="M410 150 L214 150" stroke="rgb({ACC})" stroke-width="4"/>
        <path d="M410 150 L606 150" stroke="rgb({ACC})" stroke-width="4"/>
        <g filter="url(#opg)"><circle cx="410" cy="150" r="60" fill="url(#op)"/></g>
        <circle cx="410" cy="132" r="17" fill="#2a160c"/><path d="M384 190 a26 26 0 0 1 52 0" fill="#2a160c"/>
        <g filter="url(#opg)"><circle cx="150" cy="150" r="52" fill="url(#op)"/></g>
        <text x="150" y="156" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#241206">CODE</text>
        <g filter="url(#opg)"><circle cx="670" cy="150" r="52" fill="url(#op)"/></g>
        <text x="670" y="156" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#241206">MEDIA</text>
        <g transform="translate(250,300)"><rect x="0" y="0" width="140" height="56" rx="14" fill="rgba(200,70,35,.08)" stroke="rgba(200,70,35,.7)" stroke-width="1.6"/>
          <text x="70" y="35" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="rgba(200,70,35,.9)">HIRE</text>
          <line x1="12" y1="46" x2="128" y2="10" stroke="rgb(200,70,35)" stroke-width="3"/></g>
        <g transform="translate(430,300)"><rect x="0" y="0" width="140" height="56" rx="14" fill="rgba(200,70,35,.08)" stroke="rgba(200,70,35,.7)" stroke-width="1.6"/>
          <text x="70" y="35" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="rgba(200,70,35,.9)">RAISE</text>
          <line x1="12" y1="46" x2="128" y2="10" stroke="rgb(200,70,35)" stroke-width="3"/></g>
      </svg>
      {cap("wield both alone. no headcount, no term sheet.")}</div>'''

PANELS={"quadmap":quadmap(),"labor":labor(),"capital":capital(),"code":code(),
        "media":media(),"both":both(),"route":route(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src42"; os.makedirs(outd,exist_ok=True)
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
