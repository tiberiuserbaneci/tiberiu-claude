#!/usr/bin/env python3
# TIER 3 - THE COMPLETE AI BODY. Real 3D extruded panels, non-rectangular silhouettes, dense (~1.19 fill).
# stems: difference / router / eyes / voice / hands / heart / gate / operator
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
INK=B.INK; MUT=B.MUT; DIM=B.DIM; shape=B.shape; circle=B.circle
ACC="212,162,127"; IV_ACC="150,90,45"
def head(tt,tag,ink="#FAFAF7",mut=MUT,acc=ACC): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:29px;color:{ink}">{tt}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:14px;letter-spacing:.14em;color:rgb({acc})">{tag}</span></div>')
IC={
 "mouth":'<path d="M4 12 Q12 20 20 12 Q12 16 4 12Z" fill="none" stroke="{c}" stroke-width="2"/>',
 "eyes":'<path d="M2 12 Q12 4 22 12 Q12 20 2 12Z" fill="none" stroke="{c}" stroke-width="2"/><circle cx="12" cy="12" r="3.5" fill="{c}"/>',
 "hands":'<path d="M6 12 v-4 a1.6 1.6 0 0 1 3.2 0 M9.2 8 v-2 a1.6 1.6 0 0 1 3.2 0 v2 M12.4 7 a1.6 1.6 0 0 1 3.2 0 v5 M6 12 v4 a5 5 0 0 0 9.6 2 v-6" fill="none" stroke="{c}" stroke-width="1.8"/>',
 "brain":'<path d="M9 4 a4 4 0 0 0 0 8 a4 4 0 0 0 0 8 M15 4 a4 4 0 0 1 0 8 a4 4 0 0 1 0 8 M12 5 v14" fill="none" stroke="{c}" stroke-width="1.8"/>',
 "heart":'<path d="M12 20 C4 14 4 7 8.5 7 C11 7 12 9 12 9 C12 9 13 7 15.5 7 C20 7 20 14 12 20Z" fill="none" stroke="{c}" stroke-width="1.8"/>',
}
def icon(k,c,s=26): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24">{IC[k].replace("{c}",c)}</svg>'
def foot(items,ink="#FAFAF7",mut=MUT,bg="#191614",bd="rgba(255,255,255,.06)",acc=ACC):
    chips="".join(f'<div style="flex:1;text-align:center;padding:20px 8px;background:{bg};border:1px solid {bd};border-radius:14px"><div style="font-family:DM Sans;font-weight:900;font-size:28px;color:rgb({acc});line-height:1">{b}</div><div style="font-family:DM Mono;font-size:11.5px;letter-spacing:.08em;color:{mut};margin-top:8px">{s}</div></div>' for b,s in items)
    return f'<div style="display:flex;gap:12px;margin-top:22px">{chips}</div>'
W=680
def box(inner): return f'<div style="width:{W}px">{inner}</div>'

# 1. DIFFERENCE - anatomy roster, only the MOUTH rented; rest of the body missing. slantL
def difference():
    parts=[("mouth","Mouth","talks back",True),("eyes","Eyes","sees the market move",False),("hands","Hands","ships the work",False),("brain","Brain","budgets the thinking",False),("heart","Heart","remembers you",False)]
    rows=""
    for k,nm,role,on in parts:
        c=f"rgb({ACC})" if on else DIM; tag="RENTED" if on else "MISSING"
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;padding:16px 0;border-bottom:1px solid rgba(255,255,255,.06);opacity:{1 if on else 0.5}">'
          f'<div style="width:50px;height:50px;border-radius:13px;background:{"rgba(212,162,127,.14)" if on else "rgba(255,255,255,.03)"};display:flex;align-items:center;justify-content:center">{icon(k,c,28)}</div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:21px;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:{MUT}">{role}</div></div>'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{c}">{tag}</span></div>')
    inner=(f'{head("You rented a mouth","1 OF 5 ORGANS")}'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT};margin-bottom:10px">A CHATBOT IS ONE ORGAN. A BODY NEEDS FIVE.</div>{rows}'
      f'{foot([("1","OF 5 ORGANS"),("4","MISSING"),("chat","IN A BOX")])}')
    return shape(box(inner),"slantL")

