#!/usr/bin/env python3
# TIER 3 - THE CANCELLATION RECEIPT, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Angle: 4 named subscriptions (ClickUp / Mailchimp / Zapier / Pipedrive) each swapped for the exact
# Ultron agent that replaces it - a tight 4-item swap, NOT a 6-tool ledger.
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

# 1. RECEIPT (IVORY) - a paper receipt: 4 struck line items + total + a wax CANCELED seal
def receipt():
    items=[("ClickUp","$99"),("Mailchimp","$49"),("Zapier","$19"),("Pipedrive","$24")]
    rows=""
    for nm,amt in items:
        rows+=(f'<div style="display:flex;align-items:baseline;justify-content:space-between;padding:11px 0;border-bottom:1px dashed rgba(150,120,80,.35)">'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:22px;color:#5a4634;text-decoration:line-through;text-decoration-color:#96562d">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:20px;color:#96562d;text-decoration:line-through">{amt}/mo</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The monthly bleed","4 SUBSCRIPTIONS","#2a2016")}
      <div style="display:flex;gap:34px;align-items:center">
        <div style="flex:1;background:rgba(255,255,255,.55);border:1px solid rgba(150,120,80,.22);border-radius:18px;padding:8px 24px 18px">
          {rows}
          <div style="display:flex;align-items:baseline;justify-content:space-between;padding-top:16px;margin-top:6px">
            <span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#2a2016">TOTAL</span>
            <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:#96562d">$191<span style="font-size:18px">/mo</span></span></div>
        </div>
        <svg width="196" height="196" viewBox="0 0 196 196" style="flex-shrink:0">
          <defs><radialGradient id="wax" cx="38%" cy="32%"><stop offset="0%" stop-color="#e07a4e"/><stop offset="60%" stop-color="rgb({RED})"/><stop offset="100%" stop-color="#7a2810"/></radialGradient></defs>
          <circle cx="98" cy="98" r="80" fill="url(#wax)" stroke="#5a1c0a" stroke-width="3"/>
          <circle cx="98" cy="98" r="66" fill="none" stroke="rgba(255,220,200,.5)" stroke-width="2" stroke-dasharray="4 6"/>
          <text x="98" y="90" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#fbe8df">CAN</text>
          <text x="98" y="120" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#fbe8df">CELLED</text>
        </svg>
      </div>
      {cap("four logins, four bills, one job each. that is $2,292 a year.","#8a745a")}</div>'''

# 2. WORKSPACE (DARK) - ClickUp -> owned workspace: isometric stack of 3 feature cards
def workspace():
    rows=[("Task board","every project in one view"),("Automations","triggers you set, not presets"),("Live dashboards","on your own data, refreshed daily")]
    cards=""
    for i,(nm,sub) in enumerate(rows):
        y=i*126
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="26" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{nm}</div><div style="font-family:DM Sans;font-size:14px;color:#8f8f85">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("ClickUp, cancelled","$99/MO INTO ONE")}
      <div style="perspective:1900px;height:452px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(19deg) rotateZ(-8deg);width:560px;height:400px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:388px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 22px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">one workspace, no per-seat fee</div></div></div>
      {cap("tasks, triggers and dashboards on data you own, not rented back to you.")}</div>'''

# 3. SPECTER (DARK) - Mailchimp -> outbound drip sequence as a bezier node/flow graph
def specter():
    steps=[("SEND","cold email, your domain",90),("WAIT 2d","no reply yet",230),("FOLLOW-UP","new angle, auto-written",370),("REPLY","meeting booked",510)]
    nodes=""; edges=""
    ys=[120,236,120,236]
    prev=None
    for i,(nm,sub,x) in enumerate(steps):
        y=ys[i]; on=(i==3)
        if prev is not None:
            px,py=prev
            mx=(px+x)/2
            col=f"rgb({ACC})" if on else "rgba(212,162,127,.45)"
            edges+=f'<path d="M{px+58} {py} C{mx} {py},{mx} {y},{x-58} {y}" fill="none" stroke="{col}" stroke-width="{4 if on else 2.6}"/>'
        prev=(x,y)
        fill="url(#send)" if on else "#26221d"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.12)"
        tcol="#1a0f0a" if on else "#FAFAF7"
        nodes+=(f'<g><rect x="{x-58}" y="{y-40}" width="116" height="80" rx="18" fill="{fill}" stroke="{bd}" stroke-width="{2.4 if on else 1.6}"/>'
          f'<text x="{x}" y="{y-6}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="{tcol}">{nm}</text>'
          f'<text x="{x}" y="{y+18}" text-anchor="middle" font-family="DM Sans" font-size="11.5" fill="{"#3a2010" if on else "#8f8f85"}">{sub}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Mailchimp, cancelled","SPECTER SENDS IT")}
      <svg width="812" height="380" viewBox="0 0 812 380" style="display:block;margin:14px auto 0">
        <defs><linearGradient id="send" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        {edges}{nodes}
        <text x="406" y="352" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#6f6a60" letter-spacing=".06em">unlimited contacts &#183; no send caps &#183; no monthly bill</text>
      </svg>
      {cap("SPECTER writes the sequence and follows up until it books, from your own inbox.")}</div>'''

# 4. AMPLIFY (DARK) - Zapier -> one hub dispatching to every channel on a schedule (hub-and-spokes)
def amplify():
    cx,cy,R=200,215,152
    spokes=[("LinkedIn","10:00",-58),("Email","10:20",6),("TikTok","18:00",70),("Instagram","18:30",134)]
    sv=""
    for nm,tm,a in spokes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        sv+=(f'<line x1="{cx+58}" y1="{cy}" x2="{x-46:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.4" stroke-dasharray="2 9" stroke-linecap="round"/>'
          f'<rect x="{x-46:.0f}" y="{y-30:.0f}" width="150" height="60" rx="15" fill="#26221d" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{x+29:.0f}" y="{y-4:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x+29:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">{tm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:8px">
      <svg width="470" height="440" viewBox="0 0 470 440">
        <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {sv}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">AMPLIFY</text>
        <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">schedules it</text>
      </svg>
      <div style="flex:1">
        {htitle("Zapier, cancelled","AMPLIFY MOVES IT")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">No zaps to wire and no task limits. One agent formats each asset and fires it at the right hour, per channel.</div>
        {cap("every post, right format, right time zone, no automation bill.")}</div></div>'''

# 5. STRIKER (IVORY) - Pipedrive -> deal pipeline funnel stages, one deal advancing to WON
def striker():
    stages=[("NEW",18,0.0),("QUALIFIED",11,0.24),("PROPOSAL",6,0.48),("WON",3,0.74)]
    W=560; bars=""
    for i,(nm,n,inset) in enumerate(stages):
        y=i*92
        w=W*(1-inset)
        won=(i==3)
        fill="#96562d" if won else f"rgba(150,90,45,{0.9-i*0.16:.2f})"
        bars+=(f'<div style="position:relative;height:74px;margin:0 auto 18px;width:{w:.0f}px;background:{fill};border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:0 26px;box-shadow:0 10px 20px rgba(120,80,40,.18)">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#fdf6ec;letter-spacing:.04em">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:17px;color:#fbe4d3">{n} deals</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 32px">
      {htitle("Pipedrive, cancelled","STRIKER CLOSES IT","#2a2016")}
      <div style="padding-top:6px">{bars}</div>
      {cap("STRIKER qualifies, handles objections and drafts the close plan, pipeline in memory.","#8a745a")}</div>'''

# 6. ROUTER (DARK) - 4 cancelled tool nodes converge into one Ultron ROUTER core
def router():
    tools=[("ClickUp",70,84),("Mailchimp",70,196),("Zapier",70,308),("Pipedrive",70,392)]
    scat=[("ClickUp",84),("Mailchimp",172),("Zapier",258),("Pipedrive",346)]
    left=""
    for nm,y in scat:
        left+=(f'<path d="M{162} {y} C320 {y},360 215,500 215" fill="none" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
          f'<g><rect x="30" y="{y-26}" width="132" height="52" rx="14" fill="#221f1b" stroke="rgba(200,70,35,.5)" stroke-width="1.5"/>'
          f'<line x1="46" y1="{y-14}" x2="146" y2="{y+14}" stroke="rgba(200,70,35,.55)" stroke-width="2"/>'
          f'<text x="96" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">{nm}</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Four apps, one login","THE ROUTER")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="rc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        {left}
        <g filter="url(#rg)"><circle cx="600" cy="215" r="118" fill="url(#rc)"/></g>
        <text x="600" y="204" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">ROUTER</text>
        <text x="600" y="236" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#3a2010" letter-spacing=".08em">picks the agent</text>
        <text x="600" y="372" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85" letter-spacing=".06em">plain English in &#183; the right agent out</text>
      </svg>
      {cap("type what you want done. the ROUTER hires the agent and the cheapest model that fits.")}</div>'''

# 7. TALLY (DARK) - money towers: $191/mo competitor bar vs Ultron cents; annual struck
def tally():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:28px">
      <svg width="470" height="440" viewBox="0 0 470 440">
        <defs><linearGradient id="tw" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e07a4e"/><stop offset="100%" stop-color="rgb({RED})"/></linearGradient>
        <linearGradient id="ug" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0c49e"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        <line x1="60" y1="392" x2="430" y2="392" stroke="rgba(255,255,255,.12)" stroke-width="2"/>
        <rect x="96" y="70" width="120" height="322" rx="12" fill="url(#tw)"/>
        <text x="156" y="52" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#FAFAF7">$191</text>
        <text x="156" y="416" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">4 SaaS bills / mo</text>
        <rect x="300" y="368" width="120" height="24" rx="10" fill="url(#ug)"/>
        <circle cx="360" cy="380" r="7" fill="#f0c49e"/>
        <text x="360" y="348" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="rgb({ACC})">cents</text>
        <text x="360" y="416" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">Ultron / run</text>
      </svg>
      <div style="flex:1">
        {htitle("The yearly swap","$2,292 GONE")}
        <div style="font-family:DM Sans;font-size:20px;color:#c9c3b8;line-height:1.5">Four monthly bills, <span style="color:rgb({RED});text-decoration:line-through">$2,292 a year</span>. Ultron bills pennies per run, only when the work lands.</div>
        {cap("pay per token, not per seat. no bill on the months you do not run it.")}</div></div>'''

# 8. GATE (DARK) - you own the data + HUMAN GATE approval checkpoint
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Now you own it","HUMAN GATE")}
      <svg width="820" height="410" viewBox="0 0 820 410" style="display:block;margin:0 auto">
        <defs><radialGradient id="vg" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g transform="translate(120,120)">
          <ellipse cx="90" cy="26" rx="90" ry="26" fill="#332d27" stroke="rgba(255,255,255,.12)"/>
          <path d="M0 26 V150 a90 26 0 0 0 180 0 V26" fill="#241f1a" stroke="rgba(255,255,255,.1)"/>
          <ellipse cx="90" cy="86" rx="90" ry="26" fill="none" stroke="rgba(255,255,255,.08)"/>
          <ellipse cx="90" cy="146" rx="90" ry="26" fill="none" stroke="rgba(255,255,255,.08)"/>
          <text x="90" y="200" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#8f8f85">your data, your DB</text>
        </g>
        <path d="M330 200 H470" stroke="rgb({ACC})" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
        <g filter="url(#gg)"><circle cx="600" cy="196" r="104" fill="url(#vg)"/></g>
        <g transform="translate(566,158)"><rect x="0" y="34" width="68" height="50" rx="10" fill="none" stroke="#2a160c" stroke-width="6"/><path d="M12 34 V20 a22 22 0 0 1 44 0 v14" fill="none" stroke="#2a160c" stroke-width="6"/></g>
        <text x="600" y="336" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">nothing sends without your tap</text>
      </svg>
      {cap("one operator, one login. every external move parks for your approval.")}</div>'''

PANELS={"receipt":receipt(),"workspace":workspace(),"specter":specter(),"amplify":amplify(),
        "striker":striker(),"router":router(),"tally":tally(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src65"; os.makedirs(outd,exist_ok=True)
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
