#!/usr/bin/env python3
# TIER 3 - THE UNBUILT WEDGES (s3src46) on the WIRE-ITS-EYES bar: 8 unique hand-built coded scenes,
# each an under-built AI-agent company idea + the wedge to win it, all buildable solo on Ultron.
# Clean rounded CARD/CARDIV only, warm palette, htitle + one cap each. NO generic stat-chip strips.
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
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. SURFACE - 960 dull-workflow dot field, a handful lit = the companies nobody shipped yet
def surface():
    cols,rowsn=40,24
    lit={57,166,283,391,520,648,712,833,905}
    cell=15; gap=4; dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in lit:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({ACC})" filter="url(#lg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.09)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:36px 40px 36px">
      {htitle("The boring jobs are unclaimed","THE SURFACE")}
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7">960</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:20px;color:#c9a583;margin-left:10px">repeated workflows</span></div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">9 with no agent yet</div></div>
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="lg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {dots}</svg>
      {cap("every dull, repeated task is a company nobody has bothered to ship.")}</div>'''

# 2. TAXFILER - IVORY bezier: four source documents converge into one e-filed return
def taxfiler():
    W,H=820,430
    src=[("W-2",90),("1099-NEC",180),("Receipts",270),("Last year",360)]
    hubx,huby=648,225
    edges=""; nodes=""
    for nm,y in src:
        mx=(190+hubx)/2
        edges+=f'<path d="M196 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-78} {huby}" stroke="#b98a5f" stroke-width="2.6" fill="none" opacity="0.8"/>'
        nodes+=(f'<rect x="40" y="{y-27}" width="156" height="54" rx="13" fill="#fbf6ec" stroke="rgba(120,95,60,.30)"/>'
          f'<rect x="56" y="{y-13}" width="20" height="26" rx="3" fill="none" stroke="#a07a52" stroke-width="2"/>'
          f'<text x="90" y="{y+6}" font-family="DM Mono" font-size="16" fill="#4a3f30">{nm}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 40px 34px">
      {htitle_iv("Taxes that file themselves","END TO END")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="tf" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
        <filter id="tg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="rgba(150,90,45,.4)"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#tg)"><circle cx="{hubx}" cy="{huby}" r="88" fill="url(#tf)"/></g>
        <circle cx="{hubx}" cy="{huby}" r="88" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/>
        <path d="M{hubx-30} {huby-2} l20 22 l42 -50" fill="none" stroke="#2a160c" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
        <text x="{hubx}" y="{huby+48}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">FILED</text>
        <text x="{hubx}" y="{huby+118}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#8a6a44">e-filed, every deduction</text>
      </svg>
      {cap("people pay for done, not for another calculator that helps.","#8a745a")}</div>'''

# 3. RISKPOOL - radial hub-and-spokes: one policy core, many AI-company agents as policyholders
def riskpool():
    cx,cy=250,225; Rr=175
    holders=[("refund bot",-90),("email agent",-38),("billing bot",14),("scheduler",66),
             ("support bot",118),("voice agent",170),("pricing bot",222),("outreach bot",274)]
    spokes=""; nodes=""
    for nm,a in holders:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#241f1a" stroke="rgba(255,255,255,.13)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="500" height="470" viewBox="0 0 500 470">
        <defs><radialGradient id="pol" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="pg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}
        <g filter="url(#pg)"><circle cx="{cx}" cy="{cy}" r="70" fill="url(#pol)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a160c">POLICY</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">pays the claim</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("Insurance for when AI slips","RISK POOL")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">A wrong refund, a rogue email, a bad payment. When an agent costs a business money, this is the policy that covers it.</div>
        {cap("every company running agents becomes a policyholder.")}</div></div>'''

# 4. COLLECTOR - vertical funnel: overdue invoices narrow down to cash recovered
def collector():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Collections that actually collect","PAID ON OUTCOME")}
      <svg width="760" height="460" viewBox="0 0 760 460" style="display:block;margin:0 auto">
        <defs><linearGradient id="fA" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#221f1b"/></linearGradient>
        <linearGradient id="fB" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#e6b48f"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#9a5a35"/></linearGradient></defs>
        <!-- funnel walls -->
        <polygon points="80,116 680,116 590,190 170,190" fill="rgba(212,162,127,.07)"/>
        <polygon points="170,270 590,270 490,344 270,344" fill="rgba(212,162,127,.10)"/>
        <!-- stage 1 -->
        <rect x="80" y="20" width="600" height="96" rx="16" fill="url(#fA)" stroke="rgba(255,255,255,.10)"/>
        <text x="112" y="62" font-family="DM Sans" font-weight="900" font-size="34" fill="#FAFAF7">412 invoices</text>
        <text x="112" y="92" font-family="DM Sans" font-size="17" fill="#a8a296">overdue, gathering dust</text>
        <text x="648" y="74" text-anchor="end" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb({ACC})">STAGE 1</text>
        <!-- stage 2 -->
        <rect x="170" y="190" width="420" height="80" rx="14" fill="url(#fA)" stroke="rgba(255,255,255,.10)"/>
        <text x="200" y="228" font-family="DM Sans" font-weight="800" font-size="22" fill="#FAFAF7">reminders, calls, offers</text>
        <text x="200" y="252" font-family="DM Sans" font-size="15" fill="#a8a296">chased on a schedule, never rude</text>
        <!-- stage 3 -->
        <rect x="270" y="344" width="220" height="96" rx="16" fill="url(#fB)"/>
        <text x="380" y="388" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="38" fill="#1a0f0a">$68K</text>
        <text x="380" y="416" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#3a2010">RECOVERED</text>
      </svg>
      {cap("you earn a slice of what it recovers, not a flat monthly seat.")}</div>'''

# 5. SOURCER - isometric stack of ranked candidate cards (recruiter-in-a-box)
def sourcer():
    rows=[("Maria Ilves","3 ops roles matched","94"),
          ("Devon Park","ex-Stripe AR lead","90"),
          ("Priya Nair","screened, booked Tue 10:00","88")]
    cards=""
    for i,(a,b,c) in enumerate(rows):
        y=i*150
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.16);border-radius:18px;padding:22px 24px;
          box-shadow:0 34px 50px rgba(0,0,0,.6), inset 0 2px 2px rgba(255,255,255,.10);display:flex;align-items:center;gap:22px">
          <div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:22px;color:rgb({ACC})">{a[0]}</div>
          <div style="flex:1;text-align:left"><div style="font-family:'DM Sans';font-weight:800;font-size:24px;color:#FAFAF7">{a}</div>
          <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;margin-top:2px">{b}</div></div>
          <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;background:rgb({ACC});padding:9px 17px;border-radius:12px;box-shadow:0 6px 14px rgba({ACC},.4)">
            <span style="font-family:'DM Sans';font-weight:900;font-size:24px;color:#1a0f0a;line-height:1">{c}</span>
            <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:rgba(26,15,10,.7)">MATCH</span></div></div>'''
    return f'''<div style="width:900px;{CARD};padding:38px 44px 44px">
      {htitle("Sourced, screened, booked","KILL THE RETAINER")}
      <div style="perspective:2000px;height:560px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(22deg) rotateZ(-9deg);width:600px;height:490px;position:relative">{cards}</div></div>
      {cap("cents a candidate, not an 18K recruiter retainer.")}</div>'''

