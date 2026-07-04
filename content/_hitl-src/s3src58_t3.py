#!/usr/bin/env python3
# TIER 3 - THE 10X SETUP (adaptare s3src58: "5 moves decide whether Claude Code 10x's your output").
# Angle: the 5 CONFIG DECISIONS you make at setup. Each move its own bespoke coded scene on a clean
# rounded card (WIRE-ITS-EYES bar): title + one mono caption, warm palette, no generic stat-chip strips.
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
def ititle(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'
DOWN=f'<svg width="26" height="30" viewBox="0 0 26 30"><path d="M13 2 V22 M5 15 l8 8 l8 -8" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
DOWNR=f'<svg width="26" height="30" viewBox="0 0 26 30"><path d="M13 2 V22 M5 15 l8 8 l8 -8" fill="none" stroke="rgb({RED})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# 1. SPLIT - same model, two drivers: one-liner lane (drift, 1x) vs five-move lane (clean, 10x)
def split():
    def chip(txt,col,bd):
        return (f'<div style="font-family:DM Mono;font-size:14px;color:{col};background:{bd[0]};'
                f'border:1px solid {bd[1]};border-radius:10px;padding:8px 13px;margin-bottom:9px">{txt}</div>')
    left_chips="".join(chip(t,"#c98f7f",("rgba(200,70,35,.08)","rgba(200,70,35,.30)")) for t in ["it guesses","it drifts","you rewrite half"])
    moves=["1 a real brief","2 a memory file","3 real tools","4 guards","5 a plan gate"]
    right_chips="".join(chip(t,"#e6d6c2",("rgba(212,162,127,.10)","rgba(212,162,127,.34)")) for t in moves)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Same Claude. 10x gap.","THE DIFFERENCE")}
      <div style="display:flex;align-items:stretch;gap:20px;height:452px">
        <div style="flex:1;background:linear-gradient(160deg,#2a2320,#201b18);border:1px solid rgba(200,70,35,.24);border-radius:20px;padding:22px 22px 26px;display:flex;flex-direction:column;align-items:center">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#c98f7f;align-self:flex-start">DEFAULT DRIVER</div>
          <div style="margin-top:14px;width:100%;background:#17130f;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:16px 18px;font-family:DM Mono;font-size:17px;color:#b7b0a4">&gt; just fix it</div>
          <div style="margin:12px 0 8px">{DOWNR}</div>
          <div style="width:100%">{left_chips}</div>
          <div style="margin-top:auto;font-family:DM Sans;font-weight:900;font-size:72px;color:rgb({RED});line-height:1">1x</div>
        </div>
        <div style="align-self:center;display:flex;flex-direction:column;align-items:center;gap:8px">
          <div style="width:1px;height:150px;background:linear-gradient(#0000,rgba(255,255,255,.16),#0000)"></div>
          <div style="font-family:DM Mono;font-size:14px;letter-spacing:.16em;color:#8f8f85;background:#211e1a;border:1px solid rgba(255,255,255,.12);border-radius:999px;padding:9px 12px">VS</div>
          <div style="width:1px;height:150px;background:linear-gradient(#0000,rgba(255,255,255,.16),#0000)"></div>
        </div>
        <div style="flex:1;background:linear-gradient(160deg,#38322b,#241f1a);border:1.5px solid rgba(212,162,127,.4);border-radius:20px;padding:22px 22px 26px;display:flex;flex-direction:column;align-items:center;box-shadow:inset 0 0 34px rgba(212,162,127,.08)">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC});align-self:flex-start">SET UP RIGHT</div>
          <div style="margin-top:14px;width:100%">{right_chips}</div>
          <div style="margin:4px 0 6px">{DOWN}</div>
          <div style="margin-top:auto;font-family:DM Sans;font-weight:900;font-size:72px;color:rgb({ACC});line-height:1;text-shadow:0 0 34px rgba(212,162,127,.5)">10x</div>
        </div>
      </div>
      {cap("the model never changed. the five setup moves did.")}</div>'''

# 2. BRIEF - IVORY paper spec: struck vague one-liner ghost, then 4 checked contract rows
def brief():
    rows=[("SCOPE","rate-limit the API"),("FILES","src/api/*, middleware/"),
          ("DO NOT TOUCH","auth, db schema"),("DONE","429s + tests pass")]
    body=""
    for k,v in rows:
        body+=(f'<div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.55);'
               f'border:1px solid rgba(120,95,60,.16);border-radius:14px;padding:15px 18px;margin-bottom:12px">'
               f'<svg width="24" height="24" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(150,86,45,.12)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
               f'<span style="flex-shrink:0;width:172px;font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#96562d">{k}</span>'
               f'<span style="font-family:DM Sans;font-weight:600;font-size:20px;color:#2a2016">{v}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ititle("Write a brief, not a line","MOVE 1")}
      <div style="display:flex;align-items:center;gap:13px;background:rgba(200,70,35,.06);border:1px dashed rgba(200,70,35,.4);border-radius:12px;padding:12px 18px;margin-bottom:20px">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#b0532f;flex-shrink:0">ONE-LINER</span>
        <span style="font-family:DM Sans;font-size:19px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">"fix the bug"</span>
        <span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:#b0532f;flex-shrink:0">vague guess</span></div>
      {body}
      {cap("give it scope, files, what NOT to touch, and what done looks like.","#8a745a")}</div>'''

