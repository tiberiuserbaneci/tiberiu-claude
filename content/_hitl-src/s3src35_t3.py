#!/usr/bin/env python3
# TIER 3 - THE ATOMIZER (one idea in, every channel out) - rebuilt to the WIRE-ITS-EYES bar:
# each panel a UNIQUE hand-built coded scene filling a clean rounded card, title + one-line
# caption, NO generic stat-chip strips. Angle: one input -> many outputs, via PULSE + AMPLIFY.
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

# 1. FANOUT - HERO one-to-many: a single glowing IDEA orb on the left, bezier lines fan out to
# seven labeled output nodes on the right. The multiplication diagram (directed L->R fan).
def fanout():
    labels=["LinkedIn post","X thread","Newsletter","Image","Video script","Carousel","Short reel"]
    ox,oy=168,250; n=len(labels); y0,y1=42,458
    edges=""; nodes=""
    for i,lb in enumerate(labels):
        y=y0+(y1-y0)*i/(n-1); mx=(ox+468)/2
        edges+=f'<path d="M{ox+60} {oy} C{mx:.0f} {oy},{mx:.0f} {y:.0f},466 {y:.0f}" fill="none" stroke="rgba(212,162,127,.42)" stroke-width="2.4"/>'
        nodes+=(f'<rect x="470" y="{y-24:.0f}" width="330" height="48" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="500" cy="{y:.0f}" r="7" fill="rgb({ACC})"/>'
          f'<text x="524" y="{y+6:.0f}" font-family="DM Sans" font-weight="700" font-size="18" fill="#e2dccf">{lb}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One idea, seven outputs","1 &#8594; 7")}
      <svg width="820" height="500" viewBox="0 0 820 500">
        <defs><radialGradient id="idea" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="ig" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}
        <g filter="url(#ig)"><circle cx="{ox}" cy="{oy}" r="66" fill="url(#idea)"/></g>
        <text x="{ox}" y="{oy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">IDEA</text>
        <text x="{ox}" y="{oy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one note</text>
        {nodes}
      </svg>
      {cap("one note in, a post, thread, newsletter, image and scripts out.")}</div>'''

# 2. BRIEF - refine flow: a raw dashed note -> PULSE hub (three sharp question chips) -> a clean
# brief document. Horizontal node/flow graph (distinct from the fan and the iso grid).
def brief():
    qs=["Who is it for?","One core claim?","What proof?"]
    qchips=""
    for i,q in enumerate(qs):
        qy=34+i*48
        qchips+=(f'<rect x="298" y="{qy}" width="236" height="38" rx="11" fill="#221f1b" stroke="rgba(212,162,127,.3)"/>'
          f'<text x="316" y="{qy+24}" font-family="DM Sans" font-size="15" fill="#d9d5cc">{q}</text>'
          f'<line x1="416" y1="{qy+38}" x2="416" y2="248" stroke="rgba(212,162,127,.18)" stroke-width="1.4" stroke-dasharray="3 6"/>')
    docl="".join(f'<rect x="622" y="{206+i*26}" width="{146-i*10}" height="9" rx="4.5" fill="rgba(212,162,127,.30)"/>' for i in range(5))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("PULSE sharpens the idea","STEP 01 · BRIEF")}
      <svg width="820" height="470" viewBox="0 0 820 470">
        <defs><radialGradient id="pl" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="pg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <rect x="24" y="258" width="196" height="120" rx="16" fill="rgba(250,250,247,.03)" stroke="rgba(250,250,247,.18)" stroke-dasharray="5 6" stroke-width="1.5"/>
        <text x="122" y="300" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".12em" fill="#7a746a">RAW NOTE</text>
        <text x="122" y="326" text-anchor="middle" font-family="DM Sans" font-size="16" fill="#a8a296">"an idea about</text>
        <text x="122" y="348" text-anchor="middle" font-family="DM Sans" font-size="16" fill="#a8a296">cold outbound"</text>
        <path d="M220 318 C270 318,300 318,344 318" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>
        {qchips}
        <g filter="url(#pg)"><circle cx="416" cy="318" r="66" fill="url(#pl)"/></g>
        <text x="416" y="314" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">PULSE</text>
        <text x="416" y="336" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">asks first</text>
        <path d="M482 318 C548 318,566 250,606 250" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>
        <rect x="600" y="152" width="196" height="238" rx="14" fill="#2a2724" stroke="rgba(212,162,127,.35)"/>
        <rect x="600" y="152" width="196" height="40" rx="14" fill="rgba(212,162,127,.14)"/>
        <text x="622" y="178" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">BRIEF</text>
        {docl}
        <rect x="622" y="352" width="90" height="20" rx="6" fill="rgb({ACC})"/>
        <text x="667" y="366" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="12" fill="#1a0f0a">ready</text>
      </svg>
      {cap("your half-formed note becomes a clean brief, ready to write.")}</div>'''

