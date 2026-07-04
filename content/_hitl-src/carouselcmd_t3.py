#!/usr/bin/env python3
# TIER 3 - THE CAROUSEL COMMAND, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
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

# 1. OLDBILL - the old way as a week-long GANTT: one deck stretched Mon->Fri across brief/draft/
# revision bars, a red overrun tail, and the agency retainer as the (competitor) cost line.
def oldbill():
    days=["MON","TUE","WED","THU","FRI"]
    colw=142; x0=44
    grid=""
    for i,d in enumerate(days):
        gx=x0+i*colw
        grid+=(f'<line x1="{gx}" y1="34" x2="{gx}" y2="330" stroke="rgba(255,255,255,.06)"/>'
          f'<text x="{gx+12}" y="24" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#7a746a">{d}</text>')
    bars=[("Kickoff brief",0,1.0,58,"rgba(212,162,127,.35)"),
          ("Draft round 1",0.6,1.6,116,"rgba(212,162,127,.55)"),
          ("Revision round 2",2.0,1.4,174,"rgba(212,162,127,.75)"),
          ("Revision round 3",3.1,1.1,232,f"rgb({ACC})"),
          ("Still not shipped",4.0,0.9,290,"rgba(200,70,35,.85)")]
    rows=""
    for lbl,st,sp,y,col in bars:
        bx=x0+st*colw; bw=sp*colw
        rows+=(f'<rect x="{bx:.0f}" y="{y}" width="{bw:.0f}" height="40" rx="10" fill="{col}" '
          f'style="filter:drop-shadow(0 8px 16px rgba(0,0,0,.4))"/>'
          f'<text x="{bx+16:.0f}" y="{y+26}" font-family="DM Sans" font-weight="700" font-size="16" fill="#1a0f0a">{lbl}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A week per deck","THE OLD WAY")}
      <svg width="820" height="342" viewBox="0 0 820 342" style="display:block">
        {grid}
        <line x1="{x0}" y1="330" x2="782" y2="330" stroke="rgba(255,255,255,.1)"/>
        {rows}
      </svg>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:14px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08)">
        <span style="font-family:'DM Mono';font-size:13px;color:#8f8f85">agency retainer, the old line item</span>
        <span style="font-family:'DM Sans';font-weight:900;font-size:30px;color:rgb(200,70,35)">$4,000/mo</span></div>
      {cap("briefs, revisions, queue time. a week per deck, every single deck.")}</div>'''

# 2. COMMAND - PULSE interview chat mockup: agent question bubbles + your short answers, ends with
# a "building..." status pill. Distinct chat-thread form.
def command():
    thread=[("q","PULSE","What is the angle for this deck?"),
            ("a","You","how the carousel builds itself"),
            ("q","PULSE","Which agent owns the payoff slide?"),
            ("a","You","PULSE, end to end"),
            ("q","PULSE","Channel and length?"),
            ("a","You","TikTok + IG, ten pages")]
    msgs=""
    for kind,who,txt in thread:
        if kind=="q":
            msgs+=(f'<div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:14px">'
              f'<div style="flex-shrink:0;width:38px;height:38px;border-radius:11px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 60%,#9a5a35);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:15px;color:#1a0f0a;box-shadow:0 6px 14px rgba(212,162,127,.4)">P</div>'
              f'<div style="max-width:520px;background:linear-gradient(160deg,#33302c,#242019);border:1px solid rgba(255,255,255,.09);border-radius:6px 18px 18px 18px;padding:13px 18px">'
              f'<div style="font-family:DM Mono;font-size:11px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:3px">{who}</div>'
              f'<div style="font-family:DM Sans;font-size:18px;color:#eae4d8">{txt}</div></div></div>')
        else:
            msgs+=(f'<div style="display:flex;justify-content:flex-end;margin-bottom:14px">'
              f'<div style="max-width:440px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.34);border-radius:18px 6px 18px 18px;padding:11px 18px">'
              f'<div style="font-family:DM Sans;font-size:18px;color:#f2ead8">{txt}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It interviews me","PULSE · CHAT")}
      <div style="background:#161513;border:1px solid rgba(255,255,255,.06);border-radius:22px;padding:24px 26px 22px">
        {msgs}
        <div style="display:flex;align-items:center;gap:12px;margin-top:4px">
          <span style="width:10px;height:10px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba(212,162,127,.8)"></span>
          <span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">building the deck...</span></div>
      </div>
      {cap("PULSE asks for the angle, then owns the build end to end.")}</div>'''

