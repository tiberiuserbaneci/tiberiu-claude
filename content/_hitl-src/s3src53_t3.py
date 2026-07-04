#!/usr/bin/env python3
# TIER 3 - SELL THE TOOL NOT THE HOUR. Eyes-bar standard: 8 unique hand-built coded scenes in clean
# rounded cards (CARD/CARDIV), warm palette, htitle + one mono caption each. NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. TRAPS - three crowded routes crossed out, converging on a CROWDED wall (dark)
def traps():
    lanes=[("AGENCY","too competitive",104),("COURSE","everyone is doing it",215),("FREELANCE","you rent out your hours",326)]
    body=""
    for nm,why,y in lanes:
        body+=(f'<rect x="4" y="{y-42}" width="200" height="84" rx="18" fill="#232019" stroke="rgba(255,255,255,.10)" stroke-width="1.5"/>'
          f'<text x="104" y="{y-3}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="23" fill="#d9d5cc">{nm}</text>'
          f'<text x="104" y="{y+23}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#8f8f85">{why}</text>'
          f'<line x1="212" y1="{y}" x2="512" y2="{y}" stroke="rgba({RED},.5)" stroke-width="2.5" stroke-dasharray="4 9"/>'
          f'<g stroke="rgb({RED})" stroke-width="4.2" stroke-linecap="round"><line x1="352" y1="{y-13}" x2="378" y2="{y+13}"/><line x1="378" y1="{y-13}" x2="352" y2="{y+13}"/></g>')
    wall=(f'<rect x="540" y="52" width="150" height="326" rx="22" fill="rgba({RED},.12)" stroke="rgba({RED},.5)" stroke-width="2"/>'
      f'<text x="615" y="215" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="27" fill="rgb({RED})" transform="rotate(-90 615 215)">CROWDED</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Three roads, all jammed","THE OLD WAY")}
      <svg width="700" height="430" viewBox="0 0 700 430" style="display:block;margin:0 auto">{body}{wall}</svg>
      {cap("agency, course, freelance - the same three plays everyone already runs.")}</div>'''

# 2. PRODUCT - one isometric tool box, cloned into a stack of copies (IVORY)
def product():
    def box(cx,cy,s,op,label):
        w=110*s; h=120*s
        top=f'{cx},{cy-h} {cx+w},{cy-h+62*s} {cx},{cy-h+124*s} {cx-w},{cy-h+62*s}'
        lf=f'{cx-w},{cy-h+62*s} {cx},{cy-h+124*s} {cx},{cy+h} {cx-w},{cy+h-62*s}'
        rf=f'{cx+w},{cy-h+62*s} {cx},{cy-h+124*s} {cx},{cy+h} {cx+w},{cy+h-62*s}'
        g=(f'<polygon points="{top}" fill="#e6c49f" opacity="{op}"/>'
           f'<polygon points="{lf}" fill="#c39468" opacity="{op}"/>'
           f'<polygon points="{rf}" fill="#96562d" opacity="{op}"/>')
        if label:
            g+=(f'<text x="{cx-w/2}" y="{cy-14}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#fbf3e6" transform="rotate(31 {cx-w/2} {cy-14})">AI TOOL</text>'
                f'<text x="{cx+w/2}" y="{cy-14}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" transform="rotate(-31 {cx+w/2} {cy-14})">v1.0</text>')
        return g
    ghosts=box(470,168,0.62,0.28,False)+box(430,196,0.62,0.5,False)
    tag=('<g transform="translate(392,70)"><rect x="0" y="0" width="118" height="52" rx="14" fill="#96562d"/>'
      '<circle cx="20" cy="26" r="7" fill="#fdfbf6"/>'
      '<text x="70" y="34" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#fdfbf6">$197</text></g>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("One tool, infinite copies","THE PRODUCT","#2a2016")}
      <svg width="700" height="440" viewBox="0 0 700 440" style="display:block;margin:0 auto">
        {ghosts}
        <ellipse cx="290" cy="400" rx="180" ry="26" fill="rgba(120,90,55,.16)"/>
        {box(290,230,1.0,1.0,True)}
        {tag}
        <text x="290" y="420" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8a745a" letter-spacing=".08em">built once - shipped to every buyer</text>
      </svg>
      {cap("a small paid tool people actually need, cloned for every sale.","#8a745a")}</div>'''

# 3. AUTOPILOT - overnight sale pings ticking into a running total (dark)
def autopilot():
    pings=[("02:14","AI Notion OS","$197"),("03:41","Prompt Pack","$49"),
           ("04:58","AI Notion OS","$197"),("06:22","Resume Fixer","$89"),("07:10","AI Notion OS","$197")]
    bars="".join(f'<div style="width:12px;height:{h}px;background:rgb({ACC});border-radius:3px;opacity:{o}"></div>' for h,o in [(22,.4),(38,.6),(30,.5),(52,.9),(41,.7),(60,1),(46,.8)])
    tot=(f'<div style="width:296px;flex-shrink:0;background:#201d19;border:1px solid rgba(212,162,127,.28);border-radius:22px;padding:24px 26px;display:flex;flex-direction:column">'
      f'<div style="display:flex;align-items:center;gap:9px"><span style="width:11px;height:11px;border-radius:50%;background:rgb({ACC})"></span><span style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:#8f8f85">TOTAL BANKED</span></div>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:52px;color:#FAFAF7;margin:6px 0 2px;letter-spacing:-1px">$284,120</div>'
      f'<div style="font-family:DM Sans;font-size:16px;color:rgb({ACC})">312 sales, zero calls</div>'
      f'<div style="display:flex;align-items:flex-end;gap:9px;height:64px;margin-top:auto;padding-top:16px">{bars}</div>'
      f'<div style="font-family:DM Mono;font-size:12px;color:#8f8f85;margin-top:10px">sales per hour, last night</div></div>')
    rows=""
    for t,nm,amt in pings:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;background:#221f1b;border:1px solid rgba(212,162,127,.16);border-left:3px solid rgb({ACC});border-radius:14px;padding:11px 16px">'
          f'<div style="width:34px;height:34px;border-radius:10px;background:rgba(212,162,127,.16);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:16px;color:rgb({ACC})">$</div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:700;font-size:17px;color:#FAFAF7">New sale - {nm}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:#8f8f85">{t} - you were offline</div></div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC})">{amt}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It sold while you slept","AUTOPILOT")}
      <div style="display:flex;gap:26px;align-items:stretch">
        {tot}
        <div style="flex:1;display:flex;flex-direction:column;justify-content:space-between">{rows}</div>
      </div>
      {cap("no employees, no ads, no chasing - the storefront runs overnight.")}</div>'''

# 4. GAP - dense field of wanters, a rare few actually ship (dark)
def gap():
    cols,rows,sp,ox,oy=46,22,17,10,10
    hi={(3,7),(6,21),(9,38),(11,12),(14,30),(17,44),(20,5)}
    dots=""
    for r in range(rows):
        for c in range(cols):
            x=ox+c*sp; y=oy+r*sp
            if (r,c) in hi:
                dots+=f'<circle cx="{x}" cy="{y}" r="5.4" fill="rgb({ACC})" filter="url(#dg)"/>'
            else:
                dots+=f'<circle cx="{x}" cy="{y}" r="3.4" fill="rgba(250,250,247,.11)"/>'
    read=(f'<div style="position:absolute;right:0;bottom:2px;background:#201d19;border:1px solid rgba(212,162,127,.3);border-radius:18px;padding:16px 22px;box-shadow:0 20px 40px rgba(0,0,0,.5)">'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:40px;color:rgb({ACC});line-height:1">7 in 1,012</div>'
      f'<div style="font-family:DM Mono;font-size:13px;color:#c9c3b8;margin-top:4px">actually ship a product</div>'
      f'<div style="font-family:DM Mono;font-size:12px;color:#8f8f85;margin-top:2px">the rest just talk about it</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Everyone wants a tool","THE GAP")}
      <div style="position:relative;height:420px">
        <svg width="800" height="400" viewBox="0 0 800 400" style="position:absolute;left:0;top:0">
          <defs><filter id="dg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
          {dots}</svg>
        {read}
      </div>
      {cap("the demand is obvious. building and selling it is the wall few ever clear.")}</div>'''

# 5. BUILD - plain English flows through SENTINEL into a packaged live product (dark)
def build():
    nodes=[("Your idea","one sentence",78,140,False),("SENTINEL","writes + tests",278,232,False),
           ("Human gate","your one tap",478,140,False),("Live product","$197 - shipped",672,232,True)]
    conns=""
    for i in range(len(nodes)-1):
        x1=nodes[i][2]+80; y1=nodes[i][3]; x2=nodes[i+1][2]-80; y2=nodes[i+1][3]
        mx=(x1+x2)/2
        conns+=f'<path d="M{x1} {y1} C{mx} {y1},{mx} {y2},{x2} {y2}" fill="none" stroke="rgb({ACC})" stroke-width="3.4"/>'
    nds=""
    for nm,sub,x,y,hi in nodes:
        fill=f'url(#pnode)' if hi else "#232019"
        st=f"rgb({ACC})" if hi else "rgba(255,255,255,.12)"
        tc="#2a160c" if hi else "#FAFAF7"; sc="#3a2010" if hi else "#9a9488"
        glow=' filter="url(#ng)"' if hi else ""
        nds+=(f'<g{glow}><rect x="{x-80}" y="{y-38}" width="160" height="76" rx="18" fill="{fill}" stroke="{st}" stroke-width="{2.5 if hi else 1.5}"/></g>'
          f'<text x="{x}" y="{y-4}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="{tc}">{nm}</text>'
          f'<text x="{x}" y="{y+19}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="{sc}">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Describe it, it ships it","THE BUILD")}
      <svg width="800" height="430" viewBox="0 0 800 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="pnode" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="60%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {conns}{nds}
      </svg>
      {cap("SENTINEL turns plain English into a tested, packaged product - no engineer.")}</div>'''

# 6. BUYERS - CORTEX radar sweeps the web for the exact people with the pain (dark)
def buyers():
    cx,cy,R=205,215,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (64,127,190))
    blips=[("SaaS founders",305,155),("Solo agencies",125,100),("Course sellers",205,172),("Ecom ops",35,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#bb)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    rowsd=[("Notion power-users","hot",True),("Overworked agencies","warm",True),("No-code builders","warm",False)]
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px"><span style="font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">847</span><span style="font-family:DM Mono;font-size:13px;color:#8f8f85">ranked buyers</span></div>')
    for nm,tg,hot in rowsd:
        col=f"rgb({ACC})" if hot else "#8f8f85"
        lead+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:7px 0;border-top:1px solid rgba(255,255,255,.07)"><span style="font-family:DM Sans;font-size:16px;color:#d9d5cc">{nm}</span><span style="font-family:DM Mono;font-size:12px;color:{col}">{tg}</span></div>')
    lead+='</div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="410" height="410" viewBox="0 0 410 410">
        <defs><radialGradient id="swp" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="bb" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(62)):.0f} {cy-R*math.cos(math.radians(62)):.0f} Z" fill="url(#swp)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/>
        <text x="{cx}" y="{cy+30}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">CORTEX</text></svg>
      <div style="flex:1">
        {htitle("It found the buyers","THE BUYERS")}
        {lead}
        {cap("the exact people with the pain your tool removes, ranked by intent.")}
      </div></div>'''

# 7. STOREFRONT - one ROUTER hub, six agents run the whole shop (dark)
def storefront():
    cx,cy,R=410,214,168
    spokes=[("PULSE","writes",-90),("AMPLIFY","publishes",-30),("STRIKER","closes",30),
            ("SPECTER","reaches out",90),("COUNSEL","licenses",150),("CORTEX","sources",210)]
    lines=""; nodes=""
    for nm,role,a in spokes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.45)" stroke-width="2.6"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-3:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#e2ddd2">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Sans" font-size="13" fill="#8f8f85">{role}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One command runs the shop","THE STOREFRONT")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub2" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}{nodes}
        <g filter="url(#hg2)"><circle cx="{cx}" cy="{cy}" r="62" fill="url(#hub2)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">ROUTER</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">runs the shop</text>
      </svg>
      {cap("content, outreach, checkout, licensing - one desk, you just approve.")}</div>'''

# 8. MATH - a real team costs a payroll, this costs cents (IVORY)
def math_panel():
    team=[("Developer","$6,000",100),("Marketer","$5,000",83),("Ad spend","$4,400",73),("Virtual assistant","$3,000",50)]
    rows=""
    for nm,amt,w in team:
        rows+=(f'<div style="margin-bottom:14px"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:5px">'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:16px;color:#2a2016">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:14px;color:#96562d">{amt}</span></div>'
          f'<div style="height:14px;background:rgba(150,120,80,.14);border-radius:7px;overflow:hidden"><div style="width:{w}%;height:100%;background:rgb({RED});border-radius:7px"></div></div></div>')
    left=(f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#96562d;margin-bottom:14px">THE OLD STACK</div>{rows}'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1.5px solid rgba(150,120,80,.3);padding-top:12px;margin-top:4px">'
      f'<span style="font-family:DM Sans;font-weight:800;font-size:17px;color:#2a2016">Every month</span>'
      f'<span style="font-family:DM Sans;font-weight:900;font-size:28px;color:rgb({RED})">$18,400</span></div></div>')
    right=('<div style="width:230px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;justify-content:center;'
      'background:rgba(255,255,255,.55);border:1.5px solid rgba(150,90,45,.3);border-radius:22px;padding:26px 20px">'
      '<div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#96562d">ULTRON</div>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:52px;color:#2a2016;margin:8px 0 2px;line-height:1">cents</div>'
      '<div style="font-family:DM Sans;font-size:16px;color:#5a4634;text-align:center">per sale, pay-per-token</div>'
      f'<div style="width:80px;height:14px;background:rgb({ACC});border-radius:7px;margin-top:18px"></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("A team, or cents","THE MATH","#2a2016")}
      <div style="display:flex;gap:34px;align-items:stretch">{left}{right}</div>
      {cap("the old model needs a payroll. Ultron bills per token - cents a sale.","#8a745a")}</div>'''

PANELS={"traps":traps(),"product":product(),"autopilot":autopilot(),"gap":gap(),
        "build":build(),"buyers":buyers(),"storefront":storefront(),"math":math_panel()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src53"; os.makedirs(outd,exist_ok=True)
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
