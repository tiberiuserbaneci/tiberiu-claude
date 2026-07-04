#!/usr/bin/env python3
# TIER 3 - SEVEN DEPARTMENTS, ONE DESK (adapt s3src19). Reframe: Ultron is the operations layer of
# the company - the 7 agents run departments, the queue/workflows run the back office. Each panel a
# UNIQUE hand-built coded scene on a clean rounded card, title + one caption. NO generic stat-chips.
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
# ivory header (matches the approved voice() ivory panel: dark ink title + espresso #96562d tag)
def hiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')

# 1. DEPARTMENTS - radial hub-and-spokes: one OPS core, 7 agents each staffing a department
def departments():
    cx,cy=306,250; R=178
    depts=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),
           ("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publish"),("COUNSEL","legal")]
    n=len(depts); spokes=""; nodes=""
    for i,(nm,fn) in enumerate(depts):
        a=-90+i*360/n
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.26)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="13.5" fill="#eae4d8">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+15:.0f}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="rgb({ACC})">{fn}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;text-align:center">
      {htitle("Seven desks, one payroll","THE ROSTER")}
      <svg width="612" height="520" viewBox="0 0 612 520" style="display:block;margin:0 auto">
        <defs><radialGradient id="hubd" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hgd" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#hgd)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#hubd)"/></g>
        <text x="{cx}" y="{cy-3}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a160c">OPS</text>
        <text x="{cx}" y="{cy+17}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">one core</text>
        {nodes}
      </svg>
      {cap("research, outbound, deals, content, code, publishing, legal - all staffed.")}</div>'''

# 2. QUEUE - two trays and a running drum: you fill QUEUE, the workflow fills GENERATED
def queue():
    reqs=[("Draft 12 follow-ups","SPECTER"),("Qualify 40 inbound","STRIKER"),
          ("Ship the pricing page","SENTINEL"),("Weekly numbers","CORTEX")]
    outs=[("12 emails, queued","SPECTER"),("40 leads, scored","STRIKER"),
          ("page live on main","SENTINEL"),("report, one page","CORTEX")]
    def qslip(t,who):
        return (f'<div style="background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.16);border-radius:13px;padding:12px 15px;margin-bottom:11px">'
          f'<div style="display:flex;align-items:center;justify-content:space-between">'
          f'<span style="font-family:\'DM Sans\';font-weight:600;font-size:16px;color:#d9d5cc">{t}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:10px;letter-spacing:.1em;color:#7a7468">WAITING</span></div>'
          f'<div style="font-family:\'DM Mono\';font-size:11.5px;color:rgb({ACC});margin-top:3px">{who}</div></div>')
    def oslip(t,who):
        return (f'<div style="background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-left:3px solid rgb({ACC});border-radius:13px;padding:12px 15px;margin-bottom:11px">'
          f'<div style="display:flex;align-items:center;justify-content:space-between">'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:16px;color:#FAFAF7">{t}</span>'
          f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div>'
          f'<div style="font-family:\'DM Mono\';font-size:11.5px;color:#8f8f85;margin-top:3px">{who} &middot; DONE</div></div>')
    teeth="".join(f'<line x1="{52+26*math.cos(math.radians(a)):.1f}" y1="{78+26*math.sin(math.radians(a)):.1f}" x2="{52+36*math.cos(math.radians(a)):.1f}" y2="{78+36*math.sin(math.radians(a)):.1f}" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round"/>' for a in range(0,360,45))
    reqhtml="".join(qslip(t,w) for t,w in reqs)
    outhtml="".join(oslip(t,w) for t,w in outs)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Drop the ask, collect the work","QUEUE / GENERATED")}
      <div style="display:flex;align-items:center;gap:14px;margin-top:4px">
        <div style="flex:1">
          <div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:12px">QUEUE &middot; <span style="color:#8f8f85">you drop the ask</span></div>
          {reqhtml}</div>
        <div style="width:104px;flex-shrink:0;display:flex;flex-direction:column;align-items:center">
          <svg width="104" height="140" viewBox="0 0 104 140">
            <defs><radialGradient id="grd" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
            <filter id="ggq" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
            {teeth}
            <g filter="url(#ggq)"><circle cx="52" cy="78" r="26" fill="url(#grd)"/></g>
            <circle cx="52" cy="78" r="9" fill="#2a160c"/>
            <path d="M18 40 h64 M74 32 l10 8 l-10 8" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <div style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:#9a9488;margin-top:2px">n8n runs</div>
        </div>
        <div style="flex:1">
          <div style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:12px">GENERATED &middot; <span style="color:#8f8f85">it drops the work</span></div>
          {outhtml}</div>
      </div>
      {cap("you fill one folder. the workflow fills the other.")}</div>'''

