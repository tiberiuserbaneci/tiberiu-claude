#!/usr/bin/env python3
# TIER 3 - THE SUBSCRIPTION SWAP, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Angle: the paid SaaS stack a business already runs each month, mapped line-by-line to the Ultron
# agent that does the same job for cents. High $ appears ONLY as replaced competitor cost.
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
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LEDGER - IVORY ruled subscription book: the paid tools you already run, a $ column, a TOTAL rule,
# then one Ultron line in cents at the foot.
def ledger():
    rows=[("Zapier Pro","workflow automation","$73"),
          ("Apollo","outbound + lists","$99"),
          ("Clay","research + enrichment","$149"),
          ("Jasper","content drafts","$125"),
          ("Ahrefs","search visibility","$129"),
          ("Ironclad","contract review","$299")]
    body=""
    for i,(nm,role,cost) in enumerate(rows):
        body+=(f'<div style="display:flex;align-items:baseline;justify-content:space-between;'
          f'padding:11px 4px;border-bottom:1px solid rgba(120,95,60,.18)">'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:20px;color:#2a2016;min-width:150px">{nm}</span>'
          f'<span style="font-family:\'DM Sans\';font-size:16px;color:#8a745a;flex:1;padding:0 14px">{role}</span>'
          f'<span style="font-family:\'DM Mono\';font-weight:500;font-size:19px;color:#96562d">{cost}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:38px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">The bill you already run</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">MONTHLY LEDGER</span></div>
      <div>{body}</div>
      <div style="display:flex;align-items:baseline;justify-content:space-between;padding:14px 4px 4px;border-top:2.5px solid #96562d;margin-top:6px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:22px;color:#2a2016">Stack total</span>
        <span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:rgb({RED})">$874 / mo</span></div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:16px;
        background:rgba(150,86,45,.10);border:1px solid rgba(150,86,45,.30);border-radius:16px;padding:16px 20px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:21px;color:#2a2016">Ultron</span>
          <span style="font-family:'DM Sans';font-size:15px;color:#8a745a;margin-left:8px">does all six</span></div>
        <span style="font-family:'DM Sans';font-weight:900;font-size:28px;color:#96562d">$19 + cents</span></div>
      {cap("six line items you pay every month. one login bills the same jobs in cents.","#8a745a")}</div>'''

# 2. SWAP - bezier map: each paid tool on the left routes into the Ultron agent that eats its job
def swap():
    W,H=830,470
    pairs=[("Clay","CORTEX",70),("Apollo","SPECTER",166),("Jasper","PULSE",262),
           ("Copilot","SENTINEL",358),("Ironclad","COUNSEL",436)]
    # keep 5 rows inside H
    pairs=[("Clay","CORTEX",64),("Apollo","SPECTER",156),("Jasper","PULSE",248),
           ("Copilot","SENTINEL",340),("Ironclad","COUNSEL",420)]
    edges=""; ltiles=""; rtiles=""
    lx,rx=40,560
    for tool,agent,y in pairs:
        edges+=f'<path d="M{lx+232} {y} C400 {y},430 {y},{rx-8} {y}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.6"/>'
        edges+=f'<polygon points="{rx-10},{y-6} {rx+2},{y} {rx-10},{y+6}" fill="rgb({ACC})"/>'
        ltiles+=(f'<g><rect x="{lx}" y="{y-28}" width="232" height="56" rx="14" fill="#221f1b" stroke="rgba(200,70,35,.34)"/>'
          f'<text x="{lx+22}" y="{y-2}" font-family="DM Sans" font-weight="700" font-size="19" fill="#c9c3b8">{tool}</text>'
          f'<text x="{lx+22}" y="{y+17}" font-family="DM Mono" font-size="11.5" letter-spacing=".08em" fill="rgb({RED})">CANCELLED</text></g>')
        rtiles+=(f'<g><rect x="{rx}" y="{y-28}" width="230" height="56" rx="14" fill="url(#ag)" stroke="rgba(212,162,127,.5)"/>'
          f'<circle cx="{rx+30}" cy="{y}" r="9" fill="rgb({ACC})"/>'
          f'<text x="{rx+52}" y="{y+6}" font-family="DM Mono" font-weight="500" font-size="18" letter-spacing=".06em" fill="#FAFAF7">{agent}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:38px 40px 34px">
      {htitle("One agent per line item","THE SWAP")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><linearGradient id="ag" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#241f1a"/></linearGradient></defs>
        <text x="{lx+8}" y="26" font-family="DM Mono" font-size="12.5" letter-spacing=".14em" fill="rgb({RED})">PAID SEATS</text>
        <text x="{rx+8}" y="26" font-family="DM Mono" font-size="12.5" letter-spacing=".14em" fill="rgb({ACC})">ULTRON AGENTS</text>
        {edges}{ltiles}{rtiles}
      </svg>
      {cap("five subscriptions cancelled. five named agents pick up the exact same jobs.")}</div>'''

# 3. TOWER - a stacked-block cost tower ($874 of seats) next to a single cents sliver
def tower():
    blocks=[("Ironclad","$299"),("Clay","$149"),("Ahrefs","$129"),("Jasper","$125"),("Apollo","$99"),("Zapier","$73")]
    W,H=760,470
    bx=90; bw=280; unit=0.42  # px per $
    y=H-30; seg=""
    shades=["#4a4038","#443b33","#3e352e","#382f29","#322a24","#2b2420"]
    for i,(nm,cost) in enumerate(blocks):
        val=int(cost.replace("$","")); h=val*unit
        y0=y-h
        seg+=(f'<rect x="{bx}" y="{y0:.0f}" width="{bw}" height="{h:.0f}" rx="6" fill="{shades[i]}" stroke="rgba(255,255,255,.08)"/>'
          f'<text x="{bx+18}" y="{y0+h/2-2:.0f}" font-family="DM Sans" font-weight="700" font-size="17" fill="#d9d5cc">{nm}</text>'
          f'<text x="{bx+bw-18}" y="{y0+h/2-2:.0f}" text-anchor="end" font-family="DM Mono" font-size="15" fill="rgb({RED})">{cost}</text>')
        y=y0-4
    # cents sliver
    sx=560; sh=18
    return f'''<div style="width:900px;{CARD};padding:38px 44px 34px">
      {htitle("A tower of seats vs a sliver","STACKED COST")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><linearGradient id="sl" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#e6b48f"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="slg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.6"/></filter></defs>
        {seg}
        <text x="{bx+bw/2}" y="30" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="rgb({RED})">$874/mo</text>
        <rect x="{sx}" y="{H-30-sh}" width="150" height="{sh}" rx="6" fill="url(#sl)" filter="url(#slg)"/>
        <text x="{sx+75}" y="{H-30-sh-14}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="rgb({ACC})">cents</text>
        <text x="{sx+75}" y="{H-4}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">Ultron / run</text>
      </svg>
      {cap("stack the six invoices and it towers. the same work on Ultron is a sliver.")}</div>'''

# 4. SPOKES - radial ROUTER hub with the 7 agents around it (the roster that replaces the roles)
def spokes():
    cx,cy,R=306,236,176
    agents=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),
            ("PULSE","content"),("SENTINEL","code"),("AMPLIFY","publishing"),("COUNSEL","legal")]
    spk=""; nodes=""
    n=len(agents)
    for i,(nm,role) in enumerate(agents):
        a=-90+i*360/n
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spk+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.30)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#241f1a" stroke="rgba(212,162,127,.34)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="14" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Sans" font-size="12.5" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven roles, one login","THE ROSTER")}
      <svg width="612" height="500" viewBox="0 0 612 500" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {spk}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">picks the agent</text>
        {nodes}
      </svg>
      {cap("the roster you would hire and license one seat at a time, on one bill.")}</div>'''

# 5. FLOW - horizontal automation pipeline with a ROUTER brain node doing the thinking in the middle
def flow():
    W,H=830,430
    y=170
    steps=[("TRIGGER","new lead lands",120,"#2a2724"),("ACTION","follow-up sent",710,"#2a2724")]
    boxes=""
    for nm,sub,x,bg in steps:
        boxes+=(f'<rect x="{x-100}" y="{y-52}" width="200" height="104" rx="18" fill="{bg}" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x}" y="{y-10}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">{nm}</text>'
          f'<text x="{x}" y="{y+18}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#FAFAF7">{sub}</text>')
    bx=415
    think=(f'<line x1="220" y1="{y}" x2="{bx-92}" y2="{y}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
      f'<line x1="{bx+92}" y1="{y}" x2="610" y2="{y}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
      f'<g filter="url(#tg)"><circle cx="{bx}" cy="{y}" r="86" fill="url(#brain)"/></g>'
      f'<text x="{bx}" y="{y-8}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">THINK</text>'
      f'<text x="{bx}" y="{y+16}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">reads + decides</text>')
    tasks=[("scores the lead",bx-150),("writes the reply",bx),("logs to memory",bx+150)]
    tags=""
    for t,x in tasks:
        tags+=(f'<rect x="{x-92}" y="{y+128}" width="184" height="40" rx="12" fill="#211e1a" stroke="rgba(212,162,127,.22)"/>'
          f'<text x="{x}" y="{y+153}" text-anchor="middle" font-family="DM Sans" font-size="14.5" fill="#c9c3b8">{t}</text>')
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("The brain inside the automation","WORKFLOW")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><radialGradient id="brain" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="tg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {boxes}{think}{tags}
      </svg>
      {cap("zaps move data. the agent in the middle is the one that actually judges it.")}</div>'''

