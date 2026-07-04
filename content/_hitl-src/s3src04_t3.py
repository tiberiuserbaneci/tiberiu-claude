#!/usr/bin/env python3
# TIER 3 - THE HANDOFF IS THE PRODUCT. Adapted from an IG carousel ("build a Claude 4-agent team
# that ships"). Rebuilt to the WIRE-ITS-EYES bar: each of 8 panels is a UNIQUE hand-built coded
# scene filling a clean rounded card, htitle + one mono caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; RED="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. BOTTLENECK - dark: 4 step chips around a red YOU core, every baton copy-pasted back through you
def bottleneck():
    cx,cy=380,225
    chips=[("PLAN",380,60,"paste"),("CODE",610,225,"copy"),("TEST",380,390,"paste"),("REVIEW",150,225,"copy")]
    seg=""
    for nm,x,y,lab in chips:
        mx,my=(cx+x)/2,(cy+y)/2
        seg+=(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="rgb({RED})" stroke-width="3" stroke-dasharray="4 8" opacity="0.75"/>'
          f'<text x="{mx:.0f}" y="{my-8:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgba(200,70,35,.85)">{lab}</text>'
          f'<g><rect x="{x-70}" y="{y-29}" width="140" height="58" rx="14" fill="#232019" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#e7e1d5">{nm}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You are the copy-paste","THE GLUE",tagc=f"rgb({RED})")}
      <svg width="760" height="470" viewBox="0 0 760 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="you" cx="38%" cy="32%"><stop offset="0%" stop-color="#e79274"/><stop offset="60%" stop-color="rgb({RED})"/><stop offset="100%" stop-color="#6e1f0e"/></radialGradient>
        <filter id="yg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({RED})" flood-opacity="0.55"/></filter></defs>
        {seg}
        <path d="M{cx-64} {cy} a64 64 0 1 1 6 40" fill="none" stroke="rgba(200,70,35,.5)" stroke-width="2.4" stroke-dasharray="3 7"/>
        <g filter="url(#yg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#you)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a0f06">YOU</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a1108" letter-spacing=".1em">ctrl+c ctrl+v</text>
      </svg>
      {cap("plan, code, test, review. every baton lands back in your hands.")}</div>'''

# 2. PIPELINE - dark: 4 specialist nodes hand off automatically L to R, a lit baton, output pill
def pipeline():
    nodes=[("PLAN",95),("CODE",300),("TEST",505),("REVIEW",710)]
    ny=140; circ=""
    for nm,x in nodes:
        circ+=(f'<circle cx="{x}" cy="{ny}" r="48" fill="#241f1a" stroke="rgb({ACC})" stroke-width="2.5"/>'
          f'<text x="{x}" y="{ny+6}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">{nm}</text>')
    edges=""
    for i in range(3):
        x0=nodes[i][1]+48; x1=nodes[i+1][1]-48
        edges+=(f'<path d="M{x0} {ny} C{x0+50} {ny},{x1-50} {ny},{x1} {ny}" fill="none" stroke="rgb({ACC})" stroke-width="4"/>'
          f'<path d="M{x1-14} {ny-8} L{x1} {ny} L{x1-14} {ny+8}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    # baton on second edge
    bx=(nodes[1][1]+48+nodes[2][1]-48)/2
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("They hand off themselves","AUTO PIPELINE")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs><filter id="bt" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter>
        <radialGradient id="ship" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient></defs>
        {edges}{circ}
        <circle cx="{bx:.0f}" cy="{ny}" r="11" fill="rgb({ACC})" filter="url(#bt)"/>
        <text x="{bx:.0f}" y="{ny-24:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">baton</text>
        <path d="M710 188 C710 300,410 300,410 340" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="3" stroke-dasharray="2 10"/>
        <g filter="url(#bt)"><rect x="250" y="332" width="320" height="96" rx="24" fill="url(#ship)"/></g>
        <text x="410" y="374" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">FEATURE SHIPPED</text>
        <text x="410" y="402" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".08em">finished, reviewed, tested</text>
      </svg>
      {cap("one command in, a finished feature out. no baton ever touches you.")}</div>'''

# 3. COMMAND - dark: a terminal window mockup, one plain-English command runs the whole pipeline
def command():
    rows=[("plan","done",True),("code","done",True),("test","running",False),("review","queued",False)]
    rowh=""
    for nm,st,done in rows:
        mark=(f'<span style="color:rgb({ACC})">&#10003;</span>' if done else
              (f'<span style="color:rgb({ACC})">&#9679;</span>' if st=="running" else '<span style="color:#6f6a60">&#8226;</span>'))
        stc=f"rgb({ACC})" if done else ("#d9d5cc" if st=="running" else "#6f6a60")
        rowh+=(f'<div style="display:flex;align-items:center;gap:14px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.05)">'
          f'<span style="width:16px;text-align:center;font-family:DM Mono;font-size:16px">{mark}</span>'
          f'<span style="flex:1;font-family:DM Mono;font-size:16px;color:#c9c3b8">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:14px;color:{stc}">{st}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One command kicks it off","THE TRIGGER")}
      <div style="margin:6px auto 0;width:720px;background:linear-gradient(165deg,#141310,#0b0a09);border:1px solid rgba(255,255,255,.08);border-radius:20px;overflow:hidden;box-shadow:0 26px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.06)">
        <div style="display:flex;align-items:center;gap:9px;padding:15px 20px;border-bottom:1px solid rgba(255,255,255,.06)">
          <span style="width:12px;height:12px;border-radius:50%;background:rgb({RED})"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:rgb({ACC})"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#4a453d"></span>
          <span style="margin-left:12px;font-family:DM Mono;font-size:13px;color:#8f8f85;letter-spacing:.08em">sentinel &middot; ship</span></div>
        <div style="padding:24px 26px 22px">
          <div style="font-family:DM Mono;font-size:18px;color:#e7e1d5"><span style="color:rgb({ACC})">$</span> /ship-feature <span style="color:#8f8f85">"add a billing page"</span></div>
          <div style="font-family:DM Mono;font-size:15px;color:rgb({ACC});margin:12px 0 16px">&gt; routing to 4 agents...</div>
          {rowh}
        </div></div>
      {cap("you describe the feature in plain english. the pipeline runs itself.")}</div>'''

# 4. PLAN - IVORY: a blueprint doc, the first agent scopes the ask into a checked build plan
def plan():
    tasks=["Scope the billing page","Map the screen states","Define the data it needs","List the edge cases","Hand off to the build"]
    rowh=""
    for i,t in enumerate(tasks):
        rowh+=(f'<div style="display:flex;align-items:center;gap:16px;padding:13px 0;{"border-bottom:1px solid rgba(120,95,60,.14)" if i<len(tasks)-1 else ""}">'
          f'<svg width="26" height="26" viewBox="0 0 26 26"><rect x="1.5" y="1.5" width="23" height="23" rx="6" fill="rgba(150,90,45,.10)" stroke="#96562d" stroke-width="2"/><path d="M7 13.5l4 4L19 8.5" fill="none" stroke="#96562d" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:20px;color:#2a2016">{t}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("It reads the ask, drafts the plan","AGENT 1 &middot; PLAN",ink="#2a2016",tagc="#96562d")}
      <div style="position:relative;background:rgba(255,255,255,.62);border:1px solid rgba(120,95,60,.18);border-left:5px solid #96562d;border-radius:16px;padding:20px 26px 22px;box-shadow:0 18px 34px rgba(120,95,60,.14)">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:6px">
          <span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#2a2016">BUILD PLAN</span>
          <span style="font-family:DM Mono;font-size:13px;color:#96562d">5 / 5 scoped</span></div>
        {rowh}
        <svg width="34" height="34" viewBox="0 0 24 24" style="position:absolute;top:-14px;right:-10px"><path d="M12 2l2.2 6.4L21 10.6l-5.4 4 1.9 6.8L12 17.7 6.5 21.4l1.9-6.8L3 10.6l6.8-2.2z" fill="#96562d" opacity=".9"/></svg>
      </div>
      {cap("no blank page. the request becomes a scoped, ordered plan.","#8a745a")}</div>'''

# 5. CODE - dark: SENTINEL turns the plan into a working build, modules filling to complete
def code():
    mods=[("Page &amp; layout",100),("Data &amp; logic",100),("States &amp; errors",100),("Tests wired in",100)]
    bars=""
    for nm,pct in mods:
        bars+=(f'<div style="margin-bottom:20px"><div style="display:flex;justify-content:space-between;margin-bottom:8px">'
          f'<span style="font-family:DM Sans;font-weight:600;font-size:18px;color:#e7e1d5">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">built</span></div>'
          f'<div style="height:14px;border-radius:8px;background:rgba(255,255,255,.06);overflow:hidden">'
          f'<div style="height:100%;width:{pct}%;border-radius:8px;background:linear-gradient(90deg,#7a4326,rgb({ACC}));box-shadow:0 0 16px rgba(212,162,127,.4)"></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 32px">
      {htitle("It writes the working build","AGENT 2 &middot; CODE")}
      <div style="display:flex;gap:30px;align-items:center">
        <div style="flex-shrink:0;width:250px;background:#1c1916;border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:20px 18px">
          <div style="font-family:DM Mono;font-size:13px;color:#8f8f85;letter-spacing:.1em;margin-bottom:14px">SENTINEL</div>
          {''.join(f'<div style="display:flex;align-items:center;gap:11px;padding:8px 0"><svg width="20" height="20" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">{f}</span></div>' for f in ["9 files written","0 left to do","clean, working"])}
        </div>
        <div style="flex:1">{bars}</div>
      </div>
      {cap("plain english in, a real build out. the plan becomes working software.")}</div>'''

# 6. TEST - dark: a full pass gauge next to a 48-dot field, every check lit, none red
def test():
    r=74; circ=2*math.pi*r
    dots=""
    for i in range(48):
        col=i//8; row=i%8
        x=18+col*44; y=14+row*44
        dots+=f'<circle cx="{x}" cy="{y}" r="9" fill="rgb({ACC})" opacity="0.92"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It tests every path first","AGENT 3 &middot; TEST")}
      <div style="display:flex;align-items:center;gap:40px;justify-content:center;padding:6px 0">
        <div style="position:relative;width:210px;height:210px;flex-shrink:0">
          <svg width="210" height="210" viewBox="0 0 210 210">
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="16"/>
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="16" stroke-linecap="round" stroke-dasharray="{circ:.0f} {circ:.0f}" transform="rotate(-90 105 105)" style="filter:drop-shadow(0 0 12px rgba(212,162,127,.5))"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:42px;color:#FAFAF7">48/48</span>
            <span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">0 failed</span></div></div>
        <svg width="290" height="350" viewBox="0 0 290 350" style="flex-shrink:0">{dots}</svg>
      </div>
      {cap("48 checks pass, 0 fail. the agent breaks it so you never have to.")}</div>'''

# 7. REVIEW + GATE - dark: a wax-seal approval, then the run parks at a lock for the operator's tap
def review():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It reviews, then waits for you","AGENT 4 &middot; REVIEW + GATE")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <g filter="url(#sg)"><circle cx="195" cy="200" r="118" fill="url(#seal)"/></g>
        <circle cx="195" cy="200" r="98" fill="none" stroke="rgba(42,15,6,.35)" stroke-width="2" stroke-dasharray="4 7"/>
        <text x="195" y="192" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">REVIEWED</text>
        <text x="195" y="224" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#3a2010" letter-spacing=".12em">polished &middot; approved</text>
        <text x="195" y="356" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">typos, naming, edge cases</text>
        <path d="M323 200 H600" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="610" y="128" width="146" height="146" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(654,168)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="683" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
        <text x="683" y="344" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">HUMAN GATE</text>
      </svg>
      {cap("cleaned and approved, then it stops at your yes. never unsupervised.")}</div>'''

# 8. DELIVERED - IVORY: an overnight timeline, four handoffs done, ending in a merged feature card
def delivered():
    ticks=[("plan",90),("code",250),("test",410),("review",570)]
    tk=""
    for nm,x in ticks:
        tk+=(f'<circle cx="{x}" cy="150" r="12" fill="#96562d"/>'
          f'<path d="M{x-4} 150l3 3 6-7" fill="none" stroke="#fdfbf6" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<text x="{x}" y="188" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#7a5c3c">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("You come back to a shipped feature","DELIVERED",ink="#2a2016",tagc="#96562d")}
      <svg width="740" height="300" viewBox="0 0 740 300" style="display:block;margin:0 auto">
        <line x1="30" y1="150" x2="690" y2="150" stroke="rgba(150,90,45,.35)" stroke-width="3"/>
        <text x="30" y="118" font-family="DM Sans" font-weight="700" font-size="16" fill="#2a2016">you log off</text>
        <text x="30" y="138" font-family="DM Mono" font-size="12" fill="#8a745a">11:40 PM</text>
        {tk}
        <g><rect x="600" y="98" width="132" height="104" rx="18" fill="#96562d"/>
        <text x="666" y="140" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#fdfbf6">MERGED</text>
        <text x="666" y="166" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgba(253,251,246,.85)">07:02 AM</text></g>
      </svg>
      {cap("no babysitting, no copy-paste between agents, no manual work. just done.","#8a745a")}</div>'''

PANELS={"bottleneck":bottleneck(),"pipeline":pipeline(),"command":command(),"plan":plan(),
        "code":code(),"test":test(),"review":review(),"delivered":delivered()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src04"; os.makedirs(outd,exist_ok=True)
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
