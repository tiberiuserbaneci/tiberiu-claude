#!/usr/bin/env python3
# TIER 3 - A SECOND BRAIN THAT CLOSES (adapts the "Obsidian workflow plugins / connected second brain"
# scraped carousel into Ultron). Each panel is a UNIQUE hand-built coded scene filling a clean rounded
# card, title + one-line caption, NO generic stat-chip strips. Bar = eyes_t3.py / aibody_t3.py.
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

# 1. PILE - scattered disconnected note cards, dangling links that hook onto nothing (broken/red)
def pile():
    cards=[("ICP note",40,44,-5),("call 5/8",250,32,4),("pricing?",470,58,-3),("deal - acme",648,44,6),
           ("cold email",70,190,3),("follow up",300,200,-6),("docs link",520,206,5),("todo list",690,214,-4),
           ("meeting",150,340,-3),("idea dump",396,348,4),("stack audit",596,344,-5)]
    body=""
    for lbl,x,y,r in cards:
        body+=(f'<g transform="rotate({r} {x+75} {y+33})">'
          f'<rect x="{x}" y="{y}" width="150" height="66" rx="12" fill="#232320" stroke="rgba(255,255,255,.08)"/>'
          f'<rect x="{x}" y="{y}" width="150" height="7" rx="3" fill="rgba(212,162,127,.22)"/>'
          f'<text x="{x+16}" y="{y+40}" font-family="DM Mono" font-size="14" fill="#9a948a">{lbl}</text>'
          f'<line x1="{x+16}" y1="{y+52}" x2="{x+116}" y2="{y+52}" stroke="rgba(255,255,255,.07)" stroke-width="2"/>'
          '</g>')
    for x1,y1,x2,y2 in [(198,80,240,60),(432,244,476,244),(560,112,602,150)]:
        body+=(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="rgba(200,70,35,.5)" stroke-width="2.4" stroke-dasharray="4 6"/>'
          f'<line x1="{x2-6}" y1="{y2-6}" x2="{x2+6}" y2="{y2+6}" stroke="rgb(200,70,35)" stroke-width="2.4"/>'
          f'<line x1="{x2-6}" y1="{y2+6}" x2="{x2+6}" y2="{y2-6}" stroke="rgb(200,70,35)" stroke-width="2.4"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Notes that never connect","SCATTERED")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">{body}</svg>
      {cap("linear, disconnected, and nothing ever acts on them.")}</div>'''

# 2. GRAPH - IVORY radial knowledge graph, one VAULT core, dense linked note-nodes (Obsidian-graph look)
def graph():
    cx,cy,R=410,222,168
    nodes=[("ICP",-90),("Deals",-45),("Emails",0),("Signals",45),("Docs",90),("Pricing",135),("Contacts",180),("Pipeline",-135)]
    pts=[(cx+R*math.cos(math.radians(a)),cy+R*math.sin(math.radians(a))) for nm,a in nodes]
    links=""
    for x,y in pts:
        links+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.32)" stroke-width="1.6"/>'
    for i in range(len(pts)):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%len(pts)]
        links+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(150,90,45,.14)" stroke-width="1.2" stroke-dasharray="3 6"/>'
    blobs=""
    for i,(nm,a) in enumerate(nodes):
        x,y=pts[i]
        for k in range(2):
            sa=a+(k*44-22); sx=x+50*math.cos(math.radians(sa)); sy=y+50*math.sin(math.radians(sa))
            links+=f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{sx:.0f}" y2="{sy:.0f}" stroke="rgba(150,90,45,.20)" stroke-width="1.2"/>'
            blobs+=f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="9" fill="rgba(255,255,255,.78)" stroke="rgba(150,90,45,.3)"/>'
    for i,(nm,a) in enumerate(nodes):
        x,y=pts[i]
        blobs+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="33" fill="rgba(255,255,255,.85)" stroke="rgba(150,90,45,.4)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#5a4634">{nm}</text>')
    core=(f'<circle cx="{cx}" cy="{cy}" r="52" fill="url(#gcore)" filter="url(#gg)"/>'
      f'<text x="{cx}" y="{cy+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#fff">VAULT</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("Everything wired to one core","KNOWLEDGE GRAPH","#2a2016")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><radialGradient id="gcore" cx="38%" cy="32%"><stop offset="0%" stop-color="#c98b5f"/><stop offset="100%" stop-color="#96562d"/></radialGradient>
        <filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgba(150,90,45,.5)"/></filter></defs>
        {links}{blobs}{core}</svg>
      {cap("briefs, contacts, deals and docs, one linked memory.","#8a745a")}</div>'''

# 3. MEMORY - session lifelines stacking, each writing back into one persistent core
def memory():
    core_x,core_y=650,226
    rows=[("MON","3 briefs saved",70,.42),("TUE","2 deals updated",130,.58),("WED","emails logged",190,.72),("THU","signals added",250,.86),("TODAY","writing now",310,1.0)]
    body=""
    for lbl,sub,y,fill in rows:
        w=300
        body+=(f'<rect x="30" y="{y}" width="{w}" height="52" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.08)"/>'
          f'<rect x="30" y="{y}" width="{int(w*fill)}" height="52" rx="12" fill="rgba(212,162,127,{0.06+fill*0.12:.3f})"/>'
          f'<text x="46" y="{y+22}" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="rgb(212,162,127)">{lbl}</text>'
          f'<text x="46" y="{y+41}" font-family="DM Sans" font-size="15" fill="#c9c3b8">{sub}</text>'
          f'<path d="M330 {y+26} C452 {y+26},486 226,{core_x-96} 226" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>')
    core=(f'<g filter="url(#mg)"><circle cx="{core_x}" cy="{core_y}" r="92" fill="url(#mcore)"/></g>'
      f'<text x="{core_x}" y="{core_y-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>'
      f'<text x="{core_x}" y="{core_y+24}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">VAULT</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It never forgets a thing","PERSISTENT MEMORY")}
      <svg width="820" height="404" viewBox="0 0 820 404" style="display:block;margin:0 auto">
        <defs><radialGradient id="mcore" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb(212,162,127)"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb(212,162,127)" flood-opacity="0.4"/></filter></defs>
        {body}{core}</svg>
      {cap("every session writes back to the same core. context compounds.")}</div>'''

# 4. ROSTER - org tree, one root branching to the seven named agents
def roster():
    root_x,root_y=410,30
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    n=len(agents); bw=104; gap=13; total=n*bw+(n-1)*gap; startx=(820-total)/2
    by,bh=210,128
    lines=""; boxes=""
    for i,(nm,role) in enumerate(agents):
        x=startx+i*(bw+gap); cxb=x+bw/2
        lines+=f'<path d="M{root_x} {root_y+56} C{root_x} 150,{cxb:.0f} 150,{cxb:.0f} {by}" fill="none" stroke="rgba(212,162,127,.34)" stroke-width="1.8"/>'
        boxes+=(f'<rect x="{x:.0f}" y="{by}" width="{bw}" height="{bh}" rx="16" fill="#242320" stroke="rgba(212,162,127,.3)" stroke-width="1.5"/>'
          f'<circle cx="{cxb:.0f}" cy="{by+36}" r="15" fill="rgba(212,162,127,.14)" stroke="rgba(212,162,127,.5)"/>'
          f'<text x="{cxb:.0f}" y="{by+84}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" fill="#FAFAF7">{nm}</text>'
          f'<text x="{cxb:.0f}" y="{by+106}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{role}</text>')
    root=(f'<rect x="{root_x-110}" y="{root_y}" width="220" height="56" rx="16" fill="#2a2724" stroke="rgba(255,255,255,.12)"/>'
      f'<text x="{root_x}" y="{root_y+35}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="rgb(212,162,127)">VAULT MEMORY</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven hands on your notes","THE ROSTER")}
      <svg width="820" height="372" viewBox="0 0 820 372" style="display:block;margin:0 auto">{lines}{root}{boxes}</svg>
      {cap("research, outbound, deals, content, code, publishing, legal.")}</div>'''

# 5. ROUTER - plain-English job flows through the router to the one picked agent
def router():
    hubx,huby,job_y=290,205,205
    lanes=[("SPECTER","outbound",70,True),("CORTEX","research",158,False),("STRIKER","deals",246,False),("PULSE","content",334,False)]
    edges=""; cards=""
    for nm,role,y,on in lanes:
        col="rgb(212,162,127)" if on else "rgba(212,162,127,.28)"; w=5 if on else 2.4
        edges+=f'<path d="M{hubx+62} {huby} C420 {huby},440 {y+34},520 {y+34}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd="rgb(212,162,127)" if on else "rgba(255,255,255,.09)"
        glow="filter:drop-shadow(0 0 20px rgba(212,162,127,.32))" if on else ""
        pick='<span style="font-family:DM Mono;font-size:12px;color:rgb(212,162,127)">picked</span>' if on else ''
        cards+=(f'<div style="position:absolute;left:520px;top:{y}px;width:250px;{glow}">'
          f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:13px 16px;display:flex;justify-content:space-between;align-items:center">'
          f'<div><div style="font-family:DM Sans;font-weight:800;font-size:16px;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:13px;color:#8f8f85">{role}</div></div>{pick}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Plain English in, the right agent out","THE ROUTER")}
      <div style="position:relative;height:420px">
        <svg width="820" height="420" viewBox="0 0 820 420" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="rhub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb(212,162,127)"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb(212,162,127)" flood-opacity="0.42"/></filter></defs>
          <rect x="20" y="{job_y-34}" width="150" height="68" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>
          <path d="M170 {job_y} H{hubx-64}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" stroke-dasharray="2 10"/>
          {edges}
          <g filter="url(#rg)"><circle cx="{hubx}" cy="{huby}" r="62" fill="url(#rhub)"/></g>
          <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">ROUTER</text>
          <text x="{hubx}" y="{huby+16}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">reads intent</text>
        </svg>
        <div style="position:absolute;left:34px;top:{job_y-16}px;width:122px;font-family:DM Mono;font-size:12.5px;color:#c9c3b8;text-align:center">draft 12<br>follow-ups</div>
        {cards}
      </div>
      {cap("one line in, the right agent and the cheapest tier that works, cents each.")}</div>'''

# 6. WASTE - 960-dot capacity field, only a corner lit (what you actually wire)
def waste():
    cols,rowsN,sp,ox,oy=40,24,20,20,20
    dots=""
    for r in range(rowsN):
        for c in range(cols):
            x=ox+c*sp; y=oy+r*sp
            if c<9 and r<6:
                dots+=f'<circle cx="{x}" cy="{y}" r="4" fill="rgb(212,162,127)"/>'
            else:
                dots+=f'<circle cx="{x}" cy="{y}" r="3" fill="rgba(250,250,247,.10)"/>'
    frame=f'<rect x="{ox-8}" y="{oy-8}" width="{9*sp+2}" height="{6*sp+2}" rx="8" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="1.6"/>'
    label=f'<text x="{ox-4}" y="{oy+6*sp+30}" font-family="DM Mono" font-size="13" fill="rgb(212,162,127)">what you actually wire</text>'
    big=(f'<rect x="556" y="18" width="252" height="82" rx="14" fill="rgba(18,16,14,.82)"/>'
      f'<text x="792" y="58" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="40" fill="#FAFAF7">2,700+</text>'
      f'<text x="792" y="84" text-anchor="end" font-family="DM Mono" font-size="12.5" fill="#8f8f85">capabilities you never touch</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You use a fraction of what you hold","LATENT CAPACITY")}
      <svg width="820" height="504" viewBox="0 0 820 504" style="display:block;margin:0 auto">{dots}{frame}{label}{big}</svg>
      {cap("the power is already there. almost none of it is wired to act.")}</div>'''

# 7. GATE - wax-seal HUMAN GATE holding a column of queued action chips
def gate():
    seal=(f'<g filter="url(#sg)"><circle cx="185" cy="205" r="92" fill="url(#seal)"/></g>'
      f'<circle cx="185" cy="205" r="92" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="2" stroke-dasharray="3 7"/>'
      f'<g transform="translate(157,168)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="#2a160c" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="#2a160c" stroke-width="5"/></g>'
      f'<text x="185" y="300" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">HUMAN GATE</text>')
    chips=[("Send sequence","240 contacts",56),("Publish 3 posts","AMPLIFY queue",146),("Email your VC","1 message",236)]
    cbody=""
    for t,sub,y in chips:
        cbody+=(f'<div style="position:absolute;left:360px;top:{y}px;width:410px;background:#221f1b;border:1.5px solid rgba(212,162,127,.28);border-radius:16px;padding:14px 18px;display:flex;justify-content:space-between;align-items:center">'
          f'<div><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{t}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:#8f8f85">{sub}</div></div>'
          f'<span style="font-family:DM Mono;font-size:12px;color:rgb(212,162,127);border:1px solid rgba(212,162,127,.4);border-radius:999px;padding:5px 12px">awaiting tap</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <div style="position:relative;height:420px">
        <svg width="820" height="420" viewBox="0 0 820 420" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb(212,162,127)"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb(212,162,127)" flood-opacity="0.4"/></filter></defs>
          {seal}
        </svg>
        {cbody}
      </div>
      {cap("sequences, posts and emails queue for your one approval.")}</div>'''

# 8. PAYOFF - IVORY isometric stack of shipped result cards, out the door
def payoff():
    steps=[("BRIEF","12 accounts, ranked",0),("SEQUENCE","5 steps, at the gate",1),("PROPOSAL","drafted for review",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#fff,#f2e9da);border:1.5px solid rgba(150,120,80,.28);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(120,95,60,.28), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(150,90,45,.12);border:1px solid rgba(150,90,45,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:#96562d">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#2a2016">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 44px 34px">
      {htitle("It ships work, not just notes","THE PAYOFF","#2a2016")}
      <div style="perspective:1900px;height:452px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:420px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:392px;background:#96562d;color:#fff;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(150,90,45,.4)">Out the door</div></div></div>
      {cap("a brief, a sequence, a proposal, done while you run the day.","#8a745a")}</div>'''

PANELS={"pile":pile(),"graph":graph(),"memory":memory(),"roster":roster(),
        "router":router(),"waste":waste(),"gate":gate(),"payoff":payoff()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src06"; os.makedirs(outd,exist_ok=True)
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
