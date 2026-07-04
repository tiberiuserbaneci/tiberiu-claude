#!/usr/bin/env python3
# TIER 3 - DIRECTION BEATS PROMPTS, rebuilt to the WIRE-ITS-EYES bar: each of the 8 panels is a
# UNIQUE hand-built coded scene filling a clean rounded card, title + one-line mono caption, NO
# generic stat-chip strips, no clip-path cuts, no extruded walls. Warm palette only.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"          # warm accent
IVA="#96562d"              # ivory-slide accent
BAD="rgb(200,70,35)"       # muted red, ONLY for the bad/missing state
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. MIST10 - a prompt console mockup: a vague ask with three unattached direction slots (red-missing)
def mist10():
    slots=[("AUDIENCE","who reads this?"),("TONE","how should it sound?"),("GOAL","what should it do?")]
    chips=""
    for lab,q in slots:
        chips+=(f'<div style="flex:1;background:rgba(250,250,247,.03);border:1.5px dashed rgba(200,70,35,.42);border-radius:14px;padding:16px 16px 15px;text-align:left">'
          f'<div style="display:flex;align-items:center;justify-content:space-between"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.10em;color:#c9c3b8">{lab}</span>'
          f'<svg width="18" height="18" viewBox="0 0 24 24" stroke="{BAD}" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-top:8px">{q}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:{BAD};margin-top:10px">not attached</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Everyone prompts. Few direct.","THE COMMON ERROR")}
      <div style="background:linear-gradient(160deg,#211e1a,#181613);border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:22px 24px 24px;box-shadow:inset 0 2px 3px rgba(255,255,255,.06)">
        <div style="display:flex;gap:7px;margin-bottom:18px">
          <span style="width:11px;height:11px;border-radius:50%;background:rgba(255,255,255,.18)"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:rgba(255,255,255,.12)"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:rgba(255,255,255,.08)"></span></div>
        <div style="display:flex;align-items:center;gap:16px;background:#2a2724;border:1px solid rgba(255,255,255,.10);border-radius:14px;padding:17px 18px">
          <span style="font-family:'DM Sans';font-size:23px;color:#e6e0d3;flex:1">Write me a post about AI.</span>
          <div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 60%,#9a5a35);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 2px 3px rgba(255,255,255,.4)">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h14M12 6l6 6-6 6"/></svg></div>
        </div>
        <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.16em;color:#8f8f85;margin:22px 0 12px">ATTACHED DIRECTION</div>
        <div style="display:flex;gap:14px">{chips}</div>
      </div>
      {cap("no audience, no tone, no goal: the model fills the blanks with average.")}</div>'''

# 2. DIR1 - IVORY two-card comparison: the vague topic (shrug) vs the reader brief
def dir1():
    reader=[("Founders","who is scanning the feed"),("1.7 seconds","the attention you get"),("A system","not another theory take")]
    rows="".join(f'<div style="display:flex;align-items:center;gap:12px;padding:11px 0;border-top:1px solid rgba(150,90,45,.16)"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{IVA}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#2a2016">{a}</span><span style="font-family:DM Sans;font-size:15px;color:#8a745a;margin-left:auto;text-align:right">{b}</span></div>' for a,b in reader)
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("Give it the reader, not the topic.","AIM AT A PERSON","#2a2016",IVA)}
      <div style="display:flex;align-items:stretch;gap:22px">
        <div style="width:290px;flex-shrink:0;background:rgba(120,95,60,.07);border:1.5px dashed rgba(120,95,60,.3);border-radius:20px;padding:22px 22px;display:flex;flex-direction:column">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#a08a68">THE SHRUG</div>
          <div style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#7a6a52;margin-top:14px;line-height:1.2">"Write about AI"</div>
          <div style="font-family:DM Sans;font-size:15px;color:#a08a68;margin-top:auto;padding-top:20px">the model guesses who it is for, and guesses average</div>
        </div>
        <div style="flex-shrink:0;align-self:center;font-family:'DM Sans';font-weight:900;font-size:20px;color:{IVA}">VS</div>
        <div style="flex:1;background:rgba(255,255,255,.62);border:1.5px solid {IVA};border-radius:20px;padding:22px 24px;box-shadow:0 16px 30px rgba(120,95,60,.14)">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{IVA}">THE BRIEF</div>
          <div style="margin-top:8px">{rows}</div>
        </div>
      </div>
      {cap("the same request, aimed at a person, writes itself.","#8a745a")}</div>'''

# 3. DIR2 - five real sample posts feed a voice-lock fingerprint (dark)
def dir2():
    samples=["I killed nine tools last month.","Your CRM is a graveyard of intent.","Founders do not need more dashboards.","I let Claude read 400 cold emails.","Stop hiring reps. Start directing one."]
    feed=""
    for i,s in enumerate(samples):
        feed+=(f'<div style="display:flex;align-items:center;gap:14px;background:linear-gradient(158deg,#332f2a,#221f1b);border:1px solid rgba(255,255,255,.09);border-radius:13px;padding:12px 16px;box-shadow:0 10px 20px rgba(0,0,0,.4)">'
          f'<span style="flex-shrink:0;font-family:DM Mono;font-size:12px;color:rgb({ACC})">0{i+1}</span>'
          f'<span style="font-family:DM Sans;font-size:17px;color:#e2dccf;line-height:1.25">"{s}"</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Feed it your tone, from samples","VOICE LOCK")}
      <div style="display:flex;align-items:center;gap:26px">
        <div style="flex:1;display:flex;flex-direction:column;gap:11px">{feed}</div>
        <svg width="56" height="24" viewBox="0 0 56 24" style="flex-shrink:0"><path d="M2 12h46M40 5l9 7-9 7" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex-shrink:0;text-align:center">
          <svg width="210" height="210" viewBox="0 0 210 210">
            <defs><radialGradient id="lk" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
            <filter id="lg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
            <g filter="url(#lg)"><circle cx="105" cy="98" r="82" fill="url(#lk)"/></g>
            {"".join(f'<path d="M{105-38+i*6} {70+ (i%3)*4} q19 {26-(i%2)*10} 0 {56}" fill="none" stroke="rgba(26,15,10,.42)" stroke-width="2.4" stroke-linecap="round"/>' for i in range(13))}
            <g transform="translate(88,84)"><rect x="0" y="20" width="34" height="26" rx="6" fill="#1a0f0a"/><path d="M6 20 V13 a11 11 0 0 1 22 0 v7" fill="none" stroke="#1a0f0a" stroke-width="4.5"/></g>
            <text x="105" y="204" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#FAFAF7">100% voice</text>
          </svg>
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({ACC});margin-top:2px">LOCKED</div>
        </div>
      </div>
      {cap("five best posts in, voice locked, every draft comes out yours.")}</div>'''

# 4. DIR3 - three hook shapes, one crowned the winner (dark)
def dir3():
    hooks=[("CONFESSION",'<circle cx="12" cy="8" r="4"/><path d="M5 21v-2a7 7 0 0 1 14 0v2"/>',"I told Claude to write 200 emails. Seven converted.",False),
           ("NUMBER",'<path d="M9 4v16M15 4v16M4 9h16M4 15h16"/>',"847 accounts in. It picked the 12 that closed.",True),
           ("ENEMY",'<path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/>',"Your funnel is not broken. Your targeting is.",False)]
    cards=""
    for nm,ic,line,win in hooks:
        bd=f"rgb({ACC})" if win else "rgba(255,255,255,.10)"
        bg="linear-gradient(160deg,#3a352e,#241f1a)" if win else "linear-gradient(160deg,#2c2926,#201d1a)"
        glow="box-shadow:0 24px 40px rgba(0,0,0,.5),0 0 34px rgba(212,162,127,.22);" if win else "box-shadow:0 20px 34px rgba(0,0,0,.45);"
        ribbon=(f'<div style="position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:12px;letter-spacing:.08em;padding:5px 16px;border-radius:999px;box-shadow:0 8px 16px rgba(212,162,127,.4)">PICKED</div>') if win else ""
        cards+=(f'<div style="flex:1;position:relative;background:{bg};border:1.5px solid {bd};border-radius:20px;padding:24px 20px 20px;{glow}display:flex;flex-direction:column">{ribbon}'
          f'<div style="width:46px;height:46px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;margin-bottom:14px"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ic}</svg></div>'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:10px">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:{800 if win else 600};font-size:19px;color:{"#FAFAF7" if win else "#b8b2a6"};line-height:1.3">"{line}"</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("Demand hooks in three shapes","PICK THE WINNER")}
      <div style="display:flex;gap:16px;align-items:stretch;margin-top:6px">{cards}</div>
      {cap("three angles generated, the strongest chosen: never accept the first line.")}</div>'''

# 5. DIR4 - IVORY: one idea fans into five formats (bezier fan-out)
def dir4():
    outs=[("Post","280 words"),("Carousel","8 slides"),("Reel script","35 seconds"),("Caption","first-comment kit"),("Newsletter","1 section")]
    W,H=760,440
    ix,iy=70,H//2
    edges=""; chips=""
    n=len(outs)
    for i,(nm,sub) in enumerate(outs):
        y=52+i*(H-104)/(n-1)
        mx=(ix+560)/2
        edges+=f'<path d="M{ix+52} {iy} C{mx:.0f} {iy},{mx:.0f} {y:.0f},560 {y:.0f}" fill="none" stroke="rgba(150,90,45,.4)" stroke-width="2.5"/>'
        chips+=(f'<div style="position:absolute;left:560px;top:{y-30:.0f}px;width:200px;background:rgba(255,255,255,.62);border:1.5px solid rgba(150,90,45,.28);border-radius:14px;padding:11px 16px;box-shadow:0 12px 22px rgba(120,95,60,.14)">'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#2a2016">{nm}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:#96562d;margin-top:2px">{sub}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle("One idea in, five formats out.","MULTIPLY","#2a2016",IVA)}
      <div style="position:relative;height:{H}px">
        <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="idea" cx="36%" cy="30%"><stop offset="0%" stop-color="#c98a5c"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="ig" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="14" flood-color="rgba(150,90,45,.4)"/></filter></defs>
          {edges}
          <g filter="url(#ig)"><circle cx="{ix}" cy="{iy}" r="52" fill="url(#idea)"/></g>
          <text x="{ix}" y="{iy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#fdfbf6">1</text>
          <text x="{ix}" y="{iy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#f0e2cf">idea</text>
        </svg>
        {chips}
      </div>
      {cap("one direction, five drafts: the multiplication is free.","#8a745a")}</div>'''

# 6. DIR5 - a scoring rubric with threshold bars, ranked before you look (dark)
def dir5():
    rules=[("Scroll-stop hook","first 2 lines",80),("Save-worthy asset","a map or system",85),("Brand + hierarchy","no dead space",90),("Real numbers, named tools","zero vague claims",85)]
    rows=""
    for nm,sub,thr in rules:
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;padding:15px 0;border-top:1px solid rgba(255,255,255,.07)">'
          f'<div style="width:300px;flex-shrink:0"><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{nm}</div><div style="font-family:DM Sans;font-size:14px;color:#8f8f85">{sub}</div></div>'
          f'<div style="flex:1;height:14px;background:rgba(250,250,247,.06);border-radius:7px;overflow:hidden"><div style="width:{thr}%;height:100%;background:linear-gradient(90deg,#9a5a35,rgb({ACC}));border-radius:7px"></div></div>'
          f'<div style="flex-shrink:0;font-family:DM Mono;font-weight:500;font-size:16px;color:rgb({ACC});width:74px;text-align:right">&ge; {thr}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Set the bar before the draft","PASS RULES")}
      <div style="background:linear-gradient(160deg,#242119,#1b1815);border:1px solid rgba(255,255,255,.07);border-radius:20px;padding:8px 26px 20px;box-shadow:inset 0 2px 3px rgba(255,255,255,.05)">
        <div style="display:flex;align-items:baseline;justify-content:space-between;padding:16px 0 4px">
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#8f8f85">CRITERION IN THE INSTRUCTIONS</span>
          <span style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#8f8f85">MIN /100</span></div>
        {rows}
      </div>
      {cap("your scoring rules ship with the brief, so ranking happens before you look.")}</div>'''

# 7. BURNOUT - a five-week posting grid (consistency) over a planned->sent queue lane (dark)
def burnout():
    import random
    random.seed(7)
    grid=""
    days=["M","T","W","T","F","S","S"]
    hdr="".join(f'<div style="font-family:DM Mono;font-size:12px;color:#8f8f85;text-align:center;width:44px">{d}</div>' for d in days)
    weeks=5
    for w in range(weeks):
        cells=""
        for d in range(7):
            posted=(d<5) or (w in (1,3) and d==5)
            if posted:
                op=0.35+0.14*((w+d)%5)
                cells+=f'<div style="width:44px;height:44px;border-radius:10px;background:rgba(212,162,127,{op:.2f});border:1px solid rgba(212,162,127,.3)"></div>'
            else:
                cells+='<div style="width:44px;height:44px;border-radius:10px;background:rgba(250,250,247,.04);border:1px solid rgba(255,255,255,.06)"></div>'
        grid+=f'<div style="display:flex;gap:8px">{cells}</div>'
    lane=[("PLANNED","20 slots"),("DRAFTED","20 queued"),("GATED","your review"),("SENT","10:30 daily")]
    steps=""
    for i,(nm,sub) in enumerate(lane):
        steps+=(f'<div style="flex:1;background:linear-gradient(160deg,#332f2a,#221f1b);border:1px solid rgba(255,255,255,.09);border-radius:13px;padding:13px 14px;text-align:center">'
          f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.10em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:15px;color:#e2dccf;margin-top:3px">{sub}</div></div>')
        if i<len(lane)-1:
            steps+=f'<svg width="26" height="20" viewBox="0 0 26 20" style="flex-shrink:0;align-self:center"><path d="M2 10h18M15 4l7 6-7 6" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;flex-direction:column">
      {htitle("Consistency is a system","NOT A MOOD")}
      <div style="display:flex;gap:34px;align-items:center;margin:6px 0 4px">
        <div style="flex-shrink:0">
          <div style="display:flex;gap:8px;margin-bottom:8px;padding-left:0">{hdr}</div>
          <div style="display:flex;flex-direction:column;gap:8px">{grid}</div>
        </div>
        <div style="flex:1">
          <div style="font-family:DM Sans;font-weight:900;font-size:48px;color:rgb({ACC});line-height:1">27</div>
          <div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#e2dccf;margin-top:2px">posts, five weeks</div>
          <div style="font-family:DM Sans;font-size:16px;color:#8f8f85;margin-top:10px;line-height:1.4">no gaps, no rush nights: the queue shows up when you do not feel like it.</div>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:8px;margin-top:22px">{steps}</div>
      {cap("planned slots, drafted queues, gated sends: showing up became automatic.")}</div>'''

# 8. SHIFT9 - closing: same model, two outputs, direction is the whole gap (dark)
def shift9():
    return f'''<div style="width:900px;{CARD};padding:38px 44px 40px;text-align:center">
      {htitle("Stop prompting harder","SAME MODEL")}
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:70px;height:340px;margin:10px 0 6px">
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%">
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#8f8f85">average</div>
          <div style="width:150px;height:96px;margin-top:14px;border-radius:18px 18px 6px 6px;background:linear-gradient(180deg,#3a352e,#242019);border:1px solid rgba(255,255,255,.08);box-shadow:0 20px 34px rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;font-family:DM Mono;font-size:13px;color:#8f8f85">PROMPTED</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%">
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">yours</div>
          <div style="width:150px;height:270px;margin-top:14px;border-radius:18px 18px 6px 6px;background:linear-gradient(180deg,#e6b48f,rgb({ACC}) 60%,#8a4c2c);box-shadow:0 26px 46px rgba(212,162,127,.32),inset 0 2px 3px rgba(255,255,255,.4);display:flex;align-items:flex-end;justify-content:center;padding-bottom:18px;font-family:DM Sans;font-weight:900;font-size:15px;color:#1a0f0a">DIRECTED</div>
        </div>
      </div>
      <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#FAFAF7;line-height:1.15">Same model. Same cents.<br>Direction is the whole gap.</div>
      {cap("not a bigger model, a better brief: start directing better.","#c9a583")}</div>'''

PANELS={"mist10":mist10(),"dir1":dir1(),"dir2":dir2(),"dir3":dir3(),
        "dir4":dir4(),"dir5":dir5(),"burnout":burnout(),"shift9":shift9()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/direction"; os.makedirs(outd,exist_ok=True)
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
