#!/usr/bin/env python3
# TIER 3 - STUCK AT LEVEL ONE. forms: dead-end wheel / recall card / live job monitor /
# parallel lanes / overnight schedule / level ladder w/ hidden rung / belay clip / quiet summit.
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="204,120,92"
def lv(n,t,tag):
    return (f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:16px">'
      f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC});border:1px solid rgba(204,120,92,.4);border-radius:8px;padding:5px 10px">LVL {n}</span>'
      f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:25px;color:#FAFAF7">{t}</span>'
      f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:{MUT};margin-left:auto">{tag}</span></div>')

# 1. dead-end wheel: ask, copy, close
def floor():
    cx,cy,R=180,180,120
    steps=[("ask",-90),("copy",30),("close",150)]
    nodes=""
    for nm,a in steps:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#2a2622" stroke="{DIM}" stroke-width="2"/>'
                f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="15" fill="#bdb7ab">{nm}</text>')
    arcs="".join(f'<g transform="translate({cx+R*math.cos(math.radians(a)):.0f},{cy+R*math.sin(math.radians(a)):.0f}) rotate({a+90})"><path d="M-6 -5 L6 0 L-6 5" fill="{DIM}"/></g>' for a in (-30,90,210))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px;display:flex;align-items:center;gap:34px">
      <svg width="360" height="360" viewBox="0 0 360 360">
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(255,255,255,.10)" stroke-width="2" stroke-dasharray="4 8"/>{arcs}{nodes}
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="{DIM}">LVL 1</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="{MUT}">the wheel</text></svg>
      <div><div style="font-family:DM Sans;font-weight:900;font-size:32px;color:#FAFAF7;line-height:1.1">Ask. Copy. Close.</div>
      <div style="font-family:DM Sans;font-size:19px;color:{MUT};margin-top:10px;line-height:1.4">Every session starts from zero. You spin, you never climb.</div>
      <div style="font-family:DM Mono;font-size:14px;color:rgb({ACC});margin-top:16px">88% of users never leave here</div></div></div>'''

# 2. recall card - remembers what you hate
def memory():
    avoid=["em dashes","hard-sell CTAs","meetings before noon","sending unread"]
    rows="".join(f'<div style="display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span style="font-family:DM Sans;font-weight:900;font-size:16px;color:rgb({ACC})">✕</span><span style="font-family:DM Sans;font-size:18px;color:#d7d1c6">{a}</span><span style="font-family:DM Mono;font-size:12px;color:{MUT};margin-left:auto">avoided</span></div>' for a in avoid)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {lv(2,"It remembers what you hate","PERSISTENT")}
      <div style="display:flex;gap:26px;align-items:center">
        <div style="flex:1">{rows}</div>
        <div style="flex-shrink:0;width:150px;text-align:center">
          <div style="width:96px;height:96px;margin:0 auto;border-radius:22px;background:linear-gradient(160deg,rgba(204,120,92,.16),rgba(204,120,92,.05));border:1px solid rgba(204,120,92,.34);display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(204,120,92,.14)">
            <svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="1.8"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M9 4v16M4 9h5M4 15h5"/></svg></div>
          <div style="font-family:DM Sans;font-weight:800;font-size:16px;color:#FAFAF7;margin-top:10px">held across<br>every session</div></div>
      </div></div>'''

# 3. live job monitor - works while you watch
def jobs():
    steps=[("pulled 40 leads",True),("scored + ranked",True),("drafting replies",False)]
    rows=""
    for s,done in steps:
        ic=('<svg width="22" height="22" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(127,211,154,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#7fd39a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>' if done
            else f'<svg width="22" height="22" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="rgb({ACC})" stroke-width="2.5" stroke-dasharray="30 12"/></svg>')
        rows+=f'<div style="display:flex;align-items:center;gap:12px;padding:9px 0"><span>{ic}</span><span style="font-family:DM Sans;font-size:18px;color:{"#d7d1c6" if done else "#FAFAF7"}">{s}</span></div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {lv(3,"It works while you watch","LIVE")}
      <div style="background:#191614;border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px 22px">
        <div style="display:flex;justify-content:space-between;margin-bottom:8px"><span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">follow_up.job</span><span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">running</span></div>
        {rows}
        <div style="height:8px;border-radius:4px;background:#2c2925;margin-top:12px;overflow:hidden"><div style="height:100%;width:68%;background:rgb({ACC})"></div></div></div>
      <div style="display:inline-block;margin-top:16px;background:rgba(204,120,92,.10);border:1px solid rgba(204,120,92,.28);border-radius:999px;padding:8px 16px;font-family:DM Mono;font-size:13px;color:#e9e3d7">you: watching, coffee in hand</div></div>'''

# 4. parallel lanes - it ships while you sell
def ship():
    def lane(label,who,items,acc):
        chips="".join(f'<div style="flex:1;height:34px;border-radius:8px;background:{acc};opacity:{0.5+i*0.16};display:flex;align-items:center;justify-content:center;font-family:DM Mono;font-size:12px;color:#1a0f0a">{x}</div>' for i,x in enumerate(items))
        return (f'<div style="margin-bottom:16px"><div style="display:flex;justify-content:space-between;margin-bottom:8px">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">{label}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:{MUT}">{who}</span></div>'
          f'<div style="display:flex;gap:8px">{chips}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {lv(4,"It ships while you sell","IN PARALLEL")}
      {lane("It ships","the agent",["build","test","deploy"],f"rgb({ACC})")}
      {lane("You sell","the founder",["call","demo","close"],"#4a423c")}
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:8px">two lanes, same hour: your time goes to revenue, not to the build</div></div>'''