# 2. ROUTER - a brain that routes each job to the cheapest capable tier. notch
def router():
    tiers=[("LITE","quick lookups","0.02",False),("SMART","daily execution","0.11",True),("DEEP","hard judgement","0.40",False)]
    cards=""
    for nm,role,cost,on in tiers:
        bg="linear-gradient(160deg,rgba(212,162,127,.16),rgba(212,162,127,.05))" if on else "#221f1b"
        bd="rgba(212,162,127,.4)" if on else "rgba(255,255,255,.07)"; nmcol=f"rgb({ACC})" if on else MUT
        pick=(f'<div style="margin-top:10px;font-family:DM Mono;font-size:12px;color:rgb({ACC})">&#9664; picked</div>' if on else '<div style="margin-top:10px;height:16px"></div>')
        cards+=(f'<div style="flex:1;background:{bg};border:1px solid {bd};border-radius:16px;padding:20px 16px;text-align:center">'
          f'<div style="font-family:DM Mono;font-size:14px;letter-spacing:.14em;color:{nmcol}">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:36px;color:#FAFAF7;margin:10px 0 2px">{cost}<span style="font-size:18px;color:rgb({ACC})"> c</span></div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:{MUT}">{role}</div>{pick}</div>')
    steps=[("reads the job","draft 12 follow-ups"),("scores difficulty","simple, high-volume"),("picks the tier","cheapest that can"),("runs it","0.11c, not dollars"),("logs the spend","you see every cent")]
    flow="".join(f'<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span style="font-family:DM Sans;font-weight:800;font-size:15px;color:rgb({ACC});width:120px">{a}</span><span style="font-family:DM Sans;font-size:16px;color:#cfc9bd">{b}</span></div>' for a,b in steps)
    inner=(f'{head("A brain that budgets itself","MODEL ROUTER")}'
      f'<div style="display:flex;gap:14px;margin-bottom:18px">{cards}</div>'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT};margin-bottom:4px">HOW IT PICKS</div>{flow}'
      f'{foot([("3","TIERS"),("0.11 c","PER JOB"),("70%","CHEAPER")])}')
    return shape(box(inner),"notch")

# 3. EYES - first to see: signals + head-start. arrow (dense signal rows)
def eyes():
    sig=[("Funding round",94),("Hiring spike",81),("Stack change",76),("Buying intent",69),("Exec change",63),("Product launch",58),("Tech renewal",52)]
    rows=""
    for nm,v in sig:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:12px">'
          f'<span style="width:150px;font-family:DM Sans;font-weight:600;font-size:16px;color:#e9e3d7">{nm}</span>'
          f'<div style="flex:1;height:26px;border-radius:6px;background:#211d19;overflow:hidden"><div style="width:{v}%;height:100%;background:linear-gradient(90deg,rgb({ACC}),rgba(212,162,127,.5))"></div></div>'
          f'<span style="width:44px;text-align:right;font-family:DM Mono;font-size:14px;color:rgb({ACC})">{v}%</span></div>')
    inner=(f'{head("It saw the round first","SIGNAL LEAD")}'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT};margin-bottom:14px">SIGNALS THE EYES WATCH, RANKED</div>{rows}'
      f'<div style="display:flex;align-items:center;gap:16px;margin-top:18px;background:linear-gradient(160deg,rgba(212,162,127,.14),rgba(212,162,127,.04));border:1px solid rgba(212,162,127,.34);border-radius:15px;padding:18px 22px">'
      f'<div><div style="font-family:DM Mono;font-size:12px;color:{MUT}">YOU + ULTRON</div><div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">Tue 09:12</div></div>'
      f'<svg width="46" height="22" viewBox="0 0 46 22" style="flex-shrink:0"><path d="M2 11 H36 M28 4 L44 11 L28 18" fill="none" stroke="rgb({ACC})" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      f'<div><div style="font-family:DM Mono;font-size:12px;color:{MUT}">THE VC</div><div style="font-family:DM Sans;font-weight:800;font-size:18px;color:{MUT}">Fri 16:40</div></div>'
      f'<div style="margin-left:auto;text-align:right"><div style="font-family:DM Sans;font-weight:900;font-size:30px;color:rgb({ACC});line-height:1">3 days</div><div style="font-family:DM Mono;font-size:12px;color:{MUT}">head start</div></div></div>'
      f'{foot([("4","SIGNALS"),("Tue 09:12","IT SAW"),("3 days","AHEAD")])}')
    return shape(box(inner),"arrow")

