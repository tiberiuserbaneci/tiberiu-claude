#!/usr/bin/env python3
# TIER 3 - SAME CLAUDE, SHAPED TO YOU. Angle: the identical brilliant model hands everyone the same
# generic output until you shape it with your context / voice / rules. Ultron is that shaping layer.
# Each panel a UNIQUE hand-built coded scene in a clean rounded card (WIRE-ITS-EYES bar). Helpers +
# __main__ copied verbatim from aibody_t3.py.
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
def htitiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CLONES - one bright model core fans identical DIM generic output cards (everyone gets the same)
def clones():
    core=(150,236)
    ys=[36,133,230,327,424]
    edges=""; cards=""
    for y in ys:
        cy=y+33
        edges+=f'<path d="M{core[0]+62} {core[1]} C320 {core[1]},330 {cy},428 {cy}" fill="none" stroke="rgba(250,250,247,.12)" stroke-width="2"/>'
        cards+=(f'<g><rect x="430" y="{y}" width="366" height="66" rx="15" fill="#211e1b" stroke="rgba(255,255,255,.07)"/>'
          f'<text x="452" y="{y+29}" font-family="DM Sans" font-weight="600" font-size="17" fill="#837d72">A clear, generic overview.</text>'
          f'<text x="452" y="{y+51}" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#5f5a51">OUTPUT &middot; IDENTICAL</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Brilliant, and everyone's","THE DEFAULT")}
      <svg width="820" height="490" viewBox="0 0 820 490" style="display:block;margin:0 auto">
        <defs><radialGradient id="cr" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}
        <g filter="url(#cg)"><circle cx="{core[0]}" cy="{core[1]}" r="66" fill="url(#cr)"/></g>
        <text x="{core[0]}" y="{core[1]-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#1a0f0a">ONE</text>
        <text x="{core[0]}" y="{core[1]+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#1a0f0a">MODEL</text>
        <text x="{core[0]}" y="{core[1]+96}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#8f8f85">same for all</text>
      </svg>
      {cap("out of the box it hands the same clean, generic answer to everyone.")}</div>'''

# 2. SPLIT - IVORY compare: DEFAULT bland column vs YOURS shaped column, VS divider
def split():
    def line(txt,col,strong=False):
        w="700" if strong else "500"
        return f'<div style="font-family:DM Sans;font-weight:{w};font-size:18px;color:{col};line-height:1.5;margin-bottom:9px">{txt}</div>'
    left=(line("We are excited to announce",'#9a8f7e')+line("a solution that leverages",'#9a8f7e')+line("best-in-class synergy.",'#9a8f7e'))
    right=(line("Killed nine tools last month.",'#2a2016',True)+line("Kept the one without",'#2a2016',True)+line("a chat box.",'#96562d',True))
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitiv("Same model. Two outputs.","DEFAULT VS YOURS")}
      <div style="display:flex;align-items:stretch;gap:0;margin-top:6px">
        <div style="flex:1;padding:22px 24px;background:rgba(120,95,60,.06);border:1px solid rgba(120,95,60,.16);border-radius:18px 0 0 18px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#a5967f;margin-bottom:16px">DEFAULT</div>
          {left}
          <div style="margin-top:18px;font-family:DM Mono;font-size:13px;color:#b0361f">sounds like a press release</div></div>
        <div style="position:relative;width:0;display:flex;align-items:center;justify-content:center;z-index:2">
          <div style="position:absolute;width:58px;height:58px;border-radius:50%;background:#96562d;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 26px rgba(150,90,45,.4);border:3px solid #fdfbf6">
            <span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#fdfbf6">VS</span></div></div>
        <div style="flex:1;padding:22px 24px;background:linear-gradient(160deg,rgba(212,162,127,.22),rgba(212,162,127,.08));border:1.5px solid #96562d;border-radius:0 18px 18px 0">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#96562d;margin-bottom:16px;text-align:right">YOURS</div>
          {right}
          <div style="margin-top:18px;font-family:DM Mono;font-size:13px;color:#96562d;text-align:right">sounds like your desk</div></div>
      </div>
      {cap("the exact same Claude. one reads like anyone. one reads like you.","#8a745a")}</div>'''