# 5. overnight schedule - runs while you sleep
def routines():
    jobs=[("02:00","market scan"),("04:00","content drafted"),("06:00","digest built")]
    chips="".join(f'<div style="flex:1;background:#221f1b;border:1px solid rgba(204,120,92,.2);border-radius:14px;padding:16px;text-align:center"><div style="font-family:DM Mono;font-size:15px;color:rgb({ACC})">{tm}</div><div style="font-family:DM Sans;font-weight:700;font-size:16px;color:#e9e3d7;margin-top:6px">{jb}</div></div>' for tm,jb in jobs)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {lv(5,"It runs while you sleep","OVERNIGHT")}
      <div style="display:flex;align-items:center;gap:20px;margin-bottom:18px">
        <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="1.6"><path d="M21 12.8A9 9 0 1 1 11.2 3 a7 7 0 0 0 9.8 9.8Z"/></svg>
        <div style="font-family:DM Sans;font-weight:900;font-size:28px;color:#FAFAF7">The night shift clocks in</div></div>
      <div style="display:flex;gap:14px">{chips}</div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:16px">you: asleep &nbsp;·&nbsp; the work: staged by 07:00</div></div>'''

# 6. level ladder with a hidden rung 3
def gap():
    rungs=""
    for n in range(5,0,-1):
        if n<=2: state=("solid","#e9e3d7","rgba(255,255,255,.10)")
        elif n==3: state=("glow",f"rgb({ACC})","rgba(204,120,92,.5)")
        else: state=("dim",DIM,"rgba(255,255,255,.05)")
        lab={5:"runs asleep",4:"ships as you sell",3:"HIDDEN · works for you",2:"remembers",1:"ask/copy/close"}[n]
        glow="box-shadow:0 0 34px rgba(204,120,92,.22);" if n==3 else ""
        rungs+=(f'<div style="display:flex;align-items:center;gap:16px;background:{"rgba(204,120,92,.10)" if n==3 else "#221f1b"};border:1px solid {state[2]};border-radius:12px;padding:14px 18px;margin-bottom:9px;{glow}">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:24px;color:{state[1]};width:34px">{n}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:{800 if n==3 else 600};font-size:18px;color:{state[1]}">{lab}</span>'
          f'{("<span style=font-family:DM-Mono;font-size:12px;color:rgb("+ACC+")>you are here? no.</span>") if False else ""}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {lv("?","Nobody told you level 3 exists","THE GAP")}{rungs}</div>'''

# 7. belay clip - climb fast, clipped to your control
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px">
      {lv("↑","Climb fast. Stay clipped.","SAFETY ON")}
      <div style="display:flex;align-items:center;gap:36px;margin-top:6px">
        <svg width="200" height="230" viewBox="0 0 200 230">
          <path d="M40 210 L40 30" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="1 10" stroke-linecap="round"/>
          {"".join(f'<g transform="translate(40,{40+i*44})"><rect x="-8" y="-6" width="16" height="12" rx="4" fill="none" stroke="rgb({ACC})" stroke-width="3"/></g>' for i in range(4))}
          <circle cx="120" cy="70" r="24" fill="none" stroke="rgb({ACC})" stroke-width="5"/>
          <path d="M120 46 a24 24 0 0 1 0 48" fill="none" stroke="#e08a5a" stroke-width="5"/>
          <path d="M40 92 Q90 80 108 76" fill="none" stroke="rgba(204,120,92,.6)" stroke-width="3"/>
          <text x="120" y="130" text-anchor="middle" font-family="DM Mono" font-size="13" fill="{MUT}">clip</text>
        </svg>
        <div style="flex:1">
          <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;line-height:1.1">Full ascent, roped in</div>
          <div style="font-family:DM Sans;font-size:19px;color:{MUT};margin-top:10px;line-height:1.45">Race up the levels at machine speed, clipped to your approval the whole way.</div>
          <div style="font-family:DM Mono;font-size:14px;color:rgb({ACC});margin-top:16px">nothing external moves without your tap</div></div>
      </div></div>'''

# 8. quiet summit
def ceiling():
    return f'''<div style="width:900px;{CARD};padding:40px;text-align:center">
      <div style="display:flex;justify-content:center;margin-bottom:20px">
        <svg width="220" height="130" viewBox="0 0 220 130">
          <path d="M10 120 L70 40 L110 80 L150 20 L210 120 Z" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
          <path d="M150 20 L172 48 L128 48 Z" fill="rgb({ACC})"/>
          <circle cx="150" cy="20" r="7" fill="rgb({ACC})" filter="url(#pg)"/>
          <defs><filter id="pg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="1"/></filter></defs>
        </svg></div>
      <div style="font-family:DM Sans;font-weight:900;font-size:38px;color:#FAFAF7;line-height:1.05">The ceiling is quiet.</div>
      <div style="font-family:DM Sans;font-size:20px;color:{MUT};margin-top:12px">Level 5. Nothing to click. Just systems, running.</div>
      <div style="display:inline-flex;align-items:center;gap:9px;margin-top:20px;background:rgba(204,120,92,.10);border:1px solid rgba(204,120,92,.3);border-radius:999px;padding:9px 18px">
        <span style="width:10px;height:10px;border-radius:50%;background:#7fd39a;box-shadow:0 0 12px rgba(127,211,154,.7)"></span>
        <span style="font-family:DM Mono;font-size:14px;color:#e9e3d7">all systems running</span></div></div>'''

PANELS={"floor":floor(),"memory":memory(),"jobs":jobs(),"ship":ship(),
        "routines":routines(),"gap":gap(),"gate":gate(),"ceiling":ceiling()}
if __name__=="__main__":
    print("unstuck t3:"); B.render("unstuck",PANELS)
