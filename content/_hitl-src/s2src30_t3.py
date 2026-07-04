#!/usr/bin/env python3
# TIER 3 - THE WEEKEND INSTALL, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. INSTALL - IVORY module board: a packed 3x3 grid of the 9 modules you wire once (7 agents +
# router + gate), each a warm tile with an index dot + one-line role. Scene type: tile grid.
def install():
    mods=[("ROUTER","picks the model tier"),("CORTEX","research briefs"),("SPECTER","cold outreach"),
          ("STRIKER","deal moves"),("PULSE","content in your voice"),("SENTINEL","ships the code"),
          ("AMPLIFY","posts per channel"),("COUNSEL","reviews contracts"),("GATE","your approval")]
    tiles=""
    for i,(nm,role) in enumerate(mods):
        tiles+=(f'<div style="width:246px;background:rgba(255,255,255,.55);border:1px solid rgba(150,120,80,.22);'
          f'border-radius:16px;padding:15px 17px;box-shadow:0 8px 18px rgba(120,95,60,.10);display:flex;align-items:center;gap:13px">'
          f'<div style="flex-shrink:0;width:34px;height:34px;border-radius:10px;background:linear-gradient(160deg,#e6b48f,#b06a40);'
          f'display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:15px;color:#2a160c;box-shadow:0 5px 11px rgba(150,90,45,.30)">{i+1}</div>'
          f'<div style="flex:1;min-width:0"><div style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:#2a2016;line-height:1">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:13px;color:#8a745a;margin-top:2px">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("You do not need courses","9 MODULES","#2a2016","#96562d")}
      <div style="display:flex;flex-wrap:wrap;gap:14px 14px;justify-content:center">{tiles}</div>
      {cap("one install, wired once, not a playlist of ten to binge.","#8a745a")}</div>'''

# 2. ROUTER - one job token routed down 3 tier lanes, SMART lane lit; cents on every lane
def router():
    lanes=[("LITE","quick lookups","0.02c",96,False),("SMART","daily execution","0.11c",230,True),("DEEP","hard judgement","0.40c",364,False)]
    hubx,hy=170,230; lx=470
    edges=""; cards=""
    for nm,role,cost,y,on in lanes:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; w=5 if on else 2.5
        edges+=f'<path d="M{hubx+64} {hy} C320 {hy},330 {y},{lx-6} {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 22px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:300px;top:{y-40}px;width:160px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 16px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:4px">{cost}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A brain that budgets itself","MODEL ROUTER")}
      <div style="position:relative;height:460px">
        <svg width="820" height="460" viewBox="0 0 820 460" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <rect x="10" y="{hy-28}" width="96" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="64" fill="url(#hub)"/></g>
          <text x="{hubx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{hy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        <div style="position:absolute;left:14px;top:206px;width:88px;font-family:DM Mono;font-size:12px;color:#c9c3b8;text-align:center">draft 12<br>follow-ups</div>
        {cards}
      </div>
      {cap("one job in, the cheapest tier that can actually do it - cents, not dollars.")}</div>'''

# 3. CORTEX - isometric stack of scored account briefs (research already ranked)
def cortex():
    rows=[("Northwind Robotics","hiring 3 ops roles","92"),
          ("Globex Systems","raised $4M in May","88"),
          ("Initech","no AI layer yet","81")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:25px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 17px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{c}</span>
            <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">FIT</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:38px 44px 44px">
      {htitle("400 accounts, ranked","ONE BRIEF")}
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:490px;position:relative">{cards}</div></div>
      {cap("people, companies and markets scored into one sorted brief overnight.")}</div>'''

# 4. SPECTER - vertical sequence timeline: opener -> follow-ups -> breakup, one reply lit
def specter():
    steps=[("DAY 1","Opener sent","the one specific trigger",False),
           ("DAY 3","Follow-up","a value nudge, no ask",False),
           ("DAY 5","Reply landed","meeting on the calendar",True),
           ("DAY 7","Breakup","held back, not needed",False)]
    rail='<div style="position:absolute;left:35px;top:36px;bottom:36px;width:3px;background:linear-gradient(180deg,rgb({A}),rgba(212,162,127,.2))"></div>'.replace("{A}",f"rgb({ACC})")
    rows=""
    for lab,subj,sub,lit in steps:
        dot=(f'<div style="position:relative;z-index:1;flex-shrink:0;width:26px;height:26px;border-radius:50%;margin-left:23px;'
             f'background:rgb({ACC});box-shadow:0 0 14px rgba(212,162,127,.6)"></div>' if lit else
             f'<div style="position:relative;z-index:1;flex-shrink:0;width:22px;height:22px;border-radius:50%;margin-left:25px;'
             f'background:#2a2724;border:2px solid rgba(212,162,127,.45)"></div>')
        pill=(f'<span style="margin-left:auto;font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:#1a0f0a;background:rgb({ACC});'
              f'padding:5px 13px;border-radius:999px;font-weight:600">REPLIED</span>' if lit else '')
        bd=f"rgba(212,162,127,.5)" if lit else "rgba(255,255,255,.10)"
        rows+=(f'<div style="position:relative;display:flex;align-items:center;gap:22px;margin-bottom:20px">{dot}'
          f'<div style="flex:1;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid {bd};border-radius:16px;padding:15px 20px;'
          f'box-shadow:0 14px 26px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07);display:flex;align-items:center;gap:16px">'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">{lab}</div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7;margin-top:1px">{subj}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85;margin-top:1px">{sub}</div></div>{pill}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The whole chase, drafted","MULTI-STEP")}
      <div style="position:relative;padding:6px 0">{rail}{rows}</div>
      {cap("opener, follow-ups and breakup written as one sequence, in your voice.")}</div>'''

# 5. STRIKER - deal kanban: four stages, each column packed with deal chips + a next-move footer
def striker():
    cols=[("QUALIFY",[("Acme Foods","$18k","new inbound"),("Vertex Ops","$9k","cold reply")],"book the demo"),
          ("DISCOVERY",[("Globex","$40k","pain mapped"),("Umbrella","$22k","budget found")],"map the pain"),
          ("PROPOSAL",[("Initech","$25k","plan sent"),("Soylent","$31k","in review")],"handle objection"),
          ("CLOSE",[("Hooli","$60k","verbal yes"),("Piper","$14k","signing")],"send the close plan")]
    colhtml=""
    for i,(stage,deals,move) in enumerate(cols):
        lit=(i==3)
        chips=""
        for nm,val,note in deals:
            chips+=(f'<div style="background:linear-gradient(160deg,#3a352f,#241f1a);border:1px solid rgba(255,255,255,.12);border-radius:13px;padding:13px 14px;'
              f'box-shadow:0 12px 22px rgba(0,0,0,.42)"><div style="font-family:DM Sans;font-weight:800;font-size:16px;color:#FAFAF7">{nm}</div>'
              f'<div style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC});margin-top:2px;line-height:1">{val}</div>'
              f'<div style="font-family:DM Mono;font-size:11px;color:#8f8f85;margin-top:5px;letter-spacing:.03em">{note}</div></div>')
        hbg=f"rgb({ACC})" if lit else "rgba(212,162,127,.16)"; hc="#1a0f0a" if lit else "#d9d5cc"
        colhtml+=(f'<div style="flex:1;display:flex;flex-direction:column;gap:11px">'
          f'<div style="background:{hbg};border-radius:11px;padding:9px 10px;text-align:center;font-family:DM Mono;font-size:12px;letter-spacing:.10em;color:{hc};font-weight:600">{stage}</div>'
          f'{chips}'
          f'<div style="background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.24);border-radius:11px;padding:11px 12px;font-family:DM Mono;font-size:11.5px;color:rgb({ACC});text-align:center;letter-spacing:.02em">next: {move}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every deal, its next move","PIPELINE")}
      <div style="display:flex;gap:15px;align-items:stretch">{colhtml}</div>
      {cap("qualify, discovery, objections and close plan, held per deal, not in your head.")}</div>'''

# 6. PULSE - IVORY voiceprint: waveform bars + a sample written in your voice + match readout
def pulse():
    heights=[26,44,70,52,88,110,72,120,90,132,104,150,116,140,96,126,80,110,66,92,54,74,40,58,30,46,24,38]
    bars=""
    n=len(heights)
    for i,h in enumerate(heights):
        op=0.9 if 8<=i<=19 else 0.5
        bars+=(f'<div style="width:9px;height:{h}px;border-radius:5px;background:linear-gradient(180deg,#c98b5f,#96562d);opacity:{op}"></div>')
    checks="".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["short lines","no hedging","your cadence"])
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("It writes in your voice","98% VOICE MATCH","#2a2016","#96562d")}
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:6px;height:158px;padding:0 6px;margin-bottom:22px">{bars}</div>
      <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4">
        "I killed nine tools last month. The one I kept did not have a chat box."</div>
      <div style="display:flex;gap:26px;margin-top:16px">{checks}</div>
      {cap("sampled from your real posts, banned words enforced on every draft.","#8a745a")}</div>'''

# 7. GATE - full-capability orb held on the operator's reins, memory core beneath, one lock
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Strong body. My reins.","POWER, HELD")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og)"><circle cx="200" cy="200" r="128" fill="url(#orb)"/></g>
        <text x="200" y="194" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="32" fill="#2a160c">FULL</text>
        <text x="200" y="228" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">CAPABILITY</text>
        <rect x="70" y="352" width="260" height="52" rx="14" fill="#211d19" stroke="rgba(212,162,127,.32)"/>
        <text x="200" y="384" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#c9c3b8">MEMORY CORE</text>
        <line x1="130" y1="326" x2="200" y2="352" stroke="rgba(212,162,127,.4)" stroke-width="2" stroke-dasharray="3 6"/>
        <line x1="270" y1="326" x2="200" y2="352" stroke="rgba(212,162,127,.4)" stroke-width="2" stroke-dasharray="3 6"/>
        <path d="M334 200 H610" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="130" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,168)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="306" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("every external move parks for your tap, drawing on one shared memory.")}</div>'''

# 8. OPERATOR - scattered agent nodes converge into one glowing assembled operator
def operator():
    scat=[("research",70,80),("outbound",70,200),("content",70,320),("deals",190,140),("code",190,260)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+30} {y} C340 {y},360 210,520 210" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="32" fill="#221f1b" stroke="rgba(255,255,255,.1)" stroke-width="1.5" opacity="0.75"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#a29b8e">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Assemble the operator","ONE SYSTEM")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="bod" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#bg2)"><circle cx="590" cy="210" r="122" fill="url(#bod)"/></g>
        <text x="590" y="198" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">ONE</text>
        <text x="590" y="232" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">LOGIN</text>
        <text x="590" y="368" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".08em">composed · gated · yours</text>
      </svg>
      {cap("one chat wires research, outbound, deals, content and code into one operator.")}</div>'''

PANELS={"install":install(),"router":router(),"cortex":cortex(),"specter":specter(),
        "striker":striker(),"pulse":pulse(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src30"; os.makedirs(outd,exist_ok=True)
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
