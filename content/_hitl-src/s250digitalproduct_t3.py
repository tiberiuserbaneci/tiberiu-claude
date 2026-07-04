#!/usr/bin/env python3
# TIER 3 - CREATE ONCE, SELL FOREVER. Fiecare panel o scena unica, construita din cod, pe un card
# rotunjit curat (CARD dark / CARDIV ivory), titlu + o singura legenda mono. Fara chip-strips, taieri
# sau pereti. Sursa: "50 Digital Product Ideas". Reframe Ultron: un sistem livreaza produsul pe cents.
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

# 1. MYTH - a field of 50 idea tiles, 49 struck-out and dim, ONE lit and shipped
def myth():
    cols,rowsn=10,5; cell,gap=62,13; lit=27
    tiles=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i==lit:
            tiles+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="13" fill="url(#litg)" filter="url(#lg)"/>'
              f'<path d="M{x+17} {y+32} l9 9 l19 -21" fill="none" stroke="#1a0f0a" stroke-width="4.4" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            tiles+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="13" fill="rgba(250,250,247,.045)" stroke="rgba(250,250,247,.08)"/>'
              f'<line x1="{x+15}" y1="{y+15}" x2="{x+cell-15}" y2="{y+cell-15}" stroke="rgba(200,70,35,.5)" stroke-width="2.4" stroke-linecap="round"/>')
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("50 ideas. One shipped.","THE LIST TRAP")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:14px auto 8px">
        <defs><radialGradient id="litg" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="lg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        {tiles}</svg>
      {cap("a list of 50 ideas is 50 ways not to ship. one system ships the first.")}</div>'''

# 2. SENTENCE - one plain-English prompt fans out into three finished product parts
def sentence():
    W,H=820,470
    outs=[("OFFER PAGE",160,'<circle cx="0" cy="0" r="15" fill="none" stroke="rgb({A})" stroke-width="2.6"/><path d="M-15 0 H15 M0 -15 C-9 -6 -9 6 0 15 C9 6 9 -6 0 -15" fill="none" stroke="rgb({A})" stroke-width="2.4"/>'),
          ("PDF GUIDE",410,'<path d="M-13 -17 h18 l9 9 v25 a3 3 0 0 1 -3 3 h-24 a3 3 0 0 1 -3 -3 v-31 a3 3 0 0 1 3 -3Z" fill="none" stroke="rgb({A})" stroke-width="2.4"/><path d="M5 -17 v9 h9" fill="none" stroke="rgb({A})" stroke-width="2.4"/>'),
          ("DELIVERY EMAIL",660,'<rect x="-17" y="-13" width="34" height="26" rx="4" fill="none" stroke="rgb({A})" stroke-width="2.4"/><path d="M-17 -10 L0 4 L17 -10" fill="none" stroke="rgb({A})" stroke-width="2.4"/>')]
    conns=""; cards=""
    for lbl,cx,ic in outs:
        conns+=f'<path d="M410 96 C410 220,{cx} 210,{cx} 316" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.6"/>'
        cards+=(f'<rect x="{cx-110}" y="316" width="220" height="126" rx="20" fill="url(#cg)" stroke="rgba(255,255,255,.10)"/>'
          f'<g transform="translate({cx},372)">{ic.replace("{A}",ACC)}</g>'
          f'<text x="{cx}" y="426" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".06em" fill="#e2dccf">{lbl}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One sentence in, a product out","PLAIN ENGLISH")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="cg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#35312c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient></defs>
        <rect x="110" y="28" width="600" height="68" rx="18" fill="#1c1a17" stroke="rgba(212,162,127,.4)" stroke-width="1.6"/>
        <text x="140" y="70" font-family="DM Mono" font-size="21" fill="#e8e2d6">Sell my founder audit as a 49 dollar PDF</text>
        <rect x="668" y="46" width="3" height="32" rx="1.5" fill="rgb({ACC})"/>
        {conns}{cards}</svg>
      {cap("you describe it once. Ultron returns the page, the file and the email.")}</div>'''

