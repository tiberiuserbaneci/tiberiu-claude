#!/usr/bin/env python3
# TIER 3 - ONE SKILL PER GAP, built to the WIRE-ITS-EYES bar: 8 unique hand-built coded scenes,
# each filling a clean rounded card, htitle + one-line cap, NO generic stat-chip strips.
# Source: IG carousel "I replaced my $270K creative team with 7 Claude skills" (s3src13).
# Angle diverged from the saturated content-factory bucket -> "one named skill per gap".
import importlib.util, os, math, random
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

# 1. GAPS - IVORY ledger book: the specialist salaries you paid, each struck out red, replaced by cents
def gaps():
    rows=[("Copywriter","$90K"),("Brand researcher","$70K"),("Editor","$55K"),
          ("Video editor","$40K"),("Producer / VA","$15K")]
    rh=""
    for i,(role,amt) in enumerate(rows):
        rh+=(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:15px 22px;'
             f'{"border-top:1px solid rgba(150,120,80,.18);" if i else ""}">'
             f'<span style="font-family:DM Sans;font-weight:700;font-size:20px;color:#5a4634;position:relative">'
             f'<span style="position:relative">{role}<span style="position:absolute;left:-4px;right:-4px;top:52%;height:2px;background:rgb({RED})"></span></span></span>'
             f'<span style="font-family:DM Mono;font-size:19px;color:#a06a4a;text-decoration:line-through;text-decoration-color:rgb({RED})">{amt}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The team was all gaps","REPLACED · $270K","#2a2016")}
      <div style="background:rgba(255,255,255,.55);border:1px solid rgba(150,120,80,.2);border-radius:20px;overflow:hidden">{rh}
        <div style="display:flex;align-items:center;justify-content:space-between;padding:20px 22px;background:linear-gradient(90deg,rgba(150,90,45,.1),rgba(150,90,45,.02));border-top:2px solid #96562d">
          <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016">7 named skills</span>
          <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#96562d">cents / brief</span></div></div>
      {cap("five hires, five gaps. one skill now covers each. pay per token.","#8a745a")}</div>'''

# 2. VOICE - Voice DNA: a coded waveform fingerprint + banned words struck, cadence markers kept
def voice():
    random.seed(13); bars=""
    n=44; bw=13
    for i in range(n):
        h=40+abs(math.sin(i*0.7))*120*random.uniform(.35,1); y=200-h/2
        op=.9 if 8<i<34 else .35
        bars+=f'<rect x="{40+i*bw}" y="{y:.0f}" width="7" height="{h:.0f}" rx="3.5" fill="rgb({ACC})" opacity="{op}"/>'
    banned=["actually","leverage","game-changer","synergy"]
    chips="".join(f'<div style="display:flex;align-items:center;gap:8px;padding:8px 14px;background:rgba(200,70,35,.09);border:1px solid rgba(200,70,35,.32);border-radius:999px">'
        f'<svg width="14" height="14" viewBox="0 0 24 24" stroke="rgb({RED})" stroke-width="3" fill="none"><path d="M6 6l12 12M18 6L6 18"/></svg>'
        f'<span style="font-family:DM Mono;font-size:14px;color:#c98a72;text-decoration:line-through">{w}</span></div>' for w in banned)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It writes in your voice","/voice-dna")}
      <svg width="820" height="230" viewBox="0 0 820 230" style="display:block">
        <line x1="30" y1="200" x2="790" y2="200" stroke="rgba(255,255,255,.08)"/>
        {bars}</svg>
      <div style="display:flex;gap:26px;margin-top:8px;align-items:center">
        <div style="flex-shrink:0;font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC});writing-mode:vertical-rl;transform:rotate(180deg)">NEVER SAYS</div>
        <div style="display:flex;flex-wrap:wrap;gap:12px;flex:1">{chips}</div>
        <div style="flex-shrink:0;text-align:right"><div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7;line-height:1">98%</div>
          <div style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">style match</div></div></div>
      {cap("your cadence and vocabulary, extracted. the words you never use, banned.")}</div>'''

# 3. RESEARCH - Deep Research: a bezier node/flow graph fanning a query into steps + sources
def research():
    qx,qy=90,220
    stages=[("query",qx,qy)]
    mids=[("market",300,110),("rivals",300,220),("reviews",300,330)]
    leaves=[(590,70),(590,140),(590,210),(590,280),(590,350),(590,110),(590,300)]
    edges=""
    for _,mx,my in mids:
        edges+=f'<path d="M{qx+34} {qy} C200 {qy},200 {my},{mx-32} {my}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="3"/>'
    lset=[(0,70),(0,170),(1,210),(1,280),(2,300),(2,140),(0,110)]
    for li,(idx,ly) in enumerate(lset):
        mx,my=300,mids[idx][2]
        edges+=f'<path d="M{mx+32} {my} C470 {my},470 {ly},558 {ly}" fill="none" stroke="rgba(212,162,127,.22)" stroke-width="2"/>'
    nodes=""
    for nm,mx,my in mids:
        nodes+=(f'<circle cx="{mx}" cy="{my}" r="30" fill="#241f1a" stroke="rgba(212,162,127,.5)" stroke-width="2"/>'
                f'<text x="{mx}" y="{my+5}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    for _,ly in lset:
        nodes+=f'<circle cx="590" cy="{ly}" r="8" fill="rgb({ACC})" filter="url(#rb)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Research that runs itself","/deep-research")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block">
        <defs><radialGradient id="rq" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rb" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.85"/></filter></defs>
        {edges}
        <circle cx="{qx}" cy="{qy}" r="40" fill="url(#rq)" filter="url(#rb)"/>
        <text x="{qx}" y="{qy+4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">ONE</text>
        <text x="{qx}" y="{qy+20}" text-anchor="middle" font-family="DM Mono" font-size="10" fill="#3a2010">brief</text>
        {nodes}
        <text x="690" y="215" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">31</text>
        <text x="690" y="238" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">sources cited</text></svg>
      {cap("one brief fans into a multi-step agent - market, rivals, reviews - while you step away.")}</div>'''

# 4. MEMORY - Supermemory: a concentric core with recall lifelines pulling stored facts back in
def memory():
    cx,cy=210,215
    facts=[("ICP",-90,168),("pricing",-26,168),("past drafts",38,168),("brand voice",102,168),("every reply",166,168)]
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.14)"/>' for r in (46,86,128))
    lines=""; chips=""
    for nm,a,d in facts:
        x=cx+d*math.cos(math.radians(a)); y=cy+d*math.sin(math.radians(a))
        lines+=f'<path d="M{cx} {cy} L{x:.0f} {y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
        lines+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="26" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="1.6"/>'
                f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="420" height="430" viewBox="0 0 420 430">
        <defs><radialGradient id="mc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {rings}{lines}
        <g filter="url(#mg)"><circle cx="{cx}" cy="{cy}" r="40" fill="url(#mc)"/></g>
        <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">CORE</text></svg>
      <div style="flex:1">
        {htitle("Claude that remembers you","/supermemory")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">A blank prompt forgets you every time. This core keeps your ICP, pricing, past drafts and brand voice, and pulls them into every new brief.</div>
        {cap("nothing starts from zero. every skill draws from one memory.")}</div></div>'''

# 5. AUDIO - ElevenLabs TTS: IVORY podcast player, a doc turned into narrated audio
def audio():
    random.seed(5); wf=""
    for i in range(60):
        h=8+abs(math.sin(i*0.5))*44*random.uniform(.4,1); y=64-h/2
        played=i<26
        wf+=f'<rect x="{i*11}" y="{y:.0f}" width="6" height="{h:.0f}" rx="3" fill="{"#96562d" if played else "rgba(150,90,45,.28)"}"/>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("Any doc becomes a voice","/tts","#2a2016")}
      <div style="display:flex;align-items:center;gap:22px;margin:6px 0 22px">
        <div style="flex-shrink:0;width:96px;height:120px;background:#fff;border:1px solid rgba(150,120,80,.28);border-radius:12px;box-shadow:0 12px 26px rgba(120,95,60,.2);padding:16px 12px">
          {"".join(f'<div style="height:5px;border-radius:3px;background:rgba(90,70,52,{o});margin-bottom:9px;width:{w}"></div>' for o,w in [(.5,"100%"),(.5,"88%"),(.35,"96%"),(.35,"72%"),(.35,"90%"),(.35,"60%")])}
        </div>
        <svg width="52" height="52" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M9 6l10 6-10 6z" fill="#96562d"/></svg>
        <div style="flex:1;background:rgba(255,255,255,.62);border:1px solid rgba(150,120,80,.24);border-radius:18px;padding:20px 22px;box-shadow:inset 0 2px 3px rgba(255,255,255,.8)">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px">
            <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">Your memo, narrated</span>
            <span style="font-family:DM Mono;font-size:13px;color:#96562d">04:12 / 09:38</span></div>
          <svg width="660" height="66" viewBox="0 0 660 66" style="display:block;max-width:100%">{wf}</svg></div></div>
      {cap("brief in, a narrated episode out. no mic, no booking, no editor.","#8a745a")}</div>'''

# 6. VIDEO - Remotion: a filmstrip of frames rendered from code, a render bar, no editor
def video():
    frames=""
    labs=["hook","stat","proof","list","cta"]
    for i,lb in enumerate(labs):
        x=20+i*158
        frames+=(f'<g><rect x="{x}" y="60" width="140" height="200" rx="14" fill="#211d19" stroke="rgba(212,162,127,.3)" stroke-width="1.6"/>'
                 f'<rect x="{x+16}" y="80" width="108" height="60" rx="8" fill="rgba(212,162,127,.16)"/>'
                 f'<rect x="{x+16}" y="152" width="90" height="9" rx="4" fill="rgba(255,255,255,.22)"/>'
                 f'<rect x="{x+16}" y="170" width="70" height="9" rx="4" fill="rgba(255,255,255,.14)"/>'
                 f'<text x="{x+70}" y="235" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">frame {i+1}</text>'
                 f'<text x="{x+70}" y="252" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">{lb}</text></g>')
        if i<4:
            frames+=f'<circle cx="{x+150}" cy="160" r="6" fill="rgba(212,162,127,.4)"/>'
    # sprocket holes
    holes=""
    for i in range(16):
        holes+=f'<rect x="{22+i*50}" y="34" width="20" height="12" rx="3" fill="rgba(255,255,255,.06)"/><rect x="{22+i*50}" y="274" width="20" height="12" rx="3" fill="rgba(255,255,255,.06)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Video without an editor","/remotion")}
      <svg width="820" height="330" viewBox="0 0 820 330" style="display:block">
        <rect x="6" y="20" width="808" height="280" rx="10" fill="rgba(255,255,255,.02)" stroke="rgba(255,255,255,.05)"/>
        {holes}{frames}</svg>
      <div style="display:flex;align-items:center;gap:16px;margin-top:6px">
        <div style="flex:1;height:12px;border-radius:999px;background:#221f1b;overflow:hidden;border:1px solid rgba(255,255,255,.06)">
          <div style="width:82%;height:100%;background:linear-gradient(90deg,#7a4326,rgb({ACC}))"></div></div>
        <span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">rendering · code, not clicks</span></div>
      {cap("scenes described in text, composed into finished video by code. no timeline.")}</div>'''

# 7. WRITER - Content Research Writer: an isometric conveyor research -> outline -> draft -> doc
def writer():
    steps=[("RESEARCH","31 sources pulled"),("OUTLINE","9 sections mapped"),("DRAFT","1,240 words, your voice")]
    cards=""
    for i,(nm,sub) in enumerate(steps):
        y=i*120
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:540px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
                f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:19px;color:rgb({ACC})">{i+1}</div>'
                f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
                f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div>'
                f'<svg width="26" height="26" viewBox="0 0 24 24" style="opacity:.5"><path d="M8 5l8 7-8 7" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Research to draft, end to end","/content-writer")}
      <div style="perspective:1900px;height:440px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(19deg) rotateZ(-8deg);width:540px;height:404px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:372px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Draft ready &#10003;</div></div></div>
      {cap("one chain: research feeds the outline, the outline feeds a draft in your voice.")}</div>'''

# 8. ADS - Competitive Ads Extractor: a wall of rival ad cards, a scan line, one pulled as live intel
def ads():
    random.seed(8); grid=""
    cols,rows=6,4; cw,ch=118,72; gx,gy=26,60
    hot=(3,1)
    for r in range(rows):
        for c in range(cols):
            x=gx+c*(cw+8); y=gy+r*(ch+8)
            on=(c,r)==hot
            bd=f"rgb({ACC})" if on else "rgba(255,255,255,.08)"
            bg="linear-gradient(160deg,#3a332c,#241f1a)" if on else "#201d19"
            glow="filter:drop-shadow(0 0 14px rgba(212,162,127,.5))" if on else ""
            grid+=(f'<g style="{glow}"><rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="10" fill="{bg}" stroke="{bd}" stroke-width="{2 if on else 1}"/>'
                   f'<rect x="{x+12}" y="{y+12}" width="{cw-24}" height="24" rx="5" fill="{"rgba(212,162,127,.35)" if on else "rgba(255,255,255,.07)"}"/>'
                   f'<rect x="{x+12}" y="{y+46}" width="{int((cw-24)*random.uniform(.5,.9))}" height="7" rx="3.5" fill="rgba(255,255,255,.12)"/></g>')
    scanx=gx+hot[0]*(cw+8)+cw/2
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Their ads, on your desk","/ads-extractor")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block">
        {grid}
        <line x1="{scanx:.0f}" y1="48" x2="{scanx:.0f}" y2="378" stroke="rgba(212,162,127,.4)" stroke-width="1.5" stroke-dasharray="4 6"/>
        <g transform="translate(520,320)"><rect x="0" y="0" width="278" height="70" rx="14" fill="#211d19" stroke="rgba(212,162,127,.35)" stroke-width="1.6"/>
        <text x="18" y="30" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">LIVE PULL</text>
        <text x="18" y="54" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">hook angle · offer · cadence</text></g></svg>
      {cap("scans rival ad libraries live and pulls the angle they are running right now.")}</div>'''

PANELS={"gaps":gaps(),"voice":voice(),"research":research(),"memory":memory(),
        "audio":audio(),"video":video(),"writer":writer(),"ads":ads()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src13"; os.makedirs(outd,exist_ok=True)
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
