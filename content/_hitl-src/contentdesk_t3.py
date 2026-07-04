#!/usr/bin/env python3
# TIER 3 - THE 500K CONTENT DESK. forms: week planner / hook scoring / voice signature sample /
# repurpose fan 1->5 / deliverability meter / async roster / publish-thumb gate / cost comparison.
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="200,70,35"
def head(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')

# 1. week planner auto-filled
def cal():
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    slots=[["Post","Reel"],["Carousel"],["Post","Story"],["Thread"],["Reel","Post"],["Newsletter"],["Teardown"]]
    cols=""
    for d,ss in zip(days,slots):
        chips="".join(f'<div style="background:{"rgba(200,70,35,.16)" if d=="MON" else "#2c2925"};border:1px solid {"rgba(200,70,35,.34)" if d=="MON" else "rgba(255,255,255,.06)"};border-radius:8px;padding:8px 6px;font-family:DM Sans;font-size:13px;color:{"#f0d8ce" if d=="MON" else "#cfc9bd"};text-align:center;margin-bottom:6px">{s}</div>' for s in ss)
        cols+=f'<div style="flex:1"><div style="font-family:DM Mono;font-size:12px;color:{MUT};text-align:center;margin-bottom:8px">{d}</div>{chips}</div>'
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 38px">
      {head("Monday 07:00, the week plans itself","AUTO-PLANNED")}
      <div style="display:flex;gap:10px;align-items:flex-start">{cols}</div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:18px">11 pieces slotted before you open the laptop</div></div>'''

# 2. hook scoring, winner crowned
def hooks():
    hh=[("You are the cron job in your own company.",71),("Nine tools forgot who I was.",64),("Prompts are dead. Loops run.",88)]
    best=max(h[1] for h in hh)
    rows=""
    for txt,sc in hh:
        on=sc==best
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:{800 if on else 600};font-size:18px;color:{"#FAFAF7" if on else "#bdb7ab"}">"{txt}"</div>'
          f'<div style="height:6px;border-radius:3px;background:#2c2925;margin-top:8px;overflow:hidden"><div style="height:100%;width:{sc}%;background:{f"rgb({ACC})" if on else DIM};border-radius:3px"></div></div></div>'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:26px;color:{f"rgb({ACC})" if on else MUT};width:52px;text-align:right">{sc}</span>'
          f'<span style="width:74px;font-family:DM Mono;font-size:12px;color:rgb({ACC})">{"&#9664; crowned" if on else ""}</span></div>')
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 38px">
      {head("Three hooks fight. One wins.","SCORED")}{rows}</div>'''

# 3. voice: signature sample with your phrases underlined
def voice():
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 42px">
      {head("It writes like your best day","VOICE LOCKED")}
      <div style="background:#191614;border-left:3px solid rgb({ACC});border-radius:10px;padding:20px 22px;font-family:DM Sans;font-size:21px;line-height:1.5;color:#e9e3d7">
        <span style="border-bottom:2px solid rgb({ACC})">I killed nine tools</span> last month. The one I kept <span style="border-bottom:2px solid rgb({ACC})">did not have a chat box</span>. Renters restart. <span style="border-bottom:2px solid rgb({ACC})">Owners compound</span>.</div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:18px">
        <div style="display:flex;align-items:center;gap:9px;background:rgba(200,70,35,.10);border:1px solid rgba(200,70,35,.3);border-radius:999px;padding:9px 16px">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><path d="M6 11V8a6 6 0 0 1 12 0v3"/><rect x="4" y="11" width="16" height="10" rx="2.5"/></svg>
          <span style="font-family:DM Sans;font-weight:700;font-size:15px;color:#e9e3d7">your voice, locked</span></div>
        <span style="font-family:DM Mono;font-size:14px;color:{MUT}">your cadence, your phrases, no house style</span></div></div>'''

# 4. repurpose fan 1 -> 5 native channels
def repurpose():
    chans=["LinkedIn","TikTok","Instagram","X","Newsletter"]; cx,cy=130,180; import math
    lines=""; nodes=""
    for i,c in enumerate(chans):
        y=40+i*72;
        lines+=f'<path d="M{cx+40} {cy} C 300 {cy}, 360 {y}, 470 {y}" fill="none" stroke="rgba(200,70,35,.4)" stroke-width="2.5"/>'
        nodes+=f'<g transform="translate(470,{y})"><rect x="0" y="-24" width="230" height="48" rx="12" fill="#2a2723" stroke="rgba(255,255,255,.08)"/><text x="20" y="6" font-family="DM Sans" font-weight="700" font-size="18" fill="#e9e3d7">{c}</text><text x="210" y="6" text-anchor="end" font-family="DM Mono" font-size="12" fill="rgb({ACC})">native</text></g>'
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 38px">
      {head("One brief. Five channels.","REPURPOSE")}
      <svg width="740" height="400" viewBox="0 0 740 400" style="width:100%">
        {lines}
        <g><circle cx="{cx}" cy="{cy}" r="52" fill="rgb({ACC})"/><text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a0f08">1</text><text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a1810">brief</text></g>
        {nodes}
      </svg></div>'''

# 5. deliverability meter 99.2%
def inbox():
    pct=99.2; import math
    r=100; circ=math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px;display:flex;align-items:center;gap:40px">
      <svg width="260" height="170" viewBox="0 0 260 170">
        <path d="M30 150 A100 100 0 0 1 230 150" fill="none" stroke="#2c2925" stroke-width="20" stroke-linecap="round"/>
        <path d="M30 150 A100 100 0 0 1 230 150" fill="none" stroke="rgb({ACC})" stroke-width="20" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}"/>
        <text x="130" y="130" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="52" fill="#FAFAF7">{pct}%</text>
        <text x="130" y="158" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})">INBOXED</text></svg>
      <div style="flex:1">
        <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;line-height:1.1">Seen, not spammed</div>
        <div style="font-family:DM Sans;font-size:19px;color:{MUT};margin-top:10px;line-height:1.4">warmed, paced, verified sending: your content lands where it is read.</div>
        <div style="font-family:DM Mono;font-size:14px;color:rgb({ACC});margin-top:16px">unseen content is just rent</div></div></div>'''

