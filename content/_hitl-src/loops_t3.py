#!/usr/bin/env python3
# TIER 3 - PROMPTS ARE DEAD, LOOPS RUN. forms: crontab(you) / loop-ring / define-card /
# trigger-timeline / self-grade scorecard / runaway budget drain / handbrake barrier / hours-vs-systems.
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="200,70,35"
def head(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')

# real stat strip pinned at the panel bottom -> fills the working band with dense data (aspect ~1.2),
# NOT stretched empty space (operator rule #14 / §27.9). 3 chips of real numbers per panel.
def foot(items):
    chips="".join(f'<div style="flex:1;text-align:center;padding:20px 8px;background:#191614;'
      f'border:1px solid rgba(255,255,255,.06);border-radius:14px">'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC});line-height:1">{b}</div>'
      f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:{MUT};margin-top:8px">{s}</div></div>'
      for b,s in items)
    return f'<div style="display:flex;gap:14px;margin-top:26px">{chips}</div>'

# 1. OLDWAY - crontab where the RUNNER column is YOU on every line
def oldway():
    rows=[("07:00","pull overnight leads"),("09:00","send 12 follow-ups"),("12:00","repurpose the post"),
          ("15:00","chase 3 replies"),("18:00","update the tracker"),("22:00","queue tomorrow")]
    tr="".join(f'<div style="display:grid;grid-template-columns:96px 1fr 96px;gap:12px;align-items:center;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
       f'<span style="font-family:DM Mono;font-size:16px;color:{MUT}">{tm}</span>'
       f'<span style="font-family:DM Sans;font-size:18px;color:#d7d1c6">{tk}</span>'
       f'<span style="font-family:DM Mono;font-weight:500;font-size:15px;color:rgb({ACC});text-align:right">YOU</span></div>' for tm,tk in rows)
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 38px">
      {head("Your personal crontab","RUNNER: HUMAN")}
      <div style="display:grid;grid-template-columns:96px 1fr 96px;gap:12px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,.12)">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{DIM}">WHEN</span>
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{DIM}">JOB</span>
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{DIM};text-align:right">RUNNER</span></div>
      {tr}
      {foot([("6","JOBS / DAY"),("6h","YOUR HANDS ON"),("0","ON AUTOPILOT")])}</div>'''

# 2. LOOP - a running loop ring (4 steps) with a big cycle counter at the center
def loop():
    cx,cy,R=200,200,150
    steps=[("read",-90),("act",0),("check",90),("log",180)]
    ring=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(200,70,35,.28)" stroke-width="3" stroke-dasharray="6 10"/>'
    arcs=""; nodes=""
    for nm,a in steps:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#2a201c" stroke="rgb({ACC})" stroke-width="2"/>'
                f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#e9ddd6">{nm}</text>')
    # arrowheads along the ring
    for a in (-45,45,135,225):
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a)); ang=a+90
        arcs+=f'<g transform="translate({x:.0f},{y:.0f}) rotate({ang})"><path d="M-7 -6 L7 0 L-7 6" fill="rgb({ACC})"/></g>'
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 38px">
      <div style="display:flex;align-items:center;gap:36px">
      <svg width="400" height="400" viewBox="0 0 400 400">{ring}{arcs}{nodes}
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="66" fill="#FAFAF7">212</text>
        <text x="{cx}" y="{cy+28}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})" letter-spacing="2">CYCLES RUN</text></svg>
      <div>
        <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#FAFAF7;line-height:1.1">3 sentences in.</div>
        <div style="font-family:'DM Sans';font-size:20px;color:{MUT};margin-top:8px;line-height:1.4">212 cycles out.<br>The loop did the rest.</div>
        <div style="display:inline-block;margin-top:20px;background:rgba(200,70,35,.10);border:1px solid rgba(200,70,35,.3);border-radius:10px;padding:10px 16px;font-family:DM Mono;font-size:14px;color:#e9ddd6">input once, runs forever</div>
      </div></div>
      {foot([("212","CYCLES RUN"),("3","SENTENCES IN"),("0","TIMES TYPED")])}</div>'''

