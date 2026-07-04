#!/usr/bin/env python3
# TIER 3 - OUTPUT HAS NO CEILING (s3src55). The save-time -> multiply-output reframe: saved hours
# just hand back a slow human; operators point the same AI at 10x the volume they could never run
# alone. Eight UNIQUE hand-built coded scenes on clean rounded cards, htitle + one cap each. No
# generic stat-chip strips. Copied helpers/CARD/CARDIV/__main__ from aibody_t3.py.
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
def htiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CURVE - the HERO reframe: hours-saved (flat, muted) vs output (exponential, accent) line chart
def curve():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Saved hours are a flat line","LINEAR vs EXPONENTIAL")}
      <svg width="820" height="470" viewBox="0 0 820 470" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="og" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#8a4a2c"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
          <filter id="cg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.55"/></filter>
        </defs>
        <line x1="80" y1="60" x2="80" y2="400" stroke="rgba(250,250,247,.18)" stroke-width="2"/>
        <line x1="80" y1="400" x2="772" y2="400" stroke="rgba(250,250,247,.18)" stroke-width="2"/>
        {"".join(f'<line x1="80" y1="{y}" x2="772" y2="{y}" stroke="rgba(250,250,247,.05)"/>' for y in (130,220,310))}
        <path d="M80 372 C150 322,200 306,280 304 C440 300,610 305,772 305" fill="none" stroke="#6f6a60" stroke-width="4" stroke-linecap="round"/>
        <circle cx="772" cy="305" r="6" fill="#6f6a60"/>
        <text x="576" y="290" font-family="DM Mono" font-size="14" fill="#8f8f85">HOURS SAVED &middot; caps</text>
        <path d="M80 384 C320 380,500 358,610 300 C702 250,744 158,774 74" fill="none" stroke="url(#og)" stroke-width="6" stroke-linecap="round" filter="url(#cg)"/>
        <circle cx="774" cy="74" r="9" fill="rgb({ACC})" filter="url(#cg)"/>
        <text x="470" y="150" font-family="DM Sans" font-weight="900" font-size="22" fill="rgb({ACC})">OUTPUT</text>
        <text x="470" y="176" font-family="DM Mono" font-size="13" fill="#c9a583">no ceiling</text>
        <text x="92" y="80" font-family="DM Mono" font-size="12" fill="#8f8f85">volume out</text>
        <text x="646" y="424" font-family="DM Mono" font-size="12" fill="#8f8f85">time on the tool</text>
      </svg>
      {cap("two hours back caps at two hours. output has no ceiling.")}</div>'''

# 2. SERIAL - IVORY day-planner: one lane, six task blocks butted in a row, ends 6 done at 5PM
def serial():
    tasks=[("Emails","9:00"),("Calls","10:30"),("Deck","12:00"),("CRM","14:00"),("Post","15:30"),("Review","16:30")]
    blocks=""
    for t,tm in tasks:
        blocks+=f'''<div style="flex:1;background:linear-gradient(160deg,#efe3d0,#e2d2b8);border:1px solid rgba(150,90,45,.28);border-radius:12px;padding:16px 10px;text-align:center;box-shadow:inset 0 2px 2px rgba(255,255,255,.7)">
          <div style="font-family:'DM Sans';font-weight:800;font-size:18px;color:#2a2016">{t}</div>
          <div style="font-family:'DM Mono';font-size:12px;color:#96562d;margin-top:4px">{tm}</div></div>'''
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htiv("Time back is a slow human","ONE LANE")}
      <div style="display:flex;align-items:stretch;gap:10px;margin:26px 0 22px">{blocks}</div>
      <div style="position:relative;height:34px">
        <div style="position:absolute;left:0;right:0;top:15px;height:4px;background:repeating-linear-gradient(90deg,#c9b48f 0 16px,transparent 16px 30px)"></div>
        <div style="position:absolute;left:0;top:6px;font-family:'DM Mono';font-size:12px;color:#a08a68">start</div>
        <div style="position:absolute;right:0;top:0;background:#96562d;color:#fff;font-family:'DM Sans';font-weight:800;font-size:13px;padding:6px 14px;border-radius:999px">6 done &middot; 5PM</div>
      </div>
      {cap("you skipped the commute. you still do one thing at a time.","#8a745a")}</div>'''

