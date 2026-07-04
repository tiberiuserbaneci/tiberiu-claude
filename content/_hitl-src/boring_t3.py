#!/usr/bin/env python3
# TIER 3 - BORING BEATS CLEVER, built to the WIRE-ITS-EYES bar: each of the 8 panels is a UNIQUE
# hand-coded scene (gauge / comparison / radial hub / dot field / node graph / timeline / area chart
# / iso stack) filling a clean rounded card, htitle + one mono caption. NO generic stat-chip strips,
# no clip-path cuts, no extruded walls. Warm palette, 1-2 ivory. Ultron prices in cents.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"        # warm accent
IVA="#96562d"            # ivory-card accent
BAD="rgb(200,70,35)"     # muted red, only for the losing / clever side
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'

def htitle(t,tag,ink="#FAFAF7",tagc=None):
    tagc=tagc or f"rgb({ACC})"
    return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
      f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
      f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:18px">{t}</div>'

# 1. WINDOW - gauge: the attention meter reads 1.7s, needle buried in the "no reading" danger arc
def window():
    cx,cy,R=306,330,196
    def pt(v,rr):
        th=math.radians(180-18*v)
        return cx+rr*math.cos(th), cy-rr*math.sin(th)
    ticks=""
    for v in range(0,11,2):
        x1,y1=pt(v,R); x2,y2=pt(v,R-20); lx,ly=pt(v,R-46)
        ticks+=(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(250,250,247,.28)" stroke-width="3"/>'
                f'<text x="{lx:.0f}" y="{ly+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{v}s</text>')
    tx0,ty0=pt(0,R-10); tx1,ty1=pt(10,R-10)
    dx1,dy1=pt(2,R-10)
    track=f'<path d="M{tx0:.1f} {ty0:.1f} A{R-10} {R-10} 0 0 1 {tx1:.1f} {ty1:.1f}" fill="none" stroke="rgba(250,250,247,.10)" stroke-width="16" stroke-linecap="round"/>'
    danger=f'<path d="M{tx0:.1f} {ty0:.1f} A{R-10} {R-10} 0 0 1 {dx1:.1f} {dy1:.1f}" fill="none" stroke="{BAD}" stroke-width="16" stroke-linecap="round"/>'
    nx,ny=pt(1.7,R-34)
    needle=(f'<line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" filter="url(#ng)"/>'
            f'<circle cx="{cx}" cy="{cy}" r="13" fill="rgb({ACC})"/>')
    chip=lambda t,lit:(f'<div style="flex:1;text-align:center;padding:15px 10px;border-radius:14px;'
        f'background:{"rgba(212,162,127,.12)" if lit else "rgba(250,250,247,.03)"};'
        f'border:1px solid {("rgba(212,162,127,.4)" if lit else "rgba(250,250,247,.09)")}">'
        f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:{("#FAFAF7" if lit else "#7a746a")};'
        f'{"" if lit else "text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)"}">{t}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You get 1.7 seconds","SCROLL SPEED")}
      <svg width="612" height="392" viewBox="0 0 612 392" style="display:block;margin:0 auto">
        <defs><filter id="ng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs>
        {track}{danger}{ticks}{needle}
        <text x="{cx}" y="{cy+66}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#FAFAF7">1.7s</text>
        <text x="{cx}" y="{cy+94}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="rgb({ACC})">to land the whole point</text>
      </svg>
      <div style="display:flex;gap:16px;margin-top:6px">
        {chip("the brain keeps SAFE + PREDICTABLE",True)}
        {chip("it drops SMART + SUBTLE",False)}
      </div>
      {cap("nobody is reading, they are scrolling. safe and legible wins by default.")}</div>'''

# 2. PROOF - comparison: same idea, two posts a week apart, 800 vs 47,000 views on a broken scale
def proof():
    W,H=760,452; base=396
    def bar(x,h,fill,glow):
        g="filter='url(#pg)'" if glow else ""
        return f'<rect x="{x}" y="{base-h}" width="150" height="{h}" rx="10" fill="{fill}" {g}/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Same idea, seven days apart","A/B ON MYSELF")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="pb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
          <filter id="pg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter>
        </defs>
        <line x1="70" y1="{base}" x2="{W-40}" y2="{base}" stroke="rgba(250,250,247,.14)" stroke-width="2"/>
        <!-- clever -->
        {bar(150,44,BAD,False)}
        <text x="225" y="{base-58}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="#c86e4a">800</text>
        <text x="225" y="{base+30}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".12em" fill="#9a9488">CLEVER</text>
        <text x="225" y="{base+52}" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#7a746a">the smart take</text>
        <!-- boring -->
        {bar(470,336,"url(#pb)",True)}
        <text x="545" y="{base-352}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="52" fill="#FAFAF7">47,000</text>
        <text x="545" y="{base+30}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".12em" fill="rgb({ACC})">BORING</text>
        <text x="545" y="{base+52}" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#c9a583">post daily for 30 days</text>
        <!-- multiplier -->
        <g transform="translate(348,150)">
          <rect x="0" y="0" width="74" height="52" rx="12" fill="#211d19" stroke="rgba(212,162,127,.4)"/>
          <text x="37" y="34" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="rgb({ACC})">59x</text>
        </g>
      </svg>
      {cap("clever chased asymmetric distribution. boring just showed up, every day.")}</div>'''

# 3. RULES - IVORY radial hub: BORING core, 4 tenet nodes wired around it
def rules():
    hubx,hy,R=408,246,196
    tenets=[("ONE IDEA","per post",-90),("PAYOFF","visible in 2 seconds",0),
            ("PLAIN WORDS","a 12-year-old gets",90),("FAMILIAR","format the feed knows",180)]
    spokes=""; nodes=""
    cw,ch=224,92
    for t,s,a in tenets:
        nx=hubx+R*math.cos(math.radians(a)); ny=hy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{hubx}" y1="{hy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgba(150,86,45,.45)" stroke-width="2.5"/>'
        nodes+=(f'<div style="position:absolute;left:{nx-cw/2:.0f}px;top:{ny-ch/2:.0f}px;width:{cw}px;height:{ch}px;'
          f'background:rgba(255,255,255,.62);border:1.5px solid rgba(150,86,45,.34);border-radius:16px;'
          f'display:flex;flex-direction:column;align-items:center;justify-content:center;'
          f'box-shadow:0 10px 22px rgba(120,95,60,.16), inset 0 1.5px 2px rgba(255,255,255,.9)">'
          f'<div style="font-family:\'DM Sans\';font-weight:900;font-size:21px;color:#2a2016;letter-spacing:.02em">{t}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8a745a;margin-top:2px">{s}</div></div>')
    box_w,box_h=816,500
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("The whole religion","4 RULES",ink="#17150F",tagc=IVA)}
      <div style="position:relative;width:{box_w}px;height:{box_h}px;margin:0 auto">
        <svg width="{box_w}" height="{box_h}" viewBox="0 0 {box_w} {box_h}" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="rh" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4c2c"/></radialGradient>
          <filter id="rhg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="rgba(150,86,45,.4)"/></filter></defs>
          {spokes}
          <g filter="url(#rhg)"><circle cx="{hubx}" cy="{hy}" r="80" fill="url(#rh)"/></g>
          <circle cx="{hubx}" cy="{hy}" r="80" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="1.5"/>
          <text x="{hubx}" y="{hy+8}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">BORING</text>
        </svg>
        {nodes}
      </div>
      {cap("one idea, plain words, a payoff you see fast, a shape the feed knows.","#8a745a")}</div>'''

# 4. EGO - dot field: CLEVER lights 1 (you), BORING lights the whole room (them)
def ego():
    def field(cols,rows,lit,size,gap):
        s=""
        for i in range(cols*rows):
            r,c=divmod(i,cols); x=c*(size+gap); y=r*(size+gap)
            on=i in lit
            fl="filter='url(#eg)'" if on else ""
            fc=("rgb("+ACC+")") if on else "rgba(250,250,247,.08)"
            s+=(f'<circle cx="{x+size/2:.0f}" cy="{y+size/2:.0f}" r="{size/2:.0f}" '
                f'fill="{fc}" {fl}/>')
        return s
    clever=field(6,6,{15},20,14)
    boring=field(6,6,set(range(36))-{5,30,33},20,14)
    fw=6*34-14
    col=lambda label,sub,svg,c1:(f'<div style="flex:1;text-align:center">'
        f'<svg width="{fw}" height="{fw}" viewBox="0 0 {fw} {fw}" style="display:block;margin:0 auto">'
        f'<defs><filter id="eg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>{svg}</svg>'
        f'<div style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.14em;color:{c1};margin-top:20px">{label}</div>'
        f'<div style="font-family:\'DM Sans\';font-size:16px;color:#8f8f85;margin-top:4px">{sub}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Clever is for you. Boring is for them.","WHO IT SERVES")}
      <div style="display:flex;align-items:flex-start;gap:20px;padding:6px 30px 0">
        {col("CLEVER","impresses 1 person: you",clever,BAD)}
        <div style="width:1px;align-self:stretch;background:rgba(250,250,247,.12);margin-top:10px"></div>
        {col("BORING","reaches the whole room",boring,f"rgb({ACC})")}
      </div>
      <div style="display:flex;gap:16px;margin-top:24px">
        <div style="flex:1;font-family:'DM Sans';font-size:17px;color:#7a746a;text-align:center;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)">sounding smart is a vanity metric</div>
        <div style="flex:1;font-family:'DM Sans';font-weight:700;font-size:17px;color:#c9a583;text-align:center">being understood is a growth metric</div>
      </div>
      {cap("write for the scroller who does not care that you are clever.")}</div>'''

# 5. FOURTEST - node graph: a DRAFT fans into 4 gate checks, all yes -> PUBLISH
def fourtest():
    W,H=830,432
    qs=[("Point lands in 2 seconds?",70),("One idea only?",178),("Your dad gets it?",286),("Format familiar?",394)]
    conns=""; chips=""
    dx,dcy=40,236; px=724
    for q,y in qs:
        conns+=(f'<path d="M{dx+96} {dcy} C240 {dcy},250 {y},330 {y}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>'
                f'<path d="M636 {y} C690 {y},690 {dcy},{px-4} {dcy}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="2.5"/>')
        chips+=(f'<g><rect x="330" y="{y-34}" width="306" height="68" rx="16" fill="url(#fc)" stroke="rgba(255,255,255,.10)"/>'
                f'<circle cx="368" cy="{y}" r="15" fill="rgba(127,211,154,.14)"/>'
                f'<path d="M361 {y}l4 4 8-9" fill="none" stroke="#7fd39a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<text x="398" y="{y+6}" font-family="DM Sans" font-weight="700" font-size="19" fill="#e8e2d6">{q}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Four boxes before every post","THE GATE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="fc" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#211e1a"/></linearGradient>
          <radialGradient id="fd" cx="38%" cy="30%"><stop offset="0%" stop-color="#3a352f"/><stop offset="100%" stop-color="#1c1a17"/></radialGradient>
          <radialGradient id="fp" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="fpg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter>
        </defs>
        {conns}
        <rect x="{dx}" y="{dcy-52}" width="96" height="104" rx="18" fill="url(#fd)" stroke="rgba(255,255,255,.1)"/>
        <text x="{dx+48}" y="{dcy-2}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#e6d6c2">DRAFT</text>
        <text x="{dx+48}" y="{dcy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">in</text>
        {chips}
        <g filter="url(#fpg)"><circle cx="{px+40}" cy="{dcy}" r="62" fill="url(#fp)"/></g>
        <text x="{px+40}" y="{dcy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">SHIP</text>
        <text x="{px+40}" y="{dcy+22}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">4 / 4 yes</text>
      </svg>
      {cap("one no sends it back. four yeses and only then does it ship.")}</div>'''

# 6. SKILL - timeline: PULSE runs the boring gate on a track before a draft reaches you (cents)
def skill():
    W,H=800,300; y=150; x0,x1=70,730
    stages=[("PULSE drafts","12 variants",0.0,"top"),
            ("scores to rules","one idea, plain words",0.34,"bot"),
            ("ranks the set","boring-first",0.67,"top"),
            ("you review","top 1 only",1.0,"bot")]
    track=f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgba(212,162,127,.3)" stroke-width="3"/>'
    fill=f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="rgb({ACC})" stroke-width="3" stroke-dasharray="1 0" opacity="0.6"/>'
    nodes=""
    for t,s,f,side in stages:
        cxp=x0+f*(x1-x0)
        nodes+=(f'<circle cx="{cxp:.0f}" cy="{y}" r="12" fill="rgb({ACC})" filter="url(#sk)"/>'
                f'<circle cx="{cxp:.0f}" cy="{y}" r="5" fill="#1a0f0a"/>')
        if side=="top":
            nodes+=(f'<text x="{cxp:.0f}" y="{y-58}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{t}</text>'
                    f'<text x="{cxp:.0f}" y="{y-36}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{s}</text>'
                    f'<line x1="{cxp:.0f}" y1="{y-26}" x2="{cxp:.0f}" y2="{y-12}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>')
        else:
            nodes+=(f'<text x="{cxp:.0f}" y="{y+46}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{t}</text>'
                    f'<text x="{cxp:.0f}" y="{y+68}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{s}</text>'
                    f'<line x1="{cxp:.0f}" y1="{y+12}" x2="{cxp:.0f}" y2="{y+26}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The desk runs the test first","PULSE GATE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="sk" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        {track}{fill}{nodes}
      </svg>
      <div style="display:flex;justify-content:center;margin-top:6px">
        <div style="display:inline-flex;align-items:center;gap:12px;background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:14px;padding:12px 20px">
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:#8f8f85">12 DRAFTS SCORED</span>
          <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:rgb({ACC})">5c</span>
          <span style="font-family:'DM Sans';font-size:15px;color:#c9a583">a batch, not dollars</span>
        </div>
      </div>
      {cap("you never see the clever draft, it loses before it reaches your desk.")}</div>'''

# 7. CLIENT - IVORY area chart: one trader, 2K to 30K in 25 days on the boring format
def client():
    W,H=760,400; x0,x1=78,700; by=320; top=48
    days=[0,3,6,9,12,16,20,25]; vals=[2,3,5,7,10,15,22,30]
    def X(d): return x0+d/25*(x1-x0)
    def Y(v): return by-(v/32)*(by-top)
    pts=[(X(d),Y(v)) for d,v in zip(days,vals)]
    line="M "+" L ".join(f"{x:.0f} {y:.0f}" for x,y in pts)
    area=f"M {X(0):.0f} {by} L "+" L ".join(f"{x:.0f} {y:.0f}" for x,y in pts)+f" L {X(25):.0f} {by} Z"
    grid=""
    for gv in (10,20,30):
        gy=Y(gv)
        grid+=(f'<line x1="{x0}" y1="{gy:.0f}" x2="{x1}" y2="{gy:.0f}" stroke="rgba(120,95,60,.16)" stroke-width="1"/>'
               f'<text x="{x0-10}" y="{gy+5:.0f}" text-anchor="end" font-family="DM Mono" font-size="13" fill="#a08a68">{gv}K</text>')
    ex,ey=pts[-1]
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("One trader switched formats","CLIENT PROOF",ink="#17150F",tagc=IVA)}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="car" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(150,86,45,.34)"/><stop offset="100%" stop-color="rgba(150,86,45,0)"/></linearGradient>
          <filter id="cd" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
        </defs>
        {grid}
        <path d="{area}" fill="url(#car)"/>
        <path d="{line}" fill="none" stroke="{IVA}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="{X(0):.0f}" cy="{Y(2):.0f}" r="7" fill="#8a745a"/>
        <text x="{X(0):.0f}" y="{Y(2)+30:.0f}" text-anchor="start" font-family="DM Mono" font-size="13" fill="#8a745a">Day 0 · 2K</text>
        <circle cx="{ex:.0f}" cy="{ey:.0f}" r="11" fill="rgb({ACC})" filter="url(#cd)"/>
        <circle cx="{ex:.0f}" cy="{ey:.0f}" r="5" fill="#8a4c2c"/>
        <text x="{ex:.0f}" y="{ey-22:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#17150F">30K</text>
        <text x="{ex:.0f}" y="{ey-2:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#96562d">Day 25</text>
      </svg>
      {cap("same expertise, same niche. one trade idea per post, not a technical essay.","#8a745a")}</div>'''

# 8. REFRAME - iso stack: the 1,400-word teardown gets skipped, the one plain line gets read
def reframe():
    layers=[("1,400-word teardown","skipped at scroll speed",0,True,560),
            ("300-word explainer","half-read",1,False,470),
            ("one plain line","read in full",2,False,384)]
    cards=""
    for nm,sub,i,bad,w in layers:
        y=(2-i)*128; lit=(i==2)
        bg=("linear-gradient(160deg,#e6b48f,rgb("+ACC+") 55%,#9a5a35)" if lit
            else ("linear-gradient(160deg,#332f2a,#211e1a)"))
        bd="rgba(255,255,255,.28)" if lit else "rgba(255,255,255,.09)"
        tc="#2a160c" if lit else ("#7a746a" if bad else "#cfc9bd")
        strike=("text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)" if bad else "")
        subc="#5a2c18" if lit else "#8f8f85"
        badge=(f'<div style="flex-shrink:0;background:#1a0f0a;color:rgb({ACC});font-family:\'DM Mono\';font-size:12px;'
               f'letter-spacing:.1em;padding:6px 12px;border-radius:999px">READ</div>' if lit else '')
        cards+=(f'<div style="position:absolute;left:{(560-w)//2}px;top:{y}px;width:{w}px;background:{bg};'
          f'border:1.5px solid {bd};border-radius:18px;padding:20px 24px;'
          f'box-shadow:0 30px 44px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,{".3" if lit else ".08"});'
          f'display:flex;align-items:center;gap:16px">'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:22px;color:{tc};{strike}">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:{subc};margin-top:2px">{sub}</div></div>{badge}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Boring is not low value","LEGIBLE > CLEVER")}
      <div style="perspective:1900px;height:452px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:420px;position:relative">{cards}</div>
      </div>
      {cap("the smartest content looks the simplest. legible at scroll speed wins.")}</div>'''

PANELS={"window":window(),"proof":proof(),"rules":rules(),"ego":ego(),
        "fourtest":fourtest(),"skill":skill(),"client":client(),"reframe":reframe()}

if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/boring"; os.makedirs(outd,exist_ok=True)
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
