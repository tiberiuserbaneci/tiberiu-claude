#!/usr/bin/env python3
# TIER 3 - THE PRICE OF FULL PRICE, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# ULTRON RULE: prices are CENTS. High $ figures appear ONLY as the competitor SaaS stack being
# replaced, never as an Ultron/operator cost.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"      # warm kraft accent
IVA="#96562d"          # ivory-slide accent
RED="200,70,35"        # muted red - expensive/bad states ONLY
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tc=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. TERMINAL - a Bloomberg-style terminal window mockup with a free open twin at $0
def terminal():
    # deterministic candle chart
    W,H=740,210; base=[40,58,44,72,60,92,78,120,104,138,122,158,140]
    n=len(base); step=W/(n-1)
    line="".join((f'{"M" if i==0 else "L"}{i*step:.0f} {H-30-v:.0f}') for i,v in enumerate(base))
    area=f"M0 {H-30} L"+" L".join(f'{i*step:.0f} {H-30-v:.0f}' for i,v in enumerate(base))+f" L{W} {H-30} Z"
    grid="".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="rgba(255,255,255,.05)"/>' for y in range(30,H,44))
    tick=lambda x:f'{x*step:.0f}'
    feeds=[("EURUSD","1.0842","+0.31%",True),("BRENT","82.14","-0.62%",False),("AI.IDX","4,118","+1.08%",True)]
    frows=""
    for sym,val,dl,up in feeds:
        col="#7fd39a" if up else f"rgb({RED})"
        frows+=(f'<div style="display:flex;align-items:center;gap:14px;padding:9px 0;border-top:1px solid rgba(255,255,255,.06)">'
          f'<span style="font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#c9c3b8;width:96px">{sym}</span>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#FAFAF7;flex:1">{val}</span>'
          f'<span style="font-family:DM Mono;font-size:14px;color:{col}">{dl}</span></div>')
    price=(f'<div style="display:flex;gap:16px;margin-top:18px">'
      f'<div style="flex:1;background:rgba(200,70,35,.08);border:1px solid rgba(200,70,35,.32);border-radius:16px;padding:15px 20px">'
      f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({RED})">LICENSED TERMINAL</div>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:32px;color:#FAFAF7;margin-top:3px">$24,000<span style="font-size:17px;color:#9a9488;font-weight:700">/yr</span></div></div>'
      f'<div style="flex:1;background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.34);border-radius:16px;padding:15px 20px">'
      f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">OPEN CLONE</div>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:32px;color:rgb({ACC});margin-top:3px">$0<span style="font-size:17px;color:#9a9488;font-weight:700"> same feeds</span></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One desk pays yearly","OPEN TWIN · $0")}
      <div style="background:#121110;border:1px solid rgba(255,255,255,.09);border-radius:20px;overflow:hidden;box-shadow:inset 0 2px 3px rgba(255,255,255,.06)">
        <div style="display:flex;align-items:center;gap:9px;padding:14px 20px;background:linear-gradient(180deg,#25221f,#191715);border-bottom:1px solid rgba(255,255,255,.07)">
          <span style="width:12px;height:12px;border-radius:50%;background:#d05a3a"></span><span style="width:12px;height:12px;border-radius:50%;background:#d9a24a"></span><span style="width:12px;height:12px;border-radius:50%;background:#7fb87f"></span>
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#8f8f85;margin-left:10px">MARKET TERMINAL 5.2</span>
          <span style="margin-left:auto;display:flex;align-items:center;gap:7px"><span style="width:8px;height:8px;border-radius:50%;background:#7fd39a;box-shadow:0 0 10px rgba(127,211,154,.8)"></span><span style="font-family:DM Mono;font-size:12px;color:#7fd39a">LIVE</span></span></div>
        <div style="padding:18px 22px 6px">
          <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="width:100%">
            <defs><linearGradient id="ta" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.30)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient></defs>
            {grid}
            <path d="{area}" fill="url(#ta)"/>
            <path d="{line}" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linejoin="round"/>
            <circle cx="{tick(n-1)}" cy="{H-30-base[-1]}" r="6" fill="rgb({ACC})"/>
          </svg>
          {frows}
        </div>
      </div>
      {price}
      {cap("same charts, same data feeds. the twin ships without the invoice.")}</div>'''

# 2. AGENCYFEE - horizontal cost bars: monthly agency retainer vs the open script (free)
def agencyfee():
    jobs=[("Ad audits",2800,"weekly report"),("Inbox triage",1900,"reply drafts"),("Model routers",3400,"pick the tier")]
    mx=3400; barw=560
    rows=""
    for nm,fee,desc in jobs:
        w=barw*fee/mx
        rows+=(f'<div style="margin-bottom:26px">'
          f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:9px">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:#8f8f85">{desc}</span></div>'
          f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:8px">'
          f'<div style="height:34px;width:{w:.0f}px;border-radius:9px;background:linear-gradient(90deg,rgba(200,70,35,.85),rgba(200,70,35,.45));display:flex;align-items:center;padding-left:14px;box-shadow:0 8px 18px rgba(200,70,35,.25)"><span style="font-family:DM Sans;font-weight:900;font-size:17px;color:#fff">${fee:,}<span style="font-size:12px;font-weight:700;opacity:.8">/mo</span></span></div>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({RED})">AGENCY</span></div>'
          f'<div style="display:flex;align-items:center;gap:16px">'
          f'<div style="height:34px;width:70px;border-radius:9px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.4);display:flex;align-items:center;justify-content:center"><span style="font-family:DM Sans;font-weight:900;font-size:16px;color:rgb({ACC})">FREE</span></div>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">OPEN SCRIPT · runs daily</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Agencies bill monthly","OPEN VERSIONS EXIST")}
      {rows}
      {cap("a retainer for a script that runs itself. the open version bills nothing.")}</div>'''