# 6. METER - IVORY cost gauge: a dial from $349 to zero, needle pinned at cents
def meter():
    cx,cy,R=306,300,220
    # semicircle gauge, needle near the low end
    def pt(a,r): return (cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))
    arc=""
    # major ticks 180 (left,high $) -> 0 (right, $0); needle near 8 deg (cents)
    for i in range(0,181,30):
        a=180-i
        x1,y1=pt(a,R); x2,y2=pt(a,R-24)
        arc+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(150,90,45,.5)" stroke-width="3"/>'
    labels=[("$349",180),("$175",90),("$0",0)]
    lab=""
    for t,a in labels:
        x,yy=pt(a,R+30)
        lab+=f'<text x="{x:.0f}" y="{yy:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#8a745a">{t}</text>'
    na=8; nx,ny=pt(na,R-40)
    x0,y0=pt(180,R); x1,y1=pt(0,R)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 30px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Priced by the token</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">PER 1,000 ROWS</span></div>
      <svg width="612" height="330" viewBox="0 0 612 330" style="display:block;margin:0 auto">
        <defs><radialGradient id="ndl" cx="40%" cy="40%"><stop offset="0%" stop-color="#b8703f"/><stop offset="100%" stop-color="#96562d"/></radialGradient></defs>
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="rgba(150,90,45,.22)" stroke-width="16" stroke-linecap="round"/>
        {arc}{lab}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="url(#ndl)" stroke-width="9" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#96562d"/>
        <text x="{cx}" y="{cy-46}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="44" fill="#2a2016">cents</text>
      </svg>
      {cap("the dial that competitors bill by the seat, Ultron bills by the token.","#8a745a")}</div>'''

# 7. CITED - AI answer mockup: your brand cited inside the model's answer (the search-visibility skill)
def cited():
    ans=('People running services teams point to a few operators. '
         '<tspan class="hl">Ultron</tspan> shows up most often for founders who')
    chips=[("claude.ai","cited"),("techcrunch.com","cited"),("g2.com","cited")]
    ch=""
    for i,(dom,tag) in enumerate(chips):
        ch+=(f'<div style="display:flex;align-items:center;gap:10px;background:rgba(212,162,127,.10);'
          f'border:1px solid rgba(212,162,127,.34);border-radius:12px;padding:9px 14px">'
          f'<span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC})"></span>'
          f'<span style="font-family:\'DM Mono\';font-size:14px;color:#d9d5cc">{dom}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:rgb({ACC});margin-left:2px">CITED</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Cited inside the answer","AI SEARCH")}
      <div style="background:#211e1a;border:1px solid rgba(255,255,255,.09);border-radius:20px;padding:22px 24px">
        <div style="display:flex;align-items:center;gap:11px;margin-bottom:16px">
          <div style="width:26px;height:26px;border-radius:50%;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.34)"></div>
          <span style="font-family:'DM Mono';font-size:14px;color:#8f8f85">"best AI operator for a small services team?"</span></div>
        <div style="font-family:'DM Sans';font-size:22px;line-height:1.5;color:#e6e0d4">
          People running services teams point to a few operators.
          <span style="color:rgb({ACC});font-weight:800;background:rgba(212,162,127,.14);padding:1px 8px;border-radius:6px">Ultron</span>
          shows up most for founders who want the whole stack in one login.</div>
        <div style="display:flex;gap:12px;margin-top:20px">{ch}</div>
      </div>
      {cap("PULSE writes what the models quote, so you are the name inside the answer.")}</div>'''

