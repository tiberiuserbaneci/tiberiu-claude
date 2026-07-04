#!/usr/bin/env python3
# THE 5AM SHIFT - Tier 3 panels. Each a UNIQUE hand-built coded scene on a clean rounded card,
# htitle + one-line cap, NO generic stat-chip strips, warm palette, cents. 8 distinct scene types:
# timeline / dot-field / node-graph / funnel / radial-hub(ivory) / iso-stack / gauge(ivory) / queue+gate.
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

# 1. CLOCK - vertical NIGHT TIMELINE: a 05:00 trigger fires, agents report down the night
def clock():
    events=[("05:00","Trigger fires","seven agents wake",True),
            ("05:18","CORTEX","900 accounts read",False),
            ("06:05","SPECTER","18 drafts queued",False),
            ("07:10","STRIKER","leads scored",False),
            ("08:20","PULSE + AMPLIFY","a week of posts",False),
            ("08:55","SENTINEL","PR opened",False)]
    rows=""
    for t,who,ev,trig in events:
        if trig:
            dot=('<div style="width:36px;height:36px;border-radius:50%;background:radial-gradient(circle at 34% 30%,#f0c49e,rgb('+ACC+') 58%,#7a4326);'
                 'border:2px solid rgba(212,162,127,.9);box-shadow:0 0 26px rgba(212,162,127,.75)"></div>')
            wc=f"rgb({ACC})"
        else:
            dot='<div style="width:19px;height:19px;border-radius:50%;background:#2a2724;border:2px solid rgba(212,162,127,.45)"></div>'
            wc="#FAFAF7"
        rows+=(f'<div style="display:flex;align-items:center;gap:22px;height:65px">'
          f'<div style="flex-shrink:0;width:54px;display:flex;justify-content:center;position:relative;z-index:2">{dot}</div>'
          f'<div style="flex:1">'
          f'<div style="display:flex;align-items:baseline;gap:14px">'
          f'<span style="font-family:\'DM Mono\';font-size:16px;letter-spacing:.06em;color:rgb({ACC})">{t}</span>'
          f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:{wc}">{who}</span></div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8f8f85;margin-top:1px">{ev}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Set once, runs every night","THE SCHEDULE")}
      <div style="position:relative;padding:8px 0">
        <div style="position:absolute;left:26px;top:26px;bottom:26px;width:2px;background:linear-gradient(180deg,rgb({ACC}),rgba(212,162,127,.12))"></div>
        {rows}
      </div>
      {cap("one schedule wires the whole team to the same 5AM alarm.")}</div>'''

# 2. BRIEF - DOT FIELD of accounts scanned overnight, a handful lit = the movers CORTEX ranked
def brief():
    cols,rowsn=45,20  # 900
    lit={73,168,301,412,559,640,733,806,877}
    cell=13; gap=4
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3.5" fill="rgba(250,250,247,.08)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">900</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">accounts, read</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">9 moved overnight</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("funding, hiring, stack changes: this morning's web, ranked before you wake.")}</div>'''

# 3. REACH - NODE GRAPH: three flagged accounts converge into SPECTER, fan out to a 3-step sequence
def reach():
    W,H=820,440
    accts=[("Northwind",90),("Globex",220),("Initech",350)]
    seq=[("Opener","day 0",90),("Follow-up 1","day 2",220),("Follow-up 2","day 5",350)]
    hubx,huby=400,220
    edges=""; nodes=""
    for nm,y in accts:
        edges+=f'<path d="M196 {y} C300 {y},310 {huby},{hubx-64} {huby}" stroke="rgba(212,162,127,.4)" stroke-width="2.2" fill="none"/>'
        nodes+=(f'<rect x="44" y="{y-27}" width="152" height="54" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="120" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="16" fill="#c9c3b8">{nm}</text>')
    for nm,d,y in seq:
        edges+=f'<path d="M{hubx+64} {huby} C540 {huby},560 {y},600 {y}" stroke="rgba(212,162,127,.5)" stroke-width="2.6" fill="none"/>'
        nodes+=(f'<rect x="600" y="{y-30}" width="196" height="60" rx="14" fill="#332f2a" stroke="rgba(212,162,127,.3)"/>'
          f'<text x="618" y="{y-4}" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">{nm}</text>'
          f'<text x="618" y="{y+18}" font-family="DM Mono" font-size="12.5" fill="#9a9488">{d}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One opener, two follow-ups","SPECTER")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}
        <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="62" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#1a0f0a">SPECTER</text>
        <text x="{hubx}" y="{huby+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">writes each</text>
        {nodes}
      </svg>
      {cap("a full sequence per flagged account, sitting in drafts for your review.")}</div>'''

# 4. DEALS - FUNNEL: inbound narrows to the two deals worth your time
def deals():
    cx=310; y=26; h=88; gap=14
    bands=[("Inbound","40"),("Qualified","12"),("Discovery","5"),("Proposal","2")]
    widths=[560,430,300,180,120]
    polys=""; labels=""
    for i,(nm,ct) in enumerate(bands):
        top=widths[i]; bot=widths[i+1]; yy=y+i*(h+gap)
        op=0.30+0.16*i
        polys+=(f'<polygon points="{cx-top/2:.0f},{yy} {cx+top/2:.0f},{yy} {cx+bot/2:.0f},{yy+h} {cx-bot/2:.0f},{yy+h}" '
          f'fill="rgba(212,162,127,{op:.2f})" stroke="rgba(212,162,127,.55)" stroke-width="1.5"/>')
        labels+=(f'<text x="{cx}" y="{yy+h/2-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#FAFAF7">{nm}</text>'
          f'<text x="{cx}" y="{yy+h/2+24:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="rgb({ACC})">{ct}</text>')
    fh=y+4*h+3*gap+20
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It sorted the inbound","STRIKER")}
      <svg width="620" height="{fh}" viewBox="0 0 620 {fh}" style="display:block;margin:0 auto">
        {polys}{labels}
      </svg>
      {cap("scored, noted and objection-ready: only the two real deals reach you.")}</div>'''

# 5. DRAFT - IVORY RADIAL HUB: one idea in the centre, one channel-ready post per spoke
def draft():
    cx,cy=306,222; Rr=158
    chans=[("LinkedIn",-90),("X",-18),("Newsletter",54),("Instagram",126),("Reel",198)]
    spokes=""
    for nm,a in chans:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        spokes+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.35)" stroke-width="2" stroke-dasharray="4 7"/>'
          f'<rect x="{x-72:.0f}" y="{y-24:.0f}" width="144" height="48" rx="14" fill="rgba(255,255,255,.72)" stroke="rgba(150,90,45,.28)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#2a2016">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("One idea, every channel","PULSE + AMPLIFY","#2a2016")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="idea" cx="38%" cy="32%"><stop offset="0%" stop-color="#e8b48c"/><stop offset="55%" stop-color="#b26a3e"/><stop offset="100%" stop-color="#96562d"/></radialGradient>
        <filter id="ig" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgba(150,90,45,.45)"/></filter></defs>
        {spokes}
        <g filter="url(#ig)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#idea)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#fdfbf6">1</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".14em" fill="#f6ead9">IDEA</text>
      </svg>
      {cap("written in your voice, reshaped per channel: post, thread, newsletter, reel.","#8a745a")}</div>'''

# 6. SHIP - ISO STACK: build -> test -> ship pipeline ending in a merged PR (SENTINEL)
def ship():
    steps=[("BUILD","wrote the landing page",0),("TEST","31 passed, 0 failed",1),("SHIP","live on main",2)]
    cards=""
    for nm,sub,i in steps:
        yy=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{yy}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Built, tested, shipped","SENTINEL")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:120px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Merged &#10003; PR #182</div></div></div>
      {cap("plain English in, a tested pull request out, opened before dawn.")}</div>'''

# 7. CENTS - IVORY GAUGE: the whole night's run costs cents; the old stack it replaces is the scary $
def cents():
    pct=94; r=76; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("A full night, in cents","METERED","#2a2016")}
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0;position:relative;width:210px;height:210px">
          <svg width="210" height="210" viewBox="0 0 210 210">
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="16"/>
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="#96562d" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 105 105)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:52px;color:#2a2016;line-height:1">3.4c</span>
            <span style="font-family:DM Mono;font-size:12px;color:#96562d;margin-top:2px">last night</span></div></div>
        <div style="flex:1;display:flex;flex-direction:column;gap:14px">
          <div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.66);border-left:4px solid #96562d;border-radius:12px;padding:16px 18px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg>
            <div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">The whole team, one night</div>
            <div style="font-family:DM Mono;font-size:13px;color:#8a745a">pay per token, nothing idle</div></div>
            <span style="font-family:DM Sans;font-weight:900;font-size:24px;color:#96562d">3.4c</span></div>
          <div style="display:flex;align-items:center;gap:16px;background:rgba(200,70,35,.07);border-left:4px solid rgba(200,70,35,.5);border-radius:12px;padding:16px 18px;opacity:.82">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb(200,70,35)" stroke-width="2.8"><path d="M18 6 6 18M6 6l12 12"/></svg>
            <div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#5a4634;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)">The old five-seat stack</div>
            <div style="font-family:DM Mono;font-size:13px;color:#a08a68">paid whether it ran or not</div></div>
            <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb(200,70,35)">$1,200/mo</span></div>
        </div>
      </div>
      {cap("you pay for the work done, not for seats sitting idle.","#8a745a")}</div>'''

# 8. WAKE - QUEUE behind the GATE: the night's moves parked, each pending your one tap
def wake():
    q=[("Send 18 cold emails","SPECTER"),("Publish 3 posts","AMPLIFY"),("Open PR #182","SENTINEL")]
    chips=""
    for act,who in q:
        chips+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:15px 18px;box-shadow:0 14px 26px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="flex-shrink:0;width:38px;height:38px;border-radius:11px;background:linear-gradient(160deg,#4a423a,#2a2622);display:flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,.10)">'
          f'<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{act}</div>'
          f'<div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.06em;color:#8f8f85">{who}</div></div>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});flex-shrink:0">PENDING</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Parked for your tap","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex:1;display:flex;flex-direction:column;gap:13px">{chips}</div>
        <div style="flex-shrink:0;display:flex;align-items:center;justify-content:center">
          <svg width="250" height="270" viewBox="0 0 250 270">
            <defs><radialGradient id="gorb" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
            <filter id="gog" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
            <g filter="url(#gog)"><circle cx="125" cy="120" r="98" fill="url(#gorb)"/></g>
            <g transform="translate(90,78)"><rect x="0" y="42" width="70" height="52" rx="12" fill="none" stroke="#2a160c" stroke-width="7"/><path d="M12 42 V26 a23 23 0 0 1 46 0 v16" fill="none" stroke="#2a160c" stroke-width="7"/></g>
            <text x="125" y="245" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#FAFAF7">YOUR TAP</text>
          </svg>
        </div>
      </div>
      {cap("nothing sent, nothing shipped, until you approve it at the gate.")}</div>'''

PANELS={"clock":clock(),"brief":brief(),"reach":reach(),"deals":deals(),
        "draft":draft(),"ship":ship(),"cents":cents(),"wake":wake()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src31"; os.makedirs(outd,exist_ok=True)
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