# 3. MASTER - IVORY document: the one master piece, a proven hook, body lines, a pull-quote, and
# CORTEX-sourced citation chips down the side. A light article-page object (document scene).
def master():
    widths=[92,88,80,86,72]
    body="".join(f'<div style="height:10px;border-radius:5px;background:rgba(120,90,55,.22);width:{w}%;margin-bottom:14px"></div>' for w in widths)
    srcs=[("techcrunch.com","funding data"),("your CRM","real pipeline"),("g2.com","category proof")]
    chips="".join(f'''<div style="display:flex;align-items:center;gap:11px;background:rgba(255,255,255,.55);border:1px solid rgba(150,90,45,.22);border-radius:12px;padding:9px 12px;margin-bottom:10px">
        <div style="flex-shrink:0;width:28px;height:28px;border-radius:8px;background:#96562d;color:#fdfbf6;font-family:'DM Sans';font-weight:900;font-size:14px;display:flex;align-items:center;justify-content:center">{d[0].upper()}</div>
        <div><div style="font-family:'DM Mono';font-size:13px;color:#4a3f30">{d}</div><div style="font-family:'DM Sans';font-size:12px;color:#8a745a">{n}</div></div></div>''' for d,n in srcs)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">One master, sourced and hooked</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">STEP 02 &middot; WRITE</span></div>
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1;background:rgba(255,255,255,.62);border:1px solid rgba(150,90,45,.16);border-radius:18px;padding:26px 28px;box-shadow:inset 0 2px 3px rgba(255,255,255,.9)">
          <div style="display:inline-block;font-family:'DM Mono';font-size:11px;letter-spacing:.14em;color:#fdfbf6;background:#96562d;border-radius:999px;padding:5px 13px;margin-bottom:16px">PROVEN HOOK</div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#2a2016;line-height:1.16;margin-bottom:18px">I killed nine tools. The one I kept had no chat box.</div>
          {body}
          <div style="border-left:4px solid #96562d;padding:6px 0 6px 16px;margin-top:10px;font-family:'DM Sans';font-size:17px;color:#5a4634">One article. Every claim carries a source.</div>
        </div>
        <div style="width:252px;flex-shrink:0">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#96562d;margin-bottom:12px">SOURCED BY CORTEX</div>
          {chips}
        </div>
      </div>
      {cap("CORTEX pulls real web data, PULSE writes the one master piece.","#8a745a")}</div>'''

# 4. ATOMIZE - the atomization mechanic: the master splits into an ISOMETRIC grid of six output
# tiles, each a format sized for its channel. CSS 3D iso stack (distinct from every other scene).
def atomize():
    tiles=[("LinkedIn","900 words"),("X thread","7 posts"),("Newsletter","1,200 words"),
           ("Image","1080x1350"),("Video script","45 sec"),("Carousel","8 slides")]
    grid=""
    for i,(nm,meta) in enumerate(tiles):
        r,c=divmod(i,3); x=c*196; y=r*160
        grid+=f'''<div style="position:absolute;left:{x}px;top:{y}px;width:176px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:16px;padding:18px;
          box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1)">
          <div style="width:36px;height:36px;border-radius:10px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;margin-bottom:12px">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <div style="font-family:'DM Sans';font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div>
          <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC});margin-top:4px">{meta}</div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 44px 40px">
      {htitle("The master atomizes","1 &#8594; MANY")}
      <div style="perspective:2000px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-9deg);width:548px;height:316px;position:relative">{grid}</div></div>
      {cap("one master splits into every format, sized for each channel.")}</div>'''

# 5. VOICE - IVORY gauge: a 97% voice-match ring + a sample line, and TWO format rows (short thread
# vs long newsletter) both checked. Ring/gauge scene (light).
def voice():
    pct=97; r=74; circ=2*math.pi*r; dash=circ*pct/100
    rows=[("X thread","40 words"),("Newsletter","1,200 words")]
    fr="".join(f'''<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>
        <span style="font-family:'DM Sans';font-weight:700;font-size:16px;color:#2a2016">{a}</span>
        <span style="font-family:'DM Mono';font-size:13px;color:#8a745a">{b}</span></div>''' for a,b in rows)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Every format, your voice</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">VOICE LOCK</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <div style="flex-shrink:0;position:relative;width:190px;height:190px">
          <svg width="190" height="190" viewBox="0 0 190 190">
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="rgba(150,90,45,.18)" stroke-width="15"/>
            <circle cx="95" cy="95" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 95 95)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:'DM Sans';font-weight:900;font-size:44px;color:#2a2016">{pct}%</span>
            <span style="font-family:'DM Mono';font-size:12px;color:#96562d">style match</span></div></div>
        <div style="flex:1">
          <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:18px 20px;font-family:'DM Sans';font-size:20px;color:#2a2016;line-height:1.4;margin-bottom:18px">
            "Same short lines and no hedging, whether it is 40 words or 1,200."</div>
          {fr}
        </div>
      </div>
      {cap("a 40-word thread and a 1,200-word newsletter, the same cadence.","#8a745a")}</div>'''