# 6. NEGOTIATOR - IVORY split-compare: the software bill before vs after the renewal agent
def negotiator():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle_iv("It renews your software cheaper","BEFORE / AFTER")}
      <div style="display:flex;flex-direction:column;gap:26px;margin-top:6px">
        <div>
          <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:10px">
            <span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#5a4634">Your SaaS bill today</span>
            <span style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#4a3f30">$2,400<span style="font-family:'DM Mono';font-size:14px;color:#a08a68"> /mo</span></span></div>
          <div style="height:34px;border-radius:10px;background:rgba(150,120,80,.22);overflow:hidden">
            <div style="width:100%;height:100%;background:repeating-linear-gradient(135deg,rgba(120,95,60,.32),rgba(120,95,60,.32) 10px,rgba(120,95,60,.20) 10px,rgba(120,95,60,.20) 20px)"></div></div>
        </div>
        <div>
          <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:10px">
            <span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#5a4634">After the agent negotiates</span>
            <span style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#96562d">$1,510<span style="font-family:'DM Mono';font-size:14px;color:#a08a68"> /mo</span></span></div>
          <div style="height:34px;border-radius:10px;background:rgba(150,120,80,.16);overflow:hidden">
            <div style="width:63%;height:100%;background:linear-gradient(90deg,#e6b48f,#96562d)"></div></div>
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:26px;background:rgba(255,255,255,.55);border-left:4px solid #96562d;border-radius:12px;padding:16px 20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#2a2016">Saved $890 every month</span>
        <span style="font-family:'DM Mono';font-size:13px;color:#96562d">agent runs for cents</span></div>
      {cap("it pays for itself on the first renewal it trims.","#8a745a")}</div>'''

# 7. FRONTDESK - radar sweep of inbound calls, one caught readout (the AI receptionist)
def frontdesk():
    cx,cy,R=210,220,190
    rings="".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(212,162,127,.16)"/>' for r in (63,126,190))
    blips=[("New quote",300,150),("After hours",120,96),("Booking",210,168),("Callback",40,120)]
    bl=""
    for nm,ang,dist in blips:
        x=cx+dist*math.cos(math.radians(ang)); y=cy+dist*math.sin(math.radians(ang))
        bl+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="rgb({ACC})" filter="url(#b)"/>'
          f'<text x="{x:.0f}" y="{y-16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#d9d5cc">{nm}</text>')
    lead=('<div style="background:#211d19;border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:18px 20px">'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px"><span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">Calls caught after 6pm</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">live</span></div>'
      f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Sans;font-size:17px;color:#8f8f85">Sent to voicemail</span><span style="font-family:DM Mono;font-size:14px;color:#8f8f85">0</span></div>'
      f'<div style="border-top:1px solid rgba(255,255,255,.08);margin-top:14px;padding-top:14px;font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC})">17 booked</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><radialGradient id="sw" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(212,162,127,.5)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient>
        <filter id="b" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="#1a1816"/>{rings}
        <line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="rgba(212,162,127,.12)"/><line x1="{cx}" y1="{cy-R}" x2="{cx}" y2="{cy+R}" stroke="rgba(212,162,127,.12)"/>
        <path d="M{cx} {cy} L{cx} {cy-R} A{R} {R} 0 0 1 {cx+R*math.sin(math.radians(64)):.0f} {cy-R*math.cos(math.radians(64)):.0f} Z" fill="url(#sw)"/>
        {bl}<circle cx="{cx}" cy="{cy}" r="7" fill="rgb({ACC})"/></svg>
      <div style="flex:1">
        {htitle("It answers missed calls","ALWAYS ON")}
        {lead}
        {cap("the front desk for every trade that still misses the phone.")}
      </div></div>'''

