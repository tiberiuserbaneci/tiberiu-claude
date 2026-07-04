#!/usr/bin/env python3
# TIER 3 - CREATE ONCE, SELL FOREVER, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE
# hand-built coded scene filling a clean rounded card, title + one-line caption, NO generic
# stat-chip strips, NO clip-path cuts, NO extruded walls. Warm palette. Ultron prices = cents.
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
def ivhead(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#17150F">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def ivcap(t): return cap(t,"#8a745a")

# 1. LISTTRAP - a fanned pile of dimmed SAVED idea notes vs a huge muted-red 0 LIVE
def listtrap():
    ideas=[("AI onboarding kit",-2.5,4),("Cold email teardown",2.5,60),("Notion founder CRM",-2,116),
           ("Pricing calculator",2.5,172),("Investor update bot",-2,228)]
    cards=""
    for i,(nm,rot,y) in enumerate(ideas):
        cards+=(f'<div style="position:absolute;left:{i*6}px;top:{y}px;transform:rotate({rot}deg);width:352px;'
          f'background:linear-gradient(160deg,#2c2925,#211e1a);border:1px solid rgba(255,255,255,.08);border-radius:14px;'
          f'padding:15px 18px;box-shadow:0 16px 30px rgba(0,0,0,.5);display:flex;align-items:center;justify-content:space-between">'
          f'<span style="font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#8f8a80">{nm}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.12em;color:#6f6a60;border:1px solid rgba(255,255,255,.1);padding:3px 8px;border-radius:6px">SAVED</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A vault full of maybes","50 SAVED / 0 LIVE")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="position:relative;width:404px;height:336px;flex-shrink:0">{cards}
          <div style="position:absolute;left:100px;top:290px;background:rgba(200,70,35,.14);border:1px solid rgba(200,70,35,.4);border-radius:999px;padding:7px 16px;font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:rgb(200,70,35)">+ 45 MORE SAVED</div>
        </div>
        <div style="flex:1;text-align:center">
          <div style="font-family:\'DM Sans\';font-weight:900;font-size:150px;color:rgb(200,70,35);line-height:.9">0</div>
          <div style="font-family:\'DM Mono\';font-size:15px;letter-spacing:.2em;color:#c98b7a;margin-top:6px">PRODUCTS LIVE</div>
          <div style="font-family:\'DM Sans\';font-size:18px;color:#8f8f85;margin-top:16px;line-height:1.4">A saved idea earns nothing.<br>Shipping is the only progress.</div>
        </div>
      </div>
      {cap("idea lists feel like momentum. the shelf stays empty until one goes live.")}</div>'''

# 2. PICK9 - IVORY, most-asked bar chart, the tallest bar lit as THE product
def pick9():
    bars=[("Cold-email checklist",12,True),("Pricing model teardown",7,False),("ICP worksheet",5,False),("Onboarding SOP",3,False)]
    mx=12; rows=""
    for nm,n,pick in bars:
        w=int(64+(n/mx)*380)
        col="#96562d" if pick else "rgba(150,90,45,.30)"
        lbl='<span style="font-family:\'DM Mono\';font-size:13px;color:#96562d;margin-left:12px;font-weight:500">THE PRODUCT</span>' if pick else ''
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:18px">'
          f'<div style="width:236px;font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#2a2016;text-align:right;flex-shrink:0">{nm}</div>'
          f'<div style="height:36px;width:{w}px;background:{col};border-radius:9px;box-shadow:inset 0 2px 3px rgba(255,255,255,.35), 0 6px 14px rgba(150,90,45,.18)"></div>'
          f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:23px;color:#2a2016">{n}x</span>{lbl}</div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {ivhead("Sell what they already ask for","ASKED THIS MONTH")}
      <div style="margin:10px 0 2px">{rows}</div>
      {ivcap("the template, checklist or audit you explain every week is the product hiding in plain sight.")}</div>'''

# 3. BUILD9 - one typed sentence in, arrow down, 3 assembled artifact tiles out
def build9():
    outs=[("Template pack",".zip &middot; 9 files","M4 5h16M4 12h16M4 19h10"),
          ("Setup guide",".pdf &middot; 14 pages","M7 3h7l5 5v13H7z M14 3v6h6"),
          ("Onboarding email","3-step sequence","M3 6h18v12H3z M3 7l9 6 9-6")]
    tiles=""
    for nm,meta,path in outs:
        tiles+=(f'<div style="flex:1;background:linear-gradient(160deg,#332f2a,#221f1b);border:1px solid rgba(255,255,255,.09);border-radius:18px;padding:20px 18px;box-shadow:0 18px 34px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<div style="width:44px;height:44px;border-radius:12px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;margin-bottom:14px">'
          f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"/></svg></div>'
          f'<div style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:\'DM Mono\';font-size:12px;color:#8f8f85;margin-top:4px">{meta}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One sentence in","DESK ASSEMBLES")}
      <div style="background:#211e1a;border:1px solid rgba(212,162,127,.28);border-radius:16px;padding:18px 22px;display:flex;align-items:center;gap:14px">
        <span style="font-family:\'DM Mono\';font-size:13px;color:rgb({ACC});flex-shrink:0">YOU</span>
        <span style="font-family:\'DM Sans\';font-size:20px;color:#e6e0d4">"Package my cold-email checklist as a paid kit"</span>
        <span style="width:2.5px;height:24px;background:rgb({ACC});margin-left:2px"></span></div>
      <svg width="60" height="50" viewBox="0 0 60 50" style="display:block;margin:6px auto 4px"><path d="M30 4 V38 M18 28 L30 40 L42 28" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <div style="display:flex;gap:18px">{tiles}</div>
      {cap("your workflow becomes the template pack, the guide and the system, built from your own files.")}</div>'''

# 4. PAGE9 - coded browser-window mockup of the live offer page (hero + price + FAQ)
def page9():
    faq=["Do I get the source files?","Team license available?","Free updates included?"]
    faql="".join(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px"><span style="width:6px;height:6px;border-radius:50%;background:rgb({ACC})"></span><span style="font-family:\'DM Sans\';font-size:15px;color:#b8b2a6">{q}</span></div>' for q in faq)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Live the same afternoon","OFFER PAGE")}
      <div style="background:#141210;border:1px solid rgba(255,255,255,.09);border-radius:18px;overflow:hidden;box-shadow:0 26px 50px rgba(0,0,0,.55)">
        <div style="display:flex;align-items:center;gap:8px;padding:14px 18px;background:#1f1c19;border-bottom:1px solid rgba(255,255,255,.07)">
          <span style="width:11px;height:11px;border-radius:50%;background:#3a3631"></span><span style="width:11px;height:11px;border-radius:50%;background:#3a3631"></span><span style="width:11px;height:11px;border-radius:50%;background:#3a3631"></span>
          <div style="flex:1;margin-left:10px;background:#141210;border:1px solid rgba(255,255,255,.08);border-radius:8px;padding:7px 14px;font-family:\'DM Mono\';font-size:13px;color:#9a9488">app.51ultron.com/kit</div>
          <span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.12em;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);padding:4px 10px;border-radius:6px">LIVE</span></div>
        <div style="padding:30px 34px;display:flex;gap:34px;align-items:center">
          <div style="flex:1">
            <div style="font-family:\'DM Sans\';font-weight:900;font-size:33px;color:#FAFAF7;line-height:1.12">The cold-email kit that books meetings</div>
            <div style="font-family:\'DM Sans\';font-size:17px;color:#9a9488;margin:12px 0 20px">9 templates, the audit prompt, the sending SOP.</div>
            {faql}
          </div>
          <div style="flex-shrink:0;width:214px;background:linear-gradient(160deg,#2c2925,#201d19);border:1px solid rgba(212,162,127,.3);border-radius:16px;padding:22px 20px;text-align:center;box-shadow:0 16px 30px rgba(0,0,0,.4)">
            <div style="font-family:\'DM Sans\';font-weight:900;font-size:46px;color:#FAFAF7;line-height:1">$49</div>
            <div style="font-family:\'DM Mono\';font-size:12px;color:#8f8f85;margin-bottom:18px">one-time</div>
            <div style="background:rgb({ACC});color:#1a0f0a;font-family:\'DM Sans\';font-weight:900;font-size:17px;padding:13px;border-radius:12px;box-shadow:0 10px 22px rgba(212,162,127,.35)">Get the kit</div></div>
        </div></div>
      {cap("hero, pricing and FAQ from the component pack, in your own brand tokens.")}</div>'''

# 5. DELIVERY - vertical night timeline, 03:14 timestamps, Ultron ran it for cents
def delivery():
    ev=[("03:14","Payment received","$49 &middot; Stripe"),
        ("03:14","Product delivered","kit.zip to the buyer inbox"),
        ("03:14","Receipt sent","invoice + license key"),
        ("03:15","Follow-up queued","day-3 check-in email")]
    rows=""
    for i,(t,a,b) in enumerate(ev):
        rows+=(f'<div style="display:flex;align-items:flex-start;gap:20px;padding-bottom:{0 if i==len(ev)-1 else 22}px">'
          f'<span style="font-family:\'DM Mono\';font-weight:500;font-size:16px;color:rgb({ACC});width:52px;flex-shrink:0;padding-top:2px">{t}</span>'
          f'<span style="position:relative;z-index:2;width:16px;height:16px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 0 5px rgba(212,162,127,.14);flex-shrink:0;margin-top:2px"></span>'
          f'<div style="flex:1"><div style="font-family:\'DM Sans\';font-weight:800;font-size:20px;color:#FAFAF7">{a}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:15px;color:#8f8f85;margin-top:1px">{b}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It sells while you sleep","03:14 &middot; UNATTENDED")}
      <div style="position:relative;padding-left:2px">
        <div style="position:absolute;left:63px;top:8px;bottom:28px;width:2px;background:rgba(212,162,127,.25)"></div>
        {rows}</div>
      <div style="display:flex;align-items:center;gap:12px;margin-top:8px;background:rgba(212,162,127,.08);border:1px solid rgba(212,162,127,.24);border-radius:12px;padding:12px 18px;width:fit-content">
        <span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:#8f8f85">ULTRON RAN THE WHOLE FLOW FOR</span>
        <span style="font-family:\'DM Sans\';font-weight:900;font-size:20px;color:rgb({ACC})">0.4c</span></div>
      {cap("the flow sends the product, the receipt and the follow-up while you sleep.")}</div>'''

# 6. LOOP9 - IVORY, buyer question chips funnel down into a drafted v2.0
def loop9():
    qs=["refund window?","team seats?","CSV export?","API access?","onboarding call?"]
    chips="".join(f'<span style="font-family:\'DM Sans\';font-size:15px;color:#5a4634;background:rgba(255,255,255,.6);border:1px solid rgba(150,90,45,.22);border-radius:999px;padding:8px 15px">{q}</span>' for q in qs)
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {ivhead("Buyers write version two","FEEDBACK LOOP")}
      <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;max-width:660px;margin:0 auto 4px">{chips}</div>
      <svg width="300" height="118" viewBox="0 0 300 118" style="display:block;margin:0 auto">
        <path d="M20 12 L280 12 L188 84 L188 112 L112 112 L112 84 Z" fill="rgba(150,90,45,.10)" stroke="#96562d" stroke-width="2"/>
        <text x="150" y="56" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#96562d">FUNNEL</text>
      </svg>
      <div style="display:flex;align-items:center;justify-content:center;gap:16px;margin-top:8px">
        <div style="background:#96562d;color:#fff;font-family:\'DM Sans\';font-weight:900;font-size:24px;padding:12px 26px;border-radius:14px;box-shadow:0 14px 28px rgba(150,90,45,.3)">v2.0</div>
        <span style="font-family:\'DM Sans\';font-weight:700;font-size:18px;color:#2a2016">3 fixes drafted, waiting your tap</span></div>
      {ivcap("every buyer question funnels into the next update, drafted and queued for your approval.")}</div>'''

# 7. SPREAD - a validated pipeline clones sideways into a second niche
def spread():
    def pipe(title,tag,steps,revenue,active):
        op="1" if active else ".55"
        sh=""
        for s in steps:
            sh+=('<div style="display:flex;align-items:center;gap:10px;margin-bottom:9px">'
              f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 12.5l3.5 3.5L18 7.5"/></svg>'
              f'<span style="font-family:\'DM Sans\';font-size:16px;color:#c9c3b8">{s}</span></div>')
        return (f'<div style="flex:1;background:linear-gradient(160deg,#2c2925,#201d19);border:1px solid {"rgba(212,162,127,.34)" if active else "rgba(255,255,255,.08)"};border-radius:20px;padding:22px 24px;opacity:{op}">'
          f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px"><span style="font-family:\'DM Sans\';font-weight:800;font-size:21px;color:#FAFAF7">{title}</span>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.1em;color:rgb({ACC})">{tag}</span></div>'
          f'{sh}'
          f'<div style="margin-top:14px;padding-top:14px;border-top:1px solid rgba(255,255,255,.08);font-family:\'DM Sans\';font-weight:900;font-size:26px;color:rgb({ACC})">{revenue}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One funds the next","CLONE SIDEWAYS")}
      <div style="display:flex;align-items:center;gap:14px">
        {pipe("Cold-email kit","VALIDATED",["picked","assembled","selling"],"$1,240 / mo",True)}
        <div style="flex-shrink:0;text-align:center">
          <svg width="58" height="40" viewBox="0 0 58 40"><path d="M6 20 H46 M36 10 L48 20 L36 30" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <div style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.1em;color:#8f8f85;margin-top:2px">CLONE</div></div>
        {pipe("Onboarding kit","CLONED &middot; 1 DAY",["picked","assembled","launching"],"niche #2",False)}
      </div>
      {cap("validate one niche, then let the desk clone the whole pipeline sideways.")}</div>'''

# 8. MATH9 - closing: cumulative-sales growth curve, build effort flat vs sales compounding
def math9():
    W,H=740,290
    pts=[(0,264),(74,250),(148,228),(222,220),(296,188),(370,172),(444,130),(518,102),(592,58),(666,32),(740,14)]
    poly=" ".join(f"{x},{y}" for x,y in pts)
    area=f"0,{H} "+poly+f" {W},{H}"
    dots="".join(f'<circle cx="{x}" cy="{y}" r="5" fill="rgb({ACC})"/>' for x,y in pts[2::2])
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Created once. Sold on repeat.","DIGITAL SHELF")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:6px auto 0">
        <defs><linearGradient id="af" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(212,162,127,.42)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></linearGradient></defs>
        <line x1="0" y1="{H-1}" x2="{W}" y2="{H-1}" stroke="rgba(255,255,255,.08)"/>
        <polygon points="{area}" fill="url(#af)"/>
        <polyline points="{poly}" fill="none" stroke="rgb({ACC})" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
        {dots}
        <circle cx="0" cy="264" r="7" fill="#FAFAF7"/>
        <text x="12" y="286" font-family="DM Mono" font-size="13" fill="#8f8f85">created: 1</text>
        <text x="{W}" y="32" text-anchor="end" font-family="DM Sans" font-weight="900" font-size="22" fill="rgb({ACC})">sold: 1,900+</text>
      </svg>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px">
        <div style="font-family:\'DM Sans\';font-weight:900;font-size:26px;color:#FAFAF7">Build effort: flat.</div>
        <div style="font-family:\'DM Sans\';font-weight:900;font-size:26px;color:rgb({ACC})">Sales: compounding.</div></div>
      {cap("the digital shelf never closes and never reorders stock.")}</div>'''

PANELS={"listtrap":listtrap(),"pick9":pick9(),"build9":build9(),"page9":page9(),
        "delivery":delivery(),"loop9":loop9(),"spread":spread(),"math9":math9()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/sellonce"; os.makedirs(outd,exist_ok=True)
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