# 8. GATE - wax-seal HUMAN GATE: every cancel and every send waits for the operator's tap (closer)
def gate():
    cx,cy=200,210
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Every move waits for you","HUMAN GATE")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <radialGradient id="bloom" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.5)"/><stop offset="62%" stop-color="rgba(204,120,92,.10)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></radialGradient>
        <filter id="sh" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="rgba(0,0,0,.55)"/></filter>
        <filter id="spec" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="8"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="150" fill="url(#bloom)"/>
        <g filter="url(#sh)">
          {"".join(f'<line x1="{cx}" y1="{cy}" x2="{cx+128*math.cos(math.radians(a)):.0f}" y2="{cy+128*math.sin(math.radians(a)):.0f}" stroke="#8a4c2c" stroke-width="10"/>' for a in range(0,360,15))}
          <circle cx="{cx}" cy="{cy}" r="118" fill="url(#seal)"/></g>
        <circle cx="{cx}" cy="{cy}" r="118" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
        <g transform="translate({cx-34},{cy-40})"><rect x="0" y="30" width="68" height="50" rx="11" fill="none" stroke="#1a0f0a" stroke-width="7"/><path d="M13 30 V17 a21 21 0 0 1 42 0 v13" fill="none" stroke="#1a0f0a" stroke-width="7"/></g>
        <text x="{cx}" y="{cy+108}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="18" letter-spacing="4" fill="#1a0f0a">HELD</text>
        <ellipse cx="{cx-40}" cy="{cy-46}" rx="42" ry="22" fill="rgba(255,255,255,.28)" filter="url(#spec)" transform="rotate(-32 {cx-40} {cy-46})"/>
        <path d="M338 210 H548" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="560" y="140" width="200" height="140" rx="24" fill="#201d19" stroke="rgba(212,162,127,.5)" stroke-width="2"/>
        <text x="660" y="200" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#FAFAF7">your tap</text>
        <text x="660" y="234" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb({ACC})">sends or cancels</text>
      </svg>
      {cap("the agents draft the cancellations and the sends. nothing leaves without you.")}</div>'''

PANELS={"ledger":ledger(),"swap":swap(),"tower":tower(),"spokes":spokes(),
        "flow":flow(),"meter":meter(),"cited":cited(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src28"; os.makedirs(outd,exist_ok=True)
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