# 3. WORKFLOW - bezier DAG: one trigger fans through the agents and merges at a gated send
def workflow():
    W,H=820,470
    def node(x,y,w,h,tag,sub,hot=False,lock=False):
        fill="url(#trg)" if hot else "#2a2724"
        bd=f"rgb({ACC})" if hot else "rgba(255,255,255,.11)"
        tcol="#2a160c" if hot else "rgb("+ACC+")"
        scol="#3a2010" if hot else "#c9c3b8"
        lockg=(f'<g transform="translate({x+w-30},{y+h//2-13})"><rect x="0" y="9" width="20" height="15" rx="3" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/><path d="M4 9 V5 a6 6 0 0 1 12 0 v4" fill="none" stroke="rgb({ACC})" stroke-width="2.4"/></g>') if lock else ""
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{fill}" stroke="{bd}" stroke-width="{2.4 if hot else 1.5}"/>'
          f'<text x="{x+18}" y="{y+27}" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="{tcol}">{tag}</text>'
          f'<text x="{x+18}" y="{y+49}" font-family="DM Sans" font-weight="700" font-size="17" fill="{scol}">{sub}</text>'
          f'{lockg}')
    # geometry
    trg=(40,200,160,66); enr=(250,200,160,66); drf=(470,96,160,66); scr=(470,308,160,66); snd=(660,200,150,66)
    def cxr(n): return (n[0]+n[2],n[1]+n[3]//2)
    def cxl(n): return (n[0],n[1]+n[3]//2)
    def edge(a,b,col=f"rgba(212,162,127,.55)",wd=2.6):
        x1,y1=cxr(a); x2,y2=cxl(b); mx=(x1+x2)/2
        return f'<path d="M{x1} {y1} C{mx:.0f} {y1},{mx:.0f} {y2},{x2} {y2}" fill="none" stroke="{col}" stroke-width="{wd}"/>'
    edges=edge(trg,enr)+edge(enr,drf)+edge(enr,scr)+edge(drf,snd)+edge(scr,snd)
    nodes=(node(*trg,"TRIGGER","new lead lands",hot=True)+node(*enr,"CORTEX","enrich the account")
      +node(*drf,"SPECTER","draft the reply")+node(*scr,"STRIKER","score the fit")+node(*snd,"AMPLIFY","queue to send",lock=True))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The line runs on a trigger","AUTOMATION")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="trg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        {edges}{nodes}
      </svg>
      {cap("new lead in - enriched, scored, drafted, parked to send. no clicks.")}</div>'''

# 4. STRUCTURE (IVORY) - the vault-as-business folder tree, OPERATIONS + QUEUE + GENERATED lit
def structure():
    def fico(c): return f'<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="1.9" style="flex-shrink:0"><path d="M3 7h6l2 2h10v10H3z"/></svg>'
    rows=[(0,"CLIENTS","one folder per client",False),
          (0,"PROJECTS","one folder per project",False),
          (0,"OPERATIONS","how the company runs",True),
          (1,"workflows","the n8n triggers",True),
          (1,"sops","the standing orders",True),
          (0,"CONTENT","drafts, calendars, posts",False),
          (0,"FINANCES","income, expenses, invoices",False),
          (0,"RESEARCH","briefs and market intel",False),
          (0,"QUEUE","you drop requests here",True),
          (0,"GENERATED","the system drops output",True)]
    body=""
    for ind,nm,desc,hot in rows:
        namecol="#96562d" if hot else "#2a2016"
        pad=34*ind
        elbow=(f'<span style="color:#c3ac8c;font-family:\'DM Mono\';font-size:14px;margin-right:8px">&#9492;</span>') if ind else ""
        fw=700 if ind==0 else 600
        fs=19 if ind==0 else 16.5
        body+=(f'<div style="display:flex;align-items:center;gap:11px;padding:8px 0 8px {pad}px;border-bottom:1px solid rgba(120,95,60,.12)">'
          f'{elbow}{fico("#96562d" if hot else "#8a6a45")}'
          f'<span style="font-family:\'DM Sans\';font-weight:{fw};font-size:{fs}px;color:{namecol}">{nm}</span>'
          f'<span style="font-family:\'DM Sans\';font-size:15px;color:#8a745a">&#8212; {desc}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {hiv("The org chart is folders","ONE VAULT")}
      <div>{body}</div>
      {cap("clients to generated - the whole company, on disk.","#8a745a")}</div>'''

# 5. ROUTER - dispatch board: each job routed to a desk at the cheapest tier that works
def router():
    jobs=[("Enrich a new account","CORTEX","LITE","0.02c"),
          ("Write 12 follow-ups","SPECTER","SMART","0.11c"),
          ("Draft the MSA clause","COUNSEL","DEEP","0.40c"),
          ("Schedule the drop","AMPLIFY","LITE","0.02c"),
          ("Score 40 inbound","STRIKER","SMART","0.11c")]
    rows=""
    for job,dept,tier,cost in jobs:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:15px;padding:13px 18px;margin-bottom:11px;box-shadow:0 12px 22px rgba(0,0,0,.4), inset 0 2px 2px rgba(255,255,255,.06)">'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:600;font-size:17px;color:#e8e2d6">{job}</span>'
          f'<svg width="26" height="14" viewBox="0 0 26 14" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 7h20M17 2l6 5-6 5"/></svg>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:13px;letter-spacing:.06em;color:#eae4d8;background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.32);border-radius:9px;padding:6px 12px;min-width:96px;text-align:center">{dept}</span>'
          f'<span style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});border-radius:10px;padding:6px 14px;min-width:78px;box-shadow:0 6px 14px rgba(212,162,127,.35)">'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:14px;color:#1a0f0a;line-height:1">{tier}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:11px;color:rgba(26,15,10,.72)">{cost}</span></span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The router runs dispatch","JOB &rarr; DESK &rarr; TIER")}
      <div style="margin-top:4px">{rows}</div>
      {cap("each task to the right desk at the cheapest tier that works.")}</div>'''

# 6. THROUGHPUT (IVORY) - a shift's output: ring gauge + a packed contributor breakdown
def throughput():
    pct=92; r=74; circ=2*math.pi*r; dash=circ*pct/100
    contrib=[("SPECTER","emails sent",52),("CORTEX","briefs written",38),
             ("SENTINEL","fixes shipped",24),("AMPLIFY","posts scheduled",24)]
    mx=max(c for _,_,c in contrib)
    bars=""
    for nm,role,c in contrib:
        w=int(100*c/mx)
        bars+=(f'<div style="margin-bottom:13px"><div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:5px">'
          f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.06em;color:#2a2016">{nm} <span style="color:#8a745a;letter-spacing:0">{role}</span></span>'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:17px;color:#96562d">{c}</span></div>'
          f'<div style="height:9px;border-radius:6px;background:rgba(150,90,45,.14)"><div style="height:9px;border-radius:6px;width:{w}%;background:linear-gradient(90deg,#b87a4a,#96562d)"></div></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 32px">
      {hiv("One shift clears the queue","THROUGHPUT")}
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0;position:relative;width:200px;height:200px">
          <svg width="200" height="200" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="16"/>
            <circle cx="100" cy="100" r="{r}" fill="none" stroke="#96562d" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 100 100)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:\'DM Sans\';font-weight:900;font-size:50px;color:#2a2016;line-height:1">138</span>
            <span style="font-family:\'DM Mono\';font-size:12px;color:#96562d;margin-top:3px">of 150 cleared</span></div></div>
        <div style="flex:1">{bars}</div>
      </div>
      {cap("queued at nine, cleared by noon - one operator's morning.","#8a745a")}</div>'''

# 7. GATE - approval stack: outbound work parked as HELD, one APPROVED, released by your tap
def gate():
    orders=[("Send 12 cold emails","SPECTER","APPROVED"),
            ("Post the launch thread","AMPLIFY","HELD"),
            ("Sign the MSA","COUNSEL","HELD"),
            ("Wire the invoice","STRIKER","HELD")]
    rows=""
    for act,dept,st in orders:
        ok=(st=="APPROVED")
        bd=f"rgb({ACC})" if ok else "rgba(250,250,247,.14)"
        style="solid" if ok else "dashed"
        badge=(f'<span style="display:flex;align-items:center;gap:6px;font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:rgb({ACC})"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>APPROVED</span>'
          if ok else
          f'<span style="display:flex;align-items:center;gap:6px;font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:#7a7468"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#7a7468" stroke-width="2.4"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>HELD</span>')
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:{"linear-gradient(158deg,#3a342c,#241f1a)" if ok else "rgba(250,250,247,.03)"};border:1.5px {style} {bd};border-radius:15px;padding:13px 18px;margin-bottom:12px">'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:12px;letter-spacing:.06em;color:{"#eae4d8" if ok else "#9a9488"};min-width:88px">{dept}</span>'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:{700 if ok else 600};font-size:17px;color:{"#FAFAF7" if ok else "#c9c3b8"}">{act}</span>'
          f'{badge}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing sends without your tap","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:26px;margin-top:4px">
        <div style="flex:1">{rows}</div>
        <div style="flex-shrink:0;width:196px;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <svg width="176" height="240" viewBox="0 0 176 240">
            <defs><radialGradient id="tapg" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
            <filter id="tgl" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
            <path d="M88 8 V44" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/>
            <g filter="url(#tgl)"><circle cx="88" cy="120" r="72" fill="url(#tapg)"/></g>
            <g transform="translate(88,120)"><path d="M-8 22 V-6 a8 8 0 0 1 16 0 V2 l10 3 a9 9 0 0 1 6 12 l-5 16 a12 12 0 0 1 -11 8 h-14 a12 12 0 0 1 -11 -9 l-6 -18 a7 7 0 0 1 12 -6 l6 6" fill="#2a160c" opacity="0.92"/></g>
            <text x="88" y="222" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
          </svg>
        </div>
      </div>
      {cap("every outbound move parks here. you tap, then it fires.")}</div>'''

# 8. OPERATOR - convergence: the departments, queue and workflow stream into one desk / one login
def operator():
    left=[("CORTEX",70,78),("SPECTER",70,178),("STRIKER",70,278),("PULSE",70,378),
          ("QUEUE",214,128),("WORKFLOW",214,328)]
    traces=""; nodes=""
    tx,ty=560,220
    for nm,x,y in left:
        mx=(x+tx)/2
        traces+=f'<path d="M{x+58} {y} C{mx:.0f} {y},{mx:.0f} {ty},{tx-4} {ty}" fill="none" stroke="rgba(212,162,127,.30)" stroke-width="2"/>'
        w=118 if len(nm)>7 else 92
        nodes+=(f'<rect x="{x}" y="{y-19}" width="{w}" height="38" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<text x="{x+w/2:.0f}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It runs from one desk","ONE OPERATOR")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <defs><linearGradient id="scr" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#211e1a"/></linearGradient>
        <filter id="scg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.34"/></filter></defs>
        {traces}
        <g filter="url(#scg)"><rect x="{tx}" y="{ty-118}" width="248" height="236" rx="26" fill="url(#scr)" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <rect x="{tx}" y="{ty-118}" width="248" height="42" rx="26" fill="rgba(0,0,0,.22)"/>
        <circle cx="{tx+26}" cy="{ty-97}" r="6" fill="rgb({ACC})"/><circle cx="{tx+46}" cy="{ty-97}" r="6" fill="rgba(212,162,127,.4)"/><circle cx="{tx+66}" cy="{ty-97}" r="6" fill="rgba(212,162,127,.4)"/>
        <text x="{tx+124}" y="{ty+4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="#FAFAF7">ONE DESK</text>
        <text x="{tx+124}" y="{ty+40}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">one login</text>
      </svg>
      {cap("seven desks, one queue, one login - that is the operating system.")}</div>'''

PANELS={"departments":departments(),"queue":queue(),"workflow":workflow(),"structure":structure(),
        "router":router(),"throughput":throughput(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src19"; os.makedirs(outd,exist_ok=True)
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
