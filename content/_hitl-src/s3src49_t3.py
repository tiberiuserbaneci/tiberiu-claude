#!/usr/bin/env python3
# TIER 3 - IT CLONED MY VOICE, built to the WIRE-ITS-EYES bar: 8 UNIQUE hand-built coded scenes,
# each a clean rounded card (title + one-line caption), NO generic stat-chip strips. NARROW angle:
# the voice-CLONING mechanic - how it samples your real posts, matches cadence, enforces your banned
# words, and the before/after of generic-vs-you. Warm palette only; muted red = the bad/generic state.
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

def _wave(x0,x1,y,amp,n,col,w,seed=0):
    pts=[]
    for i in range(n+1):
        t=i/n; x=x0+(x1-x0)*t
        yy=y+amp*math.sin(t*6.283*2.3+seed)*(0.5+0.5*math.sin(t*6.283*0.7+seed*1.7))
        pts.append(f"{x:.0f} {yy:.0f}")
    return f'<polyline points="{",".join(pts)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'

# 1. FLATTEN - three distinct living voice-waveforms on the left collapse into one dead flat line
#    (muted red) on the right: the generic AI voice everyone shares. Distinct scene = waveform collapse.
def flatten():
    voices=[("your posts",150,"rgb("+ACC+")",0.0),("your emails",235,"rgba(212,162,127,.7)",1.3),("your notes",320,"rgba(212,162,127,.45)",2.6)]
    live=""
    for nm,y,col,sd in voices:
        live+=_wave(60,360,y,44,60,col,3.4,sd)
        live+=f'<text x="60" y="{y-58:.0f}" font-family="DM Mono" font-size="12" fill="#8f8f85">{nm}</text>'
    funnel=('<path d="M366 150 C470 150,470 235,540 235" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
            '<path d="M366 235 H540" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
            '<path d="M366 320 C470 320,470 235,540 235" fill="none" stroke="rgba(212,162,127,.28)" stroke-width="2"/>')
    dead=('<line x1="560" y1="235" x2="800" y2="235" stroke="rgb(200,70,35)" stroke-width="4" stroke-dasharray="1 10" stroke-linecap="round"/>'
          '<text x="680" y="210" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb(200,70,35)">GENERIC AI</text>'
          '<text x="680" y="270" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#8f8f85">one flat voice</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every draft sounds the same","THE PROBLEM")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        {live}{funnel}{dead}
      </svg>
      {cap("left to itself, ai polishes you into a stranger - the same voice as everyone else's.")}</div>'''

# 2. INGEST - isometric stack of your real post cards being sampled into a voice profile.
def ingest():
    rows=[("\"I killed nine tools last month.\"","247 likes · your post","98"),
          ("\"The one I kept had no chat box.\"","from your feed","96"),
          ("\"Short lines. No hedging. Done.\"","your comment reply","94")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*140
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:600px;background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:20px 24px;box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:20px">'
          f'<div style="flex:1;text-align:left"><div style="font-family:\'DM Sans\';font-weight:800;font-size:22px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#a8a296;margin-top:3px">{b}</div></div>'
          f'<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 16px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:22px;color:#1a0f0a;line-height:1">{c}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">SAMPLED</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:38px 44px 40px">
      {htitle("It read 200 of your posts","THE SAMPLE")}
      <div style="perspective:2000px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:600px;height:440px;position:relative">{cards}</div></div>
      {cap("your real feed, not a training set - your words become the reference draft.")}</div>'''

# 3. CADENCE - sentence-length rhythm fingerprint: YOU (varied warm bars) vs GENERIC (flat uniform).
def cadence():
    you=[2,3,2,5,2,8,2,3,6,2,4,9,2,3]
    gen=[5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    def bars(vals,col,y0,lit):
        s=""; bw=44; gap=10; x=0
        for v in vals:
            h=v*22
            fill=col if lit else "rgba(154,154,146,.32)"
            s+=f'<rect x="{x}" y="{y0-h}" width="{bw}" height="{h}" rx="7" fill="{fill}"/>'
            x+=bw+gap
        return s
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It matches your cadence","THE RHYTHM")}
      <svg width="780" height="440" viewBox="0 0 780 440" style="display:block;margin:0 auto">
        <text x="0" y="30" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">YOU</text>
        {bars(you,"rgb("+ACC+")",232,True)}
        <text x="0" y="272" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#8f8f85">GENERIC</text>
        {bars(gen,"",416,False)}
        <line x1="0" y1="240" x2="780" y2="240" stroke="rgba(255,255,255,.08)"/>
      </svg>
      {cap("short. short. then one long line that lands. your pattern, kept - not the model's flat hum.")}</div>'''

# 4. BANNED - the blocklist ledger: words you never say, each struck through with a blocked LED.
def banned():
    words=["delve","leverage","synergy","robust","tapestry","seamless","boasts","in today's world","game-changer","unlock"]
    chips=""
    for w in words:
        chips+=(f'<div style="display:flex;align-items:center;gap:14px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(200,70,35,.28);border-radius:14px;padding:12px 18px;box-shadow:0 12px 22px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.06)">'
          f'<span style="flex-shrink:0;width:9px;height:9px;border-radius:50%;background:rgb(200,70,35);box-shadow:0 0 10px rgba(200,70,35,.8)"></span>'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:600;font-size:19px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.8)">{w}</span>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:rgb(200,70,35)">BLOCKED</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("The words you never say","BANNED · 0 SLIP")}
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px 22px">{chips}</div>
      {cap("every draft scanned against your blocklist - killed before it ever reaches you.")}</div>'''

# 5. DNA (IVORY) - double-helix of your style markers: two strands, labelled rungs = the voice profile.
def dna():
    W,H=640,470; cx=W/2
    strandA=""; strandB=""; rungs=""; nodes=""
    labels=["cadence","lexicon","taboo words","punctuation","sentence len","openers","emphasis"]
    n=len(labels)
    for i in range(n):
        t=i/(n-1); y=40+t*(H-80)
        ax=cx+150*math.sin(t*6.283*1.15)
        bx=cx-150*math.sin(t*6.283*1.15)
        rungs+=f'<line x1="{ax:.0f}" y1="{y:.0f}" x2="{bx:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.35)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{ax:.0f}" cy="{y:.0f}" r="12" fill="#96562d"/>'
                f'<circle cx="{bx:.0f}" cy="{y:.0f}" r="9" fill="#c98a5a"/>')
        side = ax if ax>bx else bx
        rungs+=f'<text x="{max(ax,bx)+22:.0f}" y="{y+5:.0f}" font-family="DM Mono" font-size="15" fill="#5a4634">{labels[i]}</text>'
    # smooth strand paths
    ptsA=[]; ptsB=[]
    for k in range(81):
        t=k/80; y=40+t*(H-80)
        ptsA.append(f"{cx+150*math.sin(t*6.283*1.15):.0f} {y:.0f}")
        ptsB.append(f"{cx-150*math.sin(t*6.283*1.15):.0f} {y:.0f}")
    strandA=f'<polyline points="{",".join(ptsA)}" fill="none" stroke="#96562d" stroke-width="5" stroke-linecap="round"/>'
    strandB=f'<polyline points="{",".join(ptsB)}" fill="none" stroke="#c98a5a" stroke-width="5" stroke-linecap="round"/>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;align-items:center;gap:20px">
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="flex-shrink:0">
        {rungs}{strandA}{strandB}{nodes}
      </svg>
      <div style="flex:1">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
          <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Your voice has a fingerprint</span></div>
        <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d;margin-bottom:16px">VOICE DNA</div>
        <div style="font-family:'DM Sans';font-size:20px;color:#3a2f22;line-height:1.5">Seven markers, extracted and locked: cadence, lexicon, the words you refuse, even how you open a line. One profile that is only yours.</div>
        {cap("cadence, taboo words, punctuation, openers - a style signature the model cannot fake.","#8a745a")}</div></div>'''

# 6. COMPARE (IVORY) - before/after: generic press-release sample vs your voice, same brief.
def compare():
    def panel(tag,tagcol,body,bodycol,bd,bg):
        return (f'<div style="flex:1;background:{bg};border:1.5px solid {bd};border-radius:18px;padding:22px 24px">'
          f'<div style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagcol};margin-bottom:14px">{tag}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:20px;color:{bodycol};line-height:1.5">{body}</div></div>')
    gen=panel("GENERIC","#a06a4a","We are thrilled to announce a robust, game-changing solution that seamlessly unlocks synergy for your business.","#7a6a58","rgba(150,90,45,.22)","rgba(120,95,60,.06)")
    you=panel("YOU","#96562d","I killed nine tools last month. The one I kept had no chat box. Here is why that mattered.","#2a2016","#96562d","rgba(255,255,255,.6)")
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Same brief, two writers</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">BEFORE / AFTER</span></div>
      <div style="display:flex;align-items:stretch;gap:20px">{gen}
        <div style="display:flex;align-items:center;font-family:'DM Mono';font-size:15px;color:#96562d;font-weight:500">vs</div>
        {you}</div>
      {cap("one reads like a press release. one reads like you. the brief was identical.","#8a745a")}</div>'''

# 7. GAUGE - style-match ring (per draft), enforcement stack: no draft ships below bar.
def gauge():
    pct=96; r=78; circ=2*math.pi*r; dash=circ*pct/100
    drafts=[("draft 1","94%",False),("draft 2","91% rewritten",False),("final","99%",True)]
    stack=""
    for nm,val,ok in drafts:
        col=f"rgb({ACC})" if ok else "#8f8f85"
        icon=(f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>' if ok
              else '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#8f8f85" stroke-width="2.6"><path d="M4 12h16" stroke-dasharray="2 4"/></svg>')
        stack+=(f'<div style="display:flex;align-items:center;gap:14px;background:{"linear-gradient(160deg,#403a33,#241f1a)" if ok else "#221f1b"};border:1px solid {f"rgba(212,162,127,.4)" if ok else "rgba(255,255,255,.08)"};border-radius:14px;padding:14px 18px;margin-bottom:12px">'
          f'{icon}<span style="flex:1;font-family:\'DM Mono\';font-size:16px;color:#c9c3b8">{nm}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:18px;color:{col}">{val}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;position:relative;width:200px;height:200px">
        <svg width="200" height="200" viewBox="0 0 200 200">
          <circle cx="100" cy="100" r="{r}" fill="none" stroke="rgba(212,162,127,.15)" stroke-width="16"/>
          <circle cx="100" cy="100" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 100 100)" filter="url(#gl)"/>
          <defs><filter id="gl" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter></defs></svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:48px;color:#FAFAF7">{pct}%</span>
          <span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">voice match</span></div></div>
      <div style="flex:1">
        {htitle("Every draft, scored","ENFORCED")}
        {stack}
        {cap("off-voice sentences rewritten until the match clears - nothing ships below your bar.")}</div></div>'''

# 8. SIGNATURE - closing: your voice becomes a signature stamped on every draft the body produces.
def signature():
    sig=('<path d="M60 250 C110 120,150 120,160 210 C168 280,120 300,120 220 C120 150,190 150,220 210 '
         'C245 260,300 260,300 200 C300 150,250 150,250 210 C250 280,330 285,380 210 '
         'C420 150,470 160,470 230 C470 275,520 275,560 210" fill="none" stroke="rgb('+ACC+')" '
         'stroke-width="6" stroke-linecap="round" stroke-linejoin="round" filter="url(#sg)"/>')
    drafts=""
    for i,lbl in enumerate(["post","email","landing page"]):
        x=90+i*230
        drafts+=(f'<g transform="translate({x},330)"><rect x="0" y="0" width="180" height="96" rx="14" fill="linear-gradient(160deg,#332f2a,#211e1a)" stroke="rgba(255,255,255,.10)"/>'
          f'<rect x="0" y="0" width="180" height="96" rx="14" fill="#2a2723" stroke="rgba(255,255,255,.10)"/>'
          f'<line x1="18" y1="30" x2="130" y2="30" stroke="rgba(250,250,247,.2)" stroke-width="3"/>'
          f'<line x1="18" y1="48" x2="150" y2="48" stroke="rgba(250,250,247,.12)" stroke-width="3"/>'
          f'<text x="18" y="80" font-family="DM Mono" font-size="13" fill="rgb({ACC})">signed &#10003; {lbl}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It signs in your hand","YOURS, MULTIPLIED")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <defs><filter id="sg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        <line x1="60" y1="290" x2="620" y2="290" stroke="rgba(255,255,255,.12)" stroke-width="2"/>
        <text x="60" y="285" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#8f8f85">YOUR HAND</text>
        {sig}{drafts}
      </svg>
      {cap("one profile, every post, email and page - all unmistakably you, at any volume.")}</div>'''

PANELS={"flatten":flatten(),"ingest":ingest(),"cadence":cadence(),"banned":banned(),
        "dna":dna(),"compare":compare(),"gauge":gauge(),"signature":signature()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src49"; os.makedirs(outd,exist_ok=True)
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