# 3. MEMORY - radial config core (CLAUDE.md) feeding 5 standing-rule nodes, all live
def memory():
    cx,cy=210,214
    rules=[("STACK",-90),("STYLE",-18),("DO-NOT",54),("ICP",126),("DONE BAR",198)]
    lines=""; nodes=""
    for nm,a in rules:
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="33" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
                f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="430" height="430" viewBox="0 0 430 430">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">CLAUDE</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010">.md</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("Give it a memory","MOVE 2")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">One rules file holds your stack, style, hard NOs and your bar for done. It stops re-explaining yourself every single session.</div>
        {cap("standing rules load once, so it never guesses your setup again.")}</div></div>'''

# 4. TOOLS - hub-and-spokes: Claude Code hub wired out to 5 real tools
def tools():
    cx,cy=410,232; R=168
    items=[("run tests","-140"),("read repo","-70"),("shell","0"),("browser","70"),("MCP data","140")]
    # arrange 5 around a half-fan on the right? use full radial
    ring=""
    angs=[-125,-60,0,60,125]
    for (nm,_),a in zip(items,angs):
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.45)" stroke-width="3"/>'
               f'<rect x="{x-72:.0f}" y="{y-26:.0f}" width="144" height="52" rx="14" fill="url(#tchip)" stroke="rgba(255,255,255,.10)"/>'
               f'<circle cx="{x-50:.0f}" cy="{y:.0f}" r="6" fill="rgb({ACC})"/>'
               f'<text x="{x+8:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Let it use real tools","MOVE 3")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="th" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <linearGradient id="tchip" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient>
        <filter id="thg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {ring}
        <g filter="url(#thg)"><circle cx="{cx}" cy="{cy}" r="72" fill="url(#th)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">CLAUDE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">CODE</text>
      </svg>
      {cap("wired to your repo, tests and browser, not guessing from memory.")}</div>'''