# 4. VOICE - style-match, IVORY panel. notch2
def voice():
    pct=98; r=64; circ=2*math.pi*r; dash=circ*pct/100
    ivink="#2a2016"; ivmut="#8a745a"
    inner=(f'{head("It writes in your voice","VOICE MATCH",ink=ivink,mut=ivmut,acc=IV_ACC)}'
      f'<div style="background:rgba(255,255,255,.6);border-left:4px solid rgb({IV_ACC});border-radius:12px;padding:20px 22px;font-family:DM Sans;font-size:21px;color:{ivink};line-height:1.42">'
      f'"I killed nine tools last month. The one I kept did not have a chat box."</div>'
      f'<div style="display:flex;align-items:center;gap:28px;margin-top:20px">'
      f'<div style="flex-shrink:0;position:relative;width:150px;height:150px">'
      f'<svg width="150" height="150" viewBox="0 0 160 160"><circle cx="80" cy="80" r="{r}" fill="none" stroke="rgba(150,90,45,.2)" stroke-width="12"/>'
      f'<circle cx="80" cy="80" r="{r}" fill="none" stroke="rgb({IV_ACC})" stroke-width="12" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 80 80)"/></svg>'
      f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center"><span style="font-family:DM Sans;font-weight:900;font-size:34px;color:{ivink}">{pct}%</span><span style="font-family:DM Mono;font-size:11px;color:rgb({IV_ACC})">match</span></div></div>'
      f'<div style="flex:1">'
      + "".join(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="rgb({IV_ACC})" stroke-width="2.6"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:17px;color:{ivink}">{x}</span></div>' for x in ["short operator lines","no hedging, ever","your cadence, not the model's","reads like you wrote it fast"])
      + f'</div></div>'
      f'<div style="background:rgba(255,255,255,.5);border:1px solid rgba(120,95,60,.16);border-radius:12px;padding:16px 20px;margin-top:16px;font-family:DM Sans;font-size:18px;color:{ivink};line-height:1.4">"Nine tools, one survivor. The keeper does the work while I sleep."</div>'
      f'{foot([("98%","STYLE MATCH"),("5","POSTS SAMPLED"),("0","HEDGING")],ink=ivink,mut=ivmut,bg="rgba(255,255,255,.6)",bd="rgba(120,95,60,.16)",acc=IV_ACC)}')
    return shape(box(inner),"notch2",iv=True)

# 5. HANDS - build/test/ship + a run log. bevel
def hands():
    stages=[("Build","wrote the feature"),("Test","42 passed, 0 failed"),("Ship","live on main")]
    nodes=""
    for i,(nm,sub) in enumerate(stages):
        nodes+=(f'<div style="flex:1;text-align:center"><div style="width:66px;height:66px;margin:0 auto 12px;border-radius:18px;background:linear-gradient(160deg,rgba(212,162,127,.18),rgba(212,162,127,.05));border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center"><svg width="30" height="30" viewBox="0 0 24 24"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{nm}</div><div style="font-family:DM Sans;font-size:14px;color:{MUT};margin-top:2px">{sub}</div></div>')
        if i<2: nodes+=f'<div style="flex-shrink:0;align-self:flex-start;margin-top:28px"><svg width="46" height="22" viewBox="0 0 46 22"><path d="M2 11 H36 M28 4 L44 11 L28 18" fill="none" stroke="{DIM}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
    log=[("22:09","picked up the ticket"),("22:14","opened PR #182"),("22:16","42 tests green"),("22:17","merged to main"),("22:18","deployed, live")]
    logrows="".join(f'<div style="display:flex;align-items:center;gap:14px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span style="font-family:DM Mono;font-size:13px;color:{MUT};width:80px">{ts}</span><span style="font-family:DM Sans;font-size:16px;color:#cfc9bd">{r}</span></div>' for ts,r in log)
    inner=(f'{head("Built, tested, shipped","WHILE YOU WERE OUT")}'
      f'<div style="display:flex;align-items:flex-start;gap:8px;margin:6px 0 20px">{nodes}</div>'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT};margin-bottom:4px">THE LOG, WHILE YOU WERE AT DINNER</div>{logrows}'
      f'{foot([("42","TESTS PASSED"),("0","FAILED"),("live","ON MAIN")])}')
    return shape(box(inner),"bevel")

# 6. HEART - memory core radial. circle
def heart():
    cx,cy=190,190
    organs=[("brain",-90),("eyes",-18),("hands",54),("mouth",126),("heart",198)]
    lines=""; nodes=""
    for i,(nm,a) in enumerate(organs):
        x=cx+128*math.cos(math.radians(a)); y=cy+128*math.sin(math.radians(a))
        cut=(i==2); col="rgb(200,70,35)" if cut else "rgba(212,162,127,.5)"; dash='stroke-dasharray="4 8"' if cut else ""
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="3" {dash}/>'
        nn=nm if nm in IC else "brain"
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="26" fill="#241f1a" stroke="{"rgba(200,70,35,.6)" if cut else "rgba(255,255,255,.12)"}" stroke-width="2"/>'
          f'<g transform="translate({x-13:.0f},{y-13:.0f})">{IC[nn].replace("{c}", DIM if cut else "#cfc9bd")}</g>')
    svg=(f'<svg width="380" height="380" viewBox="0 0 380 380"><defs><radialGradient id="hb" cx="50%" cy="45%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient></defs>'
      f'{lines}<circle cx="{cx}" cy="{cy}" r="46" fill="url(#hb)"/><g transform="translate({cx-15},{cy-15})">{IC["heart"].replace("{c}","#2a160c")}</g></svg>')
    inner=(f'<div style="font-family:DM Mono;font-size:14px;letter-spacing:.16em;color:rgb({ACC});text-align:center">MEMORY CORE</div>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;text-align:center;margin:6px 0 4px">Memory is the heart</div>{svg}'
      f'<div style="font-family:DM Sans;font-size:17px;color:{MUT};text-align:center;max-width:460px;line-height:1.4">Cut it and every organ goes dark: the eyes forget, the hands stall.</div>')
    return circle(inner,size=760)