# 6. async roster - a team that never meets
def desk():
    roles=[("Planner","slots the week"),("Hook smith","scores openers"),("Ghostwriter","your voice"),("Repurposer","5 channels"),("Sender","warmed inbox")]
    rows=""
    for nm,role in roles:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
          f'<span style="width:11px;height:11px;border-radius:50%;background:#7fd39a;box-shadow:0 0 12px rgba(127,211,154,.7)"></span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:19px;color:#e9e3d7">{nm}</span>'
          f'<span style="font-family:DM Sans;font-size:15px;color:{MUT};margin-right:14px">{role}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;color:#7fd39a;letter-spacing:.1em">RUNNING</span></div>')
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 36px">
      {head("The desk never meets","5 SKILLS · 0 STANDUPS")}{rows}
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:14px">all async, all in your voice, none of them in a meeting</div></div>'''

# 7. publish gate: post held for your thumb
def gate():
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 42px">
      {head("My feed, my thumb","HELD TO PUBLISH")}
      <div style="display:flex;align-items:center;gap:26px;margin-top:6px">
        <div style="flex:1;background:#191614;border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:18px 20px">
          <div style="display:flex;gap:8px;align-items:center;margin-bottom:12px"><div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(160deg,#e08a5a,rgb({ACC}))"></div><span style="font-family:DM Sans;font-weight:700;font-size:16px;color:#e9e3d7">@tiberiu.ai</span><span style="font-family:DM Mono;font-size:12px;color:{MUT};margin-left:auto">scheduled 10:00</span></div>
          <div style="font-family:DM Sans;font-size:17px;color:#cfc9bd;line-height:1.4">"I killed nine tools last month. The one I kept had no chat box..."</div>
          <div style="height:10px;border-radius:6px;background:#2c2925;margin-top:14px"></div></div>
        <div style="flex-shrink:0;text-align:center">
          <div style="width:100px;height:100px;border-radius:50%;background:linear-gradient(160deg,rgba(200,70,35,.18),rgba(200,70,35,.05));border:2px solid rgba(200,70,35,.4);display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(200,70,35,.18)">
            <svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="1.7"><path d="M9 11V6a2 2 0 0 1 4 0v5 M13 11V4a2 2 0 0 1 4 0v9 a6 6 0 0 1-6 6 h-1 a5 5 0 0 1-4-2 l-3-4 a2 2 0 0 1 3-2 l2 2"/></svg></div>
          <div style="font-family:DM Sans;font-weight:800;font-size:17px;color:#FAFAF7;margin-top:10px">your thumb</div>
          <div style="font-family:DM Mono;font-size:12px;color:{MUT}">nothing posts alone</div></div>
      </div></div>'''

# 8. cost comparison: agency retainer vs cents
def math_():
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px">
      {head("Bills in cents, not Mondays","THE MATH")}
      <div style="display:flex;align-items:flex-end;gap:50px;height:250px;padding:0 30px">
        <div style="flex:1;text-align:center;display:flex;flex-direction:column;justify-content:flex-end;height:100%">
          <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:{DIM}">$6,000</div>
          <div style="width:100%;background:linear-gradient(180deg,#4a423c,#33302b);border-radius:12px 12px 0 0;height:200px;margin-top:10px;border:1px solid rgba(255,255,255,.06)"></div>
          <div style="font-family:DM Sans;font-size:16px;color:{MUT};margin-top:10px">content agency / mo</div></div>
        <div style="flex:1;text-align:center;display:flex;flex-direction:column;justify-content:flex-end;height:100%">
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:rgb({ACC})">40¢</div>
          <div style="width:100%;background:linear-gradient(180deg,#e08a5a,rgb({ACC}));border-radius:12px 12px 0 0;height:22px;margin-top:10px;box-shadow:0 0 30px rgba(200,70,35,.3)"></div>
          <div style="font-family:DM Sans;font-size:16px;color:#e9e3d7;margin-top:10px">the desk / mo</div></div>
      </div></div>'''

PANELS={"cal":cal(),"hooks":hooks(),"voice":voice(),"repurpose":repurpose(),
        "inbox":inbox(),"desk":desk(),"gate":gate(),"math":math_()}
if __name__=="__main__":
    print("contentdesk t3:"); B.render("contentdesk",PANELS)