# 3. FANOUT - one brief orb fans (bezier) into a grid of 60 output tiles
def fanout():
    cols,rows=12,5; gx0,gy0=360,70; tw,th=32,44; gapx,gapy=6,10
    tiles=""
    for i in range(cols*rows):
        r,c=divmod(i,cols); x=gx0+c*(tw+gapx); y=gy0+r*(th+gapy)
        fill=f"rgb({ACC})" if i%5==0 else "rgba(212,162,127,.17)"
        tiles+=f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="6" fill="{fill}"/>'
    orbx=140; orby=gy0+(rows*(th+gapy)-gapy)/2
    lines=""
    for r in range(rows):
        ty=gy0+r*(th+gapy)+th/2
        lines+=f'<path d="M{orbx+52} {orby:.0f} C260 {orby:.0f},280 {ty:.0f},{gx0-8} {ty:.0f}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One brief, sixty drafts","FAN-OUT")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="fo" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="fg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}
        <g filter="url(#fg)"><circle cx="{orbx}" cy="{orby:.0f}" r="56" fill="url(#fo)"/></g>
        <text x="{orbx}" y="{orby-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">1</text>
        <text x="{orbx}" y="{orby+18:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">brief</text>
        {tiles}
        <text x="{gx0}" y="{gy0-18}" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb({ACC})">60 DRAFTS OUT</text>
      </svg>
      {cap("the same prompt you run once, run sixty times over.")}</div>'''

# 4. PARALLEL - 7 agent swimlanes firing at once, a dim ghost solo lane above
def parallel():
    lanes=[("CORTEX","research",88),("SPECTER","outbound",76),("STRIKER","deals",64),
           ("PULSE","content",92),("SENTINEL","code",70),("AMPLIFY","publishing",81),("COUNSEL","legal",58)]
    rows=""
    for nm,role,pct in lanes:
        rows+=f'''<div style="display:flex;align-items:center;gap:16px">
          <div style="width:130px;flex-shrink:0"><div style="font-family:'DM Mono';font-size:14px;letter-spacing:.1em;color:#FAFAF7">{nm}</div><div style="font-family:'DM Sans';font-size:13px;color:#8f8f85">{role}</div></div>
          <div style="flex:1;height:20px;border-radius:999px;background:rgba(250,250,247,.06);overflow:hidden;position:relative">
            <div style="position:absolute;left:0;top:0;bottom:0;width:{pct}%;background:linear-gradient(90deg,#8a4a2c,rgb({ACC}));border-radius:999px"></div></div>
          <span style="width:66px;flex-shrink:0;text-align:right;font-family:'DM Mono';font-size:13px;color:rgb({ACC})">running</span></div>'''
    ghost='''<div style="display:flex;align-items:center;gap:16px;opacity:.5;margin-bottom:6px">
          <div style="width:130px;flex-shrink:0"><div style="font-family:'DM Mono';font-size:14px;letter-spacing:.1em;color:#8f8f85">YOU</div><div style="font-family:'DM Sans';font-size:13px;color:#6f6a60">one task</div></div>
          <div style="flex:1;height:20px;border-radius:999px;background:rgba(250,250,247,.05);overflow:hidden;position:relative">
            <div style="position:absolute;left:0;top:0;bottom:0;width:12%;background:#5a554c;border-radius:999px"></div></div>
          <span style="width:66px;flex-shrink:0;text-align:right;font-family:'DM Mono';font-size:13px;color:#6f6a60">serial</span></div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Seven desks fire at once","PARALLEL")}
      <div style="display:flex;flex-direction:column;gap:14px">{ghost}{rows}</div>
      {cap("research, outbound, deals, content, code, publishing, legal - together.")}</div>'''

# 5. FIELD - dot field of 945 accounts worked overnight, 15 lit = what one hand reaches
def field():
    cols,rowsn=45,21
    lit={40,86,132,178,224,270,316,362,408,203,249,295,341,159,115}
    cell,gap=13,3; dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:50px;color:#FAFAF7">945</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#c9a583;margin-left:12px">accounts worked overnight</span></div>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">15 BY HAND</span></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("fifteen accounts a day by hand. the field is the operator's morning.")}</div>'''