# 3. DEFINE - step 1/3: a sentence compiles into a recurring job
def define():
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 42px">
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:22px;color:rgb({ACC})">01</span>
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">Define it once</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:{MUT};margin-left:auto">STEP 1 / 3</span></div>
      <div style="background:#191614;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:18px 22px;font-family:'DM Mono';font-size:19px;color:#e9ddd6">
        <span style="color:rgb({ACC})">&gt;</span> "Every morning, find who replied and draft the follow-ups."</div>
      <div style="display:flex;justify-content:center;margin:16px 0"><svg width="30" height="34" viewBox="0 0 30 34"><path d="M15 4 V26 M6 18 L15 27 L24 18" fill="none" stroke="rgb({ACC})" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div style="background:linear-gradient(160deg,rgba(200,70,35,.14),rgba(200,70,35,.04));border:1px solid rgba(200,70,35,.32);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:16px;box-shadow:0 0 40px rgba(200,70,35,.12)">
        <div style="width:44px;height:44px;border-radius:12px;background:rgba(200,70,35,.18);display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><path d="M12 6v6l4 2"/><circle cx="12" cy="12" r="9"/></svg></div>
        <div><div style="font-family:'DM Sans';font-weight:800;font-size:20px;color:#FAFAF7">follow_up.loop</div>
        <div style="font-family:'DM Mono';font-size:13px;color:rgb({ACC})">compiled · recurring · yours</div></div></div>
      {foot([("1","LINE OF ENGLISH"),("24/7","STAYS ARMED"),("0","REWRITES")])}</div>'''

# 4. TRIGGER - step 2/3: a 7-day timeline with 09:00 firing every day
def trigger():
    days=["M","T","W","T","F","S","S"]; W=760
    cells=""
    for i,dd in enumerate(days):
        x=40+i*(W-80)/7; glow=(i==2)
        dot=(f'<circle cx="42" cy="86" r="16" fill="rgb({ACC})" filter="url(#tg)"/>' if glow
             else f'<circle cx="42" cy="86" r="12" fill="rgb({ACC})" opacity="0.55"/>')
        cells+=(f'<g transform="translate({x:.0f},0)">'
          f'<text x="42" y="30" text-anchor="middle" font-family="DM Mono" font-size="15" fill="{MUT}">{dd}</text>'
          f'{dot}'
          f'<text x="42" y="128" text-anchor="middle" font-family="DM Mono" font-size="13" fill="{DIM}">09:00</text></g>')
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 42px">
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:22px;color:rgb({ACC})">02</span>
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">It fires without you</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:{MUT};margin-left:auto">STEP 2 / 3</span></div>
      <svg width="{W}" height="150" viewBox="0 0 {W} 150" style="width:100%">
        <defs><filter id="tg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <line x1="40" y1="86" x2="{W-40}" y2="86" stroke="rgba(200,70,35,.25)" stroke-width="2" stroke-dasharray="2 8"/>{cells}</svg>
      <div style="font-family:'DM Mono';font-size:15px;color:{MUT};text-align:center;margin-top:6px">same time, every day, laptop open or shut</div>
      {foot([("7/7","DAYS IT FIRED"),("09:00","EVERY DAY"),("0","REMINDERS SET")])}</div>'''

# 5. VERIFY - step 3/3: it grades its own work before you see it
def verify():
    checks=[("Draft matches your voice","PASS"),("Every claim cited","PASS"),("Under 62 words","PASS"),("No banned phrases","PASS")]
    rows="".join(f'<div style="display:flex;align-items:center;gap:14px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
      f'<svg width="24" height="24" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(127,211,154,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#7fd39a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      f'<span style="flex:1;font-family:DM Sans;font-size:18px;color:#d7d1c6">{c}</span>'
      f'<span style="font-family:DM Mono;font-size:13px;color:#7fd39a;letter-spacing:.1em">{s}</span></div>' for c,s in checks)
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px">
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:22px;color:rgb({ACC})">03</span>
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">It grades itself first</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:{MUT};margin-left:auto">STEP 3 / 3</span></div>
      <div style="display:flex;gap:26px;align-items:center">
        <div style="flex:1">{rows}</div>
        <div style="flex-shrink:0;width:150px;height:150px;border-radius:50%;background:conic-gradient(rgb({ACC}) 0 100%,#2a201c 0);display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(200,70,35,.18)">
          <div style="width:118px;height:118px;border-radius:50%;background:#1d1a17;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#FAFAF7">v3</span>
            <span style="font-family:'DM Mono';font-size:12px;color:rgb({ACC})">ready for you</span></div></div>
      </div>
      {foot([("4/4","CHECKS PASSED"),("v3","REDONE UNTIL OK"),("0","YOU EDITED")])}</div>'''

# 6. TRAP - a runaway loop draining a budget meter into the red
def trap():
    seg=""
    for i in range(20):
        col=f"rgb({ACC})" if i>=14 else ("#caa24a" if i>=9 else "#6f9e6a")
        op=1 if i>=14 else 0.4
        seg+=f'<rect x="{i*38}" y="0" width="30" height="54" rx="5" fill="{col}" opacity="{op}"/>'
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px">
      {head("Loops without exits eat budgets","NO EXIT")}
      <div style="display:flex;align-items:center;gap:30px;margin:6px 0 22px">
        <svg width="140" height="90" viewBox="0 0 140 90"><path d="M45 45 a25 25 0 1 1 25 25 a25 25 0 1 1 -25 -25" fill="none" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round"/><path d="M70 20 l8 -8 M70 20 l-2 11" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" fill="none"/></svg>
        <div><div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#FAFAF7">it runs and runs</div>
        <div style="font-family:'DM Sans';font-size:19px;color:{MUT};margin-top:4px">no stop condition, tokens bleed</div></div>
      </div>
      <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:{MUT};margin-bottom:8px">BUDGET</div>
      <svg width="768" height="54" viewBox="0 0 768 54" style="width:100%">{seg}</svg>
      <div style="display:flex;justify-content:space-between;font-family:DM Mono;font-size:13px;color:{DIM};margin-top:8px"><span>$0</span><span style="color:rgb({ACC})">drained</span></div>
      {foot([("$0","LEFT IN BUDGET"),("0","EXITS DEFINED"),("24/7","BLEEDING")])}</div>'''

