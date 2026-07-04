#!/usr/bin/env python3
# TIER 3 - THE 500K CONTENT DESK, built to the WIRE-ITS-EYES bar: each of the 8 panels is a UNIQUE
# hand-built coded scene filling a clean rounded card (calendar / podium / ivory rank / bezier fan /
# arc gauge / radial hub / parked queue / ivory cost bars). htitle + one mono cap. No stat-chip strips.
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
def htitivory(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CAL - a coded week calendar: 7 day columns, 14 post slots plotted at 10:00, channel-coloured
def cal():
    CH={"LI":("rgb(212,162,127)","#1a0f0a"),"TT":("#e7ddce","#26201a"),"IG":("#c78a5f","#1a0f0a")}
    week=[("MON",["LI","TT"]),("TUE",["IG","LI"]),("WED",["TT","IG"]),("THU",["LI","TT"]),
          ("FRI",["IG","LI"]),("SAT",["TT","IG"]),("SUN",["LI","IG"])]
    cols=""
    for day,slots in week:
        chips=""
        for ch in slots:
            bg,ink=CH[ch]
            chips+=(f'<div style="background:{bg};border-radius:9px;padding:8px 6px 7px;margin-bottom:9px;'
              f'box-shadow:0 6px 13px rgba(0,0,0,.4), inset 0 1.5px 2px rgba(255,255,255,.25)">'
              f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.06em;color:{ink};opacity:.72">10:00</div>'
              f'<div style="font-family:DM Sans;font-weight:900;font-size:16px;color:{ink};line-height:1">{ch}</div></div>')
        cols+=(f'<div style="flex:1;display:flex;flex-direction:column;align-items:stretch">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:#9a9488;text-align:center;'
          f'padding-bottom:12px;margin-bottom:14px;border-bottom:1px solid rgba(255,255,255,.09)">{day}</div>'
          f'{chips}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The week plans itself","AUTO-PLANNED")}
      <div style="background:#1a1816;border:1px solid rgba(255,255,255,.06);border-radius:20px;padding:22px 18px 14px;box-shadow:inset 0 2px 6px rgba(0,0,0,.4)">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px;padding:0 4px">
          <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">WEEK 24</span>
          <span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">14 slots &middot; 3 channels</span></div>
        <div style="display:flex;gap:10px;align-items:flex-start">{cols}</div></div>
      {cap("one line in, 14 slots out, spread across channels at 10:00 local.")}</div>'''

# 2. HOOKS - three competing hook cards, one crowned as the winner (podium comparison)
def hooks():
    picks=[("The angle","\"I killed 9 tools last month.\"",71,False),
           ("The proof","\"200 posts. One chat wrote them.\"",68,False),
           ("The winner","\"The desk bills in cents, not Mondays.\"",94,True)]
    cards=""
    for label,text,score,win in picks:
        bd=f"rgb({ACC})" if win else "rgba(255,255,255,.08)"
        bg="linear-gradient(162deg,#403a33,#241f1a)" if win else "linear-gradient(162deg,#2c2926,#201d1a)"
        glow="box-shadow:0 22px 40px rgba(0,0,0,.5),0 0 34px rgba(212,162,127,.28), inset 0 2px 2px rgba(255,255,255,.1);" if win else "box-shadow:0 16px 30px rgba(0,0,0,.45), inset 0 1.5px 2px rgba(255,255,255,.06);"
        lift="margin-top:-22px;" if win else ""
        crown=(f'<div style="position:absolute;top:-16px;left:50%;transform:translateX(-50%);background:rgb({ACC});color:#1a0f0a;'
               f'font-family:DM Sans;font-weight:900;font-size:12px;letter-spacing:.08em;padding:5px 14px;border-radius:999px;'
               f'box-shadow:0 8px 18px rgba(212,162,127,.5)">CROWNED</div>') if win else ""
        sc=f"rgb({ACC})" if win else "#8f8f85"
        lc=f"rgb({ACC})" if win else "#7a746a"
        cards+=(f'<div style="flex:1;position:relative;{lift}background:{bg};border:1.5px solid {bd};border-radius:20px;padding:26px 20px 22px;{glow}">'
          f'{crown}'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{lc};text-transform:uppercase">{label}</div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:22px;color:#FAFAF7;line-height:1.28;margin:14px 0 20px;min-height:112px">{text}</div>'
          f'<div style="display:flex;align-items:baseline;gap:8px;border-top:1px solid rgba(255,255,255,.08);padding-top:14px">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:40px;color:{sc};line-height:1">{score}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;color:#8f8f85">/100 hook score</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {htitle("Three hooks fight","HOOK BANK")}
      <div style="display:flex;gap:16px;align-items:flex-start;padding-top:20px">{cards}</div>
      {cap("three angles per post from your proven hook bank. you pick the winner.")}</div>'''

# 3. VOICE - IVORY: a sample written in your voice + 3 ranked draft variants with score bars
def voice():
    drafts=[("draft A","short lines, no hedging",94,"#96562d"),
            ("draft B","one clause too long",78,"#b98a5a"),
            ("draft C","a banned word slipped in",61,"rgb(200,70,35)")]
    bars=""
    for nm,note,sc,col in drafts:
        w=int(sc*2.9)
        bars+=(f'<div style="margin-bottom:14px">'
          f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px">'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:16px;color:#2a2016">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:14px;color:#8a745a">{note}</span></div>'
          f'<div style="display:flex;align-items:center;gap:12px">'
          f'<div style="flex:1;height:14px;border-radius:8px;background:rgba(150,90,45,.14);overflow:hidden">'
          f'<div style="width:{w}px;height:100%;border-radius:8px;background:{col}"></div></div>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:19px;color:#2a2016;width:34px;text-align:right">{sc}</span></div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitivory("It writes like me","VOICE MATCH")}
      <div style="background:rgba(255,255,255,.6);border-left:4px solid #96562d;border-radius:12px;padding:20px 22px;font-family:'DM Sans';font-size:21px;color:#2a2016;line-height:1.42;margin-bottom:22px">
        "No standups. No Slack threads. The desk shipped nine posts while I was asleep, and every one sounded like me."</div>
      {bars}
      {cap("sampled from your real posts, banned words enforced, ranked before you read.","#8a745a")}</div>'''

# 4. REPURPOSE - one brief node fans out via bezier into 5 native channel outputs
def repurpose():
    W,H=820,440
    outs=[("LinkedIn long-form",70),("Caption",158),("Carousel",246),("Newsletter",334),("Script",422)]
    hubx,huby=150,246
    edges=""; nodes=""
    for nm,y in outs:
        mx=(hubx+560)/2
        edges+=f'<path d="M{hubx+68} {huby} C{mx:.0f} {huby},{mx:.0f} {y},560 {y}" stroke="rgba(212,162,127,.5)" stroke-width="2.5" fill="none"/>'
        nodes+=(f'<rect x="560" y="{y-27}" width="238" height="54" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.10)"/>'
          f'<circle cx="592" cy="{y}" r="6" fill="rgb({ACC})"/>'
          f'<text x="612" y="{y+6}" font-family="DM Sans" font-weight="700" font-size="18" fill="#e2dccf">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One brief, five natives","REPURPOSE")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="rh" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {edges}
        <g filter="url(#rg)"><circle cx="{hubx}" cy="{huby}" r="72" fill="url(#rh)"/></g>
        <text x="{hubx}" y="{huby-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">BRIEF</text>
        <text x="{hubx}" y="{huby+20}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2416">1 idea</text>
        {nodes}
      </svg>
      {cap("linkedin long-form, caption, carousel, newsletter, script. same brief.")}</div>'''

# 5. INBOX - arc gauge at 99.2% inboxed + a warm-up send ramp sparkline
def inbox():
    cx,cy,R=250,290,190; pct=99.2
    a0,a1=180,360  # semicircle sweep
    val=a0+(a1-a0)*pct/100
    def pt(ang,r): return (cx+r*math.cos(math.radians(ang)), cy+r*math.sin(math.radians(ang)))
    x0,y0=pt(a0,R); x1,y1=pt(a1,R); xv,yv=pt(val,R)
    ramp=[45,80,120,170,225,285,345]; rw=28; rgap=16; base=350; bx0=470
    rbars=""
    for i,v in enumerate(ramp):
        x=bx0+i*(rw+rgap); h=v//2
        rbars+=(f'<rect x="{x}" y="{base-h}" width="{rw}" height="{h}" rx="5" fill="rgb({ACC})" opacity="{0.34+0.09*i:.2f}"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("99.2% inboxed","DELIVERABILITY")}
      <svg width="820" height="410" viewBox="0 0 820 410" style="display:block;margin:0 auto">
        <defs><linearGradient id="ig" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8a4a2c"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="rgba(212,162,127,.14)" stroke-width="26" stroke-linecap="round"/>
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {xv:.0f} {yv:.0f}" fill="none" stroke="url(#ig)" stroke-width="26" stroke-linecap="round"/>
        <text x="{cx}" y="{cy-26}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="70" fill="#FAFAF7">99.2%</text>
        <text x="{cx}" y="{cy+12}" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".14em" fill="rgb({ACC})">PLACEMENT</text>
        <text x="{x0:.0f}" y="{y0+38:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#7a746a">0</text>
        <text x="{x1:.0f}" y="{y1+38:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#7a746a">100</text>
        {rbars}
        <line x1="470" y1="{base}" x2="778" y2="{base}" stroke="rgba(255,255,255,.12)"/>
        <text x="624" y="392" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#9a9488">warm-up ramp &middot; 7 days</text>
      </svg>
      {cap("warm domains, ramped sends, 99.2% placement. content nobody reads is free.")}</div>'''

# 6. DESK - radial orbital hub: one chat + memory core, 4 role nodes orbiting on a ring
def desk():
    cx,cy,Rr=270,235,175
    roles=[("PLANNER",-90),("WRITER",0),("DESIGNER",90),("DISTRIBUTOR",180)]
    ring=""
    for nm,a in roles:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        ly=y+58
        ring+=(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="#241f1a" stroke="rgba(255,255,255,.13)" stroke-width="1.5"/>'
          f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="rgb({ACC})"/>'
          f'<text x="{x:.0f}" y="{ly:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".08em" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:24px">
      <svg width="540" height="470" viewBox="0 0 540 470">
        <defs><radialGradient id="dh" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="dg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{Rr}" fill="none" stroke="rgba(212,162,127,.12)" stroke-dasharray="3 8"/>
        {ring}
        <g filter="url(#dg)"><circle cx="{cx}" cy="{cy}" r="66" fill="url(#dh)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#1a0f0a">ONE CHAT</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">one memory</text>
      </svg>
      <div style="flex:1">
        {htitle("The desk never meets","NO STANDUPS")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">Planner, writer, designer, distributor - four roles, no calls, no threads. One brand memory feeds them all.</div>
        {cap("the whole pipeline runs behind one chat with one memory of your brand.")}</div></div>'''

# 7. GATE - a parked queue of drafts held behind a hold-bar, one batch-approve tap
def gate():
    q=[("Mon 10:00","LinkedIn long-form"),
       ("Mon 18:00","TikTok script"),
       ("Tue 10:00","IG carousel"),
       ("Tue 12:00","Newsletter")]
    rows=""
    for when,what in q:
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;background:linear-gradient(158deg,#332f2a,#211e1a);'
          f'border:1px solid rgba(255,255,255,.10);border-radius:14px;padding:14px 18px;margin-bottom:12px;'
          f'box-shadow:0 12px 22px rgba(0,0,0,.45), inset 0 1.5px 2px rgba(255,255,255,.07)">'
          f'<div style="flex-shrink:0;width:14px;height:14px;border-radius:50%;background:rgba(212,162,127,.2);border:2px solid rgb({ACC})"></div>'
          f'<div style="flex:1;text-align:left"><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{what}</div>'
          f'<div style="font-family:DM Mono;font-size:13px;color:#8f8f85;margin-top:1px">{when} &middot; drafted</div></div>'
          f'<span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC});flex-shrink:0">PARKED</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Nothing posts alone","HUMAN GATE")}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1">{rows}</div>
        <div style="flex-shrink:0;width:236px;display:flex;flex-direction:column;align-items:center;justify-content:center;
          background:linear-gradient(160deg,#403a33,#221f1a);border:1.5px solid rgb({ACC});border-radius:20px;padding:26px 20px;
          box-shadow:0 24px 44px rgba(0,0,0,.5),0 0 34px rgba(212,162,127,.24)">
          <svg width="58" height="58" viewBox="0 0 24 24" style="margin-bottom:14px"><rect x="3" y="10.5" width="18" height="12" rx="3" fill="none" stroke="rgb({ACC})" stroke-width="2"/><path d="M7 10.5 V7 a5 5 0 0 1 10 0 v3.5" fill="none" stroke="rgb({ACC})" stroke-width="2"/></svg>
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7;text-align:center;line-height:1.1">Approve<br>the batch</div>
          <div style="font-family:DM Mono;font-size:13px;color:rgb({ACC});margin-top:8px">4 drafts &middot; one read</div>
          <div style="margin-top:18px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:11px 26px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">your tap</div>
        </div>
      </div>
      {cap("every draft parks first. you approve the batch in one read.")}</div>'''

# 8. MATH - IVORY cost bars: the stack you replace costs real dollars, the desk bills in cents
def math_panel():
    stack=[("Planner tool","$49/mo"),("Writer / SEO","$99/mo"),
           ("Designer seat","$79/mo"),("Distribution app","$65/mo")]
    maxv=99; bx=410
    rows=""
    for nm,cost in stack:
        v=int(cost.strip("$").split("/")[0]); w=int(v/maxv*bx)
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:13px">'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:17px;color:#2a2016;width:190px;text-align:left">{nm}</span>'
          f'<div style="flex:1;height:22px;border-radius:7px;background:rgba(150,90,45,.12);overflow:hidden">'
          f'<div style="width:{w}px;height:100%;border-radius:7px;background:linear-gradient(90deg,#c98a5f,rgb(200,70,35))"></div></div>'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:17px;color:rgb(200,70,35);width:78px;text-align:right">{cost}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitivory("The desk bills in cents","METERED")}
      <div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:#a08a68;margin-bottom:14px">THE STACK YOU REPLACE</div>
      {rows}
      <div style="display:flex;align-items:stretch;gap:16px;margin-top:22px;background:linear-gradient(160deg,#2a2016,#1c150e);border-radius:18px;padding:22px 26px;box-shadow:0 20px 38px rgba(120,80,40,.3)">
        <div style="flex:1;text-align:left">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({ACC})">THE 500K DESK</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7;line-height:1.1;margin-top:4px">One subscription</div></div>
        <div style="flex-shrink:0;text-align:right;align-self:center">
          <div style="font-family:DM Sans;font-weight:900;font-size:44px;color:rgb({ACC});line-height:1">cents</div>
          <div style="font-family:DM Mono;font-size:13px;color:#c9a583">per post, metered</div></div>
      </div>
      {cap("planner, writer, designer, distributor: one subscription, metered by use.","#8a745a")}</div>'''

PANELS={"cal":cal(),"hooks":hooks(),"voice":voice(),"repurpose":repurpose(),
        "inbox":inbox(),"desk":desk(),"gate":gate(),"math":math_panel()}

if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/contentdesk"; os.makedirs(outd,exist_ok=True)
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