# 3. CATCH - IVORY receipt: sticker price $0, then the hidden line-items that make the real invoice
def catch():
    items=[("Setup + wiring","6 hrs"),("Updates","every month"),("Breakage","fixed by you"),("No gate","runs unsupervised"),("No memory","forgets each run")]
    lines=""
    for nm,val in items:
        lines+=(f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:11px 0;border-bottom:1px dashed rgba(120,95,60,.28)">'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:19px;color:#2a2016">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:15px;color:#96562d">{val}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Free, like a puppy</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">HIDDEN INVOICE</span></div>
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex-shrink:0;width:210px;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.2);border-radius:18px;padding:22px 20px;display:flex;flex-direction:column;justify-content:center;text-align:center">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#a08a68">STICKER PRICE</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:66px;color:#2a2016;line-height:1;margin:6px 0">$0</div>
          <div style="font-family:DM Mono;font-size:12px;color:#96562d;letter-spacing:.08em">before assembly</div>
        </div>
        <div style="flex:1">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#a08a68;margin-bottom:2px">WHAT IT ACTUALLY COSTS</div>
          {lines}
          <div style="display:flex;align-items:baseline;justify-content:space-between;padding-top:13px;margin-top:3px;border-top:2px solid rgba(200,70,35,.5)">
            <span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#2a2016">Assembly</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({RED})">the real bill</span></div>
        </div>
      </div>
      {cap("setup, updates, breakage, no gate, no memory. assembly is the hidden invoice.","#8a745a")}</div>'''

# 4. GLUE - tangled node graph: ten disconnected free tools, the mess between them is the job
def glue():
    W,H=760,470
    nodes=[("chart",120,90),("scraper",320,60),("mailer",540,96),("crm",650,220),
           ("router",560,360),("triage",360,410),("audit",150,380),("docs",60,250),
           ("pay",250,220),("notes",430,220)]
    # tangled edges (each tool alone, glue between them)
    E=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,0),(8,1),(8,3),(9,0),(9,4),(8,9),(2,9)]
    edges=""
    for a,b in E:
        x1,y1=nodes[a][1],nodes[a][2]; x2,y2=nodes[b][1],nodes[b][2]
        mx,my=(x1+x2)/2+((a*37)%50-25),(y1+y2)/2+((b*29)%50-25)
        edges+=f'<path d="M{x1} {y1} Q{mx:.0f} {my:.0f} {x2} {y2}" fill="none" stroke="rgba(200,70,35,.32)" stroke-width="2"/>'
    nd=""
    for nm,x,y in nodes:
        nd+=(f'<circle cx="{x}" cy="{y}" r="30" fill="#241f1a" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<circle cx="{x}" cy="{y}" r="30" fill="none" stroke="rgba(212,162,127,.22)" stroke-width="1" stroke-dasharray="3 5"/>'
          f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#c0bab0">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten free tools","= ELEVEN JOBS")}
      <div style="position:relative">
        <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">{edges}{nd}</svg>
        <div style="position:absolute;left:50%;bottom:2px;transform:translateX(-50%);background:rgba(200,70,35,.14);border:1px solid rgba(200,70,35,.4);border-radius:999px;padding:9px 22px">
          <span style="font-family:DM Sans;font-weight:900;font-size:17px;color:rgb({RED})">10 tools</span>
          <span style="font-family:DM Sans;font-weight:700;font-size:16px;color:#c9c3b8"> &nbsp;+ the glue &nbsp;=&nbsp; </span>
          <span style="font-family:DM Sans;font-weight:900;font-size:17px;color:#FAFAF7">11th job</span></div>
      </div>
      {cap("each one alone, logged out, forgetting you. the glue is the product.")}</div>'''

