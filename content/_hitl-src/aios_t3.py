#!/usr/bin/env python3
# TIER 3 - THE AI OPERATING SYSTEM. 8 bespoke forms, each distinct, none a repeat of eyes.
# forms: perspective prompt-stack / memory dossier / 9->1 convergence / night clock-dial /
#        say-once store / throughput bar / armed toggle / compound curve.
import importlib.util
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="204,120,92"
def head(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')

# 1. AMNESIA - perspective stack of identical "who are you?" prompts receding, a big x40 tally
def amnesia():
    layers=""
    for i in range(5):
        o=1-i*0.19; sc=1-i*0.05; ty=i*-14
        layers+=(f'<div style="position:absolute;left:50%;top:{60+i*30}px;transform:translateX(-50%) scale({sc});'
          f'width:560px;opacity:{o:.2f};background:linear-gradient(160deg,#33302b,#211e1b);border:1px solid rgba(255,255,255,.08);'
          f'border-radius:16px;padding:20px 26px;box-shadow:0 18px 30px rgba(0,0,0,.5)">'
          f'<div style="font-family:\'DM Mono\';font-size:13px;color:rgb({ACC});letter-spacing:.1em;margin-bottom:6px">SESSION {40-i}</div>'
          f'<div style="font-family:\'DM Sans\';font-weight:700;font-size:24px;color:#e9e3d7">"And who are you again?"</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {head("Re-introducing yourself, daily","MEMORY: OFF")}
      <div style="position:relative;height:430px">
        {layers}
        <div style="position:absolute;right:6px;bottom:0;text-align:right">
          <div style="font-family:'DM Sans';font-weight:900;font-size:96px;color:rgb({ACC});line-height:.9">40<span style="font-size:44px">×</span></div>
          <div style="font-family:'DM Mono';font-size:14px;color:{MUT};letter-spacing:.08em">same intro, this week</div></div>
      </div></div>'''

# 2. BRAIN - memory dossier: a profile with a glowing NO-LIST column
def brain():
    likes=["Ships Fridays","Cents, not seats","Operator voice","US/UK founders"]
    nos=["No em dashes","No hard sell","No meetings pre-noon","Never send unread"]
    L="".join(f'<div style="display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span style="width:7px;height:7px;border-radius:50%;background:{DIM}"></span><span style="font-family:DM Sans;font-size:17px;color:#cfc9bd">{x}</span></div>' for x in likes)
    N="".join(f'<div style="display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid rgba(204,120,92,.16)"><span style="font-family:DM Sans;font-weight:900;font-size:16px;color:rgb({ACC})">✕</span><span style="font-family:DM Sans;font-size:17px;color:#e9e3d7">{x}</span></div>' for x in nos)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {head("It knows my no-list cold","OPERATOR PROFILE")}
      <div style="display:flex;gap:26px">
        <div style="flex:1">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:{MUT};margin-bottom:8px">PREFERS</div>{L}</div>
        <div style="flex:1;background:linear-gradient(160deg,rgba(204,120,92,.14),rgba(204,120,92,.04));border:1px solid rgba(204,120,92,.30);border-radius:18px;padding:18px 20px;box-shadow:inset 0 2px 3px rgba(255,255,255,.06)">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:8px">THE NO-LIST</div>{N}</div>
      </div></div>'''

# 3. COMMAND - nine dim tabs converge into one glowing dashboard
def command():
    tabs=""
    names=["CRM","Mail","Docs","Calendar","Notion","Slack","Sheets","Drive","Analytics"]
    for i,nm in enumerate(names):
        r,c=divmod(i,1); y=i*44
        tabs+=(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;opacity:.4">'
          f'<span style="font-family:DM Mono;font-size:14px;color:{MUT};text-decoration:line-through;width:150px">{nm}</span>'
          f'<div style="flex:1;height:2px;background:linear-gradient(90deg,{DIM},transparent)"></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {head("Nine tabs died. One screen lived.","CONSOLIDATED")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="width:210px">{tabs}</div>
        <svg width="70" height="60" viewBox="0 0 70 60"><path d="M4 30 H52 M40 16 L56 30 L40 44" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex:1;background:linear-gradient(160deg,#302c27,#201d19);border:1.5px solid rgba(204,120,92,.4);border-radius:18px;padding:20px;box-shadow:0 30px 50px rgba(0,0,0,.55),0 0 60px rgba(204,120,92,.12)">
          <div style="display:flex;gap:6px;margin-bottom:14px"><span style="width:11px;height:11px;border-radius:50%;background:#d9694a"></span><span style="width:11px;height:11px;border-radius:50%;background:#caa24a"></span><span style="width:11px;height:11px;border-radius:50%;background:#6f9e6a"></span></div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#FAFAF7">One command deck</div>
          <div style="font-family:'DM Sans';font-size:17px;color:{MUT};margin-top:4px;margin-bottom:16px">every tool, one surface, your gate</div>
          {"".join(f'<div style="height:14px;border-radius:7px;background:rgba(204,120,92,{0.5-i*0.12});margin-bottom:9px;width:{100-i*16}%"></div>' for i in range(3))}
        </div>
      </div></div>'''

# 4. ALWAYS - night clock dial: task closed at 3am, found at 7am
def always():
    import math
    cx,cy,R=180,180,150
    ticks=""
    for h in range(12):
        a=math.radians(h*30-90); x1=cx+(R-14)*math.cos(a); y1=cy+(R-14)*math.sin(a); x2=cx+R*math.cos(a); y2=cy+R*math.sin(a)
        ticks+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(250,250,247,.22)" stroke-width="2"/>'
    def mark(h,col,glow):
        a=math.radians(h*30-90); x=cx+(R-40)*math.cos(a); y=cy+(R-40)*math.sin(a)
        return f'<circle cx="{x:.0f}" cy="{y:.0f}" r="10" fill="{col}" filter="url(#g)"/>' if glow else f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="none" stroke="{col}" stroke-width="3"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px;display:flex;align-items:center;gap:40px">
      <svg width="360" height="360" viewBox="0 0 360 360">
        <defs><radialGradient id="night" cx="50%" cy="45%"><stop offset="0%" stop-color="#26241f"/><stop offset="100%" stop-color="#171512"/></radialGradient>
        <filter id="g" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#night)" stroke="rgba(255,255,255,.08)"/>
        {ticks}
        <path d="M{cx} {cy} L{cx+R*math.cos(math.radians(-90)):.0f} {cy+R*math.sin(math.radians(-90)):.0f} A{R} {R} 0 0 1 {cx+R*math.cos(math.radians(120)):.0f} {cy+R*math.sin(math.radians(120)):.0f} Z" fill="rgba(60,70,110,.14)"/>
        {mark(3,f"rgb({ACC})",True)}{mark(7,"#e9e3d7",False)}
        <circle cx="{cx}" cy="{cy}" r="6" fill="rgb({ACC})"/>
        <text x="{cx}" y="{cy+70}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="{MUT}" letter-spacing="2">NIGHT SHIFT</text>
      </svg>
      <div>
        <div style="display:flex;align-items:baseline;gap:12px;margin-bottom:6px"><span style="font-family:'DM Sans';font-weight:900;font-size:40px;color:rgb({ACC})">03:00</span><span style="font-family:DM Sans;font-size:19px;color:#cfc9bd">it closed a task</span></div>
        <div style="display:flex;align-items:baseline;gap:12px;margin-bottom:22px"><span style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#FAFAF7">07:00</span><span style="font-family:DM Sans;font-size:19px;color:{MUT}">you found out</span></div>
        <div style="font-family:'DM Mono';font-size:15px;color:{MUT};line-height:1.5">the work moved<br>while you slept</div>
      </div></div>'''

# 5. RULES - say it once, stored forever
def rules():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 44px">
      {head("Say it once","PERSISTENT")}
      <div style="display:flex;align-items:center;gap:26px;margin-top:10px">
        <div style="flex:1;background:linear-gradient(160deg,#302c27,#201d19);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px 22px">
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.14em;color:{MUT};margin-bottom:8px">YOU, ONCE</div>
          <div style="font-family:'DM Sans';font-weight:600;font-size:21px;color:#e9e3d7;line-height:1.35">"Never send an email I have not seen."</div></div>
        <svg width="64" height="40" viewBox="0 0 64 40"><path d="M4 20 H46 M36 8 L52 20 L36 32" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex-shrink:0;width:230px;text-align:center;background:linear-gradient(160deg,rgba(204,120,92,.16),rgba(204,120,92,.05));border:1px solid rgba(204,120,92,.34);border-radius:18px;padding:24px 18px;box-shadow:0 0 44px rgba(204,120,92,.14),inset 0 2px 3px rgba(255,255,255,.08)">
          <svg width="40" height="40" viewBox="0 0 24 24" style="margin-bottom:8px"><path d="M6 11 V8 a6 6 0 0 1 12 0 v3" fill="none" stroke="rgb({ACC})" stroke-width="2"/><rect x="4" y="11" width="16" height="10" rx="2.5" fill="none" stroke="rgb({ACC})" stroke-width="2"/></svg>
          <div style="font-family:'DM Sans';font-weight:900;font-size:22px;color:#FAFAF7">Held forever</div>
          <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC});margin-top:4px">every session, every agent</div></div>
      </div>
      <div style="font-family:'DM Mono';font-size:14px;color:{MUT};margin-top:22px;text-align:center">no re-explaining, no drift: the memory is the whole trick</div></div>'''

# 6. PROOF - throughput bar packed with ticks, big count, coffee-still-hot chip (NOT a dot field)
def proof():
    ticks="".join(f'<rect x="{i*8.4:.1f}" y="0" width="4" height="{18 if i%10 else 34}" rx="2" fill="rgba(204,120,92,{0.85 if i%10==0 else 0.4})"/>' for i in range(100))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 44px">
      {head("Read before the coffee cooled","THROUGHPUT")}
      <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:8px">
        <div><span style="font-family:'DM Sans';font-weight:900;font-size:76px;color:#FAFAF7;line-height:.9">1,284</span>
        <span style="font-family:'DM Sans';font-weight:700;font-size:22px;color:rgb({ACC});margin-left:12px">companies, read live</span></div>
      </div>
      <div style="background:#1a1815;border:1px solid rgba(255,255,255,.06);border-radius:14px;padding:20px 22px;margin-top:14px">
        <svg width="840" height="34" viewBox="0 0 840 34" style="width:100%">{ticks}</svg></div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:20px">
        <div style="display:flex;align-items:center;gap:10px;background:rgba(204,120,92,.10);border:1px solid rgba(204,120,92,.28);border-radius:999px;padding:10px 18px">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2" stroke-linecap="round"><path d="M18 8h1a3 3 0 0 1 0 6h-1"/><path d="M3 8h15v5a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5Z"/><path d="M6 2v2M10 2v2M14 2v2"/></svg>
          <span style="font-family:'DM Sans';font-weight:700;font-size:17px;color:#e9e3d7">coffee still hot</span></div>
        <span style="font-family:'DM Mono';font-size:15px;color:{MUT}">hiring · funding · stack moves, all cited</span></div></div>'''

# 7. GATE - an armed hardware toggle: capability behind it, waiting for your tap (distinct from eyes gate)
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 44px">
      {head("Can do anything. Does nothing alone.","ARMED · WAITING")}
      <div style="display:flex;align-items:center;gap:40px;margin-top:8px">
        <div style="flex:1">
          {"".join(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;opacity:.6"><span style="width:8px;height:8px;border-radius:50%;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:18px;color:#cfc9bd">{x}</span></div>' for x in ["send 240 emails","move the pipeline","publish the deck","close the month"])}
          <div style="font-family:'DM Mono';font-size:14px;color:{MUT};margin-top:8px">all capable · all held</div>
        </div>
        <div style="flex-shrink:0;width:250px;display:flex;flex-direction:column;align-items:center">
          <div style="width:150px;height:250px;border-radius:80px;background:linear-gradient(160deg,#2a2723,#171512);border:2px solid rgba(204,120,92,.4);box-shadow:0 26px 46px rgba(0,0,0,.55),inset 0 3px 6px rgba(255,255,255,.08),inset 0 -10px 22px rgba(0,0,0,.5);position:relative">
            <div style="position:absolute;left:50%;bottom:16px;transform:translateX(-50%);width:118px;height:118px;border-radius:50%;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 60%,#8a4a2c);box-shadow:0 12px 24px rgba(0,0,0,.5),0 0 40px rgba(204,120,92,.4),inset 0 3px 4px rgba(255,255,255,.5)"></div>
            <div style="position:absolute;left:0;right:0;top:20px;text-align:center;font-family:'DM Mono';font-size:14px;letter-spacing:.16em;color:rgb({ACC})">YOUR TAP</div>
          </div>
          <div style="font-family:'DM Sans';font-weight:800;font-size:19px;color:#FAFAF7;margin-top:16px">nothing sends alone</div>
        </div>
      </div></div>'''

# 8. OWN - compound curve vs renter's daily reset sawtooth
def own():
    import math
    W,H=760,300; pad=30
    # renter sawtooth (resets), owner compound
    saw=""
    for i in range(7):
        x0=pad+i*100; saw+=f'M{x0} {H-pad} L{x0+70} {H-pad-46} '
    comp="M"+" L".join(f"{pad+i*(W-2*pad)/40:.0f} {H-pad-(1.7**(i/6))*8:.0f}" for i in range(41))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {head("Renters restart. Owners compound.","30 DAYS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="width:100%">
        <defs><linearGradient id="cf" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(204,120,92,.34)"/><stop offset="100%" stop-color="rgba(204,120,92,0)"/></linearGradient></defs>
        <line x1="{pad}" y1="{H-pad}" x2="{W-pad}" y2="{H-pad}" stroke="rgba(255,255,255,.12)"/>
        <path d="{saw}" fill="none" stroke="{DIM}" stroke-width="3" stroke-dasharray="2 6"/>
        <path d="{comp} L{W-pad} {H-pad} L{pad} {H-pad} Z" fill="url(#cf)"/>
        <path d="{comp}" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>
        <circle cx="{W-pad}" cy="{H-pad-(1.7**(40/6))*8:.0f}" r="8" fill="rgb({ACC})"/>
      </svg>
      <div style="display:flex;gap:30px;margin-top:6px">
        <div style="display:flex;align-items:center;gap:9px"><span style="width:22px;height:3px;background:{DIM}"></span><span style="font-family:DM Sans;font-size:16px;color:{MUT}">Renter: restarts every day</span></div>
        <div style="display:flex;align-items:center;gap:9px"><span style="width:22px;height:3px;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:16px;color:#e9e3d7">Owner: memory compounds</span></div>
      </div></div>'''

PANELS={"amnesia":amnesia(),"brain":brain(),"command":command(),"always":always(),
        "rules":rules(),"proof":proof(),"gate":gate(),"own":own()}
if __name__=="__main__":
    print("aios t3:"); B.render("aios",PANELS)
