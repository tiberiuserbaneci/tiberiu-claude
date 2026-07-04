#!/usr/bin/env python3
# TIER 3 - THE COMPLETE AI BODY. forms: anatomy roster / tier router / first-to-see timeline /
# voice-match ring / build-test-ship pipeline / memory-core lifelines / reins control / assembly.
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="212,162,127"
def head(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
IC={
 "mouth":'<path d="M4 12 Q12 20 20 12 Q12 16 4 12Z" fill="none" stroke="{c}" stroke-width="2"/>',
 "eyes":'<path d="M2 12 Q12 4 22 12 Q12 20 2 12Z" fill="none" stroke="{c}" stroke-width="2"/><circle cx="12" cy="12" r="3.5" fill="{c}"/>',
 "hands":'<path d="M6 12 v-4 a1.6 1.6 0 0 1 3.2 0 M9.2 8 v-2 a1.6 1.6 0 0 1 3.2 0 v2 M12.4 7 a1.6 1.6 0 0 1 3.2 0 v5 M6 12 v4 a5 5 0 0 0 9.6 2 v-6" fill="none" stroke="{c}" stroke-width="1.8"/>',
 "brain":'<path d="M9 4 a4 4 0 0 0 0 8 a4 4 0 0 0 0 8 M15 4 a4 4 0 0 1 0 8 a4 4 0 0 1 0 8 M12 5 v14" fill="none" stroke="{c}" stroke-width="1.8"/>',
 "heart":'<path d="M12 20 C4 14 4 7 8.5 7 C11 7 12 9 12 9 C12 9 13 7 15.5 7 C20 7 20 14 12 20Z" fill="none" stroke="{c}" stroke-width="1.8"/>',
}
def icon(k,c,s=26): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24">{IC[k].replace("{c}",c)}</svg>'

# 1. DIFFERENCE - anatomy roster, only the MOUTH lit; the rest of the body missing
def difference():
    parts=[("mouth","Mouth","talks",True),("eyes","Eyes","sees the market",False),("hands","Hands","ships the work",False),("brain","Brain","budgets thinking",False),("heart","Heart","remembers you",False)]
    rows=""
    for k,nm,role,on in parts:
        c=f"rgb({ACC})" if on else DIM
        tag="RENTED" if on else "MISSING"
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.06);opacity:{1 if on else 0.5}">'
          f'<div style="width:44px;height:44px;border-radius:12px;background:{"rgba(212,162,127,.14)" if on else "rgba(255,255,255,.03)"};display:flex;align-items:center;justify-content:center">{icon(k,c)}</div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:{MUT}">{role}</div></div>'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{c}">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 34px">
      {head("You rented a mouth","1 OF 5 ORGANS")}{rows}</div>'''

# 2. ROUTER - a brain that routes each job to the cheapest capable tier
def router():
    tiers=[("LITE","quick lookups","0.02","¢",False),("SMART","daily execution","0.11","¢",True),("DEEP","hard judgement","0.40","¢",False)]
    cards=""
    for nm,role,cost,u,on in tiers:
        bg="linear-gradient(160deg,rgba(212,162,127,.16),rgba(212,162,127,.05))" if on else "#221f1b"
        bd="rgba(212,162,127,.4)" if on else "rgba(255,255,255,.07)"
        sh="box-shadow:0 0 40px rgba(212,162,127,.14)" if on else ""
        nmcol=f"rgb({ACC})" if on else MUT
        foot=(f'<div style="margin-top:10px;font-family:DM Mono;font-size:12px;color:rgb({ACC})">&#9664; picked</div>'
              if on else '<div style="margin-top:10px;height:16px"></div>')
        cards+=(f'<div style="flex:1;background:{bg};border:1px solid {bd};border-radius:16px;padding:18px 16px;text-align:center;{sh}">'
          f'<div style="font-family:DM Mono;font-size:14px;letter-spacing:.14em;color:{nmcol}">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7;margin:8px 0 2px">{cost}<span style="font-size:18px;color:rgb({ACC})">{u}</span></div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:{MUT}">{role}</div>{foot}</div>')
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px">
      {head("A brain that budgets itself","MODEL ROUTER")}
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-bottom:14px">job: "draft 12 follow-ups" &nbsp;→&nbsp; routed to the cheapest tier that can</div>
      <div style="display:flex;gap:16px">{cards}</div></div>'''