# 3. OFFER - IVORY browser mockup of the hosted, priced offer page (sells itself)
def offer():
    feats=["Instant download after checkout","Delivered by email, no login","Yours to update anytime"]
    fl="".join(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:11px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:17px;color:#5a4634">{f}</span></div>' for f in feats)
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Live, priced, on your domain</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">OFFER PAGE</span></div>
      <div style="background:#fffdf8;border:1px solid rgba(120,95,60,.2);border-radius:20px;overflow:hidden;box-shadow:0 22px 44px rgba(120,95,60,.18)">
        <div style="display:flex;align-items:center;gap:9px;padding:14px 20px;background:#f1e8da;border-bottom:1px solid rgba(120,95,60,.16)">
          <span style="width:12px;height:12px;border-radius:50%;background:#d8b7a3"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#e3cdb3"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#c9b48f"></span>
          <div style="flex:1;margin-left:14px;background:#fffdf8;border:1px solid rgba(120,95,60,.18);border-radius:9px;padding:7px 16px;font-family:'DM Mono';font-size:15px;color:#7a6a52">app.51ultron.com/p/founder-audit</div></div>
        <div style="display:flex;gap:30px;padding:30px 34px 34px">
          <div style="flex-shrink:0;width:170px;height:214px;border-radius:14px;background:linear-gradient(160deg,#96562d,#c07a4a);box-shadow:0 16px 30px rgba(150,90,45,.3);display:flex;flex-direction:column;justify-content:flex-end;padding:20px">
            <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.16em;color:rgba(255,255,255,.7)">PDF - 22 PAGES</div>
            <div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#fff;line-height:1.05;margin-top:4px">Founder Audit</div></div>
          <div style="flex:1">
            <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#2a2016;line-height:1.1">The Founder Sales Audit</div>
            <div style="display:flex;align-items:baseline;gap:12px;margin:12px 0 18px">
              <span style="font-family:'DM Sans';font-weight:900;font-size:46px;color:#96562d">$49</span>
              <span style="font-family:'DM Sans';font-size:19px;color:#a08a68;text-decoration:line-through">$149</span></div>
            {fl}
            <div style="margin-top:16px;display:inline-flex;align-items:center;gap:12px;background:linear-gradient(160deg,#c07a4a,#96562d);border-radius:12px;padding:15px 30px;box-shadow:0 12px 24px rgba(150,90,45,.34)">
              <span style="font-family:'DM Sans';font-weight:900;font-size:20px;color:#fff;letter-spacing:.02em">Buy now</span>
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
          </div></div></div>
      {cap("hosted, checkout wired, on your own link. no site to build.","#8a745a")}</div>'''

# 4. PIPELINE - isometric PULSE -> AMPLIFY -> HUMAN GATE -> LIVE, held at the gate for your tap
def pipeline():
    steps=[("PULSE","wrote the launch post",False),("AMPLIFY","scheduled 6 slots",False),("HUMAN GATE","held for your tap",True),("LIVE","offer is public",False)]
    cards=""
    for i,(nm,sub,gate) in enumerate(steps):
        y=i*104
        bd="rgb("+ACC+")" if gate else "rgba(255,255,255,.14)"
        icon=('<rect x="4" y="9" width="18" height="14" rx="4" fill="none" stroke="rgb('+ACC+')" stroke-width="2.4"/><path d="M8 9 V6 a5 5 0 0 1 10 0 v3" fill="none" stroke="rgb('+ACC+')" stroke-width="2.4"/>' if gate else
              '<path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb('+ACC+')" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid {bd};border-radius:18px;padding:18px 24px;box-shadow:0 28px 42px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:48px;height:48px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="26" height="30" viewBox="0 0 26 30">{icon}</svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div>'
          + (f'<div style="flex-shrink:0;font-family:DM Sans;font-weight:900;font-size:14px;color:#1a0f0a;background:rgb({ACC});padding:7px 15px;border-radius:999px">your tap</div>' if gate else '')
          + '</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Written, scheduled, then gated","THE ASSEMBLY LINE")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:428px;position:relative">{cards}</div></div>
      {cap("PULSE writes, AMPLIFY schedules, nothing sends until you tap the gate.")}</div>'''

# 5. DELIVERY - a night clock beside a fulfilment timeline that runs while you sleep
def delivery():
    events=[("Payment cleared","02:14",True),("Delivery email sent","02:14",True),("Customer opened PDF","07:02",True)]
    rows=""
    for i,(nm,ts,ok) in enumerate(events):
        last=(i==len(events)-1)
        rows+=(f'<div style="display:flex;align-items:flex-start;gap:16px;{"" if last else "margin-bottom:6px"}">'
          f'<div style="display:flex;flex-direction:column;align-items:center">'
          f'<svg width="30" height="30" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.16)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          + ('' if last else '<div style="width:2px;height:34px;background:rgba(212,162,127,.35)"></div>')
          + '</div>'
          f'<div style="padding-top:2px"><div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:DM Mono;font-size:14px;color:rgb({ACC});margin-top:2px">{ts}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <svg width="300" height="300" viewBox="0 0 300 300" style="flex-shrink:0">
        <defs><radialGradient id="dial" cx="40%" cy="34%"><stop offset="0%" stop-color="#2c2824"/><stop offset="100%" stop-color="#131210"/></radialGradient>
        <filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="10" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        <circle cx="150" cy="150" r="128" fill="url(#dial)" stroke="rgba(212,162,127,.28)" stroke-width="2"/>
        {"".join(f'<line x1="{150+112*math.cos(math.radians(a)):.0f}" y1="{150+112*math.sin(math.radians(a)):.0f}" x2="{150+122*math.cos(math.radians(a)):.0f}" y2="{150+122*math.sin(math.radians(a)):.0f}" stroke="rgba(250,250,247,.22)" stroke-width="2.4"/>' for a in range(0,360,30))}
        <g filter="url(#mg)"><path d="M206 96 a44 44 0 1 0 20 46 a34 34 0 0 1 -20 -46Z" fill="rgb({ACC})"/></g>
        {"".join(f'<circle cx="{cx}" cy="{cy}" r="2.4" fill="#f0e6d4"/>' for cx,cy in [(96,104),(120,88),(104,132)])}
        <line x1="150" y1="150" x2="150" y2="92" stroke="#FAFAF7" stroke-width="4.5" stroke-linecap="round"/>
        <line x1="150" y1="150" x2="192" y2="168" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>
        <circle cx="150" cy="150" r="6" fill="#FAFAF7"/>
        <text x="150" y="228" text-anchor="middle" font-family="DM Mono" font-size="20" letter-spacing=".14em" fill="#e2dccf">02:14</text>
      </svg>
      <div style="flex:1">
        {htitle("Bought at 2am. Already sent.","OVERNIGHT")}
        {rows}
        {cap("payment, email, file - the handoff ran itself while you slept.")}
      </div></div>'''

# 6. GROWTH - one product on repeat: a rising sales curve to a recurring readout
def growth():
    pts=[(60,372),(140,360),(220,344),(300,320),(380,300),(460,258),(540,214),(620,158),(700,112),(752,92)]
    line="M"+" L".join(f"{x} {y}" for x,y in pts)
    area=f"M60 380 L"+" L".join(f"{x} {y}" for x,y in pts)+" L752 380 Z"
    dots="".join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="rgb({ACC})" filter="url(#dg)"/>' for x,y in pts[3::3])
    months=["W1","W2","W3","W4","W5","W6"]
    mt="".join(f'<text x="{80+i*128}" y="404" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#7a746a">{m}</text>' for i,m in enumerate(months))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Create once, sell on repeat","THE COMPOUND")}
      <div style="display:flex;align-items:baseline;gap:14px;margin:4px 0 6px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:56px;color:rgb({ACC})">$1,240</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:22px;color:#c9a583">/ mo, recurring</span>
        <span style="margin-left:auto;font-family:'DM Mono';font-size:13px;color:#8f8f85">one PDF, zero extra work</span></div>
      <svg width="800" height="410" viewBox="0 0 800 410" style="display:block;margin:0 auto">
        <defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.42)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient>
        <filter id="dg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {"".join(f'<line x1="60" y1="{y}" x2="752" y2="{y}" stroke="rgba(250,250,247,.05)"/>' for y in (110,190,270,350))}
        <path d="{area}" fill="url(#ar)"/>
        <path d="{line}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        {dots}
        <line x1="60" y1="380" x2="752" y2="380" stroke="rgba(250,250,247,.14)"/>
        {mt}</svg>
      {cap("the work is done once. the sales keep arriving after you stop.")}</div>'''

# 7. CENTS - IVORY: $49 charged vs a pennies run cost, the margin gauge nearly full
def cents():
    pct=99.9; r=76; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">Charge dollars, run on cents</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">THE MARGIN</span></div>
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex:1;display:flex;flex-direction:column;gap:16px">
          <div style="background:rgba(255,255,255,.62);border-left:4px solid #96562d;border-radius:14px;padding:18px 22px">
            <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#8a745a">YOU CHARGE</div>
            <div style="font-family:'DM Sans';font-weight:900;font-size:44px;color:#2a2016;line-height:1">$49<span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#8a745a;margin-left:10px">per sale</span></div></div>
          <div style="display:flex;align-items:center;gap:14px;padding-left:22px">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg>
            <span style="font-family:'DM Sans';font-size:18px;color:#5a4634">it costs you</span></div>
          <div style="background:rgba(255,255,255,.62);border-left:4px solid #96562d;border-radius:14px;padding:18px 22px">
            <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#8a745a">ULTRON RUN COST</div>
            <div style="font-family:'DM Sans';font-weight:900;font-size:44px;color:#96562d;line-height:1">$0.03<span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#8a745a;margin-left:10px">in tokens</span></div></div>
        </div>
        <div style="flex-shrink:0;position:relative;width:210px;height:210px">
          <svg width="210" height="210" viewBox="0 0 210 210">
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="17"/>
            <circle cx="105" cy="105" r="{r}" fill="none" stroke="#96562d" stroke-width="17" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 105 105)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016">99.9%</span>
            <span style="font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:#96562d">margin kept</span></div></div>
      </div>
      {cap("no printer, no shipping, no staff. the margin is almost the whole price.","#8a745a")}</div>'''

# 8. SYSTEM - one hub orb, six product types orbiting: one engine, many products
def system():
    cx,cy=410,225
    prods=[("PDF GUIDE",-90),("MINI-COURSE",-30),("TEMPLATE KIT",30),("AUDIT",90),("TOOLKIT",150),("CHECKLIST",210)]
    Rr=178; lines=""; nodes=""
    for nm,a in prods:
        x=cx+Rr*math.cos(math.radians(a)); y=cy+Rr*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.34)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#221f1b" stroke="rgba(255,255,255,.12)" stroke-width="1.5"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One engine, every product","THE SYSTEM")}
      <svg width="820" height="460" viewBox="0 0 820 460" style="display:block;margin:0 auto">
        <defs><radialGradient id="hubo" cx="40%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="22" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {lines}
        {nodes}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="82" fill="url(#hubo)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a160c">ONE</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="#2a160c">SYSTEM</text>
      </svg>
      {cap("stop hoarding 50 ideas. keep the engine that ships any of them.")}</div>'''

PANELS={"myth":myth(),"sentence":sentence(),"offer":offer(),"pipeline":pipeline(),
        "delivery":delivery(),"growth":growth(),"cents":cents(),"system":system()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s250digitalproduct"; os.makedirs(outd,exist_ok=True)
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