# 7. GATE - full-speed lane with a handbrake barrier at the exit door
def gate():
    lanes="".join(f'<rect x="{40+i*24}" y="{54+i*0}" width="14" height="8" rx="4" fill="rgba(200,70,35,{0.7-i*0.03})"/>' for i in range(22))
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 42px">
      {head("Full speed inside. Handbrake on the door.","GATED EXIT")}
      <div style="position:relative;background:#191614;border:1px solid rgba(255,255,255,.07);border-radius:16px;padding:26px;overflow:hidden">
        <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:{MUT};margin-bottom:10px">INSIDE THE LOOP: NO LIMITS</div>
        <div style="display:flex;align-items:center;gap:0;height:64px">
          <div style="flex:1;height:6px;background:repeating-linear-gradient(90deg,rgb({ACC}) 0 22px,transparent 22px 40px)"></div>
          <!-- barrier -->
          <div style="flex-shrink:0;width:16px;height:120px;margin-left:8px;background:linear-gradient(160deg,#e08a5a,rgb({ACC}));border-radius:6px;box-shadow:0 0 34px rgba(200,70,35,.4)"></div>
          <div style="flex-shrink:0;width:150px;text-align:center">
            <svg width="46" height="46" viewBox="0 0 24 24" style="margin-bottom:4px"><path d="M6 11 V8 a6 6 0 0 1 12 0 v3" fill="none" stroke="rgb({ACC})" stroke-width="2"/><rect x="4" y="11" width="16" height="10" rx="2.5" fill="none" stroke="rgb({ACC})" stroke-width="2"/></svg>
            <div style="font-family:'DM Sans';font-weight:800;font-size:17px;color:#FAFAF7">your tap</div></div>
        </div>
      </div>
      <div style="font-family:'DM Mono';font-size:14px;color:{MUT};text-align:center;margin-top:18px">it sprints internally, then waits at the door before anything leaves</div>
      {foot([("FULL","SPEED INSIDE"),("1","TAP TO SEND"),("0","LEAK RISK")])}</div>'''

# 8. SCALE - hours flat-capped vs systems multiplying (1,2,4,8 blocks)
def scale():
    def blocks(n):
        return "".join(f'<div style="width:34px;height:34px;border-radius:7px;background:rgb({ACC});opacity:{0.5+0.5*(k+1)/n}"></div>' for k in range(n))
    cols="".join(f'<div style="display:flex;flex-direction:column-reverse;gap:6px;align-items:center"><div style="display:flex;flex-direction:column-reverse;gap:6px">{blocks(n)}</div><span style="font-family:DM Mono;font-size:13px;color:{MUT};margin-top:8px">wk{i+1}</span></div>' for i,n in enumerate([1,2,4,8]))
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px">
      {head("Hours capped. Systems did not.","LEVERAGE")}
      <div style="display:flex;gap:40px;align-items:flex-end">
        <div style="flex-shrink:0">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:{MUT};margin-bottom:12px">YOUR HOURS</div>
          <div style="display:flex;flex-direction:column-reverse;gap:6px">{"".join(f'<div style="width:80px;height:20px;border-radius:6px;background:#3a352f"></div>' for _ in range(2))}</div>
          <div style="font-family:DM Sans;font-size:15px;color:{DIM};margin-top:10px">flat. always 24.</div></div>
        <div style="width:1px;height:180px;background:rgba(255,255,255,.10)"></div>
        <div style="flex:1">
          <div style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:12px">YOUR SYSTEMS</div>
          <div style="display:flex;gap:26px;align-items:flex-end">{cols}</div></div>
      </div>
      {foot([("1-8","IN 4 WEEKS"),("24h","HOURS CAPPED"),("x8","OUTPUT")])}</div>'''

PANELS={"oldway":oldway(),"loop":loop(),"define":define(),"trigger":trigger(),
        "verify":verify(),"trap":trap(),"gate":gate(),"scale":scale()}
if __name__=="__main__":
    print("loops t3:"); B.render("loops",PANELS)