# 3. EYES - first to see: it flagged the round days before the VC
def eyes():
    W=780
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 42px">
      {head("It saw the round first","SIGNAL LEAD")}
      <svg width="{W}" height="150" viewBox="0 0 {W} 150" style="width:100%">
        <defs><filter id="g" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <line x1="40" y1="80" x2="{W-40}" y2="80" stroke="rgba(255,255,255,.14)" stroke-width="2"/>
        <circle cx="150" cy="80" r="14" fill="rgb({ACC})" filter="url(#g)"/>
        <text x="150" y="46" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">It flagged it</text>
        <text x="150" y="118" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})">Tue 09:12</text>
        <circle cx="{W-150}" cy="80" r="11" fill="none" stroke="{DIM}" stroke-width="3"/>
        <text x="{W-150}" y="46" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="{MUT}">VC noticed</text>
        <text x="{W-150}" y="118" text-anchor="middle" font-family="DM Mono" font-size="14" fill="{DIM}">Fri 16:40</text>
        <line x1="164" y1="80" x2="{W-164}" y2="80" stroke="rgb({ACC})" stroke-width="3" stroke-dasharray="2 8"/>
      </svg>
      <div style="text-align:center;font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7;margin-top:8px">3 days of head start</div></div>'''

# 4. VOICE - style-match ring on a sample written in your voice
def voice():
    pct=98; import math
    r=64; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px;display:flex;align-items:center;gap:34px">
      <div style="flex:1">
        <div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:{MUT};margin-bottom:10px">DRAFTED IN YOUR VOICE</div>
        <div style="background:#191614;border-left:3px solid rgb({ACC});border-radius:10px;padding:16px 18px;font-family:DM Sans;font-size:19px;color:#e9e3d7;line-height:1.4">
          "I killed nine tools last month. The one I kept did not have a chat box."</div>
        <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:14px">short lines · operator voice · no hedging</div></div>
      <div style="flex-shrink:0;position:relative;width:160px;height:160px">
        <svg width="160" height="160" viewBox="0 0 160 160">
          <circle cx="80" cy="80" r="{r}" fill="none" stroke="#2a2620" stroke-width="12"/>
          <circle cx="80" cy="80" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="12" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 80 80)"/>
        </svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:36px;color:#FAFAF7">{pct}%</span>
          <span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">style match</span></div></div></div>'''

# 5. HANDS - build/test/ship pipeline, done while you were out
def hands():
    stages=[("build","wrote the feature"),("test","42 passed · 0 failed"),("ship","live on main")]
    nodes=""
    for i,(nm,sub) in enumerate(stages):
        nodes+=(f'<div style="flex:1;text-align:center">'
          f'<div style="width:64px;height:64px;margin:0 auto 12px;border-radius:18px;background:linear-gradient(160deg,rgba(212,162,127,.18),rgba(212,162,127,.05));border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;box-shadow:0 0 30px rgba(212,162,127,.12)">'
          f'<svg width="30" height="30" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7;text-transform:capitalize">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:{MUT};margin-top:2px">{sub}</div></div>')
        if i<2: nodes+=f'<div style="flex-shrink:0;align-self:flex-start;margin-top:26px"><svg width="50" height="24" viewBox="0 0 50 24"><path d="M2 12 H40 M32 5 L46 12 L32 19" fill="none" stroke="{DIM}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px">
      {head("Built, tested, shipped","WHILE YOU WERE OUT")}
      <div style="display:flex;align-items:flex-start;gap:8px;margin:14px 0">{nodes}</div>
      <div style="display:inline-block;background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.28);border-radius:999px;padding:9px 18px;font-family:DM Mono;font-size:14px;color:#e9e3d7">you: at dinner</div></div>'''

# 6. HEART - memory core with organ lifelines; sever it and the body dies
def heart():
    cx,cy=200,190; import math
    organs=[("brain",-90),("eyes",-18),("hands",54),("mouth",126),("mouth",198)]
    lines=""; nodes=""
    for i,(nm,a) in enumerate(organs):
        x=cx+150*math.cos(math.radians(a)); y=cy+150*math.sin(math.radians(a))
        cut=(i==2)
        col=f"rgb(200,70,35)" if cut else f"rgba(212,162,127,.5)"
        dash='stroke-dasharray="4 8"' if cut else ""
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="3" {dash}/>'
        if cut: lines+=f'<text x="{(cx+x)/2:.0f}" y="{(cy+y)/2-8:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="rgb(200,70,35)">✕ cut</text>'
        nn = nm if nm in IC else "brain"
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="26" fill="#241f1a" stroke="{"rgba(200,70,35,.6)" if cut else "rgba(255,255,255,.12)"}" stroke-width="2"/>'
          f'<g transform="translate({x-13:.0f},{y-13:.0f})">{IC[nn].replace("{c}", DIM if cut else "#cfc9bd")}</g>')
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:30px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="400" height="380" viewBox="0 0 400 380">
        <defs><radialGradient id="hb" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}
        <g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="46" fill="url(#hb)"/></g>
        <g transform="translate({cx-15},{cy-15})">{IC["heart"].replace("{c}","#2a160c")}</g></svg>
      <div style="flex:1">
        <div style="font-family:DM Sans;font-weight:900;font-size:32px;color:#FAFAF7;line-height:1.1">Memory is the heart</div>
        <div style="font-family:DM Sans;font-size:19px;color:{MUT};margin-top:10px;line-height:1.45">Cut it and every organ goes dark: the eyes forget, the hands stall, the voice drifts.</div>
        <div style="font-family:DM Mono;font-size:14px;color:rgb(200,70,35);margin-top:16px">no memory → no body</div></div></div>'''

