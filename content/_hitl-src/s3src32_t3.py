#!/usr/bin/env python3
# TIER 3 - THE SPAM DIAGNOSTIC, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# Angle: the 5 named mistakes that sort cold email to spam, and the exact fix for each (a diagnostic).
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

def env(x,y,w,col,op=1.0):
    h=w*0.68
    return (f'<g opacity="{op}"><rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="4" fill="none" stroke="{col}" stroke-width="2.4"/>'
      f'<path d="M{x:.0f} {y+3:.0f} L{x+w/2:.0f} {y+h*0.62:.0f} L{x+w:.0f} {y+3:.0f}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linejoin="round"/></g>')

# 1. VERDICT - a routing/sorting gate: 5 sends hit the spam filter, 4 fall to a lit red spam bin
def verdict():
    spam="".join(env(596+(i%2)*74, 356+(i//2)*38, 42, f"rgb({RED})") for i in range(4))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Sorted before it is read","THE VERDICT")}
      <svg width="820" height="454" viewBox="0 0 820 454" style="display:block;margin:0 auto">
        <defs>
          <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="13" flood-color="rgb({RED})" flood-opacity="0.5"/></filter>
          <linearGradient id="fil" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#403a33"/><stop offset="1" stop-color="#241f1a"/></linearGradient>
        </defs>
        <rect x="24" y="188" width="130" height="78" rx="16" fill="#221f1b" stroke="rgba(255,255,255,.12)"/>
        <text x="89" y="222" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="28" fill="#FAFAF7">5</text>
        <text x="89" y="246" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="rgb({ACC})">COLD SENDS</text>
        <path d="M154 224 C300 224,320 120,470 120" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2.5"/>
        <path d="M154 232 C320 232,360 356,562 356" fill="none" stroke="rgb({RED})" stroke-width="6"/>
        <rect x="300" y="172" width="120" height="112" rx="20" fill="url(#fil)" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>
        <text x="360" y="222" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">SPAM</text>
        <text x="360" y="246" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">FILTER</text>
        <rect x="470" y="86" width="156" height="70" rx="16" fill="#1f1c18" stroke="rgba(212,162,127,.3)"/>
        <text x="500" y="116" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="rgb({ACC})">INBOX</text>
        <text x="606" y="132" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="30" fill="#FAFAF7">1</text>
        {env(504,116,30,f"rgb({ACC})")}
        <g filter="url(#rg)"><rect x="558" y="288" width="234" height="152" rx="20" fill="rgba(200,70,35,.10)" stroke="rgb({RED})" stroke-width="2"/></g>
        <text x="580" y="320" font-family="DM Mono" font-size="12.5" letter-spacing=".12em" fill="rgb({RED})">SPAM</text>
        <text x="772" y="332" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="46" fill="rgb({RED})">4</text>
        {spam}
      </svg>
      {cap("four of five never reach a human. the send worked, the arrival did not.")}</div>'''

# 2. OPENS - a gauge/dial reading a fake 68 percent, struck out, next to the real reply signal
def opens():
    pct=68; r=76; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARD};padding:34px 42px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;position:relative;width:212px;height:212px">
        <svg width="212" height="212" viewBox="0 0 212 212">
          <circle cx="106" cy="106" r="{r}" fill="none" stroke="rgba(212,162,127,.14)" stroke-width="16"/>
          <circle cx="106" cy="106" r="{r}" fill="none" stroke="rgba(212,162,127,.45)" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 106 106)"/>
          <line x1="46" y1="166" x2="166" y2="46" stroke="rgb({RED})" stroke-width="5" stroke-linecap="round"/>
        </svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:48px;color:#8f8f85">68%</span>
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({RED})">GHOST OPENS</span></div></div>
      <div style="flex:1">
        {htitle("Opens are a ghost metric","MISTAKE 01")}
        <div style="font-family:DM Sans;font-size:18px;color:#c9c3b8;line-height:1.45;margin-bottom:16px">Bots and privacy proxies auto-open before a human blinks. The number lies to you.</div>
        <div style="background:#211d19;border-left:4px solid rgb({ACC});border-radius:12px;padding:16px 22px;display:flex;align-items:center;justify-content:space-between">
          <div><div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">TRACK INSTEAD</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">Reply rate</div></div>
          <div style="font-family:DM Sans;font-weight:900;font-size:42px;color:rgb({ACC})">2%</div></div>
        {cap("the fix: score replies and inbox placement, never opens.")}
      </div></div>'''

# 3. DOMAIN - an aging timeline: a red day-2 blast spike vs a 90-day warm ramp climbing to trust
def domain():
    x0,x1,ay=90,760,372
    def dx(d): return x0+(x1-x0)*d/90.0
    ticks="".join(f'<line x1="{dx(d):.0f}" y1="{ay}" x2="{dx(d):.0f}" y2="{ay+8}" stroke="rgba(255,255,255,.22)"/>'
      f'<text x="{dx(d):.0f}" y="{ay+30}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">d{d}</text>' for d in (0,30,60,90))
    warmdots="".join(f'<circle cx="{cx}" cy="{cy}" r="6" fill="rgb({ACC})"/>' for cx,cy in [(165,352),(315,318),(465,250),(615,190),(760,150)])
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A newborn domain has no name","MISTAKE 02")}
      <svg width="820" height="446" viewBox="0 0 820 446" style="display:block;margin:0 auto">
        <defs><linearGradient id="warm" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="rgba(212,162,127,.4)"/><stop offset="1" stop-color="rgb({ACC})"/></linearGradient></defs>
        <line x1="{x0}" y1="{ay}" x2="{x1}" y2="{ay}" stroke="rgba(255,255,255,.25)" stroke-width="1.5"/>{ticks}
        <rect x="98" y="150" width="20" height="222" rx="4" fill="rgb({RED})"/>
        <text x="108" y="138" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="rgb({RED})">300</text>
        <text x="108" y="118" text-anchor="middle" font-family="DM Mono" font-size="11.5" letter-spacing=".06em" fill="rgb({RED})">FLAGGED</text>
        <path d="M90 372 C 300 362, 470 250, 760 150" fill="none" stroke="url(#warm)" stroke-width="4.5" stroke-linecap="round"/>
        {warmdots}
        <circle cx="760" cy="150" r="12" fill="rgb({ACC})"/>
        <text x="742" y="128" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">trust built</text>
        <text x="742" y="146" text-anchor="end" font-family="DM Mono" font-size="12" fill="rgb({ACC})">warmed 90 days</text>
      </svg>
      {cap("the fix: age the domain 90 plus days and warm the volume up slowly.")}</div>'''

# 4. AUTH - three record seals: SPF signed, DKIM and DMARC missing, a signed after-strip as the fix
def auth():
    recs=[("SPF","sender allowed",True,180),("DKIM","signature",False,410),("DMARC","policy",False,640)]
    seals=""
    for nm,sub,ok,cx in recs:
        if ok:
            seals+=(f'<g filter="url(#sg)"><circle cx="{cx}" cy="196" r="76" fill="url(#seal)"/></g>'
              f'<path d="M{cx-30} 196 l20 22 l40 -46" fill="none" stroke="#2a160c" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            seals+=(f'<circle cx="{cx}" cy="196" r="76" fill="rgba(200,70,35,.07)" stroke="rgb({RED})" stroke-width="2.5" stroke-dasharray="6 8"/>'
              f'<line x1="{cx-26}" y1="170" x2="{cx+26}" y2="222" stroke="rgb({RED})" stroke-width="6" stroke-linecap="round"/>'
              f'<line x1="{cx+26}" y1="170" x2="{cx-26}" y2="222" stroke="rgb({RED})" stroke-width="6" stroke-linecap="round"/>')
        col="#FAFAF7" if ok else "rgb("+RED+")"
        seals+=(f'<text x="{cx}" y="308" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="21" fill="{col}">{nm}</text>'
          f'<text x="{cx}" y="330" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Unsigned mail reads as a stranger","MISTAKE 03")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="seal" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {seals}
        <rect x="120" y="366" width="580" height="56" rx="14" fill="rgba(212,162,127,.08)" stroke="rgba(212,162,127,.4)" stroke-width="1.5"/>
        <text x="146" y="400" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="rgb({ACC})">FIX</text>
        <text x="410" y="400" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">Publish all three records, sign every send</text>
      </svg>
      {cap("the fix: two of three missing is why Gmail files you as unknown.")}</div>'''

# 5. CONTENT - IVORY email paper with trigger words flagged red, next to a climbing spam-score meter
def content():
    lines=[('Subject: ',[('FREE',1),(' demo, no ',0),('GUARANTEE',1),(' needed',0)]),
           ('',[('Re: Re: FWD',1),(' about your ',0),('ACCOUNT',1)]),
           ('',[('ACT NOW',1),(' before this ',0),('$$$',1),(' offer expires',0)]),
           ('',[('100% RISK-FREE',1),(', ',0),('CLICK HERE',1),(' to claim',0)]),
           ('',[('Click here',1),(' + 4 more links, 3 images attached',0)]),
           ('',[('Unsubscribe? ',0),('Reply STOP',1),(' to opt out',0)])]
    body=""
    for pre,parts in lines:
        seg=f'<span style="color:#5a4634">{pre}</span>' if pre else ''
        for txt,flag in parts:
            if flag: seg+=f'<span style="background:rgba(200,70,35,.16);color:rgb({RED});font-weight:700;border-radius:4px;padding:1px 5px">{txt}</span>'
            else: seg+=f'<span style="color:#2a2016">{txt}</span>'
        body+=f'<div style="margin-bottom:14px;line-height:1.5">{seg}</div>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;align-items:stretch;gap:30px">
      <div style="flex:1;display:flex;flex-direction:column">
        {htitle("Your copy trips the filter","MISTAKE 04","#2a2016")}
        <div style="background:rgba(255,255,255,.66);border:1px solid rgba(120,95,60,.18);border-radius:16px;padding:22px 24px;font-family:'DM Sans';font-size:19px;flex:1">
          {body}
        </div>
        {cap("the fix: plain words, one link, no image dump. write like a human.","#8a745a")}
      </div>
      <div style="flex-shrink:0;width:132px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding-bottom:8px">
        <span style="font-family:DM Sans;font-weight:900;font-size:34px;color:rgb({RED})">8.4</span>
        <span style="font-family:DM Mono;font-size:11px;letter-spacing:.08em;color:#96562d;margin-bottom:12px">SPAM SCORE</span>
        <div style="width:38px;height:250px;border-radius:19px;background:rgba(120,95,60,.14);position:relative;overflow:hidden">
          <div style="position:absolute;left:0;right:0;bottom:0;height:84%;background:linear-gradient(0deg,rgb({RED}),#e08b5a);border-radius:19px"></div></div>
        <span style="font-family:DM Mono;font-size:11px;color:rgb({RED});margin-top:10px">HIGH</span>
      </div></div>'''

# 6. VOLUME - a line chart: a day-1 blast spike that crashes vs a smooth ramp that holds
def volume():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("You blasted on day one","MISTAKE 05")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <line x1="90" y1="366" x2="770" y2="366" stroke="rgba(255,255,255,.22)" stroke-width="1.5"/>
        <line x1="90" y1="80" x2="90" y2="366" stroke="rgba(255,255,255,.14)" stroke-width="1.5"/>
        {''.join(f'<text x="{x}" y="392" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">wk{i+1}</text>' for i,x in enumerate((230,430,630)))}
        <path d="M100 366 L150 96 L172 300 L196 366" fill="none" stroke="rgb({RED})" stroke-width="4.5" stroke-linejoin="round"/>
        <circle cx="150" cy="96" r="7" fill="rgb({RED})"/>
        <text x="150" y="82" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="rgb({RED})">300 in a day</text>
        <text x="205" y="352" font-family="DM Mono" font-size="12.5" fill="rgb({RED})">12% bounce, burned</text>
        <path d="M100 358 C240 344,360 300,520 226 C620 182,700 150,760 132" fill="none" stroke="rgb({ACC})" stroke-width="4.5" stroke-linecap="round"/>
        {''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="rgb({ACC})"/>' for x,y in [(230,318),(430,262),(630,168),(760,132)])}
        <text x="760" y="116" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">held, 0.3% bounce</text>
      </svg>
      {cap("the fix: ramp the volume week by week and verify the list first.")}</div>'''

# 7. FIX STACK - IVORY ledger: 5 mistakes flip red to signed, inbox placement climbs 41 to 92
def fixstack():
    rows=[("Ghost opens","Reply + placement"),("New domain","Aged 90 days"),
          ("Unsigned mail","SPF, DKIM, DMARC"),("Trigger copy","Plain, one link"),
          ("Day-one blast","Ramped volume")]
    rr=""
    for bad,fix in rows:
        rr+=(f'<div style="display:flex;align-items:center;gap:14px;padding:13px 0;border-bottom:1px solid rgba(120,95,60,.16)">'
          f'<span style="flex:0 0 240px;font-family:DM Sans;font-size:17px;color:#a68c6a;text-decoration:line-through">{bad}</span>'
          f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3"><path d="M5 12h13M13 6l6 6-6 6"/></svg>'
          f'<span style="display:flex;align-items:center;gap:9px"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#2a2016">{fix}</span></span></div>')
    r=58; circ=2*math.pi*r; dash=circ*0.92
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px;display:flex;gap:34px;align-items:stretch">
      <div style="flex:1;display:flex;flex-direction:column">
        {htitle("Five checks, then send","THE FIX STACK","#2a2016")}
        <div style="flex:1">{rr}</div>
      </div>
      <div style="flex-shrink:0;width:220px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(255,255,255,.5);border-radius:20px;border:1px solid rgba(120,95,60,.16)">
        <div style="position:relative;width:170px;height:170px">
          <svg width="170" height="170" viewBox="0 0 170 170">
            <circle cx="85" cy="85" r="{r}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="15"/>
            <circle cx="85" cy="85" r="{r}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 85 85)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016">92%</span>
            <span style="font-family:DM Mono;font-size:11px;color:#96562d">INBOX</span></div></div>
        <div style="font-family:DM Mono;font-size:12.5px;color:#8a745a;margin-top:14px">up from 41%</div>
      </div></div>'''

# 8. GUARD - SPECTER hub scores every draft on all 5, only clean sends pass the human gate to inbox
def guard():
    checks=["opens","domain","auth","copy","volume"]
    hubx,hy=300,222
    left=""
    for i,nm in enumerate(checks):
        y=64+i*76; x=66
        left+=(f'<path d="M{x+40} {y} C170 {y},210 {hy},{hubx-62} {hy}" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
          f'<circle cx="{x}" cy="{y}" r="26" fill="#221f1b" stroke="rgba(212,162,127,.32)" stroke-width="1.5"/>'
          f'<path d="M{x-11} {y} l8 9 l16 -18" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<text x="{x+40}" y="{y+5}" font-family="DM Mono" font-size="12.5" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("It is checked before it sends","THE GUARD")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="hb" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {left}
        <g filter="url(#hg)"><circle cx="{hubx}" cy="{hy}" r="70" fill="url(#hb)"/></g>
        <text x="{hubx}" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="19" fill="#2a160c">SPECTER</text>
        <text x="{hubx}" y="{hy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">scores 5/5</text>
        <path d="M{hubx+70} {hy} H510" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 11" stroke-linecap="round"/>
        <rect x="512" y="{hy-60}" width="118" height="120" rx="24" fill="#201d19" stroke="rgb({ACC})" stroke-width="2.5"/>
        <g transform="translate(543,{hy-30})"><rect x="0" y="30" width="56" height="42" rx="9" fill="none" stroke="rgb({ACC})" stroke-width="5"/><path d="M10 30 V17 a18 18 0 0 1 36 0 v13" fill="none" stroke="rgb({ACC})" stroke-width="5"/></g>
        <text x="571" y="{hy+82}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">human gate</text>
        <path d="M630 {hy} H700" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 11" stroke-linecap="round"/>
        <rect x="702" y="{hy-40}" width="96" height="80" rx="18" fill="#1f1c18" stroke="rgba(212,162,127,.4)"/>
        <text x="750" y="{hy-4}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">INBOX</text>
        {env(726,hy+8,48,f"rgb({ACC})")}
      </svg>
      {cap("the fix, wired in: every draft is scored on all five before you tap send.")}</div>'''

PANELS={"verdict":verdict(),"opens":opens(),"domain":domain(),"auth":auth(),
        "content":content(),"volume":volume(),"fixstack":fixstack(),"guard":guard()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src32"; os.makedirs(outd,exist_ok=True)
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