# 8. ECONOMICS - ring gauge: run cost in cents, margin kept (why any of these is a business)
def economics():
    pct=98; r=78; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARD};padding:36px 42px 34px">
      {htitle("Any of these runs on cents","CENTS TO RUN")}
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0;position:relative;width:210px;height:210px">
          <svg width="210" height="210" viewBox="0 0 210 210">
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgba(212,162,127,.16)" stroke-width="17"/>
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="17" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 105 105)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:46px;color:#FAFAF7">98%</span>
            <span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">margin kept</span></div></div>
        <div style="flex:1;display:flex;flex-direction:column;gap:14px">
          <div style="display:flex;align-items:baseline;justify-content:space-between;background:#221f1b;border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:16px 20px">
            <span style="font-family:DM Sans;font-size:18px;color:#c9c3b8">Cost to run a task</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:rgb({ACC})">0.6c</span></div>
          <div style="display:flex;align-items:baseline;justify-content:space-between;background:#221f1b;border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:16px 20px">
            <span style="font-family:DM Sans;font-size:18px;color:#c9c3b8">You charge on outcome</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">the result</span></div>
          <div style="display:flex;align-items:baseline;justify-content:space-between;background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.32);border-radius:14px;padding:16px 20px">
            <span style="font-family:DM Sans;font-size:18px;color:#e6d6c2">No seats, no servers</span>
            <span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">pay per token</span></div>
        </div>
      </div>
      {cap("pay per token, price on the outcome. the spread is the whole business.")}</div>'''

PANELS={"surface":surface(),"taxfiler":taxfiler(),"riskpool":riskpool(),"collector":collector(),
        "sourcer":sourcer(),"negotiator":negotiator(),"frontdesk":frontdesk(),"economics":economics()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src46"; os.makedirs(outd,exist_ok=True)
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