# 6. CENTS - IVORY cost-compare bars: a second hire ($4,000/mo) vs Ultron cents per run
def cents():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htiv("Tenfold output, cents to run","COST TO MULTIPLY")}
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:80px;height:352px;padding-top:6px">
        <div style="text-align:center;display:flex;flex-direction:column;align-items:center;height:100%;justify-content:flex-end">
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#6a5f4f">$4,000<span style="font-size:16px;font-weight:700">/mo</span></div>
          <div style="width:154px;height:292px;margin-top:12px;border-radius:16px 16px 0 0;background:linear-gradient(180deg,#9a8f80,#6a6155);box-shadow:inset 0 2px 3px rgba(255,255,255,.3)"></div>
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:#7a6c58;margin-top:14px">A SECOND HIRE</div>
        </div>
        <div style="text-align:center;display:flex;flex-direction:column;align-items:center;height:100%;justify-content:flex-end">
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#96562d">cents<span style="font-size:16px;font-weight:700">/run</span></div>
          <div style="width:154px;height:36px;margin-top:12px;border-radius:16px;background:linear-gradient(180deg,#d6a37c,#96562d);box-shadow:0 12px 22px rgba(150,90,45,.32),inset 0 2px 3px rgba(255,255,255,.5)"></div>
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.1em;color:#96562d;margin-top:14px">ULTRON &middot; PER TOKEN</div>
        </div>
      </div>
      {cap("more output, less bill. you pay per token, not per hire.","#8a745a")}</div>'''

# 7. GAUGE - big throughput ring dial reading 10x, tick marks around the rim
def gauge():
    cx,cy,r=155,160,120
    ticks=""
    for a in range(0,360,15):
        x1=cx+(r+10)*math.cos(math.radians(a)); y1=cy+(r+10)*math.sin(math.radians(a))
        x2=cx+(r+22)*math.cos(math.radians(a)); y2=cy+(r+22)*math.sin(math.radians(a))
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
    circ=2*math.pi*r; dash=circ*0.86
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:40px">
      <svg width="360" height="360" viewBox="0 0 360 360" style="flex-shrink:0">
        <defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#8a4a2c"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient>
        <filter id="gg2" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {ticks}
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(250,250,247,.08)" stroke-width="18"/>
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="url(#ga)" stroke-width="18" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 {cx} {cy})" filter="url(#gg2)"/>
        <text x="{cx}" y="{cy+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="78" fill="#FAFAF7">10x</text>
        <text x="{cx}" y="{cy+40}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="rgb({ACC})">output / day</text>
      </svg>
      <div style="flex:1">
        {htitle("Ten times is the floor","THROUGHPUT")}
        <div style="font-family:'DM Sans';font-size:19px;color:#c9c3b8;line-height:1.5">What one operator ships in a day used to take a small team a quarter. Same seat, same you, ten times the work out the door.</div>
        {cap("a team of one, running a team's volume.")}
      </div></div>'''

# 8. GATE - full-volume orb held on a dashed rein, one lock, your tap
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("The flood still parks","HUMAN GATE")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="orb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="og2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#og2)"><circle cx="200" cy="220" r="130" fill="url(#orb)"/></g>
        <text x="200" y="214" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="32" fill="#2a160c">10x</text>
        <text x="200" y="248" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#3a2010" letter-spacing=".1em">VOLUME</text>
        <path d="M334 220 H610" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <rect x="620" y="150" width="140" height="140" rx="30" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(662,188)"><rect x="0" y="34" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 34 V21 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="690" y="326" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">your tap</text>
      </svg>
      {cap("it can send at volume, but every external move waits for you.")}</div>'''

PANELS={"curve":curve(),"serial":serial(),"fanout":fanout(),"parallel":parallel(),
        "field":field(),"cents":cents(),"gauge":gauge(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src55"; os.makedirs(outd,exist_ok=True)
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
