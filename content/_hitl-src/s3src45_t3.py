#!/usr/bin/env python3
# TIER 3 - THE WALL AT LEVEL THREE. Adapted from IG "7 Levels" scrape, but built around the ONE wall:
# level 3 = Tools = the jump from ANSWERING to ACTING, where most people stall. Eight UNIQUE hand-built
# coded scenes, clean rounded CARD/CARDIV, warm palette, htitle + one cap each. No stat-chip strips.
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

# 1. WALL - elevation profile: two low steps, then a sheer cliff at level 3, ghost rungs 4-7 above,
#    a cohort of climber-dots piled at the base, one stalled mid-face.
def wall():
    base=410
    steps=(f'<rect x="70" y="368" width="120" height="{base-368}" rx="6" fill="#2a2723" stroke="rgba(255,255,255,.08)"/>'
           f'<rect x="190" y="324" width="120" height="{base-324}" rx="6" fill="#332e28" stroke="rgba(255,255,255,.09)"/>'
           f'<text x="130" y="{base-14}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#9a9488">LVL 1</text>'
           f'<text x="250" y="{base-14}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#c9c3b8">LVL 2</text>')
    # the cliff face at x=310, up from 324 to 120
    cliff=(f'<rect x="310" y="120" width="150" height="204" fill="rgba(200,70,35,.10)"/>'
           f'<line x1="310" y1="324" x2="310" y2="120" stroke="rgb({RED})" stroke-width="5"/>'
           f'<line x1="460" y1="324" x2="460" y2="120" stroke="rgba(200,70,35,.35)" stroke-width="2" stroke-dasharray="4 6"/>'
           f'<text x="385" y="232" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="rgb({RED})">3</text>'
           f'<text x="385" y="262" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#c98b6f">TOOLS</text>'
           f'<text x="385" y="150" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".12em" fill="#c98b6f">IT ACTS</text>')
    # ghost rungs 4-7 rising to the top right, dashed
    ghost=""
    gx,gy=460,120
    for i,n in enumerate((4,5,6,7)):
        x=gx+i*72; y=gy-i*22
        ghost+=(f'<rect x="{x}" y="{y-40}" width="60" height="40" rx="6" fill="rgba(212,162,127,.06)" stroke="rgba(212,162,127,.22)" stroke-dasharray="4 5"/>'
                f'<text x="{x+30}" y="{y-14}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#7a746a">{n}</text>')
    # cohort piled at base of the cliff + one stalled on the face
    dots=""
    for j in range(14):
        x=250+ (j%7)*10 - (14 if j>=7 else 0); y=base-8-(j//7)*12
        dots+=f'<circle cx="{x}" cy="{y}" r="5" fill="rgba(212,162,127,.5)"/>'
    dots+=f'<circle cx="308" cy="250" r="6.5" fill="rgb({ACC})" filter="url(#g1)"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Level 3 is a cliff, not a step","THE WALL")}
      <svg width="820" height="452" viewBox="0 0 820 452" style="display:block;margin:0 auto">
        <defs><filter id="g1" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <line x1="40" y1="{base}" x2="800" y2="{base}" stroke="rgba(255,255,255,.10)"/>
        {steps}{cliff}{ghost}{dots}</svg>
      {cap("one and two just talk. three is where it starts to act, and the crowd stops.")}</div>'''

# 2. JUMP - a half-circle dial: left half TALKS, right half ACTS, needle pinned at the red boundary.
def jump():
    cx,cy,R=410,300,196
    def pt(ang,rr):
        a=math.radians(180-ang); return cx+rr*math.cos(a), cy-rr*math.sin(a)
    lx1,ly1=pt(0,R); lx2,ly2=pt(90,R); rx2,ry2=pt(180,R)
    # left arc 0-90 muted, right arc 90-180 accent
    larc=f'M{lx1:.1f} {ly1:.1f} A{R} {R} 0 0 1 {lx2:.1f} {ly2:.1f}'
    rarc=f'M{lx2:.1f} {ly2:.1f} A{R} {R} 0 0 1 {rx2:.1f} {ry2:.1f}'
    # needle at boundary (top), leaning a touch into TALKS
    nx,ny=pt(84,R-24)
    ticks=""
    for ang in range(0,181,15):
        x1,y1=pt(ang,R-4); x2,y2=pt(ang,R-18)
        ticks+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Below three it answers. At three it does.","THE JUMP")}
      <svg width="820" height="360" viewBox="0 0 820 360" style="display:block;margin:0 auto">
        <defs><filter id="ng" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.8"/></filter></defs>
        <path d="{larc}" fill="none" stroke="rgba(212,162,127,.22)" stroke-width="20" stroke-linecap="round"/>
        <path d="{rarc}" fill="none" stroke="rgb({ACC})" stroke-width="20" stroke-linecap="round"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-R+2}" stroke="rgb({RED})" stroke-width="4"/>
        <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#FAFAF7" stroke-width="6" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="16" fill="#2a2724" stroke="rgb({ACC})" stroke-width="3"/>
        <text x="{cx-R+30}" y="{cy+34}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="21" fill="#9a9488">TALKS</text>
        <text x="{cx+R-30}" y="{cy+34}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="21" fill="rgb({ACC})">ACTS</text>
        <text x="{cx}" y="{cy-R-14}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({RED})">THE LINE</text>
      </svg>
      {cap("the whole ladder pivots on one move: from typing questions to taking actions.")}</div>'''

# 3. FREEZE - a column of ACTION toggles, all switched OFF (red), a cursor hovering on one.
def freeze():
    acts=[("Send outbound email","SPECTER"),("Edit and ship code","SENTINEL"),
          ("Book the meeting","STRIKER"),("Publish the post","AMPLIFY")]
    rows=""
    for i,(a,ag) in enumerate(acts):
        y=i*98
        cur=(f'<div style="position:absolute;right:-4px;top:26px"><svg width="30" height="30" viewBox="0 0 24 24" fill="#FAFAF7" stroke="#1a1816" stroke-width="1"><path d="M5 3l14 8-6 1.5L10 20 5 3z"/></svg></div>' if i==1 else '')
        rows+=(f'<div style="position:relative;background:linear-gradient(160deg,#332019,#241713);border:1.5px solid rgba(200,70,35,.30);border-radius:16px;padding:18px 22px;margin-bottom:14px;display:flex;align-items:center;justify-content:space-between">'
          f'<div><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#e8ded3">{a}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#c98b6f;margin-top:3px">{ag} &middot; capable, never allowed</div></div>'
          f'<div style="flex-shrink:0;width:72px;height:38px;border-radius:22px;background:rgba(200,70,35,.20);border:1.5px solid rgba(200,70,35,.5);position:relative">'
          f'<div style="position:absolute;left:5px;top:5px;width:26px;height:26px;border-radius:50%;background:rgb({RED})"></div></div>{cur}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("You left every action switched off","THE FREEZE")}
      <div style="margin-top:6px">{rows}</div>
      {cap("real power sits behind toggles most founders are too scared to flip on.")}</div>'''

# 4. TOOLS - bezier wiring: three agents on the left, each wired into a real system on the right.
def tools():
    pairs=[("SPECTER","the inbox",96),("SENTINEL","the repo",228),("AMPLIFY","the calendar",360)]
    edges=""; lnodes=""; rnodes=""
    for nm,sys,y in pairs:
        edges+=f'<path d="M228 {y} C400 {y},420 {y},600 {y}" fill="none" stroke="rgb({ACC})" stroke-width="4"/>'
        edges+=f'<circle cx="600" cy="{y}" r="6" fill="rgb({ACC})"/>'
        lnodes+=(f'<div style="position:absolute;left:0;top:{y-30}px;width:200px;background:linear-gradient(160deg,#3a342d,#241f1a);border:1.5px solid rgba(212,162,127,.34);border-radius:16px;padding:12px 16px">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:16px;color:#FAFAF7">an agent</div></div>')
        rnodes+=(f'<div style="position:absolute;left:600px;top:{y-30}px;width:210px;background:#201d19;border:1.5px solid rgba(255,255,255,.10);border-radius:16px;padding:12px 16px">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#8f8f85">REAL SYSTEM</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:17px;color:#e8ded3">{sys}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A tool is a wire into a real system","THE TOOLS")}
      <div style="position:relative;height:432px">
        <svg width="820" height="432" viewBox="0 0 820 432" style="position:absolute;left:0;top:0">{edges}</svg>
        {lnodes}{rnodes}</div>
      {cap("not a chat box, a hand. wire the agent to the inbox, the repo, the calendar.")}</div>'''

# 5. GATE - a queue of pending action chips held behind a gate line, one at your tap to approve.
def gate():
    q=[("draft to 12 prospects","queued"),("merge PR #182","queued"),("book Tue 09:30","queued")]
    chips=""
    for i,(a,st) in enumerate(q):
        y=40+i*84
        chips+=(f'<div style="position:absolute;left:0;top:{y}px;width:360px;background:#221f1b;border:1.5px solid rgba(255,255,255,.10);border-radius:14px;padding:14px 18px">'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#e8ded3">{a}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#8f8f85;margin-top:2px">{st} &middot; waiting</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Crossing is safe because it asks first","THE GATE")}
      <div style="position:relative;height:392px">
        {chips}
        <svg width="820" height="392" viewBox="0 0 820 392" style="position:absolute;left:0;top:0">
          <defs><filter id="gg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
          <line x1="410" y1="10" x2="410" y2="382" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="3 12" stroke-linecap="round"/>
          <text x="410" y="376" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="rgb({ACC})">HUMAN GATE</text>
          <g filter="url(#gg)"><rect x="560" y="120" width="200" height="150" rx="24" fill="#241f1a" stroke="rgb({ACC})" stroke-width="2.5"/></g>
          <path d="M628 196 l16 16 30-34" fill="none" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="660" y="252" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
        </svg></div>
      {cap("every external move parks for approval. this is what makes tools safe to switch on.")}</div>'''

# 6. PROOF - IVORY ledger of completed real actions with checkmarks + times, cents billed foot.
def proof():
    rows=[("12 outbound emails sent","09:14"),("3 pull requests merged","11:02"),
          ("8 meetings booked","14:30"),("1 landing page shipped","16:47")]
    rr=""
    for a,t in rows:
        rr+=(f'<div style="display:flex;align-items:center;gap:16px;padding:15px 4px;border-bottom:1px solid rgba(150,120,80,.16)">'
          f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:21px;color:#2a2016">{a}</span>'
          f'<span style="font-family:DM Mono;font-size:15px;color:#8a745a">{t}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It stopped answering. It shipped.</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">THE PROOF</span></div>
      <div>{rr}</div>
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-top:16px">
        <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#2a2016">Today, done</span>
        <span style="font-family:DM Mono;font-size:16px;color:#96562d">billed: a few cents</span></div>
      {cap("real actions, not more advice. and it costs cents, not a fat tool bill.","#8a745a")}</div>'''

# 7. UNLOCK - a lock springs open at the wall, the top rungs 4-7 light up as a rising stair.
def unlock():
    rungs=[("MCP",4),("SKILLS",5),("SUBAGENTS",6),("AGENT TEAMS",7)]
    cards=""
    for i,(nm,n) in enumerate(rungs):
        x=250+i*140; y=356-i*74
        cards+=(f'<g><rect x="{x}" y="{y-58}" width="128" height="58" rx="12" fill="#2f2a24" stroke="rgb({ACC})" stroke-width="2" filter="url(#ug)"/>'
          f'<rect x="{x}" y="{y-58}" width="128" height="58" rx="12" fill="rgba(212,162,127,.10)"/>'
          f'<text x="{x+64}" y="{y-30}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x+64}" y="{y-12}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">LVL {n}</text></g>')
        if i>0:
            px=250+(i-1)*140; py=356-(i-1)*74
            cards=(f'<line x1="{px+128}" y1="{py-29}" x2="{x}" y2="{y-29}" stroke="rgba(212,162,127,.4)" stroke-width="3" stroke-dasharray="5 6"/>')+cards
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Clear three and four to seven open","PAST THE WALL")}
      <svg width="820" height="410" viewBox="0 0 820 410" style="display:block;margin:0 auto">
        <defs><filter id="ug" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter></defs>
        <g transform="translate(70,300)"><rect x="0" y="34" width="72" height="56" rx="11" fill="none" stroke="rgb({ACC})" stroke-width="5"/>
          <path d="M14 34 V21 a22 22 0 0 1 44 -6" fill="none" stroke="rgb({ACC})" stroke-width="5"/>
          <circle cx="36" cy="60" r="7" fill="rgb({ACC})"/></g>
        <text x="106" y="404" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">UNLOCKED</text>
        {cards}</svg>
      {cap("the top rungs only unlock once the agent can act. this is where the pros climb.")}</div>'''

# 8. OPERATOR - a bridge across the chasm: TYPE ledge, spans marked TOOLS/GATE/ROUTER, OPERATOR orb.
def operator():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ultron starts you on the far side","THE OPERATOR")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="20" y="250" width="150" height="150" rx="10" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>
        <text x="95" y="316" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#9a9488">TYPE</text>
        <text x="95" y="342" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#7a746a">level 1</text>
        <rect x="650" y="250" width="150" height="150" rx="10" fill="#2a1d15" stroke="rgba(212,162,127,.3)"/>
        <path d="M170 262 C360 190,470 190,650 262" fill="none" stroke="rgb({ACC})" stroke-width="5"/>
        <path d="M170 300 C360 250,470 250,650 300" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="3" stroke-dasharray="4 8"/>
        <g font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})" text-anchor="middle">
          <text x="300" y="212">TOOLS</text><text x="410" y="198">GATE</text><text x="520" y="212">ROUTER</text></g>
        <g filter="url(#og)"><circle cx="725" cy="200" r="86" fill="url(#orb)"/></g>
        <text x="725" y="194" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">ONE</text>
        <text x="725" y="220" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">OPERATOR</text>
      </svg>
      {cap("tools, the router and the gate wired from day one. you begin where most quit.")}</div>'''

PANELS={"wall":wall(),"jump":jump(),"freeze":freeze(),"tools":tools(),
        "gate":gate(),"proof":proof(),"unlock":unlock(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src45"; os.makedirs(outd,exist_ok=True)
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