# 7. GATE - a powerful core held on the operator's reins
def gate():
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 42px">
      {head("Strong body. My reins.","POWER · HELD")}
      <div style="display:flex;align-items:center;gap:0;margin-top:8px">
        <div style="flex-shrink:0;width:200px;height:200px;border-radius:50%;background:radial-gradient(circle at 38% 32%,#f0c49e,rgb({ACC}) 55%,#7a4326);box-shadow:0 0 60px rgba(212,162,127,.3),inset 0 4px 6px rgba(255,255,255,.4);display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#2a160c">FULL</span>
          <span style="font-family:DM Mono;font-size:14px;color:#3a2010;letter-spacing:.1em">CAPABILITY</span></div>
        <svg width="240" height="60" viewBox="0 0 240 60" style="flex:1"><path d="M6 30 Q120 30 234 30" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="1 9" stroke-linecap="round"/>
          <circle cx="6" cy="30" r="6" fill="rgb({ACC})"/></svg>
        <div style="flex-shrink:0;text-align:center">
          <div style="width:96px;height:96px;border-radius:24px;background:linear-gradient(160deg,#2a2723,#171512);border:2px solid rgba(212,162,127,.4);display:flex;align-items:center;justify-content:center;box-shadow:0 16px 30px rgba(0,0,0,.5)">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><path d="M6 11V8a6 6 0 0 1 12 0v3"/><rect x="4" y="11" width="16" height="10" rx="2.5"/></svg></div>
          <div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7;margin-top:10px">your hand</div></div>
      </div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};text-align:center;margin-top:20px">all the power on a rein you never let go of</div></div>'''

# 8. OPERATOR - scattered organs assemble into one body/system
def operator():
    chips=["brain","eyes","hands","mouth","heart"]
    scat="".join(f'<div style="width:52px;height:52px;border-radius:14px;background:#221f1b;border:1px solid rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center">{icon(k,DIM,26)}</div>' for k in chips)
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 42px">
      {head("Assemble the body","ONE SYSTEM")}
      <div style="display:flex;align-items:center;gap:26px">
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;opacity:.65">{scat}</div>
        <svg width="64" height="40" viewBox="0 0 64 40"><path d="M4 20 H46 M36 8 L52 20 L36 32" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex:1;background:linear-gradient(160deg,rgba(212,162,127,.16),rgba(212,162,127,.05));border:1.5px solid rgba(212,162,127,.4);border-radius:20px;padding:24px;box-shadow:0 0 50px rgba(212,162,127,.14)">
          <div style="display:flex;gap:10px;margin-bottom:14px">{"".join(icon(k,f"rgb({ACC})",30) for k in chips)}</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7">One operator body</div>
          <div style="font-family:DM Sans;font-size:16px;color:{MUT};margin-top:2px">brain, eyes, hands, voice, heart: composed, gated, yours</div></div>
      </div></div>'''

PANELS={"difference":difference(),"router":router(),"eyes":eyes(),"voice":voice(),
        "hands":hands(),"heart":heart(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    print("aibody t3:"); B.render("aibody",PANELS)