# 6. SCHEDULE - AMPLIFY weekly timeline: seven day columns, each with one slotted post placed at
# its best time. A calendar/timeline scene (distinct from every graph and grid).
def schedule():
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    slots=[("LinkedIn","10:00",30),("X thread","12:30",96),("Newsletter","08:00",8),
           ("Reel","18:00",158),("Carousel","10:00",56),("Image","11:00",118),("X thread","09:00",44)]
    cols=""
    for i,d in enumerate(days):
        lb,tm,top=slots[i]
        cols+=f'''<div style="flex:1;display:flex;flex-direction:column;gap:10px">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:#8f8f85;text-align:center">{d}</div>
          <div style="flex:1;border-left:1px solid rgba(255,255,255,.06);position:relative">
            <div style="position:absolute;left:5px;right:0;top:{top}px;background:linear-gradient(160deg,#403a33,#241f1a);border:1px solid rgba(212,162,127,.4);border-radius:12px;padding:11px 9px;box-shadow:0 10px 20px rgba(0,0,0,.4)">
              <div style="font-family:'DM Sans';font-weight:800;font-size:14px;color:#FAFAF7">{lb}</div>
              <div style="font-family:'DM Mono';font-size:11px;color:rgb({ACC});margin-top:2px">{tm}</div></div>
          </div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("AMPLIFY slots each one","PER CHANNEL &middot; TZ")}
      <div style="display:flex;gap:9px;height:440px">{cols}</div>
      {cap("each format scheduled to its best channel, day and time zone.")}</div>'''

# 7. GATE - HUMAN GATE: a queue of five finished drafts held on the left, a dashed barrier, and one
# glowing TAP-TO-PUBLISH control on the right. Queue/barrier scene.
def gate():
    posts=[("LinkedIn",0),("X thread",26),("Newsletter",10),("Reel",34),("Carousel",4)]
    queue=""
    for i,(p,t) in enumerate(posts):
        x=i*94
        queue+=f'''<div style="position:absolute;left:{x}px;top:{t}px;width:82px;height:110px;background:linear-gradient(160deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.1);border-radius:12px;box-shadow:0 16px 26px rgba(0,0,0,.5);display:flex;flex-direction:column;justify-content:flex-end;padding:10px">
          <div style="font-family:'DM Sans';font-weight:700;font-size:13px;color:#e2dccf;line-height:1.15">{p}</div>
          <div style="font-family:'DM Mono';font-size:10px;letter-spacing:.06em;color:#c84623;margin-top:4px">HELD</div></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing ships without your tap","HUMAN GATE")}
      <div style="position:relative;height:440px">
        <div style="position:absolute;left:0;top:130px;font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#7a746a">QUEUE &middot; 5 DRAFTS</div>
        <div style="position:absolute;left:0;top:162px;width:490px;height:160px">{queue}</div>
        <div style="position:absolute;left:528px;top:110px;height:290px;border-left:3px dashed rgba(212,162,127,.6)"></div>
        <div style="position:absolute;left:568px;top:186px;width:216px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 55%,#9a5a35);border-radius:20px;padding:24px 22px;text-align:center;box-shadow:0 24px 44px rgba(212,162,127,.35), inset 0 2px 3px rgba(255,255,255,.4)">
          <svg width="40" height="40" viewBox="0 0 24 24" style="margin-bottom:6px"><rect x="4" y="10.5" width="16" height="11" rx="2.6" fill="none" stroke="#1a0f0a" stroke-width="2.2"/><path d="M7.4 10.5V7.6a4.6 4.6 0 0 1 9.2 0v2.9" fill="none" stroke="#1a0f0a" stroke-width="2.2"/></svg>
          <div style="font-family:'DM Sans';font-weight:900;font-size:23px;color:#1a0f0a">YOUR TAP</div>
          <div style="font-family:'DM Mono';font-size:12px;color:#3a2010;margin-top:4px">approve to publish</div></div>
      </div>
      {cap("every draft parks at the gate. one tap sends it live.")}</div>'''

# 8. ENGINE - convergence hub: a central login orb with seven channel spokes feeding into one
# reach readout. Radial hub-and-spokes (many->one, distinct from the L->R fan of scene 1).
def engine():
    cx,cy,R=410,232,166
    chans=["LinkedIn","X","News","IG","YouTube","TikTok","Blog"]
    spokes=""; n=len(chans)
    for i,ch in enumerate(chans):
        a=-90+360*i/n
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.38)" stroke-width="2"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#241f1a" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11.5" fill="#cfc9bd">{ch}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One login, the whole engine","ONE SYSTEM")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="eng" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="54%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="eg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#eg)"><circle cx="{cx}" cy="{cy}" r="80" fill="url(#eng)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">ONE</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">LOGIN</text>
      </svg>
      {cap("PULSE writes, AMPLIFY ships, you press publish once.")}</div>'''

PANELS={"fanout":fanout(),"brief":brief(),"master":master(),"atomize":atomize(),
        "voice":voice(),"schedule":schedule(),"gate":gate(),"engine":engine()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src35"; os.makedirs(outd,exist_ok=True)
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