# 3. VISUALS - IVORY brand-token board: color swatches + type spec + component chips. Design-system
# swatch scene, distinct from every other panel.
def visuals():
    sw=[("Slate","#1d1d1b"),("Book","#cc785c"),("Kraft","#d4a27f"),("Ivory","#faf8f2")]
    swatches=""
    for nm,hx in sw:
        swatches+=(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px">'
          f'<div style="width:96px;height:96px;border-radius:20px;background:{hx};box-shadow:0 12px 24px rgba(120,95,60,.24),inset 0 2px 3px rgba(255,255,255,.3);border:1px solid rgba(120,95,60,.14)"></div>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:15px;color:#2a2016">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:11px;color:#96562d">{hx}</span></div>')
    comps=""
    for c in ["mast","stat card","CTA chip","footer"]:
        comps+=f'<span style="font-family:DM Mono;font-size:13px;color:#5a4634;background:rgba(255,255,255,.6);border:1px solid rgba(150,90,45,.22);border-radius:999px;padding:8px 16px">{c}</span>'
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("My tokens, my type","BRAND KIT","#2a2016")}
      <div style="display:flex;gap:22px;justify-content:space-between;margin-bottom:24px">{swatches}</div>
      <div style="display:flex;gap:28px;align-items:center;background:rgba(255,255,255,.55);border-left:4px solid #96562d;border-radius:14px;padding:20px 24px">
        <div style="flex-shrink:0">
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#2a2016;line-height:1">DM Sans</div>
          <div style="font-family:DM Mono;font-size:16px;color:#96562d;margin-top:4px">DM Mono / meta</div></div>
        <div style="width:1px;height:64px;background:rgba(150,90,45,.22)"></div>
        <div style="display:flex;flex-wrap:wrap;gap:10px">{comps}</div>
      </div>
      {cap("brand colors, brand type, brand components. no template smell.","#8a745a")}</div>'''

# 4. SLIDES - a filmstrip of 10 assembled pages on a perspective rail, hook/body/CTA roles marked.
def slides():
    frames=""
    for i in range(10):
        role="HOOK" if i==0 else ("CTA" if i==9 else "BODY")
        lit = i==0 or i==9
        accent=f"rgb({ACC})" if lit else "rgba(212,162,127,.28)"
        inner=(f'<div style="height:8px;width:72%;border-radius:3px;background:{accent};margin-bottom:7px"></div>'
               f'<div style="height:5px;width:90%;border-radius:3px;background:rgba(255,255,255,.14);margin-bottom:5px"></div>'
               f'<div style="height:5px;width:66%;border-radius:3px;background:rgba(255,255,255,.14)"></div>')
        if i==0:
            inner=(f'<div style="font-family:DM Sans;font-weight:900;font-size:15px;color:#FAFAF7;line-height:1.15">This deck<br>built itself</div>')
        if i==9:
            inner=(f'<div style="display:flex;align-items:center;justify-content:center;height:100%"><div style="background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:11px;padding:6px 11px;border-radius:999px">COMMENT &#8594;</div></div>')
        ml="0" if i==0 else "-46px"
        frames+=(f'<div style="flex-shrink:0;width:114px;height:200px;margin-left:{ml};border-radius:16px;background:linear-gradient(165deg,#35312c,#211e1a);'
          f'border:1.5px solid {"rgba(212,162,127,.55)" if lit else "rgba(255,255,255,.09)"};'
          f'box-shadow:-18px 22px 34px rgba(0,0,0,.55),inset 0 2px 2px rgba(255,255,255,.08);padding:15px 14px;display:flex;flex-direction:column;position:relative;z-index:{i}">'
          f'<span style="font-family:DM Mono;font-size:9.5px;letter-spacing:.08em;color:{accent};margin-bottom:9px;white-space:nowrap">{i+1:02d} · {role}</span>'
          f'<div style="flex:1">{inner}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Ten pages assembled","PROVEN BONES")}
      <div style="perspective:1700px;height:300px;display:flex;align-items:center;justify-content:center">
        <div style="transform:rotateX(8deg);transform-style:preserve-3d;display:flex;align-items:center">{frames}</div>
      </div>
      {cap("hook, body, CTA: structured like the decks that already performed.")}</div>'''