# 7. GATE - full capability held on the operator's reins. tag
def gate():
    holds=["it never sends on its own","every action waits for you","one tap arms it, one tap kills it","you see the plan before it runs","kill switch on every step"]
    lis="".join(f'<div style="display:flex;align-items:center;gap:11px;margin-bottom:13px"><span style="width:7px;height:7px;border-radius:50%;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:17px;color:#d7d1c6">{x}</span></div>' for x in holds)
    inner=(f'{head("Strong body. My reins.","POWER, HELD")}'
      f'<div style="display:flex;align-items:center;gap:18px;margin:8px 0 20px">'
      f'<div style="flex-shrink:0;width:150px;height:150px;border-radius:50%;background:radial-gradient(circle at 38% 32%,#f0c49e,rgb({ACC}) 55%,#7a4326);box-shadow:inset 0 4px 6px rgba(255,255,255,.4);display:flex;flex-direction:column;align-items:center;justify-content:center"><span style="font-family:DM Sans;font-weight:900;font-size:24px;color:#2a160c">FULL</span><span style="font-family:DM Mono;font-size:11px;color:#3a2010">CAPABILITY</span></div>'
      f'<svg width="120" height="40" viewBox="0 0 120 40" style="flex-shrink:0"><path d="M6 20 H114" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="1 9" stroke-linecap="round"/><circle cx="6" cy="20" r="6" fill="rgb({ACC})"/></svg>'
      f'<div style="flex-shrink:0;text-align:center"><div style="width:90px;height:90px;border-radius:22px;background:linear-gradient(160deg,#2a2723,#171512);border:2px solid rgba(212,162,127,.4);display:flex;align-items:center;justify-content:center"><svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2"><path d="M6 11V8a6 6 0 0 1 12 0v3"/><rect x="4" y="11" width="16" height="10" rx="2.5"/></svg></div><div style="font-family:DM Sans;font-weight:800;font-size:16px;color:#FAFAF7;margin-top:8px">your hand</div></div></div>'
      f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT};margin-bottom:12px">WHAT THE GATE HOLDS</div>{lis}'
      f'{foot([("FULL","CAPABILITY"),("1","YOUR HAND"),("0","AUTO-SEND")])}')
    return shape(box(inner),"tag",pad="36px 48px")

# 8. OPERATOR - scattered organs assemble into one body. ribbon
def operator():
    chips=["brain","eyes","hands","mouth","heart"]
    scat="".join(f'<div style="width:64px;height:64px;border-radius:15px;background:#221f1b;border:1px solid rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center">{icon(k,DIM,28)}</div>' for k in chips)
    inner=(f'{head("Assemble the body","ONE SYSTEM")}'
      f'<div style="display:flex;align-items:center;gap:22px;margin-bottom:18px">'
      f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:11px;opacity:.6">{scat}</div>'
      f'<svg width="56" height="34" viewBox="0 0 56 34" style="flex-shrink:0"><path d="M4 17 H40 M32 6 L52 17 L32 28" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      f'<div style="flex:1;background:linear-gradient(160deg,rgba(212,162,127,.16),rgba(212,162,127,.05));border:1.5px solid rgba(212,162,127,.4);border-radius:20px;padding:22px"><div style="display:flex;gap:9px;margin-bottom:12px">{"".join(icon(k,f"rgb({ACC})",30) for k in chips)}</div><div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#FAFAF7">One operator body</div></div></div>'
      + "".join(f'<div style="display:flex;align-items:center;gap:11px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC});width:110px">{a}</span><span style="font-family:DM Sans;font-size:16px;color:#cfc9bd">{b}</span></div>' for a,b in [("COMPOSED","the organs work as one"),("GATED","nothing moves without you"),("YOURS","runs on your account"),("ONE TAP","you fire it, it moves")])
      + f'{foot([("5","ORGANS"),("1","BODY"),("you","ON THE GATE")])}')
    return shape(box(inner),"ribbon")

PANELS={"difference":difference(),"router":router(),"eyes":eyes(),"voice":voice(),
        "hands":hands(),"heart":heart(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    print("aibody t3:"); B.render("aibody",PANELS)