# 5. LAYER - isometric stack: mail/docs/CRM/payments under one operator layer with one memory
def layer():
    subs=[("PAYMENTS","Stripe · invoices",0),("CRM","pipeline · deals",1),("DOCS","proposals · notes",2),("MAIL","inbox · threads",3)]
    cards=""
    for nm,desc,i in subs:
        y=i*96
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:540px;background:linear-gradient(160deg,#3a352f,#252119);border:1.5px solid rgba(255,255,255,.12);border-radius:16px;padding:16px 22px;box-shadow:0 26px 40px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08);display:flex;align-items:center;gap:18px">'
          f'<div style="flex-shrink:0;width:12px;height:12px;border-radius:3px;background:rgba(212,162,127,.5)"></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#c9c3b8">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85">{desc}</div></div></div>')
    top=(f'<div style="position:absolute;left:0;top:-118px;width:540px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 58%,#9a5a35);border-radius:16px;padding:18px 22px;box-shadow:0 30px 46px rgba(212,162,127,.4), inset 0 2px 3px rgba(255,255,255,.4);display:flex;align-items:center;gap:16px">'
      f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(26,15,10,.18);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.4"><rect x="4" y="4" width="16" height="16" rx="4"/><circle cx="12" cy="12" r="3"/></svg></div>'
      f'<div><div style="font-family:DM Sans;font-weight:900;font-size:21px;color:#1a0f0a">OPERATOR LAYER</div>'
      f'<div style="font-family:DM Mono;font-size:12px;color:rgba(26,15,10,.7);letter-spacing:.08em">one desk · one memory</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("One operator layer","OVER THE STACK")}
      <div style="perspective:2000px;height:490px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(24deg) rotateZ(-11deg);width:540px;height:400px;position:relative">{cards}{top}</div></div>
      {cap("mail, docs, crm and payments wired into one desk that remembers.")}</div>'''

# 6. METER - a dial: the meter runs cents per run; the old retainers ran monthly (red high zone)
def meter():
    cx,cy,R=250,270,190
    def pt(deg,rad=R):
        a=math.radians(deg); return cx+rad*math.cos(a), cy+rad*math.sin(a)
    # top semicircle: 180 (left) .. 360 (right). cents zone left, retainer zone right.
    def arc(d0,d1,col,wd,rad=R):
        x0,y0=pt(d0,rad); x1,y1=pt(d1,rad)
        return f'<path d="M{x0:.0f} {y0:.0f} A{rad} {rad} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="{col}" stroke-width="{wd}" stroke-linecap="round"/>'
    ticks=""
    for d in range(180,361,20):
        xa,ya=pt(d,R-14); xb,yb=pt(d,R+2)
        ticks+=f'<line x1="{xa:.0f}" y1="{ya:.0f}" x2="{xb:.0f}" y2="{yb:.0f}" stroke="rgba(255,255,255,.2)" stroke-width="2"/>'
    nx,ny=pt(214,R-30)   # needle in the cents zone (low, left)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The meter runs cents","PAY PER RUN")}
      <div style="display:flex;align-items:center;gap:26px">
      <svg width="470" height="330" viewBox="0 0 500 330" style="flex-shrink:0">
        <defs><filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        {arc(180,255,f"rgb({ACC})",16)}
        {arc(255,300,"rgba(212,162,127,.28)",16)}
        {arc(300,360,f"rgb({RED})",16)}
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="15" fill="#2a2622" stroke="rgb({ACC})" stroke-width="3"/>
        <text x="{pt(196,R+30)[0]:.0f}" y="{pt(196,R+30)[1]:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">cents</text>
        <text x="{pt(344,R+30)[0]:.0f}" y="{pt(344,R+30)[1]:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({RED})">monthly</text>
        <text x="{cx}" y="{cy+58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="#FAFAF7">0.7c</text>
        <text x="{cx}" y="{cy+82}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">per run</text>
      </svg>
      <div style="flex:1;display:flex;flex-direction:column;gap:14px">
          <div style="background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.34);border-radius:14px;padding:16px 20px"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">ULTRON</div><div style="font-family:DM Sans;font-weight:900;font-size:23px;color:#FAFAF7">cents per run</div><div style="font-family:DM Sans;font-size:14px;color:#8f8f85">not per seat, not per logo</div></div>
          <div style="background:rgba(200,70,35,.07);border:1px solid rgba(200,70,35,.3);border-radius:14px;padding:16px 20px"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({RED})">OLD STACK</div><div style="font-family:DM Sans;font-weight:900;font-size:23px;color:#FAFAF7">$4,500 / month</div><div style="font-family:DM Sans;font-size:14px;color:#8f8f85">flat, whether you ran it or not</div></div>
      </div></div>
      {cap("pay per run, not per seat. the high bill only lives in the old stack.")}</div>'''

# 7. KEEP - free "gems" plug into the desk; every external action still parks for the operator's tap
def keep():
    gems=[("free scraper","web pulls"),("free charts","dashboards"),("free router","model picks")]
    rows=""
    for nm,role in gems:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.1);border-radius:16px;padding:14px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<svg width="34" height="34" viewBox="0 0 34 34" style="flex-shrink:0"><path d="M17 3 L29 12 L23 30 L11 30 L5 12 Z" fill="rgba(212,162,127,.16)" stroke="rgb({ACC})" stroke-width="2"/><path d="M5 12 H29 M17 3 L11 30 M17 3 L23 30" stroke="rgba(212,162,127,.5)" stroke-width="1.2" fill="none"/></svg>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div><div style="font-family:DM Sans;font-size:14px;color:#8f8f85">{role}</div></div>'
          # plug prong into the desk
          f'<div style="display:flex;align-items:center;gap:2px"><span style="width:22px;height:3px;background:rgb({ACC})"></span><span style="width:9px;height:16px;border-radius:2px;background:rgb({ACC})"></span></div>'
          f'<svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(127,211,154,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#7fd39a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#7fd39a;flex-shrink:0">GATED</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Keep the free gems","WIRED · GATED")}
      <div style="display:flex;flex-direction:column;gap:14px">{rows}</div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:16px;background:linear-gradient(160deg,#403a33,#241f1a);border:1px solid rgba(212,162,127,.34);border-radius:16px;padding:16px 20px">
        <div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.4);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><rect x="4" y="10" width="16" height="11" rx="3"/><path d="M8 10 V7 a4 4 0 0 1 8 0 v3"/></svg></div>
        <div><div style="font-family:DM Sans;font-weight:900;font-size:20px;color:#FAFAF7">THE DESK</div><div style="font-family:DM Sans;font-size:15px;color:#c9a583">every external action parks for your tap</div></div>
      </div>
      {cap("open tools plug in, memory shared, nothing fires without your gate.")}</div>'''

# 8. MATH - IVORY equation: knowledge is the discount, assembly is the price you actually pay
def math_panel():
    def box(label,big,sub,accent=False):
        col=IVA if accent else "#2a2016"
        bg="rgba(150,90,45,.10)" if accent else "rgba(255,255,255,.5)"
        bd="rgba(150,90,45,.4)" if accent else "rgba(120,95,60,.2)"
        return (f'<div style="flex:1;background:{bg};border:1px solid {bd};border-radius:18px;padding:20px 16px;text-align:center">'
          f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:#a08a68">{label}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:{col};line-height:1.05;margin:6px 0">{big}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8a745a">{sub}</div></div>')
    op=lambda s:f'<div style="font-family:DM Sans;font-weight:900;font-size:38px;color:#96562d;flex-shrink:0">{s}</div>'
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Knowledge is the discount</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">THE REAL MATH</span></div>
      <div style="display:flex;align-items:center;gap:16px;margin-bottom:24px">
        {box("FREE TWIN","$0","you found the open tool")}
        {op("+")}
        {box("ASSEMBLY","cents/run","the layer that wires it",True)}
        {op("=")}
        {box("OPERATOR","runs while you sleep","one desk, one memory",True)}
      </div>
      <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.5);border-left:4px solid #96562d;border-radius:12px;padding:16px 20px">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2" style="flex-shrink:0"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8Z"/></svg>
        <span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#2a2016">Know the free twin. Pay only for the layer that runs it overnight.</span>
      </div>
      {cap("assembly is the price. the discount is knowing what is already free.","#8a745a")}</div>'''

PANELS={"terminal":terminal(),"agencyfee":agencyfee(),"catch":catch(),"glue":glue(),
        "layer":layer(),"meter":meter(),"keep":keep(),"math":math_panel()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/freestack"; os.makedirs(outd,exist_ok=True)
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