# 5. CAPTIONS - IVORY editor mockup: caption doc with CTA-first line, hashtag row, first-comment
# block, a cursor typing itself in. Distinct document-editor form.
def captions():
    tags=" ".join(f'<span style="color:#96562d">#{t}</span>' for t in ["claude","ai","founder","startup","buildinpublic"])
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitle("The caption kit","AUTO-WRITTEN","#2a2016")}
      <div style="background:#fffdf8;border:1px solid rgba(150,90,45,.20);border-radius:18px;box-shadow:inset 0 2px 6px rgba(150,120,80,.10);overflow:hidden">
        <div style="display:flex;align-items:center;gap:8px;padding:12px 18px;background:rgba(150,90,45,.07);border-bottom:1px solid rgba(150,90,45,.14)">
          <span style="width:11px;height:11px;border-radius:50%;background:#d78b5c"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:rgba(150,90,45,.3)"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:rgba(150,90,45,.3)"></span>
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#96562d;margin-left:8px">caption.md</span></div>
        <div style="padding:20px 24px 22px;font-family:'DM Sans';font-size:18px;color:#2a2016;line-height:1.5">
          <div style="display:inline;background:rgba(212,162,127,.28);border-radius:4px;padding:2px 6px;font-weight:700">Comment CAROUSEL and I will send you the exact build.</div>
          <div style="margin-top:14px;color:#5a4634">You brief it once. It assembles the deck, sizes each channel, and hands back the whole kit.</div>
          <div style="margin-top:14px;font-family:'DM Mono';font-size:15px">{tags}<span style="display:inline-block;width:2px;height:20px;background:#96562d;vertical-align:-4px;margin-left:3px"></span></div>
          <div style="margin-top:16px;padding-top:14px;border-top:1px dashed rgba(150,90,45,.28);font-family:DM Mono;font-size:13px;color:#8a745a">FIRST COMMENT · drop CAROUSEL below, I read every one.</div>
        </div>
      </div>
      {cap("CTA-first caption, five hashtags, first comment. the whole posting kit.","#8a745a")}</div>'''

# 6. CLOCK - a build-progress gauge: full accent ring, center time readout, and the three
# assembled artifacts ticked below. Gauge/clock scene.
def clock():
    pct=100; r=118; circ=2*math.pi*r; dash=circ*pct/100
    ticks=""
    for a in range(0,360,30):
        x1=210+108*math.cos(math.radians(a)); y1=210+108*math.sin(math.radians(a))
        x2=210+118*math.cos(math.radians(a)); y2=210+118*math.sin(math.radians(a))
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
    done=""
    for lbl in ["Cover rendered","10 slides sized","Caption kit written"]:
        done+=(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">'
          f'<svg width="24" height="24" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.16)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{lbl}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:36px">
      <svg width="420" height="420" viewBox="0 0 420 420">
        <defs><filter id="rg" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {ticks}
        <circle cx="210" cy="210" r="{r}" fill="none" stroke="rgba(255,255,255,.07)" stroke-width="16"/>
        <circle cx="210" cy="210" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 210 210)" filter="url(#rg)"/>
        <text x="210" y="196" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="58" fill="#FAFAF7">6:40</text>
        <text x="210" y="238" text-anchor="middle" font-family="DM Mono" font-size="15" letter-spacing=".14em" fill="rgb({ACC})">MINUTES</text>
      </svg>
      <div style="flex:1">
        {htitle("Coffee brewed. Deck done.","ONE PASS")}
        {done}
        {cap("cover, slides, captions, sized per channel. while the coffee brews.")}
      </div></div>'''

