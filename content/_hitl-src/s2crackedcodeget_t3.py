#!/usr/bin/env python3
# TIER 3 - BE THE CITATION (get recommended by ChatGPT/Claude/Gemini/Google), rebuilt to the
# WIRE-ITS-EYES bar: each panel a UNIQUE hand-built coded scene filling a clean rounded card,
# title + one-line caption, NO generic stat-chip strips, NO cuts/walls. Ultron-forward.
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

# 1. ANSWER - AI-assistant answer mockup: a user query, an AI answer, ONE sourced citation card
#    (your company) lit as the recommendation. The chat scene, not a table.
def answer():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("They ask the AI now","THE ANSWER")}
      <div style="background:#151412;border:1px solid rgba(255,255,255,.07);border-radius:22px;padding:24px 26px 26px">
        <div style="display:flex;justify-content:flex-end;margin-bottom:18px">
          <div style="background:linear-gradient(160deg,#3a352f,#26221d);border:1px solid rgba(255,255,255,.10);border-radius:16px 16px 5px 16px;padding:13px 18px;max-width:520px;font-family:DM Sans;font-size:19px;color:#e7e1d5">best AI operator to grow a lean founder team?</div></div>
        <div style="display:flex;align-items:flex-start;gap:14px">
          <div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:radial-gradient(circle at 36% 30%,#f0c49e,rgb({ACC}) 55%,#7a4326);box-shadow:0 8px 18px rgba(212,162,127,.4)"></div>
          <div style="flex:1">
            <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45;margin-bottom:16px">For a lean founder team, the operator most teams point to is</div>
            <div style="background:linear-gradient(158deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:16px;padding:18px 20px;box-shadow:0 0 30px rgba(212,162,127,.28), inset 0 2px 2px rgba(255,255,255,.08);display:flex;align-items:center;gap:16px">
              <div style="flex-shrink:0;width:46px;height:46px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#eab98f,rgb({ACC}) 52%,#6f3f22)"></div>
              <div style="flex:1"><div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#FAFAF7">Ultron</div>
                <div style="font-family:DM Sans;font-size:15px;color:#b7b0a4">AI operator for founders &middot; 51ultron.com</div></div>
              <div style="flex-shrink:0;font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:999px;padding:6px 12px">CITED [1]</div></div>
            <div style="display:flex;gap:10px;margin-top:14px">
              {"".join(f'<span style="font-family:DM Mono;font-size:12px;color:#7d776c;border:1px solid rgba(255,255,255,.09);border-radius:8px;padding:6px 11px">{s}</span>' for s in ["techcrunch.com","g2.com","51ultron.com/docs"])}
            </div></div></div>
      </div>
      {cap("be the sourced answer the model hands 800M people, not the tenth blue link.")}</div>'''

# 2. CONSTELLATION - the models orbit YOUR node; every model edge points inward to one company
def constellation():
    cx,cy=456,240
    models=[("ChatGPT",120,150,"OpenAI"),("Claude",300,145,""),("Gemini",760,150,"Google"),
            ("Perplexity",150,380,""),("Copilot",760,380,""),("Google AI",456,60,"")]
    edges=""; nodes=""
    for nm,x,y,sub in models:
        edges+=f'<line x1="{x}" y1="{y}" x2="{cx}" y2="{cy}" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
        edges+=f'<circle cx="{(x+cx)/2:.0f}" cy="{(y+cy)/2:.0f}" r="3.5" fill="rgb({ACC})"/>'
    star=""
    for nm,x,y,sub in models:
        star+=(f'<circle cx="{x}" cy="{y}" r="34" fill="#221f1b" stroke="rgba(255,255,255,.13)" stroke-width="1.5"/>'
          f'<circle cx="{x}" cy="{y}" r="9" fill="rgba(212,162,127,.9)" filter="url(#bl)"/>'
          f'<text x="{x}" y="{y+58}" text-anchor="middle" font-family="DM Mono" font-size="13.5" fill="#d3cdc1">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Cited once, recommended everywhere","EVERY MODEL")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="you" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="yg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter>
        <filter id="bl" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {edges}{star}
        <g filter="url(#yg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#you)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#2a160c">YOU</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">the answer</text>
      </svg>
      {cap("every assistant pulls from the same sourced web - win the citation one time.")}</div>'''

# 3. RADAR - live radar of AI mentions across models, ranked, with a this-week lead readout
def radar():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("ChatGPT",300,150),("Gemini",120,96),("Claude",210,168),("Perplexity",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    rows=[("ChatGPT","8 answers","this week"),("Gemini","5 answers","this week"),("Claude","4 answers","this week")]
    board=""
    for a,b,c in rows:
        board+=(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.07)">'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#e7e1d5">{a}</span>'
          f'<span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">{b}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It hears your name","MENTION RADAR")}
        <div style="background:#211d19;border:1px solid rgba(212,162,127,.28);border-radius:16px;padding:8px 20px 6px">{board}
          <div style="display:flex;justify-content:space-between;align-items:baseline;padding-top:12px">
            <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:rgb({ACC})">17 answers</span>
            <span style="font-family:DM Mono;font-size:13px;color:#8f8f85">0 last month</span></div></div>
        {cap("every model, every mention, watched overnight - you see who already cites you.")}
      </div></div>'''

# 4. GRAPH - CORTEX knowledge graph: one YOU entity wired to the facts a model needs to quote
def graph():
    cx,cy=470,240
    facts=[("Category","AI operator",90,90),("Proof","3 case studies",90,240),
           ("Reviews","4.8 on G2",90,390),("Docs","51ultron.com/docs",760,120),
           ("ICP","2-50 founders",760,260),("Pricing","cents per run",760,400)]
    edges=""; nodes=""
    for lab,val,x,y in facts:
        mx=(x+cx)/2
        edges+=f'<path d="M{x} {y} C{mx:.0f} {y},{mx:.0f} {cy},{cx} {cy}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        anchor="start" if x<cx else "end"; tx=x+46 if x<cx else x-46
        nodes+=(f'<circle cx="{x}" cy="{y}" r="12" fill="#221f1b" stroke="rgb({ACC})" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="4.5" fill="rgb({ACC})"/>'
          f'<text x="{tx}" y="{y-4}" text-anchor="{anchor}" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb({ACC})">{lab.upper()}</text>'
          f'<text x="{tx}" y="{y+17}" text-anchor="{anchor}" font-family="DM Sans" font-weight="700" font-size="16" fill="#e2dccf">{val}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Why the model picks you","CORTEX MAP")}
      <svg width="820" height="480" viewBox="0 0 820 480" style="display:block;margin:0 auto">
        <defs><radialGradient id="ent" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="eg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#eg)"><circle cx="{cx}" cy="{cy}" r="60" fill="url(#ent)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ENTITY</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one you</text>
      </svg>
      {cap("category, proof, reviews and docs wired into one entity the models can quote.")}</div>'''

# 5. STACK - IVORY isometric stack of published, SOURCED content cards (built to be lifted)
def stack():
    rows=[("The AI operator math for founders","techcrunch.com","cited"),
          ("Why cold outbound decays in 10 days","51ultron.com/docs","cited"),
          ("Cents-per-run vs agency retainers","g2.com","cited")]
    cards=""
    for i,(title,src,badge) in enumerate(rows):
        y=i*138
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;background:linear-gradient(160deg,#ffffff,#f2ebdd);border:1px solid rgba(120,95,60,.18);border-radius:18px;padding:20px 24px;box-shadow:0 30px 46px rgba(120,95,60,.24), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:20px">'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:21px;color:#2a2016;line-height:1.2">{title}</div>'
          f'<div style="display:flex;align-items:center;gap:8px;margin-top:8px"><span style="font-family:DM Mono;font-size:13px;color:#96562d">{src}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;color:#a08a68">&middot; sourced &middot; dated</span></div></div>'
          f'<div style="flex-shrink:0;display:flex;align-items:center;gap:7px;background:#96562d;padding:8px 14px;border-radius:999px">'
          f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:#fff">{badge}</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 44px 40px">
      {htitle("Built to be quoted","PULSE",ink="#2a2016")}
      <div style="perspective:2000px;height:520px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:600px;height:430px;position:relative">{cards}</div></div>
      {cap("every claim carries a real source and date, written to be lifted into an answer.","#8a745a")}</div>'''

# 6. GAUGE - IVORY ring gauge: your share of the AI answer, invisible -> cited, cents pricing
def gauge():
    pct=41; r=88; circ=2*math.pi*r; dash=circ*pct/100
    bars=[("Jan","4%"),("Mar","16%"),("May","28%"),("Now","41%")]
    bh=""
    for lab,v in bars:
        h=int(float(v.strip('%'))*2.2)
        bh+=(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;justify-content:flex-end">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:16px;color:#2a2016">{v}</span>'
          f'<div style="width:34px;height:{h}px;border-radius:9px 9px 3px 3px;background:linear-gradient(180deg,#c9905f,#96562d)"></div>'
          f'<span style="font-family:DM Mono;font-size:12px;color:#a08a68">{lab}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 36px;display:flex;align-items:center;gap:38px">
      <div style="flex-shrink:0;position:relative;width:230px;height:230px">
        <svg width="230" height="230" viewBox="0 0 230 230">
          <circle cx="115" cy="115" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="20"/>
          <circle cx="115" cy="115" r="{r}" fill="none" stroke="#96562d" stroke-width="20" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 115 115)"/></svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:56px;color:#2a2016">{pct}%</span>
          <span style="font-family:DM Mono;font-size:12px;color:#96562d">share of answer</span></div></div>
      <div style="flex:1">
        {htitle("From invisible to the answer","VISIBILITY",ink="#2a2016")}
        <div style="display:flex;align-items:flex-end;gap:26px;height:150px;margin:4px 0 6px">{bh}</div>
        {cap("share of the AI answer, tracked and grown - cents per brief, not agency retainers.","#8a745a")}
      </div></div>'''

# 7. FIELD - dot field of AI answers; the lit dots are the answers that cite you (AMPLIFY reach)
def field():
    cols,rowsn=44,22
    lit={53,118,209,266,331,402,477,540,611,684,715,760,803,846,889,930,55,120,210}
    dots=""; cell=15; gap=4
    for i in range(cols*rowsn):
        rr,cc=divmod(i,cols); x=cc*(cell+gap); y=rr*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:36px 40px 36px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:DM Sans;font-weight:900;font-size:50px;color:#FAFAF7">1,000</span>
        <span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#c9a583;margin-left:10px">AI answers sampled</span></div>
        <div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">AMPLIFY</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-top:16px">
        <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">240 cite you</span>
        <span style="font-family:DM Mono;font-size:14px;color:#8f8f85">ship the sourced version to every surface the models crawl</span></div></div>'''

# 8. HUB - radial hub-and-spokes: YOU at centre feed every surface, one HUMAN GATE lock on publish
def hub():
    cx,cy=232,236
    surf=[("ChatGPT",-90),("Gemini",-18),("Google",54),("Claude",126),("Perplexity",198)]
    spokes=""; nodes=""
    for i,(nm,a) in enumerate(surf):
        x=cx+138*math.cos(math.radians(a)); y=cy+138*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#221f1b" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="rgb({ACC})"/>'
          f'<text x="{x:.0f}" y="{y+50 if a>0 or a==-90 else y-42:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="470" height="480" viewBox="0 0 470 480">
        <defs><radialGradient id="core" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">MEMORY</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one core</text>
        <g transform="translate({cx-19},{cy+96})"><rect x="0" y="15" width="38" height="28" rx="6" fill="none" stroke="rgb({ACC})" stroke-width="3.4"/><path d="M7 15 V8 a12 12 0 0 1 24 0 v7" fill="none" stroke="rgb({ACC})" stroke-width="3.4"/></g>
        <text x="{cx}" y="{cy+170}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="rgb({ACC})">HUMAN GATE</text>
      </svg>
      <div style="flex:1">
        {htitle("Be the answer AI recommends","ONE OPERATOR")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">CORTEX researches, PULSE writes it sourced, AMPLIFY ships it to every model. One memory, every publish held at your gate.</div>
        {cap("one login - researched, written, published, gated. still your company.")}</div></div>'''

PANELS={"answer":answer(),"constellation":constellation(),"radar":radar(),"graph":graph(),
        "stack":stack(),"gauge":gauge(),"field":field(),"hub":hub()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2crackedcodeget"; os.makedirs(outd,exist_ok=True)
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