# 3. MEMORY - layered CLAUDE.md document, prior sheets stacked behind, context lines highlighted
def memory():
    rows=[("SELL","fractional CFO for 2-50p SaaS"),("PRICE","cents per token, no seats"),
          ("VOICE","blunt, short lines, no hype"),("NEVER","leverage, synergy, emoji")]
    body=""
    for k,v in rows:
        body+=(f'<div style="display:flex;align-items:center;gap:14px;padding:12px 16px;background:rgba(212,162,127,.07);border-left:3px solid rgb({ACC});border-radius:8px;margin-bottom:10px">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC});width:64px;flex-shrink:0">{k}</span>'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:17px;color:#e6e0d4">{v}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One file it reads first","YOUR CONTEXT")}
      <div style="position:relative;height:452px">
        <div style="position:absolute;left:40px;top:26px;right:80px;bottom:26px;background:#1a1815;border:1px solid rgba(255,255,255,.05);border-radius:20px"></div>
        <div style="position:absolute;left:26px;top:13px;right:66px;bottom:39px;background:#1e1c18;border:1px solid rgba(255,255,255,.06);border-radius:20px"></div>
        <div style="position:absolute;left:0;top:0;right:52px;bottom:52px;background:linear-gradient(160deg,#332d26,#221e1a);border:1px solid rgba(255,255,255,.12);border-radius:20px;box-shadow:0 30px 50px rgba(0,0,0,.5);padding:24px 26px">
          <div style="display:flex;align-items:center;gap:10px;padding-bottom:14px;margin-bottom:16px;border-bottom:1px solid rgba(255,255,255,.08)">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>
            <span style="font-family:DM Mono;font-weight:500;font-size:16px;color:#eae4d8">CLAUDE.md</span>
            <span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:rgb({ACC})">read every session</span></div>
          {body}
        </div>
      </div>
      {cap("what you sell, your pricing, your rules, loaded before it types a word.")}</div>'''

# 4. VOICE - IVORY: your samples -> waveform fingerprint -> matched output, style attributes
def voice():
    import random; random.seed(7)
    bars=""
    n=34
    for i in range(n):
        h=26+abs(math.sin(i*0.7))*70+random.random()*22
        x=i*(560/n)
        bars+=f'<rect x="{x:.0f}" y="{110-h/2:.0f}" width="9" height="{h:.0f}" rx="4" fill="#96562d" opacity="{0.55+0.45*(i%3==0):.2f}"/>'
    attrs=["short lines","blunt not warm","no hype words"]
    chips="".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in attrs)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitiv("It mirrors your cadence","YOUR VOICE")}
      <div style="background:rgba(255,255,255,.55);border:1px solid rgba(150,90,45,.18);border-radius:18px;padding:22px 24px">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:#96562d">5 SAMPLES IN</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#2a2016">98% match</span></div>
        <svg width="560" height="150" viewBox="0 0 560 150" style="display:block;margin:0 auto">
          <line x1="0" y1="110" x2="560" y2="110" stroke="rgba(150,90,45,.2)" stroke-width="1"/>
          {bars}</svg>
      </div>
      <div style="margin-top:18px;background:linear-gradient(160deg,rgba(212,162,127,.2),rgba(212,162,127,.06));border-left:4px solid #96562d;border-radius:12px;padding:16px 20px;font-family:DM Sans;font-size:20px;color:#2a2016;line-height:1.4">
        "That is a nice-to-have. Cut it."</div>
      <div style="display:flex;gap:22px;margin-top:16px">{chips}</div>
      {cap("sampled from five of your posts, your banned words enforced on every draft.","#8a745a")}</div>'''

# 5. RULES - a draft passes through your rule filter: banned tokens struck (muted red), clean out
def rules():
    banned=["leverage","synergy","game-changer","!!!","emoji"]
    tokchips=""
    for b in banned:
        tokchips+=(f'<span style="position:relative;display:inline-block;font-family:DM Mono;font-size:16px;color:#a06a55;padding:7px 15px;margin:6px;background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.3);border-radius:10px;text-decoration:line-through;text-decoration-color:rgb(200,70,35);text-decoration-thickness:2px">{b}</span>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Your banned words, gone","YOUR RULES")}
      <div style="display:flex;flex-direction:column;align-items:center;gap:0">
        <div style="width:560px;background:#221f1b;border:1px dashed rgba(255,255,255,.14);border-radius:14px;padding:16px 20px;text-align:center;font-family:DM Sans;font-size:17px;color:#8f8f85">raw draft, full of hype and filler</div>
        <svg width="30" height="34" viewBox="0 0 30 34"><path d="M15 2 V26 M6 18 l9 9 9-9" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="width:600px;background:linear-gradient(160deg,#332d26,#221e1a);border:1.5px solid rgb({ACC});border-radius:18px;padding:20px 22px;box-shadow:0 24px 40px rgba(0,0,0,.5)">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">RULE FILTER</span>
            <span style="margin-left:auto;font-family:DM Mono;font-size:13px;color:rgb(200,70,35)">5 struck</span></div>
          <div style="text-align:center">{tokchips}</div></div>
        <svg width="30" height="34" viewBox="0 0 30 34"><path d="M15 2 V26 M6 18 l9 9 9-9" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="width:560px;background:rgba(212,162,127,.1);border:1px solid rgba(212,162,127,.34);border-radius:14px;padding:16px 20px;text-align:center;font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">clean, in your rules, every time</div>
      </div>
      {cap("no hype, no corporate, no emoji if you say so, enforced on every output.")}</div>'''

# 6. TEAM - vertical context spine, 7 named agents branch off it, all inheriting your shape
def team():
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),
            ("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    spinex=150; top=30; bot=458
    branches=""
    step=(bot-top)/(len(agents)-1)
    for i,(nm,role) in enumerate(agents):
        y=top+step*i
        branches+=(f'<path d="M{spinex} {y:.0f} H210" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
          f'<circle cx="{spinex}" cy="{y:.0f}" r="6" fill="rgb({ACC})"/>')
    cards=""
    for i,(nm,role) in enumerate(agents):
        y=top+step*i
        cards+=(f'<div style="position:absolute;left:214px;top:{y-27:.0f}px;width:530px;display:flex;align-items:center;gap:16px;'
          f'background:linear-gradient(160deg,#312b25,#221e1a);border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:10px 18px">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7;width:120px">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:#9a9488;flex:1">{role}</span>'
          f'<span style="font-family:DM Mono;font-size:11.5px;letter-spacing:.08em;color:rgb({ACC})">+ your context</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven agents, one you","YOUR TEAM")}
      <div style="position:relative;height:490px">
        <svg width="760" height="490" viewBox="0 0 760 490" style="position:absolute;left:0;top:0">
          <defs><linearGradient id="sp" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></linearGradient></defs>
          <rect x="{spinex-9}" y="{top-8}" width="18" height="{bot-top+16}" rx="9" fill="url(#sp)"/>
          <text x="{spinex}" y="{(top+bot)/2-6:.0f}" text-anchor="middle" transform="rotate(-90 {spinex} {(top+bot)/2:.0f})" font-family="DM Mono" font-size="14" letter-spacing=".2em" fill="#1a0f0a" style="font-weight:700">YOUR CONTEXT</text>
          {branches}
        </svg>
        {cards}
      </div>
      {cap("one shaping layer feeds every agent, so nothing you built gets forgotten.")}</div>'''

# 7. GATE - shaped output parked in an approval queue, one big operator toggle (your tap)
def gate():
    rows=[("Cold email to 40 prospects","SPECTER",True),("Pricing page copy","PULSE",False),("MSA redline","COUNSEL",False)]
    items=""
    for txt,ag,active in rows:
        bd=f"rgb({ACC})" if active else "rgba(255,255,255,.09)"
        bg="linear-gradient(160deg,#352f28,#241f1a)" if active else "#211e1b"
        tog=(f'<div style="width:64px;height:34px;border-radius:999px;background:rgb({ACC});position:relative;box-shadow:inset 0 2px 4px rgba(0,0,0,.3)"><div style="position:absolute;right:3px;top:3px;width:28px;height:28px;border-radius:50%;background:#fdfbf6;box-shadow:0 2px 5px rgba(0,0,0,.4)"></div></div>'
          if active else
          f'<div style="width:64px;height:34px;border-radius:999px;background:#3a352f;position:relative"><div style="position:absolute;left:3px;top:3px;width:28px;height:28px;border-radius:50%;background:#6a645b"></div></div>')
        st=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">approve</span>' if active else f'<span style="font-family:DM Mono;font-size:12px;color:#7a746a">waiting</span>'
        items+=(f'<div style="display:flex;align-items:center;gap:18px;background:{bg};border:1.5px solid {bd};border-radius:16px;padding:18px 22px">'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#FAFAF7">{txt}</div>'
          f'<div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.08em;color:#9a9488;margin-top:3px">SHAPED BY {ag}</div></div>'
          f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px">{st}{tog}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Nothing ships untapped","YOUR CALL")}
      <div style="display:flex;flex-direction:column;gap:16px">{items}</div>
      <div style="margin-top:20px;display:flex;align-items:center;gap:14px;justify-content:center">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
        <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">HUMAN GATE</span>
        <span style="font-family:DM Mono;font-size:13px;color:#8f8f85">your tap sends it</span></div>
      {cap("every shaped output parks for your approval, then and only then it goes.")}</div>'''

# 8. OPERATOR - a generic draft funnels through 3 shaping bands into one warm YOUR OUTPUT
def operator():
    bands=[("CONTEXT","what you sell, your rules",520),("VOICE","sampled from your posts",400),("RULES","banned words enforced",280)]
    layers=""
    for i,(nm,sub,w) in enumerate(bands):
        y=120+i*82
        layers+=(f'<div style="width:{w}px;margin:0 auto;background:linear-gradient(160deg,#332d26,#221e1a);border:1px solid rgba(212,162,127,.3);border-radius:14px;padding:12px 20px;display:flex;align-items:center;gap:14px;box-shadow:0 14px 26px rgba(0,0,0,.4)">'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC});width:88px;flex-shrink:0">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:#c9c3b8">{sub}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Generic in, you out","THE SHIFT")}
      <div style="position:relative">
        <div style="width:620px;margin:0 auto 20px;background:#211e1b;border:1px dashed rgba(255,255,255,.14);border-radius:14px;padding:14px 20px;text-align:center;font-family:DM Sans;font-size:17px;color:#837d72">the same generic Claude draft</div>
        {layers}
        <div style="display:flex;justify-content:center;margin:14px 0 18px">
          <svg width="30" height="30" viewBox="0 0 30 30"><path d="M15 2 V22 M7 15 l8 8 8-8" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div style="width:520px;margin:0 auto;background:linear-gradient(160deg,rgba(212,162,127,.28),rgba(212,162,127,.1));border:1.5px solid rgb({ACC});border-radius:18px;padding:20px 24px;text-align:center;box-shadow:0 24px 44px rgba(212,162,127,.22)">
          <div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7">YOUR OPERATOR</div>
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.08em;color:rgb({ACC});margin-top:4px">works like a teammate who knows you</div></div>
      </div>
      {cap("context, voice and rules stack into one system, not a fresh generic chat.")}</div>'''

PANELS={"clones":clones(),"split":split(),"memory":memory(),"voice":voice(),
        "rules":rules(),"team":team(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src68"; os.makedirs(outd,exist_ok=True)
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