# 7. GATE - publish queue: batched pages lined up behind ONE review gate, one operator tap
# releases them to the channels. Queue/publish-flow scene.
def gate():
    queue=""
    for i in range(6):
        op=1 - i*0.12
        queue+=(f'<div style="width:64px;height:86px;border-radius:12px;background:linear-gradient(160deg,#33302c,#221f1a);'
          f'border:1px solid rgba(255,255,255,.10);box-shadow:0 14px 24px rgba(0,0,0,.45);opacity:{op:.2f};flex-shrink:0;'
          f'display:flex;flex-direction:column;justify-content:flex-end;padding:8px">'
          f'<div style="height:6px;width:70%;border-radius:3px;background:rgba(212,162,127,.4);margin-bottom:4px"></div>'
          f'<div style="height:5px;width:90%;border-radius:3px;background:rgba(255,255,255,.12)"></div></div>')
    chans=""
    for nm in ["TikTok","Instagram"]:
        chans+=(f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:12px">'
          f'<span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC})"></span>'
          f'<span style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7">{nm}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One review. One tap.","HUMAN GATE")}
      <div style="display:flex;align-items:center;gap:20px;height:250px">
        <div style="display:flex;gap:10px;align-items:center">{queue}</div>
        <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:10px;
          background:linear-gradient(160deg,#403a33,#241f1a);border:2px solid rgb({ACC});border-radius:22px;padding:22px 24px;
          box-shadow:0 20px 40px rgba(0,0,0,.5),0 0 40px rgba(212,162,127,.2)">
          <svg width="46" height="46" viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2.5" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><path d="M8 10 V7 a4 4 0 0 1 8 0" fill="none" stroke="rgb({ACC})" stroke-width="2.2"/><circle cx="12" cy="15.5" r="1.8" fill="rgb({ACC})"/></svg>
          <span style="font-family:DM Sans;font-weight:900;font-size:20px;color:#FAFAF7">REVIEW</span>
          <span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">your tap</span></div>
        <svg width="52" height="30" viewBox="0 0 52 30"><path d="M4 15 H44 M34 6 l10 9 -10 9" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex:1;padding-left:6px">{chans}</div>
      </div>
      {cap("you review the batch once. nothing posts on its own.")}</div>'''

# 8. MATH - retainer -> runway: a tall competitor retainer bar beside a tiny Ultron cents bar,
# the difference labeled as reclaimed runway. Bar-comparison scene (Ultron = cents).
def math_panel():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Retainer money became runway","METERED, NOT SEATED")}
      <svg width="820" height="360" viewBox="0 0 820 360" style="display:block;margin:0 auto">
        <defs><linearGradient id="cbar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#c85236"/><stop offset="100%" stop-color="#8f3a24"/></linearGradient>
        <linearGradient id="ubar" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e6b48f"/><stop offset="100%" stop-color="rgb({ACC})"/></linearGradient></defs>
        <line x1="60" y1="300" x2="760" y2="300" stroke="rgba(255,255,255,.12)"/>
        <rect x="150" y="46" width="150" height="254" rx="10" fill="url(#cbar)" style="filter:drop-shadow(0 16px 30px rgba(0,0,0,.5))"/>
        <text x="225" y="34" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="rgb(200,70,35)">$4,000</text>
        <text x="225" y="326" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#8f8f85">AGENCY RETAINER / MO</text>
        <rect x="510" y="270" width="150" height="30" rx="8" fill="url(#ubar)" style="filter:drop-shadow(0 10px 20px rgba(212,162,127,.4))"/>
        <text x="585" y="256" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="rgb({ACC})">cents</text>
        <text x="585" y="326" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#8f8f85">ULTRON / DECK</text>
        <path d="M310 120 C400 120,420 260,500 282" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5" stroke-dasharray="3 8"/>
        <rect x="352" y="150" width="128" height="52" rx="14" fill="#211d19" stroke="rgba(212,162,127,.34)"/>
        <text x="416" y="176" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">reclaimed</text>
        <text x="416" y="194" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">= runway</text>
      </svg>
      {cap("metered by use, not by seats. the retainer becomes runway.")}</div>'''

PANELS={"oldbill":oldbill(),"command":command(),"visuals":visuals(),"slides":slides(),
        "captions":captions(),"clock":clock(),"gate":gate(),"math":math_panel()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/carouselcmd"; os.makedirs(outd,exist_ok=True)
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