# 5. GUARDS - ring gauge (0 off-spec merged) + a checklist of guard checks, one red block
def guards():
    r=78; circ=2*math.pi*r
    checks=[("dimensions exact",True),("fonts + palette",True),("no dead space",True),("bad diff",False)]
    rowsh=""
    for nm,ok in checks:
        col="rgb("+ACC+")" if ok else "rgb("+RED+")"
        icon=(f'<svg width="22" height="22" viewBox="0 0 24 24"><path d="M6 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
              if ok else f'<svg width="22" height="22" viewBox="0 0 24 24"><path d="M8 8l8 8M16 8l-8 8" fill="none" stroke="rgb({RED})" stroke-width="2.6" stroke-linecap="round"/></svg>')
        tag='PASS' if ok else 'BLOCKED'
        rowsh+=(f'<div style="display:flex;align-items:center;gap:14px;background:{"rgba(212,162,127,.06)" if ok else "rgba(200,70,35,.08)"};'
                f'border:1px solid {"rgba(212,162,127,.24)" if ok else "rgba(200,70,35,.34)"};border-radius:13px;padding:13px 16px;margin-bottom:11px">'
                f'{icon}<span style="font-family:DM Sans;font-weight:600;font-size:18px;color:#e6e0d4">{nm}</span>'
                f'<span style="margin-left:auto;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:{col}">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <div style="flex-shrink:0;position:relative;width:220px;height:220px">
        <svg width="220" height="220" viewBox="0 0 220 220">
          <defs><filter id="gg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
          <circle cx="110" cy="110" r="{r}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="16"/>
          <circle cx="110" cy="110" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="16" stroke-linecap="round" stroke-dasharray="{circ*0.93:.0f} {circ:.0f}" transform="rotate(-90 110 110)" filter="url(#gg)"/></svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:56px;color:#FAFAF7;line-height:1">0</span>
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:rgb({ACC});text-align:center">off-spec<br>merged</span></div></div>
      <div style="flex:1">
        {htitle("Install guards that block","MOVE 4")}
        {rowsh}
        {cap("hooks fail the bad output before it ever reaches you.")}</div></div>'''

# 6. PLAN - IVORY paper plan: 4 numbered steps, a YOUR-TAP gate stamp before EXECUTE
def plan():
    steps=[("1","map the files it will touch"),("2","write the failing tests"),
           ("3","implement, run, self-check"),("4","verify the done bar")]
    body=""
    for n,t in steps:
        body+=(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:13px">'
               f'<div style="flex-shrink:0;width:38px;height:38px;border-radius:11px;background:#96562d;display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:19px;color:#fdfbf6">{n}</div>'
               f'<div style="flex:1;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.16);border-radius:12px;padding:13px 18px;font-family:DM Sans;font-weight:600;font-size:19px;color:#2a2016">{t}</div></div>')
    stamp=(f'<div style="display:flex;align-items:center;gap:16px;margin:18px 0 4px">'
           f'<div style="flex-shrink:0;width:100px;height:100px;border-radius:50%;border:3px solid #96562d;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-9deg);box-shadow:0 8px 18px rgba(150,86,45,.2)">'
           f'<span style="font-family:DM Sans;font-weight:900;font-size:19px;color:#96562d;line-height:1">YOUR</span>'
           f'<span style="font-family:DM Sans;font-weight:900;font-size:19px;color:#96562d;line-height:1">TAP</span></div>'
           f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#2a2016">Read the plan once, approve it.</div>'
           f'<div style="font-family:DM Mono;font-size:14px;color:#8a745a;margin-top:5px">then it runs all four steps unattended</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {ititle("Approve the plan, not keystrokes","MOVE 5")}
      {body}
      {stamp}
      {cap("stop babysitting every line. gate the plan, let it run the rest.","#8a745a")}</div>'''

# 7. PAYOFF - isometric stack of shipped result cards, a 10x badge on the stack
def payoff():
    rows=[("Auth refactor","shipped, tests green"),
          ("Billing dashboard","built from a brief"),
          ("11 open bugs","closed overnight")]
    cards=""
    for i,(a,b) in enumerate(rows):
        y=i*146
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:20px 24px;box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
                f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
                f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:23px;color:#FAFAF7">{a}</div>'
                f'<div style="font-family:DM Sans;font-size:16px;color:#a8a296">{b}</div></div>'
                f'<div style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">MERGED</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("Five moves, ten times out","THE PAYOFF")}
      <div style="perspective:2000px;height:492px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:600px;height:438px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:404px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:22px;padding:11px 26px;border-radius:999px;box-shadow:0 12px 26px rgba(212,162,127,.45)">10x the output</div></div></div>
      {cap("same day, same model: the setup is the whole multiplier.")}</div>'''

# 8. OPERATOR - the 5 moves converge into one Ultron operator (accent orb)
def operator():
    scat=[("brief",70,86),("memory",70,168),("tools",70,250),("guards",70,332),("gate",70,406)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+34} {y} C340 {y},360 246,520 246" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
               f'<rect x="{x-2}" y="{y-24}" width="150" height="48" rx="13" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
               f'<text x="{x+73}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Or ship all five at once","THE OPERATOR")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="ob" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="obg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#obg)"><circle cx="590" cy="246" r="118" fill="url(#ob)"/></g>
        <text x="590" y="234" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">ULTRON</text>
        <text x="590" y="266" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#3a2010">one operator</text>
        <text x="590" y="392" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8f8f85" letter-spacing=".06em">agents · router · memory · human gate</text>
      </svg>
      {cap("the five moves wired in: seven agents, a router and your gate.")}</div>'''

PANELS={"split":split(),"brief":brief(),"memory":memory(),"tools":tools(),
        "guards":guards(),"plan":plan(),"payoff":payoff(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src58"; os.makedirs(outd,exist_ok=True)
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
