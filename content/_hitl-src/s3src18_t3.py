#!/usr/bin/env python3
# TIER 3 - KEYWORD TO RANK (SEO publishing pipeline, PULSE). Rebuilt to the WIRE-ITS-EYES bar:
# each panel a UNIQUE hand-built coded scene filling a clean rounded card, title + one caption,
# NO generic stat-chip strips. 8 distinct scene TYPES: calendar heatmap, horizontal bar chart,
# document wireframe, manuscript page, topic-cluster graph, browser SERP, rank line chart, flywheel.
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

# 1. CADENCE - IVORY calendar heatmap: every working day publishes an article
def cadence():
    days=["M","T","W","T","F","S","S"]
    hdr="".join(f'<div style="font-family:DM Mono;font-size:14px;color:#a08a68;text-align:center;padding-bottom:8px">{d}</div>' for d in days)
    cells=""
    for wk in range(5):
        for wd in range(7):
            n=wk*7+wd+1; weekend=wd>=5
            if n>31:
                cells+='<div style="height:84px;border-radius:14px;background:rgba(150,120,80,.05)"></div>'; continue
            if weekend:
                cells+=(f'<div style="height:84px;border-radius:14px;background:rgba(150,120,80,.10);border:1px solid rgba(150,120,80,.14);'
                  f'display:flex;align-items:flex-start;justify-content:flex-end;padding:8px"><span style="font-family:DM Mono;font-size:12px;color:#b7a488">{n}</span></div>')
            else:
                cells+=(f'<div style="height:84px;border-radius:14px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 60%,#c98a5e);'
                  f'box-shadow:0 10px 20px rgba(150,100,60,.25),inset 0 2px 2px rgba(255,255,255,.5);position:relative;padding:9px;overflow:hidden">'
                  f'<span style="font-family:DM Mono;font-size:12px;color:#5a3418;position:absolute;top:8px;right:9px">{n}</span>'
                  f'<svg width="24" height="28" viewBox="0 0 24 28" style="position:absolute;left:12px;bottom:9px">'
                  f'<rect x="1" y="1" width="19" height="25" rx="3" fill="#fbf4ea" stroke="#5a3418" stroke-width="1.4"/>'
                  f'<line x1="5" y1="8" x2="16" y2="8" stroke="#a06a3e" stroke-width="1.6"/>'
                  f'<line x1="5" y1="13" x2="16" y2="13" stroke="#c98a5e" stroke-width="1.6"/>'
                  f'<line x1="5" y1="18" x2="12" y2="18" stroke="#c98a5e" stroke-width="1.6"/></svg></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 40px 34px">
      {htitle("From one a month to daily","PUBLISH CADENCE",ink="#2a2016")}
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">
        <span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#4a3f30">May 2026</span>
        <span style="font-family:DM Mono;font-size:14px;color:#96562d;background:rgba(150,90,45,.10);border:1px solid rgba(150,90,45,.2);border-radius:999px;padding:6px 14px">22 articles published</span></div>
      <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:8px">{hdr}{cells}</div>
      {cap("a fresh article every working day, indexed the same night.","#8a745a")}</div>'''

# 2. KEYWORDS - horizontal bar chart of ranked keyword opportunities (volume bar + difficulty)
def keywords():
    rows=[("cold email templates",12000,28),
          ("best crm for small teams",8100,34),
          ("ai sales agent",5400,41),
          ("lead scoring software",3600,22),
          ("outbound automation tools",2900,19),
          ("sales workflow software",1800,15)]
    mx=12000; bars=""
    for kw,vol,kd in rows:
        w=110+(vol/mx)*590
        kdcol="rgb("+ACC+")" if kd<=25 else "#c99a6e"
        bars+=(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:13px">'
          f'<div style="flex-shrink:0;width:300px;text-align:right;font-family:DM Sans;font-weight:600;font-size:18px;color:#e2dccf">{kw}</div>'
          f'<div style="flex:1;position:relative;height:38px">'
          f'<div style="position:absolute;left:0;top:0;height:38px;width:{w:.0f}px;border-radius:9px;background:linear-gradient(90deg,#8a4c2c,rgb({ACC}));'
          f'box-shadow:0 6px 14px rgba(212,162,127,.25);display:flex;align-items:center;justify-content:flex-end;padding-right:12px">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:16px;color:#1a0f0a">{vol:,}</span></div></div>'
          f'<div style="flex-shrink:0;width:72px;text-align:center;font-family:DM Mono;font-size:14px;color:{kdcol};'
          f'border:1px solid rgba(255,255,255,.12);border-radius:8px;padding:6px 0">KD {kd}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("It mines what buyers search","KEYWORD MAP")}
      <div style="display:flex;align-items:center;gap:16px;margin-bottom:12px;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#8f8f85">
        <span style="width:300px;text-align:right">KEYWORD</span><span style="flex:1">MONTHLY SEARCHES</span><span style="width:72px;text-align:center">DIFF</span></div>
      {bars}
      {cap("ranked by volume and how hard each one is to win, not guesswork.")}</div>'''

# 3. BRIEF - document wireframe skeleton + SEO checklist column
def brief():
    heads=[("H2","The problem, in one line",[42,60]),
           ("H2","How it actually works",[70,48,55]),
           ("H2","Proof and the numbers",[52,64]),
           ("FAQ","People also ask",[38,44,40])]
    skel=""
    for tag,label,lines in heads:
        subs="".join(f'<div style="height:9px;border-radius:5px;background:rgba(250,250,247,.10);width:{ln}%;margin-bottom:8px"></div>' for ln in lines)
        skel+=(f'<div style="margin-bottom:16px"><div style="display:flex;align-items:center;gap:10px;margin-bottom:9px">'
          f'<span style="font-family:DM Mono;font-size:11px;color:#1a0f0a;background:rgb({ACC});border-radius:5px;padding:2px 7px">{tag}</span>'
          f'<div style="height:13px;border-radius:6px;background:rgba(250,250,247,.30);width:230px"></div></div>{subs}</div>')
    checks=["Title tag under 60 chars","Meta description written","1 primary + 4 secondary terms","3 internal links placed","FAQ schema added","Alt text on every image"]
    chk="".join(f'<div style="display:flex;align-items:center;gap:11px;margin-bottom:13px">'
      f'<svg width="20" height="20" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.16)"/>'
      f'<path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      f'<span style="font-family:DM Sans;font-size:16px;color:#d9d5cc">{c}</span></div>' for c in checks)
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("Every brief built to rank","ARTICLE OUTLINE")}
      <div style="display:flex;gap:28px">
        <div style="flex:1;background:rgba(250,250,247,.03);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:24px 24px 8px">
          <div style="height:20px;border-radius:7px;background:rgb({ACC});width:72%;margin-bottom:8px"></div>
          <div style="font-family:DM Mono;font-size:12px;color:#8f8f85;margin-bottom:20px">H1 &middot; target keyword</div>
          {skel}
        </div>
        <div style="flex-shrink:0;width:322px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.09);border-radius:18px;padding:22px 24px">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:18px">SEO CHECKLIST</div>
          {chk}
        </div>
      </div>
      {cap("title tag, meta, headings and links, set before a word is written.")}</div>'''

# 4. DRAFT - IVORY manuscript page mockup with brand-voice phrases highlighted + meta rail
def draft():
    metas=[("VOICE MATCH","98%"),("READABILITY","grade 7"),("BANNED WORDS","0"),("READ TIME","4 min")]
    rail="".join(f'<div style="background:rgba(255,255,255,.6);border:1px solid rgba(150,120,80,.2);border-radius:14px;padding:14px 16px">'
      f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#96562d;margin-bottom:4px">{t}</div>'
      f'<div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">{v}</div></div>' for t,v in metas)
    hi='background:rgba(212,162,127,.35);border-bottom:2px solid #96562d;padding:1px 3px'
    return f'''<div style="width:900px;{CARDIV};padding:36px 40px 34px">
      {htitle("Drafted in your voice","ON-BRAND DRAFT",ink="#2a2016")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1;background:#fffdf8;border:1px solid rgba(120,95,60,.18);border-radius:18px;padding:28px 30px;box-shadow:0 20px 40px rgba(120,95,60,.14),inset 0 2px 3px rgba(255,255,255,.9)">
          <div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#2a2016;line-height:1.2;margin-bottom:16px">Why small teams outgrow their first CRM</div>
          <p style="font-family:DM Sans;font-size:18px;color:#4a3f30;line-height:1.55;margin:0 0 14px">Most founders pick a CRM on day one and <span style="{hi}">outgrow it by month six.</span> The tool did not fail. The workflow did.</p>
          <p style="font-family:DM Sans;font-size:18px;color:#4a3f30;line-height:1.55;margin:0">You do not need more fields. You need <span style="{hi}">fewer steps between a reply and a booked deal.</span></p>
        </div>
        <div style="flex-shrink:0;width:212px;display:flex;flex-direction:column;gap:13px">{rail}</div>
      </div>
      {cap("sampled from your real pages, banned words enforced on every draft.","#8a745a")}</div>'''

# 5. LINKS - topic-cluster graph: one pillar hub + satellite article chips, bezier internal links
def links():
    cx,cy,R=410,232,196
    arts=[("First CRM guide",-90),("Lead scoring 101",-39),("Cold email tips",12),
          ("Pipeline stages",63),("Sales workflow",114),("Onboarding SOP",165),("Churn signals",216)]
    edges="";chips=""
    for nm,a in arts:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        mx=(cx+x)/2
        edges+=f'<path d="M{cx} {cy} C{mx:.0f} {cy},{mx:.0f} {y:.0f},{x:.0f} {y:.0f}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2"/>'
        chips+=(f'<rect x="{x-78:.0f}" y="{y-21:.0f}" width="156" height="42" rx="12" fill="#2a2724" stroke="rgba(255,255,255,.11)"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#d3cdc1">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("It weaves the internal web","TOPIC CLUSTER")}
      <svg width="820" height="472" viewBox="0 0 820 472" style="display:block;margin:0 auto">
        <defs><radialGradient id="pil" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="pg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{chips}
        <g filter="url(#pg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#pil)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#1a0f0a">PILLAR</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">7 links in</text>
      </svg>
      {cap("each post links into a cluster, so authority compounds across the site.")}</div>'''

# 6. SERP - browser search-results mockup, your result ranked #1 above two dim competitors
def serp():
    comps=[("competitor.io &rsaquo; blog","How to pick a CRM in 2026","A generic listicle of ten tools with no point of view."),
           ("othersite.com &rsaquo; guides","CRM buying guide 2026","Another roundup that never mentions small teams.")]
    dim=""
    for url,title,snip in comps:
        dim+=(f'<div style="padding:16px 20px;border-top:1px solid rgba(255,255,255,.06);opacity:.55">'
          f'<div style="font-family:DM Mono;font-size:13px;color:#8f8f85">{url}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#b8b2a6;margin:3px 0 2px">{title}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#7d786e">{snip}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("Indexed by night, climbing by week","SERP")}
      <div style="background:#161513;border:1px solid rgba(255,255,255,.09);border-radius:18px;overflow:hidden;box-shadow:0 26px 50px rgba(0,0,0,.5)">
        <div style="display:flex;align-items:center;gap:10px;padding:14px 18px;background:linear-gradient(180deg,#26231f,#1b1916);border-bottom:1px solid rgba(255,255,255,.07)">
          <span style="width:12px;height:12px;border-radius:50%;background:#3a3630"></span><span style="width:12px;height:12px;border-radius:50%;background:#3a3630"></span><span style="width:12px;height:12px;border-radius:50%;background:#3a3630"></span>
          <div style="flex:1;margin-left:8px;background:#100f0d;border:1px solid rgba(255,255,255,.08);border-radius:9px;padding:8px 14px;font-family:DM Mono;font-size:14px;color:#a8a296">search &rsaquo; best crm for small teams</div></div>
        <div style="padding:18px 20px;background:linear-gradient(160deg,rgba(212,162,127,.14),rgba(212,162,127,.04));border-left:4px solid rgb({ACC})">
          <div style="display:flex;align-items:center;justify-content:space-between">
            <div style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">yoursite.com &rsaquo; blog</div>
            <div style="font-family:DM Sans;font-weight:900;font-size:14px;color:#1a0f0a;background:rgb({ACC});border-radius:999px;padding:4px 12px">RANK #1</div></div>
          <div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7;margin:5px 0 3px">Why small teams outgrow their first CRM</div>
          <div style="font-family:DM Sans;font-size:16px;color:#c9c3b8">The tool did not fail, the workflow did. Fewer steps between a reply and a booked deal.</div></div>
        {dim}
      </div>
      {cap("submitted to search the same day, then tracked as it moves up.")}</div>'''

# 7. RANK - line/area chart: keyword position climbing 47 to 3 across ten weeks (y inverted)
def rank():
    pos=[47,44,38,31,25,19,14,10,6,4,3]
    n=len(pos); padL,padT,padR,padB=64,26,20,44
    W,H=740,360; plotW=W-padL-padR; plotH=H-padT-padB
    def X(i): return padL+i/(n-1)*plotW
    def Y(p): return padT+(p-1)/49*plotH
    pts=[(X(i),Y(p)) for i,p in enumerate(pos)]
    line=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    area=f"{padL},{padT+plotH} "+line+f" {padL+plotW},{padT+plotH}"
    grid=""
    for gp,lab in [(1,"#1"),(10,"10"),(25,"25"),(50,"50")]:
        gy=Y(gp)
        grid+=(f'<line x1="{padL}" y1="{gy:.0f}" x2="{padL+plotW}" y2="{gy:.0f}" stroke="rgba(255,255,255,.07)"/>'
          f'<text x="{padL-12}" y="{gy+4:.0f}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#8f8f85">{lab}</text>')
    dots="".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="rgb({ACC})"/>' for x,y in pts)
    x0,y0=pts[0]; x1,y1=pts[-1]
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("Position 47 to 3 in ten weeks","RANK TRACK")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="af" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.42)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
        <filter id="lg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        {grid}
        <polygon points="{area}" fill="url(#af)"/>
        <polyline points="{line}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" filter="url(#lg)"/>
        {dots}
        <text x="{x0+8:.0f}" y="{y0-10:.0f}" font-family="DM Sans" font-weight="800" font-size="17" fill="#c9c3b8">pos 47</text>
        <text x="{x1-6:.0f}" y="{y1-16:.0f}" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="22" fill="rgb({ACC})">pos 3</text>
        <text x="{padL}" y="{H-12}" font-family="DM Mono" font-size="12" fill="#8f8f85">week 1</text>
        <text x="{padL+plotW}" y="{H-12}" text-anchor="end" font-family="DM Mono" font-size="12" fill="#8f8f85">week 10</text>
      </svg>
      {cap("real tracking on every target term, so you see rank move, not vanity hits.")}</div>'''

# 8. LOOP - autopilot flywheel: research -> write -> publish -> learn around a PULSE hub
def loop():
    cx,cy,R=410,228,158
    stages=[("RESEARCH","keywords",-90),("WRITE","on-brand draft",0),("PUBLISH","same day",90),("LEARN","what ranked",180)]
    arcs="";nodes=""
    for i in range(4):
        a0=math.radians(-90+i*90+16); a1=math.radians(-90+(i+1)*90-16)
        x0=cx+R*math.cos(a0); y0=cy+R*math.sin(a0); x1=cx+R*math.cos(a1); y1=cy+R*math.sin(a1)
        arcs+=f'<path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="3"/>'
        ah=math.radians(-90+(i+1)*90-16); hx=cx+R*math.cos(ah); hy=cy+R*math.sin(ah); tang=ah+math.pi/2
        p1x=hx+11*math.cos(tang-2.5); p1y=hy+11*math.sin(tang-2.5); p2x=hx+11*math.cos(tang+2.5); p2y=hy+11*math.sin(tang+2.5)
        arcs+=f'<polygon points="{hx:.0f},{hy:.0f} {p1x:.0f},{p1y:.0f} {p2x:.0f},{p2y:.0f}" fill="rgb({ACC})"/>'
    for nm,sub,a in stages:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+17:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#9a9488">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:36px 40px 34px">
      {htitle("Set it once, it compounds","THE FLYWHEEL")}
      <svg width="820" height="464" viewBox="0 0 820 464" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {arcs}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-3}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">PULSE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">runs the loop</text>
        {nodes}
      </svg>
      {cap("research, write, publish, learn, while you run the company.")}</div>'''

PANELS={"cadence":cadence(),"keywords":keywords(),"brief":brief(),"draft":draft(),
        "links":links(),"serp":serp(),"rank":rank(),"loop":loop()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src18"; os.makedirs(outd,exist_ok=True)
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
